# Weight-Space Audit of MIT-p50c and DNA Weight Editing (SGNE-CC) at a 32,768-Token Generation Limit

> **Language / Язык:** **English** · [Русский](README_RU.md)

Qwen3.5-0.8B is a hybrid language model with 752M text parameters, 18 recurrent GatedDeltaNet layers, and 6 attention layers. In the evaluated BF16 runs, it often leaves its reasoning unfinished at the generation limit of 32,768 new tokens. In MIT CSAIL's [*Sparks of Weight-Space Programming*](https://rikiyat.github.io/blog/weight-space-programming/) (Takehi, Teoh, Zhang, Khattab, 2026; run logs: [RikiyaT/lm_understand-logs](https://github.com/RikiyaT/lm_understand-logs)), the training-free MIT-p50c weight edit raises MATH-500 accuracy from 7.9% to 48.1%, averaged across four vLLM runs under model-card settings with temperature 0.6 and a presence penalty of 1.5 for tokens already used. The base model reaches the length limit in 93.0% of generations in that reference. **Does the reduction in looping persist without random token sampling and a presence penalty? What differences in weight geometry accompany the change in behavior?**

This study audits the weight geometry of MIT-p50c and compares it with **SGNE-CC** (*Spherical Gated Norm-preserving Edit, Column-Constrained*), a 3.13 MiB weight patch obtained without gradient retraining by rotating output columns on their Euclidean spheres while preserving their original lengths. This approach is called **DNA Weight Editing**. All three BF16 models (base Qwen3.5-0.8B, MIT-p50c, and SGNE-CC) are evaluated in full across both decoding regimes — **greedy decoding (pure weights: T = 0, pp = 0)** and **model-card settings (T = 0.6, pp = 1.5)** — on all five benchmarks (`MATH-500`, `MGSM-240`, `BBH-160`, `HumanEval-164`, `MultiSpeech-64`; 30 full reasoning runs totaling 1,128 tasks per model per regime, plus non-thinking controls on MultiSpeech-64).

---

