# deadweight

**Find the dead weight in your Claude Code setup.**

Every plugin, skill, MCP server and hook you install adds text to *every single request* Claude Code sends, before you type a word. `deadweight` measures that overhead from your own session history, tells you exactly where it comes from, shows what you never actually use, and removes it with one undoable command.

[![CI](https://github.com/msertdev/deadweight/actions/workflows/ci.yml/badge.svg)](https://github.com/msertdev/deadweight/actions/workflows/ci.yml)
[![crates.io](https://img.shields.io/crates/v/deadweight.svg)](https://crates.io/crates/deadweight)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Platforms](https://img.shields.io/badge/platforms-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey)
[![Donate](https://img.shields.io/badge/donate-PayPal-00457C?logo=paypal)](https://www.paypal.me/CansuAvci)

<p align="center">
  <img src="assets/demo.svg" alt="deadweight output: every request carries 61.2k tokens before you type; 151 of 214 skills listed without a description" width="760">
</p>

An example run. Yours will look different, and that's the point.

<details>
<summary>Same output as text</summary>

```text
$ deadweight

  Before you type a word, every request carries 61.2k tokens
  measured from your latest session; median of recent sessions 63.8k
  ~19.4k from your setup · ~41.8k from Claude Code itself (system prompt + 18 tools)

  WHAT YOUR SETUP ADDS
  Deferred tool names (412)            ~7.1k  ████████████████████████
  Skill listings (214)                 ~6.2k  █████████████████████
  Hook injections (3)                  ~3.4k  ███████████▌
  MCP server instructions (4)          ~2.1k  ███████▏
  Agent listings (12)                   ~600  ██

  BIGGEST SOURCES
  name                           type           tokens    used  contents
  github                         mcp server      ~3.9k    212×  91 tools
  kitchen-sink                   plugin          ~3.6k   never  64 tools · 22 skills
  workflow-kit                   plugin          ~2.6k     14×  hooks 2.2k · 11 skills
  playwright                     mcp server      ~1.4k   never  33 tools
  devops-pack                    plugin          ~1.3k      3×  hooks 1.2k · 6 skills
  marketing-suite                plugin          ~1.1k   never  18 tools · 14 skills
  linear                         mcp server       ~810     37×  41 tools

  PROBLEMS
  ✗ 151 of 214 skills are listed without a description: the skill listing is full
      (~30.0k characters). Claude sees only their names, so it can't tell when to use them.
      Including 4 you actually use: pdf-tools:extract, review-pr, workflow-kit:plan, +1 more
      Make room: hide what you don't use (deadweight fix), or set "skillListingBudgetFraction": 0.02 in settings.json
      (default 0.01; the extra room costs up to ~8.3k tokens per request).
  ✗ 2 MCP servers failed to connect at startup
  ! 9 MCP servers never signed in, still listing 18 auth-only tools
  ! 3 skill names are listed more than once
  ! 198 of 214 listed skills were not used in 30 days (~5.1k per request)

  Run deadweight fix to disable 6 unused plugins and hide 11 unused skills and save ~6.8k tokens per request.

  UNUSED, BUT YOURS TO REMOVE
  mcp server playwright              ~1.4k   claude mcp remove "playwright"

  LOADED IN EVERY PROJECT, USED IN ONE OR TWO
  mcp server linear                  ~810    37× in /home/you/code/app (of 9 projects)
    in .claude.json, move "linear" from the top-level mcpServers into projects > "/home/you/code/app" > mcpServers
```

</details>

## Why this matters

- **Your usage limit drains faster.** The overhead is resent on every turn of every session.
- **Your context window fills sooner**, so sessions compact earlier and Claude loses track of your actual work.
- **Claude gets worse at picking the right skill.** This one surprised us: Claude Code caps the skill listing at roughly 30,000 characters. Once you go past it, skills are listed **by name only, without their descriptions**. With a few hundred skills installed, most of them end up as bare names, and Claude has no way to tell when to use them. Unused skills crowd out the ones you rely on.

None of this shows up anywhere in the UI. Plugins get installed one at a time and the total is never visible.

## Install

```sh
cargo install deadweight
```

Or grab a prebuilt binary for macOS, Linux or Windows from [Releases](https://github.com/msertdev/deadweight/releases). It's a single binary with no runtime dependencies.

deadweight is not on npm or PyPI. Packages named `deadweight` there are unrelated projects, so `npx deadweight` will not run this tool.

## Usage

```sh
deadweight                 # audit: what every request carries and where it comes from
deadweight --all           # list every source, not just the biggest
deadweight --days 60       # count anything used in the last 60 days as "used"
deadweight --json          # machine-readable output

deadweight fix --dry-run   # show what would change
deadweight fix             # disable unused plugins, hide unused skills (asks first)
deadweight scope           # load what you use in a few projects only in those (asks first)
deadweight undo            # put back the latest fix or scope

deadweight card            # save your totals as a PNG to share (no names on it)
```

`fix` options:

| flag | effect |
| --- | --- |
| `--keep NAME` | never touch this plugin or skill, or `connectors` (repeatable) |
| `--park-skills` | move unused skills into the backup folder instead of hiding them |
| `--include-hooked` | also disable unused plugins that run hooks |
| `--yes` | don't ask for confirmation |
| `--force` | run even with fewer than 5 sessions of history |

Restart Claude Code after `fix`, `scope` or `undo` to load the new setup.

### Load things only where you use them

`fix` only touches what you never use. But most setups also carry things you *do* use, just not everywhere: the frontend plugin you need in two web projects still loads in your CLI project, your infra repo and everything else, on every request.

`deadweight scope` finds them in your session history and keeps each one on only in the projects that used it:

```text
$ deadweight scope --dry-run

  Load these only in the projects that use them
  off in ~/.claude/settings.json, on in each project's .claude/settings.local.json
    plugin frontend-kit              ~5.4k   saved in 9 projects (19 of 49 sessions)
      on /home/me/code/shop
      on /home/me/code/landing
    plugin workflow-kit              ~1.2k   saved in 11 projects (45 of 49 sessions)
      on /home/me/code/api
    skill video-render               ~286    saved in 11 projects (45 of 49 sessions)
      on /home/me/code/promo

  Saves ~6.9k tokens per request in the projects that never use them. Undo any time with deadweight undo.
```

Nothing changes in the projects that use them: Claude Code reads `.claude/settings.local.json` over your user settings. A plugin is picked when it was used in at most 5 projects and at most half of the projects you worked in. `scope` takes the same `--keep`, `--include-hooked`, `--dry-run`, `--yes` and `--force` flags as `fix`.

Plugins whose hooks act on your work in any project (on every edit or shell command, or when Claude stops) are left alone unless you pass `--include-hooked`. Plugins whose hooks only add context at session start, or react to their own skills, are scoped like any other.

User-scope MCP servers used in a few projects are listed with where to move them in `.claude.json`; deadweight doesn't edit that file, because it can hold credentials and Claude Code rewrites it while running.

### Share your numbers

`deadweight card` writes `deadweight-card.png`: your total, how much of it is your setup, unused skills, and what `fix` would save. It shows totals only, never a plugin, skill or server name. `--output card.svg` gives you the SVG instead.

<p align="center">
  <img src="assets/card.png" alt="deadweight card: 61.2k tokens on every request, 198 of 214 skills never used, fix saves 6.8k per request" width="600">
</p>

Post yours. I'd like to see the biggest one.

## Use it from inside Claude Code

deadweight ships as a Claude Code plugin too, so you can ask Claude to audit its own setup:

```text
/plugin marketplace add msertdev/deadweight
/plugin install deadweight@deadweight
/deadweight
```

The plugin needs the `deadweight` binary on your `PATH` (see [Install](#install)). It adds a single short line to the skill listing, about 18 tokens.

## How it works

Claude Code keeps a transcript of every session in `~/.claude/projects/`. Alongside the conversation it records what was loaded at startup: the skill listing, the deferred tool names, MCP server instructions, the agent listing, hook output, and the token usage the API billed for each request.

deadweight reads those records:

1. **Measure.** The total comes from the API usage of the first request of your latest session (input + cache write + cache read tokens). This number is measured, not estimated.
2. **Attribute.** Each skill line, tool name, instruction block, agent and hook injection is traced to the plugin, skill, MCP server or connector that added it. Hook commands are matched against each plugin's `hooks.json`. Sizes are converted to tokens from text length; whatever your setup doesn't explain is Claude Code's own system prompt and tools.
3. **Check usage.** Every transcript from the last 30 days (including subagents) is scanned for `Skill` calls, MCP tool calls, agent launches and slash commands.
4. **Diagnose.** Failed and never-authenticated MCP servers, duplicate skill names, skills that lost their description, and single skills with very large descriptions.
5. **Scope.** Usage is also counted per project (the folder each session ran in). A plugin, user skill or user-scope MCP server that was only used in a few projects is loaded everywhere else for nothing; `deadweight scope` moves plugins and skills, and for MCP servers deadweight says where to move them.

On the author's machine, 1.4 GB of transcripts (41 sessions, 400+ subagent runs) are scanned in about a second, in parallel.

## Safety

- **Read-only by default.** Only `fix`, `scope` and `undo` write anything, and all three ask first.
- **Project files are left the way they were.** `scope` adds two keys to a project's `.claude/settings.local.json` and keeps everything else in it. A file it creates is kept out of git the way Claude Code does it (a line in the repository's `.git/info/exclude`, unless git already ignores it), and `undo` removes the file, the folder and that line again.
- **No secrets are read.** From `.claude.json` deadweight takes only MCP server *names*, never commands, environment variables or headers. A test checks that secret values never reach the output.
- **Nothing is deleted.** Plugins are disabled in `settings.json` (`enabledPlugins: false`), not uninstalled. Unused user skills are hidden from the model with `skillOverrides` (`"user-invocable-only"`), so `/name` still runs them; `--park-skills` moves them into the backup folder instead. If none of your claude.ai connectors was used, `disableClaudeAiConnectors` switches them off in Claude Code (they stay connected on claude.ai).
- **Everything is backed up.** Each `fix` writes a manifest and a copy of `settings.json` to `~/.claude/deadweight/backups/<timestamp>/`. `undo` reverts the latest one.
- **Conservative.** Plugins that run hooks may be doing useful work deadweight can't see (memory, safety checks), so they are skipped unless you pass `--include-hooked`. `fix` refuses to run with fewer than 5 sessions of history.
- **No network.** deadweight never makes a network request.

MCP servers in `.claude.json` are never edited, and neither is a single claude.ai connector while you still use others; deadweight prints the command that removes them, or where to move them, instead.

## FAQ

**Does it work with `CLAUDE_CONFIG_DIR`?** Yes, and you can also pass `--config-dir`.

**Why does `fix` skip a plugin I never use?** It runs hooks. Review it, then run `deadweight fix --include-hooked`, or disable it yourself with `/plugin`.

**I started using a scoped plugin in another project.** Turn it on there with `claude plugin enable <name>@<marketplace> --scope local`, or run `deadweight undo` to go back to loading it everywhere.

**My usage looks wrong.** Claude Code deletes transcripts older than `cleanupPeriodDays` (30 by default), so deadweight can't see further back than that. Use `--keep` for anything you use rarely but want to keep.

**Is it affiliated with Anthropic?** No. It's an independent open-source tool that reads files Claude Code writes on your machine.

## Contributing

Issues and pull requests are welcome. Start with [CONTRIBUTING.md](CONTRIBUTING.md) and the [good first issues](https://github.com/msertdev/deadweight/labels/good%20first%20issue); the whole codebase is about 4,200 lines of Rust.

If deadweight misattributes something in your setup, run `deadweight --json`, remove anything private, and open an issue with the relevant part.

## Support

If deadweight saved you tokens, a star helps other people find it. If you'd like to chip in, you can [donate via PayPal](https://www.paypal.me/CansuAvci). Thank you!

## License

MIT © [Murat Sert](https://github.com/msertdev)
