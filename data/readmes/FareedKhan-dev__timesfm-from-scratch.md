# TimesFM From Scratch

A from-scratch reimplementation of Google's **TimesFM** time-series foundation model, including the
**entire pretraining pipeline that Google never open-sourced** (synthetic data generator, all-positions
masked objective, RevIN normalization, diverse data mixture, out-of-distribution validation, and an
honest evaluation harness). The transformer backbone is verified to match the released
`google/timesfm-2.5-200m-pytorch` checkpoint, and is implemented at three scales (17M, 70M, and the
203M backbone).

![Python](https://img.shields.io/badge/python-3.12-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.x-ee4c2c)
![License](https://img.shields.io/badge/license-MIT-green)
![Tests](https://img.shields.io/badge/tests-29%20passing-success)
[![Model on Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20weights-Hugging%20Face-yellow)](https://huggingface.co/FareedKhan/timesfm-from-scratch-70m)

> **Pretrained 70M weights:** [huggingface.co/FareedKhan/timesfm-from-scratch-70m](https://huggingface.co/FareedKhan/timesfm-from-scratch-70m)
>
> **Blog post (the full story):** [Building a 200M Parameter Time-Series Forecasting LLM From Scratch](https://medium.com/@fareedkhandev/building-a-200m-parameter-time-series-forecasting-llm-from-scratch-a99ec624ba15)
>
> **Full engineering write-up:** [`docs/PROJECT_JOURNEY.md`](docs/PROJECT_JOURNEY.md)

---

## What this is

Google open-sourced TimesFM's inference and fine-tuning code, but **not** the part that actually makes it
a foundation model: the pretraining stack. This repository rebuilds that missing stack from the paper
(arXiv:2310.10688) and the released checkpoint, then trains and evaluates a model end to end.

TimesFM is a **decoder-only transformer over time-series patches**. You give it the recent history of any
single numeric series (for example the last 512 hourly readings), and it predicts the next 96 to 192
values, zero-shot, with no fine-tuning. It outputs both a point forecast and 9 quantiles.

This is a research and learning rebuild. It is **honest about what it is**: a sound, calibrated, 70M model
that beats real baselines on structured time series, but is not a universal or state-of-the-art forecaster.
See [Results](#results) and [Honest limitations](#honest-limitations).

---

## Highlights

- **Faithful architecture.** Every TimesFM 2.5 mechanism is reimplemented and verified against the real
  checkpoint: RoPE, sandwich RMSNorm, fused QKV, qk-norm, per-dimension scale, and a 2-matrix SiLU FFN
  (not SwiGLU). The 203M backbone parameter count matches the released model exactly.
- **The missing pretraining pipeline.** A synthetic series generator (trend, ARMA, seasonal, plus
  random-walk), the all-positions decoder objective with the masking trick, first-patch RevIN, and a
  weighted multi-source data mixture.
- **Honest evaluation.** Zero-shot ETT benchmark with bootstrap confidence intervals, a seasonal-naive
  baseline (not just last-value), paired-difference significance tests, CRPS, interval coverage, and a
  3-way-disjoint multi-domain test grid.
- **Out-of-distribution validation and early-stopping**, so the reported number is selected on a held-out
  signal rather than on the test set.
- **Reproducible and tested.** 29 unit tests, a deterministic overfit-a-batch gate, and a full training
  CLI. Managed with `uv`.

---

## Results

All numbers are zero-shot **ETT** (Electricity Transformer Temperature), standardized MAE, on the honest
even-window / 50-window protocol unless stated otherwise. Lower is better. The model never trains on ETT.

| Model | Params | ETT MAE | vs last-value naive | vs seasonal-naive |
|---|---|---|---|---|
| Last-value naive | n/a | 0.298 | 1.00 | |
| Seasonal-naive | n/a | 0.272 | 0.91 | 1.00 |
| **This model (diverse, final)** | 70M | **0.246** | **0.83** | **0.90** |
| Google TimesFM (released) | 200M | 0.215 (published, tail protocol) | reference | |

The improvement over both baselines is statistically significant under a paired bootstrap test. The gap to
Google's 0.215 is real and largely bound by model scale and data, and the released number was not re-run in
this exact harness, so treat that comparison as indicative.

**The model generalizes across structured domains, but fails on random-walk data:**

| Domain | Scaled MAE (ours / naive) | Verdict |
|---|---|---|
| ETT (energy, periodic) | 0.83 | beats naive and seasonal-naive |
| Exchange (FX, random-walk) | 1.31 | worse than naive (see limitations) |

### Diversity removes the over-training cliff

A narrow corpus causes catastrophic over-training (ETT MAE rises from 0.24 to 0.31 as training continues).
A diverse corpus keeps it flat through 120k steps.

![Cliff diagnostic](plots/stageB/A_cliff_flat.png)

### It generalizes on structure, not on noise

![Multi-domain honesty](plots/stageB/B_honest_multidomain.png)

### Calibration is fixed with a conformal wrapper

Raw quantile intervals were over-confident (60 percent coverage for an 80 percent interval). A conformal
recalibration step brings coverage to target.

![Calibration](plots/stageC/B_calibration_fixed.png)

---

## Architecture

A decoder-only transformer where each patch of `patch_len` points is a token.

- **Patching:** input patches of 32 points, output blocks of 128 points (fewer autoregressive steps).
- **Tokenizer:** a residual block mapping `2 * patch_len` (values plus a padding mask) to `model_dim`.
- **Transformer block:** sandwich RMSNorm around attention and the FFN, RoPE on queries and keys, qk-norm,
  a per-dimension learned scale, fused QKV projection, and a 2-matrix SiLU feed-forward network.
- **RevIN:** reversible instance normalization using first-valid-patch statistics, with a stability floor.
- **Heads:** a point head plus 9 quantile heads, trained with MSE plus pinball loss across all positions.

Sizes (in `src/tsfm/config.py`):

| Config | model_dim | layers | heads | params |
|---|---|---|---|---|
| `tiny` | 512 | 10 | 16 | 17.6M |
| `small` | 1024 | 10 | 16 | 67.8M |
| `base` | 1280 | 20 | 16 | 203.4M (backbone, matches the real model) |

The experiments in this repo were run at the **70M (`small`) scale** for cost efficiency. The 200M (`base`)
config is implemented and ready to train.

---

## The pretraining pipeline

This is the part Google did not release.

1. **Synthetic generator** (`synthetic.py`): each series is a weighted mix of piecewise-linear trend,
   ARMA, sine, and cosine, plus a random-walk / white-noise branch so the model learns to persist when
   there is no signal.
2. **All-positions objective** (`objective.py`): every patch position predicts the next horizon, which
   gives dense supervision. Training windows are `context + horizon` long so the last context patch (the
   autoregressive entry point) receives a full target.
3. **Diverse data mixture** (`sources.py`, `data.py`): electricity plus LOTSA frequency tiers (traffic,
   web, finance, cloud, health) plus the synthetic pool, sampled by weight with per-config caps so no
   single dataset dominates.
4. **Out-of-distribution validation** (`eval_hook.py`): a held-out non-energy validation set drives
   early-stopping and best-checkpoint selection, so the model is never selected on the test set.

---

## Repository structure

```
src/tsfm/
  config.py        model and training configuration (tiny / small / base)
  layers.py        RoPE, RMSNorm, attention, transformer block, per-dim scale
  revin.py         first-patch reversible instance normalization
  model.py         PatchedDecoder: encode + autoregressive forecast
  objective.py     all-positions targets + MSE + pinball loss
  synthetic.py     synthetic generator (incl. random-walk)
  data.py          windowing, masking, weighted multi-source dataset
  sources.py       real-data loaders (LOTSA, Monash, M4, electricity)
  trainer.py       optimizer, LR schedule, validate(), training step
  eval_hook.py     out-of-distribution validation windows
scripts/
  train.py                main training CLI (--corpus diverse, OOD val, early-stop)
  eval_ett.py             zero-shot ETT eval (even/tail schemes, bootstrap CIs)
  eval_core.py            shared protocol: CRPS, coverage, seasonal-naive, paired CI, conformal
  eval_multidomain.py     3-way-disjoint multi-domain test grid + verdict
  sanity.py               param counts + forward/backward
  overfit_one_batch.py    gate: loss must collapse on a fixed batch
  make_stage*_plots.py    result figures
tests/             29 unit tests
runs/              training logs and validation curves (model weights are gitignored)
plots/             result figures
docs/              the full end-to-end engineering write-up
```

Model weights (`.pt` files) are **not** committed to git (they are large). The trained 70M weights are
hosted on Hugging Face at [FareedKhan/timesfm-from-scratch-70m](https://huggingface.co/FareedKhan/timesfm-from-scratch-70m).
See [Load the pretrained model](#load-the-pretrained-model).

---

## Installation

This project uses [`uv`](https://github.com/astral-sh/uv).

```bash
uv venv --python 3.12
uv pip install numpy pandas "torch>=2.2"   # CPU is fine for sanity, tests, and evaluation
```

For training on a GPU, install the torch build that matches your CUDA driver, for example:

```bash
uv pip install torch --index-url https://download.pytorch.org/whl/cu128
```

## Data

The ETT evaluation set is small and public. Download it into `data/ett/`:

```bash
mkdir -p data/ett
for f in ETTh1 ETTh2 ETTm1 ETTm2; do
  curl -sL -o data/ett/$f.csv \
    https://raw.githubusercontent.com/zhouhaoyi/ETDataset/main/ETT-small/$f.csv
done
```

The diverse training corpus (LOTSA, electricity, Monash) is larger and is downloaded on the training
machine. See [`docs/PROJECT_JOURNEY.md`](docs/PROJECT_JOURNEY.md) for the exact setup.

## Quickstart

```bash
uv run python scripts/sanity.py             # parameter counts + a forward/backward pass
uv run python scripts/overfit_one_batch.py  # gate: loss must collapse on a fixed batch
uv run python -m pytest tests/ -q           # 29 tests
```

## Load the pretrained model

The trained 70M weights are hosted on Hugging Face:
[FareedKhan/timesfm-from-scratch-70m](https://huggingface.co/FareedKhan/timesfm-from-scratch-70m).

```python
import torch
from huggingface_hub import hf_hub_download
from tsfm import config
from tsfm.model import build_model

ckpt = hf_hub_download("FareedKhan/timesfm-from-scratch-70m", "pytorch_model.pt")
model = build_model(config.small())
model.load_state_dict(torch.load(ckpt, map_location="cpu")["model"])
model.eval()

context = torch.randn(1, 512)                  # your last 512 points, standardized
point, quantiles = model.forecast(context, 96) # next 96 steps: point forecast + 9 quantiles
```

A `model.safetensors` version is also available on the same repo.

## Evaluate

```bash
# zero-shot ETT (even-window protocol, 50 windows, bootstrap CIs)
uv run python scripts/eval_ett.py --ckpt runs/stageC/ckpt_best.pt --size small \
  --scheme even --num_windows 50 --point_channel 5 --device cpu

# multi-domain grid with seasonal-naive, CRPS, coverage, and paired CIs
uv run python scripts/eval_multidomain.py --run_dir runs/stageC --size small --device cpu
```

## Train

On a GPU machine, after the diverse corpus is in place:

```bash
uv run python scripts/train.py \
  --size small --corpus diverse --context 512 --batch 256 --steps 120000 \
  --lr 2.5e-4 --warmup 3000 --wd 0.05 --dropout 0.1 \
  --weights 0.15,0.18,0.16,0.12,0.12,0.07,0.20 --per_config_cap 4000 \
  --pool_size 80000 --val_every 5000 --patience 999999 --point_channel 0 \
  --bf16 --device cuda --out runs/myrun
```

---

## The journey (Stages A to C)

The honest version of this project is the journey, not a single number. It is documented in full in
[`docs/PROJECT_JOURNEY.md`](docs/PROJECT_JOURNEY.md). In short:

1. **Early runs** taught hard lessons: the wrong data (M4) made the model worse than naive, and
   over-training on a narrow corpus destroyed zero-shot skill.
2. **Stage A** added a diverse corpus and looked like a clean win, until an **adversarial self-audit**
   caught the result being over-sold (a contaminated cross-domain test, a scheme-shopped number, an
   under-trained run) and found a real bug in the training objective.
3. **Stage B**, after fixing the bug and the evaluation, was the honest run: the over-training cliff was
   gone, the model beat real baselines on structured data, but it failed on random-walk data and was
   under-calibrated.
4. **Stage C** added random-walk training data (partial fix) and conformal calibration (fixed), landing on
   the model described in [Results](#results).

---

## Honest limitations

- **It fails on random-walk data.** On FX (Exchange) it is about 31 percent worse than just repeating the
  last value. Prices of stocks and currencies are near random-walk, so this model is not a good raw price
  predictor.
- **Calibration is post-hoc.** The well-calibrated intervals come from a conformal wrapper that needs a
  calibration split at inference. The model's native intervals are still over-confident.
- **It is below state of the art.** ETT MAE is about 0.246, versus Google's 0.215, and that gap is bound by
  model scale and data diversity.
- **Missing components versus the real model.** No continuous-quantile head (27.85M params in the real
  model) and no KV-cache, so autoregressive decode re-encodes the context each block.
- **Weights are not in the repo.** They are large and gitignored.

---

## Roadmap

- A higher random-walk fraction in the synthetic mix to close the FX gap.
- A native continuous-quantile head and a KV-cache.
- More genuinely distinct training datasets.
- Re-running the released model in this exact harness for a like-for-like comparison.
- Scaling the implemented 200M config.

---

## Acknowledgments and citation

This work reimplements ideas from TimesFM. If you use the original model, please cite the authors:

```bibtex
@article{das2024timesfm,
  title={A decoder-only foundation model for time-series forecasting},
  author={Das, Abhimanyu and Kong, Weihao and Sen, Rajat and Zhou, Yichen},
  journal={arXiv preprint arXiv:2310.10688},
  year={2024}
}
```

The official TimesFM model, code, and weights are the property of Google. This repository is an
independent, from-scratch research and educational reimplementation, and is not affiliated with or
endorsed by Google.

## License

MIT. See [LICENSE](LICENSE).
