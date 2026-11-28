<div align="center">

[简体中文](README.zh-CN.md) · **English**

<img src="assets/logo.svg" alt="agy-cmd logo" width="80" />

# agy-cmd

**Guardrail & auto-router plugin for Google Antigravity Desktop / IDE: never stop on failing tests · fresh-perspective recovery · free-tier safe · no skipped approvals**

[![Clones](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/zou172866/repo-traffic-archive/main/badges/Antigravity-agy-cmd.json)](https://github.com/zou172866/Antigravity-agy-cmd)

[Quick Install](#quick-install) · [Features](#features) · [CLI Management](#cli-management)

</div>

---

## Why agy-cmd?

Tests are still failing, yet the agent politely announces "all done."
A free account hits a paid-only slash command and crashes mid-task.
Read-only Plan Mode blocks writing the plan file, so the agent tries to skip approval and edit code anyway.
Three patch attempts make the same bug worse, yet it keeps guessing in circles.

**`agy-cmd` puts guardrails around Google Antigravity Desktop / IDE.** Install once and let it watch silently in the background:

- **Scope-aware routing**: small edits run straight through, bigger changes ask for a plan first, and batch or multi-module tasks match native workflows automatically.
- **Stop-hook auto-retry**: when tests or build checks fail after an edit, the hook blocks early stop and keeps the agent fixing until green or the retry cap hits.
- **Fresh-perspective recovery**: repeated failures stop blind edits immediately. Free accounts dispatch a read-only investigator; Pro / Ultra accounts can auto-dispatch Boost subagents.
- **Hard approval guard**: when read-only Plan Mode blocks writing a plan file, the hook forces an inline plan in chat and blocks `exit_plan_mode` until you approve.
- **Free-tier protection**: paid-only commands stay off by default, and work runs sequentially in the main session to protect weekly quota.
- **Live Sidecar panel**: adjust retry caps, test gates, account tier, and SHA-256 self-updates anytime from the right-hand panel.

## Quick Install

Requires **Google Antigravity Desktop**, **Node.js 20+**, and **Python 3.8+**.

Run the pinned one-line installer for your OS (downloads the official release ZIP and verifies its `SHA256SUMS.txt` digest before unpacking), then restart or reload your Antigravity window.

**Windows (PowerShell):**

```powershell
irm https://raw.githubusercontent.com/zou172866/Antigravity-agy-cmd/v2.8.0/install.ps1 | iex
```

**macOS / Linux:**

```bash
curl -fsSL https://raw.githubusercontent.com/zou172866/Antigravity-agy-cmd/v2.8.0/install.sh | sh
```

### Other Install Options

- **Offline stable ZIP (with SHA-256 verification)**: download the official ZIP and `SHA256SUMS.txt` from [GitHub Releases](https://github.com/zou172866/Antigravity-agy-cmd/releases/latest):
  - Verify and install directly: `.\install.ps1 --archive .\agy-cmd-v2.8.0.zip --checksums .\SHA256SUMS.txt` (Windows) or `sh ./install.sh --archive ./agy-cmd-v2.8.0.zip --checksums ./SHA256SUMS.txt` (macOS / Linux).
  - Or extract and run `.\install.ps1` (Windows) / `sh ./install.sh` (macOS / Linux) inside the unpacked folder.
- **Manual Git clone** (a `.git` checkout inside `plugins/agy-cmd` disables Sidecar self-update to protect your working tree; update with `git pull` or use the one-line installer above):

```powershell
git clone https://github.com/zou172866/Antigravity-agy-cmd "$HOME\.gemini\config\plugins\agy-cmd"
python "$HOME\.gemini\config\plugins\agy-cmd\skills\agy-cmd\scripts\setup_auto_router.py" --install
```

On Linux / macOS / SSH hosts without a `python` symlink, replace `python` with `python3`. If installed via `agy plugin install` or Marketplace (`installedFrom`), update through Antigravity's plugin manager.

- **Standalone text rules only** (routing rules without Stop auto-retry or the Sidecar panel):

```bash
npx -y skills add zou172866/Antigravity-agy-cmd -g --all
python ~/.agents/skills/agy-cmd/scripts/setup_auto_router.py --install --standalone
```

## First Two Settings to Check

Out of the box, `agy-cmd` enables **Free-Tier Protection** and sets **Auto-Retry to 3 attempts**. Open the right-hand **agy-cmd Auto-Router** panel (or click `sidecar://agy-cmd/panel/` in chat) and confirm two settings:

1. **Auto-retry limit**: choose **Off (0)**, **Fixed count (1–50)**, or **Unlimited**.
2. **Account tier**: Google AI Pro / Ultra subscribers can switch to **Pro / Ultra** to enable automatic Boost dispatch on hard debugging tasks (such as deadlocks, race conditions, or memory leaks) and repeated failures. **Use Boost after plan approval** stays off by default. Turn it on if you also want clicking **Approve** or replying "implement the plan" to show `[agy-cmd → 计划获批，自动 Boost]` and dispatch `DeepCoder` / `DeepInvestigator` once (falling back to regular tools on invocation error, with deduplication across background-task wakeups).

## Features

### 1. Small tasks straight through, big changes planned first

- **1–2 files, explanations, or local lookups**: responds directly with zero banners or popups.
- **Ambiguous requests**: asks focused multiple-choice questions on blocking gaps (batching independent questions) before writing code.
- **3+ files or higher-risk edits**: drafts a plan and waits for your approval. In read-only Plan Mode, it writes the plan inline and blocks silent bypasses. Approved multi-module plans can continue with `/swarm execute our plan` in the App; paid users who opt into post-approval Boost get a single Boost dispatch while keeping `Stop` auto-retry state intact across background wakeups.
- **Focused side tasks & batch checks**: a self-contained investigation (such as tracing a call chain or checking a page) can go to one subagent. Checks across 5+ similar items run in batches by default; on paid tiers in the App, `/run-workflow` can fan out and collect structured results.
- **Independent lanes & multi-day work**: non-colliding multi-module edits, multi-lens reviews, or Best-of-N comparisons fit `/swarm` in the App (6 ready-to-copy templates, Gemini 4 model pairing, and a pre-launch checklist). Tightly coupled edits stay in the main session / Orchestrator, single hard failures fit `/boost`, and multi-day milestone migrations fit `/teamwork`. Active `/swarm` sessions and workers (including forked workers) are isolated by hooks so board collaboration and prompt prefix caching stay intact. [Command matrix](skills/agy-cmd/references/desktop-commands-matrix.md) · [Multi-agent & Swarm playbooks](skills/agy-cmd/references/multi-agent-playbooks.md)
- **Live web pages & interactive visuals**: launches the built-in browser or interactive UI renderer automatically.

### 2. Never stop while tests are failing

When you ask the agent to change code or fix a bug and verification fails, the `Stop` hook sends it back to investigate and fix until checks pass or your retry cap runs out.

For stricter enforcement, enable **Delivery Test Gate (run full tests before delivery)** in the panel (off by default, available on all tiers). Whenever a turn makes substantive source edits:

- **Custom verification command or detected project tests**: the full check suite (single commands or `&&` chains like `npm run typecheck && npm test`) must pass *after* the final edit before delivery. Missing checks trigger a reminder; failing checks loop within your retry budget.
- **No project tests and no custom command**: delivery is allowed conservatively without touching repo test setup, and the agent explicitly discloses missing test coverage at the end.
- **One-turn bypass**: add `skip tests` or `这次跳过测试` in your prompt to skip the gate for that turn.

In free mode, implementing an approved plan with source edits and a missed project check can also trigger one check reminder within your existing retry budget. Documentation edits, cancellations, and pending approvals never trigger it.

The hook lets the agent stop right away when:

- You only asked a question or ran read-only inspection (e.g., "why did this fail?" or "run tests to see").
- The agent just presented a plan and is waiting for approval.
- The agent stopped to ask for missing information.
- You manually clicked Stop.

To override the retry budget for a single turn, include `这次最多重试 5 次`, `这次一直重试`, or `这次不用重试` in your prompt.

### 3. Free-tier safety & stuck-loop recovery

- **Plan and quota**: Google restricts `/boost` and `/teamwork` to paid tiers, while `/swarm` and `/run-workflow` are open on all App tiers. In free mode, `agy-cmd` runs sequentially by default to conserve weekly quota; you can still invoke the latter two explicitly in supported App sessions. In the IDE or unknown hosts, routing stays safely in the main session. [Boost and plan comparison](https://antigravity.google/docs/boost/) · [Dynamic Workflows](https://antigravity.google/docs/dynamic-workflows/)
- **Optional independent review**: free users can enable a post-plan review in the panel (off by default). After editing and running checks, the main agent hands changed paths, key diffs, and test evidence to a read-only `cmd-verifier`; if that role is unavailable, the main agent reports that the review was skipped.
- **Stuck-loop circuit breaker**: on free plans (or with Boost off), 3 consecutive command failures or 2 edit-fail cycles pause blind edits and switch to read-only root-cause diagnosis. With paid Boost enabled, explicit hard debugging tasks, 3 consecutive command failures, or 3 edit-fail cycles (leaving Orchestrator's native 2-failure planner hand-back room to self-heal) dispatch `DeepInvestigator` / `DeepCoder` while the main session verifies the fix.

Hooks and installers are verified locally; live free-tier reviewer dispatch in the App and IDE remains to be verified on real accounts. [Routing research](docs/research/multi-agent-routing-best-practices.md) · [Free-tier proposal](docs/proposals/free-tier-v2.3.md)

### 4. Sidecar panel & verified self-updates

- **Instant controls**: change retry caps, trigger scope, test gates, and plan tier in the right-hand **agy-cmd** panel with immediate effect.
- **SHA-256 self-updates**: click **Check Update** in the panel header to pull GitHub Releases and update in place with SHA-256 verification and automatic rollback on failure. Startup auto-check is on by default and can be disabled in the panel, via `--auto-update-check off`, or via `AGY_CMD_DISABLE_AUTO_UPDATE_CHECK=1`. Silent auto-install is **off by default**; when turned on, it only installs same-major releases with verified SHA-256 digests and trips a per-version circuit breaker on failure.
- **Restrained Star prompt**: click `★ Star` in the header anytime. After 3 successful auto-retry saves, a single dismissible reminder appears once and never returns once resolved.
- **Chat commands**: ask directly in chat to set auto-retry to 5, enable Boost, or compare built-in Antigravity desktop slash commands.

## CLI Management

You can inspect and configure `agy-cmd` from the terminal as well:

```bash
# Inspect plugin, panel, hook, and retry status
python skills/agy-cmd/scripts/setup_auto_router.py --status

# Configure auto-retry limit (off / 1..50 / infinite)
python skills/agy-cmd/scripts/setup_auto_router.py --auto-retry off
python skills/agy-cmd/scripts/setup_auto_router.py --auto-retry 5
python skills/agy-cmd/scripts/setup_auto_router.py --auto-retry infinite

# Switch account tier and toggle post-plan Boost / fallbacks
python skills/agy-cmd/scripts/setup_auto_router.py --plan-tier free
python skills/agy-cmd/scripts/setup_auto_router.py --plan-tier paid --boost on
python skills/agy-cmd/scripts/setup_auto_router.py --boost-after-plan-approval on
python skills/agy-cmd/scripts/setup_auto_router.py --free-fallback on --plan-fallback on

# Reset cumulative auto-retry statistics without altering tier or Boost
python skills/agy-cmd/scripts/setup_auto_router.py --reset-stats

# Toggle Delivery Test Gate (off by default) and optionally configure a custom command
python skills/agy-cmd/scripts/setup_auto_router.py --delivery-test-gate on
python skills/agy-cmd/scripts/setup_auto_router.py --delivery-test-cmd "npm run typecheck && npm test"
python skills/agy-cmd/scripts/setup_auto_router.py --delivery-test-gate off

# Enable one independent review after implementing an approved plan in free mode
python skills/agy-cmd/scripts/setup_auto_router.py --free-plan-review on

# Toggle automatic GitHub Releases check on panel open (on by default)
python skills/agy-cmd/scripts/setup_auto_router.py --auto-update-check off
python skills/agy-cmd/scripts/setup_auto_router.py --auto-update-check on

# Opt in to silent same-major + SHA-256 auto-updates (off by default)
python skills/agy-cmd/scripts/setup_auto_router.py --auto-update-install on
python skills/agy-cmd/scripts/setup_auto_router.py --auto-update-install off

# Verify plugin bundle integrity and local sync
python skills/agy-cmd/scripts/setup_auto_router.py --sync-check

# Disable / remove plugin
python skills/agy-cmd/scripts/setup_auto_router.py --remove
```

Run the test suite and strict plugin validation:

```bash
npm test
python3 -m unittest discover -s test -p "test_*.py" -v
agy plugin validate --strict .
```
