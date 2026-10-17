# agent-mux

Cross-engine dispatch layer for built-in harness adapters: codex, claude, gemini, experimental agy, and Grok Build CLI. One CLI, one JSON result contract, adapter boundary for more.

> **Go rewrite.** agent-mux was recently rewritten from TypeScript to Go -- static binary, goroutine-based supervision, no runtime dependencies.
> The TS version is preserved on the `agent-mux-ts` branch.
> See [docs/](docs/) for the full technical reference.

## What It Does

AI coding harnesses (Codex, Claude Code, Gemini CLI, experimental agy, and Grok Build CLI) are powerful but isolated -- each has its own CLI flags, event format, sandbox model, and session lifecycle. agent-mux connects them through one JSON contract and prompt-driven worker identity.

Workers are defined as markdown files with YAML frontmatter. The prompt is the worker. No config files, no role tables, no indirection.

## Core Principles

1. **Tool, not orchestrator.** The calling LLM decides what to do. agent-mux handles the how.
2. **Job done is holy.** Artifacts persist across timeout and process death. Every dispatch has an artifact path.
3. **Errors are steering signals.** Every error tells the caller what failed, why, and what to try next.
4. **Single-shot with curated context.** One well-prompted dispatch beats a swarm of under-specified workers.
5. **Prompt over config.** Worker identity lives in `.md` files with frontmatter defaults. The binary is generic.
6. **Simplest viable dispatch.** CLI flags > frontmatter > hardcoded defaults. Escalate only when needed.

## Quick Start

Package-manager install:

```bash
brew install buildoak/tap/agent-mux
go install github.com/buildoak/agent-mux/cmd/agent-mux@latest
```

After any package-manager install, start with:

```bash
agent-mux onboard
```

`agent-mux onboard --dry-run` explains the setup flow without changing files or
dispatching workers. It tells the installing agent to use the latest
agent-mux skill and references from:

```text
https://github.com/buildoak/agent-mux/tree/main/skill
https://github.com/buildoak/agent-mux/blob/main/skill/SKILL.md
https://github.com/buildoak/agent-mux/blob/main/skill/references/first-run.md
https://github.com/buildoak/agent-mux/blob/main/skill/references/config-and-profiles.md
```

For the full agent-first launch sequence, see
[skill/references/first-run.md](skill/references/first-run.md).

Source install from a checkout:

```bash
git clone https://github.com/buildoak/agent-mux && cd agent-mux
go build -o agent-mux ./cmd/agent-mux
./agent-mux --version
```

`--version` returns JSON with the version string plus installed-binary
provenance: resolved executable path, Go build/module metadata, VCS metadata
when available, and Go version.

**See what workers are available:**

```bash
./agent-mux config prompts
./agent-mux config prompts --json
./agent-mux config engines
./agent-mux config engines --json
./agent-mux config engines --refresh-models --engine agy --json   # explicit agy model-cache refresh
./agent-mux config engines --refresh-models --engine grok --json  # explicit Grok model-cache refresh
```

`config prompts` reflects your local `~/.agent-mux/prompts/` directory. `config engines --json` is the active engine/model/capability source of truth for dispatch validation. For Codex, it queries the PATH-resolved CLI once per process: live `codex debug models`, bundled catalog on failure, then a conservative legacy fallback. Successful catalogs replace one another; they are never unioned.

**GPT-5.6 Sol Max and Ultra** require an explicit model and a live or bundled catalog that proves the requested tier:

```bash
./agent-mux preview -E codex -m gpt-5.6-sol -e max -C /repo "Hard bounded task"
./agent-mux -E codex -m gpt-5.6-sol -e ultra -C /repo "Hardest bounded task"
```

Codex 0.144.1 reports Max and Ultra for Sol and Terra, Max for Luna, and only through xhigh for GPT-5.5/5.4/5.4-mini. Ultra may trigger native Codex collaboration, but agent-mux does not promise delegation. Tracked opt-in profile examples live in [examples/profiles](examples/profiles/); existing personal profiles are not changed.

**Profile-based dispatch** (engine, model, effort, timeout, system prompt all resolved from the profile):

```bash
./agent-mux -P=lifter -C /repo "Add retry logic to client.ts with exponential backoff"
```

**Minimal dispatch** (JSON via `--stdin` -- the canonical machine invocation):

