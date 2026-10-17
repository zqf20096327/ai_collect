# hentai-pipeline

An autonomous NSFW anime image pipeline: pull a random adult image → caption it
with a local vision LLM → feed the danbooru-style tags into ComfyUI → save the
result. Runs as a one-shot CLI or a Gradio control panel with an always-on loop.

> **⚠️ Adult content (18+).** This project generates explicit imagery. By using
> it you confirm you are of legal age in your jurisdiction and accept full
> responsibility for what you generate and where you publish it. Intended for
> private, consensual, legal use only.

## How it works

Each iteration ("tick") runs four steps:

1. **Fetch** a random image from a source (imagefap, rule34, yande.re,
   konachan, xbooru, e621, danbooru, …).
2. **Tag** it with a vision LLM served over an OpenAI-compatible
   `/v1/chat/completions` endpoint (LM Studio, vLLM, llama.cpp server, …).
3. **Generate** a new image in ComfyUI from the configured prefix plus either
   danbooru-style tags or a natural-language vision prompt.
4. **Save** the source image and the result, and append a line to `runs.jsonl`.

## Features

- One-shot CLI (`pipeline.py`) and a Gradio control panel (`app.py`).
- Autonomous loop with start/pause and a configurable interval.
- **Source presets** and per-source auth (`login` / `api_key` / `user_id`).
- **UNET models** (Anima, Krea2, Flux, …) with separate CLIP/VAE, **or
  bundled checkpoints** (waiNSFWIllustrious, …) where CLIP/VAE are baked in.
- Up to 6 **LORAs**, each with its own strength.
- User-saveable **model** and **source** presets (`presets.json`).
- Danbooru (Cloudflare-protected) via Playwright + Chromium.

## Requirements

- Python 3.10+
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) running (default
  `http://localhost:8188`)
- A vision LLM behind an OpenAI-compatible endpoint (e.g.
  [LM Studio](https://lmstudio.ai/) on `http://127.0.0.1:1234`)
- (Danbooru source only) Playwright + Chromium

## Install

```bash
git clone <your-repo-url>
cd hentai-pipeline
python -m venv .venv
# activate it (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
python -m playwright install chromium   # only needed for the danbooru source
```

Copy the example configs and fill in your own values:

```bash
cp config.example.json config.json
cp presets.example.json presets.json
```

## Configuration

`config.json` is the main settings file (see `config.example.json`):

| Section | Meaning |
|---|---|
| `comfy` | ComfyUI host, model type, UNET/checkpoint name, CLIP/VAE, size, steps, CFG, sampler, scheduler, LORAs |
| `tagger` | vision-LLM host, model, prompt mode (tags or natural), temperature, max tags, and system prompts |
| `prompt_prefix` / `negative_prompt` | the prompt wrapper |
| `source` | source type, URL, and optional `auth_params` |
| `output_dir` / `log_file` | where results and logs go |

`presets.json` stores your saved model and source presets. See
`presets.example.json`.

> **Never commit `config.json` or `presets.json`** — they hold API keys and
> local paths. Both are in `.gitignore`.

### Model types

- `model_type: "unet"` — loads a diffusion model with an explicit
  `unet_name` + `clip_name`/`clip_type` + `vae_name` (e.g. Anima, Krea2).
- `model_type: "checkpoint"` — loads a single `checkpoint_name` via
  `CheckpointLoaderSimple`; CLIP and VAE are baked in, so those fields are
  ignored.

### Sources

`source.type` picks the fetcher:

| Type | Sites | Auth |
|---|---|---|
| `imagefap` | imagefap random page | none |
| `booru` | yande.re, konachan, xbooru, safebooru, e621, e926, rule34 | none, or `auth_params` |
| `danbooru` | danbooru (Cloudflare → browser) | `login` + `api_key` |
| `generic` | any page that lists `<img src>` thumbnails | none |

`auth_params` is optional and supports `login`, `api_key`, `user_id` — they
are appended as query parameters. Example (rule34):

```json
"source": {
  "type": "booru",
  "random_url": "https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&json=1&limit=1&tags=sort:random",
  "auth_params": { "user_id": "1234", "api_key": "YOUR_KEY" }
}
```

## Usage

### CLI — generate one image

```bash
python pipeline.py
```

### GUI — control panel + loop

```bash
python app.py
# open http://127.0.0.1:7860
```

The GUI tabs:

- **Run** — start/pause the loop, generate one now, latest image + prompt, gallery.
- **Model** — model type (UNET vs checkpoint), CLIP/VAE/weight-dtype, per-LORA strength, model presets.
- **Sampler & Size** — width/height/steps/CFG/sampler/scheduler.
- **Tagger** — choose danbooru **tags** or a **natural** prompt, configure the vision-LLM host/model/temperature, and edit the system prompt for either mode.
- **Source & Prompt** — source preset, parser type, URL, auth, prompt prefix, negative prompt.

Changes are saved with **Save & apply** and take effect on the next tick.

## Project layout

```
app.py               Gradio control panel (loop, presets, gallery)
pipeline.py          single-iteration engine (fetch → tag → generate → save)
config.json          your settings (gitignored)
presets.json         your saved presets (gitignored)
config.example.json  template for config.json
presets.example.json template for presets.json
```

## Troubleshooting

- **ComfyUI 400 "value not in list"** — a model name in `config.json` doesn't
  exist on disk; use the GUI's "Refresh lists" or check the exact filename.
- **Tagger HTTP 415** — the endpoint isn't OpenAI-compatible; point
  `tagger.host` at a `/v1/chat/completions` endpoint.
- **Danbooru "Performing security verification"** — Cloudflare. Danbooru
  needs the headed Chromium (Playwright); headless and plain HTTP won't pass.
- **No images / silent failures** — check `pipeline.log` and `runs.jsonl`.

## Disclaimer

This tool is for personal, legal, adult use only. Respect the terms of service
of any site you source from, and the laws of your jurisdiction. You are
responsible for the content you generate and publish.
