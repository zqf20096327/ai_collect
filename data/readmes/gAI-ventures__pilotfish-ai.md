# pilotfish: browser automation MCP and SDKs for AI agents

[![npm: @gaiventures/pilotfish-mcp](https://img.shields.io/npm/v/@gaiventures/pilotfish-mcp?label=%40gaiventures%2Fpilotfish-mcp)](https://www.npmjs.com/package/@gaiventures/pilotfish-mcp)
[![npm: @gaiventures/pilotfish](https://img.shields.io/npm/v/@gaiventures/pilotfish?label=%40gaiventures%2Fpilotfish)](https://www.npmjs.com/package/@gaiventures/pilotfish)
[![npm: @gaiventures/pilotfish-mcp-managed](https://img.shields.io/npm/v/@gaiventures/pilotfish-mcp-managed?label=%40gaiventures%2Fpilotfish-mcp-managed)](https://www.npmjs.com/package/@gaiventures/pilotfish-mcp-managed)
[![MCP Registry: io.github.gAI-ventures/pilotfish](https://img.shields.io/badge/MCP_Registry-io.github.gAI--ventures%2Fpilotfish-blue)](https://registry.modelcontextprotocol.io/v0.1/servers?search=io.github.gAI-ventures/pilotfish)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/gAI-ventures/pilotfish-ai)
[![gAI-ventures/pilotfish-ai MCP server](https://glama.ai/mcp/servers/gAI-ventures/pilotfish-ai/badges/score.svg)](https://glama.ai/mcp/servers/gAI-ventures/pilotfish-ai)

pilotfish is an AI browser agent and a browser automation MCP server: a real Chrome for AI agents and for your own code,
with 72% fewer tokens and 55% fewer tool calls than Playwright MCP. Pages go out as compact outlines with refs, and
after the first look only what changed, so an agent pays for each screen once.

- **Open MCP** (`@gaiventures/pilotfish-mcp`): give any MCP agent (Claude Code, Codex CLI, Cursor, ...) a real Chrome on
  your own computer. Free, no account, no API key: your agent's own model reads each page and decides every step through
  the `browser_*` tools, and this server makes no model calls. A page that offers its own tools through
  [WebMCP](https://webmachinelearning.github.io/webmcp/) gets them listed with its snapshot, callable with `browser_page_tool`.
- **SDKs for TypeScript** (`@gaiventures/pilotfish` on npm) **and Python** (`pilotfish-ai` on PyPI, imported as `pilotfish`): drive Chrome on your machine from
  code with the same tools, or send whole tasks to pilotfish's cloud browser over its REST API (tasks, batches,
  identities, saved tasks and schedules, webhooks), with the same names in both languages.

- **Install the MCP:** `npx -y @gaiventures/pilotfish-mcp` ([npm](https://www.npmjs.com/package/@gaiventures/pilotfish-mcp))
- **Install an SDK:** `npm install @gaiventures/pilotfish` · `pip install pilotfish-ai`
- **Docs:** <https://pilotfish.gai.ventures/docs/open> (the MCP), <https://pilotfish.gai.ventures/docs/sdk> (the SDKs),
  <https://pilotfish.gai.ventures/docs/api> (the REST API)
- **MCP Registry:** `io.github.gAI-ventures/pilotfish` ([listing](https://registry.modelcontextprotocol.io/v0.1/servers?search=io.github.gAI-ventures/pilotfish))
- **Issues:** <https://github.com/gAI-ventures/pilotfish-ai/issues>

## Measured against Playwright MCP

On LangChain's 100 WebVoyager tasks (11 Nov 2026), both servers driven by the same model (GPT-6 Luna) on the same
pages at the same time, with the same judge:

| Median per task | pilotfish | Playwright MCP |
| --- | --- | --- |
| Input tokens | **24.1k** (72% fewer) | 85.5k |
| Tool calls | **4.5** (55% fewer) | 10 |
| Time | **95 s** (11% faster) | 107 s |
| Answers judged correct | **66** | 63 |

The runner, task file and every result row are in [`benchmarks/`](benchmarks/). Method and other comparisons:
[pilotfish.gai.ventures/benchmarks](https://pilotfish.gai.ventures/benchmarks) and
[pilotfish.gai.ventures/compare](https://pilotfish.gai.ventures/compare).

## Install

[![Install in Cursor](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/install-mcp?name=pilotfish&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyIteSIsIkBnYWl2ZW50dXJlcy9waWxvdGZpc2gtbWNwIl19)
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_pilotfish-0098FF)](https://vscode.dev/redirect?url=vscode%3Amcp%2Finstall%3F%257B%2522name%2522%253A%2522pilotfish%2522%252C%2522command%2522%253A%2522npx%2522%252C%2522args%2522%253A%255B%2522-y%2522%252C%2522%2540gaiventures%252Fpilotfish-mcp%2522%255D%257D)
[![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_pilotfish-24bfa5)](https://insiders.vscode.dev/redirect?url=vscode-insiders%3Amcp%2Finstall%3F%257B%2522name%2522%253A%2522pilotfish%2522%252C%2522command%2522%253A%2522npx%2522%252C%2522args%2522%253A%255B%2522-y%2522%252C%2522%2540gaiventures%252Fpilotfish-mcp%2522%255D%257D)

Each button opens the app with the server filled in, for you to review and add.

**Claude Code**, in a terminal:

```sh
claude mcp add pilotfish -- npx -y @gaiventures/pilotfish-mcp
```

or as a plugin, from this repository's plugin marketplace, inside Claude Code:

```text
/plugin marketplace add gAI-ventures/pilotfish-ai
/plugin install pilotfish-browser@pilotfish
```

**Any other MCP client** (Codex CLI, Cline, Windsurf, ...): add this to its MCP settings.

```json
{
  "mcpServers": {
    "pilotfish": { "command": "npx", "args": ["-y", "@gaiventures/pilotfish-mcp"] }
  }
}
```

Node 22 or later and Google Chrome (or Chromium) on the same computer. Setup per client:
<https://pilotfish.gai.ventures/docs/open>.

## SDKs

TypeScript:

```ts
import { LocalBrowser, Pilotfish } from "@gaiventures/pilotfish";

// Chrome on your machine, through this repository's MCP: no key, no model calls.
const browser = await LocalBrowser.start();
await browser.navigate("https://news.ycombinator.com");
console.log((await browser.query("document.title")).value);
await browser.close();

// A whole task in pilotfish's cloud browser (an API key from Org settings → API keys).
const pf = new Pilotfish({ apiKey: process.env.PILOTFISH_API_KEY });
const task = await pf.tasks.run("Top story on Hacker News right now, with its points");
console.log(task.result?.result);
```

Python:

```python
from pilotfish import LocalBrowser, Pilotfish

with LocalBrowser.start() as browser:
    browser.navigate("https://news.ycombinator.com")
    print(browser.query("document.title").value)

pf = Pilotfish()  # reads PILOTFISH_API_KEY
task = pf.tasks.run("Top story on Hacker News right now, with its points")
print(task["result"]["result"])
```

Docs: <https://pilotfish.gai.ventures/docs/sdk>. Sources: `packages/sdk` (TypeScript) and `sdks/python` (Python).

## What is here

| Folder | What |
| --- | --- |
| `packages/mcp` | The local MCP server (stdio, or Streamable HTTP with `--http`): the tools, settings and the hand-off to a person. Published as `@gaiventures/pilotfish-mcp`. |
| `packages/mcp-managed` | A stdio relay to pilotfish's hosted MCP, for clients that only speak stdio. Published as `@gaiventures/pilotfish-mcp-managed`. |
| `packages/sdk` | The TypeScript SDK: `Pilotfish` (the hosted REST API) and `LocalBrowser` (this repository's MCP over stdio). Published as `@gaiventures/pilotfish`. |
| `sdks/python` | The Python SDK, the same clients with the same names, sync and async. Published as `pilotfish-ai` on PyPI. |
| `packages/cdp` | A thin, typed Chrome DevTools Protocol client. |
| `packages/browser` | Launching Chrome and driving pages over raw CDP: frames, hit-tested input, settling after an action. |
| `packages/perception` | Structure-first page snapshots, element handles, and the evidence diff after each action. |
| `packages/interrupts` | Cookie banners and ads handled deterministically, with maintained rule sets. |
| `packages/agent` | The executor every tool runs through: policy before page-affecting actions, secrets typed as `{{name}}` and never shown to the model, evidence after. |
| `plugins/pilotfish-browser` | The server as a plugin for Claude Code (`.claude-plugin/plugin.json`, `.mcp.json`) and Cursor (`.cursor-plugin/plugin.json`, `mcp.json`), listed by the marketplace files `.claude-plugin/marketplace.json` and `.cursor-plugin/marketplace.json`. |
| `.mcp.json` | The server entry, read by directories that index this repository; opening the repository in Claude Code offers to start it too. |

## Local or managed?

This repository holds the local version, free and MIT licensed, and the SDKs for both. pilotfish managed is a paid service: pilotfish runs the whole task in its cloud browser and hands your agent the result.

|  | **Local** (this repository) | **Managed** |
| --- | --- | --- |
| Who does the work | Your agent's model, one step at a time. | pilotfish runs the whole task and returns the result (the `browser_task` tool). |
| Browser and IP | A fresh Chrome on your computer, on your own IP, closed when your agent disconnects. | pilotfish's cloud browser, which keeps running when your computer is off. |
| Sites that block bots | You clear each check yourself. | Handled by the managed service. See the managed docs and pricing page for what is included. |
| Sign-ins | You sign in each time and nothing is kept. | Saved logins in an encrypted vault, several accounts per site, authenticator-app codes and codes sent to your email or phone. |
| Watching and cost | The browser window. | Live view, replays, per-task cost and monthly spending limits. |
| Compliance | Runs on your machine, under your own controls. | SOC 2 Type II compliant; how to get the report is on the [security page](https://pilotfish.gai.ventures/security#soc-2). |
| Price | Free. | Pay as you go from $5 of credit. See the pricing page for usage charges. |

Connect to managed at `https://pilotfish-be.gai.ventures/mcp` (sign in with your pilotfish account or use an organization API key), or over stdio with the relay: `npx -y @gaiventures/pilotfish-mcp-managed`. Docs: <https://pilotfish.gai.ventures/docs>. Pricing: <https://pilotfish.gai.ventures/pricing>.

## Build and test

Node 22 or later.

```sh
npm ci
npm run build
npm test                                                         # unit tests
PILOTFISH_E2E=1 npx vitest run packages/mcp --testTimeout 120000 # the MCP against a real Chrome
PILOTFISH_E2E=1 npx vitest run packages/sdk --testTimeout 120000 # the TypeScript SDK's local client against a real Chrome
npm run package                                                  # the npm packages, in packages/*/npm-package
cd sdks/python && pip install -e ".[test]" && pytest              # the Python SDK (PILOTFISH_E2E=1 for its local client)
```

The browser tests use Google Chrome when it is installed; set `PILOTFISH_CHROME` to a Chromium binary to use another.

## Contributing

This repository is a mirror: it is published from pilotfish's own repository, and every sync replaces its whole tree.
Pull requests are welcome; see [CONTRIBUTING.md](CONTRIBUTING.md). Security issues: [SECURITY.md](SECURITY.md).

## Acceptable use

pilotfish's open MCP is free software under the MIT License, but the license governs copyright only - it doesn't authorize what you automate. By using pilotfish you agree to:

- automate only sites and accounts you're authorized to use, in line with each site's terms and applicable law;
- never use it for spam, bulk account creation, collecting personal data you have no right to, credential harvesting or phishing, or getting around blocks, bans, paywalls or rate limits a site has placed on you.

Abuse of the managed service is covered by the pilotfish Terms of Service (<https://pilotfish.gai.ventures/terms>). Report security issues privately as [SECURITY.md](SECURITY.md) describes.

## License

MIT, see [LICENSE](LICENSE).
