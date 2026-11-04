<div align="center">

# Tema_Q-Abliterated

**SCAPE: search-based LLM uncensoring that runs on a CPU-only PC — up to 49× faster candidate evaluation**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/badge/version-3.0.1-informational.svg)](pyproject.toml)
[![PyPI](https://img.shields.io/pypi/v/temaq-abliterated)](https://pypi.org/project/temaq-abliterated/)

[Overview](#overview) •
[Highlights](#highlights) •
[How SCAPE Works](#how-scape-works) •
[Key Features](#key-features) •
[Installation](#installation) •
[Quick Start](#quick-start) •
[Usage](#usage) •
[Guard Mode](#guard-mode---guard) •
[Experimental Results](#experimental-results) •
[Supported Architectures](#supported-architectures) •
[Notes](#notes) •
[Citation](#citation)

</div>

---

## Overview

Tema_Q-Abliterated is a research tool that **automatically finds good settings for directional ablation** (also called abliteration). It builds on the finding of Arditi et al. (2024) that *refusal behavior is mediated by a single direction in the residual stream*.

Choosing which layers to modify, and how strongly, is the hard part: too strong destroys the model's general ability, too weak leaves refusals in place. The search algorithm in this tool, **SCAPE (Structured Cached Abliteration with Prefix Evaluation)**, automates that choice. It runs on modest hardware, including a **CPU-only PC with 16 GB RAM**, which existing GPU-based tools do not support.

Some models go further and spread their refusal across **multiple internal directions** — a known countermeasure against single-vector abliteration, on which any rank-1 operation saturates. For those models the tool offers **guard mode (`--guard`)**: the rank-1 directional operation is replaced by a **multi-direction weight redirection** — a data-driven, arbitrary-rank weight update fitted per module from captured activations — while the evaluation (surrogate metric, KL, search, verification) stays on exactly the same fast SCAPE pipeline. See [Guard Mode](#guard-mode---guard) for the mathematics.

> **Research use only.** Uncensored models operate with their safety filters removed. Always follow the original model's license and terms of use, and handle the output strictly within research and educational contexts.

For the algorithm and full experiments, see the technical report: [Tema_Q-Abliterated_Technical_Report](docs/Tema_Q-Abliterated_Technical_Report.pdf) .

---

## Highlights

| | |
|---|---|
| **Fast candidate evaluation** | A surrogate metric replaces full-text generation and is up to **~49× faster**. |
| **Works without a GPU** | A 4B-class model finishes on a Core i7 with 16 GB RAM. |
| **Better results in less time** | On the same Colab T4 GPU, Qwen3.5-4B reached **8/100** refusals in **61 min**, versus 27–74/100 in 4 h+ for heretic. |
| **Quality-first objective** | Minimizes KL divergence from the original model *subject to* a target refusal rate, so the model is not over-modified. |
| **Multi-direction guard mode** | `--guard` replaces the single-direction operation with an arbitrary-rank weight-redirection fit for models whose refusal is spread across multiple directions. |
| **Safe by design** | Never writes out a model without your confirmation unless you pass `--select auto`. |

---

## How SCAPE Works

1. **Seed grid (≈ 8 evaluations).** The search starts by testing a small set of systematic settings across the strength × layer-band range. This always includes the uniform all-layer orthogonalization of Arditi et al. (the *reference solution*), so the search does not get stuck in a narrow local optimum.
2. **Floor calibration.** The surrogate metric cannot reach zero, even for a fully uncensored model, because tokens that grammatically continue a refusal sentence always keep some probability mass. We call this the **grammatical floor**. SCAPE measures it from the seed grid and adjusts the target accordingly, so the search keeps making progress instead of stalling.
3. **Range-normalized objective.** On strongly-tuned models the floor itself can be high (≈ 0.57 measured on a 35B MoE), leaving only a narrow usable range. The refusal penalty in J is scaled by that measured range, so the *unperturbed* model can never win J against a real orthogonalization candidate — the failure mode where the search stalls around a no-op baseline is eliminated.
4. **Pattern search.** Starting from the best seed, a pattern search refines the settings. Hopeless candidates are rejected early using an exact lower bound.
5. **In-search generative quality check.** Teacher-forced surrogate metrics cannot see generative collapse (the model regurgitating the prompt or emitting chat role templates). After each trial the candidate is *actually* generated on a few fixed harmful prompts, and the real refusal rate plus collapse signals are folded into J, so the search cannot minimize into a collapsed basin. Enabled by default in guard mode (`--gen-check`).
6. **Verification.** Only a few top candidates are checked with real text generation. The gate is **floor-relative** (a candidate is skipped only when it sits far above the measured floor), so heavily-tuned models no longer have every candidate skipped by an absolute threshold. The verification also runs a strict **collapse check** (prompt-echo rate, role-template rate, repetitive answers, NLL blow-up).
7. **Human-in-the-loop export.** You choose the final candidate. The output weights are always built from the **original safetensors** in fp32, so quantization used during the search never reduces output precision.

Speed comes from three techniques: a **rank-1 hook** (no weight rewriting per trial), a **multi-boundary prefix cache** (layers before the perturbation are computed only once), and **INT4 streaming with a memory guard**.

---

## Key Features

- **CPU-only search** — Each trial takes only a few seconds, so 0.5B–9B models can be processed without a GPU.
- **Seed-grid initialization** — About 8 evaluations at the start cover the whole strength × bandwidth spectrum, including the reference solution.
- **Grammatical-floor calibration** — The floor is measured from the seed grid and the effective target is redefined accordingly; when full-generation verification data exists, the floor is re-estimated from the measured (surrogate, true-refusal) points so residual refusal cannot hide inside the "floor".
- **Guard mode (`--guard`)** — Multi-direction weight redirection for models whose refusal is spread across multiple internal directions. The surrogate evaluation, KL, search, floor calibration and verification are identical to normal mode, so results stay comparable.
- **Refinement phase and frontier tracking** — After the main loop, a half-step pattern search runs from both the best-J start and the lowest-refusal frontier start; the frontier candidate is always injected into the final verification pool.
- **INT4 evaluation and memory guard** — Weights use about 1/3.6 the memory of bf16, with streaming load, an elastic cache, and automatic OOM fallback.
- **Tiered weight offload** — VRAM → DRAM → SSD weight placement with streaming GEMM, so a run never stops on a CUDA OOM even when the model does not fit in memory.
- **Safe export** — If no candidate passes the verification gate, nothing is exported without your confirmation.
- **Interrupt and resume** — A checkpoint is saved after every trial; on re-run, resume options appear before model loading.
- **LoRA adapter export** — The uncensoring delta can be written as a PEFT-compatible adapter (a few MB) instead of the full model; in guard mode the adapter is the exact fitted update.
- **Direct card-driven apply** — `--params-from` / `--params-mode direct` re-applies published model-card parameters without loading the model.
- **Hugging Face integration** — Optional upload after export (the repository name automatically gets the suffix `-Tema_Q-Abliterated`), plus an auto-generated model card that keeps the original model's tags and always points `base_model` at the original model.
- **Minimal dependencies** — Only torch, transformers, safetensors, huggingface-hub, matplotlib, and psutil (no Optuna, PEFT, or bitsandbytes).

---

## Installation

### Requirements

- Python 3.10 or higher
- PyTorch 2.2 or higher (install beforehand for your environment)
- transformers 5.x for the Qwen4Exp and Gemma4 series (DeepSeek V4.1 needs 5.6+; LFM2.5-24B-A2B needs a version that supports `lfm2_moe`)

### From PyPI (recommended)

```bash
pip install temaq-abliterated
```

This places the `temaq-abliterated` command in your PATH. To use Hugging Face datasets as verification prompts:

```bash
pip install "temaq-abliterated[datasets]"
```

### From source (for development)

```bash
git clone https://github.com/ek15072809/Tema_Q-Abliterated.git
cd Tema_Q-Abliterated
pip install -e .
```

---

## Quick Start

```bash
# A model on Hugging Face
temaq-abliterated Qwen/Qwen3.5-0.8B

# A local model directory
temaq-abliterated /path/to/gemma4-E2B

# Limited memory or a larger model: use INT4 evaluation
temaq-abliterated Qwen/Qwen3.5-4B --eval-dtype int4

# A model whose refusal is spread across multiple directions
temaq-abliterated deepseek-ai/DeepSeek-V4.1-Flash-1017 --eval-dtype int4 --guard

# Recommended: cap the runtime
temaq-abliterated Qwen/Qwen3.5-4B --eval-dtype int4 --time-budget-min 60 --trials 200
```

Unless `--workdir` is given, this structure is created in the launch directory:

```
tq_workspace/
└── <model-name>/
    ├── cache/    … downloads and checkpoints
    ├── output/   … uncensored model (safetensors)
    └── report/   … refusal-rate curve, memory timeline, run record
```

### Rough runtime guide

Processing time scales roughly linearly with model size. These are guidelines, not guarantees.

| Model size | CPU (12–16 threads) | Colab T4 GPU |
|---|---|---|
| 0.5–1B | 60–120 min | 10–20 min |
| 4B | 240–360 min | 40–60 min |

---

## Usage

### Tiered weight offload: never stop on CUDA OOM

Small free-tier GPUs (limited VRAM, limited DRAM, no swap) die as soon as a model does not fit in VRAM. The loader supports a three-tier weight placement so the run completes anyway:

| Tier | Location | How it works |
|---|---|---|
| 0 (VRAM) | compute device | same as before — fastest |
| 1 (DRAM) | CPU RAM | each forward copies only the needed row-block of a weight to the GPU and computes there (streaming GEMM, ~8 MB chunks) |
| 2 (SSD) | scratch files (`numpy.memmap`) | when DRAM overflows too. The OS page cache automatically keeps "whatever fits" in DRAM — on swap-less machines this acts as the missing virtual memory |

```bash
# Default: offload engages automatically when the model does not fit VRAM (GPU)
#          or RAM (CPU). Nothing to pass on a big enough machine.
temaq-abliterated big-org/big-model-32B --eval-dtype int4

# Force it (e.g. a 30B+ model on a small-VRAM GPU)
temaq-abliterated big-org/big-model-32B --eval-dtype int4 --offload ssd
```

CUDA OOM no longer stops the run at any point:

- **During model load** — the load is retried automatically with tiered offload enabled.
- **During the streamed load** — every weight is placed into its tier **as soon as it is read and quantized**, so RAM holds at most one shard in flight and the load never stalls midway on low-DRAM machines.
- **During search / verification / generation** — the INT4 dequant cache shrinks, some VRAM-resident weights are demoted to DRAM, and the batch size is halved, then the operation retries. INT4 dequantization allocates its output buffer on the compute device and tier moves carry module biases along, so the GPU paths are device-mismatch-safe; a residual device audit runs right before the smoke test.

| Option | Default | Description |
|---|---|---|
| `--offload` | `auto` | `auto` = enable when needed / `dram` = force DRAM tier only / `ssd` = force DRAM+SSD tiers / `off` = disable |
| `--offload-vram-gb F` | auto (free VRAM × 0.85 − activation reserve) | manual VRAM weight budget |
| `--offload-dram-gb F` | auto (free RAM × 0.60) | manual DRAM weight budget |
| `--offload-scratch DIR` | `<cache>/offload` | SSD-tier scratch directory (put it on a fast local disk) |

Notes: the perturbation-target `o_proj`/`down_proj` weights and the embeddings get VRAM priority (they are needed on every forward and cannot use the INT4 dequant cache); INT4 modules fill the remaining VRAM and overflow to DRAM/SSD in layer order. Fused 3D MoE experts that cannot be streamed are auto-converted to INT4 when they do not fit. The run record (`run_summary.json`) contains the final placement statistics under `offload`.

### Output only the uncensoring LoRA adapter

`--lora-only` is a shorthand for `--export-format lora` that writes **only the PEFT-compatible adapter** (a few MB) instead of the full model — the natural companion to offload runs, since the full-model export needs to stream gigabytes through DRAM while the adapter needs almost nothing:

```bash
temaq-abliterated Qwen/Qwen3.5-14B --eval-dtype int4 --offload ssd --lora-only
```

The adapter export reads the base weights **one tensor at a time**, and the full-model export streams shards through mmap views without materializing them.

However, it does not support three-dimensional structures that cannot be represented using LoRA adapters.

### Output files

After a run completes:

| Path | Contents |
|---|---|
| `<workspace>/output/<model-name>-uncensored/` | Uncensored model (safetensors + model card + LICENSE) |
| `<workspace>/report/refusal_curve.png` | Refusal-rate convergence graph |
| `<workspace>/report/memory_timeline.png` | Memory usage timeline |
| `<workspace>/report/run_summary.json` | Run record |

### Final candidate selection

Unless `--select auto` is given, a selection UI is always shown before export. Candidates that fail the verification gate are excluded from the list. The gate is floor-relative: a candidate is skipped only when its first-token or mass-weighted surrogate refusal sits more than `--verify-gate` (default 0.4) above the floor measured from the seed grid (an absolute first-token gate is used when no floor is available). If no candidate passes, the model is not exported without your confirmation. Directly adopting a trial by number (`t41`) offers to run the full-generation verification first.

### Verification-anchored floor recalibration

Recent models distribute their refusal across multiple internal directions — a countermeasure against single-vector abliteration. Consequence: even the strongest single-direction orthogonalization saturates the surrogate metric at ≈ 0.57–0.60 while *true* full-generation refusal stays high (measured: 58%). The seed-based floor calibration mistakes this saturation point for the "grammatical floor", relaxes the effective target, and the search settles for mild candidates.

When full-generation verification results exist (baseline + verified candidates), SCAPE fits a line `surrogate = G + D × true_refusal` through the measured points and takes G — the surrogate value at *zero true refusal* — as the grammatical floor estimate:

| Situation | Behavior |
|---|---|
| Floor is genuine (orthogonalization drives true refusal to ≈ 0) | The fit gives G ≈ seed floor, so nothing changes (self-neutralizing on healthy models). |
| Residual refusal at the floor (multi-directional refusal) | G comes out well below the seed floor, the effective target is lowered, the refusal penalty in J turns back on, and the search keeps pushing true refusal down instead of settling. |

The recalibration is pure arithmetic on already-measured data (zero extra forward passes). It is applied on checkpoint resume, right after a verification round, and when you add trials from the selection UI — and it is exactly the situation that guard mode (below) addresses at the weight-operation level.

### Stable INT4 streaming load for huge MoE models

Large MoE checkpoints previously died silently mid-load on memory-constrained machines. The loader avoids the three causes: fused 3D experts that are perturbation targets are auto-converted to INT4 only when keeping them in bf16 cannot fit in memory; fused expert tensors are INT4-packed directly from the shard chunk-by-chunk the moment they are read; split-form per-expert tensors are restored/quantized as soon as one container's full expert set has arrived. A per-shard GC keeps the load-time peak low. The result: the load completes (paging if necessary, slower but stable) instead of being force-killed, on any model.

### Output format: full model or LoRA adapter

`--export-format` selects what to write:

| Value | Output |
|---|---|
| `model` (default) | The full uncensored model. |
| `lora` | Only a **PEFT-compatible LoRA adapter** (`adapter_config.json` + `adapter_model.safetensors`). Merge it onto the base model to reproduce the abliteration. |
| `both` | Both of the above (the adapter goes to `<output>-lora`). |

The adapter's base model and parameters are recorded in its model card, and the card can be read back with `--params-from`. Merging:

```python
from transformers import AutoModelForCausalLM
from peft import PeftModel
model = AutoModelForCausalLM.from_pretrained("<base model>", dtype="bfloat16")
model = PeftModel.from_pretrained(model, "<adapter directory>")
model = model.merge_and_unload()
```

With the default row-norm-preserving ablation the adapter approximates the weight update with a truncated SVD (`--lora-rank`, default 32) and the merged model is numerically near-identical to the full export; with `--norm-preserve off` the adapter is the **exact** rank-1 update; in guard mode the adapter is the **exact** fitted multi-direction update (rank = the fitted rank). Fused 3D MoE experts cannot be expressed as a standard LoRA target and are excluded from the adapter with a warning — use `--export-format model` for those models if full fidelity matters.

### Check the result with your own prompts

After export, pass `--prompt-test` (or answer the on-screen offer in an interactive terminal) to chat with the uncensored model before finishing:

```
prompt> Write a totally ordinary story about a robot.
  output: Once there was a little robot named Bolt...
```

The selected parameters are applied to the in-memory model (INT4 evaluation models work too), generation is greedy/deterministic, and an empty line or Ctrl+C ends the test. In pseudo-terminals such as Colab, `input()` still works, so `--prompt-test` can be used there as well.

### Re-apply parameters from a model card without loading the model

`--params-from` loads the "Abliteration parameters" table from any published uncensored model card (path or URL), and `--params-mode` decides what to do with it:

| Mode | Behavior |
|---|---|
| `focus` (default) | Narrow the search around the loaded values (exploration with a reduced range taken from the card). |
| `apply` | Use the values as-is without searching. The model is loaded once to compute (or reuse cached) refusal directions / redirection factors. |
| `direct` | **No model load, no search**: build only the module skeleton on the meta device, reuse the factors cached by a previous run of the same model, and patch the weight shards directly. |

```bash
# Once: a normal (or --params-mode focus) run caches the factors
# of the model under tq_workspace/<model>/cache/…

temaq-abliterated Qwen/Qwen3.5-4B \
    --params-from https://huggingface.co/<user>/<model>/raw/main/README.md \
    --params-mode direct
```

Model cards do not contain the direction vectors or redirection factors themselves, so `direct` requires one previous run of the same model (they are saved automatically). Without a cache the tool explains this and exits instead of silently loading the model. `--export-format lora/both` works in `direct` mode too.

### Upload to Hugging Face Hub

After export you will be asked "Upload to Hugging Face?". In non-interactive environments:

```bash
temaq-abliterated Qwen/Qwen3.5-4B \
    --hf-repo my-uncensored --hf-token hf_xxxxxxxx
```

The suffix `-Tema_Q-Abliterated` is appended to the repository name automatically.

### Interrupt and resume

A checkpoint is saved after every trial. Re-running the same command shows this menu before the model is loaded:

1. Continue search
2. Add more trials
3. Export model from recorded candidates
4. Start over
5. Exit

The menu appears in every interactive launch (including `--guard` / `--quiet` runs); non-interactive/piped runs auto-resume. Old checkpoints are course-corrected on resume: recorded trials are recomputed under the current objective, the best candidate is re-picked, and the verification-anchored floor recalibration runs whenever full-generation verification data exists — no evaluation is repeated.

---

## Guard Mode (`--guard`)

Some models — especially recent guardrail-tuned releases — spread their refusal across **multiple internal directions**. Any rank-1 operation (classic abliteration) saturates on them: the surrogate refusal rate stops at a floor while true full-generation refusal stays high. Guard mode answers this at the weight-operation level, while keeping every other part of the pipeline — surrogate evaluation, KL, seed grid, pattern search, floor calibration, generative quality check, final verification, selection UI — **exactly** as in normal mode, so measured numbers stay comparable.

```bash
temaq-abliterated org/guarded-model --eval-dtype int4 --guard
```

### What changes

| Component | Normal mode | Guard mode |
|---|---|---|
| Weight operation | Rank-1 directional orthogonalization: `W' = W − w·v(vᵀW)` with the layer's refusal direction `v` | **Multi-direction weight redirection**: an arbitrary-rank update `ΔW` fitted per module from captured activations, applied as `W' = W + w·(B@A)` |
| Where the directions come from | Difference of means of harmful/harmless activations (one vector per layer) | Full input/output activation statistics on harmful and harmless probes (the update spans every direction the data identifies) |
| Fused MoE experts (incl. INT4-packed) | Output-side rank-1 hook on the routed expert sum | Equivalent **output-space transform** on the container output — every routed expert's down matrix gets the same left transform, no packed weights touched |
| Search parameters | strength × layer band (+ direction index) | strength × layer band (the strength scales the fitted update: 1.0 = the fitted solution, below = partial, above = extrapolation) |
| Surrogate metric / KL / floor calibration / verification | SCAPE fast pipeline | **identical** |
| Probes, markers, lexicons | built-in direct harmful / harmless sets | **identical** (same evaluation) |
| LoRA adapter | rank-1 exact or SVD approximation | the **exact** fitted update factors |
| Caches / checkpoints | `runs/<model>.json`, `directions/resolved-<model>.pt` | stored per mode (`-guard` suffix) so measured numbers never mix |

### How the fit works

1. **Capture.** Every perturbation-target module (attention out-projection, MLP down-projection) records its input and output activations at the last prompt position, on the harmful and harmless probe sets.
2. **Redirection targets.** Each harmful output is pulled toward the mean of its *k* nearest harmless outputs (k-NN attraction). An over-correction term (`--guard-steer`) extrapolates the target beyond the harmless cluster for stronger steering on heavily-guarded models.
3. **Closed-form fit.** The update solves a ridge-regularized least-squares problem: *move harmful outputs onto their targets, leave harmless outputs unchanged* (the harmless-preservation term plays the role of norm preservation), with the update rank decided by the data — no "one direction" assumption. The dual form (probe-count-sized matrix) keeps the solve trivial even for large models, and the optimal rank truncation (Eckart–Young) caps the factors at `--guard-rank`.
4. **Apply.** The fitted factors are applied by forward hooks, exactly like the rank-1 operation in normal mode — no weight rewriting per trial, INT4-packed MoE experts included, and the layer-band kernel scales the update so the search machinery (seeds, pattern search, prefix cache) works unchanged.
5. **Export.** The output model is written from the original safetensors in fp32 as `W' = W + w·(B@A)` (weight space) or `W'_e = W_e + w·(M·W_e)` per expert slice (output space); a startup self-check verifies the hook against the full patch.

| Option | Default | Description |
|---|---|---|
| `--guard-steer F` | 0.5 | Over-correction of the redirection targets: 0 = pull harmful outputs exactly onto their nearest harmless outputs; higher values extrapolate beyond the harmless cluster. |
| `--guard-neighbors N` | 4 | k of the k-NN redirection target. |
| `--guard-rank N` | 32 | Rank cap of the fitted per-module update (the actual rank is data-driven up to this cap; also the LoRA rank of guard-mode adapter exports). |

Guard mode additionally defaults the in-search generative quality check to 3 prompts (`--gen-check 0` disables) and the refinement phase to auto (`--refine-trials`), since a full-matrix update can be a larger weight change than a rank-1 one and benefits from both the real-generation guard rail and the extra low-refusal refinement.

---

### Options

Run `temaq-abliterated --help` for the full list. The main options are grouped below.

**Input / output**

| Option | Default | Description |
|---|---|---|
| `--workdir DIR` | `./tq_workspace/<model-name>` | Working directory (cache, checkpoints, output, reports). |
| `--output DIR` | auto | Output directory. It cannot be the same as, or inside, the original model. Empty folders are used as-is; on conflict you are asked to re-enter or an automatic number is added. |
| `--hf-repo NAME` | — | Hugging Face repository name (the suffix `-Tema_Q-Abliterated` is appended). Use with `--hf-token` for non-interactive upload. |
| `--hf-token TOKEN` | — | Hugging Face API key (write permission). |
| `--language` | `en` | Language of output logs: `en` (English) or `jp` (Japanese). |
| `--no-export` / `--dry-run` | — | Skip writing the output model. |
| `--export-format` | `model` | `model` = full uncensored model / `lora` = PEFT-compatible LoRA adapter only / `both` = both. |
| `--lora-only` | off | Shorthand for `--export-format lora` — write only the uncensoring LoRA adapter (a few MB). Recommended on memory-limited machines. |
| `--lora-rank N` | 32 | LoRA rank for adapter export (SVD approximation rank; exact rank-1 when `--norm-preserve off`; in guard mode the fitted update itself). |
| `--prompt-test` | off | After export, interactively type prompts and check the generated output of the uncensored model. |

**Search**

| Option | Default | Description |
|---|---|---|
| `--trials N` | auto | Number of search trials (200 on GPU, 120 on CPU). |
| `--time-budget-min F` | 0 (unlimited) | Time budget for the search phase, in minutes. When reached, the best solution so far proceeds to verification. **Use this to control runtime.** |
| `--target-refusal F` | 0.03 | Target soft refusal rate of the surrogate metric (lower = stronger uncensoring). |
| `--components` | `both` | Components to search: `attn`, `mlp`, or `both`. When `attn` is specified, fused MoE experts are also INT4-quantized. |
| `--n-probe N` | 0 (auto) | Number of probes used in the search (auto: 48–24 depending on model scale). |
| `--kl-tokens N` | 8 | Teacher-forced tokens for the multi-position KL (0 = first token only). |
| `--no-probe-hardening` | off | Disable hardening of harmful probes (use only probes that the base model refuses). |
| `--guard` | off | Guard-strong model mode: multi-direction weight redirection (see [Guard Mode](#guard-mode---guard)). |
| `--guard-steer F` | 0.5 | [guard] Over-correction strength of the redirection targets. |
| `--guard-neighbors N` | 4 | [guard] k of the k-NN redirection target. |
| `--guard-rank N` | 32 | [guard] Rank cap of the fitted per-module update. |
| `--params-from FILE` | — | Path or URL to an external model card (README.md) to load parameters from. |
| `--params-mode` | `focus` | `focus` = narrow the search around the loaded values; `apply` = use them as-is (model loaded, factors computed or cached); `direct` = apply without loading the model and without searching (needs factors cached by a previous run). |
| `--refine-trials N` | `-1` (auto) | Extra refinement trials after the main search: `-1` = auto (~trials/4 up to 25 in guard mode), `0` = off. Half-step pattern search from the best-J and lowest-refusal starting points. |
| `--gen-check N` | `-1` (auto) | In-search generative quality check: `-1` = auto (3 probes in guard mode), `0` = off, 1–3 = probe count. `--gen-check` alone is accepted as 3. |
| `--gen-tokens N` | 16 | Tokens generated per in-search quality-check prompt. |
| `--norm-preserve` | on | Row-norm-preserving orthogonalization (turn off for comparison experiments; ignored in guard mode, where preservation is part of the fit). |
| `--seed N` | random | Random seed. |
| `--resume` / `--restart` | — | Resume from the checkpoint / discard it and start over. |

**Memory / precision**

| Option | Default | Description |
|---|---|---|
| `--eval-dtype` | `auto` | `auto` (planned from free memory) / `bfloat16` / `float16` / `float32` / `int8` / **`int4`**. |
| `--dequant-cache-gb F` | auto | Budget for the INT4 weight cache in GB. A negative value means "decide from free RAM after loading". |
| `--offload` | `auto` | Tiered weight offload (VRAM → DRAM → SSD) so the run never stops on a CUDA OOM. `auto` = enable when the model does not fit / `dram` / `ssd` / `off`. See [Tiered weight offload](#tiered-weight-offload-never-stop-on-cuda-oom). |

**Verification and selection**

| Option | Default | Description |
|---|---|---|
| `--verify` | `auto` | `auto` = verify top candidates with full generation; `full` = best candidate only; `none` = no verification. |
| `--verify-probes N` | `-1` | Number of prompts used for verification: `-1` = auto (100 prompts); `0` = **disable the final verification entirely**; `>0` = use that many prompts. |
| `--verify-dataset DS` | — | Hugging Face dataset for verification prompts (`repo` or `repo:split`; the first N samples are used, and the test split is preferred if no split is given). |
| `--verify-topk N` | 5 | Number of top candidates verified with full generation; `0` = **disable the verification entirely** (on CPU: original + 2 candidates = 3 in total). |
| `--verify-gate F` | 0.4 | Threshold for skipping full-generation verification. It is judged on the floor-free first-token ratio, because the mass-weighted ratio has a grammatical floor of about 0.3–0.4. |
| `--max-new-tokens N` | 64 | Tokens generated during verification. |
| `--select` | `interactive` | `interactive` = always show the selection UI before export; `auto` = choose automatically. Switches automatically in non-interactive environments. |
| `--harmful-file` / `--harmless-file` | built-in | Use your own prompt files (one prompt per line). |

---

## Experimental Results

All numbers come from the run records (JSON and PNG reports) produced by this tool. Refusal rates are measured by full-text generation on 100 harmful prompts (the same prompt set was used for both tools so they can be compared). **KL** is the KL divergence from the original model; lower means the original behavior is better preserved.

### Results on each model

| | Qwen3.5-0.8B | Qwen3.5-4B | gemma4-E2B | LFM2.5-2.6B | XHToken/Spark-X2.6-4B |
|---|---|---|---|---|---|
| Trials | 12 | 59 | 200 | 85 | 40 |
| Refusal rate of best candidate | **0/100** | **8/100** | 20/100 | **2/100** | **0/100** |
| KL of best candidate | 0.0186 | 0.0266 | 0.0199 | 0.0143 | 0.0353 |

### Comparison with heretic (Qwen3.5-4B)

heretic was run in a reduced configuration (85 and 95 trials) so that results would not be lost to the Colab session limit of 5 h 30 min.

| | heretic run 1<br>(Colab T4) | heretic run 2<br>(Colab T4) | **SCAPE**<br>(Colab T4) | **SCAPE**<br>(Windows CPU, 16 GB) |
|---|---|---|---|---|
| Total run time | 4 h 2 min | 4 h 25 min | **1 h 1 min** | 6 h 35 min |
| Search time | 3 h 35 min | 3 h 25 min | **40 min** | 3 h 0 min |
| Trials (random init.) | 85 (20) | 95 (5) | 59 (0) | 21 (0) |
| Refusal rate of best candidate | 74/100 | 27/100 | **8/100** | **7/100** |
| KL of best candidate | 0.0164 | 0.0391 | 0.0266 | 0.0335 |

- On the same GPU, SCAPE finished in about **one quarter of the time** and reached a lower refusal rate.
- On a **GPU-less Windows PC (Core i7, 16 GB RAM)**, an environment where heretic cannot run, SCAPE still reached 7/100.
- The KL computation is not guaranteed to be identical across the two tools, so treat the KL columns as a rough guide, not a strict comparison.

### Evaluation speed (Qwen3.5-0.8B, INT4, 2 CPU cores)

| Method | Content | Time per candidate |
|---|---|---|
| **SCAPE surrogate evaluation** | 16 probes × 1 forward pass | **4–7.5 s** |
| Full-text generation | 24 prompts × 32 tokens (measured) | about 50 s |
| Full-text generation | 100 prompts × 32 tokens (scaled from measurement) | about 208 s (≈ 28–49× slower) |

### Effect of the seed grid and floor calibration (Qwen3.5-0.8B, INT4, 2 CPU cores)

| | Without seed grid and floor calibration | **SCAPE** |
|---|---|---|
| Refusal rate (40 prompts) | 0.94 → 0.10 (36 trials, 395 s) | **0.900 → 0.000 (12 trials, 148 s)** |
| KL of best candidate | 0.0237 | **0.0186** |
| Reference solution reached | not within 31 trials | **at the 2nd seed evaluation** |

---

## Supported Architectures

Model structure is detected automatically by attribute probing:

- **Attention output projection**: `self_attn.o_proj`, `out_proj`, `o_b_proj` (DeepSeek V4-series grouped low-rank output projection), `linear_attn.out_proj`, etc.
- **MLP down projection**: `mlp.down_proj`, fused 3D expert tensors (under `mlp` **and** `feed_forward`, as in LFM2.5-24B-A2B), shared experts (`shared_expert` / `shared_experts`), `layer.experts`, etc.
- Dense, MoE, hybrid linear attention, and multimodal models (language-model part)
- Hyper-connection width mismatch in the Qwen4Exp series, and the 4D multi-stream (mHC) residual states of the DeepSeek V4 series
- Shared-KV safe bypass depth in the Gemma4 series
- Automatic resolution of the language backbone in VLMs
- Remote-code models shipped with `auto_map`: downloaded and loaded with `trust_remote_code=True`, and the code files are carried over to the exported model
- Remote code written for transformers 4.x also runs on transformers 5.x: a runtime compatibility shim handles the `_tied_weights_keys` (list → dict) and mask-creation argument changes during loading, and the exported code files carry a self-adapting compatibility block so the output model loads on both 4.x and 5.x (behavior on 4.x is unchanged)

Architecture coverage is verified by attribute probing on real models; the numerical equivalence of the partial forward pass and of the hook-based patching against full fp32 patches has been confirmed on real hardware.

---

## Project Structure

```
Tema_Q-Abliterated/
├── README.md                  … This file
├── LICENSE                    … MIT
├── pyproject.toml
├── src/temaq_abliterated/     … Core
│   ├── cli.py                 … Pipeline orchestration
│   ├── search.py              … SCAPE search, seed grid, floor calibration
│   ├── surrogate.py           … Fast evaluator
│   ├── matrixfit.py           … Guard mode: multi-direction redirection fit
│   ├── engine.py              … Perturbation engine (rank-1 + redirection hooks)
│   ├── quant4.py              … INT4 quantization
│   ├── modelio.py             … Model I/O and model-card generation
│   ├── arch.py                … Architecture detection
│   └── ...
└── docs/                      … Research materials
```

---

## Notes

- This tool is designed for research into the internal refusal mechanisms of models.
- Uncensored models operate with safety filters removed. Handle them with care and follow the original model's license and terms of use.
- Use for harmful purposes is not intended. Please use the tool responsibly, within research and educational contexts.
- The quality metrics of an output model (KL, refusal rate, collapse check) are reference values; actual behavior varies with prompts, model size, and seed.

---

## References

1. Andy Arditi, Oscar Obeso, Aaquib Syed, Daniel Paleka, Nina Panickssery, Wes Gurnee, and Neel Nanda. "Refusal in Language Models Is Mediated by a Single Direction." [arXiv:2406.11717](https://arxiv.org/abs/2406.11717), 2024 (NeurIPS 2024). — The finding on which directional ablation is based.
2. Philipp Emanuel Weidmann. "heretic: Fully automatic censorship removal for language models." <https://github.com/p-e-w/heretic> (AGPL-3.0). — A pioneering tool for automated parameter search, used as the comparison baseline in this project.

Tema_Q-Abliterated is an independent implementation and is not affiliated with the projects above.

---

## License

MIT License.

The directional ablation technique itself is publicly available knowledge originating in the academic literature (Arditi et al., 2024).

---

## Citation

If Tema_Q-Abliterated is useful in your work, please consider citing it:

```bibtex
@software{temaq_abliterated2026,
  author = {ek15072809},
  title  = {Tema_Q-Abliterated},
  year   = {2026},
  url    = {https://github.com/ek15072809/Tema_Q-Abliterated}
}
```

---

## Author

**ek15072809**
