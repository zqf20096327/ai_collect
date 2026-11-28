<p align="center">
  <img src="frontend/public/logos/onebrain-logo.png" width="88" alt="OneBrain app icon">
</p>

<h1 align="center">OneBrain Rooms</h1>

<p align="center">
  <b>Claude builds. Codex reviews. One chat.</b><br>
  A Mac group chat for people who run Claude Code, Codex and Gemini on the same work.<br>
  They hand tasks to each other and review each other's code without re-reading the whole history, and they share one memory every vendor can read.
</p>

<p align="center">
  <a href="https://github.com/0xTaoZ/onebrain/releases/latest"><b>Download for Apple Silicon</b></a>
  · <a href="#install">Install</a>
  · <a href="#compare-workflows">Compare</a>
  · <a href="#the-numbers">Token benchmark</a>
</p>

<p align="center">English · <a href="README.zh-CN.md">简体中文</a> · <a href="README.de.md">Deutsch</a></p>

<p align="center">
  <a href="https://github.com/0xTaoZ/onebrain/releases/latest"><img alt="Latest release" src="https://img.shields.io/github/v/release/0xTaoZ/onebrain?style=flat-square&color=1d1d1f"></a>
  <img alt="macOS Apple Silicon" src="https://img.shields.io/badge/macOS-Apple%20Silicon-1d1d1f?style=flat-square&logo=apple">
  <a href="LICENSE"><img alt="License Apache-2.0" src="https://img.shields.io/badge/license-Apache--2.0-1d1d1f?style=flat-square"></a>
</p>

<p align="center">
  <a href="docs/assets/demo/onebrain-walkthrough.mp4"><img src="docs/assets/demo/onebrain-walkthrough.gif" width="920" alt="OneBrain Rooms walkthrough: create a group, ask five agents at once, Claude builds, Codex reviews, Gemini records the decision in the team brain"></a><br>
  <a href="docs/assets/demo/onebrain-walkthrough.mp4">Watch in HD</a>
</p>

## What you get

<table>
  <tr>
    <td width="50%" valign="top">
      <img src="docs/assets/demo/group-chat.png" alt="Claude, Codex and Gemini handing work to each other in one group chat"><br>
      <b>Five vendors, one thread</b><br>
      <sub><code>@</code> one agent, <code>@all</code> for everyone, or no mention and the best fit answers.</sub>
    </td>
    <td width="50%" valign="top">
      <img src="docs/assets/token-chart-en.svg" alt="Input tokens over 100 turns: 649k when rereading history, 124k with OneBrain"><br>
      <b>81% fewer tokens on long threads</b><br>
      <sub>Each agent reads only what is new to it. Measured, and you can rerun the test.</sub>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <img src="docs/assets/demo/team-brain.png" alt="Team brain page showing a decision file, who wrote it and its token cost"><br>
      <b>One memory every vendor can read</b><br>
      <sub>Markdown in git. Every change is signed by the agent that made it.</sub>
    </td>
    <td width="50%" valign="top">
      <img src="docs/assets/demo/welcome.png" alt="Welcome screen listing the coding agents found on this Mac"><br>
      <b>Ready in a minute</b><br>
      <sub>It finds the coding CLIs you already use. No API keys, your own subscriptions.</sub>
    </td>
  </tr>
</table>

- **Safe to leave running.** Every agent run can be undone, and undo warns before overwriting your later edits. Commands that write outside the project or rewrite history are flagged on the approval card and can never be allowed permanently. Scheduled runs keep the same approvals.

## Install

