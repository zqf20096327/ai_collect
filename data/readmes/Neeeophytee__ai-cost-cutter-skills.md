<div align="center">

<img src="banner.svg" alt="AI Cost-Cutter Skills. Cut your AI bill with proof, not vibes." width="100%" />

# AI Cost-Cutter Skills

**10 installable skills that cut your AI bill with proof instead of vibes. Free, MIT.**

[![verify](https://github.com/Neeeophytee/ai-cost-cutter-skills/actions/workflows/verify.yml/badge.svg)](https://github.com/Neeeophytee/ai-cost-cutter-skills/actions/workflows/verify.yml)

</div>

Every "switch to a cheaper model" tip has the same missing piece: evidence that the cheap path still does *your* job. These skills close that gap. Each one turns a cost-cutting pattern into a procedure your coding agent runs, and every skill carries a **runnable proof block** that this repo's CI actually executes on every push and weekly on a schedule. The badge above is real, not decorative. Each skill is distilled from a recipe in the [FlowStacks](https://flowstacks.xyz) corpus, where the deterministic spine is re-checked by CI so the recipe can't silently rot.

Works in Claude Code, OpenAI Codex, Cursor, and any agent that reads the [agentskills.io](https://agentskills.io) SKILL.md format.

## The idea in one sentence

The reason people overpay for AI isn't missing tooling; it's missing trust in the cheap path. So every skill here ends with a check you can run, not a claim you have to believe.

## The skills

| Skill | Lever | One line |
|---|---|---|
| [`route-cheap-escalate-hard`](skills/route-cheap-escalate-hard/SKILL.md) | Routing | Cheap default, premium only on gated hard turns; measured per task, not per token |
| [`advisor-call-budget`](skills/advisor-call-budget/SKILL.md) | Routing | Cap how often the expensive advisor gets called; compute the real discount from actual calls |
| [`cheap-swap-guard`](skills/cheap-swap-guard/SKILL.md) | Routing | Before any cheap swap, declare the cases the premium model dominates and keep them premium |
| [`token-receipts-audit`](skills/token-receipts-audit/SKILL.md) | Visibility | Attribute spend by tokens AND dollars; volume and value are different leaderboards |
| [`context-diet`](skills/context-diet/SKILL.md) | Tokens | Index once, query small; stop re-reading files into context, and measure the drop |
| [`reasoning-effort-throttle`](skills/reasoning-effort-throttle/SKILL.md) | Tokens | Don't pay for deep thinking on easy turns; escalate effort per task, by rule |
| [`model-bakeoff`](skills/model-bakeoff/SKILL.md) | Evidence | Compare models on your real prompts, inside a free tier's caps, criterion stated first |
| [`tested-fallback`](skills/tested-fallback/SKILL.md) | Resilience | Pin an open-weights fallback with a tested-on date; a backup you never ran is a hope |
| [`free-tier-batch-plan`](skills/free-tier-batch-plan/SKILL.md) | Free tiers | Size a big batch to the rate limit and token budget before starting, with a proven ETA |
| [`free-model-triage`](skills/free-model-triage/SKILL.md) | Free tiers | Route reading-pile triage to a free model with a strict summary + needs-reply schema |

## Install

**One command, any agent (recommended):** Vercel's `skills` CLI auto-detects your coding agent (Claude Code, Cursor, Codex, Copilot, Gemini, and more) and installs into the right place for each:

```
npx skills add Neeeophytee/ai-cost-cutter-skills
```

Add `--list` to preview the 10 skills first, or `--skill token-receipts-audit` to install just one. (Discoverable on [skills.sh](https://skills.sh).)

**As a Claude Code plugin (all 10 skills):**

```
/plugin marketplace add Neeeophytee/ai-cost-cutter-skills
/plugin install cost-cutter@ai-cost-cutter-skills
```

**Manually (pick the skills you want):** copy any `skills/<name>/` folder into your project's `.claude/skills/` directory (or `~/.claude/skills/` for all projects). Codex reads the same format from `~/.agents/skills/`.

**The one-file version:** for the whole approach as passive guidance instead of commands, drop [`CLAUDE.md`](CLAUDE.md) (Claude Code) or [`AGENTS.md`](AGENTS.md) (Codex and other AGENTS.md-reading agents) into your project root, or append it to your existing one.

## When to reach for which

- The bill is high and you don't know why → `token-receipts-audit` first, always
- Bulk workload on a premium model → `route-cheap-escalate-hard`
- Cheap executor + expensive reviewer → `advisor-call-budget`
- "Can I just switch to the cheap one?" → `cheap-swap-guard`
- Coding agent re-reads the same files forever → `context-diet`
- Reasoning model, mostly easy turns → `reasoning-effort-throttle`
- New model launched, tempted → `model-bakeoff`
- Everything depends on one hosted model → `tested-fallback`
- Huge one-time backlog, no budget → `free-tier-batch-plan`
- Drowning in a reading pile → `free-model-triage`

See [EXAMPLES.md](EXAMPLES.md) for real prompts.

## How verification works (and what it doesn't claim)

Two honest layers:

1. **This repo's CI** extracts every skill's `bash verify` proof block and executes it on every push and weekly on a schedule. If a proof stops passing, the badge at the top goes red. No proof, no merge.
2. **The upstream recipes** at FlowStacks re-run each recipe's deterministic spine (configs, schemas, arithmetic) in CI on every change. The model steps (actual quality, actual per-task cost on your workload) are explicitly **fenced**: no CI can promise those, so neither do we. Every skill says out loud which part is proven and which part you must measure on your own traffic.

That second sentence is the whole philosophy: a badge should never claim more than what actually ran.

## License

[MIT](LICENSE). Prices and limits cited inside skills carry their as-of dates; check current pricing pages before relying on them.

---

<sub>Maintained alongside [awesome-ai-workflows](https://github.com/Neeeophytee/awesome-ai-workflows), a list of AI workflows re-checked by CI, [finding-unknowns-skills](https://github.com/Neeeophytee/finding-unknowns-skills), and [FlowStacks](https://flowstacks.xyz), where each recipe carries a machine-verified badge. If this pack saves you money, a star helps the next person find it.</sub>
