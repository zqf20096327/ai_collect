<p align="center">
  <img src="assets/dak.png" alt="Deep Agent Kit" width="720" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Claude%20Code-Skill-5A67D8?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0wIDE4Yy00LjQxIDAtOC0zLjU5LTgtOHMzLjU5LTggOC04IDggMy41OSA4IDgtMy41OSA4LTggOHoiLz48L3N2Zz4=&logoColor=white" alt="Claude Code Skill" />
  <img src="https://img.shields.io/badge/Run-%2Fnew--dcode--agent-5A67D8?style=for-the-badge" alt="Run /new-dcode-agent" />
  <img src="https://img.shields.io/badge/Deep%20Agents-LangChain-1C7C54?style=for-the-badge" alt="LangChain Deep Agents" />
  <img src="https://img.shields.io/badge/Agents-Any%20Provider-3178C6?style=for-the-badge" alt="Agents: Any Provider" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="MIT License" />
</p>

<h3 align="center"><em>Install one skill. Type <code>/new-dcode-agent</code> in any project. Get a working agent.</em></h3>

<p align="center">
  <strong>A Claude Code skill that scaffolds a Deep Agents (LangChain) agent for you: it interviews you, then drops a ready-to-run agent into whatever project you are in.</strong><br>
  <em>Bring your own model provider: the agents it scaffolds run on any OpenAI-compatible API, with nothing hard-coded and no vendor lock-in.</em>
</p>

<p align="center">
  <a href="#quick-start">Quick Start</a> &bull;
  <a href="#what-you-can-build">What You Can Build</a> &bull;
  <a href="#the-skill-step-by-step">The Skill</a> &bull;
  <a href="#bring-your-own-provider">Providers</a> &bull;
  <a href="#faq">FAQ</a>
</p>

---

## Quick Start

Install the skill once, then run `/new-dcode-agent` in any project. Pick either install method.

### Option 1: install the skill (simplest)

```bash
git clone https://github.com/EliaAlberti/dcode-agent-kit.git
mkdir -p ~/.claude/skills
cp -r dcode-agent-kit/skills/new-dcode-agent ~/.claude/skills/
```

`/new-dcode-agent` is now available in every project.

### Option 2: install as a plugin (managed updates)

In Claude Code:

```
/plugin marketplace add EliaAlberti/dcode-agent-kit
/plugin install dcode-agent-kit@dcode-agent-kit
```

> Installed as a plugin, the skill is namespaced: invoke it as `/dcode-agent-kit:new-dcode-agent` (the manual install in Option 1 keeps the plain `/new-dcode-agent`).

### Then, in any project, run it

```
/new-dcode-agent
```

Answer a few questions. The skill shows you a plan, then writes a ready-to-run agent folder into your current project.

```
You: /new-dcode-agent

Claude: What form should this agent take?
        1. SDK program   2. dcode agent   3. both
You: 1

Claude: Name it (kebab-case):
You: release-notes

Claude: In a sentence or two, what is it for?
You: Summarise merged pull requests into release notes.

Claude: Closest flavour? custom / project / work-jira / vps-ops / personal
You: project

Claude: Can it change things, or is it read-only?
You: read-only

Claude: Here is the spec [what it will create in ./release-notes/]. Scaffold it?
You: yes

Claude: Created ./release-notes/ (agent.py + model.py + README.md), wired to your
        provider, and ran a smoke test. Run it with: cd release-notes && python agent.py
```

---

## What You Get

- **The `/new-dcode-agent` skill**: install it once, run it in any project. It interviews you and writes a complete, working agent where you are.
- **Provider-agnostic agents**: each agent it builds works with any OpenAI-compatible API (OpenAI itself, or a compatible gateway), set in one environment variable.
- **Self-contained output**: each agent is a small folder (`agent.py` + `model.py` + `README.md`) with no shared dependencies, so you can move it, commit it, or deploy it anywhere.
- **Safe by default**: an agent that can change things gets an approval gate that pauses and asks before it acts.

---

## What Are Deep Agents and dcode?

