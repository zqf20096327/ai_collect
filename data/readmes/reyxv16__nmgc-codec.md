# NMGC - Nested Manhattan Grid Codec

A codec for compressing neural network weights, designed for memory-constrained
inference: keep the whole model in RAM (or read it from disk) in compressed
form, and decompress only the tensors actually in use, at load time or per
layer.

Two complementary variants:

| Variant | Loss | Quality knob | Typical ratio |
|---|---|---|---|
| `NestedGridCodec` | Lossy (adjustable) | `bits` per value | 3-30x depending on bits and structure |
| `ResidualCodec` (RVQ) | Lossy (adjustable) | `bits` + learned codebooks | ~5-8x, lower RMSE than uniform at the same bitrate |
| `LosslessCodec` | None (bit-exact) | - | 1.07-2.25x (bounded by data entropy) |

- **Rust decoder with a C ABI** (`libnmgc`): bit-exact vs the Python reference,
  ~150-270 MB/s, callable from any engine (C/C++, Python ctypes, Rust).
- **Hierarchical access**: the nested grid levels are bit-fields of the
  combined index, so a coarse approximation can be decoded with only the
  high bits (coarse-to-fine / progressive loading).
- **llama.cpp integration**: a minimal loader patch lets llama.cpp run with
  weights decoded from a `.nmgc` container (`LLAMA_NMGC_FILE`). Measured:
  TinyLlama-1.1B f16 PPL 7.508 -> 7.527 at 8 bits (2.06x smaller), -> 7.596
  at 6 bits (2.79x smaller).

## How it works

The idea maps intuitive concepts to concrete math:

| Concept | Implementation |
|---|---|
| what3words-style cells | Uniform grid index over the normalized range [0,1) |
| Points (x, y) in a plane | Values are paired into 2D points (`dims=2`) |
| Angles -> orthogonal steps | **Manhattan distance**: the low bits of the combined index are the (dx, dy) steps from the cell corner. No trigonometry |
| Nested grids ("apply the plane inside a cell") | **Bit slicing**: the combined B-bit index is split into levels (level 0 = most significant bits = coarse cell; deeper levels refine). Nesting is literally the bit structure of the index |
| Reference point (anchor) | Per-dimension normalization (global min/scale) or **per-block** (`block=K`), like block-wise FP8 |
| Differential coding | Zigzag delta between consecutive indices + **Huffman** (small deltas dominate -> few bits) |
| "A model to predict the point inside the cell" | `ResidualCodec`: k-means codebook per level on the residuals (residual vector quantization) |
| Bit-level compression | MSB-first packing, canonical Huffman, long codes via a secondary table |

### Honest math (important)

1. A nested uniform grid with B total bits is **equivalent to a single uniform
   grid with B bits**: same quantization error (<= `range / 2^(B+1)` with
   midpoint reconstruction). Nesting buys:
   - **coarse-to-fine access** (progressive/streaming loading),
   - **small coarse deltas** -> much better Huffman on correlated tensors,
   - the base for **learned per-level codebooks** (RVQ), which does beat a
     uniform grid at the same bitrate.
2. **Lossless compression is bounded by data entropy**: weight mantissas are
   nearly random, so `LosslessCodec` (XOR-delta + zlib) typically reaches
   1.05-2.25x. Large ratios only come from controlled loss.
3. The angle/parallax/triangle ideas reduce to Manhattan steps: they add
   trigonometric cost without accuracy gain.

## File format

A `.nmgc` container stores an index (tensor name -> offset/length) followed by
one NMGC blob per tensor. Each blob has a small header:

```
magic "NMGC", version, bits, levels, dims, ndim, shape, block, bits-per-level,
n_points, tail_n, n_blocks, per-block or global min/scale (f32),
then one packed integer stream per dimension (fixed-width or Huffman with
delta), then the optional tail element.
```

Decoding a blob produces the tensor values as `float32` with the original
shape. `nmgc_get` (Rust CLI) decodes any tensor by name from a container.

## Results

### Synthetic (2M values, fp32)

