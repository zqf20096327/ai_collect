# 🍑 Pink Peach

**A ComfyUI node pack tailored for Krea 2 Turbo.** A complete generation pipeline — from model loading to image saving — packed into streamlined nodes with intuitive settings, live interactive graphs, and a pink aesthetic UI.

> Turbo models are lightning fast but notoriously finicky: they dislike CFG, ignore standard negative prompts, and tend to generate identical facial features across different seeds. Pink Peach solves these quirks natively — offering NAG for negative guidance at CFG 1, Variance for diversity, and custom schedulers & samplers for rich detail.

---

## ✨ Features

- **All-in-One Loader** — Load UNET, CLIP (Qwen3-VL), and VAE in a single node, featuring automatic fp8 text encoder unpacking to full precision.
- **Up to 10 LoRAs in One Node** — Layer-depth surgery (composition / shape / details), interactive weight curve controls, and an overbake cleanup filter.
- **True Negative at CFG 1** — The NAG node pushes generation away from negative concepts directly inside the model's cross-attention layers.
- **Cross-Seed Diversity** — The Variance node injects semantic noise during early steps to produce diverse poses, layouts, and face shapes.
- **Custom Schedulers & Samplers** — Built-in 🌸 presets, an interactive 🧪 lab with sliders and canvas curve handles, plus preset saving.
- **Model Schedule Calibration** — The Schedule Calibrator tailors low-step schedules (e.g., 4 steps) to mirror full-step generations with minimal loss.
- **Prompt from Image & Idea** — Qwen Caption and Scene Builder leverage the built-in Qwen3-VL text encoder without extra models.
- **Post-Processing Suite** — Color correction, skin tones, wetness speculars, halation, clarity, LUT (.cube), bloom, sharpening, chromatic aberration, vignette, and analog film grain.
- **Advanced Inspection & Viewer** — A/B comparison with a magnifying loupe, split wipe, spacebar flicker, fullscreen mode, session filmstrip, and color palette extraction.
- **Custom UI Suite** — Dedicated Run bar, interactive minimap, picture-in-picture live preview, "Done!" notification chimes, custom themes, and an in-app Theme Creator.

---

## 🚀 Quick Start (Krea 2 Turbo)

**Model Pipeline:** Loader → LoRAs → Model FX → (NAG) → Custom Sigmas → Core Sampler → VAE Decode → Post-Process → Compare & Save
**Prompt Pipeline:**Prompt Encoder → (Variance) → positive input of Core Sampler

**Recommended Settings:**

| Parameter | Value | Notes |
|---|---|---|
| steps | `8` | Turbo benchmark; more than 10–12 is typically unnecessary |
| cfg | `1` | Anything higher doubles compute time and over-saturates colors |
| scheduler | `simple` + shift `0` | Krea standard baseline; alternative: `🌸ays_shift` + shift `1.0` |
| sampler | `euler` | Fastest baseline; `🌸euler_tail` provides cleaner micro-detail for +2 passes |

> ⚠ Always route the model into the sampler **from the MODEL output of Custom Sigmas**, rather than directly from the loader — otherwise, the shift calculation will mismatch between the scheduler and the model.

---

## 📦 Nodes

### Loading
| Node | Functionality |
|---|---|
| 📦 **Loader** | Loads UNET, CLIP, and VAE in a single node. Supports custom directory paths and automated fp8 CLIP unpacking (`clip_precision: auto`). |
| 💞 **LoRAs** | Up to 10 LoRAs with individual weights, bypass switches, and trigger copy. Depth control (`early / mid / late`) via an interactive graph, preset curve profiles, and 🧽 Overbake clean. |

### Prompting
| Node | Functionality |
|---|---|
| ✍️ **Prompt Encoder** | Encodes prompts using system presets. Performs orthogonal negative vector projection from positive space — ideal for CFG 1 workflows. |
| 📝 **Text** | Combines `text_before` + text + `text_after` without cumulative concatenation on re-runs. Supports disk export. |
| 🎨 **Moodboard** | Appends structured visual style descriptions from the moodboard catalog (concise / normal / strong). |
| 🎬 **Scene Builder** | Assembles scenes slot-by-slot (subject, appearance, attire, pose, location, lighting, camera angle, style, mood). Slot modes: random, library picker, custom text, Qwen-generated, or bypassed. Natural language concepts are auto-parsed across slots by Qwen. |
| 💬 **Qwen Caption** | Generates detailed prompts from input images or expands rough concepts. Modes: Krea prompt, Short caption, Tags, Style only, and Custom. |

### Canvas & Seed
| Node | Functionality |
|---|---|
| 📐 **Resolution** | Generates empty latents at target dimensions with aspect presets, mod-16 auto-rounding, and a ⇄ Flip button. |
| 🎲 **Seed** | Unified seed management across the entire graph. |

### Model Tuning
| Node | Functionality |
|---|---|
| ✨ **Model FX** | **Enhancer** — adjust prompt token contrast and cross-attention text weight; **Detail** — inject micro-detail (Sigma / Frequency / Both) across target step ranges. Negative detail yields smoothed, glamour skin. |
| 🚫 **NAG** | Enforces true negative prompting at CFG 1. Cost: ≈1.5–2× slower inference. |
| 🎭 **Variance** | Induces structural variety across seeds: Random, Composition, Texture, Expression, Grit, Soft, and Facial asymmetry. Features prompt protection zones, fade-out decay, and a late-step detail-only mode. |

