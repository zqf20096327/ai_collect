<div align="center">

# 🚀 Cursor AI Tips & Tricks

[![GitHub stars](https://img.shields.io/github/stars/murataslan1/cursor-ai-tips?style=social)](https://github.com/murataslan1/cursor-ai-tips/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/murataslan1/cursor-ai-tips?style=social)](https://github.com/murataslan1/cursor-ai-tips/network/members)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Last Updated](https://img.shields.io/badge/Updated-March%2012,%202026-brightgreen)](https://github.com/murataslan1/cursor-ai-tips)
[![Cursor Version](https://img.shields.io/badge/Cursor-2.6-blue)](https://cursor.com/changelog)

**The ultimate guide to mastering Cursor AI IDE**

*Automations, Agentic Engineering workflows, Max Mode pricing, and benchmarks for GPT-5.4 vs Claude Opus 4.6 vs DeepSeek V4 Lite*

[⚠️ Max Mode Alert](#-max-mode-pricing-alert-march-16-2026) • [🆕 Cursor 2.6](#-whats-new-in-cursor-26-march-2026) • [🆕 Cursor 2.4](#-whats-new-in-cursor-24-february-2026) • [⚔️ 2026 Models](#-2026-model-landscape) • [🎭 PlayWhite](#-playwhite-workflow) • [Shortcuts](#-keyboard-shortcuts) • [Composer](#-composer-mode) • [MCP](#-mcp-integration) • [Enterprise](#-enterprise-features) • [📅 Weekly Updates](docs/weekly-updates/)

</div>

---

> [!CAUTION]
> **🚨 CRITICAL: Revert Bug Active in Cursor 2.4.x - 2.6.x**
> 
> A **file locking conflict** between Agent Review Tab and the editor causes code changes to silently revert. Cursor team confirmed 3 root causes in March 2026: Agent Review conflict, Cloud Sync conflict, and Format On Save conflict.
> 
> **Workaround**: Close the **Agent Review Tab** before using "Fix in Chat". Exclude project from cloud sync (OneDrive/iCloud). Disable "Format On Save". Use defensive commits. [Read the Revert Bug Guide →](tips/zombie-revert-bug.md)

---

> [!WARNING]
> **💰 MAX MODE PRICING ALERT (March 16, 2026)**
> 
> Starting March 16, GPT-5.4, GPT-5.3 Codex, Claude Opus 4.6, **Claude Sonnet 4.6**, and Claude Opus 4.5 move to **Max Mode** — dynamic token-based billing instead of request-based. This is a significant price increase for heavy users. Consider DeepSeek V4 Lite via OpenRouter for budget tasks. [Read the full analysis →](tips/cursor-26-features.md)

---

## Why Cursor?

> 💰 **December 2025**: Anysphere (Cursor's parent company) valued at **$29.3 billion** after Series D funding, reflecting the explosive adoption of AI-assisted development.

Cursor is not just VS Code with AI - it's a **fork** that integrates LLMs directly into the rendering pipeline. This enables:

- **Cursor Tab**: Multi-line predictions (not just single line like Copilot)
- **Composer**: Autonomous multi-file editing agent
- **Shadow Workspace**: Background indexing for semantic search
- **Native Diffs**: Inline green/red diff visualization

---

## 🆕 What's New in Cursor 2.0/2.1

### Plan Mode (2.1)
Strategic thinking before coding. AI analyzes, plans, asks clarifying questions - then executes.

```
"Plan Mode forces 'measure twice, cut once' philosophy"
```

### Instant Grep (2.1)
Millisecond codebase search. No more context hallucinations - agent verifies every reference instantly.

### Multi-Agent Interface (2.0)
Run parallel agents using git worktrees:
- Agent 1: Refactoring component
- Agent 2: Writing tests
- No file lock conflicts

### Composer Improvements
- 4x faster than general LLMs for diff-edit loops
- Codebase-wide semantic search
- Implicit checkpoints for instant rollback

[→ Full 2.0/2.1 Guide](tips/cursor-2x-features.md)

### ⚠️ Deprecated Features

Some features were removed in 2.0/2.1:

| Removed | Replacement |
|---------|-------------|
| Interpreter Mode | Agent + Terminal |
| @Web, @Definitions | Auto-context |
| Reapply Button | Checkpoints |
| .cursorrules | .mdc files |
| Fast Request Packs | Usage-based pricing |

[→ Full Deprecated Features Guide](tips/deprecated-features.md)

### Lovable + Cursor Workflow

Popular "vibe coding" pattern for rapid prototyping:

```
1. Lovable → Design UI visually, connect to GitHub
2. Clone → Pull repo to local
3. Cursor → Add backend logic, APIs, complex features
4. Push → Sync back to Lovable
```

Users report building full SaaS products in 4 days using this hybrid approach.

[→ Full Lovable + Cursor Guide](tips/lovable-cursor-workflow.md)

---

## 🆕 What's New in Cursor 2.6 (March 2026)

> 🎯 **"The Automation Release"** — Cursor 2.6 introduces always-on, event-driven agents (Automations), Team Plugin Marketplaces, and a controversial shift to Max Mode pricing.

### Cursor Automations (GA)

The headline feature: agents that work autonomously via **triggers**, even when you're away from your computer.

| Trigger | Source | Example |
|---------|--------|---------|
| **GitHub PR** | Push, Open, Review | Auto code review on new PRs |
| **Slack Webhook** | Message, Thread | Create JIRA task from Slack |
| **Linear Issue** | Created, Updated | Auto-implement assigned issues |
| **PagerDuty** | Incident Alert | Read logs, open fix PR |
| **Cron** | Scheduled | Run daily test suite at 6 AM |

```
Example Task: Run apidog test. If fails, create Linear ticket and ping #dev-alerts on Slack.
```

> "Cursor Automations proves we've moved from 'Assistant' to 'Autonomous Worker' era." — Reddit (r/cursor), 245 upvotes

### Team Marketplaces for Plugins

Create private, internal plugin marketplaces for Teams & Enterprise plans. Distribute team-specific **MCP servers** and internal tools via private GitHub repos.

### Max Mode Pricing (Effective March 16)

Frontier models (GPT-5.4, GPT-5.3 Codex, Claude Opus 4.6, Claude Sonnet 4.6, Claude Opus 4.5) move to **dynamic token-based billing**. Pro plan's 500 fast requests will be consumed much faster.

**Budget strategy:** Use DeepSeek V4 Lite via OpenRouter for 80% of daily work.

### New Model: DeepSeek V4 Lite

| Field | Details |
|-------|---------|
| **Codename** | "0302" / "Healer Alpha" |
| **Parameters** | ~200B |
| **Context** | 1M tokens |
| **Cost** | 1/10 to 1/50 of GPT models |

Stealth-launched March 9. Popular via OpenRouter integration. Competes with frontier models at a fraction of the cost.

### Linux (Ubuntu/GNOME) Crash Fix

Ubuntu 24.04 Wayland/GNOME users: corrupted Cursor config crashes the desktop session.

```bash
rm -rf ~/.config/Cursor  # Run from TTY/recovery mode
```

[→ Full Cursor 2.6 Guide](tips/cursor-26-features.md)

---

## 🆕 What's New in Cursor 2.4 (February 2026)

> 🎯 **"The Agentic Engineering Release"** — Cursor 2.4 marks the shift from "AI assistant" to "autonomous engineer" with Long-Running Agents, Subagents, and Composer 1.5.

### Long-Running Agents (Research Preview)

Available for Ultra, Teams & Enterprise users since Feb 12, 2026. Agents can now plan and execute tasks **for hours** without human intervention.

- **Plan-First Architecture**: Agents perform full dependency analysis before making any changes — no more "chat and fix" loops
- **Cross-Module Awareness**: Agents scan all inter-module relationships to predict side-effects before editing
- **PR-Quality Output**: Tests, docs, and refactoring delivered as a single atomic operation — fewer follow-up fixes

### Subagents (Specialized Workers)

The main agent decomposes tasks into specialized subagents:

```
Main Agent
├── Terminal Subagent → Runs commands
├── Docs Subagent → Scans documentation
├── Test Subagent → Runs & writes tests
└── Refactor Subagent → Code changes
```

Parallel processing significantly reduces development time for complex features.

### Composer 1.5

A new distilled model optimized for code synthesis, positioned as a cost-effective alternative to Claude Opus 4.6:

| Aspect | Composer 1.5 | Claude Opus 4.6 |
|:-------|:-------------|:----------------|
| Speed | **30% faster** | Baseline |
| Refactoring | Excellent | Excellent |
| Abstract Planning | Good | **Superior** |
| Cost | **50% discount** | $$$ |

> ⚠️ **"Auto-Mode Anxiety"**: Users report confusion about how credits are consumed in Auto mode. API costs vs. subscription pool credits lack transparency.

### Revert Bug (v2.4.x) — Still Active

A **file locking conflict** between Agent Review Tab and the editor window:

| Symptom | Cause |
|:--------|:------|
| Code appears then reverts | Race condition between Review Tab (read-only) and Chat agent (write) |
| `git diff` shows changes but editor shows old code | IDE cache not synced with disk |

**Workaround**: Close Agent Review Tab before "Fix in Chat". Disable Format On Save.

[→ Full 2.4 Guide](tips/cursor-24-features.md)

---

---

## ⚔️ 2026 Model Landscape

The AI coding landscape reached peak competition in March 2026. The era of **"Agentic Engineering"** replaces "Vibe Coding" — engineers now orchestrate agents rather than write code.

> ⚠️ **March 16, 2026:** Frontier models move to Max Mode (token-based billing). Budget accordingly.

| Tier | Model | Best For | Cost | Context |
| :--- | :--- | :--- | :--- | :--- |
| **Senior Architect** | **Claude Opus 4.6** | Deep reasoning, multi-file refactoring (SWE-bench: 80.8%) | $$$ (Max Mode) | 1M |
| **New Contender** | **GPT-5.4** | Best overall reasoning, versatile | $$$ (Max Mode) | 1M+ |
| **10x Implementer** | **GPT-5.3 Codex** | Speed, one-shot features, Terminal-Bench leader | $$ (Max Mode) | ~1M |
| **Cost-Effective** | **Composer 1.5** | Code synthesis, refactoring (50% cheaper, still in Pro) | $ | N/A |
| **Open-Source King** | **DeepSeek V4 Lite** | Budget, local/privacy, 200B params (1/50th cost) | ¢ | 1M |
| **Analyst** | **Gemini 3.1 Pro** | Massive codebase reading, visual analysis | $ | 2M |

[→ Full 2026 Model Guide](docs/models-2026.md) | [→ 2026 Best Practices Rules](rules/cursorrules-2026-best-practices.md)

---

## 🎭 "PlayWhite" Workflow (New Trend)

The viral **Playwright + MCP** workflow for self-healing tests.
*   **What:** Connect Playwright to Cursor via MCP.
*   **Why:** Agent runs tests → Fails → Fixes code → Verify.
*   **Result:** Test-Driven Development on Autopilot.

[→ Full "PlayWhite" Guide](tips/playwhite-workflow.md)

---

## 🆕 What's New in Cursor 2.3 (December 2025)

> 🎯 **"The Stability Release"** - Cursor 2.3 focuses entirely on fixing the "Agent Hang" and "Zombie Revert" bugs that plagued version 2.2.

### Key Fixes
- **Agent Stability**: Fixed issues where Composer would freeze mid-generation.
- **Layout Controls**: New panel positioning system is now production-ready.
- **Diff View**: Critical fixes to the diff application logic.

> **Recommendation**: Upgrade to 2.3. The release focuses specifically on fixing stability issues like the "Agent Hang" and diff application bugs from 2.2.

### Process Separation (The Big Change)

Extensions now run in an isolated process. If an extension crashes, **AI keeps working**:

```
Before: Extension crash → Everything freezes
After:  Extension crash → AI continues working ✅
```

This is critical for enterprise users with large codebases.

### Layout Customization Engine

Four preset layouts with `⌘+⌥+⇥` (Mac) / `Ctrl+Alt+Tab` (Win):

| Mode | Description | Best For |
|:-----|:------------|:---------|
| **Agent** | 50/50 Chat + Editor | Pair programming with AI |
| **Editor** | Maximized editor | Deep focus |
| **Zen** | Hidden chrome | Complex algorithms |
| **Browser** | Split with Chromium | Frontend dev |

### Enterprise Features

- **Service Accounts** - Headless CI/CD automation
- **SOC 2 Certified** - Enterprise compliance ready
- **Enforcement Hooks** - Block sensitive data in prompts
- **Linux Sandboxing** - Container-friendly deployments

[→ Full 2.3 Guide](tips/cursor-23-features.md) | [→ Enterprise Features](tips/enterprise-features.md)

---

## 🚨 Critical: Revert Bug (v2.4.x)

> ⚠️ **DATA LOSS WARNING**: Active in Cursor 2.4.x. A file locking conflict between Agent Review Tab and editor.

### What Happens

- AI writes changes to disk (`git diff` confirms), but IDE cache shows old code
- "Fix in Chat" while Agent Review Tab is open causes a **race condition** — new code gets overwritten
- Risk of committing stale code without realizing

### Safety Protocol (February 2026)

| ❌ DO NOT | ✅ SAFE TO DO |
|:----------|:-------------|
| Use "Fix in Chat" with Review Tab open | Close Review Tab first |
| Trust editor view without `git diff` | Verify with `git diff` after every agent op |
| Use Format On Save with agents | Disable Prettier/formatters during agent sessions |
| Run multiple agents on same files | Use sequential agents or separate branches |

### Defensive Commit (Critical)

```bash
# BEFORE every agent operation:
git add -A && git commit -m "pre-agent-$(date +%s)"
```

[→ Full Revert Bug Guide](tips/zombie-revert-bug.md) | [→ Windows Terminal Fixes](tips/windows-terminal-fixes.md)

---

## 🧠 Gemini 3 Pro Guide

> 🏆 **HLE Benchmark Leader**: 37.5% - Best reasoning performance ever recorded.

### Model Comparison (February 2026)

| Model | SWE-bench | Best For | Cost |
|:------|:----------|:---------|:-----|
| **Claude Opus 4.6** | **80.8%** | Deep reasoning, multi-file refactoring, legacy migration | $$$ |
| **GPT-5.3 Codex** | High | Speed (30% faster than Opus), one-shot features | $$ |
| **Composer 1.5** | — | Code synthesis, refactoring (distilled, 50% cheaper) | $ |
| **Gemini 3 Pro** | — | Architecture, reasoning, codebase indexing | Free (Beta) |
| **DeepSeek V3.2** | — | Budget, local/privacy, open-source (1/50th cost) | ¢ |

### New Model Strategy (Feb 2026)

```
Architecture Planning  → Claude Opus 4.6 (Best reasoning, 1M context)
Daily Implementation   → Composer 1.5 (Fast, 50% cheaper)
Speed-Critical Tasks   → GPT-5.3 Codex (30% faster execution)
Legacy Refactoring     → Claude Opus 4.6 (91% legacy migration success)
Local/Privacy          → DeepSeek V3.2 via Ollama (local-first)
Budget Bulk Work       → DeepSeek V3.2 (50x cheaper)
```

### Configure Gemini for Codebase Indexing

```
Settings → Codebase Indexing → Model → Gemini 3 Pro
```

[→ Full Gemini 3 Pro Guide](tips/gemini-3-pro-guide.md)

---

## 🆕 What's New in Cursor 2.2


> ⚠️ **WARNING**: Cursor 2.2 has critical bugs. See [Cursor 2.2 Bugs](tips/cursor-22-bugs.md) before using.

### Debug Mode (2.2)

Agent instruments your code with logging, you trigger the bug, agent analyzes runtime data for empirical debugging.

```
1. Describe bug → 2. Agent adds logging → 3. YOU trigger bug → 4. Agent analyzes → 5. Fix proposed
```

### Visual Editor (2.2)

Bidirectional DOM ↔ Source Code editing. Select elements in browser, modify via GUI, changes write to source files.

### Multi-Agent Judging (2.2)

Multiple agents solve your prompt in parallel. "Judge" agent picks the best solution. Increases token cost but improves quality.

### ⚠️ Critical Bugs in 2.2

| Bug | Impact | Workaround |
|-----|--------|------------|
| **Revert Broken** | Data loss! | Git commit before every agent call |
| **Visual Editor Loop** | Infinite re-apply | [Avoid 'Visual' tab](tips/visual-editor-bug.md) |
| **WSL Terminal** | Agent can't run commands | Enable Legacy Terminal |

[→ Full 2.2 Features Guide](tips/cursor-22-features.md) | [→ 2.2 Bugs & Workarounds](tips/cursor-22-bugs.md)

---

## ⌨️ Keyboard Shortcuts

### The Command Hierarchy

| Command | Mac | Windows/Linux | Scope | When to Use |
|---------|-----|---------------|-------|-------------|
| **Inline Edit** | `Cmd + K` | `Ctrl + K` | Single file | Quick fixes, rename, split function |
| **Chat** | `Cmd + L` | `Ctrl + L` | Conversational | Explain code, debug, explore |
| **Composer** | `Cmd + I` | `Ctrl + I` | Multi-file | Refactoring, new features |
| **Composer Full** | `Cmd + Shift + I` | `Ctrl + Shift + I` | Multi-file | Large refactors, review diffs |
| **Add to Context** | `Cmd + Shift + L` | `Ctrl + Shift + L` | Selection | Add selected code to chat |
| **Terminal AI** | `Cmd + K` (in terminal) | `Ctrl + K` | Shell | Generate shell commands |

### Quick Reference

```
Cmd + K  → "Fix this type error"
Cmd + L  → "Explain how auth works"  
Cmd + I  → "Refactor to use Axios instead of Fetch"
```

> **Pro Tip**: Use `Cmd + K` for local scope, `Cmd + I` for global scope. Don't use `Cmd + K` for multi-file tasks.

[→ Full Shortcuts Guide](tips/keyboard-shortcuts.md) | [→ Development Workflows](tips/workflows.md)

---

## 🤖 Composer Mode

Composer is Cursor's **killer feature** - an autonomous agent that can plan and execute multi-file edits.

### Normal vs Agent Mode

| Mode | Description | Risk Level |
|------|-------------|------------|
| **Normal** | Proposes edits, you click "Accept" | Safe |
| **Agent** | Creates/deletes files, runs terminal | ⚠️ Use with caution |

### Checkpoints (Time Travel)

Composer creates snapshots at each step. If the AI breaks something:

1. Click previous Checkpoint
2. Workspace reverts instantly
3. Try different approach

### Effective Prompting

❌ **Bad**: "Add a login page"

✅ **Good**:
```
Implement a login route:
- @user_model.ts @auth_service.ts @routes.json
- Use Zod for validation
- Match error format in @errors.ts
- Create unit test in tests/auth/
```

[→ Full Composer Guide](tips/composer-mode.md)

---

## 📎 Context Management

The AI is only as good as the context you provide.

### @ Symbol Reference

| Symbol | What it does | Best for |
|--------|--------------|----------|
| `@Files` | Full file content | Active editing |
| `@Folders` | File tree + summaries | Architecture questions |
| `@Codebase` | Semantic RAG search | "Where is X used?" |
| `@Docs` | External documentation | Third-party APIs |
| `@Git` | Git history/diff | Commit messages, history |
| `@Web` | Web search | Current info |

### Pro Tips

```
@Codebase is probabilistic - if you call it "Login" 
but code says "SessionCreation", RAG may fail.

Use explicit @Files for critical tasks.
```

### Notepads (Persistent Context)

Create a `current_task_spec` Notepad with:
- PRD / Requirements
- Design constraints
- Architecture decisions

Reference with `@current_task_spec` in every new chat.

[→ Full Context Guide](tips/context-management.md) | [→ Security Best Practices](tips/security-concerns.md)

---

## 📋 .cursorrules

System prompts that customize AI behavior per project.

### Basic Setup

Create `.cursorrules` in project root:

```
You are an expert TypeScript engineer.
Use functional components with Hooks.
Use Tailwind CSS for styling.
Never use CSS modules or styled-components.
Every function needs a unit test.
```

### Advanced: .mdc Files

New system uses `.cursor/rules/*.mdc` with glob patterns:

```yaml
---
description: "React Component Rules"
globs: ["src/**/*.tsx"]
alwaysApply: false
---

Use shadcn/ui for primitives.
Components in src/ui must be presentational only.
Business logic goes in src/services.
```

### Essential Rules

| Category | Example Rule |
|----------|--------------|
| **Tech Stack** | "Use Tailwind. Never styled-components." |
| **Architecture** | "Services in src/services, UI in src/ui" |
| **Anti-Lazy** | "Output FULL file. No placeholders. No `//...existing code`" |
| **Testing** | "Every function needs unit test in tests/" |

### The Anti-Lazy Prompt (Reddit Gold)

```
You are an expert engineer.
You DO NOT use placeholders.
You output the FULL content of the file every time.
You do not be lazy.
```

[→ Full .cursorrules Guide](tips/cursorrules-guide.md) | [→ .mdc Examples](tips/mdc-examples.md)

---

## 🧠 Model Selection (February 2026 Update)

### Latest Models Comparison

| Model | Best For | Context | Speed | Cost |
|-------|----------|---------|-------|------|
| **Claude Opus 4.6** | Deep reasoning, legacy migration, multi-file refactoring | **1M** | Medium | $$$ |
| **GPT-5.3 Codex** | Speed, one-shot features, tool orchestration | ~1M | **Fast** | $$ |
| **Composer 1.5** | Code synthesis, refactoring (distilled) | — | **Fast** | $ |
| **Gemini 3 Pro** | Visuals, massive context, codebase indexing | **2M** | Fast | $ |
| **DeepSeek V3.2** | Budget, local/privacy, open-source | Large | Medium | ¢ |
| **DeepSeek V4** *(coming soon)* | Expected to rival Opus 4.6 in reasoning | TBD | TBD | ¢ |

> 🆕 **Claude Opus 4.6** (Feb 2026): SWE-bench 80.8%, 1M context with "Adaptive Thinking", 99.3% tool orchestration score. Dominant in telecom benchmarks.
> 
> 🆕 **GPT-5.3 Codex** (Feb 2026): 30% faster than Opus 4.6, excellent one-shot feature implementation.
> 
> 🆕 **Composer 1.5** (Feb 2026): Cursor's own distilled model. 50% cheaper, optimized for code synthesis.

### Model Personalities

| Model | "Vibe" |
|-------|--------|
| Claude Opus 4.6 | Senior Architect (Unmatched reasoning) |
| GPT-5.3 Codex | 10x Implementer (Speed demon) |
| Composer 1.5 | Efficient Specialist (Cost-effective) |
| Gemini 3 Pro | Creative Designer |
| DeepSeek V3.2 | The Disruptor (Open-source champion) |

### The Plan-Act Pattern (Updated for 2.4)

```
1. PLAN (Claude Opus 4.6 — Long-Running Agent):
   "Analyze request. Scan all dependencies. Create plan.md"
   
2. CRITIQUE (Gemini 3 Pro - optional):
   "Review plan.md for efficiency gaps"
   
3. EXECUTE (Composer 1.5 / GPT-5.3 Codex — Subagents):
   "Implement Step 1 of plan.md. Run tests. Deliver as atomic PR."
```

### Cost Optimization (Feb 2026)

```
Pro Plan ($20/mo):
├── Credit pool system (fast vs slow)
├── "Auto" mode switches models by task complexity
├── ⚠️ "Auto-Mode Anxiety" — unclear credit consumption
└── Set per-user spending limits (Enterprise)

Strategy:
├── Daily work → Composer 1.5 (50% cheaper, fast)
├── Heavy refactoring → Claude Opus 4.6 (BYOK)
├── Speed-critical → GPT-5.3 Codex
├── Budget/privacy → DeepSeek V3.2 via Ollama (local)
└── Hard bugs → Claude Opus 4.6 (deep reasoning)
```

> **Warning**: Don't switch models mid-conversation. It breaks the "train of thought."

[→ Full Model Guide](tips/model-selection.md)

---

## 🔌 MCP Integration

Model Context Protocol lets Cursor connect to databases, GitHub, and browsers.

### Quick Setup

Create `mcp.json` in project root:

```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "${env:DATABASE_URL}"]
    }
  }
}
```

### Popular Servers

| Server | Use Case |
|--------|----------|
| `server-postgres` | Query database schema |
| `github-mcp-server` | Manage PRs/Issues |
| `server-puppeteer` | Browser automation |
| `@playwright/mcp` | E2E testing, self-healing tests |
| `@sentry/mcp-server` | Production error debugging |

### Playwright Integration (Self-Healing Tests)

The most transformative MCP application:

```
1. Agent runs E2E test
2. Test fails (selector changed)
3. Agent analyzes DOM
4. Agent fixes test automatically
5. Agent verifies fix
```

[→ Full MCP Guide](tips/mcp-integration.md)

---

## 🔒 Security Concerns

> ⚠️ As AI agents gain autonomy, security risks increase exponentially.

### The Agentic Attack Surface

The ability of an Agent to execute shell commands and connect to the internet (via MCP) introduces new risks:

| Risk | Description |
|------|-------------|
| **Prompt Injection** | Malicious READMEs or docs that trick the AI |
| **Credential Exfiltration** | Agent accessing environment variables |
| **MCP Exploits** | Malicious MCP servers hijacking machines |
| **YOLO Mode Dangers** | Auto-execution of destructive commands |

### Security Best Practices

```
✅ Review all terminal commands before approval
✅ Use read-only MCP configurations
✅ Audit .mdc files in cloned repositories
✅ Never approve `env` or `printenv` commands
✅ Set strict YOLO mode restrictions
❌ Don't trust arbitrary @Docs sources
❌ Don't enable unrestricted shell access
```

### The "Black Box" Risk

```
⚠️ "Vibe Coding" can create unmaintainable code

If you don't understand the AI-generated code:
- You can't debug it when AI fails
- It becomes "Legacy Code" immediately
- Security vulnerabilities go unnoticed
```

[→ Full Security Guide](tips/security-concerns.md)

---

## 🔧 Troubleshooting

### Quick Fixes

| Problem | Solution |
|---------|----------|
| "Connection Failed" | New chat (Cmd+L), disable HTTP/2 |
| "Stuck Generating" | New Composer (Cmd+N) |
| Files deleted by Agent | Use checkpoint to restore |
| Rules ignored | Restart Cursor |
| High token usage | Set API spending limits |

### The "Single Purpose Composer" Rule

Don't reuse Composer windows. One task = one Composer. Prevents context pollution.

### Always Commit Before Agent

```bash
git add -A && git commit -m "checkpoint"
```

[→ Full Troubleshooting Guide](tips/troubleshooting.md)

---

## 🔥 Reddit Community Wisdom

Tips from r/cursor power users:

### The "Fresh Chat" Rule

> If debugging exceeds ~20 messages, context is polluted. Start NEW chat with summary.

### The "Delete Bug"

> In Agent mode, Cursor sometimes deletes and recreates files instead of editing. **Always commit before Agent sessions.**

### Screenshot Debugging

> Paste UI bug screenshots directly into chat. Vision models diagnose CSS issues better than text descriptions.

### Cost Control

> Set hard limits in OpenAI/Anthropic dashboard. Runaway Agent loops can drain your credit card.

### Model Switching

> Don't switch from GPT-4o to Claude mid-task. Stick to one model per conversation.

[→ Full Reddit Tips](tips/common-mistakes.md)

---

## 🔄 Workflows

### Research-First Protocol

```
1. Discovery: "Map usage of User component" (no code yet)
2. Plan: "Propose refactor plan, list affected files"
3. Critique: Review plan, challenge assumptions
4. Execute: Open Composer, paste approved plan
5. Audit: Review git diff line-by-line
```

### TDD with AI

```
1. "Write Vitest test for compound interest calculator"
2. Review test logic
3. "Now write function to pass this test"
```

### Debug with AI

```
1. Command fails in terminal
2. Click "Debug with AI" button
3. AI gets full error context automatically
4. Don't manually copy-paste errors
```

[→ Full Workflows Guide](tips/workflows.md)

---

## ⚔️ Cursor vs Competitors (March 2026)

| Feature | Cursor 2.6 | Google Antigravity | Windsurf (Wave 14) | Amazon Kiro |
|---------|------------|-------------------|----------|-------------|
| **Philosophy** | Advanced Editor + Automations | Full Autonomy (Agent-First) | Parallel Agent Flow | Spec-Driven Development |
| **Architecture** | Fork (Native) | New IDE (Cloud) | Fork (Cognition) | New IDE (AWS) |
| **Killer Feature** | Automations + Composer | Artifact Generation | Arena Mode (A/B) | Requirements.md (EARS) |
| **Model Choice** | All models (Max Mode for frontier) | Gemini + Anthropic (capped 40%) | Proprietary | Amazon Kira |
| **Price** | $20/mo (↑ Max Mode for frontier) | Free Preview (⚠️ quota issues) | $15/mo | AWS Ecosystem |
| **Biggest Issue** | Revert Bug + Max Mode pricing | "Paperweight" Quota Crisis | Aggressive Rate Limits | Poor code generation |
| **Status** | ✅ Market leader | ⚠️ Trust crisis deepens | ⚠️ Migration target | 🆕 New entrant |

### Amazon Kiro: The Spec-Driven Alternative (NEW)

Born as a reaction to "Vibe Coding" chaos. Instead of writing code, you write **requirements**.

```
1. You write → requirements.md (EARS format)
2. Kiro generates → design.md (with Mermaid diagrams)
3. Kiro generates → tasks.md
4. Agents write code following the "contract"
```

> "Philosophy is great, UI is beautiful, but Amazon's model (Kira) doesn't follow specs reliably. We're using it as a code reviewer, not a code writer." — YouTube Benchmark Tests

### Cursor vs Google Antigravity (March 2026 Update)

| Aspect | Cursor | Antigravity |
|--------|--------|-------------|
| **Control** | Developer is pilot + Automations | Developer is mission controller |
| **Verification** | Git diffs, code review | Artifacts (screenshots, logs) |
| **Best For** | Precision, existing codebases | ~~Greenfield, rapid prototyping~~ ⚠️ Quota crisis |
| **Lock-in** | Model agnostic | Google ecosystem |
| **Stability** | ✅ Reliable (revert bug aside) | ❌ Silent throttling, 4-10 day cooldowns |
| **March 2026 Issue** | Max Mode pricing backlash | **Quota crisis continues**: Mass refund requests filed |

> ⚠️ **Antigravity Trust Crisis Deepens**: Google silently changed quota policies. Users report 4-10 day cooldowns. Claude Opus 4.6 capped at 40%. Agents hallucinate and enter recursive optimization loops.

### Migration Stories (March 2026)

**Cursor → Windsurf:**
> "Since Max Mode pricing was announced, my team switched to Windsurf. Their Arena Mode lets us A/B test two models side-by-side and pick the better output."

**Antigravity → Cursor:**
> "Bought Antigravity Pro but quotas silently changed from 5-hour refresh to weekly. Locked out for 4 days. Back to Cursor and Windsurf."

### Windsurf: Parallel Agents (Wave 14)

- **Arena Mode**: A/B test two models side-by-side — pick the better output
- **Parallel Agents (Cascade)**: Work on separate git branches simultaneously
- **⚠️ "Blocked" Phenomenon**: Burst token consumption from parallel agents can block users despite 85% credits remaining

**Verdict**: **Cursor** remains the **professional's choice** despite Max Mode pricing. **Automations** is the killer feature for teams. **Kiro** has the best philosophy but worst execution. **DeepSeek V4 Lite** is the budget disruptor via OpenRouter.

[→ Full Comparison](tips/vs-competitors.md) | [→ Cursor vs Windsurf Deep Dive](tips/cursor-vs-windsurf.md)

---

## 💡 From Vibe Coding to Agentic Engineering

> 🆕 **March 2026**: The era of "Vibe Coding" is officially over. Welcome to **"Agentic Engineering"** — where engineers orchestrate agents rather than write code. (Andrej Karpathy)

### The Paradigm Shift

```
2025 "Vibe Coding":    Developer describes intent → AI implements → Developer reviews
2026 "Agentic Engineering": Developer designs architecture → Agents execute autonomously → Developer supervises
```

### The New Role: Agent Orchestrator

Engineers no longer deal with syntax. Their job is now:
- **System Architecture** — Designing the blueprint agents follow
- **Data Modeling** — Defining schemas and relationships
- **Rule Codification** — Writing `.cursorrules`, `CLAUDE.md` to constrain agents
- **Quality Supervision** — Reviewing agent output, not writing code

> *"99% of code is written by agents. Humans provide high-level oversight and quality control."* — Community consensus, Feb 2026

### The Cultural Divide: "Shadow Engineers" vs "Vibe Coders" vs "Agentic Engineers"

| Type | Description | Strength | Risk |
|------|-------------|----------|------|
| **Agentic Engineer** *(new)* | Designs systems, orchestrates agents, codifies rules | Full control, scalable | Requires deep architectural knowledge |
| **Shadow Engineer** | Manages AI agents, writes PRDs, verifies output | Maintainable code | Slower iteration |
| **Vibe Coder** | Relies entirely on natural language | Rapid MVPs | "Black box" code, debugging walls |

### Context Rot (New Phenomenon)

As Long-Running Agents work for hours, their mental model drifts from reality:

```
Agent starts → Modifies files → Mental model diverges from disk state
   ↓
Agent hallucinates → Calls non-existent functions → Corrupts codebase
```

**Mitigation**: Force periodic re-indexing. Use `.cursorrules` to mandate `git diff` verification at each step.

### Essential "Constitution" Files

| File | Purpose |
|------|---------|
| `.cursorrules` / `.mdc` | Project rules, tech stack, code style |
| `CLAUDE.md` | Agent behavioral constraints |
| MCP: **Context7** | Real-time documentation access |
| MCP: **Playwright** | Self-healing E2E tests |

### Success Stories

- **Tradofire**: Solo developer shipped complex crypto trading app
- **Enterprise ERP**: Full-scale systems built in weeks using TaskMaster workflow

### The TaskMaster Workflow

```
1. Generate detailed PRD (Product Requirement Document)
2. Feed PRD to task management system
3. Agent parses PRD into individual tickets
4. Execute tickets one by one
5. Human review at each milestone
```

[→ Full Vibe Coding Guide](tips/vibe-coding-guide.md)

---

## 🧬 GPT-5.1 Codex Guide

The deployment of GPT-5.1 Codex (December 2025) introduced new capabilities and quirks.

### The "Stupidity" Paradox

The new "smart" model sometimes behaves "stupidly" due to **over-reasoning** and safety alignment:

- Over-analyzes simple requests
- Hallucinated constraints (e.g., insisting VPS is required)
- Conservative refusals on legitimate security utilities

### Model Arbitrage Strategy

```
Complex Architecture Planning → GPT-5.1 Codex Max (expensive)
Implementation Details       → Gemini 3 Pro or Claude Sonnet (cheaper)
```

### Key Insight

**Use Composer over raw chat** — Cursor's agent harness improves model behavior significantly.

[→ Full GPT-5.1 Codex Guide](tips/gpt51-codex-guide.md)

---

## 🚀 GPT-5.2 Guide

Released December 11, 2025 — OpenAI's "Code Red" response to competitors.

### Key Specs

| Variant | Context | Output | Best For |
|---------|---------|--------|----------|
| GPT-5.2 Instant | 128K | 16K | Quick edits |
| GPT-5.2 Thinking | 200K | 32K | Complex reasoning |
| GPT-5.2 Pro | **400K** | **128K** | Massive refactors |

### Benchmarks

- **AIME 2025**: 100% (math reasoning)
- **SWE-Bench Pro**: 55.6% (can solve majority of mid-level tickets)
- **Tool Reliability**: 98.7%

### Pricing

| Tier | Input/1M | Output/1M |
|------|----------|-----------|
| Standard | $1.75 | $14.00 |
| **Cached** | **$0.175** | $14.00 |

**90% discount on cached inputs** — ideal for IDE usage.

[→ Full GPT-5.2 Guide](tips/gpt52-guide.md)

---

## 🎯 Confidence Scoring (Anti-Hallucination)

A powerful technique to combat AI hallucinations:

```
"Fix this only if you are 100% confident. Tell me your confidence score."
```

This prompt bypasses the "helpful assistant" persona and accesses the model's raw probability assessment, forcing it to:

1. Re-evaluate its own logic
2. Search for actual evidence
3. Admit uncertainty instead of hallucinating

[→ Full Confidence Scoring Guide](tips/confidence-scoring.md)

---

## 🐛 Known Bugs (Feb 2026)

### CRITICAL: Revert Bug (v2.4.x)

Agent Review Tab file locking conflict causes silent code reversion. **Close Review Tab before "Fix in Chat".**

```bash
# Always verify after agent operations:
git diff
ls -la --time=modified <filename>
```

### NEW: Context Rot

Long-Running Agents lose sync between their mental model and disk state over time. Agents start calling non-existent functions.

**Mitigation**: Force periodic re-indexing. Keep agent sessions under 2 hours or add re-indexing checkpoints.

### Other Issues

| Bug | Severity | Status |
|-----|----------|--------|
| Revert Bug (Agent Review Tab conflict) | CRITICAL | Open — Workaround available |
| Context Rot (Long-Running Agents) | HIGH | New — Mitigation: re-indexing |
| Auto-Mode credit transparency | MEDIUM | Open — "Auto-Mode Anxiety" |
| Plan mode not writing files | CRITICAL | Open (since Dec 2025) |
| Context Decay | MEDIUM | Workaround: Session Reset |

[→ Full Known Bugs Guide](tips/known-bugs-dec2025.md)

---

## 🌐 Google Antigravity (⚠️ Trust Crisis — Feb 2026)

> ⚠️ **February 2026**: Antigravity experienced a catastrophic trust failure. Quota policies silently changed, agents enter infinite loops, and the Windsurf talent acquisition signals Google's desperation.

### The Quota Crisis

| Promised | Reality (Feb 2026) |
|:---------|:-------------------|
| 5-hour refresh cycle | 4-10 day cooldowns |
| Generous Pro/Ultra limits | ~90% service reduction |
| Transparent billing | Silent throttling, no notification |

Users describe this as a **"bait-and-switch"** — mass refund requests filed.

### Claude Opus 4.6 Infrastructure Collapse

Users massively preferred Opus 4.6 over Google's own Gemini models, causing:
- Unexpected compute costs for Google's backend
- Anthropic model usage capped at **40% of total pool**
- Forced redirection to Gemini 3 Pro (users call it "lobotomized")

### v2.1.4 "Logic Patch" — Made Things Worse

| Bug | Description |
|:----|:------------|
| **Hallucination Loops** | Agents wrongly assume models lack vision, autonomously switch models mid-task, lose all context |
| **Recursive Optimization** | Agents enter infinite loops "optimizing" their own code, delete human-readable code as "unnecessary complexity" |
| **File System Corruption** | Irreversible file damage from recursive optimization agents |

### Who Should Still Use Antigravity?

```
✅ Free-tier experimentation only
✅ Non-critical greenfield projects
❌ Production codebases
❌ Anything requiring reliable uptime
❌ Claude Opus 4.6 heavy usage
```

[→ Full Google Antigravity Guide](tips/google-antigravity.md)

---

## 📜 Advanced .cursorrules

Sophisticated patterns from production teams:

### The "Shout" Protocol
```
If existing code is altered, warn by shouting:
❗️SHOUT WITH LARGE LETTERS❗️
"WARNING: Modified existing function in file.ts"
```

### "Dumb" Component Enforcement
```
Presentation components must include "Dumb" in filename:
- UserProfileCardDumb.vue
- ProductListDumb.tsx
```

### Anti-Flake Testing
```
NEVER use page.waitForTimeout(5000)
ALWAYS use built-in auto-wait mechanisms
Target elements using data-testid attributes
```

[→ Full Advanced .cursorrules Guide](tips/advanced-cursorrules.md)

---

## 📋 Strategic Recommendations (March 2026)

Based on community intelligence, the Agentic Engineering paradigm, and the Max Mode pricing shift:

1. **Adopt Cursor Automations**: Set up event-driven agents for PR reviews, test runs, and incident response
2. **Prepare for Max Mode (March 16)**: Budget frontier model usage carefully — switch to DeepSeek V4 Lite via OpenRouter for routine tasks
3. **Use Context7 MCP**: Essential for preventing hallucinations — pulls real-time docs for 2000+ libraries
4. **Close Review Tab Before "Fix in Chat"**: Critical workaround for the v2.4-2.6.x Revert Bug
5. **Exclude Projects from Cloud Sync**: OneDrive/iCloud/Google Drive causes file revert conflicts
6. **Codify Your Project Constitution**: `.cursorrules`, `CLAUDE.md`, and `.mdc` files are mandatory — autonomous agents need strict rules
7. **Use "Interface Freeze" Rule**: Prevent agents from writing sprawling implementations without approval
8. **Use "Anti-Hallucination" Rule**: Force agents to verify packages exist before importing
9. **Defensive Commits**: Always checkpoint before agent operations — `git commit -m "checkpoint"`
10. **Adopt Looped Workflows**: Plan → Test → Code → Run → Fix → Repeat (not linear "Prompt → Code")
11. **Avoid Google Antigravity for Production**: Trust crisis deepens — silent throttling, unreliable quotas
12. **Watch Amazon Kiro**: Great spec-driven philosophy, but execution needs improvement — use as reviewer for now

---

## 🚀 Quick Start Path

### Beginner (Week 1)
1. Learn `Cmd + K` for inline edits
2. Learn `Cmd + L` for chat
3. Use `@Files` to add context

### Intermediate (Week 2-3)
1. Master `Cmd + I` Composer
2. Create `.cursorrules`
3. Use `@Codebase` for exploration

### Advanced (Month 2+)
1. Agent Mode with checkpoints
2. Custom `.mdc` rules per file type
3. Research-First protocol
4. BYOK API for heavy tasks

---

## 📁 Configuration Files (Copy-Paste Ready)

Ready-to-use configuration files for optimal Cursor setup:

### MCP Configuration

```json
// .cursor/mcp.json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"]
    },
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"]
    }
  }
}
```

### Defensive Settings

```json
// .cursor/settings.json
{
  "agents": {
    "auto_apply_changes": false,
    "legacy_terminal_tool": true,
    "max_turns_per_session": 40
  },
  "models": {
    "codebase_indexing": "gemini-3-pro"
  }
}
```

[→ Full MCP Config](configs/mcp.json) | [→ Full Settings](configs/settings.json) | [→ React Rules](configs/react-shipping.mdc) | [→ Test Rules](configs/testing.mdc)

---

## 🎭 Playwright Self-Healing Tests

Tests that automatically fix themselves when selectors change:

```
1. Agent runs E2E test
2. Test fails (selector changed)
3. Agent analyzes DOM
4. Agent updates selector
5. Test passes ✅
```

### Quick Setup

```bash
# 1. Create .cursor/mcp.json (see above)
# 2. Create .cursor/rules/testing.mdc
# 3. Enable auto-tools in settings
```

[→ Full Playwright MCP Guide](tips/playwright-mcp-setup.md)

---

## 📚 Resources

- [Official Docs](https://docs.cursor.com)
- [r/cursor](https://reddit.com/r/cursor)
- [Cursor Forum](https://forum.cursor.com)
- [awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules)

---

## 🤝 Contributing

Found a tip? Share it!

1. Fork this repo
2. Add your tip to relevant file
3. Include source (Reddit, Twitter, etc.)
4. Open PR

---

<div align="center">

**⭐ Star this repo if it helped you!**

Made with 💙 by [Murat Aslan](https://github.com/murataslan1)

*Last updated: March 12, 2026*

</div>

