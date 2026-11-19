<p align="center"><img src="icon.png" width="112" alt="Agent Hive logo: a queen bee on a honeycomb"></p>
<h1 align="center">Agent Hive 🐝</h1>
<p align="center"><b>One Queen. Many bees. Your coding agents, working as a hive.</b><br>
A free, open-source Mac app that turns Claude Code, Codex, Gemini CLI, Antigravity, DeepSeek Harness and Cursor Agent<br>into a small, friendly team you can watch, schedule and steer.</p>
<p align="center">
  <a href="https://github.com/ericwang915/agent-hive/releases/latest"><img src="https://img.shields.io/github/v/release/ericwang915/agent-hive?label=release&color=F0A93B" alt="latest release"></a>
  <a href="https://github.com/ericwang915/agent-hive/releases"><img src="https://img.shields.io/github/downloads/ericwang915/agent-hive/total?label=downloads&color=F0A93B" alt="total downloads"></a>
  <a href="https://github.com/ericwang915/agent-hive/stargazers"><img src="https://img.shields.io/github/stars/ericwang915/agent-hive?label=stars&color=F0A93B" alt="GitHub stars"></a>
  <a href="https://github.com/ericwang915/agent-hive/actions/workflows/test.yml"><img src="https://github.com/ericwang915/agent-hive/actions/workflows/test.yml/badge.svg" alt="tests"></a>
  <img src="https://img.shields.io/badge/platform-macOS%2012%2B-lightgrey" alt="macOS 12 or later">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT license"></a>
</p>
<p align="center">
  <a href="https://github.com/ericwang915/agent-hive/releases/latest"><b>⬇️ Download for Mac</b></a> · <a href="#install">Install</a> · <a href="#what-you-can-do-with-it">Features</a> · <a href="#how-it-compares">How it compares</a> · <a href="#faq">FAQ</a> · <a href="https://ericwang915.github.io/agent-hive/">Website</a> · <a href="README.zh-CN.md">中文</a>
</p>

<p align="center"><img src="docs/bees.svg" width="860" alt="Seven cartoon bees in a row: Queen with a crown, then Hazel, Buzz, Mochi, Puff, Nori and a sleeping Olive, each with a line about its job"></p>

<p align="center"><i>Every agent is a bee with a name, a face and a job. They bob while they work, doze when they are idle,<br>and earn a new look as they climb from Bronze to Master.</i></p>

