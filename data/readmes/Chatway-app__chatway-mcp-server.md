<p align="center">
  <img src="assets/chatway-logo.png" alt="Chatway" width="96" height="96">
</p>

<h1 align="center">Chatway MCP Server: Connect AI Agents to Customer Support</h1>

<p align="center">
  Let ChatGPT, Claude, Gemini, Cursor, and other AI agents read and manage your
  <a href="https://chatway.app">Chatway</a> live chat conversations, support tickets, and contacts.
</p>

<p align="center">
  <a href="https://go.chatway.app/register"><strong>Create a free Chatway account</strong></a> ·
  <a href="https://developers.chatway.app/mcp/guides.mcp_connect_clients">Setup guides</a> ·
  <a href="https://developers.chatway.app/mcp/guides.mcp_overview">Documentation</a> ·
  <a href="https://registry.modelcontextprotocol.io/v0.1/servers/io.github.Chatway-app%2Fchatway/versions/latest">Chatway on the Official MCP Registry</a>
</p>

---

The Chatway MCP server connects AI agents to your Chatway inbox over the
[Model Context Protocol](https://modelcontextprotocol.io). Ask your assistant to find
conversations, summarize customer issues, reply to customers, assign agents, add private notes,
search your knowledge base, and organize contacts, all in plain language. Pair it with
[Chatway webhooks](#real-time-events-with-webhooks) to trigger your agents and workflows the moment
a new message or event happens.

**Available on every Chatway plan, including Free.** There is nothing to install or host and no
API key to manage: add the server URL to your AI client and sign in with your Chatway account.

[Chatway Live Chat](https://chatway.app) is an AI-powered customer support platform for live chat,
AI chatbots, WhatsApp, Facebook Messenger, Instagram, and more, with a shared team inbox,
automation, knowledge base, and mobile apps for iOS and Android.

| | |
|---|---|
| Server URL | `https://mcp.chatway.app/mcp` |
| Transport | Streamable HTTP |
| Authentication | OAuth 2.1 (sign in with Chatway, no API key) |
| Who can connect | Chatway workspace owners and admins |
| Plans | All plans, including Free (tag and custom data tools require a paid plan) |
| Registry name | `io.github.Chatway-app/chatway` |

<p align="center">
  <img width="1280" height="800" alt="ChatGPT connected to Chatway through the Chatway MCP server, managing live chat conversations" src="https://github.com/user-attachments/assets/cf8e4e15-13d4-4c8f-a61e-0b6dc6e2db69" />
</p>

<p align="center"><em>
  Chatway MCP in action: Connect ChatGPT and other AI agents to your website live chat to manage
  customer conversations, reply to messages, and access your knowledge base. Use webhooks to
  trigger real-time workflows when new messages or events occur, allowing your AI agents to respond
  faster and automate customer support without constantly checking for updates.
</em></p>

## Quick start

1. [Create a free Chatway account](https://go.chatway.app/register) if you don't have one.
2. Add `https://mcp.chatway.app/mcp` as a custom (remote) MCP connector in your AI client.
3. Sign in to Chatway when prompted and choose the widgets, channels, and permissions to share.
4. Ask your assistant something like "Show my latest unresolved Chatway conversations."

## Supported clients

**Tested by Chatway**

| Client | Setup |
|---|---|
| ChatGPT | [Connect ChatGPT](#chatgpt) |
| Claude | [Connect Claude](#claude) |
| Gemini CLI | [Install the extension](#gemini-cli) |
| Cursor | [Install the plugin](#cursor) |
| GitHub Copilot (VS Code) | [Add the server](#github-copilot-vs-code) |
| Cline | [Add the server](#cline) |

**Works with any client that supports remote MCP servers with OAuth**

Codex, Grok, Devin, Goose, OpenCode, and others. See the
[step-by-step setup guides](https://developers.chatway.app/mcp/guides.mcp_connect_clients)
for each client.

## What you can do

| Area | Capabilities |
|---|---|
| Conversations | List and search conversations, read message history, resolve and reopen |
| Replies and notes | Reply to customers, add private notes for your team |
| Assignment | List agents, assign conversations, hand off from AI to a human agent |
| Contacts | Search contacts and view visitor details |
| Knowledge base | Search help articles to answer customer questions |
| Tags and custom data | Tag conversations, add and update contact custom data (paid plans) |

See the [tool reference](https://developers.chatway.app/mcp/guides.mcp_tool_reference) for
every tool and its parameters.

## Real-time events with webhooks

MCP lets your agent act in Chatway when you ask it to. [Chatway webhooks](https://developers.chatway.app/webhooks/guides.webhooks_overview)
work the other way: Chatway sends a signed HTTPS request to your endpoint as soon as something
happens, such as a new visitor message, a new conversation, or a new contact. Use webhooks to wake
up your AI agent or automation (n8n, Zapier, Make, or your own server) instead of polling, then let
it read and reply through MCP or the [Chatway API](https://developers.chatway.app).

Webhooks are available on all plans, including Free. Set them up in Chatway under
**Settings → Developer Tools → Webhooks**.

### Example: Automatically answer customer support conversations

Combine Chatway webhooks with MCP to build an AI-powered customer support workflow that responds to incoming messages in real time.

Here's how it works:

1. **Customer sends a message:** A visitor sends a question through the Chatway website live chat widget.
2. **Webhook triggers the workflow:** Chatway instantly sends a webhook notification to your AI agent or automation platform (such as n8n, Make, Zapier, or your own server).
3. **AI agent retrieves context:** The agent uses Chatway MCP to read the conversation history, access customer information, and search your knowledge base for accurate answers.
4. **AI agent responds automatically:** The agent generates a relevant response and, when configured and authorized, automatically sends it to the customer through Chatway, without requiring human intervention. Alternatively, the agent can prepare a draft for human review and approval.
5. **Support team stays informed:** The entire conversation remains accessible in the Chatway shared inbox and mobile apps for iOS and Android. Human agents can take over whenever needed.

**Fully automated customer support:** With Chatway webhooks and MCP, you can connect external AI agents to automatically handle incoming customer messages, answer questions, and manage support conversations 24/7.

**Note:** MCP provides access to Chatway's tools and data, while webhooks notify your automation when events occur. Automatic responses require an external AI agent or workflow runner configured to process incoming events and execute MCP actions. MCP alone does not continuously monitor conversations.

[Learn more about Chatway webhooks](https://developers.chatway.app/webhooks/guides.webhooks_overview) | [Explore Chatway MCP](https://developers.chatway.app/mcp/guides.mcp_overview)

## Example prompts

- "Summarize today's unresolved support conversations."
- "Find customers waiting more than 2 hours for a reply."
- "Draft replies for all pricing questions, but don't send them yet."
- "Assign today's billing conversations to Alex."
- "Find conversations about refund issues this week."
- "Search the knowledge base for our refund policy and draft an answer for this customer."
- "Summarize the conversation with jane@example.com and add a private note with next steps."
- "Tag this visitor as `vip` and resolve the conversation."

## Client setup

### ChatGPT

Connect Chatway to ChatGPT to search customer conversations, manage support tickets, access contacts, and work with your knowledge base directly from ChatGPT.

1. Open [ChatGPT](https://chatgpt.com) on the web and go to **Settings → Apps**.
2. Enable **Developer mode** (requires an eligible ChatGPT plan).
3. Open **Browse Plugins**, click **+**, and create a custom MCP app named `Chatway`.
4. Enter `https://mcp.chatway.app/mcp` as the MCP server URL and select **OAuth** authentication. Leave the Client ID and Client Secret empty.
5. Sign in to Chatway and authorize the widgets, channels, and permissions you want ChatGPT to access.
6. Start a conversation, enable the Chatway app, and ask: "Show my latest unresolved Chatway conversations."

Available tools and write capabilities depend on your ChatGPT plan and workspace settings.

[Full ChatGPT setup guide](https://developers.chatway.app/mcp/guides.mcp_connect_clients)

### Claude

Connect Chatway to Claude to manage customer conversations, draft or send replies, assign support tickets, and search your knowledge base.

1. Open [Claude](https://claude.ai) and go to **Customize → Connectors**.
2. Click **+ Add → Add custom connector**.
3. Enter `Chatway` as the name and paste `https://mcp.chatway.app/mcp` as the remote MCP server URL.
4. Follow the connector setup flow, using automatic OAuth registration when prompted. No API key or manually created client credentials are required.
5. Click **Connect**, sign in to Chatway, and authorize the widgets, channels, and permissions Claude can access.
6. Ask Claude: "Summarize my latest Chatway support conversations."

For Claude Team or Enterprise, an organization owner may need to add the connector first. The connection also works with Claude Desktop and other supported Claude clients.

**Claude Code:** Run `claude mcp add --transport http --scope user chatway "https://mcp.chatway.app/mcp"`, then authenticate using `/mcp`.

[Full Claude setup guide](https://developers.chatway.app/mcp/guides.mcp_connect_clients)

### Gemini CLI

Install the Chatway extension in [Gemini CLI](https://github.com/google-gemini/gemini-cli):

```bash
gemini extensions install https://github.com/Chatway-app/chatway-mcp-server
```

Then start `gemini` and sign in to Chatway:

```
/mcp auth chatway
```

A browser window opens to sign in to Chatway and approve access. Once connected, `/mcp list`
shows the `chatway` server and its tools.

| Task | Command |
|---|---|
| Update | `gemini extensions update chatway` |
| Uninstall | `gemini extensions uninstall chatway` |
| Re-authenticate | `/mcp auth chatway` |

Gemini CLI receives the OAuth callback on `localhost`, so sign in on the same machine where
Gemini CLI is running.

### Cursor

Install the **Chatway** plugin from the [Cursor Marketplace](https://cursor.com/marketplace).
The plugin adds the Chatway MCP server and a Chatway rule that guides the agent to confirm before
sending replies or making destructive changes.

1. Install the plugin, then open **Cursor Settings → MCP** (or **Tools & MCP**).
2. Next to the `chatway` server, click **Connect** (or **Needs login**) and sign in to Chatway.
3. Once connected, the Chatway tools are listed under the server and available to the agent.

If you previously added Chatway manually in `~/.cursor/mcp.json`, remove that entry so only the
plugin's server is used.

### GitHub Copilot (VS Code)

Chatway works with GitHub Copilot Chat in VS Code in **Agent** mode.

1. Open the Command Palette (`Cmd/Ctrl + Shift + P`) and run **MCP: Add Server**.
2. Choose **HTTP**, then **Workspace** or **Global**.
3. Paste `https://mcp.chatway.app/mcp` and name the server `chatway`.
4. Trust the server when VS Code asks, then sign in to Chatway in the browser window that opens.
5. In Copilot Chat, switch to **Agent** mode. The Chatway tools appear in the tools picker.

Or add it to `mcp.json` yourself (`.vscode/mcp.json` for a workspace, or **MCP: Open User
Configuration** for all workspaces):

```json
{
  "servers": {
    "chatway": {
      "type": "http",
      "url": "https://mcp.chatway.app/mcp"
    }
  }
}
```

The root key is `servers` (not `mcpServers`), and `"type": "http"` is required.

> **One-click install from the GitHub MCP Registry** (searching `@mcp Chatway` in VS Code
> Extensions) will be available once Chatway is accepted into the curated
> [GitHub MCP Registry](https://github.com/mcp). Until then, use the steps above.

### Cline

Ask Cline: "Set up the Chatway MCP server from https://github.com/Chatway-app/chatway-mcp-server".
Cline follows [llms-install.md](llms-install.md) to add the server.

To add it yourself, open **MCP Servers → Remote Servers**, enter `chatway` as the name, paste
`https://mcp.chatway.app/mcp`, choose **Streamable HTTP**, click **Add Server**, and sign in to
Chatway when prompted. Or add this to Cline's MCP settings JSON:

```json
{
  "mcpServers": {
    "chatway": {
      "type": "streamableHttp",
      "url": "https://mcp.chatway.app/mcp",
      "disabled": false
    }
  }
}
```

`"type": "streamableHttp"` is required. Without it, Cline uses the legacy SSE transport and the
connection fails with HTTP `400`.

### Other clients

Add `https://mcp.chatway.app/mcp` as a remote MCP server using the Streamable HTTP transport and
complete the Chatway sign-in. Client-specific steps for Codex, Grok, and others are in the
[setup guides](https://developers.chatway.app/mcp/guides.mcp_connect_clients).

## Troubleshooting

- **Tools missing or `401` errors:** reconnect or re-authenticate the `chatway` server in your
  client. Tokens are revoked when the connection is disconnected in Chatway.
- **Can't approve access:** only Chatway workspace owners and admins can connect an assistant.
- **A tool isn't available:** that permission wasn't granted, or the tool requires a paid plan.
  Change permissions under **AI → External AI** in Chatway, or reconnect.

## Security and data protection

- **You choose what to share.** During sign-in you pick which widgets, channels, and permissions
  the connection gets. Tools without a granted permission are not offered to the assistant.
- **Role-checked.** Only workspace owners and admins can connect an assistant, and every action
  is limited by the authorizing user's Chatway role.
- **Server-side confirmation for sensitive actions.** Resolving or reopening a conversation,
  assigning it, and removing tags or custom data are not performed on the first call. The server
  returns a one-time confirmation token tied to the exact request, and the action only runs when
  the tool is called again with that token. How the confirmation is shown to you depends on your
  AI client.
- **No passwords or API keys shared.** Connections use OAuth 2.1; your AI client never sees your
  Chatway password.
- **Revocable at any time.** Owners and admins can change permissions or disconnect from
  **AI → External AI** in Chatway; disconnecting revokes the token immediately.
- **Hosted by Chatway.** The server runs on Chatway's infrastructure over HTTPS. This repository
  contains no server code or secrets.

Details: [Permissions & access](https://developers.chatway.app/mcp/guides.mcp_permissions_and_access) ·
[Manage connections](https://developers.chatway.app/mcp/guides.mcp_manage_connections) ·
[Security policy](SECURITY.md)

## About this repository

This repository holds Chatway's public listings for the
[official MCP Registry](https://registry.modelcontextprotocol.io), the
[Gemini CLI extension gallery](https://geminicli.com/extensions/browse/), the
[Cursor Marketplace](https://cursor.com/marketplace), and the
[Cline MCP Marketplace](https://github.com/cline/mcp-marketplace): manifests, logos, and setup
guides. Maintainers: see [MAINTAINING.md](MAINTAINING.md).

## Support

Visit the [Chatway Help Center](https://chatway.app/help) or contact the support team through
live chat on [chatway.app](https://chatway.app).

## License

The manifests, configuration, and documentation in this repository are available under the
[MIT License](LICENSE). The Chatway name and logos are trademarks of Chatway and are not covered by
this license. The hosted Chatway service and MCP server are proprietary.
