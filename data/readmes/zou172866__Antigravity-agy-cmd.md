<div align="center">

[简体中文](README.zh-CN.md) · **English**

<img src="assets/logo.svg" alt="agy-cmd logo" width="80" />

# agy-cmd

**Google Antigravity plugin: auto-route commands · Stop-hook auto-retry · auto multi-agent dispatch · fresh-perspective stuck recovery · anti-bypass plan guard**

[![Clones](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/zou172866/repo-traffic-archive/main/badges/Antigravity-agy-cmd.json)](https://github.com/zou172866/repo-traffic-archive)

[How to Install](#how-to-install) · [Features](#features) · [CLI Management](#cli-management)

</div>

---

## What is agy-cmd?

`agy-cmd` is a workflow plugin for **Google Antigravity Desktop / IDE**.

Once installed, it runs automatically in the background during every chat to handle these things:

- **Auto-route built-in workflows by task**: matches `/grill-me`, `/plan`, `/run-workflow`, and related workflows based on scope;
- **Stop-hook auto-retry guard**: keeps the agent investigating and fixing when tests or build checks fail instead of stopping early;
- **Auto-dispatch Boost on hard debugging and stuck loops**: with Pro / Ultra Boost enabled, asking to investigate or fix hard bugs (such as deadlocks, race conditions, or memory leaks) or hitting repeated failures automatically launches `DeepCoder` / `DeepInvestigator` to investigate, execute, and verify (plan-approval Boost dispatch is also available as an optional toggle in the panel);
- **Auto multi-agent dispatch**: automatically selects the right multi-agent mode for the task while keeping simple tasks in the main conversation.
- **Fresh-perspective stuck recovery (all tiers)**: when repeated fixes fail, gives one available investigator a read-only diagnosis task. The main agent checks the proposed fix.
- **Anti-bypass read-only plan guard**: when read-only Plan Mode blocks writing the plan file, forces an inline plan in chat and blocks `exit_plan_mode` so the agent cannot bypass approval and silently edit code;
- **Live right-hand Sidecar control panel**: lets you toggle retry limits, trigger scope, and free-tier protection anytime (shielding free accounts from paid-only command errors by default).

## How to Install

For the packaged stable version, download the ZIP from [GitHub Releases](https://github.com/zou172866/Antigravity-agy-cmd/releases/latest), extract it, and run `.\install.ps1` on Windows or `sh ./install.sh` on macOS or Linux.

Requires **Google Antigravity Desktop**, **Node.js (>= 20)**, and **Python 3**.

Run the one-line installer for your OS, then restart or reload your Antigravity window.

**Windows (PowerShell):**

```powershell
irm https://raw.githubusercontent.com/zou172866/Antigravity-agy-cmd/main/install.ps1 | iex
```

**macOS / Linux:**

```bash
curl -fsSL https://raw.githubusercontent.com/zou172866/Antigravity-agy-cmd/main/install.sh | sh
```

**Manual clone install:**

```powershell
git clone https://github.com/zou172866/Antigravity-agy-cmd "$HOME\.gemini\config\plugins\agy-cmd"
python "$HOME\.gemini\config\plugins\agy-cmd\skills\agy-cmd\scripts\setup_auto_router.py" --install
```

**Standalone rules only** (text routing rules without Stop auto-retry or the Sidecar panel):

```bash
npx -y skills add zou172866/Antigravity-agy-cmd -g --all
python ~/.agents/skills/agy-cmd/scripts/setup_auto_router.py --install --standalone
```

## First Two Settings to Check

To prevent free accounts from hitting errors on paid-only commands, `agy-cmd` ships with **Free-Tier Protection enabled** and **Auto-Retry set to 3 attempts** by default.

After installing, open the right-hand **agy-cmd Auto-Router** Sidecar panel (or click `sidecar://agy-cmd/panel/` in chat) and confirm:

1. **Auto-retry limit**: choose **Off (0)**, **Fixed count (1–50)**, or **Unlimited**.
2. **Account tier**: if you subscribe to **Google AI Pro / Ultra**, switch to **Pro / Ultra** to enable automatic Boost dispatch for hard debugging requests (such as deadlocks, race conditions, or memory leaks) and repeated failures. The panel’s **Use Boost after plan approval** switch is off by default; turn it on if you also want clicking **Approve** or replying “implement the plan” to output `[agy-cmd → 计划获批，自动 Boost]` and directly dispatch Antigravity’s hidden `DeepCoder` / `DeepInvestigator` Boost subagents once without requiring manual `/boost` input (falling back to standard tools only if invocation fails), with deduplication across background-task wakeups.

## Features

### 1. Automatic workflow routing by task scope

No need to memorize or manually pick built-in Antigravity slash commands for every turn:

- **1–2 files, explanations, or local lookups**: responds directly with zero extra prompts or banners.
- **Ambiguous requirements**: asks a focused multiple-choice clarification question first.
- **3+ files or higher-risk edits**: drafts an implementation plan for your approval before touching project files (even in read-only plan mode, it writes the plan inline and waits for confirmation); if you opt into **Use Boost after plan approval** under Pro / Ultra Boost, approving the plan displays `[agy-cmd → 计划获批，自动 Boost]` and dispatches `DeepCoder` / `DeepInvestigator` strictly once while preserving `Stop` auto-retry state across background-task wakeups.
- **A self-contained side task**, such as tracing a call chain or inspecting a UI, can go to one subagent. Simple lookups stay in the main session.
- **Repeated work** on five or more similar items runs in batches by default. With the panel set to a paid tier and the command available in the App, the plugin can choose `/run-workflow` to apply the same check to each item and collect structured results.
- **Separate modules that need to agree on an interface** can use `/swarm` in the App. Set the interface, give each writer distinct files and name the integration check. A single recurring failure fits `/boost`. A multi-day migration with separately verifiable milestones fits `/teamwork`. [Routing examples](skills/agy-cmd/references/desktop-commands-matrix.md)
- **Dynamic web pages or interactive visuals**: automatically triggers the built-in browser or interactive UI renderer.

### 2. Stop-hook auto-retry guard

Prevents the agent from stopping early while tests or build checks are still failing.

When you ask the AI to edit code or fix a bug and verification fails, the `Stop` hook automatically nudges it to keep investigating and fixing until checks pass or the configured retry limit is reached.

You can also opt into the **Delivery Test Gate (run full tests before delivery)** toggle in the panel (off by default, works across all tiers and ordinary coding turns):

- **Custom verification command or detected project tests**: after any substantive source edit, the agent must run and pass the full check suite (supports single commands or `&&` chains such as `npm run typecheck && npm test`) *after* the latest edit before delivering; missing checks are nudged and failing checks loop within your retry budget until green.
- **No existing test command & no custom command**: conservatively allows delivery without modifying repo test setup, while instructing the agent to explicitly disclose the missing test coverage at the end of its response.
- Say `skip tests` or `这次跳过测试` in a prompt to bypass the gate for that single turn.

For an approved implementation plan in free mode, the plugin can also request one missing project check after a confirmed source edit. This uses the existing retry budget. Documentation edits, a canceled turn or an outstanding approval do not trigger this reminder.

It lets the agent stop immediately when:

- You only asked a question (e.g., "why did this error happen?", "check the root cause", or "run tests to see") without asking for code edits;
- The AI just submitted a plan and is waiting for your approval;
- The AI needs missing information from you;
- You manually clicked Stop.

You can override the retry count for a single prompt using natural language (e.g., `这次最多重试 5 次`, `这次一直重试`, or `这次不用重试`).

### 3. Free-tier command protection & stuck-loop recovery

Prevents free accounts from triggering paid-only errors and stops blind retry loops:

- **Plan and quota**. Google offers `/boost` and `/teamwork` on paid plans. The App offers `/swarm` and `/run-workflow` on all plans. The plugin skips automatic use of the latter two in free mode to conserve weekly quota. You can explicitly request either for the current task in a supported App session. In the IDE or when availability is unknown, automatic routing stays in the main session. [Boost and plan comparison](https://antigravity.google/docs/boost/) · [Dynamic Workflows](https://antigravity.google/docs/dynamic-workflows/)
- **Optional independent review**. In free mode you can enable a review after plan implementation in the Sidecar. The main agent edits and runs checks, then hands the changed paths, relevant diff and evidence to one `cmd-verifier` with file-reading access. The option defaults to off. If the role is unavailable, the main agent reports that the independent review was skipped.
- **Hard-task & stuck-loop recovery**: on free plans (or with Boost off), 3 consecutive command failures or 2 identical edit-fail cycles pause blind edits and switch to read-only root-cause diagnosis; with paid Boost enabled, explicit hard debugging requests or repeated failures automatically dispatch `DeepInvestigator` / `DeepCoder` while the main session verifies the result.

The [routing research](docs/research/multi-agent-routing-best-practices.md) and [free-tier design proposal](docs/proposals/free-tier-v2.3.md) explain the choices. The hooks and installer have been tested locally. Dispatching the reviewer on a live free account in the App and IDE still needs verification.

### 4. Sidecar control panel & slash-command reference

Manage settings or compare built-in Antigravity slash commands anytime:

- Toggle retry count, trigger policy, and plan tier in the right-hand **agy-cmd** Sidecar panel — changes take effect immediately.
- Click `★ Star` in the panel header to follow updates on GitHub (after 3 successful auto-retry saves, a one-time dismissible reminder appears once).
- Adjust settings or inspect commands directly in chat (e.g., ask to set auto-retry to 5, enable Boost, or compare all built-in Antigravity desktop slash commands).

## CLI Management

You can also inspect and configure `agy-cmd` from the terminal:

```bash
# Inspect plugin, panel, hook, and retry status
python skills/agy-cmd/scripts/setup_auto_router.py --status

# Configure auto-retry limit (off / 1..50 / infinite)
python skills/agy-cmd/scripts/setup_auto_router.py --auto-retry off
python skills/agy-cmd/scripts/setup_auto_router.py --auto-retry 5
python skills/agy-cmd/scripts/setup_auto_router.py --auto-retry infinite

# Switch account tier
python skills/agy-cmd/scripts/setup_auto_router.py --plan-tier free
python skills/agy-cmd/scripts/setup_auto_router.py --plan-tier paid --boost on

# Toggle Delivery Test Gate (off by default) and optionally configure a custom verification command
python skills/agy-cmd/scripts/setup_auto_router.py --delivery-test-gate on
python skills/agy-cmd/scripts/setup_auto_router.py --delivery-test-cmd "npm run typecheck && npm test"
python skills/agy-cmd/scripts/setup_auto_router.py --delivery-test-gate off

# Enable one independent review after implementing an approved plan in free mode
python skills/agy-cmd/scripts/setup_auto_router.py --free-plan-review on

# Verify plugin bundle integrity
python skills/agy-cmd/scripts/setup_auto_router.py --sync-check

# Disable / remove plugin
python skills/agy-cmd/scripts/setup_auto_router.py --remove
```

Run the test suite:

```bash
npm test
python -m unittest discover -s test -p "test_*.py" -v
```
