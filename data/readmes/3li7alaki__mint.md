# mint

> Drivers organize and execute work. mint records why an atomic unit is allowed
> to be called done.

[![License: MIT](https://img.shields.io/badge/license-MIT-black)](LICENSE)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-support-ff5e5b?logo=kofi&logoColor=white)](https://ko-fi.com/3li7alaki)

An agent will report success. That report is a sentence, not evidence, and
nothing in the loop was ever asked to tell the two apart. mint is a small CLI
that holds the completion floor: declared gates, an independent check that mint
itself runs, and a receipt bound to the exact source it verified.

It owns only that. Your driver keeps projects, tickets, terminals, agents,
worktrees, retries, Git and deployment.

## Install

```bash
curl -fsSL https://raw.githubusercontent.com/3li7alaki/mint/main/install.sh | sh
```

One static binary for macOS and Linux. It creates no `.mint` directory in your
repo and never edits your `.gitignore`. State lives under `$XDG_STATE_HOME/mint`,
keyed by repository and isolated per worktree. Set `MINT_STATE_HOME` to move it.

## What a run looks like

Real output from [`docs/examples.sh`](docs/examples.sh), which runs this walkthrough
and its failure cases against the current build. State paths are shortened to `...`.

Define the unit: one goal, a scope, acceptance in EARS form, the gates to run and
the reviews it needs.

```console
$ mint spec new "expose service health" --slug health-check \
    --goal "Expose service health" --scope "src/**" \
    --acceptance "WHEN the health endpoint is called, THE service SHALL return its status" \
    --gate "tests: test -f src/app.go" --reviews adversarial
{
  "schemaVersion": 1,
  "specPath": ".../units/health-check/001/spec.xml",
  "slug": "health-check",
  "id": "001",
  "target": "main"
}
```

Start an attempt and say who is doing the work. The baseline is the point where
the lane branched off its target, like a pull request's diff, so work committed
before this command and uncommitted work are both inside what gets checked.

```console
$ mint exec init health-check 001 --attempt maker-1 \
    --executor codex --vendor openai --model gpt-6.1-sol \
    --locality local --execution-ref run-42
{
  ...
  "baseCommit": "2f6c2a36f46c1b42a02f01ba68ca554cc5d6299c",
  "target": "main"
}

$ mint verify health-check 001 --attempt maker-1
  tier: full - ok tests
```

Finish it with a checker that mint launches. Here it is a script; in real use it
is a model from a different vendor than the maker. Keep the checker outside the
repository, or it becomes an out-of-scope file in the lane's own diff. Its `ATTEST adversarial` line
meets the review the unit asked for.

```console
$ mint done health-check 001 --attempt maker-1 --checker ~/checkers/health.sh \
    --checker-executor claude-code --checker-vendor anthropic \
    --checker-model opus-5.5 --checker-locality local --checker-execution-ref check-7
  PASS - floor clean, done
    ok clause 1: verifiable-completion
    ok clause 2: maker-not-checker
    ok clause 3: safety-carve-out
    ok clause 4: anti-gaming
    ok clause 5: scope-respected
    ok clause 6: bounded-terminating
    ok clause 7: floor-gated-action
  receipt: .../receipts/health-check/001/20261108T100002-798365000Z-dc4920fc8464.json

$ mint receipt verify .../20261108T100002-798365000Z-dc4920fc8464.json
current sha256:b1880752f133393741d71a07702f7533c0ebe1e715a214feedca7b3693f204c7
```

Change one line of source, then ask again:

```console
$ mint receipt verify .../20261108T100002-798365000Z-dc4920fc8464.json
stale sha256:b1880752f133393741d71a07702f7533c0ebe1e715a214feedca7b3693f204c7 - source snapshot changed after receipt issuance
```

That is the whole product. A claim that outlives the code it described is not a
claim any more, and now you can ask.

It also holds when a lane commits a file outside its scope before the attempt
even starts:

```console
$ mint done sneaky 001 --attempt maker-2 --checker ~/checkers/health.sh ...
  FAIL - floor not clean (failed clauses: 5)
    ...
    fail clause 5: scope-respected - out-of-lane file(s): README.md, allowed: src/**
```

## The floor

Seven fixed clauses, the same for a typo and for an auth rewrite: verifiable
completion, maker and checker independence, the safety carve-out, anti-gaming,
scope, bounded terminal state, and floor-gated consequential action.

**What gets checked.** The diff runs from the merge-base of the lane with the
spec's target branch, recorded when the spec is created and printed by
`spec new` (`--target`, or a default chosen from `origin/HEAD`'s branch, `main`
and `master`; [AGENTS.md](AGENTS.md) gives the exact rule). Check the printed
target. After a rebase, start a new attempt; the spec stays.
Each attempt is graded against the exact spec it started with, and the spec cannot
be edited while an attempt runs, so a lane cannot widen its own scope to pass.
(Attempts begun by a mint older than this rule are not checked.)

**Gates** are the commands the spec declares, nothing guessed. They run in a clean
replay worktree whenever the attempt has a baseline, which every attempt started
by current mint does. Regular files under `<protected>`, plus CI workflows and hook config by
default, are restored there to their baseline bytes, and mint hashes them on disk
to prove it. A spec that declares gates gets them even for a docs-only change. If
the source changes while the gates run, `done` and `run-review` refuse to grade it.

**Reviews** count only when mint saw them happen: a checker mint launched
attested the lens, or `mint exec run-review` ran the reviewer itself. A review
typed in with `mint exec record-review` is stored as declared and never meets a
required lens.

**Independence** is structural. The checker must come from a different execution
than the maker. Safety work, which the floor detects from the diff or a spec
declares with `<risk>safety</risk>`, needs a different model vendor, and so does
any safety review lens a spec asks for, such as `security`. A box with one vendor
can finish a safety tier the floor only inferred, when a checker mint ran attests
`vendorDiversity`; the receipt then says `vendorDiverse: false`. That waiver never
covers a declared tier or a declared safety lens.

**Verdict files** (`--verdict`) still work for checkers mint cannot launch. They
default to `declared`, cannot claim to be the checker, and cannot waive
vendor diversity.

Provenance is a declared record. `executor`, `vendor`, `model`, `locality` and
`executionRef` are attributable claims mint stores; it does not pretend to
authenticate an identity it cannot see.

## What it does not stop

mint runs as you, and so do the agents it checks. An agent that can write your
`.git` directory or mint's state directory can still fake evidence there. mint
closes the known tricks (replaced objects, grafts, forged history files, filters
that rewrite protected files) but cannot fence off the same user. That boundary
needs isolation: gates and checkers in a separate machine or VM with a read-only
copy of the repository. It is planned, not built.

## Commands

| command | does |
|---|---|
| `mint spec` | define, edit, validate and inspect an atomic unit |
| `mint exec` | start an attempt, run observed reviews, record gate and terminal evidence |
| `mint verify` | run the unit's declared gates in a clean replay |
| `mint review` | print a review lens prompt. It never launches a model |
| `mint done` | evaluate the floor and issue an immutable receipt |
| `mint status` | report units, attempts, missing evidence and freshness |
| `mint receipt` | show or verify a receipt |
| `mint note` | keep unit and floor reasoning |
| `mint clean` | report or remove leftover locks, baseline refs and incomplete receipt claims |

`verify`, `done`, `status` and `receipt` take `--json`, and `spec new` and `exec`
always answer in JSON. Integrate against the JSON, never the human output.

## What it is not

- Not a work organizer. Tickets, worktrees, branches and retries stay with your driver.
- Not a decision about what is worth building. That is [blueprint](https://github.com/3li7alaki/blueprint).
- Not an agent runner, and not an authority on who ran what.

## More

- [AGENTS.md](AGENTS.md) is the exact operating contract for agents working through mint.
- [docs/principles.md](docs/principles.md) covers the product boundaries.
- [formats/](formats/README.md) holds the draft (v0) formats for signed, portable receipts.

## Support

mint is free and MIT licensed, and there is no pricing page. If it saved you an
afternoon, that is worth about the price of a coffee.

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/3li7alaki)

Need something like this built for your own stack? Commissions are open at
[ko-fi.com/3li7alaki](https://ko-fi.com/3li7alaki).

## License

MIT. See [LICENSE](LICENSE).
