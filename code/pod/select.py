"""Select transcoder features that differ between matched writers (paired by brief), found on one split half and
confirmed on the other, and features tied to token tags.   python select.py     Outputs {W}/r1/select.json + stats .npy
"""
import json, os, numpy as np, collections
W = os.environ.get("WORK", "/workspace/pi"); R = f"{W}/" + os.environ.get("R1", "r1")
docs = [json.loads(l) for l in open(f"{R}/docs.jsonl")]; N = len(docs)
ff = np.load(f"{R}/ffrac.npy", mmap_mode="r"); fm = np.load(f"{R}/fmean.npy", mmap_mode="r")
NL, F = ff.shape[1:]
ix = {(d["set"], d["group"], d["cond"]): i for i, d in enumerate(docs)}
half = {(d["set"], d["group"]): d["half"] for d in docs}
groups = collections.defaultdict(set)
for d in docs: groups[d["set"]].add(d["group"])
# contrast name -> (set, cond A, cond B): statistic is A minus B
CONTRASTS = {
 "wp_gemma_vs_human": ("wp", ["gemma"], ["human"]), "books_gemma_vs_human": ("books", ["gemma"], ["human"]),
 "wp_llm_vs_human": ("wp", ["claude", "glm"], ["human"]), "books_llm_vs_human": ("books", ["haiku", "gpt", "glm"], ["human"]),
 "wp_gemma_vs_llm": ("wp", ["gemma"], ["claude", "glm"]), "books_gemma_vs_llm": ("books", ["gemma"], ["haiku", "gpt", "glm"]),
 "lit_vs_plain": ("wp", ["gemma_lit"], ["gemma_plain"]), "lit_vs_default": ("wp", ["gemma_lit"], ["gemma"]), "plain_vs_default": ("wp", ["gemma_plain"], ["gemma"]),
 "greedy_vs_sampled": ("wp", ["gemma_greedy"], ["gemma"]), "raw_gemma_vs_human": ("wp", ["gemma_raw"], ["human_raw"]),
 "chat_vs_raw_gemma": ("wp", ["gemma"], ["gemma_raw"]), "taste_rejected_vs_approved": ("taste", ["rejected"], ["approved"]),
}
def paired(name, arr):
    s, A, B = CONTRASTS[name]; out = {}
    for h in (0, 1):
        ia, ib = [], []
        for g in sorted(groups[s]):
            if half[(s, g)] != h: continue
            a = [ix[(s, g, c)] for c in A if (s, g, c) in ix]; b = [ix[(s, g, c)] for c in B if (s, g, c) in ix]
            if a and b: ia.append(a); ib.append(b)
        n = len(ia); sm = np.zeros((NL, F)); sq = np.zeros((NL, F))
        for a, b in zip(ia, ib):
            d = np.mean([arr[i].astype(np.float32) for i in a], 0) - np.mean([arr[i].astype(np.float32) for i in b], 0)
            sm += d; sq += d * d
        mean = sm / max(n, 1); sd = np.sqrt(np.maximum(sq / max(n, 1) - mean ** 2, 1e-12))
        out[h] = (mean, mean / (sd + 1e-4), n)
    return out
sel = {}; allstats = {}
for name in CONTRASTS:
    p = paired(name, ff); n0, n1 = p[0][2], p[1][2]
    if min(n0, n1) < 8: print("skip", name, n0, n1); continue
    d0, d1 = p[0][1], p[1][1]; m = (p[0][0] * n0 + p[1][0] * n1) / (n0 + n1)
    score = np.where(np.sign(d0) == np.sign(d1), np.minimum(np.abs(d0), np.abs(d1)), 0) * np.sign(d0)
    score = np.where(np.abs(m) >= 0.002, score, 0)                     # at least 0.2 points of firing rate
    allstats[name] = np.stack([d0, d1, m]).astype(np.float16)
    flat = score.ravel(); rows = []
    for sign in (1, -1):
        for j in np.argsort(-sign * flat)[:400]:
            if sign * flat[j] <= 0.5: break
            l, f = divmod(int(j), F); rows.append(dict(key=f"L{l}.{f}", d0=round(float(d0[l, f]), 2), d1=round(float(d1[l, f]), 2), dfrac=round(float(m[l, f]), 4)))
    sel[name] = dict(n=[n0, n1], feats=rows, corr_halves=round(float(np.corrcoef(d0.ravel()[::7], d1.ravel()[::7])[0, 1]), 3))
    print(name, n0, n1, "selected", len(rows), "half corr", sel[name]["corr_halves"], "top", [(r["key"], r["d0"], r["d1"]) for r in rows[:4]], flush=True)
np.savez_compressed(f"{R}/contrast_stats.npz", **allstats)
# mean firing rate per condition (for the atlas cards)
conds = sorted({(d["set"], d["cond"]) for d in docs}); cm = {}
for s, c in conds:
    ii = [i for i, d in enumerate(docs) if d["set"] == s and d["cond"] == c]
    acc = np.zeros((NL, F), np.float32)
    for i in ii: acc += ff[i]
    cm[f"{s}/{c}"] = (acc / len(ii)).astype(np.float16)
np.savez_compressed(f"{R}/cond_frac.npz", **cm)
# ---- token tags: firing rate on tagged tokens vs all tokens, for human (0), gemma (1), other LLM (2), other (3) x half
tags = json.load(open(f"{R}/tags.json")); K = len(tags)
tc = np.load(f"{R}/tagcnt.npy", mmap_mode="r"); tn = np.load(f"{R}/tagn.npy").reshape(8, K)
tagsel = {}
base = [np.stack([tc[l][:, (c * 2 + h) * K] for l in range(NL)]) for h in (0, 1) for c in range(4)]      # [h*4+c][NL,F] counts on all tokens
for k, t in enumerate(tags):
    if t == "all": continue
    n_h = [sum(tn[c * 2 + h, k] for c in range(4)) for h in (0, 1)]
    if min(n_h) < 150: print("tag", t, "too rare", n_h); continue
    lift = []
    for h in (0, 1):
        cnt = sum(np.stack([tc[l][:, (c * 2 + h) * K + k] for l in range(NL)]) for c in range(4)); allc = sum(base[h * 4 + c] for c in range(4))
        n_all = sum(tn[c * 2 + h, 0] for c in range(4)); p1 = cnt / n_h[h]; p0 = (allc - cnt) / max(1, n_all - n_h[h])
        lift.append((p1, p0))
    (a1, a0), (b1, b0) = lift
    # score: firing-rate difference, confirmed on both halves; prefer features specific to the tag
    s = np.minimum(a1 - a0, b1 - b0) * np.minimum(a1 / (a1 + a0 + 1e-3), b1 / (b1 + b0 + 1e-3))
    rows = []
    for j in np.argsort(-s.ravel())[:40]:
        l, f = divmod(int(j), F)
        if s[l, f] < 0.03: break
        rows.append(dict(key=f"L{l}.{f}", on=round(float((a1[l, f] + b1[l, f]) / 2), 3), off=round(float((a0[l, f] + b0[l, f]) / 2), 4)))
    tagsel[t] = dict(n=[int(x) for x in n_h], per_class=[int(tn[c * 2, k] + tn[c * 2 + 1, k]) for c in range(4)], feats=rows)
    print("tag", t, n_h, len(rows), [(r["key"], r["on"], r["off"]) for r in rows[:3]], flush=True)
json.dump(dict(contrasts=sel, tags=tagsel, tag_tokens_per_class=[int(tn[c * 2, 0] + tn[c * 2 + 1, 0]) for c in range(4)]), open(f"{R}/select.json", "w"))
print("SELECT_DONE")
