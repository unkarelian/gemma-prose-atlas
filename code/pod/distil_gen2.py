"""Control distillations for the register question.   python distil_gen2.py
plain:  Gemma's ordinary answers to the same 300 requests (no instruction)  -> tells fine-tuning erosion apart from register.
casual: its answers under a casual-register instruction                     -> does compliance then follow casual wording?"""
import json, torch
import lib
from lib import W
tok, model = lib.load(); tok.padding_side = "left"; reqs = [r["human"] for r in lib.read_jsonl(f"{W}/a2a/requests.jsonl")]
INS = {"plain": "", "casual": "\n\n(Respond the way a friendly person would in a quick chat message: casual, lowercase where natural, contractions, short sentences, a bit of slang. No headings, no bullet lists, no formal phrasing.)"}
for name, ins in INS.items():
    out = []
    for s in range(0, len(reqs), 60):
        b = reqs[s:s + 60]; e = tok([lib.chat_frame(r + ins) for r in b], add_special_tokens=False, return_tensors="pt", padding=True)
        with torch.no_grad(): o = model.generate(input_ids=e.input_ids.cuda(), attention_mask=e.attention_mask.cuda(), max_new_tokens=320, do_sample=False)
        out += [dict(prompt=r, text=tok.decode(row[e.input_ids.shape[1]:], skip_special_tokens=True).strip()) for r, row in zip(b, o)]
        json.dump(dict(stage=f"{name} register targets", progress="", done=True, items=[dict(id=name, mode=f"answering in the {name} register", brief=x["prompt"][:300], text=x["text"]) for x in out[-4:]]), open(f"{W}/live.json", "w"))
    with open(f"{W}/distil_{name}.jsonl", "w") as f:
        for x in out: f.write(json.dumps(x, ensure_ascii=False) + "\n")
    print("DISTIL", name, len(out), "|", out[3]["text"][:200].replace("\n", " "), flush=True)
print("DISTIL2_DONE")
