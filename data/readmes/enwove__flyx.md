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

**FLYX** is a zero-dependency local LLM engine that fits in a single ~57 MB Windows `.exe` — fast speculative decoding, native long context, tuned per GPU, no setup required. Run supported GGUF models as they are and serve them to your browser, scripts, and coding agents over OpenAI- and Anthropic-compatible APIs.

<p align="center">
  <img src="docs/media/dashboard-light.png" width="900" alt="FLYX built-in web dashboard showing live throughput, long-context sessions, VRAM and RAM usage, and recent agent requests">
  <br><sub>Built-in web dashboard: model management, chat, live throughput, memory breakdown, and one-click agent setup.</sub>
</p>

## Key Features

- **Up to 6× faster generation** — Built-in speculative decoding (MTP, DFlash2, DSpark, and prompt lookup): **565.5 tok/s** on Qwen3.8-27B and **438.9 tok/s** on Inkling-2-Mini on an RTX 5090 ([Performance](#performance)).
- **Up to 1M native context on a consumer PC** — Runs Inkling-2-Mini at 1M context on 16 GB VRAM + 32 GB RAM.
- **Tuned per GPU, zero manual flags** — Ships measured kernel tuning tables for 16 NVIDIA GPUs and automatically sizes context length, K/V precision, and GPU/RAM placement from available memory. No guessing offload counts, batch sizes, or cache types.
- **No install, no dependencies, ~57 MB** — CUDA and C++ runtimes are linked in; only the NVIDIA driver (≥ 580) is required. No CUDA Toolkit, Python, or Docker. Single ~57 MB `.exe` on Windows (double-click to run), or a tarball on Linux.
- **Built-in web dashboard & terminal monitor** — Starts straight into a browser UI (7 languages) with guided next-step hints to search/download Hugging Face or local models, chat (text & images), read localized API docs, and watch live throughput, VRAM/RAM split, sessions, requests, and logs ([monitor guide](docs/monitor.md)).
- **One-click coding agent integration** — Speaks OpenAI (Chat Completions, Responses) and Anthropic Messages with tool calls and multi-turn prompt reuse. Launch **Claude Code** or **Codex CLI** straight into your project folder from **Integration** (Windows), or copy ready-to-run commands for **DeepSeek Harness, OpenCode, and Pi**.
- **Verified accuracy** — Every GPU kernel is tested against a `float64` reference; default FP8 K/V stays within **KL 0.0009–0.0016** of 16-bit on 27B; speculative decoding is **token-for-token identical** to plain decoding ([numerics](docs/design/numerics.md)).

## Updates

- **`v0.2.1`** — **Speeds verified on four GPUs, Inkling-2-Mini with DSpark, and image input**:
  - **Qwen3.8-27B + DFlash2** writes code at **565.5 tok/s** on an RTX 5090 (**6.03×** plain decoding), **305.7** on an RTX 4090, **332.8** on a 16 GB RTX 5070 Ti, and **234.1** on an RTX 3090. `NVFP4` W4A4 prefill on the 5090 runs at **15,496 tok/s**.
  - **Inkling-2-Mini + DSpark** — a new sparse-MoE model, with DSpark attached automatically: **438.9 tok/s** on code on the 5090 (**1.92×** plain decoding), **322.4** on the 4090, **276.2** on the 5070 Ti, and **222.0** on the 3090.
  - **Vision** — image input from the CLI, the OpenAI and Anthropic APIs, and dashboard paste / drop, for vision-capable models with an `mmproj` projector.
  - **Still zero dependencies** — one Windows `.exe`, now ~57 MB.
- **`v0.2.0`** — **Initial open-source release of FLYX**: standalone ~59 MB zero-dependency Windows `.exe` & Linux tarball, native full-context GGUF & NVFP4 inference with automatic GPU/RAM K/V extension, built-in speculative decoding (MTP / DFlash2), 7-language web dashboard, and one-click Claude Code / Codex CLI integration.

## Performance

v0.2.1 decode speed in tokens/s, verified on four GPUs (greedy). **Plain** is decoding with no drafter; the two **Speculative** columns turn the drafter on for chat and for code prompts, with the speedup over plain in parentheses.

**Qwen3.8-27B + DFlash2** — chat / mixed: 3 prompts × 128 tokens; code: 1 prompt × 128 tokens.

| GPU | Quant | Plain | Speculative · chat / mixed | Speculative · code |
|---|---|---:|---:|---:|
| **RTX 5090** (32 GB) | `NVFP4` | 93.8 | **315.5** (3.36×) | **565.5** (6.03×) |
| **RTX 4090** (24 GB) | `UD-Q4_K_XL` | 49.4 | **171.6** (3.47×) | **305.7** (6.18×) |
| **RTX 3090** (24 GB) | `UD-Q4_K_XL` | 42.8 | **131.2** (3.06×) | **234.1** (5.46×) |
| **RTX 5070 Ti** (16 GB) | `UD-IQ3_XXS` | 68.8 | **154.4** (2.24×) | **332.8** (4.84×) |

**Inkling-2-Mini + DSpark** — chat / mixed: 8 prompts × 128 tokens; code: 8 prompts × 384 tokens.

| GPU | Quant | Plain | Speculative · chat / mixed | Speculative · code |
|---|---|---:|---:|---:|
| **RTX 5090** (32 GB) | `UD-IQ3_XXS` | 225.5 | **259.8** (1.15×) | **438.9** (1.92×) |
| **RTX 4090** (24 GB) | `UD-IQ3_XXS` | 166.7 | **202.9** (1.22×) | **322.4** (1.92×) |
| **RTX 3090** (24 GB) | `UD-IQ3_XXS` | 126.2 | **136.5** (1.08×) | **222.0** (1.75×) |
| **RTX 5070 Ti** (16 GB) | `UD-IQ3_XXS` | 150.9 | **169.3** (1.12×) | **276.2** (1.80×) |

<sub>**×** is the speedup over plain decoding on the same prompts, from unrounded rates; **Plain** shows the chat / mixed run. Speculative output matched plain decoding token for token in every run that recorded token IDs (all but the Windows Qwen mixed run). Linux, except the RTX 5070 Ti on native Windows 11.</sub>

<sub>**Also measured:** Qwen3.8-27B's built-in **MTP** drafter (no extra file) reaches **286.6 / 158.0 / 121.7 / 167.2 tok/s** on the mixed prompts (5090 / 4090 / 3090 / 5070 Ti). **RTX 5090 `NVFP4`:** W4A4 prefill at **15,496 tok/s**; **203.8 tok/s** with MTP at 128K context (plain: 73.4); **164.5 tok/s** at 256K with **100%** needle retrieval (v0.2.0 run). Hardware, drivers, and exact commands: [docs/benchmarks.md](docs/benchmarks.md#v021-four-gpu-verified-benchmarks).</sub>

## Quick Start

### 1. Download and run (recommended)

Grab the latest release from [GitHub Releases](https://github.com/enwove/flyx/releases) — requires only an NVIDIA driver (≥ 580):

- **Windows:** Double-click `flyx-0.2.1-windows-x86_64-cuda13.exe` (or run `.\flyx-0.2.1-windows-x86_64-cuda13.exe serve` in PowerShell). The server starts and opens the dashboard automatically (picking another free port if `8080` is busy).
- **Linux / WSL2:** Extract the tarball and run:

```sh
./bin/flyx serve
# Or load a Hugging Face GGUF directly into the standard HF cache:
./bin/flyx serve unsloth/Qwen3.8-27B-GGUF:UD-Q4_K_XL
```

Two more to try — the DSpark drafter and the vision projector download with the model:

```sh
# Inkling-2-Mini, with DSpark attached automatically
flyx serve unsloth/Inkling-2-Mini-GGUF:UD-IQ3_XXS
# Ask about an image
flyx run unsloth/Qwen3.8-27B-GGUF:UD-Q4_K_XL --image photo.png --chat -p "Describe the image."
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
| Architectures | Qwen3.5 / Qwen3.8 (`qwen35`), Qwen3 (`qwen3`), Inkling-2-Mini (`inkling2_loop`, sparse MoE), Llama (MiniCPM5-1B) | Llama from `.flyx` only |
| Speculative drafters | MTP, DFlash2, DSpark, prompt lookup | MTP and DSpark attach automatically; DFlash2 is a companion file (`--drafter-file`, or **Draft with it** in the dashboard); DSpark pairs with Inkling-2-Mini |
| Vision | Image input with an `mmproj` projector, fetched automatically from the model's Hub repo | Qwen3.5 / Qwen3.8 today; Inkling-2-Mini is text-only |
| Model formats | GGUF (`F32`, `F16`, `BF16`, `Q2_0`, `Q4_0–Q8_0`, `Q2_K–Q6_K`, `IQ1–IQ4`, `MXFP4`, GGML `NVFP4`); `.flyx` (BF16, NVFP4; format 2 with the target's own LoRA adapters, V-LoRA, run unmerged; a DV drafter, drafting only when named: `--drafter dv`, [design](docs/design/dv.md)) | Keep all split GGUF parts in the same folder. |
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
