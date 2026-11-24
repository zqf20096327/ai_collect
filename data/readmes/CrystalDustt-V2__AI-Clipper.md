# Autonomous AI Clipper

A local-first Python CLI for video intelligence, structured AI-controlled video editing, and deterministic FFmpeg rendering. No browser UI is required: an AI agent analyzes transcript/visual timelines and authors a strict JSON **Clipper Editing Project (`CEP 1.0`)**, while validated local tools execute media transformations and renders.

---

## Key Capabilities

- **Autonomous Topic-Driven Duration & Multi-Clip Ledger**: By default (`--duration auto`), the AI decides each clip's natural length directly from its **key topic** — unlocking both punchy 12–40s shorts and **60–180s long-form Shorts** cleanly across timeline windows. Tracks completed clips via `clipper clips`, and adds extra clips without re-analyzing via `--more` / `clipper more-clips`.
- **Natural Topic Boundaries & Discovery Signals**: Computes cross-window `key_topics`, `topic_blocks`, speech pauses, terminal punctuation, `natural_cut_points` (`--snap-boundaries`), vocal **audio energy peaks** (`energy_peaks`), and localized **UI/slide change detection** (`slide_changes`) so clips open on crisp hooks/slides and never slice topics mid-sentence.
- **Face-First / Device-Screen-Second Reframing (`MediaPipe`)**: Combines MediaPipe face detection & facial-landmark active speaker detection with transcript correlation and screen-content detection:
  - Keeps speaker face as **Priority #1** and dynamically transitions to device screen (**Priority #2**) when the speaker talks about or interacts with a screen (or when no face is present).
  - Supports `auto`, `crop`, `fit_blur` (keeps 16:9 video centered uncropped inside 9:16 with a zoomed, blurred top/bottom video backdrop), `split_2up` (vertical 2-speaker podcast split-screen), and `webcam_top` (extracts corner speaker/webcam into the top band and stacks full 16:9 screen/slides cleanly below).
- **Live-Word Reels & Shorts Captions**:
  - 10 subtitle presets including `spotlight` (default), `bold`, `hormozi`, `pill`, `box`, `bounce`, `kinetic`, `karaoke`, `word`, and `minimal`, plus optional `--bottom-scrim` gradient backing and `--dual-speaker-colors` A/B speaker highlighting.
  - Bundled static OFL social fonts (`Montserrat` default, `Montserrat ExtraBold`, `Poppins`, `Poppins ExtraBold`, and `Bebas Neue`) staged cleanly via FFmpeg `fontsdir` with companion `.srt`, `.post.txt`, and `.meta.json` ready-to-post social exports (and character-proportional word fallback when source segments lack word timestamps).
- **Multi-Track Compositing, Visual Polish & Audio Processing**:
  - B-roll `video_overlays` (`cutaway`, `pip`, `split_top`, `split_bottom`), `image_overlays` (PNG/WebP logos/stickers with alpha fades), 11 `xfade` / `acrossfade` clip transitions, timed hook overlays, retention progress bars, audio-reactive `--waveform` overlays (`showwaves`), and color grading (`--look clean|punchy|cinema|warm` or custom `.cube` 3D LUT via `--lut`).
  - Registered audio assets with speech-ducked music/SFX mixing, optional `--trim-silence`, `--remove-fillers`, `--remove-retakes` (false-start/stumble cleaner), `--cold-open` teaser hook extraction, `--voice-enhance`, two-pass EBU R128 loudness normalization (`loudnorm`), hardware H.264 auto-detection (`nvenc`, `qsv`, `amf`, or `libx264`), parallel workers (`--workers`), and auto cover thumbnails (`--thumbnails`).
- **2D Preview Layout & Safe-Zone Checks (`--review enabled`)**: Verifies pixel-accurate text bounds, subtitle/overlay de-duplication, speech boundary completion, vertical platform safe zones, and 2D spatial+temporal bounding-box collision checks (`overlay_layout_collision`) across captions, text overlays, PIPs, image overlays, and progress bars.
- **Deterministic Validation & Fault-Tolerant Agent Loop**:
  - Strict Pydantic v2 `CEP 1.0` schema (`examples/cep.schema.json`), immutable revisions, context compaction with image shedding & long-video `agent_record_window` notes, error recovery hints, and mid-session prose/budget safeguards.

