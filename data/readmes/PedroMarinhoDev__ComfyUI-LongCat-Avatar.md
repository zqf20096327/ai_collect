<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.png">
  <img alt="ComfyUI-LongCat-Avatar: talking video from speech with LongCat-Video-Avatar 1.6, natively in ComfyUI" src="assets/banner-light.png" width="100%">
</picture>

<p align="center">
  <a href="#requirements"><img alt="Tested on ComfyUI 0.44" src="https://img.shields.io/badge/ComfyUI-0.44%20tested-64B5F6?style=flat-square&labelColor=555"></a>
  <a href="#speed-and-memory"><img alt="VRAM: tested on 24 GB" src="https://img.shields.io/badge/VRAM-tested%20on%2024%20GB-64B5F6?style=flat-square&labelColor=555"></a>
  <a href="#quick-start"><img alt="pip install: nothing extra" src="https://img.shields.io/badge/pip%20install-nothing%20extra-64B5F6?style=flat-square&labelColor=555"></a>
  <a href="#license-and-credits"><img alt="Model weights MIT" src="https://img.shields.io/badge/weights-MIT-64B5F6?style=flat-square&labelColor=555"></a>
</p>

<p align="center">
  <a href="#quick-start"><img alt="Get started" src="assets/button-start.svg" height="40"></a>
  <a href="example_workflows"><img alt="Workflow" src="assets/button-workflow.svg" height="40"></a>
  <a href="https://github.com/meituan-longcat/LongCat-Video"><img alt="LongCat-Video by Meituan" src="assets/button-longcat.svg" height="40"></a>
</p>

Run **[LongCat-Video-Avatar 1.6](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.6)** (Meituan LongCat)
**natively in ComfyUI**: audio-driven talking video from a start image, a prompt and speech, continued segment by
segment for as long as the speech lasts. The model is a real `MODEL`: the sampler nodes run ComfyUI's own samplers, guiders and LoRA patches on it, the
stock text encoder, VAE and Whisper loader feed it, and ComfyUI's memory manager streams it.

<p align="center"><img alt="A man in a red jacket sings into a microphone on a smoky stage; his mouth follows the speech across three segments" src="assets/demo.webp" width="576"></p>

<img alt="Two frames of each of the three segments of the same video" src="assets/segments.png" width="100%">

<sub>The distilled node, int8 ConvRot with `--use-ck-attention` on an RTX 4090 · 768×512, 3 segments, 253 frames
(10.1 s) in about 162 s · seed 42 · start image: the release's `man.png` · the animation is scaled to 576×384, without
its sound</sub>

<table>
  <tr>
    <td width="33%" valign="top"><img src="assets/icons/speech.svg" width="24" alt=""><br><b>Talking video from speech</b><br>A prompt and speech, with or without a start image. Whisper large-v3 features at 25 fps, any length of speech.</td>
    <td width="33%" valign="top"><img src="assets/icons/stream.svg" width="24" alt=""><br><b>As long as the speech</b><br>93-frame segments, each continuing from the last 13 frames of the one before, each encoded into the mp4 (NVENC or x264) as soon as it is decoded. Length costs disk, not RAM.</td>
    <td width="33%" valign="top"><img src="assets/icons/steps.svg" width="24" alt=""><br><b>Distilled and base</b><br>The release's 8-step DMD + OPSD LoRA mix at cfg 1, or the base model at 50 steps with its text + audio guidance.</td>
  </tr>
  <tr>
    <td valign="top"><img src="assets/icons/speed.svg" width="24" alt=""><br><b>int8, W6A8, W4A8</b><br>14.9, 12.3 and 8.8 GiB instead of 29.5, in ComfyUI's own quantized formats; LoRAs apply to all of them. int8 with ck attention: 5.1 s per continued step at 768×512.</td>
    <td valign="top"><img src="assets/icons/native.svg" width="24" alt=""><br><b>Native ComfyUI</b><br>ComfyUI's model, samplers, LoRA patches and dynamic VRAM; the base node's guidance is core's Dual CFG guider.</td>
    <td valign="top"><img src="assets/icons/check.svg" width="24" alt=""><br><b>Checked against the release</b><br>The DiT matches the release's to a relative 1e-6 in fp32; with real weights in bf16, cos 0.9997 to 0.9999.</td>
  </tr>
</table>

## Quick start

1. **Install the nodes** and restart ComfyUI. Search for **LongCat Avatar Native** in
   ComfyUI-Manager, or run `comfy node install longcat-avatar-native`, or clone this repository into
   `ComfyUI/custom_nodes`. It needs no packages beyond ComfyUI's own.

