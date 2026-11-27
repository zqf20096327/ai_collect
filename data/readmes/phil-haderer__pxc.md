<div align="center">

<h1><img src="readme-images/logo.png" alt="PxC" width="418"></h1>

[![License: MIT or Apache-2.0](https://img.shields.io/badge/license-MIT%20%7C%20Apache--2.0-blue)](#license)
[![Platform: Windows and Linux Mint](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20Mint-lightgrey)](#install-on-windows)
[![Python 3.11 or newer, on Linux 3.10 or newer](https://img.shields.io/badge/python-3.11%2B%20%C2%B7%20Linux%203.10%2B-blue)](#install-on-windows)

**A companion app that brings Photoshop-style generative AI to PhotoCraft, running on your own PC.**
Pick a function, type a prompt, press Generate: the result arrives as a new layer in your document.

Tested: Windows 11 · Linux Mint (X11, Cinnamon Wayland) · PhotoCraft 0.23.1 · ComfyUI 0.45.0

<img src="readme-images/plugin-window.webp" alt="The PxC window next to PhotoCraft: Text to Image with MiniMax H3 Image, the result as a new layer" width="900">

[Examples](#examples) · [Features](#features) · [Before you start](#before-you-start) · [Install on Windows](#install-on-windows) · [Install on Linux](#install-on-linux) · [Model downloads](#model-downloads) · [Functions](#functions) · [Help](#help) · [Technical details](#technical-details)

</div>

Many test rounds went into PxC, and every line of it was written with Claude Code (Opus and Sonnet 5.5). Coming from graphic design, I built it for real work, and it's already in professional use, where it can stand in for Photoshop's generative functions, running on local AI. I would love to hear your feedback. I use PxC every day and keep developing it, so bug reports and ideas go straight into the next versions.

<!-- examples:start -->
<a id="examples"></a>

## Examples

<table>
<tr>
<td width="50%" valign="top"><b>Text to Image</b><br><a href="EXAMPLES.md"><img src="readme-images/examples/text-to-image-9.jpg" width="100%"></a><br><small>Fibo 2.0 Edit Turbo · Built-in style: Vintage paper collage · “a whale swimming through the clouds above a small town, little birds around it”</small></td>
<td width="50%" valign="top"><b>Edit canvas</b><br><a href="EXAMPLES.md"><img src="readme-images/examples/edit-canvas-3.jpg" width="100%"></a><br><small>Fibo 2.0 Edit Turbo · “Make it a sunny autumn day with orange and yellow leaves on the trees and in the grass.”</small></td>
</tr>
</table>

<a href="EXAMPLES.md"><img src="readme-images/all-examples.svg" alt="All examples"></a>
<!-- examples:end -->

## Features

- **Seven SOTA models:** Flux 3 Klein, Flux 2 Klein, Qwen Image 2.1, Fibo 2.0 Edit Turbo, Krea 2 Turbo, MOSS Image and the newly released MiniMax H3 Image. Local only: of course the models run in ComfyUI on your GPU.
- **Seven generation modes:**
  - <picture><source media="(prefers-color-scheme: dark)" srcset="readme-images/icons/text-to-image-dark.png"><img src="readme-images/icons/text-to-image-light.png" alt="" width="20" height="20"></picture>&nbsp; Text to Image
  - <picture><source media="(prefers-color-scheme: dark)" srcset="readme-images/icons/expand-dark.png"><img src="readme-images/icons/expand-light.png" alt="" width="20" height="20"></picture>&nbsp; Expand Image
  - <picture><source media="(prefers-color-scheme: dark)" srcset="readme-images/icons/fill-dark.png"><img src="readme-images/icons/fill-light.png" alt="" width="20" height="20"></picture>&nbsp; Fill
  - <picture><source media="(prefers-color-scheme: dark)" srcset="readme-images/icons/remove-dark.png"><img src="readme-images/icons/remove-light.png" alt="" width="20" height="20"></picture>&nbsp; Remove
  - <picture><source media="(prefers-color-scheme: dark)" srcset="readme-images/icons/edit-dark.png"><img src="readme-images/icons/edit-light.png" alt="" width="20" height="20"></picture>&nbsp; Edit, with five modes in a list: Edit canvas · Multi image edit · Sketch to image · Scribble on photo · Scribble with reference
  - <picture><source media="(prefers-color-scheme: dark)" srcset="readme-images/icons/refine-dark.png"><img src="readme-images/icons/refine-light.png" alt="" width="20" height="20"></picture>&nbsp; Refine Image
  - <picture><source media="(prefers-color-scheme: dark)" srcset="readme-images/icons/upscale-dark.png"><img src="readme-images/icons/upscale-light.png" alt="" width="20" height="20"></picture>&nbsp; Upscale

  Not every model offers every function or mode: MOSS and Krea, for example, only do Text to Image.
- **LLMs included:** one tick lets a text model improve your prompt. It also describes the canvas and reference images, turns sketches and scribbles into prompts, and names what to remove.
- **Your own prompts:** save a prompt under a name and use it again later, with the function and model it was made for.
- **Tested settings:** every function and model starts with its tested settings; change them under Advanced settings if you like.
- **Model files made easy:**
  - **Download missing files** gets each model as one pack, every file in the right ComfyUI folder.
  - Already have a model? Pick your own file in the gear window ▸ Model Links: bf16, fp8, nvfp4, or GGUF with [ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF).
  - Six other versions (Qwen Image 2.1 Turbo, MOSS Image Base, Kromoss, Fibo 2.0 Dev, Krea 2 Turbo, MiniMax H3 w4a8) are recognised and run with their model-card settings.
- **Team use:** run ComfyUI on one strong PC or server and point several PxC installations at it (gear window ▸ Other settings ▸ ComfyUI address). The queue lists your own jobs and, read-only, the jobs of the others, and the progress bar shows how many jobs are ahead of yours.

> Unofficial community project, not affiliated with PhotoCraft, ArtCraft or Storyteller. PhotoCraft is in early alpha
> and so is this app.

<a id="style-prompt-examples"></a>
<details>
<summary><h2>Style prompt examples</h2></summary>

The Style prompts button beside the prompt adds a ready-made style text. A few of the built-in styles:

**Text to Image** (83 styles in 13 groups)

- **Photo:** Tilt-shift, miniature look · Golden hour travel photo · Drone shot from above · Night light trails, long exposure
- **Studio & product:** Studio portrait · Business headshot · Product photo, glass on white · Food photography
- **Film look:** Film look, warm dusk · Neon city night, bokeh · 1970s film, muted greens
- **Black & white:** Black and white, hard light and shadows · Double exposure, black and white
- **Painting:** Oil painting, 19th-century realism · Impressionist painting, sunny · Watercolor storybook · Japanese ink wash
- **Drawing & print:** Pencil gesture sketch · Etching, cross-hatched · Linocut print
- **Graphic & poster:** Mid-century travel poster · Risograph, blue and yellow · Clear-line comic · Vintage paper collage
- **Anime & comic:** Modern anime, clean lines · Anime, golden sky · Manga, bold ink · 1930s rubber-hose cartoon
- **3D & craft:** 3D clay render · Claymation, stop-motion · Low-poly game look · Voxel diorama, pastel
- **Pixel & glitch:** Pixel art · VHS glitch
- **Retro & vintage:** Technicolor, 1950s print · Synthwave, neon retro
- **Fantasy & sci-fi:** Dark fantasy, glowing neon · Cyberpunk neon, rain · Cosmic glow
- **Surreal:** Floating objects, blue sky · Surreal reflections, pastel

**Edit** (34 styles in 7 groups; a style that Text to Image has too carries the same name and look)

- **Photo:** Realistic photo · Studio portrait · Vintage black-and-white photo · Cyanotype blue print, glowing
- **Film look:** Film look, warm dusk · Film look, cool blue night
- **Painting:** Watercolor storybook · Oil painting, 19th-century realism · Impressionist painting, sunny · Japanese ink wash
- **Drawing & print:** Pencil gesture sketch · Linocut print · Etching, cross-hatched
- **Anime & comic:** Animated film · Modern anime, clean lines · Clear-line comic
- **Graphic & poster:** Flat vector, sunny · Mid-century travel poster · Risograph, blue and yellow
- **Retro & vintage:** Pixel art · Technicolor, 1950s print · Synthwave, neon retro

</details>

## Coming in the next version

- **SAM 3 selection:** click an object in your picture (or type what it is) and PxC selects it in PhotoCraft, ready for Fill or Remove.
- **Portable version:** a ZIP with its own Python inside: unpack it and start PxC, no setup script needed.
- **Denoise in Text to Image:** a slider that starts from the picture open in PhotoCraft (image to image) for every model; 1.0 still makes a new picture.
- **Custom LoRAs per model:** each model keeps its own LoRA list, so switching models no longer means switching LoRAs by hand.
- Minor adjustments.

## How it fits together

```
PhotoCraft  <-->  PxC  <-->  ComfyUI
```

- **PhotoCraft** is the image editor where you work and where the results land as layers.
- **ComfyUI** runs the AI models on your graphics card.
- **PxC** (this companion app, a small window of its own next to PhotoCraft) sits between them: it sends your picture or selection to ComfyUI and puts the result back as a layer.

## Before you start

You need (the software is free):

- **Windows 10/11 or Linux** with a GPU with at least 8 GB VRAM.
- **[PhotoCraft](https://github.com/storytold/photocraft/releases) 0.20.2 or newer**: the image editor where you work. PxC adds AI functions to it.
- **[ComfyUI](https://github.com/comfyanonymous/ComfyUI#installing)**: runs the AI models; leave it running while you work. Flux 2 and Upscale (Flux 3, Fibo) also need the add-on [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes) ([ComfyUI Easy Install](https://github.com/Tavris1/ComfyUI-Easy-Install) includes it).
- **[Python](https://www.python.org/downloads/windows/) 3.11 or newer** (Linux: 3.10 or newer). No Python yet? On Windows the setup offers to install it for you.
- **About 13 to 19 GB of free disk space per model you want to use, MiniMax about 38 GB, or about 30 GB with its smaller variant** (the models are large files; one model is enough to start).

Then follow [Install on Windows](#install-on-windows) or [Install on Linux](#install-on-linux).

## Install on Windows

1. **Download**: click **Code ▸ Download ZIP** (green button at the top of this page) and unpack it to a folder you keep, for example `C:\programs\pxc`. Prefer git? See [Technical details](#technical-details).
2. **Set up**: double-click **`setup-windows.bat`**. It sets everything up and puts **PxC** on your desktop; it finds `photocraft.exe` itself and asks once if it can't. No Python yet? It offers to install Python 3.13 with one key press. If that is not possible, or you say no, it opens the download page: install Python 3.13 there with the default options ("tcl/tk" stays ticked) and run `setup-windows.bat` again. (`setup-windows.bat /check` only looks and changes nothing.)
3. **Start**: start ComfyUI, close PhotoCraft if it is open, then double-click **PxC** on your desktop. PhotoCraft opens and the PxC window appears next to it.
4. **Get a model**: in the PxC window click the gear ▸ pick a model ▸ **Download missing files**, then restart ComfyUI (it reads its model folders only when it starts). **Qwen Image 2.1** and **Fibo 2.0** need no login at external websites; **Flux 3 Klein** needs a free Hugging Face account once (the button opens the page; log in and accept the licence there). You can also download the files by hand: see [Model downloads](#model-downloads).
5. **Generate**: pick a function and a model, type a prompt and press **Generate** (Ctrl+Enter). The status line at the bottom tells you what is happening.

## Install on Linux

1. **System packages** (Python 3.10+ with tkinter and venv):

   ```bash
   # Debian/Ubuntu
   sudo apt install python3 python3-tk python3-venv
   # Fedora
   sudo dnf install python3 python3-tkinter
   # Arch
   sudo pacman -S python tk
   # optional, to paste pictures from the clipboard: wl-clipboard (Wayland) or xclip (X11)
   sudo apt install wl-clipboard xclip
   # only if setup-linux.sh says libXcursor is missing (needed to drag pictures onto the reference slots)
   sudo apt install libxcursor1      # Fedora: libXcursor, Arch: libxcursor
   ```

2. **Download**: click **Code ▸ Download ZIP** (green button at the top of this page) and unpack it, or use git (see [Technical details](#technical-details)).
3. **Set up**: open a terminal in the PxC folder and run `./setup-linux.sh`. It makes a private Python environment, installs the packages and adds **PxC** to your application menu. It never installs system packages itself; if something is missing it prints the command for your distribution. (`./setup-linux.sh --check` only looks and changes nothing.)
4. **Start**: start ComfyUI, close PhotoCraft if it is open, then start **PxC** from the menu (or run `./pxc.sh`). PhotoCraft is found in `PATH`, `/opt`, `~/Applications`, `~/.local/bin` or as a Flatpak. If it is somewhere else: `PHOTOCRAFT=/path/to/photocraft ./pxc.sh`.
5. **Get a model and generate**: as in steps 4 and 5 of [Install on Windows](#install-on-windows).

Window too small or too big? Gear window ▸ **Other settings** ▸ **Interface scale**.

## Model downloads

**You do not have to sort anything yourself.** Each model is one pack: the **Download missing files** button (gear window ▸ the model) downloads all missing files of that model and puts each one into the right ComfyUI folder automatically, sub-folders included; then restart ComfyUI. The list below is the same pack for downloading by hand: put each file into the folder named below it, inside your ComfyUI folder, then restart ComfyUI. You only need the files of the models you want. "Optional" files switch extra features on; without them the model still works. The same lists as a page of their own: [docs/model-downloads.md](docs/model-downloads.md).

**Custom nodes** (small add-ons for ComfyUI; install them from the ComfyUI Manager or the link, then restart ComfyUI):
- [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes): needed for Flux 2 and for Upscale with Flux 3 and Fibo.
- [ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF): only for smaller GGUF model files (gear window, the file's field).

<!-- model-downloads:start -->

<details>
<summary><b>Flux 3 Klein</b>: about 18.2 GB needed</summary>

| File and its ComfyUI folder | Needed for | Size | Download |
|---|---|---|---|
| `flux3-image-klein-int8-convrot.safetensors`<br>`models/diffusion_models` | all functions | 5.8 GB | [Hugging Face: black-forest-labs/flux-3-image-klein-comfy](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/main/diffusion_models/flux3-image-klein-int8-convrot.safetensors) (needs a free Hugging Face login and acceptance of the licence) |
| `qwen3.5_9b_flux3_prompt_upsampler_w4a8.safetensors`<br>`models/text_encoders` | Remove Selection, Enhance my Prompt with LLM, Describe Canvas, Describe Multi Image Slot, Sketch to image, Scribble on photo | 6.7 GB | [Hugging Face: black-forest-labs/flux-3-image-klein-comfy](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/main/text_encoders/qwen3.5_9b_flux3_prompt_upsampler_w4a8.safetensors) (needs a free Hugging Face login and acceptance of the licence) |
| `qwen3vl_4b_int8_convrot.safetensors`<br>`models/text_encoders` | all functions | 4.9 GB | [Hugging Face: Comfy-Org/Krea-2](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/text_encoders/qwen3vl_4b_int8_convrot.safetensors) |
| `flux2-vae.safetensors`<br>`models/vae` | all functions | 336 MB | [Hugging Face: Comfy-Org/Flux-2-Dev](https://huggingface.co/Comfy-Org/Flux-2-Dev/resolve/main/split_files/vae/flux2-vae.safetensors) |
| `flux-3-image-klein-outpaint.safetensors`<br>`models/loras/Flux 3` | Expand Image | 161 MB | [Hugging Face: ausboss/FLUX-3-Image-Klein-Outpaint-LoRA](https://huggingface.co/ausboss/FLUX-3-Image-Klein-Outpaint-LoRA/resolve/main/flux-3-image-klein-outpaint.safetensors) |
| `flux-3-image-klein-restore.safetensors`<br>`models/loras/Flux 3` | Upscale, Refine Image | 161 MB | [Hugging Face: ausboss/FLUX-3-Image-Klein-Restore-LoRA](https://huggingface.co/ausboss/FLUX-3-Image-Klein-Restore-LoRA/resolve/main/flux-3-image-klein-restore.safetensors) |
| `4x-UltraSharpV2.safetensors`<br>`models/upscale_models` | Upscale | 140 MB | [Hugging Face: Kim2091/UltraSharpV2](https://huggingface.co/Kim2091/UltraSharpV2/resolve/main/4x-UltraSharpV2.safetensors) |

Optional (the model works without them, the named feature is greyed out):

| File and its ComfyUI folder | Feature | Size | Download |
|---|---|---|---|
| `seedvr2_3b_int8_convrot.safetensors`<br>`models/diffusion_models` | SeedVR2 pre-cleaning in Upscale | 3.5 GB | [Hugging Face: Comfy-Org/SeedVR2](https://huggingface.co/Comfy-Org/SeedVR2/resolve/main/diffusion_models/seedvr2_3b_int8_convrot.safetensors) |
| `seedvr2_ema_vae_fp16.safetensors`<br>`models/vae` | SeedVR2 pre-cleaning in Upscale | 501 MB | [Hugging Face: Comfy-Org/SeedVR2](https://huggingface.co/Comfy-Org/SeedVR2/resolve/main/vae/seedvr2_ema_vae_fp16.safetensors) |
| `taef2_decoder.pth`<br>`models/vae_approx` | live preview | 3 MB | [GitHub: madebyollin/taesd](https://raw.githubusercontent.com/madebyollin/taesd/main/taef2_decoder.pth) |

**Custom node:** Upscale also needs the custom node pack [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes) (Color Match). Install it from the ComfyUI Manager or the link, then restart ComfyUI.

</details>

<details>
<summary><b>Flux 2 Klein</b>: about 18.6 GB needed</summary>

| File and its ComfyUI folder | Needed for | Size | Download |
|---|---|---|---|
| `flux-2-klein-9b_int8_convrot.safetensors`<br>`models/diffusion_models` | all functions | 9.4 GB | [Hugging Face: obsxrver/ComfyUI-Native-INT8_ConvRot](https://huggingface.co/obsxrver/ComfyUI-Native-INT8_ConvRot/resolve/main/diffusion_models/flux-2-klein-9b_int8_convrot.safetensors) |
| `qwen_3_8b_fp8mixed.safetensors`<br>`models/text_encoders` | all functions | 8.7 GB | [Hugging Face: Comfy-Org/Flux-2-Klein-9B](https://huggingface.co/Comfy-Org/Flux-2-Klein-9B/resolve/main/split_files/text_encoders/qwen_3_8b_fp8mixed.safetensors) |
| `flux2-vae.safetensors`<br>`models/vae` | all functions | 336 MB | [Hugging Face: Comfy-Org/Flux-2-Dev](https://huggingface.co/Comfy-Org/Flux-2-Dev/resolve/main/split_files/vae/flux2-vae.safetensors) |
| `ultra_real_v4.safetensors`<br>`models/loras/Flux 2` | Upscale, Refine Image | 166 MB | [Civitai](https://civitai.com/api/download/models/2846977) (Civitai may ask you to log in) |

Optional (the model works without them, the named feature is greyed out):

| File and its ComfyUI folder | Feature | Size | Download |
|---|---|---|---|
| `qwen3vl_4b_int8_convrot.safetensors`<br>`models/text_encoders` | Enhance my Prompt with LLM, Describe Canvas, Describe Multi Image Slot, Sketch to image, Scribble on photo | 4.9 GB | [Hugging Face: Comfy-Org/Krea-2](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/text_encoders/qwen3vl_4b_int8_convrot.safetensors) |
| `taef2_decoder.pth`<br>`models/vae_approx` | live preview | 3 MB | [GitHub: madebyollin/taesd](https://raw.githubusercontent.com/madebyollin/taesd/main/taef2_decoder.pth) |

**Custom node:** Upscale (always in tiles) also needs the custom node pack [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes) (Color Match). Install it from the ComfyUI Manager or the link, then restart ComfyUI. Without it Flux 2 is locked.

</details>

<details>
<summary><b>Qwen Image 2.1</b>: about 17.3 GB needed</summary>

| File and its ComfyUI folder | Needed for | Size | Download |
|---|---|---|---|
| `qwen_image_2.1_int8_convrot.safetensors`<br>`models/diffusion_models` | all functions | 7.3 GB | [Hugging Face: Comfy-Org/Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/diffusion_models/qwen_image_2.1_int8_convrot.safetensors) |
| `qwen3vl_8b_int8_convrot.safetensors`<br>`models/text_encoders` | all functions | 9.4 GB | [Hugging Face: Comfy-Org/Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3vl_8b_int8_convrot.safetensors) |
| `qwen_image_2.1_vae_bf16.safetensors`<br>`models/vae` | all functions | 676 MB | [Hugging Face: Comfy-Org/Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/vae/qwen_image_2.1_vae_bf16.safetensors) |

Optional (the model works without them, the named feature is greyed out):

| File and its ComfyUI folder | Feature | Size | Download |
|---|---|---|---|
| `qwen3.5_9b_w4a8_gptq.safetensors`<br>`models/text_encoders` | Enhance my Prompt with LLM, Describe Canvas, Describe Multi Image Slot, Sketch to image, Scribble on photo | 7.3 GB | [Hugging Face: Comfy-Org/MOSS-Image](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/text_encoders/qwen3.5_9b_w4a8_gptq.safetensors) |
| `qwen_image_2.1_turbo_lora_avg_rank_178_bf16.safetensors`<br>`models/loras/qwen` | Turbo LoRA | 913 MB | [Hugging Face: Comfy-Org/Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/loras/qwen_image_2.1_turbo_lora_avg_rank_178_bf16.safetensors) |
| `taeqi2_1_decoder.pth`<br>`models/vae_approx` | live preview | 15 MB | [GitHub: madebyollin/taesd](https://raw.githubusercontent.com/madebyollin/taesd/main/taeqi2_1_decoder.pth) |

</details>

<details>
<summary><b>Fibo 2.0</b>: about 13.7 GB needed</summary>

| File and its ComfyUI folder | Needed for | Size | Download |
|---|---|---|---|
| `fibo2_edit_turbo_int8_convrot.safetensors`<br>`models/diffusion_models` | all functions | 8.4 GB | [Hugging Face: Comfy-Org/Fibo-2.0](https://huggingface.co/Comfy-Org/Fibo-2.0/resolve/main/diffusion_models/fibo2_edit_turbo_int8_convrot.safetensors) |
| `qwen3vl_4b_int8_convrot.safetensors`<br>`models/text_encoders` | all functions | 4.9 GB | [Hugging Face: Comfy-Org/Krea-2](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/text_encoders/qwen3vl_4b_int8_convrot.safetensors) |
| `flux2-vae.safetensors`<br>`models/vae` | all functions | 336 MB | [Hugging Face: Comfy-Org/Flux-2-Dev](https://huggingface.co/Comfy-Org/Flux-2-Dev/resolve/main/split_files/vae/flux2-vae.safetensors) |
| `4x-UltraSharpV2.safetensors`<br>`models/upscale_models` | Upscale | 140 MB | [Hugging Face: Kim2091/UltraSharpV2](https://huggingface.co/Kim2091/UltraSharpV2/resolve/main/4x-UltraSharpV2.safetensors) |

Optional (the model works without them, the named feature is greyed out):

| File and its ComfyUI folder | Feature | Size | Download |
|---|---|---|---|
| `taef2_decoder.pth`<br>`models/vae_approx` | live preview | 3 MB | [GitHub: madebyollin/taesd](https://raw.githubusercontent.com/madebyollin/taesd/main/taef2_decoder.pth) |

**Custom node:** The tiles option of Upscale also needs the custom node pack [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes) (Color Match). Install it from the ComfyUI Manager or the link, then restart ComfyUI.

</details>

<details>
<summary><b>Krea 2 Turbo</b>: about 18.6 GB needed</summary>

| File and its ComfyUI folder | Needed for | Size | Download |
|---|---|---|---|
| `krea2_turbo_int8_convrot.safetensors`<br>`models/diffusion_models` | all functions | 13.5 GB | [Hugging Face: Comfy-Org/Krea-2](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/diffusion_models/krea2_turbo_int8_convrot.safetensors) |
| `qwen3vl_4b_int8_convrot.safetensors`<br>`models/text_encoders` | all functions | 4.9 GB | [Hugging Face: Comfy-Org/Krea-2](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/text_encoders/qwen3vl_4b_int8_convrot.safetensors) |
| `qwen_image_vae.safetensors`<br>`models/vae` | all functions | 254 MB | [Hugging Face: Comfy-Org/Krea-2](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/vae/qwen_image_vae.safetensors) |

Optional (the model works without them, the named feature is greyed out):

| File and its ComfyUI folder | Feature | Size | Download |
|---|---|---|---|
| `lighttaew2_1.safetensors`<br>`models/vae_approx` | live preview | 45 MB | [Hugging Face: lightx2v/Autoencoders](https://huggingface.co/lightx2v/Autoencoders/resolve/main/lighttaew2_1.safetensors) |

</details>

<details>
<summary><b>MOSS Image</b>: about 13.1 GB needed</summary>

| File and its ComfyUI folder | Needed for | Size | Download |
|---|---|---|---|
| `moss_image_sft_int8_convrot.safetensors`<br>`models/diffusion_models` | all functions | 5.4 GB | [Hugging Face: Comfy-Org/MOSS-Image](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/diffusion_models/moss_image_sft_int8_convrot.safetensors) |
| `qwen3.5_9b_w4a8_gptq.safetensors`<br>`models/text_encoders` | all functions | 7.3 GB | [Hugging Face: Comfy-Org/MOSS-Image](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/text_encoders/qwen3.5_9b_w4a8_gptq.safetensors) |
| `flux2-vae_small.safetensors`<br>`models/vae` | all functions | 250 MB | [Hugging Face: Comfy-Org/MOSS-Image](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/vae/flux2-vae_small.safetensors) |
| `lenovo_moss.safetensors`<br>`models/loras/Moss` | Text to Image | 65 MB | [Hugging Face: Danrisi/lenovo_moss](https://huggingface.co/Danrisi/lenovo_moss/resolve/main/lenovo_moss.safetensors) |

Optional (the model works without them, the named feature is greyed out):

| File and its ComfyUI folder | Feature | Size | Download |
|---|---|---|---|
| `lora_dmd2.safetensors`<br>`models/loras/Moss` | Turbo LoRA | 1.2 GB | [Hugging Face: lodestones/MOSS-Image-Base-8-steps-dmd](https://huggingface.co/lodestones/MOSS-Image-Base-8-steps-dmd/resolve/main/lora_dmd2.safetensors) |
| `taef2_decoder.pth`<br>`models/vae_approx` | live preview | 3 MB | [GitHub: madebyollin/taesd](https://raw.githubusercontent.com/madebyollin/taesd/main/taef2_decoder.pth) |

</details>

<details>
<summary><b>MiniMax H3 Image</b>: about 37.8 GB needed (about 29.4 GB with the smaller variant)</summary>

| File and its ComfyUI folder | Needed for | Size | Download |
|---|---|---|---|
| `minimax_h3_image_pruned_int8_convrot.safetensors`<br>`models/diffusion_models` | all functions | 21.0 GB | [Hugging Face: Comfy-Org/MiniMax-H3-Image](https://huggingface.co/Comfy-Org/MiniMax-H3-Image/resolve/main/diffusion_models/minimax_h3_image_pruned_int8_convrot.safetensors) |
| `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors`<br>`models/text_encoders` | all functions | 15.7 GB | [Hugging Face: Comfy-Org/MiniMax-H3-Image](https://huggingface.co/Comfy-Org/MiniMax-H3-Image/resolve/main/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) |
| `minimax_h3_image_vae_fp16.safetensors`<br>`models/vae` | all functions | 1.2 GB | [Hugging Face: Comfy-Org/MiniMax-H3-Image](https://huggingface.co/Comfy-Org/MiniMax-H3-Image/resolve/main/vae/minimax_h3_image_vae_fp16.safetensors) |

Smaller variant (less disk space and VRAM; in our test about as good and as fast). Take it instead of the file it names; when both are in the folder, PxC uses the larger one:

| File and its ComfyUI folder | Use | Size | Download |
|---|---|---|---|
| `minimax_h3_image_pruned_w4a8.safetensors`<br>`models/diffusion_models` | instead of `minimax_h3_image_pruned_int8_convrot.safetensors` | 12.5 GB | [Hugging Face: Comfy-Org/MiniMax-H3-Image](https://huggingface.co/Comfy-Org/MiniMax-H3-Image/resolve/main/diffusion_models/minimax_h3_image_pruned_w4a8.safetensors) |

Optional (the model works without them, the named feature is greyed out):

| File and its ComfyUI folder | Feature | Size | Download |
|---|---|---|---|
| `qwen3.5_9b_w4a8_gptq.safetensors`<br>`models/text_encoders` | Enhance my Prompt with LLM, Describe Canvas, Describe Multi Image Slot | 7.3 GB | [Hugging Face: Comfy-Org/MOSS-Image](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/text_encoders/qwen3.5_9b_w4a8_gptq.safetensors) |

</details>

<details>
<summary><b>Remove background</b> (scissors button, optional)</summary>

| File and its ComfyUI folder | Feature | Size | Download |
|---|---|---|---|
| `birefnet.safetensors`<br>`models/background_removal` | Cut out, remove background | 444 MB | [Hugging Face: Comfy-Org/BiRefNet](https://huggingface.co/Comfy-Org/BiRefNet/resolve/main/background_removal/birefnet.safetensors) |
| `rmbg-2.0.safetensors`<br>`models/background_removal` | Remove background (second model) | 885 MB | [Hugging Face: chflame163/ComfyUI_LayerStyle](https://huggingface.co/chflame163/ComfyUI_LayerStyle/resolve/main/ComfyUI/models/BiRefNet/RMBG-2.0/model.safetensors) |

RMBG-2.0 is a community copy of the official file, which needs a Hugging Face login ([official page](https://huggingface.co/briaai/RMBG-2.0)).

</details>

<!-- model-downloads:end -->

## Functions

You pick a **function** at the top, type a prompt and press **Generate**. PxC sends the picture (or the selection)
to ComfyUI and puts the result back into PhotoCraft as a new layer in a group, with a soft layer mask where that makes sense.

MiniMax H3 Image draws in a size you pick in megapixels (4 to 20 MP, best at about 16 MP); **Downsize to canvas** scales the result down to your canvas and adds it as a layer, otherwise it opens as a new document in the chosen size.

| Function | What it does |
|---|---|
| **Text to Image** | A new picture from text only, as a new layer. |
| **Expand Image** | Extend the canvas with the Crop tool, fill the new area white; PxC paints it. |
| **Fill Selection** | Select an area and type what should appear there. With Flux 3, the tab **Insert reference** puts a reference image into your rectangular selection (using Flux 3's bounding-box feature). |
| **Remove Selection** | Draw a selection around any object, with a little margin, and name it in the prompt field ("car"). It is removed and the background is filled in. With Flux 3 Klein, Flux 2 Klein and Fibo you can leave the prompt empty: their text model names the subject itself. |
| **Edit** › Edit canvas | Changes the whole picture based on your prompt, or use one of the many **Style prompts** (painting, comic, film look …). |
| **Edit** › Multi image edit | Edits the picture with reference images (drop or paste images into the slots). A click on the tag on a slot puts it where your cursor is in the prompt. |
| **Edit** › Sketch to image | Turns a sketch on a white canvas into a picture in the style you choose under **Style prompts** (photo, painting, comic …). Simply replace `SUBJECT` in the prompt box with the subject. Needs the model's prompt writer file (see [Model downloads](#model-downloads)); without it this entry of the Edit list is greyed out. MiniMax runs it without a prompt writer. |
| **Edit** › Scribble on photo | Turns scribbles on a photo into real objects: scribble in bright red or green, or on a layer of its own; only that place changes. Replace `SUBJECT` in the prompt with what goes there. |
| **Edit** › Scribble with reference | Like Scribble on photo, but with a reference image: what it shows is placed where you scribbled. Replace `SUBJECT` with what it shows ("a beagle dog"). |
| **Refine Image** | The picture is cleaned up at the same size, as a new layer. Each model has one ready-made prompt for it in the prompt field (Flux 2: neutral light, Flux 3: restore old photos, Qwen Image 2.1: keep the colours; Fibo and MiniMax use the Flux 2 text); you can edit it. |
| **Upscale** | Pick a factor (1.5x to 4x) in the row "Upscale factor": the whole picture is enlarged into a new document, up to 16 MP. |

<details>
<summary>Which model offers which function</summary>

| | Flux 3 | Flux 2 | Qwen Image 2.1 | Fibo | Krea 2 | MOSS | MiniMax |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Fill Selection | ✓ | ✓ | ✓ | ✓ | | | |
| Fill › Insert reference | ✓ | | | | | | |
| Remove Selection | ✓ | ✓ | ✓ | ✓ | | | |
| Expand Image | ✓ | ✓ | ✓ | ✓ | | | |
| Edit › Edit canvas | ✓ | ✓ | ✓ | ✓ | | | ✓ |
| Edit › Multi image edit | ✓ | ✓ | ✓ | ✓ | | | ✓ |
| Upscale (new file) | ✓ | ✓ | ✓ | ✓ (up to 3x) | | | |
| Refine Image (same size) | ✓ | ✓ | ✓ | ✓ | | | ✓ |
| Edit › Sketch to image | ✓ | ✓ | ✓ | ✓ | | | ✓ |
| Edit › Scribble on photo | ✓ | ✓ | ✓ | ✓ | | | ✓ |
| Edit › Scribble with reference | ✓ | ✓ | ✓ | | | | |
| Text to Image | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

</details>

## More features

**Results**
- **Variants:** several results as layers in one group; a **live preview** shows the picture while it is made.
- **Undo / Redo** in the header take back or bring back the last AI result.
- **History** (⋯ menu, bottom right) brings back earlier settings.

**Prompts**
- **Style prompts** add a ready-made style. **Save** keeps your own prompt under a name: you find it in Style prompts ▸ Custom prompts, and it brings back the function and model it was made for.
- **Enhance my Prompt with LLM** improves your prompt; **Reroll prompt** has the text model write a new one.
- **Describe Canvas:** an LLM describes your picture, so you can reuse the description as a prompt for Text to Image.

**Reference pictures and cut-out**
- Drop, paste (Ctrl+V) or add pictures to the **reference slots**; name a slot in the prompt with **@** or a click on its tag.
- **Cut out** (scissors, bottom right, and on every slot): removes the background with BiRefNet or RMBG-2.0 as a new layer with a mask. Needs the optional files under [Model downloads](#model-downloads).

**Queue and batch**
- While a run is on, Generate becomes **Add to queue** (Text to Image, Edit canvas, Refine Image, Upscale).
- **Batch** runs Refine Image, Upscale or Edit on all open pictures or a whole folder.
- The **queue** window (Q, or the list symbol at the bottom right) shows every waiting and running job with its progress: yours and, in team use, those of the others.

**Settings and files**
- **Save settings** / **Load defaults** at the bottom of Advanced settings; a blue dot marks a changed value.
- **Hide this model** for models you do not use; **Check files** (Model Links ▸ ⋯) finds damaged downloads.

The shortcuts work only while the PxC window is active: click into it first.

| Shortcut | Does |
|---|---|
| Ctrl+Enter | Generate |
| Ctrl+Alt+Enter | Stop the run |
| Ctrl+S | Save image |
| Q | Open the queue |
| Esc | Close the queue or the settings |

<a id="help"></a>
<details>
<summary><h2>Help</h2></summary>

| You see | What to do |
|---|---|
| The dot next to **ComfyUI** (bottom left) is red, or "ComfyUI not connected" | Start ComfyUI. If it runs on another address or port: gear ▸ **Other settings** ▸ **ComfyUI address**, then Refresh. |
| "PhotoCraft not found" when you start | Windows: run `.venv\Scripts\python.exe -m pccomfy shortcut --photocraft "C:\path\to\photocraft.exe"` in the PxC folder (type `powershell` into Explorer's address bar). Linux: `PHOTOCRAFT=/path/to/photocraft ./pxc.sh`. |
| "PhotoCraft did not open the control port" | Another PhotoCraft is already running: close all of them and start through the shortcut or menu entry. Or another program uses port 7878. |
| "No control-channel token" or "rejected the token" | PhotoCraft was started without PxC's start options. Close it and start through the shortcut or menu entry. Flatpak: see [Technical details](#technical-details). |
| "You need to download …" | Open the gear window and download the missing file, then restart ComfyUI (it reads its model folders only at start). |
| A Flux 3 download is refused | Log in to Hugging Face and accept the licence on the model page first. |
| On Linux nothing appears | Run `./pxc.sh` in a terminal; the message tells you what is missing. |
| **Enhance my Prompt with LLM** is slow, especially with 8 GB of VRAM | Start ComfyUI with `--use-ck-attention` (add it at the end of the `main.py` line in your start file). On 8 GB the prompt writers ran 2 to 5 times faster and Qwen Image 2.1 about 25 % faster, with the same quality. On 16 GB it is not needed. |

**Update.**
- Once a day at the start PxC asks GitHub for a newer version (GitHub sees your IP address and the PxC version, nothing else). Untick **Check for updates** in gear ▸ **Other settings** to stop it; **Check now** asks at once.
- A newer version shows as a blue dot on the gear, with **What's new** and **Skip this version** at the top of **Other settings**.
- To install it, download **Source code (zip)** on the release page and copy what is in its folder `pxc-<version>` over your PxC folder (replace the files), or press **Update now** if you used `git clone`. Run the setup script again only if PxC says so, then restart PxC. Your settings in `data\` (Linux: `~/.config/pccomfy/`) stay as they are.

**Report a problem.** Open an issue on this repository's **Issues** page and tell us:
- what you did, what you expected and what happened (the status line at the bottom of the window is useful);
- the **report** of PxC: gear window ▸ **Other settings** ▸ **Copy report**, then paste it into the issue. It lists the PxC version, Python, your settings and what ComfyUI and PhotoCraft answered; it contains no prompts and no access tokens.

If we ask for more: the last lines of `data\exchange\runs.jsonl` (Linux: `~/.cache/pccomfy/exchange/runs.jsonl`) have one line per run, and `last-graph.json` in the same folder is the exact request sent to ComfyUI. Both can contain your prompts, so look through them before you post.

</details>

<a id="technical-details"></a>
<details>
<summary><h2>Technical details</h2></summary>

**Install with git.**

```bash
git clone https://github.com/phil-haderer/pxc.git
cd pxc
```

**Windows, by hand** (what `setup-windows.bat` does):

```bat
py -3.13 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
:: desktop shortcut (optional)
.venv\Scripts\python.exe -m pccomfy shortcut --photocraft "C:\path\to\photocraft.exe"
:: start without the shortcut (ComfyUI running, PhotoCraft closed)
.venv\Scripts\python.exe pxc.pyw --photocraft "C:\path\to\photocraft.exe"
```

If `setup-windows.bat` said it uses Python directly, use the path in `data\python.txt` instead of `.venv\Scripts\python.exe`.
The shortcut starts PhotoCraft with a control channel for PxC (local only, protected by a token, file access limited to `data\exchange`) and then PxC, without a console window.

**Linux, by hand** (what `setup-linux.sh` does):

```bash
# create the venv with the system Python: a Python from uv or pyenv brings a Tk that does not draw the Inter font
/usr/bin/python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
./pxc.sh
# menu entry (optional)
.venv/bin/python -m pccomfy shortcut --photocraft /path/to/photocraft
```

Settings and the PhotoCraft token live in `~/.config/pccomfy/`. A different ComfyUI address or port goes into `~/.config/pccomfy/config.toml` (see `config.example.toml`). `.venv/bin/python -m pccomfy scale` shows how PxC detected the display scale.

**PhotoCraft as a Flatpak.** It is found by itself; to name it: `PHOTOCRAFT=flatpak:ai.storyteller.photocraft ./pxc.sh`. The Flatpak sandbox sees only Pictures and Documents, so PxC opens `~/.config/pccomfy` and `~/.cache/pccomfy` for the Flatpak run; that lets PhotoCraft write its token file there.

**Model files.** All files with sizes, folders and links are listed under [Model downloads](#model-downloads). The gear window lists the same files with a download button; PxC enables a model when it finds all the files for its standard settings. To keep the memory use low, release 1 uses int8 ConvRot files for most models; the exceptions are the text encoders of MiniMax (nvfp4) and Flux 2 (fp8mixed) and the prompt writers (w4a8). Some files are gated: log in to Hugging Face and accept the licence on the model page first. Flux 3 is one of them.

**Known limitations.**
- Developed and tested on Windows 11 with an NVIDIA card. On Linux it was run on Linux Mint (X11 and Cinnamon Wayland); other distributions are not tested yet.
- Linux: under X11 the window stays above PhotoCraft and minimises with it; under Wayland it is a normal window that stays on top.
- During a run, PhotoCraft briefly opens a temporary document. Please don't switch documents or change the selection while a run is going.
- A run consists of several PhotoCraft steps (history entries).
- CMYK, Lab and 16-bit documents go through 8-bit RGB.

</details>

## License

Dual-licensed under [MIT](LICENSE-MIT) or [Apache-2.0](LICENSE-APACHE), at your option. The models are not part of this
repository and have their own licences (on each model's page).
