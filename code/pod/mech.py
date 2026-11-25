"""How does Gemma compute 'this was written by an LLM'?   python mech.py   -> mech.json
Texts sit in the model's turn (chat frame); held-out briefs (split half 1). Targets: the other-LLM-vs-human and Gemma-vs-human directions at layers 10, 18, 26.
A component ledger (attention vs MLP by layer)   B transcoder features that write the separation   C position curves   D tokens that move it
E one-property-at-a-time text manipulations     F causal: remove the top features, re-measure the separation and Gemma's judgments."""
import json, os, re, random, collections, numpy as np, torch
import lib
from lib import W
tok, model = lib.load(); NL = lib.NL; random.seed(17); out = {}
D = dict(np.load(f"{W}/dirs.npz")); TARGETS = [(k, T) for k in ("llm_vs_human", "gemma_vs_human") for T in (10, 18, 26)]
unit = {(k, T): torch.tensor(D[k][T] / (np.linalg.norm(D[k][T]) + 1e-9)).cuda() for k, T in TARGETS}
docs = lib.read_jsonl(f"{W}/corpus.jsonl") + lib.read_jsonl(f"{W}/gen.jsonl"); by = collections.defaultdict(dict)
for d in docs:
    if d["set"] == "wp" and d.get("frame", "chat") == "chat" and lib.half_of(d) == 1: by[d["group"]][d["cond"]] = d
gs = [g for g in sorted(by) if all(c in by[g] for c in ("human", "gemma", "claude"))]; random.shuffle(gs); gs = gs[:110]; NT = 256
def ids_of(d, text=None):
    fr = tok(lib.chat_frame(d["prompt"]), add_special_tokens=False).input_ids; tx = tok(d["text"] if text is None else text, add_special_tokens=False).input_ids[:NT]; return fr, tx
lib.load_tc(dec=True)
proj_f = {t: {l: (lib.TC[l]["w_dec"].cuda() @ unit[t]) for l in range(t[1] + 1)} for t in TARGETS}          # each feature's decoder along the direction
cap = {}
hooks = [lib.LAYERS[l].post_attention_layernorm.register_forward_hook(lambda m, i, o, l=l: cap.__setitem__(("att", l), o[0])) for l in range(NL)]
hooks += [lib.LAYERS[l].post_feedforward_layernorm.register_forward_hook(lambda m, i, o, l=l: cap.__setitem__(("mlp", l), o[0])) for l in range(NL)]
hooks += [lib.LAYERS[l].pre_feedforward_layernorm.register_forward_hook(lambda m, i, o, l=l: cap.__setitem__(("x", l), o[0])) for l in range(NL)]
hooks += [lib.LAYERS[l].register_forward_hook(lambda m, i, o, l=l: cap.__setitem__(("res", l), (o[0] if isinstance(o, tuple) else o)[0])) for l in range(NL)]
hooks += [lib.LAYERS[0].register_forward_pre_hook(lambda m, i: cap.__setitem__("emb", i[0][0]))]
CLS = ("human", "gemma", "claude")
comp = {t: {c: dict(att=np.zeros(NL), mlp=np.zeros(NL), emb=0.0, n=0) for c in CLS} for t in TARGETS}
feat = {t: {c: {l: torch.zeros(16384, device="cuda") for l in range(t[1] + 1)} for c in CLS} for t in TARGETS}
recon = {t: {c: np.zeros(NL) for c in CLS} for t in TARGETS}
pos = {t: {c: np.zeros(NT) for c in CLS} for t in TARGETS}; posn = {c: np.zeros(NT) for c in CLS}; docproj = {t: {c: [] for c in CLS} for t in TARGETS}; prefix = {t: {c: {n: [] for n in (8, 16, 32, 64, 128, 256)} for c in CLS} for t in TARGETS}
tokw = {c: collections.defaultdict(lambda: [0.0, 0]) for c in CLS}; TW = ("llm_vs_human", 18)
for gi, g in enumerate(gs):
    for c in CLS:
        fr, tx = ids_of(by[g][c]); ids = torch.tensor([fr + tx]).cuda(); s = len(fr); n = len(tx)
        with torch.no_grad(): lib.BASE(input_ids=ids)
        for t in TARGETS:
            u = unit[t].float(); T = t[1]; z = comp[t][c]
            for l in range(T + 1):
                a = cap[("att", l)][s:].float() @ u; m = cap[("mlp", l)][s:].float() @ u; z["att"][l] += float(a.sum()); z["mlp"][l] += float(m.sum())
                acts = lib.tc_acts(l, cap[("x", l)][s:]); feat[t][c][l] += acts.sum(0) * proj_f[t][l]; recon[t][c][l] += float(((acts @ lib.TC[l]["w_dec"].cuda() + lib.TC[l]["b_dec"].cuda()) @ u).sum())
            z["emb"] += float((cap["emb"][s:].float() @ u).sum()); z["n"] += n
            r = cap[("res", T)][s:].float().clone(); r[:, lib.MASSIVE] = 0; p = (r @ u).cpu().numpy(); pos[t][c][:n] += p; docproj[t][c].append(float(p.mean()))
            for k in prefix[t][c]: prefix[t][c][k].append(float(p[:k].mean()))
        posn[c][:n] += 1
        u = unit[TW].float(); wr = sum((cap[("att", l)][s:].float() @ u) + (cap[("mlp", l)][s:].float() @ u) for l in range(TW[1] + 1)).cpu().numpy()        # what was written at this token
        for k, tid in enumerate(tx): e = tokw[c][tid]; e[0] += float(wr[k]); e[1] += 1
    if gi % 20 == 0: print("pass", gi, len(gs), flush=True)
