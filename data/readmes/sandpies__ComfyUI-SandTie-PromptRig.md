# ComfyUI SandTie PromptRig (H3)

> Mirror on Hugging Face: [https://huggingface.co/sandpies/ComfyUI-SandTie-PromptRig](https://huggingface.co/sandpies/ComfyUI-SandTie-PromptRig) · Built from [ComfyUI-Hand-Tie-Clips](https://github.com/sandpies/ComfyUI-Hand-Tie-Clips)

![SandTie PromptRig (H3)](./assets/banner.png)

> **Stop hand-typing 6-field MiniMax H3 walls of text.** Drop **SandTie PromptRig (H3)** into any stock MiniMax H3 workflow (`Ref2VA`, `T2VA`, `I2VA`, `FL2VA`, `L2VA`, or `p-h3-image`), pick your cast & director dials in **SandTie Studio**, and drive either `prompt` at **0 VRAM** or native **`positive` + `latent`** directly.

[![ComfyUI](https://img.shields.io/badge/ComfyUI-%3E%3D0.38.0-e8ff47?style=flat-square&labelColor=111318)](https://github.com/comfyanonymous/ComfyUI)
[![MiniMax H3](https://img.shields.io/badge/Target-MiniMax%20H3%20(Hailuo)-7dd3fc?style=flat-square&labelColor=111318)](https://huggingface.co/Comfy-Org/MiniMax-H3)
[![Zero VRAM CPU Mode](https://img.shields.io/badge/CPU%20Tie-0%20VRAM-5fbf7a?style=flat-square&labelColor=111318)](#three-ways-to-author)
[![MIT License](https://img.shields.io/badge/License-MIT-a3a8b4?style=flat-square&labelColor=111318)](./LICENSE)

---

## Why This Exists

MiniMax H3 wants strict **six-field prompts** (`subject_definitions:`, `summary:`, `retention_analysis:`, `detailed_description:`, `overall_soundscape:`, `non_diegetic_music:`), clean `<Picture N>` / `<Subject N>` / `<Audio N>` binding, zero negations outside `<d>` dialogue tags, and exact `MM:SS.mmm` beat pacing. Writing those by hand—or juggling `LoadImage` chains across every new workflow—kills flow.

**SandTie PromptRig (H3)** wraps the entire H3 authoring engine from [ComfyUI-Hand-Tie-Clips](https://github.com/sandpies/ComfyUI-Hand-Tie-Clips) into **one plug-and-play ComfyUI V3 node**:

- **Zero HTC dependency** — install alone or side-by-side with `ComfyUI-Hand-Tie-Clips` with zero node, CSS, or HTTP route collisions.
- **Dynamic `Autogrow` sockets** — starts with 1 `ref_image_1` pin and expands up to **`ref_image_9`** (`ref_video_1..3`, `ref_audio_1..3`) as you wire nodes, matching stock `MiniMaxH3ReferenceToVideo`.
- **Two drop-in modes on one node** — run pure **`prompt` (`STRING`)** into any stock H3 node, or flip `wire_mode` to **`Direct H3 Conditioning (+ CLIP/VAE)`** to output native **`positive` (`CONDITIONING`) + `latent` (`LATENT`)** directly into `BasicGuider` & `SamplerCustomAdvanced`.
- **Persistent Reference Bible (`S1..S9`)** — upload once, run a cached 2.5 MP **Eye Scan**, assign voice `.wav`s, and reuse cast across workflows without re-wiring `LoadImage` trees.

---

## Two Ways to Wire into Stock MiniMax H3

| Mode | Set `wire_mode` to | Wire IN | Wire OUT | Best When |
|---|---|---|---|---|
| **1. Stock Prompt Drop-In** | `Prompt Only -> Stock H3 Node` | Optional `ref_image_1..9` / `brief_in` | **`prompt`** → `MiniMaxH3ReferenceToVideo.prompt` / `ImageToVideo.prompt` | Dropping straight into FastH3 / stock H3 templates (**0 VRAM**) |
| **2. Direct H3 Conditioning** | `Direct H3 Conditioning (+ CLIP/VAE)` | `clip`, `vae`, optional `audio_vae` + Bible or canvas refs | **`positive`** → `BasicGuider` · **`latent`** → `SamplerCustomAdvanced` | Casting from **Reference Bible** without `LoadImage` spaghetti |

Ready-to-run graphs ship in [`example_workflows/`](./example_workflows):
- [`SandTie_Stock_Ref2VA_PromptDropIn.json`](./example_workflows/SandTie_Stock_Ref2VA_PromptDropIn.json)
- [`SandTie_Direct_H3_Conditioning.json`](./example_workflows/SandTie_Direct_H3_Conditioning.json)

---

## Three Ways to Author

1. **`◩ CPU Tie` (0 VRAM, Instant)** — Deterministic hierarchical **Shot-Tree & StateLedger** H3 assembler combining active dials, per-shot camera/garment/orientation carry, weighted micro-beat timelines (`5–15 s`), and Reference Bible descriptions. No LLM required.
2. **`⚡ Quick Tie (1-Pass)` / `Plan -> Write` (Local LLM)** — Calls any local OpenAI-compatible server (**LM Studio**, **nInfer**, llama.cpp, vLLM) with structured `<shot_blueprint>` / `<state_ledger_invariants>` output, 2.5 MP Eye Scan vision context, and **✧ Double-Knot** pass-2 continuity verification. Pick **`LM Studio` / `nInfer`** right next to the status pill (or click **`⚙`**) inside **Open SandTie Studio** to set your URL, Model, and server path.
3. **`▶ Video -> Beats` (24-FPS OpenCV Extractor)** — Point at a reference `.mp4`, optionally trim `IN`/`OUT`, and extract motion cadence + camera trajectory + jump cuts directly into timed `[Shot N]` beats.

---

## Inside SandTie Studio (`⬒ Open SandTie Studio`)

- **19 Clean-Room Director Dials (2-Tier):**
  - *Primary 8:* `Cam` (`177`), `Light` (`71` options incl. `Soft Natural Light` & `Soft Natural Window Light`), `Style` (`94`), `Place` (`127` incl. plain enclosed & window bedrooms + combat/dance plates), `Wear` (`149`), `Action` (`194` incl. blow-for-blow `ms` fights & Uber Fights), `Stage` (`384`), `Speech` (`60`).
  - *Optics, Grade, Dance & Audio Drawer (11):* `Optics` (`94`), `Grade` (`44`), `FX` (`106`, `Delayed Mid` / `From Start`), `Dance / Pose` (`216` TikTok, K-Pop idol fingertip tutting & MV cuts, waacking/crunk, duet & ensemble flows), `Playbook` (`49`), `Cast Type` (`40`), `Genre` (`8`), `Era` (`17`), `Accent` (`30`), `Ambience` (`45` incl. `Pure Music N/A`), `Music` (`52`).
- **Performance & Audio Chips:** 5-step `MOTION`, `ENERGY`, `EXPRESSION` (+ acting read), and `LIFE` dials plus `TALK` (`Auto | All | Quotes | Silent`), `SOUND` (`Auto | Pure BGM | Quiet Air | Foley` with automatic foley-cue scrubbing), and `POV` (`Off | M | F`).
- **168 Built-In Combos + Smart Roll:** Cast-aware, domain-locked & aspect-safe (`16:9` / `4:3` / `9:16`) **Surprise Roll**, **Match Dials** from brief keywords, **Compose Brief**, **54 Clean Showcase Scripts**, and **❝ Fresh Dialogue** rewrites.
- **Built-In MiniMax H3 Rules:** Zero non-`<d>` negations, automatic TTS cleanup (`<d>[voice] "..."</d>`), semicolon/speech stripping from `overall_soundscape:` & `non_diegetic_music:`, 12 H3 motion primitives, Open-End Range & Background Plate amplitude laws, and a live `7,000`-char encoder counter.
- **All 6 MiniMax H3 Output Formats:** `Ref2VA / T2VA`, `I2VA` (`0.00 seconds` anchor), `FL2VA` (`0.00` + end-mark), `L2VA` (end-mark), `Start Frame Prep` (`p-h3-image`), and `Storyboard Beats Only`.

---

## Quick Start

1. Clone into `ComfyUI/custom_nodes/`:
   ```bash
   git clone https://github.com/sandpies/ComfyUI-SandTie-PromptRig.git
   ```
2. **Restart ComfyUI** (requires **ComfyUI v0.38.0+**) and hard-refresh your browser (`Ctrl+Shift+R`).
3. Drop **SandTie PromptRig (H3)** (under `MiniMax H3`) or load [`example_workflows/SandTie_Direct_H3_Conditioning.json`](./example_workflows/SandTie_Direct_H3_Conditioning.json).
4. Optional local LLM writer: click **`⬒ Open SandTie Studio`** → pick **`LM Studio` / `nInfer`** (or click **`⚙`** beside `Start / Stop`) to configure your URL, model, or server exe (or stay on **Instant CPU Tie** for 0-VRAM deterministic prompts).

### Required Stock Models (for H3 Video Generation)

| Component | Recommended Model | Folder |
|---|---|---|
| **Diffusion Model** | [`minimax_h3_ref2va_int8_convrot`](https://huggingface.co/Comfy-Org/MiniMax-H3/blob/main/diffusion_models/minimax_h3_ref2va_int8_convrot.safetensors) *(or FastH3 OmniRef)* | `models/diffusion_models` |
| **Text Encoder** | [`qwen3vl_32b_minimax_h3_nvfp4_awq`](https://huggingface.co/Comfy-Org/MiniMax-H3/blob/main/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) | `models/text_encoders` |
| **Video VAE** | [`minimax_h3_video_vae_int8_convrot`](https://huggingface.co/Comfy-Org/MiniMax-H3/blob/main/vae/minimax_h3_video_vae_int8_convrot.safetensors) | `models/vae` |
| **Audio VAE** | [`minimax_h3_audio_vae_fp32`](https://huggingface.co/Comfy-Org/MiniMax-H3/blob/main/vae/minimax_h3_audio_vae_fp32.safetensors) | `models/vae` |

---

## Credits & License

Built in [ComfyUI-Hand-Tie-Clips](https://github.com/sandpies/ComfyUI-Hand-Tie-Clips) (MIT).
Architecture and prompting insights acknowledge **LD Studio** (original PromptMaster layout inspiration), [wangweihong/comfyui-cinematic-gallery](https://github.com/wangweihong/comfyui-cinematic-gallery), and [loopforge0/minimaxh3-shots-skills](https://github.com/loopforge0/minimaxh3-shots-skills). See [`THIRD_PARTY_NOTICES.md`](./THIRD_PARTY_NOTICES.md).
