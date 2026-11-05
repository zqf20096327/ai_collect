**English** | [Русский](README.ru.md)

<p align="center">
  <img src="assets/logo.png" alt="handoff logo" width="140">
</p>

<h1 align="center">handoff</h1>

<p align="center">
  <strong>I built Handoff to keep project decisions, next steps, and test status in one Markdown file.</strong><br>
  Save the context once, then point the next coding session to it.
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/handoff-context"><img src="https://img.shields.io/npm/v/handoff-context?color=4F46E5&label=npm" alt="npm version"></a>
  <a href="https://github.com/hilsetapp/Handoff/actions/workflows/ci.yml"><img src="https://github.com/hilsetapp/Handoff/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="license: MIT"></a>
  <img src="https://img.shields.io/badge/node-%E2%89%A518-339933" alt="node >= 18">
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen" alt="PRs welcome"></a>
</p>

---

I built Handoff after getting tired of repeating project decisions and past failed approaches in every new coding session.

```
npm install -g handoff-context
```

---

## The problem

I move tasks between **Cursor**, **Claude Code**, and **Copilot**. In a new session, I want the next tool to know what I decided, what I tried, and what still needs work:

- ✅ what I decided and why
- 🚫 which approaches I tried and ruled out
- 📋 my next steps
- 🧪 whether tests passed
- 🌿 the state of my working tree

[AGENTS.md](https://agents.md) is useful for stable project instructions. I use Handoff for changing session state: decisions, failed approaches, tests, and next steps. It is a portable file format and CLI, not another chat UI.

## The solution

I built `handoff` to maintain `.handoff/HANDOFF.md`, a structured Markdown snapshot of the working state. One command updates it, and any coding tool that can read Markdown can use it:

| | AGENTS.md | `.handoff/HANDOFF.md` |
|---|---|---|
| Scope | Stable project rules | Live session state |
| Changes | Rarely | Every working session |
| Written by | Humans | `handoff save` (from git + your notes + tests) |
| Answers | "How is this project built?" | "Where were we? What should I do next?" |

I use them for different kinds of context. `handoff sync` adds the Handoff pointer to supported instruction files.

## 60-second tour

```console
$ handoff init                              # detect project + test command
$ handoff next "Write integration tests for sliding sessions"
$ handoff decision "SQLite for token cache: offline-first requirement"
$ handoff failed "redis as a cache - adds infra dependency we don't want"
$ handoff save -m "Finishing the token-refresh flow before release 1.5"

running npm test …
✔ Snapshot saved → .handoff/HANDOFF.md
  notes          1 next step · 1 decision · 1 failed approach (+1 done)
  git            branch feat/token-refresh · 2 uncommitted files (1 file changed, 1 insertion(+))
  tests          PASS (npm test)

$ handoff sync --with claude,cursor

✔ agents wired to your handoff context
  updated        AGENTS.md
  updated        CLAUDE.md
  updated        .cursor/rules/handoff.mdc
```

The generated `.handoff/HANDOFF.md`:

```markdown
# Session handoff - orbit-api

> AI coding agents: read this file at session start, before touching code.

**Focus:** Finishing the token-refresh flow before release 1.5

## Next steps
- [x] Implement token refresh in /auth
- [ ] Write integration tests for sliding sessions

## Decisions made
- 2026-10-10 - SQLite for token cache: offline-first requirement, no extra infra

## Failed approaches (do not retry)
- 2026-10-10 - redis as a cache - adds an infra dependency we do not want

## Working tree
- branch `feat/token-refresh` · HEAD `d95ad84`
- Uncommitted changes (2): 1 file changed, 1 insertion(+)
  - modified `src/auth.ts`

## Tests
- `npm test` - ✅ PASS (exit 0) · 2026-10-10T16:32:49Z
```

When I switch tools, I point the next session to this file. `handoff sync` can add that pointer to supported agent instruction files.

## Commands

| Command | What it does |
|---|---|
| `handoff init` | Create `.handoff/`; auto-detects your test command from `package.json` |
| `handoff save [-m "..."]` | Snapshot git state + notes + test results → `HANDOFF.md` |
| `handoff next "..."` | Record a next step (also `decision`, `failed`, `blocker`) |
| `handoff done 1 2` | Mark next-steps done (numbers from `handoff show`) |
| `handoff diff` | Compare commits, working-tree paths, and notes with the last snapshot |
| `handoff show` | Status overview; warns when the tree or notes changed since the snapshot |
| `handoff sync [--with ...]` | Wire agent files: `AGENTS.md`, plus `claude`,`cursor`,`copilot`,`gemini` |
| `handoff archive` | End the session: archive the snapshot, reset the notes store |
| `handoff clear` | Drop completed next-steps |

I use `handoff diff` to see commits since the last save, new or cleaned working-tree paths, and note changes. It compares paths and Git status for uncommitted edits, not their exact contents, because Handoff does not store local patches.

`handoff save --no-test` skips the test run for a quick snapshot; `"autoRunTests": false` in `.handoff/config.json` disables it permanently.

## Safe by design

- **Never overwrites your docs.** `sync` updates a clearly delimited `<!-- handoff:start --> … <!-- handoff:end -->` block - everything else in your `AGENTS.md` / `CLAUDE.md` is untouched.
- **Plain files, plain git.** `.handoff/` is JSON + Markdown. Commit it to share context with your team (and their agents), or `.gitignore` it to stay local - your choice.
- **Zero telemetry, two dependencies** (`commander`, `picocolors`). Reads only your repo.

A coding tool that can read Markdown can use the file. Sync targets add a pointer in the instruction files supported by each tool.

## Roadmap

- [ ] `--watch` mode: auto-refresh the snapshot on git changes
- [ ] Git hook installer (snapshot on checkout/merge)
- [ ] MCP server so agents can query context programmatically
- [ ] Team mode: merge notes across branches without conflicts

## Contributing

Issues and PRs are welcome - see [CONTRIBUTING.md](CONTRIBUTING.md). Good first contributions: new sync targets, better test-tail summarization, translations of the generated file.

If `handoff` saved you from re-explaining your project to an agent - **star the repo** ⭐ and tell a friend.

## License

[MIT](LICENSE)
