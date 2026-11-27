# Featherbox

**Website:** https://ashishyadavstudio.github.io/Featherbox/ · **Download:** [latest release](https://github.com/AshishYadavStudio/Featherbox/releases/latest)

**Local AI, light on your PC.** One app that downloads and runs text, image, video, voice and speech-to-text AI models
entirely on your own computer: no cloud, no account, no subscription. It's built for ordinary laptops
with 4–6 GB graphics cards (and works on CPU-only PCs, more slowly).

![The Featherbox Library: five finished vertical videos made on a laptop with a 4 GB graphics card](docs/img/library.webp)

- **Models**: a catalog of text, image, video and voice models, each with plain "will it run on this PC?"
  advice. Download any of them, pick which one is used, or add your own Hugging Face links.
- **Chat** with a local text model.
- **Studio** (the first ready-made creation): type a topic and get a finished vertical video with a
  script, voiceover, AI pictures or AI motion, captions and music.
- **Image**, **Video** and **Voice** tools: make a picture, a short AI clip (from text or from a picture)
  or a voice recording directly, with any installed model.
- **Transcribe**: turn a recording, a voice note or a video into text and subtitles (SRT/VTT) with
  Whisper, in 99 languages including Hindi.

## Screenshots

| | |
|---|---|
| ![Studio: topic, language, length and tone, then Write script](docs/img/studio.webp) | ![Image: prompt, model, shape and style, with a generated tea stall picture](docs/img/image.webp) |
| **Studio**: a topic in, a finished Short out | **Image**: describe a picture and your PC paints it |
| ![Video: start from a picture, describe the motion, pick model and quality](docs/img/video.webp) | ![Voice: text box, voice picker grouped by language and a speed slider](docs/img/voice.webp) |
| **Video**: short AI clips from text or a picture | **Voice**: natural voiceovers in English, Hindi and more |
| ![Transcribe: a podcast intro transcribed line by line with timestamps](docs/img/transcribe.webp) | ![Models: hardware detection and plain advice for every model](docs/img/models.webp) |
| **Transcribe**: speech to text and subtitles | **Models**: "will it run on this PC?" for every model |

## Install (for users)

Run `Featherbox-Setup-<version>.exe` (about 80 MB). There's no admin prompt and nothing else to
install first: Python and the interface are bundled. Setup adds Start-menu and desktop shortcuts and
an entry in Windows "Installed apps".

- **Featherbox** opens in its own window (Microsoft Edge app mode). A tray icon by the clock keeps it
  running; right-click it → **Quit Featherbox**. Opening the shortcut again just brings the window back.
- First start: **Models → One-click setup** downloads the AI engines and models for that PC (once).
- Everything lives in the install folder: the program in `app\` and `python\`, and models, videos and
  settings in `data\`. Updating (running a newer Setup) replaces the program and keeps `data\`.
  Uninstalling asks whether to keep `data\` so a reinstall doesn't need to download again.
- Unsigned build: Windows SmartScreen shows "Windows protected your PC" → **More info → Run anyway**
  until the installer is code-signed.

### Updates

From 0.3.0 on, Featherbox checks GitHub about once a day for a newer release; only that request is sent, nothing
personal. A banner shows the new version with its release notes, and **Update now**:

1. downloads the installer to the Temp folder;
2. checks it against the SHA-256 checksum GitHub publishes, and won't run a file that doesn't match;
3. runs it silently (`/S /UPDATE /D=<install folder>`).

Setup closes the app, replaces the program, keeps `data\`, and restarts it in the background, and the open window
reloads into the new version (about 15 s). Updating is refused while something is being made or a model is
downloading. **Models → Featherbox x.y.z** has **Check now** and a switch to turn automatic checks off. Copies
running from source only get a Download link. 0.2.x has no updater, so install 0.3.0 by hand once.

Silent install for IT/testing: `Featherbox-Setup.exe /S /D=C:\Featherbox`; uninstall with
`uninstall.exe /S` (add `/DELETEDATA` to remove models and videos too).

### Building the installer

```bash
backend\.venv\Scripts\python installer\build.py        # -> installer\dist\Featherbox-Setup-<version>.exe
```

No extra tools needed. It copies the Python runtime this venv was made from (trimmed) plus the venv's
packages and the Microsoft C++ runtime DLLs, builds the UI, compiles the launcher, setup and uninstaller
with the C# compiler that ships with Windows (`installer\Launcher.cs`, `installer\Setup.cs`), and embeds
everything in one Setup.exe. Bump `APP_VERSION` in `backend/app/config.py` for a new release.

## Quick start (developers)

Double-click `start.bat`. The first run creates the Python environment and builds the UI. After that
it opens `http://127.0.0.1:8420` in your browser.

