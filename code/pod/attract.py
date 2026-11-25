"""Why this token? For sets of (context, target token) decision points: the baseline choice, a logit lens by layer,
the transcoder features that write most toward the target (activation x decoder . unembedding), and what happens to
the choice when the top features are removed, against random features in the same layers.
    python attract.py sets.json out.json
sets.json: [{"name", "target": " rain", "contrast": [" air", ...] | null, "items": [{"prompt", "prefix"}]}]
"""
import sys, json, os, time, random, collections, torch
import lib
from lib import W
tok, model = lib.load(); lib.load_tc(dec=True)
NL, F = lib.NL, 16384; U = lib.LM.weight.float(); Uc = U - U.mean(0, keepdim=True)
sets = json.load(open(sys.argv[1])); out = json.load(open(sys.argv[2])) if os.path.exists(sys.argv[2]) else {}; random.seed(0)
def tid(s):
    i = tok(s, add_special_tokens=False).input_ids; return i[0]
def run(items, pos_ids, target, ablate=None, capture=False):
    """Forward all items; returns final log-probs at the decision position [n, V] (cpu half), and optionally MLP inputs / residuals there."""
    cap = {"x": torch.zeros(len(items), NL, lib.D), "r": torch.zeros(len(items), NL, lib.D)} if capture else None
    lps = []; BS = max(2, min(24, 9000 // max(map(len, pos_ids))))
    for s in range(0, len(items), BS):
        b = pos_ids[s:s + BS]; L = max(map(len, b)); ids = torch.full((len(b), L), tok.pad_token_id, dtype=torch.long); att = torch.zeros((len(b), L), dtype=torch.long)
        for k, e in enumerate(b): ids[k, :len(e)] = torch.tensor(e); att[k, :len(e)] = 1
        last = torch.tensor([len(e) - 1 for e in b], device="cuda"); ar = torch.arange(len(b), device="cuda"); hooks = []
        if capture:
            for l in range(NL):
                hooks.append(lib.LAYERS[l].pre_feedforward_layernorm.register_forward_hook(lambda m, i, o, l=l, s=s: cap["x"].__setitem__((slice(s, s + len(b)), l), o[ar, last].float().cpu())))
                hooks.append(lib.LAYERS[l].register_forward_hook(lambda m, i, o, l=l, s=s: cap["r"].__setitem__((slice(s, s + len(b)), l), (o[0] if isinstance(o, tuple) else o)[ar, last].float().cpu())))
        for l, fs in (ablate or {}).items():
            t = lib.TC[l]; w, bb, thr, dec = t["w_enc"][:, fs], t["b_enc"][fs], t["threshold"][fs], t["w_dec"][fs].to("cuda"); st = {}
            hooks.append(lib.LAYERS[l].pre_feedforward_layernorm.register_forward_hook(lambda m, i, o, st=st: st.__setitem__("x", o)))
            def edit(m, i, o, st=st, w=w, bb=bb, thr=thr, dec=dec):
                a = (st["x"].to(torch.bfloat16) @ w).float() + bb; a = a * (a > thr); return o - (a @ dec).to(o.dtype)
            hooks.append(lib.LAYERS[l].post_feedforward_layernorm.register_forward_hook(edit))
        with torch.no_grad():
            h = lib.BASE(input_ids=ids.cuda(), attention_mask=att.cuda()).last_hidden_state[ar, last]
            lps.append(lib.LM(h).float().log_softmax(-1).cpu())
        for hk in hooks: hk.remove()
    return torch.cat(lps), cap
def summ(lp, t, k=10):
    p = lp.exp(); top = p.mean(0).topk(k)
    return dict(p_target=round(float(p[:, t].mean()), 4), top1_is_target=round(float((lp.argmax(1) == t).float().mean()), 4),
                entropy=round(float(-(p * lp).sum(1).mean()), 3), top=[[tok.decode([int(i)]), round(float(v), 4)] for v, i in zip(top.values, top.indices)])
for S in sets:
    if S["name"] in out: continue
    t0 = time.time(); items = S["items"]; t = tid(S["target"])
    ids = [tok(lib.chat_frame(it["prompt"]) if it.get("prompt") else tok.bos_token, add_special_tokens=False).input_ids + (tok(it["prefix"], add_special_tokens=False).input_ids if it.get("prefix") else []) for it in items]
    lp, cap = run(items, ids, t, capture=True); res = dict(n=len(items), target=S["target"], base=summ(lp, t))
    d = Uc[t] if not S.get("contrast") else U[t] - U[[tid(c) for c in S["contrast"]]].mean(0)
    with torch.no_grad():
        res["lens"] = [round(float(lib.LM(lib.FNORM(cap["r"][:, l].to("cuda", torch.bfloat16))).float().log_softmax(-1)[:, t].exp().mean()), 4) for l in range(NL)]
        attr = torch.zeros(NL, F); freq = torch.zeros(NL, F)
        for l in range(NL):
            a = lib.tc_acts(l, cap["x"][:, l].cuda()); proj = lib.TC[l]["w_dec"].cuda() @ d
            attr[l] = (a * proj).mean(0).cpu(); freq[l] = (a > 0).float().mean(0).cpu()
    order = attr.flatten().argsort(descending=True); feats = []
    for j in order[:80].tolist():
        l, f = divmod(j, F); tops = (lib.TC[l]["w_dec"][f].cuda() @ U.T).topk(8).indices
        feats.append(dict(key=f"L{l}.{f}", attr=round(float(attr[l, f]), 3), freq=round(float(freq[l, f]), 3), top=[tok.decode([int(x)]) for x in tops]))
    res["features"] = feats; res["attr_total_pos"] = round(float(attr.clamp(min=0).sum()), 2); res["attr_by_layer"] = [round(float(x), 3) for x in attr.clamp(min=0).sum(1)]
    res["ablate"] = {}
    for n in (5, 20, 60, 200):
        ab = collections.defaultdict(list)
        for j in order[:n].tolist(): l, f = divmod(j, F); ab[l].append(f)
        lp2, _ = run(items, ids, t, ablate=ab); r = summ(lp2, t)
        rnd = []
        for rep in range(3):
            rb = {l: random.sample([f for f in freq[l].nonzero().flatten().tolist()] or list(range(F)), len(fs)) for l, fs in ab.items()}   # random features that fire here, same layers
            rnd.append(summ(run(items, ids, t, ablate=rb)[0], t)["p_target"])
        r["random_p_target"] = rnd; res["ablate"][n] = r
    out[S["name"]] = res; json.dump(out, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
    print(S["name"], res["n"], "base", res["base"]["p_target"], res["base"]["top"][:5], "| ablate", {n: (v["p_target"], v["random_p_target"]) for n, v in res["ablate"].items()}, "| top feats", [(x["key"], x["attr"], x["top"][:3]) for x in feats[:6]], f"{time.time() - t0:.0f}s", flush=True)
print("ATTRACT_DONE")
