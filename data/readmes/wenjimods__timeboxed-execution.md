# Timeboxed Execution

An Agent Skill that helps agents avoid deadline overruns, scope creep, skipped verification, and false completion.

```text
Define done → Reserve verification time → Stop and report honestly
```

The goal is not to make an agent rush. It is to keep work bounded, visible, and verifiable.

## 30-Second Example

A 5-minute timebox to fix a reproducible bug:

- **Define done:** Done requires an observable reproduction, a minimal fix, passing regression tests, and a fresh-process live probe.
- **Reproduce & fix:** Isolate the root cause and apply the minimal change.
- **Freeze scope & verify:** Stop implementation early to enter verification; run regression tests and execute the live probe in a fresh process.
- **Stop rule:** If acceptance is not complete at 5:00, stop and report the state honestly (`partial_verified` or `stopped_unverified`) rather than taking silent overtime.

## Quick Start

### Recommended installation

Use the Agent Skills CLI to discover this repository and install the Skill for compatible agents:

```bash
npx skills add wenjimods/timeboxed-execution
```

The CLI detects supported agents and installs the Skill into their appropriate project-level directories. This repository follows the open [Agent Skills specification](https://agentskills.io/specification) and can be used across compatible runtimes, including Codex and custom harnesses.

### Hermes

Install the latest version from `main`:

```bash
hermes skills install https://raw.githubusercontent.com/wenjimods/timeboxed-execution/main/SKILL.md --name timeboxed-execution
```

For a reproducible install pinned to the current stable release:

```bash
hermes skills install https://raw.githubusercontent.com/wenjimods/timeboxed-execution/v1.4.1/SKILL.md --name timeboxed-execution
```

The `main` URL follows the latest repository state. The `v1.4.1` URL remains fixed to that release.

### Manual installation

Download or clone this repository outside an existing Git project, then copy the `timeboxed-execution` directory into the skill directory supported by your runtime. Avoid cloning it directly inside another repository, which would create a nested Git repository.

For environments without skill discovery, provide [`SKILL.md`](SKILL.md) directly as procedural context.

## Core ideas

- Define the observable done condition before acting.
- Use a lightweight fast path for genuinely simple tasks.
- Split complex work only into independently acceptable phases.
- Reserve verification time; freeze scope before final acceptance.
- Distinguish implementation, tests, runtime behavior, and persistence.
- Stop safely at the deadline and request extensions explicitly.
- Report one of five completion states: `verified_complete`, `partial_verified`, `blocked`, `failed`, or `stopped_unverified`.

## Files

- [`SKILL.md`](SKILL.md) — the reusable workflow.
- [`references/validated-patterns.md`](references/validated-patterns.md) — anonymized observations, replay cases, and a scoring rubric.
- [`LICENSE`](LICENSE) — MIT License.

## Notes

The frontmatter follows the [open Agent Skills specification](https://agentskills.io/specification). The Skill is tool-agnostic and supports Linux, macOS, and Windows.

The observed examples are not presented as universal causal proof or performance benchmarks. Evaluate the Skill against representative tasks and counterexamples before broad adoption.
