# moire

**Catches collisions between parallel AI coding agents while both are still writing — on uncommitted work, without the other agent's cooperation.**

*One file · Python 3.8+ · standard library only · git ≥ 2.38 · MIT · warns, never blocks*

**The difference, in one line: moire sees the one state no other tool inspects —
both agents' *uncommitted* work — and claims only what it has measured.** Every
number on this page is either measured by this project, with the instrument
published so you can re-run it, or cited with its denominator attached. That
includes the measured base rate that keeps the deep semantic check optional: the
check is the product, and the evidence discipline is the warranty.

## The problem

You run several AI coding agents at once. Each works in its own git worktree so they
can't overwrite each other's files. But they can still collide in the same code —
and they do, measurably often: across 1,300+ real co-active agent PR pairs replayed
by this project, **roughly one pair in five conflicted textually** (21.4% of 718
Python pairs, 20.6% of 586 TypeScript pairs, corroborating the 19.8% published by
Xu, Subramanian & Karthik, [arXiv:2607.04697](https://arxiv.org/abs/2607.04697) —
who also measured 41.7% for cross-vendor pairs).

That rate deserves the same scrutiny as every other number here: it is measured
on the population that *can* be measured — public PR pairs whose open intervals
overlapped — and it transports to a deliberately-dispatched swarm imperfectly in
both directions. A good dispatcher partitions work, which lowers the rate; agents
sharing one task share hot files, which raises it. The collision rate inside a
partitioned swarm is unmeasured, here and anywhere. What is established: concurrent
agent work collides textually at rates two orders of magnitude above the measured
semantic-breakage rate, and by default the collision is discovered at merge time —
after both agents have finished, moved on, and lost the context that would have
made it cheap to resolve. Whoever integrates the branches inherits a conflict
neither author is around to explain.

## What moire does

After each file write, it runs a **dress rehearsal**: it combines your working tree
with each other agent's working tree in a scratch space nobody sees, and asks git's
own merge engine whether they still fit. Run here 2026-08-25 in a two-worktree lab —
both agents on the **same commit**, both edits uncommitted, which is exactly the
state nothing else can see:

```
$ moire check
CONFLICT with /private/tmp/moire-lab/repo-agent-b (feat/b) [finding b13c7ab00ab2]
    src/limits.py
  arbiter: self yields (tiebreak: self's name 'main' > peer's 'feat/b')
  actions: rebase onto theirs | narrow your change | retarget | wait for them to land | proceed
```

The finding is a fact, not a guess — the verdict comes from `git merge-tree`, the
same engine the real merge will use. The finding id is content-addressed: the other
agent's own `moire check` computes the identical id for the identical collision,
which is what makes a finding something two agents can act on without trusting each
other's claims. And the arbiter is a recommendation both sides compute
independently from observable facts, so the agents converge without negotiating.

## Where it fits

| | sees | catches |
| --- | --- | --- |
| `git merge` | overlapping lines | conflicts — at merge time |
| code review | two separate diffs | nothing; each diff looks correct |
| CI | the merged result | everything — after both have landed |
| [Clash](https://github.com/clash-sh/clash) | the committed HEAD of each worktree | conflicts between two agents' last commits |
| **`moire check`** | **both live worktrees, uncommitted included** | **conflicts, while both are still writing** |
| **`moire pending` / `compose`** | **the log of outstanding findings** | **the handoff: a finding rendered as a message another agent can verify and act on** |

## Three things that make it unusual

- **It asks nobody anything.** It reads the other agent's files. The other agent
  needs no setup, no awareness of the tool, and may be from a different vendor.
- **It is exact, not a guess.** No heuristics, thresholds, model or tuning —
  `check` runs git's own merge engine against real trees.
- **It never blocks.** Warn-only by design, with no block mode and no flag to add
  one.

Each of those is a reaction to an approach that has already been tried and
measured — the [prior-art table below](#why-not-do-it-another-way) has the
outcomes.

## Quickstart

```bash
git clone https://github.com/jamescazzetta/moire.git ~/.moire
mkdir -p ~/.local/bin && ln -sf ~/.moire/bin/moire ~/.local/bin/moire
# ~/.local/bin must be on PATH:  export PATH="$HOME/.local/bin:$PATH"

cd your-repo
moire init-swarm --agents 3                     # worktrees, hooks, skills, doctor
moire wire-client claude --scope user --apply   # shows a diff first
```

Needs **git ≥ 2.38** (older git silently misses whole classes of conflict, so
moire refuses to run below it) and **Python 3.8+**. No daemon, no server, no
config file, no account, and nothing written into your working tree. `init-swarm`
also installs two Agent Skills — one teaches an agent to act on a finding, one to
run the swarm.

The detail behind every line of that — why a symlink, the binary-only variant,
what `wire-client` writes, manual setup, and the five places a full uninstall
touches — is in [docs/INSTALL.md](docs/INSTALL.md). There is no npm package.

## Compared with Clash

**The `git merge-tree` oracle between agent worktrees is not novel.**
[Clash](https://github.com/clash-sh/clash) (Rust, MIT) ships it with a Claude Code
hook, and the same primitive is published as a measurement method by Xu,
Subramanian & Karthik. `moire check` is *different*, not first, and the difference
is a testable claim:

**Clash's simulation cannot see uncommitted work; moire's is built on it.** Clash
merges each worktree's `commit.tree_id()`; it renders a `Dirty` marker but excludes
dirty state from the simulation. That comes from reading
`src/worktree/conflict.rs` — a claim about its source, not about a run of it. When
both agents edit the same line and neither has committed, the two HEADs are the
same commit: a HEAD-based simulation has nothing to compare. The demo above is
exactly that state, and `moire check` reports the conflict.

<details>
<summary><strong>Two minutes to falsify</strong></summary>

```bash
git init -q A && cd A
mkdir src && printf 'def rate_limit(n):\n    return n\n' > src/limits.py
git add -A && git commit -qm base
git worktree add -q ../B -b feat/b

# both agents edit the SAME LINE; neither commits
printf 'def rate_limit(n):\n    return min(n, 100)\n' > src/limits.py
printf 'def rate_limit(n):\n    return max(n, 10)\n' > ../B/src/limits.py

git rev-parse --short HEAD; git -C ../B rev-parse --short HEAD   # identical
moire check
```

Commit both sides and every tool agrees.

</details>

**Where Clash wins, and it is conceded.** A Rust binary installs more easily than
a Python file you have to put on `PATH`. Clash can *gate* an edit through a
`PreToolUse` ask-hook; moire never blocks and has no flag to make it — a design
position, not a missing feature, and if you want a gate you should use Clash.
Per-check latency has not been compared and no claim is made either way.

## Commands

| | |
|---|---|
| `moire check` | Would my worktree conflict **textually** with each peer, right now? |
| `moire pending` | What findings are outstanding between me and each peer, **according to the log** — read-only, no new observation. Prints each finding's age and says to re-run `check` for a live answer. |
| `moire compose <id>` | Render one finding as a message for whatever channel your harness has, with the id the receiver re-computes from their own run. `--action rebase\|narrow\|retarget\|wait\|proceed` states what the sender chose. moire has no transport; the agent sends it. |
| `moire verify` | Optional deep check: would the merged result be **semantically broken**, right now? Reads `moire.checker` / `moire.link` from `git config`. Prints the [measured base rate](#the-case-git-merges-cleanly) of what it looks for in its own output. |
| `moire replay <a> <b>` | The `verify` mechanism on two **commits** — the measurement instrument. Stateless: no log, no cache, no snapshot, and it works in a bare clone. |
| `moire install` | Install git hooks and the binary into `.git/` |
| `moire doctor` | Check git version, hook wiring, install state |
| `moire report` | Rates over distinct pair-states, distinct findings, contested paths, and how many findings have cleared |
| `moire init-swarm` | Create N worktrees, install, place the skills, run doctor |
| `moire wire-client` | Merge the hook into a client's settings (diff, then `--apply`) |

`check`, `verify` and `replay` **never exit nonzero because of a finding** — they
warn; they never fail your build. The one exception is a refusal: exit 2 on an
unusable environment or a bad argument, before writing any log.

## How it works

For each peer worktree:

1. **Snapshot both sides** — committed, staged, unstaged and untracked changes —
   by working through a *copy* of the worktree's index. The observed worktree is
   never modified, and a peer that's mid-`git add` doesn't block observation.
   Snapshots are content-addressed: re-checking an unchanged worktree writes no
   git objects at all.
2. **Ask git** — `git merge-tree --write-tree`. Exit code gives the verdict;
   conflicting paths come out on stdout. The finding id is derived from the two
   worktree paths and the contested paths, never from anything either agent
   declares — which is why both sides compute the same id.

The hook wiring runs `check` after every file write. At [measured
cost](#cost) — 219 ms warm against three peers — that is cheap enough to be
ambient.

## The case git merges cleanly

Two agents can also collide *invisibly*: file sets disjoint, merge textually
clean, and the combination still broken — one agent renames a function while the
other, in a file git never flags, writes a new call to the old name.

**moire can check for that case, and its frequency is measured.** `moire verify`
materialises the merged tree git *would* produce, runs a real checker over self,
peer and merged, and reports only breakage the combination creates:

```
new_breakage = broken(merged) − broken(self) − broken(peer)
```

Breakage already present in someone's branch is their own problem, not a
collision; findings are rewritten through a rename map before subtracting, and
linked dependency directories are built as per-entry unions, so a peer's `git mv`
or new dependency does not manufacture false breakage.

The measured base rate, from this project's pre-registered Phase 1 study
([`PHASE1-PREREGISTRATION.md`](PHASE1-PREREGISTRATION.md), results in
[`research/phase1-results/RESULTS.md`](research/phase1-results/RESULTS.md)):
across **672 audited textually clean co-active agent PR pairs** — 570 checked at
import level with the builtin Python checker, 102 type-checked with `tsc` and
each tree's own installed dependencies — the combination broke something neither
parent had broken in **0 of them** (95% upper bounds: 0.65% import-level, 3.55%
type-level). The scope travels with the number: PR-stage work, these failure
modes and not others, no tests were run, and mid-session uncommitted work has no
corpus to measure. `verify` prints this base rate in its own output, and every
hook and skill treats it as an instrument to reach for deliberately — the
textual check is the default because the textual collision is the common one.

The builtin checker proves an import still resolves — module and name — graded
against CPython by `tests/benchmark_recall.sh` at **9 of 11** confirmed
collisions with **0 of 8** clean merges misreported. [What that score does and
does not mean](docs/MEASUREMENTS.md#what-9-of-11-measures) is worth reading
before quoting it. It reads Python only, and says so rather than implying
otherwise:

```
$ moire verify
clean   with /repo-agent-b (textual only - no semantic check was performed)
  builtin-ast examined 0 of 847 files: it reads only Python and this tree has no .py files.
  The merged result was NOT semantically verified - "clean" above means only that git found no textual conflict.
  To enable semantic verification for this repo: git config moire.checker '<command>'   (README: the --checker contract)
(measured base rate of clean-merge semantic breakage: 0 of 672 audited agent-PR pairs - docs/MEASUREMENTS.md)
```

### Pointing `verify` at your language, per repo

```bash
git config moire.checker './node_modules/.bin/tsc --noEmit | sed -E "s/\([0-9]+,[0-9]+\)//"'
git config --add moire.link node_modules
moire doctor      # warns when `verify` would have nothing to read
```

This is `git config`, never cloned with the repository — a checkout cannot carry
a command that runs on someone else's machine — and one setting covers every
worktree of the swarm. A checker must be deterministic, one repo-relative finding
per line; break that and you get false breakage rather than silence. Read the
contract before pointing `--checker` at anything:

<details>
<summary><strong>The <code>--checker</code> contract</strong> — read this before writing or choosing one</summary>

- **One finding per line, deterministic.** Identical input must give identical output. No timestamps, durations, run counts or summary lines: anything that varies between runs never cancels in the set difference and surfaces as false breakage. This is why a bare `pytest -x` or `mypy .` is unsound — both print a summary line that differs run to run.
- **Repo-relative paths.** The three trees are materialised into three different temporary directories, so an absolute path never cancels and always reports false breakage.
- **Strip line and column numbers.** A finding string embedding a position changes whenever an unrelated edit shifts lines — it fails to cancel, and it churns the `finding_id` that recurrence tracking keys on. `tsc` emits `src/x.ts(4,1): error TS2551: …`, so it needs `| sed -E "s/\([0-9]+,[0-9]+\)//"`.
- **Strip absolute paths from message bodies too.** Some checkers embed the working directory inside a fixed-width-truncated message (`tsc`'s long type dumps do), and the truncation is computed before your `sed` runs — pipe through `sed -e "s#$(pwd -P)#.#g"` and know that a diagnostic truncated at its budget can still differ across trees. moire's own materialisation directories are equal-length by construction so the tool never causes this itself.
- **Path-prefixed findings survive renames; others do not.** Rename canonicalisation rewrites a finding's *leading path* into the merged tree's namespace before the subtraction, so `src/x.ts: error …` cancels across a peer's `git mv` and a finding that does not begin with a path does not. A path mentioned mid-line is deliberately left alone rather than rewritten by guesswork.
- **Context-invariance, which no checker fully has.** A finding whose text embeds information from elsewhere in the tree changes when that elsewhere changes: rename a type and every pre-existing `tsc` diagnostic mentioning it gets new text and fails to cancel. This is a known limit of the subtraction, not a bug to report.
- **Emit everything, every time.** A checker that stops early (`-x`, `--max-errors`, fail-fast) emits a *prefix* of its findings, and prefixes of different sets do not cancel.
- **A checker that exits nonzero with no output is recorded as such** — per-tree `checker_failed` flags in the JSON — because a tree where the checker could not run measured nothing, and silence must never read as cleanliness.
- **It runs on tracked files only.** The materialised tree is `git archive` output — no gitignored `node_modules`, `.venv` or `vendor`. `--link <name>` symlinks a named directory from the worktree into each tree instead; `<name>` must be a single path component. The link is live, not read-only, so only link a directory you're content to have your checker write into.
- **Invoke tool binaries directly**, never through `npm run` / `pnpm exec` / `yarn run`. The materialised tree is not a project directory, and package-manager wrappers do their own project discovery and dependency repair as a side effect of running your command.
- **Non-source import targets are unresolved, not broken.** A relative import resolving to a `.json`, `.css` or `.svg` has no export syntax to find. Treat it like an unresolvable path — an alias, a bundler-only import — not a missing export.

</details>

## Cost

Measured 2026-08-12 on a lab repository of 62 Python files with three peer
worktrees — method, machine and load in
[docs/MEASUREMENTS.md](docs/MEASUREMENTS.md#how-the-cost-table-was-measured):

| against 3 peers | warm | cold |
| --- | --- | --- |
| `moire check` | 219 ms | 404 ms |
| `moire verify` (builtin-ast, 62 files) | 454 ms | 635 ms |

**These are ceilings, not figures** — taken under load averages of 10–11 on 8
cores; an idle machine will be faster, nothing here will be slower. Point
`--checker` at anything real and cost becomes `snapshot overhead + K × checker
runtime`, where `K = 2 × peers + 1` — which is one more reason the deep check is
a deliberate act rather than a per-write default.

## From finding to conversation

A finding is only worth what happens next, and the two halves of *next* ship
separately in today's tooling. Agent messaging is **transport with no trigger** —
Claude Code's cross-session messaging is explicit that *"a message is a piece of
text one Claude writes to another"*, and a collision warning carried that way
fires only if an agent notices the collision, decides to send, and picks the
right session. moire is the trigger: it notices the fact, names it, and renders
it sendable. The join is one command wide — moire composes the message; the
agent sends it.

`moire pending` answers *what is outstanding between me and each peer* from the
log alone — no snapshot, no peer read, nothing written (a suite case pins that by
fingerprinting `.git/moire/` around five invocations). Each finding is judged
against the latest record **of its own kind**, so a routine textual check cannot
clear a semantic finding it never re-examined. From the same lab as above:

```
$ moire pending
pre-v2 records ignored            : 0
CONFLICT with /private/tmp/moire-lab/repo-agent-b (feat/b) [finding b13c7ab00ab2] kind=textual age=0s
    src/limits.py
  arbiter: self yields (tiebreak: self's name 'main' > peer's 'feat/b')
(from the log; oldest of the above is 0s old; re-run 'moire check' for a live answer)
```

`moire compose <finding-id>` renders one finding as a message, shaped for pasting
into whatever channel the harness provides:

```
$ moire compose b13c7ab00ab2 --action narrow
moire finding b13c7ab00ab2
(computable identically from your side - derived only from the two worktree paths and the contested paths/breakage, never from anything either of us declares)

FROM
  worktree : /private/tmp/moire-lab/repo-agent-a
  branch   : main
  HEAD     : c4a432532dcc0ea930882206991473afc7e724ac
  age      : 0s

THE FACT
  CONFLICT
  contested path(s): 1
    src/limits.py
  meaning: git will stop with conflict markers here

ARBITER
  recommendation: the sender (this side) yields
  reason: tiebreak: self's name 'main' > peer's 'feat/b'
  computed from facts observable to both of us; your moire reports the same recommendation - its 'self' is you

SENDER'S ACTION
  sender is narrowing their own change to drop the contested part

VERIFY
  run `moire check` in your own worktree - the same finding id (b13c7ab00ab2) confirms it
```

Four things in that message are load-bearing:

- **The finding id is the receiver's own check, not the sender's word** — both
  sides compute it independently and get the same string.
- **It composes only from records this side logged** — the same id sits in the
  peer's records with `self` and `peer` swapped, and rendering theirs would name
  the receiver as the sender; compose refuses instead, with an explanation.
- **The arbiter is translated across the boundary** — *the sender (this side)* /
  *the receiver (your side)*, because the stored labels are relative to whoever
  ran the check.
- **`SENDER'S ACTION` binds only the sender** — a statement, never a demand.

The receiving agent's first move is not to act on the message. It is to re-run
`moire check` in its own worktree; the same finding id coming back from its own
run is the confirmation, and until then the message is another agent's claim, not
evidence. `skills/moire/SKILL.md` instructs the receiving side in exactly those
terms.

**moire never transmits any of this.** There is no `moire send`, no socket, no
discovery, no inbox and no delivery state; `compose` is a pure function of the
log that writes to stdout. Owning the wire means owning identity, retry and a
config surface, and a tool that does can only be one harness's tool. The agent
owns the wire.

**Whether any of this changes what agents do is unmeasured.** `moire report`
counts findings *cleared* and *outstanding* — cleared meaning a later check of
the same kind no longer reports it, `(cause is not implied)` — which makes the
question answerable. That is the instrument for a clearance study, not the
study, and no data exists yet.

## What observation writes, and where

"The peer needs zero participation" has a cost, and it is the peer's: **a peer
cannot opt out of being observed.** Snapshotting runs `git add -A` through a
*copy* of the peer's index, so every file in the peer's worktree that is
**untracked and not gitignored** is written as a blob into the repository's
shared object store. That is load-bearing — the canonical example is a peer's
brand-new, not-yet-committed file, and it is invisible without this — but you
should know it happens.

Verified here 2026-08-12, on a lab repo with three peer worktrees: a peer's
untracked `.env.local` was found as a blob in the shared object store after one
`moire check`, and a file under a gitignored directory was not. Three properties
bound it:

- **No new read access.** The object store is shared by every worktree of the
  repo. Anyone who can read it could already read the peer's worktree directly.
- **Gitignored files are never captured.** `git add -A` respects `.gitignore`,
  so the ordinary hygiene of gitignoring `.env*`, credentials and key material
  is also the fix here. Do it anyway; do it first.
- **The exposure is persistence, not access.** The blob is refless — nothing
  shows it in a log or a diff, and it survives until git's housekeeping prunes
  it (two weeks by default for loose objects). `git gc --prune=now` removes it
  immediately; verified here.

## Why not do it another way?

Several other approaches exist. Their measured outcomes are more instructive
than the designs, and they are why moire is shaped the way it is.

| Approach | Example | What happened |
| --- | --- | --- |
| **Agents declare what they will touch**; a registry arbitrates | MCP Agent Mail, Agent Claim MCP, [wit](https://github.com/amaar-mc/wit), [grit](https://github.com/rtk-ai/grit) | Advisory by their own documentation — nothing enforces a claim — or enforced by a lock registry every agent must join. All fail open the moment one agent, say another vendor's, doesn't participate. |
| **Let the agents talk to each other** | Claude Code cross-session messaging | Shipped by the vendor, and explicitly transport: *"a message is a piece of text one Claude writes to another, never conversation history or files."* It fires only if an agent notices the collision, decides to send, and picks the right session. moire is the noticing-and-composing half of exactly that pipeline — [`pending` and `compose`](#from-finding-to-conversation) — without becoming the transport. |
| **Detect overlap at pull-request time** | [ConE](https://arxiv.org/abs/2101.06542) (Microsoft Research + TU Delft) | Works, at scale — flagged 775 of 26,000 pull requests (3.33%) across 234 repositories; 71.48% of notifications rated "Resolved" *by users*, a user rating and not precision against ground truth. Detects *file* overlap, after both branches already exist, and ships as a comment. |
| **Warn human developers proactively** | Crystal ([Brun et al., ESEC/FSE 2011](https://cs.uwaterloo.ca/~rtholmes/papers/fse_2011_brun.pdf)) | moire's direct ancestor: it merged peers' committed code, built it, ran its tests, and showed a per-peer icon. Fifteen years later, no published evidence of durable industrial adoption for it or any of its successors. |
| **Isolate, merge later** | every commercial agent orchestrator | Works, and defers the problem to a human at merge time. This is what everyone actually ships. |
| **Merge queues** | Mergify, GitHub merge queue | Real semantic detection: full CI on speculatively merged combinations, ejecting the culprit. It runs on completed, pushed PRs — the opposite end of the lifecycle from a live worktree. |
| **Partition the work before dispatch** | [Co-Coder](https://arxiv.org/abs/2606.00953) | The strongest result in the table: cohesion-aware partitioning beat the sequential baseline (68.1% vs 56.8% pass on DevEval), while *naïve* file-based parallelism cost 60% more for a 3.2% pass-rate gain. Greenfield generation, not repository modification. |

The first two rows share a shape: they ask an agent to describe or announce its
own work. moire never asks — it reads the other worktree's files, so there is no
declaration to be wrong. It is aimed at the case partitioning cannot reach:
tightly-coupled work is exactly where concurrent agents still collide — which
also means moire's addressable surface is the residue a good dispatcher leaves,
not "everyone running parallel agents".

## Status — read this before adopting

**`moire check`: done, and its event is measured.** Correct against real
`git merge` outcomes, tested, and aimed at a collision that occurs in roughly
one of five co-active agent pairs (measured above, corroborating published
rates). Everything it finds, git finds later, for free; its value is that it
finds it earlier, on live uncommitted trees, while both agents still have the
context to resolve it cheaply.

**`moire pending` / `compose`: shipped; their effect is unmeasured, and the
test is registered.** Whether a finding that reaches an agent changes what that
agent writes is an open quantity, and the strongest prior runs against it:
Crystal, the 2011 ancestor that warned humans proactively, shows no published
evidence of durable adoption fifteen years on. That history is the null
hypothesis for this layer.
[`CLEARANCE-PREREGISTRATION.md`](CLEARANCE-PREREGISTRATION.md) fixes the study
design and the decision rule before any field data exists — surfaced-vs-blind
arms, randomized per session, minimum thirty findings each — and if surfacing
findings does not measurably change clearance, the claims here get demoted to
delivery mechanics, exactly as the rule says.
[`report`'s cleared/outstanding counts](#from-finding-to-conversation) are the
instrument.

**`moire verify`: an instrument with a measured base rate.** The mechanism is
tested, graded against CPython, and audited end to end; the failure class it
detects occurs at **0 of 672** audited PR-stage pairs (upper bounds 0.65% /
3.55% — [full results](research/phase1-results/RESULTS.md), decision rule fixed
before the data in [`PHASE1-PREREGISTRATION.md`](PHASE1-PREREGISTRATION.md)).
The measured scope has honest edges: no tests were run, and mid-session
uncommitted work has no corpus — the study measures PR-stage pairs.

**`moire replay`: the measurement instrument** behind those numbers — stateless,
works in a bare clone, and is how anyone can re-run them
([`tools/replay-corpus/`](tools/replay-corpus/)).

## Tests

```bash
bash tests/test_oracle.sh    # 12 cases: conflict detection vs real `git merge`
bash tests/test_install.sh   # 21 cases: install, hooks, path resolution, concurrency, object-store growth
bash tests/test_report.sh    # 19 cases: finding identity, pair-state metrics, replay statelessness, pending and compose
bash tests/test_setup.sh     # 14 cases: init-swarm, wire-client, settings-file handling
bash tests/test_verify.sh    # 45 cases: the semantic path — new_breakage, renames, --link union, replay
bash tests/negative_control.sh   # proves the five suites above can fail
bash tests/benchmark_recall.sh   # 19 collision fixtures graded by CPython, not by moire
```

**111 cases; measured 2026-08-25: 110 passed, 1 skipped, 0 failed.** The skip is
a `DeprecationWarning` check that only applies on Python 3.12+ and this machine
runs 3.8.2. `tests/negative_control.sh` is the answer to "a test suite that
cannot fail is worse than none": it points `MOIRE_BIN` at a `#!/bin/sh; exit 0`
stub and then at a path that does not exist, and asserts that **every** suite
exits nonzero in both scenarios — 10 of 10 checks go red as required.

`test_oracle.sh` has the strongest ground truth (a real `git merge`, compared);
`tests/benchmark_recall.sh` grades the semantic checker against CPython on the
merged tree rather than against moire's own output, and includes a
truncation-invariance control for external checkers. What each suite can and
cannot prove — and what the benchmark's score means — is in
[docs/MEASUREMENTS.md](docs/MEASUREMENTS.md#what-the-test-suites-can-and-cannot-prove).

## Repository layout

```
bin/moire            the tool — a single file, Python 3.8, standard library only
skills/              two Agent Skills: one for acting on a finding, one for
                     setting up parallel work
tests/               111 cases across five suites, plus the negative control and
                     the recall benchmark
tools/replay-corpus/ the corpus measurement harness (stdlib only, not shipped)
docs/                INSTALL.md and MEASUREMENTS.md — the detail behind this page
research/phase1-results/    the Phase 1 measurement: results, gates, audit, and
                     a submission-ready research note (NOTE.md)
PHASE1-PREREGISTRATION.md   the semantic-rate decision rule, committed before any data
CLEARANCE-PREREGISTRATION.md   the resolution-layer decision rule, committed before any data
CHANGELOG.md         what changed in each release, and why
package.json         private test-runner manifest — `npm test` only, never published
README.md            this file
LICENSE              MIT
```

There is no build step, no configuration file and no runtime dependency beyond
git.

## A note on the numbers

Every figure here is one of three things, and which one is always stated:
**measured here** (dated, machine attached, published as a ceiling where load
makes it one), **this project's own working notes** (labelled as its word), or
**cited to a primary source with its denominator attached**. The full ledger —
method and machine for every measurement, the citation table, the scope of every
score, and the Phase 1 study end to end — is
[docs/MEASUREMENTS.md](docs/MEASUREMENTS.md).

That ledger also states [the strongest published argument against this
project](docs/MEASUREMENTS.md#the-strongest-argument-against-this-project)
rather than omitting it: Mergify's *State of Merge Queues 2026* found
AI-assisted PRs broke main **1.9%** of the time against **4.4%** for PRs with no
detectable AI assistance, across 200,000+ merges — if AI-authored changes
integrate more safely, the premise here weakens. The same report finds
broken-main scaling with concurrency, from 0.77% at 2–5 engineers to 12.5% at
40+, which cuts the other way. The caveats on both cuts are in the ledger.

These are one person's measurements plus other people's published work. They are
stated precisely so that they can be contradicted.

## License

MIT — see [LICENSE](LICENSE).
