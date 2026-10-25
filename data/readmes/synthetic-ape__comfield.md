<div align="center">

<img src="web/public/favicon.svg" width="72" alt="" />

# Comfield

**An open-source, Higgsfield-style creative studio for AI images and video, built on the Comfy Developer Platform.**

Write a prompt, pick a model, choose a camera move, get takes back. Run frontier models through **Comfy Router**, or open-weights models **on your own GPU**, from one interface.

[![License: MIT](https://img.shields.io/badge/license-MIT-f0ff41?style=flat-square)](LICENSE)
[![Node 22.12+](https://img.shields.io/badge/node-22.12%2B-cfc6f2?style=flat-square)](https://nodejs.org)
[![Built on Comfy](https://img.shields.io/badge/built%20on-Comfy%20Developer%20Platform-211927?style=flat-square)](https://docs.comfy.org/development/overview)

Built for the [Open Source Higgsfield](https://comfy.org/open-source-higgsfield) challenge.

</div>

![Comfield image studio](docs/screenshots/image-studio.png)

## Contents

- [What it does](#what-it-does)
- [Example outputs](#example-outputs)
- [Quick start](#quick-start)
- [Installation in detail](#installation-in-detail)
- [Using Comfield](#using-comfield)
- [Downloading models](#downloading-models)
- [Models and capabilities](#models-and-capabilities)
- [How it works](#how-it-works)
- [Configuration](#configuration)
- [Development](#development)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)
- [License and credits](#license-and-credits)

## What it does

| | |
| --- | --- |
| **Image studio** | Text-to-image and image editing with up to 10 reference images. 2 open-weights models on your GPU plus 9 cloud models (FLUX 3, Nano Banana Pro and 2.1, Seedream 5.0 Pro and Flash, GPT Image 2, Qwen Image 3.0, Kling Image O1, Grok Imagine 2.0). |
| **Video studio** | Text-to-video, image-to-video and first-to-last-frame video, most with synchronized sound. 3 open-weights models (LTX-2, MiniMax H3, FastH3) plus 10 cloud models (Seedance 2.5, Kling 3.0 Omni, Veo 3.1 and 3.1 Fast, MiniMax H3, LTX 2.5 Pro and Fast, FLUX 3 Video, Wan 3.0, Grok Imagine Video 1.5). |
| **27 camera motions** | Dolly, crash zoom, dolly zoom, orbit, 360 orbit, bullet time, crane, tilt, pan, truck, whip pan, FPV drone, aerial reveal, snorricam and more. Each one previews live in a tiny viewfinder; Veo and Kling also get their native camera controls. |
| **Direct the shot** | Film-set controls for shot size, angle, lens, depth of field and lighting, plus 14 visual styles. |
| **Shots and takes** | Every generation is a shot with up to 4 takes (A, B, C, D), live progress, queue position and step-by-step progress for local runs. |
| **Animate anything** | One click turns any image into the first frame of a video. Drag any take onto a frame or reference slot to reuse it. |
| **Prompt enhancer** | Turns a short idea into a detailed prompt (Claude, through Comfy Router). |
| **Live pricing** | See what a cloud generation costs before you press Generate. |
| **Library** | Everything is downloaded to your machine the moment it's ready, then searchable with favorites. |
| **Models page** | Every open model in ComfyUI's template library (about 75 families) sorted into image, video, audio, 3D, text and tools. See at a glance what's downloaded and what's ready in Comfield, and download any model into ComfyUI with progress, cancel, resume and a free-space check. |
| **Built-in guide** | The gear menu has a full "How to use" guide, keyboard shortcuts and links. |

<table>
<tr>
<td width="50%"><img src="docs/screenshots/video-studio.png" alt="Video studio with camera motion presets" /><br /><sub>Video studio: frames, camera motions, takes</sub></td>
<td width="50%"><img src="docs/screenshots/model-picker.png" alt="Model picker, open weights first" /><br /><sub>Model picker: open weights first, then cloud</sub></td>
</tr>
<tr>
<td><img src="docs/screenshots/viewer.png" alt="Viewer with Animate" /><br /><sub>Viewer: animate, reuse, download</sub></td>
<td><img src="docs/screenshots/library.png" alt="Library" /><br /><sub>Library of every take</sub></td>
</tr>
<tr>
<td><img src="docs/screenshots/models.png" alt="Models page" /><br /><sub>Models page: every open model, by type, with what's ready</sub></td>
<td><img src="docs/screenshots/models-detail.png" alt="Model details with files and downloads" /><br /><sub>Model details: workflows, files, sizes, one-click download</sub></td>
</tr>
<tr>
<td><img src="docs/screenshots/guide.png" alt="Built-in guide" /><br /><sub>Built-in "How to use" guide</sub></td>
<td><img src="docs/screenshots/settings.png" alt="Settings" /><br /><sub>Settings: API key, GPU and engine status</sub></td>
</tr>
</table>

## Example outputs

All of these were generated with Comfield's open-weights models on one RTX 4070 Ti SUPER (16 GB), with no cloud credits.

| Z-Image Turbo (Neon Noir style) | Z-Image Turbo | Qwen Image Edit: "change his suit to a red velvet tuxedo" |
| --- | --- | --- |
| <img src="docs/examples/z-image-astronaut.jpg" width="260" /> | <img src="docs/examples/z-image-saxophonist.jpg" width="260" /> | <img src="docs/examples/qwen-edit-tuxedo.jpg" width="260" /> |

| LTX-2 text-to-video, 3 s with sound (orbit motion) | FastH3 image-to-video from the portrait above (dolly in), 35 s render |
| --- | --- |
| <img src="docs/examples/ltx2-fox.gif" width="420" /> | <img src="docs/examples/fasth3-animate.gif" width="300" /> |

<sub>GIFs are silent previews. The real MP4s include the generated soundtrack.</sub>

## Quick start

You need [Node.js 22.12 or newer](https://nodejs.org). For local models you also need [Comfy Desktop](https://www.comfy.org/download) (or ComfyUI) and Python 3.10+.

```bash
git clone https://github.com/synthetic-ape/comfield.git
cd comfield
npm install
npm start
```

`npm start` builds the interface, starts the server and opens **http://localhost:5177**.

No terminal? Double-click **`start-comfield.bat`** on Windows, or run **`./start-comfield.sh`** on macOS or Linux. It installs everything on first run.

Then connect at least one engine. The app walks you through it on first launch:

- **Cloud models:** paste a Comfy API key in Settings.
- **Your GPU:** open Comfy Desktop and run `npm run setup:local` once.

## Installation in detail

### 1. Get Comfield running

```bash
git clone https://github.com/synthetic-ape/comfield.git   # or download the ZIP from GitHub
cd comfield
npm install
npm start
```

Comfield runs entirely on your computer. Its web server listens on `127.0.0.1:5177` (localhost only) and keeps your settings, history and files in the `data/` folder.

### 2a. Cloud models (Comfy Router)

1. Sign in at [platform.comfy.org](https://platform.comfy.org), create an API key under **[API keys](https://platform.comfy.org/profile/api-keys)**, and add credits to your workspace.
2. In Comfield open **⚙ → Settings → Cloud models** and paste the key. You can also put `COMFY_API_KEY=comfyui-…` in a `.env` file next to `package.json` (see [`.env.example`](.env.example)).

The key stays on your machine (in `data/settings.json`) and is only sent from the Comfield server to `api.comfy.org`; the browser never sees it.

### 2b. Open-weights models on your GPU

1. **Install and open [Comfy Desktop](https://www.comfy.org/download)** (or run ComfyUI yourself). Comfield finds it on `http://127.0.0.1:8188`, falls back to port `8000`, and you can set any address in Settings.
2. **Install the Comfy API proxy once:**
   ```bash
   npm run setup:local
   ```
   This creates a private Python environment in `.venv/` and installs [`comfy-api-proxy`](https://github.com/Comfy-Org/comfy-api-proxy), the official service that serves the Comfy API v2 in front of your ComfyUI. Comfield starts and stops it for you.
3. **Download the model files.** The easy way: open the **Models** page in Comfield, click the model, and press **Download**. Comfield fetches the exact files into ComfyUI's `models/` folders (the shared models folder, with Comfy Desktop) and shows progress. The model picker also links straight there when files are missing. To download by hand instead, here is the full list:

| Model | Folder in `ComfyUI/models/` | File | Size |
| --- | --- | --- | --- |
| Z-Image Turbo | `diffusion_models/` | [z_image_turbo_bf16.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/diffusion_models/z_image_turbo_bf16.safetensors) | 12.3 GB |
| | `text_encoders/` | [qwen_3_4b.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) | 8.0 GB |
| | `vae/` | [ae.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) | 0.3 GB |
| Qwen Image Edit | `diffusion_models/` | [qwen_image_edit_2511_fp8mixed.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_edit_2511_fp8mixed.safetensors) | 20.5 GB |
| | `text_encoders/` | [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) | 9.4 GB |
| | `vae/` | [qwen_image_vae.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) | 0.3 GB |
| | `loras/` | [Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors](https://huggingface.co/lightx2v/Qwen-Image-Edit-2511-Lightning/resolve/main/Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors) | 0.8 GB |
| LTX-2 | `checkpoints/` | [ltx-2-19b-dev.safetensors](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-19b-dev.safetensors) | 43.3 GB |
| | `loras/` | [ltx-2-19b-distilled-lora-384.safetensors](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-19b-distilled-lora-384.safetensors) | 7.7 GB |
| | `latent_upscale_models/` | [ltx-2-spatial-upscaler-x2-1.0.safetensors](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-spatial-upscaler-x2-1.0.safetensors) | 1.0 GB |
| | `text_encoders/` | [gemma_3_12B_it.safetensors](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/text_encoders/gemma_3_12B_it.safetensors) | 24.4 GB |
| MiniMax H3 Open | `diffusion_models/` | [minimax_h3_fl2va_pruned_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors) | 21.0 GB |
| | `loras/` | [minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors](https://huggingface.co/lightx2v/Minimax-h3-Turbo/resolve/main/minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors) | 2.0 GB |
| MiniMax H3 Open and FastH3 | `text_encoders/` | [qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) | 15.7 GB |
| | `vae/` | [minimax_h3_video_vae_fp16.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_video_vae_fp16.safetensors) | 5.2 GB |
| | `vae/` | [minimax_h3_audio_vae_fp32.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_audio_vae_fp32.safetensors) | 0.6 GB |
| FastH3 | `diffusion_models/` | [fastvideo_fasth3_8step_v2_pruned_int8_convrot.safetensors](https://huggingface.co/FastVideo/FastVideo-FastH3-Comfy/resolve/main/diffusion_models/fastvideo_fasth3_8step_v2_pruned_int8_convrot.safetensors) | 22.1 GB |

Comfy Desktop users can also get most of these by opening the matching template in Desktop (Templates → Z-Image Turbo, Qwen Image Edit 2511, LTX-2, MiniMax H3, FastH3), which offers to download the models.

**Hardware.** Everything above was tested on an RTX 4070 Ti SUPER (16 GB VRAM) with 64 GB of system RAM. Z-Image Turbo and Qwen Image Edit are comfortable on 12 to 16 GB cards. The video models rely on ComfyUI offloading weights to system RAM; LTX-2 at full precision wants about 64 GB of RAM. Measured times are in [workflows/README.md](workflows/README.md).

### 2c. No GPU? Run the open-weights workflows on Comfy Cloud

In **Settings → Open-weights models**, choose **On Comfy Cloud**. The same workflows run on Comfy Cloud through the same SDK code, using your API key. This needs a Comfy Cloud plan that includes API access.

## Using Comfield

Open **⚙ → How to use** inside the app for the complete guide. The short version:

1. **Pick a studio** (Image or Video) and a **model** from the picker at the top of the left panel. Open-weights models come first; each model shows what it can do and whether it's ready.
2. **Add images if you want them:** reference images (edit, combine, keep a character consistent), or a start and end frame for video.
3. **Write the prompt.** Click an idea to start, or press **Enhance** to expand a short idea.
4. **Direct it:** a camera motion (video), a style, shot settings (size, angle, lens, depth of field, lighting), aspect ratio, resolution, duration, sound and the number of takes.
5. Press **Generate** (or <kbd>Ctrl</kbd>/<kbd>⌘</kbd> + <kbd>Enter</kbd>). The shot appears in the feed with live progress.
6. **Use the results:** open a take in the viewer, **Animate** an image into a video, use it as a reference, download it, favorite it, or **Reuse settings** to iterate.

The full written guide is in **[docs/USER_GUIDE.md](docs/USER_GUIDE.md)**.

| Shortcut | Action |
| --- | --- |
| <kbd>Ctrl</kbd>/<kbd>⌘</kbd> + <kbd>Enter</kbd> | Generate |
| <kbd>/</kbd> | Jump to the prompt |
| <kbd>?</kbd> | Keyboard shortcuts |
| <kbd>←</kbd> <kbd>→</kbd> | Previous or next take in the viewer |
| <kbd>Esc</kbd> | Close the viewer, menus and dialogs |

## Downloading models

The **Models** tab lists every open model in the ComfyUI template library, read live from your own ComfyUI, so it grows whenever ComfyUI updates. Models are sorted by what they make: **Image, Video, Audio, 3D, Text** and **Tools** (upscalers, depth, segmentation, background removal, frame interpolation).

| Label | Meaning |
| --- | --- |
| **Ready in Comfield** | The files are on disk and the Image or Video studio can use it now. **Use in studio** opens it there. |
| **Downloaded** | Every file for at least one of its workflows is on disk. **Open in ComfyUI** loads that workflow in ComfyUI. |
| **Works in Comfield** | The studio can use it once its files are downloaded. |
| No label | Not downloaded yet. "1 of 4 files already on disk" means shared files, such as text encoders, are already there. |

Click a model to see each of its workflows with the exact files, folders and sizes, then **Download** the set you want. Files go straight into the ComfyUI model folder they belong to. Two download at a time, the **Models** tab shows a badge while they run, **Cancel** deletes the partial file, and **Retry** resumes a failed download. Comfield checks free disk space before it starts.

A few models are gated on Hugging Face. Accept the license on the model's page, then add a Hugging Face read token in **Settings → Model downloads** (or set `HF_TOKEN`).

## Models and capabilities

### Open weights (ComfyUI workflows, free)

| Model | Studio | From text | Reference images | Start / end frame | Sound |
| --- | --- | --- | --- | --- | --- |
| Z-Image Turbo | Image | Yes | | | |
| Qwen Image Edit 2511 | Image | | 1 to 3 (required) | | |
| LTX-2 19B | Video | Yes | | Both | Yes |
| MiniMax H3 Open | Video | Yes | | Both | Yes |
| FastH3 | Video | Yes | | Both | Yes |

### Cloud (Comfy Router, pay per generation)

| Model | Studio | From text | Reference images | Start / end frame | Sound |
| --- | --- | --- | --- | --- | --- |
| Nano Banana Pro, Nano Banana 2.1 | Image | Yes | up to 8 | | |
| Seedream 5.0 Pro, Seedream 5.0 Flash | Image | Yes | up to 10 | | |
| FLUX 3 | Image | Yes | up to 10 | | |
| GPT Image 2 | Image | Yes | up to 8 | | |
| Qwen Image 3.0 | Image | Yes | up to 3 | | |
| Kling Image O1 | Image | Yes | up to 6 | | |
| Grok Imagine 2.0 | Image | Yes | | | |
| Seedance 2.5 | Video | Yes | up to 4 | Both | Yes |
| Kling 3.0 Omni | Video | Yes | up to 4 | Both | Yes |
| Veo 3.1, Veo 3.1 Fast | Video | Yes | up to 3 | Both | Yes |
| MiniMax H3 | Video | Yes | up to 4 | Both | |
| LTX 2.5 Pro, LTX 2.5 Fast (up to 4K) | Video | Yes | | | Yes |
| FLUX 3 Video | Video | Yes | | Both | Yes |
| Wan 3.0 (up to 30 s) | Video | Yes | up to 4 | Both | Yes |
| Grok Imagine Video 1.5 | Video | Yes | up to 3 | Start | |

The in-app guide (**⚙ → How to use → Studio models**) shows the same table live, including whether each model is ready on your setup. The **Models** page covers the rest of the open models ComfyUI can run.

## How it works

Comfield is a small Node server plus a React app. The server holds your API key, talks to Comfy, downloads results and pushes live updates to the browser.

```
 Browser (React + Tailwind)  ── HTTP + live updates (SSE) ──▶  Comfield server (Node 22, Hono)
                                                                │
   Cloud models ── Comfy Router via @comfyorg/sdk ──────────────┼──▶ api.comfy.org
   (comfy.models.submit / handle / get, cost estimates)         │
                                                                │
   Open weights ── Comfy API v2 via @comfyorg/sdk ──────────────┴──▶ comfy-api-proxy ──▶ your ComfyUI (GPU)
   (client.workflows / assets / jobs, live progress)                └─▶ or Comfy Cloud
```

| Comfy Developer Platform piece | What Comfield uses it for |
| --- | --- |
| **Comfy Router** (`comfy.models.submit`, `handle`, `get`) | Every cloud model. Requests are queued, followed with `handle.events()`, made idempotent with the generation id, and picked back up after a restart. |
| **Router cost estimates** (`POST /v2/models/{id}/estimate`) | The price under the Generate button. |
| **Comfy SDK + Comfy API v2** (`new Comfy()`, `workflows.fromJson`, `assets.fromFile`, `job.events()`) | Runs the open-weights workflows in [`workflows/`](workflows/): uploads frames, submits the graph, streams progress and previews, downloads outputs. |
| **comfy-api-proxy** | Serves Comfy API v2 in front of local ComfyUI. The same SDK code runs on Comfy Cloud by changing the base URL. |
| **Claude on Comfy Router** | The Enhance prompt button. |
| **ComfyUI templates and model folders** (`/templates/index.json`, `/internal/folder_paths`, `/models/{folder}`) | The Models page: which open models exist, which files each workflow needs, which are already on disk, and where new downloads go. |

More detail, including the HTTP API, data model and how to add models, is in **[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)**.

## Configuration

Everything can be set in the app. Environment variables (or a `.env` file) override the defaults:

| Variable | Default | Purpose |
| --- | --- | --- |
| `COMFY_API_KEY` | | Comfy API key for cloud models and Comfy Cloud workflows |
| `COMFYUI_URL` | `http://127.0.0.1:8188` | Where your ComfyUI listens |
| `COMFY_PROXY_URL` | `http://127.0.0.1:8189` | Where Comfield runs comfy-api-proxy |
| `COMFIELD_WORKFLOW_TARGET` | `local` | `local` (your GPU) or `cloud` (Comfy Cloud) for open-weights models |
| `COMFIELD_PORT` / `COMFIELD_HOST` | `5177` / `127.0.0.1` | Comfield's own address |
| `COMFIELD_DATA_DIR` | `./data` | Settings, history, uploads and outputs |
| `COMFIELD_NO_OPEN` | | Set to `1` to stop `npm start` opening a browser |
| `COMFIELD_AUTOSTART_PROXY` | `1` | Set to `0` to manage comfy-api-proxy yourself |
| `COMFIELD_ENHANCE_MODEL` | `anthropic/claude-opus-5-5` | Router model used by Enhance |
| `HF_TOKEN` | | Hugging Face read token, only needed to download gated models |

## Development

```bash
npm run dev          # API with reload on :5177, UI with hot reload on http://localhost:5173
npm test             # adapter and workflow tests: no API key or GPU needed
npm run typecheck
npm run screenshots  # refresh docs/screenshots from a running Comfield
```

```
server/src/
  index.ts               HTTP API, live updates (SSE), static files
  generate.ts            request validation, takes, dispatch, resume after restart
  engines/router.ts      Comfy Router runs: queue, follow, collect, download
  engines/workflow.ts    Comfy API v2 workflow runs on the local proxy or Comfy Cloud
  local/comfyui.ts       ComfyUI discovery, model-file inventory, model folders, comfy-api-proxy process
  local/catalog.ts       Models page: open models from ComfyUI's templates, grouped and checked against disk
  local/downloads.ts     model downloads into ComfyUI's folders: queue, progress, resume, cancel
  models/                model catalog, request builders, result extraction
  assist.ts              prompt enhancer and cost estimates
web/src/                 React UI: studios, feed, viewer, library, models, settings, guide
shared/                  types and creative presets used by both sides
workflows/               API-format ComfyUI workflows with input bindings
tests/                   schema and workflow tests (Vitest)
scripts/                 start, dev, local setup and screenshot helpers
```

The tests build every request body Comfield can send to Comfy Router (every aspect ratio, resolution, duration, reference and frame combination) and validate it against the model's published input schema at `docs.comfy.org/router-schemas`. They also check every workflow graph for broken bindings and dangling links.

Want to help? See [CONTRIBUTING.md](CONTRIBUTING.md).

## Troubleshooting

| Problem | Fix |
| --- | --- |
| "Your GPU" is grey | ComfyUI isn't running. Open Comfy Desktop, then click **Check again** in Settings. |
| "Your GPU" is red | comfy-api-proxy couldn't start. Run `npm run setup:local` (needs Python 3.10+). |
| A model says "Missing N model files" | Open the model picker and click **Download in Models**, or find the model on the **Models** page. |
| A download says the model is gated | Accept its license on Hugging Face, then add a Hugging Face token in **Settings → Model downloads**. |
| The Models page is empty | It reads the list from ComfyUI. Start Comfy Desktop, then click **Check again**. |
| Out of GPU memory | Choose 480p or a shorter duration and close other GPU apps. |
| First local run is slow | Models load into memory the first time; later takes are much faster. Switching model families reloads them. |
| "The Comfy API key was rejected" | Check the key in Settings; create a new one on platform.comfy.org. |
| "Out of credits" | Add credits at platform.comfy.org. |
| Port 5177 is busy | Start with `COMFIELD_PORT=5180 npm start`. |

The terminal running Comfield prints server logs. Include them when you [report a problem](https://github.com/synthetic-ape/comfield/issues/new).

## FAQ

**Do I need a GPU?** No. Cloud models only need an API key. Open-weights models need an NVIDIA GPU with ComfyUI, or Comfy Cloud.

**Is it free?** Comfield is free and open source. Open-weights models are free to run on your hardware. Cloud models cost Comfy credits per generation, and the app shows the estimate first.

**Where do downloaded models go?** Into ComfyUI's own model folders. With Comfy Desktop that's its shared models folder, so Desktop, ComfyUI and Comfield all see them. The Models page shows the free space on that drive.

**Where are my files?** In `data/media/` inside the Comfield folder, downloaded as soon as each take finishes. Settings, history and uploads are in `data/` too. Nothing leaves your machine except the requests you send to Comfy.

**Can other people on my network use it?** By default Comfield only listens on `127.0.0.1`. Set `COMFIELD_HOST=0.0.0.0` to share it on your network, but anyone who can reach it can spend your credits.

**Can I add my own ComfyUI workflow?** Yes. Export it in API format, add bindings for the prompt, seed, size and images, and register it. See [workflows/README.md](workflows/README.md) and [CONTRIBUTING.md](CONTRIBUTING.md).

## License and credits

Comfield is released under the [MIT License](LICENSE).

It's built on the [Comfy Developer Platform](https://docs.comfy.org/development/overview): [Comfy Router](https://docs.comfy.org/development/comfy-router/quickstart), the [Comfy SDK](https://github.com/Comfy-Org/comfy-typescript-sdk) and [comfy-api-proxy](https://github.com/Comfy-Org/comfy-api-proxy). Open-weights workflows are adapted from the official [ComfyUI workflow templates](https://github.com/Comfy-Org/workflow_templates). Models and hosted services are subject to their own licenses and terms; check each model's license before commercial use.
