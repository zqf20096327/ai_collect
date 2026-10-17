# Qwen-Image-2.1 on 8GB VRAM — ComfyUI + GGUF Setup

[English](README.md) | [简体中文](README_zh-CN.md) · [Quick start](#quick-start-windows--linux) · [Troubleshooting](#troubleshooting) · [Workflows](#workflows)

![Real Qwen-Image-2.1 output generated on RTX 2080 SUPER 8GB at 768×768](assets/rtx-2080-super-qwen-image-2.1-768x768.png)

*Actual RTX 2080 SUPER 8GB output · Q4 GGUF · 768×768 · 12 steps · 213.31 s end-to-end · 7623 MiB sampled peak whole-GPU memory (including desktop apps). [Benchmark details](#benchmark--proof-of-output).*

**Run Qwen-Image-2.1 locally on an 8GB NVIDIA GPU**, including RTX 2080 / 3060 8GB / 4060 8GB / 5060 8GB-class cards, using ComfyUI, quantized GGUF weights and CPU offloading.

This lightweight helper downloads the low-VRAM model stack, checks GPU/model paths, installs ready-to-import text-to-image and image-edit workflows, and launches ComfyUI with `--lowvram`.

**Trade-off:** this makes a constrained VRAM setup practical; it does **not** make inference fast or guarantee every 8GB GPU will work without tuning. Offloaded inference can take minutes per image depending on hardware, resolution and settings. See [8GB expectations](#8gb-expectations).

**Before you start:** you supply an existing ComfyUI installation; the script downloads model files from upstream, so allow substantial disk space and download time.

> Tested as a development profile on an **RTX 2080 SUPER 8GB** with Q4-class GGUF diffusion weights, the W4A8 Qwen3-VL text encoder, and the dedicated Qwen-Image-2.1 VAE.

## Why this repo exists

Qwen-Image-2.1 is unusually capable for a new open-weight image model, but the default files are still large enough to make an 8GB card look impossible at first glance. The trick is **quantization + CPU offload**, not pretending the whole stack fits in VRAM at once.

This repo turns that setup into three commands.

## Quick start (Windows / Linux)

You need:

- Windows or Linux
- NVIDIA GPU (8GB target profile)
- a recent **ComfyUI** checkout / portable install
- Git
- enough disk space for the model files (the downloads are much larger than 8GB in total)

### Windows

```powershell
git clone https://github.com/toyhank/qwen-image-2.1-8gb
cd qwen-image-2.1-8gb

.\install.ps1 -ComfyUI "D:\ComfyUI_windows_portable\ComfyUI"
```

### Linux

```bash
git clone https://github.com/toyhank/qwen-image-2.1-8gb
cd qwen-image-2.1-8gb

./install.sh /path/to/ComfyUI
```

The installer:

1. installs/updates the maintained `leejet/ComfyUI-GGUF` node;
2. downloads a Q4-class Qwen-Image-2.1 GGUF diffusion model;
3. downloads `qwen3vl_8b_w4a8.safetensors`;
4. downloads the **Qwen-Image-2.1-specific VAE**;
5. copies the bundled text-to-image and image-edit workflows into ComfyUI.

## Check before downloading

```bash
python qwen21.py doctor --comfy /path/to/ComfyUI
```

Example output:

```text
Qwen-Image-2.1 8GB doctor
=================================
GPU: NVIDIA GeForce RTX 2080 SUPER — 8.0 GiB VRAM
OK: ComfyUI-GGUF
OK: compatible GGUF found: qwen_image_2.1_Q4_K_M.gguf
OK: qwen3vl_8b_w4a8.safetensors
OK: qwen_image_2.1_vae_bf16.safetensors

Ready. Import one of the workflows/ JSON files in ComfyUI.
```

## Launch low-VRAM mode

```bash
python qwen21.py launch --comfy /path/to/ComfyUI
```

Anything after the command is passed to ComfyUI:

```bash
python qwen21.py launch --comfy /path/to/ComfyUI -- --listen 0.0.0.0
```

## What gets downloaded

| Component | File | Why |
|---|---|---|
| Diffusion model | `qwen_image_2.1-Q4_K.gguf` | Q4-class GGUF cuts GPU memory pressure |
| Text encoder | `qwen3vl_8b_w4a8.safetensors` | lower-memory Qwen3-VL encoder |
| VAE | `qwen_image_2.1_vae_bf16.safetensors` | required 2.1 VAE; old Qwen Image VAE is not interchangeable |
| Custom node | `leejet/ComfyUI-GGUF` | GGUF loader with Qwen-Image-2.1 support |

## Workflows

- `workflows/qwen-image-2.1-8gb-t2i.json` — text to image
- `workflows/qwen-image-2.1-8gb-edit.json` — image editing

Drag a JSON file into ComfyUI, or run:

```bash
python qwen21.py workflows --comfy /path/to/ComfyUI
```

## 8GB expectations

**8GB is a target VRAM profile, not a claim that all weights total 8GB.** ComfyUI may offload the text encoder / model blocks to system RAM. For a good experience, 32GB system RAM is a practical target.

Start with 1024×1024 and a single image. If you hit OOM:

- close browsers/games using VRAM;
- keep `--lowvram` enabled;
- reduce resolution;
- restart ComfyUI after changing models;
- avoid loading unrelated checkpoints at the same time.

## Troubleshooting

| Problem | What to try |
|---|---|
| `ComfyUI not found` | Pass the directory containing `main.py`, or its parent, to `--comfy`. |
| `MISSING` in `doctor` | Run the installer again; `doctor` checks for the GGUF node and three model files, not whether inference will succeed. |
| CUDA out of memory (OOM) | Close other GPU applications, lower resolution, keep `--lowvram`, and restart ComfyUI. |
| Workflow has missing nodes | Update ComfyUI and check that `custom_nodes/ComfyUI-GGUF` is installed; restart ComfyUI after installing nodes. |
| Download is interrupted | Re-run installation: downloads use `.part` files for resuming where supported. |
| Image generation is very slow | CPU offloading trades speed for memory; check available system RAM and avoid competing workloads. |

### Benchmark / proof of output

A **real text-to-image inference succeeded** on an RTX 2080 SUPER with 8192 MiB VRAM, using ComfyUI's HTTP API and the repository's `tools/benchmark_once.py` script.

| GPU | Model | Resolution / steps | Total task time | Peak GPU memory | Result |
|---|---|---|---|---|---|
| RTX 2080 SUPER 8GB | `qwen_image_2.1_Q4_K_M.gguf` | 768×768 / 12 | **213.31 s** | **7623 MiB** | Success |

- Sampler: `euler`, scheduler: `simple`, CFG: `1.0`, seed: `42`.
- Idle baseline: **2665 MiB**. Peak was sampled using `nvidia-smi` approximately every second; it represents **whole-GPU memory allocation**, including desktop processes, not model-only memory. Actual instantaneous peak may be higher than sampled.
- The elapsed time is measured from API queue submission through completed output, not pure sampler time.
- ComfyUI wrote `Qwen_8GB_benchmark_00001_.png` to its local output folder; the actual output is included above as [`assets/rtx-2080-super-qwen-image-2.1-768x768.png`](assets/rtx-2080-super-qwen-image-2.1-768x768.png).
- This is one measured 768×768 / 12-step run, **not** a speed estimate for 1024×1024 / 25 steps or other GPUs.

To create a reproducible benchmark:

1. Close unrelated GPU applications and note the ComfyUI version and model filename.
2. Record GPU VRAM with `nvidia-smi --query-gpu=timestamp,memory.used --format=csv -l 1` during generation (monitoring total GPU allocation, not necessarily model-only usage).
3. Start a single text-to-image job; measure wall-clock time from queue submission to completion, and save the resulting PNG.
4. Report resolution, step count, seed, system RAM, elapsed time and the **maximum measured** GPU memory value; upload the PNG under a repository `assets/` directory.
5. Replace the pending row with actual measurements and link the committed PNG.

If you benchmark this setup, share the details in an [issue](https://github.com/toyhank/qwen-image-2.1-8gb/issues).

## Why Qwen-Image-2.1 is worth trying

The upstream model unifies text-to-image and editing, supports multiple reference images, improves text rendering, and adds native transparency. This repo only handles the local low-VRAM plumbing; **Qwen-Image-2.1 itself belongs to the Qwen team**.

## Upstream / credits

- Qwen-Image-2.1: https://github.com/QwenLM/Qwen-Image-2.1
- ComfyUI model files: https://huggingface.co/Comfy-Org/Qwen-Image-2.1
- GGUF weights: https://huggingface.co/leejet/Qwen-Image-2.1-GGUF
- ComfyUI-GGUF: https://github.com/leejet/ComfyUI-GGUF

## License

The helper code in this repository is MIT licensed. **Model weights are not redistributed** and remain under their upstream licenses. Review the Qwen / model repository license terms before use.

---

If this saved you an evening of CUDA / VRAM debugging, a ⭐ helps other 8GB GPU owners find it.