| Family | bits | Ratio | rel_RMSE | cosine |
|---|---|---|---|---|
| NMGC gaussian | 4 | 11.4x | 0.178 | 0.985 |
| NMGC gaussian | 6 | 6.7x | 0.044 | 0.999 |
| NMGC gaussian | 8 | 4.7x | 0.011 | 0.9999 |
| NMGC correlated | 4 | 29.6x | 0.196 | 0.953 |
| NMGC correlated | 8 | 13.8x | 0.012 | 0.9998 |
| int8 (baseline) | 8 | 4.0x | 0.011 | 0.9999 |
| int4 (baseline) | 4 | 8.0x | 0.182 | 0.984 |
| Lossless | - | 1.07x | 0 | 1.0 |

NMGC at 8 bits beats int8 at the same error (4.7x vs 4.0x on i.i.d. weights;
13.8x vs 4.0x on correlated weights) thanks to delta + Huffman.

### Real models

Tensors from DeepSeek-V4-Flash-0731 (already FP8/I8 with block scales) and
Qwen3.8-27B, decoded to f32 and compressed:

| Tensor (source) | Codec | Ratio | rel_RMSE | cosine |
|---|---|---|---|---|
| expert w1 (I8+scale) | NMGC 4b | 8.2x | 0.062 | 0.9981 |
| expert w1 (I8+scale) | NMGC 6b | 5.4x | 0.015 | 0.9999 |
| expert w1 raw (I8) | Lossless | 1.03x | 0 | 1.0 |
| **embed.weight (BF16)** | NMGC 4b | **26.1x** | 1.17 | 0.655 |
| **embed.weight (BF16)** | NMGC 6b | **14.7x** | 0.28 | 0.944 |
| **embed.weight (BF16)** | NMGC 8b | **7.8x** | 0.069 | 0.996 |
| **embed.weight (BF16)** | **Lossless** | **2.25x** | 0 | 1.0 |
| embed (baseline) | int4 | 8.0x | 1.37 | 0.804 |
| wq_a (FP8+scale) | NMGC 6b | 5.9x | 0.024 | 0.9997 |
| Qwen3.8-27B layer-0 (BF16) | NMGC 6b | ~5.7x | - | - |

The embedding compresses losslessly to 2.25x (7.1 bits/value from BF16) and
lossily at 8 bits to 7.8x with cosine 0.996 - 3.6x smaller than int4 with much
better quality. Already-quantized I8/FP8 tensors leave little lossless margin
(1.03-1.19x), but NMGC at 4-6 bits halves them with bounded error.

### End-to-end: trained MLP (64-128-64-4, 4 classes, 93.4% reference)

| Variant | Acc | dAcc | Ratio |
|---|---|---|---|
| NMGC 4 bits | 0.9333 | -0.0007 | 8.9x |
| NMGC 6 bits | 0.9333 | -0.0007 | 5.7x |
| NMGC 8 bits | 0.9340 | 0.0000 | 4.0x |
| RVQ 6 bits | 0.9347 | +0.0007 | 5.6x |
| Lossless | 0.9340 | 0.0000 | 1.07x |

### llama.cpp integration (TinyLlama-1.1B f16, perplexity on a ~5k-token corpus)

| Weights | Size | PPL | dPPL vs original |
|---|---|---|---|
| Original f16 (GGUF) | 2.05 GB | 7.5079 +/- 0.385 | - |
| **NMGC 8 bits (.nmgc)** | **997 MB (2.06x)** | **7.5267 +/- 0.387** | +0.019 |
| **NMGC 6 bits (.nmgc)** | **735 MB (2.79x)** | **7.5955 +/- 0.393** | +0.088 |

The monotonic PPL degradation with fewer bits confirms llama.cpp is executing
weights decoded from the NMGC container. See `INTEGRATION_llamacpp.md` and
`llamacpp_nmgc.patch`.

## Memory savings (RAM estimates)

Model-wide estimates at nominal bit rates (headers/tables are negligible on
large tensors; effective bits can be lower with delta + Huffman):

| Model | Params | Original on disk | NMGC 4 bits | NMGC 6 bits |
|---|---|---|---|---|
| Qwen3.8-27B (dense, BF16) | ~25.9B | 51.7 GB | ~13 GB | ~19 GB |
| DeepSeek-V4-Flash (MoE, FP8) | ~150B | 155.4 GB | ~75 GB | ~112 GB |

