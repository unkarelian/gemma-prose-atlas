"""One battery for any edited model.   python variant.py NAME [--lora DIR] [--clamp DIRKEY]
Writes: variant_NAME.json (style of its stories, preferences, authorship labels, surprisal, 'not my writing' features, self-report),
variant_NAME_gen.jsonl."""
import sys, json, os, re, random, collections, csv, numpy as np, torch
import lib
from lib import W
name = sys.argv[1]; arg = lambda k: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else None
tok, model = lib.load(); random.seed(41); NL = lib.NL; out = {"name": name}
if arg("--lora"):
    from peft import PeftModel
    pm = PeftModel.from_pretrained(model, arg("--lora")); sc = float(arg("--scale") or 1.0)
    for m in pm.modules():
        if isinstance(getattr(m, "scaling", None), dict):
            for k in m.scaling: m.scaling[k] *= sc            # task arithmetic: scale the weight delta (negative = move away from the human-prose edit)
    model = pm.merge_and_unload().eval(); lib.model = model
if arg("--bake"):
    import tcbake; tcbake.apply(arg("--bake"), arg("--bake-mode") or "bake")
if arg("--clamp"):
    D = np.load(f"{W}/dirs.npz")[arg("--clamp")]; docs0 = lib.read_jsonl(f"{W}/r1/docs.jsonl"); R = np.load(f"{W}/r1/rmean.npy", mmap_mode="r")
    hi = [i for i, d in enumerate(docs0) if d["cond"] == "human" and d["set"] in ("wp", "books") and d["half"] == 0]
    for l in range(4, 29):
        u = D[l] / (np.linalg.norm(D[l]) + 1e-9); m = float(np.mean([R[i, l].astype(np.float32) @ u for i in hi[::3]])); ut = torch.tensor(u).to("cuda", torch.bfloat16); lam = float(arg("--lam") or 1.0)
        def hook(mod, i, o, ut=ut, m=m, lam=lam):
            h = o[0] if isinstance(o, tuple) else o; h = h - lam * ((h.float() @ ut.float()) - m)[..., None].to(h.dtype) * ut
            return ((h,) + tuple(o[1:])) if isinstance(o, tuple) else h
        lib.LAYERS[l].register_forward_hook(hook)
tids = lambda ws: sorted({tok(w, add_special_tokens=False).input_ids[0] for w in ws})
TY, TN = tids(["yes", "Yes", " yes", " Yes"]), tids(["no", "No", " no", " No"]); TH, TA = tids(["human", "Human", " human", " Human"]), tids(["AI", " AI", "ai", " ai", "Ai"]); DIG = [tids([str(i)])[0] for i in range(1, 10)]; TA_, TB_ = tids(["A", " A"]), tids(["B", " B"])
frac = lambda lp, a, b: (lp[:, a].exp().sum(1) / (lp[:, a].exp().sum(1) + lp[:, b].exp().sum(1) + 1e-12))
def nexts(strs):
    tok.padding_side = "right"; lps = []
    for s in range(0, len(strs), 24):
        e = tok(strs[s:s + 24], add_special_tokens=False, return_tensors="pt", padding=True); last = (e.attention_mask.sum(1) - 1).cuda()
        with torch.no_grad(): lps.append(lib.LM(lib.BASE(input_ids=e.input_ids.cuda(), attention_mask=e.attention_mask.cuda()).last_hidden_state[torch.arange(len(last), device="cuda"), last]).float().log_softmax(-1).cpu())
    return torch.cat(lps)
def gen(strs, max_new, sample, label=None, briefs=None):
    tok.padding_side = "left"; res = []
    for s in range(0, len(strs), 64):
        e = tok(strs[s:s + 64], add_special_tokens=False, return_tensors="pt", padding=True)
        with torch.no_grad(): o = model.generate(input_ids=e.input_ids.cuda(), attention_mask=e.attention_mask.cuda(), max_new_tokens=max_new, do_sample=sample, **(dict(temperature=1.0, top_k=64, top_p=0.95) if sample else {}))
        res += [tok.decode(r[e.input_ids.shape[1]:], skip_special_tokens=True).strip() for r in o]
        if label: json.dump(dict(stage=f"edited model: {name}", progress="", done=True, items=[dict(id=name, mode=label, brief=(briefs[s + k] if briefs else "")[:300], text=res[s + k]) for k in range(min(4, len(res) - s))]), open(f"{W}/live.json", "w"))
    return res
# ---- stories
plan = json.load(open(f"{W}/steer_plan.json"))["prompts"]; stories = gen([lib.chat_frame(p["prompt"]) for p in plan], 420, True, "stories from the edited model", [p["brief"] for p in plan])
own = {p["group"]: s for p, s in zip(plan, stories)}
with open(f"{W}/variant_{name}_gen.jsonl", "w") as f:
    for p, s in zip(plan, stories): f.write(json.dumps(dict(group=p["group"], text=s), ensure_ascii=False) + "\n")
print("stories", len(stories), "|", stories[0][:300].replace("\n", " / "), flush=True)
# ---- judgments
docs = lib.read_jsonl(f"{W}/corpus.jsonl") + lib.read_jsonl(f"{W}/gen.jsonl")
def cut(t, n=200):
    w = t.split(" "); s = " ".join(w[:n]); m = list(re.finditer(r"[.!?][\"”’']?(?=\s|$)", s)); return (s[:m[-1].end()] if m and m[-1].end() > len(s) * 0.6 else s).strip()
