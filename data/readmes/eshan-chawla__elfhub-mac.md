<p align="center">
  <img src="brand/elfhub-icon-1024.png" alt="elfhub" width="112">
</p>

<h1 align="center">elfhub</h1>

<p align="center"><b>AI agents that live on your Mac — they see your screen, talk with you, point at what matters, and act when you ask.</b></p>

<p align="center">
  <a href="https://github.com/eshan-chawla/elfhub-mac/releases/latest/download/elfhub.dmg"><img src="https://img.shields.io/badge/Download_for_macOS-000000?style=for-the-badge&logo=apple&logoColor=white" alt="Download elfhub for macOS" height="36"></a>
</p>

<p align="center"><sub>Public beta · macOS 14.2 or later on Apple silicon (M1 or newer) · free and open source (AGPL-3.0) · signed and notarized by Apple · <a href="https://github.com/eshan-chawla/elfhub-mac/releases">all releases</a> · <a href="https://discord.gg/ZGVzhv4ggS">Discord</a></sub></p>

---

Hold **Control + Option**, ask about whatever is on your screen, and let go. Your **Elf** — an AI agent you name and shape — answers out loud, points right at the button you need, circles what matters, writes the steps into a notepad, and, if you let it, does the clicking and typing for you, one checked step at a time.

elfhub is **desktop-first and bring-your-own-key**. There is no elfhub server, account or analytics: you pick the models (your ChatGPT plan, a cloud API with your own key, or models running on your Mac), and everything you say, type and save stays between you, your Mac and the services you chose.

## What elfhub can do

### Talk, and be heard

- **Push-to-talk anywhere.** Hold the shortcut (`Control + Option` by default, or pick your own), speak, let go. Or just type — every question, spoken or typed, lands in the same chat.
- **Draw while you talk.** With the shortcut held, drag the mouse to circle or underline what you mean. Your blue marks go to the model on the screenshot.
- **Answers you can hear.** Replies stream as text and are spoken sentence by sentence — in the most natural Apple voice on your Mac, a natural voice that runs on your Mac (Kokoro and others), ElevenLabs, or any OpenAI-compatible voice. Optional **live captions** follow the voice word by word.
- **Stop anything, instantly.** Esc stops listening, thinking, talking and acting. During a screen task you can also just say "stop".

### See and show

- **It sees what you see — when you ask.** A screenshot of the display under your mouse is taken only when you talk or send a message.
- **Points and annotates.** A pointer appears right on the element it means; highlights, circles, arrows, underlines and notes are drawn on screen in the Elf's orange, on any monitor.
- **Writes it down.** Steps, commands and code go into a floating notepad, line by line as it talks — selectable, copyable as text or Markdown, and saved with the chat.

### Act on your Mac — with your say-so

