# slopcheck

**Measure and stop structural erosion in AI-written TypeScript.**

AI writes code that works. It passes the tests, the app runs, everything looks fine.
And then, the longer it builds on its own work, it quietly makes a mess inside:
one function doing ten jobs, branches on branches, the same thing copied five times.
That mess is real, and it is measurable.

`slopcheck` measures it. **Slop Check** finds the mess and gives it one honest number.
The **Deslop** side (a skill plus this tool's checks) cleans it up, one knot at a time,
and proves the mess is gone rather than just moved.

Based on **SlopCodeBench** ([arXiv:2603.24755](https://arxiv.org/abs/2603.24755)).

## The one number

```
erosion = Σ mass(f) for callables with CC > 10
          ─────────────────────────────────────
          Σ mass(f) for all callables

mass(f) = CC(f) × √SLOC(f)
```

The square root is deliberate. Complexity dominates, size only modulates. A long,
flat function is not the failure mode. A short, branchy one is.

**Reference points, from the paper.** 473 human repositories average **0.34**. Coding
agents average about **0.68**, roughly twice as eroded, and erosion rises in **77%** of
agent trajectories. Treat these as orientation, not thresholds. The number that matters
is your own trend over time.

## Install

```bash
bun install
```

Requires [Bun](https://bun.sh). It reads `.ts` and `.tsx` (React files included, which
the paper's own checker silently skips).

## Use

```bash
bun cli.ts audit <path>                      # measure one repo
bun cli.ts audit <path> --json               # machine-readable
bun cli.ts baseline <path>... --out=baselines # save a "before" snapshot
bun cli.ts delta baselines/repo.json <path>  # compare; exits 1 if erosion rose
```

## The hook (report, never block)

`hooks/erosion-check.ts` is a Claude Code Stop hook. After each turn of work it
re-measures against the saved baseline and reports the change. It never blocks. The
first time it sees a repo it just saves the baseline. Install it in `~/.claude/settings.json`:

```json
{ "hooks": { "Stop": [{ "hooks": [{ "type": "command",
  "command": "bun ~/development/slopcheck/hooks/erosion-check.ts" }] }] } }
```

A quality signal that halts a session gets disabled within a week. One that reports gets
read. That is the whole design.

## Two decisions worth knowing

**What counts as a callable.** Erosion is a ratio over that set, so the definition moves
the score more than anything else. Default is `named`: declarations, methods, constructors,
accessors, and functions bound to a name. `--callables=all` adds anonymous inline callbacks,
which drags erosion down by padding the denominator with tiny zero-branch arrows. The choice
is stamped into every result, and `delta` refuses to compare across definitions.

**Verbosity, under a stamped rule pack.** The paper's verbosity rules are all Python, so this
tool computes its own: `rules/` carries **ts-pack-v1**, ast-grep rules for TypeScript, each
with the evidence it was authored from (see `rules/README.md`). Every result stamps
`rulesVersion`. `cloneShare` is reported separately, named for what it is.

## The experiment

`experiment/` holds a pre-registered study: does re-asserting the quality prompt on
**every** checkpoint bend the erosion curve, rather than only warning once at the start?
It runs on a small synthetic CLI app, four arms, three runs each. Short version: warning
once barely helps; reminding and checking every step keeps erosion low at no cost to the
tests passing. The finding is the repetition, not the wording.

## The story

`slides/slopcheck-story.html` is a self-contained slide deck that walks through all of
this for a non-specialist audience. Open it in a browser, arrow keys to move.

## License

MIT. Yours forever.
