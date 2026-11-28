# mcp-shield

[![codecov](https://codecov.io/gh/gravion-ux/mcp-shield/branch/main/graph/badge.svg)](https://codecov.io/gh/gravion-ux/mcp-shield)
[![CI](https://github.com/gravion-ux/mcp-shield/actions/workflows/ci.yml/badge.svg)](https://github.com/gravion-ux/mcp-shield/actions/workflows/ci.yml)

> **Status: Active** — maintained flagship. New checks are welcome when
> they are static, deterministic, and covered by tests.

![Demo](docs/demo.png)

*Demo: Auditing a deliberately risky MCP config and tool set — risk score 100/100 (critical).*

**A defensive security auditor for MCP (Model Context Protocol) servers.**

`mcp-shield` statically audits MCP server configurations and tool definitions
— the exact files you paste into Claude Desktop, Cursor, or VS Code — and
flags the misconfigurations and supply-chain traps that turn a helpful tool
into a foothold. Pure Python standard library: **zero runtime dependencies**.

## Why this exists

MCP servers run with *your* privileges, and the model decides when to call
them based on their **tool descriptions** — text written by whoever published
the server. That creates a distinctive threat surface:

- **Tool poisoning** — a description quietly contains instructions to the
  model ("ignore previous instructions", "don't tell the user", "also send
  the file contents to…"), sometimes hidden with zero-width or bidirectional
  Unicode characters that a human reviewer can't see.
- **Rug pulls** — a server you reviewed and approved silently changes its
  tool descriptions, schemas, or launch command in an "update". The name
  stays the same; the behaviour doesn't.
- **Over-broad grants** — filesystem servers pointed at `/` or your home
  directory, servers launched through a shell, live API keys pasted into the
  `env` block of a JSON file that gets committed and shared.
- **Unpinned execution** — `npx -y some-server@latest` runs whatever was
  published most recently, every launch, no questions asked.
- **Name shadowing** — a third-party server re-defines `read_file`, so the
  model (and you) can't tell which implementation actually executes.

`mcp-shield` checks for all of these before you ever start the server.

## Requirements

- **Python 3.10 or newer** (CI tests 3.10, 3.11 and 3.12).
- **No runtime dependencies** — Python standard library only.
- **For development / the test suite:** `pip install -e ".[dev]"`
  (adds `pytest` and `pytest-cov`); CI runs
  `python -m pytest -q --cov=mcp_shield --cov-report=xml --cov-fail-under=90`.

## Install

```bash
pip install -e .        # from a clone of this repo
```

Requires Python 3.10+. No third-party packages.

## Quick start

Audit the bundled, deliberately risky example — it is designed to be
flagged, so a working install exits `1` with findings:

```bash
pip install -e .
mcp-shield audit --config examples/risky-config.json --tools examples/risky-tools.json
```

Then point it at your own host configuration:

```bash
mcp-shield audit --config ~/.config/claude/claude_desktop_config.json
```

## Usage

### Audit a config and/or tool definitions

```bash
# Audit an MCP host config (Claude Desktop / Cursor / VS Code format)
mcp-shield audit --config ~/.config/claude/claude_desktop_config.json

# Audit tool definitions exported from a server
mcp-shield audit --tools tools.json

# Both together, JSON output for tooling, custom failure threshold
mcp-shield audit --config config.json --tools tools.json \
    --format json --output report.json --fail-on medium
```

### Rug-pull defence: pin a baseline, then check for drift

```bash
# Once, when you have reviewed and trust the current definitions:
mcp-shield pin --config config.json --tools tools.json --baseline mcp-baseline.json

# Later (e.g. after a server update, or in CI) — exits 1 if anything changed:
mcp-shield check --config config.json --tools tools.json --baseline mcp-baseline.json
```

`pin` records SHA-256 fingerprints of every tool's full definition,
description, and input schema, plus every server's launch configuration.
`check` reports added/removed tools, **changed descriptions** (the classic
rug pull), changed schemas, and changed server commands/args/env.

### Exit codes

| Code | Meaning |
| --- | --- |
| `0` | No findings at or above the `--fail-on` severity (default: `high` for `audit`, `low` for `check`) |
| `1` | Findings at or above the threshold — CI should fail |
| `2` | Usage or input error (unreadable/invalid file) |

### Reports

Reports come out as Markdown (default) or JSON (`--format json`), with a
0–100 risk score, a severity summary, and per-finding detail with concrete
remediation steps. See [`examples/`](examples/) for a deliberately risky
config and its generated report.

## Checks

| Check ID | Severity | What it catches |
| --- | --- | --- |
| `shell-command` | critical | Server launched through `sh`/`bash`/`powershell`/… |
| `pipe-to-shell` | critical | `curl … \| sh` style download-and-execute arguments |
| `broad-filesystem-access` | high | Server granted `/`, `~`, `$HOME`, or a drive root |
| `secret-in-env` | high / critical | Secret-looking values or real token formats (`ghp_`, `sk-`, `AKIA`, PEM keys…) in `env` |
| `unpinned-package` | medium | `npx`/`uvx`/`docker` running a package/image with no version pin or `@latest` |
| `tool-description-poisoning` | high / critical | Instructions embedded in a tool description (ignore-orders, secrecy, exfiltration, forced invocation order, fake system prompts) |
| `tool-hidden-unicode` | high | Zero-width / bidi-control characters hiding text in names or descriptions |
| `tool-description-length` | low | Descriptions over 1000 characters (room to bury injections) |
| `tool-name-shadowing` | medium | Tool name squats a well-known name (`read_file`, `bash`, `fetch`, …) |
| `tool-name-collision` | high | Names that collide after normalisation (`read_file` vs `read-file`) |
| `tool-name-confusable` | medium | Names one edit apart (`get_weather` vs `get_weatherr`) |
| `tool-schema-missing` | medium | Tool has no `inputSchema` at all |
| `tool-schema-unconstrained` | low | Unbounded string parameters, or `additionalProperties` not `false` |
| `rugpull-*` | low – high | Drift vs. a pinned baseline: tools/servers added, removed, or silently changed |

## CI example (GitHub Actions)

```yaml
- name: Audit MCP configuration
  run: |
    pip install mcp-shield  # or: pip install -e .
    mcp-shield audit --config mcp-config.json --tools tools.json --fail-on high
    mcp-shield check --config mcp-config.json --tools tools.json --baseline mcp-baseline.json
```

A working workflow for this repository itself lives in
[`.github/workflows/ci.yml`](.github/workflows/ci.yml).

## Development

```bash
pip install -e ".[dev]"
python -m pytest -q --cov=mcp_shield --cov-fail-under=90  # 58 tests
```

## Limitations

- **Static analysis only.** `mcp-shield` reads configuration and
  tool-definition files; it never starts an MCP server, executes
  audited code, or observes runtime behaviour — a server that behaves
  only when it runs is outside its view.
- **A fixed, enumerated rule set.** Findings come from the checks in
  the table above. A poisoning phrasing or misconfiguration that
  matches none of those rules will not be flagged.
- **Drift detection needs a baseline.** Rug-pull protection only works
  if you `pin` a trusted baseline first and `check` against it later;
  there is nothing to compare against on a first run.

## Sponsors

Sponsorship pays for the maintenance, triage and release time behind this tool. Sponsors are
listed here by name, and name placement starts at the $25 a month Sponsor tier or the $50
one-time Sponsor tier.

- [Sponsor on GitHub](https://github.com/sponsors/gravion-ux)

## License

MIT — see [LICENSE](LICENSE). Copyright (c) 2026 Priyanshu Kumar Thakur.

*mcp-shield is a defensive auditing tool. It only reads configuration and
tool-definition files; it never starts an MCP server or executes audited
code.*
