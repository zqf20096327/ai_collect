<p align="center">
  <picture>
    <img alt="Onyx Infer — native image generation for Apple Silicon" src="assets/banner.svg" width="100%">
  </picture>
</p>

<p align="center">
  <a href="https://github.com/phantom5125/onyx-infer/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/phantom5125/onyx-infer/ci.yml?label=CI" alt="CI"></a>
  <img src="https://img.shields.io/badge/platform-Apple%20Silicon%20%C2%B7%20macOS%2026.2%2B%20%C2%B7%20Metal%204-blue" alt="Platform">
  <img src="https://img.shields.io/badge/C%2B%2B-20%20%C2%B7%20Metal%20MSL-blue" alt="C++20 / MSL">
  <img src="https://img.shields.io/badge/Python-3.12%2B-orange" alt="Python 3.12+">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="MIT license"></a>
</p>
<p align="center">
  <a href="README.zh-CN.md">中文 README</a>
  &middot;
  <a href="https://phantom5125.github.io/onyx-infer/">Project site</a>
</p>

# onyx-infer

Generate **4096×4096 images directly on Apple Silicon** with MiniMax-H3-Image. Onyx Infer runs the text encoder, 33.1B DiT, and VAE locally in C++20 and Metal 4. The 4K path has been verified on a Mac Studio with an M5 Max and 36 GB of unified memory.

