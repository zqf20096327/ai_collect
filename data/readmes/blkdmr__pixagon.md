<!-- Original work Copyright 2026 Valentyn Karachevtsev (SpriteLoom)
     Licensed under the Apache License, Version 2.0
     Modifications Copyright 2026 Alessio Russo (Pixagon) -->

# Pixagon: an AI pixel-art assistant for Aseprite

Generate sprites from a text prompt, edit an existing sprite with a plain instruction, or redraw only a selected region. All of it runs inside Aseprite, on your own GPU or through an optional cloud provider if you don't have one.

Pixagon is an Aseprite extension. You stay in the editor the whole time. Results open in a side window, and a click drops one into your sprite as a new layer. Pixagon never edits your existing pixels.

<p align="center">
  <img src="assets/gallery/goblin.png" width="160" alt="Goblin with a dagger">
  <img src="assets/gallery/cottage.png" width="160" alt="Timber cottage">
  <img src="assets/gallery/coin.png" width="160" alt="Gold coin with a crown">
  <img src="assets/gallery/adventurer.png" width="160" alt="Adventurer in a leather coat">
</p>
<p align="center"><em>Made with Pixagon, one generation each.</em></p>

## What it does

**Generate:** make a sprite from a text prompt ("wooden cottage, thatched roof").
**Edit with AI:** change a sprite by instruction ("make the sword glow blue"). Style and everything you did not mention stays put.
**Inpaint Selection:** the same, but it only touches the region you selected.
**Rotate + Instruct:** view the same subject from another angle, for turnarounds.

<p align="center">
  <img src="assets/gallery/tall-man.png" width="160" alt="Tall man in a cloak, three-quarter view">
  <img src="assets/gallery/tall-man-front.png" width="160" alt="The same man seen from the front">
</p>
<p align="center"><em>Rotate + Instruct: the same character from two angles.</em></p>

Output goes through a pixel-art postprocess step: palette quantization, background removal, optional mirror symmetry, and fit-to-canvas, so results land clean at your sprite size.

## Two ways to run it

Pick one in Setup. You can change it later.

**Local GPU (private, free to run).** Pixagon runs the FLUX.2 Klein 4B diffusion model on your own computer. Nothing leaves your machine.

- **GPU:** NVIDIA with 12+ GB VRAM, or an Apple Silicon Mac (M1 or newer, macOS 14+). 8 GB NVIDIA cards work in a slower "Legacy 8 GB" mode.
- **RAM:** 16 GB minimum. On a Mac, 24 GB or more of unified memory is recommended.
- **Disk:** about 15 GB for the model, downloaded by Setup.

**OpenRouter (cloud, no GPU needed).** No NVIDIA GPU, no Apple Silicon Mac, or a card that is too weak? Use an OpenRouter image model instead. There is no 15 GB download. Paste your OpenRouter API key into Setup and go. The default model is google/gemini-2.5-flash-image, and you can type any OpenRouter model that returns images. Things to know:

- Requests are billed to your own OpenRouter account.
- Your prompts, and the sprite and selection you edit, are sent to OpenRouter and the model's provider.
- Cloud models are slower per picture and follow the seed less closely.
- Results still go through the same pixel-art cleanup as local ones.

There is no CPU fallback for the local model, and AMD cards and Intel Macs are not supported locally. OpenRouter works on any machine that runs Aseprite.

**Both:** Aseprite 1.3 or newer, on Windows, Linux (NVIDIA driver with CUDA 12.8 for local) or macOS.

## Install

1. Download the .aseprite-extension file and double-click it, or use Edit > Preferences > Extensions > Add Extension in Aseprite.
2. Open the Pixagon panel. Setup opens by itself if something is missing. You can also open it from the Pixagon Setup... command or the Setup... button on the panel.
3. Pick a provider: Local GPU or OpenRouter (type your API key and press Save OpenRouter settings). Press Install. It installs uv and a Python environment, plus the 15 GB model for Local GPU only. You do not need Python installed first.
4. The panel starts the server for you once everything is installed. Type a prompt and generate.

One file works on every OS. Everything Pixagon downloads lives in a per-user folder (%APPDATA%\Pixagon, ~/Library/Application Support/Pixagon or ~/.config/pixagon), not inside the extension, so updating the extension never wipes your model.

Pixagon is free, or pay what you want. The source stays open if you prefer to build it yourself.

## Your first sprite

**1. Open Pixagon.** Both commands live in the Sprite menu: Pixagon... (F1) opens the panel, Pixagon Setup... opens Setup.

<p align="center">
  <img src="assets/preview/navbar.png" width="233" alt="Aseprite Sprite menu with the Pixagon... and Pixagon Setup... commands">
</p>

**2. Run Setup once.** Pick a provider, enter your details (here an OpenRouter model and API key) and press Install. When every line reads [ok], you are ready.

<p align="center">
  <img src="assets/preview/setup-menu.png" width="420" alt="Pixagon Setup dialog with OpenRouter selected and every install step marked ok">
</p>

**3. Describe the sprite.** In the panel, pick a task, a view and a subject, set the size and how many variants you want, then press Run. The status box shows the exact text Pixagon will send.

<p align="center">
  <img src="assets/preview/generation-menu.png" width="420" alt="Pixagon panel set to Generate, 3/4 view, subject wizard's staff, 128x128, 4 variants">
</p>

**4. Pick a variant.** The results open in a side window. Click the one you like.

<p align="center">
  <img src="assets/preview/variant-menu.png" width="360" alt="Results window with four wizard's staff variants">
</p>

**5. Keep drawing.** The variant lands in your sprite as a new layer, ready to touch up by hand.

<p align="center">
  <img src="assets/preview/aseprite-injection.png" width="360" alt="The chosen wizard's staff inserted into the Aseprite canvas">
</p>

## Status

The single-file extension is new. It has been run end to end on Linux with the OpenRouter provider. The local model on Windows and macOS still needs more real-hardware testing. If something misbehaves, please report what you see in the comments or on GitHub.

## Open source and licenses

Pixagon is open source under Apache 2.0, and is a derivative work of [SpriteLoom](https://github.com/vkarach/spriteloom) by Valentyn Karachevtsev. The FLUX.2 Klein 4B model is licensed separately by Black Forest Labs under Apache 2.0 and is downloaded at runtime, not redistributed.

Source, samples and docs: [github.com/blkdmr/pixagon](https://github.com/blkdmr/pixagon) and [blkdmr.github.io/pixagon](https://blkdmr.github.io/pixagon)
