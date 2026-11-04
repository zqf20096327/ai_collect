# ⚓ memanchor

[![CI](https://github.com/AfridaMehanaz/memanchor/actions/workflows/ci.yml/badge.svg)](https://github.com/AfridaMehanaz/memanchor/actions/workflows/ci.yml)

**Persistent memory for coding agents that knows when it's out of date.**

Claude Code, Cursor and Codex forget everything between sessions. memanchor is a local
[MCP](https://modelcontextprotocol.io) server that lets them save what they learn (decisions,
conventions, gotchas) and recall it next time.

The difference: every memory is **anchored to the files it describes**. When those files change,
recall flags the memory as **STALE**, so the agent re-checks before acting on outdated knowledge.

```
> recall "jwt signing"

1 memory, 1 stale (verify before relying on them)

#4 [decision] (STALE: src/auth/keys.ts changed; tags: auth, jwt)
JWTs are signed with RS256 so other services can verify them with the public key only.
```

## Why

A wrong memory is worse than no memory. Most agent-memory tools store text and return it forever,
even after the code it describes has been rewritten. memanchor treats memory like a cache that
can be invalidated:

| | Plain notes / CLAUDE.md | Typical memory server | **memanchor** |
|---|---|---|---|
| Persists across sessions | ✅ | ✅ | ✅ |
| Searchable | grep | ✅ | ✅ BM25 + stemming |
| Knows when a memory may be outdated | ❌ | ❌ | ✅ file anchors |
| Scrubs secrets before saving | ❌ | rarely | ✅ |
| Bounded context cost | ❌ whole file | varies | ✅ token budget |
| Local, no cloud, no API key | ✅ | varies | ✅ |

## Features

- **Staleness detection.** `remember(files: [...])` stores a content hash of each file. `recall` re-hashes
  and marks memories whose files changed or were deleted. `confirm_memory` re-anchors after the agent
  re-checks. `list_memories(stale_only)` finds memories to clean up.
- **Secret redaction.** API keys (Anthropic, OpenAI, GitHub, AWS, Slack, Stripe, Google), JWTs,
  private keys, `password=` style assignments and credentials in connection strings are replaced with
  `[REDACTED:type]` before anything touches disk, and the agent is told what was scrubbed.
- **Relevance search.** SQLite FTS5 with porter stemming ("migrating" finds "migrations"), prefix
  matching, and tags weighted into the BM25 ranking.
- **Token budget.** Recall stops adding results at `max_tokens` (default 1500), so memory can't
  flood the context window.
- **Project isolation.** One database, scoped per git repository. Paths outside the project are rejected.
- **Deduplication.** Saving the same memory twice updates it instead of creating a copy.
- **Zero native dependencies.** Uses Node's built-in `node:sqlite`. Nothing to compile.

## Install

Requires Node.js 22.13 or later.

**Claude Code**

```bash
claude mcp add memanchor -- npx -y memanchor
```

**Cursor**: add to `.cursor/mcp.json`

```json
{
  "mcpServers": {
    "memanchor": { "command": "npx", "args": ["-y", "memanchor"] }
  }
}
```

**Any MCP client**: run `npx -y memanchor` as a stdio server.

The project is the git repository of the directory the server starts in. If your client starts
servers elsewhere, set `MEMANCHOR_PROJECT=/path/to/repo`. Memories are stored in
`~/.memanchor/memory.db`; override with `MEMANCHOR_DB`.

## Tools

| Tool | What it does |
|---|---|
| `remember(content, kind?, tags?, files?)` | Save a memory. `kind` is `decision`, `convention`, `gotcha`, `fact` or `todo`. `files` anchors it for staleness checks. |
| `recall(query?, kind?, limit?, max_tokens?)` | Ranked search; no query returns the most recent. Flags stale results. |
| `confirm_memory(id)` | The memory still holds after re-checking; re-anchor it to the current files. |
| `forget(id)` | Delete a wrong or obsolete memory. |
| `list_memories(kind?, stale_only?)` | Review everything, or just what needs re-checking. |

The server also sends MCP `instructions` telling the agent to recall at the start of a task,
remember what a future session would need, and verify stale memories before relying on them.

## CLI

For humans who want to see what their agent remembers:

```bash
npx memanchor list            # all memories for this repo
npx memanchor list --stale    # only ones whose files changed
npx memanchor search "auth"
npx memanchor stats
npx memanchor forget 12
```

## Evaluation

`npm run eval` measures whether recall puts the right memory first, on 24 memories from a fictional
e-commerce backend and 24 queries in three categories
([dataset](eval/recall-dataset.json)). The baseline is substring matching, which is roughly what
grepping a notes file gives you.

| system | category | queries | hit@1 | hit@3 | MRR |
|---|---|---|---|---|---|
| substring | keyword | 8 | 100% | 100% | 1.00 |
| substring | morphology | 8 | 50% | 63% | 0.59 |
| substring | paraphrase | 8 | 38% | 38% | 0.38 |
| **memanchor (BM25)** | keyword | 8 | 100% | 100% | 1.00 |
| **memanchor (BM25)** | morphology | 8 | **100%** | **100%** | **1.00** |
| **memanchor (BM25)** | paraphrase | 8 | 50% | 63% | 0.54 |
| substring | all | 24 | 63% | 67% | 0.66 |
| **memanchor (BM25)** | all | 24 | **83%** | **88%** | **0.85** |

Stemming and prefix matching fix word-form mismatches completely. **Paraphrases are the weak spot**:
"where is the app hosted" shares no words with "Production runs on AWS ECS Fargate". That's the
case for optional local embeddings (see roadmap). The dataset is small and hand-written, so treat
these numbers as a regression check, not a benchmark.

## Development

```bash
npm install
npm test        # type-check + 37 tests, including the built binary over stdio
npm run eval    # retrieval eval
```

Tests cover redaction patterns, staleness (changed, deleted, confirmed), dedup, path escapes,
project isolation, FTS query sanitising, the token budget, and every tool through a real MCP client.

## Roadmap

- Optional local embeddings (hybrid BM25 + vector) to close the paraphrase gap
- Anchor to symbols (a function, a config key) rather than whole files, so unrelated edits don't flag a memory
- Memory decay: down-rank memories that are never recalled
- Import existing `CLAUDE.md` / `.cursorrules` notes as memories

## License

MIT
