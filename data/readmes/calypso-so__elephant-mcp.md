<div align="center">

<img src="plugins/shared/assets/logo.png" alt="Elephant by Calypso" width="200">

# Elephant: PDF AI & Docs Q&A for Claude, ChatGPT and Cursor

**The MCP server that lets your AI chat with your PDFs, documents and web pages, and show the page each answer came from.**

*An elephant never forgets.*

<a href="https://chatgpt.com/plugins/plugin_asdk_app_6afcc7102b508191b4a5d134d6d70bfc"><img src="https://img.shields.io/badge/ChatGPT-official_plugin-171611?style=flat-square" alt="Elephant in ChatGPT's plugin directory"></a>
<a href="https://github.com/calypso-so/elephant-mcp/actions/workflows/ci.yml"><img src="https://github.com/calypso-so/elephant-mcp/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
<a href="https://modelcontextprotocol.io"><img src="https://img.shields.io/badge/MCP-Streamable_HTTP-3B2622?style=flat-square" alt="MCP Streamable HTTP"></a>
<a href="#how-it-works"><img src="https://img.shields.io/badge/auth-OAuth_2.1_%2B_PKCE-E9C4A8?style=flat-square" alt="OAuth 2.1 + PKCE"></a>
<a href="#license"><img src="https://img.shields.io/badge/license-MIT-green?style=flat-square" alt="License: MIT"></a>
<a href="https://glama.ai/mcp/servers/calypso-so/elephant-mcp"><img src="https://glama.ai/mcp/servers/calypso-so/elephant-mcp/badges/score.svg" alt="Elephant MCP server on Glama"></a>
<a href="https://glama.ai/mcp/connectors/io.github.calypso-so/elephant-mcp-server"><img src="https://glama.ai/mcp/connectors/io.github.calypso-so/elephant-mcp-server/badges/score.svg" alt="Elephant MCP connector on Glama"></a>

<a href="#see-it-work"><img src="docs/screenshots/cited-answer.png" alt="Elephant answering a question about a refund policy in a chat, with the answer's key sentence highlighted and the source shown as Refund-Policy.pdf, page 1" width="100%"></a>

<table>
<tr>
<td align="center" width="25%"><h3>1 URL</h3>to connect<br><sub><a href="#install">no key to paste</a></sub></td>
<td align="center" width="25%"><h3>10 tools</h3>on one server<br><sub><a href="#pick-your-server">read, save, organise</a></sub></td>
<td align="center" width="25%"><h3>0 databases</h3>on this server<br><sub><a href="#how-it-works">every request stands alone</a></sub></td>
<td align="center" width="25%"><h3>1 click</h3>to disconnect<br><sub><a href="#privacy">key revoked, access ends</a></sub></td>
</tr>
</table>