1. **Models** → **One-click setup** installs the best engines and models for the detected hardware
   (about 6.5 GB on an NVIDIA GPU). Downloads resume if interrupted.
2. **Studio** → type a topic, pick language, length and tone → **Write script**.
3. Edit the scenes if you like, pick a visual style, voice and background music → **Make video**.
4. On the finished video, fix any single scene: **New image** repaints it (about 30 s) and
   **Update voice** re-records an edited line (about 15 s). Only that scene is rebuilt. Background
   music can be changed in about 10 s.
5. Finished videos are listed in **Library** (**Edit scenes & music** reopens them) and saved under
   `data/outputs/<project>/final.mp4`.

Developer requirements: Windows 10/11, Python 3.11+, Node 18+ (only to build the UI), and an FFmpeg on
PATH, or install it from the Models page.

## Linux

Featherbox runs on Linux from source (x86-64; there is no installer or tray app yet). It is tested on
Ubuntu 24.04 LTS, and the engine builds it downloads run on Ubuntu 24.04 and newer, or any distro of the
same age (glibc 2.39+).

```bash
sudo apt install python3 python3-venv nodejs npm ffmpeg fonts-noto-core
# graphics cards through Vulkan (AMD, Intel, and NVIDIA for pictures and video):
sudo apt install mesa-vulkan-drivers libvulkan1
git clone https://github.com/AshishYadavStudio/Featherbox.git
cd Featherbox && ./start.sh
```

`start.sh` sets up Python and builds the interface on the first run, then opens
`http://127.0.0.1:8420` in your browser. Run it again to start Featherbox later; update with `git pull`.

What is different from Windows:

| | Windows | Linux |
|---|---|---|
| Text (llama.cpp) | CUDA, Vulkan or CPU | CUDA (NVIDIA driver 570+, CUDA 12.8), Vulkan or CPU |
| Pictures and video (stable-diffusion.cpp) | CUDA, Vulkan or CPU | Vulkan or CPU: there is no Linux CUDA build, so NVIDIA cards use Vulkan |
| Transcribe (whisper.cpp) | CUDA or CPU | CPU (there is no Linux CUDA build) |
| Updates | One click | `git pull` |

The engines are the official Linux builds of the same versions as on Windows, except stable-diffusion.cpp,
which uses the 2 November 2026 build: newer Linux builds are made on Ubuntu 26.04 and don't start on
24.04 LTS. That build supports every model in the catalog. Built-in AMD and Intel graphics are detected
from the kernel's device files (with `lspci` for the product name when it is installed). Hindi captions
use Noto Sans Devanagari (`fonts-noto-core`) or any other installed Devanagari font.

## How it works

```
React UI (frontend/)  ──HTTP──▶  FastAPI backend (backend/app)
                                   ├─ hardware.py   picks CUDA / Vulkan / CPU and model sizes
                                   ├─ catalog.py    pinned engine builds + curated models
                                   ├─ downloads.py  resumable installer
                                   ├─ jobs.py       one GPU job at a time
                                   ├─ engines/
                                   │   ├─ llm.py        llama.cpp `llama-server` (script writing, chat)
                                   │   ├─ image.py      stable-diffusion.cpp CLI (scene images)
                                   │   ├─ tts.py        Kokoro ONNX on CPU (voiceover, EN + HI)
                                   │   ├─ stt.py        whisper.cpp `whisper-cli` (speech to text, CPU or CUDA)
                                   │   ├─ textrender.py HarfBuzz-shaped captions (Hindi renders correctly)
                                   │   ├─ music.py      built-in music moods (synthesised, no download) + your tracks
                                   │   └─ video.py      camera moves, AI clip loops, captions, crossfades, music ducking
                                   └─ recipes/topic_to_short.py
```

