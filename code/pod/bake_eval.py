"""Evaluate a baked edit against the exact run-time ablation, the projection baseline and a random-feature control.   python bake_eval.py NAME TARGET_TOKEN
Effect: probability of the target token after an opening "The" on 340 prompts.  Side effects: KL from the unedited model's next-token distribution
and change in surprisal on held-out text of four kinds.  -> bake_NAME_eval.json"""
import sys, json, random, collections, torch
import lib, tcbake
from lib import W
name, target = sys.argv[1], sys.argv[2]; tok, model = lib.load(); random.seed(77)
tasks = [t for t in lib.read_jsonl(f"{W}/gen_tasks.jsonl") if t["set"] == "wp"]; tid = tok(target, add_special_tokens=False).input_ids[0]
docs = lib.read_jsonl(f"{W}/corpus.jsonl") + lib.read_jsonl(f"{W}/gen.jsonl"); held = {}
for c in ("human", "gemma", "claude"):
    ds = [d for d in docs if d["set"] == "wp" and d["cond"] == c and d.get("frame", "chat") == "chat" and lib.half_of(d) == 1]; random.shuffle(ds); held[c] = ds[:25]
held["requests"] = [dict(prompt=r["human"], text=r["gemma"]) for r in lib.read_jsonl(f"{W}/a2a/requests.jsonl")][200:225]
def run_target():
    tok.padding_side = "right"; ps = []
    for s in range(0, len(tasks), 34):
        e = tok([lib.chat_frame(t["prompt"]) + "The" for t in tasks[s:s + 34]], add_special_tokens=False, return_tensors="pt", padding=True); last = (e.attention_mask.sum(1) - 1).cuda()
        with torch.no_grad(): lp = lib.LM(lib.BASE(input_ids=e.input_ids.cuda(), attention_mask=e.attention_mask.cuda()).last_hidden_state[torch.arange(len(last), device="cuda"), last]).float().log_softmax(-1)
        ps.append(lp.cpu())
    lp = torch.cat(ps); top = lp.exp().mean(0).topk(5); return round(float(lp[:, tid].exp().mean()), 4), [[tok.decode([int(i)]), round(float(v), 3)] for v, i in zip(top.values, top.indices)]
NTOK = 96
def doc_ids(d):
    fr = tok(lib.chat_frame(d["prompt"]), add_special_tokens=False).input_ids[-400:]; tx = tok(d["text"], add_special_tokens=False).input_ids[:NTOK]
    return ([tok.bos_token_id] + (fr[1:] if fr[0] == tok.bos_token_id else fr)), tx
def logp(d):
    fr, tx = doc_ids(d); ids = torch.tensor([fr + tx]).cuda()
    with torch.no_grad(): return lib.LM(lib.BASE(input_ids=ids).last_hidden_state[0, -len(tx) - 1:-1]).float().log_softmax(-1), torch.tensor(tx).cuda()
def run_text(base=None):
    """Without `base`: returns the unedited distributions (half precision, on the CPU). With it: KL from them and surprisal, per kind of text."""
    store, kl, klmax, nll = {}, {}, {}, {}
    for c, ds in held.items():
        ks, km, tot, n = [], 0.0, 0.0, 0
        for j, d in enumerate(ds):
            lp, tx = logp(d); tot += float(-lp[torch.arange(len(tx)), tx].sum()); n += len(tx)
            if base is None: store[(c, j)] = lp.half().cpu()
            else:
                b = base[(c, j)].cuda().float(); k = (b.exp() * (b - lp)).sum(-1); ks.append(float(k.mean())); km = max(km, float(k.max()))
        nll[c] = round(tot / n, 3)
        if base is not None: kl[c] = round(sum(ks) / len(ks), 5); klmax[c] = round(km, 3)
    return (store, nll) if base is None else (kl, klmax, nll)
def undo(B, hooks):
    for h in hooks: h.remove()
    for l in B["layers"]:
        dp = lib.LAYERS[l].mlp.down_proj
        if isinstance(dp, tcbake.Edited): lib.LAYERS[l].mlp.down_proj = dp.lin
base_p, base_top = run_target(); base_t, base_nll = run_text(); res = {"unedited": dict(p_target=base_p, top=base_top, kl={c: 0.0 for c in held}, nll=base_nll)}
print("unedited", res["unedited"], flush=True)
CONDS = [("exact run-time ablation", f"bake_{name}.pt", "exact"), ("baked into weights", f"bake_{name}.pt", "bake"), ("projection baseline", f"bake_{name}.pt", "project"), ("baked, random features (control)", f"bake_{name}_random.pt", "bake"),
         ("exact, random features (control)", f"bake_{name}_random.pt", "exact")]
for label, path, mode in CONDS:
    B, hooks = tcbake.apply(f"{W}/{path}", mode); p, top = run_target(); kl, klmax, nll = run_text(base_t)
    res[label] = dict(p_target=p, top=top, kl=kl, kl_max_token=klmax, nll=nll); undo(B, hooks); print(label, res[label], flush=True); json.dump(res, open(f"{W}/bake_{name}_eval.json", "w"), indent=1)
print("BAKE_EVAL_DONE")
