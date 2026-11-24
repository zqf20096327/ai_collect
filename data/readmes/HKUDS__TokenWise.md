<div align="center">

<h1>
  <img src="docs/assets/logo.svg" width="48" height="48" align="absmiddle" alt="">
  TokenWise: Self-Evolving Context with <br> Up to 50% Token Savings
</h1>

<p>
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-0A7A69?style=flat-square&labelColor=071E1B"></a>
  <img alt="Agents: 9 and any shell" src="https://img.shields.io/badge/agents-9_%2B_any_shell-0A7A69?style=flat-square&labelColor=071E1B">
  <a href="https://github.com/HKUDS/.github/blob/main/profile/README.md"><img src="https://img.shields.io/badge/Feishu-Group-E9DBFC?style=flat-square&logo=feishu&logoColor=white" alt="Feishu"></a>
  <a href="https://github.com/HKUDS/.github/blob/main/profile/README.md"><img src="https://img.shields.io/badge/WeChat-Group-C5EAB4?style=flat-square&logo=wechat&logoColor=white" alt="WeChat"></a>
</p>

**English** · [简体中文](docs/zh/README.md)

</div>

<p align="center"><img src="media/images/savings.png" alt="Algorithm development and debugging (iterative bug fixing and algorithm improvement): up to 38% fewer tokens. Long-horizon software engineering (system-level engineering across large multi-module codebases): up to 50% fewer tokens. Large-context Q&amp;A (deep reasoning over long documents and histories): up to 45% fewer tokens. Self-evolution unlocks more savings: TokenWise learns from real workflows and reduces token usage by an additional 27% over time." width="100%"></p>

## Why TokenWise?

**The Problem: AI agents pay for every token they read—even the ones they do not need.**

- 🗑️ **Redundant and irrelevant tokens**
  - Repeated instructions, logs, and tool outputs
  - Outdated information that distracts the agent

- 📈 **Growing token costs**
  - Context expands with every interaction
  - Each turn pays to process the accumulated history again

- 🧠 **No self-evolving context**
  - Fixed rules cannot learn from changing workflows
  - Each agent starts over instead of reusing what works

---

### The TokenWise Approach

- ✂️ **Read less. Keep what matters.**  
  Remove noise before it reaches the model while preserving task-critical context.

- 🧠 **Evolve with every workflow.**  
  Learn from real usage and adapt to new tools, commands, and context.

- 🔄 **Learn once. Improve every agent.**  
  Share proven optimization strategies across agents and platforms.

- 📊 **See every token saved.**  
  Track per-response and cumulative savings in real time.

## 🤖 Drop-In Plugin for the Agents You Already Use

<table width="100%">
  <tr>
    <td align="center" width="16%"><img src="media/agents/claude-code.svg" width="48" height="48" alt=""><br><strong>Claude Code</strong></td>
    <td align="center" width="16%"><img src="media/agents/codex.svg" width="48" height="48" alt=""><br><strong>Codex</strong></td>
    <td align="center" width="16%"><img src="media/agents/copilot.svg" width="48" height="48" alt=""><br><strong>GitHub Copilot CLI</strong></td>
    <td align="center" width="16%"><img src="media/agents/hermes.svg" width="48" height="48" alt=""><br><strong>Hermes Agent</strong></td>
    <td align="center" width="16%"><img src="media/agents/opencode.svg" width="48" height="48" alt=""><br><strong>OpenCode</strong></td>
    <td align="center" width="16%"><img src="media/agents/codebuddy.svg" width="48" height="48" alt=""><br><strong>CodeBuddy</strong></td>
  </tr>
  <tr>
    <td align="center" width="16%"><img src="media/agents/grok.svg" width="48" height="48" alt=""><br><strong>Grok Build</strong></td>
    <td align="center" width="16%"><img src="media/agents/dsh.svg" width="48" height="48" alt=""><br><strong>DeepSeek Harness</strong></td>
    <td align="center" width="16%"><img src="media/agents/pi.svg" width="48" height="48" alt=""><br><strong>pi</strong></td>
    <td align="center" width="16%"><img src="media/images/icons/agent-shell.png" width="48" height="48" alt=""><br><strong>Any shell</strong></td>
    <td align="center" width="16%"><a href="#whats-next"><img src="media/images/icons/agent-more.png" width="48" height="48" alt=""><br><strong>More coming</strong></a></td>
  </tr>
