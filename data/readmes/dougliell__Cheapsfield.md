# Cheapsfield

**A 100% local, 100% open-weights creative studio for product, advertising and architecture visuals, built on ComfyUI and the Comfy SDK.**

**100% local** · **100% open-weights models** · **open source (Apache-2.0)** · no cloud · no API keys · no credits · no uploads

Cheapsfield is a Windows desktop app that turns sketches, product shots, renders, floor plans and photos into finished images and short videos with sound:
- **Product and advertising:** packshots from a sketch or a 3D render, studio relighting, new camera angles, placing a product in a scene, campaign looks and wider formats for banners and social posts.
- **Architecture and interiors:** sketch to render, styled floor plans, virtual staging, day to night, aerial views from a map.

Every image and video is generated **on your own GPU, by open-weights models you download once**. Nothing is sent to a server: there are no paid APIs, no partner nodes and no accounts, and the recipes use **only core ComfyUI nodes**. You work in a node canvas (**Flow**) or in focused one-screen **apps**. Under the hood, every generation is a ComfyUI workflow that runs headless through the official **Comfy SDK**.

> Built for the Comfy **Open Source Higgsfield** challenge, **Open Weights Only** category: a Higgsfield-style studio that runs entirely on your machine.

![Made with Cheapsfield: a dance moved onto another person, a character swap, a directed neon scene, an AI influencer dancing, three photos turned into one scene and a street going from day to neon with keyframes, all generated locally](docs/imagens/showcase.webp)

## What it does

![Home: animated highlights of the new apps (Shot Director, Video from References, Light from an Image, Character Swap with a before/after wipe, Motion Transfer), then pick up where you left off](docs/imagens/home.png)

The Home is a live showcase: highlights, the influencer banner and the "Made with Cheapsfield" wall are short looping videos, all generated on this machine by the app's own open-weights models (fictional people, unbranded products).

![The Home showcase: the Create Influencer banner, the New apps row and the Video from References banner (three photos in, one scene with sound out)](docs/imagens/home-showcase.png)

**Apps** are one-screen tools that write the prompt for you. You pick options and drop in images; the app builds the right prompt for each model.

![One scene through four apps: sketch, True Line, Light & Hour at blue hour, Orbit at 40°](docs/imagens/apps-results.webp)

| App | What it does | Good for |
|---|---|---|
| **Shot Director** | Describe the moment and direct it like a film: camera body, lens, focal length, aperture, framing, light, film stock, look and color grade (or the palette of any image), as a **still or a video with sound**. Optional character photo. FLUX 3, Qwen Image 2.1, Krea 2; video with FastH3, MiniMax H3 or LTX 2.5 | Campaigns, storyboards, characters |
| True Line | Sketch, 3D viewport or physical model → photorealistic image, same framing (1:1) | Products, architecture |
| Styled Plan | Restyles a 2D floor plan (and furnishes it, if you want) without touching the geometry | Architecture |
| Light & Hour | Relights a product shot or a scene: time of day, studio or natural light, atmosphere, color temperature, intensity. **From an image:** connect any photo and its light and color tone move onto your shot (Qwen Edit 2511 + Light Migration LoRA) | Products, architecture |
| Reference Mood | Applies the style and light of a reference image: a campaign look, a mood, an art style | Products, architecture |
| Orbit | New camera angles of a product or a space by orbiting the camera (rotation, tilt, zoom) | Products, architecture |
| Furnish from Moodboard | Fills a room or a store with the pieces from a moodboard | Interiors, retail |
| Object in Scene | Places a product in a scene, or swaps an existing object | Products, interiors |
| Text Retouch | Edits by instruction: add people, change the weather, change a color, make it a night shot… | Products, architecture |
| Render Finisher | Finishes a work-in-progress 3D render (product or interior): light, shadows, materials, noise | Products, architecture |
| Map to Drone | Satellite capture (Google Earth/Maps) → realistic aerial photo, same camera | Architecture |
| Ink Sketch | Photo or render → clean ink line drawing | Products, architecture |
| Beyond the Frame | Outpaints the image to a wider frame (banners, social formats) | Products, architecture |
| Upscale | 1×–4× upscaling, precise or generative | Everything |
| **Spot Edit** | Mark the photo (Area, Pin, Sketch or Arrow), say what to change at each mark and optionally attach a reference image to a mark. Only the marked area is edited and pasted back, so everything else stays pixel-identical. Qwen Edit 2511, Qwen Image 2.1 or FLUX 3 Klein | Fashion, products, interiors |
| **Create Influencer** | Creates a fictional digital influencer from a short form (look, age, hair, outfit); the image is ready to be the reference for Character Swap | Characters, campaigns |
| **Character Swap** | Replaces the person (or the scene) in a video with the one in a reference photo, keeping the motion, timing and camera. **MiniMax H3** ref2va (new audio) or **SCAIL-2** (keeps the original audio, finds the person with SAM 3.1). Quality: Turbo or Full, steps, face fidelity | Characters, campaigns |
| **Motion Transfer** | The person in your photo performs the motion from any video (a dance, a gesture, a walk) in a new scene you describe, with sound. MiniMax H3 + Fun ControlNet Union (pose from the video with RT-DETR + SDPose) | Characters, social content |
| **Video from References** | Up to 4 photos (people, products, places) and a scene you describe become one video with sound. **References:** MiniMax H3 uses each photo as `<Picture N>`, or LTX 2.3 with the Ingredients IC-LoRA builds a reference sheet. **Keyframes:** pin photos to exact seconds and the video passes through them (MiniMax H3) | Ads, social content, storyboards |
| **Reveal Video** | Before → after as a short video with sound (sketch → product shot, empty → furnished, day → night) | Products, architecture |

