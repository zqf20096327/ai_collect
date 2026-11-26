<div align="center">

<img src="docs/social-preview.png" alt="CTV - CodeToVideo: the AI is the director, the program is real" width="720">

# CTV · CodeToVideo

**Point it at any web app, write one sentence, get a demo or promo video. The AI directs; a real program records. Free, fully local, no audio.**

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![Status: alpha](https://img.shields.io/badge/status-alpha-orange)
![Node 20+](https://img.shields.io/badge/node-20%2B-339933)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

[Quick start](#quick-start) · [Formats](#formats-backgrounds-quality) · [How it works](#how-it-works) · [Honest status](#honest-status) · [**Help wanted**](#help-wanted) · [Manual](docs/MANUAL.md)

<a href="docs/demo.mp4"><img src="docs/demo.gif" alt="Demo made by CTV with a 4B local model (click to play the full video)" width="640"></a>

<sub>▶ Made end to end by CTV with `qwen3.5:4b` running locally and **no manual editing**; the neon backdrop was drawn by the model itself (`--backdrop generate`). Click the animation to play the [full video](docs/demo.mp4).</sub>

</div>

---

## Why this exists

I was tired of three things:

1. **AI hallucinates when it generates video.** Text-to-video models invent buttons, screens and features that do not exist.
2. **I cannot do video editing,** and I do not want to learn timelines and keyframes just to show my own product.
3. **Tools that turn code into a nice demo are paid.** I did not want another subscription.

So CTV flips the roles: **the AI is only the director; the program is real.**

- Your LLM reads the repo and your prompt and writes a *plan*: scenes, titles, captions, pacing, colors.
- Everything you see on screen is a **real recording of your real app**, driven by [Playwright](https://playwright.dev) through ordinary DOM / ARIA semantics. Nothing on screen can be hallucinated, because it is the real thing.
- [FFmpeg](https://ffmpeg.org) and [Remotion](https://remotion.dev) assemble the result: deterministic, local, free.

You bring **any OpenAI-compatible LLM**: a free API key, or a small model on your own machine. I built it on **Ollama + `qwen3.5:4b`** (a weak 4B model, and it was enough) and also ran it with **Gemini 2.5 and 3.5** through their OpenAI-compatible API, which worked too.

## What you get

- **One prompt, one `.mp4`.** Say the language in the prompt ("in English", "на русском", "auf Deutsch") and titles/captions follow.
- **Two formats:** a *demo* walkthrough and a *corporate-promo* look with camera moves and call-outs. [Details](#formats-backgrounds-quality).
- **480p to 4K**, genuinely sharper at higher settings.
- **Runs entirely on your machine, even in a closed environment.** With a local model nothing ever leaves your computer: no cloud, no telemetry, no stock/TTS/image APIs. Demo and promo videos of an internal or private app are fine to make offline, even on a small model.
- **Self-healing local Ollama.** If it is installed but not running, CTV starts it and keeps the model warm.
- **Language-free navigation.** No per-site selectors, button texts or word lists in the code. DOM / ARIA / geometry decide *how* to act, your LLM decides what a button *means*.
- **Multi-step uploads.** Several `--upload` files are fed to the app one per step, in order.
- **Pacing from the prompt.** "Scroll slowly" really changes scroll duration, step size and hold time.
- **Non-destructive editing.** Change one scene (title, caption, colors, background, or even re-shoot it) without touching the rest.
- **Desktop app** for setup, generation and edits (Electron, not a localhost web page) **and** a full CLI.

## Quick start

Requirements: **Node.js 20+** (22 recommended). For the free local route, install [Ollama](https://ollama.com).

```bash
git clone https://github.com/Anatomik5/codetovideo.git
cd codetovideo
npm install          # also downloads Chromium for Playwright
ollama pull qwen3.5:4b
npm run app          # opens the desktop app
```

Windows: double-click `start-app.vbs` (no console window; installs on first run). macOS / Linux: `./start-app.sh` *(unverified, please report)*.

In the app: choose **Ollama (local, free)**, model `qwen3.5:4b`, leave the key empty. You do not need to start Ollama yourself.

### Try it without a project of your own

The repo ships a tiny three-step example app:

```bash
npx ts-node scripts/demo-pipeline.ts \
  --file examples/hello-wizard/server.js \
  --upload examples/hello-wizard/sample.csv \
  --model "qwen3.5:4b" --base-url "http://localhost:11434/v1" \
  --prompt "Show the full workflow from upload to export, in English"
```

### Your own app

```bash
npx ts-node scripts/demo-pipeline.ts \
  --file "path/to/your/project/or/launch-file" \
  --upload "data/sample.xlsx" \
  --format promo --quality 1080 \
  --model "gemini-2.5-flash" --base-url "https://generativelanguage.googleapis.com/v1beta/openai/" --api-key "$KEY" \
  --prompt "Quick, energetic overview: import, review, export. Captions in English."
```

Already running app? Use `--url http://localhost:3000` instead of `--file`. Free cloud keys work too (Gemini, OpenRouter, Groq, ...); put them in `.env` (see [`.env.example`](.env.example)) or pass `--api-key`.

## Formats, backgrounds, quality

| Option | Values | What it does |
| --- | --- | --- |
| `--format` | `demo` (default) | Walkthrough: browser window on an **animated backdrop** (strokes flicker, light sweeps travel through the artwork), badge + subtitle per scene. |
| | `promo` | Corporate-ad look: clean gradient, floating tilted window, camera pushes toward the real action, a **zoomed call-out cropped from the recording**, word-by-word captions, logo end card. |
| `--backdrop` (demo) | `auto` (default for cloud models) | Model draws an SVG; if it is too sparse, a neutral motif fills the edges. |
| | `generate` | The model draws everything. Best with strong models. |
| | `motif` (default for local models) | The model only *picks* a motif family (circuit, lattice, waves, skyline, constellation); the built-in generator draws it. Fast, ideal for small models. |
| `--quality` | `480` … `2160` | Output height in px (default 720). The browser is captured at a matching real device scale factor, so higher is sharper, and slower. |

Both formats are **silent** by design.

## Editing a scene

Every run is saved as a *session* (`out/sessions/<id>/`: `manifest.json`, `clips/scene_NN.mp4`, `props.json`, `final.mp4`).

```bash
# change a title (re-renders only the affected frames)
npx ts-node scripts/demo-pipeline.ts --edit-scene 2 --edit-prompt "Change this scene's title to Cost Breakdown"

# re-shoot only scene 3
npx ts-node scripts/demo-pipeline.ts --edit-scene 3 --edit-prompt "Re-shoot this step and scroll down to the table"
```

Your LLM decides which mode the instruction needs:

- **Text / style (mode A):** titles, captions, colors, background. Clips are untouched; when only that scene's text changed, only the key-frame-aligned range is rendered and the rest is stitched back with `ffmpeg -c copy`.
- **Re-shoot (mode B):** Playwright restarts the app, silently replays the earlier steps, records **only** that scene, and the other clips stay as they were.

## How it works

[![Architecture](docs/architecture.png)](docs/architecture.png)

<sub>Editable source: [`docs/architecture.drawio`](docs/architecture.drawio) · regenerate with `node scripts/build-diagram.cjs`.</sub>

1. **Repo study:** file tree (no caches, venvs, binaries), README, manifests, launch scripts.
2. **AI director:** one structured plan: title, intro/outro, scenes (`title`, `caption`, `targetGoal`), pacing, palette, background brief and motif, in the language you asked for. A health-checked client makes small local models reliable (JSON repair, compact retries, `keep_alive`, one context size so Ollama never reloads the model).
3. **Process executor:** frees ports, starts your app directly (no shell), finds its URL, always tears the process tree down.
4. **Scene-aware browser agent:** decides each step from the live DOM, moves a visible cursor, uploads files, fills required fields, clicks forward, scrolls at most a couple of times per screen so it never loops; stops with a clear `stopReason` if it cannot continue. Button *meaning* comes from your LLM, cached per label.
5. **Scene editor:** the session store described above.
6. **Compose:** clips are concatenated without cutting motion; Remotion renders the chosen format at the chosen size.

## CLI reference

| Flag | Meaning |
| --- | --- |
| `--file` / `--repo` | Project folder or launch file. CTV studies the repo, starts the app, finds its URL. |
| `--url` | URL of an already running web app (skips launching). |
| `--launch "<cmd>"` | Command that starts the app. Overrides the model's proposal (see [Security](#security-and-privacy)). |
| `--port` | Preferred port of the launched app. |
| `--prompt` | Free-form instructions in any language: scenario, caption language, style, colors, pacing. |
| `--upload` | File to upload in the app. Repeat for several; used in order. |
| `--model` `--base-url` `--api-key` | Your LLM (`LLM_MODEL`, `LLM_BASE_URL`, `LLM_API_KEY` also work). Ollama needs no key. |
| `--theme` | `auto` · `dark` · `light` |
| `--format` `--backdrop` `--quality` | See [above](#formats-backgrounds-quality). |
| `--out` | Output `.mp4` (default `out/demo.mp4`). |
| `--project-dir` / `--session` | Saved session to edit (default: newest in `out/sessions/`). |
| `--edit-scene <n\|id>` `--edit-prompt "…"` | Scene (1-based or id like `beat_3`) and what to change. |
| `--re-render-only` | Rebuild the final video from saved clips and manifest; no browser. |
| `--max-steps <n>` `--no-render` | Developer aids for quick smoke tests. |

### Export scene subtitles

Every render also writes `final.srt` into the session folder (`out/sessions/<id>/`, next to `final.mp4`): one cue per scene, shifted by the intro, using the scene title when a caption is empty. In the desktop app press **Export subtitles (.srt)** under the video to save a copy wherever you like. For an older session, or from a script, run `npm run subtitles -- out/sessions/<id>/manifest.json`.

## Honest status

**CTV is alpha.** It works end to end, but on a very small test surface. Please read this before you invest time:

- **Tested on:** Windows 11; Ollama with `qwen3.5:4b`; Gemini 2.5 and 3.5 via the OpenAI-compatible API (author's own runs); one real Next.js + FastAPI app and the bundled example. **Not tested:** macOS, Linux, other providers, most real-world apps.
- **Navigation is heuristic.** Logins, multi-tab flows, drag-and-drop, canvas apps, iframes and shadow DOM will probably defeat it. It stops with a `stopReason` instead of looping, but "stops" is not "works".
- **Small models give small results.** A 4B model writes serviceable but generic captions, sometimes splits scenes oddly, and its background drawings are often sparse (hence the motif fallback). Bigger models should do better; I have not verified how much.
- **Web UIs only.** No native desktop apps.
- **Re-shooting one scene** can show a small cursor/scroll jump at the cut.
- **Slow on CPU.** A ~75 s video at 720p takes a few minutes to render; 1080p and above take much longer.
- **Remotion's license is not plain MIT.** Companies above a small size need a paid license. See [THIRD_PARTY.md](THIRD_PARTY.md). "Free" here means *no per-use fees*, not "no license terms anywhere".
- **Quality bar of the output** is "decent first cut", not a replacement for a human editor.
- **Tests:** unit tests for the pure helpers plus a type check (`npm run check`). No automated end-to-end tests and no hosted CI yet.
- **No audio / narration.** Out of scope for now.

If any of this bites you, [open a run report](https://github.com/Anatomik5/codetovideo/issues/new?template=run_report.yml): that is exactly the feedback the project needs.

## Help wanted

I built CTV alone because I was annoyed, and it has outgrown what one person on one machine can test. **If this idea is useful to you, please help make it solid.** Concretely:

- 🙋 **Run it on your app and send a [run report](https://github.com/Anatomik5/codetovideo/issues/new?template=run_report.yml)**, even (especially) when it fails. This is the single most valuable contribution.
- 🙋 **macOS and Linux testers.**
- 🙋 Try **bigger / other models** (Gemini, OpenRouter, Groq, local 7B-14B) and tell us what changes.
- 🙋 Improve **scene planning prompts** and **caption quality** for small models.
- 🙋 `.srt` subtitle export, more promo templates, vertical (9:16) formats, installers, Docker image.
- Design discussion: a **free local TTS** option and an alternative renderer without Remotion's license constraint.

The full list with context is in [ROADMAP.md](ROADMAP.md); ground rules are in [CONTRIBUTING.md](CONTRIBUTING.md). Small PRs and honest bug reports are equally welcome. ⭐ A star helps others find the project.

## Security and privacy

- CTV **launches your app and clicks through it like a user.** Do not point it at systems with real data or side effects.
- Repo excerpts and page labels go **only to the LLM endpoint you configure.** Local model = nothing leaves your machine. No telemetry, no other network calls.
- Model-proposed start commands are **ignored unless they are a plain call to a known dev runtime** (python, node, npm, uvicorn, cargo, ...). Use `--launch` for anything else. Treat untrusted repositories as untrusted code anyway.
- The desktop app stores your API key encrypted with the OS keychain when available.

Details and how to report a vulnerability: [SECURITY.md](SECURITY.md).

## FAQ

**Is it really free?** CTV has no per-use cost: your own LLM or a free API key, plus local tools. Mind Remotion's license for commercial use and your provider's free-tier limits.

**Why not just use a text-to-video model?** Those invent UI. CTV only shows what your app actually does.

**Why not just screen-record?** You can! CTV adds the director: it plans scenes, drives the app, times captions to the real clicks, and lets you edit one scene later without redoing everything.

**Which model should I use?** Start with `qwen3.5:4b` via Ollama (what it was built on). For better plans and captions use a stronger model; for the demo background, pick `--backdrop generate` with strong models or `motif` with small ones.

**Can it narrate?** Not yet; videos are silent by design for now.

**My app needs a login.** Not supported out of the box. Run the app logged in or with a demo account via `--url`, and tell us how it went.

## Project layout

```
app/                       desktop app (Electron): main.js, preload.js, index.html
scripts/demo-pipeline.ts   the whole pipeline + CLI
scripts/build-diagram.cjs  regenerates docs/architecture.*
src/                       Remotion compositions: DynamicDemoScene (demo), PromoScene (promo)
examples/hello-wizard/     tiny app to try CTV with
tests/                     unit tests (npm test)
docs/                      manual, architecture diagram, demo, translations
out/sessions/              your saved sessions (git-ignored)
```

## Community

[CONTRIBUTING.md](CONTRIBUTING.md) · [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) · [SECURITY.md](SECURITY.md) · [CHANGELOG.md](CHANGELOG.md) · [ROADMAP.md](ROADMAP.md) · [THIRD_PARTY.md](THIRD_PARTY.md)

Translations: [Русский](docs/ru/README.md) *(community-style translation, may lag behind this file)*.

## Thanks

- [Dathinel](https://github.com/Dathinel): the first outside contribution, the SRT subtitle exporter (#7), which the desktop app's **Export subtitles** button and the per-session `final.srt` build on.

## License

CTV is released under the [MIT License](LICENSE): **use it for free, for any purpose, modify it and share it.** The dependencies keep their own licenses, most importantly Remotion's (companies above a small size need its commercial license): see [THIRD_PARTY.md](THIRD_PARTY.md).
