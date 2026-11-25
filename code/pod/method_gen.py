"""Generate stories for the prose method under one configuration.   python method_gen.py TAG [--lora DIR] [--scale A] [--rep P] [--temp T] [--n K] [--bake FILE]
48 held-out writing prompts and 40 scene outlines from held-out books; K samples each.  -> method_TAG.jsonl"""
import sys, json, random, torch
import lib
from lib import W
tag = sys.argv[1]; arg = lambda k, d=None: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
tok, model = lib.load(); random.seed(55)
if arg("--lora"):
    from peft import PeftModel
    pm = PeftModel.from_pretrained(model, arg("--lora")); sc = float(arg("--scale", 1.0))
    for m in pm.modules():
        if isinstance(getattr(m, "scaling", None), dict):
            for k in m.scaling: m.scaling[k] *= sc
    model = pm.merge_and_unload().eval(); lib.model = model
if arg("--bake"):
    import tcbake; tcbake.apply(arg("--bake"), "bake")
wp = json.load(open(f"{W}/steer_plan.json"))["prompts"][:48]; tasks = [t for t in lib.read_jsonl(f"{W}/gen_tasks.jsonl") if t["set"] == "books" and lib.half_of(dict(book=t["book"], group=t["group"])) == 1]; random.shuffle(tasks)
jobs = [dict(set="wp", group=p["group"], prompt=p["prompt"], brief=p["brief"]) for p in wp] + [dict(set="books", group=t["group"], prompt=t["prompt"], brief="Novel scene from an outline") for t in tasks[:40]]
K = int(arg("--n", 1)); jobs = [dict(j, k=k) for j in jobs for k in range(K)]; jobs.sort(key=lambda j: len(j["prompt"])); tok.padding_side = "left"
kw = dict(do_sample=True, temperature=float(arg("--temp", 1.0)), top_k=64, top_p=0.95); rp = float(arg("--rep", 1.0))
if rp != 1.0: kw["repetition_penalty"] = rp
with open(f"{W}/method_{tag}.jsonl", "w") as f:
    for s in range(0, len(jobs), 40):
        b = jobs[s:s + 40]; e = tok([lib.chat_frame(j["prompt"]) for j in b], add_special_tokens=False, return_tensors="pt", padding=True)
        with torch.no_grad(): o = model.generate(input_ids=e.input_ids.cuda(), attention_mask=e.attention_mask.cuda(), max_new_tokens=520, **kw)
        txt = [tok.decode(r[e.input_ids.shape[1]:], skip_special_tokens=True).strip() for r in o]
        for j, t in zip(b, txt): f.write(json.dumps(dict(tag=tag, set=j["set"], group=j["group"], k=j["k"], text=t), ensure_ascii=False) + "\n")
        f.flush(); json.dump(dict(stage=f"prose method: {tag}", progress=f"{s + len(b)}/{len(jobs)}", done=True, items=[dict(id=tag, mode=f"method configuration: {tag}", brief=j["brief"][:300], text=t) for j, t in list(zip(b, txt))[:4]]), open(f"{W}/live.json", "w"))
print("METHOD_GEN_DONE", tag)
