# Context OS

**A portable, plain-Markdown context layer for AI agents.** Stop re-explaining who you are, what you're working on, and how you like to work every time you open a new chat, switch tools, or start a fresh session.

Context OS is a small set of Markdown files plus loading rules. You fill in the blanks once. Then any AI tool — Claude Code, Codex, ChatGPT, Gemini, Cursor, a local model — reads the right files, in the right order, and works the way you want without a 20-message warm-up.

It's not a framework, an app, or a dependency. It's just files. You own them. They travel with you.

> The name rides the "LLM OS" metaphor (the model is the CPU, your context window is the RAM). What this actually gives you is the **memory + loading policy** layer — the part everyone keeps rebuilding by hand in every new chat.

---

## The problem it solves

Every new session, you re-explain:

- who you are and what you do
- which projects are live and what state they're in
- your stack, your conventions, your "please give me commands not lectures"
- what's private and must not leak

Pasting one giant bio doesn't scale: it's too big for small tasks, out of date in a week, and leaks private info into tools that don't need it. Context OS fixes that with **modular files** and **a rule for what to load when**.

---

## How it works

```
                          ┌─────────────────────────────┐
            you  ─ task ─▶ │   any AI tool / agent       │
                          └──────────────┬──────────────┘
                                         │ reads an entry point
                ┌────────────────────────┼────────────────────────┐
                ▼                         ▼                         ▼
          CLAUDE.md                  AGENTS.md                (other)
          (Claude Code)         (Codex / coding agents)   TOOL_ADAPTERS.md
                └────────────────────────┼────────────────────────┘
                                         ▼
                              ┌──────────────────────┐
                              │      MANIFEST.md      │   ← the "kernel"
                              │  what to load, when,  │     decides the
                              │  privacy + truth rules│     smallest bundle
                              └───────────┬───────────┘
                                          │ loads by Level (0–4)
        ┌──────────────┬──────────────────┼──────────────────┬──────────────┐
        ▼              ▼                  ▼                  ▼              ▼
  YOU_CONTEXT.md  YOU_PROJECTS.md  YOU_TECH_STACK.md   YOU_CAREER.md  YOU_CREATIVE.md
   (who you are)   (live projects)   (stack/commands)   (optional)     (optional)
        │
        ▼
  projects/<name>/PROJECT_CONTEXT.md + CLAUDE.md   ← per-project detail
        ┊
        ┊  opt-in, never auto-loaded, git-ignored by default:
        ▼
  YOU_PRIVATE.md   (salary, family, sensitive strategy, etc.)

                ▲                                                  │
                │         end-of-session update loop               │
                └──────────  "did we learn anything durable?"  ◀───┘
                            propose a patch → you approve → it's saved
```

Three ideas do all the work:

1. **Load the smallest useful bundle.** A quick question loads almost nothing. A coding session loads your stack + the one project. You never dump everything.
2. **Privacy is a layer, not a hope.** Anything sensitive lives in `*_PRIVATE.md` files that are *opt-in per task* and **git-ignored by default**, so they don't get committed or fed to tools that don't need them.
3. **It updates itself (with your approval).** Every meaningful session ends with "did we learn anything durable?" — the agent proposes a patch to the right file, you say yes, and the context stays current instead of rotting.

---

## Load Levels (the core rule)

`MANIFEST.md` tells the agent how much to load:

| Level | When | Loads |
|---|---|---|
| **0 — Orientation** | quick chat, tight context | `YOU_CONTEXT.md` (or just its compact prompt) |
| **1 — General work** | most non-code tasks | `+ YOU_PROJECTS.md` if relevant |
| **2 — Technical** | coding, deploy, debugging | `+ YOU_TECH_STACK.md + projects/<name>/…` |
| **3 — Career** | resume, portfolio, applications | `+ YOU_CAREER.md` |
| **4 — Private** | only when you say so | `+ *_PRIVATE.md` overlays |

---