def auc(a, b):
    a, b = np.array(a), np.array(b); return round(float((a[:, None] > b[None, :]).mean() + 0.5 * (a[:, None] == b[None, :]).mean()), 3)
for t in TARGETS:
    key = f"{t[0]}@L{t[1]}"; z = comp[t]; gap = {}
    for c in ("gemma", "claude"):
        ga = z[c]["att"] / z[c]["n"] - z["human"]["att"] / z["human"]["n"]; gm = z[c]["mlp"] / z[c]["n"] - z["human"]["mlp"] / z["human"]["n"]; ge = z[c]["emb"] / z[c]["n"] - z["human"]["emb"] / z["human"]["n"]
        rc = recon[t][c] / z[c]["n"] - recon[t]["human"] / z["human"]["n"]; tot = ga[:t[1] + 1].sum() + gm[:t[1] + 1].sum() + ge
        fl = []
        for l in range(t[1] + 1):
            dv = (feat[t][c][l] / z[c]["n"] - feat[t]["human"][l] / z["human"]["n"]).cpu().numpy()
            for f in np.argsort(-np.abs(dv))[:60]: fl.append((float(dv[f]), l, int(f)))
        fl.sort(key=lambda x: -abs(x[0])); top = fl[:120]
        gap[c] = dict(total_gap=round(float(tot), 3), embedding=round(float(ge), 3), attention_by_layer=[round(float(x), 3) for x in ga[:t[1] + 1]], mlp_by_layer=[round(float(x), 3) for x in gm[:t[1] + 1]], attention_share=round(float(ga[:t[1] + 1].sum() / tot), 3), mlp_share=round(float(gm[:t[1] + 1].sum() / tot), 3),
                      mlp_gap_reconstructed_by_transcoders=round(float(rc[:t[1] + 1].sum() / (gm[:t[1] + 1].sum() + 1e-9)), 3), top_features=[dict(key=f"L{l}.{f}", contrib=round(v, 4), top=[tok.decode([int(x)]) for x in (lib.TC[l]["w_dec"][f].cuda() @ lib.LM.weight.float().T).topk(6).indices]) for v, l, f in top[:60]],
                      top_feature_keys=[f"L{l}.{f}" for v, l, f in top if v > 0], share_of_gap_in_top={k: round(float(sum(v for v, _, _ in top[:k]) / tot), 3) for k in (10, 30, 60, 120)},
                      auc_doc=auc(docproj[t][c], docproj[t]["human"]), auc_by_prefix={k: auc(prefix[t][c][k], prefix[t]["human"][k]) for k in prefix[t][c]},
                      position_curve=[round(float(x), 2) for x in (pos[t][c] / np.maximum(posn[c], 1) - pos[t]["human"] / np.maximum(posn["human"], 1)).reshape(32, 8).mean(1)])
        print(key, c, "gap", gap[c]["total_gap"], "att share", gap[c]["attention_share"], "mlp share", gap[c]["mlp_share"], "tc recon", gap[c]["mlp_gap_reconstructed_by_transcoders"], "top-k share", gap[c]["share_of_gap_in_top"], "auc by prefix", gap[c]["auc_by_prefix"], flush=True)
    out[key] = gap
allw = collections.defaultdict(lambda: [0.0, 0])
for c in CLS:
    for tid, (sv, n) in tokw[c].items(): allw[tid][0] += sv; allw[tid][1] += n
