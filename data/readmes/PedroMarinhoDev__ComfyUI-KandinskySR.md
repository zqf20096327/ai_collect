<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.png">
  <img src="assets/banner-light.png" alt="Kandinsky SR for ComfyUI: a face split by a vertical line, the source on the left and the x4 upscale on the right, with a loupe on the iris." width="100%">
</picture>

**ComfyUI-KandinskySR** runs kandinskylab's Kandinsky 6.0 Video Super-Resolution 2.0 and Kandinsky ImageSR 2.0
natively in ComfyUI.

- **The picture.** A small, soft source becomes a large, detailed one, and it stays the same picture: video in
  2 steps per tile, images in 1.
- **Fast, and it fits.** Own attention, norm and decode kernels, int8 files and an optional second GPU. 15 s of
  960x540 video to 1080p takes 3.9 min on an RTX 4090 in 10.5 GB (int8, `stitch` latent). Images run twice as
  fast as the reference.
- **Any length.** Long clips run in overlapping windows; memory does not grow with the clip.

`video x2 · x2.25 · x4` &nbsp; `images x2 · x4`

<a href="https://huggingface.co/PedroMarinhoDev/Kandinsky-SR-ComfyUI/resolve/main/assets/video/kandinsky_sr_promo.mp4"><img src="assets/film/promo.webp" alt="The Kandinsky SR promo film: a loupe moves over a picture, showing the source and then the x4 upscale." width="100%"></a>

