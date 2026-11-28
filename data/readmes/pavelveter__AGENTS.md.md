# AGENTS.md

**Engineering rules for AI coding agents. Without vibes, hallucinations, or scope creep.**

> Work it harder. Make it better. Make it faster. Make it stronger.
>
> But first, make sure it actually works.

Small diffs. Real tests. Honest reports.
A little paranoia is a feature, not a bug.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![AI Agents](https://img.shields.io/badge/AI-Agents-purple.svg)](#)
[![Engineering](https://img.shields.io/badge/Engineering-First-green.svg)](#)

---

## What Is This?

A practical engineering framework for AI-assisted software development.

Not another collection of magic prompts. Not a 400-page manifesto about the future of work. And definitely not an invitation for an LLM to rewrite half the codebase because it spotted an opportunity for "improvement".

This repository contains a modular set of rules, workflows, and tools designed to make AI coding agents more predictable, productive, and accountable.

The central idea:

**AI agents should operate like engineers, not enthusiastic autocomplete with root access.**

The system focuses on:

- **Context engineering** — retrieve relevant knowledge instead of flooding the model with everything.
- **Agentic workflows** — delegate work with explicit scope, boundaries, and recovery paths.
- **Verification-first development** — code is a hypothesis until tested.
- **Root-cause debugging** — reproduce, investigate, fix, verify.
- **Spec-driven development** — establish expected behavior before implementing complex changes.
- **Security and reliability** — treat input boundaries, secrets, permissions, and failure modes seriously.
- **Tool efficiency** — use existing tools, standard interfaces, and composable workflows.
- **Persistent knowledge** — preserve architectural context across sessions and agents.

The objective is simple:

Make AI-assisted development more predictable, reproducible, maintainable, and measurable.

## Engineering Philosophy

### 1. Context Is an Engineering Resource

More context does not automatically mean better reasoning.

Load relevant documentation, inspect the actual codebase, retrieve architectural knowledge, and avoid wasting tokens on unrelated information.

Context should be curated, not dumped.

### 2. Autonomy Needs Boundaries

An autonomous agent without constraints is just a very fast source of technical debt.

Define:

- Task scope.
- Allowed changes.
- Existing behavior that must be preserved.
- Verification requirements.
- Recovery strategy.

Give agents enough freedom to solve problems, not enough freedom to invent new ones.

### 3. Verification Beats Confidence

A successful command is not necessarily proof of correctness.

- Tests should validate behavior.
- Builds should use the actual project configuration.
- Security assumptions should be checked.
- Failure paths should be considered.
- Unverified claims should never be presented as facts.

"Works on my reasoning" is not an acceptable test result.

### 4. Root Causes Over Band-Aids

Reproduce first. Trace the execution path. Identify the actual cause.

Don't suppress errors, weaken tests, add arbitrary retries, or introduce fallback behavior just to make a failing check disappear.

### 5. Prefer Composable Tools

Use standard CLI workflows, MCP integrations, existing packages, and native platform capabilities.

Avoid reinventing functionality that already exists.

Custom code is justified when existing solutions don't fit — not because writing another implementation feels productive.

### 6. Humans Own the Decisions

Agents can investigate, implement, test, review, and propose architecture.

But responsibility for correctness, security, and architectural decisions must remain explicit.

The human is still the engineer. The model is a very capable, occasionally overconfident collaborator.

---

## Repository Structure

The repository is organized into a small core and supporting modules loaded only when needed.

| File              | Responsibility                                                                                                                                                                            |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AGENTS.md`       | Core rules: mission, scope, safe decisions, pre-edit checks, stack detection, Ponytail Ladder, bug fixing, testing, recovery, tooling, on-demand docs, done checklist, and report format. |
| `debug.md`        | Root-cause debugging. Reproduce first. Do not mask errors or weaken tests.                                                                                                                |
| `deps.md`         | Dependency rules, package commands, and safety checks before adding or bumping packages.                                                                                                  |
| `benchs/evals.md` | Test scenarios and scoring for rule changes.                                                                                                                                              |
| `git.md`          | Branch safety, diff checks, staging discipline, and commit message rules.                                                                                                                 |
| `refactor.md`     | Structural refactors without changing behavior.                                                                                                                                           |
| `review.md`       | Pre-report sanity check for scope, leftovers, correctness, and honesty.                                                                                                                   |
| `sdd.md`          | Spec-driven flow for features, APIs, schemas, and architecture shifts.                                                                                                                    |
| `security.md`     | Input boundaries, injection defense, secrets hygiene, and auth/network rules.                                                                                                             |
| `testing.md`      | Behavior tests, real boundaries, clean test data, flaky test rules, and stack test commands.                                                                                              |
| `tools.md`        | Search order (`fff`, `codebase-memory-mcp`, `rg`) and command rules.                                                                                                                      |
| `stacks/`         | Per-stack instructions loaded only when relevant.                                                                                                                                         |

### Stack-specific rules

- `stacks/go.md`
- `stacks/node.md`
- `stacks/python.md`
- `stacks/web.md`

The core document defines the rules. Supporting files provide the details.

No need to load the entire rulebook to fix a typo. We have better things to do.

---

## Toolchain

This setup uses a combination of AI tooling, CLI utilities, language toolchains, and persistent codebase context.

Some tools are essential to the workflow; others are optional accelerators.

### AI and Agent Infrastructure

| Tool                                                                   | Purpose                                                                                      |
| ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| [OpenCode](https://opencode.ai/)                                       | Primary AI coding environment. Agent execution, model selection, tools, and MCP integration. |
| [MCP](https://modelcontextprotocol.io/)                                | Standardized interface for connecting models to external tools and contextual resources.     |
| [codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | Persistent codebase knowledge, symbol relationships, and architectural context.              |

### Developer Tooling

| Tool                                             | Purpose                                                                |
| ------------------------------------------------ | ---------------------------------------------------------------------- |
| [fff](https://github.com/magnusmalm/fff-cli)     | Fast file discovery and content search.                                |
| [ripgrep](https://github.com/BurntSushi/ripgrep) | Precise source-code search and reference discovery.                    |
| [RTK](https://github.com/rtk-ai/rtk)             | Compresses command output to reduce noise and LLM context consumption. |
| [Git](https://git-scm.com/)                      | Version control, diff inspection, change isolation, and recovery.      |

### Language Toolchains

| Tool                              | Purpose                                                                                           |
| --------------------------------- | ------------------------------------------------------------------------------------------------- |
| [Go](https://go.dev/)             | Compiled systems software, CLI utilities, concurrency, testing, and performance-oriented tooling. |
| [Python](https://www.python.org/) | AI/ML development, automation, prototyping, and backend tooling.                                  |
| [uv](https://docs.astral.sh/uv/)  | Python environments, dependency management, and project execution.                                |
| [Node.js](https://nodejs.org/)    | JavaScript and TypeScript runtime and development ecosystem.                                      |
| [pnpm](https://pnpm.io/)          | Fast package management, reproducible installs, workspaces, and monorepo workflows.               |

### Why These Tools?

**codebase-memory-mcp**

Architectural knowledge should survive context resets.

Use persistent codebase context to understand relationships, symbols, and project structure before blindly exploring files.

**fff + ripgrep**

Fast discovery and precise search.

Use specialized search tools when available, but never let a missing utility block progress. Standard shell tools are perfectly acceptable.

**RTK**

Terminal output consumes context.

Reducing noise means more room for actual reasoning, relevant source code, and test results.

**Go**

Prefer the standard toolchain before adding dependencies:

- `go build ./...`
- `go test ./...`
- `go test -race ./...`
- `go vet ./...`
- `gofmt -d .`

**Python + uv**

Keep environments reproducible and dependency management explicit.

Prefer `uv run`, `uv sync`, and the project's existing configuration over ad hoc global installations.

**Node.js + pnpm**

Use the package manager declared by the project.

- `pnpm install --frozen-lockfile`
- `pnpm run <script>`
- `pnpm exec <command>`
- `pnpm -r run <script>`

Preserve `pnpm-lock.yaml`. Don't silently switch to npm or Yarn.

---

## Search Strategy

The preferred search workflow:

1. `fff` — discover relevant files and content.
2. `codebase-memory-mcp` — retrieve architectural and symbol context.
3. `rg` — verify exact definitions, references, and call sites.

Use the available tools intelligently.

If a preferred tool is missing, use a sensible alternative. Don't spend half the task installing a search utility just to avoid typing `rg`.

---

## Runtime Environment

This repository reflects an actual working environment rather than an imaginary universal developer workstation.

### Primary Environment

| Component               | Configuration |
| ----------------------- | ------------- |
| OS                      | macOS         |
| Shell                   | Zsh           |
| Terminal                | Kitty         |
| Editor                  | Vim           |
| Python                  | uv            |
| Node.js package manager | pnpm          |
| Systems language        | Go            |
| AI coding runtime       | OpenCode      |
| Context integration     | MCP           |
| Version control         | Git           |

### OpenCode Configuration

The current setup uses OpenCode-specific paths:

| Purpose                   | Path                                         |
| ------------------------- | -------------------------------------------- |
| Global configuration      | `~/.config/opencode/opencode.json`           |
| Global agent definitions  | `~/.config/opencode/agents/`                 |
| Project agent definitions | `.opencode/agents/`                          |
| Project configuration     | `opencode.json` or `.opencode/opencode.json` |

Useful documentation:

- [OpenCode](https://opencode.ai/docs/)
- [Configuration](https://opencode.ai/docs/config/)
- [Agents](https://opencode.ai/docs/agents/)
- [MCP servers](https://opencode.ai/docs/mcp-servers/)

These paths are intentional. They describe the actual environment in which this setup was developed and used.

### Using Another Agent Runtime

The core engineering rules are not tied to OpenCode.

If adapting this setup for another runtime:

1. Replace OpenCode-specific configuration paths.
2. Configure the target runtime to load `AGENTS.md`.
3. Move global instructions into the appropriate agent directory.
4. Reconfigure MCP servers and tool permissions.
5. Update runtime-specific commands, hooks, and integrations.
6. Preserve the project-level engineering rules.

Possible alternatives:

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview)
- [Codex](https://developers.openai.com/codex/)
- [Cursor](https://docs.cursor.com/)

One source of truth for engineering rules is preferable to five subtly incompatible copies.

---

## How to Use

1. Copy `AGENTS.md` and the supporting Markdown files into your project.
2. Preserve the directory structure.
3. Configure your coding agent to discover and load the instructions.
4. Check stack-specific rules against the actual project.
5. Run a small task and inspect agent behavior.
6. Adjust rules based on observed failures, not theoretical preferences.

The system should evolve with the codebase and the tools.

Don't add rules just because they sound smart. Add them because they prevent a real class of mistakes.

---

## Evaluation and Continuous Improvement

Instructions are software too.

They can become outdated, contradictory, overly restrictive, or simply ineffective.

Use `benchs/evals.md` to evaluate changes to the agent rules.

Useful evaluation scenarios include:

- Does the agent inspect existing changes before editing?
- Does it preserve unrelated user modifications?
- Does it reproduce bugs before attempting fixes?
- Does it avoid unnecessary dependencies?
- Does it select the correct package manager?
- Does it run meaningful tests?
- Does it report skipped checks honestly?
- Does it avoid expanding task scope?
- Does it recover safely from failed operations?

A rule that looks good in Markdown but changes no agent behavior is just documentation decoration.

---

## Reporting Format

Every completed task should produce a concise, evidence-based report.

The standard structure:

| Section      | Meaning                             |
| ------------ | ----------------------------------- |
| STATUS       | Current verified state.             |
| ACTION       | What was done or what must be done. |
| RESULT       | Observed outcome.                   |
| VERIFICATION | Evidence and checks performed.      |
| RISK         | Remaining risks or limitations.     |
| NEXT ACTION  | Required follow-up, if any.         |

At the end, include a **Decisions** list documenting important implementation choices and their rationale.

No hiding failed tests. No pretending skipped checks passed. No "everything looks good" when nothing was actually verified.

---

## Design Principles

- Small changes are easier to review.
- Explicit assumptions are easier to challenge.
- Reproducible workflows are easier to trust.
- Modular instructions are easier to maintain.
- Good defaults reduce unnecessary decisions.
- Real verification beats confident language.
- Engineering discipline matters more than model enthusiasm.

And one final rule:

**Never confuse generating code with solving a problem.**

The first is easy. The second is the job.

---

## License

MIT
