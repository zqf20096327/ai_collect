# Sidecar for OpenCode

**An OpenCode chat sidebar and GUI for VS Code.** Sidecar for OpenCode is a free, open-source extension that puts the [OpenCode](https://opencode.ai) coding agent in a chat panel beside your code, in VS Code, Cursor, Windsurf and VSCodium: every step on one timeline, live subagents you can open and stop, permission requests and questions answered where you type, `@` mentions, images, fork and rewind, and the agent's edits in VS Code's own diff editor.

![OpenCode 2.x](https://img.shields.io/badge/OpenCode-2.x-0a0a0a) ![VS Code 1.95+](https://img.shields.io/badge/VS%20Code-1.95%2B-0a0a0a) ![License: MIT](https://img.shields.io/badge/license-MIT-0a0a0a)

<p align="center"><img src="docs/marketplace/demo.gif" alt="Sidecar for OpenCode in action: a prompt sent from the chat sidebar, each step landing on the timeline (read, run, edit), the diff, and live subagents with one stopped" width="900"></p>

Free and open source. An independent community project, not affiliated with OpenCode; the official OpenCode extension is `sst-dev.opencode`.

## Why Sidecar

OpenCode is a capable agent. Sidecar is built so you can see and steer everything it does without leaving the editor.

- **Built on OpenCode's own API.** Sidecar talks to the OpenCode 2 service on your machine through its v2 HTTP API. Your sessions, models, providers, agents, commands, skills and permission rules are OpenCode's, so nothing is locked in: open the same session in OpenCode's terminal UI and Sidecar follows along, including rewinds and model changes made there.
- **Nothing hidden.** Each prompt gets a timeline of what the agent did: thinking time, every tool call with its input and output, diffs with your theme's syntax colors, and each subagent with its exact prompt, live activity and report.
- **You stay in control.** Nothing is ever approved for you. Permission requests, including those raised deep inside a subagent, wait in place of the message box until you answer, and you can tell the agent what to do instead. Budget Guard stops a runaway task at a cost or step limit you choose.
- **Made for VS Code.** Theme colors only (dark, light and high contrast), a layout that works from a 300 px side bar to a wide editor tab, keyboard access throughout, native notifications, and editor tabs for long output.
- **Private by design.** Sidecar connects only to your local OpenCode service, sends nothing anywhere else and collects no telemetry. It is tested with hundreds of unit tests and a headless-browser suite, and its OpenCode calls are checked against a live OpenCode 2 service.

## OpenCode coverage

| OpenCode                                   | In Sidecar                                                                                          |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------- |
| Sessions                                   | History with search, rename, fork from any prompt, archive and restore, new session                 |
| Prompts and delivery                       | Send, **steer** the running task or **queue** the next message; switch, edit or remove pending ones |
| Agents and models                          | Agent switch (Shift+Tab), models by provider, variants, defaults per workspace                      |
| Tools                                      | A timeline row per call: shell IN/OUT, reads, edits with diffs, writes, searches, and the rest      |
| Subagents                                  | Live rows with prompt, activity, Stop and Open; their requests and reports come back to you         |
| Permissions                                | Yes, Always allow (when offered), No, or No with an instruction for the agent                       |
| Questions                                  | A tabbed form with options, an Other answer and descriptions                                        |
| Commands and skills                        | The `/` palette with OpenCode's commands (yours too), `@skill` and `@agent` mentions                |
| Context                                    | Files, folders and selections, `@` mentions found by OpenCode's search, pasted images               |
| Rewind                                     | Rewind with or without code, and Restore or Apply a rewind staged in another client                 |
| Shell, compaction                          | `!command`, `/compact`                                                                              |
| Goals                                      | `/goal`: the objective, then each round's reason and next step                                      |
| Todos                                      | The agent's todo list as a checklist (OpenCode's experimental `todowrite` tool)                     |
| Background jobs                            | A row when a background shell, image or video job finishes, with its result or file                 |
| Usage                                      | Context, cost, steps, cache hits and a prompt-cache estimate                                        |
| Agent changes                              | Kept apart from your own edits, in VS Code's diff editor                                            |
| Other clients (terminal UI, other windows) | Followed live: new sessions, renames, rewinds, agent and model choices                              |

## A tour

- **One timeline per prompt.** A dot per step: text, thinking time, every tool call and every subagent. The prompt you're reading stays pinned while you scroll, and **Rewind ↺** takes the session back to just before it.
- **Readable tool calls.** Shell commands as IN/OUT boxes, reads as file links, edits as changed lines with your theme's syntax colors, old beside new in a wide panel with a divider you can drag (click for the diff editor). Click IN, OUT or a subagent's prompt to open it in full in an editor tab. Prefer it compact? Set `opencodeSidecar.activity` to `grouped`.
- **Live subagents.** Each one shows its task, prompt, current activity, tool count and time, with **Stop** and **Open ›** into its own conversation. Its report comes back as one line you can expand.
- **Answer where you type.** Permission requests and questions replace the message box until answered: _1 Yes_, _2 Yes, always allow_ (when OpenCode offers it), _3 No_, or type what the agent should do instead. Nothing is ever approved for you, and sensitive paths get a warning.
- **A message box with everything at hand.** Type **@** to mention a file, folder, subagent or skill. Paste or drop a screenshot, or use **+** for a file, the selection, a workspace search or an image. **/** opens the action palette: OpenCode's commands, `/compact`, `!command`, model, session and settings. A ring fills with the context in use (click it for context, cost, steps, the task budget and Compact), and the ◷ clock estimates the prompt cache for models that use one. The model pill has variant and Budget Guard sliders. Shift+Tab switches the agent. While the agent works you can **steer** it or **queue** your next message.
- **Guard rails.** Budget Guard stops runaway tasks at a local cost or step limit. Agent changes are kept apart from your workspace changes. Native notifications tell you when a task completes, needs input (saying what it asks), fails or is stopped; a count on Sidecar's icon shows answers that are waiting, even with the panel hidden.
- **Sessions.** **Fork** a conversation from any prompt into a new session, **archive** sessions you are done with, and search **History**. **Copy** and **Bookmark** sit under every final answer.

|                                                                    Timeline                                                                    |                                                               Tool calls                                                               |                                                                           Subagents                                                                            |
| :--------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| <img src="docs/marketplace/screenshots/timeline.png" alt="Two turns with a pinned prompt, tool calls, answers, Copy and Bookmark" width="250"> | <img src="docs/marketplace/screenshots/tools.png" alt="A read, an edit with its changed lines and a failed shell command" width="250"> |                   <img src="docs/marketplace/screenshots/subagents.png" alt="Subagent rows and a subagent's permission request" width="250">                   |
|                                                             **A subagent's view**                                                              |                                                              **Question**                                                              |                                                                       **Action palette**                                                                       |
|     <img src="docs/marketplace/screenshots/subagent-view.png" alt="A subagent's own conversation with a way back to the chat" width="250">     |      <img src="docs/marketplace/screenshots/question.png" alt="A question in place of the message box, with options" width="250">      |                    <img src="docs/marketplace/screenshots/commands.png" alt="The / action palette with sections and a filter" width="250">                     |
|                                                              **Cache and usage**                                                               |                                                             **Bookmarks**                                                              |                                                                         **@ mentions**                                                                         |
|        <img src="docs/marketplace/screenshots/usage.png" alt="Prompt cache estimate, context, cost, steps and task budget" width="250">        |            <img src="docs/marketplace/screenshots/bookmarks.png" alt="The Bookmarks popover with two answers" width="250">             | <img src="docs/marketplace/screenshots/mentions.png" alt="The @ list above the message box: folders, files and subagents, with an image attached" width="250"> |
|                                                                **Budget Guard**                                                                |                                                           **Agent changes**                                                            |                                                                         **First run**                                                                          |
|   <img src="docs/marketplace/screenshots/budget.png" alt="Budget Guard stopped the task with Continue once and Increase budget" width="250">   |  <img src="docs/marketplace/screenshots/agent-changes.png" alt="Agent changes per file, separate from workspace changes" width="250">  |               <img src="docs/marketplace/screenshots/onboarding.png" alt="The setup card with a checklist and Sign in to OpenCode" width="250">                |

## Requirements

- VS Code 1.95 or newer, in a trusted workspace (Sidecar is disabled in Restricted Mode).
- [OpenCode](https://opencode.ai) **2.x** with its background service. OpenCode 1.x is not supported.
- A model in OpenCode: its free models, your OpenCode account, or another provider connected in OpenCode. Usage and costs are between you and your provider.

## Getting started

1. Install **Sidecar for OpenCode** (`cadogy.opencode-sidecar`):
   - **VS Code:** search for it in the Extensions view, or get it from the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=cadogy.opencode-sidecar).
   - **Cursor, Windsurf, VSCodium and other VS Code-based editors:** install it from [Open VSX](https://open-vsx.org/extension/cadogy/opencode-sidecar), which their Extensions view uses.
   - **Offline:** download the `.vsix` from [Releases](https://github.com/charlesknapp/opencode-sidecar/releases) and run **Extensions: Install from VSIX…**.
2. Click the **Sidecar** icon in the Activity Bar or the Status Bar.
3. Follow the setup card if something is missing. **Install OpenCode** opens [the official install guide](https://opencode.ai/docs#install), **Start OpenCode** runs `opencode service start`, and **Sign in to OpenCode** runs OpenCode's own sign-in in a terminal. The card disappears once everything is ready, so if you already use OpenCode you won't see it.
4. Pick a model in the model pill and start chatting.

**Tip:** drag the Sidecar icon to the **Secondary Side Bar** so the chat sits beside your editor. The panel works from about 300 px wide.

## Using Sidecar

| Key                  | Where                              | What it does                                        |
| -------------------- | ---------------------------------- | --------------------------------------------------- |
| Enter / Shift+Enter  | Message box                        | Send / new line                                     |
| Alt+Enter            | Message box, while the agent works | Send this one the other way (steer ↔ queue)         |
| ↑/↓                  | Empty message box                  | Recall this session's earlier prompts               |
| @, ↑/↓, Enter or Tab | Message box                        | Mention: open the list, move, pick                  |
| Esc                  | Message box                        | Stop the running task                               |
| Shift+Tab            | Message box                        | Switch the agent (Build ↔ Plan)                     |
| 1, 2, 3 / Esc        | Permission request                 | Pick an answer by its number / No                   |
| 1–9, ←/→, Esc        | Question                           | Pick an option, switch questions, cancel            |
| ←/→                  | Slider in a menu                   | Change the variant or Budget Guard level            |
| Ctrl/Cmd+F           | The chat                           | Find in the conversation (Enter / Shift+Enter, Esc) |
| Cmd+Alt+O (macOS)    | Anywhere                           | Focus the chat                                      |

On Windows and Linux, add your own shortcut for `opencodeSidecar.focusChat` (Ctrl+Alt types characters on many keyboard layouts). The Command Palette also has **Sidecar: New Session**, **Stop**, **Show History** and **Export Session to Markdown**; bind any of them in Keyboard Shortcuts.

- **Always-allowed actions.** Choosing _Yes, always allow_ makes OpenCode save a rule for the folder. **/ → Always-allowed actions…** lists them, and you can remove any rule so OpenCode asks again.
- **Jump to latest.** Scroll up while the agent works and a **↓ Jump to latest** pill (with how many steps are new) takes you back to the end.
- **Mentions.** Type `@` and pick from the list, or keep typing to search: files and folders (found by OpenCode), subagents such as `@explore`, and OpenCode's skills. OpenCode reads mentioned files itself, and a mentioned subagent or skill is passed to the agent as such.
- **Images.** Paste or drop a PNG, JPEG, GIF or WebP into the message box, or pick image files with **+ → Attach image…**. Very large screenshots are scaled down. Sidecar tells you when the selected model doesn't list image input in OpenCode.
- **Commands.** Type `/` for the palette, or type `/name arguments` directly. OpenCode's built-in commands (such as `/init` and `/review`) and any you define are listed for the folder. `!git status` runs a shell command through OpenCode.
- **Rewind.** Hover a prompt for ↺ (and Fork). Rewind asks first in a dialog, then removes that prompt and everything after it from the session. _Rewind conversation and code_ also undoes OpenCode's file changes since then. Rewind cannot be undone and is available while the agent is idle.
- **Fork and archive.** Hover a prompt and click **Fork** to continue in a new session that has the conversation before that prompt (the prompt goes into the message box). **Fork session** in the `/` palette copies the whole conversation. The original stays as it was. **Archive** a session from History or the palette; History's **Archived sessions** lists them with **Restore** and **Delete permanently**. **Delete session…** in the palette removes the open one. Deleting always asks first.
- **Code blocks.** Besides **Copy code**, a finished block can be **inserted at the cursor** of your editor (an ordinary edit, so Undo reverts it) or **opened in a new editor** in its language.
- **Export.** **/ → Export to Markdown** (or the command) opens the session as a Markdown document: prompts, answers, tool calls with their commands, decisions and subagent reports, without thinking or long output.
- **Branch and MCP.** The header shows the Git branch the agent works on (from VS Code's Git). **/ → MCP servers…** shows the folder's MCP servers as OpenCode reports them (connected, failed with the reason, needs sign-in).
- **Steer and queue.** While the agent works, a switch in the message box's footer chooses what Enter does: **steer** (the agent reads your message at its next step; blue) or **queue** (it is sent when the task ends; purple, and the box border follows). In a narrow panel the switch shows only the chosen mode, and a click flips it. **Alt+Enter** sends one message the other way. Messages not yet delivered are listed above the box, each with a button to switch it between steer and queue, **Edit** and **Remove**.
- **Budget Guard** is a local per-task limit on cost and steps, set in the model menu. It warns at 80% and then stops the agent through OpenCode's own cancellation, offering **Continue once**, **Increase budget** or **Start new session**. Defaults: Small $0.10 / 20 steps, Medium $0.30 / 50, Large $1.00 / 120, Custom $0.50 / 80. If OpenCode reports no cost, only steps count.
- **Context ring.** It fills as the context window does, from the tokens OpenCode reports after each step and the model's context limit, and turns to your theme's warning colour from 70% and its error colour from 90%. Hover it for the numbers; click it for the session's usage and **Compact conversation**.
- **Prompt cache clock.** It counts down `opencodeSidecar.cacheWarmMinutes` (default 5) from the last step, and shows only when that step reported prompt-cache tokens, so a model without a prompt cache (such as most local ones) never shows it. It is an estimate: OpenCode reports cache tokens, not your provider's timer. Set it to `0` to hide the clock.
- **Agent changes** come from OpenCode's session snapshots, so edits you already had are not counted. **Workspace changes** is the usual HEAD ↔ working tree. When the agent's changes can't be told apart, Sidecar says so instead of guessing.
- **Other clients.** Rewinds, agent and model choices, and session changes made in OpenCode's TUI or other clients show up in Sidecar. A rewind another client has staged but not applied (such as `/undo`) hides the messages it removes, with **Restore** to bring them back or **Apply** to remove them for good. Restoring them lets OpenCode carry on with anything still queued for the session.

### Commands

| Command                      | What it does                                                     |
| ---------------------------- | ---------------------------------------------------------------- |
| Sidecar: Focus Chat          | Reveal the chat and focus the message box                        |
| Sidecar: Refresh Connection  | Re-check OpenCode, account, providers, models and agents         |
| Sidecar: Sign in to OpenCode | Run OpenCode's own sign-in in a terminal                         |
| Sidecar: New Session         | Start a fresh conversation                                       |
| Sidecar: Add Current File    | Attach the active editor's file                                  |
| Sidecar: Add Selection       | Attach the selected lines; also in the editor's right-click menu |
| Sidecar: Stop                | Cancel the running task                                          |

### Settings

| Setting                                            | Default    | Description                                                                                                                                 |
| -------------------------------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `opencodeSidecar.executablePath`                   | empty      | Path to `opencode`; empty searches `PATH` and common install locations.                                                                     |
| `opencodeSidecar.serverUrl`                        | empty      | Use a specific OpenCode server instead of the local background service.                                                                     |
| `opencodeSidecar.allowRemoteServer`                | `false`    | Allow `serverUrl` to point at a non-loopback host.                                                                                          |
| `opencodeSidecar.defaultModel`                     | empty      | `providerID/modelID` to preselect for new workspaces.                                                                                       |
| `opencodeSidecar.defaultAgent`                     | empty      | Agent to preselect, such as `build` or `plan`.                                                                                              |
| `opencodeSidecar.autoStart`                        | `false`    | Start the OpenCode background service when the view opens.                                                                                  |
| `opencodeSidecar.stickyPrompt`                     | `true`     | Keep the prompt of the turn you're reading pinned.                                                                                          |
| `opencodeSidecar.statusWords`                      | `true`     | Playful words (such as _Riding along…_), a new one every few seconds, next to the turning mark while the agent works; off shows _Working…_. |
| `opencodeSidecar.activity`                         | `detailed` | `detailed` shows every tool call; `grouped` folds runs of calls into a line.                                                                |
| `opencodeSidecar.cacheWarmMinutes`                 | `5`        | Your provider's prompt-cache lifetime for the clock; `0` hides it.                                                                          |
| `opencodeSidecar.showUsage`                        | `true`     | Show context, cost and step figures.                                                                                                        |
| `opencodeSidecar.showStatusBarItem`                | `true`     | Show the Sidecar item in the Status Bar.                                                                                                    |
| `opencodeSidecar.budget.default`                   | `medium`   | Budget level for workspaces without a saved choice.                                                                                         |
| `opencodeSidecar.budget.small/medium/large/custom` | see above  | `{ "maxCost": USD, "maxSteps": n }`; `0` disables that metric.                                                                              |
| `opencodeSidecar.budget.warnPercent`               | `80`       | Warn at this share of the budget.                                                                                                           |
| `opencodeSidecar.budget.contextWarnPercent`        | `80`       | Warn when the context window is this full; `0` turns it off.                                                                                |
| `opencodeSidecar.notifications.*`                  | `true`     | `taskComplete`, `needsInput`, `taskFailed` and `budgetStopped` notifications (the first two not while you watch the chat).                  |

## Privacy and security

- Sidecar talks only to **your local OpenCode service** (loopback unless you allow a remote server). It has **no telemetry** and no service of its own.
- **No credentials are stored or requested.** Sign-in and providers are handled by OpenCode; the local service password stays in memory.
- **Workspace content is sent only when you attach or `@`-mention it**, or when the agent reads it through OpenCode's tools under OpenCode's permission rules. Pasted images go to OpenCode with the prompt and nowhere else.
- Nothing is approved automatically. The view runs under a strict content security policy, and every message from it is validated. Logs leave out prompts and file contents and redact secrets.
- Bookmarks (a short excerpt and its session title) are stored locally in VS Code's workspace storage.

Details are in [SECURITY.md](https://github.com/charlesknapp/opencode-sidecar/blob/main/SECURITY.md).

## Known limitations

- Requires OpenCode 2.x and its background service.
- OpenCode reads attached files from disk, so unsaved editor changes are not included (you'll get a reminder).
- The prompt cache clock is an estimate, and provider quotas are not available from OpenCode.
- Reopening a session loads its most recent 400 messages.
- The interface is in English, with a few strings in Arabic.

## Sidecar or the official OpenCode extension?

The official extension, `sst-dev.opencode`, opens OpenCode's terminal UI in a split terminal and passes it your selection and file references. Sidecar is a graphical chat panel instead. Both use the same OpenCode, so you can install both and move between them: a session started in one shows up in the other.

|                         | Official extension (`sst-dev.opencode`)                                   | Sidecar for OpenCode                                                                                                                        |
| ----------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Interface               | OpenCode's terminal UI in a split terminal (Ctrl+Esc / Cmd+Esc)           | A chat panel in the side bar, secondary side bar or an editor tab                                                                           |
| Context from the editor | Shares your selection or tab; inserts file references like `@File#L37-42` | `@` mentions of files, folders, subagents and skills; the selection, files and images from **+**                                            |
| The agent's work        | In the terminal UI                                                        | A timeline per prompt with every tool call, diffs in VS Code's diff editor, live subagents, permission requests in place of the message box |
| Editors                 | VS Code and VS Code-based editors                                         | VS Code, and Cursor, Windsurf and VSCodium via Open VSX                                                                                     |

## FAQ

**What is Sidecar for OpenCode?**
A free, open-source VS Code extension that gives the OpenCode coding agent a full chat interface inside the editor. It works with the OpenCode 2 service already on your machine.

**Is there an OpenCode GUI or chat sidebar for VS Code?**
Yes: Sidecar is one. Install it from the Extensions view (search "OpenCode Sidecar"), click the Sidecar icon, and chat with OpenCode in a panel beside your code. It needs the OpenCode 2 service on your machine; the setup card helps install and start it.

**Does it work in Cursor, Windsurf or VSCodium?**
Yes. Those editors install extensions from Open VSX, where Sidecar is published as `cadogy.opencode-sidecar`.

**Which OpenCode versions does it support?**
OpenCode 2.x, with its background service running. OpenCode 1.x is not supported.

**Can I use local models, such as Ollama or LM Studio?**
Yes, if they are set up as a provider in OpenCode. Sidecar uses whatever models OpenCode offers, so any provider OpenCode supports works here too.

**Is it official?**
No. It is an independent community project and is not affiliated with OpenCode. The official OpenCode extension is `sst-dev.opencode`.

**Do I need an API key, and what does it cost?**
Sidecar is free and needs no key of its own. It uses the models you have in OpenCode: OpenCode's free models, your OpenCode account, or any provider you connect in OpenCode. Model costs are between you and your provider.

**Does it work with my existing OpenCode sessions?**
Yes. Sessions are OpenCode's, so the ones you started in the terminal UI appear in History, and changes made in either place show up in the other.

**Does my code leave my machine?**
Sidecar sends your prompts and the files you attach only to your local OpenCode service. What OpenCode then sends to a model provider is decided by OpenCode and your configuration.

**Which platforms does it run on?**
Wherever VS Code 1.95+ and OpenCode 2.x run: Windows, macOS and Linux. It needs a trusted workspace.

## Like it?

If Sidecar is useful to you, a rating on the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=cadogy.opencode-sidecar&ssr=false#review-details) or [Open VSX](https://open-vsx.org/extension/cadogy/opencode-sidecar/reviews), or a [star on GitHub](https://github.com/charlesknapp/opencode-sidecar), helps other OpenCode users find it. Bugs and ideas are welcome in [Issues](https://github.com/charlesknapp/opencode-sidecar/issues).

## About

Sidecar for OpenCode is an independent, community-built extension. It is not affiliated with, sponsored by or endorsed by OpenCode or its authors; "OpenCode" is used only to say which agent it works with.

## License

MIT. See [LICENSE](https://github.com/charlesknapp/opencode-sidecar/blob/main/LICENSE). Source, issues and releases: https://github.com/charlesknapp/opencode-sidecar