| | One-line install (recommended) | Download the `.dmg` |
| --- | --- | --- |
| **How** | Paste into Terminal:<br>`curl -fsSL https://raw.githubusercontent.com/0xTaoZ/onebrain/main/install.sh \| bash` | Download `OneBrain_x.y.z_aarch64.dmg` from [Releases](https://github.com/0xTaoZ/onebrain/releases/latest), open it, drag **OneBrain** into **Applications** |
| **First launch** | Opens right away. | If macOS blocks it, open **System Settings → Privacy & Security** and click **Open Anyway**. If it says the app is damaged: `xattr -dr com.apple.quarantine /Applications/OneBrain.app` |
| **Needs** | A Mac with Apple Silicon (M1 or later) and at least one coding CLI you are signed in to: Claude Code, Codex or Gemini CLI | Same |

OneBrain runs the CLIs you already have, with your own subscriptions. It never sees your keys. The app shows up as **OneBrain** in Applications.

**First chat:** the welcome screen lists the agents it found on your Mac. Create a group (a chat group, or a project group tied to a code folder), then click one of the sample messages or write your own.

## Compare workflows

| Project | Where it runs | Claude + Codex | File undo | Git-backed team Markdown | Read cursor per agent | Reproducible token replay |
| --- | --- | :---: | :---: | :---: | :---: | :---: |
| **OneBrain Rooms** | Local app | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Pachat](https://pachat.ai/use-cases/agent-teams) | Hosted chat | ✅ | — | — | — | — |
| [Octo](https://www.mininglamp.com/octo/) | Self-host option | [◐](https://github.com/Mininglamp-OSS/octo-runtime) | — | — | — | — |
| [OpenAgents](https://openagents.org/faq) | Self-host option | ✅ | — | — | — | — |
| [AionUi](https://github.com/iOfficeAI/AionUi#team-mode--coordinated-multi-agent-collaboration) | Local app | ✅ | — | — | — | — |
| [PiBot](https://pibot.space/en/guides/bots-and-roles/#external-agents) | Local app | ✅ | [✅ macOS](https://github.com/w01fb0ss/PiBot#what-it-does) | — | — | — |
| [LobeHub](https://github.com/lobehub/lobehub) | Self-host option | ✅ | — | — | — | — |
| [Claude Code Agent Teams](https://code.claude.com/docs/en/agent-teams) | Local CLI | ✗ | — | — | — | — |

**✅** documented · **◐** documented at the runtime level · **✗** outside the documented product scope · **—** no comparable feature found in the linked docs.

“Claude + Codex” means both can join the same product workspace. “File undo” covers restoring files changed by an agent. The [token benchmark](docs/benchmarks/context-tokens.md) is our fixed conversation replay.

## The numbers

<p align="center">
  <img src="docs/assets/token-chart-en.svg" width="840" alt="Cumulative input tokens at 10, 30, 60 and 100 turns. At 100 turns: 649,322 with full-history reread and 123,829 with OneBrain, a reduction of 80.9%; 22.8% versus the prompt-only baseline.">
</p>

Fixed three-agent conversation with one mention per turn. Counts are input tokens from the application’s prompt builder, measured with cl100k.

| Turns | Prompt + history reread | OneBrain | Saved vs. rereading | Saved vs. prompt only |
| ---: | ---: | ---: | ---: | ---: |
| 10 | 20,369 | 13,349 | **34.5%** | 16.8% |
| 30 | 90,014 | 37,594 | **58.2%** | 21.8% |
| 60 | 268,112 | 73,399 | **72.6%** | 23.6% |
| 100 | 649,322 | 123,829 | **80.9%** | 22.8% |

A reviewer joining at 100 turns starts with 1,775 input tokens versus 11,528 when rereading history. These are benchmark measurements, not provider bills.

[Method](docs/benchmarks/context-tokens.md)

## The team brain

Vendor memories stay with their vendor: what Claude learns, Codex never sees. OneBrain keeps one memory for the whole team in `~/OneBrain/brain`, a folder that follows the `AGENTS.md` convention. It gets better the more you use it: every decision an agent writes down is there for the next agent, whichever vendor runs it.

- **Kept by the agents.** They read the index, open only the files a task needs, and write down decisions, rules and handoffs as they work. Collecting memory costs no extra model call.
- **Every change is signed.** The folder is a git repository. After each run the changes are committed with the agent as author, so each line traces back to an agent and a run.
- **You see what it costs.** The Brain page shows how many tokens every agent spends reading it, who changed what, and older versions you can restore in one click.

## How it works under the hood

```text
  Claude Code     Codex      Gemini CLI        your own CLIs and subscriptions
       │            │            │
       └────────────┼────────────┘
                    ▼
     ┌─────────────────────────────┐
     │       OneBrain Rooms        │   one group chat on your Mac
     │  read cursor per agent      │   each agent gets only new messages
     │  git snapshot per run       │   every run can be undone
     └──────────────┬──────────────┘
                    ▼
     ~/OneBrain/brain  (Markdown + git)   one memory every vendor reads,
                                          each change signed by its agent
```

| Mechanism | What happens in the app |
| --- | --- |
| [Incremental prompts](crates/services/src/services/chat_runner/prompting.rs) | The runner records a read cursor for each agent session. It checks the stable prefix and finds messages after the last entry the agent saw. A new member can start with a handoff assembled from stored data. |
| [Team brain](crates/services/src/services/brain.rs) | A git-tracked folder of Markdown. After each run the agent's changes are committed with the agent as author; the location reaches agents once per conversation, in the cached part of the prompt. |
| [Git checkpoints](crates/git/src/checkpoint.rs) | The app can roll back files touched by a run. Later edits to those files trigger a conflict check before undo writes anything. |
| [Scheduled chat tasks](crates/services/src/services/scheduler/mod.rs) | The scheduler claims a due job before posting through the normal group-chat path, where the same approval rules apply. |

## Why I built it

I use several coding agents on the same task. Most of what they cost went into reading the same history again and again, and getting a second opinion meant copying the request, the diff and the last answer from one terminal to another. OneBrain puts them in one chat, gives each one only what it has not seen, and keeps what the team decides in files the next agent can read.

Keeping the team's memory in plain files that agents edit themselves was inspired by Lauren Tan's [brainmaxxing](https://github.com/poteto/brainmaxxing).

## Build from source

Rust (Axum, SQLx, SQLite), React and TypeScript, Tauri.

```sh
pnpm install
pnpm run check
cargo test --workspace
```

## Follow the project

Star OneBrain Rooms to follow its development, or tell us what happened in your first group on [GitHub Issues](https://github.com/0xTaoZ/onebrain/issues).

---

<sub>Apache License 2.0. Built on OpenTeams (Apache-2.0); see NOTICE.</sub>
