# Weight-space editing: literature and feasibility for an anti-slop surgery on Gemma 3 4B-it

Compiled 2026-11-25. Each summary comes from an abstract, paper text or blog read in this session; details I did not check are marked *unverified*. Both readings of the request have literature: (A), editing weights directly, is large and mature; (B), LLMs doing the editing, is small and almost entirely from late 2026.

## 1. What exists for (A)

**Task arithmetic and merging**
- Ilharco, Ribeiro, Wortsman et al. (2023), ICLR, arXiv:2212.04089, https://arxiv.org/abs/2212.04089. A task vector is the fine-tuned weights minus the pretrained weights. Negating one lowers performance on its task with little change on control tasks. Adding several gives a multi-task model.
- Zhang, Chen, Liu & He (2023), NeurIPS, arXiv:2306.14870, https://arxiv.org/abs/2306.14870. The same arithmetic works on LoRA modules, with no training. It covers addition, negation, unlearning and detoxifying Alpaca-LoRA.
- Yadav, Tam, Choshen, Raffel & Bansal (2023), NeurIPS, arXiv:2306.01708 (TIES), and Yu, Yu, Yu, Huang & Li (2024), ICML, arXiv:2311.03099 (DARE). Both reduce interference when deltas are combined.
- Huang, Li, Hsu et al. (2024), ACL, arXiv:2310.04799, https://arxiv.org/abs/2310.04799. "Chat vector" means chat weights minus base weights. Adding it to a continually pretrained model transfers instruction following and toxicity mitigation.
- Zheng, Wang, Ji, Huang & Peng (2025), ACL, arXiv:2404.16792 (ExPO). Scaling an alignment delta past 1 (extrapolation) improved AlpacaEval and MT-Bench for 1.8B-70B models.

**Weight steering and converting steering into weights**
- Fierro & Roger (2026), ICLR, arXiv:2511.05408, https://arxiv.org/abs/2511.05408. Contrastive weight steering: fine-tune once on the desired behaviour and once on its opposite, subtract the two deltas, and add or remove the result. On sycophancy, "evil" and refusal, it generalised further out of distribution than activation steering before general capabilities degraded. Code: github.com/safety-research/weight-steering.
- Sun, Yan, Wang & Weng (2026), NeurIPS, arXiv:2602.09870 (Steer2Edit). This converts a steering vector into rank-1 edits on selected attention heads and MLP neurons instead of a global addition. At matched utility it beat the best steering baseline (+17.2% safety, +9.8% truthfulness, −12.2% reasoning length).
- Abu Shairah, Hammoud, Turkiyyah & Ghanem (2026), EMNLP, arXiv:2508.20766 (ROSI). A rank-1 edit to every residual-writing matrix permanently adds a direction (additive steering in weight form). It raised refusal while MMLU, HellaSwag and ARC held.
- Schapiro, Park, Sosa & Varshney (2026), ICML workshop, arXiv:2607.01433 (CreativityNeuro). It scores weights Wanda-style (|W| × input-activation norm) on contrastive prompts ("Surprise me" vs "Be precise") and scales the weights important only to the creative set. It reduced mode collapse, and its gains transferred to unseen tasks where activation steering's did not. Divergent thinking and factual reasoning were not separable in weight space.

**Directional ablation baked into weights**
- Arditi, Obeso, Syed et al. (2024), arXiv:2406.11717, https://arxiv.org/abs/2406.11717. Refusal in 13 chat models is mediated by one direction. Orthogonalising the residual-writing matrices against it disables refusal "with minimal effect on other capabilities".
- Labonne (2024), HF blog, https://huggingface.co/blog/mlabonne/abliteration. An abliterated Llama-3-8B lost score on every benchmark. DPO recovered most of it, but not GSM8K. The post also cites FailSpy's "MopeyMule", a style (melancholy) abliteration.
- Lai (2025), HF blog, https://huggingface.co/blog/grimjim/norm-preserving-biprojected-abliteration. This removes only the directional part of each row of `o_proj`/`down_proj` and restores the row norms. On Gemma 3 12B a reasoning score rose over baseline (an informal leaderboard result). Measuring the direction required sparsifying the strong outlier activations, and the author recommends fp32 intermediate maths because bf16 gave worse results.
- Wollschläger, Elstner, Geisler et al. (2025), arXiv:2502.17420. Refusal is mediated by several independent directions and cones, not one.
- Fafuła (2026), arXiv:2607.17427. Abliterated Gemma-4 and Qwen3 MoE models became more optimistic (+12.2 pp and +7.4 pp) on a task that never triggers refusal, and expressed confidence moved in opposite directions in the two families.

