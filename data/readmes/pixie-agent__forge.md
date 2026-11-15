# Forge

[English](README.md) | [简体中文](README.zh-CN.md)

Forge is an AI application generation and hosting platform maintained by [Pixie Agent](https://github.com/pixie-agent). Users describe what they want in natural language; an agent plans, writes and builds a multi-file React app inside an isolated workspace, while a Cloudflare Worker handles accounts, jobs, data and publishing.

> **Licensing:** the Forge platform source is available under the [PolyForm Noncommercial 1.0.0](LICENSE) license for non-commercial use only. Commercial deployments, internal business use, paid integrations or hosted services require [written commercial authorization](COMMERCIAL-LICENSE.md). The platform template bundled into Forge-generated apps is Apache-2.0 — see `agent/template/LICENSE`.

Live instance: [app.1forgen.site](https://app.1forgen.site)

## Features

- Natural-language generation and conversational editing of multi-file React apps
- Real-time streaming of planning, code changes and build progress, with automatic fallback from SSE to polling
- Version history, draft preview, one-click publishing and source export
- D1 for platform metadata, R2 for build artifacts, KV, plus per-project × per-environment Durable Object SQLite
- Image and text attachments, follow-up requests during execution, and resume from failure checkpoints
- Email verification, Google sign-in, credits and Creem billing
- Generated-app connectors such as GA4 and Stripe
- 11-language user interface (Chinese, English, Japanese, Korean, Russian, Spanish, French, German, Italian, Portuguese, Dutch), plus a separate admin console

## Architecture

```text
Browser
  │
  ▼
Cloudflare Worker (Hono)
  ├─ Web SPA / API / SSE / publishing and preview
  ├─ D1: accounts, projects, jobs, versions and billing metadata
  ├─ R2: source snapshots, build artifacts, attachment objects
  ├─ KV: generated-app key-value data
  └─ Durable Object SQLite: per-project × per-environment app data
  │
  │ POST /run + X-Agent-Secret
  ▼
Google Cloud Run Agent
  ├─ pi coding agent
  ├─ Disposable working directory
  ├─ Vite + React template with deterministic builds
  └─ Progress, checkpoint, success and failure callbacks
```

After creating a job, the Worker dispatches the Agent via `waitUntil` and does not hold a long connection to Cloud Run for the result. The Agent reports back continuously through internal endpoints protected by `X-Agent-Secret`; the final `commit` or `fail` callback settles the job's terminal state.

For the detailed design see [docs/FORGE2.md](docs/FORGE2.md). Before the first public release, complete the organization setup and final review in the [public release checklist](docs/PUBLIC_RELEASE_CHECKLIST.md).

## Repository layout

```text
src/                    Cloudflare Worker, API and Durable Objects
web/                    React admin and user interface
agent/                  Cloud Run agent
agent/template/         React template copied into generated apps
scripts/                Deploy guards and operations scripts
docs/                   Architecture, connectors and self-hosting docs
schema*.sql             Fresh-database schema and incremental migrations
wrangler.jsonc          Maintainer environment configuration
wrangler.example.jsonc  Self-hosting configuration template
```

## Requirements

- Node.js 22.19 or higher (below 23)
- npm 10 or higher
- A Cloudflare account; the Wrangler CLI is provided by project dependencies for local development
- A model service compatible with the OpenAI, Anthropic Messages or OpenAI Responses dialect
- Google Cloud CLI and Cloud Run, for full agent deployment

The repository contains four independent lockfiles. Install all dependencies:

```bash
nvm use
npm run bootstrap
```

## Local development

Copy the local configuration:

```bash
cp .dev.vars.example .dev.vars
cp agent/.env.example agent/.env
```

Edit both files: make sure the Worker and the Agent share the same `AGENT_SECRET`, and configure the model endpoint, model ID and API key in `agent/.env`. In `.dev.vars`, both `AGENT_URL` and `AGENT_URL_FREE` should point to `http://localhost:8080`; the maintainer config already carries a production free-channel agent address, so overriding only `AGENT_URL` would send local free-channel jobs to production by mistake. The real configuration files are excluded by `.gitignore`.

Initialize the local D1 database:

```bash
npm run db:init:local
```

Start the three processes in separate terminals:

```bash
# Terminal A: agent, http://localhost:8080
npm run dev:agent

# Terminal B: worker, http://localhost:8787
npm run dev

# Terminal C: web, http://localhost:5173
npm run dev:web
```

Open `http://localhost:5173`. Published pages and preview pages are served by the Worker; verify them at `http://localhost:8787/s/<slug>/` or `/p/<token>/`.

On a fresh local database, if Resend or Google OAuth is not configured, email sign-up creates a pending account that never receives mail. For local development only, you can verify the account manually and top up trial credits after registering:

```bash
npx wrangler d1 execute DB --local --command="UPDATE users SET email_verified = 1, credits = 20 WHERE email = 'you@example.com'"
```

Adjust the email, then sign in again. Never run this development command against a remote database.

## Checks

```bash
npm run check
```

This command type-checks the Worker, Web and Agent, and builds the Web app, the Agent and the generated-app template. GitHub Actions runs the same command on `main`, `staging` and every pull request.

## Self-hosting

Do not reuse the Pixie Agent production resource configuration checked into this repository. Start from the template and create your own Cloudflare and Google Cloud resources:

```bash
cp wrangler.example.jsonc wrangler.jsonc
```

Replace the template's D1, KV, R2, agent URL, public URL and email settings, then set the required secrets. For the full procedure and security boundaries see [docs/SELF_HOSTING.md](docs/SELF_HOSTING.md).

## Security boundaries

- Requests between the Worker and the Agent use a shared `X-Agent-Secret` in both directions.
- Generated pages run in a CSP sandbox without `allow-same-origin` and cannot read Forge's main-site cookies.
- The published-app data API does not read Forge login cookies; it suits public site data and must not hold secrets.
- The admin console is enabled only after `ADMIN_PASSWORD` is set.
- `.dev.vars`, `.env`, cloud credentials, local databases and `.wrangler/` must never be committed.

Report vulnerabilities privately per [SECURITY.md](SECURITY.md); do not open public issues with exploit details or credentials.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CONTRIBUTING.md) first. Changes are recorded in [CHANGELOG.md](CHANGELOG.md). External code contributions require completing Pixie Agent's contributor licensing arrangement before merging, so the project can offer both the noncommercial source license and separate commercial licensing.

## License

- Forge platform: [PolyForm Noncommercial License 1.0.0](LICENSE)
- Commercial use: [COMMERCIAL-LICENSE.md](COMMERCIAL-LICENSE.md)
- Generated-app template: [Apache License 2.0](agent/template/LICENSE)
- Third-party components: [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)

Public availability of the source code does not grant commercial-use rights, nor does it grant any trademark rights in Forge or Pixie Agent.
