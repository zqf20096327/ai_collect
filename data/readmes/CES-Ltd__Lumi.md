# Lumi

Native desktop AI agent platform written in Rust. It can run with Claude, Crush, GeminiCLI, HERMES, CURSOR
Cargo workspace with a GPUI shell on top, a fleet of `lumi-*` crates for storage / memory / dispatch / policy / audit / pricing / cron / skills underneath, and per-team Claude Code instances driven over MCP for tool calling.

![Chat workspace](apps/lumi-gpui/docs/media/01-chat.png)

## What it is

The user-facing piece is **[lumi-gpui](apps/lumi-gpui/)** — a single binary hosting ten task surfaces in a left-rail layout:

- **Chat** — lead conversation with streamed assistant text, tool-call bubbles, permission modals, slash commands (`/clear`, `/model`, `/runtime`, `/perm`, `/help`), file attachments, `@`-mention typeahead, and live sub-agent status mirroring.
- **Cowork** — skill-tile launcher that primes the composer with a domain-specific prompt.
- **Code** — repo browser + diff preview.
- **Creative** — ComfyUI supervisor controls (start / stop / restart / open).
- **Memory** — Search, Observations, Episodes, Knowledge (table + force-directed canvas), Drafts; with run-now buttons for the capture / consolidate / distil passes and side-by-side team compare.
- **Analytics** — per-team turn / token / USD rollups, daily stacked-bar chart, per-Epic table, and an Audit sub-tab with filter pills + substring search.
- **Sprint** — five-lane kanban grouped by Epic > Story > Task with collapsible epics and a status-pill click model.
- **Plans** — surfaced plan files with an inline "Open in Plans" prompt above the chat.
- **Agents** — roster panel for hiring / firing teammates against the active team.
- **Settings** — theme, working dir, heartbeat, MCP servers (list + add HTTP), security toggles, governance templates, budgets, memory pipeline knobs, state-git init / commit / remote / push, skills library.

![Team picker](apps/lumi-gpui/docs/media/02-team-picker.png)

## Demo

Short clip (~460 KB): [apps/lumi-gpui/docs/media/demo-short.mov](apps/lumi-gpui/docs/media/demo-short.mov)

Full walkthrough (~16 MB): [apps/lumi-gpui/docs/media/demo-full.mov](apps/lumi-gpui/docs/media/demo-full.mov)

## Running it

From the workspace root:

```bash
cargo run -p lumi-gpui
```

Release build:

```bash
cargo build -p lumi-gpui --release
./target/release/lumi-gpui
```

State lives under `~/.lumi-lyra/`:

- `teams.json` — team registry (default / cowork / creative are system teams; user teams are deletable from the picker).
- `gpui-ui-state.json` — last-active tab.
- `memory/` — per-team observations, episodes, KG triples, wiki drafts.
- `audit/` — JSONL audit log read by Analytics → Audit.
- `.git/` (optional) — state versioning, managed from Settings → State sync.

![Workspace overview](apps/lumi-gpui/docs/media/03-workspace.png)

## Repo layout

```
Lumi/
├── apps/
│   └── lumi-gpui/          — desktop binary (GPUI + gpui-component)
├── crates/
│   ├── lumi-audit          — JSONL audit log + reader
│   ├── lumi-auth           — auth & token wiring
│   ├── lumi-bridge         — runtime ↔ UI event bridge
│   ├── lumi-browse         — headless browser tool
│   ├── lumi-core           — engine types
│   ├── lumi-cron           — scheduled tasks
│   ├── lumi-dispatch       — sub-agent dispatch registry
│   ├── lumi-egress         — outbound network policy
│   ├── lumi-mcp            — MCP server scaffolding
│   ├── lumi-memory         — observations / episodes / KG / smart recall
│   ├── lumi-policy         — permission & budget engine
│   ├── lumi-pricing        — provider price tables
│   ├── lumi-providers      — Claude / Anthropic providers
│   ├── lumi-skills         — skill loader (seed + user dirs)
│   ├── lumi-storage        — team / session / sprint JSON storage
│   └── lumi-team           — persona merger
├── resources/seed/         — seed personas, skills, templates
└── docs/                   — design + spec docs
```

![Memory workspace](apps/lumi-gpui/docs/media/04-memory.png)

The lead Claude Code instance is launched per-team with an MCP config pointing at in-process servers (`memory_server`, `dispatch_server`, `persona_server`, `sprint_server`, `permission_server`, `skills_server`, `browse_server`, `payload_proxy_server`, `comfy_server`). Memory MCP only mounts when the active team has a `working_dir` set, and the config is rebuilt at conversation start — switch teams and `/clear` to pick up newly populated memory tools.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).
