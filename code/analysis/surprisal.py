"""How predictable is each writer to Gemma, and where?   -> results/surprisal.json
Every text is read in the frame it was (or would have been) written in; numbers are per token of the text."""
import json, sys, numpy as np, collections
sys.path.insert(0, "pod"); import tags
from tokenizers import Tokenizer
tk = Tokenizer.from_file("data/tok/tokenizer.json")
R = "data/r1"; docs = [json.loads(l) for l in open(f"{R}/docs.jsonl")]; texts = {}
for l in open(f"{R}/texts.jsonl"): d = json.loads(l); texts[d["id"]] = d["text"]
T = np.load(f"{R}/tokens.npz"); off = T["off"]; lp = T["lp"].astype(np.float32); ent = T["ent"].astype(np.float32); rank = T["rank"]; t5p = T["t5p"].astype(np.float32); ids = T["ids"]
res = {"by_cond": {}, "by_tag": {}, "position": {}, "greedy_agree": {}}
acc = collections.defaultdict(lambda: collections.defaultdict(list)); tagacc = collections.defaultdict(lambda: collections.defaultdict(lambda: [0.0, 0.0, 0.0, 0]))
pos = collections.defaultdict(lambda: np.zeros((2, 640)))
CLS = {"human": "human", "gemma": "gemma", "claude": "llm", "glm": "llm", "haiku": "llm", "gpt": "llm"}
for i, d in enumerate(docs):
    s = slice(off[i], off[i + 1]); n = off[i + 1] - off[i]; key = f"{d['set']}/{d['cond']}"
    a = acc[key]; a["nll"].append(-lp[s].mean()); a["ent"].append(ent[s].mean()); a["top1"].append((rank[s] == 0).mean()); a["top5"].append((rank[s] < 5).mean())
    a["p1"].append(np.exp(t5p[s, 0]).mean()); a["rank_med"].append(np.median(rank[s])); a["tail"].append((rank[s] >= 50).mean())
    pos[key][0, :n] += -lp[s]; pos[key][1, :n] += 1
    cls = CLS.get(d["cond"])
    if cls and d["set"] in ("wp", "books"):
        e = tk.encode(texts[d["id"]], add_special_tokens=False); offs = e.offsets[:n]
        if len(offs) != n: continue
        tg = tags.to_tokens(tags.spans(texts[d["id"]][: offs[-1][1]]), offs)
        for k, tl in tg.items():
            if not tl: continue
            tl = np.array(tl) + off[i]; z = tagacc[cls][tags.TAGS[k]]; z[0] += float(-lp[tl].sum()); z[1] += float(ent[tl].sum()); z[2] += float((rank[tl] == 0).sum()); z[3] += len(tl)
for k, a in acc.items(): res["by_cond"][k] = dict(n=len(a["nll"]), **{m: round(float(np.mean(v)), 4) for m, v in a.items()})
for cls, tg in tagacc.items(): res["by_tag"][cls] = {t: dict(n=z[3], nll=round(z[0] / z[3], 3), ent=round(z[1] / z[3], 3), top1=round(z[2] / z[3], 3)) for t, z in tg.items() if z[3] >= 30}
for k, p in pos.items(): res["position"][k] = [round(float(x), 3) for x in (p[0] / np.maximum(p[1], 1)).reshape(64, 10).mean(1)]
json.dump(res, open("results/surprisal.json", "w"))
print("%-22s %5s %6s %6s %6s %6s %6s %6s" % ("cond", "n", "nll", "ent", "top1", "top5", "p1", "tail50"))
for k, v in sorted(res["by_cond"].items()): print("%-22s %5d %6.2f %6.2f %6.2f %6.2f %6.2f %6.3f" % (k, v["n"], v["nll"], v["ent"], v["top1"], v["top5"], v["p1"], v["tail"]))
print("\nper tag: nll / entropy / top1 for human | gemma | llm text")
for t in tags.TAGS:
    row = [res["by_tag"].get(c, {}).get(t) for c in ("human", "gemma", "llm")]
    if all(row): print("%-20s" % t, " | ".join("%7d %5.2f %5.2f %4.2f" % (r["n"], r["nll"], r["ent"], r["top1"]) for r in row))
print("\nposition (first 60 tokens, by 10):"); [print("%-18s" % k, res["position"][k][:8]) for k in ("wp/human", "wp/gemma", "wp/claude", "books/human", "books/gemma", "books/gpt")]
