# Mouse Behavioral Clone

Train a personalized mouse trajectory model on **your own** mouse movements, then use it to generate human-like cursor paths in browser automation.

## Architecture

Three-stage pipeline where each component handles one specialization:

```
Bezier (skeleton)  →  NoiseModel (spatial)  →  GRU (temporal)  →  125Hz resample
```

| Stage | Role | Output |
|---|---|---|
| **Bezier** | Fixed algorithm, generates curve skeleton, guarantees arrival | (x, y) spatial path |
| **NoiseModel** | Learns your personal spatial deviation from Bezier | (x, y) personalized path |
| **GRU (MouseModelV3)** | Learns your personal timing — receives spatial path, predicts arrival times | per-point timestamps |
| **125Hz resample** | Upsamples GRU output to realistic mouse event rate | ~125Hz events, ±3ms jitter |

**Model-led (>80%)**: NoiseModel controls path shape, GRU controls velocity curve. **Algorithm (<20%)**: Bezier provides skeleton reference, 125Hz resample simulates hardware sampling rate.

<p align="center">
  <img src="assets/demo_comparison.png" alt="Demo: Pipeline vs Bezier" width="100%">
</p>

<p align="center">
  <img src="assets/demo_animation.gif" alt="Animation: Mechanical vs Bezier vs GRU Model" width="100%">
</p>

> **Left**: Trajectory from the three-stage pipeline (Bezier skeleton + NoiseModel spatial deviation + GRU temporal profile). Colors indicate velocity (blue=slow, yellow=fast).
>
> **Right**: Pure cubic Bezier curve with fixed mathematical formula.
>
> *Models trained on the author's real mouse data. Your model will produce different trajectories.*

```bash
# Generate the animation yourself
python examples/animate_demo.py --save output.gif
```

## Why?

Most browser automation frameworks "humanize" mouse movements with the same set of Bezier curves and fixed jitter distributions. This creates a **shared behavioral fingerprint** — detect one instance, detect them all.

By training a model on your own mouse trajectories, you get:

- **Unique movement patterns** — your velocity curve, your micro-pauses, your correction style
- **Statistical indistinguishability** — distribution of generated trajectories matches your real distribution
- **Lightweight** — ~2MB GRU model + ~166KB NoiseModel, CPU inference <5ms

## Quick Start

### 1. Install

```bash
pip install torch numpy matplotlib
```

### 2. Collect your data

1. Install the Tampermonkey browser extension
2. Create a new script, paste `collector/mouse_collector.user.js`
3. Browse normally for a few days
4. Click Tampermonkey → Export, save the `.jsonl` file(s) into the `data/` directory

> The training script auto-discovers all `.jsonl` files in `data/` — no need to configure paths.

### 3. Train NoiseModel (spatial personalization)

```bash
python training/generate_trajectories.py --train-noise --epochs 100
```

Learns your personal spatial deviation from ideal Bezier paths from real data. Outputs `training/noise_model.pt` (~166KB).

### 4. Train GRU (temporal personalization)

Place your `.jsonl` files in the `data/` directory:

```bash
# Quick prototype: 200 records, 80 epochs
python training/train_mouse_model.py --epochs 80 --max_records 200

# Full training: all data, 200 epochs
python training/train_mouse_model.py --epochs 200
```

| Flag | Default | Description |
|---|---|---|
| `--epochs` | 200 | Total training epochs |
| `--max_records` | 0 (all) | Limit real data to N records |
| `--lr` | 1e-3 | Learning rate |
| `--batch_size` | 128 | Batch size |
| `--hidden` | 128 | GRU hidden size |
| `--real_weight` | 10 | How many times to repeat real data |
| `--warmup_epochs` | 5 | Epochs with pure teacher forcing before scheduled sampling |
| `--max_self_roll` | 0.30 | Max fraction of steps using model predictions (scheduled sampling) |
| `--train_noise` | 0.01 | Gaussian noise std on input features |
| `--resume` | None | Resume from checkpoint path |

Output: `training/model/best.pt` (~2MB)

> **Incremental training:** Start with 50-100 trajectories to validate the pipeline. Keep collecting data and retrain — each run produces a new `best.pt`. The model gradually converges to your personal style.

### 5. Visualize

```bash
# Static comparison: Pipeline vs Bezier
python examples/demo.py
python examples/demo.py --start 100 200 --end 800 500 --tag BUTTON
python examples/demo.py --save output.png

# Animated GIF: Mechanical / Bezier / GRU three-way comparison
python examples/animate_demo.py --save output.gif
python examples/animate_demo.py --start 200 300 --end 1100 650 --save output.gif --fps 12
```

### 6. Integrate into browser automation

```python
from mouse_controller import move_to_humanized

# Move to target
await move_to_humanized(page, target_x, target_y, tag="BUTTON")
# Then click
await page.click(target_x, target_y)
```

Model path precedence:
1. `MOUSE_MODEL_PATH` environment variable
2. `training/model/best.pt` (relative to `mouse_controller.py`)
3. Fallback: pure Bezier curve (no model loaded)