**Locate-then-edit model editing**
- Meng, Bau, Andonian & Belinkov (2022), NeurIPS, arXiv:2202.05262 (ROME), and Meng, Sen Sharma, Andonian et al. (2023), arXiv:2210.07229 (MEMIT). Rank-1 and least-squares edits to mid-layer MLP output matrices rewrite facts, scaling to thousands of them. Gupta, Rao & Anumanchipalli (2024), ACL Findings, arXiv:2401.07453, show gradual and then catastrophic forgetting under sequential edits. Fang, Jiang, Wang et al. (2025), ICLR, arXiv:2410.02355 (AlphaEdit), reduce that damage by projecting each edit onto the null space of preserved keys.

**Interpretability-guided edits and unlearning**
- Guo, Syed, Sheshadri et al. (2024), arXiv:2410.12949. Editing components localised by mechanism gave more robust unlearning with fewer side effects than output-based localisation.
- Wang, Li, Wang, Hu & Zou (2025), arXiv:2505.24428 (SSPU). This uses SAE features to define a subspace that constrains gradient-based unlearning. My searches found no paper that bakes transcoder-feature ablations into weights.
- Anthropic (2026), "Returning to the Neuron Basis, Part 2", https://alignment.anthropic.com/2026/neuron-basis-applications/. It treats each MLP neuron as a context-gated steering vector (its `down_proj` column). It finds that most WMDP-cyber unlearning methods it tested hide the knowledge rather than remove it.

**Persona and style**
- Chen, Arditi, Sleight, Evans & Lindsey (2025), arXiv:2507.21509 (persona vectors). Trait shifts during fine-tuning correlate with shifts along activation directions. "Preventative steering" during training avoids them.
- Baines, Gonzalvez Hawthorne, Koroliuk et al. (2026), arXiv:2607.07916. Per-trait LoRAs scale roughly monotonically and combine roughly additively across six models (4B-32B), with capability preserved at moderate scales.
- Paech, Roush, Goldfeder & Shwartz-Ziv (2025), arXiv:2510.15061 (Antislop). This is not a weight edit, but it is the direct anti-slop baseline. Its token-level fine-tuning (FTPO) cut slop by 90% with GSM8K and MMLU maintained, while DPO damaged writing quality and lexical diversity.

## 2. LLMs doing the editing (B)

This literature is thin and recent, and almost none of it is peer-reviewed.
- Takehi, Teoh, Zhang & Khattab (MIT; author list taken from a secondary page), "Sparks of Weight-Space Programming", blog, Nov 2026, https://rikiyat.github.io/blog/weight-space-programming/. With 50 forward passes and no gradients, a frontier model traced Qwen3.5-0.8B's reasoning loops to one direction written by two MLP layers. It subtracted that direction from 64 `down_proj` columns per layer (0.016% of weights), and MATH-500 rose from 7.9% to 48.1%. On Gemma 3 270M, which rarely loops, it improved nothing. I found no arXiv version.
- Marasini, Khadka & Rahimi (2026), arXiv:2611.18553 (WeightBench). Frontier agents read small networks well "but cannot yet patch language models".
- Ahmed (2026), arXiv:2611.08070. Opus 5.5's zero-shot weight reading is "local arithmetic plus dataset priors".
- Liu, Xu, Li et al. (2026), arXiv:2611.27920. A DeepSeek agent implanted backdoors into 0.8-3B models for about $1.74 per run, finding rank-1 orthogonalisation and single-neuron surgery by itself.
- Agents that investigate models without editing them: Shaham, Schwettmann, Wang et al. (2024), arXiv:2404.14394 (MAIA); Anthropic auditing agents (2025), https://alignment.anthropic.com/2025/automated-auditing/; and Sheshadri, Ewart, Kempf et al. (2026), arXiv:2602.22755 (AuditBench), where the agent did best with black-box tools.
- Models that generate their own weight updates through training (SEAL, Zweiger, Pari, Guo et al. 2025, arXiv:2506.10943) or a hypernetwork (Text-to-LoRA, Charakorn, Cetin, Tang & Lange 2025, ICML, arXiv:2506.06105).

From frontier labs I found auditing agents and Anthropic's agent-selected neurons. I found no frontier-lab paper in which an agent applies weight edits to another LLM.

## 3. What is feasible here

I checked the architecture facts here in the transformers `modeling_gemma3.py` source and the HF config: hidden 2560, MLP 10240, GeGLU, bf16, no biases. Cost figures are my estimates, not measurements. Each sublayer writes `post_*_layernorm(W·z)`, and that norm multiplies by `(1 + weight)` after RMS-normalising. So **orthogonalising `o_proj`/`down_proj` against r does not remove r from what the sublayer writes** unless r is first mapped through the norm gain. This is the main Gemma-specific trap.

