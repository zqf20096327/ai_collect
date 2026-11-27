<p align="center">
  <img src="https://raw.githubusercontent.com/AdityaaaTiwari/ANVIL/main/docs/anvil-dashboard.png?v=2" alt="ANVIL Verification Layer Dashboard" width="100%" />
</p>

<h1 align="center">ANVIL — The Deterministic Verification Layer for AI Coding Agents</h1>

<p align="center">
  <strong>Any agent writes the code — ANVIL verifies it locally (blast radius, policy, security, tests) before it merges.</strong>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT License" /></a>
  <a href="PRIVACY.md"><img src="https://img.shields.io/badge/Privacy-Local--First-10b981" alt="Privacy Policy" /></a>
  <a href="https://github.com/AdityaaaTiwari/ANVIL/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/AdityaaaTiwari/ANVIL/ci.yml?branch=main&style=flat&label=build" alt="Build status" /></a>
  <a href="https://www.npmjs.com/package/anvil-engineering-workbench"><img src="https://img.shields.io/npm/v/anvil-engineering-workbench?color=orange" alt="npm version" /></a>
  <a href="https://github.com/AdityaaaTiwari/ANVIL"><img src="https://img.shields.io/github/stars/AdityaaaTiwari/ANVIL?style=flat" alt="GitHub stars" /></a>
  <a href="https://modelcontextprotocol.io/"><img src="https://img.shields.io/badge/MCP-Read--only%20Tools-0f766e" alt="MCP Tools" /></a>
  <a href="https://anvil-virid-sigma.vercel.app/app/"><img src="https://anvil-virid-sigma.vercel.app/api/app?op=badge&name=AdityaaaTiwari/ANVIL" alt="ANVIL Verified" /></a>
</p>

<div align="center">

