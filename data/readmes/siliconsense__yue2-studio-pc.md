# YuE2 Studio for Windows

Create songs from lyrics and covers from your recordings on your NVIDIA GPU.
Audio and lyrics are processed locally. Includes a melody editor, MP3/FLAC
export and an optional local assistant for lyrics and style.

[Русский](README.ru.md) · [Download](https://github.com/siliconsense/yue2-studio-pc/releases/latest)

![The studio](docs/studio.jpg)

## New in 1.3.1

- Updated ComfyUI to 0.42.1 with faster YuE2 generation code.
- Existing installations update the engine automatically and retain downloaded models.
- Dependency updates preserve a working CUDA setup.

The music model and generation settings are unchanged. Tested on Windows;
exact speed gains depend on the PC and input.

## Install

Requires Windows 10/11, an NVIDIA GPU with at least 6 GB VRAM, Git for Windows
and about 25 GB of free disk space. The first run downloads the runtime and models.

1. Download and unpack the ZIP, for example into `C:\SiliconSense`.
2. Open its `studio` folder and run `start.bat`.
3. Wait for installation. The interface opens in your browser.

For Git, use [git-scm.com](https://git-scm.com/download/win).
Close the console to stop the studio. Results are saved in `songs`.

## Update

Close the studio and its console. Back up your installation. Copy **all files
from the new ZIP's `studio` folder** over your existing studio, replacing files.
Keep `engine`, `.venv`, `tools` and `songs`. Run `start.bat`, then press Ctrl+F5
in the browser. The header should show **v1.3.1**.

The first start updates the engine and dependencies. If engine source files
have local edits, the update stops and reports them instead of discarding them.

## Songs and covers

Enter a style and lyrics to create a song. For a cover, upload a recording,
transcribe its melody and chords, then generate with your lyrics. Leave style
strength off to follow the transcription. The optional lyric-fitting button
changes the melody; use it only when that is intended.

![Cover controls](docs/cover.jpg)

The duration setting is a maximum; a song can end earlier. Long generations
need more memory. The interface supports Russian and English.

The **Idea → song** tab drafts lyrics and style locally. Preview and edit the
draft before applying it. Models download separately on first use.
[Assistant instructions](docs/QWEN-EN.txt).

If startup fails, run `check.bat` and include its output in a
[bug report](https://github.com/siliconsense/yue2-studio-pc/issues).

## Licences

Studio code: [MIT](LICENSE). Model weights are downloaded separately and use
other licences, including non-commercial restrictions: [MODEL-LICENCE.md](MODEL-LICENCE.md).
