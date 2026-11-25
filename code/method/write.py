"""Step 2: write with the adapter.

    python write.py prompts.jsonl out.jsonl --adapter out_dir [--strength 1.0] [--samples 1] [--repetition 1.05]
                    [--temperature 0.7] [--max-tokens 520] [--model unsloth/gemma-3-4b-it] [--save-merged DIR]

prompts.jsonl: {"id": "...", "prompt": "..."} per line.  out.jsonl: {"id", "k", "text"} per line, --samples texts per prompt.
--strength scales the adapter before it is merged into the weights: 1.0 is the trained adapter, 0.75 a milder version, 0 the
  original model. Below about 0.75 the original habits come back quickly.
--temperature 0.7 and --repetition 1.05 are the tested settings. At temperature 1.0 the adapter loses the thread; with no
  repetition penalty it loops; with a penalty of 1.1 it is pushed off its likeliest words and gets less coherent.
--save-merged writes the edited model as ordinary weights, to serve with anything.
Without --adapter this is the unedited model, for the before/after comparison.
"""
import sys, json, torch
from transformers import AutoTokenizer, AutoModelForCausalLM

def arg(k, d): return type(d)(sys.argv[sys.argv.index(k) + 1]) if k in sys.argv else d
src, out = sys.argv[1], sys.argv[2]
MODEL, ADAPTER, STRENGTH, N = arg("--model", "unsloth/gemma-3-4b-it"), arg("--adapter", ""), arg("--strength", 1.0), arg("--samples", 1)
tok = AutoTokenizer.from_pretrained(MODEL); tok.padding_side = "left"
model = AutoModelForCausalLM.from_pretrained(MODEL, torch_dtype=torch.bfloat16, device_map="cuda")
if ADAPTER:
    from peft import PeftModel
    pm = PeftModel.from_pretrained(model, ADAPTER)
    for m in pm.modules():
        if isinstance(getattr(m, "scaling", None), dict):
            for k in m.scaling: m.scaling[k] *= STRENGTH
    model = pm.merge_and_unload()
    if arg("--save-merged", ""): model.save_pretrained(arg("--save-merged", "")); tok.save_pretrained(arg("--save-merged", ""))
model.eval()
rows = [json.loads(l) for l in open(src) if l.strip()]
jobs = sorted([(r, k) for r in rows for k in range(N)], key=lambda j: len(j[0]["prompt"]))
kw = dict(do_sample=True, temperature=arg("--temperature", 0.7), top_k=64, top_p=0.95, repetition_penalty=arg("--repetition", 1.05), max_new_tokens=arg("--max-tokens", 520))
with open(out, "w") as f:
    for s in range(0, len(jobs), 32):
        b = jobs[s:s + 32]
        frames = [tok.apply_chat_template([{"role": "user", "content": r["prompt"]}], add_generation_prompt=True, tokenize=False) for r, _ in b]
        e = tok(frames, add_special_tokens=False, return_tensors="pt", padding=True).to("cuda")
        with torch.no_grad(): o = model.generate(**e, **kw)
        for (r, k), ids in zip(b, o):
            f.write(json.dumps(dict(id=r.get("id", r["prompt"][:40]), k=k, text=tok.decode(ids[e.input_ids.shape[1]:], skip_special_tokens=True).strip()), ensure_ascii=False) + "\n")
        f.flush(); print(f"{s + len(b)}/{len(jobs)}", flush=True)
