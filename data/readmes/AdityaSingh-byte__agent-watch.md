# agent-watch

See what all your Claude Code sessions are doing, from one place.

agent-watch is a Claude Code plugin. Run several sessions at once, type `/watch` in any of them, and a console shows every other session: whether it is working, idle or waiting on you, what it changed, how its tests went, what went wrong, what it shipped, the tokens it used, and every subagent it started. Press `r` and a model reviews a session's recent work for you. Turn on `/route` and it also puts each delegated task on the cheapest model that can do it.

![The /watch console stepping through five sessions: one waiting on you, two working, two idle](docs/media/console.gif)

## Why

With four or five Claude Code sessions running, the hard part is no longer the work, it is keeping track of it. Which one is stuck on a question? Which one said "done" without running the tests? Which one pushed to the wrong branch? agent-watch answers that at a glance, without switching to each chat and scrolling back.

## Quick start

At the prompt of a Claude Code terminal session:

```
/plugin install agent-watch --marketplace AdityaSingh-byte/agent-watch
```

Answer `y` to add the marketplace and pick the user scope, so it is there in every session. Then:

| Type | To |
| --- | --- |
| `/watch` | open the console beside your conversation |
| `/watch-web` | open the same view as a page in your browser |
| `/route on` | route delegated tasks to haiku, sonnet or opus by what they need |

## What it shows

For each session running on your machine:

- **Status**: working, idle, or waiting on you (an open question, a plan to approve, or a tool call that may be waiting for your approval).
- **Asked, Replied, Finished**: the last request, the last reply, and whether that request is done, including whether tests ran after the last edit.
- **Files** it changed, with lines added and removed and how often each file was edited.
- **Tests** it ran, with pass and fail counts read from the runner's output.
- **Issues**: failed tool calls, blocked commands, your interruptions and corrections, API errors, and files edited over and over.
- **Shipped**: commits, pushes, PRs opened or merged, and deploys.
- **Tokens**: new input, cache reads and output, subagents included.
- **Agents**: each subagent the session started, the model it runs on, its task, its tokens, and why it got that model.
- **Review with AI**: on request, a model reads the session's recent activity and lists what went wrong or is at risk.

## The console: `/watch`

Open Claude Code in a terminal and type `/watch`. The console opens beside the conversation and updates every few seconds.

| Key | Does |
| --- | --- |
| `1` to `9` | Show that session's details |
| `r` | Review the shown session with AI |
| Esc | Back to the prompt; the console stays open |
| ctrl+x x | Close the console |

Press `r` on a session to have a model read its recent activity and say what went wrong or is at risk:

![An AI review of a session: the lint claim was never re-checked, the commit came before the full suite passed, and a flag file changed](docs/media/review.png)

Where no pane can be drawn (an editor's chat panel such as VS Code's, or a window too narrow), `/watch` prints a short text snapshot instead.

## The browser page: `/watch-web`

Type `/watch-web` in any Claude Code session, the VS Code panel included. A page opens in your browser and updates every few seconds while that session runs; `/watch-web stop` ends the updates. It shows everything the console does, and the reviews made from it.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/media/dashboard-dark.png">
  <img alt="The /watch-web page: the session list on the left, the chosen session's review, agents, files, tests, issues and what shipped on the right" src="docs/media/dashboard-light.png">
</picture>

The page is a local file, `~/.claude/agent-watch/index.html`. There is no server and no open port.

## Routing: `/route`

Off by default. `/route on` turns it on for all your sessions, `/route off` turns it off, and `/route` alone lists this session's routes.

Your main conversation keeps its model. Each task it hands to a subagent is placed on a model by what the task needs, never above your main model:

| Model | Gets |
| --- | --- |
| haiku | pure lookups: `find`, `list`, `summarize`, the Explore agent, when that is all the task asks |
| sonnet | routine changes: `fix`, `add`, `update`, `write tests` |
| opus | work on something weighty (security, migrations, concurrency, payments, auth) that asks for a change or for judgment |

Rules decide the clear cases instantly. Anything that asks for judgment (why, investigate, plan, design, review, compare) or only names a weighty subject goes to one short Haiku call that classifies it; if that fails, the task keeps your main model.

When a subagent on haiku or sonnet fails, a note from agent-watch follows its result, suggesting the main model run the same task again one model up. The main model decides and starts that retry itself, so it passes your permission mode as any agent call does. The retry is linked to the failed attempt, may go above your main model, and the chain stops at opus.

A run counts as failed when it says, at the start or end of its report, that it could not do the task; when its last test run failed; when its last three tool calls failed; or when it returned nothing. Some endings are shown but never retried: a run you stopped, one whose tool calls you denied, a refusal, and an API error.

