<div align="center">
  <img src="assets/readme/hero-the-sharks.svg" alt="The Sharks — five specialist shark agents at the startup reality-check table" width="100%" />
  <h1>THE SHARKS</h1>
  <h3>The startup reality-check engine.</h3>
  <p><strong>Your idea doesn't need applause. It needs five independent lines of attack.</strong></p>
  <p>One orchestrator. Five specialist AI agents. A sharper path from pitch to proof.</p>
  <p>
    <img src="https://img.shields.io/badge/AI%20Agents-5-20b8a8?style=for-the-badge" alt="Five AI agents" />
    <img src="https://img.shields.io/badge/Skills-6-4d91d9?style=for-the-badge" alt="Six skills" />
    <img src="https://img.shields.io/badge/Architecture-Model--agnostic-9875d7?style=for-the-badge" alt="Model agnostic architecture" />
    <img src="https://img.shields.io/badge/License-MIT-f0b44d?style=for-the-badge" alt="MIT License" />
  </p>
  <p><a href=".agents/skills/">Browse all six skills</a> &nbsp;·&nbsp; <a href=".agents/skills/the-sharks/SKILL.md">Master orchestrator</a></p>
</div>

---

## The market is the toughest investor in the room.

A polished pitch cannot prove demand. A large market cannot rescue broken unit economics. A clever product is not a moat. And encouragement is not validation.

**The Sharks is a multi-agent startup evaluation framework built to challenge the business before customers, competitors and investors do.** Each specialist attacks a different failure surface. The orchestrator combines their findings into a clear verdict, the riskiest assumption and a ranked list of experiments.

Built for founders, startup teams, builders, accelerators and investors who would rather discover the weak point early than explain it later.

> **Pitch the idea. Defend the assumptions. Test what survives.**

## Meet the five specialists

<div align="center">
  <img src="assets/readme/agents-lineup.svg" alt="Five distinct shark agent portraits: MINT, MAGNET, LEDGER, RAZOR and FORGE" width="100%" />
</div>

| Specialist | What it pressure-tests | The question it will not let go |
|---|---|---|
| **MINT · Revenue** | Payer vs. user, willingness to pay, pricing, urgency, recurrence and expansion | *Who pays, how much, why now—and why again?* |
| **MAGNET · Customers** | Ideal customer profile, first 10/100 prospects, acquisition channels, CAC, activation and retention | *Can you reach and keep customers at a viable cost?* |
| **LEDGER · Numbers** | Variable and fixed costs, gross and contribution margin, CAC payback, burn and break-even | *Does each sale make money after every real cost?* |
| **RAZOR · Competition** | Direct rivals, substitutes, manual workarounds, switching costs, positioning and defensibility | *Why switch to you—and what stops others copying you?* |
| **FORGE · Founder** | Founder-market fit, customer access, team capability, execution evidence and commitment | *Why is this the team equipped to win?* |

Each Shark has its own specialist skill and standalone agent prompt. The master skill coordinates the panel; hosts with native subagent support can run the specialists independently, while other hosts can use the same five lenses through the provider-neutral instructions.

## One orchestrator. Five lenses. One decision-ready output.

<div align="center">
  <img src="assets/readme/architecture.svg" alt="The Sharks architecture: a founder pitch flows to the orchestrator, fans out to five specialist agents, then returns as a verdict, Deal Meter and ranked Fix List" width="100%" />
</div>

### The operating loop

1. **Pitch** — define the problem, buyer, offer, pricing, costs, traction, customer access and ask.
2. **Interrogate** — each specialist asks one sharp question from its own domain. The panel waits for the founder's answers.
3. **Evaluate** — each agent returns an evidence-linked `IN` or `OUT`, a conviction score and a condition that would change its mind.
4. **Synthesize** — the orchestrator builds the Deal Meter, identifies the strongest point, weakest point and single `KILL SHOT`.
5. **Act** — every objection becomes a ranked fix with a low-cost experiment, metric and pass/fail threshold.
6. **Re-pitch** — return with results. A Shark changes its verdict only when evidence addresses the original objection.

## What a round gives you

| Output | What it tells you |
|---|---|
| **Deal Meter** | How many specialists are `IN` — from 0/5 to 5/5. A structured opinion, not a probability of success. |
| **Conviction scores** | A 0–10 view from each specialist, with a reason. |
| **Strongest / weakest** | The best-supported part of the pitch and the most exposed assumption. |
| **KILL SHOT** | The single risk most likely to sink the venture if left untested. |
| **Ranked Fix List** | What to change, what to test, the proof threshold and what to do next. |
| **Re-pitch comparison** | Which verdicts changed—and the evidence that earned the change. |

## A sample round: TiffinBoss

<sub><strong>Fictional demonstration.</strong> The following is an illustrative example from the project materials, not a real company assessment, market study or investment recommendation.</sub>

**The pitch:** A UPI-first tiffin subscription for PG students in Pune. Proposed price: **₹3,000/month**. Founder-estimated cooking and delivery cost: **₹2,400/month**. First acquisition idea: college WhatsApp groups.

