# ComfyUI-MiniMaxH3-PixelHead (`v0.2.0` Preview)

3D video direct pixel readout head for **MiniMax-H3** in ComfyUI (`45.7 MiB` BF16 vs `2.68 GB` stock ViT3D Video VAE).

[English](README.md) | [简体中文](README_zh.md)

[![Status: Preview](https://img.shields.io/badge/Status-Experimental%20Preview%20(Not%20Recommended)-orange)](#known-issues)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-pocis%2FMiniMax--H3--Video--PixelHead-yellow)](https://huggingface.co/pocis/MiniMax-H3-Video-PixelHead)
[![Comfy Registry](https://img.shields.io/badge/Comfy%20Registry-comfyui--minimaxh3--pixelhead-blueviolet)](https://registry.comfy.org/publishers/wither033/nodes/comfyui-minimaxh3-pixelhead)

> [!WARNING]
> **Not recommended for production use yet — please wait for upcoming optimizations.**
>
> This `v0.2.0` checkpoint is published early as an experimental baseline and low-VRAM layout preview tool:
> - Global colors, motion, `(1, 4, 4, 4, 4)` non-uniform frame timing (`17k + 5` frames), and flat 2D graphics (`36.73 dB`) decode properly.
> - However, **natural high-frequency textures (facial details, oil brushwork, foliage) and fast foreground occlusion (`25.91 dB`, `LPIPS = 0.29–0.37`) are noticeably over-smoothed** compared to the official `2.68 GB` 36-layer ViT3D Video VAE.
> - Do not use this version for final video renders. We are working on a follow-up update with perceptual LPIPS/frequency losses and native `16px` latent injection.

## Benchmark (`384×256×22f`, NVIDIA L4)

Tested on 20 held-out 22-frame clips (`T_lat = 7`, covering two `(1, 4, 4, 4, 4)` cycles; frames `0`, `11`, `17` shown below) against `minimax_h3_video_vae_int8_convrot.safetensors`:

| Video Decoder | Size | Median Latency | Speedup | Mean PSNR | Natural-Clip PSNR | LPIPS-VGG (↓) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Official `minimax_h3_video_vae` (ViT3D) | `2680.8 MiB` | `251.30 ms` | `1.0×` | *(ref)* | *(ref)* | `0.0000` |
| `MiniMaxH3VideoPixelHead` (`v0.2.0`) | `45.7 MiB` (BF16) / `91.4 MiB` (FP32) | `29.59 ms` | `8.5×` | `31.03 dB` | `25.91 – 30.13 dB` | `0.2338` (`0.29–0.37` natural) |

Breakdown by motion type:

| Subset | PSNR (↑) | LPIPS-VGG (↓) | Observation |
| :--- | :---: | :---: | :--- |
| `kinetic_cel_typo` (flat shapes & text) | `36.73 dB` | `0.0547` | Clean edges; pulls the aggregate mean up to `31.03 dB`. |
| `camera_pan_zoom` (art/photo pan & zoom) | `30.13 dB` | `0.2923` | Overall structure matches, fine brushwork and facial details are soft (`25.7–33.2 dB`). |
| `static_lockoff` (static textures) | `29.17 dB` | `0.3059` | No temporal flicker, softened surface grain. |
| `parallax_occlusion` (moving occlusion) | `25.91 dB` | `0.3677` | Blur along fast occlusion boundaries. |

![Keyframes f=0, 11, 17: stock ViT3D VAE (top rows) vs v0.2.0 preview (bottom rows)](assets/video_keyframes_comparison.png)

## Known Issues

Four factors explain the current softness and are targeted for the next revision:

1. **`16×` larger pixel volume per DiT token**: 2D heads (`Qwen-Image 2.1`, `Krea-2`) reconstruct `16×16 = 256` pixels per token. MiniMax-H3 combines a `16×` spatial VAE with `(1, 2, 2)` DiT patching, so each token spans `4 × 32 × 32 = 4,096` pixels. The stock decoder uses a 36-layer `2048`-dim ViT3D, whereas `v0.2.0` uses a `23.96M`-parameter ConvNeXt (`width = 768`).
2. **Pixel-space `MSE` regression at high terminal noise ($\sigma_{\text{last}} = 0.6316$)**: Under `video_shift = 12.0`, 8-step sampling starts its last step at $\sigma = 0.6316$. Training with pixel `L1 + MSE + gradient` alone (without perceptual LPIPS) causes the small network to average out uncertain fine textures.
3. **Latent injection resolution**: `x0_hat_vid` (`[B, 24, T_lat, H_lat, W_lat]`) already sits on the `16px` grid, but `v0.2.0` folds it `2×2` into the `32px` entry layer instead of feeding it into the `16px` stage directly.
4. **Calibration set size**: Trained for `1,800` rollouts on `280` clips at `384×256` (`25%` synthetic flat graphics).

## Related Repositories

| Model | Status | ComfyUI Node | Weights | Notes |
| :--- | :---: | :--- | :--- | :--- |
| **Qwen-Image 2.1** | Ready | [Wither033/ComfyUI-QwenImage21-PixelHead](https://github.com/Wither033/ComfyUI-QwenImage21-PixelHead) | [pocis/Qwen-Image-2.1-PixelHead](https://huggingface.co/pocis/Qwen-Image-2.1-PixelHead) | `v0.3` Wavelet (`79.3 MiB`, `37.5 ms`, `33.81 dB`, `LPIPS 0.0736`) + `v0.1` (`48.8 MiB`, `7.8 ms`), 4-ch RGBA |
| **Krea-2** | Ready | [Wither033/ComfyUI-Krea2-PixelHead](https://github.com/Wither033/ComfyUI-Krea2-PixelHead) | [pocis/Krea-2-PixelHead](https://huggingface.co/pocis/Krea-2-PixelHead) | `52.6 MiB` BF16, `6144d` bridged RGB, `59.55 ms` (`24.7×`), `33.33 dB` |
| **MiniMax-H3** *(this repo)* | Preview | [Wither033/ComfyUI-MiniMaxH3-PixelHead](https://github.com/Wither033/ComfyUI-MiniMaxH3-PixelHead) | [pocis/MiniMax-H3-Video-PixelHead](https://huggingface.co/pocis/MiniMax-H3-Video-PixelHead) | Not recommended for production yet; `45.7 MiB` BF16, `8.5×` faster, soft fine detail |
| **Training Code & Notes** | Reference | [Wither033/FastFrames-PixelHead-Trainer](https://github.com/Wither033/FastFrames-PixelHead-Trainer) | [HF Collection](https://huggingface.co/collections/pocis/fastframes-zero-vae-direct-pixelheads-comfyui-6b031df8e9212f8bae294154) | Training toolkit, DiT hook notes, and Colab L4 scripts |

## Installation (For Testing / Drafting Only)

1. Clone into `ComfyUI/custom_nodes` (or `comfy node install comfyui-minimaxh3-pixelhead`):
   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/Wither033/ComfyUI-MiniMaxH3-PixelHead.git
   ```
2. Download `minimax_h3_video_pixel_head_bf16.safetensors` (`45.7 MiB`) from [pocis/MiniMax-H3-Video-PixelHead](https://huggingface.co/pocis/MiniMax-H3-Video-PixelHead) into `ComfyUI/models/pixel_heads/`.
3. Example workflows are in [`example_workflows/`](example_workflows/). Place `MiniMax-H3 Video Pixel Head Tap` after `MiniMaxH3SigmaShift`, and connect `MiniMax-H3 Video Pixel Decode (Zero Video VAE)` to `SamplerCustomAdvanced`.

## License, Attribution & Credits


- **Original Pixel Decoder & Training Pipeline Author**: **[Seunghyun Ji (`sorryhyun`)](https://huggingface.co/sorryhyun)** ([GitHub `@sorryhyun`](https://github.com/sorryhyun)) — author and publisher of **[`sorryhyun/anima_lora`](https://github.com/sorryhyun/anima_lora)** (`project/pixel_decoder`, `library/anima/pixel_head.py`, `scripts/pixel_head/`), **[`sorryhyun/anima_pixel_decoder`](https://huggingface.co/sorryhyun/anima-pixel-decoder)**, and **[`sorryhyun/ComfyUI-Anima-PixelDecoder`](https://github.com/sorryhyun/ComfyUI-Anima-PixelDecoder)**. Key architectural and training recipes adapted here — including the no-skip ConvNeXt + `2×` `PixelShuffle` `1x`/`2x` head layout, pre-linear `f_u + g·(f_c - f_u)` feature tap + latent patch embedding, single-step teacher-forced `ReplayBuffer` distillation against `VAE(x̂0)` across mixed Base/Turbo `σ` points, 4-channel RGBA readout, and 2D Haar wavelet `(LL, LH, HL, HH)` + detached-`LL` adversarial training — build directly upon `sorryhyun`'s work.
- **Foundational Paper**: [*FastFrames: Video Generation at Interactive Latency* (`arXiv:2611.23226`)](https://arxiv.org/abs/2611.23226) (Gene Chou, Guandao Yang, Fujun Luan, Lars Mescheder, Wei Dong, Stephan R. Richter, Vladlen Koltun — Apple & Cornell, 2026).
- **License**: Released under the [MIT License](LICENSE) (retaining `Copyright (c) 2026 Seunghyun Ji` and `Copyright (c) 2026 Wither033 / pocis`). Usage with Qwen-Image 2.1, Krea-2, or MiniMax-H3 models remains subject to each respective upstream base model's license terms.
