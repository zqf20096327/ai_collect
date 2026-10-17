# hermes-gbrain-bridge

> A small, dependency-free bridge that converts scattered agent memory (Hermes, Claude Code, Codex, OpenClaw) into clean markdown for [gBrain](https://github.com/garrytan/gbrain) to ingest.

> 🇹🇼 繁體中文版本：[README.zh-TW.md](README.zh-TW.md)

Most agent tools write memory in their own format — JSONL event streams, flat-key text, SQLite. gBrain only imports markdown. If you want one searchable brain across everything you've ever asked an agent, you need a bridge. This is that bridge.

---

## Why this exists

On one normal developer machine, agent memory lives in at least **five** different places — each in its own format:

| Tool | Location | Format |
|------|----------|--------|
| [Hermes](https://github.com/NousResearch/hermes-agent) | `~/.hermes/sessions/*.jsonl` + `memories/*.md` | JSONL + `§`-delimited markdown |
| Claude Code | `~/.claude/projects/<path-hash>/*.jsonl` | Event stream JSONL |
| Codex CLI | `~/.codex/sessions/**/*.jsonl` | JSONL with `session_meta` header |
| OpenClaw archive | `~/.openclaw.pre-migration/workspace/**/*.md` | Markdown with legacy paths |
| Conductor workspaces | Encoded into the Claude Code path | Same as Claude Code |

gBrain is an excellent knowledge brain, but out of the box it only reads markdown. You don't want to lose the last three years of conversations just because they're in the wrong container. This repo is the converter that makes them ingestible — one command per source, with mtime windows, size floors, secret redaction, and a canonical event format under the hood.

---

## Architecture

```
┌──────────────────────────────────┐       ┌───────────────────────┐
│        Local machine             │       │   Cloud (Railway)     │
│                                  │       │                       │
│  ~/.hermes/sessions/             │       │   Postgres            │
│  ~/.hermes/memories/             │─┐     │   + pgvector          │
│  ~/.claude/projects/             │ │     │   + pg_trgm           │
│  ~/.codex/sessions/              │ │     │                       │
│  ~/.openclaw.pre-migration/      │ │     │   gBrain schema:      │
│                                  │ │     │    pages              │
│  ┌──────────────────────────┐    │ │     │    content_chunks     │
│  │ hermes-gbrain-bridge     │    │ │     │    timeline_entries   │
│  │  discover → filter →     │◀───┘ │     │    ...                │
│  │  adapt → redact →        │      │     │                       │
│  │  canonical event →       │      │     │                       │
│  │  markdown (one per src)  │      │     │                       │
│  └──────────────────────────┘      │     │                       │
│           │                        │     │                       │
│           ▼                        │     │                       │
│  /tmp/gbrain-staging/*.md          │     │                       │
│           │                        │     │                       │
│           ▼                        │     │                       │
│  gbrain import → embed ────────────┼────▶│                       │
│  gbrain query / serve ◀────────────┼─────│                       │
└────────────────────────────────────┘     └───────────────────────┘
```

The bridge never touches the database directly. It only produces markdown files. gBrain handles ingestion, chunking, embedding, and storage. This keeps the bridge small and the blast radius tight: if the bridge has a bug, the worst it can do is produce bad markdown in a staging dir — your brain stays safe.

---

## Quickstart

```bash
# 1. Clone and install
git clone https://github.com/howardpen9/hermes-gbrain-bridge
cd hermes-gbrain-bridge
bun install

# 2. See what's out there before committing to anything
bun run src/cli.ts discover --days 30

# 3. Dry-run the source you want to ingest
bun run src/cli.ts export --source=claude-code --dry-run --days 30

# 4. Export for real to a staging directory
bun run src/cli.ts export --source=all --out=/tmp/gbrain-staging --days 30

# 5. Hand it to gBrain
gbrain import /tmp/gbrain-staging --no-embed
gbrain embed --stale    # requires OPENAI_API_KEY
gbrain query "What was the Railway deployment decision for PredictMe?"
```

For the complete walkthrough — provisioning Railway, installing gBrain, setting up keys, connecting the MCP server — see [**docs/SETUP.md**](docs/SETUP.md).

To add an adapter for a new memory source, see [**docs/EXTENDING.md**](docs/EXTENDING.md).

---

## Supported sources

| Source | Path | Status | Notes |
|--------|------|--------|-------|
| Hermes sessions | `~/.hermes/sessions/*.jsonl` | ✅ | One md per session, tool schemas stripped |
| Hermes long-term memory | `~/.hermes/memories/MEMORY.md` | ✅ | Pass-through, `§`-delimited entries |
| Hermes user profile | `~/.hermes/memories/USER.md` | ✅ | Pass-through |
| Claude Code sessions | `~/.claude/projects/**/*.jsonl` | ✅ | `user` / `assistant` turns only; event noise stripped |
| Codex sessions | `~/.codex/sessions/**/*.jsonl` | ✅ | `session_meta` + typed role payloads |
| OpenClaw workspace archive | `~/.openclaw.pre-migration/workspace/**/*.md` | ✅ | Pass-through with mtime + min-size filter |
| OpenClaw memory DBs | `~/.openclaw/memory/*.sqlite` | 🚧 | Requires SQLite reader |
| Gemini CLI history | `~/.gemini/` | 🚧 | Not yet |
| Kimi CLI history | `~/.kimi/` | 🚧 | Not yet |
| Slock agent memory | `~/.slock/agents/*/MEMORY.md` + `notes/` | 🚧 | Not yet |

Want to add one? Read [`docs/EXTENDING.md`](docs/EXTENDING.md) — the adapter interface is ~100 lines of TypeScript.

---

## Case study: one developer's brain, end to end

We ran this bridge on a working developer's machine (Hermes + Claude Code + Codex + OpenClaw archive, 30-day mtime window for the live sources, 1-year window for the archive) and pushed everything into gBrain on Railway Postgres. Real numbers:

| Metric | Value |
|--------|-------|
| Sources enabled | 4 (Hermes, Claude Code, Codex, OpenClaw archive) |
| Raw input — Claude Code jsonl | 1,988 files / 1.4 GB |
| Raw input — Codex jsonl | 636 files / 123 MB |
| Raw input — OpenClaw md (1 year, ≥1 KB) | 1,148 files / 9.6 MB |
| Raw input — Hermes | 4 files / 104 KB |
| **After bridge filter + conversion** | **3,775 markdown docs** |
| Pages in gBrain after dedup | 3,762 |
| Chunks produced | 57,627 |
| Embeddings (text-embedding-3-large) | 57,627 / 57,627 ✅ |
| Total embedding cost | **< $2** |
| Total ingest time (import + embed) | ~55 minutes |
| DB size on Railway | ~400 MB |

The most striking number: Claude Code raw jsonl was **1.4 GB**, but after filtering event-stream noise (`progress`, `queue-operation`, `tool_use` plumbing) and keeping only user/assistant turns, it dropped to **~200 MB** of useful markdown. That filter is the difference between a $50 embedding bill for useless noise and a $2 bill for actual conversation content.

---

## What we learned

Lessons from building this bridge for a real multi-agent setup that saved us weeks of rework and a meaningful chunk of embedding spend. If you're building something similar, read this before you write adapters.

1. **gBrain imports markdown — everything else needs a bridge.** Don't expect gBrain to parse your agent's native format. Every non-markdown source (JSONL, SQLite, event streams, proprietary session formats) needs a converter. Budget for this up front.

2. **"Agent memory" is a discovery problem, not an adapter problem.** On one machine we found agent memory in 5+ scattered locations: global Claude Code, global Codex, Hermes sessions, Conductor workspaces (encoded in the Claude Code path), and a pre-migration archive. Start every bridge project with a `discover` step that reports counts per source. Don't start writing adapters until you know what you're actually up against.

3. **Per-project `.claude/` folders do not contain sessions.** Claude Code always writes session jsonls to `~/.claude/projects/<encoded-path>/` regardless of where you launched it. The per-project `.claude/` folder holds `CLAUDE.md` and `settings.json` only. Don't waste time walking project trees — the path-encoded directory name under the global `projects/` dir **is** the workspace identifier.

4. **Claude Code jsonl is an event stream, and 90% of it is noise.** Event types include `progress`, `queue-operation`, `tool_use`, `tool_result`, `user`, and `assistant`. Only the last two are conversation. Our aggressive filter dropped 1.4 GB of raw jsonl to ~200 MB of useful markdown — the rest was tool plumbing and queue events nobody ever needs to semantically search.

5. **Volume explodes faster than your intuition.** 30 days of normal usage on one machine produced ~2,000 Claude Code sessions and ~600 Codex sessions. Always enforce an mtime window **and** a size floor before running any ingest loop. "Just grab everything" becomes a $50 surprise invoice from OpenAI.

6. **Codex's session format is cleaner than Claude Code's.** Codex has a single `session_meta` event first (with `cwd`, `model`, `id`), then typed `payload.role` events. Claude Code nests content under `message.content` which may be a string, an array of parts, or an array containing `tool_use` / `tool_result` objects you need to unwrap. Write Codex first if you want an easy win; save Claude Code for when you're warmed up.

7. **Pre-migration archives defeat mtime filters.** Our `~/.openclaw.pre-migration/` was 2.1 GB but only 2 files matched a 30-day mtime — because the whole archive is, by definition, old. Historical archives need their own policy: relax mtime to 1 year, enforce a size floor (we used 1 KB), and treat them as cold-storage ingest rather than daily sync.

8. **Embedding cost is tractable — but chunker quality is the real bottleneck.** 57k chunks at `text-embedding-3-large` cost us under $2. That's not the problem. The problem is that default recursive chunking produces broad chunks, so cosine similarity for obvious queries sits around 0.03–0.07. You are paying full price for mediocre recall. LLM-based semantic chunking is where the embedding spend actually earns its keep; without it, you might as well grep.

9. **High-volume sources drown out low-volume ones in semantic search.** In our case, Claude Code contributed 53,191 of 57,627 chunks — **92%** of the brain. Semantic queries for things that clearly live in Hermes memory (e.g. "What's my timezone?") returned Claude Code sessions instead, because the sheer volume of Claude Code chunks dominated the ranking. If your sources are that imbalanced, plan for per-source weighting, source-filtered queries, or multiple brains.

---

## Design principles

- **Discovery before adapters.** Always produce a count-per-source report before writing any conversion code. The actual distribution is never what you expect.
- **One file in, one file out.** Every source session produces exactly one markdown file. This keeps import, dedup, and re-run logic trivial.
- **Canonical event as the middle format.** Every adapter emits the same `CanonicalEvent` shape before markdown serialization. Swap the output format later without touching adapters.
- **Safe by default.** Mtime windows, size floors, and secret redaction are on by default. You have to explicitly lift them.
- **Zero runtime dependencies.** Pure Bun/TS + Node stdlib. Installs in under a second. No supply-chain surface.
- **The bridge never touches the database.** Only gBrain writes to Postgres. The bridge only produces files.

---

## Security

Secrets matching common patterns — `sk-*`, `xoxb-*`, `ghp_*`, `AKIA*`, `postgres://`, etc. — are redacted before export. The redaction list is intentionally conservative, not exhaustive. **Review your staging directory before importing to a shared brain.** See `src/normalize.ts` for the exact patterns.

Secret redaction is applied at the canonical-event layer so every adapter gets it for free. When you add a new adapter, you don't need to think about secrets — just call `redactSecrets(text)` once in your conversion path.

---

## Project status

This is a working MVP used daily on one developer's machine. It is not a polished product — it is a recipe, a set of adapters, and a lessons document. The code is deliberately small so you can read all of it in one sitting and adapt it to your own agent stack.

Contributions are welcome, especially new adapters. See [`docs/EXTENDING.md`](docs/EXTENDING.md).

---

## Connecting AI tools to your brain

Once gBrain is ingested and running, the next question is: how do other coding AI tools access it?

### MCP-based integration (recommended)

gBrain ships an MCP server (`gbrain serve`) that speaks the stdio protocol. Any tool that supports MCP can connect directly — the AI gets 30 tools (search, query, get_page, put_page, list_pages, add_timeline_entry, traverse_graph, etc.) and knows how to use them from the tool definitions alone.

```bash
# Claude Code — register once, available in all future sessions
claude mcp add gbrain -s user -- \
  /path/to/.bun/bin/bun run /path/to/gbrain/src/cli.ts serve
```

| Tool | How to connect | Notes |
|------|----------------|-------|
| Claude Code | `claude mcp add gbrain -s user -- bun run gbrain/src/cli.ts serve` | ✅ stdio MCP, 30 tools auto-discovered |
| Claude Desktop | Add to `claude_desktop_config.json` | See gBrain's [`docs/mcp/CLAUDE_DESKTOP.md`](https://github.com/garrytan/gbrain/blob/main/docs/mcp/CLAUDE_DESKTOP.md) |
| Cursor / Windsurf | Both support MCP — use the same stdio config | `bun run gbrain/src/cli.ts serve` |
| Codex CLI | No MCP support — use CLI in base instructions | See below |
| Gemini CLI / Kimi | No MCP support — use CLI or HTTP endpoint | See below |

### CLI-based integration (for tools without MCP)

If your AI tool can run shell commands but doesn't support MCP, add this snippet to its system prompt, `CLAUDE.md`, `AGENTS.md`, or base instructions:

```markdown
## Knowledge Brain
You have access to a gBrain knowledge base via CLI.
- Search: `gbrain search "keyword"`
- Semantic query: `gbrain query "question"`
- Read a page: `gbrain get <slug>`
- List pages: `gbrain list`
Use these commands when you need historical context about past decisions,
conversations, or project details.
```

The AI will learn to shell out to `gbrain` when it needs historical context. Not as seamless as MCP (it has to parse CLI output instead of structured tool responses), but it works across any agent that can run Bash.

### HTTP endpoint (for remote agents or webhooks)

If you need programmatic access from a remote service, gBrain also supports a remote MCP deployment via Supabase Edge Functions. See gBrain's [`docs/mcp/DEPLOY.md`](https://github.com/garrytan/gbrain/blob/main/docs/mcp/DEPLOY.md). This gives you an HTTPS endpoint that any HTTP client can call — useful for Telegram bots, CI pipelines, or agents running on other machines.

---

## License

MIT — same as gBrain.
