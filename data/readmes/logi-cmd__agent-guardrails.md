# Agent Guardrails

**[Chinese](./docs/zh-CN/README.md)** | **English**

![Agent Guardrails](./assets/hero-banner.svg)

`agent-guardrails` checks code changes made by AI coding tools before you merge them. It records what the task is allowed to change, compares that plan with the diff and test evidence, and gives the reviewer a clear result.

It does not replace Claude Code, Codex, Cursor, Gemini, or OpenCode. It works beside them as a repo-level guardrail.

## Why use it

AI coding tools are fast, but the hard part is often the handoff:

- What exactly was the agent supposed to change?
- Did it touch files outside the task?
- Were tests or validation actually run?
- Is there evidence a reviewer can trust later?
- Did a small request turn into a broad rewrite?

`agent-guardrails` makes those questions explicit and repeatable.

## What it checks

- Scope: flags changes outside the declared task, allowed paths, or intended files.
- Validation: checks reported commands and required evidence files.
- Consistency: warns when a task spreads across too many files or directories.
- Risk: surfaces protected paths, interface changes, config changes, migration changes, and secret-like patterns.
- Reviewer output: prints a score, verdict, findings, next actions, and a concise review summary.
- Agent setup: writes repo-local helper files and MCP configuration guidance for supported agents.

## Supported agents

`agent-guardrails` can generate or update helper files for:

| Agent | Helper location |
| --- | --- |
| Claude Code | `CLAUDE.md` |
| Codex | `.codex/instructions.md` |
| Cursor | `.cursor/rules/agent-guardrails-enforce.mdc` |
| Gemini CLI | `GEMINI.md` |
| OpenCode | `.opencode/rules/agent-guardrails-enforce.md` |

## Requirements

- Node.js 18+
- Git
- A git repository for the project you want to protect

The npm package includes native runtime binaries for Windows x64, macOS x64/arm64, and Linux x64. It also includes the Node runtime.

## Quick start

```bash
npm install -g agent-guardrails

cd your-repo
agent-guardrails setup . --agent codex --lang en
agent-guardrails enforce --all --lang en
agent-guardrails doctor --lang en
```

Use the agent name you actually work with: `claude-code`, `codex`, `cursor`, `gemini`, or `opencode`.

## Core workflow

1. Set up the repo once.
2. Ask your agent to use `agent-guardrails` for the task.
3. Create a task brief with `plan`, or let an MCP-capable agent start the guarded loop.
4. Implement the smallest safe change.
5. Run validation, then run `check --review` before merge.

```bash
agent-guardrails plan \
  --task "Add input validation" \
  --intended-files "src/add.js,tests/add.test.js" \
  --allow-paths "src/,tests/,evidence/" \
  --required-commands "npm test" \
  --evidence "evidence/add-validation.md" \
  --lang en
```

![Plan output from agent-guardrails](./assets/readme-plan.svg)

```bash
npm test
agent-guardrails check --base-ref HEAD~1 --commands-run "npm test" --review --lang en
```

![Review output from agent-guardrails](./assets/readme-check-review.svg)

The screenshots above were generated from a real `agent-guardrails` run in a temporary git repository.

## MCP integration

`setup` prints the MCP snippet for the selected agent. For Codex, the snippet looks like this:

```toml
[mcp_servers.agent-guardrails]
command = "npx"
args = ["agent-guardrails", "mcp"]
```

Once connected, MCP-capable agents can read repo guardrails, start a bounded implementation loop, check after edits, and finish with a review summary.

## Commands

| Command | Purpose |
| --- | --- |
| `setup . --agent <name>` | Initialize guardrails and agent helper files for a repo. |
| `enforce --all` | Add stronger guardrail instructions for all supported agents. |
| `unenforce --all` | Remove injected guardrail instructions. |
| `plan --task "..."` | Write a task contract before implementation. |
| `check --review` | Run a reviewer-facing guardrail check. |
| `doctor` | Diagnose repo setup and runtime availability. |
| `generate-agents` | Regenerate agent helper files. |
| `mcp` | Start the stdio MCP server. |
| `serve` | Start the local API service for integrations. |
| `start`, `stop`, `status` | Manage the local background daemon. |

## Configuration

`setup` creates `.agent-guardrails/config.json`. The most common settings are:

```json
{
  "checks": {
    "scope": {
      "violationSeverity": "error",
      "violationBudget": 5
    },
    "correctness": {
      "requireCommandsReported": true,
      "requireEvidenceFiles": true
    }
  }
}
```

Useful options:

| Setting | What it controls |
| --- | --- |
| `checks.scope.violationSeverity` | Whether scope violations are blocking errors or warnings. |
| `checks.scope.violationBudget` | How many minor scope slips can be treated as soft warnings. |
| `checks.consistency.maxChangedFilesPerTask` | File-count warning threshold for one task. |
| `checks.correctness.requireCommandsReported` | Whether validation commands must be reported. |
| `checks.correctness.requireEvidenceFiles` | Whether declared evidence files must exist. |
| `checks.risk.requireReviewNotesForProtectedAreas` | Whether protected areas need review notes. |

## Optional Verity receipt

Agent Guardrails works independently. When a local [Verity](https://github.com/logi-cmd/verity) verification receipt exists, pass it explicitly:

```bash
agent-guardrails check --verity-receipt ./path/to/receipt.json --review
```

Agent Guardrails invokes `verity verify-receipt` from `PATH` without a shell. An accepted receipt is recorded as `verificationEvidence`; it proves only Verity's local runtime verification and does not satisfy scope, security, protected-path, required-command, or evidence-file requirements. If Verity is unavailable or rejects the receipt, the check is blocked.

## Evidence and docs

- [CHANGELOG](./CHANGELOG.md)
- [Workflows](./docs/WORKFLOWS.md)
- [Troubleshooting](./docs/TROUBLESHOOTING.md)
- [Release evidence](./docs/PROOF.md)
- [Executable scenarios](./docs/BENCHMARKS.md)

## License

MIT