```bash
printf '{"engine":"codex","prompt":"Review src/core.go for timeout edge cases","cwd":"/repo"}' \
  | ./agent-mux --stdin
```

`--stdin` is the canonical machine invocation and implies `--yes`, so it does
not stop for interactive preview confirmation unless the caller chooses a
different mode.

**Async dispatch** (fire, collect later):

```bash
./agent-mux -P=lifter --async -C /repo "Implement retries in client.ts" > /tmp/agent-mux-ack.json
ID=$(jq -r .dispatch_id < /tmp/agent-mux-ack.json)

./agent-mux wait "$ID"
./agent-mux result "$ID" --json
```

Dispatch output is always a single JSON object on stdout. Lifecycle subcommands (`list`, `status`, `result`, `inspect`, `wait`) default to human-readable but accept `--json`. stderr carries NDJSON event stream and heartbeat lines.

## Profiles

Worker identity lives in `~/.agent-mux/prompts/<name>.md`. Each file is a markdown document with optional YAML frontmatter that sets dispatch defaults:

```markdown
---
engine: codex
model: gpt-5.4
effort: high
timeout: 1800
description: "Scoped implementation with built-in verification"
---

# Lifter

You are a lifter. You build what was specified, verify it works, and report back.
...
```

`-P=lifter` loads `~/.agent-mux/prompts/lifter.md`, applies frontmatter defaults, and injects the markdown body as the system prompt.

`DispatchSpec.Effort` is the canonical depth field and defaults to `high`. Codex initial and resume commands forward that same value. `--reasoning` remains a deprecated alias for one release; differing explicit `--effort` and `--reasoning` values fail preflight.

**Resolution order** (later wins): hardcoded defaults -> frontmatter -> CLI flags / JSON fields. Explicit flags always override frontmatter.

`agent-mux config prompts` discovers all profiles with full metadata. `agent-mux config prompts --json` emits the catalog as a JSON array for programmatic consumption.

## Engines

| Engine | Resume | Structured events | Activity/tokens | Steering | Multimodal/image |
|--------|--------|-------------------|-----------------|----------|------------------|
| `codex` | yes | yes | activity + tokens, no cost | inbox resume / abort | no |
| `claude` | yes | yes | activity + tokens, no cost | inbox resume / abort | no |
| `gemini` | yes, UUID may fall back to latest | yes | activity + tokens, no cost | inbox resume / abort | no |
| `agy` | yes, after `agy.log` conversation ID | no, plain stdout | no structured activity/tokens/cost | inbox + `--conversation`, not live interrupt | smoke-verified, provider/model-dependent |
| `grok` | yes, exact predeclared UUID | yes, headless streaming JSON | no structured activity/tokens/cost | inbox resume / abort | no |

Engine CLIs must be installed separately -- agent-mux dispatches to them, it does not bundle them.

`agy` is CLI-first experimental support. agent-mux internally invokes the local `agy` CLI with its fixed `--sandbox`, rejects operator-supplied portable sandbox/permission/reasoning/max-turn/full-access options, stores provider diagnostics in private `agy.log`, and does not imply plugins, MCP, browser automation, Google services, or provider service actions.

`grok` is Grok Build CLI support through a conservative headless contract. The current built-in default is `grok-4.5`, verified against Grok CLI `0.2.93`; refresh the allowlist with `agent-mux config engines --refresh-models --engine grok --json` after Grok CLI updates. The default v1 path remains adapter-owned `--prompt-file` plus `--output-format streaming-json`; agent-mux writes private prompt/session/debug sidecars, predeclares an exact UUID session for resume, omits native sandbox flags by default, disables native subagents, memory, auto-update, alt-screen, web search, image/multimodal surfaces, custom sandbox policy, and native allow/deny rules. It accepts model, effort, explicit supported Grok sandbox profiles including `off`, and opt-in AgentMUX-owned v1.5 report controls. For v1.5, `grok-worker-report-schema=agent-mux.worker-report.v1` requests a text/code-only structured worker report over the same private prompt-file transport; `worker_report.json` is the sanitized canonical public artifact, while `grok_prompt.md` and resume prompt sidecars stay private. Raw native `prompt-json` and `json-schema` are not user-facing passthrough options. The v1.5 report path is fake-covered for bounded text-only worker reports and live-smoke-proven on Grok CLI 0.2.93 for bounded text dispatch, but it remains opt-in and does not imply media, search, tools, ACP, MCP, plugins, memory, or subagents. Explicit add-dir, permission-mode, reasoning, full-access, max-turns, web/X, image, native allow/deny, plugin/MCP/hook, trace/export, debug-file, best-of-n, subagent, and memory controls are rejected. It does not claim X search, web search, image input/output, structured tool telemetry, token usage, cost usage, or GAAL-native session indexing.