| Agent | Pressure point | Illustrative verdict |
|---|---|---|
| **MINT** | No paid pre-orders yet. Will a student—or parent—actually pay ₹3,000? | **OUT** · prove willingness to pay |
| **MAGNET** | WhatsApp groups are a starting channel, not yet a measured acquisition funnel. | **IN*** · validate conversion and reach |
| **LEDGER** | ₹600 headline spread narrows after fees, refunds and operating costs; the example answer leaves roughly ₹300/student. | **OUT** · rebuild the contribution model |
| **RAZOR** | Mess providers, food delivery and existing home-tiffin habits are real alternatives. | **OUT** · prove a reason to switch |
| **FORGE** | The founder must demonstrate the ability to fulfil and learn from the first orders. | **IN*** · execute and document the first 20 orders |

<div align="center">
  <h3>DEAL METER &nbsp; 2 / 5</h3>
  <p><strong>Strongest:</strong> a concrete starting channel exists.</p>
  <p><strong>Weakest:</strong> willingness to pay and true contribution margin remain unproven.</p>
  <p><strong>KILL SHOT:</strong> no reliable proof yet that enough students will pay the proposed price.</p>
</div>

**The first fixes:** run a paid trial offer through a small number of college groups; log the true cost of real orders; set a margin threshold before scaling. The `IN*` outcomes are conditional example verdicts—not real funding offers.

## Built to travel across AI platforms

The core is written in the open **Agent Skills** convention (`SKILL.md`) and keeps model instructions separate from host-specific adapters. Use the native integration where the host supports it; use the standalone specialist prompts where it does not.

| Platform / runtime | Skill path or method | Specialist-agent execution |
|---|---|---|
| **OpenAI Codex** | Portable skills in `.agents/skills/` | Use the runtime's delegation features and map `agents/*.md` into specialist instructions where needed. |
| **ChatGPT** | Skill import on eligible product surfaces and workspaces | Depends on the ChatGPT surface; the five roles can also be run as instruction-led reviews. |
| **Claude Code** | Native mirrors in `.claude/skills/` | Five native definitions in `.claude/agents/`. |
| **Claude.ai** | Import a skill bundle where custom Skills are available | Use the agent prompts in separate chats/projects; native delegation depends on the product surface. |
| **Gemini CLI** | `.agents/skills/` is a supported workspace discovery alias | Use configured orchestration or run specialist prompts as separate reviews. |
| **Cursor** | Agent Skills supported; use the documented `.cursor/skills/` discovery path if required by your setup | Cursor supports custom subagents; map the included role prompts to its agent definitions when needed. |
| **Other instruction-following models** | Use a relevant `agents/*.md` prompt as the model's instruction/context | Parallel execution is only available when the host itself provides subagents or orchestration. |

**Important:** model-agnostic does not mean every host has the same import flow, tool access or subagent runtime. The instructions are portable; native discovery and independent execution depend on the platform. No model API key or provider SDK is hard-coded into the core skills.

Official platform references: [OpenAI Skills](https://learn.chatgpt.com/docs/build-skills) · [OpenAI multi-agent](https://developers.openai.com/api/docs/guides/responses-multi-agent) · [Claude Code](https://docs.anthropic.com/en/docs/claude-code/getting-started) · [Gemini CLI Agent Skills](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/skills.md) · [Cursor Agent Skills](https://cursor.com/docs/skills) · [Cursor Subagents](https://cursor.com/docs/subagents).

## Evidence rules, not empty confidence

- **Facts stay facts.** Separate `FACT`, `FOUNDER ESTIMATE`, `ASSUMPTION` and `UNKNOWN`.
- **No invented market data.** Research claims are cited when browsing is available; otherwise they are marked unverified.
- **Math stays inspectable.** LEDGER shows formulas and assumptions rather than manufacturing precision.
- **Tests beat applause.** Paid pilots, conversion, repeat usage and measured costs outweigh likes and compliments.
- **Challenge the venture, respect the founder.** No personal insults, fabricated certainty or claims of guaranteed success.
- **Market-aware by default.** Currency, geography, customer behaviour and channels are inferred from the pitch or clarified—not hard-coded to one country.

## Inside the repository

```text
the-sharks/
├── .agents/skills/       # Portable master skill + five specialist skills
├── .claude/agents/       # Five native Claude Code subagents
├── .claude/skills/       # Claude Code skill entry points
├── .cursor/rules/        # Cursor workspace adapter
├── agents/               # Five provider-neutral specialist prompts
├── assets/               # Project identity, architecture and agent visuals
├── docs/                 # Architecture, playbook, compatibility and FAQ
├── examples/             # Fictional pitch and worked evaluation
├── prompts/              # Provider-neutral orchestration prompt
├── templates/            # Pitch brief and scorecard
├── scripts/              # Repository validation
├── tests/                # Quality checks
├── AGENTS.md             # Shared workspace instructions
├── GEMINI.md             # Gemini CLI entry point
└── install.sh            # Host-aware installer
```

## Make the panel sharper

New evaluation cases, language improvements, provider adapters and better evidence standards are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md). Do not submit private founder data, customer personal information, API keys or confidential pitch decks.

The project is released under the [MIT License](LICENSE).

<div align="center">
  <h2>Build with conviction. Validate with evidence.</h2>
  <p>If The Sharks helps you find the flaw before the market does, give the project a ⭐ and share it with a founder who values the truth over applause.</p>
</div>