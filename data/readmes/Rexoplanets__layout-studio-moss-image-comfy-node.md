# The Layout Studio for MOSS-Image (ComfyUI node)

Take the guesswork out of creating bounding-box layouts for [MOSS-Image](https://github.com/OpenMOSS/MOSS-Image/tree/main) with this free, open-source, visual spatial-precision layout editor designed specifically to generate reliable JSON bbox prompts for MOSS-Image for use with ComfyUI.

**NOTE**: This is the **custom node for ComfyUI**. For the original standalone web app, [click here](https://github.com/Rexoplanets/layout-studio-moss-image).

<p align="center">
  <img src="./standalone_app/assets/images/screenshots/layout-studio-items-tab-hero.webp" width="800" alt="The Layout Studio for MOSS-Image"><br>
  <em>The Layout Studio for MOSS-Image</em>
</p>

### 🚀 **[Launch the Live Web Demo](https://rexoplanets.github.io/layout-studio-moss-image/Layout_Studio_for_MOSS_Image.html)**
*(No installation required — runs directly in your browser. Prefer offline use? Download the latest release from the [Releases](../../releases/latest) page or [load it directly in ComfyUI](#getting-started).*

---

## Table of Contents
- [Overview](#overview)
- [Who needs a layout builder for MOSS-Image?](#who-needs-a-layout-builder-for-moss-image)
- [Main Features](#main-features)
  - [Dynamic Canvas](#-dynamic-canvas)
  - [Item Management](#%EF%B8%8F-item-management)
  - [Reference Background Image](#%EF%B8%8F-reference-background-image)
  - [Meta Tags & Palette Management](#%EF%B8%8F-meta-tags--palette-management)
  - [Danbooru & Anime Compatible](#-danbooru--anime-compatible)
  - [Multi-Format Exporting](#%EF%B8%8F-multi-format-exporting)
  - [JSON Import with Smart Dimension Matching](#%EF%B8%8F-json-import-with-smart-dimension-matching)
  - [Lightweight & Fast](#-lightweight--fast)
  - [Additional Features](#additional-features-include)
- [Caveats & Hints](#caveats--hints)
- [Getting Started](#getting-started)
- [File Structure](#file-structure)
- [License](#license)
- [About MOSS-Image](#about-moss-image)
- [Tips are welcome](#tips-are-welcome)
- [Changelog](#changelog)


---
## Overview

If, like me, you've been intrigued by the use of "bounding boxes" (or "bboxes" for short) to lay out complex compositions with better accuracy, you've encountered the same obstacles as I had:

- Crafting JSON prompts by hand is a non-starter.
- Even state-of-the-art LLMs like GPT-4o have a hard time converting natural-language or tag-based prompts into sub-pixel *yxyx* coordinate space (`-500` to `500` centered) JSON prompts.

**The Layout Studio for MOSS-Image** ComfyUI node fixes all that.

**Use the Studio right in ComfyUI to lay out what you want where**. Just hook the JSON Output to your positive prompt node and generate.

---

## Who needs a layout builder for MOSS-Image?

- <ins>**Fans of MOSS-Image:**</ins> Love MOSS-Image and want to take your gens to the next level by mastering its native spatial precision via bbox coordinates, but without all the trail-and-error when using LLMs? Hook the node to your positive-prompt node, build your images visually on a drag-and-drop canvas while the Studio handles all schema math automatically.

- <ins>**Multi-Character & Anime Creators:**</ins> Sick of so-called 'concept bleed' (mixing of traits, outfits, etc.) in multi-subject scenes? The bounding-box features of new models like Ideogram 4 and MOSS-Image is the next-gen equivalent of [regional prompting](https://stable-diffusion-art.com/regional-prompter/), and may be adopted by future models, as well. Use the Layout Studio to keep those characters separated.

- <ins>**Visual Designers & Typographers:**</ins> Need text placed where it belongs? Position headers, typography, and logos with greater visual accuracy for posters, album covers, and banners.

- <ins>**Product & E-Commerce Visual Creators:**</ins> Structure studio product shots, hero element placements, and advertising layouts while locking canvas aspect ratios and target megapixel presets (`~1 MP` to `~4 MP`).

- <ins>**Storyboard & Comic Artists:**</ins> Easily block out multi-panel sequence compositions and background layouts using native `multi_panel` and `collage` canvas modes.

- <ins>**Cross-Model Power Users:**</ins> Compose layouts visually over a reference image, then apply the structured MOSS-Image JSON schema, or copy a text-only prompt for refining with img2img or inpainting with a natural-language model like Krea 2 or a tag-based model like Illustrious, or any other model in your stack for that matter.

---

## Main Features

### 🎨 Dynamic Canvas
<p align="center">
  <img src="./standalone_app/assets/images/screenshots/canvas-dimensions-presets-type.webp" width="800" alt="Dynamic Canvas"><br>
</p>

- Automatically scales to fit any display or window size while maintaining target aspect ratios (`1:1`, `2:3`, `3:4`, `9:16`, `9:21`, `3:2`, `4:3`, `16:9`, `21:9`) and target megapixel values (`~1 MP` to `~4 MP`).
- Workspace dimensions dynamically adapt on the fly without clipping or off-screen overflow.
- The built-in visual grid, with optional grid snapping, aligns directly to MOSS-Image's requirement that canvas and bounding box dimensions follow 16-pixel multiples.
- Visual alignment crosshairs automatically highlight when an item's center point aligns horizontally or vertically with the center of the image.

---

### ⬆️ Item Management
<p align="center">
  <img src="./standalone_app/assets/images/screenshots/canvas-item-highlight.webp" width="600" alt="Item Managements"><br>
</p>

- Create scene elements with MOSS-native `text`, `object`, or `character` item types using color-coded boxes and corresponding "cards" that you can reorder with drag-and-drop in the Items tab. This also reorders the items in the exported output.
- Drag, resize, and nudge bounding boxes visually on a canvas mapped directly to MOSS-Image's standardized centralized coordinate space (`abs_centralized`, `yxyx` format from `-500` to `500`).
- Toggle individual bounding boxes on or off to preview layout variations or temporarily exclude specific elements from schema generation without deleting card data.
- Switch seamlessly between overall scene settings and bounding-box management in one minimal strip.
- Intelligent auto-focus opens item details immediately when interacting with bounding boxes on the canvas.

---

### 🖼️ Reference Background Image
<p align="center">
  <img src="./standalone_app/assets/images/screenshots/layout-studio-ref-image.webp" width="800" alt="Reference Background Image"><br>
</p>

- Insert a reference image "under" the canvas, with adjustable opacity to visually align bounding boxes directly over an existing composition.
- **NEW** (v1.1.0): Import the MOSS-Image JSON prompt and canvas size if the reference image is a .PNG file with metadata containing a MOSS-Image JSON prompt. Verified to work with .PNGs generated by: ComfyUI, Civitai Online Generator, Tensor Art Creation workspace.

---

### 🏷️ Meta Tags & Palette Management
<p align="center">
  <img src="./standalone_app/assets/images/screenshots/meta-tags-palette.webp" width="400" alt="Meta Tags & Palette Management"><br>
</p>

- Add preset or custom style meta tags and hex or named color palettes to set global scene styling.

  ⚠️ **Note:** Meta Tag and Palette values are overridden by any competing value in the prompt text. Describing media, styles, colors, and other details directly in the prompt text will often have a stronger impact on the image output than Meta Tags or Palette values.

---

### 🦋 Danbooru & Anime Compatible

- Use the dual-tabbed Meta Tag manager, featuring natural-language style tags alongside anime/Danbooru preset tags (`cel shading`, `masterpiece`, `cowboy shot`, etc.).
- Supports parenthesis weighting syntax `(tag:1.2)`
- In-app link to Safebooru tag search.

---

### ↘️ Multi-Format Exporting
<p align="center">
  <img src="./standalone_app/assets/images/screenshots/layout-studio-apply-comfyUI.webp" width="550" alt="Multi-Format Exporting"><br>
</p>

- Instantly generate and copy a MOSS-Image central-coordinate JSON schema, OR:
- A text-only prompt in natural language or tag-based format, depending on your needs. This is useful for refining or re-creating the image using a different model that doesn't understand JSON prompts, such as Krea 2, Illustrious, H3-Image, etc.

---

### ↗️ JSON Import with Smart Dimension Matching
<p align="center">
  <img src="./standalone_app/assets/images/screenshots/layout-studio-import.webp" width="550" alt="JSON Import with Smart Dimension Matching"><br>
</p>

- Import existing MOSS-Image JSON prompts to inspect, modify, and visually re-edit them on the Layout Studio canvas.
- Specify or import width and height values, with automated preset detection to match standard aspect ratio and megapixel configurations while enforcing 16-pixel multiples.
- Import existing MOSS-Image JSON prompts and canvas sizes from an existing .PNG file with metadata. Verified to work with .PNGs generated by: ComfyUI, Civitai Online Generator, Tensor Art Creation workspace.

---

### 🪶 Lightweight & Fast

- Lightweight, single-file HTML architecture built entirely with vanilla JavaScript and local Tailwind/Lucide scripts.
- No external servers or network calls required.

---

### Additional features include:

- UI Typography Scaling (A- / A+)
- Undo/Redo
- Keyboard Shortcuts
- Persistent Local Storage - prevents data loss across page refreshes
- System Cache & Heap Management - clear the cache to empty & reset storage

---

## Caveats & Hints

Keep these in mind when using bboxes with MOSS-Image:

<table><tr><td><strong>PROMPTS HAVE THE FINAL WORD<strong></td></tr></table>

For a given Item, any positions you include in its Caption/Prompt field will determine where the item ends up being shown in the image — even if you placed its bbox on the opposite side.

For example, if in the Caption for a Character Item you write, "<samp>a boy holding a stick on the left</samp>" and for a second Character Item you enter, "<samp>a dog on its hind legs on the right</samp>", MOSS-Image will follow these written instructions — even if you drag the bboxes of the boy and dog elsewhere.

So: when entering your captions, *refrain from mentioning any absolute positions of the Item*:

❌ <samp>a boy holding a stick on the left facing the dog</samp>\
✅ <samp>a boy holding a stick facing the dog</samp>

❌ <samp>a dog on its hind legs on the right facing the boy</samp>\
✅ <samp>a dog on its hind legs facing the boy</samp>

**The same rule applies to Meta Tags and Palette values**: if in the Summary you mention that the scene takes place during the golden hour but in the Palette field you enter "at night", MOSS-Image will set the scene during the golden hour, though perhaps with slightly darker shadows.

<table><tr><td><strong>BBOXES ARE NOT PIXEL-PERFECT<strong></td></tr></table>

With this initial version of MOSS-Image, even if you use the Studio, MOSS-Image does not necessarily respect the exact layout you give it.

For now, bounding boxes indicate where elements *should* be positioned and how large or small they *should* appear. Text Item placement is more accurate than Object or Character Item placement, but in general, MOSS-Image will ultimately decide where exactly the Item is shown and how much it does or doesn't remain confined by its bbox boundaries.

<table><tr><td><strong>KEEP CFG ≥ 2.5<strong></td></tr></table>

Even with the most painstakingly fine-tuned layout, if you try to gen it with < 2.5 CFG, don't be surprised if your Items end up all over the place.

For optimal results, OpenMOSS [recommends](https://github.com/OpenMOSS/MOSS-Image/blob/main/USERGUIDE.md) ≥ 50 steps, 1.5 MP or 2 MP, and 3-6 CFG:

> Default 3.0 (recommended range: 3.0–6.0). A value of 3.0 is generally sufficient for long prompts; for short prompts, we recommend increasing it as needed.

I've found a CFG @ 2.5 respects the layout even with fewer steps @ 1 MP, which makes it perfect for quickly testing your layouts before generating them at ≥ 1.5 MP.

---

## Getting Started

1. Open **ComfyUI-Manager** and click **Install via Git URL**.
2. Paste the repository URL: `https://github.com/Rexoplanets/layout-studio-moss-image-comfy-node`
3. Install and **restart ComfyUI**.
4. Open/navigate to the workflow in which you want to use the Studio.
5. ⚠️ **Important** — Refresh or hard-refresh the page, otherwise the "Open Layout Studio" button on the node won't appear. (This only needs to be done once, until an updated version of the node is installed.)
6. Add **The Layout Studio for MOSS-Image** from the **MOSS-Image** node category to your workflow
7. Hook the *JSON prompt* output to whichever node handles your workflow's positive prompt.

    ⚠️ **Important — Do Not Use with the Prompt-Enhancer Node:**

    Connect the **`JSON prompt`** output directly to your MOSS-Image workflow's prompt/text-encoder node. Passing it through the MOSS-Image prompt-enhancer node will rewrite the text and break the structured JSON layout format.

<p align="center">
  <img src="./standalone_app/assets/images/screenshots/layout-studio-hook-node-comfyUI.webp" width="700" alt="Multi-Format Exporting"><br>
</p>

6. Click the **Open Layout Studio** button. (If the button doesn’t appear, refresh the page.)

If the node doesn’t appear, check that its folder is directly inside `custom_nodes`, then look in ComfyUI’s startup console for import errors. A full restart is needed after installing a custom node.

---

## File Structure:

```
standalone_app/Layout_Studio_for_MOSS_Image.html     All-in-one visual studio interface & logic
standalone_app/assets/js/
    tailwind.js                       Local Tailwind CSS framework runtime (zero network dependency)
    lucide.js                         Local Lucide UI icon renderer (zero network dependency)
standalone_app/assets/images/         Logos
standalone_app/assets/moss-image-meta-tag-palette-suggestions.html   Cheatsheet of classic tags used for AI-image generation
__init__.py                           Required ComfyUI file
pyproject.toml                        Required ComfyUI Registry file
web/extension.js                      App wrapper for ComfyUI
nodes.py                              Required ComfyUI file
```

---

## Feedback & support

Encountered a bug or have a feature request? [Report an issue here on GitHub](https://github.com/Rexoplanets/layout-studio-moss-image-comfy-node/issues). If you don't have a GitHub account, leave a comment on the Civitai article : [Civitai.red](https://civitai.red/articles/38547/moss-image-layouts-made-easy-with-the-free-layout-studio-app) / [Civitai.com](https://civitai.com/articles/38547/moss-image-layouts-made-easy-with-the-free-layout-studio-app).

---

## License

Released open-source under the [GNU GPL v3 Licence](https://www.gnu.org/licenses/gpl-3.0.html#license-text). Independent community tool, not affiliated with OpenMOSS.

---

## About MOSS-Image

To make the most of MOSS-Image, be sure to [read its official User Guide](https://github.com/OpenMOSS/MOSS-Image/blob/main/USERGUIDE.md).

---

## Tips are welcome

If you find this tool useful, feel free to toss me some Buzz on Civitai: [Civitai.red](https://civitai.red/models/3051607/the-layout-studio-for-moss-image-draw-your-bbox-prompt-then-paste-the-json-in-any-generator) / [Civitai.com](https://civitai.com/models/3051607/the-layout-studio-for-moss-image-draw-your-bbox-prompt-then-paste-the-json-in-any-generator) 🤙

---

## Changelog

### Version 1.1.1

*22 November 2026*

- Initial Release. Instead of launching with "1.0.0", this initial release version aligns with the current version 1.1.1 of [the standalone web app](https://github.com/Rexoplanets/layout-studio-moss-image), in order to avoid any confusion.

---
