# ComfyUI-Krea2-PixelHead

Bridged direct RGB pixel readout head for **Krea-2** in ComfyUI, replacing the `242.0 MiB` 3D-causal `qwen_image_vae` (`WanVAE`) decoder.

[English](README.md) | [简体中文](README_zh.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-pocis%2FKrea--2--PixelHead-yellow)](https://huggingface.co/pocis/Krea-2-PixelHead)
[![Comfy Registry](https://img.shields.io/badge/Comfy%20Registry-comfyui--krea2--pixelhead-blueviolet)](https://registry.comfy.org/publishers/wither033/nodes/comfyui-krea2-pixelhead)

Following [*FastFrames* (`arXiv:2611.23226`)](https://arxiv.org/abs/2611.23226), this node hooks `SingleStreamDiT`'s `last.linear` on the final sampling step to extract the `6144`-dim modulated target-image tokens (stripping variable-length text and style-reference tokens) together with the denoised `2×2` latent patches (`d_lat = 64`), and decodes them to RGB with a `27.49M`-parameter (`52.6 MiB` BF16) ConvNeXt + PixelShuffle head.

At `768×768` on an NVIDIA L4, median decode latency drops from `1468.9 ms` (`qwen_image_vae`) to `59.55 ms` (`24.7×`), with `< 0.2 GB` peak extra VRAM.

![1:1 held-out comparison against stock qwen_image_vae](assets/hero_1to1_comparison.png)

## Features

- **`24.7×` faster decode, no VAE needed for T2I**: Avoids running the 3D causal convolutions of `qwen_image_vae` and prevents end-of-sampling VRAM spikes at `1024–2048px`.
- **`6144 → 1024` bridged readout**: Uses a bias-free linear bridge (`6144 → 1024`) plus `FP32` output projection, preserving fine lace, brushwork, and dark tonal transitions without `BF16` banding.
- **Compatible across Krea-2 variants**:
  - Works with `krea2_turbo` (8 steps, `CFG = 1.0`, `shift = 1.15`), `krea2_raw` (20–35 steps, `CFG > 1.0`), FP8/INT8/GGUF quantizations, and fine-tunes.
  - Supports both Text-to-Image and Style/Reference image conditioning (`tap.py` computes `txtlen` and `ref_tokens` dynamically to slice only the target image tokens).

## Benchmark (`768×768` Held-Out Fine-Art Split, NVIDIA L4)

Evaluated against `qwen_image_vae.safetensors` (`Comfy-Org/Krea-2`) across 40 held-out paintings and engravings (alternating 8-step Turbo $\sigma = 0.3109$ and multi-step $\sigma = 0.1163$):

| Decoder | Size | Median Latency | Speedup | PSNR (↑) | LPIPS-VGG (↓) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Official `qwen_image_vae` | `242.0 MiB` | `1468.90 ms` | `1.0×` | *(ref)* | `0.0000` |
| `Krea2PixelHead` | `52.6 MiB` (BF16) / `104.9 MiB` (FP32) | `59.55 ms` | `24.7×` | `33.33 dB` | `0.2300` |

- Classical & low-key portraits: `37.1 – 41.6 dB` PSNR
- Multi-subject color illustration: `32.9 – 33.5 dB` PSNR
- Fine copperplate etchings: `30.8 dB` PSNR

## Related Repositories

| Model | ComfyUI Node | Weights | Notes |
| :--- | :--- | :--- | :--- |
| **Krea-2** *(this repo)* | [Wither033/ComfyUI-Krea2-PixelHead](https://github.com/Wither033/ComfyUI-Krea2-PixelHead) | [pocis/Krea-2-PixelHead](https://huggingface.co/pocis/Krea-2-PixelHead) | `52.6 MiB` BF16, `6144d` bridged RGB, `59.55 ms` (`24.7×`), `33.33 dB` |
| **Qwen-Image 2.1** | [Wither033/ComfyUI-QwenImage21-PixelHead](https://github.com/Wither033/ComfyUI-QwenImage21-PixelHead) | [pocis/Qwen-Image-2.1-PixelHead](https://huggingface.co/pocis/Qwen-Image-2.1-PixelHead) | `v0.3` Wavelet (`79.3 MiB`, `37.5 ms`, `33.81 dB`, `LPIPS 0.0736`) + `v0.1` (`48.8 MiB`, `7.8 ms`), 4-ch RGBA |
| **MiniMax-H3** *(preview)* | [Wither033/ComfyUI-MiniMaxH3-PixelHead](https://github.com/Wither033/ComfyUI-MiniMaxH3-PixelHead) | [pocis/MiniMax-H3-Video-PixelHead](https://huggingface.co/pocis/MiniMax-H3-Video-PixelHead) | Experimental preview (not recommended for production yet; high-frequency textures are soft) |
| **Training Code & Notes** | [Wither033/FastFrames-PixelHead-Trainer](https://github.com/Wither033/FastFrames-PixelHead-Trainer) | [HF Collection](https://huggingface.co/collections/pocis/fastframes-zero-vae-direct-pixelheads-comfyui-6b031df8e9212f8bae294154) | Training toolkit, DiT hook notes, and Colab L4 scripts |

## Installation

### 1. Custom Node
Install via ComfyUI Manager (`ComfyUI-Krea2-PixelHead`), `comfy node install comfyui-krea2-pixelhead`, or `git clone`:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/Wither033/ComfyUI-Krea2-PixelHead.git
```

### 2. Weights
Download from [pocis/Krea-2-PixelHead](https://huggingface.co/pocis/Krea-2-PixelHead) into `ComfyUI/models/pixel_heads/` (or `ComfyUI/models/vae/`):

- `krea2_pixel_head_bf16.safetensors` (`52.6 MiB`): recommended, BF16 trunk + FP32 output layer.
- `krea2_pixel_head.safetensors` (`104.9 MiB`): full FP32 checkpoint.

## Usage

Example workflows are in [`example_workflows/`](example_workflows/):
- [`01_Krea2_PixelHead_ZeroVAE_EN.json`](example_workflows/01_Krea2_PixelHead_ZeroVAE_EN.json)
- [`01_Krea2_PixelHead_ZeroVAE_ZH.json`](example_workflows/01_Krea2_PixelHead_ZeroVAE_ZH.json)

```text
[Load Diffusion Model (Krea-2)] ──► [Krea-2 Pixel Head Tap]
                                         │            │
                                    MODEL│            │pixel_tap
                                         ▼            │
                                    [KSampler]        │
                                         │LATENT      │
                                         ▼            ▼
            [Load Krea-2 Pixel Head] ──► [Krea-2 Pixel Decode (Zero VAE)] ──► IMAGE
```

Pure Text-to-Image requires no VAE. When using style/reference images, keep the VAE connected only to encode the reference input image, and use `Krea-2 Pixel Decode (Zero VAE)` after `KSampler`.

## Limitations

- **Step range**: Trained across `ModelSamplingFlux(shift=1.15)` final-step $\sigma \in [0.045, 0.420]$ (5–12 step Turbo and 18–35 step Raw).
- **Offline `.latent` files**: Requires live `6144`-dim DiT features from the final denoising step; cannot decode standalone `.latent` files without running the DiT.
- **Sub-pixel chaotic splatter**: On dense ink-splatter abstractions, sub-pixel grain is slightly softer than `qwen_image_vae`.

## License & Credits

- **License**: MIT (clean-room PyTorch implementation).
- **References**: Direct pixel readout formulation from [*FastFrames: Video Generation at Interactive Latency*](https://arxiv.org/abs/2611.23226) (Apple Research, 2026); 2D feature readout and ComfyUI hook design informed by `sorryhyun/anima-pixel-decoder`.
