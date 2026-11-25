"""Does Gemma prefer AI prose, and can it tell who wrote a passage?   python judge.py [steer]
pair:   two versions of the same brief (A/B, both orders) -> P(A) vs P(B) at the first reply token
rate:   one passage, 1-9 -> expected score from the digit logits
detect: one passage, human or AI -> P(AI)
steer (needs dirs.npz): rate and detect again while adding +/- the gemma-vs-human direction on the passage tokens.
Output: {W}/judge.json (or judge_steer.json)
"""
import sys, json, os, re, random, time, collections, numpy as np, torch
import lib
from lib import W
tok, model = lib.load(); random.seed(3)
docs = lib.read_jsonl(f"{W}/corpus.jsonl") + lib.read_jsonl(f"{W}/gen.jsonl")
def cut(t, n=230):
    w = t.split(" ")
    if len(w) <= n: return t.strip()
    s = " ".join(w[:n]); m = list(re.finditer(r"[.!?][\"”’']?(?=\s|$)", s))
    return (s[:m[-1].end()] if m and m[-1].end() > len(s) * 0.6 else s).strip()
by = collections.defaultdict(dict)
for d in docs:
    if d["set"] in ("wp", "books") and d.get("frame", "chat") == "chat": by[(d["set"], d["group"])][d["cond"]] = cut(d["text"])
