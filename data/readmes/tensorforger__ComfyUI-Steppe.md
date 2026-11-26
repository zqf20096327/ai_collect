# ComfyUI-Steppe

[![Steppe: MOSS-Image 960x1280 upscaled 4x to 3840x5120 in latent space, bicubic vs Steppe zooms](https://raw.githubusercontent.com/tensorforger/tensorforger/main/assets/steppe_flux2/flux2_compare_cat.jpg)](https://raw.githubusercontent.com/tensorforger/tensorforger/main/assets/steppe_flux2/flux2_compare_cat.png)

> [!TIP]
> ### 🌾 Try it in your browser: [Steppe demo on Hugging Face](https://huggingface.co/spaces/TensorForger/Steppe)
> Upload an image and get a 2x or 4x Steppe upscale. Nothing to install.
>
> [![Open in Hugging Face Spaces](https://huggingface.co/datasets/huggingface/badges/resolve/main/open-in-hf-spaces-xl-dark.svg)](https://huggingface.co/spaces/TensorForger/Steppe)

**Steppe** is a family of *generative latent upscalers*: small generative models trained only for upscaling, which
run directly on VAE latents. The upscaled latent is **decoded straight by the VAE**: no second sampling pass of the
base model, no hires fix, no prompt.

- **2x resolution** of images and videos, e.g. 512 → 1024 or 1024 → 2048, and chained 2x → 2x.
- **2x frame rate** of videos (latent frame interpolation), also combined with 2x resolution.
- **One step**: about 45 ms for a 1024 px image with the default model. Most of the time goes to the VAE decode.
- **Sharpness control** through the high frequency feature (hff).
- Works with latents of two VAEs (see [Supported models](#supported-models)), all in the same loader and upscale nodes.

https://github.com/user-attachments/assets/5ac3da99-5d0a-496e-b78e-5911f3075968

*Wan 2.1 1.3B, 640x512 at 16 fps → Steppe 1280x1024 at 32 fps (2x resolution and 2x frame rate in one pass).*

## Supported models

Steppe models are trained per VAE: one model family serves every generative model that uses that VAE.

| generative models | VAE | Steppe models on Hugging Face | upscales |
|---|---|---|---|
| [Wan 2.1](https://huggingface.co/Wan-AI/Wan2.1-T2V-14B), [Wan 2.2 14B](https://huggingface.co/Wan-AI/Wan2.2-T2V-A14B), [Qwen-Image](https://huggingface.co/Qwen/Qwen-Image), [Qwen-Image-Edit](https://huggingface.co/Qwen/Qwen-Image-Edit), [Krea 2](https://huggingface.co/Comfy-Org/Krea-2) | Wan 2.1 VAE (`wan_2.1_vae`, `qwen_image_vae`) | [TensorForger/Steppe-Wan2.1](https://huggingface.co/TensorForger/Steppe-Wan2.1) | images and videos: 2x resolution, 2x frame rate |
| [FLUX.2 [dev]](https://huggingface.co/black-forest-labs/FLUX.2-dev), [FLUX.2 [klein] 4B](https://huggingface.co/black-forest-labs/FLUX.2-klein-4B) / [9B](https://huggingface.co/black-forest-labs/FLUX.2-klein-9B), [MOSS-Image](https://huggingface.co/OpenMOSS-Team/MOSS-Image-SFT) | FLUX.2 VAE (`flux2-vae`, `flux2-vae_small`) | [TensorForger/Steppe-Flux.2](https://huggingface.co/TensorForger/Steppe-Flux.2) | images: 2x resolution |

The model cards have the galleries, benchmarks and training details of each family. The nodes download the models on
first use.

## Installation

- **ComfyUI-Manager:** search for "Steppe" and install.
- **Comfy CLI:** `comfy node install steppe`
- **Manual:**
  ```bash
  cd ComfyUI/custom_nodes
  git clone https://github.com/TensorForger/ComfyUI-Steppe
  pip install -r ComfyUI-Steppe/requirements.txt
  ```

The nodes download models into `ComfyUI/models/latent_upscale_models` on first use. You can also download them
yourself from Hugging Face ([Wan 2.1](https://huggingface.co/TensorForger/Steppe-Wan2.1),
[FLUX.2](https://huggingface.co/TensorForger/Steppe-Flux.2)) into that folder.

## Models

Pick the models of the VAE your workflow uses: `steppe_wan_2_1_*` for the Wan 2.1 VAE, `steppe_flux_2_*` for the
FLUX.2 VAE. A model of the wrong VAE stops with an error that names the right one.

| file | steps | size | use |
|---|---|---|---|
| `steppe_wan_2_1_200M_1step.safetensors` | 1 | 445 MB | Wan 2.1 VAE **default**: the quality of the base model in one step |
| `steppe_wan_2_1_200M_base.safetensors` | 1-200 (20) | 444 MB | most control and research: steps, CFG on hff; same quality as 1-step |
| `steppe_wan_2_1_20M_1step.safetensors` | 1 | 39 MB | lite: very large outputs (2048 → 4096), real time |
| `steppe_flux_2_200M_1step.safetensors` | 1 | 385 MB | FLUX.2 VAE **default**: the quality of the base model in one step |
| `steppe_flux_2_200M_base.safetensors` | 1-200 (30) | 384 MB | most control and research: steps, CFG on hff; same quality as 1-step |
| `steppe_flux_2_20M_1step.safetensors` | 1 | 40 MB | lite: very large outputs, real time (with a tiny decoder) |

The FLUX.2 models upscale images only (no `temporal`).

## Nodes

| node | what it does |
|---|---|
| **Load Steppe Upscaler** | Loads a model and downloads released models if missing. `dtype`: auto (bfloat16 where supported) or float32. |
| **Steppe Upscale Latent** | Upscales a `LATENT`: `spatial` 2x resolution, `temporal` 2x frame rate (Wan 2.1), `hff`, `guidance`, `steps` (base models only, 0 = recommended), `seed`. |
| **Steppe Upscale Latent (Advanced)** | Adds `negative_hff`, `shift`, `noise_scale` and temporal windows for long videos. |
| **Steppe Measure HFF** | The hff value of an image, e.g. to match the sharpness of a reference. |

Basic graph: `KSampler → Steppe Upscale Latent → VAE Decode`. Images and videos use the same node.

## Example workflows

In `example_workflows/` (also listed in ComfyUI's template browser under custom nodes):

- `krea_2_steppe_image_upscale_4x.json`: Krea 2 Turbo at 960x1280, two chained Steppe nodes, 3840x5120 output.
- `wan_2.1_steppe_video_upscale_spatiotemporal.json`: Wan 2.1 T2V 1.3B at 640x512, 65 frames at 16 fps, Steppe 2x
  resolution and 2x frame rate: 1280x1024, 129 frames at 32 fps.
- `flux_2_klein_steppe_image_upscale_4x.json`: FLUX.2 [klein] 4B at 896x512, two chained Steppe nodes, 3584x2048
  output.
- `moss_image_steppe_image_upscale_4x.json`: MOSS-Image at 960x1280, two chained Steppe nodes, 3840x5120 output.

The model links and folders are in the note inside each workflow. The image workflows compare the results with the
Image Comparer of [rgthree-comfy](https://github.com/rgthree/rgthree-comfy).

### Parameters

- **hff** (high frequency feature, `0...1`, default 0.9) is the target amount of fine detail and sharpness. `-1`
  turns hff off and lets the model choose. The values are absolute: Steppe Measure HFF on a photo at the target
  resolution gives a value that matches it.
- **guidance**:
  - 1-step models: distilled guidance, trained on 1-3 (FLUX.2: 1-2). The default `1` turns it off and is safe and
    stable; `2` also works well. It is a model input, so it costs nothing.
  - Base models: classifier free guidance between `hff` and `negative_hff` (default: no hff). On Wan 2.1 the effect
    is subtle, so use 4-8 for a visible change; FLUX.2 reacts much more strongly to hff. Guidance above 1 costs two
    passes per step.
- **steps** / **shift** (base models): `0` uses the recommended values, 20 steps / shift 4 for Wan 2.1 and 30 steps /
  shift 2 for FLUX.2.
- **temporal**: T latent frames become 1 + 2 (T - 1), i.e. 81 → 161 pixel frames for Wan. The first frame is kept.
- **temporal_window** (Advanced): long videos run without windows, since memory is handled by chunking. Windows of
  about 8-16 source latent frames keep each piece close to the training clip length.

### Tips

- **Chained upscaling** 512 → 1024 → 2048 (4x): use two Steppe nodes. The 1-step model is as good as the base model
  here, too. The 20M model is fast enough for the 2048 → 4096 step.
- **Any aspect ratio** works; inputs from 512x512 pixels up are tested.
- **Base model**: same quality as the 1-step model for general use; it is for control and research (steps, CFG on
  hff, negative hff, shift, noise scale).
- **Decoding large outputs**: use `VAE Decode (Tiled)` for 2048 px images and upscaled videos.
- **Video**: 81 frames at 480x832 → 960x1664 at 2x frame rate takes 3.5 s and 9 GB peak VRAM with the 1-step model
  (RTX 5090), plus the VAE decode.
- **Not supported**: the Wan 2.2 5B (TI2V) VAE (48 channels), and FLUX.1, SD3 and SDXL latents. 16 channel FLUX.1 /
  SD3 latents pass the Wan 2.1 channel check but give wrong results.

## How it works

Latent upscalers made for hires fix only stretch the latent, so the base model has to denoise it again at the high
resolution. Steppe is a generative model itself: a window transformer on the full resolution latent grid generates
the missing detail with rectified flow, distilled to one step. Details on the model cards:
[Wan 2.1](https://huggingface.co/TensorForger/Steppe-Wan2.1#how-it-works),
[FLUX.2](https://huggingface.co/TensorForger/Steppe-Flux.2#how-it-works).

## Benchmark

1000 photos (Axis-V1), 512 → 1024 from the latent only (no prompt). Patch FID on native 256 px tiles (lower is
better); latency at batch 1 on an RTX 5090, VAE decode included.

| VAE | Steppe 200M 1-step | Steppe 20M 1-step | best other 2x solution | bicubic after decode |
|---|---|---|---|---|
| Wan 2.1 | **4.36**, 179 ms | 5.85, 141 ms | 6.33, 29 ms (Wan2.1-VAE-upscale2x decoder) | 14.13, 30 ms |
| FLUX.2 | **1.75**, 172 ms | 2.20, 131 ms | 4.28, 128 ms (FlowUpscaler, our previous model) | 8.12, 25 ms |

Full tables with FID, color shift, VRAM and plots:
[Steppe-Wan2.1](https://huggingface.co/TensorForger/Steppe-Wan2.1#benchmark),
[Steppe-Flux.2](https://huggingface.co/TensorForger/Steppe-Flux.2#benchmark). Benchmark images:
[Axis-V1](https://huggingface.co/datasets/refine-axis/axis-v1_1k) by refine-axis (CC BY 4.0).

## Python

The `steppe` package is pure PyTorch and does not need ComfyUI:

```bash
pip install "steppe[standalone] @ git+https://github.com/TensorForger/ComfyUI-Steppe"
```

```python
from steppe import UpscaleSettings, load_upscaler

upscaler = load_upscaler("steppe_wan_2_1_200M_1step.safetensors")  # downloads from Hugging Face
upscaler.model.to("cuda")
# raw (unnormalized) Wan 2.1 VAE latents, [B, 16, T, H, W] or [B, 16, H, W]
upscaled = upscaler.upscale(latents, UpscaleSettings(spatial=True, temporal=False, hff=0.9, guidance=1.0))

flux_upscaler = load_upscaler("steppe_flux_2_200M_1step.safetensors")
flux_upscaler.model.to("cuda")
# FLUX.2 latents as ComfyUI and the diffusers FLUX.2 pipelines use them: 2x2 packed and batch norm normalized,
# [B, 128, H / 16, W / 16]
flux_upscaled = flux_upscaler.upscale(flux_latents, UpscaleSettings(hff=0.9, guidance=1.0))
```

## Related

- [comfyui-flow-upscaler](https://github.com/tensorforger/comfyui-flow-upscaler): the ancestor of Steppe, a FLUX.2
  latent upscaler.
- [LUA: latent upscale adapters](https://arxiv.org/abs/2511.10629): single pass regression upscalers. Steppe is
  generative instead.

## License

MIT (see `LICENSE`). Steppe works on latents of the Wan 2.1 VAE (Apache-2.0, Wan Team, Alibaba Group) and of the
FLUX.2 VAE (Apache-2.0, Black Forest Labs); see `NOTICE`.
