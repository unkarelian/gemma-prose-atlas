# Gemma prose atlas

How Gemma 3 4B-it writes fiction, why it prefers its own style, how it tells human writing from AI writing, and two ways of editing its prose habits out. Interpretability work with Gemma Scope 2 transcoders (34 layers, 16,384 features per layer).

This is research in progress on one small model. Numbers come from the experiments described here and have not been replicated elsewhere.

## Start here

- **`ATLAS.md`**: the prose atlas. 720 labelled transcoder features, by theme and by construction, readable on GitHub. One page per theme under `atlas/`.
- **`site/atlas.html`**: the same atlas, interactive (clone the repository and open it in a browser; `site/findings.html` has every result as a card).
- **`findings.json`**: all results in plain language with their numbers.
- **`code/pod/tcbake.py`**: transcoder-guided weight ablation, a method developed here (below).

## What was done

Gemma wrote the same briefs as humans and other models: 340 r/WritingPrompts prompts (human, Claude, GLM, Gemma) and 603 novel scenes from paraphrased outlines (the author, Haiku, GPT, GLM, Gemma). Every text was read back through the model in the frame it was written in, with all transcoders recording at every token (6,373 documents, 3.66 million text tokens). Briefs were split in half, novels by whole book; features and directions were found on one half and confirmed on the other.

## Main results

**Where the habits come from**
- 60% of Gemma's stories open with "The rain…". Across 340 unrelated prompts the first token is "The" with probability 0.97, and the next is " rain" with 0.69. The pretrained-only model gives " rain" 0.0001 on the same text: the habit is created by post-training.
- "Silas" appears in a third of its stories. "It wasn't X. It was Y." runs at 13 times the human rate; after "wasn't X." the next sentence starts with "It" 86% of the time.
- Its own sampled prose is its own top choice 81% of the time (0.58 nats per token against 3.4 for human prose).

**Why it rates AI prose highly**
- It prefers its own scene to the published author's 86% of the time, and other models' prose to human prose as well.
- The preference follows an internal "written by an LLM" direction, not predictability. Pushing a human passage along that direction, with its words unchanged, raises its rating and makes Gemma call it human.
- Asked outright, it gets authorship backwards: it says "AI" most for human text and least for its own, while two independent detectors and its own internal direction separate the two almost perfectly.

**How it tells human from AI writing**
- Attention writes about 89% of the signal at layer 18. Six heads (L26.H7, L17.H7, L20.H4, L16.H6, L18.H7, L15.H2) carry most of it; zeroing them removes about two-thirds, for Claude's prose as much as for Gemma's.
- Those heads read how sentences and paragraphs open, how dialogue is marked, and whether the connective words are casual.
- Normalising typography changes nothing. Shuffling the words inside each sentence destroys it. It is phrasing, not layout or vocabulary alone.

**Editing the habits out**
- A rank-16 LoRA trained on the human versions of half the briefs removes the habits on held-out prompts (rain openings 59% to 0%, stock words 43 to 4.8 per 1,000) and its stories are flagged as AI by an independent detector 2% of the time, the same as human stories.
- The model's taste does not follow: it still prefers original-Gemma prose 77% of the time and rates its own new writing lowest. Scaling the weight change moves the writing smoothly in both directions and leaves the preference flat. Writing, taste and the label "human" were installed together by post-training and can be moved separately.

## Method: transcoder-guided weight ablation

Removes chosen transcoder features from a model by a closed-form, low-rank edit of MLP output weights. No gradient training and no examples of the desired behaviour: the inputs are feature ids and ordinary text.

1. Ridge-regress each feature's activation on the MLP's own hidden neurons (one pass over text, silent tokens included as zeros).
2. Each feature becomes a rank-one edit of the output matrix: the neuron pattern that predicts it, times its decoder direction, corrected for Gemma's post-MLP scaling norm.

Tested on 60, 150 and 218 features across 17 layers, against exact run-time ablation of the same features:

| | P(" rain" after "The") | Side-effect KL, Gemma stories | Side-effect KL, ordinary requests | MMLU |
|---|---|---|---|---|
| Unedited | 69.2% | 0 | 0 | 58.2% |
| Exact run-time ablation (60 features) | 8.6% | 0.114 | 0.0023 | |
| Baked into weights (60 features) | 7.5% | 0.118 | 0.0024 | 58.4% |
| Projection of the same directions (baseline) | 61.0% | 0.27 | 0.16 | |
| Baked, random features (control) | 69.2% | 0.001 | 0.001 | 58.4% |

The 218-feature edit also takes "wasn't X. It was Y." from 2.02 to 0.15 per 1,000 words and stock names from 52% to 12% of stories, with MMLU at 58.6%. Merged into float32 weights it gives the same result as the low-rank form. Limits: one model and one family of features; it removes exactly what the features carry, so the overall AI signature of the prose, which lives mostly in attention, is unchanged (detectors still flag 100%). A literature search found no earlier work baking transcoder-feature ablations into weights; that is a search, not a guarantee.

Use: `python tcbake.py fit NAME features.json`, then `tcbake.apply(path, mode="bake")`. `bake_eval.py` runs the comparison above.

## Layout

- `code/pod/`: everything that runs on the GPU (corpus reading, feature selection, decision-point attribution, steering, judging, the mechanism and head analyses, LoRA training, the weight-ablation method).
- `code/analysis/`, `code/build/`: local analysis and the site and atlas builders. `code/method/`: external-critic scoring and reranking for prose.
- `results/`: one JSON per experiment. `data/`: Gemma's stories for the writing prompts, the directions, per-feature statistics for all 557,056 features, feature examples, stories from the edited models.

## Not included

Text of the published novels, the scene outlines made from them, and anything a model wrote from those outlines (copyright); a private set of author edits used in one analysis; per-token arrays that would reconstruct either. Experiments on refusals and on model identity from the same project are not part of this repository.

## Model welfare

No steering, prompting or optimisation aimed at pain, suffering, fear or distress in the model. Steering stays in the range where the model is coherent unless collapse is what is being measured.

## Caveats

One model. Feature labels were written by Claude from examples and are best guesses with a confidence level. Ratings and labels are read from single-token probabilities. Most comparisons use 40 to 110 briefs. The claim that the six heads drive Gemma's judgments is not yet established.

## Credits and licence

r/WritingPrompts stories are from the dataset of Fan et al. (2018). The stock-word list in `code/pod/slop_lists.json` is from Sam Paech's slop-score (MIT). Gemma Scope 2 transcoders are Google DeepMind's. No licence has been chosen for this repository yet.
