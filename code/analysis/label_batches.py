"""Build labelling batches for the atlas: one JSON per batch in data/label/in/, each feature with its statistics and examples."""
import json, os, numpy as np, collections, random
R = "data/r1"; ex = json.load(open(f"{R}/examples.json")); why = json.load(open(f"{R}/featwhy.json")); sel = json.load(open(f"{R}/select.json"))
_cf = np.load(f"{R}/cond_frac.npz"); cf = {k: _cf[k] for k in _cf.files}; os.makedirs("data/label/in", exist_ok=True); os.makedirs("data/label/out", exist_ok=True)
CLS = ["human", "gemma", "other LLM", "other"]
cstat = {c: {f["key"]: f for f in v["feats"]} for c, v in sel["contrasts"].items()}
feats = []
for k in sorted(ex, key=lambda k: (int(k[1:].split(".")[0]), int(k.split(".")[1]))):
    l, f = map(int, k[1:].split(".")); e = ex[k]
    rates = {c: round(float(cf[c][l, f]), 3) for c in ("wp/human", "wp/gemma", "wp/claude", "wp/glm", "books/human", "books/gemma", "books/gpt", "books/haiku", "wp/gemma_plain", "wp/gemma_lit", "wp/gemma_raw", "wp/human_raw", "taste/approved", "taste/rejected")}
    exs = sorted(e["ex"], key=lambda x: -x["act"]); pick = []
    for c in (0, 1, 2, 3): pick += [x for x in exs if x["cls"] == c][:4]
    feats.append(dict(key=k, selected_for=why.get(k, []), fires_on_share_of_tokens=rates, overall_density=e["density"],
                      decoder_promotes=e["top"], decoder_suppresses=e["bottom"],
                      examples=[dict(writer=CLS[x["cls"]], act=x["act"], text=(x["s"][0][-170:] + "[[" + x["s"][1] + "]]" + x["s"][2][:40]).replace("\n", "⏎")) for x in pick]))
random.seed(2); n = 48
batches = [feats[i:i + n] for i in range(0, len(feats), n)]
for i, b in enumerate(batches): json.dump(b, open(f"data/label/in/batch_{i:02}.json", "w"), ensure_ascii=False, indent=0)
print(len(feats), "features in", len(batches), "batches;", sum(os.path.getsize(f"data/label/in/batch_{i:02}.json") for i in range(len(batches))) // 1024, "KB")
