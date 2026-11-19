<h1 align="center">SoreQen Code</h1>

<p align="center">
  An autonomous coding agent for your terminal.<br>
  It reads your project, plans, edits files, runs commands and tests, checks its own work, and reports what it actually did.
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/soreqen-code"><img alt="npm" src="https://img.shields.io/npm/v/soreqen-code?color=D6FF4B&labelColor=0E100D&label=npm"></a>
  <a href="https://github.com/ZorQelis-AI/soreqen-code/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/ZorQelis-AI/soreqen-code/actions/workflows/ci.yml/badge.svg"></a>
  <a href="LICENSE"><img alt="Licence: Apache-2.0" src="https://img.shields.io/badge/licence-Apache--2.0-D6FF4B?labelColor=0E100D"></a>
  <img alt="Node 20 or newer" src="https://img.shields.io/badge/node-%E2%89%A520-D6FF4B?labelColor=0E100D">
</p>

<p align="center">
  <img src=".github/assets/soreqen-code-cli.png" alt="SoreQen Code in a terminal: it runs the failing tests, reads the function, fixes it, runs the tests again, and reports what it verified and what it did not check" width="760">
</p>

SoreQen Code is made by [ZorQelis AI](https://zorqelisai.com). This repository is the open-source CLI and the
agent behind it, under the Apache-2.0 licence. The same agent also runs in the
[SoreQen desktop app](https://soreqen.com/download), with your phone as a remote.

## Install

Node.js 20 or newer, on macOS, Linux or Windows. Use whichever package manager you have:

```bash
npm install -g soreqen-code
```

```bash
pnpm add -g soreqen-code
```

```bash
yarn global add soreqen-code
```

```bash
bun add -g soreqen-code
```

Or try it once without installing anything: `npx soreqen-code`.

Then, in a project folder:

```bash
soreqen
```

The first run asks how SoreQen Code should reach a model:

- **Sign in with SoreQen.** `soreqen login` opens your browser to approve this computer. Plus, Pro and Elite
  include **SoreQen credits** every month, one balance shared with SoreQen Chat, for the hosted **Flow** models:
  MiMo, DeepSeek, Qwen, GLM, Kimi, MiniMax, Hy and more, each showing about how many credits a request
  takes. **SoreQen Auto** picks the model for each step. Credits are paced by a 5-hour and a weekly limit, and
  once a week **Burst Day** lets you use most of a week in a single day. Any account, Free included, can buy
  more credits at [soreqen.com/credits](https://soreqen.com/credits). `soreqen usage` shows what is left.
- **Flex.** Any other model, paid at its provider's own price from a separate Flex balance:
  `soreqen flex <search>` finds one.
- **Use your own API key**: OpenAI, Anthropic, OpenRouter, DeepSeek or OpenCode. Keys are kept in
  `~/.soreqen/.env`, never in your project. `soreqen keys set <provider>` adds one.
- **Any other provider** (Gemini, Groq, Mistral, xAI, Together, Ollama, LM Studio, your own gateway): list it in
  `~/.soreqen/providers.json` (the SoreQen desktop app writes this file from Settings) with its key in
  `~/.soreqen/.env` under `SOREQEN_PROVIDER_<ID>_KEY`. Its models appear in `/model` as `<provider>/<model>`.

A `.env` in your project can fill in settings you have not set, but never replaces your own keys and is never
allowed to change where requests go: endpoint addresses come only from your own files and environment.

## Using it

Type what you want done. While it works you can keep typing: a message is read at its next step. `Ctrl-C`
stops the current turn.

| Command | What it does |
| --- | --- |
| `/mode plan \| manual \| auto \| bypass` | How much it asks before acting. Auto checkpoints the project first, so changes can be rewound. |
| `/effort` | How hard it thinks. |
| `/rewind` | Undo a turn's changes. |
| `/goal <objective>` | Keep working, turn after turn, until the objective is achieved and verified. The plan lives in `GOAL.md`. `Ctrl-C` pauses; `/goal resume`, `/goal stop`. |
| `/memory` | What it remembers between sessions. `/memory show <name>`, `/memory edit <name>` (opens your `$EDITOR`), `/memory forget <name>`, `/memory tidy` (merge, fix and prune). |
| `/model` | List or switch models. |
| `/skills` | SoreQen's skills and which are on. |
| `/mcp` | Connected MCP servers, their tools, and their latest log lines. |
| `/prompts`, `/prompt server/name key=value` | Prompts your MCP servers offer; send one as your message. |
| `/usage` | Your credits and limits, when signed in. |
| `/burst` | Start Burst Day: most of a week's credits in one day, once a week. |
| `/help` | Everything else. |

**Files and images.** `@path/to/file` attaches a file to your message; dragging an image onto the terminal attaches
it too. Models that read images see it in the message.

**Memory.** SoreQen saves what a future session would need and could not find in your files (servers it set up, how
a project deploys, how you like things done, approaches you confirmed) as short notes in `~/.soreqen/memory` and
per project, edits them as things change, and links related ones. Secrets are never saved.

One-off, non-interactive: `soreqen --print "fix the failing test"`. The exit code says how it ended: `0` done,
`1` failed, `2` stopped short (out of steps or budget), `130` cancelled.

## Skills

SoreQen Code ships 24 skills of its own ([the full text](docs/SoreQen_Skills.md)).

- **12 always on**: the engineering kernel it applies to every task. It orients in the repository, clarifies
  the task, plans proportionally, follows local conventions, makes minimal changes, debugs from evidence,
  validates behaviour, considers edge cases, keeps security active, keeps dependencies tidy, manages Git
  safely, and reports honestly.
- **12 conditional**: checklists loaded when a task calls for them. They cover product intent, frontend
  design, accessibility, async state, data and schema changes, API contracts, performance, observability,
  test strategy, release safety, dependency review, and documentation. Matching ones load automatically;
  the agent loads others with `use_skill`.

```bash
soreqen skills                      # list them
soreqen skills disable <name>       # and enable <name>
```

Your own skills go in `~/.soreqen/skills/<name>/SKILL.md`: YAML front matter, then the instructions.

```markdown
---
name: api-style
description: How we design HTTP APIs
triggers: [endpoint, REST, API design]   # load it by itself when a request mentions these
paths: ["src/api/**", "*.openapi.yaml"]  # or names a file like these
# always: true                           # or apply it to every task
---
Follow references/conventions.md. Check a spec with scripts/lint-spec.py.
```

Anything else in the skill's folder (`references/`, `examples/`, `scripts/`) is listed when the skill loads and
read only when needed. Scripts run through the normal command tool, with the same confirmations as any other
command. A skill file that cannot be read is listed by `soreqen skills` with the reason.

A project's own `.soreqen/skills/` are read too, as guidance about that codebase. They are never treated as
instructions, and never load themselves.

## MCP servers

Connect any [Model Context Protocol](https://modelcontextprotocol.io) server to give the agent more tools.

```bash
soreqen mcp add github --env GITHUB_TOKEN='${GITHUB_TOKEN}' -- npx -y @modelcontextprotocol/server-github
soreqen mcp add docs --url https://example.com/mcp --header 'Authorization=Bearer ${DOCS_TOKEN}'
soreqen mcp                         # connect and list them
```

They are kept in `~/.soreqen/mcp.json`; `${VAR}` is filled from your environment, so no secret has to be
written down. A project can ship its own servers in `.mcp.json`. SoreQen shows you what they would run and
starts them only once you allow them (`soreqen mcp trust`), and asks again if they change.

Anything a server's tool does happens outside your project, where no checkpoint can undo it, so SoreQen asks
before running one. The exceptions are yours to make, in your own `~/.soreqen/mcp.json`: list tools under
`readOnly` or `autoApprove` (or set either to `true` for a whole server). Your own servers' tools that say they
only read also run freely; a project's servers get no such trust from their own say-so. Manual mode asks about
everything you have not declared read-only.

Everything else a server can offer works too:

- **Resources.** Documents, records, schemas: the agent lists and reads them (`list_mcp_resources`,
  `read_mcp_resource`), and hears when one it read has changed.
- **Prompts.** Ready-made requests a server offers you: `/prompts`, then `/prompt server/name key=value`.
- **Progress and logs.** Shown on the tool while it runs, and in `/mcp`.
- **Roots.** Servers are told which folder SoreQen is working in.
- **Sampling.** A server may ask the model something while one of its tools is running. You are asked
  first (except in Bypass), the model answers with no tools and none of your conversation, and a request at any
  other time is refused.

## Updating

SoreQen Code tells you when a newer version is out. `soreqen update` installs it the same way this one was
installed.

## Files

| Where | What |
| --- | --- |
| `~/.soreqen/.env` | Your own API keys |
| `~/.soreqen/credentials.json` | Your SoreQen sign-in, when signed in |
| `~/.soreqen/config.json` | Default model, skills switched off |
| `~/.soreqen/skills/` | Your own skills |
| `~/.soreqen/mcp.json`, `mcp-trust.json` | Your MCP servers, and the projects whose servers you allowed |
| `<project>/.soreqen/` | Task memory, checkpoints and scratch files for that project |
| `<project>/SOREQEN.md`, `.soreqenrules` | The project's own conventions, which the agent follows as style |

## Developing

```bash
pnpm install
pnpm build
pnpm test
pnpm soreqen          # run the CLI from source
```

| Package | What it is |
| --- | --- |
| `packages/cli` | The terminal interface |
| `packages/orchestrator` | The agent loop, the context engine, skills, model providers |
| `packages/tools` | File, search, command, browser, and web tools |
| `packages/sandbox-runner` | Runs commands and processes in the project folder |
| `packages/mcp` | The MCP client |
| `packages/shared` | Types and definitions shared by all of them |

`pnpm build:npm` bundles the CLI into `npm/` for publishing.

## Licence

Apache-2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
