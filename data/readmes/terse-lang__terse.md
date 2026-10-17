# TERSE

**Token-Efficient Representation Semantically Expressed**

TERSE is an AI-first, human-readable state format with a matching query/command syntax, designed to be:

* rich enough to store semantic information with minimal syntactic cruft in the way,
* easy to query precisely, to any needed depth,
* flexible enough to express complex state changes declaratively,
* file-based, and mappable to an object model for (de)serialization and mutation.

It is meant to be understood with minimal instruction, and to that end leans heavily on existing syntaxes.

> Status: pre-release. APIs and spec details may change before 1.0.

## A `.terse` file

```terse
# System(online)
## Agents
Accounting
Coding(prefers @System.Models.Astra)
## Models
Astra(Astra_v2_5; cost_M_usd: 1.5)
Zemma 7(Zem7; cost_M_usd: 3.0)
# Runs(by id; in-progress)
## 5783(date: 2026-12-23; completed)
### Result
"The primary answer was 42"
```

Containers (`#`/`##`/`###`) carry the hierarchy; objects are bare-name lines beneath them. Attributes ride in parentheses — bare **flags** for human descriptors (`online`, `completed`), **identifiers** (`cost_M_usd: 1.5`) when a machine will read them. `@` references point across the tree, and a bare quoted line is container text.

## Queries

Queries start with `?` and are read-only. Results are real TERSE — re-parseable, with ancestors preserved so location is always clear.

```terse
? System [DEPTH 1]
```

```terse
# System(online)
## Agents
## Models
```

```terse
? System.Agents.*
```

```terse
# System(online)
## Agents
Accounting
Coding(prefers @System.Models.Astra)
```

Read filters and slices ride in the bracketed tail and compose with `;` — for example `? System.Models.* [WHERE Its.cost_M_usd > 2]`, `[CONTAINS "answer"]`, `[WHEN 2026-12-23]`, `[LAST 5]`, `[DEPTH 2]`.

## Mutations

State changes are declarations: declare the shape and the changes, and everything unmentioned stays put — bare order does not reorder, omitted attributes do not clear.

```terse
# System.Agents
Marketing(use any model)
# System.Models
Brain(Brain_5_thinking; cost_M_usd: 4.25) [FIRST]   // ordering is state; place explicitly when it matters
## Retired                                          // declaring a container creates it
? System.Models.Astra(deprecated) [MERGED; MOVED]   // query inside a declaration: pull Astra here, tagging it on the way
```

Applying that to the file above yields:

```terse
# System(online)
## Agents
Accounting
Coding(prefers @System.Models.Astra)
Marketing(use any model)
## Models
Brain(Brain_5_thinking; cost_M_usd: 4.25)
Zemma 7(Zem7; cost_M_usd: 3.0)
### Retired
Astra(Astra_v2_5; cost_M_usd: 1.5; deprecated)
# Runs(by id; in-progress)
## 5783(date: 2026-12-23; completed)
### Result
"The primary answer was 42"
```

Directives are bracketed tails at end of line, always capitalized: placement (`FIRST`, `LAST`, `BEFORE x`, `AFTER x`), rename (`WAS`), removal (`REMOVED`), attribute merging (`MERGED`), read filters (`WHERE`, `WHEN`, `CONTAINS`, `DEPTH`), slices (`FIRST n` / `LAST n`), and command modes (`NEW`, `FILL`, `MOVED`, `AS`). A concise set that composes to change, move, rename, or copy state in bulk with minimal declaration.

## What's here

| Directory | Description |
|---|---|
| [`terse-spec/`](terse-spec/) | The language itself: [`TERSE.md`](terse-spec/TERSE.md) (the written-form guide — start here), `TERSE_Specification.md` (normative reference), and `syntax/` (token catalog, grammar, AST, parser states, semantic rules) |
| [`terse-py/`](terse-py/) | Python implementation — parser, AST, state tree, library API, and CLI (`validate`, `parse`, `fmt`, `query`, `apply`). Zero runtime dependencies, file-backed; the engine underneath `terse-mcp` |
| [`terse-mcp/`](terse-mcp/) | MCP server exposing a TERSE state store as two tools — `terse_command` (one call, two channels: `declarations` for mutations + `queries` for reads) and `terse_info` (introspection) — plus the spec on demand as MCP resources (`terse://spec/quickstart`, `terse://spec/full`) |
| [`terse-integrations/`](terse-integrations/) | Per-host glue: the Claude Code / Cowork plugin (which also installs as an OpenClaw bundle), plus Grok, Hermes, and OpenClaw wiring |
| [`apps/terse-brain/`](apps/terse-brain/) | Karpathy-style LLM wiki on TERSE — the `brain` namespace, `register-source`, lint, and an interactive HTML graph. Personal knowledge base for a single operator + agent |
| [`apps/terse-memory/`](apps/terse-memory/) | Durable agent memory on TERSE — the `memory` namespace, `init`/`wire`/`setup`/`doctor`, and a policy-in-the-store protocol so every MCP host reads the same rules |
| [`apps/terse-browser/`](terse-browser/) | Chatlog-style operator UI over the same three operations the AI uses (work in progress) |


## Quick start

New to TERSE? Start with [`terse-spec/TERSE.md`](terse-spec/TERSE.md). Wiring it into an MCP host? See [`terse-mcp/`](terse-mcp/).

### Claude Code / Cowork

This repo is also a Claude Code plugin marketplace. In a Claude Code session:

```
/plugin marketplace add terse-lang/terse
/plugin install terse@terse
```

That installs the [`terse`](terse-integrations/claude-plugin/) plugin, which launches [`terse-mcp`](terse-mcp/) over stdio and ships a `using-terse` skill. See [`terse-integrations/claude-plugin/README.md`](terse-integrations/claude-plugin/README.md) for configuration options (workspace, label, lock timeout, `TERSE_WORKSPACE`).

### OpenClaw / Grok / Hermes

The same plugin payload installs under OpenClaw as a Claude-format bundle (`openclaw plugins install`), and `terse-integrations/` carries wiring docs for [Grok CLI](terse-integrations/grok/), [Hermes](terse-integrations/hermes/), and [OpenClaw](terse-integrations/openclaw/).

## License

See individual subproject LICENSE files.