**(i) Task arithmetic with the existing deltas (cheapest).**
- Recipe: merge with `W + α·(B·A)·scale` for α ∈ {0.25, 0.5, 0.75, 1, 1.25}. Then repeat with attention-only and MLP-only deltas, and with layers 4-28 only.
- Contrastive version (Fierro & Roger): train a second rank-16 LoRA on Gemma's own stories for the same prompts and use Δ_human − Δ_gemma.
- Chat-vector version: `W_pt + β(W_it − W_pt)` with β ∈ [0.7, 1], applied only to MLP matrices of middle layers.
- Cost: seconds per merge plus one battery run per variant. The second LoRA costs one more training run.
- Risks: the LoRA's side effects come along with it. `surgery_style.json` shows its type-token ratio at 0.46 against 0.58 for humans, character names at 0.00, and exclamations at twice the human rate. The chat-vector slice will also move refusals and the chat format.
- Validation: plot every battery metric against α and look for a mid-α that keeps fluency.

**(ii) Baking in the 60-feature ablation.**
- (a) Exact version: append a fixed side branch, `mlp_out −= Σ_f JumpReLU(e_f·x̂ + b_f)·d_f`, using the 60 encoder rows and decoder columns. This is identical to the tested intervention but is not a pure weight edit.
- (b) Pure-weight version: a MEMIT/AlphaEdit-style least-squares edit of `down_proj`. Record the GeGLU hidden activations z (10240-d) on mixed text. Map the targets −Σ a_f d_f back through the post-norm (divide by `(1+γ)`, multiply by each token's RMS; first-order only), then solve a ridge regression with a null-space penalty on chat and human text. The 10240² fp32 covariance is about 0.4 GB per layer.
- (c) Blunt version: orthogonalise `down_proj` against the norm-corrected decoder directions. This removes everything that writes along them, not only these features.
- Risks: features are sparse, but a linear edit on a dense z leaks. Several layers may need editing.
- Validation: the 61% → 6% story-opening rate, KL against version (a) on held-out text, and the full battery.

**(iii) Directional ablation in weights.**
- Recipe: in fp32, with dimension 443 excluded from r, map r into each writer's pre-norm space as `r̃ = normalise((1+γ_l) ⊙ r)`. Then orthogonalise `o_proj` and `down_proj` against r̃, using Lai's row-norm-preserving form. Leave the embedding alone or untie it first, because Gemma 3 ties it to the unembedding (`tie_word_embeddings=True` in the config class), so editing it also edits the output logits. Cast to bf16 last. Start with one direction from the best-separating layer (Arditi), then try per-layer directions.
- Ablation sets the projection to 0, not to the human mean. Check in `rmean.npy` whether human text sits near 0 on r. If it does not, the "clamp to human mean" target needs a bias term that Gemma's matrices lack.
- Why the clamp probably blew up (hypotheses; none tested). The hook in `pod/variant.py` sets every token's projection, including BOS, template and left-pad tokens, to one document-mean value from human prose. It does this at 25 consecutive layers, and the correction is cast to bf16 and subtracted from a residual with huge-norm coordinates. BOS acts as an attention sink and carries massive activations (Sun, Chen, Kolter & Liu 2024, COLM, arXiv:2402.17762), so moving it is the likeliest failure.
- Diagnostic: rerun in fp32, skip positions before the reply, and log max|h| per layer to find the first non-finite value.
- Cost: minutes. Risks: the off-target disposition shifts reported for abliteration. Validation: the full battery plus surprisal.

**(iv) Better-fitting 2025-26 methods.** Steer2Edit on the prose direction (rank-1 edits only on the heads and neurons that write r), which targets the observed problem of fluency breaking before style changed. CreativityNeuro-style weight scaling with "plain human story" vs "typical story" prompts. Antislop's FTPO as a non-weight-edit baseline.

## 4. Recommendation

1. **α-sweep of the human-prose LoRA delta**, whole model and then MLP-only. It needs no new artifacts, it gives a dose-response curve, and it has the strongest support in the literature (task arithmetic, LoRA arithmetic, ExPO).
2. **Bake the 60-feature ablation**: first as the exact side branch, then as the least-squares `down_proj` edit, scored by how closely it matches the branch. The behavioural effect is already known, so success is easy to judge.

Run directional ablation (iii) only after the fp32/BOS diagnostic shows why the clamp diverged.
