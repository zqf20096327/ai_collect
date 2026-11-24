<p align="center">
  <a href="https://unimetype.com">
    <img src="./assets/hero-unimetype.png" alt="UnimeType — One keyboard for all your languages, without switching keyboards" width="100%" />
  </a>
</p>

<h1 align="center">UnimeType</h1>

<p align="center">
  <strong>One keyboard for all your languages, without switching keyboards across apps or mid-sentence.</strong><br/>
  Official community portal, package manager reference, and public issue tracker for UnimeType across macOS, Windows, Linux, iOS, Android, and ChromeOS.
</p>

<p align="center">
  <a href="./README.zh-CN.md">简体中文</a> ·
  <a href="https://unimetype.com/download">Download</a> ·
  <a href="https://unimetype.com/docs">Documentation</a> ·
  <a href="https://unimetype.com/bilingual-keyboard">How It Works</a> ·
  <a href="https://github.com/UnimeType/transliteration">Offline Model Toolkit</a> ·
  <a href="https://huggingface.co/UnimeType">Hugging Face Weights</a> ·
  <a href="https://github.com/UnimeType/unimetype/issues">Report an Issue</a>
</p>

---

## Why UnimeType Exists

Most bilingual people use **one native language alongside English** every day, yet traditional input methods force a hidden state machine onto every app switch and every mixed sentence:

- **Design (`Figma` / `Photoshop` / `Blender`)** — Single-key shortcuts (`V`, `R`, `T`, `Space`) get swallowed by floating candidate bars the moment you return from replying to a message.
- **Research (`Overleaf` / `LaTeX` / `Markdown`)** — Commands like `\cite{}`, `\begin{align}`, and half-width math punctuation turn into full-width brackets or phonetic candidates mid-draft.
- **Global Trade & Cross-App Messaging** — Moving between English quotes in `WhatsApp`, `Mail`, or `Excel` and native-script chats in `WeChat`, `LINE`, or `Slack` means guessing which keyboard layout is active before every first keystroke.
- **Gaming (`WASD` / `Shift`)** — Pressing `Shift` to sprint accidentally wakes up an IME candidate window and freezes movement.
- **Engineering (`VS Code` / `Terminal` / `Vim`)** — `Esc` and normal-mode navigation break whenever the OS remembers the wrong per-window input source.

UnimeType separates **typing** from **converting**: your keyboard stays in clean, predictable ASCII at all times, and pressing **Caps Lock** (or tapping **Convert** on mobile) converts phonetic drafts into native script in place while keeping English terms, `@handles`, URLs, file paths, and code untouched.

---

## Supported Languages & Free Browser Converters

Every supported language pairs **one native language with inline English** on a standard QWERTY layout. You can test whole-sentence conversion directly in the browser with no install or sign-up:

