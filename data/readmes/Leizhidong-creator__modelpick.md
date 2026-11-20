<p align="center">
  <img src="assets/social-preview.png" alt="ModelPick — pick the right model at every step" width="100%" />
</p>

<h1 align="center">ModelPick</h1>

<p align="center"><strong>The model router for AI agents — with cost per solved task.</strong><br/>
Coding, image, video, 3D, and audio. One CLI, one MCP server, every agent.</p>

<p align="center">
  <a href="https://github.com/Leizhidong-creator/modelpick/releases"><img alt="release" src="https://img.shields.io/github/v/release/Leizhidong-creator/modelpick?color=39c5cf" /></a>
  <a href="LICENSE"><img alt="license" src="https://img.shields.io/badge/license-MIT-39c5cf" /></a>
  <a href="package.json"><img alt="node" src="https://img.shields.io/badge/node-%3E%3D20.11-339933" /></a>
  <a href="https://modelcontextprotocol.io"><img alt="MCP" src="https://img.shields.io/badge/MCP-stdio-8a5cf6" /></a>
  <img alt="tests" src="https://img.shields.io/badge/tests-217%20passing-3fb950" />
  <img alt="adversarial" src="https://img.shields.io/badge/adversarial-28%2F28-3fb950" />
  <img alt="dependencies" src="https://img.shields.io/badge/runtime%20deps-0-3fb950" />
</p>

<p align="center"><a href="https://leizhidong-creator.github.io/modelpick/">Website</a> · <a href="https://leizhidong-creator.github.io/modelpick/#video">intro video (93s)</a> · <a href="docs/VALUE.md">How value is defined</a> · <a href="docs/ECOSYSTEM.md">Ecosystem</a></p>

---

Your agent can write code, call tools, and ship a feature. Then it picks **one model for everything** — a frontier model to classify a support ticket, to generate a barrel prop, to draft a thumbnail.

The result is predictable: 60–95% of the spend goes to work that did not need a frontier model, and the hard nodes still fail because the model was chosen for the wrong modality.

**ModelPick is a router and cost calculator, not another gateway.** Before each node, it answers three questions in one call:

1. **Which model?** Ranked for this exact task, with hard capability filters (context, text-in-image, rigging, clip length, open weights).
2. **What will it really cost?** **Cost per solved task** — list price × expected attempts, not $/M tokens.
3. **How do I connect it?** The env var, key URL, docs, and API model id.

```bash
npx -y github:Leizhidong-creator/modelpick pick "create a stylized 3D sword for a Unity game"
```

<p align="center">
  <img src="assets/terminal-pick.png" alt="ModelPick CLI recommending Tripo H3.1 for a 3D game asset" width="92%" />
</p>

<p align="center">
  <a href="https://leizhidong-creator.github.io/modelpick/#video"><img src="assets/modelpick-intro-thumb.png" alt="Watch the ModelPick intro video" width="72%" /></a>
</p>

<p align="center"><a href="https://leizhidong-creator.github.io/modelpick/#video"><strong>▶ Watch the intro video with English + 中文 captions</strong></a> · <a href="https://github.com/Leizhidong-creator/modelpick/releases/download/v0.2.0/modelpick-intro.mp4">direct MP4</a> · <a href="launch/video-storyboard.md">script &amp; storyboard</a> · <a href="assets/modelpick-intro.bilingual.srt">English + 中文 captions</a></p>

---

## Why this exists

Three things are broken in model selection today:

**1. Token prices hide the real bill.** A model that is 10× cheaper per token but needs 1.8× the attempts and 2× the output tokens is not 10× cheaper. ModelPick computes the denominator that matters: dollars per usable output.

**2. A coding agent defaults to one model, even for creative nodes.** A 3D pipeline is not a text problem. Text-in-image is not image generation. A 30-second video is not a 5-second clip. ModelPick models 20 task nodes across 5 modalities, with capability filters that reject the wrong model before scoring.

