<div align="center">
  <h1>RC</h1>
  <p><strong>Skills, agents and hooks that take an idea to shipped code — small enough that every one of them fires.</strong></p>
  <p>
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  </p>
</div>

RC is an **agent plugin** — three primitives, no more: **skills**, **agents**, **hooks**. It runs
inside your agent host; every artifact is plain markdown under a project's `.rc/`. No binary, no
daemon, no lock-in.

## Why it is small

Every skill description a plugin ships is loaded in **every** session. Claude Code caps that metadata
at `skillListingBudgetFraction` — **1% of the context window** by default, about 2k tokens on a 200k
window. Past the cap it does not disable skills, it **drops descriptions**, starting with the
least-invoked. The skill stays present by name with nothing for the model to match against: silently
mute rather than visibly broken. And because the drop order favours frequently-used skills, one that
has never fired stays mute permanently.

RC shipped 48 skills at ~355 characters of description each — roughly 6.5k tokens against a 2k budget,
three times over. So the shipped set is **17 skills**, each description capped at **150 characters**,
and the rest stays on disk in unshipped buckets. `scripts/plugin-smoke.mjs` enforces all three numbers.

Buckets are the first lever. The second is `disable-model-invocation: true`: the `rc` skill is a
reference for a human, never something the model has to reach mid-task, so it is **user-invoked** —
you still type `/rc:rc`, and its description leaves the listing entirely. Sixteen descriptions load
per session, 2,165 characters, ~540 tokens.

| | Before | Now |
| --- | --- | --- |
| Shipped skills | 48 | **17** |
| Descriptions in the listing | 48 | **16** |
| Avg. description | 355 chars | **≤150 chars** |
| Listing cost per session | ~6,500 tok | **~540 tok** |
| Commands | 10 | **2** |
| Agents | 10 | **4** |
| Hooks | 9 | **10** |

Note that `claude plugin details` estimates from the file, so a user-invoked skill still shows its
description cost there. Read that number as a ceiling, not as what is injected.

Hooks went **up**. Two rules that were prose skills the agent could skip — "no completion claim
without fresh evidence" and "fix the root cause, never silence the signal" — became deterministic
guards, which is where an every-time rule belongs.

## Three primitives, one job each

| Primitive | Job | It is in the wrong place when |
| --- | --- | --- |
| **hooks** | deterministic rules that hold *every* time | it is prose in a skill and the agent skips it under pressure |
| **skills** | the disciplines the agent reaches for | it is a sequence of other skills |
| **agents** | context isolation — fan-out, adversarial review | it has a catalog entry instead of being spawned from inside a skill |

## Installation

Claude Code:

```bash
/plugin marketplace add rodolfochicone/rc-project
/plugin install rc@rc-project
```

Auto-updates via `/plugin marketplace update`; commands are namespaced `/rc:rc-*`. The repository is
public — no authentication needed. For other hosts, see
[`docs/claude-code-plugin.md`](docs/claude-code-plugin.md).

## How it works

```
idea → rc-spec → rc-tickets → rc-implement ⇄ rc-tdd → rc-code-review → rc-git → PR
                                    ↕
                      rc-diagnose · rc-memory · rc-codemap
```

Each phase reads what the last one wrote, under `.rc/tasks/<slug>/`. Nothing is a workflow engine: a
skill invokes the next skill, and read-only work fans out to subagents spawned from inside the skill.

## Skill catalog

Only `promoted/` ships. `stacks/` and `misc/` stay on disk — editable, greppable, and free.

### The build path

| Skill | Use it to |
| --- | --- |
| [`rc-spec`](skills/promoted/rc-spec/SKILL.md) | interview an idea into a spec — product intent, then technical design, with ADRs |
| [`rc-tickets`](skills/promoted/rc-tickets/SKILL.md) | break the spec into independently implementable tickets with blocking edges |
| [`rc-implement`](skills/promoted/rc-implement/SKILL.md) | build tickets in dependency order — least code that works, then the gate |
| [`rc-tdd`](skills/promoted/rc-tdd/SKILL.md) | red → green, one vertical slice at a time, at agreed seams |
| [`rc-code-review`](skills/promoted/rc-code-review/SKILL.md) | review on three lenses — standards, spec, delete-list — then fix what it confirms |
| [`rc-git`](skills/promoted/rc-git/SKILL.md) | branch, push, open the PR, confirming each outward-facing step |

### Reached when needed

