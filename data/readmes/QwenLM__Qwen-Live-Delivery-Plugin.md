[![Qwen Live Delivery Plugin — Ship as you go. Steer as it grows. 边做边交付，方向全掌控。 The first step toward a Live Agent.](docs/assets/header-en.png)](docs/assets/header-en.png)

**English** · [中文](README.zh-CN.md)

**Available at launch: Codex CLI** · **Supported platforms: Linux · macOS** · Node.js 22+

Let agents work on long tasks, keep delivering, and respond to your feedback along the way.

## Overview

As long-horizon AI agents become increasingly mainstream, a very real concern remains: have you ever felt uneasy handing an entire time-consuming task over to an Agent, worried it would race ahead inside a “black box” and return work that misses the mark and is difficult to salvage? To address this loss of control, we introduce Qwen-Live-Delivery-Plugin, a lightweight plugin designed for long-running tasks. It helps Agents keep working reliably and delivering results over time, while letting users add requirements and steer the work at any point (human-in-the-loop). The plugin consists of three core modules:

1. **Live Delivery Skill** ([`$ld:go`](live-delivery/skills/go/SKILL.md)): Guides the Agent to choose a minimal usable first version, plan each next version from the actual results, and include validation and delivery in every iteration, without a fixed version count.
2. **Live Delivery MCP**: Uses `ld_begin`, `ld_publish`, `ld_status`, and `ld_done` to manage delivery plans and state, preserve complete version snapshots with preview entries, report the remaining budget, and wrap up the task.
3. **Lifecycle Hooks**: Pass user feedback into context on resumed turns or after tool calls, block premature turn completion while the task is active and budget remains, and support wrap-up when the user stops the task or the budget runs out.

The local browser workbench brings these capabilities together: review progress, preview and download versions, send further requirements, and adjust the total budget or stop the task. It launches browser-created tasks and interrupts and resumes the same Codex thread for new messages; Hooks then deliver the feedback into context. External CLI tasks receive feedback at supported tool or turn events.

## Demo

This demo follows an AI agent as it builds ORBIT, a personal trading research website, from the ground up through continuous delivery. The agent ships a working first version, then iteratively develops the market dashboard, strategy backtesting, and paper trading tools. Users can try each release and request changes along the way, with the agent incorporating their feedback into future updates.

![Live Delivery demo](docs/assets/orbit-live-delivery-en.gif)

## How it works

[![Start with ld:go: set a task, let the Agent work, then review and steer. Add instructions anytime; Hooks bring feedback back to the Agent for the next version. Keep every delivered result.](docs/assets/lifecycle-en.png)](docs/assets/lifecycle-en.png)

Start once, get a usable first version, and improve it one version at a time. Add requirements or change direction anytime. Delivered versions remain available when you stop the task or the budget runs out.

## Install

Installation uses your Codex model, authentication, and approval settings; no model or API key is included. Browser tasks default to the `workspace-write` sandbox. Explicitly setting `QWEN_LD_TASK_SANDBOX=danger-full-access` disables their sandbox and per-command approval, allowing access outside the workspace with your OS account permissions. The installer never enables full access automatically.

### For agents

Give Codex the repository directory and ask:

```text
Read /absolute/path/to/Qwen-Live-Delivery-Plugin/README.md and follow its installation skill to install and verify the plugin. Use /absolute/path/to/my-project as the workspace.
```

The installing agent should read the bundled [installation skill](live-delivery/skills/install/SKILL.md). After installation, `$ld:install` is available for setup and diagnosis.

### For users

Enter the repository directory and run:

```bash
cd /path/to/Qwen-Live-Delivery-Plugin
./live-delivery/install.sh --workspace /path/to/project
```

Press Enter to install the plugin, configure its hooks, and open Codex. The release archive needs no `npm install`. If Codex is already open, start a new session.

Add `--install-only` to install without opening Codex. Use `./live-delivery/install.sh --doctor` to check installation.

<details>
<summary>Update and uninstall</summary>

Finish active tasks, run `./live-delivery/install.sh --install-only` from the new package, and reopen Codex. To uninstall, run the following; workspaces and delivery records are kept:

```bash
codex plugin remove ld@live-delivery-local --json
codex plugin marketplace remove live-delivery-local --json
```

</details>

## Quick start

Start Codex in your project:

```bash
cd /path/to/project
QWEN_LD_TIME_BUDGET=12m codex
```

Enter your request:

```text
$ld:go Build an offline pendulum experiment. Let me adjust the length, pause the animation, and understand how length affects the period. Make it work on mobile too.
```

**Open the workbench URL printed in the CLI to view the plan, preview deliveries, and continue the conversation.** The link grants workbench access; keep it private and reopen the latest CLI link after a restart. The plugin tries to open a browser on a desktop. For a remote server, use the printed server address.

1. After the first delivery, select a version on the right. Open **Files** to preview or download individual files.
2. Add requirements on the left. **Enter sends; Shift+Enter inserts a newline.**
3. Use **Time budget** in the header to control the total time, or **Stop task** to finish.

Continuing a completed task keeps its conversation and all version previews in the same task. Only **New task** starts a separate history.

Use **Quick guide** in the header for pointers; close or reopen it anytime. Budgets accept minutes, hours, or days, up to 7 days. Delivery times are estimates; stopping waits for the current tool to finish.

Use the workbench on a trusted network. For local access or SSH forwarding, set `QWEN_LD_BIND_HOST=127.0.0.1` before starting Codex.

Plugin **0.1.0**, tested with Codex **0.166.0 / 0.167.1**.

## Documentation

- [Contributing](CONTRIBUTING.md) · [Development and tests](docs/development.md)
- [Security](SECURITY.md)

## Planned ToDos

- [ ] **Expand support for agent harnesses**: Build on the existing MCP delivery tools and version snapshots to support each harness’s installation workflow, lifecycle hooks, session management, and APIs for interrupting and resuming tasks. Add end-to-end compatibility tests covering release publishing, new requirements added during execution, task continuation across sessions, and task cancellation.

## Citation

If you find this plugin useful, please cite:

```bibtex
@inproceedings{qwen_live_delivery_plugin_2026,
  title={Qwen-Live-Delivery-Plugin: Ship as you go. Steer as it grows.},
  author={{Qwen Team}},
  year={2026},
  url={https://github.com/QwenLM/Qwen-Live-Delivery-Plugin}
}
```

## License

Licensed under [Apache-2.0](LICENSE).