**3. Every tool is a new integration.** ModelPick ships as a zero-dependency CLI, a stdio MCP server, a portable `SKILL.md`, and a Claude Code plugin. Same decision engine everywhere; no gateway, no lock-in, no key storage.

> **In one line:** other tools route text prompts. ModelPick routes work — coding, image, video, 3D, and audio — and prices each node per solved task.

### How is this different from a gateway or a coding router?

| | Gateway (OpenRouter, LiteLLM, Portkey) | Coding router (claude-code-router) | **ModelPick** |
|---|---|---|---|
| Optimizes | access, failover, provider margin | model switching inside a coding loop | **best price-performance at each node** |
| Modalities | mostly text; OpenRouter's live catalog is ~4% non-text | text | **text, image, video, 3D, audio** |
| Decision | route by price/availability | rules or a classifier | capability filters + benchmark-weighted utility |
| Keys | held by the gateway | local | **local file/env only; you call the provider** |
| Evidence | live prices | config | dated catalog + public benchmark + raw failures |

Gateways are useful, and ModelPick can recommend one as the setup path. But a gateway cannot tell you that a 3D node should use Tripo instead of Meshy, or that a "headline text" image needs a model with a text-rendering score above 90. That choice is what this tool makes.

More: [`research/competitive-landscape.md`](research/competitive-landscape.md) (15 products, 10 features, 53 sources).

---

## 30-second quickstart

### Windows: one command, no prompts

```bat
npm install -g modelpick
modelpick keys --ui
```

If global install is blocked by policy:

```bat
npx --yes --package=modelpick@latest modelpick keys --ui
```

Or double-click the launcher:

https://leizhidong-creator.github.io/modelpick/start-modelpick.cmd

Do **not** paste bash comments (`# ...`) into CMD; CMD does not understand `#`.

### macOS / Linux

```bash
npm install -g modelpick
modelpick keys --ui

# or no install
npx --yes --package=modelpick@latest modelpick keys --ui
```

### Then

```bash
modelpick keys list
modelpick doctor
modelpick run "hello" --local --model qwen-local:latest
```

### Why `npm install modelpick` alone is not enough

`npm install modelpick` installs into `./node_modules`; it does **not** put `modelpick` on PATH.

```bash
npm install modelpick
npx modelpick keys --ui       # ✅
# modelpick keys --ui         # ❌ not on PATH
```

Install globally for a permanent command:

```bash
npm install -g modelpick
modelpick keys --ui
```

Official npm package: https://www.npmjs.com/package/modelpick

MCP Registry: https://registry.modelcontextprotocol.io/v0/servers?search=modelpick

Fallbacks if the registry is unavailable:

```bash
# GitHub, no npm auth
npx --yes github:Leizhidong-creator/modelpick pick "refactor this 40k-line repo, cheapest that works"

# static registry mirror
npm install modelpick --registry=https://leizhidong-creator.github.io/modelpick/npm/

# offline release tarball
npm install https://github.com/Leizhidong-creator/modelpick/releases/download/v0.2.0/modelpick-0.2.0.tgz
```

<p align="center">
  <img src="assets/terminal-plan.png" alt="ModelPick planning a product launch video with a model per step" width="92%" />
</p>

---

## Works with the agents you already use

`modelpick setup` writes the files for the agent you use. It backs up existing config, keeps sibling MCP servers, and refuses to overwrite invalid JSON.

| Agent | Command | MCP file it uses |
|---|---|---|
| **Claude Code** | `setup claude-code` | `.mcp.json` (project) or `~/.claude.json` (`--global`) |
| **OpenAI Codex CLI** | `setup codex` + `codex mcp add` | `~/.codex/config.toml` |
| **Cursor** | `setup cursor` | `.cursor/mcp.json` |
| **DeepSeek Harness** | `setup dsh --global --write --profile desktop` | `~/.dsh/profiles/<profile>/cordis.patch.yml` |
| **GitHub Copilot CLI** | `setup copilot` | `.mcp.json` |
| **VS Code / Copilot agent mode** | `setup vscode` | `.vscode/mcp.json` (`servers`) |
| **Any MCP client** | `modelpick mcp` | your client's stdio config |

