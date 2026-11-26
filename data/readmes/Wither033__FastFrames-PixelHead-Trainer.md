# FastFrames-PixelHead-Trainer

Training code, model-adaptation notes, and single-GPU Colab L4/A100 notebooks for building direct pixel readout heads across 2D image and 3D video Diffusion Transformers (DiTs) in ComfyUI.

[English](README.md) | [简体中文](README_zh.md) | [Adaptation Notes & Post-Mortems (EN)](docs/PLAYBOOK_ADAPTING_NEW_MODELS_EN.md) | [新模型适配与问题记录 (ZH)](docs/PLAYBOOK_ADAPTING_NEW_MODELS_ZH.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![HF Collection](https://img.shields.io/badge/Hugging%20Face-Collection-yellow)](https://huggingface.co/collections/pocis/fastframes-zero-vae-direct-pixelheads-comfyui-6b031df8e9212f8bae294154)

## 1. Background

Flow-matching DiTs carry `3072`–`6144` channels per token right before their final linear layer (`proj_out / linear`), then project down to a `16`–`128` channel latent and rely on a large 2D/3D VAE decoder (`242 MiB` to `4.85 GB`) to reconstruct pixels.

Following the direct pixel readout formulation in [*FastFrames: Video Generation at Interactive Latency* (`arXiv:2611.23226`)](https://arxiv.org/abs/2611.23226) and single-step Replay Buffer distillation (`sorryhyun/anima-pixel-decoder`), this repository collects our clean-room MIT PyTorch library (`pixelhead_trainer`), ComfyUI `ModelPatcher` tap implementations for five backbones, and the Colab L4 (24 GB) training scripts used to train them:

- On 2D image models (`16×16` pixels/token), a `48.8–79.3 MiB` (BF16) head decodes `17.9×–86.4×` faster than the stock VAE (`37.51 ms` / `33.81 dB` / `LPIPS 0.0736` on **Qwen-Image 2.1 `v0.3` Wavelet**; `5.55–7.77 ms` on `v0.1` Fast; `59.55 ms` / `33.33 dB` on **Krea-2**), with optional single-pass `2x` (`1024 → 2048`) upscaling.
- On high-compression 3D video models (`4 × 32×32` or `8 × 32×32` pixels/token), pure pixel-space `MSE` distillation is fast (`8.5×` on MiniMax-H3) but over-smooths fine natural textures unless paired with perceptual/frequency losses — documented in full in [docs/PLAYBOOK_ADAPTING_NEW_MODELS_EN.md](docs/PLAYBOOK_ADAPTING_NEW_MODELS_EN.md).

| `Qwen-Image 2.1` (`5.55 ms`, `67.1×`, `33.91 dB`, 4-ch RGBA) | `Krea-2` (`59.55 ms`, `24.7×`, `33.33 dB`, `6144d` bridge) |
| :---: | :---: |
| ![Qwen-Image 2.1 comparison](assets/qwen21_hero_1to1_comparison.png) | ![Krea-2 comparison](assets/krea2_hero_1to1_comparison.png) |

## 2. Backbones & Released Checkpoints

Each DiT has an independent pre-linear hidden space and needs its own pixel head. Released weights are grouped in our [Hugging Face Collection](https://huggingface.co/collections/pocis/fastframes-zero-vae-direct-pixelheads-comfyui-6b031df8e9212f8bae294154):

| Backbone | Modality | Notebook (`notebooks/`) | ComfyUI Node | Weights | Status & Benchmark (L4) |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **Qwen-Image 2.1 (`v0.3` Wavelet)** | 2D RGBA (`1x` Haar Wavelet) | [`07_Train_QwenImage21...v03...ipynb`](notebooks/07_Train_QwenImage21_PixelHead_v03_Colab_A100.ipynb) | [Wither033/ComfyUI-QwenImage21-PixelHead](https://github.com/Wither033/ComfyUI-QwenImage21-PixelHead) | [pocis/Qwen-Image-2.1-PixelHead](https://huggingface.co/pocis/Qwen-Image-2.1-PixelHead) | Ready · **`37.51 ms` (`17.9×`), `33.81 dB`, `LPIPS 0.0736`**, `79.3 MiB` BF16 |
| **Qwen-Image 2.1 (`v0.1` / `v0.2`)** | 2D RGBA (`1x` & `2x`) | [`01_...L4.ipynb`](notebooks/01_Train_QwenImage21_PixelHead_Colab_L4.ipynb) / [`06_...v02.ipynb`](notebooks/06_Train_QwenImage21_PixelHead_v02_Colab_A100.ipynb) | [Wither033/ComfyUI-QwenImage21-PixelHead](https://github.com/Wither033/ComfyUI-QwenImage21-PixelHead) | [pocis/Qwen-Image-2.1-PixelHead](https://huggingface.co/pocis/Qwen-Image-2.1-PixelHead) | Ready · `v0.1`: `7.77 ms` (`86.4×`), `48.8 MiB`; `v0.2`: `115.05 ms`, `78.5 MiB` |
| **Krea-2** | 2D RGB (`1x` & `2x`) | [`02_Train_Krea2...ipynb`](notebooks/02_Train_Krea2_PixelHead_Colab_L4.ipynb) | [Wither033/ComfyUI-Krea2-PixelHead](https://github.com/Wither033/ComfyUI-Krea2-PixelHead) | [pocis/Krea-2-PixelHead](https://huggingface.co/pocis/Krea-2-PixelHead) | Ready · `59.55 ms` (`24.7×`), `33.33 dB`, `52.6 MiB` BF16 |
| **FLUX.3-Image-Klein** | 2D RGB (`1x` & `2x`) | [`03_Train_Flux3Klein...ipynb`](notebooks/03_Train_Flux3Klein_PixelHead_Colab_L4.ipynb) | [`comfyui_nodes/ComfyUI-Flux3-PixelHead`](comfyui_nodes/ComfyUI-Flux3-PixelHead) | Not trained yet | Script ready (`24.41M` params, `46.6 MiB` BF16) |
| **LTX-2.5** | 3D Video (`8*T-7` causal) | [`04_Train_LTX25_Video...ipynb`](notebooks/04_Train_LTX25_VideoPixelHead_v2_Colab_L4.ipynb) | [`comfyui_nodes/ComfyUI-LTX25-PixelHead`](comfyui_nodes/ComfyUI-LTX25-PixelHead) | Not trained yet | `v2` script ready (`23.87M` params, `2.67×` overcomplete) |
| **MiniMax-H3** | 3D Video (`(1,4,4,4,4)` causal) | [`05_Train_MiniMaxH3_Video...ipynb`](notebooks/05_Train_MiniMaxH3_VideoPixelHead_v2_Colab_L4.ipynb) | [Wither033/ComfyUI-MiniMaxH3-PixelHead](https://github.com/Wither033/ComfyUI-MiniMaxH3-PixelHead) | [pocis/MiniMax-H3-Video-PixelHead](https://huggingface.co/pocis/MiniMax-H3-Video-PixelHead) | Preview (`v0.2.0`, not recommended for production; soft fine detail) |

## 3. Method Summary

### 3.1 Input Signals: `f` (Post-AdaLN Hidden State) + `x0_hat_norm` (Denoised Latent)

In flow-matching DiTs, the final linear projection predicts velocity $v = W f + b$, and the final step's clean latent estimate is:

$$\hat{x}_0 = x_t - \sigma_{\text{last}} \cdot v$$

1. **Hook point (`post-AdaLN, pre-linear`)**: A `register_forward_pre_hook` right before the final `linear / proj_out` captures $f \in \mathbb{R}^{B \times N_{\text{img}} \times d_{\text{feat}}}$.
2. **CFG linearity**: Because the hook precedes a linear layer, combining conditional and unconditional features under `CFG > 1`:
   $$f_{\text{cfg}} = f_u + g \cdot (f_c - f_u)$$
   matches the guided velocity $v_{\text{cfg}}$ without approximation, so one checkpoint covers both `CFG = 1.0` distilled models and `CFG > 1.0` Base models.
3. **Adding `x0_hat_norm`**: Velocity $f$ alone omits the starting point $x_t$ and varies with step count. Fusing `LayerNorm(f)` with the denoised normalized latent $\hat{x}_{0,\text{norm}}$ (`EntryNorm(Bridge(Norm(f)) + LatProj(x0_hat_norm))`) improves PSNR by `> 6 dB` and stabilizes readout across 4-step, 8-step, and 35-step schedules.

### 3.2 Practical Design Details

1. **Avoid direct linear skip connections from `f` to RGB**: A linear skip stalls training near `~26.5 dB`; passing purely through ConvNeXt + PixelShuffle reaches `33–41 dB` on 2D models.
2. **Bias-free entry bridge (`Linear(d_feat -> width, bias=False)`)**: Maps `3072`–`6144` channels down to `width = 1024` (2D) or `768` (3D), keeping BF16 checkpoints around `45–53 MiB`.
3. **Keep the final linear projection overcomplete**: At the final spatial/temporal grid, keep channel width `w_final >= 2.5 × out_dim`. On `32×32`-per-token 3D video models, use three `2×` `PixelShuffle` stages down to a `4×4` spatial grid (`256 → 96` or `256 → 48`) instead of stopping at `8×8` (`256 → 1536` rank bottleneck).
4. **Run `out_proj` in `FP32`**: Wrap the final linear layer in `torch.autocast(..., enabled=False)` and keep its weights in `float32` inside BF16 `.safetensors` files to avoid `1–2` level quantization banding.
5. **Distill `TeacherVAE.decode(x0_hat)` rather than raw ground-truth images**: At finite $\sigma_{\text{last}}$, $\hat{x}_0$ has already lost part of the original noise-masked micro-detail; training against `TeacherVAE.decode(x0_hat)` provides a deterministic target.

### 3.3 High-Frequency Wavelet Upgrade (`Qwen-Image 2.1 v0.1 → v0.2 → v0.3`)

On `1024×1024` close-up portraits, slanted barcode print, and `1px` copperplate cross-hatching, `v0.3` ([`07_Train_QwenImage21_PixelHead_v03_Colab_A100.ipynb`](notebooks/07_Train_QwenImage21_PixelHead_v03_Colab_A100.ipynb), runnable on a single 24 GB L4) combines three additions:
1. **2D Haar Wavelet subband readout (`512×512` `(LL, LH, HL, HH)` + analytical `iDWT`)**: Avoids full-resolution `1024×1024` `GroupNorm + depthwise` memory traffic, running **`3.07×` faster than `v0.2`** (`37.51 ms` vs `115.05 ms` on L4) with **`-44.2%` peak activation VRAM** (`504 MiB` vs `904 MiB`).
2. **Multi-Scale `LatentSpatialHighway`**: Applies `3×3` spatial convolutions directly on `64`-ch `x0_hat_norm` across `8px`, `4px`, and `2px` grids to preserve cross-token stroke continuity.
3. **Detached-`LL` High-Frequency Wavelet PatchGAN**: Applies Hinge adversarial loss strictly to `(LH, HL, HH)` with `LL.detach()`, sharpening fine detail (`LPIPS 0.1272 → 0.0808 → 0.0736`) while simultaneously raising `PSNR` (`32.62 → 33.02 → 33.81 dB`; portraits reach `39.17 dB`).

![Qwen-Image 2.1 v0.3 4-way 1:1 comparison](assets/qwen21_v03_hero_1to1.png)

## 4. ComfyUI Backbone Hook Reference

| Backbone | Source File | Pre-Hook Module | `d_feat` | `d_lat` | Footprint / Token | Sequence Slicing & Schedule Notes |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **Qwen-Image 2.1** | `comfy/ldm/qwen_image21/model.py` | `diffusion_model.proj_out` | `4096` | `64` | `16×16` RGBA | `norm_out(hidden_states[:, prefix_len:])` strips text and `<image1>` prefix tokens before `proj_out`. |
| **Krea-2** | `comfy/ldm/krea2/model.py` | `diffusion_model.last.linear` | `6144` | `16×2×2=64` | `16×16` RGB | `SingleStreamDiT` concatenates `[txt, target_img, ref_img]`; slice `[:, txtlen : txtlen + img_tokens, :]`. |
| **FLUX.3-Klein** | `comfy/ldm/flux3/model.py` | `final_layer["image"].linear` | `3072` | `128` | `16×16` RGB | Pass `sample_sigmas=[sigma, 0.0]` in `transformer_options` for FlowMap terminal-step velocity. |
| **LTX-2.5** (`v2`) | `comfy/ldm/lightricks/av_model.py` | `diffusion_model.proj_out` | `4096` | `128` | `8t × 32×32` RGB | Unbind video latent from `NestedTensor`; drop 7 causal pre-frames (`8*T_lat - 7`). |
| **MiniMax-H3** (`v2`) | `comfy/ldm/minimax/model.py` | `diffusion_model.final_layer` | `5376` | `24×1×2×2=96` | `(1,4,4,4,4)t × 32×32` | 8-step PDD models call `F.linear` directly and bypass `video_out.forward`; hook `final_layer` and compute `mod(video_seg)`. |

## 5. Single-GPU Colab L4 (24 GB) Pipeline

Each notebook in [`notebooks/`](notebooks/) runs in three stages:

1. **Offline latent & conditioning cache (~6–10 min)**: Encodes calibration samples with the stock VAE and text encoder onto local NVMe, then unloads the `8B–32B` text encoder before training so peak VRAM stays around `9–16 GB`.
2. **Pre-flight checks (~10 sec)**: Verifies non-square spatial crop equivariance (`max_abs_diff < 1e-5`), chunked causal equivalence (`decode_chunked == forward`), and a 90-step P0 smoke climb (`>= +6 dB`) before starting the full run.
3. **Single-step Replay Buffer training (~25–45 min)**: Samples terminal $\sigma_{\text{last}}$ across distilled Turbo and multi-step Base regimes, runs a single frozen DiT forward pass per rollout, pushes `(f, x0_hat_norm, TeacherVAE.decode(x0_hat))` into a `ReplayBuffer`, and updates the PixelHead `12–16` times per rollout:
   $$\mathcal{L}_{2\text{D}} = 0.5\,\mathcal{L}_1 + 5.0\,\text{MSE} + 0.05\,(\mathcal{L}_{\nabla_h} + \mathcal{L}_{\nabla_w})$$
   (with temporal finite-difference and motion-weighted terms added for 3D video). Note that for `32×32`-per-token 3D video models, an additional perceptual loss (`LPIPS-VGG` / FFT) is needed to avoid `MSE` smoothing.

## 6. Local Verification (CPU)

```bash
pip install -e .
CUDA_VISIBLE_DEVICES="" python tests/test_all_heads_and_gates.py
```

## 7. License & References

- **Code License**: MIT License (clean-room PyTorch & ComfyUI implementation). Deployed checkpoints remain subject to the upstream base model's license terms where applicable.
- **References**:
  - Direct pixel readout, linear bridge, and gradient loss formulation: [*FastFrames: Video Generation at Interactive Latency*](https://arxiv.org/abs/2611.23226) (Gene Chou et al., Apple & Cornell, 2026).
  - Single-step Teacher-Forced Replay Buffer training and ComfyUI wrapper hooks: [`sorryhyun/anima-pixel-decoder`](https://huggingface.co/sorryhyun/anima-pixel-decoder).