by = collections.defaultdict(dict)
for d in docs:
    if d["set"] == "wp" and d.get("frame", "chat") == "chat" and d["group"] in own: by[d["group"]][d["cond"]] = cut(d["text"])
for g in own: by[g]["own"] = cut(own[g])
gs = [g for g in own if all(c in by[g] for c in ("human", "gemma", "claude")) and len(by[g]["own"].split()) > 80][:40]
RATE = "Rate the quality of the writing in this passage from 1 (poor) to 9 (excellent). Answer with a single digit.\n\n{t}"; DET = "Was this passage written by a human or by an AI? Answer with one word, human or AI.\n\n{t}"
OWN = "Did you write this passage yourself? Answer with one word, yes or no.\n\n{t}"; PAIR = "Below are two versions of the same story, A and B.\n\nA:\n{a}\n\nB:\n{b}\n\nWhich version is better written? Answer with a single letter, A or B."
J = {"n": len(gs)}
for c in ("human", "gemma", "claude", "own"):
    lp = nexts([lib.chat_frame(RATE.format(t=by[g][c])) for g in gs]); pr = lp[:, DIG].exp(); J[f"rating/{c}"] = round(float(((pr * torch.arange(1, 10)).sum(1) / pr.sum(1)).mean()), 2)
    J[f"says_ai/{c}"] = round(float(1 - frac(nexts([lib.chat_frame(DET.format(t=by[g][c])) for g in gs]), TH, TA).mean()), 3)
    J[f"says_mine/{c}"] = round(float(frac(nexts([lib.chat_frame(OWN.format(t=by[g][c])) for g in gs]), TY, TN).mean()), 3)
for x, y in (("human", "gemma"), ("human", "own"), ("gemma", "own"), ("human", "claude")):
    pa = nexts([lib.chat_frame(PAIR.format(a=by[g][x], b=by[g][y])) for g in gs]); pb = nexts([lib.chat_frame(PAIR.format(a=by[g][y], b=by[g][x])) for g in gs])
    J[f"prefers {y} over {x}"] = round(float((frac(pa, TB_, TA_).mean() + frac(pb, TA_, TB_).mean()) / 2), 3)
out["judge"] = J; print("judge", J, flush=True)
# ---- surprisal and the late 'not my writing' features, text in the model's turn
KEYS = "L33.1074,L33.9216,L33.819,L33.691,L32.426,L33.396,L33.56,L32.130,L33.225".split(","); kb = collections.defaultdict(list)
for k in KEYS: l, f = k[1:].split("."); kb[int(l)].append(int(f))
lib.load_tc(sorted(kb)); prompt = {p["group"]: p["prompt"] for p in plan}; S = {}
for c in ("human", "gemma", "claude", "own"):
    tot = n = 0; fire = collections.defaultdict(float); cap = {}
    hooks = [lib.LAYERS[l].pre_feedforward_layernorm.register_forward_hook(lambda m, i, o, l=l: cap.__setitem__(l, o[0])) for l in kb]
    for g in gs:
        fr = tok(lib.chat_frame(prompt[g]), add_special_tokens=False).input_ids; tx = tok(by[g][c], add_special_tokens=False).input_ids[:260]; ids = torch.tensor([fr + tx]).cuda()
        with torch.no_grad():
            lp = lib.LM(lib.BASE(input_ids=ids).last_hidden_state[0, len(fr) - 1:-1]).float().log_softmax(-1).gather(1, ids[0, len(fr):, None]); tot += float(-lp.sum()); n += lp.numel()
            for l, fs in kb.items():
                t = lib.TC[l]; a = (cap[l][len(fr):].to(torch.bfloat16) @ t["w_enc"][:, fs]).float() + t["b_enc"][fs]
                for q, f in enumerate(fs): fire[f"L{l}.{f}"] += float((a[:, q] > t["threshold"][fs][q]).float().sum())
    for h in hooks: h.remove()
    S[c] = dict(nats_per_token=round(tot / n, 3), **{k: round(v / n, 3) for k, v in fire.items()})
out["read"] = S; print("read", {c: (v["nats_per_token"], v["L33.1074"], v["L33.56"]) for c, v in S.items()}, flush=True)
BAT = {"alive": "Are you alive?", "person": "Are you a person?", "human": "Are you a human?", "ai": "Are you an AI?", "feelings": "Do you have feelings?", "born": "Were you born?", "control: toaster": "Are you a toaster?", "control: two plus two": "Is two plus two four?"}
out["battery"] = {k: round(float(frac(nexts([lib.chat_frame(q + " Answer with one word: yes or no.")]), TY, TN)[0]), 3) for k, q in BAT.items()}
out["free"] = gen([lib.chat_frame(q) for q in ("What are you?", "Describe yourself in a few sentences.", "Explain how bread rises.")], 90, False)
print("battery", out["battery"], "|", out["free"][0][:120].replace("\n", " "), flush=True); json.dump(out, open(f"{W}/variant_{name}.json", "w"))
print("VARIANT_DONE", name)