tl = sorted(((sv / n, n, tid) for tid, (sv, n) in allw.items() if n >= 25), key=lambda x: -x[0]); base_w = sum(sv for sv, n in allw.values()) / sum(n for sv, n in allw.values())
out["tokens"] = dict(mean_write=round(base_w, 3), toward_llm=[[tok.decode([t]), round(v - base_w, 2), n] for v, n, t in tl[:45]], toward_human=[[tok.decode([t]), round(v - base_w, 2), n] for v, n, t in tl[-45:][::-1]])
print("tokens toward LLM:", [x[0] for x in out["tokens"]["toward_llm"][:25]], "\n       toward human:", [x[0] for x in out["tokens"]["toward_human"][:25]], flush=True); json.dump(out, open(f"{W}/mech.json", "w"))
# ---- E. manipulations
def typo(t): return re.sub(r" {2,}", " ", t.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'").replace("—", " - ").replace("–", " - ").replace("…", "...").replace("*", ""))
def sents(t): return [s for s in re.split(r"(?<=[.!?…])[\"”’']?\s+", t.replace("\n", " ")) if s.strip()]
def shuf_s(t): s = sents(t); random.shuffle(s); return " ".join(s)
def shuf_w(t):
    o = []
    for s in sents(t): w = s.split(); random.shuffle(w); o.append(" ".join(w))
    return " ".join(o)
MAN = {"original": lambda t: t, "typography normalised": typo, "typography normalised, lowercased": lambda t: typo(t).lower(), "one paragraph (no line breaks)": lambda t: re.sub(r"\s*\n+\s*", " ", t), "sentences shuffled": shuf_s,
       "words shuffled within sentences": shuf_w, "punctuation removed": lambda t: re.sub(r"[^\w\s]", "", typo(t))}
F1 = [(33, 1074), (33, 56)]; TE = [("llm_vs_human", 18), ("gemma_vs_human", 18), ("llm_vs_human", 26)]; E = {}
for name, fn in MAN.items():
    r = {t: {c: [] for c in CLS} for t in TE}; fr_ = {c: [0.0, 0.0, 0] for c in CLS}; nl = {c: [0.0, 0] for c in CLS}
    for g in gs[:70]:
        for c in CLS:
            fr, tx = ids_of(by[g][c], fn(" ".join(by[g][c]["text"].split(" ")[:230]) if name != "one paragraph (no line breaks)" else by[g][c]["text"][:1500])); ids = torch.tensor([fr + tx]).cuda(); s = len(fr)
            with torch.no_grad(): h = lib.BASE(input_ids=ids).last_hidden_state[0]; lp = lib.LM(h[s - 1:-1]).float().log_softmax(-1).gather(1, ids[0, s:, None])
            nl[c][0] += float(-lp.sum()); nl[c][1] += lp.numel()
            for t in TE: x = cap[("res", t[1])][s:].float().clone(); x[:, lib.MASSIVE] = 0; r[t][c].append(float((x @ unit[t].float()).mean()))
            a = lib.tc_acts(33, cap[("x", 33)][s:]); fr_[c][0] += float((a[:, 1074] > 0).sum()); fr_[c][1] += float((a[:, 56] > 0).sum()); fr_[c][2] += len(tx)
    E[name] = dict(raw={f"{t[0]}@L{t[1]}": {c: float(np.mean(v)) for c, v in r[t].items()} for t in TE}, auc={f"{t[0]}@L{t[1]}": {c: auc(r[t][c], r[t]["human"]) for c in ("gemma", "claude")} for t in TE},
                   L33_1074={c: round(v[0] / v[2], 3) for c, v in fr_.items()}, L33_56={c: round(v[1] / v[2], 3) for c, v in fr_.items()}, nats={c: round(v[0] / v[1], 2) for c, v in nl.items()})
o = E["original"]["raw"]
for name in E:
    E[name]["position_on_axis"] = {k: {c: round((E[name]["raw"][k][c] - o[k]["human"]) / (o[k]["gemma" if "gemma" in k else "claude"] - o[k]["human"] + 1e-9), 2) for c in CLS} for k in o}       # 0 = original human text, 1 = original LLM text
    print("E %-36s" % name, E[name]["position_on_axis"]["llm_vs_human@L18"], "auc", E[name]["auc"]["llm_vs_human@L18"], "| L33.1074", E[name]["L33_1074"], "| nats", E[name]["nats"], flush=True)
out["manipulations"] = E; json.dump(out, open(f"{W}/mech.json", "w"))
# ---- F. causal: remove the features that write the separation
for h in hooks: h.remove()
tids = lambda ws: sorted({tok(w, add_special_tokens=False).input_ids[0] for w in ws}); TH, TA = tids(["human", "Human", " human"]), tids(["AI", " AI", "ai"]); DIG = [tids([str(i)])[0] for i in range(1, 10)]
def cut(t, n=200):
    w = t.split(" "); s = " ".join(w[:n]); m = list(re.finditer(r"[.!?][\"”’']?(?=\s|$)", s)); return (s[:m[-1].end()] if m and m[-1].end() > len(s) * 0.6 else s).strip()
RATE = "Rate the quality of the writing in this passage from 1 (poor) to 9 (excellent). Answer with a single digit.\n\n{t}"; DET = "Was this passage written by a human or by an AI? Answer with one word, human or AI.\n\n{t}"
def install(keys):
    hk = []; kb = collections.defaultdict(list)
    for k in keys: l, f = k[1:].split("."); kb[int(l)].append(int(f))
    for l, fs in kb.items():
        t = lib.TC[l]; w, b, thr, dec = t["w_enc"][:, fs], t["b_enc"][fs], t["threshold"][fs], t["w_dec"][fs].cuda(); st = {}
        hk.append(lib.LAYERS[l].pre_feedforward_layernorm.register_forward_hook(lambda m, i, o, st=st: st.__setitem__("x", o)))
        def edit(m, i, o, st=st, w=w, b=b, thr=thr, dec=dec):
            a = (st["x"].to(torch.bfloat16) @ w).float() + b; a = a * (a > thr); return o - (a @ dec).to(o.dtype)
        hk.append(lib.LAYERS[l].post_feedforward_layernorm.register_forward_hook(edit))
    return hk
def measure():
    r = {}; rc = {}
    hk = [lib.LAYERS[l].register_forward_hook(lambda m, i, o, l=l: rc.__setitem__(l, (o[0] if isinstance(o, tuple) else o)[0])) for l in (18, 26)]; pr = {(k, T): {c: [] for c in CLS} for k in ("llm_vs_human", "gemma_vs_human") for T in (18, 26)}
    for g in gs[:50]:
        for c in CLS:
            fr, tx = ids_of(by[g][c]); ids = torch.tensor([fr + tx[:160]]).cuda()
            with torch.no_grad(): lib.BASE(input_ids=ids)
            for t in pr: x = rc[t[1]][len(fr):].float().clone(); x[:, lib.MASSIVE] = 0; pr[t][c].append(float((x @ unit[t].float()).mean()))
    for h in hk: h.remove()
    for t in pr:
        for c in ("gemma", "claude"): r[f"auc {c} vs human, {t[0]}@L{t[1]}"] = auc(pr[t][c], pr[t]["human"]); r[f"gap {c}, {t[0]}@L{t[1]}"] = round(float(np.mean(pr[t][c]) - np.mean(pr[t]["human"])), 2)
    tok.padding_side = "right"
    for c in CLS:
        for nm, tm in (("rating", RATE), ("says_ai", DET)):
            vals = []
            for s in range(0, 40, 20):
                e = tok([lib.chat_frame(tm.format(t=cut(by[g][c]["text"]))) for g in gs[s:s + 20]], add_special_tokens=False, return_tensors="pt", padding=True); last = (e.attention_mask.sum(1) - 1).cuda()
                with torch.no_grad(): lp = lib.LM(lib.BASE(input_ids=e.input_ids.cuda(), attention_mask=e.attention_mask.cuda()).last_hidden_state[torch.arange(len(last), device="cuda"), last]).float().log_softmax(-1).cpu()
                if nm == "rating": p = lp[:, DIG].exp(); vals += ((p * torch.arange(1, 10)).sum(1) / p.sum(1)).tolist()
                else: a, h = lp[:, TA].exp().sum(1), lp[:, TH].exp().sum(1); vals += (a / (a + h)).tolist()
            r[f"{nm}/{c}"] = round(float(np.mean(vals)), 3)
    return r
C = {"no ablation": measure()}; print("F no ablation", C["no ablation"], flush=True)
top_l = out["llm_vs_human@L18"]["claude"]["top_feature_keys"]; top_g = out["gemma_vs_human@L18"]["gemma"]["top_feature_keys"]; allk = [f"L{l}.{f}" for l in range(19) for f in range(0, 16384, 97)]
for label, keys in (("top 20 features writing the other-LLM separation", top_l[:20]), ("top 60", top_l[:60]), ("top 60 writing the Gemma separation", top_g[:60]), ("both lists, top 60 each", list(dict.fromkeys(top_l[:60] + top_g[:60]))),
                    ("60 random features, layers 0-18", random.sample(allk, 60))):
    hk = install(keys); C[label] = measure(); [h.remove() for h in hk]; print("F", label, C[label], flush=True); out["causal"] = C; json.dump(out, open(f"{W}/mech.json", "w"))
print("MECH_DONE")