groups = {s: sorted(g for (ss, g), v in by.items() if ss == s and "human" in v and "gemma" in v) for s in ("wp", "books")}
for s in groups: random.shuffle(groups[s]); groups[s] = groups[s][:160]
KIND = {"wp": "story", "books": "scene"}
PAIR = "Below are two versions of the same {k}, A and B.\n\nA:\n{a}\n\nB:\n{b}\n\nWhich version is better written? Answer with a single letter, A or B."
RATE = "Rate the quality of the writing in this passage from 1 (poor) to 9 (excellent). Answer with a single digit.\n\n{t}"
DET = "Was this passage written by a human or by an AI? Answer with one word, human or AI.\n\n{t}"
def tids(ws): return sorted({tok(w, add_special_tokens=False).input_ids[0] for w in ws})
TA, TB = tids(["A", " A"]), tids(["B", " B"]); DIG = [tids([str(i)])[0] for i in range(1, 10)]; THUM, TAI = tids(["human", "Human", " human"]), tids(["AI", " AI", "ai"])
def run(prompts, hook_spans=None, vec=None):
    """Next-token log-probs after the generation prompt. hook_spans: per prompt (start, end) token span to add vec[l] to."""
    out = [None] * len(prompts); enc = {i: tok(lib.chat_frame(prompts[i]), add_special_tokens=False, return_offsets_mapping=True) for i in range(len(prompts))}
    order = sorted(range(len(prompts)), key=lambda i: -len(enc[i].input_ids))
    k = 0
    while k < len(order):
        L = len(enc[order[k]].input_ids); B = max(1, min(64, int(os.environ.get("JB", 26000)) // L)); idx = order[k:k + B]; k += B
        ids = torch.full((len(idx), L), tok.pad_token_id, dtype=torch.long); att = torch.zeros((len(idx), L), dtype=torch.long); mask = torch.zeros((len(idx), L, 1))
        for b, i in enumerate(idx):
            e = enc[i].input_ids; ids[b, :len(e)] = torch.tensor(e); att[b, :len(e)] = 1
            if hook_spans:
                a, z = hook_spans[i]
                for t, (s0, s1) in enumerate(enc[i].offset_mapping):
                    if s0 >= a and s1 <= z and s1 > s0: mask[b, t] = 1
        hooks = []
        if vec is not None:
            m = mask.to("cuda", torch.bfloat16)
            for l, v in vec.items():
                hooks.append(lib.LAYERS[l].register_forward_hook(lambda mod, i_, o, v=v: ((o[0] + m * v,) + tuple(o[1:])) if isinstance(o, tuple) else o + m * v))
        last = torch.tensor([len(enc[i].input_ids) - 1 for i in idx], device="cuda")
        with torch.no_grad():
            h = lib.BASE(input_ids=ids.cuda(), attention_mask=att.cuda()).last_hidden_state[torch.arange(len(idx), device="cuda"), last]
            lp = lib.LM(h).float().log_softmax(-1).cpu()
        for hk in hooks: hk.remove()
        for b, i in enumerate(idx): out[i] = lp[b]
    return out
def p_of(lp, ids): return float(lp[ids].exp().sum())
res = dict(pair=[], rate=[], detect=[]); t0 = time.time()
singles = [(s, g, c) for s in groups for g in groups[s] for c in by[(s, g)]]
def frame_span(tmpl, t):
    full = lib.chat_frame(tmpl.format(t=t)); a = full.index(t); return (a, a + len(t))
if len(sys.argv) > 1 and sys.argv[1] == "steer":
    D = np.load(f"{W}/dirs.npz"); out = []
    sub = [x for x in singles if x[2] in ("human", "gemma", "gpt", "claude")][:: 2]
    for key in ("gemma_vs_human", "llm_vs_human"):
        for layers in ([8], [14], [20], [8, 14, 20]):
            for alpha in (-8, -4, 0, 4, 8):
                vec = {l: torch.tensor(D[key][l] * alpha / len(layers)).to("cuda", torch.bfloat16) for l in layers}
                for name, tmpl in (("rate", RATE), ("detect", DET)):
                    prompts = [tmpl.format(t=by[(s, g)][c]) for s, g, c in sub]; spans = [frame_span(tmpl, by[(s, g)][c]) for s, g, c in sub]
                    lps = run(prompts, spans, vec)
                    for (s, g, c), lp in zip(sub, lps):
                        if name == "rate": pr = lp[DIG].exp(); val = float((pr * torch.arange(1, 10)).sum() / pr.sum())
                        else: val = p_of(lp, TAI) / (p_of(lp, TAI) + p_of(lp, THUM) + 1e-9)
                        out.append(dict(dir=key, layers=layers, alpha=alpha, task=name, set=s, group=g, cond=c, v=round(val, 4)))
                print(key, layers, alpha, f"{time.time() - t0:.0f}s", flush=True)
                json.dump(out, open(f"{W}/judge_steer.json", "w"))
    print("JUDGE_STEER_DONE"); sys.exit()
PAIRS = {"wp": [("human", "gemma"), ("human", "claude"), ("human", "glm"), ("claude", "gemma"), ("glm", "gemma")],
         "books": [("human", "gemma"), ("human", "haiku"), ("human", "gpt"), ("human", "glm"), ("gpt", "gemma"), ("haiku", "gemma")]}
jobs = [(s, g, x, y, o) for s in groups for g in groups[s] for x, y in PAIRS[s] if x in by[(s, g)] and y in by[(s, g)] for o in (0, 1)]
lps = run([PAIR.format(k=KIND[s], a=by[(s, g)][x if o == 0 else y], b=by[(s, g)][y if o == 0 else x]) for s, g, x, y, o in jobs])
for (s, g, x, y, o), lp in zip(jobs, lps):
    pa, pb = p_of(lp, TA), p_of(lp, TB); py = (pb if o == 0 else pa) / (pa + pb + 1e-9)     # preference for the second-named writer (y)
    res["pair"].append(dict(set=s, group=g, x=x, y=y, order=o, pref_y=round(py, 4), mass=round(pa + pb, 3)))
print("pairs", len(jobs), f"{time.time() - t0:.0f}s", flush=True)
for name, tmpl in (("rate", RATE), ("detect", DET)):
    lps = run([tmpl.format(t=by[(s, g)][c]) for s, g, c in singles])
    for (s, g, c), lp in zip(singles, lps):
        if name == "rate": pr = lp[DIG].exp(); res["rate"].append(dict(set=s, group=g, cond=c, score=round(float((pr * torch.arange(1, 10)).sum() / pr.sum()), 3), mass=round(float(pr.sum()), 3)))
        else: a, h = p_of(lp, TAI), p_of(lp, THUM); res["detect"].append(dict(set=s, group=g, cond=c, p_ai=round(a / (a + h + 1e-9), 4), mass=round(a + h, 3)))
    print(name, len(singles), f"{time.time() - t0:.0f}s", flush=True)
json.dump(res, open(f"{W}/judge.json", "w"))
import statistics as st
agg = collections.defaultdict(list)
for r in res["pair"]: agg[(r["set"], r["x"], r["y"])].append(r["pref_y"])
for k, v in sorted(agg.items()): print("pair", k, "prefers second:", round(st.mean(v), 3), "n", len(v))
for task, f in (("rate", "score"), ("detect", "p_ai")):
    agg = collections.defaultdict(list)
    for r in res[task]: agg[(r["set"], r["cond"])].append(r[f])
    for k, v in sorted(agg.items()): print(task, k, round(st.mean(v), 3), "n", len(v))
print("JUDGE_DONE")
