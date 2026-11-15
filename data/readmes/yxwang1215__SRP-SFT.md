<div align="center">

# Beyond Distribution Matching: Selective Margin Preservation for Supervised Fine-Tuning

**SRP-SFT: Selective Rank-Preserving Supervised Fine-Tuning**

[![Paper](https://img.shields.io/badge/Paper-PDF-red)](SRP_SFT__Selective_Rank_Preserving_Supervised_Fine_Tuning.pdf)
[![arXiv](https://img.shields.io/badge/arXiv-2610.19685-b31b1b.svg)](https://arxiv.org/abs/2610.19685)
[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)](#installation)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.6.0-orange?logo=pytorch&logoColor=white)](requirements-train.txt)

[arXiv](https://arxiv.org/abs/2610.19685) · [Paper](SRP_SFT__Selective_Rank_Preserving_Supervised_Fine_Tuning.pdf) · [Results](#results) · [Quickstart](#quickstart) · [Experiments](#experiments) · [Citation](#citation)

</div>

SRP-SFT adds a selective margin-preservation objective to supervised fine-tuning. At each teacher-forced prefix, a frozen reference model selects plausible non-target tokens and supplies their pairwise logit margins. The student receives a hinge penalty when a selected margin falls below a reference-scaled threshold. Once that threshold is met, the pair contributes no auxiliary penalty.

This repository provides the implementation of **SRP-SFT**, **LP-SFT**, ranking objectives, and SFT baselines, with reference-cache construction, DeepSpeed training, benchmark evaluation, and held-out diagnostics.

<p align="center">
  <img src="assets/srp-sft-overview.png" width="100%" alt="SRP-SFT overview: reference and student logits at the same prefix, non-target candidate pairs, and a hinge loss for margin shortfalls." />
</p>

*Figure 2 from the paper. CE supervises the target token; the SRP auxiliary acts on selected non-target pairs. At the headline setting, a contracted or reversed margin is penalized, while further expansion is allowed.*

## Highlights

- **Selective preservation.** Protect selected non-target margins with a one-sided hinge, while CE continues to fit the observed token.
- **Cached reference signals.** Precompute reference token IDs and logits once; training gathers current student logits without another reference-model pass.
- **Matched comparisons.** CE, LP-SFT, SRP-SFT, DFT, EAFT, GEM, and ASFT share a training entry point. Additional ranking objectives and structural controls are included.
- **Evaluation and diagnostics.** Generate and score mathematical and coding benchmarks; measure held-out rank flips, margin contraction, local KL, and entropy.

## Results

Results below are reported in the [paper](SRP_SFT__Selective_Rank_Preserving_Supervised_Fine_Tuning.pdf), Tables 1–2: **Qwen3-4B-Base**, **UltraFeedback**, **one epoch**, training seed **1234**. All scores are percentages.

| Method | MATH-500 pass@1 | HumanEval+ pass@1 | MBPP+ pass@1 | Reasoning mean | Code mean |
|:--|--:|--:|--:|--:|--:|
| Base | 48.11 | 45.49 | 46.12 | 42.24 | 58.92 |
| CE | 27.98 | 44.18 | 44.66 | 35.99 | 56.04 |
| GEM | 22.21 | 22.93 | 26.40 | 35.01 | 36.95 |
| DFT | 47.73 | 64.12 | **57.24** | 35.25 | 63.72 |
| ASFT | 33.41 | **64.79** | 57.09 | 37.64 | 66.74 |
| EAFT | 28.52 | 46.43 | 44.59 | 34.91 | 57.12 |
| LP-SFT | 49.56 | 57.90 | 51.87 | 43.50 | 65.91 |
| **SRP-SFT** | **54.56** | 62.84 | 56.24 | **45.11** | **69.50** |

Reasoning mean averages the twelve metrics in Table 1. Code mean averages HumanEval+ and MBPP+ pass@1/pass@4. Relative to LP-SFT, SRP-SFT raises MATH-500 pass@1 by **5.00 percentage points** and code mean by **3.59 points** at seed 1234. Across seeds 1234, 42, and 3407, its code mean is **69.48 ± 0.02**, compared with **66.17 ± 0.27** for LP-SFT (Table 3; mean ± sample standard deviation).

## Installation

Use **Python 3.12** on Linux. Cache construction and full-parameter training use CUDA GPUs; the main setting uses eight A800-80GB GPUs. The objective examples and unit tests run on CPU.

```bash
git clone https://github.com/yxwang1215/SRP-SFT.git
cd SRP-SFT

# Training, reference caches, diagnostics, and unit tests.
python3.12 -m venv .venv-train
source .venv-train/bin/activate
python -m pip install -r requirements-train.txt
```

Generation and scoring use a separate environment because the pinned vLLM and training stacks require different Transformers versions:

```bash
python3.12 -m venv .venv-eval
source .venv-eval/bin/activate
python -m pip install -r requirements-eval.txt
```

The exact dependency pins are in [requirements-train.txt](requirements-train.txt) and [requirements-eval.txt](requirements-eval.txt). Run the commands below from the repository root.

## Quickstart

### Try the objective

This small example needs only PyTorch and runs without a model download or GPU:

```python
import torch
from srpsft.objectives import local_preserving_loss

# Target token 0; non-target candidates 1 and 2.
# Reference margin: 4 - 2 = 2. Student margin: 3 - 2 = 1.
student_logits = torch.tensor([[[6.0, 3.0, 2.0]]], requires_grad=True)
loss, metrics = local_preserving_loss(
    selected_logits=student_logits,
    target_ids=torch.tensor([[0]]),
    top_ids=torch.tensor([[[1, 2]]]),
    base_top_logits=torch.tensor([[[4.0, 2.0]]]),
    valid_mask=torch.tensor([[True]]),
    variant="srp",
    mu=1.0,
    rank_margin_fraction=1.0,
)
loss.backward()
print(metrics["aux_loss"].item())  # 1.0: the margin shortfall
```

### 1. Build the reference cache

Activate the training environment. The cache stores reference signals at supervised response positions and is reused across methods and training seeds.

```bash
source .venv-train/bin/activate

torchrun --standalone --nproc_per_node=8 -m scripts.precompute_cache \
  --model Qwen/Qwen3-4B-Base \
  --dataset HuggingFaceH4/ultrafeedback_binarized \
  --dataset-revision 3949bf5f8c17c394422ccfab0c31ea9c20bdeb85 \
  --split train_sft --output artifacts/cache/train \
  --top-k 10 --max-length 2048 --batch-size 2 --seed 1234 \
  --save-target-logits
```

The default cache stores the reference's overall top-K; the loss excludes the supervised token. Add `--exclude-target-from-topk` to select exactly K non-target tokens during cache construction.

### 2. Train SRP-SFT

```bash
torchrun --standalone --nproc_per_node=8 -m scripts.train \
  --model Qwen/Qwen3-4B-Base \
  --cache artifacts/cache/train \
  --output outputs/srpsft/seed1234/train --method srpsft \
  --epochs 1 --micro-batch-size 1 --effective-batch-size 128 \
  --learning-rate 2e-5 --warmup-ratio 0.03 --beta2 0.95 \
  --top-k 10 --mu 1.0 --rank-margin-fraction 1.0 \
  --seed 1234 --metrics-jsonl
```

Training uses bf16, AdamW, cosine decay, gradient checkpointing, and DeepSpeed ZeRO-2 by default. For this setting, it exports a Hugging Face checkpoint under `outputs/srpsft/seed1234/train/epoch-01-step-478/` and writes resumable DeepSpeed checkpoints, `run_config.json`, and per-step `train_metrics.jsonl`.

Use `--method lpsft --mu 1.0` for LP-SFT, or `--method ce --mu 0.0` for CE, with separate output directories. Change `--seed` to 42 or 3407 for the other main-study seeds.

### 3. Evaluate the checkpoint

Switch to the evaluation environment. MATH-500 uses 16 samples per problem at temperature 0.6:

```bash
source .venv-eval/bin/activate
CKPT=outputs/srpsft/seed1234/train/epoch-01-step-478

python -m evaluation.evaluate_math \
  --model "$CKPT" --mode chat --suite math500 \
  --tensor-parallel-size 8 --seed 1234 --n 16 \
  --max-tokens 4096 --max-model-len 8192 \
  --output outputs/srpsft/seed1234/eval/math500.jsonl
```

For HumanEval+, generate 20 samples per task and then execute the EvalPlus tests on CPU:

```bash
python -m evaluation.evalplus_codegen \
  --model "$CKPT" --mode chat --dataset humaneval \
  --tensor-parallel-size 8 --seed 1234 \
  --n-samples 20 --temperature 0.8 --top-p 1.0 \
  --max-tokens 4096 --max-model-len 8192 \
  --output outputs/srpsft/seed1234/eval/humaneval.jsonl

python -m evaluation.run_evalplus_cpu \
  --dataset humaneval \
  --samples outputs/srpsft/seed1234/eval/humaneval.jsonl
```

Use `--dataset mbpp` in both code-evaluation commands for MBPP+. Mathematical suites also include `aime` (32 samples by default) and `gsm8k`. Evaluators retain per-sample outputs and write summary JSON files.

## Method

For a selected reference-preferred pair `(i, j)`, let its reference and student logit margins be `Δᵀ = zᵀᵢ − zᵀⱼ` and `Δˢ = zˢᵢ − zˢⱼ`. SRP-SFT adds a one-sided hinge to the ordinary target CE:

$$
\mathcal{L}_{\mathrm{SRP},t}
= \frac{1}{|\mathcal{P}_t|}
\sum_{(i,j)\in\mathcal{P}_t}
\max\left(0,\rho\Delta^T_{ij,t}-\Delta^S_{ij,t}\right),
\qquad
\mathcal{L}=\mathcal{L}_{\mathrm{CE}}+\mu\mathcal{L}_{\mathrm{SRP}}.
$$

Pairs are oriented by the frozen reference, ties are ignored, and the loss is averaged over supervised response positions. The headline setting uses **K = 10, ρ = 1, μ = 1**, with at most 45 pairs per position. The hinge is a soft training penalty; it does not impose a hard constraint on every update.

| Parameter | CLI flag | Role |
|:--|:--|:--|
| K | `--top-k` | Candidate coverage; pair count grows quadratically |
| ρ | `--rank-margin-fraction` | Requested fraction of each reference margin |
| μ | `--mu` | Auxiliary weight relative to target CE |

At `ρ = 0`, the auxiliary penalizes ranking inversions. At `0 < ρ < 1`, it permits bounded contraction. At `ρ = 1`, it requests the reference margin; at `ρ > 1`, it requests a larger margin. LP-SFT instead minimizes forward KL between reference and student distributions renormalized over the non-target candidates.

The loss and its diagnostics are implemented in [srpsft/objectives.py](srpsft/objectives.py).

## Experiments

[run_paper.sh](run_paper.sh) records the full cache → training → evaluation → diagnostics sequence and method-specific settings. The Quickstart separates these stages so each uses its own environment.

| Experiment | Entry point or flags |
|:--|:--|
| SFT baselines | `--method ce`, `lpsft`, `srpsft`, `dft`, `eaft`, `gem`, `asft` |
| Ranking comparisons | `rank_order`, `rank_mse`, `ranknet`, `listnet`, `listmle`, `spearman`, `kendall`, `smooth_srp`, `bild`, `bild_full`, `rlkd` |
| Sensitivity | `--top-k`, `--mu`, `--rank-margin-fraction` |
| Pair-graph controls | `--pair-graph adjacent` or `top1_rest` |
| Two-sided penalty | `--srp-penalty two_sided_l1` |
| Candidate controls | `--include-gt`; `--candidate-source random_k` with a cache built using `--random-k` |
| Longer training | `--epochs 10 --save-quarter-hf` |
| Other backbones | `--model` during cache construction and training; `--zero-stage 3` for larger models |
| Entropy-matched evaluation | `scripts.fit_logit_scale` followed by evaluator `--logit-scale` |

For held-out diagnostics, build a second cache using `--split test_sft --output artifacts/cache/heldout` with the same model, dataset revision, and cache settings. Then use the training environment:

```bash
source .venv-train/bin/activate

torchrun --standalone --nproc_per_node=8 -m scripts.heldout_diagnostics \
  --model outputs/srpsft/seed1234/train/epoch-01-step-478 \
  --cache artifacts/cache/heldout \
  --output outputs/srpsft/seed1234/diagnostics.json \
  --max-examples 998 --rho 1.0
```

The diagnostics report rank flips, margin contraction, local KL, and entropy curves. For broad likelihood benchmarks such as MMLU, ARC-Challenge, HellaSwag, LogiQA2, and BBH, use the pinned `lm-evaluation-harness` in the evaluation environment; task settings are described in Appendix D of the paper.

## Repository structure

```text
SRP-SFT/
├── srpsft/                 # Objectives, baselines, tokenization, and cache loading
├── scripts/                # Cache construction, training, and diagnostics
├── evaluation/             # Math/code generation, scoring, and HF fallback
├── tests/                  # CPU tests for objectives, baselines, and cache data
├── assets/                 # README figure rendered from the paper
├── requirements-train.txt  # Pinned training and test dependencies
├── requirements-eval.txt   # Pinned generation and scoring dependencies
├── run_paper.sh            # Full experiment sequence and method settings
└── SRP_SFT__Selective_Rank_Preserving_Supervised_Fine_Tuning.pdf
```

Generated caches belong in `artifacts/`; checkpoints and evaluation outputs belong in `outputs/`. Both are excluded from version control.

## Tests

```bash
source .venv-train/bin/activate
python -m pytest -q
```

The CPU tests cover objective values and gradients, candidate masking, margin controls, SFT baselines, and cached-data loading.

## Citation

If you use this work, please cite the accompanying manuscript:

```bibtex
@misc{wang2026srpsft,
  title = {Beyond Distribution Matching: Selective Margin Preservation for Supervised Fine-Tuning},
  author = {Yuxuan Wang and Guangxiang Zhao and Xinyu Tan and Yahui Han and
            Xinxiang Yin and Zhonghai Wu and Xiangzheng Zhang and Lin Sun and Tong Yang},
  year = {2026},
  eprint = {2610.19685},
  archivePrefix = {arXiv},
  primaryClass = {cs.LG},
  url = {https://arxiv.org/abs/2610.19685}
}
```