![Agent Hive's honeycomb running a relay team of coding agents: one bee writes, another reviews and sends it back, a third tests](docs/relay.gif)

<p align="center">If the bees make you smile, a ⭐ helps other people find the hive.</p>

## What is Agent Hive?

Agent Hive is a macOS app that runs several coding-agent CLIs at once and lets them work as a team. Each agent is a **bee**: Claude Code, Codex, Gemini CLI, Antigravity (`agy`), DeepSeek Harness (`dsh`), Cursor Agent, or any command you like, working in its own folder. You can talk to each bee, put it on a schedule, chain bees into a relay where one writes and another reviews, or pull them into a group and let **Queen** hand out the work.

It uses the CLIs and logins you already have, including a Claude or ChatGPT subscription. It ships no API keys, stores none, has no account and no server of its own.

## Highlights

- 🐝 **Any agent, mixed in one team.** Claude Code writes, Codex reviews, Gemini tests. Any CLI that takes a prompt can be a bee.
- 🌙 **Agents that work while you are away.** Schedules (once, daily, weekdays, weekends, weekly, monthly, every N minutes) and event triggers (new commits, GitHub pull requests, comments and CI failures, another bee finishing), catch-up for runs missed while the Mac slept, and a daily budget that stops automatic runs when it is used up.
- 👑 **A lead agent instead of ten terminals.** Tell Queen what you want; she picks the bees, dispatches the work, waits for the results and sums them up.
- 🔁 **Review built into the flow.** Relay teams of up to six bees send a reviewer's findings back to the writer until it approves. Build a team by dragging one bee onto another. Every bee has a diff view with commit, push and pull request.
- 🗂️ **Everything they made, in one place.** A Files page lists every PDF, deck, chart and link the bees produced, by bee and project. Search finds bees, skills, memory and anything said in a conversation.
- 🍯 **Spends fewer tokens than the CLI on its own.** Sessions are compacted before they get expensive, scheduled runs start fresh, unused tools and MCP servers are left out. In a measured three-round task a bee carried about 30% less context per round than plain `claude -p` on the same machine with the same setup (29k against 44k tokens).
- 🧠 **It remembers.** Overnight, two helper bees turn the day's conversations into long-term memory and reusable skills. New sessions start with both.
- 🔒 **Nothing to trust but your own machine.** MIT licensed, no build step, no telemetry; the only request the app makes on its own is a check for new releases on GitHub. The app is signed and notarized by Apple and updates itself if you let it.

## Install

```bash
curl -fsSL https://raw.githubusercontent.com/ericwang915/agent-hive/main/install.sh | bash
```

This downloads the latest release for your Mac (Apple silicon or Intel), puts `Agent Hive.app` in `/Applications` and opens it. With Homebrew: `brew install --cask ericwang915/tap/agent-hive`. You can also download the `.dmg` from the [releases page](https://github.com/ericwang915/agent-hive/releases). The app is signed and notarized by Apple.

To run from source instead:

```bash
git clone https://github.com/ericwang915/agent-hive.git
cd agent-hive
npm install
npm start
```

### Requirements

- macOS 12 or later
- At least one agent CLI on your `PATH`: [`claude`](https://docs.claude.com/en/docs/claude-code), `codex`, `gemini`, `agy`, `dsh` or Cursor's `agent` (older installs: `cursor-agent`). Queen, the daily report and the night bees need `claude`.
- `git` for diffs, commits, branches and pull requests. `gh` is optional and used to open pull requests.

## What you can do with it

### Let Queen lead a group

Pull bees into a group and tell Queen what you want. She picks the right bees, dispatches the work, waits for the results and sums them up. She only wakes the bees she needs, and she asks before hatching new ones.

![Queen dispatches two bees from the group chat beside the honeycomb and reports back](docs/queen.gif)

A group works without Queen too. `@mention` a bee and it starts right away. Leave the name out and a small, cheap model picks the bee the message is for, so the others stay asleep; a bee with nothing to add stays quiet. Stickers work both ways. A bee can hand part of the job to another by `@mentioning` it, for at most three hops.

### Chain bees into a relay team

Up to six bees share a folder and pass work down the line. A reviewer can send its findings back to the writer until it approves, for at most three rounds. Bees on the same step run in parallel, each in its own git worktree, and a final bee merges their results. A bee that is already in the hive can join a team too: pick it from the Relay menu, or drag it onto the bee it should follow, and onto a second one to have it merge both (it moves into the team's folder and goes back to its own when it leaves), and a link between two bees can be taken out without deleting either. The clip at the top is one such team.

**Build one by dragging.** Drag a bee onto the bee it should follow. Drop two bees on the same one and they work in parallel; drag a bee onto a second one and it waits for both and merges their work.

![Four bees dragged into a squad: Buzz and Mochi follow Hazel, Puff merges both, then the squad runs](docs/drag.gif)

A relay team is also a **squad** with a name. Queen can hand it a whole job with one call and hears back once, when the chain is finished or stuck. You can start it yourself from any group: `@Shop-squad add an export button`. The group shows the chain and each bee's state as it runs.

### Read every step, then review the diff

Each bee has its own chat window with the full conversation. Replies stream in as they are written, edits show as inline diffs, sub-agents are nested, and every round shows its cost. Type `@` to point at a file, `/` for commands, Shift-Tab to switch between Ask, Auto-edit and Plan. The bee's folder sits in a sidebar on the left, and file paths in the conversation are clickable: they open at the line mentioned. The Files tab is a small editor: create, rename and delete files and folders, edit and save, find in a file, and search the whole folder by name or text. The Changes tab shows the diff. Commit, discard, push and open a pull request from there, or keep a bee on its own branch and merge when you are happy.

![A bee's chat, then its diff](docs/chat.gif)

### See the whole hive at a glance

The Hive page opens as a honeycomb; a switch takes you to the classic cards. Each squad is a cluster shaped by its relay: a chain sits in a row, a review loop is marked on the shared edge, and bees that work in parallel fan out and meet again at the merge. Click a cell and its full card, with every button, shows beside the comb. Drag a bee onto another and it joins that bee's squad; click the badge on a link to take the link out.

![The honeycomb view: a squad with a review loop, a squad with two bees in parallel and a merge, and three bees on their own](docs/honeycomb.png)

### Hatch a bee in a few clicks

Pick a folder and an engine. Give it a prompt and a schedule, or leave both empty and just talk to it. A bee starts on its CLI's default model; the model button under the chat box changes it at any time.

![The hatch dialog](docs/hatch.gif)

### And the rest

- **Schedules.** Once, daily, weekly, monthly, or every N minutes. Runs missed while the Mac slept are caught up the same day.
- **Event triggers.** Instead of a time, a bee can wait for something to happen: new commits on a branch (in its folder or on the remote), a GitHub event (new pull request, new comment, CI failure, through the `gh` CLI), or another bee finishing or failing. What happened is attached to its prompt. Its own commits and comments do not wake it, and a cooldown keeps bursts to one run.
- **Sleep-safe.** Running bees stop when the lid closes and pick up where they left off when it opens, or when the app restarts.
- **Permissions.** Approve each action from the app (Claude Code), auto-accept edits, allow everything, or plan first and change nothing. Switch at any time from the chat.
- **Context.** A meter shows how full a Claude Code bee's session is. `/compact` summarises it on the spot, and `/new` starts over.
- **Token savers.** A session that is half full (100k tokens at most), or large and idle for an hour, is compacted before its next round. Scheduled runs start a new session. Each bee's settings list your MCP servers, so you tick only the ones it needs. Reports and the night bees use a smaller model. All adjustable.
- **Spend.** Cost and tokens per round, and a daily budget that holds back automatic runs once it is used up.
- **Memory and skills.** Overnight, *Dreamer* tidies long-term memory and *Gardener* turns the day's conversations into reusable skills. New sessions start with both.
- **Dashboard.** A 24-hour activity timeline, spend, and Queen's daily report.
- **Upgrades.** When a newer release is out, an Upgrade button appears in the sidebar. It downloads the release, checks that it is signed by the same developer, swaps the app and restarts. Settings (the gear at the bottom of the sidebar) can install new versions automatically once no bee is working, and notify you when one is out.
- **Ranks.** Every finished round counts. A bee climbs from Bronze through Silver, Gold, Platinum and Diamond to Master, and its look changes with each rank.
- **Files page.** Everything the bees produced in one list, newest first: files they wrote or named in a reply (PDFs, decks, charts, CSVs) and links they gave (artifacts, Google Slides, pull requests). Each row shows the bee and its project; filter by kind or bee, open the file, or jump to it in the bee's window.
- **Chats in the sidebar.** Every bee and squad in one list: its name and what it is for, or what it is doing right now. A squad folds into one line and opens when something is going on.
- **Search everything.** The search box and ⌘K find bees, skills, memory, and what was said in any bee's conversation or group; a hit opens the chat at that message.
- **Right-click anything.** Rename, settings, stop and delete for bees and groups.

## How it compares

Several good tools run coding agents in parallel. They differ in what they are built around. This is how Agent Hive sees the field in November 2026; check each project for its current features.

| Tool | Built around | Good fit when |
|---|---|---|
| **Agent Hive** | A standing team: scheduled agents, a lead agent (Queen), relay teams with review loops, memory and skills. Open source, macOS. | You want agents that keep working on a schedule, hand work to each other, and that you can supervise from one window. |
| [Conductor](https://www.conductor.build) | Parallel workspaces, each agent in its own git worktree. A proprietary macOS app. | You want to start many independent tasks on one repository and review each branch. |
| [Claude Squad](https://github.com/smtg-ai/claude-squad) | A terminal UI on tmux, each agent in its own git worktree. Open source. | You live in the terminal and want sessions that survive a closed window. |
| [Vibe Kanban](https://github.com/BloopAI/vibe-kanban) | A kanban board of tasks that agents pick up in workspaces. Open source. | You think in tickets and want a board as the main view. |
| Claude Code agent teams | Several Claude Code instances that message each other. Claude only. | You use only Claude Code and want it to split one task among teammates. |

What Agent Hive adds on top of running agents side by side:

- **Scheduling with catch-up, sleep-safe runs and a daily budget**, so unattended work is predictable.
- **Routing by a small model.** In a group, a message without an `@mention` goes only to the bee it concerns; the others stay asleep and cost nothing.
- **Review loops across engines**: a reviewer on one model can send work back to a writer on another, for at most three rounds.
- **Token controls you can see**: a context meter, automatic compaction, cost per round, and a checklist of MCP servers per bee.
- **Memory and skills** that are distilled from your own conversations and shared by every bee.

Agent Hive also uses git worktrees, for bees that run in parallel on the same step of a relay.

## Safety

Bees run real commands on your machine, with the permission level you choose. "Allow all" skips every confirmation, so only use it in folders you trust.

The app listens on `127.0.0.1` on a random port, protected by a per-launch token. Claude Code uses it to ask for permission decisions, and Queen uses it to call her tools. Nothing is exposed to the network.

State lives in `~/Library/Application Support/Agent Hive/`. Workspaces, skills and memory live under `~/AgentHive/` by default.

## FAQ

### Is Agent Hive free?

Yes. It is open source under the MIT license. You pay only for the agent CLIs you already use, through their own subscriptions or API billing.

### Does it need an API key?

No. Agent Hive starts the CLIs installed on your Mac (`claude`, `codex`, `gemini`, `agy`, `dsh`, `cursor-agent`) with the logins they already have. It stores no key. If your shell profile exports an API key for one of them (`DEEPSEEK_API_KEY`, `GEMINI_API_KEY`, `GOOGLE_API_KEY`, `CODEX_API_KEY`, `CURSOR_API_KEY`), the app hands it on to that CLI, as a terminal would.

### Does it work with a Claude Pro or Max subscription, or ChatGPT Plus?

Yes. If the CLI works in your terminal, it works as a bee, with the same account and limits.

### Which coding agents does it support?

Claude Code, Codex CLI, Gemini CLI, Antigravity (`agy`), DeepSeek Harness (`dsh`) and Cursor Agent out of the box, plus any command line that accepts a prompt (a custom template with `{prompt}`). Queen, the daily report and the night bees need Claude Code.

### How is it different from Claude Code subagents or agent teams?

Subagents and agent teams are features of Claude Code and use Claude only. Agent Hive runs separate, long-lived agents from different vendors, each with its own folder, session, schedule and chat window, and keeps running them after you close the conversation.

### Can agents run on a schedule, like a cron job for Claude Code?

Yes. Each bee can run once, daily, weekly, monthly or every N minutes. Runs missed while the Mac slept are caught up the same day, and a daily budget can stop automatic runs.

### Does my code leave my machine?

Agent Hive has no server and sends your code nowhere. The agent CLIs talk to their own providers exactly as they do in your terminal. The only request the app makes on its own is a check for new releases on GitHub.

### Does it run on Windows or Linux?

Not yet. It is built and tested for macOS 12 or later, on Apple silicon and Intel.

### How do I update it?

An Upgrade button appears in the sidebar when a new release is out. Settings can also install new versions automatically once no bee is working.

## How it is built

No build step and no framework: plain HTML, CSS and JS in the renderer, Electron in the main process, two small dependencies for Markdown.

| File | Role |
|---|---|
| `main.js` | Main process: state, process management, scheduling, relay execution, git, approvals, groups and Queen |
| `core.js` | Engines and command lines, schedule keys, output parsers, relay planning, git and worktree helpers |
| `team.js` | Relay-team graph helpers, shared by main and renderer |
| `queen.js` | Queen's tools, dispatch rules and result parsing |
| `garden.js` | Skills and memory files, Dreamer and Gardener prompts |
| `events.js` | Event triggers: checking the settings, telling what is new on GitHub, matching a finished bee |
| `outputs.js` | Files page: finding the files and links a bee produced in its log |
| `update.js` | Upgrade: finding, downloading, verifying and installing a newer release |
| `files.js` | File browser: listing, reading and locating paths inside a bee's folder |
| `approve-mcp.js`, `hive-mcp.js` | Small MCP stdio servers that call back into the app |
| `index.html`, `app.js` | Main window |
| `chat.html`, `chat.js` | Per-bee chat window |
| `test.js` | Unit tests for everything that does not need Electron |

```bash
npm test             # unit tests
npm run dist         # build an ad-hoc signed .zip and .dmg into dist/
npm run dist:signed  # the same, signed and notarized (needs CSC_NAME and NOTARYTOOL_PROFILE)
```

## Contributing

Issues and pull requests are welcome, and so are stars: they are how other people find the hive. 🐝 See [CONTRIBUTING.md](CONTRIBUTING.md) for how the code is laid out and how to add an engine.

## License

[MIT](LICENSE)
