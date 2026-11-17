# The Guided Model Router

A token-economical, quality-first **model & effort router** for [Claude Code](https://claude.com/claude-code) — now an installable plugin that actively nudges every turn, proves what it saved, and never blocks you.

Claude Code has no built-in router that switches models by task complexity. v1 of this project added one as a static prompt: a triage table the main model was supposed to remember. v2 makes routing **active**: a hook classifies every prompt and injects a one-line hint, pinned subagents enforce the actual model swap, and `/router-stats` shows the real dispatches, tokens, and estimated dollars saved.

## The ladder

| Task | Tier | Agent |
|------|------|-------|
| broad search / grep / "where is X" | Haiku · low | `Explore` |
| 1-file edit, rename, format, known command | Haiku · low | `quick-haiku` |
| standard feature / refactor / tests | Sonnet · medium | `worker-sonnet` (parallel-friendly) |
| subtle bug / architecture / perf, well-posed | Opus · high | inline or `deep-opus` |
| complex / novel / ambiguous, **substantial plans & design decisions**, or a failed tier | **Fable · xhigh** | `deep-fable` |

Default main model is **Opus 4.8 / high effort** (quality-first). Three postures are available (below); the ladder and its agents are identical across all of them — only the starting rung moves.

## What's new in v2

**Active routing, not a memorized table.** A `UserPromptSubmit` hook (`bin/classify.sh`) reads every prompt, scores it against local heuristics in `config/rules.json` (pattern match, zero API cost), and — if the result is ambiguous — can optionally fall back to one tiny Haiku call. It then injects a one-line routing hint into context: *"this looks like standard → consider dispatching `worker-sonnet`."* The main model doesn't have to remember the ladder anymore; it gets reminded every turn. The hook is fail-open by design: any error, missing dependency, or disabled classifier means no hint and a clean exit — it never blocks or slows a turn.

**Fable participates in planning.** Substantial plans and architecture/design decisions — *"make a plan for X"*, *"what's the best approach"*, *"weigh the options"*, *"how should we structure this"* — now route to the `complex` tier and dispatch `deep-fable`, instead of being absorbed inline on Opus. Quick, well-posed plans stay on Opus; the point is that the strongest reasoning *participates* in the hard planning, not that every plan escalates.

**Proof, not a promise — who actually ran.** A `PreToolUse(Task)` hook (`bin/log-dispatch.sh`) logs every subagent dispatch to a local JSONL ledger. Run `/router-stats` and it leads with a **per-tier, per-model delegation table** straight from that ledger — the honest answer to *"was that Haiku, Sonnet, Opus, or Fable?"* It then shows main-loop token usage from the session transcript (labeled as such — a subagent's tokens live in its own context and never enter the main transcript) plus an estimated dollar amount kept off the baseline model.

**Ships as a plugin.** Install from a marketplace in two commands, or keep using the manual script if you don't want the plugin system. Ships with an English stub by default; a French locale is available in `locales/`.

**Configurable end to end.** Every tier's agent/model/effort, three ready-made postures, classifier knobs, and per-model pricing live in `config/router.config.json`; the classifier's pattern rules live in `config/rules.json`. Model IDs live only in that one config file, so there are no dated model IDs scattered through prompts to rot.

## Why it saves tokens (for you and for Anthropic)

Two mechanisms, not just "a cheaper model":

1. **Cheaper tier per task** — searches and mechanical edits run on Haiku instead of the flagship, standard work runs on Sonnet, and Opus/Fable are spent only where they earn it.
2. **Context isolation (the big one)** — a subagent reads files in *its own* context and returns only a short conclusion. Those file contents never enter the main thread, so every later turn stays cheap. File-heavy work is pushed into disposable contexts.

v2 adds a third lever: **active enforcement**. In v1, savings depended on the main model remembering to delegate. In v2, the classifier hint nudges it every turn, and `/router-stats` shows whether the nudge is actually being followed. The ledger makes it concrete: you can see exactly how many tasks each tier absorbed, and estimate what that delegation kept off the baseline model — see the sample report below.

Fixed overhead is kept deliberately small: the always-loaded stub is about 15 lines per turn, and the classifier hook is a fast local shell script per prompt (no network call unless the prompt is ambiguous and the Haiku fallback is enabled).

## Install

### As a plugin (recommended)

```
/plugin marketplace add nobodyohm-web/claude-code-model-router
/plugin install model-router
```

That's it — the agents, skill, hooks, and config load automatically. Restart Claude Code if prompted.

### Manual install

```bash
git clone https://github.com/nobodyohm-web/claude-code-model-router && cd claude-code-model-router
./install.sh          # idempotent; supports --dry-run to preview changes
# then restart Claude Code
```

`./uninstall.sh` reverses it cleanly. Use this path if you're not on a Claude Code build with plugin support, or prefer to vendor the files directly into `~/.claude`.

Either way, work normally afterwards — the router routes on its own. Force a tier by naming its agent ("use `deep-fable` for this").

## Prove it: `/router-stats`

```
$ /router-stats

Model Router — who did the work
================================

Delegations by tier (from ledger — this is who actually ran):
  tier        model               count   share
  standard    claude-sonnet-5     3       43%
  search      claude-haiku-4-5    2       29%
  complex     claude-fable-5      1       14%
  mechanical  claude-haiku-4-5    1       14%
  total                           7

Main loop this session (from transcript — main model only, NOT subagents):
  claude-opus-4-8       in 210,400  out 12,800   $1.37

Estimated tokens kept off claude-opus-4-8 (rough proxy):
  ~$0.53 saved by delegating 7 task(s) to cheaper tiers instead of the baseline.

Note: delegation counts are exact (from the ledger). Transcript tokens cover the main loop
only — subagent tokens live elsewhere — so the "saved" figure is an ESTIMATE from the per-tier
averages in config/router.config.json (stats.est_tokens_per_dispatch), priced vs the baseline.
```

The delegation counts are **exact** — every dispatch is logged, so the "who ran" table is ground truth. The transcript section covers the **main loop only**: in real Claude Code a subagent's tokens live in its own context and never enter the main transcript, so they can't be summed there. The "saved" figure is therefore an honest **estimate** — ledger dispatch counts × the rough per-tier token averages in `config/router.config.json` (`stats.est_tokens_per_dispatch`), priced against the baseline model. Edit those averages, the prices, or the baseline and the estimate moves with them — it's not a billed number from Anthropic.

`/router-stats` also prints an **"Effort distribution"** section and an effort column on the delegation table, since effort now varies independently of tier (see `effort_variants` below) — the ledgers log the effort of every classification and dispatch, so you can see not just which tier ran but at what effort.

## Configure

Everything lives in `config/router.config.json` (tiers → agent/model/effort, classifier knobs, pricing) and `config/rules.json` (the classifier's pattern rules, one weighted rule set per tier).

| Profile | `model` | `effortLevel` | Note |
|---------|---------|----------------|------|
| `quality-first` (default) | `opus[1m]` | `high` | Opus orchestrates, delegates down, escalates to Fable. |
| `balanced` | `sonnet[1m]` | `medium` | Sonnet orchestrates, Opus is the hard tier, Fable for complex. |
| `max-savings` | `haiku` | `low` | Haiku pilots and delegates almost everything upward. |

Switch profiles by setting `"profile"` in `config/router.config.json`, or hand-edit `model`/`effortLevel` in `settings.json` directly — the agents and rules are identical across postures, only the starting rung moves.

Other useful knobs, all in `config/router.config.json`:

- `classifier.enabled` / `classifier.inject_hint` — turn the active hook on/off without uninstalling.
- `classifier.haiku_fallback` — whether ambiguous prompts get one small Haiku call (needs `ANTHROPIC_API_KEY`).
- `classifier.confidence_margin` / `classifier.min_prompt_chars` — how decisive a match must be, and how short a prompt can be before it's skipped entirely.
- `telemetry.enabled` / `telemetry.ledger_path` — where dispatches are logged for `/router-stats`.
- `telemetry.log_classifications` / `telemetry.classifications_path` — whether `classify.sh` also records the routed tier of every prompt (defaults on; path defaults to `classifications.jsonl` beside the dispatch ledger), so `/router-stats` can show what the router suggested per request even when nothing was delegated.
- `stats.baseline_model` / `stats.est_tokens_per_dispatch` — the baseline the "saved" estimate is measured against, and the rough per-tier token averages it multiplies dispatch counts by (subagent tokens aren't in the transcript, so this is the honest proxy).
- `pricing_usd_per_mtok` — per-model input/output prices used for the cost estimate; edit these to match your actual plan.
- `effort_variants` / `stats.effort_output_multiplier` — the tier×effort agents the classifier can route to, and the per-effort output-cost weights `/router-stats` uses to estimate effort-aware savings.
- `effort_signals` (in `rules.json`) — quick/thorough phrases that modulate effort ±1 independently of the tier.

## How it works

- **Stub** (`locales/stub.en.md`, appended into `CLAUDE.md` by `install.sh`, or auto-loaded as a plugin) — the always-on ladder table, so routing is visible every turn without a lookup.
- **Agents** (`agents/*.md`) — five tiered subagents, each pinned to a `model` + `effort`. Loaded only when dispatched, so the rich guardrails in their bodies cost nothing until they run.
- **Skill** (`skills/model-router/SKILL.md`) — the full policy: decision procedure, escalation protocol, parallelism and supervision guidance, anti-patterns. Lazy-loaded, zero cost until consulted.
- **Hooks** (`hooks/hooks.json`) — `UserPromptSubmit` runs `bin/classify.sh` (the active classifier); `PreToolUse(Task)` runs `bin/log-dispatch.sh` (the dispatch ledger).
- **`bin/` scripts** — `classify.sh` (heuristics + optional Haiku fallback, fail-open; also logs each prompt's routed tier to the classifications ledger), `log-dispatch.sh` (append-only JSONL logger), `router-stats.sh` (opens with a per-request "router suggestions" table from the classifications ledger, then the dispatch ledger's per-tier/per-model delegation table, main-loop transcript tokens, and an estimate of what delegation kept off the baseline).
- **`config/`** — `router.config.json` (tiers, profiles, classifier knobs, pricing) and `rules.json` (classifier pattern rules). The single source of truth for every model ID, so nothing rots when a model is renamed.
- **`skills/router-stats/SKILL.md`** — wires the `/router-stats` command to `bin/router-stats.sh` and adds the "these are estimates" caveat automatically.
- **`.claude-plugin/`** — `plugin.json` and `marketplace.json`, so the whole thing installs as a single Claude Code plugin.
- Quality gates: `tests/*.bats` exercise the classifier's routing decisions against a labeled prompt corpus, and GitHub Actions runs them (plus shellcheck) on every push.

## Notes / limits

- **No mid-session model swap exists in Claude Code.** A hook cannot change the model the main conversation is running on — that's an API-level constraint, not a bug here. Enforcement in v2 is therefore two-layered: pinned-model subagents (the only place the model actually changes) plus the injected hint (the only lever that influences the *main* model's own behavior). The router steers; it doesn't override.
- **The dollar figure is an estimate.** The delegation counts in `/router-stats` are exact (from the ledger), but the "saved" figure multiplies those counts by the rough per-tier token averages in `config/router.config.json` (`stats.est_tokens_per_dispatch`) and prices them against the baseline — because a subagent's real tokens never land in the main transcript. Treat "saved" as directionally accurate, not a reconciled invoice.
- **The Haiku fallback needs `ANTHROPIC_API_KEY`.** Without it, the classifier still runs — it just relies on the local heuristics in `rules.json` and abstains (no hint) on genuinely ambiguous prompts instead of calling out to Haiku.
- **Fixed overhead per turn:** the always-loaded stub is roughly 15 lines, and the classifier hook runs one fast local script per prompt. Both are designed to cost less than the first delegated search repays.
- The plugin ships with an English stub by default (`locales/stub.en.md`); a French version is in `locales/stub.fr.md` if you prefer to route in French — routing behavior itself is language-independent.
- No secrets or project data are included — this is pure editor configuration plus local, append-only telemetry ledgers under `~/.claude/router/` (`dispatches.jsonl` and `classifications.jsonl`).
