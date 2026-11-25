"""Pass 2: for the features in r1/featlist.json, collect the strongest firing tokens (one per document, per writer class),
with a text window, and the tokens each feature's decoder promotes and suppresses.   python examples.py
Output: r1/examples.json
"""
import os, json, time, collections, torch
import lib
from lib import W
R = f"{W}/" + os.environ.get("R1", "r1")
tok, model = lib.load()
keys = json.load(open(f"{R}/featlist.json")); by = collections.defaultdict(list)
for k in keys: l, f = k[1:].split("."); by[int(l)].append(int(f))
lib.load_tc(sorted(by), dec=True)
docs = lib.read_jsonl(f"{R}/docs.jsonl"); texts = {d["id"]: d for d in lib.read_jsonl(f"{R}/texts.jsonl")}
CAT = {"human": 0, "gemma": 1, "claude": 2, "glm": 2, "haiku": 2, "gpt": 2}; KC = 10
order = list(range(len(docs)))
if os.environ.get("LIMIT"): order = order[:: max(1, len(order) // int(os.environ["LIMIT"]))]
enc = {}
for i in order:
    d = dict(docs[i], **texts[docs[i]["id"]]); fr, tx, off = lib.encode_doc(d); enc[i] = (fr, tx, off)
P = {l: dict(idx=torch.tensor(fs, device="cuda"), w=lib.TC[l]["w_enc"][:, fs], b=lib.TC[l]["b_enc"][fs], thr=lib.TC[l]["threshold"][fs],
             v=torch.zeros(len(fs), 4, KC, device="cuda"), g=torch.full((len(fs), 4, KC), -1, dtype=torch.long, device="cuda"),
             n=torch.zeros(len(fs), device="cuda"), s=torch.zeros(len(fs), device="cuda")) for l, fs in by.items()}
cur = {}
def hook(l):
    def h(m, i, o):
        p = P[l]; x = o[cur["bi"], cur["ti"]]
        a = (x.to(torch.bfloat16) @ p["w"]).float() + p["b"]; a = a * (a > p["thr"])           # [n, nf]
        p["n"] += (a > 0).sum(0); p["s"] += a.sum(0)
        B = cur["B"]; big = torch.full((B, cur["T"], a.shape[1]), -1.0, device="cuda"); big[cur["bi"], cur["tl"]] = a
        mv, mt = big.max(1)                                                                      # per doc: [B, nf]
        gid = cur["doc"][:, None] * 1000 + mt                                                    # doc * 1000 + text token
        for c in range(4):
            sel = cur["cat"] == c
            if not sel.any(): continue
            v = torch.cat([p["v"][:, c], mv[sel].T], 1); g = torch.cat([p["g"][:, c], gid[sel].T], 1)
            tv, ti = v.topk(KC, 1); p["v"][:, c] = tv; p["g"][:, c] = g.gather(1, ti)
    return h
hooks = [lib.LAYERS[l].pre_feedforward_layernorm.register_forward_hook(hook(l)) for l in by]
t0 = time.time(); k = 0; BUDGET = int(os.environ.get("BUDGET", 30000)); ntk = 0
while k < len(order):
    i0 = order[k]; L = len(enc[i0][0]) + len(enc[i0][1]); B = max(1, min(BUDGET // L, 64, len(order) - k)); idx = order[k:k + B]
    ids = torch.full((B, L), tok.pad_token_id, dtype=torch.long); att = torch.zeros((B, L), dtype=torch.long); bi, ti, tl = [], [], []
    for b, j in enumerate(idx):
        fr, tx, _ = enc[j]; s = fr + tx; ids[b, :len(s)] = torch.tensor(s); att[b, :len(s)] = 1
        bi += [b] * len(tx); ti += list(range(len(fr), len(s))); tl += list(range(len(tx)))
    cur.update(bi=torch.tensor(bi, device="cuda"), ti=torch.tensor(ti, device="cuda"), tl=torch.tensor(tl, device="cuda"), B=B, T=lib.MAXTEXT,
               doc=torch.tensor(idx, device="cuda"), cat=torch.tensor([CAT.get(docs[j]["cond"], 3) for j in idx], device="cuda"))
    with torch.no_grad(): lib.BASE(input_ids=ids.to("cuda"), attention_mask=att.to("cuda"))
    k += B; ntk += len(bi)
    if (k // B) % 20 == 0: print(f"{k}/{len(order)} docs {time.time() - t0:.0f}s", flush=True)
for h in hooks: h.remove()
U = lib.LM.weight.float()
def snippet(di, t, before=28, after=6):
    fr, tx, off = enc[di]; text = texts[docs[di]["id"]]["text"]
    a = off[max(0, t - before)][0]; b = off[min(len(tx) - 1, t + after)][1]; s, e = off[t]
    return [text[a:s], text[s:e], text[e:b]]
out = {}
for l, fs in by.items():
    p = P[l]; dec = lib.TC[l]["w_dec"][fs].to("cuda")                                           # [nf, d]
    lg = dec @ U.T; top = lg.topk(12, 1).indices.cpu(); bot = (-lg).topk(8, 1).indices.cpu()
    for q, f in enumerate(fs):
        ex = []
        for c in range(4):
            for v, g in zip(p["v"][q, c].tolist(), p["g"][q, c].tolist()):
                if v <= 0 or g < 0: continue
                di, t = divmod(g, 1000); d = docs[di]
                ex.append(dict(doc=d["id"], cls=c, act=round(v, 1), t=t, private=bool(d.get("private")), s=snippet(di, t)))
        out[f"L{l}.{f}"] = dict(density=round(float(p["n"][q]) / ntk, 5), mean_act=round(float(p["s"][q] / p["n"][q].clamp(min=1)), 1),
                                 top=[tok.decode([int(x)]) for x in top[q]], bottom=[tok.decode([int(x)]) for x in bot[q]], ex=ex)
json.dump(out, open(f"{R}/examples.json", "w"), ensure_ascii=False)
print("EXAMPLES_DONE", len(out), time.time() - t0)
