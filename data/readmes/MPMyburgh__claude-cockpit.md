# claude-cockpit

![/cockpit: see what every Claude Code agent is doing](assets/cockpit-card.png)

A Claude Code mod that adds a sidebar showing what the main thread, every subagent and every background task is doing right now.

![The cockpit sidebar docked next to a Claude Code chat while three agents run](assets/cockpit-screenshot.png)

The chat on the left is blurred. The sidebar on the right is what the mod adds.

## Why

When Claude launches three agents in the background, the chat tells you they started, and then you wait.

While you wait there are a few things you want to know. Is each agent still working, and on what? Has one gone quiet? Is one stuck until you approve a command? How much context has the main thread used, and what has the batch cost so far?

Cockpit keeps those answers in a sidebar next to the chat and redraws it every second while anything is running.

## What it shows

### MAIN

The conversation you are typing in.

- `state`: working, with a running clock, or idle, with how long it has been idle and how long the last turn took.
- `model`: the model, the effort level, and the request and tool counts for this turn. A red `errors` line appears when calls have failed this turn.
- `ctx`: a bar with the percentage and the tokens used out of the window. It turns yellow at 80% and red at 90%.
- `cache`: the minutes of prompt cache left, counted from the last request.
- `now`: the open tool call and how long it has been running. Between calls it says `thinking`, `writing reply` or `preparing Bash call`, and it turns red with `needs approval` when a permission prompt is waiting.
- `last`: the last six finished calls, each with ✓ or ✗.

### BACKGROUND

The shells, Monitors and Workflow runs that the main thread started in the background. A running task shows its elapsed time, and a finished one is marked done, failed, stopped or expired. A running Monitor also shows how many events it has sent.

### AGENTS

One block per subagent. The heading carries the counts and the estimated cost of all of them together.

- A running agent shows elapsed time, tool calls, errors, context size, estimated cost, model, effort and agent type.
- Under that is what it is doing this second: the open tool call, `thinking`, or what it is waiting on.
- After three minutes with no activity the line turns yellow and reads `quiet 3m12s`. When the agent is waiting on a permission prompt it turns red and reads `needs approval`.
- An agent started by another agent is indented under its parent, and Workflow agents are grouped under their run.

Click an agent to open it. You get its last eight tool calls and its answer, or its latest message if it is still working. From there you can view its transcript, stop it, or type a note that is sent to it.

You also get a toast when a background agent finishes. A native notification fires when an agent fails, when the whole batch is done, and when a background shell, Monitor or Workflow finishes or fails, so you can work in another window in the meantime.

When the sidebar is closed, one line above the prompt carries the summary:

```
● main 3m05s · agents 1 running · 1 stalled  │  thinking  /cockpit
```

## Install

You need Claude Code with mod support. This was built and tested on Claude Code 2.1.322 on macOS.

```zsh
git clone https://github.com/MPMyburgh/claude-cockpit ~/.claude/mods/cockpit
```

To load the mod in every session, add its absolute path to `CLAUDE_CODE_PLUGIN_DIRS` (colon-separated) in `~/.claude/settings.json`:

```json
{ "env": { "CLAUDE_CODE_PLUGIN_DIRS": "/Users/you/.claude/mods/cockpit" } }
```

For a single session, use `claude --plugin-dir ~/.claude/mods/cockpit` instead.

Then start `claude`.

## Use

```
/cockpit          # open the sidebar
/cockpit clear    # remove finished agents and background tasks from it
```

In the fullscreen view the sidebar opens by itself the first time. Rows are clickable, and the buttons have hotkeys: `v` view transcript, `s` stop, `m` back to main, `c` clear finished.

## Things to know

- Costs are estimates, and only subagents get one. `hooks/agents.ts` holds a small table of prices per model family and charges cache writes at the 1-hour rate. A model that isn't in the table shows no cost. Edit the table when prices change.
- The `cache` line assumes the 1-hour prompt cache, which is why it says `(1h assumed)`. If your sessions use the 5-minute cache, change `CACHE_TTL_MS` in `hooks/register.tsx`.
- An agent that was already running when the mod loaded is picked up from Claude Code's own agent list. Its clock and counts start from the moment cockpit first saw it.
- A note you type in the sidebar reaches the agent as a user message that begins `[note from the user, via cockpit]`.
- The colours are hex constants at the top of `hooks/register.tsx`. They were picked for a Dracula terminal theme, so change them to suit yours.
- Cockpit reads tool-call labels, token counts and agent messages inside your session to draw the sidebar. It makes no network calls. Its only output is the sidebar, the summary line, toasts and system notifications.

## Tests

```zsh
cd ~/.claude/mods/cockpit && claude plugin test .
```

## License

MIT
