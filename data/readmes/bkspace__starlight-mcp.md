# starlight-mcp

Give your [Astro](https://astro.build) or [Starlight](https://starlight.astro.build) docs site an [MCP](https://modelcontextprotocol.io) server.

Agents connect to `https://your-site.com/mcp` and get three tools — `search_docs`, `get_doc`, `list_docs` — answered straight from your docs content collection. No database, no embeddings, no separate service: the corpus is a JSON file emitted at build time, and the server is a stateless JSON-RPC handler small enough to read in one sitting.

```bash
npm install starlight-mcp
```

**Live demo**: the discountkit docs serve theirs at `https://discountkit.app/mcp` —

```bash
claude mcp add --transport http discountkit-docs https://discountkit.app/mcp
```

## How it works

1. **Build time** — the Astro integration injects two prerendered routes into your site:
   - `/mcp/docs-index.json` — every page of your docs collection (title, description, URL, cleaned markdown body)
   - `/mcp-schema.json` — a machine-readable tool catalog agents can discover before connecting (link it from your `llms.txt`)
2. **Runtime** — a dependency-free handler speaks stateless [streamable HTTP](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#streamable-http): plain JSON-RPC over POST. It loads the corpus once per isolate and answers `initialize`, `tools/list` and `tools/call`. On SSR sites the integration injects this for you; on static sites you add one tiny shim on your host (Cloudflare recipe below).

Because the transport is stateless HTTP, it works from Claude Code, Cursor, VS Code, Windsurf and anything else that speaks MCP — no SSE, no sessions, no sticky routing.

## Quickstart

### 1. Add the integration

```js
// astro.config.mjs
import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";
import starlightMcp from "starlight-mcp";

export default defineConfig({
  site: "https://your-site.com", // required — URLs in results are absolute
  integrations: [
    starlight({ title: "My Docs" }),
    starlightMcp({
      serverName: "my-docs",
      siteLabel: "My Product",
      docsRedirect: "/docs/ai-tools/", // where humans land if they open /mcp in a browser
    }),
  ],
});
```

That's the whole setup for **SSR sites** (`output: "server"`): the live endpoint is injected at `/mcp`.

For **static sites** the build emits the corpus and schema, and you serve the endpoint with a few lines of host glue:

### 2. Static sites on Cloudflare Workers

```ts
// worker/index.ts
import { createStaticMcpWorker } from "starlight-mcp/cloudflare";

export default createStaticMcpWorker({
  serverName: "my-docs",
  siteLabel: "My Product",
  docsRedirect: "/docs/ai-tools/",
});
```

```jsonc
// wrangler.jsonc
{
  "name": "my-docs-site",
  "main": "worker/index.ts",
  "compatibility_date": "2025-06-01",
  "assets": {
    "directory": "./dist",
    "binding": "ASSETS",
    "run_worker_first": ["/mcp"] // script wakes up ONLY for /mcp
  }
}
```

Every other request is served from the static assets layer without invoking the Worker — you pay for script execution only on MCP traffic.

### 3. Any other host

`starlight-mcp/handler` is a pure `(Request) => Promise<Response>` with zero dependencies — wire it into whatever speaks fetch:

```ts
import { createMcpHandler } from "starlight-mcp/handler";

const handler = createMcpHandler({
  serverInfo: { name: "my-docs", version: "1.0.0" },
  siteLabel: "My Product",
  loadIndex: async () => {
    // return DocEntry[] from wherever your build put docs-index.json
    const res = await fetch("https://your-site.com/mcp/docs-index.json");
    return res.json();
  },
});
```

## Connecting clients

```bash
# Claude Code
claude mcp add --transport http my-docs https://your-site.com/mcp
```

```jsonc
// Cursor — .cursor/mcp.json
{
  "mcpServers": {
    "my-docs": { "url": "https://your-site.com/mcp" }
  }
}
```

Clients that only speak stdio can bridge with [`mcp-remote`](https://www.npmjs.com/package/mcp-remote):

```jsonc
{
  "mcpServers": {
    "my-docs": {
      "command": "npx",
      "args": ["mcp-remote", "https://your-site.com/mcp"]
    }
  }
}
```

## Tools

| Tool | Arguments | Returns |
| --- | --- | --- |
| `search_docs` | `query` | Top 5 pages by weighted term match (title ×6, description ×3, body occurrences), each with URL, description and a snippet around the first hit |
| `get_doc` | `path` (doc id or URL) | One full page as markdown with its source URL |
| `list_docs` | — | Every page with title, description and URL |

## Options

All options are optional.

| Option | Default | What it does |
| --- | --- | --- |
| `serverName` | `<site-host>-docs` | MCP server name reported to clients |
| `serverVersion` | `"0.1.0"` | Version reported to clients |
| `path` | `"/mcp"` | Endpoint path; corpus lands at `${path}/docs-index.json`, catalog at `${path}-schema.json` |
| `collection` | `"docs"` | Which content collection to index (Starlight's is `docs`) |
| `siteLabel` | site host | Human-readable product name used in tool descriptions and `initialize` instructions |
| `instructions` | generated | The `instructions` string agents see on connect |
| `include` | all | Only index docs whose id starts with one of these prefixes |
| `exclude` | none | Drop docs whose id starts with one of these prefixes |
| `docsRedirect` | — | 302 humans who open the endpoint in a browser to this page (otherwise: a polite 405 JSON explainer) |
| `toolDescriptions` | generated | Replace the description of any tool, e.g. `{ search_docs: "Search the Acme docs (billing, webhooks, SDKs)…" }` — worth hand-tuning so agents know when to reach for it. Object form also overrides argument descriptions: `{ search_docs: { description: "…", args: { query: "e.g. 'webhook retries'" } } }` |

MDX noise (import statements, standalone `<Component>` tag lines) is stripped from indexed bodies automatically.

## Make it discoverable

Two cheap tricks that make agents actually find the server:

- **llms.txt** — lead with the MCP endpoint before your page list, e.g.
  ```
  ## MCP server
  Connect for structured search instead of scraping:
  claude mcp add --transport http my-docs https://your-site.com/mcp
  Tool catalog: https://your-site.com/mcp-schema.json
  ```
- **A docs page for humans** — an "AI tools" page with per-editor install snippets, and point `docsRedirect` at it so people who open `/mcp` in a browser land somewhere useful.

## Notes

- **Ships TypeScript source.** The package is consumed through bundlers — Astro/Vite, wrangler's esbuild, Bun, tsx — which all eat `.ts` natively. Plain `node` without a bundler needs a transpile step (compiled dist is on the roadmap).
- **Protocol** — implements stateless streamable HTTP for protocol versions `2025-06-18` and `2025-03-26`: `initialize`, `ping`, `notifications/*` (202), `tools/list`, `tools/call`; CORS is open so browser-based clients work.
- **State** — none. No sessions, no KV, no cookies. The corpus is cached per isolate/process and refreshes on deploy.

## Roadmap

- Compiled `dist/` + `.d.ts` for bundler-free Node consumers
- Optional MiniSearch-backed index for large doc sets
- `extraTools` escape hatch for site-specific tools
- Custom `clean` function for exotic MDX
- Conformance tests against the official MCP SDK client
- `llms.txt` / `llms-full.txt` generation from the same corpus

## Prior art

- [Varity's docs](https://github.com/varity-labs/varity-docs) — the `/mcp-schema.json` + llms.txt recruiting pattern
- [mcpdoc](https://github.com/langchain-ai/mcpdoc) — llms.txt-driven docs MCP as a local stdio server
- Built for (and proven on) the [discountkit](https://discountkit.app) docs

## License

MIT © bkspace
