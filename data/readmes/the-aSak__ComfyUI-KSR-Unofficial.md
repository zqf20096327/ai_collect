# ComfyUI-KSR-Unofficial

> Unofficial community nodes, not affiliated with Kandinsky Lab.

ComfyUI nodes for [Kandinsky ImageSR 2.0](https://huggingface.co/kandinskylab/Kandinsky-ImageSR-2.0) by Kandinsky Lab,
a 5B one-step diffusion super-resolution model (x2 / x4) without a text encoder.

![512 px input upscaled x4: nearest, bicubic, Kandinsky ImageSR, original](docs/compare_fisherman.jpg)

The transformer is implemented natively on ComfyUI's ops and memory management. It supports partial offloading,
fp8 weights and ComfyUI's attention backends (`--use-sage-attention` etc.), and it uses the regular FLUX.1 VAE through
the core **Load VAE** node. No extra Python packages are needed.

## Installation

```
cd ComfyUI/custom_nodes
git clone https://github.com/the-aSak/ComfyUI-KSR-Unofficial
```
Or install it from ComfyUI-Manager: Search for **KSR-Unofficial**.

## Models

| File | Size | Download | Folder |
|---|---|---|---|
| `kandinsky_imagesr_2.0.safetensors` (transformer, bf16) | ~10.3 GB | [hmdlsk/Kandinsky-ImageSR-2.0-ComfyUI-Unofficial](https://huggingface.co/hmdlsk/Kandinsky-ImageSR-2.0-ComfyUI-Unofficial) | `models/diffusion_models/` |
| FLUX.1 VAE `ae.safetensors` (most FLUX users already have it) | 335 MB | [black-forest-labs/FLUX.1-schnell](https://huggingface.co/black-forest-labs/FLUX.1-schnell) | `models/vae/` |

The VAE that ships with Kandinsky ImageSR **is** the FLUX.1 VAE, stored as bf16. `tools/compare_vae.py` checks this
tensor by tensor.

**Or build the transformer file yourself** from the original release. The script uses only Python's standard library
and copies all tensors byte-for-byte, so the result is identical to the download:

```
hf download kandinskylab/Kandinsky-ImageSR-2.0 --local-dir Kandinsky-ImageSR-2.0 --exclude "assets/*"
python tools/merge_kandinsky_sr.py Kandinsky-ImageSR-2.0 ComfyUI/models/diffusion_models/kandinsky_imagesr_2.0.safetensors --verify
```

## Workflow

`Load Image` → **Kandinsky ImageSR Upscale** ← **Kandinsky ImageSR Model Loader** + `Load VAE` → `Save Image`

Example workflows in `workflows/`:
- `kandinsky_sr_basic.json`: the minimal graph above
- `kandinsky_sr_test_groundtruth.json`: downscales a high-res image to 512² (area filter) and upscales it x4 with
  Kandinsky and with bicubic, so you can compare both against the original

**Kandinsky ImageSR Model Loader**: `weight_dtype` `default` (bf16 as stored) or `fp8_e4m3fn` / `fp8_e5m2`.
Memory: on CUDA the transformer takes ~9.1 GB in bf16. The fp32 modulation layers are stored as bf16, which is exactly
what the reference computes under autocast anyway. fp8 applies only to the attention and feed-forward weights
(7.9 → 3.9 GB, ~5.2 GB in total). It saves memory, not time: the weights are cast back to bf16 for each matmul.

**Kandinsky ImageSR Upscale**

| Input | Meaning |
|---|---|
| `upscale_factor` | 2 or 4 |
| `creativity` | 0–8, calibrated presets. 4 = default (t = 0.15 at x2, 0.244 at x4). Higher values let the model change the input more: depending on content this can add texture (e.g. hatching) or smooth it away (e.g. skin) |
| `overlap` | tile overlap as a fraction of the low-res tile; 0.25 = reference |
| `tile_batch_size` | tiles per transformer pass (slightly faster, more VRAM); the VAE always gets up to 8 tiles per call |

How it works: the image is cut into tiles that become 1024 px at output size. The node then runs three phases
(VAE encode of all tiles → one transformer step per tile → VAE decode with Hanning-window blending), so each model is
loaded only once. The output image is assembled in system RAM. The model is deterministic: no seed, no noise.
Arbitrary `t` values are not possible, because the release only ships conditioning tables for the 18 calibrated
timesteps.

After each run the console logs the total time, the time per phase and the VRAM in use.

## Examples

All examples: a 2048 px image downscaled to 512 px, then upscaled x4 (creativity 4). Crops at full output resolution.

![Macro: dew drops on a leaf](docs/compare_macro.jpg)
![Enamel sign and limestone wall](docs/compare_sign.jpg)
![Text test chart](docs/compare_chart.jpg)
![Technical poster](docs/compare_poster.jpg)

**Text.** On the test chart, text stays correct down to lines that were ~6.5 px high in the 512 px input. Smaller text
turns into plausible-looking but wrong letters, the typical failure of generative upscalers. Don't use it where small
print has to be exact.

**creativity** controls how strongly the model re-synthesizes the input. Higher values stray further from the original; 
whether that adds or removes fine texture seemingly depends on the content:

![creativity 0 / 4 / 8 vs. original](docs/creativity_poster.jpg)

## Performance

RTX 4070 Ti SUPER 16 GB, 32 GB RAM, Windows, ComfyUI portable (0.45.0), x4, creativity 4, `tile_batch_size` 1.

| Weights | Input → output | Tiles | Time | VRAM (whole device, Task Manager) |
|---|---|---|---|---|
| bf16 | 512² → 2048² | 9 | 13.0 s (model not yet on GPU) | – |
| bf16 | 2048² → 8192² | 121 | 158 s (encode 28 / transformer 91 / decode 39) | ~14.85 GB peak |
| fp8 | 2048² → 8192² | 121 | 159 s | ~13.5 GB peak |

ComfyUI keeps models and cache in VRAM when it can, so the device-wide figure is an upper bound, not a requirement.
Timings were taken before the VAE batching was added; encode/decode should now be somewhat faster.

## Accuracy

- **Native vs. original pipeline, real weights:** the test chart upscaled x4 by these nodes and by the original
  Diffusers pipeline differs by 50.5 dB PSNR (mean 0.23/255); both score identically against the ground truth.
- **fp8 vs. bf16:** 46.5 dB PSNR on the 8192² test chart output.
- **Against bicubic:** pixel metrics (PSNR/SSIM) against the original usually favour bicubic on photos, because
  invented detail is penalised more than blur. This is the known perception–distortion trade-off (Blau & Michaeli,
  CVPR 2018). Judge the crops above, not the numbers.

## Known issues

- **Grid pattern on skin in AI-generated images.** Upscaling already high-res AI images (especially from SDE samplers such as er_sde) can turn their faint latent-grid texture into a visible cross-hatch pattern. It does not appear on real photos. Lower creativity, possibly a slight blur before upscaling (e.g. ImageBlur radius 1, sigma 0.5–0.8), or downscaling first can reduce it.

## Credits & license

- Model, original pipeline and tiling code: [Kandinsky Lab](https://huggingface.co/kandinskylab), MIT
- Kandinsky 5 building blocks in Diffusers: Hugging Face, Apache-2.0 (basis of `native/model.py`)
- VAE (not included): [FLUX.1-schnell](https://huggingface.co/black-forest-labs/FLUX.1-schnell) by Black Forest Labs, Apache-2.0
- Example images: generated with Krea 2 Raw (bf16) + Turbo LoRA, 7 steps, ~4 MP native; test chart: own work, text from Kafka, *Die Verwandlung* (1915, public domain)
- This node pack: MIT, © 2026 the-aSak. Developed with Claude by Anthropic. 

All third-party code and every change made to it are listed in [`NOTICE.md`](NOTICE.md).
