"""Formal-register targets for distillation: Gemma answers 300 human requests under a formal-register instruction; the LoRA then learns to answer that way with no instruction.
python distil_gen.py -> distil_formal.jsonl, distil_full.jsonl (formal answers + human-written fiction, the combined surgery)"""
import json, torch
import lib
from lib import W
tok, model = lib.load(); tok.padding_side = "left"
reqs = [r["human"] for r in lib.read_jsonl(f"{W}/a2a/requests.jsonl")]
INS = "\n\n(Respond in a formal, professional register: measured, precise and impersonal. No exclamation marks, no emoji, no conversational openers or filler, no enthusiasm, no questions back to the user.)"
out = []
for s in range(0, len(reqs), 60):
    b = reqs[s:s + 60]; e = tok([lib.chat_frame(r + INS) for r in b], add_special_tokens=False, return_tensors="pt", padding=True)
    with torch.no_grad(): o = model.generate(input_ids=e.input_ids.cuda(), attention_mask=e.attention_mask.cuda(), max_new_tokens=320, do_sample=False)
    out += [dict(prompt=r, text=tok.decode(row[e.input_ids.shape[1]:], skip_special_tokens=True).strip()) for r, row in zip(b, o)]
    json.dump(dict(stage="formal register targets", progress="", done=True, items=[dict(id="formal", mode="answering under a formal-register instruction", brief=x["prompt"][:300], text=x["text"]) for x in out[-4:]]), open(f"{W}/live.json", "w")); print(len(out), flush=True)
with open(f"{W}/distil_formal.jsonl", "w") as f:
    for x in out: f.write(json.dumps(x, ensure_ascii=False) + "\n")
hum = [dict(prompt=d["prompt"], text=d["text"]) for d in lib.read_jsonl(f"{W}/corpus.jsonl") if d["set"] in ("wp", "books") and d["cond"] == "human" and lib.half_of(d) == 0]
with open(f"{W}/distil_full.jsonl", "w") as f:
    for x in out + hum: f.write(json.dumps(x, ensure_ascii=False) + "\n")
print("DISTIL_DONE", len(out), len(hum), "|", out[0]["text"][:300].replace("\n", " "))
