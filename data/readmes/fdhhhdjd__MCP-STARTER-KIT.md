<p align="center">
  <img src="assets/banner.png" alt="MCP Starter Kit — A secure bridge to your backend" width="100%" />
</p>

<h1 align="center">MCP Starter Kit</h1>

<p align="center">
  <b>A production-ready starter to build a secure MCP server for any project</b><br/>
  <sub>Connect Claude, ChatGPT and any AI agent to your backend with just a URL + API key.</sub>
</p>

<p align="center">
  <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white">
  <img alt="MCP" src="https://img.shields.io/badge/MCP-Streamable%20HTTP%20%2B%20stdio-6E56CF">
  <img alt="OAuth 2.0" src="https://img.shields.io/badge/OAuth%202.0-PKCE-2EA043">
  <img alt="License" src="https://img.shields.io/badge/License-MIT-blue">
</p>

---

## What is this?

**MCP Starter Kit** scaffolds a **secure, online MCP (Model Context Protocol) server**
for **any project**. It's the machine-to-machine bridge between an AI agent
(Claude Desktop/Web, ChatGPT, or your own agent) and your backend API — each *tool*
maps to one endpoint and is authenticated with an **API key + scopes**.

```
AI agent ──MCP (Streamable HTTP / stdio / OAuth)──▶ <project>-mcp ──REST + Bearer key──▶ Your backend
```

The kit is project-agnostic: you provide the project name, backend URL and the list
of tools — the templates already ship with all the security hardening baked in.

## Features

- **Two transports** — Streamable HTTP (online, many clients) + stdio (Claude Desktop).
- **Stateless OAuth 2.0** (PKCE S256) so the ChatGPT app / Claude web (which require OAuth,
  with no field to paste an API key) can connect. Header-key auth keeps working in parallel.
- **Security hardening**, ready out of the box:
  - Verify the key against the backend **at `initialize`** (blocks pre-auth DoS).
  - Session cap + idle-TTL sweep, per-IP rate limit on the initialize path.
  - Bind `sha256(key)` to the session; SSRF cross-host block + request timeouts.
  - Audit to **stderr** (stdout is reserved for JSON-RPC), secrets redacted.
  - Non-root Dockerfile, TLS terminated at the reverse proxy.
- **Read-only by default** — add a write scope explicitly if you ever need one.

## How to use

0. (Optional but recommended) Fill [`feature.md`](feature.md) — your project config + the
   list of tools you want. Then tell the agent "scaffold the MCP from feature.md".
1. Or just read / run [`SKILL.md`](SKILL.md) — it asks for the **MCP project name** and
   whether your backend **already has an API-key system**.
   - **Not yet** → follow [`API-KEY-BACKEND-GUIDE.md`](API-KEY-BACKEND-GUIDE.md) to build it
     (hashed keys + scopes + `/ext/me` + a create/edit/revoke admin tab).
   - **Already have it** → scaffold the MCP repo from [`templates/`](templates/).
2. In `templates/`: rename `gitignore` → `.gitignore`, replace `__PROJECT__` with your
   project name, fill `.env`, and add your tools in `src/server.ts`.
3. `npm install && npm run build` → host behind TLS (path `/mcp`) → connect your client.

## Connect a client

| Client | How |
|---|---|
| **Claude Desktop** | `npx -y mcp-remote https://<domain>/mcp --header "Authorization: Bearer <key>"` |
| **Claude web** | Custom connector: URL `/mcp`, header **`x-api-key`** = key |
| **ChatGPT app** | Requires **OAuth** enabled + a Business/Enterprise plan; Auth = OAuth, Streamable HTTP → paste key on the consent page |
| **OpenAI API** | `tools:[{type:"mcp", server_url:".../mcp", headers:{"x-api-key":"<key>"}}]` |

## Structure

```
feature.md                intake form — fill your project config + tool list, then generate
SKILL.md                  workflow + confirmation questions
API-KEY-BACKEND-GUIDE.md  how to build the backend API-key system (if you don't have one)
templates/                full MCP source (just change the name + tool list)
  ├── package.json  tsconfig.json  Dockerfile  .env.example  gitignore  README.md
  └── src/ index config apiClient audit server http oauth stdio (.ts)
```

## License

MIT

---

<p align="center">
  <img src="assets/logo.png" width="140" alt="TàiHeo Dev" /><br/><br/>
  <b>Built by <a href="https://codewebkhongkho.com">codewebkhongkho.com</a></b>
</p>