- **Real computer use, step by step.** With action mode on, your Elf clicks, types, scrolls, presses shortcuts, opens apps and websites — taking a fresh look at the screen after every step, reading the window's controls through Accessibility, and waiting for pages, downloads or builds to finish instead of guessing.
- **You choose how much it asks.** *Ask first* (a popup before each new task and each new app), *Auto* (asks only before sending, deleting, buying or anything else that can't be undone), or *Allow all* for when you're watching (never remembered after you quit). Pick 15 to 250 steps per task.
- **Guardrails that don't move.** Only your own words count as permission — never text on the screen. Passwords, secure fields, password managers and private websites (banks, payment pages, patient portals) are always your step. Quit, log out, delete and force-quit shortcuts always ask. Touching the mouse or keyboard takes over at once, and every decision is written to a local action log.

### A team of Elfs

- **Your main Elf runs the show.** It keeps a **memory** of you and of what you've talked about (`user.md`), which you can read, edit and undo any time.
- **Add more Elfs** — your own, or the Researcher and Writer starters. Talk to one by name ("Juniper, …") or pick it in the chat box; each has its own chat, voice, model, instructions and skills.
- **Background tasks.** Hand an Elf something long and keep working. It reports back when it's done, asks if it's stuck, and can ask to borrow the screen — only with your yes.
- **Skills, files and folders.** Elfs keep working notes and files in their own folder, learn skills when you ask (the agentskills.io `SKILL.md` layout, so Hermes-style skills drop right in), and can work in folders you grant them. Every change they make is listed with **Undo**.
- **Web search** for Elfs you allow: DuckDuckGo by default, or Brave, Tavily, Exa, Firecrawl, your own SearXNG — or Claude's own web search.
- **Share an Elf** as a `.elf` file: its personality, skills and files — never your keys or folder access.

### Chat, history and costs

- **Every chat saved on your Mac**, searchable, renamable, named for you after the first reply (optional), with a fresh chat after a quiet half hour.
- **Screenshots in context** (optional): see the screenshot each question sent, with a Before / After switch for your drawing and the Elf's marks.
- **Usage and cost**: tokens and an estimated cost per model and kind of work, kept only on your Mac.
- **Built to stay affordable on long sessions**: prompt caching, a trimmed history, and only the newest screenshots of a long screen run are sent.

## Your models, your choice

| Layer | Options |
|-------|---------|
| **Speech-to-text** | Apple on-device recognition (default), on-device models you download (Whisper, Parakeet and more, run with MLX), AssemblyAI, or any OpenAI-compatible endpoint (OpenAI, Groq, a local faster-whisper server) |
| **Language model** | **Continue with ChatGPT** (uses your ChatGPT plan, no key — with a fallback model for when the plan's limit is reached) · Anthropic, OpenAI, Google Gemini, OpenRouter, Mistral, xAI, Groq, DeepSeek, Together AI with your key · Ollama, LM Studio or llama.cpp on your Mac · any OpenAI-compatible endpoint |
| **Voice** | Apple voices (default), natural voices that run on your Mac (Kokoro and more), ElevenLabs, any OpenAI-compatible speech endpoint, or off |

A model that can see images looks at your screen, points and acts; a text-only model still talks and chats. The on-device model assistant finds Ollama, downloads recommended models with live progress, and switches to them in a click.

## Privacy

There's no elfhub server, account or analytics. What leaves your Mac:

- **Your questions** go only to the language model you chose — straight from the app, with your key from the Keychain or your ChatGPT sign-in.
- **Screenshots** leave only when you ask something, and only if your model can see images. Password managers and private websites are left out, and card, insurance, health and ID numbers are blacked out before a screenshot is sent.
- **Two small background requests** go to that same model, both switchable in Settings › Privacy & permissions: a quiet chat's text, to build your main Elf's memory, and a new chat's first exchange, to name it.
- **Web searches and pages** — only for Elfs you let use the web, never anything on your own network.
- **Model downloads** from Hugging Face — only when you press Download, without an account.
- **A daily update check** with GitHub (turn it off in Settings › General).

Keys and sign-ins live in your Keychain. Chats, memory, files and the action log stay in your Library folder. When something unexpected breaks, elfhub can draft a GitHub issue for you, with keys and personal details taken out — nothing is sent unless you submit it yourself.

## Install

1. [Download `elfhub.dmg`](https://github.com/eshan-chawla/elfhub-mac/releases/latest/download/elfhub.dmg) (always the latest version).
2. Open it and drag **elfhub** into **Applications**.
3. Open elfhub. It's signed and notarized, so macOS only asks you to confirm opening an app from the internet.

Setup takes six short steps — name your Elf, pick a model, choose how it hears and sounds, set the shortcut and permissions, and decide what stays on your Mac — then an optional hands-on tutorial.

**Updates:** once a day elfhub checks GitHub Releases and shows what's new with Install, Remind me later and Skip. Updates are signed, so only real elfhub releases install. Your settings, keys, chats and Elfs carry over.

### Permissions

| Permission | Why |
|---|---|
| **Microphone** | Push-to-talk (not needed if you only type) |
| **Speech Recognition** | Apple's on-device speech-to-text, and saying "stop" during screen actions |
| **Accessibility** | The global shortcut, reading on-screen controls, and acting for you |
| **Screen Recording** | Screenshots when you ask (takes effect after a restart; setup has a Quit & reopen button) |

## Build from source

You need an Apple silicon Mac with macOS 14.2+, and Xcode 26+ with its Metal Toolchain (`xcodebuild -downloadComponent MetalToolchain`) for the on-device speech engine (MLX).

1. `open elfhub.xcodeproj`
2. Copy `Config/Local.xcconfig.example` to `Config/Local.xcconfig` and set `DEVELOPMENT_TEAM` and `ELFHUB_BUNDLE_IDENTIFIER` (a free Personal Team works).
3. Select the `elfhub` scheme and press **⌘R**.

Build from Xcode rather than `xcodebuild` in a terminal — terminal builds reset macOS privacy permissions (Screen Recording, Accessibility, …). The unit tests (`elfhubTests/`, around 970 of them) run with the `elfhub-OnlyUnitTest` scheme.

### How it fits together

A native SwiftUI app with AppKit where it needs it: a chat-first main window (your Elfs and chats in the sidebar, Settings at the bottom), a menu bar panel for quick access, and a click-through overlay on every screen for the pointer, marks and status pill. One turn pipeline serves voice and chat alike: capture → model (with tools for the Elf's files, screen steps and pointing) → speech, marks and actions → history. Provider-agnostic model clients speak Anthropic, OpenAI-compatible, Gemini and the ChatGPT plan's Responses API.

The full technical map — every file, decision and convention — is in [`AGENTS.md`](AGENTS.md) (also `CLAUDE.md`), written so a coding agent can work on elfhub from day one.

```
elfhub/          Swift source (flat; see the Key Files table in AGENTS.md)
elfhubTests/     Unit tests
brand/           App icon artwork (all rights reserved, not AGPL — see brand/LICENSE.md)
evals/           Computer-use evaluation tasks
scripts/         Release, DMG, appcast and icon scripts
release-notes/   Notes for each release
```

## Feedback and contributing

elfhub is in public beta, so tell us what breaks:

- **[Discord](https://discord.gg/ZGVzhv4ggS)** — the quickest way in for questions and help.
- **[GitHub issues](https://github.com/eshan-chawla/elfhub-mac/issues)** — bug reports and feature requests (or use **Support** at the bottom of the app's sidebar).
- **Security issues** — please report privately, as described in [SECURITY.md](SECURITY.md).

elfhub is licensed under the [GNU AGPL v3.0](LICENSE) — fork it, hack on it, build your own version. Pull requests are welcome. Parts of the code began in [Clicky](https://github.com/farzaa/clicky) (MIT); see [NOTICE](NOTICE).

The app icon is the exception: the igloo icon, menu bar icon and artwork (`brand/` and the app's icon images) are all rights reserved and not part of the open-source licence. If you ship your own build, give it your own icon — see [brand/LICENSE.md](brand/LICENSE.md).
