"""Which attention heads write the 'LLM-written' signal, and which source tokens do they read?   ATTN=eager python heads.py -> heads.json
For layers 15-18, 20 and 26: each head's share of the human-vs-LLM gap, where it looks, the source tokens that carry the most evidence each way,
and what happens to the separation and to Gemma's judgments when the top heads are switched off."""
import json, os, re, random, collections, numpy as np, torch
import lib
from lib import W
tok, model = lib.load(); NL = lib.NL; random.seed(23); out = {}; torch.set_grad_enabled(False)
D = dict(np.load(f"{W}/dirs.npz")); LAY = {15: 18, 16: 18, 17: 18, 18: 18, 20: 26, 26: 26}; KEY = "llm_vs_human"
unit = {T: torch.tensor(D[KEY][T] / (np.linalg.norm(D[KEY][T]) + 1e-9)).cuda().float() for T in (18, 26)}
att0 = lib.LAYERS[0].self_attn; NH = model.config.text_config.num_attention_heads if hasattr(model.config, "text_config") else model.config.num_attention_heads; HD = att0.o_proj.in_features // NH
docs = lib.read_jsonl(f"{W}/corpus.jsonl") + lib.read_jsonl(f"{W}/gen.jsonl"); by = collections.defaultdict(dict)
for d in docs:
    if d["set"] == "wp" and d.get("frame", "chat") == "chat" and lib.half_of(d) == 1: by[d["group"]][d["cond"]] = d
gs = [g for g in sorted(by) if all(c in by[g] for c in ("human", "gemma", "claude"))]; random.shuffle(gs); gs = gs[:80]; NT = 192; CLS = ("human", "gemma", "claude")
cap = {}; hooks = []
for l in LAY:
    A = lib.LAYERS[l].self_attn
    hooks.append(A.o_proj.register_forward_pre_hook(lambda m, i, l=l: cap.__setitem__(("z", l), i[0][0])))
    hooks.append(A.o_proj.register_forward_hook(lambda m, i, o, l=l: cap.__setitem__(("o", l), o[0])))
    hooks.append(A.v_proj.register_forward_hook(lambda m, i, o, l=l: cap.__setitem__(("v", l), o[0])))
gam = {l: (1 + lib.LAYERS[l].post_attention_layernorm.weight.float()) for l in LAY}
WO = {l: lib.LAYERS[l].self_attn.o_proj.weight.float() for l in LAY}                                   # [2560, NH*HD]
dvec = {l: (unit[LAY[l]] * gam[l]) @ WO[l] for l in LAY}                                                # direction pulled back through the norm gain and o_proj: [NH*HD]
gap = {l: {c: np.zeros(NH) for c in CLS} for l in LAY}; n_tok = {c: 0 for c in CLS}
look = {l: {c: np.zeros((NH, 4)) for c in CLS} for l in LAY}                                            # attention mass to: start token, prompt, earlier text, itself
ev = {l: [collections.defaultdict(lambda: [0.0, 0]) for _ in range(NH)] for l in LAY}; chk = []
for gi, g in enumerate(gs):
    for c in CLS:
        d = by[g][c]; fr = tok(lib.chat_frame(d["prompt"]), add_special_tokens=False).input_ids; tx = tok(d["text"], add_special_tokens=False).input_ids[:NT]; ids = torch.tensor([fr + tx]).cuda(); s = len(fr); T = len(fr) + len(tx)
        with torch.no_grad(): o = lib.BASE(input_ids=ids, output_attentions=True)
        for l in LAY:
            z = cap[("z", l)].float(); rms = (cap[("o", l)].float().pow(2).mean(-1) + 1e-6).sqrt()                                  # [T]
            ph = (z.view(T, NH, HD) * dvec[l].view(NH, HD)).sum(-1) / rms[:, None]                                             # each head's write along the direction, per position
            gap[l][c] += ph[s:].sum(0).cpu().numpy()
            A = o.attentions[l][0].float()                                                                                       # [NH, T, T]
            At = A[:, s:, :]; look[l][c] += torch.stack([At[:, :, 0].sum(1), At[:, :, 1:s].sum((1, 2)), torch.stack([torch.tril(At[h, :, s:], -1).sum() for h in range(NH)]), torch.stack([At[h, :, s:].diagonal().sum() for h in range(NH)])], 1).cpu().numpy()
            vv = cap[("v", l)].float(); NKV = vv.shape[-1] // HD; e = (vv.view(T, NKV, HD).repeat_interleave(NH // NKV, dim=1) * dvec[l].view(NH, HD)).sum(-1)      # grouped-query attention: query heads share value heads                                          # evidence value of each source position, per head  [T, NH]
            contrib = (At / rms[s:][None, :, None]) * e.T[:, None, :]                                                            # [NH, dest, src]
            if gi == 0 and c == "human": chk.append((l, float((contrib.sum(-1).T - ph[s:]).abs().max() / (ph[s:].abs().max() + 1e-9))))
            src = contrib[:, :, s:].sum(1).cpu().numpy()                                                                         # evidence delivered from each text source position, summed over readers
            for h in range(NH):
                for k, tid in enumerate(tx): x = ev[l][h][tid]; x[0] += float(src[h, k]); x[1] += 1
        n_tok[c] += len(tx)
    if gi % 20 == 0: print("pass", gi, len(gs), "sum check", chk, flush=True)