**Deep Agents** is a [LangChain](https://github.com/langchain-ai/deepagents) framework for building capable AI agents in Python. You call `create_deep_agent(...)` with a system prompt and some tools (plain Python functions), and you get an agent that can plan, use those tools, run sub-agents, and pause for your approval before risky actions.

**dcode** (the `deepagents-code` CLI) is a terminal coding agent built on that same framework. You can add **agents** to it: named identities you chat with, each with its own knowledge and rules. The built-ins are `coder` and `researcher`, and you switch with `/agents`.

This skill builds both: standalone Python agents you run or deploy, and dcode agents you chat with. You do not need to know the internals. The skill handles the wiring.

---

## What You Can Build

The skill can create three kinds of agent. You pick one when it asks.

| Form | What it is | Where it goes | Best for |
| --- | --- | --- | --- |
| **SDK program** | A standalone Python agent (`create_deep_agent`) you run, schedule, or deploy | `./<name>/` in your current project | Automation, headless jobs, anything you put on a server |
| **dcode agent** | A named identity you chat with inside the dcode CLI | `~/.deepagents/<name>/` | An interactive expert you switch into with `/agents` |
| **Both** | A dcode agent that acts as the cockpit for a deployed SDK program | both locations | A monitor you can run headless and also talk to |

An agent that can change things (restart a service, post an update, write a file) gets an **approval gate** so it pauses and asks before it acts.

---

## The Skill, Step by Step

`/new-dcode-agent` walks through four steps and never runs `git`, so committing stays your call.

```
  +----------------------------------------------------------------+
  |  1. Interview    form, name, purpose, flavour, tools,          |
  |                  model, safety                                  |
  |  2. Spec         shows you the plan and waits for your OK       |
  |  3. Scaffold     writes a self-contained agent folder into      |
  |                  your current project                          |
  |  4. Smoke-test   imports and runs it once to prove it works    |
  +----------------------------------------------------------------+
```

1. **Interview.** It asks what you want: an SDK program, a dcode agent, or both; a name; what it is for; the closest flavour; which tools and MCP servers it needs; which model; and whether it can change things (if so, it adds an approval gate).
2. **Spec.** It shows you exactly what it will create and waits. Nothing is written until you confirm.
3. **Scaffold.** It writes a self-contained agent folder (`agent.py` + a sibling `model.py` + `README.md`) into your current project, wired to your provider.
4. **Smoke-test.** It imports the new agent and runs it once. If the agent can change things, it proves the approval gate actually pauses before acting.

You end up with a working agent that already follows the safe defaults: read-only first, approval required before anything destructive.

---

## Bring Your Own Provider

Every scaffolded agent gets its model from a sibling `model.py` (`chat_model()`), which reads your settings from the environment or a `.env`. No provider is baked into the code.

| Variable | Required | What it does |
| --- | --- | --- |
| `LLM_API_KEY` | Yes | Your provider API key (`OPENAI_API_KEY` also works) |
| `LLM_BASE_URL` | No | Your provider's endpoint. Leave blank for OpenAI's default |
| `LLM_MODEL` | No | The model id to use (it must exist on your provider) |
| `USE_RESPONSES_API` | No | Set to `1` only if your provider supports the OpenAI Responses API |

Point `LLM_BASE_URL` at any OpenAI-compatible gateway and your agents run on that provider.

---

## What's Inside

| Path | What it is |
| --- | --- |
| `skills/new-dcode-agent/SKILL.md` | The skill: the whole wizard, self-contained |
| `.claude-plugin/plugin.json` | Plugin manifest (for the marketplace install) |
| `.claude-plugin/marketplace.json` | Marketplace listing for this plugin |
| `reference/deepagents-guide.md` | A concise Deep Agents and dcode reference |
| `assets/dak.png` | The banner |

---

## FAQ

<details>
<summary><strong>Where does the skill build the agent?</strong></summary>

Into your current project. Run `/new-dcode-agent` from the folder you are working in, and it writes a `./<name>/` agent folder right there. You are never locked into this repo.

</details>

<details>
<summary><strong>Do I need to clone this repo every time?</strong></summary>

No. You install the skill once (Option 1 or 2 above). After that, `/new-dcode-agent` is available in every project without cloning anything.

</details>

<details>
<summary><strong>Do I need the dcode CLI?</strong></summary>

No. The SDK agents this skill builds run on their own with just Python and your API key. dcode is only needed if you choose the **dcode agent** form, the chat-with-it identity.

</details>

<details>
<summary><strong>Which model providers work?</strong></summary>

Any provider with an OpenAI-compatible API. Set `LLM_API_KEY`, and if you are not using OpenAI, set `LLM_BASE_URL` to your provider's endpoint and `LLM_MODEL` to a model it offers. Nothing else changes.

</details>

<details>
<summary><strong>Is my API key safe?</strong></summary>

Yes. Keys are read from the environment or a `.env` at runtime. Nothing is written into the generated code, and a scaffolded agent's `README.md` reminds you to keep `.env` out of git.

</details>

<details>
<summary><strong>What is the difference between a dcode agent and an SDK program?</strong></summary>

An **SDK program** is a standalone Python agent you run or deploy (good for automation and headless jobs). A **dcode agent** is an identity you chat with interactively inside the dcode CLI. You can build either, or both together, where the dcode agent is the cockpit for a deployed program.

</details>

<details>
<summary><strong>The skill mentions an "approval gate". What is that?</strong></summary>

It is a safety pause. An agent that can change things is set up so it stops and asks for your approval before running a tool that acts (for example restarting a service). Under the hood this is the SDK's `interrupt_on` paired with a checkpointer, and the skill verifies the pause actually fires before it hands the agent over.

</details>

---

## Credits

Created by [Elia Alberti](https://github.com/EliaAlberti). Built with and for [Claude Code](https://docs.anthropic.com/en/docs/claude-code) and [LangChain Deep Agents](https://github.com/langchain-ai/deepagents).

---

## License

MIT. See [LICENSE](LICENSE).