**Subject: Architecture / Product** is available in 11 apps. It adapts the generated prompt to buildings and interiors or to products and advertising.

<p>
  <img src="docs/imagens/sketch-to-photo.webp" width="49%" alt="True Line: an ink line drawing of a sneaker becomes a real product photo, same framing">
  <img src="docs/imagens/character-swap.webp" width="49%" alt="Character Swap: the person in the video is replaced by the one in a reference photo, same motion and camera">
</p>

### Shot Director

![Shot Director: the light cards with thumbnails generated locally, and four results: a Krea 2 close-up of a cyclist, your character in a neon street (Qwen Edit 2511), a FastH3 video with sound and your character in motion (MiniMax H3)](docs/imagens/shot-director.webp)

Write the scene, then pick from six cards, each with a thumbnail of the same scene rendered locally for every option: **Camera** (body, lens, focal length, aperture), **Framing**, **Light**, **Film**, **Look** and **Grade**. *From an image* takes the color palette of any picture, right in the app. Switch between **Image** and **Video**: the model menu changes with it, and each model gets the prompt written its way. Connect a **character** photo to keep the same person (Qwen Edit 2511 for stills, MiniMax H3 ref2va for video). Inspired by Comfy's Cinematic Studio (MIT), but every model runs on your GPU.

### Motion Transfer

![Motion Transfer: three moments of a dance video (left of each pair) performed by the fitness influencer on a rooftop at sunset (right)](docs/imagens/motion-transfer.webp)

The video only lends its **pose**: it becomes a skeleton video (RT-DETR + SDPose, core nodes) that drives MiniMax H3 through the Fun ControlNet Union, with your photo as `<Picture 1>`. The place, the camera and the sound come from your text.

### Video from References

![Video from References: the app with three photos (a young man, a green sneaker, a house with a pool) and four results: MiniMax H3 turns the three photos into one scene, LTX 2.3 from a reference sheet, keyframes from day at 0 s to neon at 4.5 s, and Relight with the light of a neon photo](docs/imagens/video-references.webp)

Drop in the person, the product and the place, name them if you want, and describe what happens. MiniMax H3 sees each photo as `<Picture 1..4>`; LTX 2.3 gets them on one 16:9 reference sheet built inside the workflow (Ingredients IC-LoRA). In **Keyframes** mode REF1 is the reference and REF2 to REF4 are guide frames fixed at the seconds you choose (`MiniMaxH3AddGuide`, a core node). The same idea works for light: in **Light & Hour → From an image**, the light and color tone of any photo move onto your shot.

### Spot Edit

![Spot Edit: mark an area, a pin or a sketch in lime, say what to change, and only that part of the photo changes (jacket recolor, sneakers from a reference photo, a sketched dog, a handbag)](docs/imagens/spot-edit.webp)

Draw an **Area** around what may change, drop a **Pin** or an **Arrow** on a spot, or **Sketch** what you want to add, then write the request for each mark. Any mark can use **REF1** or **REF2** (for example, the exact sneakers from a product photo). The recipe crops the marked area, edits it at about 1 megapixel and pastes it back onto the original with a soft mask, using only core ComfyUI nodes (`ImageCrop`, `ImageScale`, `ImageCompositeMasked`). Outside the Areas, the result is identical to the input.

Each app opens in its own workspace: inputs and options on the left, the result with a before/after slider, and the session's results below.

![The True Line app: a sketch as BASE, Late Afternoon light, and the before/after of the result](docs/imagens/app-true-line.png)

**Flow** is a Miro-style canvas with *Generate image*, *Edit image* and *Generate video* nodes, plus every app as a node. Chain results, compare versions, and every output PNG embeds its recipe, so you can rebuild the node that generated it in one click. Each plug shows what it takes (image or video); drop a link anywhere on a node and it snaps to the right plug, and hover a link to cut it with the scissors.

