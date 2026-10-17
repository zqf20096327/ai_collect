# SingChat MCP

**English** | [简体中文](./README.zh-CN.md) | [繁體中文](./README.zh-TW.md) | [日本語](./README.ja.md) | [한국어](./README.ko.md) | [Français](./README.fr.md) | [Português](./README.pt.md) | [Español](./README.es.md) | [العربية](./README.ar.md) | [Русский](./README.ru.md) | [ไทย](./README.th.md) | [हिन्दी](./README.hi.md) | [اردو](./README.ur.md)

> Free live chat + AI support agent for your website. Set it up from **Claude Code, Cursor, ChatGPT, Grok, or Gemini**. No signup.

[![MCP Registry](https://img.shields.io/badge/MCP%20Registry-org.singchat%2Fsingchat-6E56CF)](https://registry.modelcontextprotocol.io/?search=org.singchat)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)

**Endpoint:** `https://mcp.singchat.org`

SingChat MCP lets any MCP-capable AI assistant create a free SingChat workspace, drop a live-chat widget on your website, and then manage conversations, train the AI, and read analytics, all from your editor or chat app. One command, zero signup.

Landing page: **https://mcp.singchat.org**

---

## Screenshots

[![SingChat live chat widget embedded in a web app dashboard](./assets/singchat-live-chat-widget.png)](https://singchat.org)
*The SingChat live chat widget, embedded in a real product with a single script tag.*

[![SingChat AI support agent answering a customer question in the chat widget](./assets/singchat-ai-support-agent.png)](https://singchat.org)
*The AI support agent answers customer questions instantly and hands off to a human when needed.*

[![SingChat in-widget help center with self-service articles and FAQ](./assets/singchat-help-center-articles.png)](https://singchat.org)
*A built-in help center puts self-service articles and FAQ right inside the widget.*

[![SingChat knowledge base search inside the chat widget](./assets/singchat-knowledge-base-search.png)](https://singchat.org)
*Instant knowledge base search lets visitors find answers on their own.*

---

## Quick start

### Claude Code

```bash
claude mcp add --transport http singchat https://mcp.singchat.org
```

Then just ask your assistant: *"Set up SingChat for my website."* It runs `singchat_setup`, which creates a free workspace and hands you, in the chat, a **ready-to-use dashboard login (email + temporary password + login URL)**, a ready-to-paste embed snippet, and your API key. Log in at https://singchat.org/login with those details to reach the full dashboard, then change the email and password under Settings. The whole thing is done by the AI, no signup form.

### Cursor

Add to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "singchat": {
      "url": "https://mcp.singchat.org"
    }
  }
}
```

### ChatGPT

Settings, enable **Developer mode**, then add a remote MCP connector with the URL above. It also works as a `search` / `fetch` connector for company knowledge and deep research.

### Grok (xAI)

`grok.com/connectors`, **New Connector**, **Custom**, then paste the URL above. Grok discovers the tools automatically.

### Gemini (Gemini CLI)

Add the same URL to the `mcpServers` block in Gemini CLI's `settings.json`:

```json
{
  "mcpServers": {
    "singchat": {
      "url": "https://mcp.singchat.org"
    }
  }
}
```

The consumer Gemini app has no "add MCP" button yet, so use the Gemini CLI.

### Any stdio-only client

```bash
npx mcp-remote https://mcp.singchat.org
```

> **Works beyond the command line.** MCP is just an HTTPS endpoint, so it also works wherever the client app supports MCP, including **Claude Desktop (Mac/Windows)**, **ChatGPT desktop**, **claude.ai**, and **ChatGPT on the web**. Use the same URL, `https://mcp.singchat.org`.

---

## What you can do

Once connected, your assistant gets 17 tools. Every tool acts only on the workspace bound to your API key, no tenant argument is ever accepted.

| Tool | What it does |
| --- | --- |
| `singchat_setup` | Create a free workspace and return a dashboard login (email + password), the website embed snippet, and an API key (no signup) |
| `get_embed_snippet` | Get the HTML / React / Next embed code for your workspace |
| `claim_account` | Get a link to claim a workspace created from your editor |
| `list_conversations` / `get_conversation` | Browse and read visitor conversations |
| `reply_to_conversation` / `resolve_conversation` | Reply live and close threads without leaving your editor |
| `add_knowledge` | Crawl a website or add Q&A pairs to train the AI (RAG) |
| `list_knowledge` / `search_knowledge` | Inspect training status and retrieve knowledge |
| `configure_agent` / `set_keywords` | Tune the AI agent, model, prompt, and keyword auto-replies |
| `manage_faq` | Create / update / delete FAQ items |
| `get_analytics` | Conversation, message, and resolution stats |
| `search` / `fetch` | OpenAI-compatible tools so the same URL works as a ChatGPT connector |
| `ping` | Health check |

---

## Why SingChat

- **Free tier, no signup** to start. The `singchat_setup` flow provisions a real workspace instantly.
- **AI support agent** with website-crawl + Q&A training (RAG), keyword rules, and human handoff.
- **Embed on any platform.** Native SDKs for Web, iOS, Android, React Native, and Flutter, a full-screen WebView embed that drops SingChat into any mobile or desktop app (connect once, it auto-updates), a one-script-tag web widget for any site, plus Telegram / WhatsApp channels.
- **13 languages**, white-label branding, and a hosted platform, nothing to self-host.

## Links

- **Landing:** https://mcp.singchat.org
- **Docs:** https://singchat.org/docs/mcp
- **MCP Registry:** [`org.singchat/singchat`](https://registry.modelcontextprotocol.io/?search=org.singchat)
- **Website:** https://singchat.org

## License

MIT, see [LICENSE](./LICENSE). This repository holds the public manifest, examples, and documentation for the hosted SingChat MCP server.