### Claude Code

```bash
npx -y github:Leizhidong-creator/modelpick setup claude-code
# writes .mcp.json, .claude/skills/modelpick/, and a CLAUDE.md block
claude mcp list        # modelpick should appear
```

Restart Claude Code, run `/mcp`, and approve the project server. Then ask: `pick a model for a 3D sword for Unity`.

Plugin alternative, inside Claude Code:

```text
/plugin marketplace add Leizhidong-creator/modelpick
/plugin install modelpick@modelpick
```

### OpenAI Codex CLI

```bash
npx -y github:Leizhidong-creator/modelpick setup codex
# or write the global MCP row directly, with a backup:
npx -y github:Leizhidong-creator/modelpick setup codex --global --write
codex mcp list
```

`setup codex` writes `AGENTS.md` and `.agents/skills/modelpick/`. Codex reads MCP servers from `~/.codex/config.toml`, so `--global --write` appends the row or you can use `codex mcp add`:

```bash
codex mcp add modelpick -- npx -y github:Leizhidong-creator/modelpick mcp
```

### Cursor

```bash
npx -y github:Leizhidong-creator/modelpick setup cursor
```

It writes `.cursor/mcp.json`, `.cursor/rules/modelpick.mdc`, `.cursor/skills/modelpick/`, and `AGENTS.md`. Open **Cursor → Settings → MCP** and confirm `modelpick` is connected.

### DeepSeek Harness

DSH has no `.mcp.json`. MCP servers are Cordis rows in the profile patch:

```bash
npx -y modelpick setup dsh --global --write --profile desktop
```

It writes the portable skill to `~/.dsh/skills/modelpick/`, appends `AGENTS.md`, and adds one MCP row to `~/.dsh/profiles/desktop/cordis.patch.yml` (backing the file up first).

**Restart DSH** after this. Then ask it:

```text
Use modelpick pick_model for a low-poly sword for Unity. Show costPerTask and the key.
```

Without `--write`, `setup dsh` prints the row instead of editing a live profile. The MCP server itself can be tested without DSH:

```bash
node bin/modelpick.js mcp
# then send initialize + tools/list over stdio
```

### GitHub Copilot CLI

```bash
npx -y github:Leizhidong-creator/modelpick setup copilot
copilot mcp list
```

It writes `.mcp.json`, `.github/skills/modelpick/`, and `AGENTS.md`. Restart Copilot and ask for a model pick.

### VS Code / Copilot agent mode

```bash
npx -y github:Leizhidong-creator/modelpick setup vscode
```

