# ComfyUI Ultimate Auto Sampler Config Grid Testing Suite

<br>
Want to support development of this project? Buy me a coffee on Ko-fi:
<br><br>
<a href="https://ko-fi.com/jasonhoku" target="_blank">
  <img src="https://storage.ko-fi.com/cdn/brandasset/kofi_button_blue.png" alt="Support Me on Ko-fi" height="41">
</a>
<br><br>

**A professional-grade benchmarking and "IDE-like" testing suite for ComfyUI.**

Stop guessing which Sampler, Scheduler, Prompt, Denoise, Model, Lora or CFG value works best. This custom node suite allows you to generate massive Cartesian product grids, view them in an interactive infinite-canvas dashboard, and refine your settings with a "Revise & Generate" workflow without ever leaving the interface.

<img width="1840" height="895" alt="image" src="https://github.com/user-attachments/assets/5f8ac634-1ae8-4b51-a9d7-1b1752d1bda4" />

---

## ⚡ Quick Start — The 3 Nodes You Need

This suite is **three separate nodes** that must all be added and wired together. Don't stop after adding just one — here's how they connect:

```
┌──────────────────────────┐     configs_json    ┌──────────────────────────┐     dashboard_html    ┌──────────────────────────┐
│                          │ ──────────────────▶ │                          │ ────────────────────▶ │                          │
│  Ultimate Config Builder │                     │  Ultimate Sampler Grid   │                       │  Ultimate Grid Dashboard │
│      (Visual UI)         │                     │       (Generator)        │                       │         (Viewer)         │
│                          │                     │                          │                       │                          │
└──────────────────────────┘                     └──────────────────────────┘                       └──────────────────────────┘
   Point-and-click GUI for                          The engine — loads models,                         Renders the infinite-canvas
   building your test grid.                          runs every sampler × CFG ×                         dashboard with your result
   (Optional — you can also                          step × LoRA combination.                           grid for browsing, rating,
   write JSON directly.)                             Also accepts Checkpoint, CLIP,                     and revising.
                                                     and VAE inputs.
```

Node names in the "Add Node" menu, under `sampling/testing`:

| # | Node Name                      | Role                                                |
|---|--------------------------------|-----------------------------------------------------|
| 1 | **Ultimate Config Builder**    | Visual GUI for building configs *(optional)*        |
| 2 | **Ultimate Sampler Grid**      | The generator — **required**                        |
| 3 | **Ultimate Grid Dashboard**    | The result viewer — **required**                    |

### 🚀 Fastest way to try it

**Drag [`SamplrConfig-Basic-Workflow.json`](SamplrConfig-Basic-Workflow.json) into your ComfyUI canvas** — it includes all three nodes pre-wired with a working example. Swap in your checkpoint and hit Run.

**Or start from a model-specific example:** [`examples/`](examples/README.md) has one ready workflow per model family (SDXL/Illustrious, Anima, Z-Image Turbo, Krea 2, Flux.2 Klein 9B, MOSS-Image) with the model, text encoder, CLIP type and VAE already set. See [`examples/README.md`](examples/README.md) for the files each one needs.

> **Troubleshooting:** If the Config Builder loads as a plain node with no sliders/UI, right-click it and choose *Fix this node*, or delete and re-add it. Make sure you're on the latest version via Comfy Manager (1.9.2 or newer) and have restarted ComfyUI after updating.

### Manual wiring

If you'd rather build the graph yourself:

1. Add **Ultimate Sampler Grid** and connect your Checkpoint / CLIP / VAE to its inputs.
2. Add **Ultimate Grid Dashboard** and connect the Generator's `dashboard_html` output to the Viewer's input.
3. *(Optional)* Add **Ultimate Config Builder** and wire its `configs_json` output into the Generator's `configs_json` input. Without it, you can type a JSON config directly into the Generator's `configs_json` widget.

---

## 📑 Table of Contents

