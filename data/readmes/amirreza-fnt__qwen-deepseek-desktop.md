<div align="center">

# Qwen & DeepSeek Desktop

**A free, open-source desktop AI coding assistant for Windows — chat with Qwen and DeepSeek in one app, stream full code in the chat, and let the model edit your project with reviewed diffs.**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)
![PySide6 / Qt 6](https://img.shields.io/badge/PySide6-Qt%206-41cd52.svg)
![Platform: Windows](https://img.shields.io/badge/platform-Windows%2010%2F11-0078d6.svg)
![Languages: English | فارسی](https://img.shields.io/badge/UI-English%20%7C%20%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-purple.svg)

**English** · [فارسی](README.fa.md)

<img src="docs/screenshots/en-dark.png" alt="Qwen & DeepSeek Desktop – dark theme" width="860">

</div>

> **Unofficial project.** Not affiliated with, endorsed by or sponsored by DeepSeek, Alibaba Cloud or Qwen. It talks to the *web* versions of these services using **your own account's web session**. Please read the [disclaimer](#disclaimer).

## Why?

The web chats of Qwen and DeepSeek are great at code, but copying code back and forth into your editor is slow. This app puts both models in one native desktop window and adds what a coding assistant needs: full code streamed line by line inside the chat, a **Project mode** where the model proposes file changes that you review as diffs, and **agent tools** (read/search files, run commands, download, call APIs) that only run with your approval.

## Features

- 🤖 **Qwen + DeepSeek in one desktop app** – pick the service and model per chat; the Qwen model list can be refreshed from the site in Settings.
- 🌐 **Embedded browser login** – sign in to chat.qwen.ai once in a built-in browser (QtWebEngine). You complete any login or verification yourself; the session stays in a local profile.
- ⚡ **Streaming code in the chat** – long replies (tens of thousands of characters) stream smoothly, with syntax highlighting and one-click *Copy code*.
- 📁 **Project mode with reviewed diffs** – the model proposes whole files, SEARCH/REPLACE edits or deletions; you see a unified or side-by-side diff and press **Apply**. Every write is backed up and can be undone.
- 🛠️ **Agent tools with approval** – folder tree, find, grep, read files and inspect images run automatically *inside the project folder*; terminal commands (PowerShell/cmd), downloads and external HTTP requests show a card and run only when you click **Run**.
- ✂️ **Token-efficient edit tools** – move/copy line ranges between files, replace lines, regex search-and-replace across files, rename/move paths with best-effort import fixes (JS/TS, CSS, HTML, PHP, C/C++, Python, Java, Go) and apply unified patches – without the model retyping code.
- 🎨 **Light & dark themes** with the Vazirmatn font.
- 🌍 **Bilingual UI: English & فارسی** – full RTL layout for Persian, LTR for English; follows your system language by default.
- 🔐 **Privacy-minded** – tokens live in Windows Credential Manager, logs are redacted (no tokens, cookies, emails or message text), chat history stays on your PC.

## Screenshots

| English · Light | فارسی · Dark |
|---|---|
| <img src="docs/screenshots/en-light.png" width="420"> | <img src="docs/screenshots/fa-dark.png" width="420"> |
| **Project mode – review the diff before writing** | **Agent tools – commands need your approval** |
| <img src="docs/screenshots/en-project-review.png" width="420"> | <img src="docs/screenshots/en-agent-tools-dark.png" width="420"> |
| **Side-by-side diff** | **فارسی · Project mode** |
| <img src="docs/screenshots/en-project-side-by-side.png" width="420"> | <img src="docs/screenshots/fa-project-review.png" width="420"> |

## Install

### Option 1 – Windows build (no Python needed)

Download the latest zip from [**Releases**](https://github.com/amirreza-fnt/qwen-deepseek-desktop/releases), extract the **whole folder**, and run `DeepSeekDesktop-Stable.exe`.

### Option 2 – From source (pip)

Requires Python 3.11+ (Windows 10/11 recommended; the UI also runs on Linux for development).

```bash
git clone https://github.com/amirreza-fnt/qwen-deepseek-desktop.git
cd qwen-deepseek-desktop
python -m venv .venv
.venv\Scripts\activate          # Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

### Option 3 – Build your own .exe

```bat
build.bat
```

This creates a venv, installs the requirements and runs PyInstaller. Output: `dist\DeepSeekDesktop-Stable\DeepSeekDesktop-Stable.exe` (copy the entire folder; it is ~450 MB because it bundles QtWebEngine).

## Usage

1. **Qwen (recommended):** open *Settings → Services*, choose **Qwen** with the **Built-in browser** connection, click *Sign in / verify Qwen in the built-in browser*, sign in to your own account and press **Continue**. Qwen may be region-restricted; use it only where it is available to you.
2. **DeepSeek:** paste your own web session token in *Settings → DeepSeek* (see [docs/TECHNICAL_NOTES.md](docs/TECHNICAL_NOTES.md)). Never enter your password.
3. Type a message – **Enter** sends, **Shift+Enter** adds a new line.
4. **Project mode:** click **Project**, choose a folder, tick files or mention them with `@file`. Ask for a change, review it under *Proposed changes* and press **Apply** (or **Undo last changes**).
5. **Agent tools:** keep *Agent tools* ticked in the Project panel. Read-only look-ups run automatically; commands, downloads and external requests wait for **✔ Run** / **✖ Reject**.
6. **Language:** *Settings → Appearance → Language* (System default / English / فارسی). Restart to apply. You can also start with `python main.py --lang en`.

## FAQ

**Is it free?** The app is free and MIT-licensed. It uses the free web chat of each service with your own account, so that service's limits and terms apply.

**Does it bypass captchas or rate limits?** No. If the site asks for verification, you complete it yourself in the built-in browser. The app never solves captchas, forges anti-bot signatures or exports cookies.

**Is this the official Qwen/DeepSeek app?** No. It is an independent, unofficial client. The private web APIs can change at any time and break things.

**Where is my data stored?** Chats: `%LOCALAPPDATA%\DeepSeekDesktop\history.sqlite3` (unencrypted). Tokens: Windows Credential Manager. Built-in browser profile: `%LOCALAPPDATA%\DeepSeekDesktop\qwen-web`.

**Can the model delete my files or run anything it wants?** No. File changes are proposals until you press *Apply* (with backups and undo), paths are confined to the project folder, and commands/downloads/external requests require a click on *Run*.

**Why is the build so big?** It bundles Qt WebEngine (Chromium) for the built-in browser.

**Linux/macOS?** The code is cross-platform Qt and the test suite runs on Ubuntu, but token storage and packaging target Windows. Contributions welcome!

## Disclaimer

This is an **unofficial**, community project. It is **not affiliated with, endorsed by or sponsored by DeepSeek, Alibaba Cloud / Alibaba Group or the Qwen team**; all product names and trademarks belong to their owners and are used only to describe compatibility. The app uses the web sessions of **your own account** through private, undocumented interfaces that may change or stop working at any time. You are responsible for complying with each service's **Terms of Service** and the laws of your country. The app does **not** bypass captchas, paywalls, rate limits or regional restrictions. Provided "as is", without warranty – see [LICENSE](LICENSE).

## Contributing

Issues and PRs are welcome – see [CONTRIBUTING.md](CONTRIBUTING.md). Translations live in `app/i18n_en.py`; the tests make sure every string is translated.

## License

[MIT](LICENSE) © amirreza-fnt. Bundled: Vazirmatn font (SIL OFL 1.1, `app/assets/fonts/OFL.txt`), DeepSeek PoW WASM solver from [deepseek4free](https://github.com/xtekky/deepseek4free) (MIT, `dsk/LICENSE`).

---

⭐ If this app saves you time, a star helps others find it.
