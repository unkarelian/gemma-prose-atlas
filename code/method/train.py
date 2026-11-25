"""Step 1: teach the model the prose you want, as a small adapter.

    python train.py pairs.jsonl out_dir [--model unsloth/gemma-3-4b-it] [--epochs 3] [--rank 16] [--lr 1e-4]

pairs.jsonl: one JSON object per line, {"prompt": "...", "text": "..."}.
  prompt = the request the model would get (a writing prompt, or a short outline of the scene)
  text   = prose you consider good, written for that request (a scene of 300-600 words works well)
A few hundred pairs are enough: the published-prose adapter in the write-up used 333 scenes.
The loss is on the text only, in the model's own chat frame, so the adapter changes how it answers and nothing else.
Needs: torch, transformers, peft. About 20 GB of GPU memory for a 4B model in bf16; 15 minutes for 333 pairs.
"""
import sys, json, random, time, torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import LoraConfig, get_peft_model

def arg(k, d): return type(d)(sys.argv[sys.argv.index(k) + 1]) if k in sys.argv else d
src, out = sys.argv[1], sys.argv[2]
MODEL, EPOCHS, RANK, LR = arg("--model", "unsloth/gemma-3-4b-it"), arg("--epochs", 3), arg("--rank", 16), arg("--lr", 1e-4)
MAX_TEXT, MAX_PROMPT, BATCH, ACCUM = 448, 560, 2, 2
random.seed(31); torch.manual_seed(31)

tok = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForCausalLM.from_pretrained(MODEL, torch_dtype=torch.bfloat16, device_map="cuda")
# attention and MLP projections of the language model only (the pattern also skips a vision tower if there is one)
cfg = LoraConfig(r=RANK, lora_alpha=2 * RANK, lora_dropout=0.0, task_type="CAUSAL_LM",
                 target_modules=r"^(?!.*(vision|multi_modal)).*\.(q_proj|k_proj|v_proj|o_proj|gate_proj|up_proj|down_proj)$")
model = get_peft_model(model, cfg); model.print_trainable_parameters()
train = [p for p in model.parameters() if p.requires_grad]
for p in train: p.data = p.data.float()
opt = torch.optim.AdamW(train, lr=LR, weight_decay=0.0)

def frame(prompt):          # the chat frame, ending where the model's answer starts
    ids = tok(tok.apply_chat_template([{"role": "user", "content": prompt}], add_generation_prompt=True, tokenize=False), add_special_tokens=False).input_ids
    return ids[:1] + ids[1:][-MAX_PROMPT:]
end = tok.convert_tokens_to_ids("<end_of_turn>") if "<end_of_turn>" in tok.get_vocab() else tok.eos_token_id
rows = [json.loads(l) for l in open(src) if l.strip()]
data = [(frame(r["prompt"]), tok(r["text"], add_special_tokens=False).input_ids[:MAX_TEXT] + [end]) for r in rows]
print(len(data), "pairs", flush=True)

pad = tok.pad_token_id if tok.pad_token_id is not None else 0; step = 0; t0 = time.time(); model.train()
for ep in range(EPOCHS):
    random.shuffle(data)
    for s in range(0, len(data), BATCH):
        b = data[s:s + BATCH]; L = max(len(f) + len(t) for f, t in b)
        ids = torch.full((len(b), L), pad); lab = torch.full((len(b), L), -100); att = torch.zeros((len(b), L), dtype=torch.long)
        for k, (f, t) in enumerate(b):
            x = f + t; ids[k, :len(x)] = torch.tensor(x); att[k, :len(x)] = 1; lab[k, len(f):len(x)] = torch.tensor(t)
        with torch.autocast("cuda", dtype=torch.bfloat16):
            loss = model(input_ids=ids.cuda(), attention_mask=att.cuda(), labels=lab.cuda()).loss
        (loss / ACCUM).backward(); step += 1
        if step % ACCUM == 0:
            torch.nn.utils.clip_grad_norm_(train, 1.0); opt.step(); opt.zero_grad()
        if step % 40 == 0: print(f"epoch {ep} step {step} loss {loss.item():.3f} {time.time() - t0:.0f}s", flush=True)
model.save_pretrained(out); print("saved", out)
