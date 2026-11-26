# ComfyUI-ReaVideoBreakdown

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![ComfyUI](https://img.shields.io/badge/ComfyUI-custom%20node-orange)](https://github.com/comfyanonymous/ComfyUI)
[![Tests](https://github.com/benjiyaya/ComfyUI-ReaVideoBreakdown/actions/workflows/test.yml/badge.svg)](https://github.com/benjiyaya/ComfyUI-ReaVideoBreakdown/actions/workflows/test.yml)

**Shot-by-shot video reverse engineering** (the [rea-video](https://github.com/JuneYaooo/rea-video) idea) as two ComfyUI nodes:

1. **Video Breakdown (Rea · native VLM)** — point it at any video and it splits the footage into shots, then for **every shot** tells you:
   - **how it was made** — live action / AI video / 3D render / code motion-graphics / screen capture / still pan / 2D animation / …
   - **what is in it** — subject, setting, lighting, colour, style
   - **the camera work** — *measured* with optical flow (pan px/s, zoom %/s, handheld vs smooth), not guessed
   - **a ready-to-use text-to-video prompt** — one per shot, delimited and wired straight into your favourite video model
2. **VideoPrompt Mod With References** — feeds Node 1's `breakdown_json` + reference images + a plain-English instruction ("use image_1 as the woman, replace character-1, make her speak") through the same native VLM, and rewrites the whole video as one **MiniMax H3 Ref2VA** prompt with `<Subject N>` / `<Picture N>` labels — ready for the native `MiniMaxH3ReferenceToVideo` node.

🎬 **Video tutorial** — making videos with MiniMax H3 + the ReaVideo nodes: [youtu.be/oYRpAddkki8](https://youtu.be/oYRpAddkki8)

All reports are in the open [VIDEO.md](https://github.com/JuneYaooo/rea-video) style (`video_md`), plus structured JSON, plus plain delimited prompts.

## Gallery

Real runs (Qwen3.5 9B VLM text encoder via `CLIPLoader`):

| Night drift (2 shots · live action 100%) | Ruined cathedral (3 shots · 3D 36% + live 26% + AI 38%) | Café / park (5 shots · live action 100%) |
|---|---|---|
| ![Night drift breakdown](assets/example-1.png) | ![Cathedral breakdown](assets/example-2.png) | ![Café breakdown](assets/example-3.png) |

Each panel: workflow → `video_md` report → `breakdown_json` → `prompts` → `summary` → keyframe preview.

## How it sees — your native VLM, nothing else

You load a **vision-language text encoder** with the core **CLIPLoader**
(`qwen_image`, `joyimage`, `ovis`, `gemma`/`ltxv`, `qwen3vl`, `minimax`, …). That CLIP **is** the
vision model. This node reads each shot through the **same path as ComfyUI's core
"Generate Text" node** (`comfy_extras/nodes_textgen.py`):

```python
tokens = clip.tokenize(prompt, videos=[shot_frames], system_prompt=...)
ids    = clip.generate(tokens, max_length=..., temperature=...)
text   = clip.decode(ids)
```

- Frames are passed as a **video batch**, so the model sees motion, not just stills.
  (If your encoder doesn't support `videos=`, the node falls back to per-frame `images=` automatically.)

The node only adds what ComfyUI doesn't do natively:

```
video frames ──▶ shot detection (OpenCV, CPU) ──▶ per shot: sample N frames ──▶ native VLM ──▶ JSON record ──▶ VIDEO.md + prompts
                        │                                  │                      (tokenize →
                        └─ cut / fade / dissolve / flash   └─ measured camera     generate → decode)
                           boundary detection                 motion (optical flow
                                                              + RANSAC similarity fit)
```

Shot detection uses HSV-histogram distance + pixel diff with adaptive thresholds; camera motion is
Lucas–Kanade optical flow + RANSAC similarity fit on consecutive pairs → `static` / `smooth_move` /
`handheld`, pan (px/s) and zoom (%/s).

## Install

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/benjiyaya/ComfyUI-ReaVideoBreakdown.git
cd ComfyUI-ReaVideoBreakdown
pip install -r requirements.txt   # just numpy + opencv-python-headless; torch comes with ComfyUI
```

Restart ComfyUI. Also available through **ComfyUI Manager** once registered on the
[Comfy Registry](https://registry.comfy.org).

The node itself has **zero extra dependencies** beyond what ComfyUI already ships. The bundled
[example workflow](example_workflows/rea_breakdown.json) additionally uses two popular display packs
(optional, only for nicer text previews): [pysssss Custom-Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts)
(`Show Text`) and [comfyui-easy-use](https://github.com/yolain/ComfyUI-Easy-Use) (`Show Any`).

## Use — Node 1: Video Breakdown

**`Video Breakdown (Rea · native VLM)`** (category `RE-VIDEO/breakdown`).

```
LoadVideo ─▶ GetVideoComponents ─ images ─▶ ┐
                              └ frame_rate ─▶ fps
CLIPLoader (type = qwen_image / joyimage / …, a VLM) ─ clip ─▶ ┘
                                                 Video Breakdown (Rea · native VLM)
```

### Inputs

| Input | Default | Meaning |
|---|---|---|
| `images` | — | every frame as an IMAGE batch (`LoadVideo → GetVideoComponents`, VHS, etc.) |
| `fps` | `25.0` | batch frame rate (`0` = assume 25) |
| `clip` | — | **a VLM text encoder** (CLIPLoader). Not a plain SD1.5 CLIP. |
| `sensitivity` | `0.5` | cut-detector sensitivity — higher finds more shots |
| `min_shot_seconds` | `0.24` | shots shorter than this get merged into their neighbour |
| `frames_per_shot` | `8` | frames sampled per shot and shown to the VLM as a video batch (1–32) |
| `max_length` | `1024` | VLM max generated tokens per shot |
| `temperature` | `0.4` | VLM sampling — lower = more reliable JSON |
| `seed` | `0` | VLM seed |
| `language` | `en` | `en` / `zh` report + prompts |
| `max_side` | `512` | downscale frames to this max side before the VLM (bounds VRAM) |

### Outputs

| Output | Type | Meaning |
|---|---|---|
| `video_md` | STRING | full VIDEO.md-style report (front-matter, timeline, per-shot details + prompts) |
| `breakdown_json` | STRING | the same breakdown as structured JSON (shot boundaries, composition %, records) |
| `prompts` | STRING | one ready-to-use video prompt per shot, delimited `[Shot NN \| time \| made_of]` |
| `summary` | STRING | one-line verdict, e.g. `3 shots, 11.6s @ 24.00fps: 3D render 36%, live action 26%…` |
| `keyframes` | IMAGE | first frame of each shot, for a `Preview Image` node |
| `shot_count` | INT | number of detected shots |

Wire `prompts` (or parse `breakdown_json`) straight into your text-to-video node.

### Example output

`video_md` (abridged — from the night-drift run above):

```markdown
---
format: videomd-like
subformat: rea-video-comfyui-vlm
reader: native ComfyUI VLM text encoder (clip.tokenize -> generate -> decode); no clip_vision
duration: 14.00
fps: 24.000
size: 1280x704
shots: 2
---

## Verdict
2 shots · live action 100%

## Timeline
| # | time | in | made | camera (measured) | description |
|---|------|----|------|-------------------|-------------|
| 00 | 00:00.00-00:07.06 | cut | live action | smooth camera move | A white sports car drifts through a rain-slicked neon-lit city street at night… |
| 01 | 00:07.06-00:14.00 | cut | live action | handheld camera | The white sports car accelerates sharply, motion blur streaking the neon lights… |

## Shot details & remake prompts
### #00 00:00.00-00:07.06 · live action
A white sports car drifts through a rain-slicked neon-lit city street at night, camera
smoothly following the car until it accelerates away…
- shot size: wide · camera: smooth pan right following the car · lighting: neon signage + wet pavement reflections
- measured camera~: smooth camera move (pan 189px/s, zoom -0.4%/s)
- **video prompt:** A white sports car drifts through a rain-slicked neon-lit city street at night…
```

`prompts`:

```
[Shot 00 | 00:00.00-00:07.06 | 7.06s | live_action]
A white sports car drifts through a rain-slicked neon-lit city street at night, camera smoothly following…

[Shot 01 | 00:07.06-00:14.00 | 6.94s | live_action]
The white sports car accelerates sharply, capturing motion blur as it speeds past the camera…
```

`~` marks tool-measured values (OpenCV); everything else comes from the VLM actually seeing the frames.

## Use — Node 2: VideoPrompt Mod With References

**`VideoPrompt Mod With References`** (category `RE-VIDEO/breakdown`) — a ComfyUI **V3** node with dynamic reference inputs, so it needs a recent ComfyUI (the version that ships the native MiniMax H3 nodes).

Take Node 1's `breakdown_json`, up to **9 reference images**, and a plain-English instruction, and rewrite the entire source video as one official **MiniMax H3 full-reference (Ref2VA)** prompt:

```
ReaVideoBreakdown ─ breakdown_json ─▶ ┐
LoadImage ×N ───── image_1..image_9 ─▶ VideoPrompt Mod With References ─ prompt ─▶ MiniMaxH3ReferenceToVideo
user_instruction ────────────────────▶   (native VLM CLIP)           ─ prompt_json / label_map
```

The VLM emits the six H3 sections — `subject_definitions`, `summary`, `retention_analysis`, `detailed_description`, `overall_soundscape`, `non_diegetic_music` — with `<Subject N>` / `<Picture N>` labels, shot order/cuts/camera preserved from the breakdown, dialogue as `<d>[Language] …</d>` with stable `(Sx)` speaker IDs, and the timeline fitted to `target_seconds`.

### Inputs

| Input | Default | Meaning |
|---|---|---|
| `clip` | — | the same VLM text encoder as Node 1 |
| `breakdown_json` | — | Node 1's `breakdown_json` output |
| `user_instruction` | `""` | plain-English edit request, e.g. *"use image_1 as the woman, replace character-1, make her speak"* |
| `ref_images` | none | dynamic `image_1`…`image_9` (Autogrow); `image_N` = `<Picture N>` |
| `target_seconds` | `0` | total duration the rewrite must fit (`0` = source duration) |
| `max_length` / `temperature` / `seed` | `2048` / `0.4` / `0` | VLM generation controls |
| `max_side` | `768` | reference-image downscale cap |

### Outputs

| Output | Meaning |
|---|---|
| `prompt` | the six-section Ref2VA prompt — wire into `MiniMaxH3ReferenceToVideo.prompt` |
| `prompt_json` | sections + label map + target duration as JSON (for scripting/debugging) |
| `label_map` | human-readable `image_N → <Picture N>` wiring reminder |

**Wiring contract:** the image you feed `image_N` here must be the *same image, same slot* you feed `ref_image_N` on the native H3 node — that's what makes `<Picture N>` line up. Audio is wired **directly into the native node** (`ref_audio_*`), never through this one; v1 deliberately does not emit `<Audio N>` tags, because the native node's audio latent conditions the model regardless of prompt tags.

## Tips

- **Use a VLM, not a CLIP.** A plain SD1.5/SDXL CLIP can't see images. The node detects this and
  warns you in every output instead of crashing the graph.
- **Stable JSON:** keep `temperature` ≤ 0.5. Higher values make livelier prose but looser structure.
- **Long videos:** raise `sensitivity` for fast cutting (ads, trailers); lower it for single-take footage.
- **VRAM:** `max_side 512` + `frames_per_shot 8` is cheap. Raise `max_side` to 768/1024 for detail-heavy shots.
- **Chinese output:** set `language: zh` — report, labels and prompts all switch.
- **Remake loop:** feed each `[Shot NN]` block of `prompts` to Wan / Kling / Veo / Sora-style nodes,
  reassemble with your edit nodes — the time codes in the delimiters give you the cut order.
- **Node 2:** keep `image_N` here and `ref_image_N` on the native H3 node as the same image, same order — that's what `<Picture N>` refers to.
- **Node 2:** set `target_seconds` when shortening a longer source; the VLM re-times the `[Shot N] At MM:SS.mmm` stamps to fit.

## Test (no GPU / torch needed)

```bash
python tests/test_offline.py
```

Mocks the VLM `tokenize/generate/decode` contract, builds a synthetic 3-shot video, and verifies
shot detection, per-shot records, distinct usable prompts, JSON validity, robust reply parsing, and
example-workflow widget order. Runs on CPU in seconds; CI runs it on every push. (Covers Node 1; Node 2 needs a real ComfyUI with `comfy_api`.)

## Honest limits

- Description/prompt quality = your VLM's quality. It describes what it sees; it does not invent.
- Visual production only — no audio/BPM analysis, OCR, or subtitle export. Node 2 deliberately does not manage reference audio in v1 (see the wiring contract above).
- Shot detection is content-agnostic but conservative on extreme slow dissolves; tune `sensitivity`.

## Credits & license

- Method concept: [rea-video](https://github.com/JuneYaooo/rea-video) by [JuneYaooo](https://github.com/JuneYaooo) (Apache-2.0) — the open VIDEO.md breakdown format and the `made_of` label set.
- Built on ComfyUI's native VLM text-encoder path (`comfy_extras/nodes_textgen.py`).
- H3 Ref2VA prompt format: the official [MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) `skills/h3-prompt-writing` reference.

MIT — see [LICENSE](LICENSE).
