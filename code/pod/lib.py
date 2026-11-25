"""Shared pieces for the pod scripts: model, Gemma Scope 2 transcoders, chat frame, corpus IO."""
import json, os, re, struct, time, hashlib, urllib.request
from concurrent.futures import ThreadPoolExecutor
import torch, torch.nn as nn

MID = os.environ.get("MID", "unsloth/gemma-3-4b-it")       # ungated mirror of google/gemma-3-4b-it
GS_REPO = "google/gemma-scope-2-4b-it"
TC_PATH = "transcoder_all/layer_{l}_width_16k_l0_small/params.safetensors"
W = os.environ.get("WORK", "/workspace/pi")
MASSIVE = 443                                               # a residual dimension with huge constant values
dev = "cuda"
tok = model = LAYERS = FNORM = LM = BASE = None
NL = D = 0
MAXTEXT = 640                                               # text tokens read per document


def load():
    global tok, model, LAYERS, FNORM, LM, BASE, NL, D
    from transformers import AutoTokenizer, AutoModelForCausalLM
    t0 = time.time()
    tok = AutoTokenizer.from_pretrained(MID)
    try:
        from transformers import Gemma3ForConditionalGeneration as G
    except Exception:
        G = AutoModelForCausalLM
    model = G.from_pretrained(MID, dtype=torch.bfloat16, device_map=dev, **({"attn_implementation": "eager"} if os.environ.get("ATTN") == "eager" else {})).eval()
    cfg = model.config.text_config if hasattr(model.config, "text_config") else model.config
    NL, D = cfg.num_hidden_layers, cfg.hidden_size
    LAYERS = next(m for n, m in model.named_modules() if isinstance(m, nn.ModuleList) and len(m) == NL and n.endswith("layers") and "vision" not in n)
    FNORM = next(m for n, m in model.named_modules() if n.endswith("language_model.norm") or n == "model.norm")
    LM = model.lm_head if hasattr(model, "lm_head") else model.get_output_embeddings()
    BASE = model.model
    print(f"model loaded in {time.time() - t0:.0f}s: {NL} layers d={D} {next(model.parameters()).dtype}", flush=True)
    return tok, model


def _get(url, headers, timeout=300, tries=5):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=timeout) as r:
                return r.status, r.read()
        except Exception as e:
            if i == tries - 1: raise
            time.sleep(2 + 3 * i)


def fetch_tensors(path, names, repo=GS_REPO):
    """Read named tensors of a safetensors file on the Hub by HTTP range; cached on disk."""
    cdir = f"{W}/tc_cache"; os.makedirs(cdir, exist_ok=True)
    out, need = {}, []
    for k in names:
        f = f"{cdir}/{hashlib.md5((path + k).encode()).hexdigest()}.pt"
        if os.path.exists(f): out[k] = torch.load(f)
        else: need.append((k, f))
    if not need: return out
    url = f"https://huggingface.co/{repo}/resolve/main/{path}"
    st, b = _get(url, {"Range": "bytes=0-7"}); n = struct.unpack("<Q", b)[0]
    _, hb = _get(url, {"Range": f"bytes=8-{7 + n}"}); hdr = json.loads(hb)
    for k, f in need:
        m = hdr[k]; a, z = m["data_offsets"]; assert m["dtype"] == "F32"
        st, raw = _get(url, {"Range": f"bytes={8 + n + a}-{8 + n + z - 1}"})
        assert len(raw) == z - a, "short read"
        out[k] = torch.frombuffer(bytearray(raw), dtype=torch.float32).reshape(m["shape"]).clone()
        torch.save(out[k], f)
    return out


TC = {}
def load_tc(layers=None, dec=False, workers=6):
    """Encoders (bf16 on the GPU) for the given layers; with dec=True also decoders (kept on the CPU, float32)."""
    ls = list(range(NL)) if layers is None else list(layers)
    names = ("w_enc", "b_enc", "threshold") + (("w_dec", "b_dec") if dec else ())
    def one(l):
        p = fetch_tensors(TC_PATH.format(l=l), names)
        t = {"w_enc": p["w_enc"].to(dev, torch.bfloat16), "b_enc": p["b_enc"].to(dev), "threshold": p["threshold"].to(dev)}
        if dec: t["w_dec"], t["b_dec"] = p["w_dec"], p["b_dec"]
        TC[l] = t
    t0 = time.time()
    with ThreadPoolExecutor(workers) as ex: list(ex.map(one, [l for l in ls if l not in TC or (dec and "w_dec" not in TC[l])]))
    print(f"transcoders: {len(TC)} layers in {time.time() - t0:.0f}s", flush=True)


def tc_acts(l, X):
    """JumpReLU transcoder activations for MLP inputs X [n, d] -> [n, 16384] float32 (GPU)."""
    t = TC[l]
    p = (X.to(torch.bfloat16) @ t["w_enc"]).float() + t["b_enc"]
    return p * (p > t["threshold"])


def chat_frame(prompt):
    return tok.apply_chat_template([{"role": "user", "content": prompt}], tokenize=False, add_generation_prompt=True)


def split_opening(text, n=60):
    m = list(re.finditer(r"\S+", text))
    if len(m) <= n + 40: return None
    e = m[n - 1].end()
    return text[:e], text[e:]


def half_of(doc):
    """Split-half key: whole books for the novel set, the brief's hash otherwise."""
    k = doc.get("book") or doc["group"]
    return int(hashlib.md5(k.encode()).hexdigest(), 16) % 2


def read_jsonl(p):
    return [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]


def encode_doc(doc):
    """Token ids for the frame and the text (capped), and text-token character offsets."""
    if doc.get("frame") == "raw":
        fr = [tok.bos_token_id] + (tok(doc["opening"], add_special_tokens=False).input_ids if doc.get("opening") else [])
    else:
        fr = tok(chat_frame(doc["prompt"]), add_special_tokens=False).input_ids if doc.get("prompt") else [tok.bos_token_id]
    e = tok(doc["text"], add_special_tokens=False, return_offsets_mapping=True)
    return fr, e.input_ids[:MAXTEXT], e.offset_mapping[:MAXTEXT]