### Schedulers & Samplers
| Node | Functionality |
|---|---|
| 📈 **Custom Sigmas** | Step distribution control: standard schedules, 🌸 presets (`ays_shift`, `megapixel`, `soft_landing`, `sculptor`, `upscale_refiner`, `sakuga`), and a 🧪 lab. Interactive curve with hover telemetry, step preview frames, and direct curve handles. |
| 🍑 **Core Sampler** | Advanced sampler featuring structured noise profiles (White, Velvet Pink, Subsurface Warmth, Chiaroscuro, Anisotropic), variations, and a 🧪 lab (base method, heun_tail, eta, noise bands, restart). Custom 🌸 samplers: `euler_tail`, `clean_ode`, `restart`, `momentum`, `velvet_sde`, and `freq_sde`. |
| 📐 **Schedule Calibrator** | Calibrates an optimized low-step schedule for a specific checkpoint by matching structure and texture metrics against a high-step baseline across multiple seeds. Exports as a 📐 preset. Computationally heavy (hundreds of evaluation passes), but executed only once per model. |

### Image Processing
| Node | Functionality |
|---|---|
| 🧁 **VAE Decode** | Latent decoding featuring pre-conversion tonal depth enhancements and subtle micro-sharpening. |
| 🌈 **Post-Process** | Exposure, contrast, saturation, melanin shift, wet specular highlights, film halation, clarity, LUT (.cube), bloom, sharpening, chromatic aberration, vignetting, and analog grain. Supports alpha masking. |
| 💾 **Compare & Save** | Side-by-side A/B image analysis: interactive loupe, wipe curtains, spacebar flicker, fullscreen inspection, session history filmstrip, slideshow mode, and palette sampling. Saves to PNG (with embedded metadata) or compressed JPEG. |
| 📂 **Load Image** | Loads local images from disk. |

### Workflow Utilities
| Node | Functionality |
|---|---|
| 🔀 **Router** | Conditional switch passing one of two inputs through. |
| 🧩 **Groups ON/OFF** | Canvas group toggles (operates like inline bypass — preserving execution integrity). |
| 🎛 **Master Remote** | Centralized dashboard: gathers widgets from scattered nodes into a single control surface. |
| 📁 **Preset Manager** | Serializes and restores full graph parameters via unified configuration files. |
| 📍 **Jump** | Canvas navigation bookmarks mapped to hotkeys. |
| 🗒 **Note** | Rich formatted sticky notes; unformatted text can be routed downstream as prompt strings. |
| 🧾 **Reporter** | Compiles comprehensive parameter audit reports to reproduce specific outputs. |
| 🔊 **Save Audio** | Audio export node (flac / wav / mp3). |
| 🎞 **Filmstrip** | Sequential step reel tracking progressive latent denoising. |
| 📊 **System Monitor** | Live telemetry for GPU load, VRAM allocations, CPU utilization, and system RAM with 60-second history curves. |
| 🎨 **Color Box** | Palette curator mapping colors into prompt tokens (~245 color dictionary matched via CIEDE2000). |
| 💖 **Heart** | Aesthetic dashboard: particle canvas effects and daily successful generation counters. |

---

## 🌸 UI & Themes

Under ComfyUI Settings → **Pink Peach**:

- **Pink Run bar** — Custom floating execution bar: batch sizing, trigger modes, instant cancel, queue flush, and execution history.
- **Pink minimap** — Color-coded overview map tracking groups and active processing nodes.
- **Picture-in-picture** — Floating viewport rendering live step previews.
- **Done sound** — Audio chimes and OS notifications on queue completion (bundled presets or custom audio).
- Candy progress indicators, heart pulses along connections, pastel bus links, falling sakura petals, custom cursor trails, and the Nunito UI typeface.
- **Theme Creator** (Right-click canvas) — Custom workspace palette designer.

### ⌨ Keyboard Shortcuts

| Shortcut | Action |
|---|---|
| `Alt+R` | Focus Master Remote |
| `Alt+T` | Focus Text node (cursor auto-focused inside input) |
| `Alt+S` | Focus Compare & Save |
| `Alt+V` | View current Compare & Save image in fullscreen |
| `Alt+Enter` / `Alt+Shift+Enter` | Queue Prompt / Queue to Front |

Rebindable via Settings → Keybinding → "Pink Peach". Fully compatible with multilingual keyboard layouts.

---

## 🍰 Recipes

- **Single Image Variations** — Route Seed 1 → sampler seed (fixed), Seed 2 → variation_seed (randomize), variation_strength `0.1`.
- **Image-to-Prompt** — Route Load Image → Qwen Caption (mode: Krea prompt, length: long) → text_before in Text node → prompt in Prompt Encoder.
- **Diverse Faces** — In Variance: mode Facial asymmetry, strength `40`, protect First Quarter.
- **Enhanced Micro-Detail** — In Model FX: detail `0.2` (Sigma mode), sampler `🌸euler_tail`, Post-Process sharpness `0.25`.

---
## 🔧 Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/pink-qink/ComfyUI-Pink-Peach.git
Restart ComfyUI
Optional dependencies: For GPU load and temperature readouts in System Monitor, ensure pynvml or the nvidia-smi utility is present (otherwise, only VRAM metrics are reported). To enable the Filmstrip and step-by-step progress previews, set Live preview to enabled in ComfyUI settings.

📂 Repository Structure
`lora_triggers.txt` LoRA trigger index and baseline weights: lora_name "trigger1, trigger2" weight: 0.85
`system_presets.json / negative_presets.json` Preset definitions for Prompt Encoder
`lab_presets.json` Saved 🎀 schedules, samplers, and 📐 calibration data
`luts/` Color lookup tables (.cube)
`themes/` Workspace aesthetic
`themesnotes/` Workspace notes and local documentation
`gen_presets/` Serialized parameter snapshots for Preset Manager
`mood/` Style moodboard catalog
`pinky/notification/` Audio assets for queue completion alerts

An in-depth, widget-by-widget breakdown for every node is available in the local guide inside the nodepack (notes/).

💗 Made with love