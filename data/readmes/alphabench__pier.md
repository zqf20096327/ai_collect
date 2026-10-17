# pier

**pier** is a terminal coding agent — an interactive CLI that plans, edits code, runs
commands, and drives an agentic tool loop, powered by models served through the Pier bridge
(with BYOK support). It's written in TypeScript and runs on [Bun](https://bun.sh), and it
ships as a single self-contained binary.

It aims for a fast, keyboard-first REPL with the slash-command and tool conventions users of
modern coding-agent CLIs will find familiar: a readline composer, streaming assistant output,
inline permission prompts, plan/auto/accept-edits modes, subagents, MCP, and project memory.

## Install

Prebuilt binaries install with one command (macOS/Linux):

```bash
curl -fsSL https://dl.piercode.com/stable/install.sh | sh
```

Or build from source (requires [Bun](https://bun.sh)):

```bash
bun install
bun run build            # → dist/pier  (single compiled binary)
```

## Quick start

```bash
pier login               # pair this device with your Pier account (device-code flow)
pier                     # open the interactive REPL
pier exec "…"            # run one task headlessly, streaming to stdout
```

During development you can run without compiling:

```bash
bun run dev              # === bun src/entry.ts
bun run dev login
```

Config lives in `~/.pier` by default (override with `PIER_HOME`). The bridge defaults to
`http://localhost:9000/v1` (override with `PIER_BASE_URL`; production is
`https://api.piercode.com/v1`).

## Commands

| Command       | What it does                                   |
| ------------- | ---------------------------------------------- |
| `pier`        | Open the interactive REPL (default)            |
| `pier exec …` | Run one task headlessly, streaming to stdout   |
| `pier resume` | Resume a saved conversation (`--list` to list) |
| `pier login`  | Pair this device with your Pier account        |
| `pier logout` | Clear saved credentials                        |
| `pier models` | List available models                          |
| `pier keys`   | Manage BYOK provider API keys                  |
| `pier update` | Check for a newer release                      |
| `pier doctor` | Check config, auth, and bridge reachability    |

## Custom instructions

pier ships with a strong built-in system prompt, but it's yours to shape. There are two ways to
influence what the model is told, and they compose:

**1. Layer on top — `CLAUDE.md` / `AGENTS.md` (recommended for most people).**
Drop a `CLAUDE.md` or `AGENTS.md` in your repo (or `$PIER_HOME/CLAUDE.md` for a personal, all-projects
note) and pier discovers it from the repo root down to your cwd, `@path` imports and all, and layers
it onto the session. Use this to teach pier your conventions, build/test commands, and house rules —
without touching the core agent behavior. This is always on and needs no config.

**2. Replace the base prompt — for power users who want to re-author the agent.**
Set an `instructions` key in `$PIER_HOME/config.json` (default `~/.pier/config.json`) to **fully
replace** pier's built-in base system prompt. The value is either a **path** to a `.md`/`.txt` file or
an **inline string**:

```jsonc
// ~/.pier/config.json
{
  "instructions": "~/.pier/my-agent.md"   // a file path (~ expands; relative paths resolve to cwd)
  // — or an inline prompt —
  // "instructions": "You are Ada, a meticulous Rust reviewer. ..."
}
```

Or point at a file with an environment variable (handy for scripting / per-invocation prompts), which
**takes precedence** over the config key:

```bash
PIER_INSTRUCTIONS_FILE=./prompts/reviewer.md pier exec "review my diff"
```

Precedence: `PIER_INSTRUCTIONS_FILE` → config `instructions` → the built-in default. A replaced base
still gets your `CLAUDE.md`/`AGENTS.md` layered on top, so you can override the core prompt and keep
your project notes. If a configured file is missing or unreadable, pier warns and falls back to the
default rather than failing your session.

> Subscription note: when you run through a Pier subscription, the bridge may add extra
> harness guidance on top of your base for an elevated experience. Running with your own API keys
> (BYOK) or your own bridge gives you the base prompt exactly as configured above — nothing hidden.

## Data handling & local mode

What leaves your machine: the model prompt for each turn (your instructions plus the code and
command output the agent reads, and your cwd/OS/git-branch context), sent over TLS to the Pier
bridge (subscription) or directly to your provider (BYOK). On a signed-in session, conversation
threads are also synced to your Pier account so `pier resume` works across devices.

To keep everything on-device, run with `--local` (disables thread sync and runs the Auto-mode
classifier locally for that session), or make it permanent:

```bash
pier config set threadSync false
```

The CLI has **no analytics and no crash reporting**. BYOK API keys are stored only on your machine
(`credentials.json`, mode 0600) and are never sent to Pier. Full details, retention windows, and
your rights: <https://www.piercode.com/privacy>.

## Features

- **Interactive REPL** — a readline composer (with an optional vim keymap), streaming assistant
  output, a live token/context footer, and an inline permission dialog.
- **Native tools** — Read/Write/Edit/MultiEdit, Grep/Glob, Bash (with background shells +
  `BashOutput`/`KillShell`), TodoWrite, Task (subagents), Skill, WebSearch/WebFetch, and
  apply_patch — each running through clean handlers with a permission gate.
- **Permission modes** — `default`, `plan`, `acceptEdits`, `auto`, and `bypassPermissions`,
  cycled with Shift-Tab. `auto` classifies would-be prompts and fails safe to a prompt on error.
- **OS-level sandboxing** — Bash runs inside a real OS sandbox (seatbelt on macOS, bubblewrap on
  Linux) sized to the active permission mode.
- **Project memory** — `CLAUDE.md` / `AGENTS.md` files (with recursive `@path` imports) are
  discovered from the repo root down to the cwd and prepended to the session.
- **Subagents, MCP, and skills** — built-in and disk-defined subagents, an MCP client
  (stdio + streamable-http), and SKILL.md-based skill bundles.
- **Slash & custom commands** — a built-in command set (`/help`, `/model`, `/mode`, `/compact`,
  `/init`, `/status`, …) plus custom commands loaded from `$PIER_HOME/commands/*.md`.
- **Context management** — client-side compaction (`/compact` + auto-compaction), microcompaction,
  and an optional per-turn token budget.
- **Resilience** — pre-first-token retry/backoff on transient errors and a once-per-turn model
  fallback.
- **Thread persistence** — every conversation is saved locally and resumable with `pier resume`.
  On a signed-in session, threads also sync to your Pier account (best-effort) so you can resume
  them on other devices.
- **Rendered transcript** — markdown rendering with theme-aware syntax highlighting, structured
  add/remove diffs for edits, collapsible tool output, a live todo checklist, and image support.

## Architecture

The CLI speaks only the OpenAI **Responses** API; the Pier Go bridge translates to the
underlying Chat Completions provider. The code is organized by concern:

- `src/protocol/` — Responses wire types (`items.ts`), the model catalog (`models.ts` + bundled
  `models_catalog.json`), and approval/sandbox types.
- `src/bridge/` — the model client: `sse.ts` (frame parser), `events.ts` (ordering-invariant
  validator), `client.ts` (POST /v1/responses), `models.ts` (GET /v1/models).
- `src/auth/` — device pairing + token storage.
- `src/engine/` — the turn loop: `callModel.ts` is the model seam;
  `translate-in.ts`/`translate-out.ts` convert between the internal content-block model and
  Responses items/SSE; `turn.ts` is the agentic loop (approval gate + hooks); `exec.ts` is the
  headless path; plus compaction, retry, and fallback.
- `src/tools/native/` — the native tool set; `registry.ts` filters tools by permission mode.
- `src/safety/` — the permission engine, sandbox adapter, and trust model.
- `src/hooks/` — lifecycle hooks (`SessionStart`, `UserPromptSubmit`, `PreToolUse`,
  `PostToolUse`, `Stop`).
- `src/agents/`, `src/skills/`, `src/mcp/`, `src/commands/`, `src/context/` — subagents, skills,
  MCP, slash/custom commands, and project memory.
- `src/ink.ts` — a small facade over the real [`ink`](https://github.com/vadimdemedes/ink)
  renderer, the theme-aware Box/Text layer (`src/components/design-system/`), and pier's
  terminal extensions (`src/terminal/`: ANSI rendering, hyperlinks, clipboard, titled panes,
  terminal title).
- `src/tui/` — the REPL: composer, transcript cells, spinner/footer, dialogs, and onboarding.

## Development

```bash
bun install
bun test             # unit tests
bun run typecheck    # tsc --noEmit
bun run lint         # biome
bun run build        # bun build --compile → dist/pier (single binary)
```

See [CONTRIBUTING.md](./CONTRIBUTING.md) for more, and [RELEASE.md](./RELEASE.md) for how
releases are cut and published.

## License

pier is **source-available** under the [Business Source License 1.1](./LICENSE). In plain
terms: you're free to read, build, modify, and use pier — including in production and at
work. What you may not do is offer pier itself (or a derivative of it) to third parties as
a competing product or service — rebranding and redistributing it as your own product, or
selling it as a hosted service. Every copy must also carry the same license, so it can't be
relicensed. On the change date each version converts to the Apache License 2.0. See
[LICENSE](./LICENSE) for the exact terms.
