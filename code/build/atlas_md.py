"""Markdown version of the atlas, readable on GitHub: ATLAS.md (index) + atlas/<theme>.md   python3 build/atlas_md.py OUTDIR"""
import json, os, re, sys, collections
out = sys.argv[1] if len(sys.argv) > 1 else "share"; A = json.load(open(os.environ.get("PI_ATLAS") or "results/atlas.json")); os.makedirs(f"{out}/atlas", exist_ok=True)
slug = lambda g: re.sub(r"[^a-z0-9]+", "-", g.lower()).strip("-")
pc = lambda x: f"{100 * x:.1f}"
md = lambda s: str(s).replace("|", "\\|").replace("\n", " ").replace("<", "&lt;")
by = collections.defaultdict(list)
for f in A["features"]: by[f["group"]].append(f)
idx = ["# Prose atlas: Gemma 3 4B-it", "", f"{len(A['features'])} transcoder features (Gemma Scope 2, 34 layers x 16,384) that fire differently for different writers of the same brief, attach to a prose construction, or write toward one of Gemma's habitual tokens. Labels were written by Claude from each feature's examples, firing rates and output tokens; they are best guesses with a confidence level.",
       "", "The interactive version is `site/atlas.html` (clone the repo and open it in a browser; it needs `site/assets/`). The same data as JSON is `results/atlas.json`.", "",
       "Columns: **G / H / L** = share of text tokens the feature fires on in Gemma's, human and other-LLM stories (r/WritingPrompts, same prompts), in percent.", "", "| Theme | Features | Layers |", "|---|---|---|"]
for g in A["groups"]:
    fs = sorted(by[g], key=lambda f: (f["layer"], f["feat"])); ls = [f["layer"] for f in fs]
    idx.append(f"| [{g}](atlas/{slug(g)}.md) | {len(fs)} | {min(ls)}–{max(ls)} |")
    L = [f"# {g}", "", f"{len(fs)} features. [Back to the index](../ATLAS.md)", "", "| Feature | Label | Kind | Conf. | G | H | L | Promotes |", "|---|---|---|---|---|---|---|---|"]
    for f in fs:
        r = f["rates"]; llm = (r.get("wp/claude", 0) + r.get("wp/glm", 0)) / 2
        L.append(f"| [{f['key']}](#{f['key'].lower().replace('.', '')}) | {md(f['label'])} | {f['kind']} | {f['conf']} | {pc(r.get('wp/gemma', 0))} | {pc(r.get('wp/human', 0))} | {pc(llm)} | {md(' '.join(repr(t)[1:-1] for t in f['top'][:5]))} |")
    L.append("")
    for f in fs:
        r = f["rates"]
        L += [f"## {f['key']}", "", f"**{md(f['label'])}** ({f['kind']}, {f['conf']} confidence)", "", md(f["note"]), "",
              "Fires on (% of tokens): " + ", ".join(f"{c} {pc(v)}" for c, v in r.items()) + ".", ""]
        if f["contrasts"]: L += ["Writer contrasts (paired effect size on each half, change in firing rate): " + "; ".join(f"{c['c']} {c['d0']}/{c['d1']} ({pc(c['dfrac'])} pts)" for c in f["contrasts"]) + ".", ""]
        tg = [w[4:] for w in f["why"] if w.startswith("tag:")]
        if tg: L += ["Constructions: " + ", ".join(tg) + ".", ""]
        if f["attract"]: L += ["Writes toward: " + "; ".join(f"{a['set']} “{a['target']}” (rank {a['rank']})" for a in f["attract"]) + ".", ""]
        L += ["Promotes: " + " ".join(f"`{md(repr(t)[1:-1])}`" for t in f["top"][:10]) + "  ", "Suppresses: " + " ".join(f"`{md(repr(t)[1:-1])}`" for t in f["bottom"][:6]), ""]
        for x in f["ex"][:6]: L.append(f"- *{x['w']}* ({x['v']}): {md(x['t']).replace('[[', '**[').replace(']]', ']**')}")
        L.append("")
    open(f"{out}/atlas/{slug(g)}.md", "w").write("\n".join(L))
idx += ["", "## By construction", "", "Features that fire on a construction's tokens; `pre:` = one token before it starts.", "", "| Construction | Tokens (human / Gemma / other LLM) | Top features |", "|---|---|---|"]
K = {f["key"]: f for f in A["features"]}
for t, v in A["tags"].items():
    idx.append(f"| {t} | {v['per_class'][0]:,} / {v['per_class'][1]:,} / {v['per_class'][2]:,} | " + "; ".join(f"{k} ({md(K[k]['label'])})" for k in v["feats"][:4] if k in K) + " |")
open(f"{out}/ATLAS.md", "w").write("\n".join(idx) + "\n"); print("atlas markdown:", len(A["groups"]), "theme files")
