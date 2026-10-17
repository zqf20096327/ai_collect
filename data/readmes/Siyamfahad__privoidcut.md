<div align="center">

# PrivoidCut

**The private, offline AI video editor. Talking head in, motion-graphics short out.**

by [**Privoid.ai**](https://privoid.ai) · right-sized AI, owned by you

Drop in a video → PrivoidCut cuts the dead air, transcribes every word, picks an animated graphic for each line, frames your face around it, adds word-synced captions, checks its own layout and renders a 1080×1920 MP4.<br>
No cloud. No API keys. No subscription. Everything runs on your computer.

[Demo](#demo) · [Install](#install) · [The app](#the-app) · [Command line](#command-line) · [Local AI](#local-ai-models) · [How it works](#how-it-works) · [Templates](docs/TEMPLATES.md) · [Contributing](CONTRIBUTING.md)

</div>

## Demo

<div align="center">

| Original &nbsp;→&nbsp; Edited by PrivoidCut |
|:---:|
| <img src="docs/demo/demo.webp" width="660" alt="Before and after: the original video on the left, PrivoidCut's edit with headline, framed speaker, 90% stat card and captions on the right"> |

**Watch with sound:** [original clip](docs/demo/before.mp4) · [edited clip](docs/demo/after.mp4)

</div>

Everything on the right was made automatically from the original on the left (which already had simple burned-in captions; PrivoidCut reframes the speaker so they stay out of the way): the headline hook, the speaker moving between full screen and a framed card, the animated **90%** stat, highlighted keywords, the "zero control" sticker and the word-by-word captions. Planning ran on a local `gpt-oss-20b` in LM Studio; the 30 s clip rendered in under 2 minutes on an RTX 3060.

### The editor

<img src="docs/ui-editor.png" alt="The PrivoidCut app: phone preview of the video on the left, settings cards for clip, look, captions, editing style, local AI and transcription on the right" width="100%">

### 50 templates, 4 themes

<img src="docs/templates.jpg" alt="All 50 templates" width="100%">

<img src="docs/themes.jpg" alt="The same graphics in the paper, midnight, bold and sunset themes" width="100%">

## Features

- **Automatic jump cuts:** pauses longer than 0.7 s (adjustable) are cut out before editing.
- **50 motion-graphics templates:** kinetic type, lists, charts, comparisons, real-screenshot callouts, hand-drawn notes and more ([full list](docs/TEMPLATES.md)), plus plain "talking" beats so the edit can breathe.
- **Face-aware speaker layouts:** the speaker moves smoothly between full screen, split, card, a picture-in-picture bubble and graphic-only, always cropped around the face.
- **Word-synced captions** with the current word highlighted. Graphics land on the exact word they illustrate.
- **Local AI planning:** a local LLM chooses a template per line and writes the copy, schema-constrained and validated. No model? A rule-based planner still makes a complete edit.
- **Real evidence:** drop in screenshots or give URLs. A local vision model reads them so they appear when you mention them.
- **Self-checking:** before rendering, every frame is measured for text over your face, overflowing text, overlaps, empty screens and text that flashes by too fast. Problems are fixed automatically.
- **Fully editable:** every decision is saved. In the app, swap templates, layouts and text per line and re-render without re-planning.
- **Customisable:** theme, brand colour, caption style, graphics density, allowed layouts and templates, AI creativity, resolution.
- **Windows, macOS and Linux**, plus Docker. Optional NVIDIA GPU acceleration.

## Install

You need **Python 3.10+** and **ffmpeg**; the installers check for both and offer to install what's missing.

### Windows: one command

```powershell
git clone https://github.com/Siyamfahad/privoidcut
cd privoidcut
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

The script:
1. finds Python, or offers to install it with `winget`;
2. installs ffmpeg with `winget` if it's missing;
3. creates a `.venv`;
4. if it sees an NVIDIA GPU, asks whether to add GPU support;
5. installs headless Chromium;
6. runs `privoidcut doctor`.

Then **double-click `privoidcut-ui.bat`** to open the app.

Flags: `-Gpu` (force GPU support), `-NoGpu`, `-Yes` (don't ask questions).

### macOS / Linux: one command

```bash
git clone https://github.com/Siyamfahad/privoidcut && cd privoidcut
./install.sh            # add --gpu on Linux with an NVIDIA card, --yes for no questions
.venv/bin/privoidcut ui
```

### Manual install

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
pip install -e .                 # or: pip install -e ".[gpu]" for NVIDIA GPUs
python -m playwright install chromium
privoidcut doctor
```

| OS | ffmpeg |
|---|---|
| Windows | `winget install Gyan.FFmpeg` |
| macOS | `brew install ffmpeg` |
| Debian / Ubuntu | `sudo apt install ffmpeg` |

### GPU acceleration (NVIDIA, optional)

Transcription runs on the CPU by default. With an NVIDIA GPU, install the CUDA libraries as Python wheels (about 1.5 GB, no CUDA toolkit needed):

```bash
pip install -e ".[gpu]"
privoidcut doctor        # should show: OK  GPU transcription (ready)
```

With `--whisper auto` (the default), PrivoidCut uses the more accurate **medium** speech model on a working GPU and **small** on the CPU. Measured on an RTX 3060 for 30 s of speech, model loading included:

| Speech model | NVIDIA GPU | CPU (Ryzen 7 7700) |
|---|---|---|
| small | 2.4 s | 4.7 s |
| medium | 4.4 s | 12.4 s |

macOS uses the CPU; Apple-Silicon Macs are fast enough with `small`.

### Docker

```bash
docker build -t privoidcut .

# the app (open the ...?token=... link printed in the logs)
docker run --rm -p 127.0.0.1:7860:7860 -v privoidcut-data:/data \
  -e PRIVOIDCUT_LLM_URL=http://host.docker.internal:1234/v1 privoidcut

# the command line, on videos in the current folder
docker run --rm -v "$PWD:/work" -w /work privoidcut edit my_video.mp4 --no-llm
```

The image is CPU-only (about 4 GB with Chromium, ffmpeg and the speech model). Point `PRIVOIDCUT_LLM_URL` at the model server on your host (LM Studio `:1234/v1`, Ollama `:11434`).

## The app

```bash
privoidcut ui            # or double-click privoidcut-ui.bat on Windows
```

Opens **http://127.0.0.1:7860** in your browser. Projects are stored in `~/privoidcut`.

1. **Drop a video** on the page, or paste a file path (nothing is copied).
2. **Settings:** every option, grouped into cards:

| Card | Options |
|---|---|
| Clip & pacing | whole video or a start/length range · dead-air removal · pause threshold |
| Look | theme (paper, midnight, bold, sunset) · accent colour · output 540p / 720p / 1080p |
| Captions | on/off · words per line · size · UPPERCASE · highlight colour |
| Editing style | graphics density (calm / balanced / busy) · which speaker layouts to use · which templates to use |
| Local AI | planner model · vision model · creativity |
| Transcription | speech model (auto, tiny … large-v3) · CPU / NVIDIA GPU · names & jargon hint |
| Evidence | drag in screenshots/photos · web pages to capture |

3. **Create video.** Watch live progress per stage (transcribe → cut silence → frames & face → evidence → plan → checks → render), cancel any time, and follow the log.
4. **Edit beats.** Every line of speech becomes a card with its thumbnail, transcript, template, layout and on-screen text. Swap the template from a visual picker, change the layout, rewrite any text (with character limits shown), then click **Re-render with my edits**. Nothing is re-planned.
5. **Templates.** Browse all 50 with previews in each theme; switch off any you never want the planner to use.
6. Compare **original vs edited**, download the MP4, open the storyboard, or open the project folder.

## Command line

```bash
privoidcut edit video.mp4                                   # full edit with defaults
privoidcut edit video.mp4 --duration 25 --resolution 540    # quick 25 s preview
privoidcut edit video.mp4 --theme midnight --accent "#00c2ff" --density busy
privoidcut edit video.mp4 --evidence ./screenshots --url https://example.com/article
privoidcut edit video.mp4 --hint "ChatGPT, OpenAI, Notion"  # help with names and jargon
privoidcut edit video.mp4 --no-llm                          # no AI at all
privoidcut edit video.mp4 --plan video_privoidcut_work/plan.json   # re-render a hand-edited plan
```

<details>
<summary><b>All <code>privoidcut edit</code> options</b></summary>

| Option | Default | Meaning |
|---|---|---|
| `-o, --out` | `<video>_privoidcut.mp4` | output file |
| `--start`, `--duration` | whole video | the part to edit, in seconds |
| `--keep-silence` | off | keep long pauses instead of cutting them |
| `--silence-gap` | `0.7` | cut pauses longer than this (seconds) |
| `--theme` | `paper` | `paper`, `midnight`, `bold`, `sunset` |
| `--accent` | theme's | accent colour, e.g. `#ff3366` |
| `--resolution` | `1080` | output width: `540`, `720`, `1080` (always 9:16) |
| `--preview` | off | shorthand for `--resolution 540` |
| `--density` | `balanced` | `calm`, `balanced`, `busy`: how many lines get a graphic |
| `--layouts` | all | speaker layouts to allow: `full,top,frame,pip,hidden` |
| `--exclude` | none | template ids never to use (see `privoidcut templates`) |
| `--no-captions` | off | no captions |
| `--caption-words` | `3` | max words per caption line |
| `--caption-size` | `76` | caption size in px at 1080 wide |
| `--caption-color` | theme's | colour of the word being spoken |
| `--no-uppercase` | off | captions in normal case |
| `--model` | `auto` | planner model on your local server |
| `--vlm` | `auto` | vision model for evidence images |
| `--temperature` | `0.4` | planner creativity, 0.1-1.0 |
| `--no-llm` | off | plan with rules only |
| `--evidence` | none | folder of images to show |
| `--url` | none | web page to capture as evidence (repeatable) |
| `--whisper` | `auto` | speech model: `auto`, `tiny`, `base`, `small`, `medium`, `large-v3` |
| `--device` | `auto` | `auto`, `cpu`, `cuda` |
| `--hint` | none | names/jargon said in the video |
| `--plan` | none | render from an existing `plan.json` |
| `--work` | next to output | working folder (caches transcripts and frames) |

</details>

Other commands:

| Command | What it does |
|---|---|
| `privoidcut ui` | the app (`--port`, `--projects DIR`, `--no-browser`, `--host`; see [Security](#security)) |
| `privoidcut templates` | list all templates |
| `privoidcut gallery --out gallery [--theme sunset] [--only bar_chart,versus]` | render templates to contact sheets |
| `privoidcut doctor` | check ffmpeg, Chromium, speech model, GPU, face detector, model server and models |

Each edit writes, next to your video: the MP4, a `_storyboard.jpg` (one frame per line), a `_report.json` (every beat's template and layout, and any warnings), and a `_work/` folder whose `plan.json` you can edit and re-render with `--plan`.

## Local AI models

PrivoidCut finds a local model server automatically and never uses a cloud API:

| Server | How |
|---|---|
| [LM Studio](https://lmstudio.ai) | download models in the app, then start the server (`lms server start`, port 1234) |
| [Ollama](https://ollama.com) | `ollama pull qwen3:8b` and `ollama pull qwen3-vl:8b` (port 11434) |
| llama.cpp `llama-server` | any GGUF model on port 8080 |
| anything OpenAI-compatible | `PRIVOIDCUT_LLM_URL=http://host:port/v1` |

With `auto`, PrivoidCut picks the best installed **planner** (Qwen3 › gpt-oss › Mistral Nemo › Gemma 3 › Qwen2.5 …) and **vision model** (Qwen3-VL › Qwen2.5-VL › Gemma 3 …). Only one model is loaded at a time; the vision model is unloaded before planning.

| GPU memory | Planner | Vision |
|---|---|---|
| 8 GB | Qwen3 8B (Q4) | Qwen2.5-VL 7B (Q4) |
| 12 GB | gpt-oss 20B or Qwen3 8B | Qwen2.5-VL 7B / Qwen3-VL 8B |
| 16 GB+ | Qwen3 14B, gpt-oss 20B | Qwen3-VL 8B |
| no GPU | `--no-llm`, or a 3-4B model | none (file names describe images) |

No server? PrivoidCut still works: the rule-based planner turns numbers into stat cards, questions into question cards, contrasts into "not X but Y" and so on.

## How it works

```
video ─► faster-whisper words ─► cut dead air ─► ffmpeg frames ─► face track (YuNet) ─┐
                                  └► beats ─► planner (local LLM / rules) ─► plan ─────┤
         evidence images / URLs ─► vision-model descriptions ──────────────────────────┘
                                                                                        ▼
                      composition (HTML + PrivoidCut motion engine) in headless Chromium
                                                                                        ▼
               QC: seek through the timeline, measure every element ─► auto-fix ─► repeat
                                                                                        ▼
                             frame-by-frame capture ─► ffmpeg (H.264 + original audio)
```

- **Beats.** The transcript is split into 1.3-5.5 s units at sentence ends and pauses. Each beat gets one template and one speaker layout.
- **Planner.** Pass 1: the LLM picks a template id per beat (the JSON schema only allows valid ids). Pass 2: it fills that template's slots, schema-constrained again. Python validates everything (types, lengths, numbers, image names), asks for one rewrite with exact feedback when text is too long, and falls back to rules for anything still invalid. A pacing pass prevents repeats, keeps one-off templates (hook, poster, end card) to one use, and balances graphics against plain talking according to the density setting.
- **Motion engine** (`privoidcut/web/engine.js`). A small deterministic timeline: every value is a pure function of time, so any frame renders identically however you seek to it. It covers springs, easing, clip wipes, stroke drawing, counters and typewriters, with no animation library.
- **QC.** The runtime seeks through the video in the browser and measures real element boxes against the face, the stage, the captions and each other. An issue must persist for half a second to count, so mid-animation frames aren't flagged.

## Performance

Ryzen 7 7700 + RTX 3060 12 GB, 30 s clip:

| Mode | Time |
|---|---|
| rules only, 540p | ~40 s |
| gpt-oss-20b planning, 540p | ~75 s |
| gpt-oss-20b + vision model + web capture, 1080p | ~2 min |

Rendering runs at about 18-22 frames per second at 1080p; most of the rest is the LLM.

## Security

PrivoidCut never uploads your media. The app listens on **127.0.0.1** and only answers requests addressed to localhost; cross-origin `POST`s from other websites are refused. If you start it with `--host 0.0.0.0` to use it from another device, it prints a warning and requires a random **access token** (open the printed `?token=` link once). See [SECURITY.md](SECURITY.md).

## Tips

- **Start with a 20-30 s sample** (`--duration 25 --resolution 540`) to settle on a style, then do the full video at 1080p.
- **Use raw footage.** Videos that already have burned-in captions will show the old captions under the new ones.
- **Vertical 9:16 recordings** give the most layout options. Horizontal footage is cropped around your face; if the face is too large for graphics over a full-screen speaker, PrivoidCut switches to split layouts automatically.
- Speak in clear sentences. Numbers, lists and comparisons give the planner the most to work with.
- Brand names come out wrong? Put them in the **names & jargon** box (`--hint`).

## Limitations

- English only for now (captions, rules and prompts).
- Small local models write decent but not brilliant copy. Check the storyboard and tweak lines in the beat editor.
- No music or sound effects yet.

## Contributing

New templates are the easiest way in: one JavaScript file each ([guide](docs/WRITING_TEMPLATES.md)). See [CONTRIBUTING.md](CONTRIBUTING.md) for setup, tests and the PR checklist, and the [changelog](CHANGELOG.md) for what's new.

```bash
pip install -e ".[dev]" && pytest      # 27 tests: planning, silence cuts, app API & security, every template in every theme
```

## Acknowledgements

- **[SeeCut](https://github.com/YeJe-cpu/SeeCut)** for the original idea of an AI editor that turns talking-head footage into motion-graphics shorts and reviews its own cuts. PrivoidCut is an independent, from-scratch implementation (no code shared) built around the opposite constraint: everything runs offline on local models.
- [faster-whisper](https://github.com/SYSTRAN/faster-whisper) (transcription), [Playwright](https://playwright.dev) (headless rendering), [OpenCV YuNet](https://github.com/opencv/opencv_zoo) (face detection), [FFmpeg](https://ffmpeg.org), and the font authors listed in [NOTICE](NOTICE).
- [LM Studio](https://lmstudio.ai), [Ollama](https://ollama.com) and [llama.cpp](https://github.com/ggml-org/llama.cpp), which make local models practical.

## About Privoid

PrivoidCut is built and maintained by **[Privoid.ai](https://privoid.ai)**, an AI agency that builds **custom, private, local AI systems** for businesses: faster, fully under your control, and a fraction of the frontier-API bill. Assistants, automation and media pipelines run on your own hardware, and no data leaves your premises. PrivoidCut is a small, open example of that approach.

**Want private AI built for your team?** → [privoid.ai](https://privoid.ai)

## License

[MIT](LICENSE) © 2026 Privoid. "Privoid" and "PrivoidCut" are names of Privoid; forks are welcome under a different name. Bundled fonts are under the SIL Open Font License or Apache 2.0; the face detector model is MIT. See [NOTICE](NOTICE).

---

<div align="center">
  <a href="https://privoid.ai">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="docs/privoid-logo-white.png">
      <source media="(prefers-color-scheme: light)" srcset="docs/privoid-logo-dark.png">
      <img src="docs/privoid-logo-dark.png" alt="Privoid.ai" width="260">
    </picture>
  </a>
  <p><b>Right-sized AI. Owned by you.</b><br>
  <sub>Made with care by <a href="https://privoid.ai">Privoid.ai</a> · custom local ML systems: faster, private, a fraction of the frontier-API bill.</sub></p>
</div>
