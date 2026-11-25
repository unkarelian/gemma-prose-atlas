"""Pass 1: read every document in its frame and record, for all 34 x 16,384 transcoder features,
per-document mean activation and firing rate, plus token-tag sums by writer class and split half,
per-document mean residuals, and per-token surprisal / entropy / rank / top-5 alternatives.

    python read.py            (LIMIT=n for a smoke test)
Outputs in {W}/r1/.
"""
import os, json, time, sys, numpy as np, torch
import lib, tags
from lib import W
OUT = f"{W}/" + os.environ.get("R1", "r1"); os.makedirs(OUT, exist_ok=True)
tok, model = lib.load(); lib.load_tc()
NL, D, F, K = lib.NL, lib.D, 16384, len(tags.TAGS)

docs = lib.read_jsonl(f"{W}/" + os.environ.get("CORPUS", "corpus.jsonl"))
for d in docs: d["frame"] = "chat" if d.get("prompt") else "raw"
if os.path.exists(f"{W}/gen.jsonl") and not os.environ.get("CORPUS"): docs += lib.read_jsonl(f"{W}/gen.jsonl")
for d in [d for d in docs if d["set"] == "wp" and d["cond"] == "human" and not os.environ.get("CORPUS")]:
    sp = lib.split_opening(d["text"])
    if sp: docs.append(dict(id=d["id"] + "_raw", set="wp", group=d["group"], cond="human_raw", frame="raw", opening=sp[0], text=sp[1]))
docs = [d for d in docs if len(d["text"].split()) >= 20]
CAT = {"human": 0, "gemma": 1, "claude": 2, "glm": 2, "haiku": 2, "gpt": 2}
enc = []
for d in docs:
    fr, tx, off = lib.encode_doc(d)
    tg = tags.to_tokens(tags.spans(d["text"][: off[-1][1]]), off)
    enc.append((fr, tx, tg)); d["half"] = lib.half_of(d); d["n"] = len(tx); d["nf"] = len(fr)