2. **Get the files** from Hugging Face,
   [PedroMarinhoDev/LongCat-Video-Avatar-1.6-ComfyUI](https://huggingface.co/PedroMarinhoDev/LongCat-Video-Avatar-1.6-ComfyUI), whose folders mirror `ComfyUI/models`: one transformer
   (see [Which file](#which-file)), the two LoRAs and the Whisper encoder.

   | Folder | File | Size | Source |
   | --- | --- | --- | --- |
   | diffusion_models | [`longcat-video-avatar/longcat_video_avatar_1.6_bf16.safetensors`](https://huggingface.co/PedroMarinhoDev/LongCat-Video-Avatar-1.6-ComfyUI/blob/main/diffusion_models/longcat-video-avatar/longcat_video_avatar_1.6_bf16.safetensors), or a smaller one | 29.5 GiB | `base_model/` |
   | loras | [`longcat-video-avatar/longcat_video_avatar_1.6_dmd_lora_bf16.safetensors`](https://huggingface.co/PedroMarinhoDev/LongCat-Video-Avatar-1.6-ComfyUI/blob/main/loras/longcat-video-avatar/longcat_video_avatar_1.6_dmd_lora_bf16.safetensors) | 1.55 GiB | `loraA/` (DMD) |
   | loras | [`longcat-video-avatar/longcat_video_avatar_1.6_opsd_lora_bf16.safetensors`](https://huggingface.co/PedroMarinhoDev/LongCat-Video-Avatar-1.6-ComfyUI/blob/main/loras/longcat-video-avatar/longcat_video_avatar_1.6_opsd_lora_bf16.safetensors) | 1.55 GiB | `loraB/` (OPSD) |
   | audio_encoders | [`whisper_large_v3_encoder_fp16.safetensors`](https://huggingface.co/PedroMarinhoDev/LongCat-Video-Avatar-1.6-ComfyUI/blob/main/audio_encoders/whisper_large_v3_encoder_fp16.safetensors) | 1.19 GiB | `whisper-large-v3/` (encoder only) |
   | text_encoders | `umt5_xxl_bf16.safetensors` (or any Wan 2.1 UMT5 file) | | identical to Wan 2.1's |
   | vae | `wan_2.1_vae.safetensors` | | identical to Wan 2.1's |

   The text encoder and VAE of LongCat-Video are byte-identical to Wan 2.1's (same sha256 on Hugging Face), so the
   Wan 2.1 files you may already have work. The Source column is the folder of the release
   ([meituan-longcat/LongCat-Video-Avatar-1.6](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.6)) each
   file was made from; to make them yourself, download it and run
   `python custom_nodes/ComfyUI-LongCat-Avatar/tools/convert.py <release folder> ComfyUI/models`.

3. **Open a workflow and run.** Drag [`example_workflows/longcat_avatar_video.json`](example_workflows/longcat_avatar_video.json) into
   ComfyUI, pick your start image and speech, write the prompt and queue. The node makes the whole video and outputs a
   VIDEO for Save Video. Give it clean speech (see [Troubleshooting](#troubleshooting)).

## Which file

Plain round-to-nearest quantized copies, in ComfyUI's native formats through the Comfy Kitchen layouts (no GPTQ).
Download them from [Hugging Face](https://huggingface.co/PedroMarinhoDev/LongCat-Video-Avatar-1.6-ComfyUI) into `ComfyUI/models/diffusion_models/longcat-video-avatar/`, or make them
from the bf16 file:

```bash
python custom_nodes/ComfyUI-LongCat-Avatar/tools/quantize.py <bf16 file> {int8_convrot,w6a8,w4a8}
```

Block linears are in the named format, adaLN modulation layers in int8 ConvRot, and embedders, audio projection and
final layer in bf16. They load with the same node, LoRAs included.

| File | Size | Step (4090, 768x512x93) | Layer output error (random inputs) |
| --- | --- | --- | --- |
| [`..._bf16`](https://huggingface.co/PedroMarinhoDev/LongCat-Video-Avatar-1.6-ComfyUI/blob/main/diffusion_models/longcat-video-avatar/longcat_video_avatar_1.6_bf16.safetensors) | 29.5 GiB | 14.5-15.0 s | - |
| [`..._int8_convrot`](https://huggingface.co/PedroMarinhoDev/LongCat-Video-Avatar-1.6-ComfyUI/blob/main/diffusion_models/longcat-video-avatar/longcat_video_avatar_1.6_int8_convrot.safetensors) | 14.9 GiB | 10.5 s | 1.4% |
| [`..._w6a8`](https://huggingface.co/PedroMarinhoDev/LongCat-Video-Avatar-1.6-ComfyUI/blob/main/diffusion_models/longcat-video-avatar/longcat_video_avatar_1.6_w6a8.safetensors) | 12.3 GiB | 10.6 s | 2.1% |
| [`..._w4a8`](https://huggingface.co/PedroMarinhoDev/LongCat-Video-Avatar-1.6-ComfyUI/blob/main/diffusion_models/longcat-video-avatar/longcat_video_avatar_1.6_w4a8.safetensors) | 8.8 GiB | 10.6 s | 6.4% |

The step times in this table are an earlier measurement, before the clean-frame cache, and their attention backend
was not recorded. The current figure for int8 ConvRot with `--use-ck-attention` is in
[Speed and memory](#speed-and-memory); W6A8 and W4A8 have not been timed that way, and no file's video quality has
been measured against bf16 beyond the layer error above.

## Workflows

Both make the whole video from a start image, a prompt and speech in one node: 93-frame segments (3.7 s at 25 fps),
each continuing from the last 13 frames of the one before, as many as the speech needs, each encoded into the mp4 as
soon as it is decoded (HEVC or H.264 on NVENC, else x264). Only one segment is ever in memory, so the length costs
disk, not RAM.

- [`example_workflows/longcat_avatar_video.json`](example_workflows/longcat_avatar_video.json): **LongCat Avatar Video (distilled, 8
  steps)**, the release's recommended setting.
- [`example_workflows/longcat_avatar_video_base.json`](example_workflows/longcat_avatar_video_base.json): **LongCat Avatar Video
  (base, 50 steps, text + audio guidance)**, the base model alone with a negative prompt. Each step runs the model
  three times and there are 50 of them, so expect it to be many times slower than distilled.

## The nodes

| Node | What it does |
| --- | --- |
| **Load LongCat Avatar Model** | The DiT. |
| **LongCat Avatar Audio Encode** | Whisper large-v3 features at 25 fps, any length (30 s windows, like the release), and `segments`, how many segments cover the speech. Speech that peaks above 0.9 is scaled down to a 0.9 peak (over all channels, before the mono mix and the 16 kHz resample); quieter speech is left as it is. This is what the release's vocal separator does to its output. |
| **LongCat Avatar Video (distilled, 8 steps)** and **LongCat Avatar Video (base, 50 steps, text + audio guidance)** | The whole video; output a VIDEO for Save Video. They share the segment loop and differ only in the guider, conds and sigmas of a segment (see [Sampling](#sampling)). |

The two video nodes' shared inputs:

| Input | |
| --- | --- |
| `start_image` | Optional. Continued segments keep an identity reference: the start image, or without one the first segment's first latent, like the release. |
| `seed` | Segment `n` draws its noise from seed + n. |
| `max_segments` | Stops early. |
| `ref_img_index` | The reference's time position. |
| `encoder` | NVENC or x264. |

## Sampling

**Distilled**: the release's 8 distilled sigmas (flow shift 7) for every segment, euler, cfg 1. The first `mix_steps`
(4) steps use `mix_alpha` DMD + `1 - mix_alpha` OPSD and the rest OPSD alone: the release's `--mix_steps 4
--mix_alpha 1.0`. The two phases are clones of the model with ComfyUI's own LoRA patches, so it equals two chained
samplers bit for bit and costs nothing extra; quantized checkpoints work too.

**Base**: the base model alone, no LoRAs. The first segment uses the release's `steps` (50) sigmas; continued
segments use its `enhance_hf` schedule (the steps above sigma 0.5, then 10 even steps down to 0.05), so they have
fewer steps, and the progress bar counts the real total. Guidance is the release's formula, uncond + text_guidance *
(cond - uncond_text) + audio_guidance * (uncond_text - uncond), with cond = prompt + speech, uncond_text = negative +
speech and uncond = negative + silent speech (both guidances 4 by default). That is core's Dual CFG guider in regular
style (cond1 the prompt, cond2 the negative with speech, negative the negative without), which the node uses. Each
step runs the model on all three conds. For a quick check, `steps` 2 and `max_segments` 2 run the first schedule (2
steps) and the continued one (1 step above 0.5 plus the release's fixed 10) once each: 13 steps in all.

## Speed and memory

RTX 4090, the distilled node (8 steps), int8 ConvRot checkpoint with `--use-ck-attention`:

| Size | First segment | Continued segments | 3 segments | Host RAM |
| --- | --- | --- | --- | --- |
| 768x512 | 5.7 s per step | 5.1 s per step (5.6 without the cache) | about 162 s, 10 s of video | about 6.5 GiB, 4 GiB without the cache |
| 1280x720 | | 20.9 s per step, with or without the cache | | about 8 GiB, 25 GiB with the cache |

- Step 1 of each segment takes about 13.5 s on its own.
- Continued segments compute the conditioning frames once per sampling phase and reuse them. **The cache helps at
  768x512 and not at 1280x720**: there the 13 GB cache pushes the weights out to pinned RAM, and that costs what the
  cache saves.
- The base node does not use the cache. A short check at 768x512 (2 segments, `steps` 4) ran at 17.0 s per step,
  three conds each.
- Dynamic VRAM fills the card in every run, so the VRAM peak (about 24 GB) says nothing about what a run needs.
- bf16 with xformers attention was about 15 s per step at 768x512 and needs about 30 GB of RAM for the streamed DiT
  plus the 11 GB text encoder; that was measured before the cache and not rerun.

## Differences from the release

- No vocal separation: give clean speech. The release separates vocals with an MDX model first; the encode node
  only applies that step's peak limit (audio-separator 0.30.2 `normalize` with `max_peak` 0.9: louder speech is
  scaled down to 0.9, quieter speech is not amplified, since its `min_peak` of -0.9 never triggers). With music
  under the voice (the release's own `man.mp3` example) the mouth stops following the words after about a second;
  with clean speech it tracks them.
- The release resamples Whisper features with the total generation length; here with the audio length plus a 4 s
  silence tail. Frame times differ by under one Whisper frame (20 ms).
- Noise: each segment draws fresh noise from seed + segment; the release continues one generator through all
  segments. The same seed gives a different video than the release's.
- Timestep embedding and modulations run in the model dtype (bf16) instead of the release's fp32 autocast.
- Multi-person (two-speaker) generation and the release's `mask_frame_range` are not ported.

## Troubleshooting

<details>
<summary><b>The mouth stops following the words</b></summary>

There is no vocal separation here (see [Differences from the release](#differences-from-the-release)). With music
under the voice the mouth stops following the words after about a second. Separate the vocals first, with any tool,
and give the node clean speech.
</details>

<details>
<summary><b>Host RAM fills up at 1280x720</b></summary>

At 1280x720 the clean-frame cache takes host RAM to about 25 GiB, against about 8 GiB without it, and gives no speed
there. 768x512 needs about 6.5 GiB. The bf16 DiT streams from system RAM: plan on about 30 GB for it plus the 11 GB
text encoder, or use a quantized file.
</details>

<details>
<summary><b>The base node is slow</b></summary>

Each step runs the model on three conds and there are 50 steps for the first segment; continued segments always
take at least the release's fixed 10-step tail. For a quick check use `steps` 2 and `max_segments` 2 (13 steps).
</details>

## Requirements

| | Tested |
| --- | --- |
| ComfyUI | 0.44.0 |
| GPU | RTX 4090, 24 GB |
| PyTorch | 2.14.1 with CUDA 13.2, Linux |
| Python packages | none beyond ComfyUI's own |

## Verification

- The release's DiT vs the port, random weights, fp32, all three call shapes (audio + text,
  image start, continuation with reference frame): relative error 1e-6.
- Real weights, bf16: release vs port cos 0.9997 (image start) and 0.9999 (continuation),
  the same distance both sit from an fp32 run.
- Whisper features vs the release's HF code; every layer within
  2e-5 in fp32.
- `tests/`: CPU tests of the nodes, the sigma schedules, the video writer and both workflows against the node
  schemas.

## License and credits

The code of this pack is GPL-3.0, like ComfyUI ([LICENSE](LICENSE), [NOTICE](NOTICE)). The model weights are MIT (Meituan; no trademark or patent rights). See the release's model card. The release's code,
[meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video), is MIT too. LongCat-Video-Avatar is
by the Meituan LongCat team ([model](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.6),
[code](https://github.com/meituan-longcat/LongCat-Video),
[tech report](https://github.com/meituan-longcat/LongCat-Video/blob/main/assets/LongCat-Video-Avatar-1.6-Tech-Report.pdf)).
The demo's start image is `assets/avatar/single/man.png` from the release's repository; the video is this pack's own
render.
