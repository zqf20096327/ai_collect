<!-- mcp-name: io.github.n-kostadinov/yfinance-agent-mcp -->

# yfinance-agent-mcp: Yahoo Finance MCP server for AI trading-research agents

[![PyPI](https://img.shields.io/pypi/v/yfinance-agent-mcp)](https://pypi.org/project/yfinance-agent-mcp/)
[![Python versions](https://img.shields.io/pypi/pyversions/yfinance-agent-mcp)](https://pypi.org/project/yfinance-agent-mcp/)
[![CI](https://github.com/n-kostadinov/yfinance-agent-mcp/actions/workflows/ci.yml/badge.svg)](https://github.com/n-kostadinov/yfinance-agent-mcp/actions/workflows/ci.yml)
[![Docs](https://github.com/n-kostadinov/yfinance-agent-mcp/actions/workflows/docs.yml/badge.svg)](https://n-kostadinov.github.io/yfinance-agent-mcp/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](https://github.com/n-kostadinov/yfinance-agent-mcp/blob/main/LICENSE)

**yfinance-agent-mcp** is a read-only [Model Context Protocol](https://modelcontextprotocol.io/) server that gives AI agents market data from Yahoo Finance through [yfinance](https://github.com/ranaroussi/yfinance): quotes, price history with ready-made indicators, news, screeners, earnings and economic calendars, fundamentals, analyst views, options and live prices.

It is built for agents that follow news and trends and prepare trading decisions: answers are small, timestamped and honest about delays, and failures come back as actionable errors instead of empty data.

```bash
uvx yfinance-agent-mcp
```

**[Documentation](https://n-kostadinov.github.io/yfinance-agent-mcp/)** · **[Tools](https://n-kostadinov.github.io/yfinance-agent-mcp/tools/)** · **[Changelog](https://github.com/n-kostadinov/yfinance-agent-mcp/blob/main/CHANGELOG.md)**

## Why this server

- **13 tools that cover all of yfinance**, shaped for agents rather than one tool per library method.
- **Answers that fit in context.** Price history comes with returns, SMA 20/50/200, RSI 14, ATR 14 and the 52-week range instead of thousands of raw bars; every response stays under 20,000 characters by default.
- **Freshness you can check.** Every answer carries `as_of`; quotes add `market_state`, `quote_source` and `delay_min`, because many exchanges are delayed by 15 minutes.
- **Errors an agent can act on:** `rate_limited` (with the seconds to wait), `not_found`, `invalid_argument` (with the valid values) and `upstream_error`, never a silent empty result.
- **Gentle with Yahoo.** One shared session, a process-wide rate limit, a pause after HTTP 429, and a short-lived cache with its own expiry times.
- **Safe with news.** Publisher text arrives in fields marked `untrusted`, so agents treat headlines as data, not instructions.
- **Read-only.** It cannot place orders.

## Quick start

You need [uv](https://docs.astral.sh/uv/getting-started/installation/). `uvx` downloads and runs the server; it talks MCP over stdio.

### Claude Code

```bash
claude mcp add yfinance -- uvx yfinance-agent-mcp
```

Or install the plugin, which adds the server and a market-research skill:

```text
/plugin marketplace add n-kostadinov/yfinance-agent-mcp
/plugin install yfinance@yfinance-agent-mcp
```

On Claude Code 2.1.275 or later this works in one step: `/plugin install yfinance --marketplace n-kostadinov/yfinance-agent-mcp`.

### Claude Desktop

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "yfinance": {
      "command": "uvx",
      "args": ["yfinance-agent-mcp"]
    }
  }
}
```

### Cursor

Add to `.cursor/mcp.json` (project) or `~/.cursor/mcp.json` (global):

```json
{
  "mcpServers": {
    "yfinance": {
      "command": "uvx",
      "args": ["yfinance-agent-mcp"]
    }
  }
}
```

### VS Code

Add to `.vscode/mcp.json`:

```json
{
  "servers": {
    "yfinance": {
      "type": "stdio",
      "command": "uvx",
      "args": ["yfinance-agent-mcp"]
    }
  }
}
```

### Windsurf

Add to `~/.codeium/windsurf/mcp_config.json`:

```json
{
  "mcpServers": {
    "yfinance": {
      "command": "uvx",
      "args": ["yfinance-agent-mcp"]
    }
  }
}
```

More clients, including the Claude Agent SDK, are covered in the [client guides](https://n-kostadinov.github.io/yfinance-agent-mcp/clients/claude-code/).

## Tools

| Tool | What it answers |
|---|---|
| `search_symbols` | Which Yahoo symbol is "Nvidia", "SAP" or "gold"? |
| `get_quotes` | Price, change, day range, volume and freshness for up to 25 symbols |
| `get_market_overview` | Is the market open, and how are the indices doing? |
| `get_price_history` | Trend, momentum and volatility: indicators plus the latest bars |
| `get_news` | Latest news for symbols or a topic, newest first, publisher text marked untrusted |
| `screen_securities` | Candidates from Yahoo's predefined screens or a custom query |
| `get_sector_industry` | Leaders, ETFs and industries of a sector or industry |
| `get_events` | Earnings, IPO, economic and split calendars; a symbol's next earnings |
| `get_fundamentals` | Income, balance sheet, cash flow, valuation history, key ratios |
| `get_analyst_view` | Price targets, ratings, rating changes, EPS and revenue estimates |
| `get_options` | Calls and puts around the current price, every expiration |
| `get_ticker_dataset` | Holders, insider trades, dividends, splits, SEC filings, fund holdings and more |
| `get_live_quotes` | The price right now, from Yahoo's streaming feed |

Each tool is described in detail, with examples, in the [tool reference](https://n-kostadinov.github.io/yfinance-agent-mcp/tools/).

## Example prompts

- "What moved NVDA today? Check the news, the price action and whether earnings are coming."
- "Screen today's top gainers and tell me which ones have above-average volume and analyst upgrades."
- "Compare AAPL and MSFT: valuation, margins, growth and the 6-month trend."
- "Is the US market open? How are the indices and Bitcoin doing right now?"

## Configuration

Everything is optional; set environment variables in your client's server config.

| Variable | Default | Meaning |
|---|---|---|
| `YFINANCE_AGENT_MCP_RATE_LIMIT` | `2` | Requests per second to Yahoo |
| `YFINANCE_AGENT_MCP_RATE_BURST` | `5` | Requests allowed at once |
| `YFINANCE_AGENT_MCP_TTL_<CATEGORY>` | per category | Seconds a cached answer stays valid, e.g. `YFINANCE_AGENT_MCP_TTL_QUOTES=5` |
| `YFINANCE_AGENT_MCP_CACHE_DIR` | user cache dir | Where yfinance keeps its timezone and cookie caches |
| `YFINANCE_AGENT_MCP_LANG` / `_REGION` | `en-US` / `US` | Yahoo locale |
| `YFINANCE_AGENT_MCP_PROXY` | none | Proxy URL for Yahoo requests |
| `YFINANCE_AGENT_MCP_LOG_LEVEL` | `WARNING` | Log level (logs go to stderr) |

See the [configuration guide](https://n-kostadinov.github.io/yfinance-agent-mcp/configuration/) for all cache categories.

## Disclaimer

yfinance-agent-mcp is not affiliated with, endorsed by, or vetted by Yahoo. It uses yfinance, which reads Yahoo Finance's publicly available endpoints; Yahoo's [terms of service](https://legal.yahoo.com/us/en/yahoo/terms/otos/index.html) say the data is for personal use. Data can be delayed, incomplete or wrong. Nothing here is investment advice, and the server cannot trade. Read the full [disclaimer](https://n-kostadinov.github.io/yfinance-agent-mcp/disclaimer/).

## Acknowledgements

This server is built on [yfinance](https://github.com/ranaroussi/yfinance) by Ran Aroussi
and its contributors, which does the hard work of reading Yahoo Finance. yfinance is
licensed under the [Apache License 2.0](https://github.com/ranaroussi/yfinance/blob/main/LICENSE.txt);
see its [documentation](https://ranaroussi.github.io/yfinance/) and
[PyPI page](https://pypi.org/project/yfinance/). If this server is useful to you, consider
[sponsoring yfinance's author](https://github.com/sponsors/ranaroussi).

## Contributing

Issues and pull requests are welcome. See the [contributing guide](https://github.com/n-kostadinov/yfinance-agent-mcp/blob/main/CONTRIBUTING.md) to set up the project with uv and run the tests.

## License

[MIT](https://github.com/n-kostadinov/yfinance-agent-mcp/blob/main/LICENSE)