| Language Pair | What You Type on English QWERTY | In-Place Result After `Convert` | Browser Converter |
| --- | --- | --- | --- |
| **Chinese + English** (`Pinyin`) | `wo gang push le new build, ming tian kan yi xia metrics` | `我刚 push 了 new build，明天看一下 metrics。` | [Pinyin Converter](https://unimetype.com/tools/pinyin-to-chinese) |
| **Japanese + English** (`Romaji`) | `ashita no design review, Figma no link okuru ne` | `明日の design review、Figma の link 送るね。` | [Romaji Converter](https://unimetype.com/tools/romaji-to-hiragana) |
| **Hindi + English** (`Hinglish`) | `main abhi cab me hoon, 7pm tak main gate ke paas milte hain` | `मैं अभी cab में हूँ, 7pm तक main gate के पास मिलते हैं।` | [Hinglish Converter](https://unimetype.com/tools/english-to-hindi) |
| **Arabic + English** (`Arabizi`) | `7abibi el PDF gahez, ab3ato 3ala WhatsApp?` | `حبيبي ال PDF جاهز، ابعته على WhatsApp؟` | [Arabizi Converter](https://unimetype.com/tools/arabizi-to-arabic) |
| **Russian + English** (`Translit`) | `ya popravil maket v Figma i skinul PDF v Slack` | `я поправил макет в Figma и скинул PDF в Slack.` | [Translit Converter](https://unimetype.com/tools/translit-to-cyrillic) |

Additional supported languages & no-login browser tools: **[Vietnamese](https://unimetype.com/tools/vietnamese-tone-converter)** (`Quốc ngữ` tones), **[Greek](https://unimetype.com/tools/greeklish-to-greek)** (`Greeklish`), **[Spanish](https://unimetype.com/tools/spanish-accent-converter)**, **[French](https://unimetype.com/tools/french-accent-converter)**, **[Portuguese](https://unimetype.com/tools/portuguese-accent-converter)**, **[German](https://unimetype.com/tools/german-umlaut-converter)**, and **[Italian](https://unimetype.com/tools/italian-accent-converter)**.

---

## Download & Package Managers

Always verify or download the latest signed installers from **[unimetype.com/download](https://unimetype.com/download)** or install via official platform stores and package managers:

| Platform | Official Store / Direct Installer | CLI Package Manager / Repository |
| --- | --- | --- |
| **macOS** (`14.0+`, Apple Silicon & Intel) | [Download Signed `.dmg`](https://unimetype.com/download#macos) | `brew install --cask losdwind/tap/unimetype` |
| **Windows** (`11`, `x64` & `ARM64`) | [Microsoft Store](https://apps.microsoft.com/detail/xp9mnldwmc0xz3) · [Signed `.exe`](https://unimetype.com/download#windows) | `winget install xp9mnldwmc0xz3` |
| **Linux** (`X11` & `Wayland`, `IBus`) | [Download `.deb` / `.rpm`](https://unimetype.com/download#linux) | [APT Repo](https://downloads.unimetype.com/apt/dists/stable/Release) · [DNF `.repo`](https://downloads.unimetype.com/rpm/unimetype.repo) · [Arch `PKGBUILD`](./packaging/arch/PKGBUILD) |
| **iOS & iPadOS** (`17.0+`) | [Apple App Store](https://apps.apple.com/app/id6478013435) | App Store auto-update |
| **Android** (`8.0+`) | [Google Play](https://play.google.com/store/apps/details?id=com.figurich.unimetype.android) · [Signed `.apk`](https://unimetype.com/download#android) | Google Play / Direct signed APK |
| **ChromeOS** (`ChromeOS` & `Crostini`) | [Chrome Web Store](https://chromewebstore.google.com/detail/unimetype/fpghahkgnabhebiegilekfbkdnafhjgc) · [`.zip`](https://unimetype.com/download#chromeos) | Chrome Web Store auto-update |

---

## Open-Weight Offline Models (`Transliteration 2.0` · `v2.6`)

Desktop clients (`macOS`, `Windows`, `Linux`) support **100% offline on-device conversion** through any local OpenAI-compatible runtime (`LM Studio`, `Ollama`, `mlx_lm.server`, or `llama-server`) with zero network requests.

- **Local Inference Toolkit & Protocol Spec**: **[`UnimeType/transliteration`](https://github.com/UnimeType/transliteration)** — Official `unimetype-convert-short-v3` compact JSON protocol, protected-span restoration, one-command `Ollama` / `LM Studio` / Apple Silicon `MLX` / `llama.cpp` launchers, and the reproducible 60-case `Smoke-60` benchmark.
- **Apache-2.0 Weights on Hugging Face (`12` Languages / `13` Modes)**:
  - [`UnimeType/Transliteration-2.0-0.8B`](https://huggingface.co/UnimeType/Transliteration-2.0-0.8B) · [`Safetensors`](https://huggingface.co/UnimeType/Transliteration-2.0-0.8B-Safetensors) · [`GGUF`](https://huggingface.co/UnimeType/Transliteration-2.0-0.8B-GGUF)
  - [`UnimeType/Transliteration-2.0-4B`](https://huggingface.co/UnimeType/Transliteration-2.0-4B) · [`Safetensors`](https://huggingface.co/UnimeType/Transliteration-2.0-4B-Safetensors) · [`GGUF`](https://huggingface.co/UnimeType/Transliteration-2.0-4B-GGUF)
  - [`UnimeType/Transliteration-2.0-9B`](https://huggingface.co/UnimeType/Transliteration-2.0-9B) · [`Safetensors`](https://huggingface.co/UnimeType/Transliteration-2.0-9B-Safetensors) · [`GGUF`](https://huggingface.co/UnimeType/Transliteration-2.0-9B-GGUF)
- **Interactive Browser Playground**: **[`UnimeType/Transliteration-Playground`](https://huggingface.co/spaces/UnimeType/Transliteration-Playground)**

---

## How UnimeType Compares to Traditional IMEs

- **[UnimeType vs. Google Input Tools](https://unimetype.com/vs/google-input-tools)** — Native desktop and mobile input method with whole-sentence context instead of Chrome-only word-by-word spacebar replacement.
- **[UnimeType vs. Rime (`Squirrel` / `Weasel`)](https://unimetype.com/vs/rime)** — Zero preedit candidate bar eating single-key shortcuts in Figma, Overleaf, or Vim, with optional local GGUF / MLX offline inference.
- **[UnimeType vs. Google Japanese Input (`Mozc`)](https://unimetype.com/vs/google-japanese-input)** — Type Japanese + English on standard US ANSI keyboards without Kana/Eisu mode toggles or accidental full-width ASCII (`ａｂｃ`).
- **[UnimeType vs. Gboard](https://unimetype.com/vs/gboard)** & **[vs. Yamli](https://unimetype.com/vs/yamli)** — Stay on one QWERTY layout across WhatsApp, WeChat, LINE, and Slack without cycling the Globe key across non-Latin scripts.

---

## Issue Tracker & Host Compatibility Reports

This repository serves as the public issue tracker for UnimeType clients:

- **[Bug Report](https://github.com/UnimeType/unimetype/issues/new?template=bug_report.yml)** — Crashes, UI glitches, conversion errors, or installer issues.
- **[App / Editor / Game Compatibility Report](https://github.com/UnimeType/unimetype/issues/new?template=app_compatibility.yml)** — Report any desktop app, web editor, terminal, or game where in-place selection replacement, cursor positioning, or shortcut passthrough misbehaves.
- **[Feature or Language Request](https://github.com/UnimeType/unimetype/issues/new?template=feature_request.yml)** — Suggest workflow improvements, shortcuts, or phonetic schemes.

---

## Privacy & Security

- **Normal typing never leaves your device.** Ordinary ASCII keystrokes stay 100% local (`0 Bytes` uploaded) until you explicitly trigger **Convert**, **Polish**, or **Explain** ([Private AI Keyboard Architecture](https://unimetype.com/private-ai-keyboard)).
- **Zero-network offline mode.** Point UnimeType Desktop at `http://127.0.0.1:1234/v1` (`LM Studio`) or `http://127.0.0.1:11434/v1` (`Ollama`) to run every conversion locally on your own hardware.
- To report a security vulnerability privately, see **[`SECURITY.md`](./SECURITY.md)** or email **[security@unimetype.com](mailto:security@unimetype.com)**.
