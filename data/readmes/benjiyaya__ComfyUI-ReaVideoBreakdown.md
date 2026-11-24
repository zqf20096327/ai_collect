# ComfyUI-ReaVideoBreakdown

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![ComfyUI](https://img.shields.io/badge/ComfyUI-custom%20node-orange)](https://github.com/comfyanonymous/ComfyUI)
[![Tests](https://github.com/benjiyaya/ComfyUI-ReaVideoBreakdown/actions/workflows/test.yml/badge.svg)](https://github.com/benjiyaya/ComfyUI-ReaVideoBreakdown/actions/workflows/test.yml)

**Shot-by-shot video reverse engineering** (the [rea-video](https://github.com/JuneYaooo/rea-video) idea) as a single ComfyUI custom node.

Point it at any video and it splits the footage into shots, then for **every shot** tells you:

- **how it was made** — live action / AI video / 3D render / code motion-graphics / screen capture / still pan / 2D animation / …
- **what is in it** — subject, setting, lighting, colour, style
- **the camera work** — *measured* with optical flow (pan px/s, zoom %/s, handheld vs smooth), not guessed
- **a ready-to-use text-to-video prompt** — one per shot, delimited and wired straight into your favourite video model

- Using Minimax H3 + REA VIdeo node to create some videos : https://youtu.be/oYRpAddkki8

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

## Use

One node: **`Video Breakdown (Rea · native VLM)`** (category `RE-VIDEO/breakdown`).

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

## Tips

- **Use a VLM, not a CLIP.** A plain SD1.5/SDXL CLIP can't see images. The node detects this and
  warns you in every output instead of crashing the graph.
- **Stable JSON:** keep `temperature` ≤ 0.5. Higher values make livelier prose but looser structure.
- **Long videos:** raise `sensitivity` for fast cutting (ads, trailers); lower it for single-take footage.
- **VRAM:** `max_side 512` + `frames_per_shot 8` is cheap. Raise `max_side` to 768/1024 for detail-heavy shots.
- **Chinese output:** set `language: zh` — report, labels and prompts all switch.
- **Remake loop:** feed each `[Shot NN]` block of `prompts` to Wan / Kling / Veo / Sora-style nodes,
  reassemble with your edit nodes — the time codes in the delimiters give you the cut order.

## Test (no GPU / torch needed)

```bash
python tests/test_offline.py
```

Mocks the VLM `tokenize/generate/decode` contract, builds a synthetic 3-shot video, and verifies
shot detection, per-shot records, distinct usable prompts, JSON validity, robust reply parsing, and
example-workflow widget order. Runs on CPU in seconds; CI runs it on every push.

## Honest limits

- Description/prompt quality = your VLM's quality. It describes what it sees; it does not invent.
- Visual production only — no audio/BPM analysis, OCR, or subtitle export (out of scope for one node).
- Shot detection is content-agnostic but conservative on extreme slow dissolves; tune `sensitivity`.

## Credits & license

- Method concept: [rea-video](https://github.com/JuneYaooo/rea-video) by [JuneYaooo](https://github.com/JuneYaooo) (Apache-2.0) — the open VIDEO.md breakdown format and the `made_of` label set.
- Built on ComfyUI's native VLM text-encoder path (`comfy_extras/nodes_textgen.py`).

MIT — see [LICENSE](LICENSE).
