"""Merge labels, statistics and examples into results/atlas.json (publishable: no novel text, no private edits)."""
import json, glob, os, numpy as np, collections
R = "data/r1"; ex = json.load(open(f"{R}/examples.json")); why = json.load(open(f"{R}/featwhy.json")); sel = json.load(open(f"{R}/select.json")); _cf = np.load(f"{R}/cond_frac.npz"); cf = {k: _cf[k] for k in _cf.files}
lab = {}
for f in sorted(glob.glob("data/label/out/batch_*.json")):
    try:
        for x in json.load(open(f)): lab[x["key"]] = x
    except Exception as e: print("bad", f, e)
CONDS = ["wp/human", "wp/gemma", "wp/claude", "wp/glm", "books/human", "books/gemma", "books/haiku", "books/gpt", "books/glm", "wp/gemma_plain", "wp/gemma_lit", "wp/gemma_greedy", "wp/gemma_raw", "wp/human_raw", "taste/approved", "taste/rejected"]
cstat = {c: {f["key"]: f for f in v["feats"]} for c, v in sel["contrasts"].items()}
att = json.load(open("data/attract.json")) if os.path.exists("data/attract.json") else {}
attr = collections.defaultdict(list)
for n, v in att.items():
    for r, f in enumerate(v["features"][:30]): attr[f["key"]].append(dict(set=n, target=v["target"], rank=r + 1, attr=f["attr"]))
conf = json.load(open(f"{R}/conf.json")) if os.path.exists(f"{R}/conf.json") else {}
CLS = ["human", "Gemma", "other LLM", "other"]; feats = []
for k, e in ex.items():
    l, f = map(int, k[1:].split(".")); L = lab.get(k, {})
    exs = []
    for c in range(4):
        pub = [x for x in sorted(e["ex"], key=lambda x: -x["act"]) if x["cls"] == c and not x["private"] and not x["doc"].startswith("books/")][:3]      # nothing derived from the novels or their outlines is published
        exs += [dict(w=CLS[c], v=round(x["act"]), t=(x["s"][0][-150:] + "[[" + x["s"][1] + "]]" + x["s"][2][:40]).replace("\n", "⏎")) for x in pub]
    feats.append(dict(key=k, layer=l, feat=f, label=L.get("label", "(unlabelled)"), kind=L.get("kind", "unclear"), group=L.get("group", "Unclear"), conf=L.get("conf", "low"), note=L.get("note", ""),
                      why=why.get(k, []), density=e["density"], top=e["top"][:10], bottom=e["bottom"][:6],
                      rates={c: round(float(cf[c][l, f]), 4) for c in CONDS if c in cf},
                      contrasts=[dict(c=c, d0=s[k]["d0"], d1=s[k]["d1"], dfrac=s[k]["dfrac"]) for c, s in cstat.items() if k in s],
                      attract=attr.get(k, []), entropy=conf.get(k), ex=exs))
BN = set(json.load(open("data/book_names.json"))) if os.path.exists("data/book_names.json") else set(); import re as _re
def scrub(t):          # drop quoted phrases that contain a character name from the novels
    return _re.sub(r"['\"‘“][^'\"’”]{0,80}['\"’”]", lambda m: "[a quoted phrase]" if any(w.strip(".,'’s") in BN for w in m.group(0).split()) else m.group(0), t)
for x in feats: x["note"] = scrub(x["note"]); x["label"] = scrub(x["label"])
feats.sort(key=lambda x: (x["layer"], x["feat"]))
groups = collections.Counter(x["group"] for x in feats)
json.dump(dict(features=feats, groups=[g for g, _ in groups.most_common()], conds=CONDS,
               tags={t: dict(n=v["n"], per_class=v["per_class"], feats=[f["key"] for f in v["feats"][:8]]) for t, v in sel["tags"].items()},
               contrasts={c: dict(n=v["n"], half_corr=v["corr_halves"]) for c, v in sel["contrasts"].items()}), open("results/atlas.json", "w"), ensure_ascii=False)
print(len(feats), "features,", len(lab), "labelled;", dict(groups.most_common()))
