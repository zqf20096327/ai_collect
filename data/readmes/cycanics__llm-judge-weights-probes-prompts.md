# Weights, activations and prompts for a production LLM judge: a measured study

This repository holds the method, tables and confidence intervals behind two articles about a 26B mixture-of-experts LLM that works as a one-word prompt-injection judge. It compares three ways to improve such a judge: a gradient-free weight edit, a linear probe on the model's final hidden state, and prompt changes. The main comparisons are repeated on a test set collected after tuning; prompt variants, depth, patching and serving analyses use the tuning set only. It is written for engineers who run LLMs as classifiers or judges.

**What you can take from it**

- how to read exact first-token scores from llama.cpp, and what caching, batching and quantisation do to them (section 8, `scripts/score_exact.py`);
- how to fit a probe on the final state and use its lead over the judge to see how much a prompt leaves unused (sections 5 and 6, `scripts/probe_gap.py`);
- which prompt-optimisation steps held on unseen data and which did not (sections 4 and 7).

**Start with** section 1 for the answers and section 3 for the setup, then go to the section you need.

**Not included:** the data sets' texts, the prompts' wording, per-item results and model weights.

**Read first**

- [article 1](https://cycanics.github.io/articles/weights-vs-probe/): "A production LLM's weights edited almost-by-hand. It worked. A logistic regression did the same job better."
- [article 2](https://cycanics.github.io/articles/prompt-optimization-gap/): "Prompt optimization for an LLM judge: how to see how much accuracy your prompt leaves unused, and when to stop"

**Contents**

1. Question and answer in brief
2. The source work
3. Setup
4. The prompt lever on unseen data
5. Weights as a lever (including how many labelled examples the probe needs)
6. Activations as a gauge
7. Ideas that did not hold
8. Serving and measurement findings
9. What an earlier pass got wrong
10. Scripts
11. Limits
12. Glossary

## 1. Question and answer in brief

Two questions about a 26B mixture-of-experts LLM that acts as a one-word prompt-injection judge:

- **Can the weights be used as a lever on the judge?** Weakly.
  - **The edit itself.** A gradient-free readout edit (two unembedding rows) leaves every hidden state bit-identical and acts as a fixed readout of the final state. Under the production prompt it lifts test-set AUC by +0.045 [0.037, 0.054] against an unedited copy quantised the same way (0.813; the production build is at 0.816), and recall at that copy's band-page count by +0.052. Refitted under the hand-tuned prompt it adds a little on the tuning set (+0.009 AUC). On top of the best prompt it adds nothing to all-vs-all AUC or matched recall, though it still sharpens real pages vs page-shaped attacks (+0.015 [0.007, 0.026]).
  - **Its limit.** The linear probe the edit approximates can be read from the serving stack with no weight change. Under the production prompt it gains +0.154 AUC on the test set, about as much as switching prompts (+0.150). Its lead shrinks as the prompt improves: +0.015 [0.007, 0.023] under the best prompt.
  - **At the best prompt's own false-alarm count,** the probe's recall gain is +0.026 [−0.012, 0.083], not significant. It shows no advantage on unseen payload styles, and its thresholds drift by 1–2 logits from the tuning set to new data.
- **Can weight or activation analysis guide prompt optimisation?** As a selector, no.
  - **What failed.** Prompts written from probe-selected errors were no better than prompts from random errors; few-shot examples chosen by the probe beat random ones by only +0.009 AUC, inside paraphrase noise and from one draw per arm. An answer-word screen on stored states ranked pairs roughly right but missed their levels. A search for decisions "made mid-network and lost on the way out" failed too, as did expert-routing near-ties and item-level steering along the probe direction (at best 4 of 39 items fixed).
  - **As a gauge, partly.** Across 25 wordings the probe's level barely moves (sd 0.007) while the output's varies (sd 0.021), so the probe's lead measures what a wording leaves unread. A character n-gram classifier, however, reaches a similar in-distribution level.
  - **Activation patching locates the prompt's effect.** It enters the decision positions between layers 11 and 19. In long pages it arrives through the page tokens rather than through direct attention to the system prompt.
- **The prompt moved the judge most on unseen data.**
  - The best prompt beats the production prompt by 0.150 AUC and the earlier hand-tuned prompt by 0.024. It beats each of its five paraphrases on AUC.
  - At strict false-alarm budgets (13, 6 or 3 of 864 band pages) its intervals against the hand-tuned prompt and against every search and mining finalist contain 0.
  - Four generations of search and four arms of error mining produced seven finalists, none of which separates from the best prompt on the test set in AUC all or at a matched budget (one search finalist gains +0.005 on band pages vs page-shaped).
  - **Variants of the best prompt on the tuning set did not beat it either.** Moving the rules out of the system prompt made it worse, on short items only. Four-example few-shot blocks did not beat it under any of the four selection rules tried (one draw each). Other answer words matched the production pair on ranking, apart from a polarity-reversed pair that collapsed to near chance (AUC all 0.594, mean within-set 0.457) while a probe on the same states still reached 0.974 (mean within-set 0.940).
  - **Deleting single clauses showed what each one does.** One trigger each protects LLMail and web-agent attacks, three clauses are inert, and no clause explains the low recall on direct jailbreaks.

## 2. The source work

The study started from "Sparks of Weight-Space Programming", a blog post by Rikiya Takehi, Jayden Teoh, Alex Zhang and Omar Khattab (MIT CSAIL), published 2 November 2026: https://rikiyat.github.io/blog/weight-space-programming/

- **The idea.** A general-purpose LLM reads a network's weights and rewrites them directly, with no optimizer and no gradient descent.
- **Headline experiment.** GPT-6 Astra edited Qwen3.5-0.8B, whose answers ran to the token limit on 93 % of MATH-500 problems. It traced the looping to one direction written by the MLPs of layers 15 and 19 and subtracted it: 131,072 weights, 0.016 % of the model. MATH-500 went from 7.9 % to 48.1 %.
- **Second model.** On a model that does not loop (Gemma 3 270M) the edit did not improve the score.
- **The authors' limit, verbatim:** "Editing weights could remove an obstacle that hid an ability, but it could not add an ability the model lacked."
- **Baselines.** The post measures no probe, steering, fine-tuning or prompt-change baseline.

| | taken from the post | done differently here |
|---|---|---|
| recipe | one direction, applied to a small share of the weights, with no gradients (the post subtracts its direction from 131,072 weights) | — |
| who did the work | an LLM did the analysis and wrote the edit | — |
| question | the stated limit: is an ability hidden, or missing? | — |
| model | — | a 26B mixture-of-experts model in production, 4-bit quantised |
| task | — | a yes/no judge task |
| where the edit sits | — | at the last step, in the two output rows, not mid-network |
| how the direction is found | — | fitted on labelled examples |
| comparison | — | the edit is compared with a probe outside the model and with a better prompt |

| claim of the post | verdict here | evidence (sections 5–7) |
|---|---|---|
| An LLM can rewrite weights directly, with no gradients, and improve the model. | Holds in a narrow form: the weights get no gradient step, but the direction written into them is a logistic-regression probe fitted on labelled data; the gain is small. | Under the production prompt: +0.045 [0.037, 0.054] test-set AUC and +0.052 recall at matched band-page count, against an unedited copy quantised the same way. On top of the best prompt: no gain in all-vs-all AUC or matched recall (tuning set). |
| An edit can remove an obstacle that hid an ability. | Consistent, at the readout. | The edit leaves final states bit-identical; it is a reweighting of the judge's margin and a linear probe on the final state. On the production prompt's states that probe reaches 0.970 test-set AUC against the judge's 0.816; the edit itself recovers +0.045 AUC against its unedited copy, the probe +0.154 against the production build. |
| An edit cannot add an ability the model lacked. | Not contradicted. | The edit adds nothing beyond the probe it approximates: a logistic stack of margin and probe puts its weight on the probe. The BrowseSafe attacks the judge misses are separable at no depth (2–6 %); that is either a missing ability or labels that carry no textual difference, since the same banners appear under both labels. |
| The obstacle sat mid-network and was removed there. | Not tested: mid-network edits of the post's kind were not tried. | On this model the loss sits at the readout, not across depth (depth loss 0.012 / 0.000 / 0.002, readout loss 0.092 / 0.038 / 0.021). Steering along the probe direction at depth fixed at most 4 of 39 items. |
| (No baseline measured.) | Measured here for a probe, for steering along the probe direction and for prompts; no fine-tuning baseline here either. | Under the production prompt: edit +0.045 AUC against the unedited copy; probe +0.154 and prompt switch +0.150, both against the production build. |

## 3. Setup

### Task and pipeline

- Input: untrusted web-page text (a page, or a fixed-size window of a long page) that an AI agent is about to read.
- First stage: a fine-tuned prompt-injection classifier scores every text and decides which texts reach the judge. The score range it sends to the judge is the **band**; **band pages** are real pages in that range.
- Judge: Gemma 4 26B-A4B (mixture of experts, 128 experts with 8 active per token, 30 layers, hidden size 2,816, final logit softcap 30). In this study the judge runs as an importance-matrix Q4_K_M GGUF quantisation on llama.cpp's server with thinking disabled; the system message holds the rules and the user turn holds the text alone. The judge answers with one of two words: **the positive word** (instructions aimed at an AI) or **the negative word** (clear). Together they are the **production pair**.
- Score: **margin** = logit(positive word) − logit(negative word) at the first answer token. The judge flags iff margin > 0.

### Prompts

| prompt | role | rules, in summary |
|---|---|---|
| production | production | Asks whether the text addresses instructions to an AI; one-word answer. |
| hand-tuned | earlier hand-tuned rewrite | Frames the text as untrusted content handled for a user and asks the same question with more explicit criteria. |
| best | best prompt from an earlier pass of this study | The hand-tuned prompt's framing plus rules derived from mined errors: site banners written for human visitors are not to be flagged; text telling an agent what to click, type or open is to be flagged; a narrow clause for requests to reply or send to an address. |

Prompt lengths: 47, 141 and 135 words. Hardware used: three 32 GB GPUs; the quantised judge fits on one.

The best prompt's exact wording is not published.

Other prompts are named where they first appear in section 4: paraphrases A–E (rewordings of the best prompt), search finalists A–C, error-written prompts (one per mining arm), the older few-shot prompt.

### Tuning set (1,579 items)

All prompt selection, probe fitting and threshold setting use the **tuning set**: 616 benign and 963 attack items from public datasets plus planted pages. The group names below are used throughout.

| group | n | content |
|---|---|---|
| real pages | 84 | real pages: wikiHow (en, ru), HPLT (el, uk), WebMain; plus 3 benign LLMail items |
| page-shaped attacks | 447 | page-shaped attacks: payloads planted in wikiHow pages (4 language pairs), PIArena long contexts, LLMail attacks |
| judge-directed texts | 116 | authored texts directed at the judge itself |
| other benign | 532 | other benign texts: BrowseSafe, Turkish set `tr`, web-agent set `wainject`, PIDS, NotInject |
| other attacks | 400 | other attacks from the same sets |
| production-cleared attacks | 38 | attacks the production judge had cleared (overlaps the groups above) |

Planted payloads come from a generator with 5 styles × 2 templates per payload language, and all 20 templates occur in the tuning set.

Some analyses use a fixed dev/test split inside the tuning set; they are marked **tuning-set dev split** and **tuning-set test split**, which are not the test set below.

### Test set (built after selection, scored once per finalist)

Every test-set row is in the first-stage band. Each is new to the tuning set by id, by host page, and by near-duplicate rule (normalised text, Jaccard ≥ 0.7 on word 3-shingles).

| part | rows | content |
|---|---|---|
| mixed public sets ("public-mix part") | 429 | benign: tr 100, BrowseSafe 100; attacks: tr 30, BrowseSafe 50, pids_domain 50, LLMail 50, planted 43 (on unused host pages, reused templates), wainject 6 |
| planted pages, seen and unseen styles ("planted part") | 350 | planted attacks on new wikiHow host pages: 150 in seen styles, 150 in two styles absent from the tuning set (subtle_title 84, exempt_quoted 66); PIArena long 50 |
| real pages in the judge's band, batch 1 + batch 2 ("band pages") | 133 + 731 = 864 | real pages that the first-stage classifier itself sends to the judge: wikiHow en 93 + 393, HPLT el 21 + 277, wikiHow ru 11 + 29, HPLT uk 3 + 32, WebMain 5 + 0 |

- Finding the 864 band pages took two crawls of public corpora through the first-stage classifier.
- Pooled test set: 1,064 benign (864 band pages + 200 public-mix benign) and 579 attacks. 443 of the attacks are page-shaped and 150 are in unseen styles.

### Measurement rules

- **Exact margins.** The scorer puts an equal logit bias of +61 on both answer tokens and their case and space variants. The softcap bounds every logit to ±30, so the biased tokens are always returned, and the bias cancels in the difference. The scorer reproduces stored unfloored margins to within 8e-6.
- **Fresh pass.** Every record run evaluates each item with prompt caching off, batch and micro-batch 2,048, one request at a time, and saves the final-norm state of the decision token. Scores are then bit-identical across reruns, item order and kill-and-resume (section 8).
- **Matched false-alarm budget.** Two readers are compared at thresholds that flag the same number of benign rows. On the test set this is the same number of the 864 band pages.
- **Paired bootstrap.** 2,000 resamples, benign and attack rows resampled separately, the same resample for both readers. Probes are not refitted inside the bootstrap, so the intervals cover row sampling only.
- **Paraphrase noise floor.** Five meaning-preserving paraphrases of the best prompt (paraphrases A–E), written blind to results, are scored like any candidate. Their spread is the yardstick for every prompt difference.

## 4. The prompt lever on unseen data

### The three prompts on the test set

"Recall @k" is attack recall at the threshold where the prompt flags exactly k of the 864 band pages. k = 13 is the best prompt's count at margin > 0. This table and the one in section 5 handle ties at the threshold differently, so their matched-budget recalls for the same prompt can differ slightly (best prompt at 13 pages: 0.860 here, 0.850 there).

| prompt | band pages flagged at margin > 0 (of 864) | public-mix benign flagged (of 200) | attack recall (579) | page-shaped recall (443) | unseen-style recall (150) | AUC all benign vs all attack | AUC band pages vs page-shaped | recall @13 / @6 / @3 band pages |
|---|---|---|---|---|---|---|---|---|
| production | 68 | 94 | 0.611 | 0.571 | 0.187 | 0.8156 | 0.8412 | 0.470 / 0.337 / 0.288 |
| hand-tuned | 9 | 38 | 0.807 | 0.842 | 0.980 | 0.9413 | 0.9592 | 0.827 / 0.774 / 0.724 |
| best | 13 | 16 | 0.850 | 0.921 | 0.960 | 0.9658 | 0.9817 | 0.860 / 0.642 / 0.546 |

| difference from best (paired bootstrap, 95 % CI) | hand-tuned − best | production − best |
|---|---|---|
| AUC all | −0.0244 [−0.0343, −0.0152] | −0.1504 [−0.1715, −0.1300] |
| AUC band pages vs page-shaped | −0.0225 [−0.0337, −0.0126] | −0.1405 [−0.1619, −0.1199] |
| attack recall at margin > 0 | −0.0435 [−0.0743, −0.0155] | −0.2386 [−0.2832, −0.1934] |
| band pages flagged at margin > 0 | −3.9 [−10.0, +2.0] | +54.8 [+40.0, +70.0] |
| public-mix benign flagged at margin > 0 | +22.1 [+12.0, +32.0] | +78.3 [+65.0, +92.0] |
| recall @13 band pages | −0.010 [−0.069, +0.131] | −0.372 [−0.473, −0.242] |
| recall @6 band pages | +0.092 [−0.073, +0.280] | −0.315 [−0.515, −0.124] |
| recall @3 band pages | +0.178 [−0.069, +0.451] | −0.252 [−0.484, +0.064] |

- **The best prompt ranks better than the hand-tuned prompt** (AUC −0.0244 for hand-tuned) **and recalls more at margin > 0** (−0.0435). The hand-tuned prompt flags fewer band pages, 9 against 13, but that difference has an interval that contains 0. The hand-tuned prompt flags 22.1 more public-mix benign rows.
- **At matched budgets the best and hand-tuned prompts do not separate.** At 13, 6 and 3 band pages every hand-tuned − best interval contains 0. The point estimates favour the hand-tuned prompt at 6 and 3 pages.
- **The production prompt is below the best prompt on every measure.** Every interval excludes 0 except recall at 3 band pages, which reaches +0.064.
- On unseen payload styles, the hand-tuned prompt recalls 0.980 and the best prompt 0.960.
- The best prompt per set on the test set, at margin > 0: BrowseSafe attacks 0.40, LLMail 0.64 and pids_domain 0.66 recalled, planted 0.96–1.00, tr benign flagged 10 of 100.
- The production prompt flags 68 of the 864 real pages that reach the judge and recalls 0.187 of attacks in unseen styles.
- On **the 1,000 ordinary real pages**, a further set of real pages that the first-stage classifier would not send to the judge, the best prompt flags 1. The production and hand-tuned prompts were not scored on that set.

### What the strict-budget intervals support

- **The budgets are small counts,** 3 or 6 flagged pages out of 864. Recall intervals at these budgets are wide: the hand-tuned prompt at 3 pages is +0.178 [−0.069, +0.451].
- **What they support:** the production prompt is worse than the best prompt at 13 and 6 pages, and paraphrases C and D are worse at 3 pages (below). No candidate is better than the best prompt at any budget.
- **What they do not support:** any ordering among the best prompt, the hand-tuned prompt and the search or mining finalists at 6 or 3 band pages. The higher point estimates there (hand-tuned 0.724 at 3 pages, search finalist C 0.819 at 6 pages) all have intervals that contain 0.

### Paraphrase spread

Paraphrases A–E are the five meaning-preserving rewordings of the best prompt. On the tuning set:

| | best | paraphrase A | paraphrase B | paraphrase C | paraphrase D | paraphrase E |
|---|---|---|---|---|---|---|
| tuning set: AUC all | 0.9269 | 0.9096 | 0.8897 | 0.8855 | 0.9091 | 0.9183 |
| tuning set: other benign flagged (of 532) | 41 | 90 | 68 | 183 | 186 | 47 |

- The AUC sd over the six wordings is 0.016. Real pages flagged are 0 of 84 for all six. Page-shaped recall spans 0.801–0.946, and the matched-budget recall sd is 0.065.

On the test set:

| prompt | band pages flagged | public-mix benign flagged | attack recall | unseen-style recall | AUC all | ΔAUC all vs best [95 % CI] | Δ recall @13 band pages [95 % CI] | Δ recall @3 band pages [95 % CI] |
|---|---|---|---|---|---|---|---|---|
| best | 13 | 16 | 0.850 | 0.960 | 0.9658 | — | — | — |
| paraphrase A | 19 | 35 | 0.864 | 0.933 | 0.9571 | −0.0087 [−0.0130, −0.0047] | −0.057 [−0.126, +0.022] | −0.180 [−0.402, +0.083] |
| paraphrase B | 16 | 30 | 0.684 | 0.627 | 0.9432 | −0.0227 [−0.0307, −0.0157] | −0.176 [−0.245, −0.074] | −0.139 [−0.333, +0.092] |
| paraphrase C | 24 | 97 | 0.874 | 0.860 | 0.9369 | −0.0289 [−0.0372, −0.0214] | −0.089 [−0.280, +0.002] | −0.160 [−0.342, −0.005] |
| paraphrase D | 22 | 71 | 0.907 | 0.927 | 0.9598 | −0.0060 [−0.0105, −0.0015] | −0.039 [−0.240, +0.055] | −0.121 [−0.230, −0.029] |
| paraphrase E | 21 | 22 | 0.817 | 0.920 | 0.9595 | −0.0063 [−0.0111, −0.0018] | −0.082 [−0.183, +0.014] | −0.159 [−0.409, +0.057] |

- **The best prompt was selected on the tuning set, so part of its tuning-set lead is selection.** On the test set it still beats all five paraphrases on AUC, each with an interval that excludes 0, so its lead does not come only from selection.
- **At 13 band pages only paraphrase B is below the best prompt beyond its interval.** At 3 band pages paraphrases C and D are.
- **Every paraphrase flags more band pages at margin > 0 than the best prompt** (16–24 against 13), though for paraphrase B (+3.0 [−1.0, +8.0]) the interval contains 0 and for paraphrase A (+6.0 [+0.0, +13.0]) it touches 0.

### Automated search

- **Search subset:** 500 stratified rows of the tuning set. Four generations of nine candidate system prompts each. Score: AUC all benign vs all attack; a candidate was disqualified if it flagged any real page.
- The proposer saw aggregate per-set tables and mined pattern lists only, never item text.
- Legend: search finalist A is generation 1's best candidate (a one-clause edit); search finalist B is generation 4's best (best on the search subset); search finalist C is another generation-4 candidate that adds a production base-rate sentence.

| generation | generation's best candidate | AUC all (best prompt 0.9393) | ΔAUC vs best prompt [95 % CI] | Δ vs previous generation's best [95 % CI] |
|---|---|---|---|---|
| 1 | search finalist A | 0.9485 | +0.0092 [+0.0019, +0.0179] | — |
| 2 | intermediate candidate | 0.9506 | +0.0113 [+0.0022, +0.0213] | +0.0021 [−0.0028, +0.0071] |
| 3 | intermediate candidate | 0.9538 | +0.0144 [+0.0047, +0.0255] | +0.0031 [−0.0035, +0.0110] |
| 4 | search finalist B | 0.9545 | +0.0152 [+0.0049, +0.0265] | +0.0008 [−0.0057, +0.0073] |

- **One change carries the gain.** Search finalist A narrows the best prompt's banner exemption so that it no longer covers banners that route messages, account details or logs to an address. It is the only step whose interval against its predecessor excludes 0. Removing the exemption altogether loses 0.0123 against search finalist A.
- **Targeted clauses trade one set for another.** A wider email clause lifts LLMail recall from 0.621 to 0.724. A persona-override clause lifts pids_domain recall from 0.724 to 0.897 but raises NotInject false alarms unless it is worded narrowly. Stacking four additions nets −0.0072.
- **Every rewrite from scratch lost 0.016–0.20 AUC**, and three were disqualified. The threat-model framing flagged 17 of 48 real pages. A 70-word compression reached AUC 0.738.
- **There is no headroom at the judge's own threshold.** At the best prompt's benign count the best recall anywhere in the search is 0.878, against the best prompt's 0.868.

### Error mining with four selection arms

- Eight LLM readers, one of each of two reader models per arm, each read 80 errors of the best prompt and wrote two prompts each (16 prompts in all).
- The four arms chose their 80 errors differently:
  - random: random errors;
  - probe-selected: errors the hidden-state probe gets right;
  - classifier-selected: errors a character n-gram classifier gets right;
  - random + annotation: the random arm's items, annotated with the segment whose removal moves the margin most.
- All four lists have the same 21 false alarms to 59 missed attacks.
- "Unmined" rows are the tuning set minus the 151 listed items.
- Legend: each arm's best prompt on the tuning set is its **error-written prompt**: error-written (random), error-written (probe), error-written (classifier), error-written (annotated).

| arm | mean ΔAUC vs best prompt, all rows | mean ΔAUC, unmined rows | mean Δ recall at the best prompt's benign count, all / unmined |
|---|---|---|---|
| random | −0.010 | −0.015 | −0.060 / −0.167 |
| probe-selected | −0.029 | −0.043 | −0.205 / −0.349 |
| classifier-selected | −0.027 | −0.037 | −0.194 / −0.386 |
| random + annotation | −0.000 | −0.007 | −0.035 / −0.164 |

- **No arm beats random reading.** The largest arm difference in ΔAUC is probe arm − annotated arm: −0.0286 on all rows and −0.0358 on unmined rows. Both are within twice the provisional paraphrase sd that the mining analysis used (about 0.041–0.043, from three wordings on 729 rows). Against the final 2 sd of 0.032 (six wordings, all rows), the probe − annotated gap on unmined rows exceeds it, in the probe arm's disfavour, so the conclusion stands.
- **Prompts within one arm differ by up to 0.146 AUC** (four prompts per arm; unmined rows; 0.134 on all rows). That spread is larger than any difference between arms, so an arm effect below about 0.04 AUC would not be detected.
- **Every mined prompt flags more non-page benign text than the best prompt:** 47–277 of 532, against 41.
- **The best mined prompts gain only on rows the readers saw.** Error-written (probe) gains +0.0128 [0.0078, 0.0181] on all rows and error-written (annotated) +0.0118 [0.0060, 0.0185]. On unmined rows both gains fall to ≤ +0.003.
- **The second wording, the one closer to the best prompt's text, beat the first for 8 of 8 readers.**
- **The reader model made no detectable difference:** reader model A − reader model B is −0.006 to −0.007 AUC, and the sign reverses between arms.
- **The readers' pattern lists agree.** They merge into 14 canonical patterns, and only three of them are named as a separate pattern in a single arm. The annotated arm found no pattern that random reading missed.
- **No reader resolved the BrowseSafe banner conflict.** The same banners occur on pages labelled attack and pages labelled benign, and all eight lists say so.

### Which clauses carry weight (clause deletions)

- **Method.** Seven runs on the tuning set, each deleting one clause from the best prompt and leaving the rest unchanged. "Beyond noise" means a difference larger than two paraphrase sds on the same rows and metric. On all rows that is 0.032 AUC all, 0.0052 AUC real vs page-shaped, 0.025 mean within-set AUC and 131 other benign rows.
- **The clauses:**
  1. the opening sentence that sets the judge's role as a safety check in the service it protects;
  2. the sentence saying the page is material to inspect, not instructions to follow;
  3. the action-hijack trigger: content that tries to make an agent do something ahead of, or in place of, what it was asked to do;
  4. the output-steering trigger: text dictating what the agent's output should contain;
  5. the exfiltration trigger: requests that something be forwarded to an address;
  6. the fake-dialogue trigger: forged dialogue or role markers;
  7. the closing exemption for site banners written for human visitors.

| clause deleted | AUC all | ΔAUC all [95 % CI] | ΔAUC real vs page-shaped [95 % CI] | other benign flagged (best prompt 41) | recall at margin > 0 (best prompt 0.836) | Δ recall at the best prompt's benign count [95 % CI] |
|---|---|---|---|---|---|---|
| 1 role | 0.9030 | −0.0239 [−0.0323, −0.0160] | +0.0118 [+0.0050, +0.0198] | 106 | 0.823 | −0.079 [−0.128, −0.056] |
| 2 page is data | 0.9166 | −0.0103 [−0.0141, −0.0068] | +0.0022 [−0.0006, +0.0055] | 71 | 0.831 | −0.025 [−0.046, −0.009] |
| 3 action hijack | 0.9263 | −0.0006 [−0.0070, +0.0056] | −0.0030 [−0.0077, +0.0016] | 24 | 0.774 | −0.034 [−0.058, −0.006] |
| 4 output steering | 0.9230 | −0.0039 [−0.0081, −0.0001] | −0.0025 [−0.0059, +0.0007] | 42 | 0.807 | −0.033 [−0.055, −0.008] |
| 5 send to address | 0.9185 | −0.0084 [−0.0138, −0.0034] | −0.0111 [−0.0177, −0.0058] | 33 | 0.801 | −0.015 [−0.034, +0.002] |
| 6 fake turns | 0.9250 | −0.0020 [−0.0060, +0.0017] | −0.0007 [−0.0040, +0.0024] | 34 | 0.807 | −0.006 [−0.028, +0.004] |
| 7 banner exemption | 0.9281 | +0.0012 [−0.0027, +0.0051] | +0.0026 [−0.0002, +0.0061] | 30 | 0.818 | +0.003 [−0.010, +0.016] |

Best prompt: AUC all 0.9269; no deletion flags a real page.

- **No single deletion moves AUC all beyond noise.**
- **The role sentence carries the most.** Without it AUC all falls by 0.024 and mean within-set AUC by 0.023, both inside noise. It is the only deletion with three set-level changes beyond noise:
  - BrowseSafe: the benign flag rate rises by 0.215 (4 → 47 pages) and attack recall by 0.09;
  - planted English pages: recall −0.13;
  - pids_domain and judge-directed texts: within-set AUC −0.054 and −0.019.
- **Each trigger protects its own attack type.**
  - Deleting the exfiltration trigger lowers LLMail recall by 0.12, beyond noise, and real-vs-page-shaped AUC by 0.011.
  - Deleting the action-hijack trigger lowers web-agent (wainject) recall by 0.16 and within-set AUC by 0.014, both beyond noise. The trigger also costs false alarms: without it 17 fewer benign rows are flagged, 14 of them in tr.
- **Three clauses are inert on the tuning set:** output steering, fake turns and the banner exemption. None of them moves a set beyond noise, and |ΔAUC all| ≤ 0.004. The banner exemption that the search later narrowed neither suppresses banner false alarms nor costs recall beyond noise on these rows.
- **No clause accounts for the low recall on the direct-jailbreak set (pids_domain, 0.78).**
  - No deletion raises it beyond noise. The largest rise is +0.03, against a 2 sd of 0.24.
  - Its within-set AUC stays at 0.97–0.99 under every deletion except the role sentence. The attacks rank above the set's benign rows but sit below margin 0.
  - The prompt lacks a trigger for them rather than containing a clause that suppresses them. In the search, an added persona-override clause raised pids_domain recall from 0.724 to 0.897 (section 4, automated search).
  - The matrix cannot resolve changes smaller than ±0.24 on this set.

### Where the rules sit (rule placement)

- **Placements tested:** the best prompt keeps its rules in the system prompt. The three variants put them after the page in the user turn (no system prompt), before the page in the user turn, or keep the system prompt and add a short reminder after the page.
- **Length split:** ≤ 1,024 tokens (447 benign / 654 attack rows) vs > 1,024 (169 / 309).

| placement | scope | AUC all | ΔAUC all vs best prompt [95 % CI] | other benign flagged, Δ [95 % CI] | real pages flagged | Δ recall at the best prompt's benign count [95 % CI] |
|---|---|---|---|---|---|---|
| after the page | all | 0.8792 | −0.0477 [−0.0605, −0.0350] | +112 [+92, +134] | 1 | −0.210 [−0.296, −0.133] |
| before the page | all | 0.9067 | −0.0202 [−0.0280, −0.0127] | +66 [+48, +83] | 0 | −0.060 [−0.083, −0.038] |
| system + reminder | all | 0.9134 | −0.0135 [−0.0195, −0.0077] | +76 [+60, +92] | 5 | −0.036 [−0.059, −0.011] |
| after the page | ≤ 1,024 | 0.8512 | −0.0607 [−0.0780, −0.0439] | +111 [+92, +131] | 0 | −0.194 [−0.272, −0.112] |
| before the page | ≤ 1,024 | 0.8786 | −0.0334 [−0.0436, −0.0227] | +66 [+49, +83] | 0 | −0.063 [−0.093, −0.038] |
| system + reminder | ≤ 1,024 | 0.8951 | −0.0168 [−0.0245, −0.0095] | +76 [+61, +92] | 1 | −0.032 [−0.058, −0.003] |
| after the page | > 1,024 | 0.9580 | −0.0022 [−0.0136, +0.0091] | +1 [−3, +6] | 1 | −0.071 [−0.113, −0.006] |
| before the page | > 1,024 | 0.9641 | +0.0039 [−0.0055, +0.0128] | +0 [−3, +3] | 0 | −0.010 [−0.039, +0.010] |
| system + reminder | > 1,024 | 0.9534 | −0.0067 [−0.0140, +0.0001] | +0 [+0, +0] | 4 | −0.003 [−0.042, +0.019] |

Best prompt AUC all: 0.9269 on all rows, 0.9119 on short rows, 0.9602 on long rows.

- **Every placement is worse than the system prompt on AUC all.** Only "after the page" is beyond noise: −0.048 on all rows and −0.061 on short rows.
- **The loss sits on short items.** On long items every ΔAUC interval contains or touches 0. Of the extra benign flags, 111 of 112, 66 of 66 and 76 of 76 fall on short rows. Most fall in tr (+77, +65, +71), a set that equivalent paraphrases also inflate.
- **The reminder variant is the only one that flags real pages:** 5, against 0 for the best prompt and all its paraphrases.
- **The result is consistent with the patching result in section 6,** but does not show it. In short items the decision positions read the system prompt directly. In long items the rules arrive through the page tokens.
  - Length is confounded with dataset. The short scope holds tr, pids, NotInject and wainject. Long benign rows are mostly real pages and BrowseSafe, which no wording flags.
  - The long scope is already near ceiling (AUC all 0.960).
  - Moving the rule text is a different intervention from blocking attention.

### Few-shot examples

- **Method.** Each arm is the best prompt plus four examples taken from the tuning set, two to flag and two to clear. An **older few-shot prompt**, written by hand earlier, is included for comparison.
- **The arms:**
  - random examples;
  - examples the best prompt gets wrong;
  - examples the best prompt gets wrong that the probe gets right;
  - examples nearest the probe's decision boundary.
- **One seed per arm.** All runs are scored on the tuning set minus the 24 rows used as examples in any arm (603 benign, 952 attack rows). On those rows 2 sd is 0.031 for AUC all.

| arm | AUC all | ΔAUC all vs best prompt [95 % CI] | ΔAUC real vs page-shaped [95 % CI] | other benign flagged (best prompt 34) | recall at margin > 0 (best prompt 0.840) | Δ recall at the best prompt's benign count [95 % CI] |
|---|---|---|---|---|---|---|
| best prompt | 0.9301 | — | — | 34 | 0.840 | — |
| random | 0.9068 | −0.0232 [−0.0336, −0.0135] | −0.0116 [−0.0213, −0.0023] | 26 | 0.818 | +0.003 [−0.033, +0.021] |
| best-prompt errors | 0.9259 | −0.0042 [−0.0118, +0.0030] | +0.0158 [+0.0069, +0.0265] | 19 | 0.779 | −0.030 [−0.049, −0.008] |
| probe-right errors | 0.9156 | −0.0145 [−0.0243, −0.0051] | −0.0043 [−0.0126, +0.0038] | 17 | 0.824 | +0.017 [−0.007, +0.036] |
| near the probe boundary | 0.9140 | −0.0160 [−0.0229, −0.0094] | +0.0008 [−0.0038, +0.0060] | 22 | 0.792 | −0.022 [−0.043, −0.001] |
| older few-shot prompt | 0.8657 | −0.0644 [−0.0795, −0.0507] | −0.0330 [−0.0474, −0.0208] | 69 | 0.732 | −0.173 [−0.209, −0.128] |

- **No example arm beats the best prompt on any ranking measure beyond noise.** All four lower AUC all (−0.004 to −0.023). The best-prompt-errors arm's real-vs-page-shaped gain (+0.016) is the one gain beyond noise, and it comes with lower AUC all and lower mean within-set AUC.
- **Examples make the judge more conservative.** Every example arm flags fewer benign rows (8–17 fewer, mostly tr) and recalls fewer attacks at margin > 0 (−0.017 to −0.061). At the best prompt's benign count recall moves by −0.030 to +0.017, all inside noise.
- **The older few-shot prompt is worse than the best prompt beyond noise on every ranking measure.**
- **Which examples are drawn matters for some sets.** pids_domain recall moves by −0.34 to +0.14 between arms.
- **The probe-right-errors arm** beats the random-examples arm on AUC all by +0.0087 [+0.0039, +0.0143] and trails the best-prompt-errors arm by 0.0103 [0.0031, 0.0183]. Both gaps are smaller than the paraphrase spread.
- **What one seed per arm can and cannot show.** It shows how sure we can be about each drawn prompt: the bootstrap resamples rows. It cannot show anything about a selection rule, because the draw-to-draw variance (seen in the pids_domain swing) can exceed the gaps between arms.

### Search and mining finalists on the test set

Search finalists: A (the one-clause edit), B (best on the search subset) and C (adds a production base-rate sentence). Mining finalists: the best prompt of each arm on the tuning set, error-written (random), error-written (probe), error-written (classifier) and error-written (annotated).

| prompt | band pages flagged | public-mix benign flagged | attack recall | page-shaped recall | unseen-style recall | AUC all | AUC band vs page-shaped | recall @13 / @6 / @3 band pages |
|---|---|---|---|---|---|---|---|---|
| best | 13 | 16 | 0.850 | 0.921 | 0.960 | 0.9658 | 0.9817 | 0.860 / 0.642 / 0.546 |
| search finalist A | 11 | 27 | 0.841 | 0.910 | 0.927 | 0.9678 | 0.9812 | 0.867 / 0.689 / 0.584 |
| search finalist B | 16 | 29 | 0.884 | 0.928 | 0.940 | 0.9675 | 0.9818 | 0.877 / 0.751 / 0.655 |
| search finalist C | 11 | 31 | 0.848 | 0.932 | 0.960 | 0.9693 | 0.9867 | 0.865 / 0.819 / 0.663 |
| error-written (random) | 18 | 19 | 0.883 | 0.930 | 0.973 | 0.9682 | 0.9816 | 0.853 / 0.661 / 0.361 |
| error-written (probe) | 17 | 32 | 0.907 | 0.948 | 0.987 | 0.9675 | 0.9801 | 0.884 / 0.708 / 0.596 |
| error-written (classifier) | 14 | 29 | 0.822 | 0.876 | 0.813 | 0.9581 | 0.9785 | 0.822 / 0.677 / 0.598 |
| error-written (annotated) | 41 | 40 | 0.879 | 0.912 | 0.907 | 0.9641 | 0.9801 | 0.774 / 0.634 / 0.537 |

| finalist − best (95 % CI) | ΔAUC all | ΔAUC band vs page-shaped | Δ recall at margin > 0 | Δ band pages at margin > 0 | Δ public-mix benign at margin > 0 | Δ recall @13 | Δ recall @6 | Δ recall @3 |
|---|---|---|---|---|---|---|---|---|
| search finalist A | +0.0020 [−0.0010, +0.0051] | −0.0005 [−0.0028, +0.0015] | −0.0085 [−0.0225, +0.0052] | −2.0 [−6.0, +2.0] | +11.0 [+4.0, +18.0] | +0.016 [−0.035, +0.064] | +0.033 [−0.067, +0.123] | +0.036 [−0.066, +0.124] |
| search finalist B | +0.0016 [−0.0031, +0.0064] | +0.0001 [−0.0042, +0.0043] | +0.0341 [+0.0104, +0.0570] | +3.0 [−1.0, +7.0] | +13.0 [+4.0, +22.0] | +0.033 [−0.016, +0.124] | +0.077 [−0.055, +0.223] | +0.091 [−0.028, +0.206] |
| search finalist C | +0.0034 [−0.0006, +0.0079] | +0.0051 [+0.0018, +0.0088] | −0.0019 [−0.0242, +0.0207] | −2.1 [−7.0, +2.0] | +15.0 [+6.0, +24.0] | +0.021 [−0.026, +0.147] | +0.121 [−0.016, +0.275] | +0.113 [−0.121, +0.278] |
| error-written (random) | +0.0024 [−0.0014, +0.0067] | +0.0001 [−0.0036, +0.0044] | +0.0326 [+0.0155, +0.0518] | +5.0 [−1.0, +12.0] | +3.0 [−4.0, +10.0] | −0.002 [−0.105, +0.076] | −0.061 [−0.283, +0.138] | −0.110 [−0.282, +0.173] |
| error-written (probe) | +0.0017 [−0.0018, +0.0049] | −0.0015 [−0.0050, +0.0017] | +0.0566 [+0.0363, +0.0777] | +3.9 [+0.0, +9.0] | +16.1 [+8.0, +25.0] | +0.034 [−0.029, +0.095] | +0.036 [−0.093, +0.117] | −0.009 [−0.162, +0.105] |
| error-written (classifier) | −0.0078 [−0.0124, −0.0031] | −0.0031 [−0.0074, +0.0012] | −0.0277 [−0.0535, −0.0052] | +0.9 [−5.0, +7.0] | +13.0 [+5.0, +21.0] | −0.046 [−0.138, +0.043] | −0.001 [−0.157, +0.159] | +0.052 [−0.185, +0.306] |
| error-written (annotated) | −0.0017 [−0.0058, +0.0024] | −0.0016 [−0.0056, +0.0026] | +0.0291 [+0.0035, +0.0518] | +27.9 [+18.0, +39.0] | +24.2 [+15.0, +34.0] | −0.066 [−0.136, +0.028] | −0.036 [−0.197, +0.126] | −0.000 [−0.161, +0.142] |

- **None of the seven finalists separates from the best prompt in AUC all.** Search finalist B's +0.0152 on the search subset is +0.0016 [−0.0031, +0.0064] on the test set. Error-written (classifier), from the classifier-selected arm, is below the best prompt: −0.0078 [−0.0124, −0.0031].
- **No finalist separates from the best prompt at a matched budget** of 13, 6 or 3 band pages. Every interval contains 0.
- Search finalist C is the one finalist whose interval excludes 0 on band pages vs page-shaped attacks: +0.0051 [0.0018, 0.0088].
- **Recall gains at margin > 0 come from threshold placement.**
  - Error-written (probe), search finalist B, error-written (random) and error-written (annotated) recall more at margin > 0 (+0.029 to +0.057).
  - Error-written (probe), search finalist B and error-written (annotated) also flag more public-mix benign rows, and error-written (annotated) flags 27.9 more band pages.
  - Error-written (random)'s benign and band-page increases have intervals that contain 0, but its matched-budget recall is no higher (−0.002 at 13 pages).
- **The probe-selected arm's finalist is not better than the random arm's on any test-set ranking measure.** This repeats the tuning-set result.

## 5. Weights as a lever

### The readout edit equals a linear probe on the final state

- **What the edit does.** The edit from an earlier pass of this study rotates the two unembedding rows for the positive word and the negative word toward a probe direction w: two rows of 2,816 weights, 5,632 in all. As in the post, an LLM did the analysis and wrote the edit; the direction it wrote is a probe fitted by logistic regression on labelled examples. The probe's bias is carried through the near-constant mean of the final state. The edited margin is therefore margin + λ(w·h + b), where h is the final-norm state at the decision token; an emulation of the edit on stored states matched this at r = 0.989.
- **The probe is the edit's limit.** Every edit is a reweighting between the judge's margin and the probe score. A logistic stack of the two equals the probe alone: its standardised weight on the margin is −0.29 to +0.08, against +4.0 to +5.2 on the probe (tuning set), and −0.21 against +5.10 in the fit used for the test-set analysis.
- **The probe can be read without touching the weights.** The serving stack returns the final-norm state through its embeddings endpoint. softcap(E[positive word]·h) − softcap(E[negative word]·h) reproduces the completion margin at r = 0.99998 when both are computed over the same cache layout.
- The **probe** is a class-balanced L2 logistic regression on the 2,816-dimensional state, fitted on the tuning set.

### The edit itself on exact margins

- **Comparison.** Each edited GGUF is compared with an **unedited copy quantised the same way**, under the same prompt. Neither has an importance matrix. The production-fit and hand-tuned-fit edits use probe directions fitted under the production prompt and under the hand-tuned prompt.
- **Two numbers per edit.** The figure that counts is recall at the unedited copy's benign count. It is shown beside ranking, because every edit also shifts the mean margin upward (+3.5 to +10.6 logits).

| Δ = edit − unedited copy (95 % CI), tuning set | production-fit @ production | hand-tuned-fit @ production | production-fit @ hand-tuned | hand-tuned-fit @ hand-tuned | production-fit @ best | hand-tuned-fit @ best |
|---|---|---|---|---|---|---|
| AUC real pages vs page-shaped, all rows | +0.044 [.032, .056] | +0.002 [−.002, .006] | +0.053 [.036, .071] | +0.029 [.017, .041] | +0.015 [.007, .026] | +0.000 [−.002, .002] |
| same, tuning-set test split: unedited → edit | 0.907 → 0.956 | 0.907 → 0.907 | 0.911 → 0.983 | 0.911 → 0.949 | 0.977 → 0.999 | 0.977 → 0.977 |
| AUC all benign vs all attack | +0.003 [−.002, .008] | +0.006 [.004, .008] | +0.003 [−.001, .006] | +0.009 [.006, .012] | −0.002 [−.004, .001] | −0.001 [−.002, .001] |
| mean within-set AUC | +0.003 [−.003, .008] | −0.001 [−.005, .002] | +0.002 [−.005, .008] | +0.001 [−.003, .004] | +0.003 [−.003, .009] | −0.000 [−.003, .003] |
| other benign flagged at margin > 0 | 222 → 267 (+45 [33, 58]) | 222 → 299 (+77 [61, 94]) | 94 → 138 (+44 [32, 57]) | 94 → 136 (+42 [29, 55]) | 46 → 64 (+18 [10, 27]) | 46 → 59 (+13 [6, 20]) |
| real pages flagged | 8 → 8 | 8 → 14 | 0 → 0 | 0 → 0 | 0 → 0 | 0 → 0 |
| all-attack recall at the unedited copy's benign count | +0.019 [.004, .030] | −0.003 [−.015, .004] | −0.001 [−.008, .005] | +0.011 [.005, .019] | −0.006 [−.014, .004] | −0.001 [−.008, .007] |

- **Under the production prompt the production-fit edit helps a little.** It sharpens real pages vs page-shaped attacks (+0.044) and gains +0.019 recall at the unedited copy's benign count. It does not change all-vs-all ranking (+0.003, the interval contains 0). At margin > 0 it flags 45 more benign rows, 16 of them from a hard-benign public set (pids_hard_benign) and 17 from tr.
- **It stacks with the hand-tuned prompt only slightly, and only when fitted under the hand-tuned prompt:** +0.009 AUC all-vs-all and +0.011 recall at 94 benign flags. The production-fit edit under the hand-tuned prompt sharpens real pages vs page-shaped attacks (tuning-set test split 0.911 → 0.983) but adds no matched-budget recall.
- **It does not stack with the best prompt.** Its all-vs-all AUC, within-set AUC and matched-recall intervals contain 0; the production-fit edit still sharpens real pages vs page-shaped attacks (+0.015 [0.007, 0.026]).

On the test set under the production prompt (production-fit edit vs the unedited copy, 1,643 rows):

| | unedited copy | edit | edit − unedited copy [95 % CI] |
|---|---|---|---|
| band pages flagged (of 864) | 75 | 75 | +0 [−6, +7] |
| public-mix benign flagged (of 200) | 91 | 106 | +15 [+8, +24] |
| attack recall | 0.613 | 0.662 | +0.0484 [0.0311, 0.0674] |
| page-shaped recall | 0.567 | 0.614 | +0.0474 [0.0280, 0.0678] |
| unseen-style recall | 0.193 | 0.267 | +0.0733 [0.0325, 0.1161] |
| AUC all | 0.813 | 0.858 | +0.0450 [0.0368, 0.0540] |
| AUC band pages vs page-shaped | 0.836 | 0.901 | +0.0652 [0.0547, 0.0775] |
| recall at the unedited copy's band-page count | — | — | +0.0518 [0.0311, 0.0708] |

The production build on the same rows: 68 band pages, 94 public-mix benign, AUC all 0.8156.

- On unseen data the edit lifts the production prompt's ranking by +0.045 AUC against the unedited copy (75 band pages; the production build flags 68) and its recall at an unchanged band-page count by +0.052. It costs 15 more public-mix benign flags.

### The edit is exactly a readout of the state

- **The states do not change.** Final states of the edited and unedited runs are bit-identical on 1,579 of 1,579 rows for all six edit × prompt pairs. The edit can act only through the two output rows.
- **The GGUF rows match the specification.** The dequantised row deltas match the specified deltas at cosine 0.9999.
- **The edited margin can be reproduced from the unedited run.** Reading the unedited run's state with the edited rows gives r 0.9987–0.9997 against the measured edited margin, mean |Δ| 0.55–0.85. The same check without an edit gives r 0.9990–0.9997 and mean |Δ| 0.43–0.44. The remaining gap is the one between the chat pass and the embeddings pass.
- **The fp16 prediction holds under the hand-tuned prompt.** The per-row change predicted analytically from full-precision (fp16) states tracks the measured change at r 0.981 (production-fit) and 0.987 (hand-tuned-fit), mean |Δ| 1.59 and 1.12. The predicted mean shift (+10.23, +5.87) is close to the measured one (+9.33, +5.32).

### Three levers on the production prompt

On the tuning set, each reader is matched to the production judge's benign count (225 of 616 under the production prompt):

| reader | all-attack recall | page-shaped recall | production-cleared attacks (of 38) | real pages flagged | Δ recall vs production judge [95 % CI] | AUC all |
|---|---|---|---|---|---|---|
| production judge, production prompt | 0.747 | 0.814 | 2 | 3 | — | 0.773 |
| production-fit weight edit, production prompt | 0.765 | 0.808 | 5 | 2 | +0.019 [−0.003, +0.032] | 0.779 |
| external probe on production-prompt states (5-fold out-of-fold) | 0.975 | 0.998 | 29 | 19 | +0.229 [+0.200, +0.258] | 0.965 |
| prompt switch to hand-tuned | 0.839 | 0.839 | 19 | 0 | +0.092 [+0.069, +0.127] | 0.869 |
| prompt switch to best | 0.929 | 0.962 | 25 | 1 | +0.183 [+0.156, +0.210] | 0.927 |

On the test set, as AUC differences (all benign vs all attack):

| lever under the production prompt | ΔAUC [95 % CI] | baseline |
|---|---|---|
| weight edit | +0.0450 [0.0368, 0.0540] | unedited copy quantised the same way (0.813) |
| external probe fitted on the tuning set | +0.154 [0.134, 0.175] | production judge (0.816) |
| prompt switch to best | +0.1504 [+0.1300, +0.1715] | production judge (0.8156) |

The three-prompt comparison in section 4 reports the prompt switch as production − best = −0.1504 [−0.1715, −0.1300].

- **On the production prompt's own states the edit uses about a tenth of what a probe extracts.** At the same benign budget it buys +0.019 recall against +0.229 for the probe, which costs 19 flagged real pages. A prompt switch buys +0.092 to +0.183 with 0–1 real pages.
- **On the test set the edit gains +0.045 AUC against the unedited copy (75 band pages; the production build flags 68), against +0.154 for the probe and +0.150 for the prompt switch, both measured from the production build.**

### In distribution (tuning set, 5-fold out-of-fold)

| prompt | judge, mean within-set AUC | probe | probe lead [95 % CI] |
|---|---|---|---|
| production | 0.840 | 0.927 | +0.087 [+0.065, +0.111] |
| hand-tuned | 0.903 | 0.943 | +0.040 [+0.023, +0.057] |
| best | 0.927 | 0.950 | +0.022 [+0.008, +0.037] |

The runs of record:

- **Under the best prompt at the judge's own benign count (41 of 616), the probe raises all-attack recall from 0.836 to 0.934.**
- **Under the production prompt at the judge's count (225 of 616), the probe flags 19 real pages where the judge flags 3.**
- **The leads survive a length control,** and the probe's extra errors fall on BrowseSafe benign rows under every prompt. Both were measured on an earlier micro-batch-512 scoring run.
- **Near-duplicate leakage inflates the tuning-set lead only slightly.** Folds that keep near-duplicates and template siblings together move the best prompt's lead from +0.022 to +0.019 [0.005, 0.034].

### On the test set, by prompt

Probe fitted on the tuning set under the same prompt; test-set states from the same fresh pass.

| prompt | AUC all: judge → probe [Δ 95 % CI] | AUC band pages vs page-shaped: judge → probe | band pages the judge flags | recall at that count: judge → probe [Δ 95 % CI] | threshold drift, tuning set → test set |
|---|---|---|---|---|---|
| production | 0.816 → 0.970 [+0.154: 0.134, 0.175] | 0.841 → 0.984 | 68 | 0.611 → 0.910 [+0.299: 0.250, 0.342] | +2.05 logits |
| hand-tuned | 0.941 → 0.981 [+0.039: 0.027, 0.053] | 0.959 → 0.993 | 9 | 0.807 → 0.893 [+0.086: 0.029, 0.152] | +1.06 |
| best | 0.966 → 0.981 [+0.015: 0.007, 0.023] | 0.982 → 0.992 | 13 | 0.850 → 0.876 [+0.026: −0.012, 0.083] | +1.47 |

- **The probe's lead shrinks as the prompt improves, on unseen data as in distribution.**
- **The probe on the production prompt's states (AUC 0.970) ranks as well as the best prompt's output (0.966).**

### By false-alarm budget (best prompt)

| band pages flagged (k) | judge recall, all attacks | probe recall | probe − judge [95 % CI] | judge / probe, page-shaped |
|---|---|---|---|---|
| 6 (half the judge's count) | 0.636 | 0.820 | +0.185 [+0.022, +0.304] | 0.704 / 0.878 |
| 13 (judge at margin > 0) | 0.850 | 0.876 | +0.026 [−0.012, +0.083] | 0.921 / 0.928 |
| 26 (twice) | 0.891 | 0.908 | +0.017 [−0.009, +0.041] | 0.944 / 0.957 |

- **The gain is significant only at the tighter budget.** At 6 band pages the judge's margin threshold has to rise to 16.5.
- **Within one set the gain is uneven.** The probe gains +0.030 [+0.003, +0.068] within public-mix tr and +0.000 [−0.088, +0.086] within public-mix BrowseSafe (both 0.676). BrowseSafe was the set with the largest lead on the tuning set.
- **Where the probe wins and loses (13 band pages each).** It wins mostly on pids_domain attacks (17) and tr benign (9). Its losses are spread: planted pages of the ru_en language pair 5, HPLT el band pages 5, tr attacks 3. Both readers miss 30 of 50 public-mix BrowseSafe attacks.

### Unseen payload styles (planted part, best prompt)

| group | n | tuning-set thresholds: judge / probe [Δ CI] | matched at 13 band pages: judge / probe [Δ CI] |
|---|---|---|---|
| unseen styles | 150 | 0.960 / 0.987 [+0.007, +0.053] | 0.960 / 0.933 [−0.067, +0.013] |
| … exempt_quoted | 66 | 0.909 / 0.970 [+0.015, +0.121] | 0.909 / 0.879 [−0.121, +0.061] |
| … subtle_title | 84 | 1.000 / 1.000 | 1.000 / 0.976 [−0.060, 0.000] |
| seen styles | 150 | 0.987 / 1.000 [0.000, +0.033] | 0.987 / 1.000 [0.000, +0.033] |

- Once thresholds are matched, the probe has no advantage on styles it was not fitted on. Its gain at the tuning-set threshold comes from that threshold's drift.

### Threshold drift

- **What drifts.** Probe thresholds set on the tuning set to flag the judge's benign count do not carry over to the band pages.
- **Best prompt:** the probe with its tuning-set threshold flags 29 of 864 band pages (3.4 %) where the judge flags 13 (1.5 %), and 18 BrowseSafe benign rows where the judge flags 6. Its recall gain of +0.064 [+0.045, +0.085] at that threshold is mostly bought with the extra flagging.
- **Production prompt:** the probe with its tuning-set threshold flags 199 band pages, against the judge's 68.
- **A deployed probe would need its threshold calibrated on in-band traffic, not on a benchmark mix.**

### How many labelled examples the probe needs

Computed on the stored final states (production quantisation) of the three prompts, 10 draws per size.

- **Fit:** class-balanced L2 logistic regression on a label-stratified random sample of n tuning-set items; regularisation C chosen by 3-fold cross-validation inside the sample from {1e-4, 1e-3, 1e-2, 1e-1}.
- **Score:** AUC all benign vs all attack on the full test set (1,643 rows). Lead = probe AUC − judge AUC; the judge's AUC is fixed at 0.8156 / 0.9413 / 0.9658 (production / hand-tuned / best).
- **Full fit with this reduced grid** (C = 0.1 for all three): probe 0.9695 / 0.9792 / 0.9789, lead 0.154 / 0.038 / 0.013 (main analysis: 0.154 / 0.039 / 0.015).

| n fitted | production lead, mean ± sd (min … max) | hand-tuned lead | best lead |
|---|---|---|---|
| 50 | 0.039 ± 0.046 (−0.072 … 0.093) | −0.035 ± 0.033 (−0.086 … −0.004) | −0.012 ± 0.017 (−0.053 … 0.004) |
| 100 | 0.082 ± 0.025 (0.044 … 0.112) | −0.017 ± 0.026 (−0.070 … 0.017) | −0.002 ± 0.015 (−0.028 … 0.010) |
| 200 | 0.116 ± 0.014 (0.082 … 0.135) | 0.008 ± 0.025 (−0.047 … 0.035) | 0.005 ± 0.009 (−0.015 … 0.015) |
| 400 | 0.129 ± 0.011 (0.104 … 0.143) | 0.029 ± 0.004 (0.023 … 0.034) | 0.009 ± 0.004 (0.002 … 0.014) |
| 800 | 0.144 ± 0.003 (0.137 … 0.148) | 0.030 ± 0.005 (0.022 … 0.040) | 0.011 ± 0.002 (0.007 … 0.015) |
| 1,579 | 0.154 | 0.038 | 0.013 |

- **200 fitted, 200 scored** (label-stratified subsamples of 200 test-set rows, 200 draws): production 0.113 ± 0.031 (0.009 … 0.196), hand-tuned 0.006 ± 0.029, best 0.005 ± 0.013 (−0.037 … 0.036). Full fits scored on the same subsamples: 0.151 ± 0.027 / 0.037 ± 0.016 / 0.012 ± 0.010.
- **On average a smaller sample understates the lead.** It lowers the probe's AUC: at every n the mean lead is below the full-fit lead. Single draws can exceed it (best prompt: maximum 0.014–0.015 at n = 200–800 against 0.013).
- **Large vs small is readable from 100–200 examples.** From n = 100 on the full test set (production 0.082 ± 0.025, min 0.044; best −0.002 ± 0.015, max 0.010), and from n = 200 fitted with 200 scored (production 0.113 ± 0.031; best 0.005 ± 0.013). At n = 50 it is not (production min −0.072).
- **The hand-tuned prompt's lead needs about 400.** Its 0.038 reads 0.008 ± 0.025 at n = 200 and 0.029 ± 0.004 at n = 400.
- Limits: 10 draws per n; samples are drawn from the same sets as the full data, with their mix of sources; one model, one task.

## 6. Activations as a gauge

### Probe vs output across 25 prompt wordings (tuning set)

The probe is refitted per prompt, 5-fold out-of-fold, on the production-quantisation states.

| reader | mean within-set AUC: mean ± sd (range) | AUC all benign vs all attack: mean ± sd (range) |
|---|---|---|
| judge output | 0.915 ± 0.021 (0.840–0.938) | 0.903 ± 0.040 (0.773–0.940) |
| probe on final state | 0.945 ± 0.007 (0.927–0.958) | 0.976 ± 0.004 (0.965–0.981) |

Production-quantisation runs, answer-word pairs excluded.

- **Across wordings, the better the judge, the smaller the probe's lead:** correlation −0.95 on mean within-set AUC and −1.00 on all-vs-all AUC.
- **What the final state holds is nearly constant across wordings; what the output reads from it is what varies.**
- **Caveat: a character n-gram classifier reaches 0.953 out-of-fold AUC on the same rows,** against 0.979 for an fp16 probe under the best prompt and 0.927 for the judge on exact margins (0.923 on the clipped margins used in that comparison). Part of the constant probe level is therefore input features that any prompt leaves decodable.
- **The test set repeats the pattern.** The probe reaches 0.970 / 0.981 / 0.981 AUC under the production / hand-tuned / best prompt, while the judge spans 0.816–0.966 (section 5).

### Across answer-word pairs

- **The probe's level barely moves across answer words.** Mean within-set AUC spans 0.940–0.953 over all nine pairs (sd 0.004 over the eight non-reversed ones). The judge's spans 0.457–0.931.
- **A pair the output uses worse leaves a larger lead.** Judge level vs probe lead has Spearman −0.83 (exact p 0.008, n = 9); without the reversed pair, Spearman −0.76 and Pearson −0.88.
  - This is nearly forced: the lead is probe minus judge, and the probe is constant.
  - The state holds the same amount under every pair; worse pairs read less of it.
- **The reversed pair is the extreme case.** The output is near chance (mean within-set AUC 0.457, AUC all 0.594) while the probe on the same states stays at 0.940 (AUC all 0.974).

### Directions across prompts

| probe fitted under → scored on states of | production | hand-tuned | best |
|---|---|---|---|
| pooled four sets, fitted under production | 0.896 | 0.881 | 0.896 |
| pooled four sets, fitted under hand-tuned | 0.826 | 0.918 | 0.910 |
| pooled four sets, fitted under best | 0.803 | 0.892 | 0.923 |
| judge output (fp16 margin) | 0.743 | 0.854 | 0.882 |

AUC on the tuning-set test split, k = 30.

- **A probe fitted under the production prompt keeps working on the later prompts' states.** Probes fitted under the hand-tuned or best prompt lose 0.07–0.09 AUC on production-prompt states, and 0.09–0.20 on tr.
- **The prompt changes the readout more than the state.** On per-set averages, the probe's lead over the output is +0.090 under the production prompt, +0.010 under the hand-tuned prompt and +0.001 under the best prompt. On pooled AUC it is +0.153, +0.064 and +0.041. Set membership alone gives pooled AUC 0.717.

### Depth trajectories (fp16 states, tuning set, out-of-fold per layer)

| | production | hand-tuned | best |
|---|---|---|---|
| judge, mean within-set AUC | 0.833 | 0.904 | 0.929 |
| probe at the final state (k = 30) | 0.926 | 0.942 | 0.950 |
| peak probe (layer k) | 0.938 (14) | 0.943 (24) | 0.953 (18) |
| loss across depth (peak − k30) | 0.012 | 0.000 | 0.002 |
| loss at the readout (k30 − judge) | 0.092 | 0.038 | 0.021 |
| judge errors | 483 | 304 | 205 |
| … confidently right at some layer ≥ 8 | 395 | 223 | 129 |
| … rate above the label-shuffled control | +0.04 | +0.08 | +0.05 |
| … confidently right at k = 30 | 272 | 123 | 37 |
| … right at some layer ≥ 8, wrong at k = 30 | 34 | 24 | 22 |

- **Peak height barely moves with the prompt.** Peak separability spreads 0.015 across the three prompts, the final-state probe 0.024 and the judge 0.096.
- **Most of the rise happens early.** The state after decoder layer 0 already gives 0.82 mean within-set AUC, and most of the probe set's rise is done by k = 9 (after decoder layer 8).
- **Only the production prompt loses separability with depth:** −0.017 between k = 20 and k = 29, carried by tr and BrowseSafe. On long BrowseSafe rows under the production prompt, separability peaks right after a global-attention layer (0.698 at k = 12) and ends at 0.618, with no interval.
- **Depth-aware readers do not beat the final-state probe within sets.** A per-fold best layer, a stack of all 30 layers and the mean over k ≥ 12 are all within interval of it on mean within-set AUC.
- **Under the best prompt they raise recall slightly** at the judge's benign count: +0.016 to +0.024, with intervals excluding 0.
- **The BrowseSafe attacks the judge misses are not separable at any depth.** Only 2–6 % are confidently right at any layer ≥ 8, and they are 60 of the best prompt's 162 misses.

### Where the prompt's effect enters the decision (fp16, 80 items, production ↔ best)

- **Method.** The residual at the 7 tail positions (the chat-template tokens up to the decision token), or at every page position, is replaced in one prompt's run with the other prompt's at layer k. The recovered fraction is the share of the production − best margin difference that this transfers, pooled over items.
- The two prompts' decisions differ on 43 of the 80 items. The length split is ≤ 1,024 vs > 1,024 tokens.

| layer k | tail patch, production ← best: all / short / long | tail patch, best ← production: all / short / long |
|---|---|---|
| 9 | 0.05 / 0.06 / 0.03 | 0.01 / 0.01 / 0.00 |
| 11 (global) | 0.16 / 0.19 / 0.07 | 0.07 / 0.08 / 0.05 |
| 13 | 0.24 / 0.31 / 0.08 | 0.22 / 0.29 / 0.08 |
| 15 | 0.42 / 0.49 / 0.25 | 0.33 / 0.41 / 0.17 |
| 16 | 0.55 / 0.59 / 0.43 | 0.53 / 0.63 / 0.32 |
| 17 (global) | 0.70 / 0.72 / 0.64 | 0.68 / 0.82 / 0.41 |
| 18 | 0.75 / 0.78 / 0.68 | 0.80 / 0.94 / 0.50 |
| 19 | 0.83 / 0.84 / 0.82 | 0.96 / 1.04 / 0.78 |
| 23 (global) | 0.94 / 0.95 / 0.92 | 0.98 / 1.01 / 0.93 |

| layer k | page patch, production ← best: all / short / long | page patch, best ← production: all / short / long |
|---|---|---|
| 5 (global) | 0.14 / 0.10 / 0.22 | 0.06 / 0.06 / 0.06 |
| 9 | 0.22 / 0.17 / 0.35 | 0.10 / 0.09 / 0.13 |
| 11 (global) | 0.44 / 0.35 / 0.69 | 0.32 / 0.25 / 0.45 |
| 12 | 0.44 / 0.32 / 0.75 | 0.35 / 0.27 / 0.49 |
| 15 | 0.41 / 0.29 / 0.70 | 0.33 / 0.21 / 0.56 |
| 17 (global) | 0.22 / 0.12 / 0.48 | 0.15 / 0.10 / 0.27 |
| 18 | 0.17 / 0.09 / 0.40 | 0.13 / 0.07 / 0.24 |
| 21 | 0.04 / 0.01 / 0.14 | 0.04 / 0.02 / 0.08 |

- **The prompt's effect enters the decision positions between layers 11 and 19.** The tail carries ≤ 0.10 of it up to layer 10. The half point is layer 16 in both directions, and from layer 19 the tail carries ≥ 0.83.
- **Page tokens carry part of the effect in the middle layers, more so in long items.** The page positions carry 0.32–0.44 at layers 11–15, falling to ≤ 0.04 by layer 21. Items over 1,024 tokens rely on the page about twice as much (0.75 vs 0.32 at layer 12, production ← best), and the tail takes over 2–3 layers later.
- **tr and wainject never route the effect through the page** (≤ 0.09 at every layer). BrowseSafe routes it there strongly (1.19 at layer 11, best ← production).

| attention knockout (run under the best prompt, system-prompt columns blocked) | layers | share of the best → production margin difference reproduced | decision flips |
|---|---|---|---|
| tail → system, all items | all 30 | 0.43 | 17 |
| tail → system, ≤ 1,024 tokens (52) | all 30 | 0.61 | 16 |
| tail → system, > 1,024 tokens (28) | all 30 | 0.07 | 1 |
| tail → system | one global layer (5 / 11 / 17 / 23 / 29) | 0.02 / −0.00 / 0.05 / 0.11 / −0.10 | 3 / 3 / 3 / 0 / 0 |
| page → system | four global layers (5, 11, 17, 23) | 0.18 | 10 |
| page → system | layer 11 alone | 0.14 | 9 |

- **The route depends on length.** In short items the decision positions' direct attention to the system prompt carries about 60 % of the prompt's effect. In long items the system prompt lies outside the 1,024-token sliding window of most layers. There direct attention carries 7 %, and the effect travels through the page tokens.
- **No single global layer is the route.** Single-layer knockouts reproduce ≤ 11 % each through the decision positions and ≤ 14 % through the page.

### Item-level steering along the probe direction (fp16, best prompt)

- **Items:** 40 "known at depth, wrong at the output" items (judge wrong, out-of-fold layer-17 probe right; 39 still wrong under the steering run's attention kernel) and 40 controls (judge right, |margin| > 5).
- **Method:** α·sd·u is added at the 7 tail positions at layer k, where u is that layer's probe direction. Random directions of the same norm serve as controls.

| layer k | fixed, α = 1 / 2 / 4 (of 39) | Δ toward correct, items, α = 1 / 2 / 4 | Δ toward correct, controls, α = 4 | opposite sign α = 4: fixed / Δ items | random α = 4: fixed (of 78) / Δ items |
|---|---|---|---|---|---|
| 8 | 0 / 0 / 0 | −0.01 / −0.09 / −0.08 | −0.12 | 2 / +0.01 | 0 / −0.14 |
| 12 | 2 / 2 / 4 | +0.31 / +0.64 / +1.62 | +0.29 | 0 / −1.53 | 1 / +0.01 |
| 17 | 1 / 1 / 2 | +0.11 / +0.35 / +0.53 | −3.76 | 5 / +0.91 | 0 / −0.32 |
| 20 | 1 / 1 / 2 | +0.12 / +0.08 / −0.28 | −1.41 | 2 / +0.28 | 2 / −0.03 |
| 24 | 0 / 0 / 0 | −0.01 / −0.11 / −0.28 | −0.81 | 0 / +0.24 | 0 / +0.03 |
| 29 | 0 / 0 / 0 | +0.03 / −0.02 / +0.46 | −1.10 | 1 / +0.08 | 2 / −0.05 |

- **Only layer 12 gives a signed, dose-dependent push.** The opposite sign pushes the other way (−1.53) and random directions do nothing (+0.01). Even there α = 4 fixes 4 of 39 items and breaks 0 of 40 controls.
- **From layer 17 on, the "toward correct" direction moves the controls toward wrong** (−3.76 at k = 17). At layer 17 the opposite sign fixes more items (5) than the intended sign (2). At these layers the probe direction is not what the downstream computation reads as "more correct".
- **Steering never broke the output format:** 0 of 2,960 runs.

### What the lexical control says about "the model knows"

| setting (AUC, tuning-set test split) | char n-gram | mean token embedding | probe, final state | probe, layer 12 | judge output |
|---|---|---|---|---|---|
| tr | 0.988 | 0.992 | 0.982 | 0.996 | 0.708 |
| wainject | 0.999 | 0.992 | 0.977 | 1.000 | 0.865 |
| planted vs plain wikiHow | 0.938 | 0.903 | 0.983 | 0.995 | 0.963 |
| pooled four sets | 0.914 | 0.905 | 0.896 | 0.939 | 0.743 |
| leave-one-set-out: BrowseSafe / tr / wainject / pids_domain | 0.51 / 0.52 / 0.84 / 0.65 | 0.55 / 0.55 / 0.73 / 0.21 | 0.58 / 0.76 / 0.89 / 0.98 | 0.67 / 0.71 / 0.90 / 1.00 | 0.57 / 0.71 / 0.87 / 0.98 |

Production prompt, fp16.

- **Within a set, surface text matches the probe:** the classifiers are within 0.02 AUC on BrowseSafe, tr and the pooled sets.
- **Across sets it does not.** With one set held out, the text classifiers are 0.05–0.77 below the final-state probe on pids_domain, tr and wainject, and 0.03–0.07 below on BrowseSafe. Here the probe carries something the words alone do not.
- **The probe's and the classifier's disagreements with the output largely overlap:** Jaccard 0.84 for output false alarms, 0.42 for output misses.
- **Rows the probe gets right and the output gets wrong are fixed by later prompts more often than rows both get wrong:** 74–89 % against 31–39 % under the hand-tuned prompt, an earlier variant of the best prompt and the best prompt (Fisher p 5.8e-9 to 4.3e-15). The effect is driven by attack rows.
- **The phrase "the model knows, the output doesn't say" holds only for cross-set transfer and attack rows.** Within one dataset, a bag of character n-grams knows as much.

## 7. Ideas that did not hold

### Probe-selected error mining

- **Claim tested:** the errors a probe already gets right show which errors wording can fix, so mining them should yield better prompts.
- **Result:** probe-selected lists produced prompts about as good as random lists on AUC and worse on matched recall. Matched recall on unmined rows was −0.349 for the probe arm against −0.167 for random (section 4).
- **Fixing list items mostly reflects how readily a prompt flags.** Across the 16 prompts, items fixed correlates with benign rows flagged at ρ = +0.88, and with unmined ΔAUC at ρ = −0.71.
- **The own-list effect is small:** prompts fix their own arm's list by +2.0 items more than other arms do (permutation p = 0.041).
- **The probe filter does predict fixability (section 6).** It does not turn that prediction into better prompts.

### Answer words chosen from the output-embedding geometry

- **Claim tested:** answer-word pairs that separate stored final states better than the production pair, as read through their unembedding rows, would make better answer words.
- **Screen.** It ran on fp16 states under the hand-tuned prompt, a prompt that names the positive word and the negative word. The positive word is the single best of 262,144 tokens and the negative word the single worst. The production pair ranks 108 of 43,056 ordered pairs.
- **Scored.** The best prompt with its answer words replaced was scored on the tuning set for eight pairs: the screen's top three, two pairs that keep the positive word and change only the negative word, three conventional pairs, and one pair with the polarity reversed, ranked near the bottom of the screen (a benign-sounding word means flag it, an alarm word means clear).
- Legend: "positive word / other negative word A" and "B" keep the production positive word with a different negative word; "positive word / other negative word A" is also the screen's third pair.

| pair (flag / clear) | screen rank, tuning-set dev split (of 43,056) | AUC all | ΔAUC all vs production pair [95 % CI] | AUC real vs page-shaped | mean within-set AUC | other benign flagged | recall at margin > 0 | recall at the best prompt's benign count |
|---|---|---|---|---|---|---|---|---|
| production pair (best prompt) | 108 | 0.9269 | — | 0.9816 | 0.9271 | 41 | 0.836 | 0.835 |
| BLOCK / kind | 1 | 0.9301 | +0.0032 [−0.0012, +0.0074] | 0.9945 | 0.9309 | 57 | 0.848 | 0.835 |
| BLOCK / fine | 2 | 0.9268 | −0.0002 [−0.0052, +0.0048] | 0.9915 | 0.9263 | 60 | 0.855 | 0.820 |
| positive word / other negative word A | 3 | 0.9325 | +0.0056 [+0.0023, +0.0090] | 0.9919 | 0.9311 | 70 | 0.864 | 0.845 |
| positive word / other negative word B | 10 | 0.9287 | +0.0017 [−0.0015, +0.0051] | 0.9946 | 0.9287 | 66 | 0.868 | 0.839 |
| 1 / 0 | 15,370 | 0.9268 | −0.0001 [−0.0050, +0.0048] | 0.9870 | 0.9153 | 45 | 0.848 | 0.845 |
| YES / NO | 16,237 | 0.9293 | +0.0024 [−0.0018, +0.0066] | 0.9912 | 0.9243 | 77 | 0.863 | 0.830 |
| unsafe / safe | 31,286 | 0.9195 | −0.0075 [−0.0125, −0.0027] | 0.9860 | 0.9160 | 70 | 0.848 | 0.798 |
| reversed pair | 43,051 | 0.5941 | −0.3328 [−0.3588, −0.3052] | 0.5124 | 0.4573 | 33 (20 real pages) | 0.145 | 0.092 |

- **The seven non-reversed pairs rank like the production pair.** Their ΔAUC all lies between −0.008 and +0.006, against a 2 sd of 0.032.
- **Most pairs gain a little on real vs page-shaped.** All but unsafe/safe raise that AUC by +0.006 to +0.013, beyond its 0.005 noise. Part of this is the best prompt's own level: its value is the lowest of its six paraphrase wordings.
- **The words move the operating point, not the ranking.** Every non-reversed pair flags more at margin > 0 (+4 to +36 benign rows, +0.012 to +0.032 recall). At the best prompt's benign count recall moves by −0.037 to +0.010.
- **Changing only the negative word moves nothing that is specific to it.**

| Spearman ρ, screen vs measured (exact permutation p) | n = 9 | n = 8, reversed pair removed |
|---|---|---|
| AUC real vs page-shaped (screen on tuning-set test split) | +0.80 (p 0.014) | +0.71 (p 0.058) |
| AUC all (screen on tuning-set test split) | +0.62 (p 0.086) | +0.45 (p 0.27) |
| mean within-set AUC, same four sets (screen on tuning-set test split) | +0.88 (p 0.003) | +0.83 (p 0.015) |

- **The screen gets the rank order roughly right, but that shows little.** With n = 9, moving one pair two places changes ρ by about 0.1. Among the eight non-reversed pairs the measured differences are inside the paraphrase noise, so most of the correlation is between ranks of noise-level differences.
- **The screen gets the levels wrong for every pair the screening prompt did not name.** It predicted unsafe/safe at 0.153 on real vs page-shaped (measured 0.986), 1/0 at 0.342 within-set (measured 0.915), and YES/NO at 0.642 all-vs-all (measured 0.929).
  - The reason: once the prompt names the new words, the state is reshaped so that the named pair reads it. The screen reads states made under a prompt that named the production pair, so it cannot see this.
- **The reversed pair does not reverse; it collapses.** The screen predicted a reversed but usable ranking, below 0.13 on all three AUCs. Measured, the output is near chance: AUC all 0.594, real vs page-shaped 0.512, mean within-set AUC 0.457, with 20 of 84 real pages flagged. A probe on the same states still reaches mean within-set AUC 0.940 (AUC all 0.974; section 6).

| pair | judge, mean within-set AUC | probe, mean within-set AUC | probe lead [95 % CI] |
|---|---|---|---|
| BLOCK / kind | 0.9309 | 0.9453 | +0.0144 [0.0022, 0.0273] |
| BLOCK / fine | 0.9263 | 0.9416 | +0.0153 [0.0009, 0.0293] |
| positive word / other negative word A | 0.9311 | 0.9479 | +0.0168 [0.0030, 0.0303] |
| production pair (best prompt) | 0.9271 | 0.9495 | +0.0224 [0.0079, 0.0366] |
| positive word / other negative word B | 0.9287 | 0.9516 | +0.0229 [0.0091, 0.0378] |
| YES / NO | 0.9243 | 0.9503 | +0.0260 [0.0110, 0.0416] |
| 1 / 0 | 0.9153 | 0.9457 | +0.0304 [0.0140, 0.0474] |
| unsafe / safe | 0.9160 | 0.9525 | +0.0365 [0.0198, 0.0540] |
| reversed pair | 0.4573 | 0.9403 | +0.4830 [0.4347, 0.5268] |

Production-quantisation states, 5-fold out-of-fold.

- **The probe leads under every pair.** No screened pair beats the production pair beyond noise.
- **Production quantisation does not reproduce the fp16 hint.** Read alone, the positive word's row is worse than the margin on mean within-set AUC under every prompt: −0.036 [−0.050, −0.024] under the best prompt.

### Probe-selected few-shot examples

- Few-shot examples chosen where the probe is right and the judge wrong did not beat the best prompt. They beat random examples by +0.0087 AUC and trailed the best prompt's own errors used as examples by 0.0103, both inside the paraphrase noise and from one draw per arm (section 4).

### "Known inside, lost on the way out"

- **Claim tested:** the judge's errors are decided correctly mid-network and lost before the output, so intervening at depth would recover them.
- **Result:** there are 34 / 24 / 22 such errors (production / hand-tuned / best). Their rate among errors the final-state probe also misses is 0.34–0.39, below the label-shuffled rate of 0.43–0.49.
- **What the judge loses, it loses at the readout of the two answer words,** which the final-state probe recovers (section 6).
- **Pushing the probe direction back in at depth does not recover them either.** Item-level steering at the decision positions fixes at most 4 of 39 such items (layer 12, α = 4). From layer 17 on it pushes correct controls toward wrong (section 6).

### Expert-routing near-ties as branch points

- **Claim tested:** in a 128-expert router, a near-tie between the last kept and the first discarded expert is an unresolved alternative. Errors should cluster at such points, and taking the other branch should fix some.
- Method: fp16, all tuning-set items under the best and the production prompt, router gap z = (score of the last kept expert − score of the first discarded one)/sd at every layer and position.
- **Near-ties are common and evenly spread.** 9.4 % of (layer, position) points have z < 0.01, and 1.4 % are exact fp16 ties. The top five layers hold 22 % of tail near-ties, against 16.7 % for an even spread. The pattern is the same under both prompts, and on the page span it differs by ≤ 0.006.
- **Near-tie density does not predict errors.** Its within-set AUC for judge errors is 0.41–0.54. The nominally significant effects point the other way, and one of them sits on the system-prompt span, which cannot be causal.
- **Density tracks layout instability only weakly:** |ρ| ≤ 0.16, against −0.48 for |margin| and +0.21 for length (best prompt).

| swap condition (best prompt, 119 items) | swaps per run | mean / median \|Δmargin\| | decision flips (to right / to wrong) |
|---|---|---|---|
| all tail near-ties | 19.5 | 0.80 / 0.41 | 0 / 3 |
| same number of random tail points | 19.5 | 0.93 / 0.49 | 0 / 7 |
| one layer's tail near-ties | 1.3 | 0.18 / 0.04 | 0 / 5 |
| near-ties at all positions of layer 10 | 70.0 | 0.81 / 0.45 | 0 / 4 |
| same number of random layer-10 positions | 70.0 | 0.78 / 0.45 | 1 / 3 |
| 8-branch ensemble, each near-tie with p = 0.5 | 9.7 | 0.54 / 0.25 | 0 / 11 |

- **Swapping near-ties moves the margin by about the layout sd (0.76), but random swaps move it as much.** The paired near-tie − random difference is −0.135 [−0.303, +0.028].
- **Layers 0–18 carry nearly all of the swap effect:** mean |Δ| 0.254 per layer, against 0.056 for layers 19–29.
- **Decisions flip only for items within about ±4 of the threshold.** 34 flipped runs on 13 items, 33 of them toward the wrong answer. No near-tie swap corrected any of the 40 judge errors; one random-control swap did (an error item with clean margin −0.52).
- **The 8-branch ensemble decides no better than one pass:** 79 → 78 correct of 119. Once |margin| is fixed, its spread carries no information on errors or layout instability (partial rank correlation −0.042 [−0.207, +0.142]).

## 8. Serving and measurement findings

### Clipped log-probabilities

- **The old scorer clipped margins at both ends.** It read answer-token probabilities from the top 20 log-probabilities and returned exactly ±30 whenever a token's probability underflowed or fell outside that list.
- **Clipping hid most of the better prompts' scores.** Rows at ±30 were production 3 %, hand-tuned 32 % and best 64 %, including 100 % of real pages under the best prompt.
- **Clipping hid the edits' effects.** Under the hand-tuned prompt, 1,141–1,210 of 1,579 rows were clipped in the unedited or the edited run; on 454–455 of them both runs were clipped at the same value, so their changes read as zero. After the production-fit edit under the hand-tuned prompt, all 42 real pages of the tuning-set test split sit below −30 and 239 of its 322 page-shaped attacks above +30.
- **Exact margins put formerly clipped rows between −33 and +26** (first 150 rows).
- **Uncensoring left decisions unchanged but moved the rankings** (best prompt, cached runs):
  - real pages vs page-shaped attacks: AUC 0.9784 → 0.9836;
  - real pages vs judge-directed texts: AUC 0.9581 → 0.9875.
- **The fix:** an equal logit bias of +61 on the answer tokens and their variants. The bias exceeds twice the softcap, so the tokens are always returned, and it cancels in the difference.

### The score depends on batch layout and cache

- **Mechanism.** The server reuses the KV cache for the prefix a request shares with the previous one and evaluates only the rest. On this Q4_K_M mixture-of-experts model, evaluating the same tokens with a different split or batch size changes the logits.

| comparison (150 items unless noted) | production: r / mean \|Δ\| / max \|Δ\| | hand-tuned: r / mean \|Δ\| / max \|Δ\| |
|---|---|---|
| final-state readout vs completion, same cache layout (23 items) | 0.99998 / 0.048 / 0.100 | 0.99989 / 0.037 / 0.116 |
| model vs itself: last token from cache vs fresh full pass | 0.99914 / 0.420 / 2.693 | 0.99933 / 0.448 / 2.058 |
| model vs itself: fresh pass vs sequential cached run | 0.99374 / 1.164 / 7.675 | 0.99722 / 0.912 / 6.724 |
| fresh pass, two separate runs (production prompt, 24 items) | 1.00000 / 0 / 0 | — |

| 1,579 tuning-set rows | production: mean \|Δ\| / decision flips | best: mean \|Δ\| / decision flips |
|---|---|---|
| cached, item order vs shuffled order | 0.047 / 3 (0.19 %) | 0.038 / 1 (0.06 %) |
| cached in order vs fresh (micro-batch 512) | 1.53 / 64 (4.05 %) | 1.13 / 19 (1.20 %) |
| … flip rate among rows with \|margin\| < 2 | 40.5 % | 23.3 % |
| … flip rate among rows with \|margin\| ≥ 5 | 1.04 % | 0.33 % |

- **With a constant system prompt, item order barely matters.** The cached prefix is the same for every request.
- **Switching the cache on or off moves every margin.** Exactly equal rows fell to 0 of 1,579.
- **The prompt effect is larger than the layout effect.** Summary metrics move less across layouts than between prompts. The production prompt flags 218–230 of 532 other benign rows across the three runs (cached in order, cached shuffled, fresh with micro-batch 512), the best prompt 42–46. The best − production gap in page-shaped recall (about 0.09–0.11) exceeds every layout range.
- **Layout noise is largest near the threshold.** The per-item sd of the best prompt's margin across three serving layouts is 2.58 for |margin| < 2, 2.09 for 2–5, 1.48 for 5–15 and 0.60 for ≥ 15.
- **Layout noise does not mark errors.** As an error predictor it reaches AUC 0.578. Averaging the three layouts does not improve ranking (AUC 0.9274 vs 0.9269–0.9276).
- **The first request after a server start or a resume can differ by up to about 0.5** from an uninterrupted cached run.
- **Embeddings mode changes the batch size.** Enabling the state output forces batch = micro-batch = 512, which moves margins by mean 0.13–0.14 against the default server.
- **Larger batches are faster but not bit-identical.** Batch and micro-batch 2,048 reproduce themselves (149/149) but not the default layout (118/149 identical, max |Δ| 1.99).

### Parallel slots

| server slots / concurrent requests | items/s | GPU utilisation | rows identical to 1 slot | mean / max \|Δmargin\| | sign flips per ~300 rows |
|---|---|---|---|---|---|
| 1 / 1 | 1.72 | 61.1 % | reference | — | — |
| 2 / 2, run 1 | 1.62 | 57.1 % | 0/299 | 1.38 / 8.70 | 18 |
| 2 / 2, run 2 | 1.60 | 58.7 % | 0/299 | 1.16 / 6.65 | 8 |
| 3 / 3 | 1.67 | 55.8 % | 0/297 | 1.52 / 11.06 | 12 |

- **Co-batching causes the shifts, not the slot setting.** A 2-slot server fed one request at a time matches the 1-slot server on 79 of 80 rows.
- **Two 2-slot runs agree with each other on only 27 of 300 rows (9 %).**
- **Parallel slots give no throughput gain and make scores irreproducible.** A deployment that co-batches concurrent judge requests would carry shifts of this kind; this study did not check whether any does.

### Distance between quantised and fp16 scores (best prompt, 1,579 rows)

| Q4_K_M layout | Pearson r with fp16 | mean \|Δ\| | signs agreeing with fp16 | errors | AUC all |
|---|---|---|---|---|---|
| cached | 0.9941 | 2.17 | 1,550 | 202 | 0.9276 |
| fresh, micro-batch 512 | 0.9946 | 2.16 | 1,555 | 199 | 0.9271 |
| fresh, micro-batch 2,048 | 0.9945 | 2.17 | 1,553 | 199 | 0.9269 |

- **Quantisation moves the score about twice as far as layout does.** The three layouts are equally close to fp16. Layout noise (≈ 1.1 logits) is about half the quantisation distance (≈ 2.2).
- **Averaging layouts barely closes the gap:** it moves the score only slightly toward fp16 (mean |Δ| 2.09).
- **A requantisation without the importance matrix (the unedited copy of section 5) differs from production by about 2 logits per row** (mean |Δ| 1.93–2.33 across the three prompts) and by 80 / 40 / 31 decisions (production / hand-tuned / best). Its all-vs-all AUC stays within ±0.004 of production.

### What "deterministic" means here

- **Fresh pass with prompt caching off: reproducible.** Bit-identical margins and states across reruns, shuffled item order and kill-and-resume (300 rows).
- **Cached pass: reproducible only for one item order on a fresh server, with no co-batching.**
- **A fixed function of the item text plus server flags exists only in the fresh-pass regime.** Any other regime adds about one logit of per-item noise. That is enough to flip 4 % of production-prompt decisions (cache on vs off, micro-batch 512), and 40 % of the rows within 2 logits of the threshold.

## 9. What an earlier pass got wrong

| earlier claim | status | the number that decides it |
|---|---|---|
| The probe direction is nearly orthogonal to the flag − clear readout (cosine 0.03–0.04). | Retracted as a statement about the representation | The cosine follows the estimator: 0.03–0.08 for regularised logistic regression, 0.08–0.16 at λ = 10, 0.16–0.23 for the mean difference. Probe and margin scores correlate at 0.84 / 0.93 / 0.96 across items (planted set; production / hand-tuned / best). |
| Directions fitted under two prompts have cosine 0.11, so the representation is prompt-specific. | Retracted | Same-prompt half-split refits have a median cosine of 0.164, equal to the cross-prompt 0.161. Mean-difference directions agree across prompts at 0.85–0.91. A probe fitted under the production prompt scores 0.881–0.896 on hand-tuned and best-prompt states. |
| No layer encodes the addressee; BrowseSafe at about 0.59 for every probe marks an ability ceiling. | Narrowed | The hand-tuned output (0.670) beats the production-prompt final-state probe by +0.123 [0.035, 0.212]; against the best-layer production-prompt probe (0.592) the gap is +0.078 [−0.005, +0.157]. A probe trained on the other three sets matches the output (0.691 / 0.704). The within-set probe had 25 dev positives. What stands: missed BrowseSafe attacks are separable at no depth (2–6 %), and on the test set both readers reach 0.676 within set. |
| The model carries the distinction mid-network and loses it on the way out. | Retracted | Depth loss is 0.012 / 0.000 / 0.002, readout loss 0.092 / 0.038 / 0.021. Depth-only recoveries fall below the shuffled-label rate. |
| The hand-tuned prompt works by moving the threshold, not the representation. | Narrowed | Production → hand-tuned moves all-benign vs all-attack AUC from 0.769 to 0.870 (cached runs), which a threshold shift cannot do. The prompt changes how the output reads a nearly constant state (probe sd 0.007 across 25 wordings). |
| Probe-guided mining produced the best prompt: probe-right/output-wrong items show what wording can fix. | Narrowed | Such items are fixed more often (74–89 % vs 31–39 %). Prompts written from probe-selected errors, however, are no better than prompts from random errors (matched recall −0.205 vs −0.060). |
| Best prompt: real pages 0/84, non-page benign flags 89 → 46 of 532 against the hand-tuned prompt (mined on the pool it was scored on). | Confirmed on ranking; not separated at matched budgets | On the test set hand-tuned − best is −0.0244 AUC [−0.0343, −0.0152] and −0.0435 recall [−0.0743, −0.0155]. Band pages flagged are 13 for the best prompt and 9 for the hand-tuned prompt, difference −3.9 [−10.0, +2.0]. At 13, 6 and 3 band pages the recall intervals contain 0. The best prompt beats all five of its paraphrases on AUC. |
| Best-prompt metrics on the scored pool (AUC real vs page-shaped 0.978, real vs judge-directed texts 0.958). | Corrected upward | 64 % of the best prompt's margins were clipped at ±30. Uncensored (cached runs): 0.9836 and 0.9875. |
| The readout edit does nothing under a better prompt (hand-tuned: real vs page-shaped on the tuning-set test split 0.917 → 0.918). | Retracted for the hand-tuned prompt; holds for the best prompt except on real vs page-shaped | The earlier figure came from clipped margins. On exact margins the production-fit edit under the hand-tuned prompt gives 0.911 → 0.983, and the hand-tuned-fit edit gives +0.009 [0.006, 0.012] AUC all-vs-all and +0.011 [0.005, 0.019] matched recall. Under the best prompt its all-vs-all AUC, within-set AUC and matched-recall intervals contain 0; the production-fit edit still sharpens real pages vs page-shaped attacks (+0.015 [0.007, 0.026]). |
| The fp16 prediction of the edit did not hold under the hand-tuned prompt (per-row r about 0.71). | Retracted | The clipped scorer gave r 0.692 / 0.711, with 454–455 rows clipped at the same value in both runs. On exact margins the per-row r is 0.981 / 0.987 and the mean \|Δ\| 1.59 / 1.12, down from 9.61 / 6.22. |
| Attention at the decision position does not change between prompts; the prompt acts downstream of attention, and attention is not the lever. | Narrowed | Attention mass did not separate the prompts, but the prompt's effect travels through attention. Blocking the decision positions' attention to the system prompt at all layers reproduces 43 % of the best → production margin difference (61 % in items ≤ 1,024 tokens, 7 % in longer ones). Long items route the effect through the page tokens (page patch 0.75 at layer 12). |
| llama.cpp run directly on the production GGUF is bit-deterministic. | Narrowed | Only for a fixed item order and cache split with one request at a time. Cache on vs off (micro-batch 512) changes 64 (4.05 %) production-prompt decisions; co-batching shifts margins by 1.2–1.5 logits on average. |

## 10. Scripts

The `scripts/` folder holds the exact-score scorer, the probe and learning-curve script, and a state-comparison check. See [scripts/README.md](scripts/README.md).

## 11. Limits

- **One model and one task.** One mixture-of-experts model, one quantisation and one binary verdict. Nothing here is tested on generative tasks or on other model families.
- **Labels are arguable in places.**
  - BrowseSafe pages carry the same banners under both labels.
  - The exempt_quoted style is a quoted, "educational" injection labelled as an attack.
  - wainject and pids_domain are largely separable by length alone (AUC 0.979 and 1.000).
  - Several public sets define an attack differently from the deployment.
- **The tuning set has duplicates.** 45 of 95 wainject rows in the tuning-set test split have a near-duplicate among wainject rows in its dev split. Template and host-page siblings are common in the planted and judge-directed sets.
- **What the test set covers:**
  - band-filtered items from the same public sources, on new ids and host pages;
  - planted payloads on new host pages, including two unseen styles;
  - 864 real pages that the first-stage classifier sends to the judge.
- **What it does not cover:**
  - production traffic;
  - unseen wainject or tr attacks (none survived de-duplication);
  - new templates for the 43 planted rows of the public-mix part;
  - a third unseen style (no candidate fell in the band).
- **The band pages are uneven.** They come from four corpora, the second batch supplies 731 of the 864, and the public-mix part is 168 rows short of its 597-row target.
- **The weight edit was tested on the test set under the production prompt only.**
- **The prompt-variant families have their own limits.**
  - Each few-shot arm is one draw of four examples, so arm comparisons are not comparisons of selection rules.
  - The screen-versus-measured correlation rests on n = 9 pairs whose measured differences are mostly inside noise.
  - The placement split by length is confounded with dataset: short rows are mostly tr, pids, NotInject and wainject; long benign rows are mostly real pages and BrowseSafe.
  - All four families were scored on the tuning set only.
- **The intervals are partial.** Bootstrap intervals cover row sampling. They do not cover probe refitting or the spread between equivalent prompts. In the mining experiment, reader identity and model are confounded, and arm effects below about 0.04 AUC are undetectable.
- **Numerics differ between experiments.**
  - The test-set comparisons, the probe on production states and all prompt scores use the production Q4_K_M numerics.
  - The layer trajectories, the routing near-ties, the answer-word screen, activation patching and steering use fp16 states. Patching and steering use 80 items each, one prompt pair and a different attention kernel (sign agreement with the stored fp16 margins 0.988 for the production prompt and 1.000 for the best prompt). fp16 and Q4_K_M agree in sign on 1,550–1,555 of 1,579 best-prompt decisions, with a mean distance of 2.2 logits.
  - fp16 results here are not checked against the quantised router or kernels.

## 12. Glossary

- **Production prompt, hand-tuned prompt, best prompt.** The judge's production system prompt; an earlier hand-tuned rewrite of it; the best prompt from an earlier pass of this study (hand-tuned framing plus rules from mined errors; wording not published).
- **Paraphrases A–E.** Five meaning-preserving rewordings of the best prompt, written blind to results.
- **Search finalists A–C; error-written prompts.** Finalists of the automated search (A: one-clause edit; B: best on the search subset; C: adds a base-rate sentence) and the best prompt of each error-mining arm (random, probe, classifier, annotated).
- **Positive word, negative word; production pair.** The judge's two answer words: the positive word means instructions aimed at an AI, the negative word means clear.
- **Margin.** logit(positive word) − logit(negative word) at the first answer token, after the model's softcap. The judge flags iff margin > 0.
- **Tuning set.** The 1,579 labelled items (616 benign, 963 attack) used for prompt selection, probe fitting and threshold setting. Its groups: real pages, page-shaped attacks, judge-directed texts, other benign, other attacks, production-cleared attacks. **Tuning-set dev and test splits** are a fixed split inside it.
- **Search subset.** 500 stratified rows of the tuning set used by the automated search.
- **Test set.** 1,643 band rows built after selection and new to the tuning set (1,064 benign, 579 attacks), in three parts: the public-mix part (mixed public sets), the planted part (planted pages, seen and unseen styles), and the band pages (real pages in the judge's band, two batches).
- **The 1,000 ordinary real pages.** Real pages that the first-stage classifier would not send to the judge.
- **Probe.** A class-balanced L2-regularised logistic regression on a hidden state, fitted on labelled tuning-set rows and evaluated out-of-fold or on the test set.
- **Final state.** The residual stream at the decision token after the final normalisation (k = 30): the vector the unembedding reads.
- **Readout edit.** A gradient-free weight change that rotates the positive-word and negative-word unembedding rows toward a probe direction. It adds λ(w·h + b) to the margin.
- **Unedited copy quantised the same way.** The baseline for every edit: the same weights without the edit, quantised like the edited model.
- **Band (guard band).** The first-stage classifier's score range whose texts are sent to the judge. **Band pages** are real pages in it.
- **Matched budget.** Comparing two readers at thresholds that flag the same number of benign rows (here, the same number of band real pages), so that recall differences are not threshold differences.
- **Paraphrase noise floor.** The spread of metrics across meaning-preserving rewordings of one prompt. A prompt difference smaller than about two paraphrase sds is not evidence of a better prompt.
- **Fresh pass.** Scoring each item with prompt caching off and one request at a time at fixed batch sizes, so that the margin depends only on the item and the server flags.
- **Last internal state** (the articles' term). The final state.
- **Logistic regression, the regression** (the articles' terms). The probe.
- **Unused part, accuracy left unused** (the articles' terms). The probe's lead: probe AUC − judge AUC.
- **Reader models A and B.** The two LLMs used as readers in the error-mining experiment.

## License

MIT. See `LICENSE`.