---

## Requirements

- **Python** `>= 3.11`
- **FFmpeg & FFprobe** with `libx264` and `libass` available on `PATH` (or via `CLIPPER_FFMPEG` / `CLIPPER_FFPROBE`, or `.tools/*/bin` on Windows)
- On headless Linux environments running MediaPipe/OpenCV: `libgl1`, `libegl1`, `libgles2`, and `libglib2.0-0`
- Optional extras declared in [pyproject.toml](pyproject.toml):
  - `transcription` (`faster-whisper`) for local offline word-level speech transcription
  - `download` (`yt-dlp`) for supported URL resolution
  - `dev` (`pytest`, `ruff`) for testing and linting

---

## Installation

Install with [uv](https://docs.astral.sh/uv/):

```bash
# Full installation (recommended)
uv sync --extra transcription --extra download --extra dev
```

Or use the included helper scripts (which also install the `clipper` command shim into `~/.local/bin`):

```powershell
# Windows (PowerShell)
pwsh ./scripts/sync.ps1
```

```bash
# macOS / Linux
bash ./scripts/sync.sh
```

Verify your environment, binaries, MediaPipe models, bundled fonts, and detected GPU encoder:

```bash
clipper doctor
```

> FFmpeg builds can be downloaded from [ffmpeg.org/download.html](https://ffmpeg.org/download.html). The first Whisper run downloads the configured model locally and reuses its cache afterward (transcription runs locally on CPU/int8 by default and never sends audio to external LLM providers).

---

## Configure the AI Provider

Copy `config.example.yaml` to `config.yaml` (gitignored) or configure via `CLIPPER_<SETTING>` environment variables. Any setting can also be paired with `.env.example` as reference (`.env` is not implicitly loaded).

### Local Ollama
```powershell
$env:CLIPPER_PROVIDER = "ollama"
$env:CLIPPER_BASE_URL = "http://localhost:11434"
$env:CLIPPER_MODEL = "YOUR_TOOL_CAPABLE_MODEL"
$env:CLIPPER_VISION = "true"  # Set true only if your model supports both images and tools
clipper run "video.mp4"
```

### OpenAI-Compatible Endpoint
```powershell
$env:CLIPPER_PROVIDER = "openai"
$env:CLIPPER_BASE_URL = "https://api.openai.com/v1"
$env:CLIPPER_MODEL = "YOUR_COMPATIBLE_MODEL"
$env:OPENAI_API_KEY = "YOUR_API_KEY"
clipper run "video.mp4"
```

Verify structured tool-call compatibility before running long edits:

```bash
clipper provider-check
```

> If `faster-whisper` is not installed, pass `--srt source.srt` to supply captions (per-word timestamps are automatically interpolated), or set `CLIPPER_TRANSCRIPTION=off` for visual-only workflows with `CLIPPER_VISION=true`.

---

## Quick Usage Examples

```bash
# Default autonomous pipeline: AI decides each clip's length (12-180s) by key topic,
# unlocking both quick Shorts and 60-180s long-form Shorts, 9:16 portrait,
# Face-First/Screen-Second auto-reframe, Montserrat live-word spotlight captions
clipper run video.mp4

# Focus specifically on deep 45-180s long-form Shorts (or pass explicit MIN-MAX e.g. 90-240)
clipper run video.mp4 --duration long

# Keep 16:9 clips centered inside 9:16 with a zoomed, blurred video backdrop top & bottom
clipper run video.mp4 --framing-mode fit_blur

# Stylized Reels/Shorts captions and custom bundled font
clipper run video.mp4 --subtitles hormozi
clipper run video.mp4 --subtitles pill --font Poppins
clipper run video.mp4 --subtitles bounce --font "Bebas Neue"

# Tighten pauses, filler words & false-start retakes, add a cold-open teaser hook, enhance voice, progress bar & cover thumbnails
clipper run video.mp4 --trim-silence --remove-fillers --remove-retakes --cold-open --voice-enhance --progress-bar --thumbnails --workers 2

# Inspect stored clips & create additional distinct clips from the same source
clipper clips PROJECT_ID
clipper more-clips PROJECT_ID --clips 3 --subtitles hormozi

# Resume a paused or interrupted session without repeating completed stages
clipper resume PROJECT_ID
```

---

## Try the Engine Without AI Credentials

Two reproducible local scripts generate real synthetic video/audio fixtures and render MP4s without requiring an API key:

```bash
uv run python examples/make_demo.py
uv run python examples/audio_mix_demo.py
```

Live end-to-end provider acceptance can also be tested against your configured endpoint:

```bash
uv run python examples/live_acceptance.py VIDEO --duration 15-45 --srt optional.srt
```

---

## Command Reference

```text
clipper --help
clipper doctor
clipper provider-check
clipper setup-path
clipper schema --output examples/cep.schema.json

clipper ingest VIDEO_OR_URL
clipper analyze PROJECT_ID [--srt optional.srt]
clipper inspect PROJECT_ID --at-ms 83450 [--end-ms 90000 --samples 6]
clipper search PROJECT_ID "query"
clipper highlights PROJECT_ID [--generate]

clipper run SOURCE [OPTIONS]
clipper more-clips PROJECT_ID [--clips 3 ...]
clipper resume PROJECT_ID
clipper status PROJECT_ID
clipper clips PROJECT_ID
clipper render PROJECT_ID [--results ./results --workers 2]

clipper import-edit PROJECT_ID CEP.json
clipper finalize PROJECT_ID HIGHLIGHT_ID EXPECTED_REVISION
clipper tool PROJECT_ID media.get_timeline '{"start_ms":0,"end_ms":60000}'

clipper reframe PROJECT_ID HIGHLIGHT_ID CLIP_ID --aspect 9:16 --framing-mode auto --split-scenes
clipper snap-boundaries PROJECT_ID HIGHLIGHT_ID
clipper trim-silence PROJECT_ID HIGHLIGHT_ID [CLIP_ID] --min-silence 500 --pad 80 --remove-fillers --remove-retakes
clipper cold-open PROJECT_ID HIGHLIGHT_ID [--start-ms 12000 --end-ms 15200 --transition fade]
clipper transition PROJECT_ID HIGHLIGHT_ID FROM_CLIP TO_CLIP --type wipeleft --duration-ms 500
clipper overlay-video PROJECT_ID HIGHLIGHT_ID vo1 --start-ms 1000 --end-ms 4000 --mode pip --pip-position top_right
clipper overlay-image PROJECT_ID HIGHLIGHT_ID io1 --asset-id brand_logo --start-ms 0 --end-ms 3000 --position top_right --scale 0.2 --opacity 0.9
clipper asset-register PROJECT_ID whoosh.wav whoosh "Own recording" --category sfx
clipper assets PROJECT_ID
clipper review PROJECT_ID HIGHLIGHT_ID results/PROJECT_ID/clip.mp4
clipper thumbnail PROJECT_ID HIGHLIGHT_ID results/PROJECT_ID/clip.mp4
```

Key `clipper run` flags:
- `--aspect 9:16|16:9|1:1` (default `9:16`)
- `--duration auto|long|MIN-MAX` (default `auto`: AI sizes each clip 12–180s based on its key topic, unlocking long-form Shorts; `long`: 45–180s; or explicit bounds like `20-60` or `90-300`)
- `--clips auto|COUNT` (default `auto`, up to 8 highlights per batch, 30 max)
- `--more` (add new non-overlapping clips to an existing project)
- `--framing-mode auto|crop|fit_blur|split_2up|webcam_top` (`--auto-reframe/--no-auto-reframe`, default `auto` enabled)
- `--subtitles bold|minimal|word|kinetic|karaoke|bounce|spotlight|box|pill|hormozi|off` (default `spotlight`)
- `--font Montserrat|"Montserrat ExtraBold"|Poppins|"Poppins ExtraBold"|"Bebas Neue"` (default `Montserrat`)
- `--bottom-scrim`, `--dual-speaker-colors`, `--waveform`, `--look none|clean|punchy|cinema|warm`, `--lut PATH.cube`
- `--trim-silence`, `--remove-fillers`, `--remove-retakes`, `--cold-open`, `--voice-enhance`, `--progress-bar`, `--thumbnails`
- `--review enabled|disabled` (default `disabled`; when enabled, runs preview quality checks & bounded revision fixes before finalization)
- `--workers N` (parallel highlight rendering workers)

---

## Timeline & Safety Contract

- `CEP 1.0` uses **one ordered, gapless video track** backed by the ingested source. Clip array order defines output order; source ranges are half-open integer milliseconds `[source_start_ms, source_end_ms)`.
- Keyframes use **clip-local output ms** starting at `0`; overlays (`overlays`, `video_overlays`, `image_overlays`) and registered audio tracks use **finished-video ms**.
- Every modification increments `revision` cleanly and returns state to `EDITING`. Rendering accepts only finalized `READY_TO_RENDER` or verified `COMPLETED` projects.
- Unknown schema keys/fields are rejected (`extra="forbid"`). AI outputs are never executed as shell commands; caption text is escaped before ASS rendering; direct HTTP(S) downloads enforce public-address SSRF checks and DNS-pinned redirects.
- Source files referenced by `source.json` are hashed and kept in place (finalization fails if modified).

---

## Workspace Artifacts

```text
workspaces/projects.sqlite3
workspaces/video_<hash>/
  source.json                 # Original local path, SHA-256, stream metadata, source URL
  intelligence/               # VID, transcript JSON/SRT, scenes, silence, highlights, ledger
  frames/                     # Decoded inspection frames with PTS metadata
  edits/                      # CEP 1.0 JSON files and revision history
  previews/                   # Preview renders, contact sheets, quality reports
  logs/                       # FFmpeg / media diagnostics
  agent_session.json          # Persisted conversation & tool call history
  agent_history/              # Archived exchanges from context compaction
  assets/                     # Registered audio/video/image assets with provenance hashes
results/video_<hash>/         # Final MP4s, companion .srt captions, manifests, optional .thumb.jpg
```

---

## Development & Testing

```bash
# Lint source, tests, and examples
uv run --extra dev ruff check src tests examples

# Run full test suite (92 tests covering timing, MediaPipe tracking, styles, FFmpeg rendering, compaction, URLs)
uv run --extra dev pytest -q
```

---

## Limitations

- Platform URL downloading relies on `yt-dlp` returning obtainable direct media formats; playlists, live streams, DRM, streaming manifests, cookie-gated sessions, and JavaScript anti-bot challenges are not supported (local media files remain supported).
- Subtitle overflow (`text_layout`) is a Pillow bounding-box measurement estimate rather than rendered-pixel OCR; black/silent/peak warnings in quality reports are objective diagnostics and may require editorial judgment.
- Model quality depends on the configured provider/model's structured JSON tool-calling reliability.

---

## License & Notices

Released under the [MIT License](LICENSE). See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for bundled font (OFL-1.1) and MediaPipe model (Apache-2.0) attributions.

References: [FFmpeg Filters](https://ffmpeg.org/ffmpeg-filters.html) · [PyAV](https://pyav.org/docs/stable/api/container.html) · [faster-whisper](https://github.com/SYSTRAN/faster-whisper) · [yt-dlp](https://github.com/yt-dlp/yt-dlp) · [MediaPipe](https://developers.google.com/mediapipe) · [Ollama Chat API](https://docs.ollama.com/api/chat) · [OpenAI Chat Completions](https://platform.openai.com/docs/api-reference/chat/create)
