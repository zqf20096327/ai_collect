![Bercy — Branch, Execute, Relay, Converge, Yield](docs/en/bercy-banner.png)

<p align="center">
  <b>Turn one sentence into a team of AI agents that split the work, check each other and adapt as results come in.</b><br>
  A local desktop app for the coding agents you already use: Codex, Claude Code, OpenClaw, DeepSeek Harness and Pi.
</p>

<p align="center">
  <a href="https://github.com/beProactive01/Bercy/releases/latest"><img alt="Latest release" src="https://img.shields.io/github/v/release/beProactive01/Bercy"></a>
  <a href="https://github.com/beProactive01/Bercy/actions/workflows/test.yml"><img alt="Tests" src="https://github.com/beProactive01/Bercy/actions/workflows/test.yml/badge.svg"></a>
  <a href="LICENSE"><img alt="MIT license" src="https://img.shields.io/github/license/beProactive01/Bercy"></a>
  <img alt="macOS on Apple Silicon" src="https://img.shields.io/badge/macOS-Apple%20Silicon-black">
</p>

<p align="center">
  <b>English</b> · <a href="README.zh-CN.md">简体中文</a> · <a href="#see-it-work">Demos</a> · <a href="#quick-start">Quick start</a> · <a href="#how-bercy-is-different">Why Bercy</a> · <a href="#runtimes">Runtimes</a>
</p>

![Three agents check conversion, crashes and support tickets in parallel, then a release lead recommends expanding on iOS and pausing Android](docs/demos/checkout-rollout.gif)

## What you get

- **One brief, a whole team.** Describe the goal. Bercy plans the roles, the deliverables and who waits for whom, then runs independent parts in parallel. You stop copying output from one chat into the next.
- **Agents check each other's work.** A review node sends work back with specific issues for up to two rounds. It runs on a different model from the one that did the work, so Claude can review what Codex built and Codex can review Claude.
- **Plans that adapt instead of failing.** When a node reports a blocker or a gap, Bercy adds the missing step and holds the work that depends on it. Every change is saved as a plan version with its reason.
- **The best agent for each step.** Mix Codex, Claude Code, OpenClaw, DeepSeek Harness, Pi or any ACP runtime in one workflow. Bercy matches each node to a runtime with the capabilities it needs, or you choose.
- **A process you keep.** Save a workflow that worked, reuse it with a new brief, run it on a schedule or share it as a file.
- **Local and in your control.** Bercy runs on your Mac with your own CLI sign-ins. It makes no network requests itself. Edit any node before it runs, approve commands and rerun from the node that went wrong.

## How Bercy is different

| | One agent session | A board of parallel agents | **Bercy** |
| --- | --- | --- | --- |
| Who splits the work | You, prompt by prompt | You, card by card | **The planner, from one brief** |
| Results reach the next step | Within one context | No, each agent works alone | **Yes, outputs flow downstream and converge** |
| When something is missing | You notice and restart | You add another card | **A step is added and the reason recorded** |
| Quality check | You read everything | You review each diff | **A second model reviews and sends work back** |
| Mixing vendors | One vendor | Usually | **Per node, matched by capability** |
| Reuse | Copy old prompts | Start a new board | **Versioned workflows, schedules and shareable files** |

## See it work

### Describe the goal and get a plan

Ask “How should we launch family sharing?” and request release notes, a QA checklist and a combined launch brief. Codex gives the first two tasks independent branches and connects the brief after both. Open any node to read its assignment. The recording skips the model wait.

![Typing the launch question, generating a three-node plan with Codex and opening the release-notes assignment](docs/demos/auto-plan.gif)

### Watch the plan change while it runs

In the built-in subscription demo, the tester finds a gap in older-client coverage. Bercy adds a compatibility reviewer to that branch while the copywriter keeps working. The release manager waits for the new checks before delivering the package.

![A four-node workflow starts, gains a compatibility reviewer and delivers the release package](docs/demos/adaptive-run.gif)

### Let a second model review the work

Open a node with one input and turn on **Review node**. The reviewer either approves the work or returns it with concrete issues, and the upstream node revises it, for up to two rounds. When you haven't pinned a runtime, Bercy routes the review to a different connected runtime from the one that produced the work, and waits for it if it's busy. The node panel shows the pairing, for example “Cross-model review: Codex produced the input, so Claude checks it.”

```text
Implement (Codex) ──▶ Review (Claude) ──▶ Deliver
        ▲                    │
        └── return: issues ──┘   up to two rounds
```

### Draw the graph yourself