for h in hooks: h.remove()
heads = []
for l in LAY:
    for h in range(NH):
        gh = {c: gap[l][c][h] / n_tok[c] for c in CLS}; lk = sum(look[l][c][h] for c in CLS); lk = lk / lk.sum()
        items = sorted(((sv / n, n, t) for t, (sv, n) in ev[l][h].items() if n >= 25), key=lambda x: -x[0]); mean = sum(sv for sv, n in ev[l][h].values()) / max(1, sum(n for sv, n in ev[l][h].values()))
        heads.append(dict(head=f"L{l}.H{h}", target_layer=LAY[l], gap_claude=round(float(gh["claude"] - gh["human"]), 2), gap_gemma=round(float(gh["gemma"] - gh["human"]), 2), looks_at=dict(start_token=round(float(lk[0]), 3), prompt=round(float(lk[1]), 3), earlier_text=round(float(lk[2]), 3), itself=round(float(lk[3]), 3)),
                          reads_as_llm=[[tok.decode([t]), round(v - mean, 2), n] for v, n, t in items[:25]], reads_as_human=[[tok.decode([t]), round(v - mean, 2), n] for v, n, t in items[-25:][::-1]]))
heads.sort(key=lambda x: -(x["gap_claude"] + x["gap_gemma"])); out["heads"] = heads
for x in heads[:10]: print(x["head"], "gap claude/gemma", x["gap_claude"], x["gap_gemma"], x["looks_at"], "| LLM:", [t[0] for t in x["reads_as_llm"][:10]], "| human:", [t[0] for t in x["reads_as_human"][:10]], flush=True)
json.dump(out, open(f"{W}/heads.json", "w"))
# ---- switch the top heads off
tids = lambda ws: sorted({tok(w, add_special_tokens=False).input_ids[0] for w in ws}); TH, TA = tids(["human", "Human", " human"]), tids(["AI", " AI", "ai"]); DIG = [tids([str(i)])[0] for i in range(1, 10)]
def cut(t, n=200):
    w = t.split(" "); s = " ".join(w[:n]); m = list(re.finditer(r"[.!?][\"”’']?(?=\s|$)", s)); return (s[:m[-1].end()] if m and m[-1].end() > len(s) * 0.6 else s).strip()
RATE = "Rate the quality of the writing in this passage from 1 (poor) to 9 (excellent). Answer with a single digit.\n\n{t}"; DET = "Was this passage written by a human or by an AI? Answer with one word, human or AI.\n\n{t}"
def auc(a, b): a, b = np.array(a), np.array(b); return round(float((a[:, None] > b[None, :]).mean()), 3)
def install(hs):
    hk = []; kb = collections.defaultdict(list)
    for x in hs: l, h = x[1:].split(".H"); kb[int(l)].append(int(h))
    for l, hh in kb.items():
        def pre(m, i, hh=hh):
            z = i[0].clone()
            for h in hh: z[..., h * HD:(h + 1) * HD] = 0
            return (z,)
        hk.append(lib.LAYERS[l].self_attn.o_proj.register_forward_pre_hook(pre))
    return hk
def measure():
    r = {}; rc = {}; hk = [lib.LAYERS[l].register_forward_hook(lambda m, i, o, l=l: rc.__setitem__(l, (o[0] if isinstance(o, tuple) else o)[0])) for l in (18, 26)]; pr = {T: {c: [] for c in CLS} for T in (18, 26)}
    for g in gs[:50]:
        for c in CLS:
            d = by[g][c]; fr = tok(lib.chat_frame(d["prompt"]), add_special_tokens=False).input_ids; ids = torch.tensor([fr + tok(d["text"], add_special_tokens=False).input_ids[:160]]).cuda()
            with torch.no_grad(): lib.BASE(input_ids=ids)
            for T in pr: x = rc[T][len(fr):].float().clone(); x[:, lib.MASSIVE] = 0; pr[T][c].append(float((x @ unit[T]).mean()))
    for h in hk: h.remove()
    for T in pr:
        for c in ("gemma", "claude"): r[f"auc {c} vs human @L{T}"] = auc(pr[T][c], pr[T]["human"]); r[f"gap {c} @L{T}"] = round(float(np.mean(pr[T][c]) - np.mean(pr[T]["human"])), 1)
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
C = {"all heads on": measure()}; print("OFF none", C["all heads on"], flush=True); top = [x["head"] for x in heads]; allh = [f"L{l}.H{h}" for l in LAY for h in range(NH)]
for label, hs in (("top 1 head off", top[:1]), ("top 3 heads off", top[:3]), ("top 6 heads off", top[:6]), ("6 random heads from the same layers off", random.sample([x for x in allh if x not in top[:6]], 6))):
    hk = install(hs); C[label] = dict(heads=hs, **measure()); [h.remove() for h in hk]; print("OFF", label, hs, C[label], flush=True); out["switch_off"] = C; json.dump(out, open(f"{W}/heads.json", "w"))
print("HEADS_DONE")
