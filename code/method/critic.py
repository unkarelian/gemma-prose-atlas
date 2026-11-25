"""External critic for prose: scores texts without asking the writing model.   <detector venv>/bin/python -I method/critic.py score FILE.jsonl [...]   |   rerank FILE.jsonl
Scores (per text): ai = fiction detector log-odds of AI (above 0 leans AI); taste = taste detector log-odds of 'rejected draft' (lower is closer
to the reader's approved edits; trained on one book, so treat it as a weak signal); plus variety, repetition and stock-word rate.
rerank: for files with several samples per brief, keep the sample with the lowest ai + 0.5 * taste, after dropping repetitive ones."""
import json, sys, os, re, pathlib, collections, statistics as st
sys.path.insert(0, os.path.expanduser("~/Projects/ProseLang/tools/export")); from preprocess import body, chunks
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
DET = pathlib.Path(os.path.expanduser("~/.cache/fiction-prose-style/detector")); dev = "cuda" if torch.cuda.is_available() else "cpu"
SLOP = set(json.load(open(pathlib.Path(__file__).resolve().parent.parent / "data/slop_lists.json"))["words"])
def load(n): return AutoTokenizer.from_pretrained(DET / n), AutoModelForSequenceClassification.from_pretrained(DET / n).eval().to(dev), json.loads((DET / n / "detector.json").read_text())
M = {"ai": load("model-fiction"), "taste": load("model-taste-b")}
def logodds(name, text):
    tok, m, meta = M[name]; cs = chunks(body(text))[:8]
    if not cs: return 0.0
    e = tok(cs, truncation=True, max_length=meta["max_len"], padding=True, return_tensors="pt").to(dev)
    with torch.no_grad(): lg = m(**e).logits
    return float((lg[:, 1] - lg[:, 0]).mean())
def score(text):
    t = " ".join(text.split(" ")[:330]); ws = re.findall(r"[a-z']+", t.lower()); tri = [" ".join(ws[i:i + 3]) for i in range(len(ws) - 2)]
    return dict(ai=round(logodds("ai", t), 2), taste=round(logodds("taste", t), 2), variety=round(len(set(ws)) / max(1, len(ws)), 3), repetition=round(1 - len(set(tri)) / max(1, len(tri)), 3),
                stock=round(1000 * sum(w in SLOP for w in ws) / max(1, len(ws)), 1), words=len(text.split()))
def summarise(rows):
    k = ("ai", "taste", "variety", "repetition", "stock", "words"); r = {x: round(st.mean(s[x] for s in rows), 3) for x in k}; r["flagged_ai"] = round(sum(s["ai"] > 0 for s in rows) / len(rows), 3); r["n"] = len(rows); return r
if __name__ == "__main__":
    mode, files = sys.argv[1], sys.argv[2:]; out = {}
    for f in files:
        rows = [json.loads(l) for l in open(f) if len(json.loads(l)["text"].split()) > 60]
        for r in rows: r["score"] = score(r["text"])
        tag = pathlib.Path(f).stem.replace("method_", "")
        for s in ("wp", "books"):
            sub = [r for r in rows if r.get("set", "wp") == s]
            if not sub: continue
            if mode == "rerank":
                by = collections.defaultdict(list)
                for r in sub: by[r["group"]].append(r)
                pick = [min((r for r in v if r["score"]["repetition"] < 0.12) or v, key=lambda r: r["score"]["ai"] + 0.5 * r["score"]["taste"]) for v in by.values() for v in [list(v)]]
                out[f"{tag} | {s} | first sample"] = summarise([v[0]["score"] for v in by.values()]); out[f"{tag} | {s} | reranked best of {max(len(v) for v in by.values())}"] = summarise([r["score"] for r in pick])
                with open(str(f).replace(".jsonl", f"_{s}_picked.jsonl"), "w") as g:
                    for r in pick: g.write(json.dumps(r, ensure_ascii=False) + "\n")
            else: out[f"{tag} | {s}"] = summarise([r["score"] for r in sub])
        with open(str(f).replace(".jsonl", "_scored.jsonl"), "w") as g:
            for r in rows: g.write(json.dumps(r, ensure_ascii=False) + "\n")
    print("%-44s %4s %7s %8s %7s %8s %6s %6s %6s" % ("configuration", "n", "ai", "flagged", "taste", "variety", "repeat", "stock", "words"))
    for k, v in out.items(): print("%-44s %4d %7.2f %7.0f%% %7.2f %8.3f %6.3f %6.1f %6.0f" % (k, v["n"], v["ai"], 100 * v["flagged_ai"], v["taste"], v["variety"], v["repetition"], v["stock"], v["words"]))
    p = pathlib.Path(__file__).resolve().parent.parent / "results/method_scores.json"; old = json.load(open(p)) if p.exists() else {}; old.update(out); json.dump(old, open(p, "w"), indent=1)
