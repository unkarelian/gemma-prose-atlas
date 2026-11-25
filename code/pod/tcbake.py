"""Transcoder-guided weight ablation: remove chosen transcoder features from a model by editing MLP output weights.

A feature f at layer l contributes  a_f(x) * d_f  to the layer's write (the output of post_feedforward_layernorm), where a_f is the
transcoder activation and d_f its decoder row. Gemma writes  y = m / rms(m) * (1 + gamma)  with  m = n @ W_down.T  and n the MLP's hidden
neurons (10,240 per layer). To remove the feature inside the weights we need the weights themselves to compute a_f:

    1. ridge-regress  e_f = a_f * rms(m)  on the hidden neurons n over a text sample   ->  g_f  (one vector over neurons per feature)
    2. edit           W_down  <-  W_down - sum_f  (d_f / (1 + gamma)) (outer) g_f                (rank one per feature)

so that  m' = m - sum_f (n . g_f) d_f / (1 + gamma)  and  y' ~ y - sum_f a_f d_f.  Tokens where the feature is silent have target 0, so the
fit keeps the edit inactive there. Variants for comparison: `project` removes the decoder directions from everything the MLP writes
(the abliteration-style baseline); `exact` is the run-time ablation with the transcoder itself (the reference).

    python tcbake.py fit NAME features.json [--lam 1e-3]     -> bake_NAME.pt   (also bake_NAME_random.pt, a control with random features)
    import tcbake; tcbake.apply(path, mode="bake" | "project" | "exact")       -> installs the edit in the loaded model
"""
import sys, json, os, random, collections, torch, torch.nn as nn
import lib
from lib import W
F = 16384


class Edited(nn.Module):
    """down_proj with a low-rank correction kept in float32 (bfloat16 weights cannot hold the edit); identical to editing the weight matrix."""
    def __init__(self, lin, G, Dm, mode):
        super().__init__(); self.lin, self.mode = lin, mode
        self.G = nn.Parameter(G.float(), requires_grad=False); self.Dm = nn.Parameter(Dm.float(), requires_grad=False)        # G [10240, k], Dm [k, 2560] = d / (1 + gamma)
        if mode == "project": self.Q = nn.Parameter(torch.linalg.qr(Dm.float().T)[0], requires_grad=False)                   # orthonormal basis of the directions, in m-space
    def forward(self, n):
        m = self.lin(n)
        if self.mode == "bake": return m - ((n.float() @ self.G) @ self.Dm).to(m.dtype)
        mf = m.float(); return (mf - (mf @ self.Q) @ self.Q.T).to(m.dtype)
    def merged_weight(self):
        return self.lin.weight.float() - (self.G @ self.Dm).T


def gamma(l): return lib.LAYERS[l].post_feedforward_layernorm.weight.float()
def apply(path, mode="bake", scale=1.0):
    B = torch.load(path); hooks = []
    for l, b in B["layers"].items():
        L = lib.LAYERS[l]
        if mode == "exact":
            t = b; st = {}
            hooks.append(L.pre_feedforward_layernorm.register_forward_hook(lambda m, i, o, st=st: st.__setitem__("x", o)))
            def edit(m, i, o, st=st, t=t):
                a = (st["x"].to(torch.bfloat16) @ t["w_enc"].cuda().to(torch.bfloat16)).float() + t["b_enc"].cuda(); a = a * (a > t["thr"].cuda()); return o - scale * (a @ t["w_dec"].cuda()).to(o.dtype)
            hooks.append(L.post_feedforward_layernorm.register_forward_hook(edit))
        else:
            Dm = (b["w_dec"].cuda() / (1 + gamma(l))[None]) * scale; L.mlp.down_proj = Edited(L.mlp.down_proj, b["G"].cuda(), Dm, mode)
    return B, hooks


