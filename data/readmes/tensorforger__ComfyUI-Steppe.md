# ComfyUI-Steppe

[![Steppe: 4× detail, decoded directly. No second denoising pass of the base model.](https://raw.githubusercontent.com/tensorforger/tensorforger/main/assets/steppe/hero_cat.jpg)](https://raw.githubusercontent.com/tensorforger/tensorforger/main/assets/steppe/hero_cat.png)

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
- Works with latents of the **Wan 2.1 VAE**, which is used by Wan 2.1, Wan 2.2 14B, Qwen-Image, Qwen-Image-Edit and
  Krea 2, among others. Both `wan_2.1_vae` and `qwen_image_vae` decode the upscaled latents.

https://github.com/user-attachments/assets/5ac3da99-5d0a-496e-b78e-5911f3075968

*Wan 2.1 1.3B, 640x512 at 16 fps → Steppe 1280x1024 at 32 fps (2x resolution and 2x frame rate in one pass).*

Models: [TensorForger/Steppe-Wan2.1](https://huggingface.co/TensorForger/Steppe-Wan2.1) on Hugging Face.
The nodes download them on first use.

## Gallery

[![Any style, one model](https://raw.githubusercontent.com/tensorforger/tensorforger/main/assets/steppe/compare_anime.jpg)](https://raw.githubusercontent.com/tensorforger/tensorforger/main/assets/steppe/compare_anime.png)

[![Texture, not blur](https://raw.githubusercontent.com/tensorforger/tensorforger/main/assets/steppe/compare_cloth.jpg)](https://raw.githubusercontent.com/tensorforger/tensorforger/main/assets/steppe/compare_cloth.png)

[![Any aspect ratio](https://raw.githubusercontent.com/tensorforger/tensorforger/main/assets/steppe/compare_leaves.jpg)](https://raw.githubusercontent.com/tensorforger/tensorforger/main/assets/steppe/compare_leaves.png)

All examples: Krea 2 Turbo, Steppe 200M 1-step, chained 2x → 2x, no prompt and no refinement pass. Bicubic tiles are
upscaled by the same factor from the same input. Click an image for the full resolution card.

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
yourself from [Hugging Face](https://huggingface.co/TensorForger/Steppe-Wan2.1) into that folder.

## Models

[![Three models, one node](https://raw.githubusercontent.com/tensorforger/tensorforger/main/assets/steppe/models_lineup.jpg)](https://raw.githubusercontent.com/tensorforger/tensorforger/main/assets/steppe/models_lineup.png)

| file | steps | size | use |
|---|---|---|---|
| `steppe_wan_2_1_200M_1step.safetensors` | 1 | 445 MB | **default**: the quality of the base model in one step |
| `steppe_wan_2_1_200M_base.safetensors` | 1-200 (20) | 444 MB | most control and research: steps, CFG on hff; same quality as 1-step |
| `steppe_wan_2_1_20M_1step.safetensors` | 1 | 39 MB | lite: very large outputs (2048 → 4096), real time |

## Nodes

| node | what it does |
|---|---|
| **Load Steppe Upscaler** | Loads a model and downloads released models if missing. `dtype`: auto (bfloat16 where supported) or float32. |
| **Steppe Upscale Latent** | Upscales a `LATENT`: `spatial` 2x resolution, `temporal` 2x frame rate, `hff`, `guidance`, `steps` (base model only), `seed`. |
| **Steppe Upscale Latent (Advanced)** | Adds `negative_hff`, `shift`, `noise_scale` and temporal windows for long videos. |
| **Steppe Measure HFF** | The hff value of an image, e.g. to match the sharpness of a reference. |

Basic graph: `KSampler → Steppe Upscale Latent → VAE Decode`. Images and videos use the same node.

[![The 4x example workflow](https://raw.githubusercontent.com/tensorforger/tensorforger/main/assets/steppe/workflow.jpg)](https://raw.githubusercontent.com/tensorforger/tensorforger/main/assets/steppe/workflow.png)

## Example workflows

In `example_workflows/` (also listed in ComfyUI's template browser under custom nodes):

- `krea_2_steppe_image_upscale_4x.json`: Krea 2 Turbo at 960x1280, two chained Steppe nodes, 3840x5120 output.
- `wan_2.1_steppe_video_upscale_spatiotemporal.json`: Wan 2.1 T2V 1.3B at 640x512, 65 frames at 16 fps, Steppe 2x
  resolution and 2x frame rate: 1280x1024, 129 frames at 32 fps.

The model links and folders are in the note inside each workflow.

### Parameters

[![hff: dial in the detail](https://raw.githubusercontent.com/tensorforger/tensorforger/main/assets/steppe/hff_portrait.jpg)](https://raw.githubusercontent.com/tensorforger/tensorforger/main/assets/steppe/hff_portrait.png)

- **hff** (high frequency feature, `0...1`, default 0.9) is the target amount of fine detail and sharpness. `-1`
  turns hff off and lets the model choose. The values are absolute: Steppe Measure HFF on a photo at the target
  resolution gives a value that matches it.
- **guidance**:
  - 1-step models: distilled guidance, trained on 1-3. The default `1` turns it off and is safe and stable; `2` also
    works well. It is a model input, so it costs nothing.
  - Base model: classifier free guidance between `hff` and `negative_hff` (default: no hff). The effect is subtle,
    so use 4-8 for a visible change. Guidance above 1 costs two passes per step.
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
- **Not supported**: the Wan 2.2 5B (TI2V) VAE (48 channels), and FLUX, SD3 and SDXL latents. 16 channel FLUX.1 /
  SD3 latents pass the channel check but give wrong results.

## How it works

[![A generative upscaler in latent space](https://raw.githubusercontent.com/tensorforger/tensorforger/main/assets/steppe/how_it_works.jpg)](https://raw.githubusercontent.com/tensorforger/tensorforger/main/assets/steppe/how_it_works.png)

Latent upscalers made for hires fix only stretch the latent, so the base model has to denoise it again at the high
resolution. Steppe is a generative model itself: a window transformer on the full resolution latent grid generates
the missing detail with rectified flow, distilled to one step. Details on the
[model card](https://huggingface.co/TensorForger/Steppe-Wan2.1#how-it-works).

## Benchmark

[![Benchmark: latency vs patch FID](https://raw.githubusercontent.com/tensorforger/tensorforger/main/assets/steppe/benchmark_plot.jpg)](https://raw.githubusercontent.com/tensorforger/tensorforger/main/assets/steppe/benchmark_plot.png)

1000 photos (Axis-V1), 512 → 1024 from the Wan 2.1 latent only (no prompt), patch FID on native 256 px tiles (lower
is better). Latency at batch 1 on an RTX 5090, VAE decode included.

| solution | patch FID | latency |
|---|---|---|
| Steppe 200M base, 20 steps | **4.31** | 1051 ms |
| Steppe 200M 1-step | 4.36 | 179 ms |
| Steppe 20M 1-step | 5.85 | 141 ms |
| Wan2.1-VAE-upscale2x decoder (spacepxl) | 6.33 | 29 ms |
| SPAN 2x after decode | 11.19 | 35 ms |
| Real-ESRGAN x2 after decode | 13.83 | 57 ms |
| bicubic after decode | 14.13 | 30 ms |
| latent upscalers made for hires fix (SesquiLSR, NN latent) | 29-51 | ~135 ms |

[![Benchmark crops against the ground truth](https://raw.githubusercontent.com/tensorforger/tensorforger/main/assets/steppe/benchmark_gallery.jpg)](https://raw.githubusercontent.com/tensorforger/tensorforger/main/assets/steppe/benchmark_gallery.png)

Benchmark images: [Axis-V1](https://huggingface.co/datasets/refine-axis/axis-v1_1k) by refine-axis (CC BY 4.0),
cropped. Full table with FID, color shift and VRAM:
[model card](https://huggingface.co/TensorForger/Steppe-Wan2.1#benchmark).

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
```

## Related

- [comfyui-flow-upscaler](https://github.com/tensorforger/comfyui-flow-upscaler): the ancestor of Steppe, a FLUX.2
  latent upscaler.
- [LUA: latent upscale adapters](https://arxiv.org/abs/2511.10629): single pass regression upscalers. Steppe is
  generative instead.

## License

MIT (see `LICENSE`). Steppe works on latents of the Wan 2.1 VAE (Apache-2.0, Wan Team, Alibaba Group); see `NOTICE`.
