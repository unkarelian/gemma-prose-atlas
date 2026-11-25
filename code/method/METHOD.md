# Making a small model's prose better: what worked, what did not

Tested on Gemma 3 4B-it. The recipe is three steps and takes about 20 minutes on one 24 GB GPU. It is a modest
improvement, measured by blind readers, and it comes with one clear warning about how *not* to measure it.

## The recipe

1. **Train a small adapter on prose you think is good.** Rank-16 LoRA on the attention and MLP projections,
   3 epochs, learning rate 1e-4, loss on the text only, in the model's own chat frame. We used 333 scenes from
   published novels, each paired with a short outline of the scene as the request.
   `python train.py pairs.jsonl adapter/`
2. **Write at temperature 0.7 with a repetition penalty of 1.05.** One sample. Adapter at full strength.
   `python write.py prompts.jsonl out.jsonl --adapter adapter/`
3. **Check refusals before you use the edited model for anything else** (see "Safety" below).

That is all of it. Everything else we tried made it worse.

## What it does

Blind readers (Claude Opus, given the project owner's prose standard, which penalises polish and stock phrasing and
rewards plain, specific writing) scored unlabelled openings 1 to 10 and ranked them. 48 held-out writing prompts
per round.

| | prose | coherence | fits the brief | ranked above unedited |
|---|---|---|---|---|
| Unedited model | 2.7 – 3.0 | 6.4 – 6.5 | 6.1 – 6.3 | |
| **Recipe** (round 2) | 3.9 | 4.9 | 6.0 | 33 of 48 |
| **Recipe** (round 3, fresh readers) | 4.2 | 4.8 | 5.7 | 28 of 48 |
| Human story for the same prompt | 5.9 | 6.3 | 6.2 | |

So: the recipe is preferred to the unedited model in 61 of 96 comparisons (64%). It removes the stock prose
(openings in the rain, the same few character names, "it wasn't X, it was Y", scents of something and regret) and
writes in a plainer, more specific voice. It pays for this in coherence: the edited model loses the thread more
often. It is still well short of the human story, and readers still identify most of its text as machine-written
(73–85%, against 100% for the unedited model). `SAMPLES.md` has four side-by-side examples, including the one
where it did worst.

## What did not work, and why it matters

**Do not select or tune by AI-text detector.** This is the main lesson. By detector score the first version of the
recipe was a complete success and the final one looks mediocre:

| | detector: share leaning AI | blind coherence | blind rank vs unedited |
|---|---|---|---|
| Unedited | 100% | 7.3 | |
| Adapter, temperature 1.0 | 6% | 4.3 | slightly worse |
| + repetition penalty 1.1 | 4% | 3.6 | worse |
| + best of 4 by detector | 0% | 3.3 | worst; never ranked first |
| Recipe (temperature 0.7, penalty 1.05) | 25% | 4.9 | better, 64% |
| Human | 2% | 6.6 | |

Each step that pleased the detector made the text less coherent, because to a detector disorder looks human.
Picking the detector's favourite of four samples reliably picked the least orderly one. The same held on the
adapter's home ground (scenes from outlines of held-out novels): coherence 6.7 unedited, 4.0 adapter, 2.5 with
penalty and picking, against 9.0 for the author.

Other things that did not help:

- **Sampling at temperature 1.0.** Human prose is high-entropy (Gemma finds it about twice as surprising per token
  as its own). A 4B model taught to write at that entropy cannot hold a thread when sampled at full temperature.
- **Lower still (0.5, 0.6).** No better than 0.7.
- **No repetition penalty.** At 0.7 without one the adapter loops (repeated three-word runs go from 3% to 10%) and
  readers rank it below the unedited model. A penalty of 1.1 overshoots.
- **Weaker adapter.** At 0.75 strength most of the old habits are back; at 0.5 all of them.
- **Lowering the temperature of the unedited model.** No change at all; the stock prose is its most likely output.
- **Plan first, then write.** Having the unedited model plan the beats and the adapter write them gave stiff
  scripts (22 of 48 against unedited).
- **Training on amateur stories** (r/WritingPrompts) instead of published prose: passes detectors even more
  easily, and in the samples we read it wanders more (not blind-tested at the final settings).
- **Asking the model itself which sample is better.** Its taste is not changed by the adapter. It still prefers the
  unedited model's prose 77% of the time, so it would pick the wrong one.
- **Removing the habits directly in the weights** (transcoder features baked into the MLP weights, see
  `../pod/tcbake.py`). This is precise (rain openings 61% → 8% with nothing else moved) and useful as a tool, but
  it deletes specific habits one at a time; the prose around them stays the same and is still flagged 100%.

## Safety

Changing a model's default voice can weaken its refusals. In our runs an adapter that taught a formal,
impersonal voice raised compliance with harmful requests from 12% to 55% (and to 72–81% for requests worded the way
an AI agent words them). The published-prose adapter above did not do that: 12% → 16% for plain wording, 14–21% →
22–25% for agent-style wording, the same small shift as a control adapter trained on ordinary answers. Check your
own adapter on a refusal set before and after; do not assume a style edit is only a style edit.

## Limits

- One model (Gemma 3 4B-it), one adapter size, 333 training scenes. A larger model should lose less coherence.
- The readers were a language model applying one person's stated standard, not a panel of people. Language models
  have their own taste for machine prose, which is the reason the standard was given to them explicitly.
- Openings of about 300 words only. Nothing here tests whether a full story holds together.
- The adapter in this write-up was trained on copyrighted novels and is not distributed. Train your own on prose
  you have the right to use.

## Files

- `train.py`, `write.py`: the recipe, standalone (torch, transformers, peft).
- `critic.py`: the detector measurements used above. A diagnostic, not a selector.
- `SAMPLES.md`: side-by-side openings.
- Numbers: `results/method_scores.json` (detector), `results/method_blind*.json` (blind reading).
