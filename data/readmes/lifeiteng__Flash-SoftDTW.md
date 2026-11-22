# Flash-SoftDTW

![Flash-SoftDTW](https://raw.githubusercontent.com/lifeiteng/Flash-SoftDTW/main/docs/images/banner.jpg)

**Fast, memory-lean, exact soft-DTW for PyTorch — CUDA and CPU, dense and banded, forward and backward.**

[中文文档](https://github.com/lifeiteng/Flash-SoftDTW/blob/main/README.zh-CN.md)

Flash-SoftDTW computes the soft dynamic time warping value of a batch of cost
matrices and its exact gradient (the expected alignment). It is built for
training: variable-length batches, Sakoe-Chiba bands, warp penalties, fp16 /
bf16 inputs and arbitrary strides are first-class, and the kernels never
materialize more than one `[B, T, S]` buffer.

- **Fast.** A skewed-strip wavefront kernel keeps the DP dependency chain in
  registers and warp shuffles. On an RTX PRO 6000 (Blackwell) it is
  **54–365× faster in the forward pass and 18–98× faster forward+backward**
  than a row-sequential CUDA baseline on dense problems (table below).
- **No length limit.** Sequences of any length (tested up to 4096 × 4096),
  any band width; there is no "one thread per column, at most 1024" cap.
- **Memory-lean.** Inference (`torch.no_grad()` or inputs without
  `requires_grad`) keeps only `O(B · (T + S))` scratch — no score matrix.
  Training stores a single `[B, T, S]` fp32 buffer; the backward pass
  recomputes transition probabilities on the fly instead of saving them.
- **Banded alignment in compact storage.** Pass a `[B, T, 2]` band and a
  `[B, T, W]` cost tensor: memory scales with the band width `W`, not with
  `S`, and only in-band cells are evaluated.
- **Exact and well-tested.** ~600 test cases (CPU plus two GPUs) against an independent float64
  reference: values, gradients, `torch.autograd.gradcheck`, CPU/CUDA parity,
  band construction vs. `pyts`, invariances (permutation, padding,
  `gamma → 0` → hard DTW), half / bfloat16, non-contiguous inputs.
- **Numerically careful.** Base-2 log-sum-exp with a finite sentinel instead
  of `inf` (no NaNs from `inf - inf`), and a backward pass that normalizes the
  predecessor weights directly instead of using `R - cost`, which loses
  precision for small `gamma`.

<p align="center"><img src="https://raw.githubusercontent.com/lifeiteng/Flash-SoftDTW/main/docs/images/soft_alignment.png" width="92%" alt="Soft alignment computed by Flash-SoftDTW"></p>
<p align="center"><sub>Expected alignment (the gradient of soft-DTW w.r.t. the cost matrix) of two warped signals, dense and inside a Sakoe-Chiba band.</sub></p>

## Installation

Requirements: PyTorch (tested with 2.13 + CUDA 12.9 and 2.15 CPU), `ninja`,
`setuptools >= 77`, a C++ compiler supported by your PyTorch build, and the
CUDA toolkit matching your PyTorch build for the GPU kernels.

The PyPI package is `flash-softdtw-torch` (import name `flash_softdtw`). It
is unrelated to the `flash-softdtw` package on PyPI; do not install both into
one environment, as they share the import name.

**From PyPI** (source distribution, compiled on install). Install PyTorch
first, then:

```bash
pip install flash-softdtw-torch --no-build-isolation
```

`--no-build-isolation` lets the build see your installed PyTorch (the
extension is compiled against it). The CUDA kernels are built when PyTorch has
CUDA and a CUDA toolkit is found (set `CUDA_HOME` if `nvcc` is not on `PATH`); `TORCH_CUDA_ARCH_LIST` picks
the target GPUs and `MAX_JOBS` bounds compile parallelism:

```bash
CUDA_HOME=/usr/local/cuda TORCH_CUDA_ARCH_LIST="8.0;8.9;9.0;12.0" MAX_JOBS=4 \
  pip install flash-softdtw-torch --no-build-isolation
```

If a PyPI mirror has not synced the latest release yet, add
`--index-url https://pypi.org/simple`.

**From source:**

```bash
git clone https://github.com/lifeiteng/Flash-SoftDTW.git
cd Flash-SoftDTW
pip install . --no-build-isolation
# pick target GPUs explicitly, e.g.:
TORCH_CUDA_ARCH_LIST="8.0;8.9;9.0;12.0" pip install . --no-build-isolation
```

Without a CUDA toolkit the CPU backend is built. Running from a source
checkout without installing also works: the extension is JIT-compiled on first
use.

## Quick start

```python
import torch
import flash_softdtw as fsd

x = torch.randn(32, 400, 80, device="cuda", requires_grad=True)   # [B, T, C]
y = torch.randn(32, 350, 80, device="cuda")                       # [B, S, C]
x_lens = torch.randint(200, 401, (32,), device="cuda")
y_lens = torch.randint(200, 351, (32,), device="cuda")

# 1) A loss module: distance + soft-DTW, optionally banded.
loss_fn = fsd.SoftDTWLoss(gamma=0.1, metric="sqeuclidean")
loss = loss_fn(x, y, x_lens, y_lens)
loss.backward()

# Soft-DTW divergence (Blondel et al., 2021): non-negative, 0 iff x == y.
div = fsd.SoftDTWLoss(gamma=0.1, normalize=True)(x, y, x_lens, y_lens)

# Sakoe-Chiba band: only cells within `window` steps of the diagonal.
banded = fsd.SoftDTWLoss(gamma=0.1, window=20)(x, y, x_lens, y_lens)

# 2) The raw operator on any cost matrix.
cost = fsd.pairwise_cost(x, y, metric="l1")        # [B, T, S]
value = fsd.soft_dtw(cost, x_lens, y_lens, gamma=0.1, warp_penalty=0.5)  # [B]
value.sum().backward()

# 3) Banded operator with compact storage.
band = fsd.sakoe_chiba_band(x_lens, y_lens, window=20)   # [B, T, 2] = [begin, end)
cost_b = fsd.pairwise_cost(x[:, : band.size(1)], y, "l1", band=band)  # [B, T, W]
value_b = fsd.soft_dtw(cost_b, x_lens, y_lens, band=band, gamma=0.1)
```

## Definition

For each batch element, with cells `(i, j)`, `0 ≤ i < x_len`, `0 ≤ j < y_len`:

```
R(-1, -1) = 0,   R(-1, j) = R(i, -1) = +inf,   R(cell outside the band) = +inf
R(i, j)   = C(i, j) + softmin_γ( R(i-1, j-1),  R(i-1, j) + w,  R(i, j-1) + w )
value     = R(x_len - 1, y_len - 1)
softmin_γ(a, b, c) = -γ · log(e^{-a/γ} + e^{-b/γ} + e^{-c/γ})
```

`w` is `warp_penalty`, an extra cost for horizontal / vertical steps.
`γ → 0` recovers classic DTW. The gradient of `value` with respect to `C` is
the expected alignment matrix and is returned in the same (dense or compact)
layout as `cost`, with zeros outside the band. If the end cell is outside the
band or the stored tensor, the value is `+inf` and the gradient is zero.

## API

| Function | Description |
|---|---|
| `soft_dtw(cost, x_lens=None, y_lens=None, *, band=None, gamma=1.0, warp_penalty=0.0, rows_per_block=0)` | Differentiable soft-DTW values `[B]` of `[B, T, S]` (dense) or `[B, T, W]` (compact band) costs. Any float dtype; half / bf16 accumulate in fp32 and return fp32 values. `rows_per_block` overrides the CUDA strip height (0 = auto). |
| `SoftDTWLoss(gamma=1.0, metric="sqeuclidean", window=None, warp_penalty=0.0, normalize=False, reduction="mean")` | `nn.Module` taking feature sequences `x [B, T, C]`, `y [B, S, C]` and optional lengths. `normalize=True` (soft-DTW divergence) requires `window=None`. |
| `pairwise_cost(x, y, metric="sqeuclidean", band=None, width=None)` | `"sqeuclidean"`, `"euclidean"`, `"l1"`, `"cosine"` or a callable; dense or compact band layout. `"sqeuclidean"` / `"cosine"` use matrix multiplies; `"l1"` uses a dedicated broadcast kernel pair (not `torch.cdist`), whose cost grows with the feature dimension, so prefer `"sqeuclidean"` for wide features. |
| `sakoe_chiba_band(x_lens, y_lens, window, max_len=None)` | Per-row `[begin, end)` columns of a Sakoe-Chiba band along the (non-square) diagonal, shape `[B, max_len, 2]`; pass `max_len` (the padded `T`) to avoid a device sync. |
| `band_width`, `band_columns`, `gather_band` | Helpers for compact band storage. |

Bands must be non-decreasing along `T` (true for Sakoe-Chiba and any monotone
warping window). Gradients are first order. `+inf` costs act as obstacles.
Internally values are kept in base-2 units scaled by `1 / gamma`; they must
stay below `1e29` in that unit (float32; `1e299` for float64), which only
matters for extreme `gamma` / cost combinations.

## Benchmarks

RTX PRO 6000 Blackwell Max-Q (sm_120), PyTorch 2.13 + CUDA 12.9, fp32,
`gamma = 0.05`, `warp_penalty = 10`. CUDA-event timing, median of 10 runs
after warm-up, GPU otherwise idle. Cost construction is not timed. The
baseline is an earlier row-sequential CUDA soft-DTW implementation (not part
of this repository) that computes value and gradient in one pass, so its
forward and forward+backward times coincide.
Numbers are specific to this machine.



<p align="center"><img src="https://raw.githubusercontent.com/lifeiteng/Flash-SoftDTW/main/docs/images/speedup.png" width="92%" alt="Speedup chart"></p>

**Dense, `T = S`** (milliseconds):

| B | T = S | Flash fwd | Baseline fwd | Speedup | Flash fwd+bwd | Baseline fwd+bwd | Speedup |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 128 | 0.093 | 5.28 | **56×** | 0.240 | 5.29 | **22×** |
| 1 | 512 | 0.371 | 85.7 | **231×** | 1.24 | 85.7 | **69×** |
| 1 | 1024 | 0.938 | 342 | **365×** | 3.50 | 342 | **98×** |
| 8 | 1024 | 1.01 | 349 | **345×** | 4.44 | 352 | **79×** |
| 64 | 512 | 0.383 | 96.3 | **252×** | 1.70 | 96.4 | **57×** |
| 64 | 1024 | 1.33 | 399 | **300×** | 5.14 | 400 | **78×** |
| 256 | 128 | 0.099 | 5.44 | **55×** | 0.301 | 5.47 | **18×** |
| 256 | 512 | 0.702 | 100 | **142×** | 3.55 | 100 | **28×** |
| 256 | 1024 | 2.41 | 402 | **167×** | 13.8 | 403 | **29×** |

**Large batch, narrow Sakoe-Chiba band** (`B = 512`, `T ≤ 64`, `S ≤ 160`,
window 4, variable lengths, `gamma = 0.1`, `warp_penalty = 1`): fwd 0.079 ms
vs 0.359 ms (**4.6×**), fwd+bwd 0.168 ms vs 0.369 ms (**2.2×**). At this size
(≈ 0.2 M cells) launch latency dominates, and timings of such short kernels
vary with the GPU clock state (up to ~2× faster when the GPU is already
boosted).

**Long sequences** (no length cap):

| B | T = S | fwd | fwd+bwd | extra memory (fwd+bwd) |
|---:|---:|---:|---:|---:|
| 1 | 2048 | 2.9 ms | 12.0 ms | 32 MiB |
| 8 | 2048 | 3.8 ms | 17.4 ms | 256 MiB |
| 1 | 4096 | 10.1 ms | 50.8 ms | 128 MiB |
| 8 | 4096 | 14.0 ms | 66.3 ms | 1.0 GiB |
| 64 | 4096 | 15.2 ms | 72.2 ms | 8.0 GiB |

The Flash-SoftDTW side of these tables is reproduced on your GPU by:

```bash
python benchmarks/bench.py --gamma 0.05 --warp-penalty 10 --band ""            # dense table
python benchmarks/bench.py --gamma 0.1 --warp-penalty 1 --band 512x64x160x4 --lengths ""  # narrow band
python benchmarks/long_sequences.py --gamma 0.1                                  # long sequences
```

## How it works

<p align="center"><img src="https://raw.githubusercontent.com/lifeiteng/Flash-SoftDTW/main/docs/images/wavefront.png" width="92%" alt="Skewed-strip wavefront"></p>

Rows of a problem are cut into strips of `P` rows with one thread per row.
Inside a strip, thread `k` processes column `j = jbase + t − k` at tick `t`,
so the three DP predecessors of every cell were produced one or two ticks
earlier by the same thread or by thread `k − 1`:

- neighbour values travel through `__shfl_up_sync` (one shuffle per tick);
  only warp boundaries use double-buffered shared memory, and only strip
  boundaries use a small per-problem column buffer in global memory;
- with `P = 32` a tick needs no barrier at all and a block packs four
  independent problems — the fast path for narrow bands and large batches;
- softmin runs in base 2 (`ex2.approx` / `lg2.approx`) on a branch-free path
  with a finite sentinel for unreachable cells;
- operands of the next 8 ticks are prefetched while the current ones are
  consumed;
- the backward pass replays the wavefront in reverse tick order and pushes
  expected-alignment messages (left / up / diagonal) to the predecessors,
  recomputing normalized transition weights from the saved `R`.

## Testing

```bash
pip install pytest numpy pyts
python -m pytest -q
```

CUDA tests run automatically when a GPU is visible (every visible GPU, up to
two).

## Citation

If you use Flash-SoftDTW in your research, please cite this repository and the
soft-DTW papers:

```bibtex
@software{flash_softdtw,
  author = {Li, Feiteng},
  title  = {Flash-SoftDTW: Fast, memory-lean soft-DTW for PyTorch},
  url    = {https://github.com/lifeiteng/Flash-SoftDTW},
  year   = {2026}
}
@inproceedings{cuturi2017softdtw,
  title     = {Soft-DTW: a Differentiable Loss Function for Time-Series},
  author    = {Cuturi, Marco and Blondel, Mathieu},
  booktitle = {ICML},
  year      = {2017}
}
@inproceedings{blondel2021divergence,
  title     = {Differentiable Divergences Between Time Series},
  author    = {Blondel, Mathieu and Mensch, Arthur and Vert, Jean-Philippe},
  booktitle = {AISTATS},
  year      = {2021}
}
```

## License

Apache License 2.0. See [LICENSE](https://github.com/lifeiteng/Flash-SoftDTW/blob/main/LICENSE).