## Quick start (the easy way)

You don't fill these files in by hand. Let the AI do it from what it already knows about you.

1. **Get the files** — fork/clone this repo, or download it as a folder. Keep it somewhere stable (e.g. `~/context-os/`).
2. **Point your AI tool at the folder and say:**

   > **"Read SETUP.md and set up Context OS for me."**

   It reads your repo, your prior context, and anything it already knows, drafts your `YOU_*.md` files, shows you the draft, and asks only about the gaps. You start filled-in, never blank. (See [`SETUP.md`](SETUP.md).)
3. **End sessions with the loop** — paste `prompts/session-end.md` ("did we learn anything durable?"). Approve the patch. The context keeps itself current.

That's the whole loop. Everything below is reference for when you want to go deeper.

> **No GitHub, or prefer a browser?** [readthemanifest.net](https://readthemanifest.net) builds the same files from what your AI tools already know about you, and can keep them in a private repo it creates for you or serve them to Claude and ChatGPT through one MCP link. Same layer, no terminal.

### Doing it by hand (optional)

Prefer to fill them in yourself? Open the `YOU_*.md` files — each has instructions and an example at the top. You only *need* `YOU_CONTEXT.md` to start. Then:

- **Claude Code** reads `CLAUDE.md` automatically · **Codex / coding agents** read `AGENTS.md` automatically.
- **ChatGPT / Gemini / others:** paste `prompts/handoff.md` plus the relevant `YOU_*.md` file(s).
- **Add a project:** copy `projects/example-project/` to `projects/your-project/` and fill it in.

> **Privacy note:** `YOU_PRIVATE.md` and `YOU_CAREER_PRIVATE.md` are git-ignored by default (see `.gitignore`). Copy the `*.example.md` versions to the real filename and fill them in — your real private files will never be committed.

---

## What's in here

**System files (use as-is):**

- `MANIFEST.md` — the loader: load levels, source-of-truth order, privacy/verification rules
- `TOOL_ADAPTERS.md` — how to adapt to a specific tool, plus a self-adapter for unknown tools
- `CLAUDE.md` — entry point + working rules for Claude Code
- `AGENTS.md` — entry point + working rules for Codex-style agents
- `prompts/` — reusable bootstrap / project-start / session-end / handoff / merge prompts

**Your content (fill in the blanks):**

- `YOU_CONTEXT.md` — who you are, how you want agents to work *(start here)*
- `YOU_PROJECTS.md` — live project index + status
- `YOU_TECH_STACK.md` — stack, commands, conventions, gotchas
- `YOU_CAREER.md` / `YOU_CREATIVE.md` — optional domain modules
- `YOU_PRIVATE.example.md` / `YOU_CAREER_PRIVATE.example.md` — copy → fill → stays local
- `projects/example-project/` — template for per-project context

---

## Design principles

- **Plain Markdown, no lock-in.** Every file is human-readable and tool-agnostic. No runtime, no install.
- **Order-independent.** Whichever tool touches the files first, you should converge on the same useful context. No tool's version is "primary."
- **Current state, not a transcript.** These files are a maintained source of truth, not a chat log. Keep them lean; update deliberately.
- **You decide.** Agents *propose* updates. They don't silently rewrite who you are.

---

## Using it? Say so

This repo is used far more than it is talked about, and the author cannot see how. If Context OS is in your workflow, two minutes helps:

- **[Tell me how you use it](https://github.com/DTM-repo/Context-OS/issues/new?template=using-it.md)** — which tools, what you changed, what you dropped.
- **[Report a gap or a bug](https://github.com/DTM-repo/Context-OS/issues/new?template=gap-or-bug.md)** — a tool that ignores the loader, a file that never earns its place.
- Star it if it saved you a warm-up. That is how other people find it.

## License

MIT — do whatever you want with it. Attribution appreciated, not required.

*Originally built and battle-tested as one person's personal cross-tool context system, then stripped to a reusable template.*
