<div align="center">

<img src="public/icons/icon128.png" width="88" alt="Kontext" />

# Kontext

**Hit a chat limit? Carry the whole conversation to another AI — in one click.**

Capture any [ChatGPT](https://chatgpt.com) or [Claude](https://claude.ai) chat, distill it into a portable *kontext*, and continue it in the other — local-first, no account.

[![Chrome Extension](https://img.shields.io/badge/Chrome-Extension-4285F4?logo=googlechrome&logoColor=white)](https://developer.chrome.com/docs/extensions)
[![Manifest V3](https://img.shields.io/badge/Manifest-V3-1a73e8)](https://developer.chrome.com/docs/extensions/mv3/intro/)
[![TypeScript](https://img.shields.io/badge/TypeScript-strict-3178C6?logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Tests](https://img.shields.io/badge/tests-65_passing-3ecf8e)](tests/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

[![On-device AI](https://img.shields.io/badge/On--device-Gemini_Nano-7c5cff)](https://developer.chrome.com/docs/ai/built-in)
[![BYOK](https://img.shields.io/badge/BYOK-OpenAI_·_Anthropic_·_Gemini_·_OpenRouter-orange)](#summarizer-the-fallback-chain)
[![No telemetry](https://img.shields.io/badge/telemetry-none-000000)](#privacy-non-negotiable)

<br>

*"Your context is an asset. Kontext makes it portable."*

**Full-fidelity capture · on-device summaries · one-click handoff · never auto-sends · nothing leaves your machine.**

<br>

[How It Works](#how-it-works) · [Features](#features) · [Quick Start](#quick-start) · [Summarizer](#summarizer-the-fallback-chain) · [Privacy](#privacy-non-negotiable)

</div>

---

```
        CAPTURE                    DISTILL                    HAND OFF
   ┌────────────────┐        ┌────────────────┐        ┌────────────────┐
   │  ChatGPT /     │        │   Summarize    │        │  Open the other │
   │  Claude chat   │───────▶│  on-device or  │───────▶│  AI, auto-fill  │
   │  (internal API │        │  your own key  │        │  the composer   │
   │   full history)│        │  → a "kontext" │        │  (never sends)  │
   └────────────────┘        └────────────────┘        └────────────────┘
        every turn              summary + raw            clipboard fallback
      not a DOM scrape        stored in a library         always available

              ▲                                                  │
              │           limit banner detected?                 │
              └──────────  "Continue in Claude →"  ◀─────────────┘
                          the moment you hit a cap
```

---

## Why This Exists

You're deep in a ChatGPT session — decisions made, code written, context built — and you hit the message cap. Continuing in Claude means re-explaining everything, and that backstory eats the *new* chat's context window before you've asked a single question.

**Kontext moves the conversation, not just the text.** It reads the full chat through the platform's own API (every turn of the active branch — not a lossy scrape of what happens to be on screen), distills it into a structured handoff, and drops it into the target AI's composer. The other direction works too. Everything stays on your machine.

---

## How It Works

```
1. CAPTURE   Side panel → content script replays the platform's own
             conversation API with your session. Lossless transcript,
             every turn, active branch only.

2. DISTILL   Summarizer chain turns the transcript into a "kontext":
             Goal · Current state · Decisions · Key facts · Code · Open threads,
             plus the last few turns verbatim. Raw transcript always kept.

3. HAND OFF  "Continue in Claude/ChatGPT" opens the target, waits for the
             composer, and fills it (React-safe insertion). You review and
             hit send — Kontext never sends for you. Context is also copied
             to your clipboard as a guaranteed fallback.
```

A **kontext** always stores *both* the summary and the raw transcript — re-summarize any time, export the raw, nothing is lost.

---

## Features

| | Feature | Detail |
|---|---|---|
| 🎯 | **Full-fidelity capture** | Replays the platform's internal conversation API with your session — every turn, code and all. Not a DOM scrape that breaks on the next UI redesign. |
| 🧠 | **On-device summaries** | Chrome's built-in Gemini Nano runs the summary locally — free, private, no key. Long chats are map-reduced to fit its context. |
| 🔑 | **Bring your own key** | Fallback to OpenAI, Anthropic, Gemini, or **OpenRouter** (free-tier models). A toggle flips the order to prefer your key over on-device. |
| ↔️ | **One-click handoff** | "Continue in Claude/ChatGPT" auto-fills the target composer. **Never auto-sends** — you always review first. |
| ⏱️ | **Limit-moment detection** | The instant a "you've hit your limit" banner appears, a toast offers to continue elsewhere — meeting you at the exact pain point. |
| 📚 | **Local library** | Every kontext is saved: search, view, re-summarize, delete. Your portable memory across AI tools. |
| 📊 | **Live progress** | Spinner + stage text (model-download %, "part 2 of 5 (~40s left)"), plus a completion notification for long runs. |
| 🔒 | **Local-first** | No server, no account, no telemetry. The only outbound calls are the platforms themselves and — if you opt in — your BYOK provider. |

---

## Quick Start

**Requirements:** Chrome 128+ (for on-device AI) and Node 20+ to build.

```bash
git clone https://github.com/anuragmerndev/kontext-ai.git
cd kontext-ai
npm install
npm run build
```

Then load it:

1. Open `chrome://extensions`
2. Enable **Developer mode** (top-right)
3. **Load unpacked** → select the `dist/` folder
4. Pin Kontext, open a ChatGPT or Claude chat, and hit **Capture chat**

### Develop

| Command | Does |
|---|---|
| `npm run watch` | Rebuild on change (hit ⟳ on the extension after) |
| `npm test` | Unit tests (Vitest) — 65 passing |
| `npm run typecheck` | Strict TypeScript, no emit |
| `npm run build` | Production `dist/` |

---

## Summarizer: the fallback chain

Summaries try each engine in order, first available wins:

```
   ┌──────────────┐      ┌──────────────┐      ┌──────────────┐
   │ Gemini Nano  │      │  Your API    │      │     Raw      │
   │  on-device   │ ───▶ │  key (BYOK)  │ ───▶ │  transcript  │
   │  free, private│      │ 4 providers  │      │  (no engine) │
   └──────────────┘      └──────────────┘      └──────────────┘
```

- **Gemini Nano** — Chrome's built-in model, on your machine, no key, no cost. First run downloads the model (progress shown).
- **BYOK** — add a key in Settings for **OpenAI**, **Anthropic**, **Gemini**, or **OpenRouter**. OpenRouter has free-tier models (default `meta-llama/llama-3.3-70b-instruct:free`) — a zero-cost summarizer even where Nano isn't available.
- **Prefer my key** — a settings toggle flips the order so your provider runs first.
- **Raw fallback** — if no engine is available, the kontext keeps the full transcript and the handoff uses that. Never a dead end.

---

## Privacy (non-negotiable)

- **Local-first.** Kontexts live in extension storage. Summaries run on-device by default.
- **No account. No server. No analytics. No telemetry.**
- **Minimal permissions.** `storage`, `sidePanel`, `clipboardWrite`, `notifications`, plus host access to `chatgpt.com` and `claude.ai` only. BYOK provider hosts are *optional* permissions, requested only when you add a key.
- **The only outbound traffic** is the AI platform you're on (the same requests the page itself makes) and — solely if you configure one — your chosen BYOK provider.

---

## Architecture

Manifest V3 · TypeScript (strict) · esbuild · Vitest · zero runtime dependencies · no UI framework.

```
┌─ Side Panel ─────────┐      ┌─ Service Worker ─────┐
│ capture · library    │ ◀──▶ │ handoff routing      │
│ kontext view · BYOK  │      │ tab + payload relay   │
└──────────────────────┘      └──────────┬───────────┘
                                          │ messages
                     ┌────────────────────┴────────────────────┐
                     │ Content scripts (chatgpt.com / claude.ai)│
                     │ capture adapters · injector · limit-watch│
                     └──────────────────────────────────────────┘
```

Full design in [docs/superpowers/specs](docs/superpowers/specs/2026-07-03-kontext-design.md); manual test matrix in [docs/e2e-checklist.md](docs/e2e-checklist.md).

---

## Roadmap

- [ ] Chrome Web Store listing (assets, privacy policy page)
- [ ] Storage-quota warning + cleanup
- [ ] More platforms (Gemini, Grok, DeepSeek)
- [ ] DOM-fallback capture for resilience against API changes
- [ ] MCP server exposing your kontext library to coding agents

---

## License

MIT — see [LICENSE](LICENSE).

---

<div align="center">

Built with [Claude Code](https://claude.com/claude-code) · [@anuragmerndev](https://github.com/anuragmerndev)

*"You don't need a bigger context window. You need your context to travel."*

</div>
