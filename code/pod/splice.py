"""Time course of the late-layer 'not my text' features around a change of writer.   python splice.py   -> r1/splice.json
Conditions (per-position firing rate, averaged over stories, positions counted from the start of the text):
 gemma / human            : the whole text by one writer, in the chat frame (model turn)
 gemma_then_human         : Gemma's first 120 tokens, then the human story on the same prompt from its token 120
 human_then_gemma         : the reverse
 user_gemma / user_human  : the same texts placed in the USER turn ("Here is a story I wrote:")
 raw_human_then_gemma     : no chat template; the human's first 60 words, then Gemma's own continuation of them
"""
import os, json, random, collections, numpy as np, torch
import lib
from lib import W
R = f"{W}/r1"; tok, model = lib.load(); random.seed(6)
KEYS = "L33.1074,L33.9216,L33.819,L33.691,L32.426,L33.396,L28.4207,L33.56,L32.130,L33.225,L33.1729,L33.543".split(",")
by = collections.defaultdict(list)
for k in KEYS: l, f = k[1:].split("."); by[int(l)].append(int(f))
lib.load_tc(sorted(by)); T = 360; CUT = 120
docs = {d["id"]: d for d in lib.read_jsonl(f"{W}/corpus.jsonl") + lib.read_jsonl(f"{W}/gen.jsonl")}
groups = [g for g in sorted({d["group"] for d in docs.values() if d["set"] == "wp"}) if f"wp/{g}/gemma" in docs and f"wp/{g}/human" in docs and f"wp/{g}/gemma_raw" in docs]
random.shuffle(groups); groups = groups[:150]
enc = lambda s: tok(s, add_special_tokens=False).input_ids
cap = {}; hooks = [lib.LAYERS[l].pre_feedforward_layernorm.register_forward_hook(lambda m, i, o, l=l: cap.__setitem__(l, o[0])) for l in by]
acc = collections.defaultdict(lambda: {k: np.zeros(T) for k in KEYS}); cnt = collections.defaultdict(lambda: np.zeros(T)); ent = collections.defaultdict(lambda: np.zeros(T))
def run(name, frame, text_ids):
    text_ids = text_ids[:T]; ids = torch.tensor([frame + text_ids]).cuda(); n = len(text_ids)
    with torch.no_grad():
        h = lib.BASE(input_ids=ids).last_hidden_state[0, len(frame):]; lp = lib.LM(h).float().log_softmax(-1); ent[name][:n] += (-(lp.exp() * lp).sum(-1)).cpu().numpy()
        for l, fs in by.items():
            t = lib.TC[l]; a = (cap[l][len(frame):].to(torch.bfloat16) @ t["w_enc"][:, fs]).float() + t["b_enc"][fs]; a = (a > t["threshold"][fs]).float().cpu().numpy()
            for q, f in enumerate(fs): acc[name][f"L{l}.{f}"][:n] += a[:, q]
    cnt[name][:n] += 1
for gi, g in enumerate(groups):
    G, H, RAW = docs[f"wp/{g}/gemma"], docs[f"wp/{g}/human"], docs[f"wp/{g}/gemma_raw"]
    fr = enc(lib.chat_frame(G["prompt"])); gi_, hi_ = enc(G["text"]), enc(H["text"])
    if min(len(gi_), len(hi_)) < T: continue
    run("gemma", fr, gi_); run("human", fr, hi_); run("gemma_then_human", fr, gi_[:CUT] + hi_[CUT:]); run("human_then_gemma", fr, hi_[:CUT] + gi_[CUT:])
    for nm, ti in (("user_gemma", gi_), ("user_human", hi_)):
        full = lib.chat_frame("Here is a story I wrote:\n\n@@@"); a, b = full.split("@@@"); pre = enc(a); ids_ = pre + ti[:T] + enc(b)
        run(nm, pre, ti[:T] + enc(b))
    op = enc(RAW["opening"]); run("raw_human_then_gemma", [tok.bos_token_id], op + enc(RAW["text"]))
    if gi % 25 == 0: print(gi, len(groups), flush=True)
out = {name: dict(n=int(cnt[name].max()), entropy=[round(float(x), 3) for x in ent[name] / np.maximum(cnt[name], 1)], feats={k: [round(float(x), 3) for x in v / np.maximum(cnt[name], 1)] for k, v in acc[name].items()}) for name in acc}
json.dump(dict(cut=CUT, T=T, keys=KEYS, conds=out), open(f"{R}/splice.json", "w"))
for name, v in out.items(): print(name, v["n"], {k: [round(float(np.mean(x[a:b])), 2) for a, b in ((0, 60), (60, 120), (120, 150), (150, 240), (240, 360))] for k, x in list(v["feats"].items())[:3]})
print("SPLICE_DONE")
