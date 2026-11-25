"""Anti-slop surgery, conventional version: a rank-16 LoRA that writes the human version of each brief.   python train_lora.py human
Trains on split half 0 (other prompts and other books are held out). Loss on the text tokens only.  -> {W}/lora_<name>/"""
import sys, json, random, time, torch
import lib
from lib import W
from peft import LoraConfig, get_peft_model
name = sys.argv[1]; tok, model = lib.load(); random.seed(31); torch.manual_seed(31)
if name == "books":
    data = [(lib.chat_frame(d["prompt"]), d["text"]) for d in lib.read_jsonl(f"{W}/corpus.jsonl") if d["set"] == "books" and d["cond"] == "human" and lib.half_of(d) == 0]      # published prose only
elif name == "human":
    data = [(lib.chat_frame(d["prompt"]), d["text"]) for d in lib.read_jsonl(f"{W}/corpus.jsonl") if d["set"] in ("wp", "books") and d["cond"] == "human" and lib.half_of(d) == 0]
else:
    data = [(lib.chat_frame(d["prompt"]), d["text"]) for d in lib.read_jsonl(f"{W}/distil_{name}.jsonl")]
cfg = LoraConfig(r=16, lora_alpha=32, lora_dropout=0.0, target_modules=r".*language_model.*\.(q_proj|k_proj|v_proj|o_proj|gate_proj|up_proj|down_proj)", task_type="CAUSAL_LM")
model = get_peft_model(model, cfg); model.print_trainable_parameters()
for p in model.parameters():
    if p.requires_grad: p.data = p.data.float()
opt = torch.optim.AdamW([p for p in model.parameters() if p.requires_grad], lr=1e-4, weight_decay=0.0)
EPOCHS = int(sys.argv[2]) if len(sys.argv) > 2 else 2; BS = 2; ACC = 2; MAXT = 448; steps = 0; t0 = time.time(); model.train()
bos = tok.bos_token_id; eot = tok.convert_tokens_to_ids("<end_of_turn>")
def fr_ids(f):
    x = tok(f, add_special_tokens=False).input_ids; x = x[1:] if x and x[0] == bos else x
    return [bos] + x[-560:]
enc = [(fr_ids(f), tok(t, add_special_tokens=False).input_ids[:MAXT] + [eot]) for f, t in data]
print(len(enc), "examples", flush=True)
for ep in range(EPOCHS):
    random.shuffle(enc)
    for s in range(0, len(enc), BS):
        b = sorted(enc[s:s + BS], key=lambda x: -(len(x[0]) + len(x[1]))); L = len(b[0][0]) + len(b[0][1])
        ids = torch.full((len(b), L), tok.pad_token_id, dtype=torch.long); lab = torch.full((len(b), L), -100, dtype=torch.long); att = torch.zeros((len(b), L), dtype=torch.long)
        for k, (f, t) in enumerate(b): x = f + t; ids[k, :len(x)] = torch.tensor(x); att[k, :len(x)] = 1; lab[k, len(f):len(x)] = torch.tensor(t)
        with torch.autocast("cuda", dtype=torch.bfloat16):
            loss = model(input_ids=ids.cuda(), attention_mask=att.cuda(), labels=lab.cuda()).loss
        (loss / ACC).backward(); steps += 1
        if steps % ACC == 0: torch.nn.utils.clip_grad_norm_([p for p in model.parameters() if p.requires_grad], 1.0); opt.step(); opt.zero_grad()
        if steps % 40 == 0: print(f"epoch {ep} step {steps} loss {loss.item():.3f} {time.time() - t0:.0f}s", flush=True)
model.save_pretrained(f"{W}/lora_{name}"); print("LORA_DONE", name, steps)