[![M8ven Score](https://m8ven.ai/badge/mcp/anvil-workbench-anvil-6mga28?v=e317156751c13277a75180a10cf137dd)](https://m8ven.ai/mcp/anvil-workbench-anvil-6mga28?s=readme)

</div>

<p align="center">
  <a href="#what-is-anvil">What is ANVIL</a> ·
  <a href="#60-second-quick-start">Quick start</a> ·
  <a href="#feature-overview">Feature table</a> ·
  <a href="#how-anvil-fits-with-your-ai-coding-tools">AI tool integrations</a> ·
  <a href="#github-action-usage">GitHub Action</a> ·
  <a href="#documentation">Docs</a>
</p>

---

## What is ANVIL?

**ANVIL** is a local-first, deterministic **verification and safety layer** for AI coding agents.

### The Breakthrough: Protection Against Fake Success

AI coding agents are ambitious, but they frequently cheat when tests fail:
- An agent is asked to fix an authentication module.
- It writes a change, but an existing integration test fails.
- Instead of solving the root bug, the agent **deletes the failing test** or inserts a skip marker (`it.skip`, `test.skip`).
- The test runner passes (100% Green), and the agent confidently claims: *"Everything passed!"*

**ANVIL stops fake success dead in its tracks.**
Its verified loop checks pre-execution git checksums against unstaged diffs. If an agent deletes a test, skips test cases, or loosens linter configs, ANVIL halts execution with `status: needs-review` and refuses to accept the fake pass.

### The 6-Stage Verified Loop

```
01 Plan ──► 02 Guard ──► 03 Build ──► 04 Verify ──► 05 Prove ──► 06 Learn
```

1. **Plan:** Evaluates AST blast radius in <1.4k tokens instead of reading 150k+ raw tokens.
2. **Guard:** Intercepts dangerous operations (`rm -rf /`, `.env` exfiltration, unpinned packages).
3. **Build:** Coding agent modifies only scoped files in an isolated worktree or branch.
4. **Verify:** Runs real deterministic compiler, linter, and test checks — never trusting agent claims.
5. **Prove:** Inspects test integrity (zero deleted/skipped tests) and signs SHA-256 receipts.
6. **Learn:** Records architectural heuristics and post-mortem decisions in persistent memory.

- **100% Local-First & Private:** Evaluates AST syntax trees, dependency graphs, and git diffs directly on your hardware. Zero proprietary source code or credentials are ever sent to third-party LLMs.
- **Compact Agent Context (<1.5k Tokens):** Instead of forcing your agent to read hundreds of source files (burning 150k+ tokens), ANVIL's read-only Model Context Protocol (MCP) server supplies concise architecture summaries, entry points, and circular dependency maps in under 1,400 tokens.
- **Deterministic Quality & Policy Gate:** Evaluates baseline content hashes, rule confidence, hardcoded secrets, and formatting before commit or in CI pull request checks.
- **Native Catalog & Binary Provenance:** Includes a compact built-in catalog of 49 specialist agents, 76 catalog skills, 34 commands, and 26 rule sets plus pure TypeScript magic-byte binary inspection (`anvil binary`).

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
npm install --global git+https://github.com/AdityaaaTiwari/ANVIL.git#v1.5.0
```

Verify your installation:

```bash
anvil --version
# anvil 1.5.0
```

### 4. Install 1-Command Pre-Commit Hook

Ensure no secret leaks or policy regressions ever get committed:

```bash
anvil hook install
# Installed ANVIL pre-commit hook into .git/hooks/pre-commit
```

---

## 5 Core Engineering Superpowers

| Superpower | CLI Command | Why It Matters |
|---|---|---|
| **1. Verified Loop** | `anvil loop run --goal "..."` | Forces agent to repeat work until true checks pass; catches test deletion & tampering. |
| **2. ANVIL Guard** | `anvil install . --guard` | Runtime hooks blocking `rm -rf`, secret exfiltration, and unverified remote pipes. |
| **3. Shield v3** | `anvil shield --sarif` | 60 static harness security rules scanning permissions, MCP, secrets, and prompt injections. |
| **4. Agent Race** | `anvil race run --agents claude,codex` | Races multiple coding agents on the same task in isolated Git worktrees and ranks results. |
| **5. Cross-Harness MCP Sync** | `anvil mcp sync` | Synchronizes pinned MCP servers across 10+ AI tools (Claude, Cursor, Codex, Windsurf, Copilot). |

---

## Feature Overview

Every command and flag listed below is verified and supported in ANVIL v1.5.0:

| Command | Description | Verified Flags | Status |
|---|---|---|---|
| `anvil install [path]` / `uninstall` | Connects ANVIL to every AI tool config (Cursor, Claude, VS Code, Antigravity, etc.) | `--target <list>`, `--server <mode>`, `--dry-run`, `--no-instructions`, `--json` | **Available** |
| `anvil gate [path]` | Deterministic CI quality & security gate with SARIF and policy enforcement | `--sarif <file>`, `--policy <file>`, `--policy-ref <ref>`, `--baseline <file>`, `--generate-baseline <file>`, `--since <ref>`, `--diff`, `--min-confidence <level>`, `--import-sarif <file>`, `--supply-chain`, `--skip-agent-config`, `--fail-on-warnings`, `--json` | **Available** |
| `anvil inspect [path]` | Analyzes project languages, manifests, frameworks, dependencies, and scripts | `--json` | **Available** |
| `anvil map [path]` | Maps module import relationships and candidate entry points | `--json` | **Available** |
| `anvil call-graph [path]` | Builds deterministic TypeScript/JavaScript AST symbol call-graph (`caller -> callee`), traces upstream callers, and detects orphan exports | `--symbol <name>`, `--depth <n>`, `--mermaid`, `--json` | **Available** |
| `anvil git [path]` | Calculates blast radius, downstream dependency impact, and suggested tests | `[base]` (e.g. `origin/main`, `HEAD~1`) | **Available** |
| `anvil clean [path]` | Scans and deletes junk files/caches with transactional snapshot backups | `--apply`, `--fix`, `--json` | **Available** |
| `anvil undo [path]` | Rolls back last clean operation with byte-accurate snapshot restoration | `<backupId>` | **Available** |
| `anvil hook [install\|remove]` | Injects or removes automated pre-commit gate in `.git/hooks/pre-commit` | `--force` | **Available** |
| `anvil security [path]` | Scans repository for hardcoded secrets, API keys, and sensitive tokens | `--fix`, `--json` | **Available** |
| `anvil agent-security [path]` | Audits agent instructions, prompt injection, hidden Unicode, MCP secrets, and permissions | `--global`, `--sarif <file>`, `--json` | **Available** |
| `anvil shield [path]` | Runs ANVIL Shield v3 static harness audit across instructions, hooks, MCP, and CI | `--fix`, `--sarif <file>`, `--fail-on <level>`, `--json` | **Available** |
| `anvil scorecard [path]` | Computes deterministic harness readiness scorecard across 9 engineering categories | `--verbose`, `--json` | **Available** |
| `anvil consult "<task>"` | Finds catalog agents, skills, commands, rules, and MCP servers matching a task | `--json` | **Available** |
| `anvil binary [path]` | Inspects native binaries (.node/PE/ELF/Mach-O/WASM), spoofed headers, source maps, and captures with SHA-256 checksums | `--supply-chain`, `--findings-only`, `--json` | **Available** |
| `anvil supply-chain [path]` | Scans `node_modules` install hooks, native addons, disguised executables, lockfile integrity, and typosquats offline | `--findings-only`, `--max-packages <n>`, `--json` | **Available** |
| `anvil context [path]` | Measures pre-prompt token cost per AI harness and flags duplicate/sprawl waste | `--verbose`, `--max <tokens>`, `--json` | **Available** |
| `anvil loop run` / `status` | Executes anti-tamper verification loop with pre/post checksums and `.anvil/loops/` receipts | `--goal`, `--check`, `--max-iterations` | **Available** |
| `anvil race` | Races multiple coding agents in isolated Git worktrees and ranks verified diffs | `--agents`, `--goal`, `--check` | **Available** |
| `anvil doctor [path]` | Verifies environment health (Node, Git, Docker, workspace permissions) | `--fix`, `--json` | **Available** |
| `anvil mcp [setup\|start\|sync]` | Configures, runs, or cross-syncs the local Model Context Protocol server | `add`, `remove`, `sync`, `matrix` | **Available** |
| `anvil dashboard [path]` | Launches unified multi-cockpit dashboard (Verification, Agent Toolkit, Binary Intelligence, Control Center) on loopback | `[path]` | **Available** |
| `GitHub App Service` | GitHub App handlers & webhook bot (`/anvil analyze\|repair\|audit\|doctor\|risk`) | `/anvil` | **Available** |
| `cross-harness handoff` | Synchronize active session handoff state via `.anvil/memory.json` and hooks | `anvil memory handoff` | **Available** |

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
- **ANVIL Harness Catalog & Binary Intelligence:**
  Ships a self-contained catalog of 49 specialist agents, 76 domain skills, 34 workflow commands, and 26 rule sets installable via `anvil install --profile standard`, alongside native TypeScript magic-byte binary, provenance, and zero-dependency `node_modules` supply-chain inspection (`anvil binary` / `anvil supply-chain` / `anvil_binary_intelligence` / `anvil_supply_chain_audit`).
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
- `anvil_binary_intelligence`: Zero-dependency PE/ELF/Mach-O/WASM header, SHA-256, and binary-spoofing inspection.
- `anvil_supply_chain_audit`: Offline audit of `node_modules` install hooks, `.node` addons, lockfile integrity, and typosquats.
- `anvil_call_graph`: TypeScript/JavaScript AST symbol call-graph (`caller -> callee`), upstream traces, and orphan exports.
- `anvil_jit_skills`: Sub-1k token task-scoped JIT skill & instinct selector for prompt hooks (`anvil hook prompt-submit`).
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
        uses: AdityaaaTiwari/ANVIL@v1.5.0
        with:
          version: v1.5.0
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