def texts(n_each=260):
    docs = lib.read_jsonl(f"{W}/corpus.jsonl") + lib.read_jsonl(f"{W}/gen.jsonl"); random.seed(5); out = []
    for cond, k in (("gemma", n_each), ("human", n_each), ("claude", n_each // 2), ("gemma_plain", 80), ("gemma_lit", 80)):
        ds = [d for d in docs if d["set"] == "wp" and d["cond"] == cond and d.get("frame", "chat") == "chat"]; random.shuffle(ds); out += ds[:k]
    ds = [d for d in docs if d["set"] == "books" and d["cond"] in ("gemma", "human")]; random.shuffle(ds); out += ds[:160]
    try: out += [dict(prompt=r["human"], text=r["gemma"]) for r in lib.read_jsonl(f"{W}/a2a/requests.jsonl")][:200]
    except Exception: pass
    random.shuffle(out); return out


def batches(ds, tok, budget=9000, maxtext=256):
    enc = [tok(lib.chat_frame(d["prompt"]), add_special_tokens=False).input_ids[-500:] + tok(d["text"], add_special_tokens=False).input_ids[:maxtext] for d in ds]
    enc = [([tok.bos_token_id] + e if e[0] != tok.bos_token_id else e) for e in enc]; enc.sort(key=len, reverse=True); i = 0
    while i < len(enc):
        L = len(enc[i]); B = max(1, min(budget // L, 24)); b = enc[i:i + B]; i += B
        ids = torch.full((len(b), L), tok.pad_token_id, dtype=torch.long); att = torch.zeros((len(b), L), dtype=torch.bool)
        for k, e in enumerate(b): ids[k, :len(e)] = torch.tensor(e); att[k, 1:len(e)] = True          # position 0 (the start token) is left out of the fit
        yield ids.cuda(), att.cuda()


if __name__ == "__main__" and sys.argv[1] == "fit":
    name = sys.argv[2]; keys = json.load(open(sys.argv[3])); lam = float(sys.argv[sys.argv.index("--lam") + 1]) if "--lam" in sys.argv else 1e-3
    tok, model = lib.load(); by = collections.defaultdict(list)
    for k in keys: l, f = k[1:].split("."); by[int(l)].append(int(f))
    random.seed(1); rnd = {l: random.sample(range(F), len(fs)) for l, fs in by.items()}                     # control: the same number of random features per layer
    lib.load_tc(sorted(by), dec=True); ds = texts(); fit, held = ds[len(ds) // 8:], ds[:len(ds) // 8]
    H = lib.LAYERS[0].mlp.down_proj.in_features; S = {l: dict(NtN=torch.zeros(H, H, device="cuda"), NtE=torch.zeros(H, 2 * len(fs), device="cuda"), n=0) for l, fs in by.items()}
    cap = {}; hooks = []
    for l in by:
        hooks.append(lib.LAYERS[l].pre_feedforward_layernorm.register_forward_hook(lambda m, i, o, l=l: cap.__setitem__(("x", l), o)))
        hooks.append(lib.LAYERS[l].mlp.down_proj.register_forward_hook(lambda m, i, o, l=l: (cap.__setitem__(("n", l), i[0]), cap.__setitem__(("m", l), o))[0] and None))
    def acts(l, x, fs):
        t = lib.TC[l]; a = (x.to(torch.bfloat16) @ t["w_enc"][:, fs]).float() + t["b_enc"][fs]; return a * (a > t["threshold"][fs])
    def targets(l, att):
        x, n, m = cap[("x", l)][att], cap[("n", l)][att].float(), cap[("m", l)][att].float(); rms = (m.pow(2).mean(-1, keepdim=True) + 1e-6).sqrt()
        return n, torch.cat([acts(l, x, by[l]), acts(l, x, rnd[l])], 1) * rms, rms
    ntok = 0
    for ids, att in batches(fit, tok):
        with torch.no_grad():
            lib.BASE(input_ids=ids, attention_mask=(ids != tok.pad_token_id))
            for l in by: n, E, _ = targets(l, att); S[l]["NtN"] += n.T @ n; S[l]["NtE"] += n.T @ E; S[l]["n"] += len(n)
        ntok += int(att.sum())
    print("fit tokens", ntok, flush=True); out, ctl, rep = {"layers": {}, "keys": keys}, {"layers": {}}, {}
    for l, fs in by.items():
        A = S[l]["NtN"].double(); A += lam * A.diagonal().mean() * torch.eye(H, device="cuda", dtype=torch.float64); G = torch.linalg.solve(A, S[l]["NtE"].double()).float(); k = len(fs); t = lib.TC[l]
        out["layers"][l] = dict(feats=fs, G=G[:, :k].cpu(), w_dec=t["w_dec"][fs].clone(), w_enc=t["w_enc"][:, fs].float().cpu(), b_enc=t["b_enc"][fs].cpu(), thr=t["threshold"][fs].cpu())
        ctl["layers"][l] = dict(feats=rnd[l], G=G[:, k:].cpu(), w_dec=t["w_dec"][rnd[l]].clone(), w_enc=t["w_enc"][:, rnd[l]].float().cpu(), b_enc=t["b_enc"][rnd[l]].cpu(), thr=t["threshold"][rnd[l]].cpu())
        S[l] = None; torch.cuda.empty_cache(); rep[l] = dict(G=G)
    # held-out fidelity: how well do neurons predict each feature, and how close is the edited write to the exact ablation
    acc = {l: dict(se=torch.zeros(2 * len(fs), device="cuda"), st=torch.zeros(2 * len(fs), device="cuda"), sm=torch.zeros(2 * len(fs), device="cuda"), n=0, err_bake=0.0, err_none=0.0, err_proj=0.0, tgt=0.0) for l, fs in by.items()}
    for ids, att in batches(held, tok):
        with torch.no_grad():
            lib.BASE(input_ids=ids, attention_mask=(ids != tok.pad_token_id))
            for l, fs in by.items():
                n, E, rms = targets(l, att); P = n @ rep[l]["G"]; a = acc[l]; a["se"] += (P - E).pow(2).sum(0); a["st"] += E.pow(2).sum(0); a["sm"] += E.sum(0); a["n"] += len(n); k = len(fs)
                d = lib.TC[l]["w_dec"][fs].cuda(); g1 = 1 + gamma(l); m = cap[("m", l)][att].float(); y = m / rms * g1; c = (E[:, :k] / rms) @ d                        # exact contribution in y-space
                m2 = m - (P[:, :k] @ (d / g1)); y2 = m2 / (m2.pow(2).mean(-1, keepdim=True) + 1e-6).sqrt() * g1; Q = torch.linalg.qr((d / g1).T)[0]; m3 = m - (m @ Q) @ Q.T; y3 = m3 / (m3.pow(2).mean(-1, keepdim=True) + 1e-6).sqrt() * g1
                a["err_bake"] += float((y2 - (y - c)).pow(2).sum()); a["err_proj"] += float((y3 - (y - c)).pow(2).sum()); a["err_none"] += float(c.pow(2).sum()); a["tgt"] += float(y.pow(2).sum())
    report = {}
    for l, fs in by.items():
        a = acc[l]; var = a["st"] - a["sm"].pow(2) / a["n"]; r2 = (1 - a["se"] / var.clamp(min=1e-9)).cpu(); k = len(fs)
        report[l] = dict(features=[f"L{l}.{f}" for f in fs], r2=[round(float(x), 3) for x in r2[:k]], r2_random=round(float(r2[k:].mean()), 3),
                         unexplained_bake=round(a["err_bake"] / max(a["err_none"], 1e-9), 4), unexplained_project=round(a["err_proj"] / max(a["err_none"], 1e-9), 4), removed_share_of_write=round(a["err_none"] / a["tgt"], 5))
        print(f"L{l}: {k} features, R2 mean {sum(report[l]['r2']) / k:.3f} (min {min(report[l]['r2']):.3f}); residual vs exact ablation: baked {report[l]['unexplained_bake']:.3f}, projection {report[l]['unexplained_project']:.2f} (1.0 = no edit); features carry {100 * report[l]['removed_share_of_write']:.2f}% of the layer's write", flush=True)
    out["report"] = report; torch.save(out, f"{W}/bake_{name}.pt"); torch.save(ctl, f"{W}/bake_{name}_random.pt"); json.dump(report, open(f"{W}/bake_{name}_report.json", "w")); print("BAKE_FIT_DONE", name)
