<div align="center">
  <img src="docs/assets/logo.png" alt="Antigravity for Android" width="72" />
  <h1>Antigravity for Android</h1>
  <p>
    Run the <strong>Antigravity AI coding agent on Android</strong> (ARM64 APK).<br />
    Antigravity <strong>v2.35.0</strong> (Linux ARM64) runs natively on Android Bionic — no PRoot or chroot.
  </p>
  <p>
    <a href="https://github.com/Comzvy/antigravity-arm64-android/releases/latest"><img src="https://img.shields.io/github/v/release/Comzvy/antigravity-arm64-android?style=flat-square&color=38bdf8" alt="Release" /></a>
    <a href="https://github.com/Comzvy/antigravity-arm64-android/actions/workflows/build-and-release.yml"><img src="https://img.shields.io/github/actions/workflow/status/Comzvy/antigravity-arm64-android/build-and-release.yml?branch=main&style=flat-square&label=CI" alt="CI" /></a>
    <img src="https://img.shields.io/badge/Android-7.0%2B-3DDC84?style=flat-square" alt="Android 7.0+" />
    <img src="https://img.shields.io/badge/ARM64-v8.0%2B-6366F1?style=flat-square" alt="ARM64 v8.0+" />
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache--2.0-F59E0B?style=flat-square" alt="License" /></a>
  </p>
  <p>
    <strong><a href="https://github.com/Comzvy/antigravity-arm64-android/releases/latest">Download APK</a></strong>
    &nbsp;·&nbsp;
    <a href="RELEASE_NOTES.md">Release Notes</a>
    &nbsp;·&nbsp;
    <a href="#quick-start">Quick Start</a>
    &nbsp;·&nbsp;
    <a href="#build-from-source">Build</a>
  </p>
</div>

<br />

<p align="center">
  <img alt="Antigravity for Android interface" src="docs/assets/hero_dark.png" width="100%" />
</p>

## Features

- **Native Bionic core** — runs Antigravity v2.35.0 (`language_server`) directly on Android ARM64 with `liblse_compat.so` (ARMv8.0-A+ LSE/SIMD emulation, no PRoot/chroot).
- **Multi-provider AI (BYOK)** — Gemini, OpenAI, Anthropic Claude, OpenRouter, Groq, DeepSeek, or any OpenAI/Anthropic-compatible endpoint.
- **Skills & Plugins Catalogue** — built-in catalogue (`10` plugins, `23` skills) with one-tap install and uninstall under **Settings ➔ Skills & Plugins**.
- **Touch & Desktop UX** — drag conversations into any folder (Workspaces/Projects, Groups, Pinned), responsive bottom sheets without IME focus conflicts, Desktop Mode toggle, dark/light theme sync, wake lock, file picker, and persistent Stop notification.
- **Voice mode** — on-device speech recognition, cloud transcription (Whisper / Gemini), and native text-to-speech.
- **Built-in terminal** — PTY bash shell, `pkg` package manager, and `agy-daemon` background task scheduler.
- **Shizuku integration** — optional elevated ADB shell (`rish`) and status bar notifications (`agy-notify`).

## Quick Start

1. Download `antigravity.apk` from the [latest release](https://github.com/Comzvy/antigravity-arm64-android/releases/latest) (Android 7.0+ ARM64; installs cleanly over existing `v2.x` builds).
2. Grant **All Files Access**, and **Microphone** if using voice mode (optional: Shizuku).
3. Install CLI tools inside the built-in terminal:
   ```bash
   pkg update && pkg install git python nodejs bash
   ```
4. Configure API keys under **Settings ➔ AI Models & API Keys**, or browse extensions under **Settings ➔ Skills & Plugins**.

## Build from Source

```bash
bash build.sh            # dist/antigravity.apk (production, com.agy, port 45157)
bash build.sh --dev      # dist/antigravity-dev.apk
bash test_all_modules.sh # full modular & live core test suite
```

## Structure

| Directory | Purpose |
| :--- | :--- |
| [`app/`](app/) | Android host — Activities, WebView bridge, AI router, `CatalogueManager`, foreground service |
| [`web/`](web/) | Workbench UI bundle and modular JS patches |
| [`modules/`](modules/) | APK builder, runtime packager, ELF binary patchers, standalone runner |
| [`env/`](env/) | Bionic userspace bootstrap, `pkg` manager, `agy-daemon` |
| [`config/`](config/) | Version, build, and runtime constants |
| [`docs/`](docs/) | Logo and screenshot assets |

---

<p align="center">
  <sub>Maintained by <a href="https://github.com/Comzvy">Comzvy</a> · Licensed under <a href="LICENSE">Apache-2.0</a></sub>
</p>
