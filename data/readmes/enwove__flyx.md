<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/brand/flyx-readme-banner-dark.svg">
    <img alt="FLYX: fast, lightweight local inference." src="docs/brand/flyx-readme-banner.svg" width="100%">
  </picture>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-2d6a4f" alt="Apache-2.0 License"></a>
  <img src="https://img.shields.io/badge/platform-Windows%20%7C%20Linux-555" alt="Windows and Linux">
  <a href="https://discord.gg/ZtUPXBxYhN"><img src="https://img.shields.io/badge/Discord-Join-5865F2?logo=discord&logoColor=white" alt="Join FLYX Discord"></a>
  <a href="https://enwove.ai/flyx/wechatqr"><img src="https://img.shields.io/badge/WeChat-Join%20Group-07C160?logo=wechat&logoColor=white" alt="WeChat Group QR"></a>
</p>

<p align="center">
  <b>English</b> ·
  <a href="docs/i18n/README_zh.md">中文</a> ·
  <a href="docs/i18n/README_ja.md">日本語</a> ·
  <a href="docs/i18n/README_ko.md">한국어</a> ·
  <a href="docs/i18n/README_es.md">Español</a> ·
  <a href="docs/i18n/README_fr.md">Français</a> ·
  <a href="docs/i18n/README_de.md">Deutsch</a>
</p>

---

<p align="center">
  <a href="#quick-start">Quick Start</a> ·
  <a href="#performance">Performance</a> ·
  <a href="docs/models.md">Models</a> ·
  <a href="docs/server.md">CLI &amp; API</a> ·
  <a href="llms.txt">llms.txt</a>
</p>

**FLYX** is a zero-dependency local LLM engine in a ~50 MB binary — native long context, tuned per GPU, no setup required. Run GGUF models as they are and serve them to your browser, scripts, and coding agents over OpenAI- and Anthropic-compatible APIs.

<p align="center">
  <img src="docs/media/dashboard-light.png" width="900" alt="FLYX built-in web dashboard showing live throughput, long-context sessions, VRAM and RAM usage, and recent agent requests">
  <br><sub>Built-in web dashboard: model management, chat, live throughput, memory breakdown, and one-click agent setup.</sub>
</p>

## Key Features

