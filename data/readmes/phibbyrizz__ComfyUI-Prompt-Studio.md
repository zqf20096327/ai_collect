<p align="center">
  <img src="assets/prompt-studio-hero.png" alt="Prompt Studio for ComfyUI" width="100%">
</p>

# ComfyUI Prompt Studio Suite v3.3

**Turn a reference image and a simple idea into a production-ready image prompt or MiniMax H3 video script — directly inside ComfyUI.**

Prompt Studio sends the reference image to multimodal models through OpenRouter and combines that visual context with your creative direction. A small built-in helper node also reports the reference image's closest standard aspect ratio so you can match that ratio in the image or video generator you use afterward.

## What's new in v3.3

- `AspectRatioDetector` is now included directly with Prompt Studio.
- No separate mystery aspect-ratio node pack is required.
- Aspect ratio is a user-facing readout only; it is not injected into Still or Video prompt context.
- The detector is intentionally simple: `IMAGE -> aspect_ratio_str`.
- Public workflow ships with the OpenRouter API-key field blank.

## Features

- **Reference-aware prompting:** Uses the supplied reference image as multimodal visual context.
- **Aspect Ratio Readout:** Reports friendly ratios such as `2:3 (Classic Portrait)`, `3:2 (Classic Landscape)`, `16:9 (Landscape)`, and `9:16 (Portrait / Story)`.
- **Dual Engine Architecture:**
  - **Track A — Still Prompt Studio:** Leave Still Direction blank for faithful reconstruction guidance, or add creative direction to modify the scene.
  - **Track B — MiniMax H3 Video Script:** Produces a structured video prompt with shots, timing, camera direction, soundscape, and music cues.
- **Independent directions:** Still and Video directions can be controlled separately.
- **Switchboard Control:** Run either track independently.
- **Target Model:** Tailor the still prompt-writing style for Generic, FLUX, Krea 2, or SDXL.

## Required Custom Nodes

Install these through ComfyUI Manager:

| Node Pack | Required Nodes |
|---|---|
| ComfyUI-Custom-Scripts | `ShowText|pysssss` |
| ComfyUI-KJNodes | `StringConstant` |
| rgthree-comfy | `Fast Bypasser (rgthree)` |
| comfyui-openrouter | `OpenRouterNode` |

`AspectRatioDetector` is included with Prompt Studio itself.

OpenRouter usage requires an OpenRouter account and may incur API charges depending on the model selected.

## Installation

### ComfyUI Manager / Registry

Once Prompt Studio is published to the Comfy Registry, install **Prompt Studio Suite** from ComfyUI Manager and restart ComfyUI.

### Manual

Clone or download this repository into:

`ComfyUI/custom_nodes/ComfyUI-Prompt-Studio`

Restart ComfyUI afterward.

If you previously installed the old standalone `ComfyUI_AspectRatioDetector` test/local folder, remove it from `custom_nodes` to avoid registering the same legacy node twice.

## Quick Start

1. Install the required node packs above and restart ComfyUI.
2. Open `prompt_studio_v3.json`.
3. Enter your OpenRouter API key in **OpenRouter API Key**.
4. Load a reference image.
5. Confirm **Detected Aspect Ratio** reports the reference shape.
6. Optionally enter Still Direction and/or Video Direction.
7. Select the track(s) you want and queue the workflow.
8. Use the resulting prompt/script in your target image or video generator, matching its output aspect ratio to the displayed reference ratio when desired.

## Aspect Ratio Detection

Prompt Studio's built-in detector intentionally does one job: it maps the reference image dimensions to the closest common aspect ratio and displays that ratio.

It does **not**:
- resize the image,
- choose a generation resolution,
- inject aspect-ratio instructions into the AI prompt,
- or control an external image/video generator.

This keeps the readout deterministic while leaving generation settings under your control.

## API Key Safety

Never publish or share a workflow after entering your personal OpenRouter API key without removing the key first. The repository's public workflow is distributed with this field blank.

## Outputs

- **Still track:** production-ready still-image prompt.
- **Video track:** MiniMax H3-oriented production script.
- **Detected Aspect Ratio:** friendly reference ratio for matching downstream generation.

## License

See `LICENSE`.
