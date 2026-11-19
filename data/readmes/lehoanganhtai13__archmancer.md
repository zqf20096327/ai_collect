<p align="center">
  <img src="assets/banner.webp" alt="Two chibi wizards casting an agent-system architecture as a glowing magic circle while a small white dog bounces at their feet" width="100%">
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-blue.svg" alt="License: Apache-2.0"></a>
  <img src="https://img.shields.io/badge/Claude_Code-plugin-555555.svg" alt="Claude Code plugin">
  <img src="https://img.shields.io/badge/Codex-plugin-555555.svg" alt="Codex plugin">
  <img src="https://img.shields.io/badge/Agent_Skills-compatible-555555.svg" alt="Agent Skills compatible">
</p>

# Archmancer

Give your coding agent an architect's view of agent systems: software where a model chooses the next call or action on the way to an outcome. Eight skills teach it the architecture, the component contracts and the engineering process, so it maps the whole system, chooses the smallest design that meets the requirements, and traces failures to the hand-off that caused them.

**Claude Code**

```
/plugin marketplace add lehoanganhtai13/archmancer
/plugin install archmancer@archmancer
```

**Codex**

```
codex plugin marketplace add lehoanganhtai13/archmancer
codex plugin add archmancer@archmancer
```

**Other coding agents** (Cursor, Gemini CLI, GitHub Copilot, OpenCode and other agents that load Agent Skills)

```
npx skills add lehoanganhtai13/archmancer
```

