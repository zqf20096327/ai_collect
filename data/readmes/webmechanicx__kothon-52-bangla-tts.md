<p align="center">
  <img src="assets/app-icon.png" width="160" alt="Kothon 52 Bangla TTS logo">
</p>

# Kothon 52 Bangla TTS

A standalone desktop application for Bengali text-to-speech synthesis using the [BosonLab/chatterbox-bangla](https://huggingface.co/BosonLab/chatterbox-bangla) model.

## Features

- **Text-to-Speech**: Enter Bengali text and generate speech
- **Voice Cloning**: Optionally clone a voice from a reference recording
- **Record Your Voice**: Record directly from your microphone to create a voice profile (5-10 s of clear speech recommended)
- **Voice Profiles**: Profiles are stored in an embedded SQLite database (`voices.db`); select any profile from a dropdown before generating
- **Preview / Delete**: Listen to a stored profile's reference audio or delete it
- **Playback**: Play generated audio in-app
- **Save**: Export generated audio as WAV files
- **Cross-platform**: macOS (.dmg), Windows (.zip), Linux (.deb)

## Installation

### macOS
Download `Kothon52BanglaTTS-1.2.0-macOS.dmg` and drag to Applications.

### Windows
Download `Kothon52BanglaTTS-1.2.0-Windows.zip`, extract, and run `Kothon52BanglaTTS.exe`.

### Linux
Download `Kothon52BanglaTTS-1.2.0-Linux.zip`, extract, and install `Kothon52BanglaTTS-1.2.0-Linux.deb` with `sudo dpkg -i`.

## First Run

On first launch the app downloads model weights (~3.2 GB) from Hugging Face. This only happens once.

On first recording, the OS will ask for microphone permission (macOS: System Settings → Privacy & Security → Microphone).

## Data Locations

The user-data folder keeps its historical name (`ChatterboxBanglaTTS`) for compatibility with existing installs.

| Platform | Path |
|----------|------|
| macOS | `~/Library/Application Support/ChatterboxBanglaTTS/` |
| Windows | `%APPDATA%\ChatterboxBanglaTTS\` |
| Linux | `$XDG_DATA_HOME/ChatterboxBanglaTTS/` (default `~/.local/share/`) |

Contains: `voices.db` (profile metadata), `voices/` (profile audio), `recordings/`, `output/`, `models/`.

## Building from Source

```bash
# Clone
git clone <repo>
cd kothon-52-bangla-tts

# Setup
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install pyinstaller

# Run in dev mode
python app/main.py

# Build standalone macOS .app + DMG (requires ffmpeg on PATH)
scripts/build_macos.sh
```

## Project Structure

```
app/
  main.py              # PySide6 GUI (recording, profiles, synthesis)
  voice_db.py          # Embedded SQLite voice profile store
  ui/                  # Theme, icons, widgets, overlay dialogs
vendor/
  chatterbox-finetuning/  # Upstream inference toolkit (vendored, unmodified)
  chatterbox_/           # Patched Chatterbox TTS inference code
Kothon52BanglaTTS.spec    # PyInstaller spec (onedir + mic permission)
scripts/
  build_macos.sh       # macOS .app + DMG build
.github/workflows/
  build.yml            # CI: builds Windows + Linux installers
requirements.txt
```

## Credits

- [BosonLab/chatterbox-bangla](https://huggingface.co/BosonLab/chatterbox-bangla) - Model
- [gokhaneraslan/chatterbox-finetuning](https://github.com/gokhaneraslan/chatterbox-finetuning) - Inference toolkit (vendored)
- [ResembleAI/chatterbox](https://github.com/resemble-ai/chatterbox) - Base model
