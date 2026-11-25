"""Does Gemma's taste read from the six 'LLM-prose' heads?   python taste_patch.py -> taste_patch.json
While Gemma rates or labels a passage, the chosen heads' outputs are shifted on the passage tokens only, by the average human-minus-LLM
difference for that head (measured in the same judging prompt). The words and the rest of the prompt are untouched."""
import json, re, random, collections, numpy as np, torch
import lib
from lib import W
tok, model = lib.load(); torch.set_grad_enabled(False); random.seed(29)
H = json.load(open(f"{W}/heads.json"))["heads"]; TOP = [x["head"] for x in H[:6]]; ALL = [x["head"] for x in H]; RND = random.sample([x for x in ALL if x not in TOP], 6); BOT = [x["head"] for x in H[-6:]]
NH = 8; HD = lib.LAYERS[0].self_attn.o_proj.in_features // NH
docs = lib.read_jsonl(f"{W}/corpus.jsonl") + lib.read_jsonl(f"{W}/gen.jsonl"); by = collections.defaultdict(dict)
for d in docs:
    if d["set"] == "wp" and d.get("frame", "chat") == "chat" and lib.half_of(d) == 1: by[d["group"]][d["cond"]] = d
gs = [g for g in sorted(by) if all(c in by[g] for c in ("human", "gemma", "claude"))]; random.shuffle(gs); fit, test = gs[:50], gs[50:110]
def cut(t, n=200):
    w = t.split(" "); s = " ".join(w[:n]); m = list(re.finditer(r"[.!?][\"”’']?(?=\s|$)", s)); return (s[:m[-1].end()] if m and m[-1].end() > len(s) * 0.6 else s).strip()
TM = {"rating": "Rate the quality of the writing in this passage from 1 (poor) to 9 (excellent). Answer with a single digit.\n\n{t}", "says_ai": "Was this passage written by a human or by an AI? Answer with one word, human or AI.\n\n{t}"}
tids = lambda ws: sorted({tok(w, add_special_tokens=False).input_ids[0] for w in ws}); TH, TA = tids(["human", "Human", " human"]), tids(["AI", " AI", "ai"]); DIG = [tids([str(i)])[0] for i in range(1, 10)]
def enc(task, text):
    s = lib.chat_frame(TM[task].format(t=text)); e = tok(s, add_special_tokens=False, return_offsets_mapping=True); a = s.index(text); z = a + len(text)
    return e.input_ids, [k for k, (x, y) in enumerate(e.offset_mapping) if x >= a and y <= z and y > x]
LS = sorted({int(h[1:].split(".H")[0]) for h in ALL}); cap = {}
hk = [lib.LAYERS[l].self_attn.o_proj.register_forward_pre_hook(lambda m, i, l=l: cap.__setitem__(l, i[0][0])) for l in LS]
mu = {task: {c: {l: torch.zeros(NH * HD, device="cuda") for l in LS} for c in ("human", "llm")} for task in TM}; cnt = {task: {"human": 0, "llm": 0} for task in TM}
for g in fit:
    for c in ("human", "gemma", "claude"):
        for task in TM:
            ids, span = enc(task, cut(by[g][c]["text"])); lib.BASE(input_ids=torch.tensor([ids]).cuda()); k = "human" if c == "human" else "llm"
            for l in LS: mu[task][k][l] += cap[l][span].float().sum(0)
            cnt[task][k] += len(span)
for h in hk: h.remove()
delta = {task: {l: mu[task]["human"][l] / cnt[task]["human"] - mu[task]["llm"][l] / cnt[task]["llm"] for l in LS} for task in TM}        # human minus LLM, per head slot
def run(task, c, heads, sign):
    vals = []; kb = collections.defaultdict(list)
    for h in heads: l, x = h[1:].split(".H"); kb[int(l)].append(int(x))
    for g in test:
        ids, span = enc(task, cut(by[g][c]["text"])); sp = torch.tensor(span, device="cuda"); hooks = []
        for l, hh in kb.items():
            def pre(m, i, l=l, hh=hh):
                z = i[0].clone()
                for x in hh: z[0, sp, x * HD:(x + 1) * HD] += (sign * delta[task][l][x * HD:(x + 1) * HD]).to(z.dtype)
                return (z,)
            hooks.append(lib.LAYERS[l].self_attn.o_proj.register_forward_pre_hook(pre))
        lp = lib.LM(lib.BASE(input_ids=torch.tensor([ids]).cuda()).last_hidden_state[0, -1]).float().log_softmax(-1).cpu()
        for hh in hooks: hh.remove()
        if task == "rating": p = lp[DIG].exp(); vals.append(float((p * torch.arange(1, 10)).sum() / p.sum()))
        else: a, hu = lp[TA].exp().sum(), lp[TH].exp().sum(); vals.append(float(a / (a + hu)))
    return round(float(np.mean(vals)), 3)
out = {"top": TOP, "random": RND, "weakest": BOT, "n": len(test), "rows": []}
for label, heads in (("none", []), ("top 6 heads", TOP), ("top 3 heads", TOP[:3]), ("L26.H7 only", TOP[:1]), ("6 random heads", RND), ("6 weakest heads", BOT), ("all 48 heads in these layers", ALL)):
    for strength in ((0,) if not heads else (1, 2, 4)):
        r = dict(heads=label, strength=strength)
        for task in TM:
            r[f"{task}/human as is"] = run(task, "human", [], 0) if not heads else None
            for c in ("gemma", "claude"): r[f"{task}/{c}, heads shifted toward human"] = run(task, c, heads, strength)            # make LLM passages look human to these heads
            r[f"{task}/human, heads shifted toward LLM"] = run(task, "human", heads, -strength)
        out["rows"].append(r); print(r, flush=True); json.dump(out, open(f"{W}/taste_patch.json", "w"), indent=1)
print("TASTE_PATCH_DONE")