- [Quick Start](#-quick-start--the-3-nodes-you-need)
- [Key Features](#-key-features)
  - [Powerful Grid Generation](#-powerful-grid-generation)
  - [Distributed Processing (Multi-Machine)](#-distributed-processing-multi-machine)
  - [Upscaling & Post-Processing](#-upscaling--post-processing)
  - [Favorites Export & Workflow Packing](#-favorites-export--workflow-packing)
  - [Interactive Dashboard (The "IDE")](#-interactive-dashboard-the-ide)
  - [The "Revise & Generate" Workflow](#-the-revise--generate-workflow)
  - [Curation & JSON Export](#-curation--json-export)
- [Optional Companion Plugins](#optional-companion-plugins)
- [Installation](#-installation)
- [Getting Started](#getting-started)
  - [The Nodes](#1-the-nodes)
  - [Generator Node Parameters](#2-generator-node-parameters)
    - [Core Settings](#core-settings)
    - [Performance Settings (incl. Text-Encoder Batching)](#performance-settings)
    - [Advanced Settings](#advanced-settings)
  - [The JSON Configuration](#3-the-json-configuration)
  - [Hybrid Inputs (Optional)](#4-hybrid-inputs-optional)
- [Config Builder Node (Visual UI For Creating Runs)](#-config-builder-node-visual-ui)
  - [Run Settings](#run-settings)
  - [Basic Setup](#basic-setup)
  - [Understanding the Interface](#understanding-the-interface)
  - [Session Management](#session-management)
  - [Config Management (Save/Load Presets)](#config-management-saveload-presets)
  - [Config Arrays](#config-arrays)
  - [Fast CivitAI Info Lookup](#fast-civitai-info-lookup)
    - [Basic Parameters](#basic-parameters)
    - [Iteration Count Display](#iteration-count-display)
    - [Config Array Controls](#config-array-controls)
  - [Models Section](#models-section)
  - [LoRAs Section](#loras-section)
  - [LoRA Trigger Words](#lora-trigger-words)
    - [Trigger Word Lookup Modal](#trigger-word-lookup-modal)
    - [Trigger Word Placement Control](#trigger-word-placement-control)
  - [LoRA Bypass States](#lora-bypass-states)
  - [Strength Locking](#strength-locking)
  - [Folder Expansion (Models & LoRAs)](#folder-expansion-models--loras)
  - [LoRA Stacking](#lora-stacking)
  - [VAEs Section](#vaes-section)
  - [Attention Modes](#attention-modes)
  - [Skip Layer Guidance](#skip-layer-guidance-dit-models)
  - [MOSS-Image, Flux.2, Krea 2 (16 px latent models)](#moss-image-flux2-krea-2-16-px-latent-models)
  - [Model-Specific Prompts](#model-specific-prompts)
  - [Recursive Cartesian Prompt Builder](#recursive-cartesian-prompt-builder)
  - [Prompt Combinators & Regional Prompts (COUPLE)](#prompt-combinators--regional-prompts-couple)
  - [Job Order & Preview Pass](#job-order--preview-pass-run-settings)
  - [Image Metrics (Optional)](#image-metrics-optional)
  - [Workflow Sweep](#workflow-sweep-sweep-any-comfyui-workflow)
- [Dashboard Interface](#-dashboard-interface)
  - [Header Bar](#header-bar)
  - [Toolbar](#toolbar)
  - [Navigation & Controls](#navigation--controls)
  - [Card Overlays](#card-overlays)
  - [JSON Bars](#json-bars-bottom--horizontal-layout)
  - [Revision Modal](#revision-modal)
  - [Pairwise Review](#pairwise-review-blind-ab-compare--scoreboard)
  - [Stats Panel](#stats-panel-per-setting-analytics)
  - [Standalone Dashboard](#standalone-dashboard-phone--second-monitor)
- [Example Workflows](#-example-workflows)
  - [Quick Quality Test](#quick-quality-test-40-images)
  - [Multi-Model Comparison](#multi-model-comparison-9-images)
  - [LoRA Stack Testing](#lora-stack-testing-24-images)
  - [Random LoRA Selection](#random-lora-selection)
  - [Full Model Folder Test](#full-model-folder-test)
  - [CLIP Skip for Anime Models](#clip-skip-for-anime-models)
  - [LoRA Trigger Word Filtering](#lora-trigger-word-filtering)
  - [Model Folder Expansion](#model-folder-expansion)
  - [LoRA Strength Sweep](#lora-strength-sweep)
  - [Quality Enhancement Stack](#quality-enhancement-stack)
- [Preset Configs](#-preset-configs)
- [Performance Tips](#-performance-tips)
- [Tips & Best Practices](#-tips--best-practices)
- [Troubleshooting](#-troubleshooting)
  - [Generation Issues](#generation-issues)
  - [Dashboard Issues](#dashboard-issues)
  - [LoRA & Trigger Word Issues](#lora--trigger-word-issues)
  - [Model & CLIP Issues](#model--clip-issues)
  - [Config Builder UI Issues](#config-builder-ui-issues)
  - [Remote VAE Issues](#remote-vae-issues)
  - [Interrupt/Cancel Issues](#interruptcancel-issues)
  - [Browser Compatibility](#browser-compatibility)
- [JSON Output Format Reference](#json-output-format-reference)
- [API Integration (Config Builder)](#api-integration-config-builder)
  - [Run API (headless runs)](#run-api-headless-runs-discord-bot-session-hub-curl)
  - [Dashboard, Review, Metrics & Sweep Routes](#dashboard-review-metrics--sweep-routes)
- [File Locations](#file-locations)
- [Keyboard Shortcuts](#keyboard-shortcuts)
  - [Dashboard](#dashboard)
  - [Compare mode](#dashboard-compare-mode-blind-pairwise-review)
  - [Config Builder](#config-builder)
- [Distributed Processing](#-distributed-processing)
  - [Setting Up Distribution](#setting-up-distribution)
  - [Master Text Encoding](#master-text-encoding)
  - [Model Sync](#model-sync)
  - [Distribution Troubleshooting](#distribution-troubleshooting)
- [Notes for AI Development](#-notes-for-ai-development)
  - [Development / Tests](#development--tests)
  - [Key Gotchas](#key-gotchas-for-ai-development)
  - [Server Event Types](#server-event-types)
- [Changelog](#-changelog)
- [License](#-license)
- [Credits](#-credits)

---

## 🌟 Key Features

### 🚀 Powerful Grid Generation

<img width="951" height="601" alt="image" src="https://github.com/user-attachments/assets/2e2c3253-7ab3-46e2-9b60-440de5077ee3" />


* **Cartesian Product Engine:** Automatically generates every permutation of your input settings. Test unlimited Samplers, Schedulers, CFG scales, Sizes, Prompts, LoRA combinations all in one go.
* **Visual Config Builder:** A point-and-click GUI for building complex sampler configurations — no JSON editing required. Searchable dropdowns, drag sliders, folder expansion, LoRA stacking, and trigger word management all built in.
* **Non-Standard Model Support:** Full support for SD3, Flux, Z-Image, and other non-standard architectures with automatic latent channel detection.
* **Multi-Model Support:** Test multiple checkpoints in a single run by passing an array of model names or folder paths.
* **Model Folder Expansion:** Use `"model": "FolderName/"` to test all checkpoints in a folder automatically — perfect for comparing different versions or architectures.
* **CLIP Skip Support:** Control which CLIP layer to use for text encoding with the `clip_skip` parameter — essential for anime models (typically -2) vs realistic models (typically 0).
* **Intelligent CLIP Encoding:** Automatically detects when multiple models are used and handles CLIP encoding correctly per-model to ensure accurate results.
* **Batch Encoding on Model Switch:** When switching between models, all prompts are batch-encoded at once rather than per-generation, resulting in 3-6x faster encoding for multi-model workflows.
* **Multi-LoRA Stacking:** Layer multiple LoRAs with custom strengths using the `+` separator. Supports folder expansion for testing entire LoRA directories.
* **LoRA Trigger Word Filtering:** Use `lora_omit_triggers` to exclude specific trigger words from auto-appended LoRA triggers, giving you fine control over prompts.
* **Random LoRA Selection:** Randomly select LoRAs from folders with `[count,strength]` or `[count,strength,random]` syntax. Supports both reproducible (seed-based) and truly random selection modes.
* **Auto LoRA Trigger Words:** Automatically fetches and appends LoRA trigger words from CivitAI API using SHA256 hash lookup. Results are cached locally for offline use.
* **Multi-Seed Generation:** Add extra random variations per config with the `add_random_seeds_to_gens` parameter — perfect for evaluating consistency.
* **Smart Caching:** Intelligently skips model and LoRA reloading when consecutive runs share the same resources, making generation instant for parameter tweaks.
* **Stop & Resume:** Intelligent skip detection — if you stop a generation mid-run, resuming will skip already-generated images and continue where you left off.
* **Advanced Skip Logic:** Uses conditioning tensor hashing to detect prompt changes even when using pre-encoded conditioning from CLIP nodes.
* **LoRA Compatibility Detection:** Automatically detects and skips incompatible LoRAs with detailed error reporting, preventing log spam.
* **Graceful Interruption:** Cancel button now stops ALL remaining jobs (not just current generation) and saves all completed work including pending remote VAE decodes.
* **VAE Batching:** Includes a `vae_batch_size` input to batch decode images, significantly speeding up large grid runs.
* **Text-Encoder Batching:** The `te_batch_size` Run Setting encodes several prompts per text-encoder pass (MOSS-Image, Krea 2, Qwen-Image), intended to cut pre-encode time on prompt-heavy grids. Off by default, and the live check argues for leaving it off: Measured 2026-11-04 on a 5060 Ti with MOSS-Image (Qwen3.5-9B w4a8): a batch of 8 was 1.5x SLOWER per prompt than one-by-one (padding to the longest prompt in the batch) and the images were not identical to the unbatched run (the encoder outputs match to relL2 5e-5, which the sampler amplifies into visibly different images), so leave it at 1 unless you measure a gain on your encoder.
* **Live Dashboard Updates:** Configure `flush_batch_every` to update the dashboard incrementally (e.g., every 4 images) instead of waiting for the entire batch to complete.
* **Remote VAE Support:** Offload VAE decoding to remote servers (HuggingFace endpoints or local) for 20-30% faster generation and lower VRAM usage.
* **VAE Selection & Iteration:** Test multiple VAEs per config — add individual VAEs from a searchable dropdown or expand entire VAE folders. Each VAE becomes a dimension in the Cartesian grid.
* **Attention Mode Testing:** Grid-test different attention implementations (`default`, `sage`, `sage3`, `flash`, `xformers`, etc.) as a combinatorial dimension. Find the optimal attention backend for your hardware.
* **CLIP Encoding Combinators:** Advanced prompt syntax with `AND`, `CAT`, `AVG(weight)`, and `BREAK` keywords for multi-segment conditioning. `AND` creates separate conditioning entries, `CAT` concatenates token contexts, `AVG(0.5)` blends prompts, and `BREAK` forces new 77-token chunks. `COUPLE` splits a prompt into left/right (or top/bottom) regions, see [Prompt Combinators & Regional Prompts (COUPLE)](#prompt-combinators--regional-prompts-couple).
* **Model-Specific Prompts:** Per-config prompt prefix and suffix fields for model-appropriate quality tags (e.g., prepend `"masterpiece, best quality"` for anime models, append `"4k, photorealistic"` for realistic models).
* **Recursive Cartesian Prompt Builder:** Visual chip-based prompt editor with `{option1|option2|option3}` syntax that expands into all combinations. Nest multiple groups for exponential prompt variation.
* **Model & LoRA On/Off Switches:** Toggle individual models and LoRAs on/off without removing them from the config. Bypassed entries are omitted from both the preview JSON and the generated config output.
* **Drag-and-Drop Reorder:** Rearrange models, LoRAs, text encoders, and VAEs by dragging them into your preferred order.
* **Per-Config Resolutions:** Override the sampler node's global resolution with per-config resolution lists. Each resolution becomes a Cartesian dimension.
* **Redesigned Resolution Picker:** Nested dropdown with categorized presets (SD 1.5, SDXL, Flux, etc.) and a custom resolution editor for saving your own presets.
* **Seed Behavior Settings:** Per-config seed control — `fixed` uses the node seed, `randomize` generates a new seed per image, `full_run_seed` overrides the node seed entirely.
* **Configurable Label Mode:** Toggle overlay labels on dashboard cards showing model, sampler, scheduler, steps, CFG, and other parameters directly on each image.
* **GPU Cooldown:** Automatic pause between generations to prevent thermal throttling. Configurable interval, duration, and optional VRAM clearing.
* **Image Metrics (optional):** Run Settings checkbox that stores sharpness, entropy, colorfulness, contrast, luma, saturation and Sobel edges for every saved image in the manifest (see [Image Metrics](#image-metrics-optional)).
* **Workflow Sweep:** sweep any ComfyUI workflow exported as API JSON. Bind any input as an axis, dry run it, then pause, resume or cancel; every image lands in a normal USCG session (see [Workflow Sweep](#workflow-sweep-sweep-any-comfyui-workflow)).
* **Job Order (Minimize reloads):** reorders the whole job list so each model and LoRA stack loads as few times as possible (see [Job Order & Preview Pass](#job-order--preview-pass-run-settings)).
* **Preview Pass (generator side):** renders the whole grid cheaply first; reject the losers and only the survivors render at full quality (see [Job Order & Preview Pass](#job-order--preview-pass-run-settings)).
* **Skip Layer Guidance:** Builder option that wraps ComfyUI's `SkipLayerGuidanceDiTSimple` for DiT models (see [Skip Layer Guidance](#skip-layer-guidance-dit-models)).
* **16 px latent models:** MOSS-Image, Flux.2 and Krea 2 render at the size you ask for, with the CLIP type picked for the detected family (see [MOSS-Image, Flux.2, Krea 2](#moss-image-flux2-krea-2-16-px-latent-models)).
* **Examples folder:** [`examples/`](examples/README.md) has one ready workflow per model family.

### 🌐 Distributed Processing (Multi-Machine)
* **Multi-Worker Distribution:** Split large grid runs across multiple ComfyUI instances. A master node coordinates job distribution while workers process images in parallel and upload results back.
* **One-Click Setup:** Enable distribution in the Config Builder's Distribution Settings section. Add worker URLs (e.g., `http://192.168.1.100:8188`) and toggle "Enable Distribution."
* **Worker Connection Testing:** Test connectivity to each worker with a single click — status dots show green (reachable), yellow (testing), or red (error).
* **Master Text Encoding:** Optional "Use Master Text Encoding" toggle — the master pre-encodes ALL unique prompts (including LoRA-specific combinations) and sends the encoded conditionings to workers. Workers skip CLIP encoding entirely, saving significant time on prompt-heavy grids.
* **Model Sync:** Optional "Sync Models to Workers" toggle — automatically transfers checkpoint and LoRA files from the master to workers that don't have them.
* **Smart Job Queue:** Thread-safe job distribution with automatic re-queuing on worker timeout (configurable, default 600s) and max 3 retries before abandoning a job.
* **Per-Worker Logging:** Final generation summary shows each worker's completed/failed job counts for full visibility into the distributed run.
* **Live Distribution Status:** Dashboard receives real-time distribution status updates showing worker activity and progress.
* **Backward Compatible:** Workers gracefully fall back to local CLIP encoding if master-encoded conditionings aren't available.

### 🔍 Upscaling & Post-Processing
* **Array-Based Upscaling:** Define multiple upscale configurations, each with its own mode, models, ratios, and denoise values. All combinations are expanded via Cartesian product — test 3 upscale models × 2 ratios × 2 denoise values = 12 upscaled variants per source image.
* **Five Upscaling Modes:** `hires_only` (latent upscale + re-denoise), `model_only` (upscale model like RealESRGAN), `model_then_hires` (upscale model followed by hires denoise pass), `seedvr2` (SeedVR2 diffusion-based upscaler), and `florence2_hires` (Florence2-driven targeted hi-res fix — see below).
* **Florence2 Hi-Res Fix:** Targeted region inpaint using [kijai/ComfyUI-Florence2](https://github.com/kijai/ComfyUI-Florence2)'s referring-expression segmentation. Type what you want fixed (`face`, `hands`, `eyes`, `clothing`) as a free-text input; Florence2 detects the polygon, USCG crops to that region, runs a megapixel-scaled hi-res inpaint pass with your chosen denoise/sampler/steps, and pastes the result back with feathered blending. Pick model/LoRA from each image's original manifest entry or use the Builder's currently-loaded one. Grid-test face fixes the same way you grid-test base configs — combine with other upscale steps in one pipeline for a base-hi-res → face-fix chain. Requires the `ComfyUI-Florence2` custom node (auto-detected at job start with a clear install hint if missing).
* **Upscale Model Discovery:** Automatically detects installed upscale models from ComfyUI's `upscale_models` folder with a searchable dropdown in the Config Builder.
* **Tiled VAE Support:** Enable tiled VAE decoding for upscaled images to handle large resolutions without running out of VRAM.
* **Only Final Output Saved:** When upscaling is enabled, only the upscaled version is saved — the intermediate base image is automatically skipped, keeping your session clean.
* **Dashboard Upscale:** upscale one image or every favorite straight from the Dashboard, with a full pipeline editor, presets and a real Cancel — see [Dashboard Upscale](#dashboard-upscale).

### Dashboard Upscale
The up-arrow button (⬆) on a card opens the upscale modal for that image, or for all favorited images.

* **Presets:** pick one from the list; the badge shows `Preset: X`, `Preset: X (modified)` after you edit it, or `Unsaved config`. **Update preset** overwrites the loaded preset, **Save as…** stores the edits under a new name, **Revert** drops the edits, **Delete** removes the preset. Presets are shared with the Config Builder (same file), and every save re-reads the file first so a preset someone else added meanwhile is never lost.
* **Inline editing:** add, remove, switch off and **reorder** pipelines and steps with the ▲ ▼ buttons (buttons, not drag and drop, so it works on a phone). Mode, ratios, denoise, steps, tiled sampling / VAE, upscale models, SeedVR2 and Florence2 options are all editable.
* **Validation:** a field that cannot work (`1.5,x` as ratios, denoise above 1, no upscale model for a model mode, empty Florence2 text, ...) is outlined in red, listed under the editor, and **Run** stays disabled until it is fixed. Warnings (an upscale model that is not installed, several denoise values for Florence2) do not block. The server validates again and answers `400` with the list if something slips through.
* **Run vs Run once:** **Run** appears when the config equals the loaded preset; once you change anything it reads **Run once (unsaved)**. Either way the config is sent as it is and nothing is written to the presets file unless you press Update / Save as. A line under the editor says how many images and outputs the run will produce.
* **Cancel:** **Cancel job** is only shown while a job runs (the editor is locked meanwhile). The job stops between images, pipelines, steps and combinations, and *inside* the sampler within one step (a cancel-aware copy of the model; ComfyUI's global interrupt is never used, so a Generator run in the queue is unaffected). SeedVR2 runs in an external node and can only stop between steps. Outputs finished before the cancel are kept and appear exactly once; the status line reads `Cancelled: 3/10 images done, 5 new images kept`. **Close** only hides the modal: reopen it (or reload the page) and it re-attaches to the running job. One job per session at a time (a second start answers `409`).
* **Phone:** below 600 px wide the modal fills the screen, buttons are 44 px touch targets, inputs are 16 px and Run / Cancel stay pinned to the bottom.
* **Note:** upscaled files are saved in the session's image format, and carry the nodes workflow when the session was generated with *Embed ComfyUI Nodes Workflow*.

### 📦 Favorites Export & Workflow Packing
* **Pack Full ComfyUI Workflow:** Embed the entire current ComfyUI graph into exported favorite images as PNG metadata. Drag the exported image back into ComfyUI to restore the full workflow.
* **Pack Config Data as Nodes Workflow:** Generate a per-image pure-nodes workflow from each image's specific config (sampler, scheduler, steps, CFG, model, LoRA, prompt). Each exported image gets its own workflow matching exactly how it was generated. Images the Dashboard sent no workflow for (for example an export from an older page) get the same graph built server-side. To have the graph in every image from the start, turn on *Embed ComfyUI Nodes Workflow* in Run Settings.
* **Cleaned Favorites Manifest:** Export only favorited items in the manifest — non-favorited entries are excluded from the copied manifest.json.
* **Delete All Non-Favorited Items:** One-click cleanup to permanently delete all non-favorited images from a session and update the manifest. Includes a confirmation dialog to prevent accidents.
* **Export Positive Prompt as .txt:** Save the positive prompt alongside each exported image as a plain text file — useful for training datasets.
* **Organize by Prompt or LoRA:** Optionally sort exported favorites into subfolders grouped by unique prompt or LoRA combination.

### 🎨 Interactive Dashboard (The "IDE")
* **Infinite Canvas with Pan/Zoom:** Google Maps-style navigation with mouse drag, mousewheel zoom, and keyboard shortcuts.
* **Virtual Scrolling:** Ultra-optimized rendering handles thousands of images smoothly by only loading visible items — scroll through 5000+ images without lag.
* **Mobile Touch Support:** Full pinch-to-zoom and pan gestures on mobile devices with optimized touch controls.
* **Fullscreen Mode:** Click the fullscreen button (⛶) to expand the dashboard to fill your entire screen.
* **Favorites System:** Star your best images with a ⭐ button — favorites are collected in a separate gold JSON bar for easy export.
* **Smart Filtering:** Toggle visibility by Model, Sampler, Scheduler, Denoise, or LoRA type. **Shift+Click** to isolate a single filter for quick A/B testing.
* **Intelligent Sorting:** Instantly sort your grid by **Oldest**, **Newest**, or **Fastest** (generation time). Your preference is saved to localStorage.
* **Go to Image #:** Jump directly to any image number with the "Go to #" input field in the header.
* **Auto-Load Sessions:** Dashboard automatically loads when generation starts — no manual session name entry needed.
* **Session Management:** Save and load previous testing sessions directly from the UI.
* **Keyboard Navigation:** `Space` to scroll rows, `Arrow Keys` to pan, `+/-` to zoom, `0` to reset, `F` to auto-fit.
* **Real-Time ETA Progress Bar:** Shows estimated time remaining during generation with a progress bar in the dashboard header.
* **Unified Settings Panel:** Gear icon (⚙️) opens a consolidated settings panel with Session management, Grid Display controls, Export Favorites, and Scan External Directory — replacing the old separate SESSION button.
* **Scan External Directory:** Load image sessions from any folder (including other ComfyUI instances) into the dashboard for viewing and filtering. Reads PNG metadata for full config display.
* **Export Favorites:** Copy all favorited images to a dedicated export folder with optional CivitAI metadata packing for sharing.
* **Preview Pass support:** preview images carry an amber `PREVIEW` badge, a **Pass** filter row (Preview / Full, shown once previews exist) separates them, and a preview whose cell now has a full image is hidden by default (isolate `Preview` in the Pass row to see them). A bar under the header counts previews and offers **Full pass for survivors (N)**, which switches Preview Pass off in the matching Config Builder and queues the workflow (falls back to instructions if the ComfyUI frontend does not allow it).
* **Pairwise Review:** blind A/B compare mode (`C` key) with Bradley-Terry ratings and a per-setting scoreboard (see [Pairwise Review](#pairwise-review-blind-ab-compare--scoreboard)).
* **Standalone Dashboard + Run API:** open the dashboard as a normal web page (phone, second monitor) and start headless runs with `POST /config_tester/run` (see [Standalone Dashboard](#standalone-dashboard-phone--second-monitor) and [Run API](#run-api-headless-runs-discord-bot-session-hub-curl)).

### ⚡ The "Revise & Generate" Workflow
* **One-Click Revision:** Click "REVISE" on any image to open a detail view.
* **Complete Metadata View:** Shows model, seed, prompts (with trigger words), and all generation parameters.
* **Instant Tweak:** Adjust CFG, Steps, or Sampler for *just that specific image*.
* **Generate New:** A "GENERATE NEW" button queues the new variation immediately without needing to disconnect wires or change the main batch.
* **Drag Into Load Image:** Drag the big image in the Revise view onto a Load Image node (sets its `image` widget) or onto empty canvas (creates a Load Image node), or click **Send to Load Image** (the selected Load Image, the only one, or a new one beside the dashboard). A node drop and the button *reference* the file as `benchmarks/<session>/images/<file> [output]` (no copy in `input/`, but the workflow then depends on that folder; a canvas drop is made by ComfyUI's frontend, which uploads a copy). To always copy instead, set `USCG_DRAG_UPLOAD = true` in `resources/logic_dragdrop.js`. On the standalone page the button is **Download image**.
* **Similarity Reel:** The revision modal shows a side-scrolling reel of all other images that share the same seed, allowing for perfect A/B comparison.
* **Multiple Prompts:** Use an array to run multiple prompts in one run without re-running your entire workflow: `["picture of a forest", "mountains at night", "masterpiece, painting of dog"]`

### 🧹 Curation & JSON Export
* **Rejection System:** Click the red **"✕"** on bad generations to hide them.
* **Triple JSON Bars (Horizontal Layout):**
    * **Green Bar (Left):** Automatically groups all *accepted* configs into a clean, optimized JSON array ready for copy-pasting.
    * **Gold Bar (Center):** Contains all *favorited* configs — your best-performing settings.
    * **Red Bar (Right):** Collects all *rejected* configs so you know exactly what settings to avoid.

---

## Optional Companion Plugins

Some advanced features live in separate companion plugins:

- **[ComfyUI-USCG-RemoteVAE](https://github.com/JasonHoku/ComfyUI-USCG-RemoteVAE)**
  — Offload VAE decoding to HuggingFace Remote VAE endpoints
  (saves VRAM for large latents). Install via Comfy Manager
  (search "USCG Remote VAE") or `git clone` into `custom_nodes/`.

- **[ComfyUI-USCG-Distributed](https://github.com/JasonHoku/ComfyUI-USCG-Distributed)**
  — Distribute grid generation across multiple ComfyUI machines on
  your LAN (master + worker model). Install via Comfy Manager
  (search "USCG Distributed") or `git clone` into `custom_nodes/`.

- **[ComfyUI-USCG-CivitAI](https://github.com/JasonHoku/ComfyUI-USCG-CivitAI)**
  — Auto-detect LoRA trigger words and look up model/LoRA metadata from
  CivitAI (by file hash). Install via Comfy Manager (search "USCG CivitAI")
  or `git clone` into `custom_nodes/`.

---

## 📦 Installation

1. Navigate to your ComfyUI `custom_nodes` directory:
    ```bash
    cd ComfyUI/custom_nodes/
    ```

2. Clone this repository:
    ```bash
    git clone https://github.com/YOUR_USERNAME/ComfyUI-Ultimate-Auto-Sampler-Config-Grid-Testing-Suite.git
    ```

3. Restart ComfyUI.

The Config Builder node is included automatically — no separate installation is required.

**Requirements:**
- ComfyUI (latest version recommended)

**File Structure:**
```
ComfyUI/custom_nodes/ComfyUI-Ultimate-Auto-Sampler/
├── __init__.py                      # Server routes, API endpoints, node mappings
├── sampler_node.py                  # Main "Sampler Grid" node
├── dashboard_node.py                # "Dashboard Viewer" node
├── config_builder_node.py           # "Config Builder" node backend
├── json_text_node.py                # "Smart JSON" node
│
├── generation_orchestrator.py       # Main orchestration layer & generation loop
├── image_generation.py              # KSampler & VAE wrappers
├── model_loader.py                  # Checkpoint/LoRA/VAE loading and patching
├── model_cache.py                   # 3-tier model caching system
├── remote_vae.py                    # Remote VAE offloading
│
├── batch_encoding.py                # CLIP batch encoding with combinator support
├── regional_prompt.py               # COUPLE regional prompts (parser, masks)
├── conditioning_cache.py            # Disk-based conditioning cache
├── lora_utils.py                    # LoRA searching & validation
├── trigger_words.py                 # CivitAI trigger word fetching & prompt assembly
├── config_utils.py                  # Config parsing, expansion & Cartesian products
├── directory_scanner.py             # External directory session scanner
├── metadata_packer.py               # PNG/WebP metadata embedding for exports
├── manifest_utils.py                # Manifest read/write/merge helpers
├── html_generator.py                # Reads /resources/ to build dashboard HTML
│
├── distribution.py                  # Facade: distributed mode lives in the ComfyUI-USCG-Distributed companion
├── civitai.py                       # Facade: CivitAI downloads live in the ComfyUI-USCG-CivitAI companion
│
├── web/                             # [ComfyUI Integration Layer]
│   ├── dashboard.js                 # Dashboard node registration & messaging
│   ├── smart_json_text.js           # JSON node & syntax highlighting
│   └── conf_builder/                # [Config Builder UI Modules]
│       ├── conf-builder-main.js           # Entry point, widget registration
│       ├── conf-builder-ui-components.js  # Reusable UI (dropdowns, sliders, cards)
│       ├── conf-builder-config-management.js # Save/Load/state rendering logic
│       ├── conf-builder-utilities.js      # Data fetching, caching, calculations
│       └── conf-builder-distribution.js   # Distribution settings UI
│
└── resources/                       # [Dashboard SPA Core]
    ├── template.html                # HTML skeleton for dashboard
    ├── report.css                   # Styling (infinite canvas, cards, modals)
    ├── logic_state.js               # Global state variables
    ├── logic_utils.js               # API & helper functions
    ├── logic_ui.js                  # UI renderer (DOM creation, modals)
    ├── logic_virtual.js             # Virtual scroll engine & viewport
    ├── logic_pipeline.js            # Sorting & filtering pipeline
    ├── logic_events.js              # Event listeners (messages, keyboard)
    └── logic_init.js                # Initialization & startup
```

---

## Getting Started

### 1. The Nodes
This suite consists of three nodes found under the `sampling/testing` category:

1. **Ultimate Sampler Grid (Generator):** The engine. It handles model loading, grid generation, and saving.
2. **Ultimate Grid Dashboard (Viewer):** The display. It renders the HTML output.
3. **Ultimate Config Builder:** The visual GUI for building configs without writing JSON.

**Basic Setup:**
* Add the **Generator** node.
* Connect your Checkpoint, CLIP, and VAE (optional, see "Hybrid Inputs" below).
* Add the **Viewer** node.
* Connect the `dashboard_html` output from the Generator to the input of the Viewer.
* *(Optional)* Add the **Config Builder** node and connect its `configs_json` output to the Generator's `configs_json` input.

### 2. Generator Node Parameters

#### Core Settings
* **`ckpt_name`**: Default checkpoint to use (can be overridden by `model` in JSON or optional input).
* **`positive_text`** / **`negative_text`**: Prompts. Supports arrays: `["prompt 1", "prompt 2"]` or JSON arrays.
* **`seed`**: Base seed. Each config uses this seed unless overridden.
* **`denoise`**: Denoise strength(s). Supports single value, array, or comma-separated: `"1.0"` or `"0.8, 0.9, 1.0"`.

#### Performance Settings
* **`vae_batch_size`**: How many images to decode at once.
  - `4` (default): Good for 8-12GB VRAM
  - `12-24`: For 24GB+ VRAM  
  - `-1`: Decode all images at once (fastest, but risky)
  
* **`te_batch_size`** (Run Setting "Text Encoder Batch Size"): How many prompts to encode per text-encoder forward. `1` (default) = off. Measured 2026-11-04 on a 5060 Ti with MOSS-Image (Qwen3.5-9B w4a8): a batch of 8 was 1.5x SLOWER per prompt than one-by-one (padding to the longest prompt in the batch) and the images were not identical to the unbatched run (the encoder outputs match to relL2 5e-5, which the sampler amplifies into visibly different images), so leave it at 1 unless you measure a gain on your encoder.
  - Only MOSS-Image, Krea 2 and Qwen-Image encoders batch; every other encoder ignores it.
  - Weighted prompts and `AND` / `CAT` / `AVG()` / `BREAK` / `COUPLE` prompts are still encoded one at a time.
  - The first batch is self-checked against a single-prompt encode; on any mismatch the run falls back to one-by-one automatically. A CUDA OOM halves the batch and retries.
  - The pre-encode summary line shows how many prompts were batched.

* **`flush_batch_every`**: Update dashboard every X images (0 = use VAE batch size).
  - `0`: Wait until VAE batch is full
  - `4`: Update dashboard every 4 images (recommended for live monitoring)

#### Advanced Settings
* **`overwrite_existing`**: 
  - `False` (default): Skip already-generated images (resume mode)
  - `True`: Re-generate everything
  
* **`add_random_seeds_to_gens`**: Generate X extra random variations per config.
  - `0` (default): Only use base seed
  - `3`: Generate 3 additional random seed variations per config
  - Extra seeds are deterministic per base seed — the same base seed always gives the same extras, changing the base seed gives new ones

* **`lookup_and_append_lora_triggerwords`**: Automatically fetch and append LoRA trigger words.
  - `False` (default): Use prompts as-is
  - `True`: Calculate SHA256 hash of each LoRA, query CivitAI API for trigger words, cache results locally, and prepend to prompts
  - Cache stored in `loras_tags.json` for offline use

* **`session_name`**: Folder name where results are saved (`ComfyUI/output/benchmarks/{session_name}/`).

### 3. The JSON Configuration
The `configs_json` widget determines your grid. It accepts an array of objects. All fields support single values or arrays. You can write JSON by hand or use the [Config Builder Node](#-config-builder-node-visual-ui) to build it visually.

**Basic Example:**
```json
[
  {
    "sampler": ["euler", "dpmpp_2m"],
    "scheduler": ["normal", "karras"],
    "steps": [20, 30],
    "cfg": [7.0, 8.0]
  }
]
```
*Generates 16 images (2 samplers × 2 schedulers × 2 steps × 2 cfg)*

**Advanced Features:**

#### Multi-Model Testing
```json
[
  {
    "sampler": "euler",
    "scheduler": "normal", 
    "steps": 20,
    "cfg": 7.0,
    "model": [
      "sd_xl_base_1.0.safetensors",
      "juggernautXL_v9.safetensors",
      "ponyDiffusionV6XL_v6.safetensors"
    ]
  }
]
```
*Tests 3 different models with the same settings*

#### Folder Expansion
```json
[
  {
    "sampler": "euler",
    "scheduler": "normal",
    "steps": 20, 
    "cfg": 7.0,
    "model": "sdxl_models/"
  }
]
```
*Trailing `/` tests ALL models in the folder.*

#### Multi-LoRA with Stacking
```json
[
  {
    "sampler": "euler",
    "scheduler": "normal",
    "steps": 20,
    "cfg": 7.0,
    "lora": [
      "None",
      "style_lora.safetensors:0.8:1.0",
      "style_lora.safetensors:0.5:1.0 + detail_lora.safetensors:1.0:1.0",
      "loras_folder/"
    ]
  }
]
```
*LoRA format: `filename:strength_model:strength_clip`*  
*Stack with `+` separator: `lora1:0.8:1.0 + lora2:1.0:1.0`*

#### Resolution Grid
```json
// In resolutions_json input:
[
  [1024, 1024],
  [1024, 1536], 
  [1536, 1024]
]
```

#### Multiple Prompts
```json
// In positive_text input (as JSON array):
[
  "a beautiful landscape, mountains, sunset",
  "cyberpunk city at night, neon lights",
  "portrait of a warrior, detailed armor"
]
```

### 4. Hybrid Inputs (Optional)
The Generator node features built-in widgets for Model Selection and Prompts, but also has **Optional Inputs** for flexibility:
* **Standalone Mode:** Use the dropdown menu to select a checkpoint and type prompts into the text boxes.
* **Hybrid Mode:** Connect a `MODEL`, `CLIP`, `VAE`, or `CONDITIONING` wire. The node will automatically ignore the internal widget and use the connected input instead.
* **Non-Standard Models:** For SD3, Flux, Z-Image, and other architectures:
  - Connect `optional_model`, `optional_clip`, and `optional_vae` from your model loader
  - Connect `optional_positive` and `optional_negative` for pre-encoded conditioning
  - The node automatically detects latent channel count (4 for SD1.5/SDXL, 16 for SD3/Flux/Z-Image)
  - Skip detection uses conditioning tensor hashing to properly detect prompt changes
* **Latent Input:** Connect a `LATENT` to use img2img or upscaling workflows. The image size is the latent size times the model's latent ratio (8 px per cell for SD/SDXL/Flux.1, 16 for Flux.2/MOSS-Image/Krea 2), so the manifest and upscale target sizes are right for every family.
  - For SD3/Flux: Use `EmptySD3LatentImage` instead of `EmptyLatentImage`
  - Latent dimensions are automatically preserved

---

## 🔧 Config Builder Node (Visual UI)

<img width="1408" height="867" alt="image" src="https://github.com/user-attachments/assets/7eb54f26-d098-4c80-8bb8-37e85a1ef1dc" />

The Config Builder node replaces manual JSON editing with an intuitive visual interface. Instead of writing configuration arrays by hand, you can point and click to select models and LoRAs, drag sliders to adjust strengths, expand entire folders, stack multiple LoRAs, manage trigger words, and preview JSON output in real-time.

All configuration data is automatically synchronized with the Ultimate Sampler Grid node.

### Run Settings

The Run Settings section of the Builder holds options that apply to the whole run rather than to one config array (overwrite/resume, flush batch size, VAE batch size, model cache, trigger-word mode, ...). One of them:

* **Embed ComfyUI Nodes Workflow** (`pack_nodes_metadata`, off by default): write the Revise "copy as nodes" graph (checkpoint, LoRAs, both prompts, empty latent, KSampler, VAE Decode, Preview) into every saved PNG and WebP, plus the API `prompt`, so dragging the image onto the ComfyUI canvas loads it. Covers Generator images, upscales (a Note node describes the upscale), remote-VAE images, dashboard upscales and distributed worker images (stamped by the master after collection). JPG cannot carry a ComfyUI workflow; diffusion-model / GGUF / LTX video / Workflow Sweep items are skipped. The graph is rebuilt from the image's own config, so it reproduces the checkpoint + LoRA + sampler setup, not regional (COUPLE) masks or upscale chains.
* **Additional Random Seeds** (`add_random_seeds_to_gens`, 0-100): render this many extra images per config using extra seeds on top of the base seed. Handy for telling "the base model did that" from "the LoRA did that" by checking whether a quirk survives across seeds. The extra seeds are derived from the base seed, so the same base seed always gives the same extras (and resuming an interrupted run works). Contributed by DRuggeri (PR #21).

Covered in their own sections: [Job Order & Preview Pass](#job-order--preview-pass-run-settings), [Image Metrics](#image-metrics-optional), Text Encoder Batch Size ([`te_batch_size`](#performance-settings)).

### Basic Setup

1. **Add the Node:** Right-click on the canvas → `Add Node` → `sampling/testing` → `Ultimate Config Builder`
2. **Connect to Sampler:**
   - Connect the `configs_json` output to the `configs_json` input of the `Ultimate Sampler Grid (Generator)` node
   - Connect the `session_name` output to the `session_name` input of the generator (optional)
3. **Start Building:** The Config Builder UI will appear in the node with one config array ready to customize.

### Understanding the Interface

```
┌─────────────────────────────────────────────────┐
│ 📁 Session Management                          │
│ (Session name, Load session, Refresh button)   │
├─────────────────────────────────────────────────┤
│ 💾 Config Management                           │
│ (Save/Load JSON presets, Auto-save toggle)     │
├─────────────────────────────────────────────────┤
│ ⚙️ Config Arrays                               │
│ ┌─────────────────────────────────────────┐   │
│ │ Config 1                                 │   │
│ │ - Samplers, Schedulers, Steps, CFG      │   │
│ │ - Models Section (expandable)            │   │
│ │ - LoRAs Section (expandable)             │   │
│ │ - Omit Triggers Section                  │   │
│ └─────────────────────────────────────────┘   │
│ ┌─────────────────────────────────────────┐   │
│ │ Config 2...                              │   │
│ └─────────────────────────────────────────┘   │
├─────────────────────────────────────────────────┤
│ 📋 JSON Preview                                │
│ (Real-time preview of generated config)        │
└─────────────────────────────────────────────────┘
```

### Session Management

Located at the top of the interface, this section controls the output session name for your tests.

* **Session Name:** Sets the folder name where results are saved (`ComfyUI/output/benchmarks/{session_name}/`). Enter a descriptive name like `"sdxl_quality_test"` or `"character_lora_comparison"`. Changes automatically update the connected Sampler Grid node.
* **Load Session:** Load a previously saved session's metadata from a searchable dropdown.
* **Refresh Models/LoRAs:** Reload the list of available models and LoRAs from disk. Use when you've added new files or the dropdowns are showing stale data.

### Config Management (Save/Load Presets)

Save and load configuration presets as JSON files for reuse across projects.

* **Config Name (Filename):** Name for the JSON preset file. Stored at `ComfyUI/output/benchmarks/configs/{config_name}.json`.
* **Load Saved Config:** Searchable dropdown showing all available `.json` config files. Replaces current config arrays with the loaded preset.
* **Save Config Now:** Manual save button to persist current configuration to disk. Creates a reusable JSON file containing all config arrays, models, LoRAs, trigger settings, and strength locks.
* **Auto-Save (2s):** Toggle to automatically save the config file every 2 seconds. Recommended for long editing sessions.

### Config Arrays

Config Arrays are the building blocks of your testing grid. Each array defines a set of parameters that will be multiplied into all possible combinations.

### Fast CivitAI Info Lookup

<img width="1178" height="505" alt="image" src="https://github.com/user-attachments/assets/68146aae-c785-4e4b-bc5e-8a1962a14270" />

<img width="1072" height="506" alt="image" src="https://github.com/user-attachments/assets/a11178e2-0745-4e56-a9b4-5225f968b051" />

<img width="1074" height="271" alt="image" src="https://github.com/user-attachments/assets/7849d711-f939-47b5-be20-c44eb664fd19" />

#### Basic Parameters

* **Config Name:** Label for this config group (purely organizational, not used in generation).
* **Samplers:** Comma-separated list of samplers to test (e.g., `"euler, dpmpp_2m, dpmpp_2m_sde"`).
* **Schedulers:** Comma-separated list of schedulers (e.g., `"normal, karras, exponential"`).
* **Steps:** Comma-separated list of step counts (e.g., `"20, 30, 40"`).
* **CFG:** Comma-separated list of CFG scale values (e.g., `"6.0, 7.0, 8.0"`).
* **Samplers Dropdown:** Searchable dropdown auto-populated with all available samplers from the connected sampler node. Select multiple to add them as a comma-separated list.
* **Schedulers Dropdown:** Searchable dropdown auto-populated with all available schedulers. Works the same as the samplers dropdown.
* **Attention Mode:** Dropdown selector for attention implementations (`default`, `sage`, `sage3`, `flash`, `xformers`, etc.). Select multiple to test as a grid dimension.

#### Iteration Count Display

```
⏱️ Iterations: 144
```

Shows the total number of images this config array will generate:
**Formula:** Models × LoRAs × Samplers × Schedulers × Steps × CFG  
Updates in real-time as you add/remove items.

#### Config Array Controls

* **➕ Add Model** — Adds a new model slot to the Models section.
* **➕ Add LoRA** — Adds a new LoRA slot to the LoRAs section.
* **📋 Duplicate Config** — Creates an exact copy of this config array (useful for variations).
* **🗑️ Delete Config** — Removes this entire config array.
* **▼ Collapse/Expand** — Toggle visibility of Models and LoRAs sections.
* **➕ Add VAE** — Adds a new VAE slot to the VAEs section for testing multiple VAE decoders.

### Models Section

Each model card includes:

* **Model Name (Searchable):** Dropdown with fuzzy search through all available checkpoints. Supports folder structure display (e.g., `"subfolder/model.safetensors"`).
* **Type Selection:**
  - **Single File (default):** Test just this specific model.
  - **Folder (Separate):** Expand folder — each model becomes a separate test. Multiplies iteration count by number of models in folder.
  - **Folder (Combined):** *Reserved for future use.*
* **🗑️ Remove Model:** Deletes this model from the config (at least one model is always required).
* **🔘 On/Off (Bypass) Switch:** Toggle a model on or off without removing it. Bypassed models are grayed out and excluded from the generated config output.
* **🔍 CivitAI Model Lookup:** Opens a metadata panel showing model info fetched from CivitAI (name, base model, tags, creator, description). Includes a direct link to the model page.

### LoRAs Section

Each LoRA card includes:

* **LoRA Name (Searchable):** Dropdown with fuzzy search. Supports special syntax — end with `/` for folder expansion, end with `/*` for combined folder stack.
* **Type Selection:**
  - **Single File:** Load this specific LoRA.
  - **Folder (Separate):** Test each LoRA in the folder individually with the same strength settings.
  - **Folder (Combined):** Stack ALL LoRAs in the folder into a single load.
* **Model Strength Slider:** Range 0.0–2.0 (default 1.0). Controls how strongly the LoRA affects the model. Number input accepts values beyond slider range.
* **CLIP Strength Slider:** Shown when the lock is off. Range 0.0–2.0 (default 1.0). Controls how strongly the LoRA affects text encoding. Independent from model strength.
* **＋ Add Strength:** The ＋ button next to the Model Strength box adds another strength to compare, as a new row right below (up to 8 strengths per LoRA, the base sliders count as the first). With **Lock Model & CLIP Strength Together** on (the default) each row is one *Strength* slider used for both model and CLIP; with the lock off each row has its own *Model* and *CLIP* sliders and is one job (pair). ✕ removes a row. A row equal to the base or to an earlier row is greyed out ("duplicate, ignored") and skipped. Rows belong to the LoRA name, so two cards with the same LoRA share them.
* **Job count:** every strength is one full copy of the config's jobs, differing only in the LoRA strength, so the count multiplies (a config with 3 strengths and 2 samplers is 6 jobs). With several LoRAs in one config they are stacked together and you get every combination, first LoRA slowest: a LoRA with 2 strengths plus a LoRA with 3 strengths is 6 stacked entries. The Iterations counter and the preview JSON both show it. Folder entries are never stacked; their rows become separate entries.
* **🔗 Lock Strengths:** Toggle to link model and CLIP strengths so both sliders move together. Turning it on also sets CLIP = model on every extra row.
* **Old "Compare Strengths" box:** Workflows saved with the old comma-separated Compare Strengths box still load and run unchanged; their values show up as ＋ rows and are converted the first time you edit that LoRA.
* **🔍 Lookup Trigger Words:** Opens the Trigger Word Lookup Modal (fetches from CivitAI API).
* **🚫 Bypass Trigger Fetch:** Toggle to prevent automatic trigger word lookup for this LoRA.
* **🗑️ Remove LoRA:** Deletes this LoRA from the config (at least one is always required).
* **🔘 On/Off (Bypass) Switch:** Toggle a LoRA on or off without removing it. Bypassed LoRAs are grayed out and excluded from both the preview JSON and the Python node's `config_json` output.

### LoRA Trigger Words

The Config Builder integrates with CivitAI's API to automatically fetch and manage trigger words for your LoRAs.

**How It Works:**
1. When you select a LoRA, the node calculates its SHA256 hash.
2. The hash is sent to CivitAI to retrieve metadata.
3. Results are cached in `ComfyUI/output/benchmarks/loras_tags.json`.
4. Cached data is reused on subsequent loads (offline-capable).

#### Trigger Word Lookup Modal

Click the **🔍 Lookup Trigger Words** button to open the modal:

```
╔════════════════════════════════════════════╗
║ LoRA Trigger Word Manager                 ║
║                                            ║
║ LoRA: character_style_v2.safetensors      ║
║ Model: Character Style LoRA v2             ║
║ Base Model: SDXL 1.0                       ║
║ Creator: ArtistName                        ║
║                                            ║
║ Tags: character, anime, style              ║
║                                            ║
║ Trigger Words:                             ║
║ ☑️ character_name                          ║
║ ☑️ red_hair                                ║
║ ☑️ blue_eyes                               ║
║ ☐ masterpiece  (excluded)                 ║
║ ☐ best quality (excluded)                 ║
║                                            ║
║ [✅ Save Selections]  [❌ Cancel]          ║
╚════════════════════════════════════════════╝
```

* **Checkboxes** to select which trigger words to exclude.
* **Metadata display** showing model info before deciding.
* **Persist selections** — saved exclusions apply to all future generations.
* **CivitAI link** to open the model page in a new tab.

Excluded triggers are stored in the config array's `lora_omit_triggers` array and automatically filtered during generation.

#### Trigger Word Placement Control

Control exactly where trigger words are inserted in your prompts. For each LoRA with trigger words, you can choose:

* **None (Default):** Trigger words are **prepended** to the beginning of the positive prompt. Best for character LoRAs and style LoRAs that need early influence.
* **Positive Start:** Explicitly prepend to positive prompt (same as None/default).
* **Positive End:** **Append** trigger words to the end of the positive prompt. Best for quality tags and detail LoRAs.
* **Negative Start:** **Prepend** trigger words to the negative prompt. Best for negative embeddings and "anti-style" LoRAs.
* **Negative End:** **Append** trigger words to the negative prompt. Best for quality-control negative tags.

Set placement by opening the trigger word modal, selecting placement from the dropdown at the bottom, and saving. The placement is stored in `lora_triggerwords_append_settings`.

### LoRA Bypass States

Bypass states allow you to mark specific LoRAs to skip automatic trigger word fetching.

**When to use:** LoRAs without triggers, offline work, custom workflows where you're manually adding triggers, or speed optimization for known LoRAs.

Toggle the **🚫 Bypass Trigger Fetch** checkbox on a LoRA card. The card shows a ⚠️ indicator when bypassed. Bypass state is saved in the `lora_bypass_states` object.

### Strength Locking

Click the **🔗 Lock Strengths** button on a LoRA card to link model and CLIP strengths. When locked, both sliders move together maintaining the ratio. For example, if locked at 1.0/0.8 (ratio 1.25), changing model to 1.2 sets CLIP to 0.96.

Useful for maintaining tested ratios and quickly scaling both strengths up/down together.

### Folder Expansion (Models & LoRAs)

Folder expansion allows you to test entire directories of models or LoRAs without manually adding each file.

**Model Folder Expansion:** Select a folder path ending with `/` and set type to "Folder (Separate)." All `.safetensors` files in that folder are tested individually with the same settings.

**LoRA Folder Expansion — Separate:** Path ending with `/`, type "Folder (Separate)." Each LoRA in the folder is tested individually. All use the same strength settings, and trigger words are fetched for each automatically.

**LoRA Folder Expansion — Combined:** Path ending with `/*`, type "Folder (Combined)." ALL LoRAs in the folder are stacked into a single load. Creates one config with multiple LoRAs stacked at the same strength. Trigger words from all LoRAs are combined. Great for quality enhancement stacks, multi-concept combinations, or testing "everything at once" scenarios.

### LoRA Stacking

Combine multiple LoRAs into a single generation by adding multiple LoRA slots to a config array.

**Manual Stacking:** Click **➕ Add LoRA** multiple times and configure each independently with different files, strengths, and trigger settings. All selected LoRAs are applied simultaneously.

**Generated config format:**
```json
{
  "lora": "character_lora.safetensors:1.0:1.0 + style_lora.safetensors:0.8:0.8 + detail_lora.safetensors:0.5:0.5"
}
```

**Mixed Expansion + Manual:** You can combine folder expansion with manual stacking — for example, a combined quality folder plus a specific character LoRA stacked together.

### VAEs Section

Each VAE card includes:

* **VAE Name (Searchable):** Dropdown with fuzzy search through all available VAE models. Supports folder structure display.
* **Type Selection:**
  - **Single File:** Test just this specific VAE.
  - **Folder (Separate):** Expand folder — each VAE becomes a separate iteration, multiplying the total grid size.
* **🗑️ Remove VAE:** Deletes this VAE from the config.

VAEs are treated as a Cartesian dimension just like samplers or models. If you add 3 VAEs, your total iteration count is multiplied by 3.

### Attention Modes

Select which attention backend implementations to test. Available options depend on your system (e.g., `default`, `xformers`, `pytorch`, `flash`, `sage`, `sage3`, `sub_quad`, `split`; a backend that is not installed is skipped with a warning and the job runs with default attention). If a backend is installed but fails while sampling, the job is retried once with default attention and the item records `attention_fallback` (the mode that failed). Like other parameters, you can select multiple modes and they become a grid dimension.

### Skip Layer Guidance (DiT models)

**Extra Model & Sampling Options → Skip Layer Guidance** wraps ComfyUI's `SkipLayerGuidanceDiTSimple` node: between Start % and End % the negative (uncond) pass skips the listed transformer blocks, which sharpens structure on DiT models (MOSS-Image, Flux.2, SD3, ...). Fields: Double Layers, Single Layers (comma-separated block indices), Start %, End %. The defaults are the official MOSS-Image workflow's values (single block `22`, 0–50 %); ComfyUI's generic default is `7, 8, 9`. Every image in the config array gets the patch, so compare with/without by duplicating the array.

JSON: `"use_slg": true, "slg_single_layers": "22", "slg_double_layers": "", "slg_start_percent": 0.0, "slg_end_percent": 0.5`

### MOSS-Image, Flux.2, Krea 2 (16 px latent models)

Set **Model Type = Diffusion Model**, pick the diffusion file (e.g. `moss_image_sft_int8_convrot.safetensors`), the text encoder (`qwen3.5_9b_w4a8_gptq.safetensors`), **CLIP Type = `moss_image`**, and the Flux.2 VAE (`flux2-vae.safetensors`) in the VAEs section.

* The CLIP Type list is read from your installed ComfyUI's `CLIPLoader`, so new model families appear without a plugin update. If you leave it at `stable_diffusion` for a diffusion model, the generator picks the CLIP type that matches the detected model family and logs it (MOSS-Image needs `moss_image` to get its chat template; with `stable_diffusion` ComfyUI builds a generic Qwen3.5 encoder).
* The empty latent follows the model's latent format: 16 px per latent cell for the Flux.2 family, 8 for SD / SDXL / Flux.1. Use sizes that are multiples of 16; a 832x1216 job renders at 832x1216. Earlier releases always used 8, which made 16x models render at double size and run ~10x slower than the stock workflows.
* Pre-encoding loads the text encoder once per pass instead of once per prompt (ComfyUI's dynamic VRAM loader re-prepares a model on every encode, which is the repeated `Model ... prepared for dynamic VRAM loading` log line). What remains is the encoder itself: the Qwen3.5-9B encoder costs roughly 0.8 s per prompt on a 16 GB card, the same as the stock workflow, so a 60-prompt grid spends about a minute encoding before the first image. SDXL's CLIPs take about 0.15 s per prompt, Krea 2 and Qwen-Image about 0.3 s. The pre-encode summary line reports the measured ms/prompt.
* Text-encoder batching (`te_batch_size`, default 1 = off) puts several prompts through one encoder forward, which amortises the encoder's fixed per-forward cost; details in [`te_batch_size`](#performance-settings).

### Model-Specific Prompts

Per-config prompt prefix and suffix fields that are prepended/appended to all prompts generated by that config array:

* **Prompt Prefix:** Text prepended to the positive prompt (e.g., `"masterpiece, best quality, "` for anime models).
* **Prompt Suffix:** Text appended to the positive prompt (e.g., `", 4k, photorealistic"` for realistic models).

These fields are especially useful when testing multiple models that require different quality tags or style descriptors.

### Recursive Cartesian Prompt Builder

A visual chip-based prompt editor that supports variation groups using `{option1|option2|option3}` syntax:

```
a {photo|painting|sketch} of a {cat|dog} in a {forest|city}
```

This expands into all combinations (3 × 2 × 2 = 12 prompts):
- "a photo of a cat in a forest"
- "a photo of a cat in a city"
- "a painting of a dog in a forest"
- ... etc.

The editor provides a visual chip interface for building and editing these variation groups. Each group is displayed as a clickable chip that can be expanded to add/remove options. Multiple groups can be nested for exponential prompt variation.

### Prompt Combinators & Regional Prompts (COUPLE)

Positive and negative prompts understand these keywords (capitals, as their own word):

* `A AND B` makes separate conditioning entries (a trailing ` :1.3` after a part is its weight), `A CAT B` concatenates token contexts, `A AVG(0.3) B` blends two prompts, `BREAK` starts a new 77-token chunk.
* `COUPLE` splits the image into regions, each with its own prompt, using ComfyUI's native masked conditioning (no extra nodes or patches).

```
[<base>] COUPLE[(<layout>)] <region1> | <region2> [| <region3> [| <region4>]]
```

* `COUPLE` or `COUPLE(cols)`: regions side by side, left to right. `COUPLE(rows)`: stacked bands, top to bottom.
* 2 to 4 regions of equal size, separated by a top-level `|` (a `|` inside `()`, `[]`, `{}` or `<>` is not a separator).
* The text before `COUPLE` is the **base**: it applies to the whole image. Regions are not prefixed with the base; the base and the region are blended in each region's area.
* A region may end with ` :w` (space, colon, number) to weight it; ` :0` turns the region off. An empty region (`a | | b`) leaves that part of the image to the base. Lowercase `couple` is plain text.
* A region can use `AND` / `CAT` / `AVG()` / `BREAK` too. Invalid syntax (one region, more than four, unknown layout, two `COUPLE`, an empty base with an empty region) stops the run before any model is loaded, listing the bad prompts.

Examples:

```
no humans, scenery, sports car COUPLE red sports car | blue sports car
2girls, park, sunny COUPLE(cols) 1girl, red hair AND smiling | 1girl, blue hair :1.3
sky, mountains, masterpiece COUPLE(rows) clouds, sunset | snowy peak
```

Notes:

* Each region costs one extra model pass per sampling step.
* Text that is added after the prompt goes into the **base**, not the last region: LoRA trigger words, the model prompt prefix/suffix, and the HiRes prompt with "Append to end". HiRes "Replace" drops the regions (the replacement text is used as is). "Prepend" adds the text in front of the whole prompt, which makes it part of the base.
* Prompt groups in the Builder are joined with `, `, so text in a later group lands in the last region. Put the `COUPLE` text in the **last** prompt group.
* Masks are built at the size of the latent being sampled, so HiRes, tiled HiRes, Florence2 HiRes crops and img2img latents all work.
* Image metrics that use the prompt text (such as ImageReward) score the plain text with the markers removed.

Limitations: no per-region LoRAs, equal splits only (no ratios), hard region edges, not supported by Workflow Sweep or LTX video (the text is encoded literally, and LTX prints a warning), and distributed workers must run the same USCG version (an older worker ignores the tag and applies every region to the whole image, without an error).

### Job Order & Preview Pass (Run Settings)
Both live in the **Run Settings** section of the Config Builder and default to the old behaviour.

* **Job Order:** `As written (default)` runs one resolution pass after another, exactly as before. `Minimize model/LoRA reloads` re-groups the job list by model, LoRA stack, VAE and resolution. `As written` is already grouped by model (and Builder per-config resolutions stay inside their model group), so Minimize only changes anything when LoRA folders or random LoRA picks expand into different stacks (e.g. a model with 2 LoRA folders alternating A1 B1 A2 B2 becomes A1 A2 B1 B2), or when a batched latent is connected (one pass per latent). LoRA stacks are grouped before VAEs, so a model with several VAEs and several LoRA stacks can switch VAE more often than as written. The log prints the model/LoRA/VAE switch counts before and after and says when nothing changed. **Start At Job #** numbers follow the chosen order. In distributed mode the master computes the order and queues jobs to workers in it (see **Distributed parity** below); Start At Job skips the earlier plan positions there too, and they count as done in the progress bar.
* **Preview Pass:** renders every cell cheaply first (fewer **Preview Steps**, smaller image via **Preview Scale** x0.25/0.33/0.5/0.75 snapped to the model's latent grid, optional **Preview CFG Override**, upscaling skipped) so you see the whole grid in a fraction of the time. Preview images carry a `PREVIEW` badge on the Dashboard. Reject the losers, then **untick Preview Pass and queue again**: only the surviving cells render at full quality, and each full image replaces its preview in the default Dashboard view. Interrupted preview passes resume (previews already done are skipped), and a preview pass skips cells that already have a full image. Not used when a latent input is connected; LTX video configs always render normally. Works in distributed mode too (the master decides which cells to render and stamps every preview, whichever machine rendered it).
* **Skip Rejected Previews** (default on) and **Only Favorited Previews**: apply when Preview Pass is OFF. Cells whose preview you rejected are skipped, including after **Delete Rejected** (the rejection is remembered in `meta.rejected_preview_fps`). With *Only Favorited*, a cell that has a preview is rendered only if that preview is favorited; cells with no preview are still rendered. `Overwrite Existing` does not override a rejection.
* A cell is identified by a **config fingerprint** (model, LoRA stack, VAE, text encoders, sampler, scheduler, CFG, denoise, seed, raw prompts, full resolution, plus advanced-sampling/SLG/deep-shrink settings; *not* steps). Cells whose seed is re-randomised on every run (`random_before`, extra random seeds) cannot be matched to a preview and simply render again.
* ETA: preview and full jobs cost roughly 10x apart and the rolling average lags when slow models are grouped together; treat the ETA as approximate under Minimize.

### Image Metrics (Optional)

Run Settings has a **Compute Image Metrics** checkbox (default OFF). When it is on, every saved still image (base generations and upscales; videos are skipped) gets a `metrics` object in `manifest.json`, computed from the decoded image at save time (about 1-5 ms per image on the GPU, nothing when the box is unchecked):

| Metric | What it is | Range |
|---|---|---|
| `sharpness` | Variance of the 3x3 Laplacian of luma on the 0-255 scale (OpenCV-style "variance of Laplacian") | 0 = flat, large = lots of edges |
| `entropy` | Shannon entropy of the 256-bin luma histogram | 0-8 bits |
| `colorfulness` | Hasler and Suesstrunk (2003) colorfulness | ~0 grey, >100 very colorful |
| `contrast` | Standard deviation of luma (RMS contrast) | 0-0.5 |
| `luma` | Mean brightness (Rec.601 luma) | 0-1 |
| `saturation` | Mean HSV saturation | 0-1 |
| `sobel` | Mean Sobel gradient magnitude of luma (0-1 scale; kernels /4, so a full black-to-white step reads 1) | 0 = flat; most generations land well under 0.2 (measure your own); max ~1.41 |

Notes:
* `sobel` complements `sharpness`: it responds to real edges and ignores pixel-level noise (a 1-pixel checkerboard reads 0 Sobel but a huge sharpness), so a high Sobel with a moderate sharpness means structure, not grain. It is absent for images smaller than 3 px on a side.
* Metrics are measured on an "analysis image": the long side is block-averaged down to at most 1024 px (by the smallest integer factor), so a 2x upscale stays comparable with its 1024 base image and the cost is capped. The constant is `ANALYSIS_MAX_SIDE` in `image_metrics.py`; changing it would make old sessions incomparable.
* They measure image **signal, not taste**: noise raises sharpness and entropy, and a dark moody image is not a worse one. Use them to rank and filter, then look.
* Upscales are measured again (a derived image never inherits its source's numbers). Dashboard-triggered upscales measure only when the source image had metrics.
* Items from remote Distributed workers are measured too: the worker computes the built-in metrics on its decoded image, and the master scores the optional scorer packs for every worker image in one pass after collection (so workers do not need the scorer pack installed). An older companion/worker sends no metrics and the master measures the saved file instead; workers on an older USCG omit Sobel, and the master measures it from the saved file.
* Optional scorer packs plug in through `nodes.NODE_CLASS_MAPPINGS` without any import, and their scores are stored next to the built-ins. The Builder lists each pack with `installed`, `installed, but <problem>` (for example "no model file in models/aesthetic") or `not installed (install ...)` (text only, nothing is downloaded); the checkbox is only clickable when the pack is usable. See **Optional scorer packs** below.

**Optional scorer packs**

* **Aesthetic score** (`metrics.aesthetic`, verified end to end) uses the [Strimmlarn's Aesthetic Score](https://github.com/strimmlarn/ComfyUI-Strimmlarns-Aesthetic-Score) pack (pinned and tested at `42bed3f`; the pack is unmaintained). The value is the LAION improved-aesthetic-predictor score on a roughly 1-10 scale (most generations land between 4 and 7; the node quantises it to 0.01). It is a taste proxy trained on human ratings, not a quality guarantee, and it is not comparable with the built-in signal metrics. Install, with ComfyUI stopped:
  1. `git clone https://github.com/strimmlarn/ComfyUI-Strimmlarns-Aesthetic-Score` into `custom_nodes/` (check out `42bed3f` to match what was tested).
  2. `python -m pip install --no-deps "clip @ git+https://github.com/openai/CLIP.git"` and `python -m pip install pytorch-lightning` (the pack imports it but its requirement file does not list it; no torch change was needed in our test).
  3. Put `sac+logos+ava1-l14-linearMSE.pth` (3.7 MB, from `christophschuhmann/improved-aesthetic-predictor`) into `ComfyUI/models/aesthetic/`. The pack forces that folder, so `extra_model_paths` entries for it are ignored.
  4. The first run downloads the CLIP ViT-L/14 weights (933 MB) to `~/.cache/clip/`; copy `ViT-L-14.pt` there first to keep that download out of a timed run.
  USCG passes **one image per call** (the node only scores image 1 of a batch) and rescales the node's integer x100 output. The node reloads CLIP from disk on every call, so expect several seconds per image (measured 7.6 s per image on an RTX 3070 8 GB next to an SDXL 1024x1024 run, about 0.9 GB extra VRAM; the SDXL run itself took 10-16 s per image). USCG asks ComfyUI's memory manager to free VRAM before each call. On a card this small a model may be evicted and reloaded, which is slower but correct. The node hardcodes `cuda`, so CPU/MPS/AMD hosts fail and the adapter switches itself off for the run with one warning (the built-in metrics are unaffected). A per-adapter timing line (`[GridTester] 📏 metric adapter 'aesthetic': N images, mean X ms`) is printed when the run ends.
* **ImageReward** has a registry entry checked against the source of `ZaneA/ComfyUI-ImageReward@5e9936d` (prompt comes from the item's positive prompt, score is the FLOAT output, roughly -2 to +2 and relative to the prompt, so only compare scores of the same prompt), but it ships **disabled**, and a wave-3 feasibility check (11/4/26) confirmed why: the only PyPI release the pack pins, `image-reward==1.4`, fails to import under transformers 5 (`find_pruneable_heads_and_indices` and `PreTrainedModel.get_head_mask` were removed), so it needs a hand patch of `site-packages/ImageReward/models/BLIP/med.py` on every transformers-5 host; it also pins `timm==0.6.13`, builds `fairscale`, downloads 1.8 GB on first load and may trip `torch.load(weights_only=True)`. On a transformers-4 host that has the pack working, enabling it is a one-word change in `image_metrics.ADAPTERS` (set `enabled` to True); note the score uses only the first ~35 BERT tokens of the prompt, so compare within one prompt only.
* **In the Dashboard:** once a session has metrics, the Sort popup gains one option per metric (descending, items without the metric sort last, in both the primary and secondary lists), the Logic Filter field list gains a **Metrics** group, and a **Metric range** row adds `>= min` / `<= max` filters in one click (placeholders show the observed range). The label panel has a **Metrics** checkbox that prints `Shp:812 Ent:7.41 Col:41.2 ...` on each card. Logic filters skip items that lack the field, so images without metrics (older items, videos) stay visible; Quick Filter is categorical and does not list metrics, use the Logic Filter for ranges. Sessions without metrics show none of this.
* **Older sessions:** the cog panel's **IMAGE METRICS** section has **Compute metrics for this session**, a background job (CPU only, no VRAM, about 50 ms per image) that measures every image that is missing any metric (for example Sobel on sessions measured before it existed; values already stored are never changed), skips videos, shows progress and can be cancelled by clicking the button again. It rewrites only the `metrics` field under the manifest lock, so favorites and notes you change meanwhile survive. Do not run it on a session that is still generating.
* The setting is session-level (like GPU Cooldown), so it is NOT a per-config field: it lives in `_session_settings.metrics`, not in `_EXPECTED_CONFIG_KEYS` or `expand_configs`.

### Workflow Sweep (sweep any ComfyUI workflow)

**Add Workflow Sweep** (next to Add Config Array) turns a config array into a sweep over *your own ComfyUI workflow*. Instead of USCG re-implementing a model family, the workflow you exported runs as-is through ComfyUI's own executor, one prompt per job, and every image lands in a normal USCG session (manifest, dashboard, favorites, filters, export).

1. In ComfyUI export the workflow with **Workflow > Export (API)**. Load that file (or paste it) in the Workflow Sweep section. Editor-format JSON (with `nodes` and `links`) is rejected with a hint.
2. **Image to collect**: the IMAGE socket that feeds the first Save Image is picked automatically; change it in the dropdown. Only the nodes upstream of that socket run (the workflow's own Save Image / Preview nodes are skipped unless you tick *Also run the workflow's own outputs*).
3. **Sweep axes**: click a *Suggested* chip or `＋ sweep` next to any input in the node list. Each axis is one input (or several that must share a value, e.g. a seed feeding two nodes) with a list of values; the job count is the product of all axes. Special axes: **Positive / Negative prompt** (values come from the config's Prompts section, with the usual groups and 1-to-1 pairing rule), **LoRA** (bind LoraLoader nodes as slots; `name:0.8`, weight arrays `name:[0.5,1.0]`, folders and `None` work as in standard configs), **Resolution** (`WxH` into two width/height inputs). A linked input can be replaced by a literal with `＋ override link`.
4. **Dry run** shows the first concrete prompts (template plus your substitutions plus the collector node), the validation result of job 1 and the exact job count, and lets you download a job as API JSON to compare by hand. **Start sweep** starts the run from the Builder; queueing the **Generator** node starts the same sweep and returns the dashboard immediately. **Pause / Resume / Cancel** control it, and a status line follows it.

How it behaves:
* Jobs are queued two at a time through ComfyUI's normal queue (so you can keep using ComfyUI, and nothing blocks the executor). Axes are ordered so loader values stay adjacent (checkpoint outermost, sampler settings innermost), which lets ComfyUI's cache keep models loaded between jobs. `--cache-none` or very tight RAM reloads models every job.
* Each job has a fingerprint of the exact substituted workflow. Starting the same sweep again (also after a ComfyUI restart) skips jobs already in the session; *Overwrite existing* re-runs them and replaces the old image.
* A failed job is recorded and the sweep continues; three failures in a row pause it. Pressing Cancel in ComfyUI during a job, or clearing the queue, pauses the sweep instead of silently finishing; Resume re-runs the affected jobs.
* Manifest items get the normal fields (model, sampler, scheduler, steps, cfg, seed, denoise, vae, size, prompts) read from the workflow, plus `wf_params` (your bound values), `wf_fingerprint`, `wf_sweep_id`. Sweep items show a **JOB** button instead of REVISE (see *Dashboard for sweeps* below).
* Each sweep writes `benchmarks/<session>/workflow_sweeps/<sweep_id>.json` (templates, bindings, per-job status) so any executed prompt can be reconstructed.
* **Re-running the same sweep attaches to it.** Queueing the Generator again (or pressing Start) while the identical sweep is active does not fail and does not queue anything twice: it attaches to the running sweep (console: "Same workflow sweep already running ... attaching") and a paused sweep stays paused (Resume is the Builder's button). "Identical" means the same session name, the same ordered job fingerprints, the same *Start at job* and the same *Overwrite existing*. Anything else gets a clear refusal ("A workflow sweep is already active (session ..., sweep ..., n/m done, state). This run was NOT started. Pause or cancel it ..."; ComfyUI shows it in its error dialog, the route answers 409 with `session_name`). *Add random seeds* are deterministic (derived from the base seed, 0 like the Generator), so the same sweep always produces the same jobs: re-queueing attaches, and a resume after a finished or interrupted run skips the jobs already in the session.
* **Loading a sweep session in the Builder** (Load Session) restores the Workflow Sweep arrays (workflow, output, bindings, custom prompts) from the `configs_json` that sweep sessions now store in their manifest meta. Sessions made before this change have no saved configs: the Builder shows a notice ("Load the workflow JSON again into a Workflow Sweep array; finished jobs are skipped by fingerprint") and leaves the arrays alone.
* * **Video outputs.** *Output to collect* lists *Images* and *Video* sources. Video sources are: the feeder of a `SaveVideo` (a VIDEO socket, e.g. `CreateVideo`), the frames feeding a `VHS_VideoCombine`, `SaveWEBM`, `SaveAnimatedWEBP` or `SaveAnimatedPNG` (marked "frames"; the sweep splices a core `CreateVideo` node in front of the collector with the sink's `frame_rate` / `fps` (and the VHS `audio`), so a swept fps works), and any node that returns a VIDEO. A SaveImage/PreviewImage feeder is still the default when the workflow has one; a video-only workflow (no SaveImage) now defaults to its video output. Each job saves ONE mp4 (H.264, through ComfyUI's own `VideoInput.save_to`, the workflow embedded as metadata) plus a middle-frame poster `vid_<id>.preview.png` into `benchmarks/<session>/images`, with the same manifest fields as LTX videos (`media_type: "video"`, `video_path`, `preview_path`, `poster`, `frames`, `frame_rate`, `duration_seconds`). Cards play the video; **JOB** stays available and the Compare view plays both videos. Resume and *Overwrite existing* work as for images (the old mp4 and its poster are deleted); a video and an image collection of the same socket never skip each other. Limits: VHS `format`, `loop_count` and `pingpong` are ignored (always mp4/h264); the WEBM `codec`/`crf`, WEBP `lossless`/`quality`/`method` and APNG `compress_level` settings are ignored too, alpha is dropped, and a literal fps outside CreateVideo's 1-120 is clamped (with a warning); a VHS node fed with latents (`vae` input) or a `meta_batch` is not offered as a source; one video per job; the workflow's own SaveVideo/VHS node only runs with *Also run the workflow's own outputs*; collecting a file-backed VIDEO (e.g. `LoadVideo`) decodes all its frames into RAM once to make the poster.
* **Mixed runs.** A Builder with both standard arrays and Workflow Sweep arrays runs in ONE Generator queue: the standard configs run first, then the sweep starts into the same session (and the same manifest). The sweep is validated (job 1) and checked for a conflicting active sweep BEFORE the standard jobs start, so a broken workflow fails early ("nothing ran"). *Start At Job* is one global numbering: standard jobs 1..N, sweep jobs N+1.. (the Builder's own *Start sweep* button keeps sweep-only numbering). *Overwrite existing* applies to both phases. The Preview pass and the optional_* inputs apply to the standard configs only. Cancelling during the standard phase means the sweep never starts; cancelling during the sweep uses the sweep's pause/resume. The dashboard bar shows "Standard jobs complete ... Workflow sweep next" and then "Sweep job x/M".
* v1 limits: one image or video output per job, one sweep at a time, no upscale/distribution/trigger-word features, and Revise does not apply.

**Dashboard for sweeps.** Items carry `wf_params` (the bound values, numbers or strings). The **Quick Filter** gets one extra type per *varied* key (`WF cfg`, `WF sampler_name`, ...; picking a value filters and the facet panel lists them), the **Logic Filter** gets a *Workflow params* group of the numeric keys (`wf:KSampler.cfg >= 5`), and the **Labels** panel has a *Workflow params* checkbox that tags each card with its varied values (`cfg:4`). Standard sessions show none of this. The **JOB** button opens a read-only *Workflow job* panel (source, output, sweep id, job number, parameter table) with **Download job prompt (API JSON)** and **Copy job prompt**: `GET /config_tester/sweep/job_prompt?session_name=&sweep_id=&job_index=` rebuilds the prompt exactly as it ran (template + substitutions) minus the USCG collector node, so queueing it in ComfyUI reproduces the image. If the browser blocks the download inside the dashboard iframe, use Copy.

---

## 🖥️ Dashboard Interface

### Header Bar
* **Model/Prompt Info:** Shows current model and prompt metadata.
* **Go to Image #:** Jump directly to any image by entering its number (shown in bottom-left of cards).
* **Column Count:** Set fixed grid columns or leave at 0 for auto-sizing.
* **Zoom Controls:** `⊙` (reset), `−` (zoom out), `+` (zoom in).

### Toolbar
* **⚙️ Settings Panel (Gear Icon):** Opens a unified settings panel with four sections:
  - **Session:** Name input + SAVE/LOAD buttons. Dashboard auto-loads when connected to sampler and generation starts.
  - **Grid Display:** Go to Image #, Column Count, Reset Zoom controls.
  - **Export Favorites:** Export starred images to a dedicated folder with optional CivitAI metadata packing.
  - **Scan External Directory:** Load image sessions from any folder path into the dashboard.

* **ETA Progress Bar:** During generation, a real-time progress bar appears in the header showing estimated time remaining and completion percentage.

* **Filter Groups:** Click colored buttons to toggle visibility:
  - **Model** (Purple): Filter by checkpoint
  - **Sampler** (Cyan): Filter by sampler type
  - **Scheduler** (Blue): Filter by scheduler
  - **Denoise** (Red): Filter by denoise value
  - **LoRA** (Orange): Filter by LoRA configs
  - **Shift+Click:** Isolate single filter (deselect all others)

* **Sort Button:** Cycles between **Sort: Oldest** (default), **Sort: Newest**, and **Sort: Fastest** (by generation time). Preference is saved to localStorage.

* **Fullscreen Button (⛶):** Expand dashboard to fill entire screen.

### Navigation & Controls

**Mouse:**
- Left-click or middle-click drag to pan
- Scroll wheel to zoom in/out
- Right-click on canvas to focus for keyboard controls

**Touch (Mobile/Tablet):**
- Single finger drag to pan
- Two finger pinch/spread to zoom
- Tap card to reveal buttons

**Keyboard:**
- `Space` — Scroll down one row
- `Shift+Space` — Scroll up one row
- `↑↓←→` — Pan in any direction
- `+/-` — Zoom in/out
- `0` — Reset zoom to 1:1
- `F` — Auto-fit first row to viewport width

### Card Overlays
* **Bottom Left:** Index number (#1, #2, etc.) — used for "Go to #" feature.
* **Bottom Right:** Generation time in seconds.
* **Top Left (on hover):** Red ✕ button to reject/hide image.
* **Top Right (on hover):** Gold ⭐ button to favorite image, and green "REVISE" button to open studio view.
* **Bottom Center:** amber `PREVIEW · N st` badge on preview-pass images (hover for the full-quality size/steps it stands in for).

### JSON Bars (Bottom — Horizontal Layout)
* **Green Bar (Left — Accepted):** Contains optimized JSON of all currently visible images. Click to select all, then copy-paste back into the `configs_json` widget to refine your batch.
* **Gold Bar (Center — Favorites):** Contains configs of all images you starred with ⭐. Your best-performing settings in one place.
* **Red Bar (Right — Rejected):** Contains the configs of images you deleted with the ✕ button. Know what to avoid.

### Revision Modal

Clicking **REVISE** on a card opens the studio view:
1. **Left:** Full-resolution preview.
2. **Top Right — Read-Only Info:** Model used, seed number, positive prompt (with trigger words if applicable), negative prompt.
3. **Bottom Right — Adjustable Parameters:** Sampler, Scheduler, Steps, CFG, Denoise, LoRA.
4. **Bottom:** "Related Variants" reel showing other images with the same seed.
5. **GENERATE NEW:** Queues the specific config you just edited.

### Pairwise Review (blind A/B compare + scoreboard)

The star is an absolute signal that says little about which *setting* wins. Compare mode records fast two-up votes and rolls them up per setting.

* **Start:** the two-rectangles button in the dashboard header, the `C` key, or the cog panel section **PAIRWISE REVIEW**. Votes go through the current filter and never include rejected items.
* **Pairing modes:** *Matched* (same prompt and seed, different settings), *Same settings, different seed* (noise-floor check), *One axis at a time* (exactly one of model, LoRA, sampler, scheduler, CFG, steps, denoise, resolution, prompt, upscale differs; optional axis focus) and *Random* (same media type). Pairs prefer items with few votes and never mix images with videos. When every unvoted pair is used up the queue repeats voted pairs and shows a badge.
* **Blind by default:** only "A" and "B" are shown, placement is randomised per pair. After a vote a short reveal (off / 1 s / 2 s) outlines the winner and shows only the settings that differ. Any key or tap during the reveal advances without voting. Tap or click an image to vote for it. Panes stack on portrait phones.
* **Ratings:** votes feed a Bradley-Terry model (ghost-player prior, 1500 = average). Sort the grid by **Rating**, or enable the **Rating** field in Label Mode to see `★rating · votes` on voted cards.
* **Scoreboard:** per axis, win % (ties count half) with 95% Wilson intervals and the mean rating of the items with that value. Only votes where exactly one axis differs are attributed (a hidden difference such as the VAE blocks attribution; the footer lists the most common extra differences). Rows with fewer than 3 pairs read "not enough data". Seed is a noise-floor block: if seeds alone "win" as much as settings do, the other numbers are noise. Copy JSON / Copy CSV export the board.
* **Storage:** votes live in the session `manifest.json` as a top-level `comparisons` list `[{a, b, winner, ts, mode, blind?}]` (`a`/`b` are item ids, `a` is the left/top item, `winner` is `a`, `b` or `tie`). Old manifests without the field work unchanged. Votes for items that were deleted stay on disk and are ignored. Every manifest writer (generation saves, the remote VAE worker, the legacy `save_manifest` route) keeps the on-disk `comparisons` untouched. A directory re-scan (`scan_directory`) regenerates item ids, so votes of a scanned session are not carried over.
* **Routes:** `POST /config_tester/save_comparisons` `{session_name, append: [...], remove: ["ts:a:b", ...]}` and `POST /config_tester/clear_comparisons` `{session_name}`. They only touch `comparisons`.
* **Phone:** the lightbox is stacked (preview on top, form below) with a pinned action bar `Prev | Favorite | Reject | Compare | Revise | Next`; **Compare** opens compare mode from the lightbox. On a phone swipe **left = A**, **right = B** (same as the arrow keys); a tap on a pane still votes, a short or mostly-vertical drag does nothing. Videos autoplay muted and inline side by side (a play button appears if the browser refuses autoplay). The standalone page header has a share button (system share sheet, else copies the link) and a session picker button.
* **Manifest fields:** every upscaled item carries `base_width` / `base_height` (the size of the generated image the upscale started from; compare's Resolution axis uses them, older manifests fall back to an estimate from `upscale_ratio`). Scanned folders get `source_relpath` and **stable ids** (derived from the relative path, in `[2^52, 2^53)`, so they never collide with generated ids), so re-scanning a folder keeps favorites, notes, metrics and votes.
* **Caveat:** win % across mixed opponents is not a controlled effect size; pair choice is biased by the filter and the low-vote preference. Use it to rank candidates, then confirm with a matched one-axis run.

### Stats Panel (per-setting analytics)

The **bar-chart button** in the header bar (or **SETTINGS STATS (PER AXIS)** in the cog panel's Manifest Analytics section) opens a docked panel in the top-right corner (bottom of the screen on phones). It is not a modal: it stays open while you favorite, reject, filter, vote and while new images arrive, and refreshes itself (at most 4 times per second).

* **One table per setting:** model, LoRA, sampler, scheduler, steps, CFG, denoise, resolution, attention mode, upscale, pass (preview or full), prompt, plus every Workflow Sweep parameter (`wf_params`; parameters with more than 64 distinct values, such as seeds, are skipped). Axes where every item has the same value are folded into a "Same for every item" line.
* **Columns:** n, Fav % and Rej % (share of that value's items), Avg s (mean generation time), one column per metric the session has (mean over the items that have it) and Rating (mean pairwise rating, only after you voted). Click a header to sort; the choice is remembered.
* **Small samples:** rows with fewer than 3 items are dimmed and always sorted below the rest; the best Fav % row (3 or more items) is highlighted.
* **Scope:** *Current filter* applies the Quick/Button/Logic/Search filters but not the Favorites / Non-Favorited / Rejected visibility toggles, so rejects and favorites are still counted when the grid hides them (otherwise Reject % would always read 0). *Whole session* counts everything except superseded previews.
* **Copy Markdown** copies every table for the current scope and sort, ready to paste into an issue or chat.
* Press `Escape` (after the Filters popup) or the X to close; the panel can also be collapsed to its title bar.

### Standalone Dashboard (phone / second monitor)

The dashboard is also served as a normal web page, with the same live updates as the node:

```
http://<comfyui-host>:8188/config_tester/dashboard?session=<session_name>
```

- Without `?session=` you get the session landing cards; picking a session updates the URL, so refresh keeps your place.
- Open it from the node with the **↗** button in the dashboard header (it opens the page for the session you are viewing).
- It opens its own ComfyUI websocket, so new images and the ETA bar update live while a run is going. After your phone sleeps, it reloads the session when you come back, without duplicating cards. Reverse proxies that do not upgrade websockets (some Tailscale Serve / nginx setups) lose live updates; the **R** key and the resume reload still work.
- Touch screens get 44px buttons, and the lightbox gets a bottom bar (Prev / Favorite / Reject / Revise / Next). The in-node view is unchanged apart from the extra header button.
- **GENERATE NEW** in the lightbox queues through the run API below, into the session you are viewing. "Pack workflow" in export needs the ComfyUI tab and is disabled here.
- **Lazy loading:** the page itself is a small shell (~70 KB, ~12 KB gzipped); the dashboard code is two cached files, `/config_tester/dashboard_bundle_js` (~409 KB, ~99 KB gzipped) and `_css` (~49 KB, ~9 KB gzipped), referenced by content hash with `Cache-Control: immutable`, so the browser downloads them once and every later load (and every node iframe) pays only the shell's 304. Editing a file in `resources/` changes the hash, so a reload picks it up. The image data comes from `GET /config_tester/manifest?session=<name>` (compact JSON, gzip, `ETag`). A 1000-image session is about 160 KB over the wire instead of 3.7 MB of page plus 3.5 MB of `manifest.json`, and a phone that wakes up and finds nothing new pays one 304. The page, the bundles and the manifest all answer `If-None-Match`. `--enable-compress-response-body` is not needed. Set `USCG_INLINE_DASHBOARD_ASSETS=1` to inline everything into the page again (one self-contained document).
- Like ComfyUI itself, the page has no authentication. Only expose it on a network you trust.

---

## 🎯 Example Workflows

Ready-to-load workflow files for each model family live in [`examples/`](examples/README.md).

### Quick Quality Test (40 images)
```json
[
  {
    "sampler": ["dpmpp_2m", "euler"],
    "scheduler": ["karras", "normal"],
    "steps": [20, 30],
    "cfg": [6.0, 7.0, 8.0],
    "denoise": "1.0"
  }
]
```

### Multi-Model Comparison (9 images)
```json
[
  {
    "sampler": "euler",
    "scheduler": "normal",
    "steps": 25,
    "cfg": 7.0,
    "model": [
      "model_v1.safetensors",
      "model_v2.safetensors", 
      "model_v3.safetensors"
    ]
  }
]
```
Set `add_random_seeds_to_gens: 2` to get 3 variations per model (27 total images).

### LoRA Stack Testing (24 images)
```json
[
  {
    "sampler": "euler",
    "scheduler": "normal",
    "steps": 25,
    "cfg": 7.0,
    "lora": [
      "None",
      "style.safetensors:0.6:1.0",
      "style.safetensors:0.8:1.0",
      "style.safetensors:1.0:1.0",
      "style.safetensors:0.8:1.0 + detail.safetensors:0.5:1.0",
      "style.safetensors:1.0:1.0 + detail.safetensors:1.0:1.0"
    ]
  }
]
```

### Random LoRA Selection

Randomly select LoRAs from a folder for variety and experimentation:

**Basic:** `"lora": "XL/Styles/[3,0.85]"` — Selects 3 random LoRAs at strength 0.85 (seed-based, reproducible).

**Truly Random:** `"lora": "XL/Styles/[3,0.85,random]"` — Add `random` keyword for non-reproducible selection.

**Dual Strength:** `"lora": "XL/Characters/[2,0.8,0.6]"` — Model strength 0.8, CLIP strength 0.6.

**Combined with Regular LoRAs:**
```json
"lora": "XL/base.safetensors:1.0 + XL/Styles/[2,0.7] + XL/Details/[1,0.5,random]"
```
Loads `base.safetensors` always, picks 2 reproducible style LoRAs, and picks 1 truly random detail LoRA.

### Full Model Folder Test
```json
[
  {
    "sampler": "dpmpp_2m",
    "scheduler": "karras",
    "steps": 25,
    "cfg": 7.0,
    "model": "realistic_models/"
  }
]
```

### CLIP Skip for Anime Models
```json
[
  {
    "sampler": "euler",
    "scheduler": "normal",
    "steps": 28,
    "cfg": 7.0,
    "model": "anime_model.safetensors",
    "clip_skip": -2
  }
]
```
- `clip_skip: 0` (default) — Use last layer (best for realistic models)
- `clip_skip: -2` — Skip 2 layers (best for anime/illustration models)

Test multiple values: `"clip_skip": [0, -1, -2, -3]`

### LoRA Trigger Word Filtering
```json
[
  {
    "sampler": "euler",
    "steps": 28,
    "cfg": 7.0,
    "lora": "style2.safetensors:0.8:0.6",
    "lora_omit_triggers": ["style", "makeup", "jewelry"]
  }
]
```
Filters apply to ALL LoRAs in the stack.

### Model Folder Expansion
```json
[
  {
    "model": ["SD1.5/", "SDXL/", "Flux/"],
    "sampler": "euler",
    "steps": 28
  }
]
```
Tests all models from all three folders with the same settings.

### LoRA Strength Sweep

Find the optimal strength for a new LoRA using the Config Builder: add the LoRA once, set the base strength to 0.4, then press **＋** five times and set the new rows to 0.6, 0.8, 1.0, 1.2 and 1.5 (6 strengths in total, 8 at most). Keep everything else minimal (1 sampler, 1 scheduler) and compare the 6 images side by side. With the lock off each row also has its own CLIP value, so you can sweep model and CLIP together as pairs. In the Dashboard the label overlay shows each image's strength (for example `detail:0.60:0.60`) even with "unique only" on, because the strength differs between cards.

### Quality Enhancement Stack

Create a consistent quality stack using the Config Builder: add 3 LoRAs manually (e.g., detail_enhancer at 1.0, color_boost at 0.6, sharpness at 0.5), use the trigger word modal to set all placements to **Positive End**, exclude generic tags like "masterpiece" and "best quality", then save as a reusable preset.

---

## 📋 Preset Configs

### 🏆 Group 1: The "Gold Standards" (Reliable Realism)

*Tests the 5 most reliable industry-standard combinations.*  
5 samplers × 2 schedulers × 2 step settings × 2 cfgs = **40 images**

```json
[
  {
    "sampler": ["dpmpp_2m", "dpmpp_2m_sde", "euler", "uni_pc", "heun"],
    "scheduler": ["karras", "normal"],
    "steps": [25, 30],
    "cfg": [6.0, 7.0],
    "lora": "None"
  }
]
```

### 🎨 Group 2: Artistic & Painterly

*Tests creative/soft combinations best for illustration and anime.*  
2 samplers × 3 schedulers × 3 step settings × 2 cfgs = **36 images**

```json
[
  {
    "sampler": ["euler", "dpmpp_2m"],
    "scheduler": ["simple", "beta", "normal"],
    "steps": [20, 25, 30],
    "cfg": [1.0, 4.5],
    "lora": "None"
  }
]
```

### ⚡ Group 3: Speed / Turbo / LCM

*Tests ultra-fast configs. (Note: Ensure you are using a Turbo/LCM capable model or LoRA).*  
4 samplers × 3 schedulers × 4 step settings × 2 cfgs = **96 images**

```json
[
  {
    "sampler": ["lcm", "euler", "dpmpp_sde", "euler_ancestral"],
    "scheduler": ["simple", "sgm_uniform", "karras"],
    "steps": [4, 5, 6, 8],
    "cfg": [1.0, 1.5],
    "lora": "None"
  }
]
```

### 🦾 Group 4: Flux & SD3 Specials

*Tests configs specifically tuned for newer Rectified Flow models like Flux and SD3.*  
2 samplers × 3 schedulers × 3 step settings × 2 cfgs = **36 images**

```json
[
  {
    "sampler": ["euler", "dpmpp_2m"],
    "scheduler": ["simple", "beta", "normal"],
    "steps": [20, 25, 30],
    "cfg": [1.0, 4.5],
    "lora": "None"
  }
]
```

### 🧪 Group 5: Experimental & Unique

*Tests niche combinations for discovering unique textures.*  
6 samplers × 4 schedulers × 5 step settings × 4 cfgs = **480 images**

```json
[
  {
    "sampler": ["dpmpp_3m_sde", "ddim", "ipndm", "heunpp2", "dpm_2_ancestral", "euler"],
    "scheduler": ["exponential", "normal", "karras", "beta"],
    "steps": [25, 30, 35, 40, 50],
    "cfg": [4.5, 6.0, 7.0, 8.0],
    "lora": "None"
  }
]
```

---

## 🔧 Performance Tips

### For Large Batches (1000+ images)
1. Set `flush_batch_every: 10-20` to see progress updates without overwhelming the browser.
2. Use `vae_batch_size: 8-12` (balance between speed and VRAM).
3. Enable `overwrite_existing: False` so you can stop/resume safely.

### For Multi-Model Testing
1. Use identical LoRA/prompt settings across models for fair comparison.
2. Use `add_random_seeds_to_gens: 2-3` to evaluate model consistency.

### For MOSS-Image / Krea 2 / Qwen-Image grids with many prompts
1. `te_batch_size` (Run Settings > Text Encoder Batch Size) is NOT a free win: on MOSS-Image a batch of 8 measured 1.5x slower and not image-identical (see Performance Settings). Try it only on an encoder you have measured; lower it if you see an OOM retry message.

### For Memory-Constrained Systems
1. Lower `vae_batch_size` to 1-2.

---

## 💡 Tips & Best Practices

### Organization
- Use descriptive config names: `"