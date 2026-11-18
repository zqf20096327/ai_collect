<p align="center">
  <img src="assets/hero.svg" alt="Awesome AI Coding Agents — a curated, regularly verified guide to AI coding agents: CLI tools, IDE assistants, and autonomous developer agents" width="100%">
</p>

# Awesome AI Coding Agents [![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)

> A curated and regularly verified guide to AI coding agents, CLI coding tools,
> autonomous coding assistants, and open-source developer agents.

Dozens of tools now claim to write code for you. This list helps you tell them
apart: it pairs **source-verified facts** (license, stars and last-commit pulled
straight from the GitHub API) with **clearly-labelled editorial fields**
(category, interface, local-model support, provider flexibility, pricing), so
you can compare on the things that actually decide a choice.

<!-- AUTO:stats -->
**42 agents** &nbsp;·&nbsp; 30 open-source, 12 proprietary &nbsp;·&nbsp; 10 CLI, 18 IDE, 14 autonomous &nbsp;·&nbsp; 23 run local models
<!-- /AUTO:stats -->

Every row has a verified date. The data lives in [`data/agents.json`](data/agents.json)
and you can slice it yourself with [`scripts/agents.py`](scripts/agents.py).

## Contents

- [What counts as an AI coding agent](#what-counts-as-an-ai-coding-agent)
- [The landscape at a glance](#the-landscape-at-a-glance)
- [The directory](#the-directory)
  - [Best CLI AI coding agents](#best-cli-ai-coding-agents)
  - [AI coding agents for VS Code and other IDEs](#ai-coding-agents-for-vs-code-and-other-ides)
  - [Autonomous coding agents](#autonomous-coding-agents)
- [Comparison views](#comparison-views)
  - [Open-source coding agents](#open-source-coding-agents)
  - [Local-model coding agents](#local-model-coding-agents)
  - [Multi-provider agents](#multi-provider-agents)
  - [Agents that run your tests](#agents-that-run-your-tests)
- [Which one should I use?](#which-one-should-i-use)
- [Query the data yourself](#query-the-data-yourself)
- [Methodology](#methodology)
- [Contributing](#contributing)
- [Maintenance](#maintenance)
- [About Tartarus](#about-tartarus)
- [License](#license)

## What counts as an AI coding agent

To be listed, a tool must:

1. **Write or change code** with an LLM — not just autocomplete snippets. Pure
   completion tools (and dev utilities) are out of scope unless they also drive
   multi-step edits.
2. **Exist and be reachable today** — a working homepage, and for open-source
   tools a real GitHub repository that resolves.
3. Be classifiable into one of: **CLI agent**, **IDE agent**, or **autonomous**
   agent.

Open-source and proprietary tools are both welcome. Inclusion is not an
endorsement, and ordering inside a table is by GitHub stars (a popularity proxy),
not by quality.

## The landscape at a glance

<p align="center">
  <img src="assets/comparison.svg" alt="Bar chart of agent counts by category (CLI, IDE, autonomous) plus an openness and capabilities summary" width="100%">
</p>

> Stars and licenses are from the GitHub API on each row's **verified** date.
> Feature flags are editorial: `yes` / `no` / `partial` / `?` (unknown).

## The directory

### Best CLI AI coding agents

Terminal-native agents that edit your repo and run commands.

<!-- AUTO:dir-cli -->
| Name | Category | Interface | OSS | License | Stars | Local | Multi-provider | Pricing |
|---|---|---|---|---|---|---|---|---|
| [OpenCode](https://github.com/anomalyco/opencode) | cli | cli | yes | MIT | 227,447 | yes | yes | free |
| [Claude Code](https://github.com/anthropics/claude-code) | cli | cli | no | see repo | 155,973 | no | no | paid |
| [OpenAI Codex CLI](https://github.com/openai/codex) | cli | cli | yes | Apache-2.0 | 135,612 | ? | partial | free |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | cli | cli | yes | Apache-2.0 | 108,893 | no | no | freemium |
| [Goose](https://github.com/aaif-goose/goose) | cli | cli | yes | Apache-2.0 | 56,706 | yes | yes | free |
| [Aider](https://github.com/Aider-AI/aider) | cli | cli | yes | Apache-2.0 | 50,153 | yes | yes | free |
| [Qwen Code](https://github.com/QwenLM/qwen-code) | cli | cli | yes | Apache-2.0 | 30,707 | yes | partial | free |
| [Crush](https://github.com/charmbracelet/crush) | cli | cli | yes | see repo | 29,106 | yes | yes | free |
| [Plandex](https://github.com/plandex-ai/plandex) | cli | cli | yes | MIT | 15,923 | yes | yes | freemium |
| [Tartarus](https://github.com/TartarusAIDev/tartarus-console) | cli | cli/api | no | proprietary | — | no | no | paid |
<!-- /AUTO:dir-cli -->

### AI coding agents for VS Code and other IDEs

Agents that live inside an editor (VS Code, JetBrains, or their own fork).

<!-- AUTO:dir-ide -->
| Name | Category | Interface | OSS | License | Stars | Local | Multi-provider | Pricing |
|---|---|---|---|---|---|---|---|---|
| [Zed](https://github.com/zed-industries/zed) | ide | ide | yes | see repo | 95,198 | yes | yes | freemium |
| [Cline](https://github.com/cline/cline) | ide | ide | yes | Apache-2.0 | 71,705 | yes | yes | free |
| [Continue](https://github.com/continuedev/continue) | ide | ide | yes | Apache-2.0 | 36,503 | yes | yes | freemium |
| [Tabby](https://github.com/TabbyML/tabby) | ide | ide | yes | see repo | 33,933 | yes | ? | free |
| [Void](https://github.com/voideditor/void) | ide | ide | yes | Apache-2.0 | 28,707 | yes | yes | free |
| [Kilo Code](https://github.com/Kilo-Org/kilocode) | ide | ide | yes | MIT | 28,031 | yes | yes | free |
| [Roo Code](https://github.com/RooCodeInc/Roo-Code) | ide | ide | yes | Apache-2.0 | 24,238 | yes | yes | free |
| [Twinny](https://github.com/twinnydotdev/twinny) | ide | ide | yes | MIT | 3,701 | yes | yes | free |
| [Refact.ai](https://github.com/smallcloudai/refact) | ide | ide | yes | BSD-3-Clause | 3,528 | yes | yes | freemium |
| [Aide](https://github.com/codestoryai/aide) | ide | ide | yes | AGPL-3.0 | 2,187 | ? | partial | freemium |
| [Amazon Q Developer](https://aws.amazon.com/q/developer/) | ide | ide/cli | no | proprietary | — | no | no | freemium |
| [Augment Code](https://www.augmentcode.com) | ide | ide | no | proprietary | — | no | partial | freemium |
| [Cursor](https://cursor.com) | ide | ide | no | proprietary | — | no | partial | freemium |
| [GitHub Copilot](https://github.com/features/copilot) | ide | ide | no | proprietary | — | no | partial | freemium |
| [JetBrains AI (Junie)](https://www.jetbrains.com/ai-assistant/) | ide | ide | no | proprietary | — | partial | partial | freemium |
| [Sourcegraph Cody](https://sourcegraph.com/cody) | ide | ide | no | proprietary | — | no | partial | freemium |
| [Tabnine](https://www.tabnine.com) | ide | ide | no | proprietary | — | partial | partial | freemium |
| [Windsurf](https://windsurf.com) | ide | ide | no | proprietary | — | no | partial | freemium |
<!-- /AUTO:dir-ide -->

### Autonomous coding agents

Agents that take a goal and work multiple steps with less hand-holding
(frameworks and issue-to-PR tools included).

<!-- AUTO:dir-auto -->
| Name | Category | Interface | OSS | License | Stars | Local | Multi-provider | Pricing |
|---|---|---|---|---|---|---|---|---|
| [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | autonomous | browser | yes | see repo | 188,071 | ? | partial | freemium |
| [OpenHands](https://github.com/OpenHands/OpenHands) | autonomous | cli/browser | yes | MIT | 93,630 | yes | yes | freemium |
| [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | autonomous | cli | yes | MIT | 71,322 | yes | yes | free |
| [Open Interpreter](https://github.com/openinterpreter/openinterpreter) | autonomous | cli | yes | Apache-2.0 | 68,895 | yes | yes | free |
| [GPT Engineer](https://github.com/AntonOsika/gpt-engineer) | autonomous | cli | yes | MIT | 54,951 | ? | partial | free |
| [ChatDev](https://github.com/OpenBMB/ChatDev) | autonomous | cli | yes | Apache-2.0 | 34,764 | ? | partial | free |
| [GPT Pilot / Pythagora](https://github.com/Pythagora-io/gpt-pilot) | autonomous | ide | yes | see repo | 33,643 | ? | partial | freemium |
| [SWE-agent](https://github.com/SWE-agent/SWE-agent) | autonomous | cli | yes | MIT | 20,821 | yes | yes | free |
| [bolt.diy](https://github.com/stackblitz-labs/bolt.diy) | autonomous | browser | yes | MIT | 20,098 | yes | yes | free |
| [Devika](https://github.com/stitionai/devika) | autonomous | browser | yes | MIT | 19,546 | yes | yes | free |
| [Sweep](https://github.com/sweepai/sweep) | autonomous | api | yes | see repo | 7,710 | ? | ? | unknown |
| [Devon](https://github.com/entropy-research/Devon) | autonomous | cli | yes | AGPL-3.0 | 3,451 | ? | yes | free |
| [Devin](https://devin.ai) | autonomous | browser | no | proprietary | — | no | no | paid |
| [Replit Agent](https://replit.com/ai) | autonomous | browser | no | proprietary | — | no | no | freemium |
<!-- /AUTO:dir-auto -->

## Comparison views

Cross-cutting slices of the same data. Want a different cut? See
[Query the data yourself](#query-the-data-yourself).

### Open-source coding agents

Top open-source agents by stars. License is the SPDX id from the GitHub API
(`see repo` when GitHub can't detect a standard license).

<!-- AUTO:cmp-opensource -->
| Name | Category | Interface | OSS | License | Stars | Local | Multi-provider | Pricing |
|---|---|---|---|---|---|---|---|---|
| [OpenCode](https://github.com/anomalyco/opencode) | cli | cli | yes | MIT | 227,447 | yes | yes | free |
| [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | autonomous | browser | yes | see repo | 188,071 | ? | partial | freemium |
| [OpenAI Codex CLI](https://github.com/openai/codex) | cli | cli | yes | Apache-2.0 | 135,612 | ? | partial | free |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | cli | cli | yes | Apache-2.0 | 108,893 | no | no | freemium |
| [Zed](https://github.com/zed-industries/zed) | ide | ide | yes | see repo | 95,198 | yes | yes | freemium |
| [OpenHands](https://github.com/OpenHands/OpenHands) | autonomous | cli/browser | yes | MIT | 93,630 | yes | yes | freemium |
| [Cline](https://github.com/cline/cline) | ide | ide | yes | Apache-2.0 | 71,705 | yes | yes | free |
| [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | autonomous | cli | yes | MIT | 71,322 | yes | yes | free |
| [Open Interpreter](https://github.com/openinterpreter/openinterpreter) | autonomous | cli | yes | Apache-2.0 | 68,895 | yes | yes | free |
| [Goose](https://github.com/aaif-goose/goose) | cli | cli | yes | Apache-2.0 | 56,706 | yes | yes | free |
| [GPT Engineer](https://github.com/AntonOsika/gpt-engineer) | autonomous | cli | yes | MIT | 54,951 | ? | partial | free |
| [Aider](https://github.com/Aider-AI/aider) | cli | cli | yes | Apache-2.0 | 50,153 | yes | yes | free |
<!-- /AUTO:cmp-opensource -->

### Local-model coding agents

Agents that can run against local or self-hosted models (`yes` or `partial`).

<!-- AUTO:cmp-local -->
| Name | Category | Interface | OSS | License | Stars | Local | Multi-provider | Pricing |
|---|---|---|---|---|---|---|---|---|
| [OpenCode](https://github.com/anomalyco/opencode) | cli | cli | yes | MIT | 227,447 | yes | yes | free |
| [Zed](https://github.com/zed-industries/zed) | ide | ide | yes | see repo | 95,198 | yes | yes | freemium |
| [OpenHands](https://github.com/OpenHands/OpenHands) | autonomous | cli/browser | yes | MIT | 93,630 | yes | yes | freemium |
| [Cline](https://github.com/cline/cline) | ide | ide | yes | Apache-2.0 | 71,705 | yes | yes | free |
| [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | autonomous | cli | yes | MIT | 71,322 | yes | yes | free |
| [Open Interpreter](https://github.com/openinterpreter/openinterpreter) | autonomous | cli | yes | Apache-2.0 | 68,895 | yes | yes | free |
| [Goose](https://github.com/aaif-goose/goose) | cli | cli | yes | Apache-2.0 | 56,706 | yes | yes | free |
| [Aider](https://github.com/Aider-AI/aider) | cli | cli | yes | Apache-2.0 | 50,153 | yes | yes | free |
| [Continue](https://github.com/continuedev/continue) | ide | ide | yes | Apache-2.0 | 36,503 | yes | yes | freemium |
| [Tabby](https://github.com/TabbyML/tabby) | ide | ide | yes | see repo | 33,933 | yes | ? | free |
| [Qwen Code](https://github.com/QwenLM/qwen-code) | cli | cli | yes | Apache-2.0 | 30,707 | yes | partial | free |
| [Crush](https://github.com/charmbracelet/crush) | cli | cli | yes | see repo | 29,106 | yes | yes | free |
<!-- /AUTO:cmp-local -->

### Multi-provider agents

Agents that work with more than one model provider.

<!-- AUTO:cmp-multi -->
| Name | Category | Interface | OSS | License | Stars | Local | Multi-provider | Pricing |
|---|---|---|---|---|---|---|---|---|
| [OpenCode](https://github.com/anomalyco/opencode) | cli | cli | yes | MIT | 227,447 | yes | yes | free |
| [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | autonomous | browser | yes | see repo | 188,071 | ? | partial | freemium |
| [OpenAI Codex CLI](https://github.com/openai/codex) | cli | cli | yes | Apache-2.0 | 135,612 | ? | partial | free |
| [Zed](https://github.com/zed-industries/zed) | ide | ide | yes | see repo | 95,198 | yes | yes | freemium |
| [OpenHands](https://github.com/OpenHands/OpenHands) | autonomous | cli/browser | yes | MIT | 93,630 | yes | yes | freemium |
| [Cline](https://github.com/cline/cline) | ide | ide | yes | Apache-2.0 | 71,705 | yes | yes | free |
| [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | autonomous | cli | yes | MIT | 71,322 | yes | yes | free |
| [Open Interpreter](https://github.com/openinterpreter/openinterpreter) | autonomous | cli | yes | Apache-2.0 | 68,895 | yes | yes | free |
| [Goose](https://github.com/aaif-goose/goose) | cli | cli | yes | Apache-2.0 | 56,706 | yes | yes | free |
| [GPT Engineer](https://github.com/AntonOsika/gpt-engineer) | autonomous | cli | yes | MIT | 54,951 | ? | partial | free |
| [Aider](https://github.com/Aider-AI/aider) | cli | cli | yes | Apache-2.0 | 50,153 | yes | yes | free |
| [Continue](https://github.com/continuedev/continue) | ide | ide | yes | Apache-2.0 | 36,503 | yes | yes | freemium |
<!-- /AUTO:cmp-multi -->

### Agents that run your tests

Agents whose tool execution lets them run commands and test suites, not just
suggest edits — the basis for automated-testing workflows.

<!-- AUTO:cmp-testing -->
| Name | Category | Interface | OSS | License | Stars | Local | Multi-provider | Pricing |
|---|---|---|---|---|---|---|---|---|
| [OpenCode](https://github.com/anomalyco/opencode) | cli | cli | yes | MIT | 227,447 | yes | yes | free |
| [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | autonomous | browser | yes | see repo | 188,071 | ? | partial | freemium |
| [Claude Code](https://github.com/anthropics/claude-code) | cli | cli | no | see repo | 155,973 | no | no | paid |
| [OpenAI Codex CLI](https://github.com/openai/codex) | cli | cli | yes | Apache-2.0 | 135,612 | ? | partial | free |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | cli | cli | yes | Apache-2.0 | 108,893 | no | no | freemium |
| [Zed](https://github.com/zed-industries/zed) | ide | ide | yes | see repo | 95,198 | yes | yes | freemium |
| [OpenHands](https://github.com/OpenHands/OpenHands) | autonomous | cli/browser | yes | MIT | 93,630 | yes | yes | freemium |
| [Cline](https://github.com/cline/cline) | ide | ide | yes | Apache-2.0 | 71,705 | yes | yes | free |
| [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | autonomous | cli | yes | MIT | 71,322 | yes | yes | free |
| [Open Interpreter](https://github.com/openinterpreter/openinterpreter) | autonomous | cli | yes | Apache-2.0 | 68,895 | yes | yes | free |
<!-- /AUTO:cmp-testing -->

## Which one should I use?

A quick decision guide. It points at documented capabilities, not at any one
product.

- **You live in a terminal and want the agent there** → a CLI agent: Aider,
  OpenCode, Goose, Codex CLI, Gemini CLI. Want it uncensored and hosted?
  Tartarus.
- **You want it inside your editor** → Cline, Roo Code, Continue, Kilo Code
  (VS Code, open-source); Cursor or Windsurf (their own editor, proprietary);
  Copilot or JetBrains AI (inside an IDE you already use).
- **You must run models locally / offline** → filter for
  [local-model agents](#local-model-coding-agents): Aider, Cline, Continue,
  Tabby (self-hosted), Void, Twinny.
- **You want to switch model providers freely** → see
  [multi-provider agents](#multi-provider-agents).
- **You want it fully open-source** → see
  [open-source coding agents](#open-source-coding-agents) and check the license
  column (Apache-2.0 and MIT are the most permissive here; AGPL is copyleft).
- **You want it to resolve whole issues / PRs on its own** → OpenHands,
  SWE-agent, Sweep, or a hosted autonomous agent like Devin.

See [docs/choosing-an-agent.md](docs/choosing-an-agent.md) for the long version.

## Query the data yourself

Everything above is generated from [`data/agents.json`](data/agents.json). The
CLI is pure standard library — no install:

```bash
# open-source CLI agents, most-starred first
python scripts/agents.py --category cli-agent --open-source --sort stars

# agents that run local models and support multiple providers, as markdown
python scripts/agents.py --local --provider --format md

# everything Apache-2.0, just the names
python scripts/agents.py --license Apache-2.0 --format names

# raw JSON for your own tooling
python scripts/agents.py --interface ide --format json
```

## Methodology

- **Source-verified** (`license`, `stars`, `last_commit`, repo existence) comes
  from the GitHub API on the row's `verified` date. Proprietary tools are
  verified by a live homepage check.
- **Editorial** (`category`, `interface`, `local_models`,
  `provider_flexibility`, `tool_execution`, `platforms`, `pricing`) is
  best-effort classification. It can lag; corrections are welcome.
- A model's *refusal* behaviour, benchmark scores, and quality are **not** rated
  here — this list is about what a tool *is*, not how good it is.

Full write-up: [docs/methodology.md](docs/methodology.md).

## Contributing

Add or fix an agent via [`data/agents.json`](data/agents.json), then run the
validator and regenerate the tables:

```bash
python scripts/build_dataset.py   # re-pulls verified fields (needs gh or a token)
python scripts/validate.py        # schema + integrity
python scripts/gen_tables.py      # refresh README tables
python -m unittest discover tests
```

See [CONTRIBUTING.md](CONTRIBUTING.md) and the issue templates
(suggest an agent, report outdated info, correct a comparison, report a broken
link). One change per PR; cite a source for any factual claim.

## Maintenance

- A scheduled workflow re-checks links and flags stale data; it opens a
  reviewable PR rather than editing descriptions automatically.
- Star counts and licenses are refreshed by re-running `build_dataset.py`.
- Dead links are fixed or the entry is removed.

## About Tartarus

This list is maintained by [**Tartarus AI**](https://tartarusai.dev/?utm_source=github&utm_medium=readme&utm_campaign=awesome-ai-coding-agents&utm_content=about),
which makes an uncensored AI coding agent. Tartarus is listed in the directory on
the same terms as every other tool — alphabetically within its table, with the
same fields — and it is not ranked above competitors. If you think its entry is
unfair, [open an issue](https://github.com/TartarusAIDev/awesome-ai-coding-agents/issues).

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](LICENSE)

To the extent possible under law, the contributors have waived all copyright and
related rights to this work ([CC0 1.0](LICENSE)). The data is free to reuse;
attribution is appreciated but not required.