![A Flow: one photo into Light & Hour, six moods out (daylight to night) and a before/after Compare node. Each plug shows what it takes (image or video); drop a link anywhere on a node and it snaps to the right plug, hover a link and the scissors cut it](docs/imagens/flow.png)

![Reveal Video: the sketch becomes the photo over 5 seconds, 1080p with LTX 2.5 HD](docs/imagens/reveal-video.webp)

**Video:** *Generate video* and *Reveal Video* run on **LTX 2.5** (the default, up to **1080p** with the two-stage HD recipe), **MiniMax H3** or **FastH3** (MiniMax H3 distilled to 8 steps by FastVideo). They support text-to-video, image-to-video from a first frame, and first-to-last-frame transitions, with native audio. You switch models in the node; the matching workflow is picked automatically.

## How it is built

- **Desktop shell:** Tauri 2 (Rust) + React 19. Projects, gallery and history live in a SQLite library folder you choose (never in AppData).
- **Generation:** a local ComfyUI runs headless as a child process. Cheapsfield talks to it **through the Comfy SDK**:
  - `comfy-sdk` + `comfy-api-proxy` (Comfy API v2) in an isolated Python environment (`engine/sdk`);
  - a small bridge (`engine/sdk/ponte.py`) submits workflows, streams progress and downloads outputs.
- **Recipes** (`engine/workflows`): API-format ComfyUI workflows plus a manifest that tells the app where prompt, seed, size and images go. See [`engine/CONTRATO_WORKFLOWS.md`](engine/CONTRATO_WORKFLOWS.md).
  - **Core ComfyUI nodes only:** no custom nodes and no API (partner) nodes.
  - Models are matched **by file name**, so recipes run whatever subfolders your models live in.
- **Models (all open weights):**
  - images: Qwen Image 2.1, Qwen Image Edit 2511, FLUX 3 Klein (base and distilled, with the official prompt upsampler), Krea 2, FLUX.1 Fill;
  - Create Influencer (`t2i`): Krea 2, Qwen Image 2.1 or FLUX 3 Klein;
  - Spot Edit (`pontual`): Qwen Image Edit 2511, Qwen Image 2.1 or FLUX 3 Klein, crop → edit → paste back with a mask;
  - video: LTX 2.5, MiniMax H3 (fl2va for generation; ref2va + turbo ref2v LoRA for Character Swap, Shot Director with a character and Motion Transfer) and FastH3 (8-step distilled H3);
  - Character Swap with SCAIL-2 (Wan 2.1 14B, nvfp4) + SAM 3.1 masks; Motion Transfer with the MiniMax H3 Fun ControlNet Union + SDPose / RT-DETR;
  - Video from References with MiniMax H3 (up to 4 `<Picture N>` references, or keyframes with `MiniMaxH3AddGuide`) and LTX 2.3 22B + the Ingredients IC-LoRA (reference sheet); Light & Hour *From an image* with the Light Migration LoRA on Qwen Edit 2511;
  - upscaling: 4x-UltraSharp.

  Full list with sizes, sources and licenses: [`docs/MODELOS.md`](docs/MODELOS.md).
- **Optional local LLM** (llama.cpp `llama-server` + a GGUF model): improves prompts and describes images. **Set it up for me** downloads the official llama.cpp (CUDA) and Qwen3-VL 4B Instruct (Apache-2.0, reads text and images, ~3.6 GB, fits next to ComfyUI on an 8 GB GPU), or point it to your own. Without it, everything else works.

## Requirements

- Windows 10/11 x64.
- NVIDIA GPU: **12 GB** VRAM minimum, **16 GB** recommended (the video models offload to RAM above that). 32 GB+ system RAM recommended.
- **ComfyUI 0.41 or newer**, optional: Cheapsfield uses your install as-is (the portable build, ComfyUI-Easy-Install, or a git clone with a `venv`/`.venv`) and never modifies it. **No ComfyUI? The setup installs the official portable build for you** (about 2 GB to download, 6 GB on disk).
- **Python**, optional: a Python 3.10+ on the PATH is used once to create the Comfy SDK environment; without one, the setup downloads the official Python 3.12 package (15 MB) into the app folder, with no system install.
- Disk space for the models you want, from about 17 GB (Qwen Image 2.1 only) to about 255 GB (all 42 unique catalog files; 237.1 GiB).

## Install

