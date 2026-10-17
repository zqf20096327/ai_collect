<!--
  qwen-harness — the private, offline, zero-dependency AI coding agent for local
  Qwen models via Ollama.
  SEO keywords: local LLM agent, offline AI coding assistant, Ollama, Qwen,
  qwen2.5-coder, qwen3-coder, autonomous coding agent, tool-using LLM, agentic loop,
  ReAct, function calling, multi-agent, zero-dependency, TypeScript, Node.js,
  private AI, on-device AI, self-hosted AI, no API key, terminal CLI agent,
  local inference, code generation, developer tool.
  The banner / typing line / badges are decorative external images (shields.io,
  vercel, demolab) rendered only on GitHub; they do not affect the tool.
-->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1f6feb,100:8957e5&height=190&section=header&text=qwen-harness&fontSize=52&fontColor=ffffff&fontAlignY=38&desc=The%20private%2C%20offline%20AI%20coding%20agent%20for%20local%20Qwen%20models&descSize=16&descAlignY=60" alt="qwen-harness" />

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=900&color=8957E5&center=true&vCenter=true&width=680&lines=Private.+Offline.+Zero+dependencies.;A+real+AI+coding+agent+%E2%80%94+not+a+chatbot.;Powered+by+Ollama+%2B+Qwen%2C+on+YOUR+machine.;No+cloud.+No+API+keys.+No+data+leaves." alt="tagline" />

<p>
  <img src="https://img.shields.io/badge/tests-697%20passing-2ea44f" alt="tests" />
  <img src="https://img.shields.io/badge/dependencies-0-2ea44f" alt="zero dependencies" />
  <img src="https://img.shields.io/badge/build-none-2ea44f" alt="no build step" />
  <img src="https://img.shields.io/badge/runs-100%25%20offline-6e40c9" alt="offline" />
  <img src="https://img.shields.io/badge/license-Apache_2.0-blue" alt="license Apache-2.0" />
  <img src="https://img.shields.io/badge/Ollama-Qwen-000000?logo=ollama&logoColor=white" alt="ollama qwen" />
  <img src="https://img.shields.io/badge/TypeScript-3178c6?logo=typescript&logoColor=white" alt="typescript" />
</p>

### Turn a model running on your own machine into a real, tool-using software agent.

No cloud. No API keys. No telemetry. Your code never leaves your computer.

**[📘 Use it](./USER-GUIDE.md)** &nbsp;·&nbsp; **[🧩 How it works](./THIRD_PARTY_NOTICES.md)** &nbsp;·&nbsp; **[🤝 Contribute](./CONTRIBUTING.md)** &nbsp;·&nbsp; **[🙏 Help wanted](./OPEN-PROBLEMS.md)** &nbsp;·&nbsp; **[⚖️ License](./LICENSE)**

</div>

---

## 🧭 Looking for…

| Looking for… | Go to |
|---|---|
| 📘 Install &amp; use it (step by step) | **[USER-GUIDE.md](./USER-GUIDE.md)** |
| 🧩 How it works (architecture &amp; design) | **[THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md)** |
| 🐳 Run it safely / contained | **[USER-GUIDE.md](./USER-GUIDE.md)** → *Running contained* |
| 🙏 Open problems / help wanted | **[OPEN-PROBLEMS.md](./OPEN-PROBLEMS.md)** |
| 🤝 Contribute | **[CONTRIBUTING.md](./CONTRIBUTING.md)** |
| ⚖️ License (Apache-2.0) | **[LICENSE](./LICENSE)** |

---

## 🌟 Why qwen-harness?

- 🔒 **Truly private & offline.** The model, your files, and every transcript stay on
  your machine. Zero network egress, no accounts, no API keys, no vendor lock-in.
- ⚡ **Zero dependencies, zero build step.** Pure TypeScript run directly by Node —
  clone, point it at Ollama, go. Nothing to install from a registry.
- 🤖 **A real agent, not a chatbot.** It reads, searches, writes, and edits files and
  runs commands in a permission-gated **read → decide → act → observe** loop —
  including **multi-agent** delegation, **long-term memory**, and **resumable sessions**.
- 🛡️ **Safe by default.** Every action passes a permission gate, **file tools are confined to your
  workspace** (symlink-proof), and the most dangerous commands are blocked. For full isolation, run it
  inside Docker/WSL or set a sandbox wrapper.
- 🪶 **Built for small local models.** Argument validation + repair, malformed
  tool-call recovery, and automatic context compaction make modest models reliable.
- ✅ **Battle-tested.** 697 automated tests, plus a mandatory secret scan on every run.

## ✨ What it can do

