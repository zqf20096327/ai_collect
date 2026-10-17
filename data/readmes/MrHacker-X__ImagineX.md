<div align="center">

# ⃤ I M A G I N E X ⃤

### *AI on your Telegram - ask anything, generate any image, one bot.*

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Telegram](https://img.shields.io/badge/Platform-Telegram-2CA5E0?style=flat-square&logo=telegram&logoColor=white)
![OpenAI](https://img.shields.io/badge/AI-OpenAI%20API-412991?style=flat-square&logo=openai&logoColor=white)
![Stars](https://img.shields.io/github/stars/MrHacker-X/ImagineX?style=flat-square&color=orange)
![Forks](https://img.shields.io/github/forks/MrHacker-X/ImagineX?style=flat-square&color=cyan)

</div>

---

## 📋 Table of Contents

- [🎯 Why ImagineX?](#-why-imaginex)
- [🧭 What It Does](#-what-it-does)
- [🚀 Quick Start](#-quick-start)
- [📦 Installation](#-installation)
- [✨ Features](#-features)
- [⌨️ Usage](#%EF%B8%8F-usage)
- [⚙️ Configuration](#%EF%B8%8F-configuration)
- [🧰 Tech Stack](#-tech-stack)
- [⚠️ Disclaimer](#%EF%B8%8F-disclaimer)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [👨‍💻 Developer](#-developer)

---

## 🎯 Why ImagineX?

> Deploying an AI assistant on Telegram shouldn't require a framework, a database, or a weekend of reading docs. **ImagineX is two handlers and a config file**: clone it, drop in your OpenAI key and bot token, and you have a working `/ask`-anything `/gen`-any-image bot in under two minutes.
>
> **v2.0 keeps the simplicity but modernizes the engine.** The old release was built on python-telegram-bot 13.x and the legacy OpenAI SDK - both deprecated and no longer compatible with current API endpoints. Every layer is now upgraded: async handlers on python-telegram-bot 21+, OpenAI SDK v1+, and Chat Completions (`gpt-4o-mini` by default) instead of the retired completion endpoint.

---

## 🧭 What It Does

| # | Command | What it does |
|---|---------|-------------|
| 1️⃣ | `/ask <question>` | Sends your question to an OpenAI chat model and replies with the answer |
| 2️⃣ | `/gen <prompt>` | Turns a text prompt into an image via the OpenAI images API and sends it as a photo |

**What this bot is NOT:** it is **not** a commercial service, **not** a group-assistant platform, and **not** meant to be resold. It is a personal AI bot for your own Telegram account - see the [Disclaimer](#%EF%B8%8F-disclaimer).

---

## 🚀 Quick Start

```bash
git clone https://github.com/MrHacker-X/ImagineX.git
cd ImagineX
pip install -r requirements.txt
python imaginex.py                # after filling config.py
```

<details>
<summary><b>🔑 Where do I get the credentials?</b></summary>

| Credential | Where to get it |
|------------|-----------------|
| Telegram bot token | Message [@BotFather](https://telegram.me/BotFather) on Telegram → `/newbot` |
| OpenAI API key | [platform.openai.com/api-keys](https://platform.openai.com/api-keys) |

</details>

---

## 📦 Installation

```bash
# 1. clone
git clone https://github.com/MrHacker-X/ImagineX.git
cd ImagineX

# 2. install dependencies
pip install -r requirements.txt

# 3. configure (edit config.py, or export env vars)
nano config.py          # put your OPENAI_API_KEY and BOT_TOKEN here

# 4. run
python imaginex.py
```

### Supported Systems

| OS | Status | Notes |
|----|--------|-------|
| 🐧 Linux | ✅ Fully supported | Any distro with Python 3.8+ |
| 📱 Termux (Android) | ✅ Fully supported | `pkg install python`, then the steps above |
| 🪟 Windows | ✅ Fully supported | Python from python.org, then the steps above |
| 🍎 macOS | ✅ Fully supported | `brew install python`, then the steps above |

> 💡 The bot fails fast with a clear message if a credential is missing - it will never die on an obscure stack trace.

---

## ✨ Features

| | Feature | Description |
|---|---------|-------------|
| 💬 | **Chat Completions** | `/ask` runs on OpenAI chat models (`gpt-4o-mini` default, configurable) |
| 🎨 | **Image generation** | `/gen` returns a DALL·E image as a Telegram photo - no links to open |
| ⚡ | **Fully async** | python-telegram-bot 21+ event loop; the bot stays responsive during generation |
| 🏎️ | **Live progress** | "typing…" / "uploading photo…" chat actions while the AI works |
| 🧱 | **Error containment** | A failed API call replies with an apology message - it never kills the process |
| 🔧 | **Single config file** | All credentials and tunables in one place, env-var override supported |
| 🩹 | **Fail-fast validation** | Missing key or token → one clear error line at startup, not a crash mid-chat |
| 🪶 | **Minimal dependencies** | 4 packages: `python-telegram-bot`, `openai`, `requests`, `colorama` |

<details>
<summary><b>🔄 What changed from the original v1.x?</b></summary>

| v1.x (old) | v2.0 (now) |
|------------|------------|
| python-telegram-bot 13.x (deprecated, broken on modern Python/APIs) | **python-telegram-bot 21+**, fully async |
| openai 0.28 SDK (removed from PyPI support) | **openai SDK v1+** |
| `Completion` API + `gpt-3.5-turbo-instruct` (endpoint retired) | **Chat Completions** (`gpt-4o-mini` default) |
| Hand-rolled `requests` POST to the images API | **Native images API** through the SDK |
| Image download broke on modern DALL·E URLs (extension parsing) | Downloads anything, strips the temp file after sending |
| Blocking calls froze the bot while waiting on OpenAI | Blocking work runs off the event loop via `asyncio.to_thread` |
| Silent crashes with bare `print` errors | Structured logging + global error handler |
| Credentials only via config.py | config.py **or** environment variables (env wins) |

</details>

---

## ⌨️ Usage

Open Telegram, find your bot, and send:

| Command | Example | Result |
|---------|---------|--------|
| `/start` | `/start` | Welcome message |
| `/help` | `/help` | List of available commands |
| `/ask` | `/ask Explain quantum tunneling simply` | AI answer to your question |
| `/gen` | `/gen a cat astronaut riding a palm tree` | AI-generated image as a photo |
| anything else | `/foo` | Friendly "invalid command" hint |

### From the command line

```bash
python imaginex.py      # starts long-polling; Ctrl+C to stop
```

---

## ⚙️ Configuration

Everything lives in [`config.py`](config.py) - and every setting can be overridden from the shell:

| Setting | Env var | Default | Description |
|---------|---------|---------|-------------|
| OpenAI key | `OPENAI_API_KEY` | *(required)* | Your OpenAI API key |
| Bot token | `BOT_TOKEN` | *(required)* | Token from @BotFather |
| Chat model | `CHAT_MODEL` | `gpt-4o-mini` | Model used by `/ask` |
| Image size | `IMAGE_SIZE` | `512x512` | Size used by `/gen` (256x256 / 512x512 / 1024x1024) |
| Max tokens | `MAX_TOKENS` | `1024` | Longest `/ask` response |

```bash
# either edit config.py, or:
export OPENAI_API_KEY="sk-..."
export BOT_TOKEN="123456:AA-..."
export CHAT_MODEL="gpt-4o"
```

> 🔒 Environment variables always win over config.py - useful for keeping secrets out of a cloned repo.

---

## 🧰 Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3.8+ |
| Bot framework | `python-telegram-bot` 21+ (async) |
| AI | `openai` SDK v1+ — Chat Completions + Images API |
| HTTP | `requests` (connectivity check, image download) |
| UI | `colorama` terminal output |

---

## ⚠️ Disclaimer

> ### Read this before using ImagineX.
>
> 1. **Personal use only.** ImagineX is designed for personal use and exploration. It is not intended for commercial deployment or group settings - bots answering for many users can burn API credits fast and breach OpenAI's usage policies.
> 2. **Your credentials, your responsibility.** The bot uses *your* OpenAI key: every `/ask` and `/gen` is billed to your account. Keep your API key and bot token out of public repos, screenshots, and shared config files.
> 3. **API usage policies apply.** Your use of OpenAI's models through this bot is additionally governed by OpenAI's [usage policies](https://openai.com/policies). You are responsible for the prompts you send.
> 4. **No warranty.** ImagineX is provided "as is", with no warranty of any kind. The author is **not liable** for any misuse, cost, or damage resulting from the use or abuse of this bot.

---

## 🤝 Contributing

Contributions are welcome!

```bash
# 1. fork it
# 2. create your branch
git checkout -b feature/amazing-feature
# 3. commit
git commit -m "Add amazing feature"
# 4. push
git push origin feature/amazing-feature
# 5. open a Pull Request
```

Ideas worth exploring: streaming answers (edit-in-place messages), per-chat conversation memory, a `/settings` command, Dockerfile for one-line deployment.

---

## 📜 License

ImagineX is the original project by MrHacker-X - see the [`LICENSE`](https://github.com/MrHacker-X/ImagineX) file in the upstream repository for details.

---

## 👨‍💻 Developer

| | |
|---|---|
| **Dev** | MrHacker-X |
| **GitHub** | [github.com/MrHacker-X](https://github.com/MrHacker-X) |
| **Email** | [contact@vritrasec.com](mailto:contact@vritrasec.com) |
| **Website** | [vritrasec.com](https://vritrasec.com) |
| **Network** | [link.vritrasec.com](https://link.vritrasec.com) |

---

<div align="center">

### ⭐ Star the repo if ImagineX put AI in your pocket ⭐

*Built by MrHacker-X - ask responsibly, generate responsibly.*

</div>