- **Native long context, no quality loss** — Gives every model its full trained context on a single consumer GPU. When K/V cache outgrows VRAM, it spills cleanly into system RAM instead of truncating or sliding-windowing: **123 tok/s at 256K on a 24 GB RTX 4090**, **165 tok/s at 256K on an RTX 5090** (`NVFP4`), and **100% long-context retrieval across 32K–256K** ([details](docs/benchmarks.md#1-qwen38-27b-long-context-coding-benchmark)).
- **Tuned per GPU, zero manual flags** — Ships measured kernel tuning tables for 11 NVIDIA GPUs and automatically sizes context length, K/V precision, and GPU/RAM placement from available memory. No guessing offload counts, batch sizes, or cache types.
- **No install, no dependencies, ~50 MB** — CUDA and C++ runtimes are linked in; only the NVIDIA driver (≥ 580) is required. No CUDA Toolkit, Python, or Docker. Single ~50 MB `.exe` on Windows (double-click to run), ~45 MB tarball on Linux.
- **Built-in web dashboard & terminal monitor** — Starts straight into a browser UI (7 languages) with guided next-step hints to search/download Hugging Face or local models, chat, read localized API docs, and watch live throughput, VRAM/RAM split, sessions, requests, and logs ([monitor guide](docs/monitor.md)).
- **One-click coding agent integration** — Speaks OpenAI (Chat Completions, Responses) and Anthropic Messages with tool calls and multi-turn prompt reuse. Launch **Claude Code** or **Codex CLI** straight into your project folder from **Integration** (Windows), or copy ready-to-run commands for **DeepSeek Harness, OpenCode, and Pi**.
- **Verified accuracy** — Every GPU kernel is tested against a `float64` reference; default FP8 K/V stays within **KL 0.0009–0.0016** of 16-bit on 27B; every speed optimization preserves **token-for-token identical** output ([numerics](docs/design/numerics.md)).

## Updates

- **`2026-11`** — **Initial open-source release of FLYX**: standalone ~50 MB zero-dependency Windows `.exe` & Linux tarball, native full-context GGUF & NVFP4 inference with automatic GPU/RAM K/V extension, built-in speculative decoding (MTP / DFlash2), 7-language web dashboard, and one-click Claude Code / Codex CLI integration.

## Performance

Greedy coding benchmark on **Qwen3.8-27B GGUF** with built-in **MTP** speculative decoding (`--drafter mtp --ctx max --chat --no-think -n 512 --ignore-eos`), measuring 512-token code generation at **1K**, **128K**, and **256K** context (`NVFP4` on RTX 5090, `UD-Q4_K_XL` on 24 GB GPUs, `UD-IQ3_XXS` on 16 GB GPUs; exact prefill times, automatic 262K memory placement, `flyx bench` drafter tables, and reproducible commands in [docs/benchmarks.md](docs/benchmarks.md)):

| GPU | Model | 1K decode | 128K decode | 256K decode | 256K retrieval |
|---|---|---:|---:|---:|:---:|
| **RTX 5090** (32 GB) | `NVFP4` | **350.2 tok/s** | **228.7 tok/s** | **164.5 tok/s** | **100%** (4/4 multi-needle) |
| **RTX 5080** (16 GB) | `UD-IQ3_XXS` | **225.9 tok/s** | **161.0 tok/s** | **105.8 tok/s** | **100%** (5/5 depth grid) |
| **RTX 5070 Ti** (16 GB, WSL2) | `UD-IQ3_XXS` | **167.4 tok/s** | **104.6 tok/s** | **61.2 tok/s** | **100%** (5/5 + 4/4 multi) |
| **RTX 4090** (24 GB) | `UD-Q4_K_XL` | **193.6 tok/s** | **155.9 tok/s** | **122.7 tok/s** | **100%** (20/20 + 4/4 multi) |
| **RTX 4080** (16 GB) | `UD-IQ3_XXS` | **172.3 tok/s** | **111.0 tok/s** | **99.0 tok/s** | **100%** (3/3 @ 1K–256K) |
| **RTX 3090** (24 GB, 300 W) | `UD-Q4_K_XL` | **135.8 tok/s** | **97.5 tok/s** | **68.1 tok/s** | **100%** (3/3 @ 1K–256K) |

<sub>**RTX 5090 + DFlash2 (`NVFP4`, `--drafter all`):** **365.0 tok/s** (1K) and **273.1 tok/s** (128K, `30.1 s` prefill); `flyx bench` mixed prompts reach **311.6 tok/s** (`DFlash2`). **Long-context retrieval (Needle-in-a-Haystack):** **51/51 (100%)** exact recall across all 6 GPUs (32K–256K `5%–95%` depth grids and 256K 4-needle retrieval, covering both full-GPU FP8 and Host-RAM + 2-bit StrataFlux; [full grid](docs/benchmarks.md#3-long-context-attention-fidelity-needle-in-a-haystack-suite)).</sub>

## Quick Start

### 1. Download and run (recommended)

Grab the latest release from [GitHub Releases](https://github.com/enwove/flyx/releases) — requires only an NVIDIA driver (≥ 580):

- **Windows:** Double-click `flyx-*-windows-x86_64-cuda13.exe` (or run `.\flyx.exe serve` in PowerShell). The server starts and opens the dashboard automatically (picking another free port if `8080` is busy).
- **Linux / WSL2:** Extract the tarball and run:

```sh
./bin/flyx serve
# Or load a Hugging Face GGUF directly into the standard HF cache:
./bin/flyx serve unsloth/Qwen3.8-27B-GGUF:UD-Q4_K_XL
```

Open the dashboard at `http://127.0.0.1:8080` → pick or download a model in **Model** → launch **Claude Code / Codex** directly (or copy any agent command) from **Integration**.

| Client / Endpoint | Base URL |
|---|---|
| OpenAI SDKs (Chat Completions, Responses, Completions) | `http://127.0.0.1:8080/v1` |
| Anthropic SDKs & Claude Code (`ANTHROPIC_BASE_URL`) | `http://127.0.0.1:8080` |
| Web Dashboard | `http://127.0.0.1:8080/` |
| Telemetry JSON (`flyx monitor`) | `http://127.0.0.1:8080/v1/telemetry` |

<details>
<summary><b>Build from source</b> (CUDA 13, CMake 3.24+, Ninja, g++ 11+ / MSVC 2022)</summary>

```sh
cmake --preset dev && cmake --build --preset dev    # outputs in ~/flyx-build/bin

# Run or serve directly by Hugging Face name
~/flyx-build/bin/flyx run unsloth/Qwen3.8-27B-GGUF:UD-Q4_K_XL --chat -p "Write a haiku about GPUs."
~/flyx-build/bin/flyx serve unsloth/Qwen3.8-27B-GGUF:UD-Q4_K_XL --port 8080
```

> **WSL2 note:** Keep build trees and model files on the Linux filesystem (`~/models`, `~/flyx-build`); `/mnt/<drive>` degrades model load times severely.

</details>

<details>
<summary><b>Python usage &amp; curl example</b></summary>

```sh
curl http://127.0.0.1:8080/v1/chat/completions -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "Hello!"}]}'
```

```python
import flyx

eng = flyx.Engine("~/models/Qwen3.8-27B-UD-Q4_K_XL.gguf", lib="~/flyx-build/bin/libflyx.so")
reply = eng.session().chat_full(
    [{"role": "user", "content": "Name the capital of France."}],
    enable_thinking=False,
    max_new_tokens=64,
)
print(reply["content"])
```

</details>

## Supported Models & Hardware

| Dimension | Supported | Notes |
|---|---|---|
| Architectures | Qwen3.5 / Qwen3.8 (hybrid GDN + gated attention), Qwen3 dense, Llama (MiniCPM5-1B) | Dense text only (no MoE, no vision); Llama from `.flyx` only |
| Model formats | GGUF (`F32`, `F16`, `BF16`, `Q4_0–Q8_0`, `Q2_K–Q6_K`, `IQ1–IQ4`, GGML NVFP4); `.flyx` (BF16, NVFP4; format 2 with the target's own LoRA adapters, V-LoRA, run unmerged; a DV drafter, drafting only when named: `--drafter dv`, [design](docs/design/dv.md)) | MXFP4 refused; split GGUFs need all parts in one folder |
| GPUs | RTX 30 / 40 / 50 series, L4, L40S, A100, H100 (`sm_80`–`sm_120`; `sm_100` in Linux release) | Single GPU per process (`CUDA_VISIBLE_DEVICES`); driver ≥ 580 |
| Platforms | Windows (native MSVC), Linux, WSL2 | Single-file `.exe` / ZIP / wheel on Windows; tarball / `manylinux` wheel on Linux |

## Documentation

For AI agents, start with [llms.txt](llms.txt).

- **Use & Integrate:** [docs/server.md](docs/server.md) · [docs/models.md](docs/models.md) · [docs/monitor.md](docs/monitor.md) · [docs/benchmarks.md](docs/benchmarks.md)
- **Build & Test:** [docs/building.md](docs/building.md) · [docs/testing.md](docs/testing.md)
- **Design & Contracts:** [docs/design/architecture.md](docs/design/architecture.md) · [docs/design/numerics.md](docs/design/numerics.md) · [docs/design/gguf.md](docs/design/gguf.md) · [docs/design/tree-verification.md](docs/design/tree-verification.md) · [docs/design/dv.md](docs/design/dv.md)
- **Contribute & Governance:** [AGENTS.md](AGENTS.md) · [CONTRIBUTING.md](CONTRIBUTING.md) · [SECURITY.md](SECURITY.md) · [docs/prior-art.md](docs/prior-art.md)

## Contact Us

- **Discord:** [Join the FLYX Discord](https://discord.gg/ZtUPXBxYhN)
- **WeChat:** [Scan the WeChat group QR code](https://enwove.ai/flyx/wechatqr)
- **Issues & Feedback:** [GitHub Issues](https://github.com/enwove/flyx/issues)

For collaborations and partnerships, please contact us at [contact@enwove.ai](mailto:contact@enwove.ai).

## License

Apache-2.0. Third-party attributions are listed in [NOTICE](NOTICE) and [docs/prior-art.md](docs/prior-art.md).
