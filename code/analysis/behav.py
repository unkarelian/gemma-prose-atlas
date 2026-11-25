"""Behaviour before internals: how often each writer uses each construction, and how Gemma opens.  -> results/behav.json"""
import json, sys, re, collections, os, statistics as st
sys.path.insert(0, "pod"); import tags
docs = [json.loads(l) for l in open("data/corpus.jsonl")] + [json.loads(l) for l in open("data/gen.jsonl")]
def cap(t, n=450): return " ".join(t.split(" ")[:n])
rate = collections.defaultdict(lambda: collections.defaultdict(list)); extra = collections.defaultdict(lambda: collections.defaultdict(list))
for d in docs:
    t = cap(d["text"]); nw = max(1, len(t.split())); key = f"{d['set']}/{d['cond']}"; sp = tags.spans(t)
    for k, v in sp.items(): rate[key][k].append(1000 * len(v) / nw)
    sents = [len(t[a:b].split()) for a, b in zip([s[0] for s in sp["sent_start"]], [s[1] for s in sp["sent_end"]])]
    if len(sents) > 3:
        extra[key]["sent_len_mean"].append(st.mean(sents)); extra[key]["sent_len_sd"].append(st.pstdev(sents))
    ws = re.findall(r"[a-z']+", t.lower()); extra[key]["ttr_300"].append(len(set(ws[:300])) / max(1, len(ws[:300])))
    extra[key]["para_words"].append(nw / max(1, len(sp["para_start"]))); extra[key]["dialogue_share"].append(sum(b - a for a, b in sp["dialogue"]) / max(1, len(t)))
out = {k: dict(n=len(v["sent_start"]), **{t: round(st.mean(x), 3) for t, x in v.items()}, **{t: round(st.mean(x), 3) for t, x in extra[k].items()}) for k, v in rate.items()}
# openings
op = {}
for cond in ("human", "gemma", "gemma_greedy", "gemma_plain", "gemma_lit", "claude", "glm", "haiku", "gpt"):
    for s in ("wp", "books"):
        ds = [d for d in docs if d["set"] == s and d["cond"] == cond]
        if not ds: continue
        first = [re.split(r"(?<=[.!?])\s", d["text"].strip())[0] for d in ds]
        w1 = collections.Counter(f.split()[0].strip('"“*') for f in first if f.split()); w3 = collections.Counter(" ".join(f.split()[:3]) for f in first)
        op[f"{s}/{cond}"] = dict(n=len(ds), first_word=w1.most_common(6), first3=w3.most_common(6), distinct_first3=round(len(w3) / len(ds), 3))
# names
names = {}
for key in ("wp/human", "wp/gemma", "books/gemma", "wp/claude", "wp/glm", "wp/gemma_greedy", "wp/gemma_raw"):
    c = collections.Counter(); n = 0
    for d in docs:
        if f"{d['set']}/{d['cond']}" != key: continue
        n += 1; c.update(set(re.findall(r"(?<=[a-z,;] )[A-Z][a-z]{2,}\b", cap(d["text"]))))
    names[key] = dict(n=n, top=[(w, round(k / n, 3)) for w, k in c.most_common(25)])
json.dump(dict(rates=out, openings=op, names=names), open("results/behav.json", "w"), indent=1)
keys = ["wp/human", "wp/gemma", "wp/gemma_greedy", "wp/gemma_plain", "wp/gemma_lit", "wp/gemma_raw", "wp/claude", "wp/glm", "books/human", "books/gemma", "books/haiku", "books/gpt", "books/glm"]
print("%-16s" % "per 1000 words" + "".join("%9s" % k.split("/")[1][:8] for k in keys))
for t in ["sent_len_mean", "sent_len_sd", "para_words", "dialogue_share", "ttr_300", "slop_word", "slop_tri", "simile_like", "as_if", "em_dash", "ellipsis", "semicolon", "exclaim", "question", "wasnt_it_was", "not_just", "emotion_pack", "something", "seemed", "bookism", "tag_adverb", "voice_barely", "body_cliche", "eyes", "air_silence", "moment", "ly_adverb", "just_adv", "abstract", "short_sent", "long_sent", "list3", "said", "name", "couldnt_help"]:
    print("%-16s" % t + "".join("%9.2f" % out[k][t] for k in keys))
for k, v in op.items(): print(k, v["distinct_first3"], v["first3"][:4])
for k, v in names.items(): print(k, v["top"][:14])