| Skill | Use it to |
| --- | --- |
| [`rc-diagnose`](skills/promoted/rc-diagnose/SKILL.md) | root-cause any bug or failure, then fix and verify — no fix before the cause |
| [`rc-memory`](skills/promoted/rc-memory/SKILL.md) | recall and record what this project taught: facts, lessons, golden paths |
| [`rc-codemap`](skills/promoted/rc-codemap/SKILL.md) | build cheap per-directory structure maps before exploring a large repo |
| [`rc-council`](skills/promoted/rc-council/SKILL.md) | stress-test a high-impact decision across advisors, preserving dissent |
| [`rc-writing-for-agents`](skills/promoted/rc-writing-for-agents/SKILL.md) | author or trim a skill, an `AGENTS.md`, or a hook — and audit context cost |
| [`rc-codebase-design`](skills/promoted/rc-codebase-design/SKILL.md) | decide where an interface goes and how much it hides — module, depth, seam, adapter |
| [`rc-interface-design`](skills/promoted/rc-interface-design/SKILL.md) | build UI with craft, avoiding generic AI aesthetics |
| [`rc-typescript`](skills/promoted/rc-typescript/SKILL.md) | type design — illegal states unrepresentable, no escape hatches |
| [`rc-python`](skills/promoted/rc-python/SKILL.md) | idiomatic typed Python 3.12+ — asyncio, dataclasses, pytest, ruff, uv |
| [`rc-sql`](skills/promoted/rc-sql/SKILL.md) | relational query and schema work — read-only analysis by default |
| [`rc`](skills/promoted/rc/SKILL.md) | learn what RC offers and how the pieces fit — **user-invoked only** (`/rc:rc`) |

Shared rules live once, in [`references/conventions.md`](skills/promoted/rc/references/conventions.md):
`.rc` resolution, Serena navigation, untrusted content, root-cause-over-workaround, the
verification-evidence bar, project memory. They used to be pasted into 8 skills.

### Not shipped — load by name

**`skills/stacks/`** — [`rc-rust`](skills/stacks/rc-rust/SKILL.md) ·
[`rc-axum`](skills/stacks/rc-axum/SKILL.md) · [`rc-sqlx`](skills/stacks/rc-sqlx/SKILL.md) ·
[`rc-sveltekit`](skills/stacks/rc-sveltekit/SKILL.md)

**`skills/misc/`** — [`rc-board`](skills/misc/rc-board/SKILL.md) (Linear/Jira) ·
[`rc-gan`](skills/misc/rc-gan/SKILL.md) (adversarial quality loop) ·
[`rc-qa-execution`](skills/misc/rc-qa-execution/SKILL.md) ·
[`rc-openapi`](skills/misc/rc-openapi/SKILL.md) · [`rc-postman`](skills/misc/rc-postman/SKILL.md) ·
[`rc-readme`](skills/misc/rc-readme/SKILL.md) (README from the codebase) ·
[`rc-a11y`](skills/misc/rc-a11y/SKILL.md) · [`rc-seo`](skills/misc/rc-seo/SKILL.md) ·
[`rc-observability`](skills/misc/rc-observability/SKILL.md) ·
[`rc-resilience`](skills/misc/rc-resilience/SKILL.md) · [`rc-video`](skills/misc/rc-video/SKILL.md)

To promote one, move it into `skills/promoted/`, cut its description to 150 characters, add it to
`.claude-plugin/plugin.json` and this catalog — and demote something else or raise
`PROMOTED_CEILING` on purpose. The smoke test fails until the set is consistent.

## Commands

Two, both thin prompt macros with no skill behind them — which is what a command is for.

| Command | Does |
| --- | --- |
| `/rc-commit-msg` | a Conventional Commits message from the staged diff. Never commits. |
| `/rc-plano` | explore → state assumptions → plan → stop for approval. Writes no code. |

The other eight were "invoke skill A, then B, then C" — a workflow written in prose, duplicating the
orchestration the skills already carry — and went away with the skills they drove. The full
invocation guide, in Portuguese, is [COMMANDS.md](COMMANDS.md).

## Agents

Four council archetypes, dispatched by `rc-council`. Not a general-purpose worker pool: the host's own
`Explore`, Context7 and a `model:` override already cover recon, library lookups and hard reasoning.
Four leaf-worker agents that duplicated them shipped for months with zero invocations, so they are gone.

| Agent | Perspective |
| --- | --- |
| [`pragmatic-engineer`](agents/pragmatic-engineer.md) | execution reality, maintenance burden, team velocity |
| [`architect-advisor`](agents/architect-advisor.md) | boundaries, coupling, long-horizon coherence |
| [`security-advocate`](agents/security-advocate.md) | attack surface, blast radius, compliance |
| [`devils-advocate`](agents/devils-advocate.md) | hidden assumptions, edge cases, failure modes |

## Hooks

Configured in [`hooks/hooks.json`](hooks/hooks.json), gated by `RC_HOOK_PROFILE`
(`minimal|standard|strict`) and `RC_DISABLED_HOOKS`. **Every hook fails open** — an environment
problem never blocks a tool call — and each ships a `--selftest`.

