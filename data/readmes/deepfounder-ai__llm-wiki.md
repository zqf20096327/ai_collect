# llm-wiki

A Claude Code plugin that turns Claude into an active librarian for your own knowledge.

Instead of classic RAG (re-deriving answers on every query), Claude incrementally builds and
maintains a persistent markdown wiki that synthesizes sources over time. Based on
[Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

## What it gives you

- **`/llm-wiki:wiki-ingest`** — save a URL, file, or the current session into the wiki. Claude
  decides: update an existing page or create a new one. Keeps sources, cross-links, and an index
  in sync.
- **`/llm-wiki:wiki-query`** — ask the wiki a question. Claude answers from the most relevant
  pages and can persist the answer back.
- **Proactive saving** — when something worth remembering surfaces in conversation, Claude
  dispatches the `wiki-curator` sub-agent *without* waiting for a command.
- **Per-session memory hygiene** — a soft reminder every ~10 turns if nothing has been saved, and
  a "you had a substantive session with no ingest" prompt on the next session start.

## Install

```
/plugin marketplace add deepfounder-ai/llm-wiki
/plugin install llm-wiki
```

Restart your Claude Code session after install so the SessionStart hook picks up.

## First run

```
/llm-wiki:wiki-ingest --global https://some-article-you-want-to-keep
```

Claude will create `~/.claude/wiki/` on first use, download the source into `sources/`, and write
the first page under `pages/`. The global wiki is shared across all your Claude Code projects; an
optional per-project wiki lives at `<project>/wiki/` — the plugin auto-routes writes between them
based on content.

## How it works

Three layers (as in the source gist):

1. **Raw sources** — immutable. URL copies in `sources/`, local files by reference.
2. **The wiki** — `pages/<slug>.md` with YAML frontmatter; a `wiki-curator` sub-agent is the sole
   writer.
3. **The schema** — `schema.md` per scope tells the curator how to maintain the wiki (naming,
   page types, writing rules, linking conventions).

Three hooks implement the "active librarian" behaviour:

- **SessionStart** injects a compact wiki index and a behavioural nudge ("use `wiki-curator`
  proactively, don't wait for a command").
- **UserPromptSubmit** counts turns per session and injects a soft reminder every N prompts if no
  ingest has happened.
- **SessionEnd** writes a "pending ingest" marker if the session was substantive and nothing was
  saved; the next SessionStart surfaces it.

Full design: [docs/superpowers/specs/2026-04-17-llm-wiki-plugin-design.md](docs/superpowers/specs/2026-04-17-llm-wiki-plugin-design.md).

## Configuration

Environment variables:

| Variable | Default | Effect |
|---|---|---|
| `LLM_WIKI_GLOBAL_PATH` | `~/.claude/wiki` | Where the global wiki lives. |
| `LLM_WIKI_REMIND_EVERY` | `10` | How often (in user prompts) the soft reminder fires. Set lower for a nudgier plugin. |

Hand-edit `~/.claude/wiki/schema.md` to change the curator's maintenance rules for your global
wiki. A project can have its own `wiki/schema.md` that augments the global one.

## Status

- **v0.1** — ingest, query, SessionStart index, curator sub-agent, schema templates, validator.
- **v0.2** — proactive-save nudge, periodic reminder hook, pending-ingest marker.
- **v0.3** (planned) — `/wiki-lint` (orphans, broken `related[]`, duplicates, stale sources),
  `/wiki-stats`, optional `/wiki-rename`.

## License

MIT — see [LICENSE](LICENSE).
