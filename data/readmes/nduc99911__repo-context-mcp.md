# repo-context-mcp

**MCP server that helps AI coding agents understand a repository** — without dumping the entire monorepo into the prompt.

[![CI](https://github.com/nduc99911/repo-context-mcp/actions/workflows/ci.yml/badge.svg)](https://github.com/nduc99911/repo-context-mcp/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Node.js >= 18](https://img.shields.io/badge/node-%3E%3D18-brightgreen)](package.json)
[![MCP](https://img.shields.io/badge/MCP-stdio-purple)](https://modelcontextprotocol.io)

Works with **Codex**, **Claude Code**, **Cursor**, **Cline**, and any client that speaks [Model Context Protocol](https://modelcontextprotocol.io).

## Why

AI agents waste tokens re-walking `node_modules`, missing entrypoints, or pasting random files. **repo-context-mcp** exposes three focused tools:

| Tool | Purpose |
| --- | --- |
| `repo_map` | Lightweight tree + manifests/entrypoints |
| `search_code` | Fast substring search with path:line hits |
| `pack_context` | Token-budgeted markdown pack for LLM prompts |

Local-only. No cloud. No telemetry. Stdio transport.

## Install

```bash
# run from source
git clone https://github.com/nduc99911/repo-context-mcp.git
cd repo-context-mcp
npm install
npm run build

# or via npx (after publish)
npx -y repo-context-mcp
```

Requires **Node.js 18+**.

## CLI (no MCP client)

```bash
npm run build

# repository map
node dist/cli.js map .
node dist/cli.js map examples/sample-repo

# search
node dist/cli.js search login examples/sample-repo

# token-aware pack
node dist/cli.js pack . --focus auth,api --max-tokens 8000

# JSON for scripts / CI
node dist/cli.js map . --json
node dist/cli.js pack . --focus src --json
```

After global install / `npx`:

```bash
npx repo-context-mcp map .
npx repo-context-mcp pack . --focus auth
```

## MCP client config

### Claude Desktop / Claude Code

```json
{
  "mcpServers": {
    "repo-context": {
      "command": "npx",
      "args": ["-y", "repo-context-mcp"],
      "env": {
        "REPO_CONTEXT_ROOT": "/absolute/path/to/your/repo"
      }
    }
  }
}
```

### Cursor

Settings → MCP → add server with command `npx` and args `["-y", "repo-context-mcp"]`.

### Codex / generic stdio

```bash
REPO_CONTEXT_ROOT=/path/to/repo node /path/to/repo-context-mcp/dist/server.js
```

From this repository after build:

```bash
npm run build
node dist/cli.js serve
# or: node dist/server.js
```

See also `examples/mcp-config.claude.json` and `examples/mcp-config.local.json`.

Optional env:

| Variable | Meaning |
| --- | --- |
| `REPO_CONTEXT_ROOT` | Default repository root when tools omit `root` |

Each tool also accepts an explicit `root` argument.

## Tools

### `repo_map`

```text
root?: string
max_depth?: number      # default 6
max_entries?: number    # default 400
```

Returns a markdown tree, file count, and likely entrypoints (`package.json`, `README.md`, `src/index.ts`, `AGENTS.md`, …). Skips `node_modules`, `.git`, `dist`, etc.

### `search_code`

```text
query: string
root?: string
max_results?: number    # default 50
case_sensitive?: boolean
```

Substring search across source-like extensions.

### `pack_context`

```text
root?: string
focus?: string[]        # keywords / path fragments to prioritize
max_tokens?: number     # default 12000 (approx)
max_files?: number      # default 40
```

Ranks files (entrypoints + focus matches), respects a rough token budget (~4 chars/token), and returns a single markdown document ready to paste into an agent prompt or PR review.

## Library API

You can use the core without MCP:

```ts
import {
  buildRepoMap,
  formatRepoMap,
  searchCode,
  packContext,
} from "repo-context-mcp";

const map = buildRepoMap({ root: process.cwd() });
console.log(formatRepoMap(map));

const hits = searchCode({ root: process.cwd(), query: "TODO" });
const pack = packContext({
  root: process.cwd(),
  focus: ["auth"],
  maxTokens: 8000,
});
console.log(pack.markdown);
```

## Demo (no MCP client)

```bash
npm install
npm test
npm run build

# map the sample tree
node --input-type=module -e "import { buildRepoMap, formatRepoMap } from './dist/index.js'; console.log(formatRepoMap(buildRepoMap({ root: 'examples/sample-repo' })));"
```

## Security

- Reads files only under the requested `root`.
- Does not execute project code.
- Skips common vendor dirs and obvious binaries.
- Still: only point it at repositories you trust.

See [SECURITY.md](SECURITY.md).

## Project status

**v0.1.1** — MCP server + CLI + gitignore + PR Action.

Roadmap:

- [x] `.gitignore` respect
- [x] CLI (`map` / `search` / `pack`) + `--json`
- [x] GitHub Action: pack context on each PR
- [ ] Optional ripgrep backend for large monorepos
- [ ] Baseline symbol index (tree-sitter) for `find_symbol`
- [ ] Configurable ignore file (`.repo-contextignore`)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

```bash
npm install
npm test
npm run lint
npm run build
```

## License

[MIT](LICENSE) © Nguyen Duc

---

Built as a real maintainer / agent-tooling utility for the MCP ecosystem — not a placeholder repo. Issues and PRs welcome.