Every routing decision, failure and retry shows under **Agents** in `/watch` and `/watch-web` for the sessions you are watching; `/route` shows the current session's own.

Never re-routed: forks, workflow agents, teammates, and custom agent types, which keep the model their definition gives them. A model the main model named itself is kept, though a failure on it can still suggest a retry.

## Settings

| Setting | Where | Does |
| --- | --- | --- |
| Review model | `/config` | The model **Review with AI** asks: `haiku`, `sonnet` (the default) or `opus` |
| Routing | `/route on`, `/route off` | Kept across your sessions |
| `AGENT_WATCH_ROOT` | environment | The folder to watch in place of Claude Code's own: another machine's copy, or a demo |

## How it works

Every running Claude Code session registers itself in `~/.claude/sessions/` and writes its conversation to a transcript under `~/.claude/projects/`, with each subagent's beside it. agent-watch reads those files. It never changes them, sends nothing to another session, and needs no setup in the sessions it watches. Scanning starts only when you run `/watch` or `/watch-web`, and stops when you close the console or stop the page.

Reading is incremental: after the first pass, only what each transcript gained is read. A transcript over 16 MB is read in detail from its last 16 MB, so for very long sessions the files, tests and issues cover recent activity; its token count still covers the whole session.

Routing hooks the moment a subagent is started (to pick its model) and the moment its result reaches the main model (to judge it and, if it failed, add the retry note).

### Privacy

- Everything is read and kept on your machine. The browser page and its data live in `~/.claude/agent-watch/`, a folder only your user can read, like the transcripts themselves. The data file gets a new random name each time you run `/watch-web`, so no other web page opened from your disk can find it, and it is deleted when you stop the page.
- Two model calls leave your machine, on your own account: **Review with AI** sends a summary of the shown session's recent activity (requests, commands with short output, file names, test results) to the review model, and routing an unclear task sends its title and text to Haiku to classify it.
- With routing on, each session writes its routes (task titles, models, outcomes) to `~/.claude/agent-watch/routes/<session id>.json`, in the same private folder. The file goes when the session ends or starts over with `/clear`, and one left by a crash is cleared after a day.

## Requirements and limits

- Claude Code with plugin hooks, tested on 2.1.299 to 2.1.301. The plugin hooks API is early access and can change between Claude Code releases.
- macOS and Linux. It uses `ps`, `sh`, `tail`, `head`, `perl` and `open` or `xdg-open`.
- The console needs a terminal; the VS Code chat panel cannot draw plugin panes yet, so use `/watch-web` there.
- "Waiting for your approval" is inferred from a tool call that has run long, so a slow command reads the same way.
- Issues are found by rules. They flag what failed, not whether the approach was right; the AI review covers that.

## FAQ

**Does it slow my sessions down?** No. In a session where you have not run `/watch` or `/watch-web` and routing is off, its hooks return at once. Watching reads only what each transcript gained, every three seconds, from the one session that watches.

**Does it send my code anywhere?** Only when you press `r` (a summary of that session's activity goes to the review model) or when routing classifies an unclear task (its title and text go to Haiku). Both are calls on your own account. Nothing else leaves your machine.

**Can it change what my other sessions do?** Watching never does. With routing on, it picks the model of each subagent your sessions start and may add a note suggesting a retry; the main model always decides.

## Uninstall

At a Claude Code prompt, or as `claude plugin uninstall agent-watch` from a shell:

```
/plugin uninstall agent-watch
```

Then delete `~/.claude/agent-watch/` to remove the page and any routes files.

## Development

```
claude plugin validate .
claude plugin test .
```

| Path | Holds |
| --- | --- |
| `hooks/register.tsx` | the hooks module: commands, the console pane, the scan loop, reviews, the browser page feed |
| `hooks/reader.ts` | finding live sessions and reading transcripts incrementally |
| `hooks/transcript.ts` | turning transcript rows into status, files, tests, issues, shipped work and tokens |
| `hooks/router.ts`, `hooks/routing.ts` | the routing rules and the hooks that apply them |
| `hooks/shell.ts` | reading shell commands: commits, pushes, PRs, deploys, test runs |
| `web/index.html` | the browser page |
| `tests/` | the test suite, run by `claude plugin test` |
| `docs/demo/` | the scripts that make the pictures in this README |

To try a change, run `claude --plugin-dir .` from the repo.

### The pictures in this README

They show made-up sessions of a fictional team, never real work. To make them again (needs `ffmpeg`, the Python packages `pyte` and `pillow`, and a logged-in `claude`):

```
python3 docs/demo/seed.py /tmp/agent-watch-demo
python3 docs/demo/record.py --root /tmp/agent-watch-demo --plugin . --out docs/media --review
kill $(cat /tmp/agent-watch-demo/pids.txt)
```

## License

[MIT](LICENSE)