🧩 Use real tools (`read` · `find-files` · `grep` · `write` · `edit` · `multi-edit` · `bash` · `powershell` · `todo`) &nbsp;•&nbsp;
⚡ run independent **tool calls in parallel** &nbsp;•&nbsp;
👥 split work across **2 parallel agents** (with a **live subagent panel** — each worker's task + tokens, pinned while they run) &nbsp;•&nbsp;
🧠 **remember** facts across chats &nbsp;•&nbsp;
💾 **resume** any conversation &nbsp;•&nbsp;
🌊 **stream** answers live &nbsp;•&nbsp;
🔁 switch models on the fly &nbsp;•&nbsp;
🛑 **cancel** a running task with Ctrl+C &nbsp;•&nbsp;
🪶 auto-compact long chats &nbsp;•&nbsp;
🎨 **colorized** markdown + **syntax-highlighted** code + **clickable links** + diff output (NO_COLOR-safe) &nbsp;•&nbsp;
⌨️ **command history** + Tab-autocomplete &nbsp;•&nbsp;
📊 a **context-usage meter** &nbsp;•&nbsp;
🎚️ pick models with `/model`.

## 🎯 Built for

Developers who want a **private, air-gapped coding agent** · teams avoiding cloud AI
costs and data exposure · anyone running **local LLMs** who wants real *actions*, not
just chat · learners who want a clean, readable **agent architecture** to study.

## 📖 Documentation

This README is the front door. Everything else lives in a focused document:

| Looking for… | Go to |
|---|---|
| **Install, run & use it** — step-by-step, plain-English | **[USER-GUIDE.md](./USER-GUIDE.md)** |
| **Architecture + data-flow diagram, project structure, technology choices, dependencies** | **[THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md)** |
| **Contributing & the dev/test workflow** | **[CONTRIBUTING.md](./CONTRIBUTING.md)** |
| **License (Apache-2.0)** | **[LICENSE](./LICENSE)** |

## 🚀 Try it in 60 seconds

```bash
ollama serve     # start your local model server
npm start        # launch the agent (interactive)
# Windows tip: use .\qwen.cmd instead of npm start — then Ctrl+C cancels a running
# request without closing the app (npm's shell shim exits on the first Ctrl+C).
```

Then just type what you want in plain English. Full walkthrough, options, and
examples → **[USER-GUIDE.md](./USER-GUIDE.md)**.

## 💡 Using it to the fullest

The small things that make it genuinely useful day to day:

**🗣️ It holds the whole conversation.** In the interactive REPL the agent remembers
everything said so far, so follow-ups just work:
```text
> Read config.ts and tell me what it does.
> Now add a comment at the top explaining that.   ← it knows "that" = config.ts
```

**⏸️ Stop now, continue later — right where you left off.** Every chat is saved and the
REPL prints a session id at startup:
```bash
npm start -- --list-sessions       # find a past chat
npm start -- --resume <id>         # reopen it with full context restored
# inside the REPL:  /sessions  (list)    /new  (start fresh)
```

**🧠 It remembers across different chats.** Tell it something durable and it comes back
later, even in a brand-new conversation:
```text
> Remember that our build output goes in the dist folder.
# …a new chat, another day:
> Where does the build output go?        →  "the dist folder"
```

**👥 Hand a big job to a team (max 2 at once).**
```bash
npm start -- --multi "add a header comment to every file in src, in parallel"
```

**🔁 Switch brains for the task** — fast 7B for everyday work, the bigger model for hard
problems, mid-chat:
```text
/model qwen3-coder:30b        (/model qwen2.5-coder:7b to switch back)
```

**🎚️ Decide how often it checks with you:**
```text
/mode acceptEdits   # stop confirming each edit (dangerous commands still blocked)
/mode plan          # look only, change nothing
/mode default       # ask before every change (the safe default)
```

**⚡ One-and-done for a quick task:**
```bash
npm start -- "list the files here and tell me which is largest"
npm start -- --json "…"     # emit one JSON event per line (JSONL) for scripts / piping / logs
npm start -- --verify "npm test" "fix the failing build"   # run a check after the task; if it fails the agent fixes it (≤3 tries)
npm start -- --web "summarize https://example.com/post"    # opt-in web_fetch (off by default): asks per website (Once/Always/No, session-scoped), only URLs already in the chat, SSRF-blocked, page treated as untrusted data
npm start -- --web "search for the fastest rust http client"  # web_search too (needs QWEN_HARNESS_SEARCH_URL + _KEY — a Tavily-compatible backend; no provider bundled)
# a shell curl/wget/Invoke-WebRequest bypasses the web_fetch safety pipeline, so it is ALWAYS gated (asks even in bypass); QWEN_HARNESS_SHELL_NET=deny hard-blocks it
```

**⌨️ REPL commands:** `/help` · `/model [tag]` · `/mode [mode]` · `/models` · `/context` · `/cost` · `/search <text>` · `/sessions` · `/new` · `/resume` · `/rename <title>` · `/compact` · `/keys` · `/diff` · `/editor` · `/verify [cmd]` · `/image <path>` · `/copy` · `/rewind` · `/theme` · `/clear` · `/perms` · `/exit`. On a terminal the **rich input is on by default**: a live `/` command menu (with argument submenus), `@` file mentions, fish-style **ghost-text** suggestions (→/End to accept) — relevance-ranked to the current chat, plus **model-proposed next-step suggestions** on an empty line (Tab cycles them, → fills one in; `QWEN_HARNESS_NO_SUGGEST=1` to disable), Ctrl+R search, **bracketed paste** (big pastes collapse to `[Pasted text #N]` and expand on send), **undo/redo** (Ctrl+Z/Ctrl+_), a **kill-ring** + word-wise editing, `!shell` escape, **arrow-key permission approvals** (↑/↓ + Enter), **Shift+Tab** to cycle the permission mode, a live **↑in ↓out** token counter (per turn + in the status line; also `/cost`), **fuzzy-searchable** pickers and menus (fzf-style ranking; name a chat with `/rename`), **word-level diff highlights**, **markdown tables** (width-aware, rounded corners) + **ER diagrams** (a `mermaid`/`er` erDiagram code block renders as ASCII entity boxes), a **live task checklist pinned above the input while the agent works** (✓ ticks update in place; the final list lands in the transcript once), **plan approval done right** — in plan mode the model presents its plan as an auto-sizing boxed step list (each step with a one-line "how") shown as a self-erasing approval preview, and approving it **starts execution immediately**; the model can also **ask you a question** (single- or multi-choice with a custom-answer option) when it genuinely needs a decision (which API, which approach first) — info-gathering only, never to hand you work, a **stall indicator** when the model goes quiet, the session in your **tab title**, `/copy` to put the last answer on the clipboard, **file checkpoints + `/rewind`** (undo the agent's edits back to any earlier ask — and undo the undo), **secret-aware paste** (a pasted API key is never echoed to the screen), a **resume recap**, **Esc-Esc** to clear the line, **Ctrl+S** to stash/restore a draft, **Ctrl+L** to redraw, and a **`+N -N`** added/removed summary on edits, **syntax-highlighted** code blocks, **clickable links** (OSC-8), one-time **first-run tips**, key **hints** in menus, **terminal-native notifications** — an OS popup straight from an escape sequence on kitty/ghostty/WezTerm/iTerm2 (with a plain bell elsewhere; default on a TTY, `QWEN_HARNESS_BELL=0` to silence; tmux-safe) plus an optional OS toast (`QWEN_HARNESS_NOTIFY=1`), fired when a **permission prompt waits >6s** or a **longer turn completes** (tune with `QWEN_HARNESS_NOTIFY_AFTER=<seconds>`, `0` = every turn), and a **reduced-motion** mode (`QWEN_HARNESS_REDUCED_MOTION=1`), **terminal-resize** re-layout, **drag-and-drop** file paths into the prompt, an opt-in **mouse** (`QWEN_HARNESS_MOUSE=1`; Linux/macOS + Windows Terminal-class consoles): **double-click** moves the caret; text selection stays NATIVE — **Shift+drag** at the prompt (terminals bypass mouse capture while Shift is held) and plain drag whenever a task is running (the mouse is handed back to the terminal then, so wheel-scrolling works too). An experimental in-app drag-select with copy-on-release (OSC 52) exists behind `QWEN_HARNESS_DRAG_SELECT=1`, and inline **images** in supporting terminals (`/image <path>`; iTerm2/kitty). Prefer the classic line editor? `QWEN_HARNESS_PLAIN_INPUT=1` gives the plain readline REPL (Tab-complete + UP/DOWN history, y/a/N approvals). Piped/non-TTY input always uses the plain path.

> Prefer a full, step-by-step walkthrough? → **[USER-GUIDE.md](./USER-GUIDE.md)**.

## ⭐ At a glance

**697 tests · 0 dependencies · no build step · 100% offline · Apache-2.0 licensed.**

## 🙏 Help wanted

A few hard problems are still open — reliable tool-calls on small models, blocking destructive commands without
a sandbox, prompt-injection resistance, and more. Each is documented with a **reproducible proof** and a stable
ID (`Help001`, `Help002`, …) in **[OPEN-PROBLEMS.md](./OPEN-PROBLEMS.md)**.

> 🐳 **Running in Docker/WSL already neutralises or contains 4 of the 7** (the safety ones) — the rest are
> model-quality questions. Ideas, references, and PRs are very welcome: open an issue titled `[HelpNNN] …`.

## 🔎 Keywords

`local LLM agent` · `offline AI coding assistant` · `Ollama` · `Qwen` ·
`qwen2.5-coder` · `qwen3-coder` · `autonomous coding agent` · `tool-using LLM` ·
`agentic loop` · `ReAct` · `function calling` · `multi-agent` · `zero-dependency` ·
`TypeScript` · `Node.js` · `private AI` · `on-device AI` · `self-hosted AI` ·
`no API key` · `terminal / CLI AI` · `local inference` · `code generation` ·
`developer tool`

<sub>💡 For real discoverability, also set these as the repository **Description** and
**Topics** in GitHub's “About” panel — that, plus this README, is what search engines
and GitHub search index.</sub>

<div align="center"><sub>Apache-2.0 Licensed · Designed to run entirely on your machine 🖥️</sub></div>
