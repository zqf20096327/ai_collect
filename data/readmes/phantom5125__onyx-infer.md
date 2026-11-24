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

[Generate your first image](docs/QUICKSTART.md) · [Measured performance](#measured-results-m5-max-36-gb-mac1714) · [Onyx Studio](plugin/onyx-studio/README.md)

The six-step 4096×4096 teapot benchmark took 329.6 s on the 36 GB M5 Max. The 1024×1024 benchmark took a median 175 s on a 24 GB M4 MacBook Air on battery. [M5 Max benchmark](benchmarks/results/native-v1-stability.json) · [M4 Air benchmark](benchmarks/results/m4-air-24gb-dit-prefetch-v1.json)

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

The checkpoint is ~135 GB. The machine grants a 28.08 GiB working set. That gap dictates
everything: group-wise W4 weights, phase residency, block streaming, chunked attention —
and an engine that plans memory explicitly instead of hoping unified memory sorts it out.

## Optimization leaderboard

Each row uses the same 1024×1024 teapot request on the M5 Max with 36 GB of unified memory
(seed 42, six sampling steps). All candidates matched the baseline PNG byte for byte.
The benchmark records include sample counts, output hashes, and the source revision.

| Configuration | Median wall time | Peak memory | Speed vs. baseline | Evidence |
| --- | ---: | ---: | ---: | --- |
| Native streaming baseline | 42.30 s | 3.19 GiB | 1.00× | [Baseline measurements](benchmarks/results/native-round1-zero-cache.json) |
| Grouped Q4 zero-point cache | 42.63 s | 3.18 GiB | 0.99× | [Measurement](benchmarks/results/native-round1-zero-cache.json) |
| Direct reads into Metal buffers | 38.74 s | 1.70 GiB | 1.09× | [Measurement](benchmarks/results/native-round2-direct-pread.json) |
| Shared-memory BF16 modulation packing | 37.50 s | 1.70 GiB | 1.13× | [Measurement](benchmarks/results/native-round3-cpu-modulation.json) |
| Fused DiT attention and tensor views | 34.65 s | 1.86 GiB | 1.22× | [Measurement](benchmarks/results/native-round4-fused-attention-views.json) |
| Streaming DiT prefetch (default) | **32.81 s** | 1.79 GiB | **1.29×** | [Measurement](benchmarks/results/m5-max-36gb-dit-prefetch-default-v1.json) |

The [teapot benchmark write-up](site/blog/posts/four-rounds-one-byte-identical-teapot.md)
explains each change, including the zero-point cache regression.

## Key features

- **Full-native pipeline, zero runtime reuse** — MPSGraph + hand-written MSL kernels over our
  own packed Q4 weights; staged, streaming execution with VAE tiling.
- **16 MP direct generation** — 4096×4096 straight from the DiT (one token = 32×32 px),
  no upscaler. The teapot benchmark run took 329.6 s with a sampled process-tree peak
  RSS of 2.14 GB.
- **Replayable v1 protocols** — six versioned protobuf contracts (`onyx.common/job/model/plan/trace/loop.v1`);
  a RunRecord for every run; outputs verified by SHA-256 and reproduced by replay.
- **Evidence-first optimization loop** — the leaderboard above is not a narrative; each round
  is backed by measurement JSON, correctness gates, and an output-hash proof.
- **Three execution profiles for W4** — `max-quality` uses the default MPSGraph path,
  `memory-min` streams weights at every stage, and `speed-focus` tests BF16 SIMD and weight
  caching. The profile registry records the settings and validation criteria.
- **Versioned, immutable model packages** — ModelScope revisions pinned, per-file SHA-256,
  resumable multi-part downloads, streaming group-wise W4 packing.

## Measured results (M5 Max 36 GB, Mac17,14)

Headline numbers on the benchmark machine; the optimization history lives in the
leaderboard above. We publish the gaps next to the wins.

| Measurement | Value | Source |
| --- | --- | --- |
| 1024×1024 native generation | 32.81 s median (text 5.25 / DiT 22.95 / VAE 4.65), 1.79 GiB peak | `m5-max-36gb-dit-prefetch-default-v1.json` |
| 4096×4096 teapot benchmark run | 329.61 s, sampled process-tree peak RSS 2.14 GB, replay verified | [native-v1-stability.json](benchmarks/results/native-v1-stability.json) |
| Numerical fidelity | text-tower corr 0.9999987; VAE pixel corr 0.999993 | `native-baseline-v1.json` |
| Q4 GEMM vs MLX (published gap) | 28.12 ms vs 1.71 ms median on 1024×5376×5376 — 16.5× | `m5-max-36gb-q4-operator-v1.json` |
| Native vs community W8A8 (published gap) | 38.74 s vs 23.61 s on the same request — 1.64× | `native-v1-stability.json` |

Both the wins and the gaps live in `benchmarks/results/` as committed JSON.

## Quick start

The [first-image guide](docs/QUICKSTART.md) covers the native build, verified checkpoint download, W4 conversion, and a 1024×1024 run.

- **System** — Apple Silicon, macOS 26.2 or later, the Xcode Metal 4 toolchain, and `uv` with Python 3.12 or later.
- **Disk** — About **62 GB** of inference files, including the VAE, PDD heads, and tokenizer. Allow about **200 GB** for the original checkpoint and converted files, plus space for build tools.
- **Tested hardware** — 1024×1024 generation on M4 Air (24 GB) and M5 Max (36 GB). The minimum supported unified memory is unverified.

Use `memory-min` for all-streaming weights or `speed-focus` to try the BF16 SIMD kernel and DiT weight cache. The measured H3 W4 pipeline is fastest with the default MPSGraph path. See [the optimization campaign](docs/OPTIMIZATION_CAMPAIGN.md).

[Onyx Studio](plugin/onyx-studio/README.md) adds local image generation, engine inspection, and an illustrated book reader to DeepSeek Harness.

For repeated native generation, pass `--modulation-cache <directory>` to reuse the six-step DiT modulation tables across prompts, seeds, and image sizes. The first request builds the tables. Later requests can reuse them, and the DiT stage reports the cache status.

For 1024×1024 requests on the 36 GiB benchmark machine, `--dit-cache-mib 10240` speeds up the default MPSGraph path by keeping repeatedly read weights in memory. Native output reports the applied budget. At 16 MP, the same budget increased system swap. [Tuning and verification](docs/NATIVE_TUNING.md)

Use `onyx label-prompt` to describe lettering for H3 or `onyx compose-labels` to place exact text and leader lines after generation. [Image text workflows](docs/IMAGE_TEXT.md)

Cross-profile stage matrices, gate checks, and the aggregated capability report:

```bash
uv run python benchmarks/run_profiles.py --sizes 1024x1024,4096x4096 --runs 3 --output artifacts/benchmarks/profile-stage-matrix.json
uv run python tools/check_profile_gates.py artifacts/benchmarks/profile-stage-matrix.json
uv run python tools/build_benchmark_report.py
```

The MLX reference environment is separate: `uv sync --extra reference`.

## Documentation

| Document | Contents |
| --- | --- |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Positioning, constraints from official specs, module boundaries |
| [docs/PROTOCOLS.md](docs/PROTOCOLS.md) | The six versioned protobuf contracts |
| [docs/LOOP.md](docs/LOOP.md) | Loop engineering and controlled RSI |
| [docs/V1_REVIEW.md](docs/V1_REVIEW.md) | v1 freeze review with acceptance evidence |
| [docs/PROFILES.md](docs/PROFILES.md) | The three execution profiles and their acceptance gates |
| [docs/ACCELERATION.md](docs/ACCELERATION.md) | Acceleration roadmap: Mac feature levers, transferable infra-team advice, priority queue |
| [docs/BENCHMARKS.md](docs/BENCHMARKS.md) | Aggregated benchmark capability report (generated) |
| [docs/VALIDATION.md](docs/VALIDATION.md) | Local and hardware validation |
| [docs/LORA_ADAPTERS.md](docs/LORA_ADAPTERS.md) | LoRA adapter notes |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contribution entry points |

Project site & engineering blog: **https://phantom5125.github.io/onyx-infer/**
(sources in [`site/`](site/), blog built by [`tools/build_blog.py`](tools/build_blog.py)).

## Guides

Guides we've published on the engineering blog, most recent first:

- [Nov 18 2026: Four rounds, one byte-identical teapot](site/blog/posts/four-rounds-one-byte-identical-teapot.md) — the full story behind the leaderboard above, including the round that regressed.
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