It writes `.vscode/mcp.json` under `servers` (VS Code's schema, not `mcpServers`), the portable skill, and `AGENTS.md`. In VS Code run **MCP: List Servers**, start `modelpick`, then ask in agent mode. Sibling servers are preserved.

### Any MCP client

```json
{
  "mcpServers": {
    "modelpick": {
      "command": "npx",
      "args": ["-y", "github:Leizhidong-creator/modelpick", "mcp"]
    }
  }
}
```

Tools exposed: `pick_model`, `run_model`, `get_decision_packet`, `plan_workflow`, `compare_models`, `get_setup`, `list_models`, `explain_task`. Recommendations work without any provider key; the key is only needed to run the chosen model.

**Portable skill:** `.agents/skills/modelpick/SKILL.md` is read by Codex, Cursor, Copilot CLI, Devin/Windsurf, and DeepSeek Harness. Claude Code gets its own copy. The skill tells the agent when to call `pick_model` and how to report the result.

---

## The number that matters: cost per solved task

```
raw cost per attempt = tokens × price (cache-aware)   OR   units × unit price
expected attempts    = 1 / (1 − 1.15 × (100 − quality) / 100)     capped at 4
cost per solved task = raw cost × expected attempts
```

**Worked example — 80K input / 8K output, 60% cache hit, agentic coding:**

| Model | quality | raw cost | expected attempts | **cost per solved task** |
|---|---:|---:|---:|---:|
| Claude Fable 5.2 | 92.3 | $0.59 | 1.10 | **$0.64** |
| Gemini 4 Carbon | 87.3 | $0.15 | 1.17 | **$0.17** |
| DeepSeek V4.1 Flash | 70.7 | $0.010 | 1.51 | **$0.015** |
| Claude Haiku 5.5 | 68.8 | $0.008 | 1.56 | **$0.012** |

The cheap model is **53× cheaper** and **23.5 quality points worse**. The interesting answer is the third row: **mid-quality agentic coding at 2.3% of the frontier cost**. The right answer depends on the node — which is why the tool shows both sides instead of hiding the trade-off behind a token price.

Quality is a weighted mix of public benchmark signals (BenchLM overall/coding, CursorBench 4.0, capability-specific scores). Expected attempts is a transparent model, shown on every result — not a promise. If a number is estimated, the CLI prints `~`.

---

## What it covers

**40 models · 18 providers · 20 task nodes · 5 modalities.** Current as of **2026-11-19**; every price carries a source and read date.

| Modality | Nodes | Example models in the catalog |
|---|---|---|
| **Text** | coding, review, refactor, debug, plan, long-context, research, writing, translation, extraction, classification, data, computer-use | Claude Fable 5.2, GPT-6.2 Astra/Sol, Gemini 4 Carbon/Hydrogen, DeepSeek V4.1 Flash, Claude Haiku 5.5, Kimi K3.1 Pro |
| **Image** | generation, editing, text-in-image | Nano Banana 2.1/Pro, GPT Image 2.6, Seedream 5.5 |
| **Video** | text/image → clip, dialogue, 30s takes | Veo 3.1 / Fast (Vertex), Kling 4.0, Seedance 2.5 |
| **3D** | text/image → game-ready asset, rigging | Tripo H3.1, Hunyuan3D 3.1 Pro, Meshy 7.1, TRELLIS 2 (open) |
| **Audio** | TTS, STT, music | Eleven v4, Voxtral TTS 3, GPT Transcribe, Voxtral Transcribe 3, Lyria 3.5, MiniMax Music 3 |

The catalog is a **dated snapshot**, not a live price feed. `modelpick update` refreshes from the repo; `modelpick doctor` warns when it is stale.

---

## Tested decisions

<p align="center">
  <img src="assets/benchmark.png" alt="ModelPick decision benchmark: 115 runs, 100% top-1 acceptable, 100% hard constraints" width="92%" />
</p>

| Metric | Development set | Held-out set | Target |
|---|---:|---:|---:|
| Top-1 acceptable | **100%** (115 runs) | **100%** (35 runs) | ≥75% |
| Top-3 acceptable | **100%** | **100%** | ≥92% |
| Intent accuracy | **100%** (39 scenarios) | **100%** (12 scenarios) | ≥95% |
| Hard constraint pass | **100%** | **100%** | 100% |
| Price stability (±20%) | **100%** | **100%** | ≥80% |
| p95 decision latency | **1.1 ms** | **1.1 ms** | ≤300 ms |

**What this is:** 39 expert-labeled scenarios expanded into balanced/cost/quality runs, plus a 12-scenario held-out set authored after the benchmark froze. Every run checks task detection, top-1/top-3 acceptability, hard constraints, cost regret, and stability under ±20% price perturbation.

**What this is not:** a live model-output benchmark. It does not call providers, and it does not prove quality labels are universally correct. Quality scores are derived from public leaderboards; expected attempts is a model. The full methodology, failures, and reproduction commands live in [`tests/TEST_PLAN.md`](tests/TEST_PLAN.md), [`tests/results/`](tests/results/), and [`bench/`](bench/).

<p align="center">
  <img src="assets/cost-quality.png" alt="Quality versus cost per solved task for coding models" width="92%" />
</p>

Full per-node tables: [`docs/LEADERBOARD.md`](docs/LEADERBOARD.md).

### Value, measured

`node bench/value.js` simulates 4,000 jobs per task across five task types, using catalog quality as first-pass success and the router's retry curve:

| Strategy | First-pass | Cost / solved | Quality parity | Cost vs frontier |
|---|---:|---:|---:|---:|
| Frontier always | 93.7% | $0.6417 | 100% | 100% |
| **Value pick** | **89.4%** | **$0.2563** | **95.4%** | **41.6%** |
| Cheapest always | 87.6% | $0.2060 | 93.5% | 39.1% |

The value pick keeps **95.4% of frontier first-pass quality at 41.6% of the cost**. The cheapest model saves 2.5 cost points but loses 1.9 quality points and fails a 90%-parity bar on two of five tasks. This is synthetic; the arithmetic and the definition are in [`docs/VALUE.md`](docs/VALUE.md), and the evidence behind every quality score is in [`docs/QUALITY.md`](docs/QUALITY.md).

### Multi-dimensional scorecard

[`tests/results/SCORECARD.md`](tests/results/SCORECARD.md) combines six dimensions from committed evidence:

| Correctness | Cost | Robustness | Coverage | Safety | Operability | Composite |
|---:|---:|---:|---:|---:|---:|---:|
| 100 | 84.2 | 100 | 100 | 100 | 100 | **96.8 / A** |

<p align="center"><img src="assets/scorecard.png" alt="ModelPick six-dimension scorecard" width="82%" /></p>

Correctness is the decision benchmark; it is not an independent output benchmark. Cost is regret plus the value simulation. Robustness is price perturbation, retry sensitivity, and determinism. Coverage is every task and model. Safety is the 25-case adversarial suite. Operability is p95 latency, `modelpick verify`, and line coverage (84.8%).

---

## The decision engine

```
request
  │
  ├─ task detection (20 nodes, English + Chinese) ── explicit --task always wins
  ├─ intent parsing (cheap / fast / best / open-source / budget / exclude)
  ├─ hard requirements (context, text-in-image, rigging, lip-sync, clip length)
  │
  ├─ capability filter → candidates
  ├─ benchmark-weighted quality
  ├─ cache-aware cost × expected attempts
  ├─ latency + context fit
  └─ weighted utility → pick + alternatives + why + trade-offs + setup
```

Presets: `balanced` (task weights), `value` (price-performance), `quality`, `cost`, `speed`, `privacy`. Budgets and quality floors are hard constraints, not suggestions.

**The default is a value decision, not a bargain hunt.** The value pick is the cheapest model within **8 quality points of the best eligible model**; if the band is empty, it falls back to the top recommendation. It is returned as `picks.value` and `value`, with the quality gap and the percentage of the best model's cost. The full definition, simulation, and sensitivity analysis are in [`docs/VALUE.md`](docs/VALUE.md).

Every answer includes:
- `recommendation.slug`, `quality`, `costPerTask`, `expectedAttempts`, `latencySec`
- `why[]` and `tradeoffs[]`
- `setup.direct` (env, key URL, docs, API model) and an OpenRouter fallback for text models
- `catalog.version`, `stale`, `priceConfidence`

---

## Bring your own decision model

The deterministic router is the default. If you want a judge or decision model
(Claude, GPT, Gemini, a Google decision model, or a local model) to re-rank the
shortlist, keep it outside the key store:

```bash
modelpick decide "rigged 3D character for Unity" --json > packet.json
# send packet.prompt to your judge; save its JSON as verdict.json
modelpick pick "rigged 3D character for Unity" --verdict verdict.json

# Decision-model candidates with exact endpoints and prices:
modelpick judges
```

`judges` includes **Jev (System One)** (`jev-latest`, Venice, $0.042/1M input) and **Gemini Decision 1** (`gemini-decision-1`, $0.10/1M input, zero output). They are decision models, not generation models.

The verdict can only reorder the shortlist, at most two positions, and cannot
invent a model or override a hard constraint. `pick_model` accepts the same
`verdict` object over MCP. The protocol, guardrails, and meta-evaluation
thresholds are in [`docs/JUDGES.md`](docs/JUDGES.md).

---

## Commands

```text
modelpick pick "<task>"            Rank models for one node
modelpick plan "<goal>"            Multi-step workflow, one model per step
modelpick compare <a> <b> --task   Side-by-side cost per solved task
modelpick models                   Browse the catalog
modelpick tasks                    List the 20 nodes
modelpick show <model>             Endpoint, auth, SDK, curl, and evidence
modelpick decide "<task>"          Build a portable decision packet for any judge
modelpick verify                   Verify catalog, evidence, benchmarks, hashes
modelpick eval <file>              Analyze your own pass/fail runs
modelpick add-model <file>         Add a private/custom model
modelpick setup [agent]            Install MCP + skill
modelpick mcp                      Run the stdio MCP server
modelpick keys                     Configure keys (wizard) or list status
modelpick keys --ui                Localhost-only key page
modelpick keys set OPENAI_API_KEY  Hidden-input key setup
modelpick keys test ENV            Live key check
modelpick keys remove ENV          Delete a local key
modelpick doctor                   Diagnose install, keys, freshness
modelpick update                   Refresh the catalog snapshot
modelpick bench                    Run the decision benchmark
```

Useful flags: `--optimize`, `--max-cost`, `--min-quality`, `--open-weights`, `--context`, `--exclude`, `--task`, `--verdict`, `--json`, `--explain`, `--no-color`.

```bash
# Machine-readable for any agent
modelpick pick "edit this product photo, remove the background" --json

# Quality floor + budget
modelpick pick "implement OAuth" --min-quality 85 --max-cost 0.25

# Open weights only
modelpick pick "refactor this repo" --open-weights

# Only models whose key is already in this shell
modelpick pick "refactor this repo" --available

# Need 400K tokens of context
modelpick pick "read this 400-page document" --context 400000
```


### Configure keys locally

`pick`, `plan`, and `compare` never need a key. To execute a model, configure at least one provider.

```bash
modelpick keys                 # interactive wizard
modelpick keys --ui            # localhost-only page, opens in your browser
modelpick keys list           # status only; values are never printed
modelpick keys test OPENAI_API_KEY
modelpick keys remove OPENAI_API_KEY
```

### Execute text models

```bash
# Auto-route from the prompt, then execute with the local key
modelpick run "refactor this function" --task coding-agent

# Pin a model
modelpick run "write a launch headline" --model gpt-6.2-sol

# Provider only (highest-quality text model for that provider)
modelpick run "review this diff" --provider anthropic

# No key at all: local Ollama
modelpick run "hello" --local --model qwen-local:latest
```

Cloud execution currently covers **text** models through OpenAI, Anthropic, Gemini, DeepSeek, and OpenRouter. Image, video, 3D, and audio execution adapters are next. The key is read from the local store/env and is never accepted as an argument.

### Run locally with no key

```bash
modelpick run "explain this function" --local
modelpick run --status
modelpick run "hello" --local --model qwen2.5:0.5b --json
```

This calls the local Ollama daemon at `127.0.0.1:11434`. It is text-only, lower quality than cloud models, and requires the model to be pulled first. Cloud `run_model` execution is the next layer.

Keys are stored in `~/.modelpick/secrets.json` with mode `0600`; environment variables take precedence. They are **not** sent to ModelPick, telemetry, or the judge model. They are only sent to the provider you choose.

The page binds to `127.0.0.1` with a one-time token. It is not a remote service. See [`docs/KEYS.md`](docs/KEYS.md).

No key at all? Use local Ollama for a text-only demo:

```bash
ollama pull qwen2.5:0.5b
modelpick keys list            # shows Ollama local status
modelpick pick "explain this function" --available
```

Ollama is a local runtime, not "Llama" itself; it can run Qwen, Llama, and other GGUF models. It is lower quality than cloud models and is not a 3D/video provider.

### Only have a few API keys?

You do not need every provider. ModelPick separates **the best decision** from **what you can run right now**:

```bash
modelpick pick "refactor this repo"
```

```text
! key missing: GEMINI_API_KEY, GOOGLE_API_KEY — recommendation is still valid
run now  GPT-6.2 Sol · $0.20 · quality 83.9 · key OPENAI_API_KEY
```

- `--available` restricts ranking to models whose key exists (or any text model if you have `OPENROUTER_API_KEY`).
- The JSON always includes `availability.bestAvailable`, `availability.fallbacks`, and `recommendation.availability.missing`.
- An `OPENROUTER_API_KEY` is a universal fallback for text models; `FAL_KEY` covers many media models.
- If a capability has no accessible model, the tool says so instead of inventing a recommendation.

### Add your own model

Bring a private endpoint, a self-hosted vLLM/Ollama model, or a provider the catalog does not cover:

```bash
modelpick add-model --example > my-model.json
# edit the slug, provider env var, pricing, and quality scores
modelpick add-model my-model.json
modelpick pick "refactor this repo"          # it is now a candidate
modelpick add-model --remove my-model
```

The model is written to `~/.modelpick/overrides.json`, validated against the full catalog before saving, and never touches the repo. You can also add a whole list with `{ "models": [...] }`.

### Connect without guessing the endpoint

`pick` gives you the env var and key URL. `show` gives you the full connection card:

```bash
modelpick show tripo-h3.1
```

```text
CONNECT
endpoint  https://api.tripo3d.ai/v2/openapi
model id  h3.1
auth      bearer · env TRIPO_API_KEY
platform  https://platform.tripo3d.ai
docs      https://developers.tripo3d.ai/en/docs
sdk       REST / MCP

example
curl -X POST "https://api.tripo3d.ai/v2/openapi/task" \
  -H "Authorization: Bearer $TRIPO_API_KEY" \
  -H "content-type: application/json" \
  -d '{"type":"text_to_model","prompt":"a stylized sword"}'
```

The same object is returned by the MCP `get_setup` tool. If an endpoint is a provider's common path rather than a freshly verified one, the card says so (`typical` vs `verified`).

---

## Built to change

Model prices move weekly. New providers appear monthly. The engine is deliberately data-first:

| Layer | File | Change without code |
|---|---|---|
| Models, prices, IDs | `catalog/models.json` | `catalog/quality.json` + `scripts/sync-catalog.js` |
| Task nodes, weights, floors, anchors | `catalog/tasks.json` | edit JSON, run `npm run validate` |
| Retry curve, presets, anchors | `catalog/policy.json` | edit JSON |
| Your private models / price overrides | `~/.modelpick/overrides.json` | add a full model object or patch a slug |
| Workflows | `catalog/plans.json` | add steps referencing task ids |
| Agent adapters | `src/integrations/` | one function per agent |

**Custom model example:**

```json
{
  "models": [
    {
      "slug": "my-private-model",
      "name": "My Private Model",
      "provider": { "id": "internal", "name": "Internal", "env": ["INTERNAL_KEY"], "keysUrl": "https://…", "docsUrl": "https://…" },
      "modality": "text",
      "contextWindow": 200000,
      "pricing": { "unit": "mtok", "input": 1, "output": 2, "currency": "USD" },
      "quality": { "overall": 88, "coding": 88, "codingAgent": 88, "reasoning": 88, "longContext": 80, "writing": 80, "multimodal": 60, "cheapWork": 70 },
      "speed": { "outputTps": 50, "ttftMs": 1000 },
      "tags": ["benchmarked"],
      "openWeights": false,
      "sources": [{ "name": "internal", "url": "https://…", "readAt": "2026-11-19" }]
    }
  ],
  "exclude": ["model-you-never-want"],
  "policy": { "presets": { "cost": { "quality": 0.35, "cost": 0.65, "speed": 0, "context": 0 } } }
}
```

No fork. No rebuild. `modelpick doctor` validates the result.

---

## Data, honesty, and limits

- **Prices:** models.dev / OpenRouter for text; BenchLM media pricing, Google Vertex, OpenAI, fal, Tripo, Meshy, ElevenLabs for media. Read date on every source.
- **Quality:** BenchLM BenchAlign and CursorBench 4.0 for text; vendor specs plus public comparisons for media. Media quality is the least independently verified part of the catalog; it is labeled and dated.
- **Known omissions:** Veo is Vertex-only now; Sora 2 is discontinued; GPT-Image-1 and Imagen 4 are retired. These are deliberately not in the catalog.
- **No telemetry.** No key storage. Recommendations work offline. `keys` reads presence only.
- **Not a gateway.** ModelPick does not proxy requests, mark up tokens, or hold your data. You call the provider directly.

See [`docs/DATA.md`](docs/DATA.md) for provenance and [`research/`](research/) for the underlying research.

---

## Development

```bash
node scripts/validate.js       # catalog + policy + manifests
node --test "tests/**/*.test.js"
node bench/run.js              # decision benchmark -> tests/results/
node bench/holdout.js          # held-out decision benchmark
node bench/value.js            # cost-per-solved-task simulation
node tests/adversarial/run.js  # 28 adversarial cases
node scripts/live_smoke.js      # free/public endpoint smoke (network)
node scripts/check.js          # all of the above
node scripts/make_assets.py    # regenerate README/test images
```

Requirements: Node ≥ 20.11. Runtime dependencies: **zero**. Python + Pillow are only needed to regenerate images.

- [Architecture](docs/ARCHITECTURE.md)
- [Data provenance](docs/DATA.md)
- [How value is defined](docs/VALUE.md)
- [Quality evidence](docs/QUALITY.md)
- [Media evidence: the first independent correction](docs/MEDIA_EVIDENCE.md)
- [Bring your own eval](docs/EVALS.md)
- [Self-hosting](docs/SELF_HOST.md)
- [NPM mirror](docs/NPM_MIRROR.md)
- [Live endpoint evidence](docs/LIVE_TESTING.md)
- [Ecosystem and embedding](docs/ECOSYSTEM.md)
- [Judge/decision models](docs/JUDGES.md)
- [Publishing and launch runbook](docs/PUBLISHING.md)
- [Growth playbook](launch/GROWTH.md)
- [Per-node leaderboard](docs/LEADERBOARD.md)
- [Model applicability](docs/APPLICABILITY.md)
- [Multi-dimensional scorecard](tests/results/SCORECARD.md)
- [Adversarial review](tests/ADVERSARIAL_REVIEW.md)
- [Test form: 20 tasks × 40 models](tests/results/TEST_FORM.md)
- [Citation metadata](CITATION.cff)
- [Design partner program: 5 slots](docs/DESIGN_PARTNERS.md)
- [Test plan](tests/TEST_PLAN.md)
- [Benchmark methodology](bench/METHODOLOGY.md)
- [Contributing](CONTRIBUTING.md)
- [Security](SECURITY.md)
- [Changelog](CHANGELOG.md)

---

## Roadmap

- [x] Publish to npm (`npx modelpick`) and submit to MCP directories
- [ ] Live price refresh from provider APIs with signed snapshots
- [ ] Community-contributed task nodes and quality evidence
- [ ] Router mode: optionally execute the recommended call through the user's own key
- [ ] Cost ledger: track actual spend per node across a project
- [ ] Windows-native MCP shim (no `cmd /c`)

If ModelPick saves you money, **star the repo** — it is the only distribution channel for a tool with no VC and no telemetry.

<p align="center"><sub>MIT © 2026 Lei Zhidong · built with zero runtime dependencies and a healthy distrust of token pricing.</sub></p>
