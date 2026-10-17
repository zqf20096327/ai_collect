# PolyScribe

PolyScribe is a lightweight desktop tool for fully offline live **speech transcription** and **translation**, powered by [Vosk](https://alphacephei.com/vosk/) and [Argos Translate](https://www.argosopentech.com/). It includes a polished desktop GUI with real-time transcription, a built-in model downloader (76 models across 34 languages), and a full set of productivity features — all running 100% offline.

## Features

- 🎙️ Real-time speech recognition (fully offline, powered by Vosk)
- 🌐 Translate spoken language into 20+ languages (Argos Translate)
- 🔊 Text-to-speech output of transcribed/translated text
- 🖥️ Modern desktop GUI with 8 color themes (Dark, Light, Rose, Blush, Sage, Violet, Navy, Amber)
- 📦 Built-in Model Manager — 76 Vosk models + Argos packages, filtered by language/quality, download with progress bar
- 📁 Transcribe audio files (WAV/MP3/M4A/FLAC/OGG/AAC via ffmpeg)
- 🔍 Auto language detection — records a short sample and picks the best model
- 💾 Export transcripts as .txt, .srt (subtitles), or .json
- 🕐 Session history — past sessions autosave and can be browsed/reopened
- 🖼️ Floating subtitle overlay — always-on-top translucent window for presentations
- ⌨️ Keyboard shortcuts (Cmd/Ctrl+Shift+S = start/stop, Cmd+F = search, Cmd+E = export)
- 🔤 Font size controls (A+/A−) for accessibility
- ⚡ Low-confidence word highlighting (amber + underline) so you can spot likely errors
- 🧪 Unit + integration test suite (98 tests, including live URL verification)
- 💻 Terminal mode also available for headless/server use

## Requirements

- Python 3.11 (important: `sentencepiece` may break on later versions)
- Works on macOS, Windows, and Linux with compatible audio devices
- Tkinter (bundled with Python on macOS/Windows; Linux: `sudo apt install python3-tk`)
- Optional: `ffmpeg` on PATH for transcribing non-WAV audio files

## Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/kcitlyn/PolyScribe.git
cd PolyScribe

# 2. Create virtual environment (Python 3.11 recommended)
python3.11 -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the GUI
python desktop/gui.py
```

On first launch, open the **Models** tab to download a speech model (the "English (US) — small" at 40 MB is fast to grab). Then switch to the Transcribe tab and hit Start.

## Usage

### GUI Mode (recommended)

```bash
python desktop/gui.py
```

**Transcribe tab:**
- Select mode (transcription / translation), source + target language, and microphone
- Click **Start** to begin live recognition, **Stop** to end
- Use **Detect language** to auto-detect (needs 2+ models installed)
- Use **Open audio file…** to transcribe a recording from disk
- **Export…** saves the transcript as .txt, .srt, or .json
- **Overlay** opens a floating subtitle window

**Models tab:**
- Filter by language or quality tier (small/medium/large)
- Download models with a progress bar
- Delete models you no longer need

**History tab:**
- Past sessions are saved automatically when you stop recording
- Double-click to reload, or export/delete

### Terminal Mode

```bash
python desktop/main.py
```

Follow the on-screen prompts for mic, mode, and language.

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Cmd/Ctrl+Shift+S | Start / stop listening |
| Cmd/Ctrl+F | Search transcript |
| Cmd/Ctrl+E | Export transcript |
| Cmd/Ctrl++ | Increase font size |
| Cmd/Ctrl+- | Decrease font size |

## Themes

Switch between 8 themes in the top-right picker. Your choice is saved between sessions.

| Theme | Style |
|-------|-------|
| Dark | Deep purple-blue |
| Light | Clean white/blue |
| Rose | Soft pink |
| Blush | Warm pastel pink |
| Sage | Earthy green |
| Violet | Soft purple |
| Navy | Deep navy with cyan |
| Amber | Warm orange-peach |

## Manual Model Setup (optional)

If you prefer to download models manually:

1. Create the folders (already exist after clone):
   ```
   models/vosk_models/      ← unzipped Vosk model folders go here
   models/translation_models/ ← .argosmodel files go here
   ```

2. Download Vosk models from https://alphacephei.com/vosk/models

3. Download Argos models from https://www.argosopentech.com/argospm/index/

4. Install Argos packages:
   ```bash
   python desktop/install_translation_package.py
   ```

PolyScribe auto-detects any Vosk model by folder name. No code changes needed.

## Running Tests

```bash
pip install pytest
pytest tests/ -v              # all tests (offline + network)
pytest tests/ -m "not network"  # skip URL verification
```

The test suite covers language detection, resampling math, transcript export/history, catalog structure, and live download URL verification.

## Building a Standalone App

```bash
pip install pyinstaller
python desktop/build_app.py
```

Produces `dist/PolyScribe.app` (macOS), `dist/PolyScribe/PolyScribe.exe` (Windows), or `dist/PolyScribe/PolyScribe` (Linux). Models are not bundled — the app downloads them through the Model Manager on first run.

## Project Structure

This is a monorepo: `core/` holds the speech/translation logic shared by every
frontend, and each platform (`desktop/`, `rpi/`) is a thin frontend on top of it.

```
PolyScribe/
├── core/                        # shared logic — no UI, no hardware
│   ├── utils.py                 # terminal prompts & audio loop (desktop CLI)
│   ├── languages/
│   │   ├── languages.py         # auto-scans vosk_models/, 34 languages
│   │   ├── speak.py             # text-to-speech (pyttsx3)
│   │   └── voice_config.json    # TTS defaults
│   └── translation/
│       ├── transcription.py     # Vosk streaming + file transcription
│       └── text_translate.py    # Argos translation wrapper
├── desktop/                      # desktop GUI + CLI frontend
│   ├── gui.py                   # Desktop GUI (Tkinter)
│   ├── model_manager.py         # Model downloader UI
│   ├── vosk_catalog.py          # Full 76-model Vosk catalog
│   ├── themes.py                # 8 color themes + persistence
│   ├── widgets.py                # Custom PillButton / Card widgets
│   ├── transcript.py            # Transcript model, export, history
│   ├── language_detect.py       # Auto language detection
│   ├── main.py                  # Terminal mode entry point
│   ├── build_app.py             # PyInstaller build script
│   └── install_translation_package.py
├── rpi/                          # Raspberry Pi frontend (prototype/WIP)
│   ├── main.py                  # RPi entry point
│   ├── utils_hardware.py        # transcription/translation loop for hardware I/O
│   ├── requirements.txt         # adds RPi.GPIO on top of the root requirements
│   └── hardware/
│       ├── display_logic.py     # on-device menu/display state machine
│       ├── input_handler.py     # GPIO button + keypad drivers
│       └── config.json          # device runtime config
├── tests/                       # 98 tests (pytest), cover core/ + desktop/
├── models/                      # (gitignored) downloaded models
├── history/                     # (gitignored) autosaved sessions
├── requirements.txt
└── third_party/                 # Vosk + Argos license texts
```

## Raspberry Pi

`rpi/` is an early, in-progress port of PolyScribe for a standalone device with a
keypad and small display instead of a desktop GUI — it reuses `core/` for speech
recognition and translation and adds GPIO-driven input/display in `rpi/hardware/`.
It previously lived in its own repo (`PolyScribe-RPI`), now merged in here so the
shared logic in `core/` stays in one place instead of drifting between two copies.

## Text-to-Speech Voices

- **macOS:** Most languages pre-installed.
- **Windows:** Settings → Time & Language → Speech → Add voices.
- **Linux:** Install `espeak-ng` or `festival`.

List available voices:
```python
from languages.speak import Speak
Speak.print_all_voices_available()
```

## Licenses

- [Vosk](https://github.com/alphacep/vosk-api) — Apache 2.0 ([license](./third_party/vosk-api-LICENSE.txt))
- [Argos Translate](https://github.com/argosopentech/argos-translate) — GNU GPLv3 ([license](./third_party/argostranslate-LICENSE.txt))

---

If you found this project helpful or interesting, I'd really appreciate a ⭐! Feel free to open an issue, submit a pull request, or reach out.