order = sorted(range(len(docs)), key=lambda i: -(len(enc[i][0]) + len(enc[i][1])))
if os.environ.get("LIMIT"): order = order[:: max(1, len(order) // int(os.environ["LIMIT"]))]
docs = [docs[i] for i in order]; enc = [enc[i] for i in order]; N = len(docs)
print(N, "docs", sum(d["n"] for d in docs), "text tokens", sum(d["n"] + d["nf"] for d in docs), "total tokens", flush=True)
with open(f"{OUT}/docs.jsonl", "w") as f:
    for d in docs: f.write(json.dumps({k: v for k, v in d.items() if k not in ("text", "prompt", "opening")}) + "\n")
with open(f"{OUT}/texts.jsonl", "w") as f:
    for d in docs: f.write(json.dumps({k: d.get(k) for k in ("id", "text", "opening", "prompt", "frame")}, ensure_ascii=False) + "\n")
json.dump(tags.TAGS, open(f"{OUT}/tags.json", "w"))

mode = "r+" if os.path.exists(f"{OUT}/state.pt") else "w+"
fmean = np.lib.format.open_memmap(f"{OUT}/fmean.npy", mode=mode, dtype=np.float16, shape=(N, NL, F))
ffrac = np.lib.format.open_memmap(f"{OUT}/ffrac.npy", mode=mode, dtype=np.float16, shape=(N, NL, F))
if mode == "r+":
    S = torch.load(f"{OUT}/state.pt"); print("resuming at doc", S["next"], flush=True)
else:
    S = dict(next=0, rmean=torch.zeros(N, NL, D, dtype=torch.float16), tagsum=torch.zeros(NL, F, 8 * K), tagcnt=torch.zeros(NL, F, 8 * K),
             tagn=torch.zeros(8 * K), doctag=torch.zeros(N, K, dtype=torch.int16), tk=[None] * N)
TS, TCN = S["tagsum"].to("cuda"), S["tagcnt"].to("cuda")
BUDGET = int(os.environ.get("BUDGET", 22000))
cur = {}
def pre_hook(l):
    def h(m, i, o):
        a = lib.tc_acts(l, o[cur["bi"], cur["ti"]])
        nz = (a > 0).float()
        cur["fm"][:, l] = (cur["DM"].T @ a) / cur["nd"]; cur["ff"][:, l] = (cur["DM"].T @ nz) / cur["nd"]
        TS[l] += a.T @ cur["M"]; TCN[l] += nz.T @ cur["M"]
    return h
def res_hook(l):
    def h(m, i, o):
        x = (o[0] if isinstance(o, tuple) else o)[cur["bi"], cur["ti"]].float()
        cur["rm"][:, l] = (cur["DM"].T @ x) / cur["nd"]
    return h
hooks = [lib.LAYERS[l].pre_feedforward_layernorm.register_forward_hook(pre_hook(l)) for l in range(NL)]
hooks += [lib.LAYERS[l].register_forward_hook(res_hook(l)) for l in range(NL)]

t0 = time.time(); i = S["next"]; nb = 0; seen = 0
while i < N:
    L = len(enc[i][0]) + len(enc[i][1]); B = max(1, min(BUDGET // L, 48, N - i)); idx = list(range(i, i + B))
    ids = torch.full((B, L), tok.pad_token_id, dtype=torch.long); att = torch.zeros((B, L), dtype=torch.long)
    bi, ti, cols, rows = [], [], [], []; r0 = 0
    for b, j in enumerate(idx):
        fr, tx, tg = enc[j]; s = fr + tx; ids[b, :len(s)] = torch.tensor(s); att[b, :len(s)] = 1
        bi += [b] * len(tx); ti += list(range(len(fr), len(s)))
        cg = (CAT.get(docs[j]["cond"], 3) * 2 + docs[j]["half"]) * K
        for k, tl in tg.items():
            rows += [r0 + t for t in tl]; cols += [cg + k] * len(tl); S["doctag"][j, k] = len(tl)
        r0 += len(tx)
    n = len(bi); bi_t, ti_t = torch.tensor(bi, device="cuda"), torch.tensor(ti, device="cuda")
    M = torch.zeros(n, 8 * K, device="cuda"); M[torch.tensor(rows, device="cuda"), torch.tensor(cols, device="cuda")] = 1
    DM = torch.zeros(n, B, device="cuda"); DM[torch.arange(n, device="cuda"), bi_t] = 1
    cur.update(bi=bi_t, ti=ti_t, M=M, DM=DM, nd=DM.sum(0)[:, None], fm=torch.zeros(B, NL, F, device="cuda"), ff=torch.zeros(B, NL, F, device="cuda"),
               rm=torch.zeros(B, NL, D, device="cuda"))
    with torch.no_grad():
        last = lib.BASE(input_ids=ids.to("cuda"), attention_mask=att.to("cuda")).last_hidden_state
        hp = last[bi_t, ti_t - 1]; tgt = ids.to("cuda")[bi_t, ti_t]; del last
        lp_, en_, rk_, t5i, t5p = [], [], [], [], []
        for c in range(0, n, 1536):
            lp = lib.LM(hp[c:c + 1536]).float().log_softmax(-1); a = lp.gather(1, tgt[c:c + 1536, None])
            lp_.append(a[:, 0]); en_.append(-(lp.exp() * lp).sum(-1)); rk_.append((lp > a).sum(-1)); v, ix = lp.topk(5, -1); t5i.append(ix); t5p.append(v); del lp
        lp_, en_, rk_, t5i, t5p = [torch.cat(x).cpu() for x in (lp_, en_, rk_, t5i, t5p)]
    S["tagn"] += M.sum(0).cpu()
    fmean[idx] = cur["fm"].cpu().numpy().astype(np.float16); ffrac[idx] = cur["ff"].cpu().numpy().astype(np.float16)
    S["rmean"][idx] = cur["rm"].cpu().to(torch.float16)
    r0 = 0
    for b, j in enumerate(idx):
        m = len(enc[j][1]); sl = slice(r0, r0 + m); r0 += m
        S["tk"][j] = dict(ids=torch.tensor(enc[j][1], dtype=torch.int32), lp=lp_[sl].half(), ent=en_[sl].half(), rank=rk_[sl].int(), t5i=t5i[sl].int(), t5p=t5p[sl].half())
    i += B; nb += 1; seen += B * L
    if nb % 20 == 0: print(f"{i}/{N} docs  {seen / (time.time() - t0):.0f} tok/s  {time.time() - t0:.0f}s  gpu {torch.cuda.max_memory_allocated() / 2**30:.1f}G", flush=True)
    if nb % 150 == 0 or i >= N:
        S["next"] = i; S["tagsum"], S["tagcnt"] = TS.cpu(), TCN.cpu(); fmean.flush(); ffrac.flush(); torch.save(S, f"{OUT}/state.pt")
np.save(f"{OUT}/rmean.npy", S["rmean"].numpy()); np.save(f"{OUT}/tagsum.npy", S["tagsum"].numpy()); np.save(f"{OUT}/tagcnt.npy", S["tagcnt"].numpy())
np.save(f"{OUT}/tagn.npy", S["tagn"].numpy()); np.save(f"{OUT}/doctag.npy", S["doctag"].numpy())
tk = S["tk"]; off = np.cumsum([0] + [len(t["ids"]) for t in tk])
np.savez(f"{OUT}/tokens.npz", off=off, **{k: torch.cat([t[k] for t in tk]).numpy() for k in ("ids", "lp", "ent", "rank", "t5i", "t5p")})
print("READ_DONE", time.time() - t0)