[Generate your first image](docs/QUICKSTART.md) · [Measured performance](#benchmarks) · [Onyx Studio](plugin/onyx-studio/README.md)

PyTorch and Diffusers support offline import and reference validation. Native generation uses MPSGraph and Metal kernels.

## Generated on Apple Silicon

Resized previews of actual Onyx output, with the original generation resolution noted in each caption.

<table>
  <tr>
    <td align="center" width="50%"><img src="site/assets/gallery/pelican-bicycle.jpg" width="480" alt="Pelican riding a red bicycle by the sea"><br><b>Pelican on a bicycle</b><br><sub>4096×4096 · direct 16 MP generation</sub></td>
    <td align="center" width="50%"><img src="site/assets/gallery/red-agate.jpg" width="480" alt="Polished red agate with translucent mineral bands"><br><b>Red agate</b><br><sub>4096×4096 · direct 16 MP generation</sub></td>
  </tr>
  <tr>
    <td align="center"><img src="site/assets/gallery/moon-surface.jpg" width="480" alt="Detailed lunar surface with crisp craters against a black sky"><br><b>Lunar surface</b><br><sub>4096×4096 · direct 16 MP generation</sub></td>
    <td align="center"><img src="site/assets/gallery/moka-pot-w4.jpg" width="480" alt="Moka pot blueprint with the exact title MOKA POT"><br><b>Moka pot blueprint</b><br><sub>1024×1024 · W4 · exact short title</sub></td>
  </tr>
</table>

## Why it exists

The H3 checkpoint is about 135 GB. The M5 Max benchmark machine has a recommended GPU
working set of 28.08 GiB. Onyx uses group-wise W4 quantization, weight streaming, and
chunked attention to run H3 within that budget.

## Key features

- **Native inference** on Apple Silicon with MPSGraph, Metal kernels, and streamed group-wise W4 weights.
- **Direct 16 MP generation** at 4096×4096 with tiled VAE decoding.
- **Replayable runs** with versioned Protobuf contracts, a RunRecord, and SHA-256 output verification.
- **Versioned model packages** with pinned source revisions, resumable downloads, and per-file SHA-256 checks.

## Benchmarks

H3 W4 teapot request, seed 42, six sampling steps, and the `max-quality` profile. Peak memory is sampled process-tree RSS.

| Hardware | Resolution | Wall time | Peak RSS | Record |
| --- | --- | ---: | ---: | --- |
| M5 Max, 36 GB | 1024×1024 | 19.58 s median (3 runs) | 1.71 GiB | [1024×1024 run data](benchmarks/results/campaign-20261123/against-main-1024.json) |
| M5 Max, 36 GB | 4096×4096 | 227.93 s (1 run) | 1.91 GiB | [4096×4096 run data](benchmarks/results/campaign-20261123/against-main-4096.json) |
| MacBook Air M4, 24 GB | 1024×1024 | 174.98 s median (3 runs) | 1.79 GiB | [v0.3.1, battery power](benchmarks/results/m4-air-24gb-dit-prefetch-v1.json) |

The M5 Max runs used a warm DiT modulation cache. The first request computes the tables. [Benchmark methodology and results](docs/OPTIMIZATION_CAMPAIGN.md)

## Quick start

The [first-image guide](docs/QUICKSTART.md) covers the native build, verified checkpoint download, W4 conversion, and a 1024×1024 run.

- **System** — Apple Silicon, macOS 26.2 or later, the Xcode Metal 4 toolchain, and `uv` with Python 3.12 or later.
- **Disk** — About **62 GB** of inference files, including the VAE, PDD heads, and tokenizer. Allow about **200 GB** for the original checkpoint and converted files, plus space for build tools.
- **Tested hardware** — 1024×1024 generation on M4 Air (24 GB) and M5 Max (36 GB). The minimum supported unified memory is unverified.

The default profile is `max-quality`. Choose `memory-min` to stream VAE weights, `m5-fast` to use the M5 neural accelerators with a different numerical path, or `speed-focus` to evaluate BF16 SIMD and DiT weight caching. [Execution profiles](docs/PROFILES.md)

Native generation caches DiT modulation tables by default in `~/Library/Caches/onyx-infer/modulation`. Use `--modulation-cache <directory>` to choose a location or `--no-modulation-cache` to disable it. [Native tuning guide](docs/NATIVE_TUNING.md)

[Onyx Studio](plugin/onyx-studio/README.md) adds local image generation, engine inspection, and an illustrated book reader to DeepSeek Harness. For lettering and annotations, see the [image text guide](docs/IMAGE_TEXT.md).

## Documentation

| Document | Contents |
| --- | --- |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Positioning, constraints from official specs, module boundaries |
| [docs/PROTOCOLS.md](docs/PROTOCOLS.md) | The six versioned protobuf contracts |
| [docs/LOOP.md](docs/LOOP.md) | Loop engineering and controlled RSI |
| [docs/V1_REVIEW.md](docs/V1_REVIEW.md) | v1 freeze review with acceptance evidence |
| [docs/PROFILES.md](docs/PROFILES.md) | Execution profiles and acceptance gates |
| [docs/ACCELERATION.md](docs/ACCELERATION.md) | Acceleration options and validation priorities |
| [docs/BENCHMARKS.md](docs/BENCHMARKS.md) | Aggregated benchmark capability report (generated) |
| [docs/VALIDATION.md](docs/VALIDATION.md) | Local and hardware validation |
| [docs/LORA_ADAPTERS.md](docs/LORA_ADAPTERS.md) | LoRA adapter notes |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contribution entry points |

Project site & engineering blog: **https://phantom5125.github.io/onyx-infer/**
(sources in [`site/`](site/), blog built by [`tools/build_blog.py`](tools/build_blog.py)).

## Guides

Guides we've published on the engineering blog, most recent first:

- [Nov 18 2026: Four rounds, one byte-identical teapot](site/blog/posts/four-rounds-one-byte-identical-teapot.md) — measurements from four early kernel and weight-loading experiments.
- [Nov 18 2026: Sixteen megapixels on 36 GB of unified memory](site/blog/posts/sixteen-megapixels-on-36gb.md) — how the engine manages memory for 4096×4096 direct generation.
- [Nov 18 2026: Why we're building an inference engine from scratch](site/blog/posts/why-native-from-scratch.md) — the 135 GB → 28.08 GiB math and the design principles that follow from it.

## License

Onyx Infer source code is available under the [MIT License](LICENSE). Vendored and derived MLX code retains its [Apple MLX license](ops/metal/mlx_root/LICENSE). H3 model files are obtained separately and governed by the [upstream MiniMax license](https://github.com/MiniMax-AI/MiniMax-H3-Image/blob/main/LICENSE).

## Cite

If you find onyx-infer useful in your research, cite it as:

```bibtex
@misc{onyx-infer,
  author = {Daocheng Ying},
  title = {onyx-infer: native image generation for Apple Silicon},
  year = {2026},
  publisher = {GitHub},
  url = {https://github.com/phantom5125/onyx-infer}
}
```
