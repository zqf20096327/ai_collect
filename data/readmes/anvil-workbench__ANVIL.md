<p align="center">
  <img src="https://raw.githubusercontent.com/anvil-workbench/ANVIL/main/docs/anvil-dashboard.png?v=2" alt="ANVIL Verification Layer Dashboard" width="100%" />
</p>

<h1 align="center">ANVIL — The Deterministic Verification Layer for AI Coding Agents</h1>

<p align="center">
  <strong>Any agent writes the code — ANVIL verifies it locally (blast radius, policy, security, tests) before it merges.</strong>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT License" /></a>
  <a href="https://github.com/anvil-workbench/ANVIL/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/anvil-workbench/ANVIL/ci.yml?branch=main&style=flat&label=build" alt="Build status" /></a>
  <a href="https://www.npmjs.com/package/anvil-engineering-workbench"><img src="https://img.shields.io/npm/v/anvil-engineering-workbench?color=orange" alt="npm version" /></a>
  <a href="https://github.com/anvil-workbench/ANVIL"><img src="https://img.shields.io/github/stars/anvil-workbench/ANVIL?style=flat" alt="GitHub stars" /></a>
  <a href="https://modelcontextprotocol.io/"><img src="https://img.shields.io/badge/MCP-Read--only%20Tools-0f766e" alt="MCP Tools" /></a>
</p>

<p align="center">
  <a href="#what-is-anvil">What is ANVIL</a> ·
  <a href="#60-second-quick-start">Quick start</a> ·
  <a href="#feature-overview">Feature table</a> ·
  <a href="#how-anvil-fits-with-your-ai-coding-tools">AI tool integrations</a> ·
  <a href="#github-action-usage">GitHub Action</a> ·
  <a href="#documentation">Docs</a> ·
  <a href="#credits--upstream-attribution">Credits</a>
</p>

---

## What is ANVIL?

**ANVIL** is a local-first, deterministic **verification layer** for AI-assisted software engineering.

When AI coding agents (Claude Code, Cursor, Codex, Antigravity, OpenCode) generate changes across your repository, ANVIL provides the structural safety net before code reaches review or merges into production:

- **100% Local-First & Private:** Evaluates AST syntax trees, dependency graphs, and git diffs directly on your hardware. Zero proprietary source code or credentials are ever sent to third-party LLMs.
- **Compact Agent Context (<1.5k Tokens):** Instead of forcing your agent to read hundreds of source files (burning 150k+ tokens), ANVIL's read-only Model Context Protocol (MCP) server supplies concise architecture summaries, entry points, and circular dependency maps in under 1,400 tokens.
- **Deterministic Quality & Policy Gate:** Evaluates baseline content hashes, rule confidence, hardcoded secrets, and formatting before commit or in CI pull request checks.
- **Complements Agent Libraries:** ANVIL complements prompt/skills libraries like [ECC](https://github.com/affaan-m/ECC) by providing the verification, blast-radius calculation, and policy enforcement engine.

---

## 60-Second Quick Start

### 1. Connect ANVIL to your AI tools in one step

```bash
# Registers ANVIL MCP server, stop hooks, and guidelines in Cursor, Claude Code, VS Code, etc.
npx -y anvil-engineering-workbench install . --hooks
```

*See the [Universal Tool Installer Guide](docs/install.md) and [Agent Stop Hooks Guide](docs/agent-hooks.md) for tool-specific targets (`--target`), dry-run preview, and uninstall.*

### 2. Run verification gate instantly with npx

```bash
# Evaluate repository quality gate & secrets
npx anvil-engineering-workbench gate .

# Inspect project stack and package manifests
npx anvil-engineering-workbench inspect .

# Map architecture imports and module boundaries
npx anvil-engineering-workbench map .
```

### 3. Global Installation

```bash
npm install --global anvil-engineering-workbench
```

*Or install directly from the verified GitHub release:*

```bash
npm install --global git+https://github.com/anvil-workbench/ANVIL.git#v1.2.0
```

Verify your installation:

```bash
anvil --version
# anvil 1.2.0
```

### 4. Install 1-Command Pre-Commit Hook

Ensure no secret leaks or policy regressions ever get committed:

```bash
anvil hook install
# Installed ANVIL pre-commit hook into .git/hooks/pre-commit
```

---

## Feature Overview

Every command and flag listed below is verified and supported in ANVIL v1.2.0:

| Command | Description | Verified Flags | Status |
|---|---|---|---|
| `anvil install [path]` / `uninstall` | Connects ANVIL to every AI tool config (Cursor, Claude, VS Code, Antigravity, etc.) | `--target <list>`, `--server <mode>`, `--dry-run`, `--no-instructions`, `--json` | **Available** |
| `anvil gate [path]` | Deterministic CI quality & security gate with SARIF and policy enforcement | `--sarif <file>`, `--policy <file>`, `--policy-ref <ref>`, `--baseline <file>`, `--generate-baseline <file>`, `--since <ref>`, `--diff`, `--min-confidence <level>`, `--import-sarif <file>`, `--skip-agent-config`, `--fail-on-warnings`, `--json` | **Available** |
| `anvil inspect [path]` | Analyzes project languages, manifests, frameworks, dependencies, and scripts | `--json` | **Available** |
| `anvil map [path]` | Maps module import relationships and candidate entry points | `--json` | **Available** |
| `anvil git [path]` | Calculates blast radius, downstream dependency impact, and suggested tests | `[base]` (e.g. `origin/main`, `HEAD~1`) | **Available** |
| `anvil clean [path]` | Scans and deletes junk files/caches with transactional snapshot backups | `--apply`, `--fix`, `--json` | **Available** |
| `anvil undo [path]` | Rolls back last clean operation with byte-accurate snapshot restoration | `<backupId>` | **Available** |
| `anvil hook [install\|remove]` | Injects or removes automated pre-commit gate in `.git/hooks/pre-commit` | `--force` | **Available** |
| `anvil security [path]` | Scans repository for hardcoded secrets, API keys, and sensitive tokens | `--fix`, `--json` | **Available** |
| `anvil agent-security [path]` | Audits agent instructions, prompt injection, hidden Unicode, MCP secrets, and permissions | `--global`, `--sarif <file>`, `--json` | **Available** |
| `anvil doctor [path]` | Verifies environment health (Node, Git, Docker, workspace permissions) | `--fix`, `--json` | **Available** |
| `anvil mcp [setup\|start]` | Sets up or runs local read-only Model Context Protocol server | `[setup]` | **Available** |
| `anvil dashboard [path]` | Launches unified multi-cockpit dashboard (ANVIL, ECC, REA, FORGE) on loopback | `[path]` | **Available** |
| `cross-harness handoff` | Synchronize active task state between Cursor and Claude Code | — | *Coming soon* |
| `GitHub App Service` | Hosted GitHub App for automatic pull request comments & check runs | — | *Coming soon* |

---

## How ANVIL Fits With Your AI Coding Tools

ANVIL acts as the local inspection and verification harness for your agent:

```text
[ AI Coding Agent ] ──writes code──> [ Local Repo ] ──verified by──> [ ANVIL Gate ] ──PR──> [ Merge ]
  (Claude / Cursor /                    (AST Map, Blast Radius,
   Codex / Antigravity)                  Secrets, Downstream Tests)
```

### Supported Harnesses & Ecosystems

- **Claude Code:**
  Run `anvil install . --hooks --target claude`. Claude accesses read-only MCP tools (`anvil_map_architecture`, `anvil_change_risk`, `anvil_inspect_project`) to query repository structure without bloating context windows, while stop hooks automatically check changes on completion.
- **Cursor IDE:**
  Run `anvil install . --hooks --target cursor`. Automatically configures `.cursor/mcp.json` and `.cursor/hooks.json` so Cursor's agent receives immediate gate feedback before stopping.
- **ECC (affaan-m/ECC):**
  Complements ECC's 1,500+ skills and prompt workflows with ANVIL's deterministic verification, blast radius, and agent security scanning. See the [ECC Integration Guide](docs/integrations/ecc.md).
- **REA (morluto/rea):**
  Powers an end-to-end reverse-engineering and binary analysis pipeline: use REA for binary/bundle inspection and ANVIL for safe patch verification and CI gating. See the [REA Integration Guide](docs/integrations/rea.md).
- **Codex & OpenCode:**
  Use standard `AGENTS.md` instructions and run `anvil gate .` to verify changes before committing.
- **Google Antigravity (AGY):**
  Integrates seamlessly with AGY workspace configurations and rules. See the [Antigravity Integration Guide](docs/integrations/antigravity.md).

### Canonical MCP Tools

All ANVIL MCP tools are strictly read-only and enforce safety bounds:

- `anvil_inspect_project`: Inspect stack, manifests, and scripts.
- `anvil_map_architecture`: Deterministic import graph and circular ring detection.
- `anvil_change_risk`: Blast radius and suggested test targets for uncommitted diffs.
- `anvil_git_intelligence`: Working copy diff and affected modules.
- `anvil_quality_audit`: Static project hygiene and workflow audit.
- `anvil_security_audit`: Entropy-based secret scanning with zero network calls.
- `anvil_clean_preview`: Safe dry-run inspection for caches and junk.
- `anvil_doctor`: Diagnostic environment check for Node, Git, Docker, and permissions.

---

## GitHub Action Usage

Enforce deterministic verification on every pull request using the official ANVIL GitHub Action:

```yaml
name: ANVIL Verification Gate

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  gate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Run ANVIL Quality & Security Gate
        uses: anvil-workbench/ANVIL@v1.2.0
        with:
          version: v1.2.0
          operation: gate
          project-path: .
          baseline-file: .anvil/baseline.json
          sarif-file: anvil-results.sarif
          pr-comment: "true"
          github-token: ${{ secrets.GITHUB_TOKEN }}

      - name: Upload SARIF to GitHub Security Tab
        if: always()
        uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: anvil-results.sarif
```

---

## Documentation

Explore detailed guides in the `docs/` directory:

- 📖 **[Documentation Index](docs/README.md)**: Full guide directory.
- 🚀 **[Getting Started](docs/getting-started.md)**: Step-by-step onboarding walkthrough.
- 🔌 **[Antigravity Integration](docs/integrations/antigravity.md)**: Setup ANVIL with Google Antigravity.
- 🤖 **[Claude Code Integration](docs/integrations/claude-code.md)**: Claude Code CLI adapter.
- 🛠️ **[MCP Server Guide](docs/mcp-server.md)**: Model Context Protocol setup and tool schemas.
- 📋 **[Policy-as-Code](docs/policy-as-code.md)**: Configure `.anvil/policy.json` rules and baselines.
- 🛡️ **[CI Gate & SARIF Integration](docs/ci-gate-and-sarif.md)**: GitHub Actions and SARIF reports.
- ⚡ **[Token Benchmark Results](docs/token-benchmark-results.md)**: Empirical comparison measuring 96%+ token savings.

---

## Credits & Upstream Attribution

ANVIL is open-source software licensed under the **[MIT License](LICENSE)**.

- **Upstream Foundation:** ANVIL started as a fork of the **[FORGE project](https://github.com/ansh44233/FORGE-ECC)** by **[Ansh](https://github.com/ansh44233)**. We gratefully acknowledge Ansh and the FORGE community for their original foundational work in agent harnesses. See [NOTICE](NOTICE) and [ACKNOWLEDGEMENTS.md](ACKNOWLEDGEMENTS.md) for full attribution.
- **Ecosystem Complement:** ANVIL complements prompt, skills, and agent catalogs like [ECC (Everything Claude Code)](https://github.com/affaan-m/ECC) by Affaan M, acting as the local verification, AST inspection, and policy enforcement engine.
- **Standards:** Built on the open [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) and the [OASIS SARIF v2.1.0 standard](https://docs.oasis-open.org/sarif/sarif/v2.1.0/sarif-v2.1.0.html).
