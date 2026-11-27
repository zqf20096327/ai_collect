# pi-charter

English | [简体中文](README.zh-CN.md)

Spec-driven delivery for the [Pi coding agent](https://pi.dev): you and the model write a short contract for one change (a *charter*), you approve it, and a gated pipeline of separate agents implements it, runs your project's checks, audits it independently and, optionally, tidies it up. You get back a report generated from recorded facts, not from a model's summary of itself.

The workflow is a state machine enforced by code. A model cannot approve its own spec, skip the audit, edit the contract after approval, or declare work verified that was not.

```text
 you + model            you          implementer      your checks       auditor(s)        refiner
┌──────────────┐   ┌──────────┐   ┌──────────────┐   ┌───────────┐   ┌─────────────┐   ┌──────────┐   ┌────────┐
│ draft brief  │──▶│ approve  │──▶│ write code,  │──▶│ test/lint │──▶│ verify each │──▶│ simplify │──▶│ report │
│ and spec     │   │ (dialog) │   │ prove each AC│   │ typecheck │   │ AC, no edits│   │ (guarded)│   │        │
└──────────────┘   └──────────┘   └──────┬───────┘   └─────┬─────┘   └──────┬──────┘   └──────────┘   └────────┘
        ▲                                │ questions       │ fail           │ findings
        │                                ▼                 ▼                ▼
        └───── revise ◀──────────── you decide      auto-repair,       you decide:
                                                    then you decide    fix / waive / revise
```

## Quick start

Requirements: Pi 1.5 or later, Node.js 22.19 or later. Git is optional but recommended (see [what git adds](#what-git-adds)).

```bash
git clone <this repository> pi-charter
pi install ./pi-charter
```

(The package is not published to npm yet; once it is, `pi install npm:pi-charter` does the same.)

Then, in Pi, from your project directory:

```text
/charter
```

That turns Charter mode on with sensible defaults: an implementer and an auditor, both using your session's model. Describe the change you want. The model drafts `brief.md` and `spec.md` with you, asking one question at a time. When you are satisfied, it requests approval and you confirm in a dialog. The pipeline then runs until it is finished or needs a decision from you.

To choose different models per role, enable the refiner, or have your test and lint commands run as gates:

```text
/charter setup
```

## What a charter is

A charter lives in `.charter/<id>/` and consists of:

| File | Content |
| --- | --- |
| `brief.md` | Why the change is worth doing, the outcome, what is in and out of scope. |
| `spec.md` | Requirements (`R1: The <actor> MUST ...`) and acceptance criteria (`AC1`) with GIVEN / WHEN / THEN and a concrete example each. |
| `design.md` | Optional. Technical decisions that must be fixed before implementation. |
| `attachments/` | Optional. Mock-ups, sample files and anything else that is part of the contract. |

A small example of `spec.md`:

```markdown
### R1: The exporter MUST quote values that contain a comma

- Change: added

#### AC1: Comma values are quoted

- GIVEN a row whose name is `Doe, Jane`
- WHEN the CSV export runs
- THEN the name column of that row is `"Doe, Jane"`

| name      | exported    |
| --------- | ----------- |
| Doe, Jane | "Doe, Jane" |
| Ada       | Ada         |
```

`charter_lint` checks the documents deterministically before you are asked to approve: every requirement states an obligation and is traceable to a criterion or an existing test, every criterion has all three clauses and a concrete example, ids are unique, no placeholder is left, and vague outcomes ("works correctly") are flagged. The full rule list is in [docs/workflow.md](docs/workflow.md#lint-rules).

## What is enforced by code

| Guarantee | How |
| --- | --- |
| Only you approve. | Approval is a dialog answered by you, or the `/charter approve` command typed by you. The model's tool cannot approve without it. |
| Only you decide questions and findings. | `charter_resolve` shows the exact decisions for your confirmation. Without a UI, only `/charter decide` records them. |
| The contract is frozen after approval. | Documents are hashed and archived at approval. File tools refuse edits; any other change is detected before a run, and an agent's change is undone and reported. |
| Every acceptance criterion is answered. | An agent's report is rejected, with reasons, unless it covers exactly its criteria, each with evidence. "Done" with a failing criterion is rejected. |
| The auditor does not write code. | Its file tools work only in a scratch directory, and the work tree is compared before and after: whatever it changed is restored and named in the report. |
| Agents never see each other's claims. | Each agent runs in a fresh session. The auditor gets the approved documents and the list of changed files from git, not the implementer's report. |
| Failing checks never reach the audit. | Your check commands run as real processes after implementation. A failure goes straight back to the implementer with the output, a bounded number of times, then to you. |
| A refinement cannot change behavior unnoticed. | It may only touch files the implementation touched. If it leaves that scope, or breaks a check that passed before, it is rolled back entirely. |
| Loops end. | Implementation cycles and automatic repairs are budgeted; each agent run has a time limit. Going beyond a budget needs your say. |
| The summary is true. | `report.md` is generated from the saved reports, check results and decisions. Skipped, waived and reverted work is listed as such. |

## Commands

| Command | Purpose |
| --- | --- |
| `/charter` | Turn the mode on, or show the status when it is on. |
| `/charter new <title>` | Create a charter and start drafting. |
| `/charter resume [id]` | Continue an existing charter, at whatever stage it is, also after a restart. |
| `/charter status` · `list` · `log [n]` · `report` | Inspect. |
| `/charter lint` | Check the documents. |
| `/charter approve [id]` | Approve and start the pipeline. |
| `/charter decide <ref> <decision> <text> ; ...` | Record your decisions, e.g. `/charter decide audit-1/F1 fix must match the spec ; F2 waive cosmetic`. |
| `/charter go` | Continue the pipeline; grants one more cycle if the budget is spent. |
| `/charter skip [reason]` | Skip the pending checks, audit or refinement. It is reported as not performed. |
| `/charter reopen` | Return an approved charter to drafting. |
| `/charter rollback [checkpoint]` | Restore the project files to a checkpoint (default: the state at approval) and reopen. |
| `/charter prune [id]` | Delete the git checkpoints of a finished charter. |
| `/charter setup` · `doctor` | Configure interactively; verify configuration, models, git and checks. |
| `/charter off` | Turn the mode off. Files are kept. |

The model works through six tools that are visible only while the mode is on: `charter_new`, `charter_lint`, `charter_approve`, `charter_advance`, `charter_resolve`, `charter_status`.

## Configuration

Charter works without a configuration file. To change something, create `.pi/charter.json` in the project (or `~/.pi/agent/charter.json` for all projects; the project file is layered on top):

```json
{
  "version": 1,
  "roles": {
    "implementer": { "model": "anthropic/claude-sonnet-5", "thinking": "high" },
    "auditor": { "model": "openai/gpt-6", "thinking": "medium", "shards": 2 },
    "refiner": { "enabled": true }
  },
  "checks": [
    { "name": "typecheck", "run": "npm run typecheck" },
    { "name": "test", "run": "npm test", "timeoutSeconds": 900 }
  ]
}
```

A role without a `model` uses the session's model. Using a different model family for the auditor than for the implementer gives a more independent second opinion. Every field is described in [docs/configuration.md](docs/configuration.md).

## Performance

Model time dominates any agent workflow, so the design goal is to spend fewer model round trips and fewer tokens per charter, and to add as little as possible on top.

- **One tool call drives the whole pipeline.** After approval, implement, checks, audit and refinement run inside a single tool call. The coordinating model is not woken between phases just to call the next tool.
- **Agents stop the moment they report.** The report tool ends the run, so there is no closing "summary" round trip, and an invalid report is corrected inside the same, still cached, session instead of failing the run.
- **Briefs replace discovery.** Each agent starts with the approved documents inline, the exact criteria it answers for, the changed files from git, earlier decisions, and the checks that will run.
- **Checks before tokens.** Deterministic failures (tests, lint, types) are caught by processes and sent back to the implementer directly; no auditor run is spent on code that does not pass its own checks.
- **Parallel audit.** With `shards > 1`, acceptance criteria are split across auditors that run concurrently, which shortens the audit of larger specs. If one auditor fails, the others' results are kept and only the failed part is re-run.
- **Cache-friendly prompts.** The long coordinator instructions are sent once per session; only a three-line state section changes as the charter moves.
- **Near-zero cost when unused.** Pi loads a small declaration module at startup; the engine is imported the first time Charter is actually used.
- **Shared model runtime.** Credentials and model catalogs are loaded once per session and reused by every agent run.

Measured with `npm run bench` (Node 22.23, Linux x64, a shared container; figures varied by up to a factor of two between runs, so read them as orders of magnitude):

| Operation | Time |
| --- | --- |
| Startup module, paid by every Pi session | ≈ 5 ms |
| Engine and agent runner, loaded on first use | ≈ 45 ms |
| Parse and lint a spec with 200 criteria (44 KB) | ≈ 2 ms |
| Checkpoint a 5,000-file work tree | ≈ 45 ms |
| Snapshot it again with 21 changed files | ≈ 35 ms |
| Restore those files to the checkpoint | ≈ 55 ms |
| Engine overhead for a whole pipeline with git (approve, implement, audit, refine, report) | ≈ 250 ms |
| Coordinator model calls from approval request to presented report, three agents | 2 |
| Agent model calls after filing the report | 0 |

The benchmark uses Pi's built-in faux model provider, so it measures the overhead of this package, not the speed of any real model.

## What git adds

Charter never commits, stages, stashes or switches branches. With `git.checkpoints` on (the default) it takes *snapshots* of the work tree through a private index and keeps them under `refs/charter/`, which gives you:

- an exact list of files changed since approval, passed to the auditor and used as the refiner's scope;
- detection and undo of project changes made by an auditor;
- automatic rollback of a refinement that leaves its scope or breaks a check;
- `/charter rollback`, which is itself undoable.

Before any automatic restore, the state about to be overwritten is saved as a checkpoint, so nothing an agent (or you) wrote is ever destroyed by the pipeline.

Without a repository the pipeline still runs: implementation, checks and audit work, the refiner is skipped, and the items above are unavailable. `/charter doctor` tells you which applies.

## Relation to pi-maestro, OpenSpec and Spec Kit

pi-charter was written after studying [pi-maestro](https://github.com/emilioSp/pi-maestro), which pioneered a code-enforced, spec-driven builder/verifier workflow as a Pi extension, and it borrows ideas that pi-maestro in turn credits to [OpenSpec](https://github.com/Fission-AI/OpenSpec) and [GitHub Spec Kit](https://github.com/github/spec-kit): a behavior contract with GIVEN/WHEN/THEN scenarios and concrete examples, requirement deltas, and traceability from requirement to verification. pi-charter is an independent implementation with its own design, vocabulary and code; nothing was copied.

How it differs from pi-maestro 0.21, the version studied:

| | pi-maestro 0.21 | pi-charter |
| --- | --- | --- |
| Approval | The model records it after reading your reply | A dialog or command only you can answer |
| Checks before approval | Documents exist, criterion numbering; everything else is the model's review | Deterministic linter: structure, traceability, clauses, examples, placeholders, vague outcomes |
| Spec freeze | By instruction | Hashes, archived copies, guarded file tools, automatic restore |
| Project checks | Left to the agents | Run by code as gates, with bounded automatic repair |
| Phase chaining | The model calls one tool per phase | One tool call runs every phase |
| Agent run ending | Agent replies after its handoff | The report ends the run |
| Agent ends without a report | The run fails | The agent is reminded once in the same session |
| Verifier isolation | Trusted to clean up after itself | Scratch-only file tools, work-tree comparison and restore |
| Parallel verification | No | Optional auditor shards |
| Simplifier safety | Instruction | Scope enforcement, check comparison, automatic rollback |
| Interrupted or failed run | Manual follow-up | Advance again; `/charter resume` after a restart |
| Undo | None | Checkpoints and `/charter rollback` |
| Budgets | None | Time limit per run, cycle and repair budgets |
| Cost visibility | None | Tokens, cost and duration per run and in total |
| Final summary | Written by the model | Generated from the recorded results |
| Configuration | Required, per project, models mandatory | Optional, layered, models default to the session's |
| Runtime | Node 26 | Node 22.19 or later |

## Limitations

- **Not yet exercised with live models.** The test suite drives real Pi sessions and the real `pi` executable end to end, but the models in those tests are scripted. The mechanics are tested; how well real models follow the role prompts is not, so expect to tune the prompts.
- Parallel auditors share one checkout. Checks that write to fixed paths or ports can interfere with each other, which is why `shards` defaults to 1.
- Snapshots honor `.gitignore`. Changes an auditor makes to ignored files are not detected.
- The refinement is protected by scope enforcement and your checks, not by a second audit.
- A model editing frozen documents through the shell is detected before the next run rather than prevented.
- In RPC mode the host application answers the dialogs; whether a human is behind them is up to that host.
- Developed and tested on Linux. Windows is untested.

## Development

```bash
npm install
npm run check      # typecheck + tests: unit, engine, and end-to-end against real Pi sessions
npm run bench
```

The code is plain TypeScript that Node runs directly; there is no build step. See [docs/architecture.md](docs/architecture.md).

## License

[MIT](LICENSE)