**[See it work](#see-it-work) · [What people use it for](#what-people-use-it-for) · [ChatGPT plugin](#the-official-chatgpt-plugin) · [Install](#install) · [Pick your server](#pick-your-server) · [First minute](#first-minute) · [How it works](#how-it-works) · [Privacy](#privacy) · [Build](#build) · [Deploy](#deploy) · [License](#license)**

</div>

---

<table>
<tr>
<th width="50%">Your AI alone</th>
<th width="50%"><img src="plugins/shared/assets/icon.png" width="18" height="18" alt=""> Your AI with Elephant</th>
</tr>
<tr>
<td valign="top">

> I can't see your lease, so I can't say whether you may sublet. Many leases allow it with the landlord's consent; check the subletting clause or ask your landlord.

</td>
<td valign="top">

> Yes, with the landlord's written consent, requested 30 days ahead (clause 14.2).
>
> **Source:** *Lease-2026.pdf*, page 6 · Home bucket

</td>
</tr>
</table>

**Same question. One guess, one answer with its source.** <sub>Illustrative example.</sub>

## See it work

Four things Elephant does that a pasted PDF cannot.

<table>
<tr>
<td width="50%" valign="top">
<img src="docs/screenshots/passage-search.png" alt="A search for warranty coverage period returning two passages from Warranty-Terms.pdf, each with the matching sentence highlighted and its page number" width="100%">
<h3>The exact passage, not a summary of it</h3>
<code>elephant-search</code> returns the wording as the document has it, with the line that matched and the page it is on.
</td>
<td width="50%" valign="top">
<img src="docs/screenshots/several-documents.png" alt="One answer about descaling a kettle that cites two files, a product guide and the warranty terms, each with its page" width="100%">
<h3>One answer, drawn from several documents</h3>
<code>elephant-ask</code> reads across everything you saved and names every file it used, each with its page.
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="docs/screenshots/says-when-it-does-not-know.png" alt="Elephant replying that it could not find a parental leave policy in the saved documents, with the label No sources cited" width="100%">
<h3>It says when it does not know</h3>
No answers from thin air. When your documents do not cover a question, Elephant tells you so and cites nothing.
</td>
<td width="50%" valign="top">
<img src="docs/screenshots/buckets.png" alt="Five buckets, among them Product docs, Policies and Onboarding, each listing its sources and whether they are ready" width="100%">
<h3>Buckets keep your knowledge tidy</h3>
Group sources by team, client or project. Your AI can save into them and reorganise them. It can never delete them.
</td>
</tr>
</table>

<sub>Real answers, recorded from a demo workspace of fictional documents.</sub>

## What people use it for

Save a file once, ask it any time, from whichever AI you already use. Elephant searches the text, tables and images in what you saved and answers only from them.

| You have | You ask | You get |
|---|---|---|
| **Lecture notes, textbooks, slides** | *"Summarise chapter 4 and quiz me on it"* | Study notes you can check against the page |
| **Research papers** | *"Which of my papers measure this, and how?"* | A literature review with the passage behind each claim |
| **A lease, contract or insurance policy** | *"What does it say about ending early?"* | The clause, quoted, with its page |
| **User manuals** | *"How do I reset the filter light?"* | The steps, without reading the manual |
| **Invoices, receipts, statements** | *"What did I pay this supplier last year?"* | Totals, dates and line items from your PDFs |
| **Books and long reports** | *"What is the argument of part two?"* | A summary, then answers to your follow-ups |
| **Meeting notes and screenshots** | *"What did we decide about pricing?"* | The decision, the number or the name you half remember |

**Why not paste the PDF into the chat?** A pasted file lives in one conversation, in one app, until the context runs out. Elephant keeps everything you saved, searches all of it at once, and works the same in Claude, ChatGPT and Cursor.

- **Every answer shows its source**: the file, the page and the passage.
- **It says when it does not know.** If your sources do not cover a question, Elephant says so and adds nothing of its own.
- **Fast or deep, your call.** A quick lookup takes a few seconds; a comparison across several documents gets more work when you ask for it.
- **A second brain with nothing to configure.** It is retrieval-augmented generation (RAG) over your own documents, without a vector database, an embedding model or a pipeline to run.

## The official ChatGPT plugin

<a href="https://chatgpt.com/plugins/plugin_asdk_app_6afcc7102b508191b4a5d134d6d70bfc"><img src="docs/screenshots/chatgpt-plugin.png" alt="Elephant's listing in ChatGPT's plugin directory: Elephant: PDF AI & Docs Q&A, Ask your PDFs, with sources, an Install plugin button, three starter prompts, developer Calypso, category Productivity" width="100%"></a>

**[Elephant: PDF AI & Docs Q&A](https://chatgpt.com/plugins/plugin_asdk_app_6afcc7102b508191b4a5d134d6d70bfc)** is in ChatGPT's plugin directory, published by Calypso and reviewed by OpenAI before it was listed. Install it once and any ChatGPT chat can answer from your PDFs, notes and web pages, with the file and the page on every answer. No key to paste, nothing to install on your computer.

1. **Install** the plugin from ChatGPT's directory.
2. **Sign in** and choose: read only, or also save and organise.
3. **Ask** in any chat. The answer names the file and the page.

<div align="center">

<a href="https://chatgpt.com/plugins/plugin_asdk_app_6afcc7102b508191b4a5d134d6d70bfc"><img src="https://img.shields.io/badge/Install_in_ChatGPT-171611?style=for-the-badge" alt="Install Elephant in ChatGPT"></a>

<sub>Needs an Elephant account. It never deletes your files.</sub>

</div>

## Install

<img src="docs/screenshots/one-url-ten-tools.png" alt="The hosted endpoint https://mcp.calypso.so/elephant/mcp beside Elephant's ten tools in three groups: read, save and organise" width="100%">

Elephant is a hosted MCP server. You give your client one URL; it opens a sign-in, you pick a team and press Allow. No download, no key to paste, nothing to keep secret.

```text
https://mcp.calypso.so/elephant/mcp
```

| Client | How |
|---|---|
| **ChatGPT** | Install [Elephant: PDF AI & Docs Q&A](https://chatgpt.com/plugins/plugin_asdk_app_6afcc7102b508191b4a5d134d6d70bfc) from ChatGPT's plugin directory, then sign in |
| **Claude Code** | `claude mcp add --scope user --transport http elephant https://mcp.calypso.so/elephant/mcp`, then open the sign-in link it prints |
| **Claude Desktop, Cursor, Windsurf, and others** | Add a remote (Streamable HTTP) server with the URL above; the client discovers sign-in on its own |
| **Any MCP client** | Streamable HTTP + OAuth 2.1 with dynamic registration and PKCE. If it can talk to a remote MCP server, it can talk to Elephant |

Hand-written config, where a client wants one:

```json
{ "mcpServers": { "elephant": { "type": "http", "url": "https://mcp.calypso.so/elephant/mcp" } } }
```

Disconnect any time from **API Keys** in Calypso. The connection ends with the key.

### Run it locally

The same server ships on npm as [`@calypsohq/elephant-mcp-server`](https://www.npmjs.com/package/@calypsohq/elephant-mcp-server) for clients that want a local stdio server, or for a key you manage yourself. It needs Node 20 or later and a Calypso API key from **API Keys** in Calypso; the key is read from the environment, never from a flag.

```bash
CALYPSO_API_KEY=sk-… npx -y @calypsohq/elephant-mcp-server
```

| Client | How |
|---|---|
| **Claude Code** | `claude mcp add --scope user -e CALYPSO_API_KEY=sk-… elephant -- npx -y @calypsohq/elephant-mcp-server` |
| **Claude Desktop, Cursor, Windsurf, and others** | Add a stdio server with the config below |

```json
{ "mcpServers": { "elephant": { "command": "npx", "args": ["-y", "@calypsohq/elephant-mcp-server"], "env": { "CALYPSO_API_KEY": "sk-…" } } } }
```

Locally it publishes all ten tools, since the key is yours and the Calypso API decides what it may do. `--preset elephant` keeps it read-only; `--preset elephant-builder` keeps only the add tools. `CALYPSO_API_BASE_URL` points it at another Calypso API.

<sub>Needs an Elephant account: sign up at [elephant.calypso.so](https://elephant.calypso.so). Nothing saved in it yet? Elephant will tell you, and show you the first step — see [First minute](#first-minute).</sub>

## Pick your server

| Server | Endpoint | Scope | Tools |
|---|---|---|---|
| **Elephant by Calypso** · `elephant` | `/elephant/mcp` | `elephant:read`, plus `elephant:write` and `elephant:organise` when you allow them | All ten tools below |
| **Elephant Builder by Calypso** · `elephant-builder` | `/elephant/builder/mcp` | `elephant:write` | The four add tools. Kept for existing connections; Elephant now does the same |

One server does everything, and you decide how much. When you connect, you choose what Elephant may do: read only, or also save and organise. Your assistant is offered exactly the tools you allowed and is told what it cannot do. Nothing in Elephant deletes.

| Tool | What it does |
|---|---|
| `elephant-ask` | Answers from every bucket you have, with sources, including one created a moment ago. `buckets` limits it to up to five; `depth` (`fast`, `balanced`, `deep`) sets how much work the answer gets. Each question stands alone |
| `elephant-search` | The matching passages in full and where they live, no answer written |
| `elephant-list-buckets` | Your buckets (folders of sources), to aim a search |
| `elephant-open-source` | One source's details: name, type, size, and whether it is ready |
| `elephant-add-file` | Adds a file the client attached, a public URL, or base64 bytes |
| `elephant-add-files` | Up to 100 files in one request |
| `elephant-add-website` | Adds a web page; Calypso reads it and writes its title, summary and tags |
| `elephant-create-bucket` | A new bucket to hold sources |
| `elephant-rename-bucket` | A bucket's name or description; the sources in it stay as they are |
| `elephant-move-sources` | Files a source in another bucket. Added there first, then taken out of the old one; nothing is deleted |

## First minute

The hatch lives in the protocol, not on a page. Right after Allow, the next thing a person sees is their assistant's reply — so that is where Elephant introduces itself, and only while it has to:

- **Session instructions** change with the team: empty → *greet briefly, offer the three steps, never answer from general knowledge*; with knowledge → the normal text plus *cite, and open the source on request*.
- **One prompt, `elephant-get-started`** — `/mcp__elephant__elephant-get-started` in Claude Code, a starter wherever the client surfaces prompts. Empty team: add a first source → wait for *ready* → ask something only your files know. Team with knowledge: *"2 buckets, 41 sources ready"* and three questions drawn from its bucket names.
- **The first answer on an empty team is the hatch**: `elephant-ask` and `elephant-search` return the card instead of calling the agent. It stops the moment a source is ready — the only state is the team's knowledge, read fresh (cached 20 s per caller, re-read once when it says empty).

## How it works

```text
your AI client ──POST──▶ mcp.calypso.so/elephant/mcp          server/  (this repo)
   │                401 + WWW-Authenticate ─▶ /.well-known/oauth-protected-resource/elephant/mcp
   └──OAuth 2.1 (PKCE, dynamic registration)──▶ login.calypso.so/oauth/*      Calypso web app
                                                 consent mints a scoped Calypso API key
server verifies the token, unseals the grant's key ──▶ api.calypso.so/v1     Calypso API
```

| Rule | What it means |
|---|---|
| **No state** | No database, no sessions. Every `POST` builds a fresh server for its caller, so any instance serves any request |
| **One key per grant** | Allowing access mints a Calypso API key limited to what you allowed: reading, and saving and organising only if you said so |
| **Tools follow consent** | `tools/list` returns the tools of the scopes your grant carries. A read-only connection sees four tools, and its instructions say what it cannot do |
| **Short, bound tokens** | ES256 JWT, 15 minutes, audience = the endpoint URL. A token for one server is refused on the other |
| **Key travels sealed** | The grant's key rides inside the token, sealed with AES-256-GCM. Only this server and the authorization server hold the key to open it |
| **Revocation is real** | Disconnect revokes the key. Calls fail within a minute, whatever token the client still holds |
| **Fair use** | 120 requests per minute per caller across both servers. Over that: `429` with `Retry-After` |
| **Empty team says so** | A team with no ready source gets the first-minute card instead of an answer, and never a guess |

The authorization server lives in the Calypso web app at `login.calypso.so`, not here. This repo is the MCP server and the packaging for app directories.

## Privacy

- **Your files stay in Calypso.** A file your client attaches reaches Calypso through the client's temporary download link. The bytes never pass through this server, and nothing is written to its disk.
- **No prompts stored here.** The server keeps no database. It logs tool names, ids, counts and errors, never question text, answers or file contents.
- **Your team decides.** Access needs a team member's consent. It ends within 15 minutes of that person leaving the team, and within a minute of Disconnect.
- **No secret anywhere.** Configs and app packages carry only the endpoint URL. A client finds sign-in from the server's protected-resource metadata.

## Build

Node 20 or later. CI runs both on every pull request and every push to `main`, on Node 20 and 22.

```bash
cd server  && npm ci && npm test && npm run lint && npm run smoke   # MCP server
cd plugins && npm ci && npm test && npm run build -- --profile all  # directory packages + SHA256SUMS
```

| Folder | What it is | Read more |
|---|---|---|
| [`server/`](server/) | The MCP server, hosted (Streamable HTTP, OAuth) and local (stdio, published to npm): one class per tool, presets, bearer auth, rate limit, the first-minute hatch | [server/README.md](server/README.md) |
| [`plugins/`](plugins/) | Profiles, skills and the packaging tool for app directories. Same tree, same bytes: builds are reproducible | [plugins/README.md](plugins/README.md) |

Probe a live deployment, `tools/list` included:

```bash
SMOKE_BASE_URL=https://mcp.calypso.so SMOKE_API_KEY=sk-… npm run smoke
```

## Deploy

[`render.yaml`](render.yaml) describes the service: `elephant-mcp`, root `server/`, health check `/healthz`, manual deploys.

The npm package publishes itself from `.github/workflows/publish.yml` on every push to `main` whose `server/package.json` version is not on the registry yet (environment `npm-publish`, secret `NPM_TOKEN`). Bump the version in the same pull request as the change.

| Env | Default | Purpose |
|---|---|---|
| `ELEPHANT_PUBLIC_BASE_URL` | `https://mcp.calypso.so` | Public origin; each endpoint's token audience |
| `CALYPSO_OAUTH_ISSUER` | `https://login.calypso.so` | Authorization server |
| `CALYPSO_API_BASE_URL` | `https://api.calypso.so/v1` | Calypso API |
| `ELEPHANT_TOKEN_ENC_KEY` | none | 32-byte base64 key, shared with the authorization server. Unset: OAuth off, API keys only |
| `ELEPHANT_JWKS_URL` | `<issuer>/.well-known/jwks.json` | Token signing keys |
| `ELEPHANT_REQUESTS_PER_MINUTE` | `120` | Per-caller request budget |
| `PORT` | `8080` | Listen port |

## License

[MIT](LICENSE).

---

<div align="center">

🐘 **You already saved it. Elephant remembers where.**

<sub>
<a href="server/README.md">Server</a> ·
<a href="plugins/README.md">Packaging</a> ·
<a href="render.yaml">Deploy</a> ·
<a href="https://calypso.so">Calypso</a> ·
<a href="https://github.com/calypso-so/elephant-mcp/issues">Issues</a>
</sub>

</div>