</table>


## 🪙 See How Much TokenWise Saves

**Every response shows the tokens saved and the reduction percentage—directly inside your agent.**

<p align="center"><img src="media/images/cards.png" alt="The card at the end of an answer in Claude Code, Codex, GitHub Copilot CLI, Hermes Agent, OpenCode, CodeBuddy, Grok Build, DeepSeek Harness and pi" width="100%"></p>

<sub>Results are based on one real-world run with each agent.</sub>

## 🚀 Get Started

### Install with Your Agent - Recommended

Paste the following into your agent:

```bash
Install TokenWise for every supported agent on this machine and verify that each integration works.

Repository: https://github.com/HKUDS/TokenWise
```

TokenWise starts working with your next command—no configuration required.

To add custom optimization rules, invoke TokenWise from your agent:

```bash
/tokenwise          # Claude Code and other supported agents
$tokenwise          # Codex
@tokenwise          # OpenCode and DeepSeek Harness
/skill:tokenwise    # pi
```

### Install Manually

Requirements: **Node.js 22** and **pnpm**.

```bash
# Clone and build TokenWise
git clone https://github.com/HKUDS/TokenWise.git
cd TokenWise
pnpm install
pnpm build

# Install the CLI globally
npm install -g ./packages/cli

# Detect your agents and install TokenWise
tokenwise setup

# Verify every agent integration
tokenwise doctor --probe
```

<p align="center"><a href="https://youtu.be/9p36ZR2rNtE"><img src="media/video/promo.gif" alt="TokenWise in nine agents: noise turns into coins, every answer ends with what was saved, and the savings grow through the week" width="100%"></a></p>
<p align="center"><sub>▶ <a href="https://youtu.be/9p36ZR2rNtE">Watch the video on YouTube</a> · 35 seconds</sub></p>