1. Download the latest `Cheapsfield-<version>-windows-x64.zip` from [**Releases**](https://github.com/dougliell/Cheapsfield/releases) and extract it to a folder you own, for example `C:\Users\<you>\Apps\Cheapsfield`.
2. Run `Cheapsfield.exe`. The **first-run setup** walks you through:
   - **Library folder:** where your projects, gallery and backups go.
   - **ComfyUI:** found automatically on your drives, or pick its folder. **None? Press *Install ComfyUI for me*:** it downloads the official portable ComfyUI for NVIDIA next to the app, extracts it and selects it. Then the Comfy SDK is prepared (*Prepare the Comfy SDK*, about 20 s; it installs `comfy-sdk` and `comfy-api-proxy` from PyPI into `sdk\.venv`).
   - **GPU:** the card with the most VRAM is preselected.
   - **Models:**
     - models you already have are found by file name in your ComfyUI `models` folder, in its `extra_model_paths.yaml` and in any folder you link;
     - missing ones download from Hugging Face, with a queue, progress and resume;
     - a few repositories (FLUX 3 Klein, LTX 2.5) ask you to accept their license on Hugging Face first; paste a read token in the setup.
   - **Local LLM** (optional): **Set it up for me** does it in one click, or skip it.
3. Open an app, drop an image, press **Generate**.

You can reopen the setup at any time from *Settings → Initial setup and models*.

![First-run setup with no ComfyUI on the computer: Install ComfyUI for me downloads the official portable build and sets everything up](docs/imagens/setup-comfyui.png)

![First-run setup: models grouped by feature, found in your folders or downloaded](docs/imagens/setup-models.png)

## Build from source

```powershell
# Node.js 22+, Rust (stable, MSVC) and the Tauri prerequisites for Windows
git clone https://github.com/dougliell/Cheapsfield.git
cd Cheapsfield\app
npm install
powershell -ExecutionPolicy Bypass -File ..\engine\sdk\instalar.ps1   # Comfy SDK env for development
npm run app                                                             # dev mode (Vite + Tauri)
npx tauri build --no-bundle                                             # release exe in src-tauri\target\release
```

Tests: `cargo test` (in `app/src-tauri`) and `npx tsc --noEmit` (in `app/`). To package a release zip (exe + recipes + SDK installer), run `powershell -File app\scripts\empacotar-release.ps1`.

## Project layout

| Folder | What is there |
|---|---|
| `app/src` | React UI: Hub, Flow canvas, apps (`apps/`), app screen (`studio/`), first-run setup |
| `app/src-tauri` | Rust core: library and SQLite, jobs, ComfyUI process, model catalog and downloads, LLM |
| `engine/workflows` | Recipes (ComfyUI API workflows + manifests) and the model catalog |
| `engine/sdk` | Comfy SDK bridge and installer |
| `engine/comfy` | Generators for the recipes and the model catalog |
| `docs/MODELOS.md` | Models, sources and licenses |

## Licenses: read this before commercial use

- **Cheapsfield's code** is released under the [Apache License 2.0](LICENSE).
- **The models are not covered by that license.** Each one has its own terms, linked in [`docs/MODELOS.md`](docs/MODELOS.md). Several are **non-commercial or restricted**:
  - Qwen Image 2.1: Qwen Research License;
  - FLUX.1 Fill [dev]: non-commercial license;
  - FLUX 3 Klein: FLUX Kommunity License;
  - LTX 2.5: LTX-2.x Community License (a paid license above a revenue threshold);
  - MiniMax H3 (and FastH3, the Fun ControlNet): MiniMax H3 Community License (regional and revenue limits);
  - SAM 3.1 (Character Swap with SCAIL-2): Meta SAM License;
  - 4x-UltraSharp V2: CC BY-NC-SA 4.0.

  **Commercial use of generated content may require a license from the model makers.** Review each license against your intended use.
- `engine/comfy/flux3_upsampler_t2i.txt` is the official FLUX 3 prompt-upsampler system prompt published by Black Forest Labs.

## Privacy

Nothing leaves your machine except:
- the model downloads you start (Hugging Face);
- the one-time Python packages for the Comfy SDK (PyPI);
- the links you click.

There is no telemetry and no account.

## Credits

[ComfyUI](https://github.com/comfyanonymous/ComfyUI) and the [Comfy SDK](https://pypi.org/project/comfy-sdk/) by Comfy Org; the model makers (Qwen, Black Forest Labs, Lightricks, MiniMax, Krea, Z.ai (SCAIL-2), FastVideo (FastH3), Alibaba PAI (Fun ControlNet), Meta (SAM 3.1), SDPose, lightx2v, Kijai, fal, the Light Migration LoRA and the community quantizers listed in `docs/MODELOS.md`); Comfy's [Cinematic Studio](https://github.com/Comfy-Org/comfy-cinematic-studio) (MIT), the idea behind Shot Director; [Tauri](https://tauri.app), [React Flow](https://reactflow.dev) and [llama.cpp](https://github.com/ggml-org/llama.cpp).
