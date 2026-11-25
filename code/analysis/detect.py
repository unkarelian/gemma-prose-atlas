"""Score texts with the user's fiction AI detectors (independent of Gemma).   <detector venv>/bin/python -I analysis/detect.py
model-fiction: ModernBERT, 60-word chunks, log-odds of AI (above 0 leans AI).  model-fiction-scene: UltraBERT-150M, the whole text up to 2048 tokens.
-> results/detector.json"""
import json, sys, pathlib, collections, random, re, os
sys.path.insert(0, os.path.expanduser("~/Projects/ProseLang/tools/export"))
from preprocess import body, chunks
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
ROOT = pathlib.Path(__file__).resolve().parent.parent; DET = pathlib.Path(os.path.expanduser("~/.cache/fiction-prose-style/detector")); dev = "cuda" if torch.cuda.is_available() else "cpu"
def load(name):
    tok = AutoTokenizer.from_pretrained(DET / name); m = AutoModelForSequenceClassification.from_pretrained(DET / name).eval().to(dev); return tok, m, json.loads((DET / name / "detector.json").read_text())
CH = load("model-fiction"); SC = load("model-fiction-scene")
def chunk_score(text):
    tok, m, meta = CH; cs = chunks(body(text))[:8]; lo = []
    for i in range(0, len(cs), 16):
        e = tok(cs[i:i + 16], truncation=True, max_length=meta["max_len"], padding=True, return_tensors="pt").to(dev)
        with torch.no_grad(): lg = m(**e).logits
        lo += (lg[:, 1] - lg[:, 0]).tolist()
    return sum(lo) / max(1, len(lo))
def scene_score(text):
    tok, m, meta = SC; e = tok([body(text)], truncation=True, max_length=meta["max_len"], return_tensors="pt").to(dev)
    with torch.no_grad(): lg = m(**e).logits[0]
    return float(lg[1] - lg[0])
cap = lambda t, n=320: " ".join(t.split(" ")[:n])
sets = collections.OrderedDict(); random.seed(0)
gens = collections.defaultdict(list)
for l in open(ROOT / "data/gen.jsonl"):
    d = json.loads(l)
    if d["set"] == "wp": gens[d["cond"]].append(d["text"])
corp = collections.defaultdict(list)
for l in open(ROOT / "data/corpus.jsonl"):
    d = json.loads(l)
    if d["set"] == "wp": corp[d["cond"]].append(d["text"])
for k, v in (("human (stories)", corp["human"]), ("Claude", corp["claude"]), ("GLM", corp["glm"]), ("Gemma default", gens["gemma"]), ("Gemma, told plain", gens["gemma_plain"]), ("Gemma, told literary", gens["gemma_lit"]), ("Gemma, raw continuation", gens["gemma_raw"])):
    random.shuffle(v); sets[k] = v[:64]
for v in ("scale_-1.0", "scale_-0.5", "base", "scale_0.25", "scale_0.5", "scale_0.75", "lora_human", "lora_formal", "lora_full", "bake_rain60", "bake_habits", "bake_habits_names"):
    p = ROOT / f"data/variant_{v}_gen.jsonl"
    if p.exists(): sets["edited: " + v] = [json.loads(l)["text"] for l in open(p)]
st = collections.defaultdict(list)
if (ROOT / "data/steer.jsonl").exists():
    for l in open(ROOT / "data/steer.jsonl"): d = json.loads(l); st[d["cond"]].append(d["text"])
    for c in ("base", "human_L6_a4", "no_rain_60", "more_gemma_L12_a8", "llmdir_L12_a8"): sets["steered: " + c] = st[c]
sy = collections.defaultdict(list)
if (ROOT / "data/sysid_gen.jsonl").exists():
    for l in open(ROOT / "data/sysid_gen.jsonl"):
        d = json.loads(l)
        if d["kind"] == "story": sy[d["sys"]].append(d["text"])
    for c in ("none", "you are a human", "you are a large language model", "named human", "character (role-play)", "you are not alive"): sets["system prompt: " + c] = sy[c]
out = {}; per = {}
for k, ts in sets.items():
    ts = [cap(t) for t in ts if len(t.split()) > 80]; a = [chunk_score(t) for t in ts]; b = [scene_score(t) for t in ts]
    out[k] = dict(n=len(ts), chunk_logodds=round(sum(a) / len(a), 2), chunk_share_flagged_ai=round(sum(x > 0 for x in a) / len(a), 3), scene_logodds=round(sum(b) / len(b), 2), scene_share_flagged_ai=round(sum(x > 0 for x in b) / len(b), 3)); per[k] = [round(x, 2) for x in a]
    print("%-44s n %3d  chunk %6.2f (%3.0f%% AI)   scene %6.2f (%3.0f%% AI)" % (k, len(ts), out[k]["chunk_logodds"], 100 * out[k]["chunk_share_flagged_ai"], out[k]["scene_logodds"], 100 * out[k]["scene_share_flagged_ai"]), flush=True)
json.dump(dict(summary=out, per_text_chunk_logodds=per), open(ROOT / "results/detector.json", "w"), indent=1)