Available on **macOS and Linux**. Integration depth varies by agent; see [connection details](#how-each-agent-is-connected).

## What’s Next
- **More agents** — Cursor, Gemini CLI, Kimi Code, and more.
- **Shared context learning** — Transfer proven context strategies across agents.
- **Task-aware context** — Adapt context for coding, research, and long-running tasks.
- **Context observability** — Show what is removed, retained, and why.
- **Performance-aware optimization** — Save more tokens while preserving task-critical context.

## Agent-Readable Setup & Integration

<details>
<summary><strong>Install by hand, agent by agent</strong></summary>
<br>

From the checkout, after `npm install -g ./packages/cli`:

```sh
pi install "$PWD/adapters/pi"                                   # pi
dsh plugin --profile web add -w "$PWD/adapters/dsh"             # DeepSeek Harness (your profile)
claude plugin marketplace add "$PWD" && claude plugin install tokenwise@tokenwise
codex plugin marketplace add "$PWD" && codex plugin add tokenwise@tokenwise    # then trust its hooks in /hooks
codebuddy plugin marketplace add "$PWD" && codebuddy plugin install tokenwise@tokenwise
grok plugin marketplace add "$PWD" && grok plugin install tokenwise@tokenwise --trust
copilot plugin marketplace add "$PWD" && copilot plugin install tokenwise@tokenwise

# OpenCode
mkdir -p ~/.config/opencode/plugins
cp adapters/opencode/dist/index.js ~/.config/opencode/plugins/tokenwise.js

# Hermes Agent
mkdir -p ~/.hermes/plugins
cp -R adapters/hermes/tokenwise ~/.hermes/plugins/tokenwise
hermes plugins enable tokenwise && hermes config set context.engine tokenwise

# The tokenwise skill, where each agent reads skills
cp -R skills/tokenwise ~/.claude/skills/            # Claude Code; likewise ~/.codebuddy/skills, ~/.grok/skills,
                                                    # ~/.config/opencode/skills, ~/.hermes/skills and ~/.copilot/skills
cp -R skills/tokenwise ~/.agents/skills/            # Codex, pi and DeepSeek Harness

# Anything else: wrap the command
tokenwise run -c 'cargo test'
```

`tokenwise setup` runs these for you; `tokenwise setup --dry-run` only prints them.

</details>

<details>
<summary><strong id="how-each-agent-is-connected">How each agent is connected</strong></summary>
<br>

| Agent | Context on demand | Learning from inside the agent |
|---|---|---|
| pi 1.1+ | in-process; TokenWise writes the compacted context | `/tokenwise` panel |
| DeepSeek Harness 0.2.x | in-process; TokenWise writes the compacted context | Plugins page, **Learn now** |
| OpenCode 1.19+ | in-process; TokenWise writes the compacted context | `tokenwise learn` |
| Hermes Agent 0.22+ | Python plugin and context engine | `tokenwise learn` |
| Claude Code 2.1+ | hooks; the catalog follows Claude's own summary | `/tokenwise:learn` |
| Codex 0.162+ | hooks; the catalog follows Codex's own summary | `$tokenwise learn` |
| CodeBuddy 2.175+ | hooks and a mod that rewrites the stored summary | `/tokenwise:learn` |
| Grok Build 1.0+ | hooks; the catalog follows Grok's own summary | `/tokenwise:learn` |
| GitHub Copilot CLI 1.0+ | hooks; shell output only (Copilot compacts with its own summary) | `tokenwise learn` |
| Any agent or shell | `tokenwise run`, recall over MCP | `tokenwise learn` |

Every agent also gets the `tokenwise` skill: `/tokenwise`, `$tokenwise` in Codex,
`@tokenwise` in OpenCode and DeepSeek Harness, `/skill:tokenwise` in pi. Each agent's folder under [`adapters/`](adapters) has the details;
[docs/adapters.md](docs/adapters.md) shows how to connect another agent.

</details>

<details>
<summary><strong>Commands</strong></summary>
<br>

| Command | What it does |
|---|---|
| `tokenwise setup [agent...]`, `uninstall [--purge]` | add TokenWise to your agents, or take it out |
| `tokenwise saved [--month\|--all]` | what TokenWise saved you, as a pixel jar in the terminal (`--json` for the numbers) |
| `tokenwise dashboard [--port N] [--no-open]` | the same jar as a page in your browser, filling as it saves |
| `tokenwise report [--host H] [--session S]` | the detailed numbers behind `saved`, per session or agent, for troubleshooting |
| `tokenwise checkup` | what it shortens, its learned rules, and the commands worth teaching it |
| `tokenwise teach "<command>"`, `teach check\|preview\|keep\|drop` | teach it one command from your own agent |
| `tokenwise preview "<command>"` | a recorded output of that command: the original and what the model reads |
| `tokenwise learn --learner L`, `learn status\|cancel` | start learning in the background, follow it, stop it |
| `tokenwise rules [list\|off\|on\|rollback]` | the learned rules |
| `tokenwise filters` | every built-in rule and what it guarantees to keep |
| `tokenwise recall <id>` | read a set-aside original back |
| `tokenwise run -c '<command>'` | run any command through TokenWise |
| `tokenwise doctor [--probe]` | whether TokenWise works in each of your agents (`--probe`: each runs one command to prove it), configuration, what each agent supports |

`tw` works in place of `tokenwise` everywhere.

</details>

<details>
<summary><strong>Configuration and privacy</strong></summary>
<br>

Nothing needs configuring. To change something, write `~/.tokenwise/config.json`;
`TOKENWISE_DISABLE=1` switches everything off for one run. Every `TOKENWISE_*`
setting can also be written `TW_*` (`TW_HOME`, `TW_DISABLE`): Codex and DSH drop
variables with TOKEN in their name from the shells they run.

Everything stays on your machine: originals are readable only by you and deleted
after 14 days. The one thing that leaves your machine is a learning round you
start yourself: the learner is your own agent, so the recorded output it reads
goes to that agent's model provider, as it did when the agent first ran the
commands. Set `"evidence": false` to record nothing.

</details>

[Architecture](docs/architecture.md) · [Adding an agent](docs/adapters.md) · [Changelog](CHANGELOG.md) · [Media kit](media/README.md) · [MIT License](LICENSE)

<sub>Icons made by <a href="https://www.magnific.com" title="Magnific">Magnific</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a>. Agent icons belong to their products; sources in <a href="media/agents/NOTICE.md">media/agents/NOTICE.md</a>.</sub>
