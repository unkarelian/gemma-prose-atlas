"""Are the late-layer features that mark 'human text' confidence features?   python conf.py
For chosen features, token-level correlation of activation with the entropy and surprisal of the model's next-token prediction,
within each writer class, on a sample of documents. Output r1/conf.json"""
import os, json, random, collections, numpy as np, torch
import lib
from lib import W
R = f"{W}/r1"; tok, model = lib.load(); random.seed(4)
KEYS = os.environ.get("KEYS", "L32.426,L33.691,L33.396,L33.1074,L33.669,L33.9216,L33.819,L33.1447,L28.4207,L33.225,L33.56,L32.130,L32.184,L33.543,L33.449,L31.1784,L33.1729,L32.450,L30.85,L33.833").split(",")
by = collections.defaultdict(list)
for k in KEYS: l, f = k[1:].split("."); by[int(l)].append(int(f))
lib.load_tc(sorted(by))
docs = lib.read_jsonl(f"{R}/docs.jsonl"); texts = {d["id"]: d for d in lib.read_jsonl(f"{R}/texts.jsonl")}
CAT = {"human": "human", "gemma": "gemma", "claude": "llm", "glm": "llm", "haiku": "llm", "gpt": "llm"}
pick = []
for c in ("human", "gemma", "llm"):
    ii = [i for i, d in enumerate(docs) if CAT.get(d["cond"]) == c and d["set"] == "wp"]; random.shuffle(ii); pick += ii[:120]
acts = collections.defaultdict(list); ents, nlls, cls = [], [], []; cap = {}
hooks = [lib.LAYERS[l].pre_feedforward_layernorm.register_forward_hook(lambda m, i, o, l=l: cap.__setitem__(l, o[0])) for l in by]
for n, i in enumerate(pick):
    d = dict(docs[i], **texts[docs[i]["id"]]); fr, tx, _ = lib.encode_doc(d); ids = torch.tensor([fr + tx]).cuda()
    with torch.no_grad():
        h = lib.BASE(input_ids=ids).last_hidden_state[0]; lp = lib.LM(h[len(fr):-1]).float().log_softmax(-1)      # predictions made at text tokens 0..n-2
        ents.append(-(lp.exp() * lp).sum(-1).cpu()); nlls.append(-lp.gather(1, ids[0, len(fr) + 1:, None])[:, 0].cpu()); cls += [CAT[docs[i]["cond"]]] * (len(tx) - 1)
        for l, fs in by.items():
            t = lib.TC[l]; a = (cap[l][len(fr):-1].to(torch.bfloat16) @ t["w_enc"][:, fs]).float() + t["b_enc"][fs]; a = a * (a > t["threshold"][fs])
            for q, f in enumerate(fs): acts[f"L{l}.{f}"].append(a[:, q].cpu())
ent, nll, cls = torch.cat(ents).numpy(), torch.cat(nlls).numpy(), np.array(cls); out = {}
def corr(a, b): return round(float(np.corrcoef(a, b)[0, 1]), 3) if a.std() > 0 else None
for k in KEYS:
    a = torch.cat(acts[k]).numpy(); on = a > 0; r = dict(all=dict(r_entropy=corr(on, ent), r_surprisal=corr(on, nll), fires=round(float(on.mean()), 3)))
    for c in ("human", "gemma", "llm"):
        m = cls == c; q = np.quantile(ent[m], [0.25, 0.5, 0.75]); b = np.digitize(ent[m], q)
        r[c] = dict(r_entropy=corr(on[m], ent[m]), r_surprisal=corr(on[m], nll[m]), fires=round(float(on[m].mean()), 3), fires_by_entropy_quartile=[round(float(on[m][b == j].mean()), 3) for j in range(4)])
    # matched comparison: within the same entropy decile, does it still fire more for human text than for Gemma's?
    dec = np.quantile(ent, np.linspace(0.1, 0.9, 9)); bb = np.digitize(ent, dec)
    r["human_minus_gemma_within_entropy_decile"] = round(float(np.mean([on[(bb == j) & (cls == "human")].mean() - on[(bb == j) & (cls == "gemma")].mean() for j in range(10) if ((bb == j) & (cls == "human")).sum() > 50 and ((bb == j) & (cls == "gemma")).sum() > 50])), 3)
    out[k] = r; print(k, r["all"], "| human", r["human"]["fires_by_entropy_quartile"], "| gemma", r["gemma"]["fires_by_entropy_quartile"], "| h-g matched", r["human_minus_gemma_within_entropy_decile"], flush=True)
json.dump(out, open(f"{R}/conf.json", "w")); print("CONF_DONE")
