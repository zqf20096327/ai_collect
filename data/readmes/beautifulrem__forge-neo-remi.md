<div align="center">

# Forge Neo Remi

**A zero-node, conflict-safe, studio-grade AI image creation workbench built on Stable Diffusion WebUI Forge Neo — Anima-first, multi-DiT, and Gradio-free (FastAPI + React 19 SPA).**

[English](README.md) | [简体中文](README.zh-CN.md)

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue.svg)](LICENSE)
[![Python 3.13](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Branch: remi](https://img.shields.io/badge/branch-remi-8A2BE2)](https://github.com/beautifulrem/forge-neo-remi/tree/remi)
[![Upstream: Forge Neo](https://img.shields.io/badge/upstream-Forge%20Neo-2ea44f)](https://github.com/Haoming02/sd-webui-forge-classic/tree/neo)

<img src="docs/images/readme/hero-en.webp" alt="The Generate view of Forge Neo Remi with a generated Forge Remi logo" width="100%">

</div>

Forge Neo Remi is a downstream distribution of [Forge Neo](https://github.com/Haoming02/sd-webui-forge-classic/tree/neo), itself built on [Stable Diffusion WebUI Forge](https://github.com/lllyasviel/stable-diffusion-webui-forge) and [AUTOMATIC1111 WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui). It is not a node-graph editor and not a new base model: Remi pairs Forge Neo's runtime and modern DiT model stack with a studio-grade, Gradio-free web workbench (FastAPI + SQLite queue + React 19 SPA), declarative capability-driven controls (`remi.ui` v1), non-node composable workflows, and deep Anima integration aimed at 8–24 GB consumer GPUs and Apple Silicon unified memory.

> [!IMPORTANT]
> This is an independent downstream branch, not an official release of Forge Neo or any bundled model family. Remi favors integrated, conflict-safe workflows over compatibility with every legacy extension: third-party extensions built for the old Gradio UI must be ported to `remi.ui` (see [Migrating from the Gradio UI](docs/remi-webui/usage.md#migrating-from-the-gradio-ui)).

## Why Remi?

- **Studio workbench & capability-driven Generate view.** A fast, Gradio-free React 19 SPA with refined light and dark themes, phone layouts, full keyboard control, and reload-free English / 简体中文 switching. `ModelCapability` automatically folds panels that do not apply to the loaded model family (with clear reasons), shows Model Bar quantization/capability badges (`Diffusers`, `GGUF`, `INT8-ConvRot`, `FP8`, `NVFP4`, `Turbo`, `RGBA`, `Control`), and surfaces actionable pre-submit **Workflow Advice** chips with one-click fixes.
- **Non-node composable workflows (Recipes & Linear Pipelines).** Save, share, and apply cross-model **Recipes** (conflict-checked parameter subsets) and run **Linear Multi-Stage Pipelines** (`Prompt Upsample → Generate → Refine → Finish`) with content-addressed upstream stage caching—change a downstream refine or upscale parameter and automatically reuse earlier outputs without wiring a node graph.
- **End-to-end creative loop.** Organize outputs with **Gallery Boards**, trace parent/child **Asset Lineage**, inspect two runs via pixel slider plus structured **Parameter Diff**, check alpha transparency with **Lightbox 4-backdrop** switching (`B`), **Send to Reference Image** with model-aware slot badges (`<image_1>`, `ref_image_0`, `ref_0`), iterate locally via **Canvas In-Place Staging**, expand prompts with the **Multimodal/Local Prompt Upsampler (PUP)**, and compose structured layouts in **JSON Builder** (MOSS-Image, FLUX.3 Layout, and Bria Fibo 2.0 VGL 2.0).
- **Anima-first inference & conflict-safe runtime.** Full 2B / 2.9B / 3.8B support (28/40/52-block layouts + native Qwen3.5 semantic connector), cross-depth LoRA and ControlNet-LLLite remapping, Control-LoRA / VACE, native samplers, guidance, spatial controls, and **Anima Remi Presets** safe baselines—with mutually exclusive stacks locked before sampling in both the browser and API ([details](docs/remi-webui/usage.md#anima-integration)).
- **Worker isolation, multi-GPU pools & Apple Silicon support.** Run in-process by default or opt into isolated inference via `WorkerProtocol`: `--worker-process` (crash/OOM auto-recovery and zero UI/WebSocket GIL contention), `--worker-gpus 0,1` (multi-GPU worker pool), and `--worker-mlx` (optional Apple Silicon MLX / `mflux` sidecar). These flags are a preview: they list the workers in the Workers monitor, but the queue does not dispatch to them and still runs every job in-process. Includes Apple Silicon MPS dequantized-weight caching, unified-memory awareness, and the reproducible `tools/perf/bench_inference.py` benchmark suite.
- **Stable Extension API v1 & upstream governance.** Versioned `remi.ui` (`REMI_API_VERSION = "1.0"`), optional `remi-extension.json` manifests, per-extension **Diagnostics** (load times, hook/action errors and timeouts), the public `remi.testing` contract verifier, and automated upstream divergence tracking (`tools/upstream_forks.py budget`, `FORKED <= 6`).
- **Batteries included.** Frequently used extensions ship as [built-ins](docs/remi-webui/usage.md#built-in-extensions), ported to `remi.ui` and guarded by automated Python, Vitest, and Playwright + axe gates.

## Screenshots

| | |
| --- | --- |
| <img src="docs/images/readme/themes-en.webp" alt="The Generate view, half in the light theme and half in the dark theme"> | <img src="docs/images/readme/anima-en.webp" alt="The Anima panels of the Generate view"> |
| Light and dark themes, three resizable panes | Anima Remi Presets and capability-gated panels |
| <img src="docs/images/readme/editor-en.webp" alt="The img2img image editor with an inpaint mask"> | <img src="docs/images/readme/gallery-en.webp" alt="The Gallery page"> |
| Image editor: masks, sketch layers, selections, in-place staging | Gallery: boards, lineage, search, stars, parameter diff compare |
| <img src="docs/images/readme/queue-en.webp" alt="The Queue page"> | <img src="docs/images/readme/phone-en.webp" alt="Three pages in the phone layout"> |
| Queue: live preview, priorities, linear pipelines & recipes | Phone layouts: Generate, Gallery and Queue |

The [usage guide](docs/remi-webui/usage.md#the-remi-webui) describes every page.

## Quick Start

You need [Git](https://git-scm.com/downloads), [Python 3.13](https://www.python.org/downloads/) or [uv](https://docs.astral.sh/uv/), a PyTorch device (an NVIDIA GPU is the most widely tested; Apple Silicon works through MPS) and [Node.js](https://nodejs.org/) 22.18+ or 24.11+ to build the web interface.

```bash
git clone --branch remi https://github.com/beautifulrem/forge-neo-remi.git forge-neo-remi
cd forge-neo-remi
```

Then run `./webui.sh` on Linux and macOS, or `webui-user.bat` on Windows.

The first launch installs Python dependencies, builds `webui/dist`, and prints `Running on local URL:  http://127.0.0.1:7860/`. Place checkpoints, VAEs, and text encoders in the matching `models/` subfolders, then pick them in the model bar. Optional worker modes (`--worker-process`, `--worker-gpus 0,1`, `--worker-mlx`) can be passed via `COMMANDLINE_ARGS` or `python launch.py`.

For a first Anima image, open **Anima Remi Presets** in Generate and apply **Official Base/Aesthetic — Safe (Recommended)**, or **Official Turbo — Fast (CFG 1 · 10 steps)** for an Anima-Turbo checkpoint.

The usage guide covers [detailed installation](docs/remi-webui/usage.md#quick-start) (`uv`, machines without Node.js, Docker), [launch options](docs/remi-webui/usage.md#launch-options), [where data is stored](docs/remi-webui/usage.md#where-data-is-stored), [keyboard shortcuts](docs/remi-webui/usage.md#keyboard-shortcuts), [security and remote access](docs/remi-webui/usage.md#security-and-remote-access), and [troubleshooting](docs/remi-webui/usage.md#troubleshooting).

## Supported Model Families

Remi retains Forge Neo's modern-model runtime while adding capability-driven tooling across Tier-1 and Tier-2 DiT families ([model & acceleration details](docs/remi-webui/usage.md#dit-families-controlnet-union--acceleration)):

- **Anima & Anima Edit:** 2B (28 blocks), 2.9B (40), and 3.8B (52, with native `qwen35_4b` semantic connector), cross-depth LoRA / ControlNet-LLLite remapping, Control-LoRA / VACE, and **Anima RGBA** ([details](docs/remi-webui/usage.md#anima-29b-and-38b-checkpoints); Anima RGBA requires its [LoRA and VAE](https://huggingface.co/localai0301/Anima-RGBA))
- **Qwen-Image, Qwen-Image-Edit & Qwen-Image-2.1:** Base and 8-step Turbo; Diffusers folders, Unsloth FP8 / INT8-ConvRot, and GGUF; lossless cross-step prefix KV cache, bidirectional fused/unfused MLP LoRA mapping, `Qwen-2.1 per-block` compile, Spectrum forecasting, native 4-channel RGBA generation/mask editing, and **`Qwen-Image-2.1-Fun-Controlnet-Union`** via unified `DiTControlPatch`
- **FLUX.3 Image Klein:** Base and step-distilled; multi-reference editing (`ref_image_{i}` slots); BFL / ComfyUI single files, Diffusers, FP8 / INT8, and GGUF; **Multimodal/Local PUP** and JSON Builder BBox layouts — plus **FLUX Kontext** and **FLUX.2 Klein**
- **Z-Image (Base / Turbo / Omni / Edit):** Diffusers/sharded loading, sensitive-layer quantization guards, cross-step text/RoPE caching, per-block compile, Spectrum seam, and **`Z-Image-Turbo-Fun-Controlnet-Union`**
- **MOSS-Image, MOSS-Image-Edit & Kromoss:** structured Layout prompts in JSON Builder and native **8-step DMD2 LoRA** workflow advice
- **Krea 2 & Krea 2 Identity Edit:** step-invariant conditioning/reference/RoPE caching, SLG hook, and Spectrum seam
- **ERNIE-Image (8B, Apache 2.0):** Diffusers/sharded loading, sensitive-layer quantization protection, and capability-driven defaults
- **Bria Fibo 2.0 (8.1B Dev & 4-step Edit Turbo):** structured **VGL 2.0 JSON** mode in JSON Builder and PUP (*note: Bria Fibo 2.0 weights are licensed under CC BY-NC 4.0 for non-commercial use only*)
- **Classic & video/utility families:** SD 1.x, SDXL variants, PiD 1.5, Mugen, Lumina Image 2, Chroma, and Wan 2.2 image/video workflows
- **Quantization & acceleration:** **GGUF** checkpoints and text encoders (Triton K-quant dequantization where available; GGUF-native layers stay quantized across reloads), **FP8** (including Anima scaled FP8), **INT8-ConvRot**, **NVFP4**, **SVDQuant**, per-block `torch.compile`, and **Spectrum** forecasting (**Chebyshev**, plus opt-in **TaylorSeer** and **MagCache** modes)

Use the upstream [model download guide](https://github.com/Haoming02/sd-webui-forge-classic/wiki/Download-Models) for checkpoint, VAE, and text-encoder directory layouts.

## Documentation

- [Usage guide](docs/remi-webui/usage.md): every page, Anima & DiT integration, installation, launch & worker options, data, shortcuts, migration from Gradio, built-in extensions, security, troubleshooting, compatibility notes
- [Remi Anima generation and parameter guide](docs/remi-anima-generation-guide.zh-CN.md) (zh-CN)
- [API guide (REST `/api/v2`, WebSocket, `/sdapi/v1`)](docs/remi-webui/api.md)
- [Extension developer guide (`remi.ui` v1, manifests, `remi.testing`)](docs/remi-webui/extension-guide.md)
- [Security](docs/remi-webui/security.md) and [Docker](docker/README.md)
- [WebUI architecture](docs/remi-webui/architecture.md) and [Anima feature seams](docs/remi-architecture-notes.md)
- [Absorbing Forge Neo updates](docs/remi-webui/upstream-absorption.md) and [Upstream PR roadmap & code-bloat audit](docs/remi-webui/upstream-pr-candidates.md)
- [Inference & memory benchmarks](docs/research/inference-performance.md) and [UI performance measurements](docs/research/ui-performance.md)
- [2026 Q4–2027 Q2 roadmap](docs/research/roadmap-2026-q4.zh-CN.md) (zh-CN), [competitive & architecture research](docs/research/competitive-and-architecture-research-2026-11.zh-CN.md) (zh-CN), and [Anima optimization research](docs/research/anima-generation-optimizations.md)
- [Documentation index](docs/remi-webui/README.md)
- [Forge Neo Wiki](https://github.com/Haoming02/sd-webui-forge-classic/wiki) · [Model downloads](https://github.com/Haoming02/sd-webui-forge-classic/wiki/Download-Models) · [Inference references](https://github.com/Haoming02/sd-webui-forge-classic/wiki/Inference-References)

## Issues and Contributions

Before opening an issue, reproduce it on the current `remi` branch with third-party extensions disabled. Include:

- Remi commit hash
- Operating system, browser, GPU/backend, Python and PyTorch versions
- Checkpoint family and quantization format
- Launch arguments (including any `--worker-*` flags) and relevant generation parameters
- Full console traceback, browser console output for UI issues, or a minimal reproduction

Use the [Remi issue tracker](https://github.com/beautifulrem/forge-neo-remi/issues) for Remi-specific behavior. Upstream-only issues should be reproduced against [Forge Neo](https://github.com/Haoming02/sd-webui-forge-classic/tree/neo) before being reported there.

Contributions should declare model behavior via `ModelCapability` / `remi.ui`, keep upstream-shared runtime diffs minimal (`python tools/upstream_forks.py budget` enforces `FORKED <= 6`), preserve upstream CRLF line endings (`tools/check_line_endings.py`), and add regression tests. `tools/check.sh` runs all Python, contract, i18n, bundle-budget, lint, Vitest, and Playwright + axe gates.

## Upstream and Acknowledgements

Remi builds on the work of [AUTOMATIC1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui), [lllyasviel](https://github.com/lllyasviel/stable-diffusion-webui-forge), [Haoming02](https://github.com/Haoming02/sd-webui-forge-classic), [ComfyUI](https://github.com/Comfy-Org/ComfyUI), and the authors of the bundled extensions and algorithms. Their original licenses and notices remain with their respective components; Settings → Licenses lists them, and links the web interface build's `THIRD-PARTY-NOTICES.txt` (every library it ships, with its license text; `webui/tools/notices.mjs`).

## License

The main project is licensed under the [GNU Affero General Public License v3.0](LICENSE). Bundled extensions, vendored components, and third-party model weights (such as Bria Fibo 2.0 under CC BY-NC 4.0) carry their own licenses; consult the `LICENSE` files and model cards before use.

The web interface offers its users the source code of the running server (AGPL-3.0 section 13): the sign-in screen, Settings → Licenses and Settings → Server and models link it. If you run a modified copy that others use over a network, publish your source and start the server with `--source-url` pointing at it. Details, and the origin and license of each built-in extension without a license file of its own: [docs/remi-webui/licensing.md](docs/remi-webui/licensing.md).
