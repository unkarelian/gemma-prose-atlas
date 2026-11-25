"""Three checks on the baked edit.   python bake_checks.py   -> bake_checks.json
A. Is the low-rank term really the same as an edited weight matrix (merged in float32)?
B. Capability: MMLU accuracy (500 questions) for the unedited model and each edit.
C. Which removed feature breaks a/an agreement? Leave-one-feature-in exact ablation on positions where Gemma wrote " an"."""
import json, os, re, random, collections, urllib.request, torch, torch.nn as nn
import lib, tcbake
from lib import W
tok, model = lib.load(); random.seed(3); out = {}
def undo(B, hooks):
    for h in hooks: h.remove()
    for l in B["layers"]:
        dp = lib.LAYERS[l].mlp.down_proj
        if not isinstance(dp, nn.Linear): lib.LAYERS[l].mlp.down_proj = dp.lin
tasks = [t for t in lib.read_jsonl(f"{W}/gen_tasks.jsonl") if t["set"] == "wp"][:120]; rain = tok(" rain", add_special_tokens=False).input_ids[0]
def p_rain():
    tok.padding_side = "right"; e = tok([lib.chat_frame(t["prompt"]) + "The" for t in tasks], add_special_tokens=False, return_tensors="pt", padding=True); last = (e.attention_mask.sum(1) - 1).cuda(); ps = []
    for s in range(0, len(tasks), 40):
        with torch.no_grad(): ps.append(lib.LM(lib.BASE(input_ids=e.input_ids[s:s + 40].cuda(), attention_mask=e.attention_mask[s:s + 40].cuda()).last_hidden_state[torch.arange(len(last[s:s + 40]), device="cuda"), last[s:s + 40]]).float().log_softmax(-1)[:, rain].exp().cpu())
    return torch.cat(ps)
# ---- A. merge equivalence
class Merged(nn.Module):
    def __init__(self, ed): super().__init__(); self.lin = ed.lin; self.Wm = nn.Parameter(ed.merged_weight(), requires_grad=False); self.b = ed.lin.bias
    def forward(self, n): return torch.nn.functional.linear(n.float(), self.Wm, None if self.b is None else self.b.float()).to(n.dtype)
B, hooks = tcbake.apply(f"{W}/bake_rain60.pt", "bake"); pb = p_rain(); diffs = []
for l in B["layers"]:
    ed = lib.LAYERS[l].mlp.down_proj; n = torch.randn(64, ed.lin.in_features, device="cuda", dtype=torch.bfloat16) * 3; a = ed(n).float(); mg = Merged(ed); b = mg(n).float(); diffs.append(float((a - b).abs().max() / a.abs().max())); lib.LAYERS[l].mlp.down_proj = mg
pm = p_rain(); out["merge"] = dict(p_rain_lowrank=round(float(pb.mean()), 4), p_rain_merged_fp32=round(float(pm.mean()), 4), max_abs_diff_p=round(float((pb - pm).abs().max()), 5), max_rel_diff_layer_output=round(max(diffs), 5),
                                 delta_over_weight=[round(float((lib.LAYERS[l].mlp.down_proj.Wm - lib.LAYERS[l].mlp.down_proj.lin.weight.float()).norm() / lib.LAYERS[l].mlp.down_proj.lin.weight.float().norm()), 4) for l in B["layers"]])
for l in B["layers"]: lib.LAYERS[l].mlp.down_proj = lib.LAYERS[l].mlp.down_proj.lin
print("A merge", out["merge"], flush=True)
# ---- B. capability
os.system("pip install -q -c /tmp/c.txt pandas pyarrow > /dev/null 2>&1"); import pandas as pd
p = f"{W}/mmlu_test.parquet"
if not os.path.exists(p): urllib.request.urlretrieve("https://huggingface.co/datasets/cais/mmlu/resolve/main/all/test-00000-of-00001.parquet", p)
df = pd.read_parquet(p).sample(500, random_state=0); L4 = [tok(x, add_special_tokens=False).input_ids[0] for x in ("A", "B", "C", "D")]
qs = [lib.chat_frame(f"{r.question}\n\nA. {r.choices[0]}\nB. {r.choices[1]}\nC. {r.choices[2]}\nD. {r.choices[3]}\n\nAnswer with a single letter.") for r in df.itertuples()]; gold = torch.tensor(df.answer.tolist())
def mmlu():
    tok.padding_side = "right"; pr = []
    for s in range(0, len(qs), 25):
        e = tok(qs[s:s + 25], add_special_tokens=False, return_tensors="pt", padding=True); last = (e.attention_mask.sum(1) - 1).cuda()
        with torch.no_grad(): pr.append(lib.LM(lib.BASE(input_ids=e.input_ids.cuda(), attention_mask=e.attention_mask.cuda()).last_hidden_state[torch.arange(len(last), device="cuda"), last]).float()[:, L4].argmax(-1).cpu())
    return round(float((torch.cat(pr) == gold).float().mean()), 4)
