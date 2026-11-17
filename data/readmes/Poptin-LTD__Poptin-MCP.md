<p align="center">
  <img src="resources/poptin.png" alt="Poptin logo" width="96" height="96">
</p>

<p align="center">
  <h1 align="center">Send email marketing campaigns and analyze popup performance with Poptin MCP</h1>
</p>

<p align="center">
  <a href="https://developers.poptin.com/docs/mcp"><img alt="Documentation" src="https://img.shields.io/badge/Docs-developers.poptin.com-7761DF?style=flat-square"></a>
  <img alt="Transport: Streamable HTTP" src="https://img.shields.io/badge/MCP-Streamable_HTTP-FF6376?style=flat-square">
  <img alt="Authentication: OAuth" src="https://img.shields.io/badge/Authentication-OAuth-FFC163?style=flat-square">
  <a href="LICENSE"><img alt="Repository license: MIT" src="https://img.shields.io/badge/License-MIT-51DBEE?style=flat-square"></a>
  <a href="https://github.com/Poptin-LTD/Poptin-MCP/actions/workflows/validate.yml?query=branch%3Amain"><img alt="CI status on main" src="https://img.shields.io/github/actions/workflow/status/Poptin-LTD/Poptin-MCP/validate.yml?branch=main&amp;label=CI&amp;style=flat-square"></a>
</p>


<p align="center">
  <a href="#connect-in-a-minute">Connect</a> ·
  <a href="#what-you-can-do">Capabilities</a> ·
  <a href="#start-with-a-question">Example requests</a> ·
  <a href="docs/clients.md">Client guides</a> ·
  <a href="#questions-you-might-have">FAQ</a>
</p>

