<p align="center">
  <img src="fastlane/metadata/android/en-US/images/icon.png" width="88" alt="Saturn icon">
</p>

<h1 align="center">Saturn</h1>

<p align="center"><b>Your phone, now with an agent that does the work.</b><br>
Shell, Node, git, and phone hardware tools in a standalone app — no root, no Termux, no backend server.<br><br>
<a href="https://gouravraghuwanshi.github.io/saturn-agent/"><b>Website</b></a> · <a href="../../releases/latest"><b>Download</b></a> · <a href="https://pi.dev"><b>Pi</b></a></p>

<p align="center">
  <img src="docs/media/saturn-demo.gif" width="300" alt="Saturn running a task on Android">
  <br><sub><a href="docs/media/saturn-demo.mp4">Full-quality video</a></sub>
</p>

---

Saturn is an agent that can do anything on your phone, not just code. [Pi](https://pi.dev) runs the agent loop, and Saturn gives it a phone to work on: an on-device Linux userland, phone integrations, and the app around it. Pick a model provider, give it a task, and it edits files, runs commands, builds web apps, or triggers phone actions on your device. Pi extensions and slash commands work the same way they do on desktop.

## Features

- **On-device Linux userland:** Ships Node.js, bash, git, ripgrep, ssh, and built-in utilities (`jq`, `pdftotext`, etc.) without Termux or root, plus an interactive terminal if you want direct shell access.
- **Concurrent tasks:** Each task runs in its own `pi --mode rpc` process with a persistent session you can revisit, branch, or export.
- **Artifacts:** Files created for you (HTML pages, reports, scripts, data) are collected in an Artifacts view for previewing and sharing.
- **Phone APIs:** Termux:API-compatible commands (`termux-torch`, `termux-camera-photo`, `termux-location`, `termux-sensor`, `termux-notification`, `termux-tts-speak`, contacts, etc.) routed through a local, token-protected bridge.
- **Scheduling:** `saturn-schedule` registers Android alarms for one-off timers or cron-style recurring tasks that run even when the app is closed.
- **Browser, GitHub, and SSH:** An in-app browser the agent can inspect and drive, GitHub sign-in for `gh`/`git` workflows, and SSH access to remote machines.
- **Android integration:** Share and drag-and-drop target, notification replies, home-screen widget, quick-settings tile, voice input, AppFunctions, and adaptive layouts for tablets, foldables, and DeX.
- **Flexible models:** Sign in with ChatGPT, Claude, Copilot, and others, or bring your own API key (OpenRouter, Anthropic, OpenAI, etc.).

## Privacy

Saturn has no accounts, ads, analytics, or backend servers. Files, projects, and credentials stay in the app's private storage. Traffic only leaves the device to the AI provider (and any external services like GitHub or SSH) that you configure. See [PRIVACY.md](PRIVACY.md).

## Installation

Download the APK from [Releases](../../releases). Requires **Android 10+** on **arm64-v8a**.

Once installed, Saturn checks for new releases and verifies update APKs against its own signing key before installing.

## Optional: Cross-app UI control

To let the agent read and tap other apps, install the separate [Phone Control](https://github.com/gouravraghuwanshi/phone-control-mcp) MCP server, which uses Android's Accessibility API with an explicit stop button and confirmation prompts for sensitive actions. Saturn itself does not use the Accessibility API.

## How it works

Android blocks executing binaries from writable app storage on `targetSdk 29+`, but allows execution from the APK's native library directory (`nativeLibraryDir`). Saturn bundles Termux-built binaries as `lib*.so` files in `jniLibs` (`useLegacyPackaging = true`) and symlinks them into a `usr/` prefix on startup.

The Jetpack Compose UI communicates with each `pi --mode rpc` child process over JSON stdio, while Termux:API-compatible CLI shims call back into the app over a local, token-authenticated bridge.

## Build from source

Prerequisites: JDK 17, Android SDK (platform 37, NDK r29), and Node.js/npm.

```sh
python3 -I runtime/import_termux.py   # toolchain -> jniLibs + assets (sha256-verified)
runtime/build-pi-bundle.sh            # official Pi from npm -> assets/pi-bundle.zip
./gradlew assembleGithubRelease
```

Two build flavors share the codebase:
- `github`: Full feature set (GitHub Releases / F-Droid).
- `play`: Google Play policy compliant (no contacts permission, no downloaded native Node add-ons).

See [RELEASING.md](RELEASING.md) and [store/PLAY_STORE.md](store/PLAY_STORE.md) for details.

## Contributing

Bug reports, feature ideas, and pull requests are welcome. For bug reports, include what you asked Saturn to do and what happened.

## Thanks

Saturn is built on the work of others:

- [Pi](https://pi.dev) by Earendil Works, the agent harness that runs every task
- [Node.js](https://nodejs.org) and [npm](https://github.com/npm/cli)
- [Termux](https://github.com/termux) packages and terminal view
- Inter and JetBrains Mono fonts

See [THIRD_PARTY.md](THIRD_PARTY.md) for licenses. Saturn is not affiliated with Earendil Works or Termux.

## License

[Apache-2.0](LICENSE) for Saturn's own code. Bundled components retain their respective licenses.
