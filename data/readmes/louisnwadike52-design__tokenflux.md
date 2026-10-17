# TokenFlux

> Intelligent token and context optimization for Claude Code.

[![npm version](https://img.shields.io/npm/v/tokenflux-cli.svg)](https://www.npmjs.com/package/tokenflux-cli)
[![CI](https://github.com/louisnwadike52-design/tokenflux/actions/workflows/ci.yml/badge.svg)](https://github.com/louisnwadike52-design/tokenflux/actions/workflows/ci.yml)
[![license: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

📦 **npm:** [`tokenflux-cli`](https://www.npmjs.com/package/tokenflux-cli) · 💻 **source:** [github.com/louisnwadike52-design/tokenflux](https://github.com/louisnwadike52-design/tokenflux)

TokenFlux installs a compact, carefully engineered [Agent Skill](https://code.claude.com/docs/en/skills) that gives Claude Code a disciplined **token-efficiency layer**: gather the minimum context needed to complete a task _correctly_ — search before reading, read targeted ranges, filter command output, avoid redundant reads and tool calls — and never trade correctness for token savings.

**Zero runtime dependencies. Fully local. No telemetry, no API keys, no network calls.**

## Why it exists

Coding agents burn context on low-value retrieval: whole-repository crawls, full reads of huge files to find one function, rereads of unchanged files, and verbose command dumps. That waste crowds out the context that matters and shortens useful session length.

A one-line "be concise" instruction doesn't fix this — the waste is in _what gets consumed_, not what gets said. TokenFlux encodes concrete acquisition discipline (search → identify → targeted read → reason → act), context-priority rules, and hard safety constraints, as a skill Claude Code applies while it works.

TokenFlux optimizes **token efficiency, not token count**: a cheap read that prevents a wrong edit is efficient; a skipped read that causes one is not. **Correctness always beats token savings.**

## Installation

```bash
npm install -g tokenflux-cli
tokenflux install
```

Or without a global install:

```bash
npx tokenflux-cli install
```

The npm package is `tokenflux-cli`; the installed command and the skill are both simply `tokenflux`.

That's it — Claude Code discovers the skill automatically, and you can invoke it explicitly with `/tokenflux`.

Verify:

```bash
tokenflux status
tokenflux doctor
```

## Quick start

```bash
# personal scope (default): ~/.claude/skills/tokenflux/
tokenflux install

# project scope: <repo>/.claude/skills/tokenflux/ — commit it to share with your team
tokenflux install --project

# optional: project configuration
tokenflux init
tokenflux config set mode aggressive
```

## Commands

| Command               | What it does                                                                  |
| --------------------- | ----------------------------------------------------------------------------- |
| `tokenflux install`   | Install the skill (`--project`, `--claude-dir <path>`, `--force`)             |
| `tokenflux uninstall` | Remove it — deletes only files tokenflux installed                            |
| `tokenflux status`    | Version, install state, skill path, config summary with per-key sources       |
| `tokenflux doctor`    | Validate environment, installation, and configuration, with remediation hints |
| `tokenflux init`      | Create a project-level `.tokenflux.json` with defaults                        |
| `tokenflux config`    | `list` · `get <key>` · `set <key> <value> [--global]` · `path`                |
| `tokenflux export`    | Build a portable skill bundle for other Claude surfaces (see below)           |
| `tokenflux version`   | Print the version (also `--version` / `-v`)                                   |

Exit codes: `0` success, `1` operational failure, `2` usage error. Color output respects `NO_COLOR`.

## Using TokenFlux beyond Claude Code

The skill is standard Agent Skills format (a folder with a `SKILL.md`), so it ports to every surface that supports skills:

```bash
tokenflux export                 # → ./tokenflux-skill.zip
tokenflux export --dir ./bundle  # → ./bundle/tokenflux/ (plain folder)
```

- **claude.ai and Claude Desktop** — Settings → Capabilities → Skills → upload `tokenflux-skill.zip`.
- **Claude API** — upload the same zip via the [Skills API](https://docs.claude.com/en/docs/agents-and-tools/agent-skills), then reference it from your agent runs.
- **Claude Code on another machine** — `npx tokenflux-cli install`, or unzip the bundle into `~/.claude/skills/`.
- **Other Agent-Skills-compatible platforms** — point them at the exported folder.

## Configuration

Optional. TokenFlux works out of the box with sensible defaults.

`.tokenflux.json` (project, found in the working directory or any ancestor) overrides `~/.tokenflux.json` (global), which overrides the defaults:

```json
{
  "mode": "balanced",
  "maxContextExpansion": 3,
  "avoidGeneratedFiles": true,
  "avoidNodeModules": true,
  "preferTargetedReads": true,
  "preferSearchBeforeRead": true,
  "preserveCriticalContext": true
}
```

The installed skill reads the project's `.tokenflux.json` at task time, so changing settings never requires reinstalling.

### Optimization modes

- **`balanced`** (default) — cut obvious waste; when in doubt, gather the context.
- **`aggressive`** — also trim marginal reads and redundant tool output; still verify anything correctness-critical.
- **`maximum`** — minimum viable context wherever it is safe; correctness checks remain mandatory.

Safety rules apply in every mode: never skip validation or tests, never guess instead of reading required code, never hide errors, never drop requirements or security-relevant details.

## Example

The same task — "fix the `refreshToken` bug in the auth service" — approached two ways:

**Without TokenFlux:**

```text
read package.json → list entire repository tree → read src/auth/service.ts (900 lines)
→ read src/auth/controller.ts, src/auth/jwt.ts, src/users/service.ts "for context"
→ reread src/auth/service.ts → run the full test suite with verbose output
→ paste hundreds of lines of passing logs
```

**With TokenFlux:**

```text
rg -n "refreshToken" src/          → 3 hits, all in src/auth/service.ts
read lines 210–260 of service.ts   → the affected function and its callers
fix the bug
npx vitest run auth --reporter=dot → inspect the one failure, fix, re-run
```

Same engineering quality; far less context consumed by things that never influenced the change.

TokenFlux makes **no numeric savings claims** — actual impact depends on your repository, tasks, and habits, and v0.1 ships no measurement system. (A local, opt-in measurement mechanism is on the roadmap; claims will follow evidence.)

## Architecture

```text
src/
├── cli/          command dispatch, arg parsing, target resolution, commands/
├── config/       schema, defaults, validation, discovery, precedence, get/set
├── installer/    managed install/uninstall/verify with content-hash metadata
├── skill/        SKILL.md parser + validator (shared by doctor and tests)
├── utils/        output, sha256, stored-zip writer, package root/version
└── index.ts      programmatic API
skills/tokenflux/SKILL.md   the canonical skill, shipped in the npm tarball
```

Installs are **managed**: tokenflux records a `.tokenflux.meta.json` (version + per-file sha256) beside the skill. Re-running `install` is idempotent; unmanaged or locally modified files are never overwritten without `--force`; `uninstall` deletes only what the metadata lists — never neighboring skills, never your added files.

The skill itself is capped at **8 KB, enforced by test** — TokenFlux must not waste tokens explaining token optimization.

## Development

```bash
npm install
npm run build       # compile src/ → dist/
npm run typecheck   # strict TS over src + tests
npm run lint        # eslint + prettier --check
npm test            # build, then node --test over compiled tests
```

Requirements: Node ≥ 20. Tests run entirely in temp directories — your real `~/.claude` is never touched.

## Publishing

```bash
npm run lint && npm test   # also enforced by prepublishOnly
npm pack --dry-run         # audit tarball contents
npm publish
```

Published as [`tokenflux-cli`](https://www.npmjs.com/package/tokenflux-cli) on npm. (The registry rejects the bare name `tokenflux` as too similar to an unrelated existing package; the installed command and the skill are still simply `tokenflux`.)

## Troubleshooting

Run `tokenflux doctor` first — every check prints a remediation hint. Common cases:

- **"a skill already exists … but was not installed by tokenflux"** — something else created `skills/tokenflux/`. Re-run with `--force` to take it over, or remove it manually.
- **"installed skill files have local modifications"** — you edited the installed `SKILL.md`. Back up your edits, then `tokenflux install --force`.
- **Claude config directory missing** — run Claude Code once, or pass `--claude-dir`, or set `CLAUDE_CONFIG_DIR`. `tokenflux install` creates it if needed.
- **Skill not triggering** — invoke it explicitly with `/tokenflux`, or mention token efficiency in your prompt; check `tokenflux status` shows it installed and up to date.

## Privacy

TokenFlux runs entirely on your machine. It makes no network requests, sends no telemetry, uploads no source code, and requires no API key. The only writes it performs are the skill files under the Claude config directory you target and the config files you ask it to create.

## Contributing

Issues and pull requests are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md) and our [Code of Conduct](CODE_OF_CONDUCT.md); report vulnerabilities per [SECURITY.md](SECURITY.md). Keep the skill under its byte budget and every source file within 200 lines; `npm test` holds you to both.

## License

[MIT](LICENSE)
