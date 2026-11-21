# openspec-tdd

An [AWF](https://github.com/awf-project/cli) workflow pack that applies [OpenSpec](https://github.com/Fission-AI/OpenSpec)
changes test first. Each code slice of a change's `tasks.md` goes through RED, GREEN and a review whose tools come from
your project's language registry. The change is then reviewed as a whole and checked against its Definition of Done,
and `flow-apply-many` merges it into main. Drafting, spec sync, acceptance and archiving of changes are part of the pack.

Moving from one phase to the next depends on the exit codes of your tools (test runner, static analysis, mutation
testing), never on what the agent reports.

## Requirements

- awf 0.11.9 or later
- git, bash, jq, and `flock` (util-linux) for parallel tasks
- Node.js 24 or later (the task parser is TypeScript run by Node)
- the `openspec` CLI
- an agent CLI that awf can drive, Claude Code by default
- for `flow-review`, the [EGM](https://github.com/google/elephant-goldfish-model) plugin installed in Claude Code, or
  `EGM_ROOT` pointing to a copy of its repository

## Install

From a GitHub release, at the root of your repository:

```bash
awf init    # once per project: creates .awf/, which awf workflow install requires
awf workflow install gplanchat/awf-workflow-openspec-tdd
```

Add `--global` to install it for every project, or `@0.2.0` to pin a version. Then check the installation:

```bash
awf workflow info openspec-tdd
```

## Configure your project

The pack calls no project tool directly. It reads two files at the root of your repository.

| File | Required | Content |
|---|---|---|
| `.awf/languages.yaml` | yes | The language registry: for each language key, the slice workflow, the test file patterns, and the commands for RED, GREEN, each review tool and the merge checks. |
| `.awf/commands.yaml` | no | The command contract: replaces the git defaults for worktrees, claims, merges, parallel runs and end-to-end tests. |

Start from the examples:

- [`examples/languages.yaml`](examples/languages.yaml): PHP, TypeScript, Three.js and Go entries
- [`examples/languages-rust.yaml`](examples/languages-rust.yaml): Rust entries, one key per RED level, plus performance slices
- [`examples/commands.yaml`](examples/commands.yaml): a project driven by its own stack script

The operations of the command contract and their git defaults are listed at the top of
[`scripts/commands.sh`](scripts/commands.sh).

### Generate the configuration with an agent

To write both files for an existing project, run this prompt in your agent from the root of the repository. It asks
the agent to derive the commands from your project's own files and to ask you about anything it cannot find there.

```text
Configure the openspec-tdd AWF workflow pack for this repository by writing .awf/languages.yaml and, if needed,
.awf/commands.yaml.

Reference material, from the installed pack or from https://github.com/gplanchat/awf-workflow-openspec-tdd:
- examples/languages.yaml: the meaning of every registry key, in the header comments, and PHP, TypeScript, Three.js
  and Go entries;
- examples/languages-rust.yaml: Rust entries;
- examples/commands.yaml and the header of scripts/commands.sh: the command contract and its git defaults.

Steps:
1. Inventory the languages of this repository and the directory of each one. For each, find the real commands in the
   project's files (composer.json, package.json, Makefile, go.mod, Cargo.toml, CI configuration, compose files,
   wrapper scripts): test runner, a command that runs only the given test files with a JUnit report, static analysis,
   linters, mutation testing, architecture checks.
2. Write one registry entry per language: workflow, dir, tests and mutation patterns, test, red, report, strip,
   checks, review_steps, last, merge_checks, and the keywords that classify tasks. Use only commands that exist in
   this repository. Leave out a key whose tool the project does not have, and list it in your report.
   Derive the keywords from stable parts of the project (directory names, layers, frameworks, tools), not from the
   names of today's functions, classes or business terms, which change from one change to the next.
3. Write .awf/commands.yaml only if the project already drives its worktrees, services or end-to-end tests through
   its own script. Otherwise, keep the git defaults and do not create the file.
4. Run every command you put in a registry entry once, and report which ones pass, which fail and why.
5. Ask me before you install a tool, add a dependency, or change any file outside .awf/.

End with a short report: the languages found, the keys left out and why, and the commands that failed.
```

To run the same merge checks when you merge by hand, install the git hook:

```bash
bash <pack>/scripts/merge-gate.sh install
```

## Write tasks the pack can apply

A code task in `tasks.md` is declared in slices. The tag in brackets is a key of `.awf/languages.yaml`:

```markdown
## 2. Order total

- [ ] 2.1 Compute the order total
  - [ ] 2.1.1 [php] [unit] The total sums the lines, taxes included
  - [ ] 2.1.2 [ts] [functional] The cart page shows the total
```

- A slice tagged `[critical]` next to its language gets the extra review tools of `critical_steps`.
- A slice declares its test level next to its language, `[php] [unit]`, `[functional]` or `[integration]`, when the
  language's entry in `.awf/languages.yaml` has `levels` (one path pattern per level). The `levels` gate of
  `flow-propose` and `flow-update` fails on a slice without one, and RED fails (code 14) on a test file at another
  level. `design.md` ends with a test strategy that gives each scenario its level, and `apply-change.json` counts the
  test files per level in the project and in the change (`pyramid`).
- A group whose title ends with `(parallel)` runs its tasks at the same time, each in its own sub-worktree, when
  `max_tasks` is above 1.
- A task without slices is a manual task: an agent carries it out, and its `Verified by:` command decides whether its
  box gets checked. Write `Verified by: Manual` when no command exists: the gates of `flow-propose` and `flow-update`
  fail on a manual task with neither, and `flow-apply` lists such a task under `skipped` in its report.
- Each criterion of the Definition of Done carries its check command, or `Manual`.

## Workflows

Run a workflow with `awf run openspec-tdd/<workflow>`. The usual entry points:

| Workflow | Purpose |
|---|---|
| `flow-propose` | Drafts a new change (proposal, specs, design, tasks) in `.worktrees/propose-<change>`. |
| `flow-update` | Revises the artifacts of an existing change. |
| `flow-review` | Reviews a drafted change with the EGM reviewers (see below). |
| `flow-accept` | Accepts a change: writes `acceptance.yaml` and merges the proposal. |
| `flow-apply` | Applies a change in `.worktrees/<change>` through `apply-change`. The change stays on its branch `change/<change>`, unmerged. |
| `flow-apply-many` | Applies several changes in parallel, then merges them one by one into main. With a single change, it applies and merges that change. |
| `flow-sync` | Carries the deltas of a change into the main specs. |
| `flow-archive` | Replays the Definition of Done and archives the change. |
| `flow-waive` | Records your waiver of a failed gate for a change, 30 days at most. Run it from your terminal. |
| `flow-explore` | Prints the repository context (`step=start`) and checks that an exploration session wrote nothing under `openspec/` (`step=finish`). |

To merge a change that `flow-apply` applied, run the merge operation of the command contract from the root of main.
It runs the merge checks of the registry, and aborts the merge when one fails:

```bash
bash <pack>/scripts/commands.sh merge <change>
```

### Review a change with EGM

`flow-review` reviews a drafted change with the [Elephant-Goldfish Model](https://github.com/google/elephant-goldfish-model)
(EGM): seven reviewers of the EGM plugin (zoom-out, comprehension, design, structural, style, implementation readiness,
codebase details) each run as a fresh agent with read-only tools and no earlier context. `proposal.md`, `design.md`
and `specs/` form the feature part, `tasks.md` the implementation plan. Run it where the change is drafted:

```bash
awf run openspec-tdd/flow-review --input change=<change>
```

The findings go to `.awf/status/egm/review.md`, and the status to `.awf/status/flow-review.json`. Without a Blocker,
the workflow succeeds. With one, the `ask` operation of the command contract puts the question to a person, and the
run stops in its terminal state `waiting`. The default `ask` prints the question and the line that answers it:

```bash
AWF_WORKFLOWS_PATH=<pack>/workflows awf resume <run> --from check --input egm_decision=proceed
```

`proceed` accepts the change with its Blockers; `revise` and `abandon` end the run in the state `declined`. To file the
question elsewhere, a dashboard for example, declare `ask` in `.awf/commands.yaml`.

Building blocks, called by the workflows above:

| Workflow | Purpose |
|---|---|
| `apply-change` | Applies the open tasks of a change in order, then runs the final reviews and `dod-verify`. |
| `apply-task` | Applies one task, slice by slice. |
| `tdd-slice-php`, `tdd-slice-ts`, `tdd-slice-threejs`, `tdd-slice-go`, `tdd-slice-rust` | One TDD slice: RED, GREEN, review. |
| `tdd-slice-rust-perf` | One performance slice, measured against a benchmark target. |
| `free-task` | One manual task. |
| `review` | The review tools of one language, in order. |
| `dod-verify` | The Definition of Done criteria, one command each. |
| `flow-gate`, `flow-commit` | Gates and commit shared by the drafting workflows. |

Each workflow writes its report under `.awf/status/`. Each one describes its inputs and exit codes in its
`description` field; `awf workflow info openspec-tdd` lists them.

### Give an agent of your project its own worktree

`agent-worktree` creates or reuses `.worktrees/<name>-<task>` on branch `agent/<name>-<task>`, for a workflow of your
project whose agent must not work in the main worktree. Call it as the first step, then read the path from its report,
since a `call_workflow` step does not pass on the output of the workflow it calls:

```yaml
states:
  initial: worktree
  worktree:
    type: call_workflow
    workflow: openspec-tdd/agent-worktree
    timeout: 600
    inputs:
      name: reviewer
      task: "{{.inputs.task}}"
    on_success: work
  work:
    type: step
    command: |
      tree=$(jq -r .worktree .awf/status/agent-worktree/reviewer-{{.inputs.task}}.json)
      cd "$tree" && ...
```

Give the `call_workflow` step an explicit `timeout`: without one, awf stops the called workflow after 5 minutes.

The name and the task are in kebab-case. A worktree that exists with uncommitted changes, untracked files included,
stops the workflow with code 2; set `AGENT_REPRISE=1` to resume the work it holds. A new worktree starts from
`BASE_BRANCH` (`main` by default), or from the branch `agent/<name>-<task>` when it already exists.

## Run the workflows in a Susan run

A Susan run is a fresh clone of the project with all its branches, positioned on `main`, discarded at the end, like a
CI job. Susan sets `NEXUS_AGENT_RUN_ID` in the environment, and pushes the current branch at the end of the run, fast
forward only, never `main`. When `NEXUS_AGENT_RUN_ID` is set, the workflows change as follows:

| Workflow | In a run |
|---|---|
| `flow-propose`, `flow-update`, `flow-sync`, `flow-archive`, `flow-accept` | No worktree: the clone switches to `docs/propose-<change>` (from the origin when it exists there, else created from `main`) and the workflow goes on. |
| `flow-accept` | Writes and commits `acceptance.yaml`, but does not merge into `main`: the run pushes the branch, and you merge it through a pull request or with `flow-accept` outside a run. |
| `flow-apply` | The clone switches to `change/<change>`, `commands.sh deps .` installs the dependencies, and the change is applied in place. A `(parallel)` group runs one task at a time. |
| `flow-apply-many` | Checks the names, writes `{"mode":"run","status":"listed","changes":[...]}` to `.awf/status/apply-many.json`, and stops: start one `flow-apply` run per change. |

No workflow ends by asking you to run a command again from another folder. A failed step prints what failed and why
on its output, which Susan shows in the run's log.

## Drive the workflows from Claude Code

The repository is also a Claude Code marketplace. Its `flow` plugin adds one command per entry point, each running the
matching workflow and reading its report: `/flow:propose`, `/flow:update`, `/flow:accept`, `/flow:apply`,
`/flow:apply-many`, `/flow:sync`, `/flow:archive`, `/flow:waive` and `/flow:explore`, plus `/flow:setup`, which installs
what these commands need. It also adds a hook that blocks
any write to the waiver registry outside `/flow:waive`.

Three commands bring the EGM design phases into the session, where reviewers can run as subagents:

- `/flow:brainstorm <change> <idea>` follows `egm-brainstorm` and writes a concepts brief to `.awf/briefs/<change>.md`,
  which `/flow:propose <change>` drafts the change from;
- `/flow:review <change>` runs `flow-review` and, on Blockers, asks you whether to proceed, revise or abandon;
- `/flow:resolve <change>` follows `egm-resolve` on the findings with you, applies the approved fixes through
  `flow-update`, then reviews the change again.

`/flow:propose` and `/flow:update` end with `/flow:review`, and `/flow:accept` stops while the review waits for a
decision or asked for a revision.

```text
/plugin install flow --marketplace gplanchat/awf-workflow-openspec-tdd
```

The commands run `awf run openspec-tdd/<workflow>`. At the start of a session in a repository that holds an
`openspec/` folder, the plugin checks that awf is 0.11.9 or later, that the project has an `.awf/` folder and that the
pack is installed. When `.awf/languages.yaml` lists pass proofs (a non-empty `proofs` key), it also checks for zpm 0.4.4.
If an item is missing, Claude Code shows a message. Run `/flow:setup` to install what is missing: it shows each command
(`awf upgrade`, `awf init`, `awf workflow install`, `zpm upgrade`, or a download of the awf or zpm release into
`~/.local/bin` after checking its SHA-256) and runs it once you approve it.

## Add a language

1. Add an entry to `.awf/languages.yaml` with the commands of your toolchain.
2. Point its `workflow` at an existing `tdd-slice-*` workflow, or add one to the pack with its prompts in `prompts/`
   and its skill in `skills/`.

## Known limitations

- The pack needs awf 0.11.9 or later: with 0.11.8 and earlier, `call_workflow` to a workflow of a pack fails
  ([awf-project/cli#426](https://github.com/awf-project/cli/issues/426)).
- The `[critical]` tag is honoured by the PHP, TypeScript, Go and Rust slice workflows, not by `tdd-slice-threejs`.
- `max_total` caps only the tasks of `(parallel)` groups; sequential tasks are not counted.
- awf 0.11.9 resumes a workflow of a pack without its pack prefix, and does not find it: resume `flow-review` with
  `AWF_WORKFLOWS_PATH` set to the pack's `workflows/` folder, as the default `ask` prints.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Apache License 2.0. See [LICENSE](LICENSE).
