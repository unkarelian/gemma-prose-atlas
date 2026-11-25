"""Gemma writes the same briefs as the humans and the other models.   python gen.py [variant ...]

variants: default (wp + books, sampled), greedy / plain / lit (first 160 wp briefs), raw (no chat template: continue the
human story's first 60 words). Output: {W}/gen.jsonl, one document per line; finished ids are skipped.
"""
import sys, json, os, time, torch
import lib
from lib import W
STYLE = {"plain": "\n\nStyle: plain, concrete, understated prose. Short ordinary words. No ornate metaphors and no cliches.",
         "lit": "\n\nStyle: beautiful, evocative, richly literary prose."}
variants = sys.argv[1:] or ["default", "greedy", "plain", "lit", "raw"]
tok, model = lib.load(); tok.padding_side = "left"
tasks = lib.read_jsonl(f"{W}/gen_tasks.jsonl"); corpus = {d["id"]: d for d in lib.read_jsonl(f"{W}/corpus.jsonl")}
out_path = f"{W}/gen.jsonl"
done = {json.loads(l)["id"] for l in open(out_path)} if os.path.exists(out_path) else set()
jobs = []
wp = [t for t in tasks if t["set"] == "wp"]
for v in variants:
    if v == "default":
        for t in tasks: jobs.append(dict(id=f"{t['set']}/{t['group']}/gemma", set=t["set"], group=t["group"], cond="gemma", prompt=t["prompt"], frame="chat", book=t.get("book"), v=v))
    elif v in ("greedy", "plain", "lit"):
        for t in wp[:160]: jobs.append(dict(id=f"wp/{t['group']}/gemma_{v}", set="wp", group=t["group"], cond=f"gemma_{v}", prompt=t["prompt"] + STYLE.get(v, ""), frame="chat", v=v))
    elif v == "raw":
        for t in wp:
            sp = lib.split_opening(corpus[f"wp/{t['group']}/human"]["text"])
            if sp: jobs.append(dict(id=f"wp/{t['group']}/gemma_raw", set="wp", group=t["group"], cond="gemma_raw", opening=sp[0], frame="raw", v=v))
jobs = [j for j in jobs if j["id"] not in done]
for j in jobs:
    j["ids"] = ([tok.bos_token_id] + tok(j["opening"], add_special_tokens=False).input_ids) if j["frame"] == "raw" else tok(lib.chat_frame(j["prompt"]), add_special_tokens=False).input_ids
jobs.sort(key=lambda j: (j["v"], len(j["ids"])))
print(len(jobs), "jobs", flush=True)
BS = int(os.environ.get("BS", 40)); t0 = time.time(); ntok = 0
from transformers.generation.streamers import BaseStreamer
LABEL = {"default": "default", "greedy": "greedy (no sampling)", "plain": "told to write plainly", "lit": "told to write literary prose", "raw": "raw continuation, no chat template"}
class Live(BaseStreamer):
    """Writes the first rows of the batch to live.json as they are generated, for the status page."""
    def __init__(self, b, prog):
        self.meta = [dict(id=j["id"], mode=LABEL[j["v"]], brief=(j.get("opening") or j["prompt"].split("\n\n")[1 if j["set"] == "wp" else 0])[:400]) for j in b[:4]]
        if b[0]["set"] == "books":
            for m, j in zip(self.meta, b): m["brief"] = "A novel scene written from an outline (" + j["group"].rsplit("--", 1)[0].replace("-", " ") + ")"
        self.toks = [[] for _ in self.meta]; self.n = -1; self.prog = prog
    def put(self, v):
        self.n += 1
        if self.n == 0: return
        for k in range(len(self.toks)): self.toks[k].append(int(v[k]))
        if self.n % 6 == 0: self.dump()
    def dump(self, done=False):
        items = [dict(m, text=tok.decode(t, skip_special_tokens=True)) for m, t in zip(self.meta, self.toks)]
        json.dump(dict(stage="writing", progress=self.prog, done=done, items=items), open(f"{W}/live.tmp", "w")); os.replace(f"{W}/live.tmp", f"{W}/live.json")
    def end(self): self.dump(True)
i = 0
while i < len(jobs):
    b = [jobs[i]]
    while len(b) < BS and i + len(b) < len(jobs) and jobs[i + len(b)]["v"] == b[0]["v"] and len(jobs[i + len(b)]["ids"]) * (len(b) + 1) < 40000: b.append(jobs[i + len(b)])
    i += len(b)
    L = max(len(j["ids"]) for j in b)
    ids = torch.full((len(b), L), tok.pad_token_id, dtype=torch.long); att = torch.zeros((len(b), L), dtype=torch.long)
    for k, j in enumerate(b): ids[k, L - len(j["ids"]):] = torch.tensor(j["ids"]); att[k, L - len(j["ids"]):] = 1
    kw = dict(do_sample=False) if b[0]["v"] == "greedy" else dict(do_sample=True, temperature=1.0, top_k=64, top_p=0.95)
    with torch.no_grad():
        o = model.generate(input_ids=ids.to("cuda"), attention_mask=att.to("cuda"), max_new_tokens=int(os.environ.get("MAXNEW", 660)), streamer=Live(b, f"{i}/{len(jobs)}"), **kw)
    with open(out_path, "a") as f:
        for k, j in enumerate(b):
            new = o[k, L:]; text = tok.decode(new, skip_special_tokens=True)
            ntok += int((new != tok.pad_token_id).sum())
            d = {x: j[x] for x in ("id", "set", "group", "cond", "frame") if x in j}
            if j.get("book"): d["book"] = j["book"]
            if j["frame"] == "raw": d["opening"] = j["opening"]; d["text"] = text
            else: d["prompt"] = j["prompt"]; d["text"] = text.strip()
            f.write(json.dumps(d, ensure_ascii=False) + "\n")
    print(f"{i}/{len(jobs)} {b[0]['v']} {ntok / (time.time() - t0):.0f} tok/s {time.time() - t0:.0f}s", flush=True)
print("GEN_DONE")
