<div align="center">

# TokenDiet

### Your code is overpaying for AI. `/tokendiet` finds where — free, in your editor, in about a minute.

A Claude Code plugin that audits your own repo for wasteful LLM API spend — missing prompt caching, uncapped retries, prompt bloat, no batching, overpowered models — and hands you a concrete, honest fix plan. Runs on **your** agent, **your** tokens, **your** repo. Nothing leaves your machine.

[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](./LICENSE)
[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-plugin-d97757.svg)](https://docs.claude.com/en/docs/claude-code/plugins)
[![Built by Fortytude](https://img.shields.io/badge/built%20by-Fortytude-111.svg)](https://fortytude.dev)

</div>

---

Hosted LLM APIs bill per token. Most codebases quietly re-send the same system prompt uncached on every call, run offline batch jobs on the real-time API, never cap a retry loop, and pretty-print JSON into the prompt. None of it shows up in a code review — it shows up on the invoice.

`/tokendiet` reads your code the way a senior LLM-cost engineer would, finds those patterns at the exact `file:line`, explains the mechanism, and gives you the fix. It offers to apply the safe, behavior-preserving ones for you.

And it **never invents a dollar figure.** More on why that matters below — it's the whole point.

## 📋 What a run looks like

You type `/tokendiet`. Your agent walks your repo and prints something like this (illustrative — your findings and paths will differ):

```text
## TokenDiet audit — whole repo
Reviewed 14 LLM call-sites across 6 files. Found 4 findings.

### Safe mechanical wins (behavior-preserving — ship these)

1. Missing prompt caching — src/agent/planner.py:57
   WHAT: a ~2,100-token system prompt + tool schema is re-sent uncached on every
         Anthropic call.
   WHY:  cached reads bill at ~10% of the input rate (Anthropic published) — right
         now you pay full input price for the same bytes on every request.
   FIX:  add cache_control:{type:"ephemeral"} on the last stable system block.
   CLASS: SAFE-MECHANICAL

2. Timestamp busting the cache — src/agent/planner.py:44
   WHAT: `Current time: {datetime.now()}` sits at the FRONT of the system prompt.
   WHY:  caching is a prefix match; a value that changes every call invalidates
         everything after it, so the hit rate is ~0 even once caching is on.
   FIX:  move the timestamp to the end of the prompt, after the static prefix.
   CLASS: SAFE-MECHANICAL  (this IS the cache win for this prefix — counted once)

### Suggestions to validate (behavior-change — your call)

3. Overpowered model for a classify task — src/route/intent.py:88
   WHAT: `classify_intent()` calls a flagship model to pick one of 5 labels.
   WHY:  a small model is roughly ~5× cheaper on input and may handle a labeling
         task fine — but a swap changes output quality.
   FIX:  try a cheaper same-family model and validate the labels on your own data.
   CLASS: BEHAVIOR-CHANGE  (a downgrade is a suggestion, never a promised saving)

### Guard-rails & notes (informational)

4. No max_tokens cap in the agent loop — src/agent/loop.py:15
   WHAT: the completion call has no max_tokens / max output ceiling.
   WHY:  a runaway loop or a degenerate response can emit the full output window —
         an unbounded bill. (A ceiling, not a saving — no dollar figure.)
   FIX:  add an explicit max_tokens sized to what the response needs.
   CLASS: INFORMATIONAL

Want me to apply the 2 safe mechanical wins? I'll show the diff first.

— Audited by /tokendiet · TokenDiet by Fortytude (fortytude.dev). Free & open source.
```

That's the whole product. No signup, no dashboard, no dollar amount pulled out of thin air.

## ⚡ Install

In Claude Code:

```text
/plugin marketplace add Fortytude/TokenDiet
/plugin install tokendiet@tokendiet
```

Then run it:

```text
/tokendiet
```

That's it. `marketplace add` points Claude Code at this repo; `install` pulls the `tokendiet` plugin from it. No API keys of ours, no account, no config.

Prefer the terminal? The same works non-interactively once the marketplace is added:

```bash
claude plugin marketplace add Fortytude/TokenDiet
claude plugin install tokendiet@tokendiet
```

### Not on Claude Code?

The same audit ships for three more editors — same knowledge, native packaging. Each folder under [`editors/`](./editors) has its own README:

| Editor | Get it | Run it |
|---|---|---|
| **Cursor** | copy [`editors/cursor/.cursor/`](./editors/cursor) into your repo | `/tokendiet` in Agent chat |
| **GitHub Copilot** | copy [`editors/copilot/.github/`](./editors/copilot) into your repo | `/tokendiet` in Copilot Chat |
| **Codex** | copy [`editors/codex/.agents/` + `AGENTS.md`](./editors/codex) into your repo | `$tokendiet`, or just ask "audit my LLM cost" |

## 🎯 Usage

`/tokendiet` takes an optional scope. Give it as much or as little as you want:

```text
/tokendiet                 # audit the whole repo
/tokendiet src/ai/         # audit a single path or module
/tokendiet the auth flow   # audit an area, described in words
/tokendiet my last PR      # git-diff the last PR/commit, audit only changed call-sites
```

Scoping to `my last PR` is the fast one to wire into your habit — audit the AI code you just wrote before you merge it.

## 🔎 What it catches

The plugin ships a catalog of ~20 LLM-cost waste patterns. It matches each call-site against them — in Python **and** TS/JS — across OpenAI, Anthropic, the Vercel AI SDK, LangChain / LlamaIndex, AWS Bedrock, Google Gemini, and raw HTTP calls. It follows home-grown wrappers to the real provider call, because that's where the waste usually hides.

Findings are grouped by how safe the fix is:

#### ✅ Safe mechanical wins — behavior-preserving, ship the diff

The model sees the exact same thing; only billing changes.

- **Missing prompt caching** — a large static prefix (system prompt + tool schema + few-shot) re-sent uncached on every call.
- **Cache busted by a volatile prefix** — a timestamp, uuid, or unsorted `json.dumps` sitting *before* the static content, dropping the hit rate to ~0.
- **Cache present but disabled by default** — the plumbing exists but a default flag / short TTL / misplaced breakpoint leaves it off.
- **Tool schema re-sent uncached** — a big tool catalog passed every agent turn with no cache breakpoint (often the largest cacheable region).
- **Few-shot examples not cached** — a static example block paid for at full input price every call.
- **Unstructured output + parse/retry loop** — free-text + `json.loads` + retry-on-failure, where a structured-output contract would kill the loop.
- **Missing `max_tokens` cap** — added as a real fix (a bill ceiling), never sold as a saving.
- **Legacy / retired model id** strictly dominated by its successor (same-or-better quality *and* cheaper) — a pure string swap, the only model change that ships mechanically.

#### 🤔 Suggestions to validate — behavior-change, your call

These change what the model sees or does. The plugin suggests them and tells you to validate on your own outputs. It never auto-applies them.

- **Overpowered model for a simple task** — a flagship on a classify/extract/route/title sub-task. Always a suggestion, never a promised saving.
- **No model routing / cascade** — a single flagship for all traffic where a confidence-gated cascade could help.
- **RAG over-fetch** — `top_k` / chunk size cranked high, stuffing low-relevance chunks into every prompt.
- **Re-embedding without a content-hash cache** — an embedding loop that re-embeds unchanged content every run.
- **Verbose payload serialization** — `json.dumps(x, indent=2)` / `JSON.stringify(x, null, 2)` shipping whitespace as tokens.
- **High reasoning effort on trivial calls** — extended thinking / `reasoning_effort:"high"` on a fire-and-forget utility call.
- **Sync API on an offline workload** — a bulk / cron / eval loop with no user waiting, where the **Batch API is 50% off** (published rate). Offline-only — never suggested on a live request path.

#### 🛡️ Guard-rails & notes — informational, always $0

Risk ceilings and enablers, not trims. Reported as leads, never with a dollar figure.

- **Uncapped / amplified retries** — a retry that re-sends the whole request N× on failure (worse when the SDK already retries underneath).
- **Growing conversation history** — an unbounded `messages` list replayed in full every agent turn (O(n²) accumulation).
- **Duplicate / mergeable calls** — the same payload sent twice, or N sequential calls that could merge into one.
- **No spend cap** on a public / agent entry point — a blast-radius guard against a runaway loop or abuse.
- **No cost / usage instrumentation** — no Langfuse / OpenLLMetry / OTel spans, so waste is invisible until you add them.

It also knows the **dead levers not to recommend** — the `token-efficient-tools` header (a no-op on Claude 4+), lowering `max_tokens` to cut *input* cost (it can't), temperature/top_p "tuning" for cost (no billing effect), and adding `cache_control` on OpenAI/Gemini (their caching is automatic — the lever is ordering). Bad advice is worse than no advice.

## ⚙️ How it works

There's no TokenDiet server. There's no TokenDiet account. There's no TokenDiet API key.

The plugin is a slash command plus a skill — a body of LLM-cost knowledge (the waste catalog, per-provider detection heuristics, and a strict honesty contract). When you run `/tokendiet`, **your own Claude Code agent** loads that knowledge and audits **your** code with **your** tokens on **your** machine.

That means the privacy story is simple and real: **your code never leaves your laptop.** We can't see your repo, log it, store it, or train on it, because it never reaches us. The plugin is just files you can read in this repo.

## 🤝 The honesty contract

This is the part that makes the report worth screenshotting.

**TokenDiet never invents a dollar figure.** It can't see your traffic — your call volume, your cache hit rate, your easy/hard query mix are all runtime facts that live on your machine, not in your code. So any "$X/month saved" number would be fabricated, and a fabricated number poisons the whole report the moment someone divides it back out.

Instead:

- It describes waste **qualitatively** — the pattern, the mechanism, the fix.
- It **cites published provider rates as facts** — "cached reads bill at ~10% of the input rate," "the Batch API is 50% off" — but never multiplies a rate into a total.
- A **model swap is always a suggestion, never a saving.** Changing the model changes output quality; that's a bet on output the plugin can't see, so it never attaches a dollar figure to it and it never auto-applies it.
- It **cites evidence** — every finding points at a real `file:line`. No evidence, no finding.
- It **never claims to be exhaustive** — static analysis catches direct SDK calls and followable wrappers (~80% of direct call-sites) and misses fully-dynamic dispatch. It says "I reviewed N call-sites," never "I found everything."

If you *do* explicitly ask "how much will this save me?", it asks for your monthly bill or call volume first and contextualizes against *that* — clearly, as an estimate that depends on your traffic. It just never volunteers a number it can't stand behind.

That discipline is the reason the report is trustworthy. The honesty *is* the product.

## 🛠️ Built by Fortytude

TokenDiet is built by [Fortytude](https://fortytude.dev) — we build tools for people
shipping with AI. This plugin is free, open source, and stays that way. If it saves you
money, a ⭐ on the repo is the only thanks we ask.

## 🧩 Contributing

TokenDiet is MIT-licensed and built to be extended. The knowledge lives in flat, readable files — adding a new waste pattern is a documentation change, not a code change.

```text
tokendiet/
├── commands/
│   └── tokendiet.md                      # the /tokendiet slash command + workflow
├── skills/tokendiet/
│   ├── SKILL.md                          # the methodology and fix taxonomy
│   └── references/
│       ├── waste-catalog.md              # the ~20 waste patterns  ← add one here
│       ├── detection-heuristics.md       # how to find call-sites, per provider
│       └── honesty-rules.md              # the honesty contract
├── editors/
│   ├── cursor/                           # Cursor packaging (.cursor/commands + rule)
│   ├── copilot/                          # GitHub Copilot packaging (.github/prompts)
│   └── codex/                            # Codex packaging (.agents/skills + AGENTS.md)
└── .claude-plugin/
    ├── plugin.json                       # plugin manifest
    └── marketplace.json                  # marketplace entry
```

Good first contributions:

- **A new waste pattern** — add an entry to `waste-catalog.md` with the code shape (Python **and** TS/JS), the mechanism, the fix, and the honesty class. Match the format of the existing entries.
- **Better detection** — improve a provider's grep/heuristics in `detection-heuristics.md`, especially for wrappers or a framework we don't cover well yet.
- **A new command** — a focused variant (e.g. a caching-only pass) under `commands/`.

Two hard rules for any contribution: **every finding must cite a real `file:line`, and nothing may fabricate a dollar figure.** A PR that adds a "$X saved" claim will be declined — that line is the point of the project. Open an issue to discuss anything larger.

## 📄 License

[MIT](./LICENSE) © Fortytude. Use it, fork it, ship it.

---

<div align="center">

**Built by [Fortytude](https://fortytude.dev)** · [Report an issue](https://github.com/Fortytude/TokenDiet/issues)

If `/tokendiet` found something worth fixing in your repo, drop a ⭐ — it helps other devs find it.

</div>