## Contents
1. [Geometry of the Weight Edits: MIT-p50c vs. SGNE-CC](#1-geometry-of-the-weight-edits-mit-p50c-vs-sgne-cc)
2. [5-by-2 Summary Matrix and Mathematics (MATH-500 and MGSM-240)](#2-5-by-2-summary-matrix-and-mathematics-math-500-and-mgsm-240)
3. [Out-of-Domain Transfer: Logic and Code (BBH-160, Web of Lies, HumanEval-164)](#3-out-of-domain-transfer-logic-and-code-bbh-160-web-of-lies-humaneval-164)
4. [8-Language Text Generation (MultiSpeech-64)](#4-8-language-text-generation-multispeech-64)
5. [Method Scope, Conclusion, and Reproducibility (SHA-256)](#5-method-scope-conclusion-and-reproducibility-sha-256)

---

## 1. Geometry of the Weight Edits: MIT-p50c vs. SGNE-CC

Both weight patches are produced by directly modifying the pretrained weights of Qwen/Qwen3.5-0.8B. The model architecture, tokenizer, and inference code remain unchanged; layer indices below start at zero. Geometric properties of both edits can be checked in FP64 double precision from the open patch file `sgne_cc_dna_delta.npz` (3.13 MiB) and the base weights via `python3 apply_dna_patch.py --verify-only` (and side-by-side against the MIT checkpoint via `--compare`):

| Verifiable Weight Property (BF16) | Qwen3.5-0.8B | MIT-p50c | SGNE-CC (DNA Weight Editing) |
| :--- | :---: | :---: | :---: |
| Scalar elements in replacement region (of 752,393,024) | 0 (0%) | 131,072 (0.017%; 130,188 changed) | 2,032,640 (0.270%; 1,993,382 bitwise changed) |
| Edited feed-forward output columns (`mlp.down_proj`) | 0 | 128 (2 layers: indices 15 and 19) | 802 (15 feed-forward layers) |
| Edited recurrent GatedDeltaNet output columns (`out_proj`) | 0 | 0 (0 of 18 layers) | 1,182 (9 recurrent layers) |
| Edited attention output columns (`o_proj`) | 0 | 0 | 0 (0 of 6 layers) |
| Edited recurrent GatedDeltaNet gate rows (of 288) | 0 | 0 | **1** (layer 16, row 12, cosine 0.986582) |
| Column Frobenius norm of update | 0.000000 | 2.239452 | 3.570648 (full 3.574724) |
| Update energy per edited column | 0.0000 | 0.0392 | 0.0064 |
| Relative update norm on edited region | 0.0000 | 0.7349 | 0.2372 (different supports: 128 vs. 1,984 columns) |
| Column rotation angle (median / max) | 0° | 27.1° / 87.3° | **8.8°** / 93.7° |
| First singular mode energy share (layers 15 / 19 / 23) | — | **99.9995% / 99.9991%** / — | **67.58% / 73.43% / 55.92%** |
| Ratio of edited to original column norm | 1.000000 | **[1.002808, 2.142614]** | **[0.998375, 1.001620]** |
| Maximum column norm deviation | 0.0000% | **+114.2614%** (layer 19), **+70.5913%** (layer 15) | **0.1625%** (after BF16 rounding) |
| Minimum column rotation cosine | 1.000000 | 0.047701 (layer 19) | -0.063676 (layer 19, on original-norm sphere) |

Three structural differences separate the two edits:

1. **Column directions and norms.** In each of the two modified feed-forward output matrices of MIT-p50c (layer indices 15 and 19), the first singular mode accounts for over 99.999% of update energy. Individual column norms increase by up to 114.3%, reaching more than twice their pretrained length. In SGNE-CC, column directions are rotated while keeping norms close to their pretrained values: the largest measured deviation after BF16 rounding is about 0.16%, with a median rotation angle of 8.8° and a maximum of 93.7°. Preserving individual column norms does not by itself preserve pairwise angles between columns, output activation magnitudes, or model behavior.
2. **Distribution across feed-forward and recurrent blocks.** Three quarters of Qwen3.5-0.8B's depth consist of recurrent GatedDeltaNet layers, which MIT-p50c leaves untouched. SGNE-CC spreads a multi-rank update across the output matrices of 15 feed-forward layers and 9 recurrent layers, leaving all 6 attention layers unchanged.
3. **Single decay-gate row modification.** In the 13th of the 16 heads at layer index 16, one recurrent gate row is shifted in Euclidean norm from 1.0286 to 1.0452. This change is intended to alter recurrent state retention at the transition from reasoning to the final answer; whether it acts selectively at that boundary requires separate activation-level testing.

> **Working hypothesis.** Multi-step reasoning circuits are already formed in Qwen3.5-0.8B during pretraining, but become trapped inside a recurrent verification loop: output column angles steer reasoning trajectories, while stability across a 32,768-token horizon is linked to preserving the sphere of pretrained column norms. Because the two edits differ simultaneously across several factors — column norms, update rank, layer selection, edited block types, and the gate row in layer 16 — the empirical results below are consistent with this hypothesis, yet do not isolate the causal effect of norm preservation on their own. Direct causal testing requires separate ablations, such as rescaling MIT-p50c's edited columns back to their original lengths.

### Generation Protocol at a 32,768-New-Token Limit
To test sensitivity to decoding settings, models are evaluated with reasoning enabled, one run per task, random seed 0, and a ceiling of 32,768 newly generated tokens (the limit on generated output length, not the model's 262,144-token positional context window). Decoding parameters are stored in the `sampling` field of the main trace files, and recorded via the author's protocol in the manifest for the two post-freeze holdout files. The two regimes differ jointly in temperature, truncation thresholds, and presence penalty:
* **Greedy decoding (pure weights: T = 0, pp = 0)** — temperature 0, top_p 1.0, top_k 0 without random token sampling or a presence penalty: the most probable next token is chosen at every step. Unlike Qwen3.5-0.8B's factory `generation_config.json` (which also sets T = 0.6 and pp = 1.5), this regime isolates intrinsic weight dynamics without external sampler intervention.
* **Model-card settings (T = 0.6, pp = 1.5)** — temperature 0.6, top_p 0.95, top_k 20, and a presence penalty of 1.5 for tokens already used: at each step, 1.5 is subtracted once from the logit of any token that has already appeared in the generated response, regardless of count. Prompt tokens are excluded from this seen-token mask.

All ten benchmark slices (5 datasets × 2 regimes) across all three models (Qwen3.5-0.8B, MIT-p50c, SGNE-CC) include complete per-item traces from a unified batched PyTorch generator with BF16 weights. Under the author's run protocol, generations were executed on NVIDIA A100 and RTX PRO 6000 Blackwell accelerators in native hardware BF16, with selected shards run on NVIDIA T4 using FP16 Tensor Core matrix multiplications and FP32 normalizations. In `traces/audit_bf16_vs_t4_parity60_pure_t0.json`, a direct BF16 (RTX PRO 6000 Blackwell / A100) versus T4 FP16 numerical parity check across 60 greedy traces (20 per model) finds 20/20 grade agreement on Base (0 vs. 0), 19/20 (95%) on MIT-p50c (0 vs. 1), and 13/20 (65%) per-item agreement on SGNE-CC with matched aggregate counts (10/20 vs. 9/20) due to rounding sensitivity along long reasoning trajectories; per-file GPU assignment was not stored inside the `.jsonl` traces and rests on the author's protocol record.

Mathematical answers are graded symbolically with `math-verify`: strict grading (`strict_ok`) requires completed reasoning, normal generation end, and a correct expression in the final answer box; for MGSM, whitespace and thousands separators in integers are normalized beforehand. Both `MATH-500` charts (Fig. 1 and Fig. 2) show direct single-engine PyTorch comparisons across all three models, while MIT's external vLLM reference for `T = 0.6, pp = 1.5` is compared in §2.2.

---

## 2. 5-by-2 Summary Matrix and Mathematics (MATH-500 and MGSM-240)

Removing the presence penalty and random sampling (**greedy decoding, T = 0, pp = 0**) sharply reverses the comparison between the two edits. Without the external `-1.5` presence penalty, **MIT-p50c** drops by `2.2x–13.5x` across all five datasets, while its cutoff rate at 32,768 tokens jumps from `17.29%` to `85.11%` across all 1,128 prompts. By contrast, the norm-preserving spherical patch **SGNE-CC** beats MIT-p50c on **all five benchmarks (5 of 5)** in greedy accuracy, completion rate, and output length. Conversely, under model-card settings (`T = 0.6, pp = 1.5`), SGNE-CC remains `4.1x` shorter (`3,680.7` vs. `14,984.7` mean tokens across 1,128 prompts, `1.42%` vs. `17.29%` cutoffs) while trailing MIT-p50c in accuracy on `MATH-500`, `MGSM-240`, and numerically on `BBH-160` and `HumanEval-164`.

| Benchmark (tasks) | Decoding regime | Qwen3.5-0.8B (Acc / Cutoffs / Tok) | MIT-p50c (Acc / Cutoffs / Tok) | SGNE-CC (Acc / Cutoffs / Tok) | Paired test (SGNE-CC vs. MIT-p50c) |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **MATH-500** (500) | Greedy (`T = 0, pp = 0`) | 0/500 (0.00%) · 100.0% · 32,768.0 | 25/500 (5.00%) · 95.00% · 31,350.5 | **215/500 (43.00%)** · **18.40%** · **8,558.0** | McNemar `+195 / −5`, p = 3.24 × 10⁻⁵¹ |
| **MATH-500** (500) | Card (`T = 0.6, pp = 1.5`) | 39/500 (7.80%) · 92.20% · 30,632.6 | **259/500 (51.80%)** · 28.20% · 21,052.9 | 235/500 (47.00%) · **1.60%** · **5,319.4** | `+56 / −80`, p = 0.048 *(vs. vLLM s0: +65/−71, p = 0.67)* |
| **MGSM-240** (240) | Greedy (`T = 0, pp = 0`) | 5/240 (2.08%) · 97.50% · 31,987.0 | 51/240 (21.25%) · 70.83% · 24,006.4 | **92/240 (38.33%)** · **20.42%** · **8,186.4** | `+54 / −13`, 40-block p = 1.67 × 10⁻⁶ |
| **MGSM-240** (240) | Card (`T = 0.6, pp = 1.5`) | 62/240 (25.83%) · 66.67% · 23,604.5 | **137/240 (57.08%)** · 3.75% · 8,625.3 | 100/240 (41.67%) · **2.08%** · **3,089.7** | `+15 / −52`, 40-block p = 9.04 × 10⁻⁵ |
| **BBH-160** (160) | Greedy (`T = 0, pp = 0`) | 0/160 (0.00%) · 100.0% · 32,768.0 | 6/160 (3.75%) · 94.38% · 31,670.9 | **66/160 (41.25%)** · **16.88%** · **7,249.2** | `+61 / −1`, p = 2.73 × 10⁻¹⁷ *(strict: 0 / 6 / 51)* |
| **BBH-160** (160) | Card (`T = 0.6, pp = 1.5`) | 3/160 (1.88%) · 96.25% · 31,850.6 | **81/160 (50.62%)** · 14.38% · 16,939.7 | 66/160 (41.25%) · **0.62%** · **2,446.0** | `+20 / −35`, p = 0.058 |
| **HumanEval-164** (164) | Greedy (`T = 0, pp = 0`) | 9/164 (5.49%) · 90.85% · 29,855.1 | 23/164 (14.02%) · 78.05% · 26,274.1 | **53/164 (32.32%)** · **13.41%** · **5,077.3** | `+37 / −7`, p = 5.30 × 10⁻⁶ *(`<think>`: 12.52x)* |
| **HumanEval-164** (164) | Card (`T = 0.6, pp = 1.5`) | 26/164 (15.85%) · 35.37% · 12,564.7 | **51/164 (31.10%)** · 13.41% · 8,751.8 | 46/164 (28.05%) · **0.00%** · **1,056.0** | `+13 / −18`, p = 0.473 *(`<think>`: 14.11x)* |
| **MultiSpeech-64** (64) | Greedy (`T = 0, pp = 0`) | 2/64 (3.12%) · 96.88% · 31,802.4 | 17/64 (26.56%) · 56.25% · 20,173.2 | **23/64 (35.94%)** · **34.38%** · **13,011.2** | `+11 / −5`, p = 0.210 |
| **MultiSpeech-64** (64) | Card (`T = 0.6, pp = 1.5`) | 43/64 (67.19%) · 29.69% · 11,508.3 | **58/64 (90.62%)** · **0.00%** · **2,509.2** | 57/64 (89.06%) · 3.12% · 2,910.1 | `+4 / −5`, p = 1.000 |
| **All 5 suites total (1,128)** | **Greedy (`T = 0, pp = 0`)** | **16/1,128 (1.42%) · 97.96% · 32,123.7** | **122/1,128 (10.82%) · 85.11% · 28,461.1** | **449/1,128 (39.80%) · 18.79% · 8,039.9** | — |
| **All 5 suites total (1,128)** | **Card (`T = 0.6, pp = 1.5`)** | **173/1,128 (15.34%) · 75.53% · 25,598.5** | **586/1,128 (51.95%) · 17.29% · 14,984.7** | **504/1,128 (44.68%) · 1.42% · 3,680.7** | — |

### 2.1. Full MATH-500 under Greedy Decoding (Pure Weights: T = 0, pp = 0)

![MATH-500 — Greedy Decoding (T = 0, pp = 0)](charts_mobile_sections/01_math__math500_greedy_t0_en.png)

**Fig. 1. At temperature zero without a presence penalty, SGNE-CC solves 8.6 times as many full MATH-500 problems as MIT-p50c.** *All 500 MATH-500 problems under greedy decoding (`T = 0, pp = 0`), single PyTorch engine, 32,768-token ceiling. Strict grading requires closed reasoning, normal completion, and a correct boxed answer.*

Without random sampling or a presence penalty, Base Qwen3.5-0.8B solves 0 of 500 problems under strict grading (0.00%, all 500 hitting the 32,768-token ceiling), MIT-p50c solves 25 (5.00%, 475 cutoffs, mean length 31,350.5 tokens), and SGNE-CC solves 215 (43.00%, 92 cutoffs = 18.40%, mean length 8,558.0 tokens). The paired advantage of SGNE-CC over MIT-p50c is +195/−5 problems (exact paired McNemar test, p = 3.24 × 10⁻⁵¹) with 5.16x fewer cutoffs and 3.66x shorter responses. Another 25 SGNE-CC completions terminate cleanly before the ceiling without a final `\boxed{}` wrapper.

On many problems, MIT-p50c reaches the correct intermediate result early inside its reasoning block, yet never transitions to a final answer. On a problem converting Cartesian coordinates to polar coordinates (`precalculus/807`), MIT-p50c derives the right result near the start of its draft and then repeats an edge-case verification paragraph 451 consecutive times up to the 32,768-token ceiling, leaving the visible answer empty. SGNE-CC writes the correct boxed answer and stops at 2,394 tokens (1,944 in reasoning). This example illustrates the difference in stopping behavior, though a single trace does not explain every error on the benchmark.

| Grading Rule on Full MATH-500 (500 Problems, Greedy T = 0, pp = 0) | Qwen3.5-0.8B | MIT-p50c | SGNE-CC | McNemar (SGNE vs. MIT) |
| :--- | :---: | :---: | :---: | :---: |
| **Strict grading** (closed reasoning, completed generation, and correct boxed answer) | 0.00% (0/500) | 5.00% (25/500) | **43.00%** (215/500) | +195/−5, p = 3.24 × 10⁻⁵¹ |
| **MIT primary rule** (MIT answer extraction and symbolic check without requiring generation end) | 2.80% (14/500) | 6.40% (32/500) | **43.00%** (215/500) | +188/−5 |
| **MIT fallback rule** (answer extraction from unfinished reasoning and symbolic check) | 14.20% (71/500) | 18.60% (93/500) | **44.20%** (221/500) | — |

Even under MIT's fallback rule extracting numbers from truncated 32k reasoning drafts, SGNE-CC maintains more than a 2x lead (221 vs. 93 of 500). The archived 100-problem stratified sample across seven subjects (`strat100`) at temperature zero matches the full benchmark: 0 / 4 / 44 under strict grading (+41/−1, p = 1.96 × 10⁻¹¹), 1 / 5 / 44 under MIT's primary rule, and 7 / 20 / 45 under MIT's fallback rule.

**Post-freeze holdout check (`Holdout-300` and `FreshBlind-49`).** Under the study protocol, at most 200 MATH-500 problems were used during SGNE-CC angle selection and debugging. Disjoint lists of the 200 calibration and 300 untouched problem identifiers are published in `suites/reproducibility_and_holdout_manifest.json` and verified by `scripts/verify_paper_metrics.py`; without an external pre-release timestamp, freeze chronology rests on the author's protocol. Across all **300 untouched problems** at temperature zero, Base solves 0/300 (0.00%), MIT-p50c solves 20/300 (6.67%, 93.33% cutoffs, 30,850.5 tokens), and SGNE-CC solves **154/300 (51.33%, 14.67% cutoffs, 7,143.2 tokens; +138/−4, p = 6.00 × 10⁻³⁶)**. Under model-card settings, the same 300 problems yield 33/300 (11.00%), 180/300 (60.00%), and 165/300 (55.00%; +34/−49, p = 0.124). From the 300 untouched problems, 49 items (7 per subject) were deterministically sampled via SHA-256 alongside 7 long-form essays of 1,500–2,000 words (`suites/fresh_blind56_32k_suite.json`): at temperature zero, SGNE-CC solves **24 of 49 (48.98%)** versus 2/49 (4.08%) for MIT-p50c (+22/−0, p = 4.77 × 10⁻⁷) and 0/49 for Base (p = 1.19 × 10⁻⁷); under model-card settings, SGNE-CC again solves 24/49 versus 23/49 in the direct PyTorch run (+7/−6, p = 1.000) and 25/49 in MIT's first external vLLM run (+8/−9, p = 1.000; four-run mean 23.8). Across the seven essays at temperature zero, SGNE-CC closes reasoning on 6 of 7 prompts and finishes before the limit on 2 of 7, whereas Base closes none (0 of 7).

### 2.2. Full MATH-500 under Model-Card Settings (T = 0.6, pp = 1.5) and Difficulty Breakdown

![MATH-500 — Model-Card Settings (T = 0.6, pp = 1.5)](charts_mobile_sections/02_math__math500_mit_pp15_en.png)

**Fig. 2. Under model-card settings on the unified PyTorch engine, SGNE-CC trails MIT-p50c in solved count while generating four times shorter traces with minimal length cutoffs.** *All 500 MATH-500 problems at T = 0.6, pp = 1.5 on a single PyTorch BF16 engine: 39, 259, and 235 solved problems.*

Switching from greedy decoding to model-card settings (`T = 0.6, pp = 1.5`) sharply lifts MIT-p50c: in the unified PyTorch run across all 500 problems (`traces/math500_*_think32k_card_pp15.jsonl`), solved problems climb from 25 to **259 of 500 (51.80%)**, and 32k cutoffs fall from 95.0% to 28.20%. Base solves 39 problems (7.80%, 92.20% cutoffs, 30,632.6 tokens) and SGNE-CC solves **235 (47.00%; McNemar +56/−80, nominal p = 0.0482)**. Meanwhile, SGNE-CC's mean output is 4.0 times shorter (5,319.4 vs. 21,052.9 tokens) and hits the generation ceiling 17.6 times less often (1.60% vs. 28.20%). Among SGNE-CC's cleanly finished responses, 62 omit a final `\boxed{}` answer box and are marked incorrect under strict grading.

Compared against MIT's external vLLM logs (first run: 241 of 500 = 48.20%; four-run mean: 48.10%, 33.05% cutoffs, 22,037.1 tokens; independent H200 measurement on the MIT model card: 51.0% accuracy and 31.6% cutoffs), no statistically significant difference is detected between SGNE-CC and MIT's first vLLM run (+65/−71, p = 0.6683), and SGNE-CC outputs are 4.14 times shorter than the four-run vLLM mean with 20.7 times fewer cutoffs. Across 166 problems with identical extracted answer strings, the published verifier and the MIT logs agree on all 166 verdicts.

**Difficulty and subject breakdown (`Level 1–2` and `Level 3–5`) across both regimes:**
* **Introductory Levels 1–2 (133 problems).** Under model-card settings, MIT-p50c solves 103 problems (77.44%, 12.78% cutoffs, 14,283.6 tokens), SGNE-CC solves 92 (69.17%, 0.75% cutoffs, 2,566.5 tokens; McNemar +11/−22, p = 0.0801), and Base solves 22 (16.54%, 83.46% cutoffs, 28,124.3 tokens). Under **greedy decoding (`T = 0, pp = 0`)**, the ordering flips: **SGNE-CC increases to 95/133 (71.43%)** with 8.27% cutoffs and 4,931.4 mean tokens, whereas MIT-p50c drops nearly 8x to **13/133 (9.77%)** with 90.23% cutoffs and 29,913.4 tokens (+84/−2, p = 9.67 × 10⁻²³; Base 0/133).
* **Upper Levels 3–5 (367 problems).** Under model-card settings, MIT-p50c solves 156 problems (42.51%, 33.79% cutoffs, 23,506.1 tokens), SGNE-CC solves 143 (38.96%, 1.91% cutoffs, 6,317.1 tokens; +45/−58, nominal p = 0.2369), and Base solves 17 (4.63%). By subject within Levels 3–5 under model-card settings, MIT-p50c leads in elementary and high-school algebra (96/142 = 67.6% vs. 77/142 = 54.2%; +14/−33, p = 0.0079), number theory gives 23/47 (48.9%) vs. 20/47 (42.6%; p = 0.65), and across four harder subjects combined (intermediate algebra, precalculus, geometry, and counting with probability) SGNE-CC leads 46/178 (25.8%) vs. 37/178 (20.8%; +23/−14, p = 0.1877). Under **greedy decoding (`T = 0, pp = 0`)**, SGNE-CC solves **120/367 (32.70%)** (70/142 in algebra/prealgebra, 36/178 in the four-subject group, 14/47 in number theory) compared with **12/367 (3.27%)** for MIT-p50c (+111/−3, p = 2.38 × 10⁻²⁹) and 0/367 for Base.

### 2.3. Multilingual Grade-School Word Problems (MGSM-240, 6 Languages): Both Regimes

![MGSM-240 — Greedy Decoding (T = 0, pp = 0)](charts_mobile_sections/03_math__mgsm240_greedy_t0_en.png)

**Fig. 3. Under greedy decoding on multilingual MGSM-240 word problems, SGNE-CC beats MIT-p50c in accuracy across all six languages.** *Forty problems across six languages (240 responses at T = 0, pp = 0): 5, 51, and 92 correct answers.*

![MGSM-240 — Model-Card Settings (T = 0.6, pp = 1.5)](charts_mobile_sections/04_math__mgsm240_mit_pp15_en.png)

**Fig. 4. Under model-card settings on MGSM-240, MIT-p50c regains the lead in total solved count while SGNE-CC generates 2.8 times shorter responses.** *The same 240 responses at T = 0.6, pp = 1.5: 62, 137, and 100 correct answers. Per-language dots are descriptive and not independent samples.*

Across MGSM-240 (the same 40 story problems translated into Russian, Chinese, Japanese, French, Spanish, and German), contrasting the two regimes highlights the role of sampler intervention:
* **Greedy decoding (`T = 0, pp = 0`):** SGNE-CC solves **92 of 240 (38.33%, 20.42% cutoffs, 8,186.4 tokens)** compared with **51 of 240 (21.25%, 70.83% cutoffs, 24,006.4 tokens)** for MIT-p50c and **5 of 240 (2.08%, 97.50% cutoffs, 31,987.0 tokens)** for Base. Discordant pairs are +54/−13; an exact clustered sign-flip permutation test across the 40 six-language blocks yields two-sided p = 1.67 × 10⁻⁶ (naive McNemar p = 4.47 × 10⁻⁷). On Chinese, removing `pp = 1.5` drops MIT-p50c from 23/40 (57.5%) to **3/40 (7.5%, 90.0% cutoffs)**, while SGNE-CC maintains **19/40 (47.5%)**.
* **Model-card settings (`T = 0.6, pp = 1.5`):** MIT-p50c leads with **137 of 240 (57.08%, 3.75% cutoffs, 8,625.3 tokens)** versus **100 of 240 (41.67%, 2.08% cutoffs, 3,089.7 tokens)** for SGNE-CC and **62 of 240 (25.83%, 66.67% cutoffs, 23,604.5 tokens)** for Base. SGNE-CC's accuracy deficit is statistically significant (+15/−52, exact 40-block clustered permutation test p = 9.04 × 10⁻⁵; naive McNemar p = 6.46 × 10⁻⁶). Across the 52 misses relative to MIT-p50c, median output lengths are 5,364 and 1,934 tokens; traces show literal misreadings of verbal comparisons and ratios (`mgsm/ru/010, 014, 018, 024`, `mgsm/de/028, 038`, `mgsm/fr/011, 018`) alongside arithmetic slips.

| MGSM Language (40 tasks each) | `T = 0, pp = 0` — Base / MIT / SGNE (Acc %) | `T = 0, pp = 0` — Cutoffs MIT / SGNE | `T = 0, pp = 0` — Tokens MIT / SGNE |
| :--- | :---: | :---: | :---: |
| **RU** (Russian) | 10.0% / 35.0% / **42.5%** | 55.0% / **10.0%** | 18.89k / **5.13k** |
| **ZH** (Chinese) | 0.0% / 7.5% / **47.5%** | 90.0% / **17.5%** | 29.76k / **7.71k** |
| **JA** (Japanese) | 0.0% / 12.5% / **37.5%** | 77.5% / **20.0%** | 26.05k / **8.09k** |
| **FR** (French) | 2.5% / 17.5% / **35.0%** | 75.0% / **12.5%** | 25.60k / **5.45k** |
| **ES** (Spanish) | 0.0% / 27.5% / **35.0%** | 62.5% / **22.5%** | 21.75k / **8.74k** |
| **DE** (German) | 0.0% / 27.5% / **32.5%** | 65.0% / **40.0%** | 21.99k / **14.00k** |

---

## 3. Out-of-Domain Transfer: Logic and Code (BBH-160, Web of Lies, HumanEval-164)

Under the study protocol, both weight patches were selected solely on mathematical tasks: this is documented in the MIT paper for MIT-p50c, and recorded in `suites/reproducibility_and_holdout_manifest.json` for SGNE-CC. The evaluations below measure out-of-domain transfer of the fixed models to symbolic logic and Python code synthesis across both decoding regimes.

### 3.1. Symbolic Logic (BBH-160 and Web of Lies)

![BBH-160 — Greedy Decoding (T = 0, pp = 0)](charts_mobile_sections/05_logic__bbh160_greedy_t0_en.png)

**Fig. 5. Under greedy decoding, SGNE-CC retains the exact same 41.3% logic accuracy while MIT-p50c collapses from 50.6% to 3.8%.** *Eight BIG-Bench Hard subtasks of 20 problems each (160 problems total at T = 0, pp = 0), normalized `clean_bbh` grading.*

![BBH-160 — Model-Card Settings (T = 0.6, pp = 1.5)](charts_mobile_sections/06_logic__bbh160_mit_pp15_en.png)

**Fig. 6. Under model-card settings on BBH-160, both edits multiply solved counts over Base; SGNE-CC generates 6.9 times shorter responses with near-zero length cutoffs.** *The same 160 tasks at T = 0.6, pp = 1.5, normalized `clean_bbh` grading.*

On BBH-160 (**8 subtasks × 20 problems = 160 problems**), stability without sampler intervention cleanly separates the edits:
* **Greedy decoding (`T = 0, pp = 0`):** SGNE-CC achieves **66 of 160 (41.25% `clean_bbh` accuracy, zero percentage-point drop** from `pp = 1.5`; 16.88% cutoffs, 7,249.2 mean tokens). Without the presence penalty, MIT-p50c collapses more than 13x to **6 of 160 (3.75%, 94.38% cutoffs, 31,670.9 tokens)** and Base solves 0 of 160 (0.00%, 100.0% cutoffs, 32,768.0 tokens). SGNE-CC beats MIT-p50c by +61/−1 problems (p = 2.73 × 10⁻¹⁷; raw numeric `strict_ok` counts are 0 / 6 / 51).
* **Model-card settings (`T = 0.6, pp = 1.5`):** Base solves 3 of 160 (1.88%), MIT-p50c solves **81 (50.62%)**, and SGNE-CC solves **66 (41.25%)**. The accuracy difference between the edits does not cross p = 0.05 (+20/−35, p = 0.0581), while SGNE-CC's mean output is 6.93 times shorter (2,446.0 vs. 16,939.7 tokens) with 23 times fewer cutoffs (0.62%, or 1 cutoff, vs. 14.38%, or 23 cutoffs for MIT-p50c and 154 for Base; saved numeric `strict_ok` counts are 1 / 66 / 54, +19/−31, p = 0.1189).
* **Truth-and-lie chains (`Web of Lies`, 20 problems inside `BBH-160`).** Under greedy decoding (`T = 0, pp = 0`), both Base and MIT-p50c score 0 of 20 (100% cutoffs at 32,768 tokens), whereas SGNE-CC solves **7 of 20 (35.0%, 15.0% cutoffs, 6,485.5 tokens; +7/−0, p = 0.0156)**. Under model-card settings (`T = 0.6, pp = 1.5`), SGNE-CC completes all 20 prompts with zero cutoffs and scores **9 of 20 (45.0%, 1,844 tokens)** vs. 7 of 20 for MIT-p50c (35.0%, 4 cutoffs, 19,250 tokens; +4/−2, p = 0.6875) and 0 of 20 for Base (+9/−0, p = 0.0039); MIT-p50c's truncated trace `bbh/web_of_lies/000` loops after closing its reasoning at token 18,833.

### 3.2. Python Code Generation (HumanEval-164, Unit Tests)

![HumanEval-164 — Greedy Decoding (T = 0, pp = 0)](charts_mobile_sections/07_code__humaneval164_greedy_t0_en.png)

**Fig. 7. Under greedy decoding without sampling noise, SGNE-CC sets the all-time high of the study — 32.3% (53 of 164) with 12.5x shorter reasoning.** *Full 164-problem HumanEval suite at T = 0, pp = 0, sandboxed unit tests.*

![HumanEval-164 — Model-Card Settings (T = 0.6, pp = 1.5)](charts_mobile_sections/08_code__humaneval164_mit_pp15_en.png)

**Fig. 8. Under model-card settings on HumanEval-164, SGNE-CC compresses reasoning by 14.1x and finishes 100% of responses, trailing MIT-p50c by 5 problems (p = 0.47).** *The same 164 problems at T = 0.6, pp = 1.5, archived unit-test run.*

On Python code synthesis (`HumanEval-164`), removing sampling noise and presence penalty yields **SGNE-CC's highest pass@1 score across the entire study**:
* **Greedy decoding (`T = 0, pp = 0`):** SGNE-CC passes **53 of 164 problems (`32.32%` `pass@1`)**, exceeding not only greedy Base (`9/164 = 5.49%`, 90.85% cutoffs, 29,855.1 tokens) and greedy MIT-p50c (`23/164 = 14.02%`, 78.05% cutoffs, 26,274.1 tokens), but also MIT-p50c under model-card settings (`51/164 = 31.10%`). Within greedy decoding, SGNE-CC beats MIT-p50c (+37/−7, p = 5.30 × 10⁻⁶) and Base (+47/−3, p = 3.71 × 10⁻¹¹). Mean reasoning length inside `<think>` drops by **12.52x** (1,767.9 vs. 22,129.0 tokens for MIT-p50c and 29,641.3 for Base), with 5,077.3 mean total tokens and 13.41% cutoffs. Code is extracted from 157 of 164 SGNE-CC responses (154 valid under `ast.parse`); outcomes break down as `PASS = 53`, `ASSERTION_FAIL = 92`, `RUNTIME_ERROR = 9`, `UNCLOSED_THINK_32K = 7`, `SYNTAX_ERROR = 3` (versus `105` unclosed `<think>` blocks for MIT-p50c and `148` for Base; MIT-p50c yields 59 extracted, 51 `ast.parse`-valid).
* **Model-card settings (`T = 0.6, pp = 1.5`):** according to the archived unit-test report (recorded in `suites/reproducibility_and_holdout_manifest.json` and reproducible inside an isolated container via `scripts/grade_humaneval_sandbox.py`), Base passes 26 of 164 (15.85%, 35.37% cutoffs, 12,564.7 tokens), MIT-p50c passes 51 (31.10%, 13.41% cutoffs, 8,751.8 tokens), and SGNE-CC passes 46 (28.05%, 0.00% cutoffs, 1,056.0 tokens). No statistically significant difference is detected between edits (McNemar +13/−18, p = 0.4731); both exceed Base (p ≤ 0.0029). SGNE-CC's `<think>` length is **14.11x shorter** (448.8 vs. 6,334.3 tokens). Code is extracted from all 164 SGNE-CC responses (158 `ast.parse`-valid; failures: 81 `AssertionError`, 28 `RuntimeError`, 7 `SyntaxError`, 2 timeouts). Even with `pp = 1.5`, eight unfinished MIT-p50c responses produce multi-thousand-token runs of a single character up to 32,768 — spaces (`HumanEval/24`, `HumanEval/159`), closing parentheses `')))))...'` (`HumanEval/61`), or nines `'99999...'` (`HumanEval/144`).

---

## 4. 8-Language Text Generation (MultiSpeech-64)

MultiSpeech-64 spans 8 applied writing genres across 8 languages (Russian, English, Chinese, German, Spanish, French, Japanese, and Arabic), totaling 768 responses across three models and four decoding modes (two reasoning runs at 32,768 tokens plus two non-thinking control runs at 4,096 tokens). An automated filter credits a response when all formal conditions hold simultaneously: reasoning is closed, generation reaches normal completion, the visible answer is non-empty, repeated eight-character sequences stay at or below 25% (and repeated four-word sequences at or below 20% for space-delimited scripts), and the check detects no foreign-script insertions. This filter measures **formal generation stability**, not semantic coherence, factual accuracy, or instruction following — content failures are examined separately below. With 8 prompts per language, per-language profiles are descriptive.

### 4.1. Greedy Decoding (Pure Weights: T = 0, pp = 0)

![MultiSpeech-64 — Greedy Decoding (T = 0, pp = 0)](charts_mobile_sections/09_speech__multispeech64_greedy_t0_en.png)

**Fig. 9. At temperature zero, both edits raise the share of formally completed texts over Base, and SGNE-CC leaves fewer than one quarter as many unclosed reasoning blocks as MIT-p50c.** *Eight languages across eight genres without random sampling or a presence penalty; 2, 17, and 23 of 64 responses pass the automated filter.*

Without random sampling or a presence penalty, both edits multiply the automated-filter pass rate over Base (p < 10⁻⁴): Base passes 2 of 64 prompts (3.1%), MIT-p50c passes 17 (26.6%), and SGNE-CC passes 23 (35.9%; McNemar +11/−5, p = 0.210). Counting languages with zero passed prompts (0 of 8), Base fails completely on six of eight languages, MIT-p50c on two (Japanese and Arabic), and SGNE-CC on one (German). Numerically, SGNE-CC scores higher on five languages (English, Chinese, Spanish, Japanese, and Arabic), ties MIT-p50c on French, and trails on Russian and German. Failure patterns differ across the three models:
* **Base Qwen3.5-0.8B stalls inside reasoning.** In 60 of 64 prompts, the visible answer is empty: all 32,768 tokens are spent inside the draft, reaching normal completion only twice.
* **MIT-p50c finishes reasoning but loops in visible text.** Reasoning remains unclosed in 22 of 64 prompts (with normal completion in 28), yet without a presence penalty the model repeats lines inside the visible response: in the Arabic formal letter (`ar/formal_letter`) it inflates the form header `**الاسم:** [الاسم الكامل]` to 68.5k characters, in English popular science (`en/pop_science`) it repeats a paragraph to 134.2k characters, and in the Chinese brief (`zh/structured_brief`) it repeats `扶手、扶手...` (“armrest”) until the length ceiling.
* **SGNE-CC leaves fewer unclosed reasoning blocks:** 5 cases versus 22 for MIT-p50c (4.4 times fewer; 6 empty visible answers total), reaching normal completion on 42 of 64 prompts. On the three prompts above, SGNE-CC produces compact finished texts, lowering median length across the suite to 2,235 tokens versus 32,768 for MIT-p50c (mean 13,011.2 vs. 20,173.2). At temperature zero, SGNE-CC shows a higher rate of paired asterisks (16.53 vs. 5.55 per 1,000 characters, a count that includes ordinary Markdown emphasis) and retains repetition failures in German; on the Russian historical portrait (`ru/historical_portrait`), all three models leave reasoning unfinished at temperature zero.

### 4.2. Model-Card Settings (T = 0.6, pp = 1.5): Repetition, Script Insertions, and Factual Distortions

![MultiSpeech-64 — Model-Card Settings (T = 0.6, pp = 1.5)](charts_mobile_sections/10_speech__multispeech64_mit_pp15_en.png)

**Fig. 10. Under model-card settings, both edits close reasoning on every prompt while retaining isolated repetition failures and foreign-script insertions.** *43, 58, and 57 of 64 responses pass the automated filter; the formal filter does not verify factual accuracy.*

Under model-card settings, neither MIT-p50c nor SGNE-CC leaves any unfinished reasoning blocks (0 of 64 versus 13 of 64 for Base). No difference is detected between the two edits on the formal filter (58 of 64 vs. 57 of 64, p = 1.000), and both significantly exceed Base (43 of 64, nominal p < 0.005). SGNE-CC has a lower median length (1,861 vs. 2,311 tokens) but a higher mean (2,910.1 vs. 2,509.2 tokens) due to two German responses reaching the 32,768 limit. In non-thinking control runs at a 4,096-token limit, no significant differences appear among the three models: 29 / 31 / 33 of 64 under greedy decoding (p ≥ 0.48 across all pairs) and 61 / 61 / 59 of 64 under model-card settings (p ≥ 0.625), though those controls are bounded by 64 prompts and a surface filter.

**Content limitations.** First, under model-card settings, MIT-p50c produces three responses with Chinese characters inserted mid-word into Russian and Arabic prose («сохранять стабильную航速 при низких температурах», `يحقق双赢`, `| المهمة |责任人 |`), while SGNE-CC produces two in Arabic (`نصف的量`, `قواعد定期`) and none in Russian (8 of 8). Whether the presence penalty directly causes these insertions can only be tested by varying that parameter alone. Second, four of SGNE-CC's five remaining repetition-threshold failures occur in German (4 of 8, plus one in Spanish); linking this pattern to German compound nouns remains an untested hypothesis. Third, on `ru/historical_portrait`, although Fridtjof Nansen is named explicitly in the prompt, SGNE-CC replaces his name with “fleet commander **F. 1895**” and finishes cleanly, passing the automated filter. This case shows that formal completion guarantees neither instruction fidelity nor preservation of prompt facts.

---

## 5. Method Scope, Conclusion, and Reproducibility (SHA-256)

### What DNA Weight Editing Establishes — and What It Does Not
1. **Observed behavior.** The fixed SGNE-CC weight patch substantially reduces output length and 32,768-token cutoff rates across all five benchmarks (`MATH-500`, `MGSM-240`, `BBH-160`, `HumanEval-164`, `MultiSpeech-64`) in both decoding regimes. Under greedy decoding without sampling or a presence penalty (`T = 0, pp = 0`), SGNE-CC outperforms both MIT-p50c and Base across all 5 of 5 benchmarks (`39.80%` vs. `10.82%` and `1.42%` across 1,128 prompts) and sets the study's highest score on `HumanEval-164` (`32.32%`). The causal contribution of column norm preservation relative to the patch's other factors, as well as any effect on latent factual recall, is not established by these comparisons.
2. **Length and accuracy trade-offs.** Relative accuracy depends on the task family and decoding mode. Without the external presence penalty (`T = 0, pp = 0`), MIT-p50c loses most of its gain, whereas SGNE-CC retains stability (e.g., an unchanged `41.25%` on `BBH-160` across both regimes and `71.43%` on `MATH-500` Levels 1–2). Conversely, under model-card settings (`T = 0.6, pp = 1.5`), MIT-p50c beats SGNE-CC significantly on multilingual `MGSM-240` word problems (`57.08%` vs. `41.67%`) and scores higher in direct PyTorch runs on full `MATH-500` (`51.80%` vs. `47.00%`) and numerically on `BBH-160` (`50.62%` vs. `41.25%`) and `HumanEval-164` (`31.10%` vs. `28.05%`). These regimes must be reported separately rather than compressed into a uniform “shorter without loss” claim.
3. **Independent artifact verification.** The rotation-angle search procedure is not released, whereas the BF16 weight patch (`sgne_cc_dna_delta.npz`), partition manifest, all 8 benchmark suites, 38 trace files, 3 official MIT reference files, and the BF16/T4-FP16 parity file (**52 files locked by SHA-256 checksums**) are fully public. Weight geometry and all saved-trace metrics can be verified locally on a CPU; re-running GPU generation and executing model-generated code in a sandbox remain separate procedures.

### Protocol Limitations
* **One run per task.** All direct PyTorch runs record one output per prompt (seed 0), so seed-to-seed variance inside the PyTorch generator is unmeasured; four external vLLM runs are available for the MIT reference on full MATH-500 under model-card settings.
* **Hardware protocol, numerical precision, and statistics.** Direct traces were generated with a shared batched runner across several accelerators: under the author's protocol, NVIDIA A100 and RTX PRO 6000 Blackwell in hardware BF16 and selected shards on NVIDIA T4 using FP16 matrix multiplications and FP32 normalizations. In `traces/audit_bf16_vs_t4_parity60_pure_t0.json`, a 60-trace `T = 0` parity check between native BF16 and T4 FP16 (20 tasks per model) shows 20/20 item agreement on Base (0 vs. 0 on RTX PRO 6000 Blackwell), 19/20 on MIT-p50c (0 vs. 1 on A100-SXM4-40GB), and 13/20 (65%) per-item agreement on SGNE-CC at matched aggregate counts (10/20 vs. 9/20 on RTX PRO 6000 Blackwell). Available decoding parameters, prompt templates, and numerical modes are documented in `suites/reproducibility_and_holdout_manifest.json`, while per-file GPU assignment was not stored inside the `.jsonl` trace files. An independent re-run at temperature zero in vLLM remains a useful external check. All p-values across subsets and subject slices are nominal without multiplicity correction; p > 0.05 indicates an undetected difference at the given sample size rather than proof of model equivalence.
* **Code execution safety.** `scripts/grade_humaneval_sandbox.py` runs model-generated Python code under the current user account (`python -I` isolates Python import paths, not the filesystem or network). Run it solely inside a disposable container or virtual machine.

### Conclusion
Comparing these fixed weight edits across the complete 5 × 2 matrix shows that distinct weight-space geometries coincide with stark differences in intrinsic stability without sampler intervention. Under model-card settings, the presence penalty lifts MIT-p50c out of repetition loops and yields higher accuracy on MGSM-240 word problems and full MATH-500, but once that penalty is removed (`T = 0, pp = 0`), MIT-p50c drops by 2.2x–13.5x while SGNE-CC maintains performance across all five suites and sets the study's highest score on HumanEval-164. Isolating the causal contribution of norm preservation from layer selection, update rank, and the gate row in layer 16 requires targeted ablations, and formally terminated outputs in both edits can still exhibit factual distortions or language-specific repetitions. Releasing the open patch and 38 trace files lets readers verify both the artifact geometry and every reported metric locally.

### Artifact Checksums (SHA-256), Licensing, and Offline Verification
* Archival Zenodo deposit (bilingual paper, `sgne_cc_dna_delta.npz` patch, and complete repository archive): [DOI 10.5281/zenodo.24235218](https://doi.org/10.5281/zenodo.24235218).
* Author code, the weight patch file, and manuscript text are open under **Apache-2.0** ([`LICENSE`](LICENSE)). Included or adapted third-party code, datasets, and reference logs retain their original licenses; sources and notices are listed in [`NOTICE`](NOTICE) and [`THIRD_PARTY_LICENSES.md`](THIRD_PARTY_LICENSES.md).
* Base model: Qwen/Qwen3.5-0.8B (752,393,024 text parameters, BF16). Verified files: `model.safetensors` — `04b1c301231dd422b8860db31311ab2721511346a32cb1e079c4c4e5f1fe4696`; `config.json` — `b90b86f35c8e6925ef74ee04d0e758f0a845c83a42089ad82bbaa948de9b4204`; `tokenizer.json` — `5f9e4d4901a92b997e463c1f46055088b6cca5ca61a6522d1b9f64c4bb81cb42`.
* SGNE-CC weight patch (`sgne_cc_dna_delta.npz`, 3.13 MiB, modified columns and gate row in BF16): `4e4d36e032869bc10f56e2a2033a52d3f2774321cf867ef6f74274a7c0d1566d`.
* Comparison checkpoint MIT-p50c: distributed separately by the MIT authors on Hugging Face ([RikiyaT/Qwen3.5-0.8B-weight-space-programming](https://huggingface.co/RikiyaT/Qwen3.5-0.8B-weight-space-programming)) and supported via `--compare` in `apply_dna_patch.py`.
* Manifest and benchmark suites (`suites/*.json`, 9 files):
  * `reproducibility_and_holdout_manifest.json`: `c36bd257d55e7643f0c10378fdd935f184e1740630b7c0a05f42f48cea01689a`
  * `fresh_blind56_32k_suite.json`: `63ba2cf247934afbc767865a5727eb403bbbc6af3205d44d3e755fe849a43e89`
  * `suite_math500_full.json`: `a596fa9b05b35f2c0ff32b70ea620d3241d90862cbd9bd1e77af738bb5c78a9b`
  * `suite_math500_strat100.json`: `6347b75c46d4969a1c021ff8d42ba80e3c5c1a00540e62b7dc6fd0b8a8dd0c79`
  * `suite_mgsm240.json`: `07fc6f003fb91dbffac881f825bbb1636d7b9509c6d3fb928aeb9fc0edda32d5`
  * `suite_bbh160.json`: `d39a779dd69e915e4dd995d19be973e4108b4039e9721b5d1620493838db001c`
  * `suite_unseen_humaneval164.json`: `5703edc81a78f82dca58da583036dd73e22715085ca99540c8d88189f19e1a89`
  * `suite_unseen_mgsm240_bbh160.json`: `5de44113cae2b07d8a693d1c87a2e61de5a18d79dd9c01e1049b10453f41df66`
  * `suite_multispeech64.json`: `8fa2da6c2ab8bd7d64659c24b1ead845032f19db6a3c79e05790a4d30afabe55`
* `MATH-500` traces (500 problems, greedy `T = 0, pp = 0` — Base / MIT / SGNE): `97e2b70bbe81367254a972b7efd4b0c649a35c6f08ae0fb992bc1c545c936a4f` / `ea51d00c88bf65a26acd82a977290ae0b5392eddfb8b18abb18826f773b6a8c8` / `4b94c6c55599f40f26973af412b513b519d5d6232ebf374b16137089c7f4baf4`
* `MATH-500` traces (500 problems, card `T = 0.6, pp = 1.5` — Base / MIT / SGNE): `6d06d373c429c760584a553ebf9ed26a639f42ee64b4ce72b86d0c49fc3c113c` / `2c766bf006030cb15dd6d8256534ca6ad730b8a780d9c058872d09d9b150ffb6` / `8f4fed10df896a6ffe5f367982f23d88625cdee1b3cba5a40801626ce3b7be9a`
* External MIT vLLM reference (`traces/mit_official_math500_ref/`: `mit_p50c_merged.json` / `mit_p50c_official_500_per_problem.json` / `mit_unedited_merged.json`): `c93d3db30a612ef0da396014fdfbe011efbcf2cd417e2e6125664d7effdd0471` / `a699f8b5e31c8db138f5137ceba736fa26275630fdac803ba824ba1b1bad3edf` / `5c31370485b9f197f592745e935eeaee6b09dc127daa5b2a8be1ebbcbc210221`
* Archived `MATH-500` `strat100` (T = 0 — Base / MIT / SGNE): `8df959b204995ca909f68533c1bb857f4e9a2a04789cf9dc27b8bb46fede68fd` / `4634cb4a5234cfce5627d8b31b6e103d28ebac009735e5c3475b6ac7913aeb26` / `bf1a30e67cf900fbb892c5b4ac6ed7220fc64d8ef2e87e29ec6b6fa69187f350`; holdout `blind56` traces (Base / SGNE): `58d0db19f5d3d95dea9e4cb39b9a66979cfaef01a5235be8ed4b9945b1064ec0` / `2072450af148d124fb09f9698d9eb137b933f44014f125e91f394709d7e5a14e`
* `MGSM-240` traces (greedy `T = 0` — Base / MIT / SGNE): `d0f05df915c4f9d501a7d0cf4e6062d164791c59d2de84c422b5280df11477ae` / `8f05359ab873100db2e083e5600b5fdced7df25b005c9a0a4cc0a490132afa5a` / `7aab88c558d2550bf848c8f0cf81d5033a1ae9c7de1b85db16d4eb611d880690`
* `BBH-160` traces (greedy `T = 0` — Base / MIT / SGNE): `ab9852c54587a7196a7c155b8626348b6bddaf4bcef72546b7f32347c50963d7` / `7ef1b9c7159a2b3798f7ac93943a6d8eba1a0d21d2cbca4e90b92efab33129c8` / `658bf3a2c313ca693117a1d8e63e1f635e6f45e7258f0d561c83bee4f1699cf8`
* Merged `MGSM-240 + BBH-160` traces (card `T = 0.6, pp = 1.5` — Base / MIT / SGNE): `8e7fa9ece63a7de7399b786dc53df8a1c1287e049bbea25e612a836c996fe23e` / `317556c3dd0e42b2561c37cd36d82e847a3fa2884523508e02348b0f9c96ba64` / `a8936581d18a482b773ad40f71cd6bfc59e93a5bc57280b44e3d30a963a93767`
* `HumanEval-164` traces (greedy `T = 0` — Base / MIT / SGNE): `a9b1aba270fc6f53be031749248e269c85d32302540e129419997eb30b0c72b5` / `038bd14e53ccfdffb4a25aa59da8769306ddd49036b5f415398c040cda51cd3c` / `f8f40e0640f1b5bacca883a063da1b40627560efb5e7f898000ee067af314322`
* `HumanEval-164` traces (card `T = 0.6, pp = 1.5` — Base / MIT / SGNE): `b2fd764fe9f681567a0d35a3251f484f9969c9149b63044589773e178369b041` / `dd1c6ea407d53ce0a4b9e22f5ec9436c2984419b074ac847c273293b1f0c4a13` / `fc67fef2e2db445be97d94c6ac23981b848f557d10e981a0d043a06767c42106`
* `MultiSpeech-64` traces (greedy `T = 0` with reasoning — Base / MIT / SGNE): `13fece99c98ae619687cf71970b45d52b326d751a536d2ce678b56cd4e6c994d` / `a2574d87d70ec5da102be1be12dd8c2de7c7fdfa29fa6a523be1ed863422408d` / `f9f27c9b36c53b4605b5d57eb2d6aa81f4a9c845269b065995b495c2d60c2a29`; (card `pp = 1.5` with reasoning — Base / MIT / SGNE): `8b4767ca1b1dc0af3466a486bedbb50e685df339ed65111b81c84292ed633ccd` / `a088d9444b7c40baa3b43a014e3ce83bbe320005ff7901d169c7c3cc536121e2` / `d1f5687daeebb949635bbc44e7ac6494040ab3e5ab0a6980f7b6afd335d463bd`
* Non-thinking `MultiSpeech-64` controls (`nothink`, `T = 0` — Base / MIT / SGNE): `38029c2f1e5e8726ec493a91a9c4cc70c8e9b2f97bcd2e4d1c0b5a209ebfd0f3` / `dc29caa22c759a9c9166e1db003a573e78229c63a7c7a856a7dc746938c99cd5` / `9f805c6ea9f67f9828b83a6893ed1f8c688eefddd4fd586496099e93869db7e9`; (`pp = 1.5` — Base / MIT / SGNE): `c28645dd975aa0276986fb1b98bff9164e9c5a8b7dfa90cd696ed770fb34cd20` / `9f837413c7bce853d2ddb4d58390f3449b963bf7cbe9314bdff8bce9ad4ff484` / `e63dca071bda5112356eb4257e348a4e03137f0d849a88a6f0131d13f1cd1248`
* BF16 vs. T4 FP16 numerical parity audit (`traces/audit_bf16_vs_t4_parity60_pure_t0.json`): `f7d1cf696698de33538b166efdc721aec05bc207360b88533479bcb7f632d584` *(all **52** tracked files are automatically verified via SHA-256 by `scripts/verify_paper_metrics.py`)*.
* Standalone model assembly and local CPU verification without a GPU (`pip install -r requirements.txt`):
  * Assemble a ready-to-use BF16 checkpoint for Transformers, vLLM, or SGLang: `python3 apply_dna_patch.py --out ./Qwen3.5-0.8B-SGNE-CC` (pass `--base-model <path>` if already downloaded locally; otherwise Qwen/Qwen3.5-0.8B is downloaded from Hugging Face and SHA-256-verified).
  * Verify FP64 weight geometry in memory without writing a 1.75 GB copy: `python3 apply_dna_patch.py --verify-only` (add `--compare RikiyaT/Qwen3.5-0.8B-weight-space-programming` or a local folder path for side-by-side comparison with MIT-p50c).
  * Verify all 52 SHA-256 checksums and recompute saved-trace metrics: `python3 scripts/verify_paper_metrics.py`.
  * Re-run HumanEval-164 unit tests (executes model-generated code — run inside an isolated container): `python3 scripts/grade_humaneval_sandbox.py`.

### Independent Replications & External Audits

- **Dave Uhlemann (`NeoCortex0815`) — *Knowing Is Not Committing v0.5* (Sections 3.13–3.14):** independent `llama.cpp` evaluation, `GatedDeltaNet`-only replication, and multi-run council comparison ([DOI: 10.5281/zenodo.24420522](https://doi.org/10.5281/zenodo.24420522), [repo](https://github.com/NeoCortex0815/knowing-is-not-committing)).
- **`Human-AI-Evolution` (`@HedonismJesse`) — 5-arm Hugging Face `transformers` replication & component ablation:** independently replicated greedy `T = 0` recovery on the 300-item held-out manifest (`143/300` strict), released `MLP-only` and `gate-minus` `.npz` deltas ([`weight-space-notes`](https://github.com/Human-AI-Evolution/weight-space-notes), [discussion #4](https://github.com/RikiyaT/lm_understand-logs/issues/4#issuecomment-7062726129)), and showed that removing the `L16` decay-gate row does not reduce accuracy (`147/300`) while `MLP down_proj` carries termination (`0%` cap hits) and `GDN out_proj` suppresses mid-trace repetition.
- **Carlos Toledo (`@carlostoledo1891`):** independent dual-grader re-verification across all 3,000 published `MATH-500` responses ([discussion #4](https://github.com/RikiyaT/lm_understand-logs/issues/4#issuecomment-7060542882)).
- **Follow-up pure-Transformer transfer (`SGNE-CC v2`):** [`Nondual-Observer/deepseek-r1-1.5b-sgne-cc-v2`](https://github.com/Nondual-Observer/deepseek-r1-1.5b-sgne-cc-v2) ([DOI: 10.5281/zenodo.24398165](https://doi.org/10.5281/zenodo.24398165)) transfers norm-preserving `mlp.down_proj` column rotation (`205` columns, `0.0177%`, no gates or recurrent layers) to `DeepSeek-R1-Distill-Qwen-1.5B`.

### Author Note and AI Collaboration Disclosure
This work was done by Igor M. Zhuk ([ORCID 0009-0003-1670-8388](https://orcid.org/0009-0003-1670-8388)) in collaboration with AI—both on the research itself and on the code, figures, and text. The author takes full responsibility for all claims, and every number can be verified locally from the open `.npz` patch, 38 trace files, and CPU scripts (52 files under SHA-256).

* **Ready-to-run BF16 checkpoint (Hugging Face):** [`Nondual-Observer/Qwen3.5-0.8B-SGNE-CC`](https://huggingface.co/Nondual-Observer/Qwen3.5-0.8B-SGNE-CC)
* **Archival Zenodo Deposit:** [DOI: `10.5281/zenodo.24235218`](https://doi.org/10.5281/zenodo.24235218)
* **Theoretical Framework (`DOT`):** *Distinction Observable Theory (`DOT`)* ([GitHub: `Nondual-Observer/DOTheory`](https://github.com/Nondual-Observer/DOTheory) · [Zenodo Concept DOI: `10.5281/zenodo.23481643`](https://doi.org/10.5281/zenodo.23481643))

---

## Supporting the Research

Donations support the open [DOT (`Nondual-Observer/DOTheory`)](https://github.com/Nondual-Observer/DOTheory) project by an independent developer. Support helps:

- conduct larger computational experiments;
- develop theoretical formalization;
- create reproducible research tools;
- publish “For Dummies: How to Prompt an AGI”.

It also makes it possible to dedicate more time to the research and preserve its independent, open character.

| Currency | Network | Address |
|---|---|---|
| Bitcoin | BTC | `bc1qlaxsrum7fxpml57nsrtkjfkkxl5v3xtj4d0uxe` |
| USDT | TRC20 | `TM8U2EqVaT3tjvG6NyuKTqY4F5qc2A69Sy` |
| Ethereum | ETH | `0x4fFc68f0d55d19Fa5EBd5f6570a41E100aFe4a98` |