Each project folder keeps its scene images, voice lines and video segments, so a touch-up rebuilds
one segment, re-joins the segments (a stream copy) and re-mixes the music.

**Music.** Five built-in moods (Calm, Uplifting, Playful, Mysterious, Epic) are synthesised with numpy
(pads, bass, plucks, bells, FFT reverb), so they're royalty-free and need no download. "Auto" picks
a mood from the script's tone. Your own tracks (mp3/wav/m4a/ogg/flac) go to `data/music/`. FFmpeg
`sidechaincompress` ducks the music about 9 dB while the voice is speaking (about 22 dB under the
voice at the default 50% volume).

Low-VRAM design: the text model is unloaded before images are generated. Voiceover runs on the CPU
**in parallel** with image generation on the GPU. If the text model doesn't fit fully, GPU layers are
calculated from free VRAM.

## Model library

The **Models** page lists every model the app knows about, in tabs: Text, Image, Video, Voice, Music and
Engines. Each model gets advice for *this* PC, but nothing is ever blocked: you can download any model.

| Badge | Meaning |
|---|---|
| Runs well | Fits in the graphics memory (or runs fast on the CPU, for voice) |
| Runs slowly | Part of the model is kept in RAM / runs on the CPU |
| Very slow | CPU only, or far more graphics memory needed than this PC has |
| Probably won't run | Not enough RAM; you get a "download anyway?" check first |

- **Use this** picks which installed text and image model the Studio uses.
- **Add your own model**: paste a Hugging Face file link (`.gguf` text models, or SD 1.5 / SDXL
  `.safetensors` checkpoints). The link is checked and the size read before it is added. Gated models
  (which need a Hugging Face login) are not supported yet. User-added text models are placed on the
  GPU automatically by llama.cpp (`--fit on`).
- Files shared by several models (the Flux VAE, Qwen3 4B used by Z-Image, the umt5 video encoder, the
  Wan 2.2 VAE) are downloaded once and only deleted when no installed model needs them.
- Image architectures used by the catalog: SD 1.5, SDXL, FLUX.1, FLUX.3, Z-Image and Qwen-Image 2.1.
  Piper and MusicGen are listed as coming soon.

### Added in November 2026 (marked "New")

| Kind | Models |
|---|---|
| Text | Qwen3.5 2B, 4B and 9B; Gemma 4 E2B, E4B and 12B; Qwen3.6 35B-A3B (needs 32 GB+ RAM) |
| Image | FLUX.3 Image Klein (6–8 GB GPU, works on 4 GB with offloading); Qwen-Image 2.1 Turbo (10–12 GB GPU) |
| Video | Wan 2.2 5B Turbo: the same model distilled to 4 steps, so clips take a fraction of the time |

Their download links and sizes are verified, and their settings follow stable-diffusion.cpp's and
llama.cpp's documentation, but they have not yet been run on our test PCs. The new text models use
llama.cpp's own memory fitting (`--fit on`), because their designs (Gemma 4's shared and sliding-window
memory, Qwen3.5's hybrid layers) don't suit Featherbox's simple per-layer estimate. Neither family
"thinks" before answering unless asked, so script writing stays fast.

Not added yet:
- **Voice:** no new model works with the current engines. Kokoro v1.0 and Whisper Large v3 Turbo are
  still the newest of their kinds. Newer voices (Kitten TTS 2, OmniVoice, IndicF5 for Indian
  languages) need a new voice engine.
- **Bigger video models** (LTX-2.3/2.5, MiniMax-H3): their main model alone is 10 GB or more, plus a
  12–32B text encoder, which is impractical on 4–8 GB GPUs.
- **LingBot-Video 1.3B:** light, but it expects long structured JSON scene descriptions instead of
  plain prompts.

## Image, Video and Voice tools