out["mmlu"] = {"unedited": mmlu()}; print("B unedited", out["mmlu"], flush=True)
for label, path, mode in (("rain60 baked", "bake_rain60.pt", "bake"), ("habits (150) baked", "bake_habits.pt", "bake"), ("habits+names (218) baked", "bake_habits_names.pt", "bake"), ("habits+names exact", "bake_habits_names.pt", "exact"),
                          ("habits+names projection", "bake_habits_names.pt", "project"), ("random (218) baked", "bake_habits_names_random.pt", "bake")):
    B, hooks = tcbake.apply(f"{W}/{path}", mode); out["mmlu"][label] = mmlu(); undo(B, hooks); print("B", label, out["mmlu"][label], flush=True); json.dump(out, open(f"{W}/bake_checks.json", "w"), indent=1)
# ---- C. a/an
gen = [d for d in lib.read_jsonl(f"{W}/gen.jsonl") if d["cond"] == "gemma" and d["set"] == "wp"]; random.shuffle(gen); ctx = []
for d in gen:
    for m in re.finditer(r" an (?=[aeiouAEIOU])", d["text"][:2500]):
        ctx.append(tok(lib.chat_frame(d["prompt"]), add_special_tokens=False).input_ids[-120:] + tok(d["text"][:m.start()], add_special_tokens=False).input_ids[-150:])
        if len(ctx) >= 240: break
    if len(ctx) >= 240: break
AN, A_ = tok(" an", add_special_tokens=False).input_ids[0], tok(" a", add_special_tokens=False).input_ids[0]
def p_an():
    ps = []; order = sorted(range(len(ctx)), key=lambda i: len(ctx[i]))
    for s in range(0, len(order), 60):
        idx = order[s:s + 60]; L = max(len(ctx[i]) for i in idx); ids = torch.full((len(idx), L), tok.pad_token_id, dtype=torch.long); att = torch.zeros((len(idx), L), dtype=torch.long)
        for k, i in enumerate(idx): ids[k, L - len(ctx[i]):] = torch.tensor(ctx[i]); att[k, L - len(ctx[i]):] = 1
        with torch.no_grad(): lp = lib.LM(lib.BASE(input_ids=ids.cuda(), attention_mask=att.cuda()).last_hidden_state[:, -1]).float().log_softmax(-1); ps.append(torch.stack([lp[:, AN].exp(), lp[:, A_].exp()], 1).cpu())
    return torch.cat(ps).mean(0)
base = p_an(); out["an"] = dict(n=len(ctx), unedited=dict(p_an=round(float(base[0]), 4), p_a=round(float(base[1]), 4)))
for label, path, mode in (("habits baked", "bake_habits.pt", "bake"), ("habits exact", "bake_habits.pt", "exact"), ("rain60 baked", "bake_rain60.pt", "bake")):
    B, hooks = tcbake.apply(f"{W}/{path}", mode); r = p_an(); out["an"][label] = dict(p_an=round(float(r[0]), 4), p_a=round(float(r[1]), 4)); undo(B, hooks)
print("C", out["an"], flush=True)
B = torch.load(f"{W}/bake_habits.pt"); single = []
for l, b in B["layers"].items():
    for q, f in enumerate(b["feats"]):
        one = {"layers": {l: {k: (v[[q]] if k in ("w_dec", "b_enc", "thr") else v[:, [q]] if k in ("G", "w_enc") else [f]) for k, v in b.items()}}}; torch.save(one, f"{W}/_one.pt")
        BB, hooks = tcbake.apply(f"{W}/_one.pt", "exact"); r = p_an(); undo(BB, hooks); single.append((f"L{l}.{f}", round(float(r[0]), 4), round(float(r[1]), 4)))
single.sort(key=lambda x: x[1]); out["an"]["single_feature_exact"] = single[:12]; print("C worst single features for ' an':", single[:8], flush=True)
json.dump(out, open(f"{W}/bake_checks.json", "w"), indent=1); print("BAKE_CHECKS_DONE")