Note: decoding to f16 for compute requires ~2 bytes/param of RAM. For a 27B
model that is ~52 GB, so on memory-limited hardware the practical pattern is:
keep the compressed container in RAM/disk and decode only the tensors of the
layer in use (AirLLM-style). `nmgc_get` provides exactly this primitive
(~270 MB/s).

## Installation

```bash
pip install numpy scikit-learn gguf   # core: numpy; extras: sklearn (RVQ), gguf (pack_gguf)
cd rust && cargo build --release      # optional: Rust decoder / CLI (nmgc.dll, nmgc_get.exe, nmgc_bench.exe)
```

Run the tests:

```bash
python -m pytest nmgc/tests
```

## Usage

```python
from nmgc import NestedGridCodec, ResidualCodec, LosslessCodec
import numpy as np

weights = np.random.normal(0, 0.02, size=(4096, 4096)).astype(np.float32)

# Lossy, adjustable: error ~= range / 2^(bits+1) per value
c = NestedGridCodec(bits=6, levels=2, dims=2, block=512, entropy="auto")
blob = c.compress(weights)              # -> bytes
rec  = c.decompress(blob)               # -> np.ndarray, same shape

# Learned codebooks (RVQ) - lower RMSE at the same bitrate
rc = ResidualCodec(bits=6, levels=2, fit_subset=100_000)
rec = rc.decompress(rc.compress(weights))

# Lossless (bit-exact, handles NaN/inf/-0.0)
lc = LosslessCodec()
rec = lc.decompress(lc.compress(weights))

# Progressive (coarse-to-fine): decode with only the top k bits of the index
rec_coarse = c.decompress_coarse(blob, keep_bits=4)
```

CLI tools (Rust):

```bash
nmgc_get.exe model.nmgc --list                       # list tensors
nmgc_get.exe model.nmgc token_embd.weight out.f32    # decode one tensor
nmgc_bench.exe blob.nmgc                             # decode speed benchmark
```

Pack a model (safetensors or GGUF) into a `.nmgc` container:

```bash
python -m nmgc.experiments.pack_model <model_dir> model.nmgc --prefix model.language_model. --bits 6 --block 512
python -m nmgc.experiments.pack_gguf  <model.gguf>  model.nmgc --bits 6 --block 512
```

Benchmarks and validation:

```bash
python -m nmgc.experiments.bench_synthetic    # compression-vs-error curves
python -m nmgc.experiments.bench_real         # real DeepSeek-V4-Flash tensors
python -m nmgc.experiments.mlp_e2e            # trained MLP accuracy after compression
python -m nmgc.experiments.validate_rust      # Rust decoder bit-exact vs Python
```

## Repository structure

```
nmgc/
  codec.py          # NestedGridCodec: nested grid + delta + Huffman
  rvq.py            # ResidualCodec: learned per-level codebooks (RVQ)
  lossless.py       # LosslessCodec: XOR-delta + zlib
  huffman.py        # canonical Huffman (long codes via secondary table)
  bitio.py          # MSB-first bit reader/writer
  metrics.py        # RMSE, cosine, ratio, bits/value
  safetensors_io.py # raw safetensors reader (FP8/BF16) + tensor extraction
  rust/             # Rust decoder (libnmgc): C ABI + CLI tools
  tests/            # unit tests
  experiments/      # benchmarks, packing tools, validation
INTEGRATION_llamacpp.md   # llama.cpp loader patch documentation
llamacpp_nmgc.patch       # the patch (apply with: git apply llamacpp_nmgc.patch)
skills/nmgc-compression/  # agent skill: apply NMGC to any project (SKILL.md + references + example)
LICENSE
```

## Agent skill

`skills/nmgc-compression/` is a packaged skill that lets an AI agent apply
NMGC compression to any project: choosing lossy bits vs lossless, packing
models into `.nmgc` containers, decoding tensors on demand, integrating with
llama.cpp, and validating quality. It includes the algorithm reference, the
binary format spec, measured results, and a runnable example. Install it by
copying the folder into your agent's skills directory, or use the zip in
`dist/nmgc-compression.zip`.

## License

MIT - see [LICENSE](LICENSE).

---

❤️ Hecho con cariño por Reinaldo Moreno