| Hook | Event | Effect |
| --- | --- | --- |
| `git-guard` | PreToolUse(Bash) | denies destructive git (`reset --hard`, `clean`, bare force-push); asks on rebase and `--force-with-lease` |
| `commit-guard` | PreToolUse(Bash) | never commit or push unasked |
| `db-guard` | PreToolUse(Bash) | database access read-only by default |
| `gateguard` | PreToolUse(Edit\|Write\|MultiEdit) | grounding before the first edit of a file |
| `no-workarounds-guard` | PreToolUse(Edit\|Write\|MultiEdit) | asks before an edit adds `as any`, a lint suppression, or a swallowed error |
| `verify-guard` | Pre + PostToolUse(Bash) | stamps the gate when it runs; asks before a commit whose code changed after that stamp |
| `observe` | PostToolUse(Edit\|Write\|MultiEdit\|Bash) | appends tool observations for the `rc-memory` distill pass |
| `memory-load` | SessionStart | surfaces the memory store |
| `repair-guidance` | PostToolUse(Edit\|Write\|MultiEdit\|Task) | corrective guidance on a repairable failure, so the agent fixes the cause |
| `notify` | Stop, Notification | desktop notification |

The two new guards are the mechanical half of rules that were prose. `verify-guard` proves the gate has
not been run since the last code change — not that it passed; a hook cannot read an exit code
reliably, and guessing pass/fail from output would be a heuristic pretending to be a gate. Pass/fail
stays with the agent under the evidence bar in `conventions.md`.

Both **ask** rather than **deny**, because every pattern they match has a legitimate form — a
branded-type constructor, a `@ts-expect-error` in a test that asserts a type error, a work-in-progress
commit on your own branch. A guard that refuses legitimate work is a guard people disable.

## Artifacts

```
.rc/
  tasks/<slug>/
    _prd.md _techspec.md _tasks.md      # spec + master ticket list
    task_01.md … task_N.md              # one ticket each
    adrs/                               # architecture decision records
    notes.md                            # task-scoped scratch, deleted with the task
    code-review-NNN.md                  # review + fix rounds
  memory/                               # durable store
    INDEX.md <slug>.md                  # facts
    lessons.json LESSONS.md             # machine-owned lesson store
    observations.jsonl                  # raw capture
  analysis/                             # diagnose reports outside a slug
  ROADMAP.md                            # phases for unattended mode
```

## Route manual

[`docs/manual/rc-manual.html`](docs/manual/rc-manual.html) is the human-facing manual: the whole
inventory — 17 shipped skills, the 15 on disk, 4 agents, 2 commands, 10 hooks — plus 11 playbooks by
situation (feature, bug, understand before touching, review and trim, tests, architecture decision,
memory, security, writing for agents, board, unattended mode). It is an HTML **fragment**: no
`<!doctype>`, no `<head>` — the artifact host wraps it on publish, and `scripts/build-manual.py`
wraps it with print rules for the PDF ([`rc-manual.pdf`](rc-manual.pdf)). See
[`docs/manual/README.md`](docs/manual/README.md) for both flows.

The manual used to drift silently — it froze at the 6.0.0 inventory while the repo went to 7.x. The
gate now checks it in both directions: everything shipped must be named in it, and every name in a
catalog position must exist on disk.

## Output styles

[`output-styles/`](output-styles) ships two pt-BR styles that keep the engineering behaviour intact:
`Conciso PT` (direct answers, no preamble) and `Tutor PT` (explains the reasoning while it solves).

## Configuration

No runtime config file. Model and reasoning effort live in each skill's and agent's frontmatter
(`model:` / `effort:`). Hook behaviour is set by env vars:

| Var | Values | Effect |
| --- | --- | --- |
| `RC_HOOK_PROFILE` | `minimal` \| `standard` \| `strict` | which hooks are active (cumulative; default `standard`) |
| `RC_DISABLED_HOOKS` | `name,name` | force-skip specific hooks |
| `RC_DRY_RUN` | `1` | log guard decisions instead of enforcing them |
| `RC_INSTINCTS` | `0` | disable observation capture |

## Verification

```bash
node scripts/plugin-smoke.mjs        # the gate: frontmatter, buckets, budget, links, hooks, manual
node scripts/lessons.mjs --selftest
node scripts/validate-tasks.mjs --selftest
node scripts/validate-tasks.mjs --slug <feature>   # ticket files under a project's .rc/tasks/
bash hooks/scripts/<hook>.sh --selftest
```

`plugin-smoke.mjs` guards what the eye misses: a skill missing from this catalog, a promoted skill
absent from the manifest (or a non-promoted one present in it), a description over budget, a missing
anti-trigger, a dangling reference, an orphan bundled file, a hook script nobody wired up, a
dependency on the Claude-only `Workflow` tool, the promoted-count ceiling, and a route manual that
has drifted from the components the repo actually ships.

## Supported hosts

Claude Code is the shipped channel. Nothing in the set depends on a host-exclusive tool — the gate
fails a skill built on the Claude-only `Workflow` tool — so any host that reads the `.agents/skills`
convention loads the same skills; hooks and manifests are the Claude-Code-specific part.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md). Before opening a PR, run the gate
above. Adding a skill is a deliberate trade: promote one only by demoting one, or by raising the
ceiling on purpose.

## License

MIT — see [LICENSE](LICENSE).