Then start with `/archmancer:agent-system-engineering <your task>` in Claude Code, `$agent-system-engineering <your task>` in Codex, or the `agent-system-engineering` skill in other agents. Details for each client are under [Installation](#installation).

## Why

An agent system takes more than a model and a prompt. An agent loop where a fixed workflow would do. A tool call nobody authorized. An empty search read as "there is no answer". A configuration change that never reached the run. A timed-out payment retried before anyone checked the first one. Addressing these failures takes a system view. Archmancer gives your coding agent a map of the responsibilities and concrete checks to work through.

- **A map of the whole system.** Ten responsibilities, from task intake to delivery, each routed to the skill that owns it.
- **The smallest design that holds.** A coded workflow before an agent loop, in-process work before queues, plain retrieval before graphs.
- **A check inside every plan.** Every requirement gets an owner, failure behavior and a check; a model that skipped a tool call does not prove the call would have been blocked.
- **A debugging route.** Identify the run, code revision and effective settings, then find the first hand-off that went wrong.

## How it works

Start with `archmancer:agent-system-engineering`. It maps the target system from outcome to execution and evidence, identifies the checks a plan needs, and routes the task to relevant component skills and chapters. Use it for a new or existing agent system, including deciding when a single model call or a coded workflow meets the requirements without an adaptive loop.

Describe the system and the task after the skill name:

```
/archmancer:agent-system-engineering <your task>
```

For example:

| Goal | Task |
| --- | --- |
| Design | Design a support agent that answers from help-center articles and can issue refunds up to an approved limit. |
| Extend | Add a tool to an existing assistant: its inputs, permissions, results and failure checks. |
| Debug | After a reconnect, the assistant repeats an external action; trace the run to the first divergence. |
| Optimize | The token bill doubled after a release; find the measured cause before changing anything. |
| Harden | Review a document-reading agent for prompt injection and unauthorized tool actions. |
| Migrate | Switch model providers and prove which code and settings reached each run. |

- **Codex:** write `$agent-system-engineering` instead of the slash command.
- **Other agents:** invoke `agent-system-engineering` the way your agent calls skills; the skills install without the `archmancer:` prefix.
- **Narrower questions:** call a component skill directly, for example `/archmancer:agent-trust-and-privacy`.

## What's inside

| Skill | What it covers |
| --- | --- |
| `archmancer:agent-system-engineering` | The starting map: system responsibilities, architectural trade-offs and routes through design, planning, building, debugging, optimization and review. |
| `archmancer:agent-harness-model-and-tools` | How the next step is chosen: workflows, agent loops and delegation; model requests and responses; tools, authorized actions and observed results. |
| `archmancer:agent-runtime-and-interaction` | How work starts, runs and finishes: task admission, scheduling, cancellation, recovery, streaming, reconnect and result delivery. |
| `archmancer:agent-configuration-and-delivery` | Which code and settings govern a run: validation, versions, activation evidence, rollout, rollback and drift. |
| `archmancer:agent-context-and-state` | What the model sees and what survives: context assembly, history, compaction, prompt caching, memory and checkpoints. |
| `archmancer:agent-evidence-and-knowledge` | How answers get their evidence: scoped source access, retrieval, freshness, citations and the lifecycle of an owned corpus when one is needed. |
| `archmancer:agent-diagnostics-evaluation-and-resource-control` | How behavior and resource use are checked: run evidence, tracing, evaluation, comparisons, cost attribution and limits. |
| `archmancer:agent-trust-and-privacy` | Who may act and how data is protected: authorization, isolation, approval, credentials, prompt injection, retention and deletion. |

## Installation

The repository holds one plugin package each for Claude Code and Codex, and a `skills/` folder in the Agent Skills format for other coding agents. All three carry identical skill bodies; only the front matter descriptions differ, because clients read them differently. Claude Code and Codex each have their own catalog file at the repository root.

<details>
<summary><b>Claude Code</b></summary>

```
/plugin marketplace add lehoanganhtai13/archmancer
/plugin install archmancer@archmancer
```

The same steps from a shell: `claude plugin marketplace add lehoanganhtai13/archmancer`, then `claude plugin install archmancer@archmancer`. Add `--scope project` to enable it for a repository only.

Reload with `/reload-plugins` or start a new session. Skills appear as `/archmancer:<skill>`, for example `/archmancer:agent-system-engineering`.

`claude plugin uninstall` can leave a copy under `~/.claude/plugins/cache/`, where other agents may still find the skills by searching the filesystem; delete it if you want the skills gone from view.

</details>

<details>
<summary><b>Codex</b></summary>

```
codex plugin marketplace add lehoanganhtai13/archmancer
codex plugin add archmancer@archmancer
```

Both commands run non-interactively. Start a new session so the bundled skills load. The plugin can also be installed from the `/plugins` browser. Skills are listed by `/skills` and can be invoked with `$`, for example `$agent-system-engineering`.

`codex plugin remove` can leave a copy under `~/.codex/plugins/cache/`; delete it if you want the skills gone from view.

</details>

<details>
<summary><b>Other coding agents</b></summary>

```
npx skills add lehoanganhtai13/archmancer
```

The `skills` command line tool discovers the eight skills in the root `skills/` folder; select all eight when prompted so links between skills keep working. It detects the coding agents on your machine and asks where to install; add `-a <agent>` to choose one, or `-g` to install for every project instead of the current one. Without the tool, copy the folders under `skills/` into the skills directory your agent reads, keeping them side by side because the skills link to each other.

Skills install under their own names, for example `agent-system-engineering`, without the `archmancer:` prefix. The skills follow the Agent Skills format, but they have been tested only with Claude Code and Codex; after installing, check that your agent lists them. For a CLI install, run `npx skills remove` (add `-g` for a global install) and select only the eight skills listed above. For a manual install, delete only those eight copied folders.

</details>

## Activation

<details>
<summary><b>Invoking the entry skill, the optional routing line, and turning it off</b></summary>

Skills are chosen from their descriptions, which does not guarantee that the entry skill loads for a given request. Invoke the entry skill by name and verify that it loads: `/archmancer:agent-system-engineering` in Claude Code, `$agent-system-engineering` in Codex. In other agents, ask for it by name, for example `Use the agent-system-engineering skill to <your task>`, and verify that it loads.

You can also add one routing line to the project instructions of the repository where you work (`CLAUDE.md` for Claude Code, `AGENTS.md` for Codex and other agents that read it). It asks the assistant to use the entry skill first; verify that behavior on the client version and project scope you use.

The optional routing line deliberately covers LLM software more broadly than agent systems, so the entry skill can also help decide whether a single call or coded workflow is sufficient; it does not require an agent loop for every feature.

Claude Code:

```
For planning, designing, debugging or reviewing any software that calls an LLM (assistants, bots, CLIs, batch jobs, RAG, agents, model pipelines), load the `archmancer:agent-system-engineering` skill first and follow its routes to the component skills before writing the plan.
```

Codex and other agents:

```
For planning, designing, debugging or reviewing any software that calls an LLM (assistants, bots, CLIs, batch jobs, RAG, agents, model pipelines), use the `agent-system-engineering` skill first and follow its routes to the component skills before writing the plan.
```

To stop using the set in Claude Code, disable the plugin (`claude plugin disable archmancer@archmancer`, with the same `--scope` used to install) or uninstall it. In Codex, remove it with `codex plugin remove archmancer@archmancer`. For other agents, use the removal steps under Installation. Remove the routing line as well; otherwise the assistant may look for a skill that is no longer installed.

</details>

## License

Apache-2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