<sub>▶ LOOP · 4.5 s · [the whole film with sound ↗](https://huggingface.co/PedroMarinhoDev/Kandinsky-SR-ComfyUI/resolve/main/assets/video/kandinsky_sr_promo.mp4)</sub>

## Video

<a href="https://huggingface.co/PedroMarinhoDev/Kandinsky-SR-ComfyUI/resolve/main/assets/video/nice_compare.mp4"><img src="assets/clips/nice.webp" alt="A man eats a crumb, then speaks to the camera. Left: the source; right: Kandinsky SR x4." width="100%"></a>
<sub>▶ LOOP · 3.7 s · [full clip with sound ↗](https://huggingface.co/PedroMarinhoDev/Kandinsky-SR-ComfyUI/resolve/main/assets/video/nice_compare.mp4)</sub>

<sub>480x270 → 1920x1080 (x4), 25 fps, 100 frames · `kandinsky6_vsr_2.0_distilled2steps_bf16`, `fast`, `stitch` pixels, seed 42 · 69.1 s on an RTX 4090 + RTX 3090 (`second_gpu`) · the same 800x900 crop of both (the face).</sub>

<a href="https://huggingface.co/PedroMarinhoDev/Kandinsky-SR-ComfyUI/resolve/main/assets/video/stage_compare.mp4"><img src="assets/clips/stage.webp" alt="A performer with a microphone in front of a blue backdrop. Left: the source; right: Kandinsky SR x4." width="100%"></a>
<sub>▶ LOOP · 3.5 s · [full clip with sound ↗](https://huggingface.co/PedroMarinhoDev/Kandinsky-SR-ComfyUI/resolve/main/assets/video/stage_compare.mp4)</sub>

<sub>360x360 → 1440x1440 (x4), 30 fps, 180 frames · `kandinsky6_vsr_2.0_distilled2steps_bf16`, `fast`, `stitch` pixels, seed 42 · 133.2 s on an RTX 4090 + RTX 3090 (`second_gpu`) · the whole frame.</sub>

<a href="https://huggingface.co/PedroMarinhoDev/Kandinsky-SR-ComfyUI/resolve/main/assets/video/rollsafe_compare.mp4"><img src="assets/clips/rollsafe.webp" alt="A man thinks, then taps a finger to the temple. Left: the source; right: Kandinsky SR x4." width="100%"></a>
<sub>▶ LOOP · 3.0 s · [full clip with sound ↗](https://huggingface.co/PedroMarinhoDev/Kandinsky-SR-ComfyUI/resolve/main/assets/video/rollsafe_compare.mp4)</sub>

<sub>640x360 → 2560x1440 (x4), 30 fps, 409 frames · `kandinsky6_vsr_2.0_distilled2steps_bf16`, `fast`, `stitch` pixels, seed 42 · 658.3 s on an RTX 4090 + RTX 3090 (`second_gpu`) · the same 680x760 crop of both (the face and hand).</sub>

For the comparison the source is enlarged with bicubic to the output size. Every source frame is kept: the clips go into the node as frames (its `images` input), since its video input thins sources above 24 fps to 24 fps.

## Images

In every comparison below, the source is enlarged with bicubic to the output size.

<img src="assets/cards/dress.webp" alt="A woman in a green sequin dress on a teal backdrop. Left: the whole upscale; right: the face, the source and Kandinsky SR." width="100%">

<sub>800x1200 → 3200x4800 (x4) · `kandinsky_image_sr_2.0_bf16`, creativity 4, `fast` · 15.1 s on an RTX 4090 · the square: the face, 285x380 output pixels, shown at 2x (1:1 at the column's width)</sub>

<img src="assets/cards/knit.webp" alt="A woman with wavy hair and wire glasses in a ribbed camel sweater, chin on hand. Left: the whole upscale; right: the sweater's stitches, the source and Kandinsky SR." width="100%">

<sub>1080x1480 → 4320x5920 (x4) · `kandinsky_image_sr_2.0_bf16`, creativity 4, `fast` · 29.6 s on an RTX 4090 · the square: the sweater's stitches, 273x380 output pixels, shown at 2x (1:1 at the column's width)</sub>

<img src="assets/cards/perfume.webp" alt="A perfume bottle lying on moss, its label reading Forest Essence, Elixir. Left: the whole upscale; right: the label's small print, the source and Kandinsky SR." width="100%">

<sub>1024x768 → 4096x3072 (x4) · `kandinsky_image_sr_2.0_bf16`, creativity 4, `fast` · 12.8 s on an RTX 4090 · the square: the label's small print, 416x200 output pixels, shown at 2x (1:1 at the column's width)</sub>

<img src="assets/cards/freckles.webp" alt="A close-up of a young woman's face, half in shadow, freckles and green eyes. Left: the whole upscale; right: the lower lashes and skin, the source and Kandinsky SR." width="100%">

<sub>896x1200 → 3584x4800 (x4) · `kandinsky_image_sr_2.0_bf16`, creativity 4, `fast` · 18.1 s on an RTX 4090 · the square: the lower lashes and skin, 270x380 output pixels, shown at 2x (1:1 at the column's width)</sub>

<p>
<a href="https://huggingface.co/PedroMarinhoDev/Kandinsky-SR-ComfyUI/resolve/main/assets/showcase/pool.jpg"><img src="assets/splits/pool.webp" alt="A young man with glasses lines up a pool shot under warm lamps. Left half: the source; right half: Kandinsky SR, the glasses." width="50.42%"></a><a href="https://huggingface.co/PedroMarinhoDev/Kandinsky-SR-ComfyUI/resolve/main/assets/showcase/cereal.jpg"><img src="assets/splits/cereal.webp" alt="A blue bowl of cornflakes with raspberries and blueberries, milk splashing, honey dripping from a dipper. Left half: the source; right half: Kandinsky SR, a raspberry among the flakes." width="49.47%"></a><br>
<a href="https://huggingface.co/PedroMarinhoDev/Kandinsky-SR-ComfyUI/resolve/main/assets/showcase/wall.jpg"><img src="assets/splits/wall.webp" alt="A man in a linen shirt leans on a sunlit plaster wall, holding a daisy. Left half: the source; right half: Kandinsky SR, the face." width="50.42%"></a><a href="https://huggingface.co/PedroMarinhoDev/Kandinsky-SR-ComfyUI/resolve/main/assets/showcase/penguin.jpg"><img src="assets/splits/penguin.webp" alt="A man in a parka and knit hat sits in the snow beside penguins. Left half: the source; right half: Kandinsky SR, a penguin's feathers." width="49.47%"></a><br>
<a href="https://huggingface.co/PedroMarinhoDev/Kandinsky-SR-ComfyUI/resolve/main/assets/showcase/painting.jpg"><img src="assets/splits/painting.webp" alt="An oil painting of a thawing town at sunset, a church spire, crows and snowdrops by a pool of meltwater. Left half: the source; right half: Kandinsky SR, the church spire." width="50.42%"></a><a href="https://huggingface.co/PedroMarinhoDev/Kandinsky-SR-ComfyUI/resolve/main/assets/showcase/field.jpg"><img src="assets/splits/field.webp" alt="A woman in a grey hanbok holds a bouquet in a field of wildflowers below a mountain. Left half: the source; right half: Kandinsky SR, the face." width="49.47%"></a><br>
<a href="https://huggingface.co/PedroMarinhoDev/Kandinsky-SR-ComfyUI/resolve/main/assets/showcase/sunset.jpg"><img src="assets/splits/sunset.webp" alt="A woman at a wooden railing at sunset with a folding bike and a ginger cat, a tower on the hill behind. Left half: the source; right half: Kandinsky SR, the cat's fur." width="50.42%"></a><a href="https://huggingface.co/PedroMarinhoDev/Kandinsky-SR-ComfyUI/resolve/main/assets/showcase/hiker.jpg"><img src="assets/splits/hiker.webp" alt="A smiling hiker with poles on a rocky ridge above green hills. Left half: the source; right half: Kandinsky SR, the plaid shirt." width="49.47%"></a><br>
<a href="https://huggingface.co/PedroMarinhoDev/Kandinsky-SR-ComfyUI/resolve/main/assets/showcase/map.jpg"><img src="assets/splits/map.webp" alt="A rider on a scooter above a 3D city map, tiny cars and the Statue of Liberty below. Left half: the source; right half: Kandinsky SR, the miniature cars." width="50.42%"></a><a href="https://huggingface.co/PedroMarinhoDev/Kandinsky-SR-ComfyUI/resolve/main/assets/showcase/mural.jpg"><img src="assets/splits/mural.webp" alt="Miniature figures painting a beach mural that reads No one can come close. Left half: the source; right half: Kandinsky SR, the lettering." width="49.47%"></a>
</p>

Each tile: one region at 1:1 output pixels (2x in the file), the source left of the line, Kandinsky SR right of it, the whole picture top right. Every picture here is the Image SR node's output at its defaults (`kandinsky_image_sr_2.0_bf16`, creativity 4, `fast`), untouched; 9-30 s each on an RTX 4090. The picture of the hiker, already 1887x1887, is x2; the rest x4. Click a tile for the full-size output (JPEG, quality 95).

## Install

- **ComfyUI Manager:** search for "Kandinsky SR".
- **Comfy CLI:** `comfy node install kandinsky-sr-native`
- **git:** `git clone https://github.com/PedroMarinhoDev/ComfyUI-KandinskySR` in `ComfyUI/custom_nodes`.

There is nothing to `pip install`; restart ComfyUI afterwards.

## Model files

All on [PedroMarinhoDev/Kandinsky-SR-ComfyUI](https://huggingface.co/PedroMarinhoDev/Kandinsky-SR-ComfyUI), laid out
like ComfyUI's `models` folder, so one command puts every file in place:

```bash
cd ComfyUI/models
hf download PedroMarinhoDev/Kandinsky-SR-ComfyUI --local-dir . --include "*.safetensors"
```

Video needs one transformer, the KVAE and the upscaler for your scale; images need one image transformer and the
FLUX.1 VAE (`ae.safetensors`, which most ComfyUI installs already have).

<details>
<summary>Every file, its size and folder</summary>

| File | Size | Folder | Needed for |
|---|---|---|---|
| [kandinsky6_vsr_2.0_distilled2steps_bf16](https://huggingface.co/PedroMarinhoDev/Kandinsky-SR-ComfyUI/blob/main/diffusion_models/kandinsky-sr/kandinsky6_vsr_2.0_distilled2steps_bf16.safetensors) | 3.19 GB | `diffusion_models/kandinsky-sr/` | video (one of the two) |
| [kandinsky6_vsr_2.0_distilled2steps_int8_convrot](https://huggingface.co/PedroMarinhoDev/Kandinsky-SR-ComfyUI/blob/main/diffusion_models/kandinsky-sr/kandinsky6_vsr_2.0_distilled2steps_int8_convrot.safetensors) | 1.96 GB | `diffusion_models/kandinsky-sr/` | video (one of the two) |
| [kandinsky_kvae_3d_2.0_t4s16_bf16](https://huggingface.co/PedroMarinhoDev/Kandinsky-SR-ComfyUI/blob/main/vae/kandinsky-sr/kandinsky_kvae_3d_2.0_t4s16_bf16.safetensors) | 3.48 GB | `vae/kandinsky-sr/` | video |
| [kandinsky6_sr_latent_upscaler_x2_bf16](https://huggingface.co/PedroMarinhoDev/Kandinsky-SR-ComfyUI/blob/main/latent_upscale_models/kandinsky-sr/kandinsky6_sr_latent_upscaler_x2_bf16.safetensors) | 1.53 GB | `latent_upscale_models/kandinsky-sr/` | video x2 and x2.25 |
| [kandinsky6_sr_latent_upscaler_x4_bf16](https://huggingface.co/PedroMarinhoDev/Kandinsky-SR-ComfyUI/blob/main/latent_upscale_models/kandinsky-sr/kandinsky6_sr_latent_upscaler_x4_bf16.safetensors) | 2.89 GB | `latent_upscale_models/kandinsky-sr/` | video x4 |
| [kandinsky_image_sr_2.0_bf16](https://huggingface.co/PedroMarinhoDev/Kandinsky-SR-ComfyUI/blob/main/diffusion_models/kandinsky-sr/kandinsky_image_sr_2.0_bf16.safetensors) | 9.06 GB | `diffusion_models/kandinsky-sr/` | images (one of the two) |
| [kandinsky_image_sr_2.0_int8_convrot](https://huggingface.co/PedroMarinhoDev/Kandinsky-SR-ComfyUI/blob/main/diffusion_models/kandinsky-sr/kandinsky_image_sr_2.0_int8_convrot.safetensors) | 5.14 GB | `diffusion_models/kandinsky-sr/` | images (one of the two) |
| [ae](https://huggingface.co/black-forest-labs/FLUX.1-schnell/blob/main/ae.safetensors) (FLUX.1 VAE) | 0.34 GB | `vae/` | images |

The files are the released weights repackaged into single safetensors files with their settings in the metadata,
plus int8 ConvRot variants of the two transformers. The converters are in [`tools/`](tools/).

</details>

## Workflows

[`example_workflows/`](example_workflows/) has one workflow for video and one for images; they also show up in
ComfyUI's template browser. Point their Load Video / Load Image nodes at your own files.

## Nodes and inputs

Video runs a 2-step pi-Flow distilled diffusion transformer with NABLA sparse attention, the KVAE 3D video VAE and
latent upscalers; clips are cut into overlapping tiles, upscaled and blended back. Images run a one-step transformer
on the FLUX.1 VAE, tiled the same way. Both are ComfyUI models on ComfyUI's own memory management, with no vendored
runtime. Four nodes under **Kandinsky SR**:

- **Load Kandinsky Video SR Models:** the transformer (`bf16` or `int8_convrot`), the KVAE and the two latent
  upscalers. `second_gpu` (advanced) gives a second card its own copy of the transformer and the KVAE; each card then
  takes the next tile when it is free.
- **Kandinsky Video SR Upscale:** a video (or images) in, a video file out, with the source's audio and frame rate.
  Sources faster than 24 fps are thinned to 24 fps, as in the reference.
- **Load Kandinsky Image SR Model:** the image transformer (`bf16` or `int8_convrot`). The VAE is the stock FLUX.1
  VAE from ComfyUI's own **Load VAE** node.
- **Kandinsky Image SR Upscale:** `scale` 2x or 4x, `creativity` 0-8 (how much detail the model invents; 4 is the
  release default), `kernels` fast or exact, `tile_batch_size` (advanced).

<details>
<summary>Kandinsky Video SR Upscale inputs</summary>

| Input | Default | What it does |
|---|---|---|
| `scale` | 2x | 2x, 2.25x (a 1.125x pre-upscale, then 2x) or 4x |
| `seed` | 42 | start noise; the same seed gives the same frames on any card |
| `kernels` | fast | `fast`: custom attention, norm and decode kernels (CUDA with Triton). `exact`: the reference's arithmetic |
| `stitch` | pixels | `pixels`: decode every tile and blend the frames, as the reference does. `latent`: blend the tiles' latents and decode each frame once: faster, a little sharper where tiles overlap |
| `window_frames` | 361 | the longest stretch the model sees at once; longer clips run in overlapping windows (see [Long clips](#long-clips)). Lower it to use less VRAM |
| `overlap` | 0.2 | least overlap between neighbouring tiles |
| `encoder` | auto | NVENC HEVC / H.264 or x264 for the output file |
| `fps` | 24 | frame rate of an `images` input |

</details>

## Speed

The variants below ran on the same input and differ only in `kernels`, `stitch` and the transformer file's precision. At 1:1 they look alike, with the small differences named under each picture; they differ in time and memory.

<img src="assets/cards/methods_image.webp" alt="The same detail from each image variant: exact bf16, fast bf16, exact int8, fast int8." width="100%">

<sub>The face close-up x4: the same region of the iris, 204x280 output pixels at 2x (1:1 at the column's width), one variant per column with its seconds and peak VRAM (the process's peak in nvidia-smi) on an RTX 4090 alone. PSNR against fast bf16: exact bf16 52.98 dB; exact int8 49.10 dB; fast int8 49.48 dB. Enlarged, the int8 panes differ from the default in a few pixels of the catchlights (at most 44 of 255).</sub>

<img src="assets/cards/methods_video.webp" alt="The same detail from each video variant: exact bf16 pixels, fast bf16 pixels, fast bf16 latent, fast int8 pixels, fast int8 latent." width="100%">

<sub>The clip x4, frame 75: the same region of the eye, 161x280 output pixels at 2x (1:1 at the column's width), one variant per column with its seconds and peak VRAM (torch's peak allocation) on an RTX 4090 alone. PSNR against fast bf16 pixels: exact bf16 pixels 47.56 dB; fast bf16 latent 46.33 dB; fast int8 pixels 47.59 dB; fast int8 latent 46.18 dB. Enlarged, the two `latent` panes have slightly softer catchlights and iris edge (at most 37 of 255); the rest differ by about 1 of 255 on average.</sub>

Through the nodes on a warm ComfyUI server (0.44), input to finished file, on an RTX 4090 and an RTX 3090.
"Reference" is kandinskylab's own code on the same card.

| Job | Card | Reference | This pack | Peak VRAM |
|---|---|---|---|---|
| Video, 5 s, 768x512 → 1536x1024 | 4090 | 241 s | 95 s (`fast`), 71 s (+ `stitch` latent) | |
| Video, 15 s, 960x540 → 1920x1080 | 4090 | | 4.8 min; 3.9 min (int8 + `stitch` latent) | 13.3 GB; 10.5 GB |
| Image, 1024x1024 x4, int8 | 4090 | 18.3 s | 9.2 s | 7.2 GB |

<details>
<summary>All measurements</summary>

**Video, 15 s (361 frames):**

| Output | Cards | Settings | Time | Peak VRAM |
|---|---|---|---|---|
| 960x540 → 1920x1080 | 4090 | defaults | 4.8 min | 13.3 GB |
| 960x540 → 1920x1080 | 4090 | int8 + `stitch` latent | 3.9 min | 10.5 GB |
| 960x540 → 1920x1080 | 4090 + 3090 | defaults | 4.0 min | 13.3 GB |
| 1920x1080 → 3840x2160 | 4090 + 3090 | `stitch` latent | 15.7 min | 17.3 GB |

**Video, 5 s (121 frames, 768x512 → 1536x1024), RTX 4090:**

| | Time |
|---|---|
| Reference (its uncompiled decoder) | 241 s |
| `exact` | 189 s |
| `fast` (default) | 95 s |
| `fast` + `stitch` latent | 71 s |

`exact` stays as close to the reference's frames as the reference is to itself between its compiled and uncompiled
runs (54.5 dB); `fast` is 53.5 dB from the reference. The fast decode works in float16 where the reference uses
bfloat16, and is the closer of the two to a float32 decode.

**Images, RTX 4090, int8 file with `fast`:**

| | Reference | This pack | Peak VRAM |
|---|---|---|---|
| 1024x1024 x2 | 6.6 s | 3.4 s | 7.0 GB |
| 1024x1024 x4 | 18.3 s | 9.2 s | 7.2 GB |
| 640x424 x4 | 4.4 s | 2.3 s | 7.0 GB |

</details>

The bf16 image file takes about 40% longer and 12 GB. The fast kernels need an NVIDIA card (RTX 30 series or newer)
with Triton; without them the nodes run the plain paths, which are much slower for video.

## Long clips

There is no length limit. A clip longer than `window_frames` (361 frames, 15 s at 24 fps) runs as overlapping
windows: each goes through the whole pipeline, neighbours share 9 frames, and those are cross-faded. Frames are read
and written a window at a time, so memory does not grow with the clip.

Where two windows meet, detail softens slightly for about a third of a second, because the two windows render the
shared frames a little differently. Smaller windows (for example 121) use much less VRAM and are faster per frame,
with more joins.

## Differences from the reference

- The start noise is drawn on the CPU, so a seed gives the same result on every card (the reference draws it on the
  GPU, where it depends on the card model).
- The reference darkens a few pixels in each corner of every frame (a clamp in its tile blend); this pack does not.
- A clip that is not 1 + 8k frames long is padded instead of cut, so no input frame is dropped.
- Clips longer than 15 s, the `latent` stitch, a second card and the int8 files are additions.

## License and credits

The nodes are under the GNU GPL v3 ([LICENSE](LICENSE)), like ComfyUI, whose code they import. The model code
follows kandinskylab's releases, under the MIT License ([LICENSE-MIT](LICENSE-MIT)); [NOTICE](NOTICE) lists which
files are adapted from where.

- Kandinsky 6.0 VSR: [kandinskylab/kandinsky-video-sr](https://github.com/kandinskylab/kandinsky-video-sr),
  [weights](https://huggingface.co/kandinskylab/Kandinsky-6.0-VSR-2.0-distilled2steps-Diffusers) (MIT)
- Kandinsky ImageSR: [kandinskylab/kandinsky-image-sr](https://github.com/kandinskylab/kandinsky-image-sr),
  [weights](https://huggingface.co/kandinskylab/Kandinsky-ImageSR-2.0) (MIT)
- FLUX.1 VAE: [black-forest-labs/FLUX.1-schnell](https://huggingface.co/black-forest-labs/FLUX.1-schnell) (Apache-2.0)

This project is not affiliated with kandinskylab.
