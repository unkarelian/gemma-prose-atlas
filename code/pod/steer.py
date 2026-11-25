"""Round 2: generation under interventions.   python steer.py plan.json out.jsonl   |   python steer.py check
plan.json: {"prompts": [{"group", "prompt"}], "max_new": 400,
            "conds": [{"name", "add": [[layer, key, alpha]], "ablate": ["L12.345"], "scale": 0.0}]}
 add:    residual stream += alpha * dirs[key][layer] after that layer, at every position (dirs.pt: key -> [NL, D] raw mean differences)
 ablate: transcoder features whose write to the MLP output is multiplied by `scale` (0 removes it)
check: where do the transcoders write? Prints the unexplained variance against the raw MLP output and the post-norm output.
"""
import sys, json, os, time, collections, torch
import lib
from lib import W
from transformers.generation.streamers import BaseStreamer
tok, model = lib.load(); tok.padding_side = "left"

if sys.argv[1] == "check":
    lib.load_tc([5, 12, 20, 28], dec=True); cap = {}
    hs = []
    for l in (5, 12, 20, 28):
        hs.append(lib.LAYERS[l].pre_feedforward_layernorm.register_forward_hook(lambda m, i, o, l=l: cap.__setitem__(("in", l), o[0])))
        hs.append(lib.LAYERS[l].mlp.register_forward_hook(lambda m, i, o, l=l: cap.__setitem__(("mlp", l), o[0])))
        hs.append(lib.LAYERS[l].post_feedforward_layernorm.register_forward_hook(lambda m, i, o, l=l: cap.__setitem__(("post", l), o[0])))
    d = lib.read_jsonl(f"{W}/gen.jsonl")[3]; ids = tok(lib.chat_frame(d["prompt"]) + d["text"][:1500], add_special_tokens=False, return_tensors="pt").input_ids.cuda()
    with torch.no_grad(): model(input_ids=ids)
    for l in (5, 12, 20, 28):
        a = lib.tc_acts(l, cap[("in", l)][5:]); y = a @ lib.TC[l]["w_dec"].cuda() + lib.TC[l]["b_dec"].cuda()
        for k in ("mlp", "post"):
            t = cap[(k, l)][5:].float(); print(l, k, "FVU", round(float(((t - y) ** 2).sum() / ((t - t.mean(0)) ** 2).sum()), 3), "L0", round(float((a > 0).sum(1).float().mean()), 1), flush=True)
    sys.exit()

plan = json.load(open(sys.argv[1])); out_path = sys.argv[2]
import numpy as np
dirs = {k: torch.tensor(v) for k, v in np.load(f"{W}/dirs.npz").items()} if os.path.exists(f"{W}/dirs.npz") else {}
done = {json.loads(l)["id"] for l in open(out_path)} if os.path.exists(out_path) else set()
OUTPOINT = os.environ.get("OUTPOINT", "post")
class Live(BaseStreamer):
    def __init__(self, metas, prog): self.meta = metas[:4]; self.toks = [[] for _ in self.meta]; self.n = -1; self.prog = prog
    def put(self, v):
        self.n += 1
        if self.n == 0: return
        for k in range(len(self.toks)): self.toks[k].append(int(v[k]))
        if self.n % 6 == 0: self.dump()
    def dump(self, done=False):
        items = [dict(m, text=tok.decode(t, skip_special_tokens=True)) for m, t in zip(self.meta, self.toks)]
        json.dump(dict(stage="steering", progress=self.prog, done=done, items=items), open(f"{W}/live.tmp", "w")); os.replace(f"{W}/live.tmp", f"{W}/live.json")
    def end(self): self.dump(True)
need = sorted({int(k[1:].split(".")[0]) for c in plan["conds"] for k in c.get("ablate", [])})
if need: lib.load_tc(need, dec=True)
t0 = time.time()
for ci, c in enumerate(plan["conds"]):
    jobs = [p for p in plan["prompts"] if f"{c['name']}/{p['group']}" not in done]
    if not jobs: continue
    hooks = []
    for layer, key, alpha in c.get("add", []):
        v = (float(alpha) * dirs[key][layer].float()).to("cuda", torch.bfloat16)
        def add(m, i, o, v=v):
            h = o[0] if isinstance(o, tuple) else o
            return ((h + v,) + tuple(o[1:])) if isinstance(o, tuple) else h + v
        hooks.append(lib.LAYERS[layer].register_forward_hook(add))
    ab = collections.defaultdict(list)
    for k in c.get("ablate", []): l, f = k[1:].split("."); ab[int(l)].append(int(f))
    for l, fs in ab.items():
        t = lib.TC[l]; w, b, thr, dec = t["w_enc"][:, fs], t["b_enc"][fs], t["threshold"][fs], t["w_dec"][fs].to("cuda"); st = {}
        hooks.append(lib.LAYERS[l].pre_feedforward_layernorm.register_forward_hook(lambda m, i, o, st=st: st.__setitem__("x", o)))
        def edit(m, i, o, st=st, w=w, b=b, thr=thr, dec=dec, s=float(c.get("scale", 0.0))):
            a = (st["x"].to(torch.bfloat16) @ w).float() + b; a = a * (a > thr)
            return o + ((s - 1.0) * (a @ dec)).to(o.dtype)
        mod = lib.LAYERS[l].post_feedforward_layernorm if OUTPOINT == "post" else lib.LAYERS[l].mlp
        hooks.append(mod.register_forward_hook(edit))
    BS = int(os.environ.get("BS", 64))
    for s in range(0, len(jobs), BS):
        b = jobs[s:s + BS]; enc = [tok(lib.chat_frame(p["prompt"]), add_special_tokens=False).input_ids for p in b]; L = max(map(len, enc))
        ids = torch.full((len(b), L), tok.pad_token_id, dtype=torch.long); att = torch.zeros((len(b), L), dtype=torch.long)
        for k, e in enumerate(enc): ids[k, L - len(e):] = torch.tensor(e); att[k, L - len(e):] = 1
        metas = [dict(id=f"{c['name']}/{p['group']}", mode=c.get("label", c["name"]), brief=p.get("brief", p["prompt"])[:300]) for p in b]
        with torch.no_grad():
            o = model.generate(input_ids=ids.cuda(), attention_mask=att.cuda(), max_new_tokens=plan.get("max_new", 400), do_sample=not c.get("greedy", False),
                               **({} if c.get("greedy") else dict(temperature=1.0, top_k=64, top_p=0.95)), streamer=Live(metas, f"{ci + 1}/{len(plan['conds'])}"))
        with open(out_path, "a") as f:
            for k, p in enumerate(b):
                f.write(json.dumps(dict(id=f"{c['name']}/{p['group']}", set="steer", group=p["group"], cond=c["name"], frame="chat", prompt=p["prompt"],
                                        text=tok.decode(o[k, L:], skip_special_tokens=True).strip()), ensure_ascii=False) + "\n")
    for h in hooks: h.remove()
    print(f"{ci + 1}/{len(plan['conds'])} {c['name']} {time.time() - t0:.0f}s", flush=True)
print("ROUND2_DONE")
