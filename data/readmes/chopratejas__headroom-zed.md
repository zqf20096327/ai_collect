# Headroom for Zed

Context compression for Zed's AI agent. Same answers, fraction of the tokens.

## What it does

This extension registers [Headroom](https://github.com/chopratejas/headroom) as an MCP context server in Zed, giving the AI agent three tools:

| Tool | What it does |
|------|-------------|
| `headroom_compress` | Compress large content (files, JSON, logs, search results) on demand |
| `headroom_retrieve` | Retrieve original uncompressed content by hash |
| `headroom_stats` | Show session stats: tokens saved, cost saved, recent events |

## Setup

### 1. Install Headroom

```bash
pip install "headroom-ai[mcp]"
```

### 2. Install the extension

In Zed: **Extensions** → search **Headroom** → **Install**

That's it. Zed's agent now has access to compression tools.

### 3. (Optional) Automatic compression for all traffic

The MCP tools above are on-demand — the agent calls them when it wants to compress. For automatic compression of every LLM request, start the Headroom proxy:

```bash
headroom proxy
```

Then add to your Zed settings (`settings.json`):

```json
{
  "language_models": {
    "openai": {
      "api_url": "http://localhost:8787/v1"
    }
  }
}
```

Now every request is automatically compressed — 50-90% fewer tokens, same quality. The MCP tools and proxy work independently or together.

## How it works

The extension tells Zed to run `headroom mcp serve` as a background process. This starts Headroom's MCP server, which exposes the compression tools over the Model Context Protocol. Zed's agent can then call these tools like any other MCP tool.

Compression uses Headroom's full pipeline: SmartCrusher for JSON, CodeCompressor for code, Kompress for text (with `[ml]` extra). Originals are stored locally for the session and retrievable on demand — nothing is lost.

## Requirements

- [Headroom](https://github.com/chopratejas/headroom) — `pip install "headroom-ai[mcp]"`
- Python 3.10+
- `headroom` command in PATH

## License

Apache License 2.0