Standalone pages for working with one kind of model directly. Everything is saved under
`data\creations\<image|video|voice>\` (the file plus a `.json` with the settings used), so each page keeps
a gallery with Download, "Use these settings again", Delete and Open folder.

| Tool | Input | Options | Speed on an RTX 3050 4 GB |
|---|---|---|---|
| **Image** | A description | Model, shape (portrait / square / landscape), style, 1–4 images, negative prompt, seed | ~40 s per image (Z-Image Turbo) |
| **Video** | A description, optionally a starting picture (upload, or **Animate** from the Image page) | Model, shape, Fast / Best, seed | ~3 min per 2 s clip (Wan 2.2, Fast) |
| **Voice** | Up to 5,000 characters, English or Hindi | Voice (grouped by language), speed | Seconds; runs on the CPU, never queued behind GPU jobs |

Image and Video run as GPU jobs, one at a time, shared with the Studio. Shapes keep about the model's
native pixel count (Z-Image: 576×1024, 768×768, 1024×576; Wan: 480×832, 640×640, 832×480). If another
program is holding the graphics memory, the error names it (e.g. "python.exe in D:\Tools\TTS") instead of
showing raw engine output.

## Transcribe (speech to text)

**Transcribe** turns a file (MP3, WAV, M4A, OGG, FLAC, or a video such as MP4/MKV/MOV) or a microphone recording
into text with timestamps. Click a line to play from there; copy the text or download TXT, SRT or VTT
subtitles. Results are saved in `data\creations\transcript\`.

- **Models** (Models → Speech to text), all from whisper.cpp, quantised:

  | Model | Size | Best for |
  |---|---|---|
  | Whisper Base | 57 MB | Quick drafts of clear English |
  | Whisper Small | 181 MB | Balance; can translate to English |
  | **Whisper Large v3 Turbo** (recommended) | 547 MB | Near-best accuracy, Hindi and Indian languages |
  | Whisper Large v3 | 1 GB | Most accurate, best translation to English |

- **Engines**: `whisper.cpp (CPU)` (9 MB) runs anywhere, in its own queue, so it never waits behind an image or
  video job. On NVIDIA PCs, `whisper.cpp (NVIDIA CUDA)` is far faster. Only the needed files (258 MB) are pulled
  out of the 685 MB release zip with HTTP range requests, and it reuses the CUDA runtime that the llama.cpp
  engine already installed. If the GPU run fails (for example, graphics memory is full), it falls back to the CPU.
- A tiny Silero voice-activity model (1 MB) skips silence, which stops Whisper inventing text in quiet parts.
- Speed for 107 s of speech (Ryzen 7 5800H / RTX 3050 4 GB):

  | | CPU | NVIDIA GPU |
  |---|---|---|
  | Whisper Base | 10 s | — |
  | Whisper Large v3 Turbo | 64 s | **8 s** |

  "Detect automatically" costs one extra pass (about 13 s on the CPU), so picking the language is quicker.

## AI motion (optional video models)

With a Wan video model installed (Models → Video), scenes can move instead of using a slow zoom and pan:

- **Studio → Motion**: *Still pictures*, *AI motion on the first scene* (a moving hook) or
  *AI motion on every scene*.
- **Finished video → scene card**: **Animate** a still scene, **New motion** for a different take, or
  **Make still** to go back. Only that scene is rebuilt.
- **Wan 2.2 TI2V 5B** animates the picture Z-Image painted (image-to-video), so the look stays the same.
  **Wan 2.1 T2V 1.3B** is lighter but makes the clip from the text prompt only.
- How a clip is made: 33 frames at 480×832 (about 2 s), interpolated to 30 fps, upscaled to 1080×1920 and
  lightly sharpened, then turned into a seamless loop that only plays forwards (its last half second
  crossfades into its start), slowed 1.25× and repeated to fill the voice line. Captions are burned in on
  top as usual.
- **Still scenes** get a slow camera move (push in, pull out, pan or drift; six kinds, eased at both ends).
  Frames are drawn with sub-pixel accuracy on all processor cores, so the motion glides instead of
  stepping. Scenes are joined with a 0.25 s crossfade that falls in the pause after each voice line.
- **Clip quality** (Studio → Motion, a global setting):
  - **Fast clips** (default) decode with the 22 MB TAEHV tiny decoder (MIT, `taew2_2` / `taew2_1`).
    Slightly softer detail; the first frame still matches the painted picture.
  - **Best quality** uses the full Wan VAE.
- Speed on an RTX 3050 4 GB (Wan 2.2 5B, 20 steps, ~2 min of animating per clip):

  | | Fast clips | Best quality |
  |---|---|---|
  | Decoding one clip | 1.4 s | ~220 s |
  | Animating one scene of a finished video | **2.6 min** | 7.1 min |
  | 4-scene Short with a moving first scene | ~5 min | 10 min |

  For Best on cards under 10 GB the decoder is told to use 128 px tiles with less overlap up front (the
  default tiles run out of memory and retry, which took twice as long; decoding on the CPU took 37 min).

## Development

```bash
# backend (port 8420)
cd backend && .venv/Scripts/python run.py --no-browser
# frontend with hot reload (port 5173, proxies /api to 8420)
cd frontend && npm run dev
```

The data folder can be moved with the `FEATHERBOX_DATA` environment variable (the old `SRIJAN_DATA`
still works).

Tests use only Python's built-in `unittest` (nothing extra is installed, so nothing extra ships in the
installer, which bundles `backend/.venv`). They run in a throwaway data folder, never your real one, and
GitHub Actions runs them on every push together with a web UI type check and build:

```bash
backend/.venv/Scripts/python -m unittest discover -s tests -t .
```

## License

Featherbox itself is released under the [MIT License](LICENSE). The AI engines and models it downloads
keep their own licenses, listed below.

## Licenses of bundled/downloaded components

| Component | License |
|---|---|
| llama.cpp, stable-diffusion.cpp | MIT |
| Qwen2.5 / Qwen3 / Qwen3.5 / Qwen3.6 models, Gemma 4, Mistral Nemo, Sarvam-M | Apache-2.0 |
| Llama 3.1 / 3.2 | Llama Community License |
| Gemma 3 | Gemma Terms of Use |
| DreamShaper 8, Realistic Vision 6, Counterfeit 2.5, Juggernaut XL | CreativeML OpenRAIL-M |
| DreamShaper XL Lightning | OpenRAIL++ |
| Z-Image Turbo, FLUX.1 schnell, Wan 2.1 / 2.2 (and Wan 2.2 5B Turbo) | Apache-2.0 |
| FLUX.3 Image Klein | FLUX Kommunity License (check before commercial use) |
| Qwen-Image 2.1 Turbo | Qwen Research License (not for commercial use) |
| Kokoro TTS | Apache-2.0 |
| whisper.cpp, Whisper models (OpenAI), Silero VAD | MIT |
| FFmpeg (BtbN GPL build) | GPL |

Check each license before selling the app or using generated content commercially.

## Roadmap

- [x] Regenerate a single scene image or voice line without re-rendering everything
- [x] Background music with auto-ducking (built-in moods + your own tracks)
- [ ] Optional MusicGen model for AI-composed music (needs PyTorch, about 4 GB)
- [ ] Fact-check pass for scripts (small models still slip, especially in Hindi)
- [ ] More recipes: lecture → notes + quiz, product photo → ad, podcast → clips
- [x] One-click Windows installer (no admin, bundled Python, tray launcher, uninstaller)
- [ ] Code-sign the installer (removes the SmartScreen warning)
- [x] Linux (from source; tested on Ubuntu 24.04)
- [ ] Mac version
- [x] Bigger model library with "will it run here?" advice, model choice and your own Hugging Face links
- [x] AI motion with Wan video models (whole video, first scene, or single scenes)
- [ ] Piper voices for more Indian languages
- [x] Standalone tools: image generator, video generator, text-to-speech
- [x] Speech-to-text (whisper.cpp): files, videos and microphone, SRT/VTT subtitles, CPU or CUDA
- [ ] Hugging Face model search inside the Models page
- [x] Update notifications and one-click updates (checksum-verified)
