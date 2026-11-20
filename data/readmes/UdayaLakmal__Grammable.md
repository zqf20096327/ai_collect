<div align="center">

<img src="docs/icon-256.png" width="128" alt="Grammable app icon" />

# Grammable

### Free, open-source AI writing assistant for macOS

**Fix grammar and spelling, change tone, rewrite and format text in _any_ Mac app —
powered by the AI you already have: Claude Code, Codex CLI, Gemini CLI, Antigravity, Devin, Ollama, LM Studio or Apple Intelligence.
No AI yet? Grammar fixes work out of the box, and a free offline AI is three clicks away.**

**No subscription. No account. No servers. 100% free.**

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
[![macOS 12+](https://img.shields.io/badge/macOS-12%2B-black?logo=apple)](#requirements)
[![Swift](https://img.shields.io/badge/Swift-5.9%2B-orange?logo=swift)](Package.swift)
[![Build](https://github.com/UdayaLakmal/Grammable/actions/workflows/ci.yml/badge.svg)](https://github.com/UdayaLakmal/Grammable/actions/workflows/ci.yml)
[![Latest release](https://img.shields.io/github/v/release/UdayaLakmal/Grammable?include_prereleases)](https://github.com/UdayaLakmal/Grammable/releases)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-Support%20Grammable-FF5E5B?logo=ko-fi&logoColor=white)](https://ko-fi.com/udayalakmal)

[**Download**](https://github.com/UdayaLakmal/Grammable/releases/latest) ·
`brew install --cask udayalakmal/tap/grammable` ·
[Demo](#see-it-in-action) ·
[Features](#features) ·
[How it works](#how-it-works) ·
[AI backends](#supported-ai-backends) ·
[Presets](#custom-presets) ·
[Privacy](#privacy) ·
[FAQ](#faq)

</div>

<p align="center">
  <img src="docs/screenshots/menu.png" width="300" alt="Grammable actions menu: fix grammar, change tone, rewrite, format" />
  <img src="docs/screenshots/review-grammar.png" width="500" alt="Grammable grammar check: accept or reject each correction" />
</p>

---

## See it in action

<table>
  <tr>
    <td align="center" width="33%"><a href="docs/demo/fix-grammar.gif"><img src="docs/demo/fix-grammar.gif" alt="Demo: Grammable fixes grammar and spelling in a TextEdit note" /></a></td>
    <td align="center" width="33%"><a href="docs/demo/make-professional.gif"><img src="docs/demo/make-professional.gif" alt="Demo: Grammable rewrites a note in a professional tone" /></a></td>
    <td align="center" width="33%"><a href="docs/demo/settings-tour.gif"><img src="docs/demo/settings-tour.gif" alt="Demo: Grammable menu bar menu and Settings tabs" /></a></td>
  </tr>
  <tr>
    <td align="center"><b>Fix grammar &amp; spelling</b><br/><sub>Review each correction, then replace.</sub></td>
    <td align="center"><b>Change the tone</b><br/><sub>Make Professional, pasted back in one click.</sub></td>
    <td align="center"><b>Menu bar &amp; Settings</b><br/><sub>Default AI, offline AI, presets, privacy.</sub></td>
  </tr>
</table>

<p align="center"><sub>Click any demo to see it full size.</sub></p>

---

## Why Grammable?

You **already pay for Claude, ChatGPT or Gemini**, or can run a free local model. Why pay another monthly subscription just to write better?

Grammable is **more than a grammar checker**. Select text in any app and fix it, rewrite it, change its tone, shorten it, or turn it into bullet points or an email, all with **your own AI** and **your own prompts**.

It's a tiny **menu bar app** that turns the AI tools already installed on your Mac into a **system-wide writing assistant** — without the extra subscription, the browser extension or sending your writing to yet another company.

| | Grammable | Typical subscription writing assistants |
|---|---|---|
| Price | **Free forever (GPL-3.0)** | Monthly subscription |
| AI model | **Your choice:** Claude, GPT/Codex, Gemini, Antigravity, Devin, Llama, Qwen, Mistral, Apple on-device… | Vendor's model only |
| Offline mode | **Yes** (Ollama, LM Studio, Apple Intelligence, built-in macOS checker) | No |
| Works with nothing installed | **Yes** — grammar & spelling via the macOS checker | — |
| Works in | **Any app** with selectable text | Selected apps / browser |
| Extra account | **None** | Required |
| Your own prompts | **Yes** — shareable Markdown presets | Limited |
| Source code | **Open** | Closed |

> **Reuse what you already have.** If Claude Code, Codex, Gemini, Antigravity or Devin's command-line tool is signed in on your Mac, Grammable simply runs it — on the plan you already pay for. No API keys to paste, nothing new to buy.

### What about Apple's built-in Writing Tools?

macOS has checked spelling since the first Mac OS X and grammar since Mac OS X 10.5 Leopard (2007), but that checker misses many mistakes an AI catches. AI rewriting (Apple Intelligence **Writing Tools**) only arrived in **macOS Sequoia 15.1 (October 2024)**, and only on **Apple silicon** Macs.

- 💻 **On Monterey, Ventura, Sonoma or an Intel Mac?** Your Mac has **no built-in AI rewriting at all**. Grammable adds it, powered by Claude, Codex, Gemini, Ollama or any other supported AI, back to **macOS 12**.
- ✨ **On Sequoia or later with Apple silicon?** Grammable still goes further:
  - 🧠 **Your choice of model:** Claude, GPT, Gemini, Llama and more, or Apple's own on-device model on macOS 26.
  - 🧩 **Your own presets:** write a prompt once and it becomes a one-click action.
  - ✅ **Every fix shown separately:** accept or reject each correction instead of taking the whole rewrite.
  - ⌨️ **One shortcut everywhere:** the same **⌃⌥G** menu in every app, including apps where Writing Tools doesn't show up.

---

## Features

- ✍️ **Grammar & spelling check** for any selected text — mistakes are shown as individual changes you can **accept or reject one by one**.
- 🎭 **Tone adjustment** — Professional, Friendly, Confident, Concise, Simplify.
- 🔁 **Rewrite & improve** — clearer, smoother writing with an editable before/after view.
- 📋 **Format text** — bullet points, email format, or anything you define.
- 🖱️ **Appears when you select text** — a small **G** button pops up next to your selection; click it for actions. No live typing surveillance.
- ⌨️ **Global shortcut `⌃⌥G`** — works even when the pop-up button is turned off.
- 🧠 **Choose the AI per action** — e.g. on-device Ollama for grammar, Claude for tone.
- 🆓 **Works with no AI installed** — *Fix Grammar & Spelling* uses the spelling and grammar checker built into macOS, and takes over automatically if your AI isn't installed or running.
- 📦 **One-click free offline AI** — *Settings → AI Backends → Free offline AI* installs Ollama and downloads a small model with a progress bar. No account, nothing leaves your Mac.
- 🔒 **Privacy badge on every result** — always shows whether your text stayed **On-device** or went to the **Cloud**.
- 📝 **Custom presets as Markdown files** — write your own house style, share it on GitHub.
- 🟢 **Menu bar on/off switch** — pause Grammable instantly.
- 🚀 **Starts quietly at login** — sits in the menu bar after a restart, with no windows. Turn it off in Settings.
- 🚫 **Per-app exclusions** — never pops up in Terminal, Keychain Access, or apps you choose.
- 🔑 **Never reads password fields.** Your clipboard is restored after every action.
- 🪶 **Native & lightweight** — Swift + SwiftUI, ~2 MB universal binary (Apple silicon & Intel), no Electron. Runs on **macOS 12 Monterey** and later.
- 🧰 **Command-line mode** — `Grammable --run fix-grammar "text"` for scripts and Shortcuts.

## How it works

```
 Select text in any app ──► G button appears ──► pick an action ──► review ──► Replace / Copy
        (Mail, Slack, Notes, Safari, Chrome, Word, VS Code, …)         │
                                                                       ▼
        Claude Code · Codex CLI · Gemini CLI · Antigravity CLI · Devin CLI · Ollama · LM Studio · Apple Intelligence
                                  (no AI? grammar fixes use the macOS spell checker)
```

1. **Select** some text you wrote — in any app.
2. Click the **G** button that appears next to it (or press **`⌃⌥G`**).
3. Choose an action: **Fix Grammar & Spelling**, **Make Professional**, **Make Concise**, **Format as Email**… (number keys `1`–`9` work too). The bottom of the menu shows which AI will be used, and a notice with **Set Up Free AI…** appears if none is set up.
4. **Review** the suggestion:
   - *Grammar fixes* → every change is listed; tick the ones you want.
   - *Rewrites* → an editable before/after view.
5. Press **Replace** (`↩`) to put the text back in place, or **Copy**.

<p align="center">
  <img src="docs/screenshots/review-rewrite-dark.png" width="480" alt="Grammable tone rewrite with on-device badge, dark mode" />
</p>

## Supported AI backends

Grammable never bundles a model or calls its own server. It drives tools **you already have installed** — and works without any of them for grammar and spelling:

| Backend | Where your text goes | What you need | Cost |
|---|---|---|---|
| **[Claude Code](https://docs.anthropic.com/en/docs/claude-code)** | ☁️ Anthropic, under **your own** Claude account | `claude` CLI installed & signed in | Included in your Claude plan |
| **[Codex CLI](https://github.com/openai/codex)** | ☁️ OpenAI, under **your own** ChatGPT / OpenAI account | `codex` CLI installed & signed in | Included in your ChatGPT plan |
| **[Gemini CLI](https://github.com/google-gemini/gemini-cli)** | ☁️ Google, under **your own** Google account | `gemini` CLI installed & signed in | Free tier available |
| **[Antigravity CLI](https://antigravity.google/docs/cli/install)** | ☁️ Google, under **your own** Antigravity account | `agy` CLI installed & signed in. Slower (often 10–70 s): it runs as a full agent | Included in your Antigravity plan |
| **[Devin CLI](https://cognition.com/blog/devin-for-terminal)** | ☁️ Cognition, under **your own** Devin account | `devin` CLI installed & signed in (`devin auth login`) | Counts toward your Devin plan |
| **[Ollama](https://ollama.com)** | 🔒 **Stays on your Mac** | Ollama running + any model (`ollama pull llama3.2`) | Free |
| **[LM Studio](https://lmstudio.ai)** / Jan / llama.cpp | 🔒 **Stays on your Mac** | Local OpenAI-compatible server | Free |
| **Apple Intelligence** | 🔒 **Stays on your Mac** | macOS 26+, Apple silicon, Apple Intelligence on, built with Xcode 26+ | Free |
| **macOS Spelling & Grammar** (built in) | 🔒 **Stays on your Mac** | Nothing — always available. Grammar & spelling fixes only, no rewrites | Free |

> 💡 **Install the command-line tool, not just the app.** Grammable runs Claude Code, Codex, Gemini, Antigravity and Devin through their **command-line tools**. Having only the desktop app (Claude, ChatGPT, Antigravity, Antigravity IDE or Devin) isn't enough. Install the CLI with the commands below and run it once in Terminal to sign in. If none is set up, **Settings → AI Backends** shows these commands and tells you which apps are missing their command-line tool.

**No AI installed? It still works.** *Fix Grammar & Spelling* falls back to the spelling and grammar checker built into macOS, so it works on any Mac with zero setup. For rewrites and tone changes, **Settings → AI Backends → Free offline AI** sets up [Ollama](https://ollama.com) in three clicks: download Ollama, start it, then pick a small model (Llama 3.2 3B, 2 GB, or 1B, 1.3 GB, for older or Intel Macs). Grammable downloads it with a progress bar and makes it your default. Nothing is bundled in the 2 MB app, and no text ever leaves your Mac.

> ⚠️ **Important — about "local".** Grammable itself runs entirely on your Mac and has no servers. However, **Claude Code, Codex CLI, Gemini CLI, Antigravity CLI and Devin CLI are cloud services**: when you choose them, your selected text is sent to Anthropic, OpenAI, Google or Cognition using **your own** installed and signed-in CLI, under your account and their terms. For **fully offline** use, choose **Ollama**, **LM Studio**, **Apple Intelligence** or the built-in **macOS Spelling & Grammar** checker. Every result shows an **On-device** or **Cloud** badge so you always know.

<p align="center"><img src="docs/screenshots/settings-backends.png" width="560" alt="Grammable AI backend settings" /></p>

Grammable finds the CLIs automatically (Homebrew, npm, bun, volta, nvm, `~/.local/bin`…). You can also set a custom path and model for each backend in **Settings → AI Backends**, and test it with one click.

## Installation

### Homebrew (recommended)

```bash
brew install --cask udayalakmal/tap/grammable
```

Then open **Grammable** from Applications and allow **Accessibility** when asked.
On Homebrew 7, if you're asked to trust the tap, run `brew trust udayalakmal/tap` first.

**Upgrading:**

```bash
brew update && brew upgrade --cask grammable
```

If Homebrew says the latest version is already installed but Grammable is older, `brew update` was skipped — run it first. After each upgrade, remove Grammable from the Accessibility list with **–** and add it again with **+** (needed until releases are notarized).

Settings opens by itself only on the first launch. After that Grammable starts quietly at login; open it again from Applications or Spotlight to reach Settings.

### Download

1. Download the latest **`Grammable-x.y.z.zip`** from [**Releases**](https://github.com/UdayaLakmal/Grammable/releases/latest).
2. Unzip and drag **Grammable.app** to **Applications**.
3. Open it. If macOS says it can't verify the developer, **right-click → Open** once, or run:
   ```bash
   xattr -dr com.apple.quarantine /Applications/Grammable.app
   ```
4. Allow **Accessibility** when asked (System Settings → Privacy & Security → Accessibility; on Monterey, System Preferences → Security & Privacy → Privacy → Accessibility). This lets Grammable read your selection and paste the result back.
5. Look for the **G** icon in the menu bar. Done!

### Build from source

Requires Xcode 15+ (Xcode 26+ to include Apple Intelligence support).

```bash
git clone https://github.com/UdayaLakmal/Grammable.git
cd Grammable
./scripts/build-app.sh          # creates dist/Grammable.app (universal)
open dist/Grammable.app
```

Run the tests with `swift test`.

### Set up an AI backend (optional)

Grammar and spelling fixes work without one. For tone changes and rewrites, pick any of these:

```bash
# Option A — reuse a subscription you already have (cloud)
npm install -g @anthropic-ai/claude-code && claude      # sign in once
npm install -g @openai/codex && codex                   # sign in once
npm install -g @google/gemini-cli && gemini             # sign in once
curl -fsSL https://antigravity.google/cli/install.sh | bash && agy      # Antigravity, sign in once
curl -fsSL https://cli.devin.ai/install.sh | bash && devin auth login   # Devin, sign in once

# Option B — 100% offline and free (easiest: Settings → AI Backends → Free offline AI)
brew install ollama && ollama serve &
ollama pull llama3.2
```

No AI at all? *Fix Grammar & Spelling* still works using the macOS spell checker.

## Custom presets

Every action is a plain **Markdown file** in `~/.grammable/presets/`. Create one in **Settings → Presets → Create**, or by hand:

```markdown
---
name: Professional Email
icon: briefcase        # any SF Symbol name
mode: rewrite          # rewrite = before/after view · fix = accept/reject each change
backend: claude        # optional: claude | codex | gemini | antigravity | devin | ollama | openai-compatible | apple | builtin
model: haiku           # optional, backend-specific
order: 15              # optional, position in the menu
---
Rewrite the text as a clear, polite, professional email.
Keep it short. Do not invent facts.
```

- A file with the same name as a built-in preset (e.g. `fix-grammar.md`) **replaces** it — click **Customize** in Settings to start from the built-in.
- Use `backend:` to **mix AIs per action**: free local Ollama for quick grammar fixes, Claude for nuanced tone.
- Browse and share community presets in the [`presets/`](presets) folder — pull requests welcome!

**Built-in presets:** Fix Grammar & Spelling · Improve Writing · Make Professional · Make Friendly · Make Confident · Make Concise · Simplify · Format as Bullet Points · Format as Email

## Command line

The app binary doubles as a CLI — useful for scripts, Automator and Shortcuts:

```bash
G=/Applications/Grammable.app/Contents/MacOS/Grammable
$G --status                                    # which backends are available
$G --list                                      # list presets
$G --render-ui ~/Desktop/grammable-ui          # render every screen to PNG
$G --run fix-grammar --diff "i has went home"  # → I went home.
$G --run fix-grammar --backend builtin "teh email"   # macOS spell checker, no AI
pbpaste | $G --run professional --backend ollama | pbcopy
```

## Privacy

- **No servers, no telemetry, no analytics, no account.** Grammable never phones home.
- Selected text is read **locally** to decide whether to show the button. It is sent to an AI **only when you choose an action**, and **only** to the backend you picked.
- **Password fields are never read.** Terminal and Keychain Access are excluded by default, and you can add any other app in Settings → Privacy.
- Your **clipboard is restored** after copy/paste fallbacks, and temporary entries are marked so clipboard managers ignore them.
- CLIs run in an empty temporary folder with tools, MCP servers and project settings **disabled** (Claude Code runs with `--tools "" --strict-mcp-config --setting-sources ""`), so the AI only ever sees the text you selected.
- Nothing you write is logged or stored.

## Requirements

- macOS 12 Monterey or later (Apple silicon or Intel)
- Accessibility permission
- An AI backend from the table above for tone changes and rewrites (grammar fixes work without one)

## FAQ

<details>
<summary><b>Is Grammable really free? What's the catch?</b></summary>

Yes — it's GPL-3.0 open source. There's no paid tier, no account and no server costs, because the AI runs through tools you already have. If it saves you a subscription, consider [buying me a coffee on Ko-fi](https://ko-fi.com/udayalakmal) ☕.
</details>

<details>
<summary><b>Does it check my writing as I type?</b></summary>

No, on purpose. Grammable never watches your typing and does no live underlining. It works only on text you select and only when you ask: grammar & spelling fixes, tone changes, rewriting and formatting in any app, using an AI of your choice.
</details>

<details>
<summary><b>Does it work offline?</b></summary>

Yes, with **Ollama**, **LM Studio** (or any local OpenAI-compatible server), **Apple Intelligence**, or the built-in **macOS Spelling & Grammar** checker. Claude Code, Codex, Gemini, Antigravity and Devin need the internet.
</details>

<details>
<summary><b>Do I need to install an AI first?</b></summary>

No. *Fix Grammar & Spelling* works immediately using the checker built into macOS (it's simpler than an AI: it catches spelling and common grammar mistakes). For tone changes and rewrites, open **Settings → AI Backends → Free offline AI**: Grammable helps you install the free Ollama app and downloads a small model (Llama 3.2 3B, about 2 GB, or 1B, about 1.3 GB, for older or Intel Macs). Grammable itself stays about 2 MB — no model is bundled.
</details>

<details>
<summary><b>I have the Claude / Antigravity / Devin app. Why isn't it listed as available?</b></summary>

Grammable needs each service's **command-line tool**, which is separate from its desktop app. Install it (see [Set up an AI backend](#set-up-an-ai-backend-optional)), run it once in Terminal to sign in, then click **Refresh** in Settings → AI Backends. Settings tells you when an app is installed without its command-line tool.
</details>

<details>
<summary><b>Do I need an API key?</b></summary>

No. Grammable uses the CLIs you have already signed in to (Claude Code, Codex, Gemini, Antigravity, Devin), or local models that need no key at all.
</details>

<details>
<summary><b>Which apps does it work in?</b></summary>

Any app where you can select text: Mail, Notes, Messages, Pages, Safari, Chrome, Slack, Discord, Notion, Microsoft Word & Outlook, VS Code and more. For apps that don't expose text through Accessibility, Grammable falls back to copy/paste automatically (use `⌃⌥G`).
</details>

<details>
<summary><b>Why isn't it on the Mac App Store?</b></summary>

The App Store sandbox forbids running other command-line tools and the Accessibility features Grammable needs. It is distributed through GitHub instead.
</details>

<details>
<summary><b>The G button doesn't appear.</b></summary>

Check that Grammable is **Enabled** in the menu bar, Accessibility is granted (Settings → General), and the app isn't in the exclusion list (Settings → Privacy). After updating an unsigned build, macOS may require you to remove and re-add Grammable in the Accessibility list. You can always use `⌃⌥G`.
</details>

<details>
<summary><b>Homebrew says it's up to date, but I have an old version.</b></summary>

Homebrew refreshes taps only occasionally. Run `brew update`, then `brew upgrade --cask grammable`. If that still doesn't help: `brew reinstall --cask udayalakmal/tap/grammable`.
</details>

<details>
<summary><b>How do I stop Grammable from starting at login?</b></summary>

Turn off **Launch at login** in Settings → General (or in System Settings → General → Login Items). Settings opens automatically only on the very first launch; afterwards Grammable starts quietly in the menu bar.
</details>

<details>
<summary><b>Which backend is fastest?</b></summary>

Local models on Apple silicon (Ollama with a small model such as `llama3.2` or `qwen2.5:3b`) usually answer in 1–3 seconds. Agent CLIs typically take 3–8 seconds. Set a smaller model (e.g. `haiku` for Claude) in Settings for faster replies.
</details>

## Roadmap

- [ ] Customizable keyboard shortcut
- [x] Homebrew tap (`brew install --cask udayalakmal/tap/grammable`)
- [ ] Official Homebrew cask (`brew install --cask grammable`, needs notarized builds)
- [ ] Signed & notarized releases
- [ ] Preset chaining (e.g. Fix Grammar → Make Concise)
- [ ] Explanations for each grammar fix
- [ ] Localization
- [x] Works without an AI (macOS spell checker) and one-click offline AI setup
- [x] macOS 12 Monterey support

## Contributing

Bug reports, presets and pull requests are very welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). The easiest way to contribute is to **share a useful preset** in [`presets/`](presets).

## Support

Grammable is free and always will be. If it's useful to you:

- ⭐ **Star this repo** — it helps others find it
- ☕ [**Buy me a coffee on Ko-fi**](https://ko-fi.com/udayalakmal)
- 🐛 [Report bugs & request features](https://github.com/UdayaLakmal/Grammable/issues)

## License

Copyright © 2026 Udaya Lakmal.

Grammable is free software: you can redistribute it and/or modify it under the terms of the [GNU General Public License v3.0](LICENSE) or (at your option) any later version.

Claude, Codex, Gemini, Antigravity, Devin, Ollama, LM Studio, Apple Intelligence and Apple are trademarks of their respective owners. Grammable is an independent project and is not affiliated with or endorsed by any of them.

---

<sub>Keywords: free grammar checker for Mac, AI writing assistant macOS, open source grammar checker, rewrite text with AI, tone changer, paraphrasing tool, spell checker, proofreading app, Claude Code, Codex CLI, Gemini CLI, Ollama, LM Studio, Antigravity CLI, Devin CLI, local LLM, offline AI writing, offline grammar checker, works on macOS Monterey, Apple Intelligence Writing Tools alternative, menu bar app, SwiftUI.</sub>