## Features

- **Profile-based dispatch** -- `-P=<name>` loads engine, model, effort, timeout, skills, and system prompt from a single markdown file. One flag replaces six.
- **Recovery and signals** -- Start a follow-up dispatch with `--recover=<id>` to include prior context. Live nudge/redirect require a live FIFO or resume-capable engine; agy uses resume-backed inbox delivery after its Antigravity conversation ID is discovered.
- **Two-phase timeout** -- Soft timeout fires a wrap-up signal when the adapter supports it, grace period allows clean exit, hard timeout kills. Agy uses plain stdout and does not receive a soft-timeout wrap-up prompt. Artifacts are preserved at every phase.
- **Async dispatch** -- Fire and forget with `--async`. Collect results later with `wait` or `result`.
- **Event streaming** -- Event-stream engines emit NDJSON on stderr, but event richness is adapter-specific. Codex, Claude, and Gemini can surface structured tool/file activity; Grok exposes headless text/error/end events without structured tool/file telemetry; Agy is plain stdout only.
- **Hooks** -- Pattern-based deny/warn rules evaluated on harness events.
- **Skill injection** -- Load `SKILL.md` runbooks into the dispatch prompt. Skills carry scripts, references, and setup.
- **Timeout and diagnostics** -- Global dispatch timeout is the sole hard backstop. Workers are trusted to complete within their timeout. 5-second watchdog cycle updates `status.json` for live observability. Process-group signals ensure grandchildren die with the harness. Forensic tools (`status.json`, `events.jsonl`, `steer nudge`) replace automatic kills for silent-worker diagnosis.
- **Durable persistence** -- Every dispatch writes `meta.json` and `result.json` under `~/.agent-mux/dispatches/<id>/`. Artifact directory created before the harness starts.
- **config prompts** -- `agent-mux config prompts` lists all discoverable profiles with engine, model, effort, timeout, and description.

## Authentication

| Engine | Personal use (OAuth) | Otherwise (`env var`) |
|--------|---------------------|----------------------|
| Codex | OAuth device auth via `codex auth` (`~/.codex/auth.json`) | `OPENAI_API_KEY` |
| Claude | OAuth via `claude` binary login (subscription) | `ANTHROPIC_API_KEY` |
| Gemini | `gcloud auth` application-default credentials | `GEMINI_API_KEY` |
| agy | Owned by the local `agy` CLI configuration | No agent-mux-managed fallback |
| Grok | Owned by the local `grok` CLI login | No agent-mux-managed fallback |

For personal use, OAuth tokens from your existing subscriptions are the primary
auth path -- no API keys needed. Set the env var when OAuth is not available.
agent-mux will attempt dispatch if any auth path is available --
`MISSING_API_KEY` is a warning, not a hard failure.

> **Note on the Claude engine:** agent-mux invokes the `claude` CLI binary
> directly -- it is not an SDK or API wrapper. For personal use with your own
> Claude Code subscription, OAuth login is the natural path. Set
> `ANTHROPIC_API_KEY` when OAuth is not an option.

## Documentation

| Doc | What |
|-----|------|
| [docs/](docs/) | Full technical reference -- architecture, config, dispatch lifecycle |
| [docs/agy.md](docs/agy.md) | Agy engine contract, limitations, model cache, steering, and AX gates |
| [docs/engines.md](docs/engines.md#grok-adapter) | Grok adapter contract, rejected native surfaces, resume, and artifact privacy |
| [SKILL.md](skill/SKILL.md) | Operational manual for AI agents using agent-mux |
| [first-run.md](skill/references/first-run.md) | Agent-first first-launch and onboarding reference |
| [BACKLOG.md](BACKLOG.md) | Open bugs, feature requests, spec gaps, and known limitations |
| [references/](skill/references/) | Engine comparison, prompting guide, output contract, config guides, installation |

## License

[MIT](./LICENSE)
