# ComfyUI-QwenImage21-PixelHead

Direct RGBA pixel readout head (`v0.3` Haar Wavelet High-Fidelity & `v0.1` Fast `1x` / `2x`) for **Qwen-Image 2.1** in ComfyUI, replacing the `644.2 MiB` 64-channel WanVAE decoder at the end of sampling.

[English](README.md) | [简体中文](README_zh.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-pocis%2FQwen--Image--2.1--PixelHead-yellow)](https://huggingface.co/pocis/Qwen-Image-2.1-PixelHead)
[![Comfy Registry](https://img.shields.io/badge/Comfy%20Registry-comfyui--qwenimage21--pixelhead-blueviolet)](https://registry.comfy.org/publishers/wither033/nodes/comfyui-qwenimage21-pixelhead)

---

## What's New in `v0.3` (2026-11-24 — 2D Haar Wavelet + Latent Spatial Highway + Detached-`LL` HF-GAN)

`v0.3` (`qwen_image_2.1_pixel_head_v03_bf16.safetensors`, `79.3 MiB`) upgrades `v0.2` across latency, activation VRAM, and sub-pixel detail:

- **Exact 2D Haar Wavelet readout (`512×512` `(LL, LH, HL, HH)` + `0`-parameter analytical `iDWT`)**: Replaces `v0.2`'s full-resolution `1024×1024` `GroupNorm + depthwise` stage with norm-free `WaveletConvBlock2d` blocks on the half-resolution wavelet grid. At `1024×1024` on NVIDIA L4, decode latency drops **`3.07×` vs `v0.2`** (`115.05 ms → 37.51 ms`, **`17.9×` faster** than the `671.57 ms` official `644.2 MiB` VAE) while peak activation VRAM drops **`44.2%`** (`904 MiB → 504 MiB`).
- **Multi-Scale `LatentSpatialHighway` (`3×3` conv bridge on `64`-ch `x0_hat_norm`)**: Carries neighbor-token stroke geometry directly from the denoised latent into the `8px`, `4px`, and `2px` wavelet grids, sharpening slanted barcode micro-text (`36.2 dB`) and dense `1px` copperplate cross-hatching (`+0.56 dB` domain gain over `v0.2`).
- **Detached-`LL` High-Frequency Wavelet PatchGAN (`LL.detach()`)**: Applies Hinge adversarial supervision strictly to the high-frequency `(LH, HL, HH)` subbands while detaching low-frequency `LL` luminance/chrominance, avoiding GAN color drift and lifting overall held-out `PSNR` to **`33.81 dB`** (`+0.79 dB` over `v0.2`, `+1.19 dB` over `v0.1`) and `LPIPS-VGG` to **`0.0736`** (`-42.1%` vs `v0.1`, `-8.9%` vs `v0.2`).
- **Node version requirement**: Update this custom node to **`v1.3.0+`** (`git pull` or ComfyUI Manager) before loading `v0.3` weights. A single loader node automatically detects `v0.3`, `v0.2`, and `v0.1` (`1x` / `2x`) checkpoints.

![1:1 held-out 4-way comparison: Official 644MB VAE vs v0.1 vs v0.2 vs v0.3 Wavelet](assets/v03_hero_1to1.png)

*(Full 6-row `1:1` native-pixel 4-way comparison board: [`assets/v03_4way_1to1_comparison.png`](assets/v03_4way_1to1_comparison.png))*

---

## Features

- **No `644.2 MiB` VAE required during sampling/decode**: Avoids `VAEDecode` intermediate VRAM spikes (`1.9–7.5 GB` at `1024–2048px`), offloads weights back to CPU after decoding, and includes cosine-blended `2K/4K` tiling (`tile_mode`).
- **Checkpoint tiers**:
  - **`v0.3` Wavelet High-Fidelity (`79.3 MiB` BF16 — Recommended default)**: `37.51 ms` on L4 (`~47.9 ms` on RTX 4060 Ti), `33.81 dB` overall PSNR (`39.17 dB` on close-up portraits), `0.0736` LPIPS-VGG.
  - **`v0.1` Fast (`48.8 MiB` `1x` / `52.1 MiB` `1x+2x`)**: `5.5–7.8 ms` on L4 (`~3.4 ms` on A100) for rapid batch seed drafting, plus an optional single-pass `2x` (`1024 → 2048`) branch.
  - **`v0.2` 1px Pyramid (`78.5 MiB` BF16)**: Retained on Hugging Face for reproducibility (`115.05 ms` on L4, `33.02 dB` PSNR).
- **Sampling & conditioning compatibility**:
  - Supports 8-step Turbo LoRA (`CFG = 1.0`) and 20–35 step Base sampling (`CFG = 3.5–4.5`) via `SigmaAdaLN`.
  - Supports Text-to-Image and `<image1>` multi-image reference editing (`norm_out` strips reference prefix tokens before `proj_out`).
  - Compatible with ComfyUI's `QwenImage21Cache` and outputs 4-channel RGBA (`image_rgb`, `alpha_mask`, `image_rgba`).

---

## Benchmark (`1024×1024` Held-Out Multi-Step Split on NVIDIA L4: `8s Turbo`, `20s CFG=3.5`, `24s CFG=4.5`)

Evaluated across 36 held-out `1024×1024` generations against `qwen_image_2.1_vae_bf16.safetensors` (`Comfy-Org/Qwen-Image-2.1`):

| Decoder | BF16 Size | `1024²` Latency (L4) | Speedup | Peak Act. VRAM | Overall PSNR (↑) | Overall LPIPS-VGG (↓) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Official Qwen-Image 2.1 VAE** | `644.2 MiB` | `671.57 ms` | `1.0×` | `~1.9–3.2 GB` | *(ref)* | `0.0000` |
| **`PixelHead v0.3` (Haar Wavelet + HF-GAN)** | **`79.3 MiB`** | **`37.51 ms`** | **`17.9×`** | **`504 MiB`** | **`33.81 dB`** | **`0.0736` (`-42.1%`)** |
| `PixelHead v0.2` (1px Full-Res Pyramid) | `78.5 MiB` | `115.05 ms` | `5.8×` | `904 MiB` | `33.02 dB` | `0.0808` |
| `PixelHead v0.1` (8×8 Linear) | `48.8 MiB` | `7.77 ms` | `86.4×` | `< 200 MiB` | `32.62 dB` | `0.1272` |

### Per-Domain Breakdown (`PSNR ↑ / LPIPS-VGG ↓`)

| Domain (`1024×1024` Held-Out) | `v0.1` (8×8 Linear) | `v0.2` (1px Pyramid) | **`v0.3` (Haar Wavelet + Highway)** | `v0.3` Gain vs `v0.2` |
| :--- | :---: | :---: | :---: | :--- |
| **`portrait` (Close-up skin pores & hair)** | `37.29 dB` / `0.1211` | `38.25 dB` / `0.0630` | **`39.17 dB` / `0.0572`** | **`+0.92 dB` PSNR, `-9.2%` LPIPS** |
| **`small_text` (Slanted tickets & signage)** | `32.50 dB` / `0.1235` | `32.80 dB` / `0.0792` | **`33.61 dB` / `0.0727`** | **`+0.81 dB` PSNR, `-8.2%` LPIPS** |
| **`fine_art` (Copperplate cross-hatching)** | `26.82 dB` / `0.1490` | `26.85 dB` / `0.1107` | **`27.41 dB` / `0.0987`** | **`+0.56 dB` PSNR, `-10.8%` LPIPS** |

---

## Installation

### 1. Install or Update Custom Node (`v1.3.0+` required for `v0.3` weights)
Install or update via ComfyUI Manager (`ComfyUI-QwenImage21-PixelHead`), `comfy node install comfyui-qwenimage21-pixelhead`, or `git`:

```bash
cd ComfyUI/custom_nodes/ComfyUI-QwenImage21-PixelHead
git pull
```

*(Fresh install: `git clone https://github.com/Wither033/ComfyUI-QwenImage21-PixelHead.git` inside `ComfyUI/custom_nodes`.)*

### 2. Download Weights
Download from [pocis/Qwen-Image-2.1-PixelHead](https://huggingface.co/pocis/Qwen-Image-2.1-PixelHead) into `ComfyUI/models/pixel_heads/` (or `ComfyUI/models/vae/`):

- **`qwen_image_2.1_pixel_head_v03_bf16.safetensors` (`79.3 MiB` — Recommended)**: `v0.3` Haar Wavelet + Latent Spatial Highway `1x` head (`37.51 ms` on L4, sharpest portraits, small print, and cross-hatching).
- `qwen_image_2.1_pixel_head_bf16.safetensors` (`48.8 MiB`): `v0.1` Fast `1x` head (`7.77 ms` on L4, rapid seed drafting).
- `qwen_image_2.1_pixel_head_x2_bf16.safetensors` (`52.1 MiB`): `v0.1` combined `1x` + `2x` (`1024 → 2048` quick upscale via `output_scale`).
- `qwen_image_2.1_pixel_head_v02_bf16.safetensors` (`78.5 MiB`): Previous `v0.2` 1px pyramid checkpoint, plus full `FP32` variants (`_v03.safetensors`, `_v02.safetensors`, etc.).

---

## Usage

Example workflows (defaulting to `v0.3`) are in [`example_workflows/`](example_workflows/):
- [`01_QwenImage21_PixelHead_ZeroVAE_EN.json`](example_workflows/01_QwenImage21_PixelHead_ZeroVAE_EN.json)
- [`01_QwenImage21_PixelHead_免VAE极速直出与对比_ZH.json`](example_workflows/01_QwenImage21_PixelHead_免VAE极速直出与对比_ZH.json)

```text
[Load Diffusion Model] ──► (Optional 8-Step LoRA / QwenImage21Cache) ──► [Qwen-Image 2.1 Pixel Head Tap]
                                                                               │              │
                                                                          MODEL│              │pixel_tap
                                                                               ▼              │
                                                                          [KSampler]          │
                                                                               │LATENT        │
                                                                               ▼              ▼
                                   [Load Qwen-Image 2.1 Pixel Head] ──► [Qwen-Image 2.1 Pixel Decode (Zero VAE)]
```

---

## Related Repositories

| Model | ComfyUI Node | Weights | Notes |
| :--- | :--- | :--- | :--- |
| **Qwen-Image 2.1** *(this repo)* | [Wither033/ComfyUI-QwenImage21-PixelHead](https://github.com/Wither033/ComfyUI-QwenImage21-PixelHead) | [pocis/Qwen-Image-2.1-PixelHead](https://huggingface.co/pocis/Qwen-Image-2.1-PixelHead) | **`v0.3` Wavelet (`79.3 MiB`, `37.5 ms`, `LPIPS 0.0736`)** + `v0.1` (`48.8 MiB`, `7.8 ms`), 4-ch RGBA |
| **Krea-2** | [Wither033/ComfyUI-Krea2-PixelHead](https://github.com/Wither033/ComfyUI-Krea2-PixelHead) | [pocis/Krea-2-PixelHead](https://huggingface.co/pocis/Krea-2-PixelHead) | `52.6 MiB` BF16, `6144d` bridged RGB, `59.55 ms` (`24.7×`), `33.33 dB` |
| **MiniMax-H3** *(preview)* | [Wither033/ComfyUI-MiniMaxH3-PixelHead](https://github.com/Wither033/ComfyUI-MiniMaxH3-PixelHead) | [pocis/MiniMax-H3-Video-PixelHead](https://huggingface.co/pocis/MiniMax-H3-Video-PixelHead) | Experimental preview (high-frequency video textures are currently soft) |
| **Training Code & Notes** | [Wither033/FastFrames-PixelHead-Trainer](https://github.com/Wither033/FastFrames-PixelHead-Trainer) | [HF Collection](https://huggingface.co/collections/pocis/fastframes-zero-vae-direct-pixelheads-comfyui-6b031df8e9212f8bae294154) | Training toolkit, DiT hook notes, and training notebooks (`01`–`07`) |

## Limitations

- **Extreme `1px` dense woodcut micro-engravings**: `v0.3` matches the `644 MiB` stock VAE closely on portraits (`39.17 dB`), ticket print (`33.61 dB`), and copperplate hatching, while ultra-dense `1px` woodcut engravings (`17.9 dB`, `LPIPS 0.105`) remain slightly softer than the `644 MiB` causal conv decoder.
- **Offline `.latent` files**: Decoding requires the final-step `4096`-dim DiT features captured by the Tap node during sampling.

## License, Attribution & Credits


- **Original Pixel Decoder & Training Pipeline Author**: **[Seunghyun Ji (`sorryhyun`)](https://huggingface.co/sorryhyun)** ([GitHub `@sorryhyun`](https://github.com/sorryhyun)) — author and publisher of **[`sorryhyun/anima_lora`](https://github.com/sorryhyun/anima_lora)** (`project/pixel_decoder`, `library/anima/pixel_head.py`, `scripts/pixel_head/`), **[`sorryhyun/anima_pixel_decoder`](https://huggingface.co/sorryhyun/anima-pixel-decoder)**, and **[`sorryhyun/ComfyUI-Anima-PixelDecoder`](https://github.com/sorryhyun/ComfyUI-Anima-PixelDecoder)**. Key architectural and training recipes adapted here — including the no-skip ConvNeXt + `2×` `PixelShuffle` `1x`/`2x` head layout, pre-linear `f_u + g·(f_c - f_u)` feature tap + latent patch embedding, single-step teacher-forced `ReplayBuffer` distillation against `VAE(x̂0)` across mixed Base/Turbo `σ` points, 4-channel RGBA readout, and 2D Haar wavelet `(LL, LH, HL, HH)` + detached-`LL` adversarial training — build directly upon `sorryhyun`'s work.
- **Foundational Paper**: [*FastFrames: Video Generation at Interactive Latency* (`arXiv:2611.23226`)](https://arxiv.org/abs/2611.23226) (Gene Chou, Guandao Yang, Fujun Luan, Lars Mescheder, Wei Dong, Stephan R. Richter, Vladlen Koltun — Apple & Cornell, 2026).
- **License**: Released under the [MIT License](LICENSE) (retaining `Copyright (c) 2026 Seunghyun Ji` and `Copyright (c) 2026 Wither033 / pocis`). Usage with Qwen-Image 2.1, Krea-2, or MiniMax-H3 models remains subject to each respective upstream base model's license terms.