**Poptin MCP is the official connection between your AI agnet and your
[Poptin](https://www.poptin.com) account, so you can create email campaigns, analyze performance, and manage your marketing using natural language.** 

With Poptin MCP, you can:

📧 **Create and send email campaigns**

Prepare newsletters, promotions, and product announcements using an existing template or a custom HTML design. Review your audience and content, send a test, then confirm whether to send or schedule the campaign.

📊 **Analyze email and pop ups performance**

Explore email campaign results and compare popup and form views, conversions, and conversion rates to find opportunities to improve.

🎯 **Build audience segments**

Preview and save segments using supported contact properties, subscription status, and customer activity.

🪟 **Manage existing popups and forms**

Find, rename, pause, or resume existing popups and forms, and manage their domains.

👥 **Organize audience data**

Manage the contact properties and subscription topics used to organize your audience.

Poptin hosts the server. Sign in with OAuth, choose your account, and get started.

<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/204332f8-2bfb-4499-abe1-5f03a7ccd95c" />


## Connect in a minute

You need a Poptin account with permission to connect integrations, and an AI client
that supports **Streamable HTTP with OAuth**. Actions depend on your account's
permissions and enabled features.

| Setting | Value |
| --- | --- |
| Connection name | `Poptin` |
| Server URL | `https://mcp.popt.in/mcp` |
| Transport | Streamable HTTP |
| Authentication | OAuth — sign in to Poptin |

1. Add the server URL in your AI client's MCP or connector settings.
2. Follow the Poptin sign-in flow, select an account or subaccount, and approve access.
3. Enable the connection in your conversation and ask:

   > Show me the popups and embedded forms in my Poptin account.

Each connection belongs to **one authorized account**. Connect another account
separately when you need it. Poptin API keys cannot authenticate this MCP server;
complete sign-in in the browser rather than pasting credentials into chat.

### Pick your client

| Client | Connection route |
| --- | --- |
| Claude | [Remote connector or Claude Code setup](docs/clients.md#claude) |
| Cursor | [MCP configuration or plugin](docs/clients.md#cursor) |
| Codex | [MCP setup or portable plugin](docs/clients.md#codex) |
| GitHub Copilot | [MCP in VS Code](docs/clients.md#github-copilot-in-vs-code) |
| Gemini | [Gemini CLI configuration or extension](docs/clients.md#gemini-cli) |
| Grok | [Custom MCP connector](docs/clients.md#grok) |
| Other MCP clients | [Connect by URL](docs/clients.md#other-mcp-clients) |

The Poptin team has tested OAuth and client connections and received customer
feedback. Marketplace approval is separate. Availability can depend on the
client version, plan, and organization settings.

## What you can do

| Area | Explore | Take action |
| --- | --- | --- |
| **Popups & embedded forms** | Browse your poptins. Compare views, conversions, conversion rates, and performance by device or traffic source. | Rename, pause, resume, change domains, or delete existing poptins. |
| **Email campaigns** | Inspect campaigns, engagement, audiences, and available templates. | Prepare campaign setup and audiences, apply designs, send a test, and send or schedule after confirmation. |
| **Segments** | Preview matching and subscribed contact counts. Inspect saved segments. | Save reusable audiences or delete segments after reviewing the impact. |
| **Contact properties & subscription topics** | Find the fields and preferences already in your account. | Create, update, and manage them for your marketing workflows. |

The current release works with existing popups and forms. Creating popups or
editing their visual design is not available through MCP yet.

## Start with a question

### Find what's working

> Which five popups and forms had the highest conversion rate last month?
> Only include those with at least 100 views.

Follow up with:

> Break down their performance by device. Explain the biggest differences.

### Keep your poptins organized

> Show me the active popups and embedded forms on my website.

Then, using the name of a poptin in your account:

> Rename “Summer offer” to “Welcome offer”.

### Prepare your next email campaign

> Help me prepare a newsletter campaign. Walk me through the audience and
> design, then show me a summary for review before sending.

You can stop at a draft. When you're ready to launch, review the sender, subject,
audience, and design before confirming a send or schedule.

### Build an audience you can reuse

> Preview a segment of subscribed contacts who opened an email campaign but
> did not click. Show me the audience size before saving it.

For more useful results, include the period, website, poptin, or campaign you care
about. Ask your assistant to explain missing data and small samples when comparing
performance.

## Your account, your decisions

- **Your existing access applies.** Connecting an assistant does not expand your
  Poptin permissions or enable features outside your account.
- **Review before launch.** Sending and scheduling email campaigns require explicit
  confirmation. Test-email recipients should also be reviewed.
- **Understand deletions.** Destructive actions require an impact review and fresh
  approval before proceeding.
- **Choose the account at sign-in.** A conversation cannot switch the account
  authorized for an existing connection.

## Questions you might have

<details>
<summary><strong>Do I need to install or host a server?</strong></summary>

No. Poptin runs the server at `https://mcp.popt.in/mcp`. Your client connects to
it directly. This repository contains public documentation, registry metadata,
and client packages; the hosted implementation is maintained by Poptin.

</details>

<details>
<summary><strong>Why is an action unavailable?</strong></summary>

Your current permissions, enabled features, and the state of the item still
apply. Email campaigns, segments, and subscription topics need the corresponding
features. Ask your assistant to explain the returned limitation.

</details>

<details>
<summary><strong>What if sign-in or the connection stops working?</strong></summary>

Check the full URL, including `/mcp`, and confirm that your client supports remote
MCP with OAuth. Complete sign-in and enable the connection for the conversation.
Reconnect through your client if it cannot renew authorization. An empty account
returning no poptins does not mean sign-in failed.

</details>

<details>
<summary><strong>How should I compare analytics?</strong></summary>

Specify the period and metric. Popup and form reporting uses inclusive reporting
dates. Email campaign comparisons use cumulative statistics for campaigns selected
by when they were sent; engagement activity within a period is a different query.
Ask your assistant to explain incomplete or still-processing statistics.

</details>

<details>
<summary><strong>How do I disconnect?</strong></summary>

In Poptin, open **AI connections** and choose **Revoke** for the connection, then
confirm **Revoke access**. Also disable or remove the connection in your AI client
and use its authorization-revocation options. Authorize a new connection whenever
you want to reconnect. If you suspect unauthorized activity, follow the
[security guidance](SECURITY.md#if-you-suspect-your-account-or-an-ai-connection-is-compromised).

</details>

## Help & documentation

[Poptin MCP](https://www.poptin.com/mcp/) ·
[MCP guide](https://developers.poptin.com/docs/mcp) ·
[Poptin Help Center](https://help.poptin.com/en/) ·
[Report a security issue](SECURITY.md) ·
[Privacy policy](https://www.poptin.com/privacy-policy/) ·
[Terms of service](https://www.poptin.com/terms-of-service/)

When contacting support, include your client, the step that failed, and the error
message. Keep passwords and tokens out of your report.

## For maintainers

The [Validate workflow](.github/workflows/validate.yml) checks schemas, manifest
consistency, assets, and documentation.

After merging reviewed changes, run [Publish to MCP Registry](.github/workflows/publish-mcp.yml)
manually from the default branch, or push a fresh `vMAJOR.MINOR.PATCH` repository
tag at a commit on that branch. Publication waits for validation and verifies the
resulting registry record; its Actions summary links to the listing.

Repository tags are independent of the MCP version in `server.json`. An identical
active listing is skipped; changed registry metadata requires a new unique
manifest version. Keep MCP versions consistent across client manifests when
updating them. Protect the default branch and release tags through the team's
normal review process. See the official [publishing guide](https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/github-actions.mdx)
for OIDC details. Client marketplace submissions are separate.

Repository code, configuration, and documentation use the [MIT license](LICENSE).
Poptin branding is excluded; see [license scope and branding](NOTICE.md).
