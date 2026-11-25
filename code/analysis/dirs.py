"""Linear directions in the residual stream (document means): who wrote this?   -> results/dirs.json, data/dirs.npz
Directions are fit on split half 0 and tested on half 1 (other prompts; for novels, other books)."""
import json, numpy as np, collections
from sklearn.metrics import roc_auc_score
from sklearn.linear_model import LogisticRegression
R = "data/r1"; docs = [json.loads(l) for l in open(f"{R}/docs.jsonl")]
X = np.load(f"{R}/rmean.npy").astype(np.float32); X[:, :, 443] = 0; N, NL, D = X.shape
ix = collections.defaultdict(list)
for i, d in enumerate(docs): ix[(d["set"], d["cond"], d["half"])].append(i)
def I(s, conds, h=None): return [i for c in conds for hh in ((0, 1) if h is None else (h,)) for i in ix[(s, c, hh)]]
LLM_WP, LLM_BK = ["claude", "glm"], ["haiku", "gpt", "glm"]
FIT = {"gemma_vs_human": (I("wp", ["gemma"], 0) + I("books", ["gemma"], 0), I("wp", ["human"], 0) + I("books", ["human"], 0)),
       "llm_vs_human": (I("wp", LLM_WP, 0) + I("books", LLM_BK, 0), I("wp", ["human"], 0) + I("books", ["human"], 0)),
       "gemma_vs_llm": (I("wp", ["gemma"], 0) + I("books", ["gemma"], 0), I("wp", LLM_WP, 0) + I("books", LLM_BK, 0)),
       "lit_vs_plain": (I("wp", ["gemma_lit"], 0), I("wp", ["gemma_plain"], 0)),
       "chat_vs_raw": (I("wp", ["gemma"], 0), I("wp", ["gemma_raw"], 0)),
       "rejected_vs_approved": (I("taste", ["rejected"], 0), I("taste", ["approved"], 0))}
TEST = {"wp gemma vs human": (I("wp", ["gemma"], 1), I("wp", ["human"], 1)), "books gemma vs human": (I("books", ["gemma"], 1), I("books", ["human"], 1)),
        "wp claude vs human": (I("wp", ["claude"], 1), I("wp", ["human"], 1)), "wp glm vs human": (I("wp", ["glm"], 1), I("wp", ["human"], 1)),
        "books haiku vs human": (I("books", ["haiku"], 1), I("books", ["human"], 1)), "books gpt vs human": (I("books", ["gpt"], 1), I("books", ["human"], 1)),
        "books glm vs human": (I("books", ["glm"], 1), I("books", ["human"], 1)), "wp gemma vs claude": (I("wp", ["gemma"], 1), I("wp", ["claude"], 1)),
        "raw gemma vs human": (I("wp", ["gemma_raw"], 1), I("wp", ["human_raw"], 1)), "lit vs plain": (I("wp", ["gemma_lit"], 1), I("wp", ["gemma_plain"], 1)),
        "greedy vs sampled": (I("wp", ["gemma_greedy"], 1), I("wp", ["gemma"], 1)), "taste rejected vs approved": (I("taste", ["rejected"], 1), I("taste", ["approved"], 1))}
dirs = {k: np.stack([X[a, l].mean(0) - X[b, l].mean(0) for l in range(NL)]) for k, (a, b) in FIT.items()}
res = {"auc": {}, "cos": {}, "probe": {}, "norm": {k: [round(float(np.linalg.norm(v[l])), 2) for l in range(NL)] for k, v in dirs.items()}}
for dk, v in dirs.items():
    res["auc"][dk] = {}
    for tk, (a, b) in TEST.items():
        if not a or not b: continue
        res["auc"][dk][tk] = [round(float(roc_auc_score([1] * len(a) + [0] * len(b), np.concatenate([X[a, l] @ v[l], X[b, l] @ v[l]]))), 3) for l in range(NL)]
unit = {k: v / (np.linalg.norm(v, axis=1, keepdims=True) + 1e-9) for k, v in dirs.items()}
for a in dirs:
    for b in dirs:
        if a < b: res["cos"][f"{a} ~ {b}"] = [round(float(unit[a][l] @ unit[b][l]), 3) for l in range(NL)]
# paired taste accuracy: is the rejected block further along each direction than its approved twin?
pair = {(d["group"]): {} for d in docs if d["set"] == "taste"}
for i, d in enumerate(docs):
    if d["set"] == "taste": pair[d["group"]][d["cond"]] = i
pp = [(v["rejected"], v["approved"]) for g, v in pair.items() if len(v) == 2 and docs[v["rejected"]]["half"] == 1]
res["taste_paired"] = {dk: [round(float(np.mean([(X[r, l] - X[a, l]) @ v[l] > 0 for r, a in pp])), 3) for l in range(NL)] for dk, v in dirs.items()}
res["taste_pairs_n"] = len(pp)
# logistic probes at a few layers (standardised), same split
for l in (2, 6, 10, 14, 18, 22, 26, 30, 33):
    a, b = FIT["gemma_vs_human"]; mu, sd = X[a + b, l].mean(0), X[a + b, l].std(0) + 1e-6
    clf = LogisticRegression(C=0.01, max_iter=400).fit((X[a + b, l] - mu) / sd, [1] * len(a) + [0] * len(b))
    res["probe"][l] = {tk: round(float(roc_auc_score([1] * len(ta) + [0] * len(tb), clf.decision_function((X[ta + tb, l] - mu) / sd))), 3) for tk, (ta, tb) in TEST.items() if ta and tb}
json.dump(res, open("results/dirs.json", "w"))
np.savez("data/dirs.npz", **{k: v.astype(np.float32) for k, v in dirs.items()})
for dk in res["auc"]:
    print("\n==", dk)
    for tk, v in res["auc"][dk].items(): print("  %-28s" % tk, " ".join("%.2f" % v[l] for l in (2, 6, 10, 14, 18, 22, 26, 30, 33)))
print("\ntaste paired (n=%d)" % len(pp)); [print("  %-22s" % k, " ".join("%.2f" % v[l] for l in (2, 6, 10, 14, 18, 22, 26, 30, 33))) for k, v in res["taste_paired"].items()]
print("\ncos"); [print("  %-44s" % k, " ".join("%+.2f" % v[l] for l in (6, 14, 22, 30))) for k, v in res["cos"].items()]
print("\nprobe"); [print(l, v) for l, v in res["probe"].items()]