## Model Details

### NoiseModel (spatial personalization) — `training/generate_trajectories.py`

| Layer | Detail |
|---|---|
| Input | `[sx, sy, cx1, cy1, cx2, cy2, ex, ey]` — Bezier control points (normalized to viewport) |
| Encoder | FC(8→128) → ReLU → FC(128→128) → ReLU → hidden state |
| Decoder | 2-layer GRU, hidden=128, dropout=0.2, auto-regressive generation |
| Decoder input | `[prev_x, prev_y, progress, dx_to_target, dy_to_target]` (5-dim) |
| Output | `[next_x, next_y]` — spatial only, no timing |
| Size | ~166KB |

**Training strategy:** First 5 epochs pure teacher forcing (tf_ratio=1.0), then linear decay to 0.0 (fully self-rolling). Position-dependent weight: last 20% of trajectory gets 1x→4x penalty to ensure endpoint convergence. Trained exclusively on real data.

**Inference fallback:** If the generated last point deviates >2px from target, the last 3 points are linearly blended toward the target (k=1→100%, k=2→67%, k=3→33%).

### GRU / MouseModelV3 (temporal personalization) — `training/train_mouse_model.py`

| Layer | Detail |
|---|---|
| Input (per step) | `[dx_to_target, dy_to_target, prev_dx, prev_dy, prev_dt, progress]` (6-dim) |
| Tag Embedding | 22 HTML tags → 16-dim |
| Context | `[start_x, start_y, end_x, end_y, tag_embed]` (20-dim) → FC → ReLU → FC → ReLU → hidden |
| GRU | 2 layers, hidden=128, dropout=0.1 |
| Output head | FC(128→64) → ReLU → Dropout(0.1) → FC(64→3) |
| Output | `[delta_x, delta_y, delta_t]` — relative deltas |
| Time transform | log1p on raw dt (compresses [0.008s, 3494s] → [0, 8.8]) |
| Size | ~2MB |

**Training strategy:** MSE+clip loss (clip target_t at 0.15 log1p, ~160ms) to preserve speed variation while suppressing extreme outliers. Position-dependent weight: last 20% of trajectory gets 4x penalty. Scheduled sampling: warmup_epochs with teacher forcing, then linear decay to max_self_roll (0.30).

**Inference:** speed_factor=0.70 (model predicts slower than real, scaled to match median). Fallback endpoint convergence: last 3 points blended to target if deviation >2px. `generate_from_path()` accepts a spatial path from NoiseModel and predicts personalized timestamps.

### 125Hz Resampling — `train_mouse_model.py::_resample_to_realistic_rate()`

GRU output is ~30 points at ~36Hz, far below real mouse sampling rates. The resampling layer:

- **Adaptive interval**: fast movement → sparse events (~14ms), slow/deceleration → dense events (~4ms), based on local velocity
- **±3ms temporal jitter**: Gaussian noise (σ=1.5ms, clipped to 4-14ms range) simulating hardware sampling noise
- **±0.3px spatial jitter**: sub-pixel sensor noise
- **Variable point count**: same start/end produces 20-80+ events per generation, preventing fixed-count fingerprinting

### `generate()` — end-to-end generation (standalone, no spatial path input)

When no spatial path is provided, `MouseModelV3.generate()` generates both spatial path and timing from scratch using target-directed stepping with physiological tremor (σ≈4px at 1920px viewport), structured oscillation (3-8px perpendicular wobble), and end-game micro-corrections (hesitation wobble when dist < 6% of viewport).

## Repo Structure

```
mouse-behavioral-clone/
├── assets/
│   ├── demo_comparison.png          # Static trajectory comparison
│   └── demo_animation.gif           # Animated 3-way comparison
├── collector/
│   └── mouse_collector.user.js      # Data collection (Tampermonkey script)
├── training/
│   ├── train_mouse_model.py         # GRU model + training
│   ├── generate_trajectories.py     # NoiseModel training + synthetic data
│   ├── noise_model.pt               # Pre-trained NoiseModel
│   ├── model/                       # Trained GRU models (best.pt)
│   └── requirements.txt
├── inference/
│   ├── mouse_controller.py          # Runtime inference (3-stage pipeline)
│   └── virtual_cursor.py            # In-page cursor overlay JS
├── examples/
│   ├── demo.py                      # Static visualization (Pipeline vs Bezier)
│   └── animate_demo.py              # Animated 3-way comparison GIF
└── data/                            # Place your .jsonl files here
```

## Limitations

- ~100 real trajectories is enough for proof of concept; thousands is better for production
- Multi-modal behavior (keyboard, scroll cadence) is not yet modeled
- NoiseModel assumes "real = Bezier + residual" — a generative approach (diffusion/VAE) would be more expressive
- Scheduled sampling is slow on large datasets; pure teacher forcing with input noise is recommended for fast iterations

## License

[MIT](LICENSE) — Free to use, modify, and distribute.

## Reference

FP-Agent: Fingerprinting AI Browsing Agents, arXiv:2605.01247, May 2026
