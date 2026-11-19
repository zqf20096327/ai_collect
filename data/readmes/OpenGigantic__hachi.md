<div align="center">

# Hachi

**The governed personal agent**

_Safety, spend, and self-improvement enforced by code — not by vibes._

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Status: pre-release](https://img.shields.io/badge/status-pre--release-orange.svg)](#project-status)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-purple.svg)](https://docs.astral.sh/ruff/)
[![.og token savings: 97.6%](https://img.shields.io/badge/.og%20token%20savings-97.6%25-brightgreen)](docs/reference/benchmark.md)

</div>

---

## What is Hachi?

Every capability the agent has — or teaches itself — is a typed, versioned, lintable,
permission-scoped `.og` file you can diff and audit. Every token has a budget the loop enforces
mid-turn. Every shell command, path, URL, and memory write passes a guard that exists in source
code, not in a system prompt.

The architecture exists because two failure modes recur in 2026-era personal agents:
**marketplace poisoning** of third-party extensions, and **learning loops that rewrite the
agent's behaviour without supervision**. Hachi is built to make both structurally impossible.

| Problem | How Hachi solves it |
|:--------|:--------------------|
| **Runaway token spend** | Per-session _and_ per-turn cost/token caps enforced **between** LLM calls — the loop projects the next call's worst-case cost and refuses it before it starts. Lazy tool groups and prompt-cache-aware breakpoints keep the baseline low. The $47-echo-loop story is structurally impossible under a turn cap. |
| **Ungoverned self-learning** | `save_skill` bumps semver and appends a changelog instead of overwriting. Lint plus dense-budget rejection bounds what the agent may write. `::assertions` make learned procedures machine-checkable **before** execution. Your manual edits are never silently overwritten. |
| **Exposed attack surface** | The gateway binds loopback with bearer-token auth by default, and refuses to start unauthenticated on a public interface. `security-audit` runs as a CI gate. Permission tiers gate filesystem, shell and MCP at **call time** — not as runtime prompts the model can argue with. |
| **Skill library context bloat** | `.og` files are queryable at sub-file granularity: the agent reads a ~30-token routing index, then pulls only the node a task needs. [Measured: **97.6% fewer tokens** vs dump-all](docs/reference/benchmark.md) — given correct routing, with retrieval quality benchmarked separately. |

> **Honest scope caveat.** Below ~30 k tokens of total library content, a cached dump-all is
> competitive on token cost. ObjectGraph is built for libraries that grow past that threshold —
> sub-file node granularity matters when the library no longer fits in a single context window.
> The 97.6% figure assumes retrieval succeeded; it is not an average over arbitrary queries.

---

## At a glance

| | |
|:--|:--|
| **Format** | ObjectGraph `.og` — typed node graph · [spec](spec/og-spec-v1.0.md) · [conformance suite](spec/conformance/) · [paper](https://arxiv.org/abs/2604.27820) |
| **Loop** | ReAct with pre-flight budget enforcement, tool-group unlocking, and history compaction |
| **Skills** | 31 bundled · BM25 + optional embedding retrieval · semver + changelog on every write |
| **Tools** | 62 built-in — files, shell, browser, vision, voice, Google Workspace, Notion, Slack, MCP, scheduling, delegation |
| **Surfaces** | Textual TUI · FastAPI gateway (REST + SSE) · React web UI · Telegram / Slack / Discord / WhatsApp · OpenAI-compatible `/v1/chat/completions` |
| **Models** | Anthropic · OpenAI-compatible · OpenRouter · Groq · DeepSeek · Gemini · local Ollama |
| **Memory** | ChromaDB vault (facts + bounded user profile) · episodic recall · knowledge graph · nightly append-only gardener |
| **Engineering** | 4,300+ tests · `import-linter` layer contracts · CI on Linux / macOS / Windows · opt-in OpenTelemetry |

---

## Quickstart

Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/). No API key is needed to develop or to
run the test suite.

```bash
git clone https://github.com/OpenGigantic/hachi && cd hachi
uv sync
uv run hachi quickstart      # pick a provider, validate the key, choose a safety tier
uv run hachi                 # start chatting
```

`quickstart` validates your provider key **before** the first message instead of failing
mid-conversation. Prefer a one-shot? `uv run hachi run --once "summarise today's changes"`.

```bash
uv run hachi serve           # gateway + web UI on http://127.0.0.1:8787
uv run hachi doctor          # diagnostics: paths, provider, permissions, skills health
uv run hachi skill benchmark # reproduce the .og token-savings number
```

---

## The `.og` format

An agent does not read a document linearly — it retrieves. A `.og` file is built for that: a
routing index you can read for ~30 tokens, then only the node a task needs.

```og
::meta
  title: Software Engineer Sub-Agent
  version: 1.0.0
  scope: worker

::index
  # node-id             | type    | scope | conf | keywords
  identity              | concept | all   | 1.0  | persona, engineer
  execution-protocol    | concept | all   | 1.0  | rules, constraints

::node[execution-protocol]
->[:role=rule]
::dense
Never deviate from the assigned task. Read first, then act.
::steps
1. Read the files the task references
2. Execute with the minimum number of tool calls
::assertion
  trigger: after[write_file]
  check: file_exists == true
  on-fail: ->[:retry limit=1] current_step
::end
```

Three things follow from that structure, and they are the reason the governance works:

- **`::dense` / `::full` split** — the agent can decide it needs more before paying for it
- **`::assertion`** — preconditions are executable, so a learned procedure is checkable before
  it runs, not after it fails
- **`::changelog`** — a self-written skill is a versioned diff, never a silent overwrite

Spec: [`spec/og-spec-v1.0.md`](spec/og-spec-v1.0.md) · Conformance: [`spec/conformance/`](spec/conformance/) ·
Paper: [arXiv:2604.27820](https://arxiv.org/abs/2604.27820) _(first-party — our own paper)_

---

## Architecture

```
   CLI / TUI          Gateway (REST+SSE)      Channels            Web UI
       │                     │                   │                  │
       └─────────────────────┴─────────┬─────────┴──────────────────┘
                                       ▼
                            ┌─────────────────────┐
                            │    Orchestrator     │  session boot, wiring,
                            │                     │  shared services
                            └──────────┬──────────┘
                                       ▼
                            ┌─────────────────────┐
                            │   ExecutionLoop     │  reason → act → observe
                            │  ┌───────────────┐  │
                            │  │ budget checks │  │  pre-flight: refuses a call
                            │  │ compaction    │  │  that would cross the cap
                            │  └───────────────┘  │
                            └────┬───────────┬────┘
                                 │           │
                   ┌─────────────▼──┐   ┌────▼──────────────┐
                   │  ToolRegistry  │   │  BaseLLMClient    │
                   │   62 tools     │   │  any provider     │
                   └─────────────┬──┘   └───────────────────┘
                                 │
                   ┌─────────────▼──────────────────────────┐
                   │  Guards — always in the call path      │
                   │  PermissionGate · net_guard ·          │
                   │  MemoryGuard · untrusted_content       │
                   └────────────────────────────────────────┘
```

Module layering is enforced by `import-linter`, not convention: `cli`/`tui`/`channels` →
`gateway`/`client` → `core`/`og_engine`/`tools`. The engine cannot import the gateway; CI fails
if it tries. See [ARCHITECTURE.md](ARCHITECTURE.md).

---

## What's inside

<table>
<tr><td valign="top" width="50%">

**Governance**
- Permission tiers: `sandbox` / `guided` / `unrestricted`
- Call-time path and shell gating, SSRF guard
- Per-session **and** per-turn cost caps
- Daily spend ledger, per-sender rate limits
- Untrusted content spotlighting

**Skills & learning**
- 31 bundled `.og` skills
- `save_skill` → semver bump + changelog
- Lint + `::assertion` checks before execution
- Usage tracking, stale detection, graph view

</td><td valign="top" width="50%">

**Surfaces**
- Textual TUI with streaming and interrupt
- FastAPI gateway + React web UI
- Telegram, Slack, Discord, WhatsApp
- OpenAI-compatible `/v1/chat/completions`

**Integrations**
- Google Workspace (Gmail, Drive, Calendar)
- Notion, Slack, MCP servers
- Universal REST adapter driven by `.og`
- Browser automation, vision, voice

</td></tr>
</table>

Full reference: [docs/guides/](docs/guides/) — configuration, memory, cookbook, git sync.

---

## Security model

| Control | Behaviour |
|:--|:--|
| **Gateway auth** | Bearer token, `compare_digest`. `HACHI_GATEWAY_NO_AUTH=1` refuses to start on a non-loopback bind. Only `/`, `/health`, `/readiness` and the OAuth callback are unauthenticated. |
| **Fail-safe defaults** | A missing `device-permissions.og` drops to the `sandbox` tier. It never fails open. |
| **Credentials** | OS keyring; resolved lazily at call time, never at boot. |
| **Memory writes** | Untrusted content is quarantined and needs approval before entering long-term storage. |
| **CI** | `security-audit` + `pip-audit` gate pull requests; `bandit` runs advisory. |

> **Known gap:** CI does not yet scan the tracked tree for committed secrets —
> `security-audit` inspects the environment and resolved config, not files. Tracked as a
> release blocker.

Vulnerability disclosure: [SECURITY.md](SECURITY.md) · Conduct: [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)

---

## Project status

<a name="project-status"></a>

**Pre-release.** Not yet on PyPI and not yet public, so `pipx install hachi-og` and the
`curl | bash` one-liner **do not work today** — install from source as shown above. The first
public beta will be `v0.1.0`, accompanied by a changelog and a signed release.

What that means in practice: the CLI surface and the `.og` format are settling but may still
change between minor versions. Treat `0.x` minor bumps as potentially breaking.

---

## Documentation

| | |
|:--|:--|
| **[Configuration](docs/guides/configuration.md)** | Every environment variable and `settings.toml` key |
| **[Memory](docs/guides/memory.md)** | How Hachi remembers across turns and sessions |
| **[Cookbook](docs/guides/cookbook.md)** | Copy-paste recipes for common tasks |
| **[Benchmark](docs/reference/benchmark.md)** | Methodology behind the token-savings number |
| **[Decisions](docs/DECISIONS.md)** | Settled architectural choices and why |
| **[Bug bank](docs/bug-bank.md)** | 90+ regressions and the rule each one left behind |

`docs/DECISIONS.md` and `docs/bug-bank.md` are the two files that best explain how this project
thinks. They are kept current as a matter of policy.

---

## Contributing

```bash
uv run python scripts/preflight.py          # the gate: ruff, mypy, skill lint, eval, full pytest
uv run python scripts/preflight.py --quick  # fast inner loop
```

Read [CONTRIBUTING.md](CONTRIBUTING.md) first. The lowest-friction contribution is a new `.og`
skill — around 30 lines, no Python, linted in CI.

This project is developed with AI agents, so `CLAUDE.md`, `AGENTS.md` and `.claude/` are tracked
on purpose. You don't need any of it to contribute; `preflight.py` is the gate that matters.

## License

**Apache-2.0** — see [LICENSE](LICENSE) and [NOTICE](NOTICE). This is a permissive licence: you
may use, modify and redistribute Hachi, including commercially. The express patent grant (§3)
and the trademark carve-out (§6) are the reasons it was chosen over MIT.

The **name and logo are not licensed** — see [TRADEMARK.md](TRADEMARK.md). A fork is welcome;
calling it the official Hachi is not.

The `.og` specification and the arXiv paper are separate works (CC BY 4.0).
