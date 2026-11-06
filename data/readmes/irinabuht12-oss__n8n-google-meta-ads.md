# n8n + Google Ads + Meta Ads via MCP

Product pages: [Google Ads MCP](https://www.get-ryze.ai/google-ads-mcp) · [Meta Ads MCP](https://www.get-ryze.ai/meta-ads-mcp)

Two importable n8n workflows that put an AI agent on top of your real Google Ads and Meta Ads accounts through the Ryze MCP connector. No Google Ads developer token, no Meta app review: the connector handles the API access, you sign in with the account that owns the ads.

## Connect the MCP first

1. In n8n add an **MCP Client Tool** node (`@n8n/n8n-nodes-langchain.mcpClientTool`)
2. Endpoint: `https://connector.get-ryze.ai/mcp`, transport HTTP streamable, authentication OAuth2
3. Approve the Google or Facebook login once. Every tool (campaign reports, search terms, GAQL, Meta insights, GA4, Search Console) is then available to the agent

The same URL works outside n8n: `claude mcp add ryze --transport http https://connector.get-ryze.ai/mcp` in Claude Code, or Settings › Connectors › Add custom connector in claude.ai, ChatGPT and Cursor. [Setup guide with screenshots →](https://www.get-ryze.ai/how-to-connect-claude-to-google-meta-ads-mcp)

## Workflows

| File | What it does |
|---|---|
| `clawdbot-n8n-google-meta.json` | **AI Agent - MCP Data + Gamma Report.** Chat trigger → AI agent (Gemini) with the Ryze MCP client tool pulls Google Ads and Meta Ads performance → Gamma API builds a presentation → waits for render → emails the deck through Gmail. Ask "audit last week" and get a slide deck in your inbox. |
| `n8n-to-share.json` | **Nano Banana Static Ad Spinner.** Form trigger → Firecrawl scrapes the brand site → Gemini writes brand guidelines into a Google Doc → generates static ad variations with Nano Banana from a reference image. Pair it with the MCP workflow to push winners into the ad account. |

Import: n8n → Workflows → Import from file. Credentials you need: Ryze MCP (OAuth, free), Google Gemini, Gmail, Gamma API for the first workflow; Firecrawl, Gemini, Google Docs for the second.

## More

- [Google Ads + Meta Ads + GA4 MCP](https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp): the connector, every client, 250+ tools
- [48 free Claude marketing skills](https://github.com/irinabuht12-oss/marketing-skills)
- Built by [Ryze AI](https://www.get-ryze.ai)