Double-click the canvas to add a node. Drag the output ports of **Draft copy** and **QA checks** onto **Launch kit**. Move the kit and both dependencies follow it.

![Adding three tasks in the manual builder, connecting two inputs to a shared node and creating the workflow](docs/demos/manual-builder.gif)

## Quick start

Bercy runs on Macs with Apple Silicon. Windows and Intel Macs aren't supported yet.

[Download Bercy for Apple Silicon (.dmg)](https://github.com/beProactive01/Bercy/releases/download/v0.1.14/Bercy-0.1.14-arm64.dmg), or pick a version from [Releases](https://github.com/beProactive01/Bercy/releases). Open the disk image and drag Bercy into Applications.

The app isn't notarized yet, so macOS blocks it the first time. Run this once in Terminal, then open Bercy as usual:

```sh
xattr -dr com.apple.quarantine /Applications/Bercy.app
```

Or try to open Bercy, then go to **System Settings → Privacy & Security** and choose **Open Anyway**.

To run from source, install Node.js and npm. The project is tested with Node.js 26.5.

```sh
npm ci
npm start
```

1. Open **Settings → Runtimes** and connect at least one CLI you've installed and signed in to. Connect two runtimes so reviews can run on a different model.
2. Choose **New task → Multi-agent workflow** and enter a brief:

   > Prepare user-facing release notes and a regression checklist for subscriptions in an expense-tracking app.

3. Watch the graph run, open any node to read its prompt and output, and find the final answer beside the graph.

To check the plan before anything runs, turn off automatic start in **Settings → Execution**. You can also pick a single agent to skip planning, or build the graph by hand.

## Save, schedule and share workflows

- **Save.** Choose **Save workflow**. *Structure only* keeps roles, dependencies, deliverables and runtime settings, and writes fresh briefs for the next task. *Full* keeps every node's brief too. Saving again under the same name adds a version.
- **Schedule.** Open a workflow and choose **Schedule a run**. Bercy captures the nodes, brief and attachments. Run it once, every few hours, daily or weekly, in local time. Each occurrence is a separate run. Keep Bercy open, even minimized. After sleep or a restart it runs the most recent missed occurrence.
- **Share.** In **Saved workflows**, choose **Export** to write a `.bercy.json` file, or **Import** to add one to your library. Files carry the workflow definition only, never past task text, results or files. A full workflow includes node briefs, so check them before sharing. Imported files are validated and rebuilt before use.

## Runtimes

| Runtime | Local command | Integration |
| --- | --- | --- |
| Codex | `codex` | App server with image input, streaming output and mid-run instructions |
| Claude Code | `claude` | Streaming JSON with image input and tool events |
| OpenClaw | `openclaw` | CLI connected to your configured Gateway |
| DeepSeek Harness | `dsh acp` | Sessions over the Agent Client Protocol |
| Pi | `pi` | JSON events with image input. Commands are offered only to nodes that need them |

Add any other ACP-compatible runtime in **Settings**. Each runtime runs two nodes at once by default, adjustable from one to four. Bercy routes each node to a runtime with the capabilities it needs (writing files, running commands or going online), or you assign one yourself.

## How it works

Choose **Projects → + → Add folder** to use an existing local repository. Start a task with **+** beside its project name to read, edit, and test files in that folder. You can change the folder in **Manage project**. Workflows that have already started keep their original directory.

Workflow state and execution records live in local SQLite storage. Bercy sends prompts only to the runtimes you connect, under your own accounts. For software projects, nodes share one project directory with separate owned paths. The project's acceptance command runs once the project nodes finish, according to your approval settings.

```sh
npm test              # run the test suite
npm run package:mac   # write the Apple Silicon app and DMG to build/
```

Run the real Codex regression cases with `npm run test:regression`. To test code development, changes and test generation only, use `npm run test:regression -- coding`. [Regression guide](regression/README.md)

[Planning guide](desktop/planning-guide.en.md) · [Workflow and prompt notes (Chinese)](工作流机制与提示词.md) · [Prompt implementation](desktop/prompts.cjs) · [Desktop process](desktop/) · [Canvas and scheduler](dist/)

## Contributing

Bug reports, runtime adapters and workflow files are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) to get set up.

## License

[MIT](LICENSE). Use, modify and redistribute Bercy freely, including commercially, as long as you keep the copyright notice.

---

<p align="center"><b>Bercy = Branch · Execute · Relay · Converge · Yield</b><br>
The Chinese name, 百溪, means a hundred streams. Each branch flows into the result you take away.</p>
