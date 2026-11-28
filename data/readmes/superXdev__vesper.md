<picture>
  <source media="(prefers-color-scheme: dark)" srcset="brand/logo/masters/vesper-horizontal-dark.svg">
  <img src="brand/logo/horizontal/vesper-horizontal-black.svg" alt="Vesper logo: a ghost and the Vesper wordmark" height="64">
</picture>

# Vesper

Vesper researches a company and up to 4 competitors from public information, then shows how they appear to acquire customers, where the market is underserved, and which experiments to run next. This page covers what Vesper does, how to run it locally, and how the repo is organized.

Every insight cites the evidence it came from (refs like `A3`), and anything Vesper couldn't check is shown as "Not checked", never as a negative result.

## Screenshots

These screenshots come from a research on vercel.com against Netlify, Cloudflare and AWS. All of them are in [`brand/gallery`](brand/gallery).

<p align="center">
  <img src="brand/gallery/03-overview.png" alt="Research overview for Vercel: positioning, a summary and signal strength per growth channel" width="100%">
  <br><sub><b>Overview:</b> positioning, a summary of the market and how strongly each channel shows up</sub>
</p>

<table>
  <tr>
    <td width="50%" valign="top">
      <img src="brand/gallery/02-competitor-suggestions.png" alt="New research form with suggested competitors for vercel.com">
      <br><sub><b>Pick competitors:</b> Vesper suggests the closest ones before research starts</sub>
    </td>
    <td width="50%" valign="top">
      <img src="brand/gallery/04-competitors.png" alt="Market overview table comparing channel strength for Vercel, Netlify, Cloudflare and AWS">
      <br><sub><b>Competitors:</b> signal strength per channel, side by side</sub>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <img src="brand/gallery/07-content.png" alt="Vercel's most viewed YouTube videos, ranked by views">
      <br><sub><b>Content:</b> each company's posts and videos, most viewed first</sub>
    </td>
    <td width="50%" valign="top">
      <img src="brand/gallery/08-opportunities.png" alt="Top opportunity card with potential, confidence and effort">
      <br><sub><b>Opportunities:</b> gaps in the market, each with an experiment to run</sub>
    </td>
  </tr>
  <tr>
    <td colspan="2" align="center">
      <img src="brand/gallery/10-evidence.png" alt="Evidence drawer showing the source behind a claim" width="50%">
      <br><sub><b>Evidence:</b> every ref opens the source it came from, with how it was observed and when</sub>
    </td>
  </tr>
</table>

## Tech stack

- [Turborepo](https://turborepo.com) and pnpm workspaces for the monorepo
- [Vue](https://vuejs.org) 3, Vite and Tailwind CSS v4 for `web`
- [Hono](https://hono.dev) on Node for `api`
- [BullMQ](https://bullmq.io) on Redis for background research jobs
- PostgreSQL with [Drizzle ORM](https://orm.drizzle.team) for storage
- [Model Context Protocol](https://modelcontextprotocol.io) SDK for the MCP server

## Prerequisites

- Node.js 24.12 or later
- pnpm 10.28 (the version in `package.json` `packageManager`)
- Docker with Compose, for PostgreSQL and Redis

To run Vesper without installing Node.js or pnpm, see [Run with Docker](#run-with-docker).

## Getting started

From the repo root:

1. Install dependencies.

   ```bash
   pnpm install
   ```

2. Create your environment file.

   ```bash
   cp .env.example .env
   ```

3. Start PostgreSQL (port 5433) and Redis (port 6380). The ports are offset so they don't collide with local instances on the default ports.

   ```bash
   docker compose up -d
   ```

4. Create the database tables.

   ```bash
   pnpm db:migrate
   ```

5. Start the API, the worker and the web app.

   ```bash
   pnpm dev
   ```

Open http://localhost:5173 and enter a company website, for example `linear.app`.

To check the API is up:

```bash
curl http://localhost:3000/api/health
```

```text
{"status":"ok"}
```

## Run with Docker

This section runs the whole app in containers: migrations, `api`, the worker and `web`. You only need Docker with Compose 2.24 or later.

1. From the repo root, create your environment file and add any API keys you want to use. Docker works without it, using rule-based analysis only.

   ```bash
   cp .env.example .env
   ```

2. Build the images and start the stack.

   ```bash
   docker compose --profile app up -d --build
   ```

Open http://localhost:8080. Set `VESPER_WEB_PORT` in `.env` to use another port.

The services start in order:

| Service    | Image        | What it does |
| ---------- | ------------ | ------------ |
| `postgres` | `postgres:17-alpine` | Database, stored in the `postgres-data` volume |
| `redis`    | `redis:7-alpine` | Job queue and progress events, stored in the `redis-data` volume |
| `migrate`  | `vesper-api` | Applies migrations, then exits |
| `api`      | `vesper-api` | The API on port 3000, inside the Compose network only |
| `worker`   | `vesper-api` | Runs research jobs |
| `web`      | `vesper-web` | nginx serving `web` and proxying `/api` to `api` |

Compose reads API keys and AI settings from `.env`. It replaces `DATABASE_URL`, `REDIS_URL`, `HOST` and `PORT` with container addresses, so you don't need to edit them. The Scrape Creators response cache is kept in the `vesper-cache` volume.

To use the CLI or MCP server with the Docker stack, point them at `web`, which proxies the API:

```bash
VESPER_API_URL=http://127.0.0.1:8080 pnpm vesper list
```

To follow the logs or stop the stack:

```bash
docker compose --profile app logs -f api worker
docker compose --profile app down
```

`down` keeps your data. Add `-v` to delete the volumes as well.

> [!NOTE]
> Inside a container, `localhost` is the container itself. If `OPENAI_COMPATIBLE_BASE_URL` points at a server on your machine, use `http://host.docker.internal:<port>` instead. The `claude-code` and `codex` engines need those CLIs installed, so they aren't available in Docker.

> [!WARNING]
> The API has no authentication yet. Compose publishes `web` on 127.0.0.1 only. Don't expose it on a public address without a proxy that adds authentication.

A plain `docker compose up -d` still starts only PostgreSQL and Redis, for the `pnpm dev` setup above. Don't run the `app` profile and `pnpm dev` against the same Redis: both workers would take jobs from the same queue.

## Scripts

Run these from the repo root.

| Script            | Description                                                       |
| ----------------- | ----------------------------------------------------------------- |
| `pnpm dev`        | Start `api` (server and worker) and `web` in watch mode           |
| `pnpm build`      | Build `web` for production                                        |
| `pnpm type-check` | Type-check every workspace                                        |
| `pnpm lint`       | Lint `web` with oxlint and ESLint                                 |
| `pnpm test`       | Run the `core` test suite (Vitest)                                |
| `pnpm db:migrate` | Apply database migrations                                         |
| `pnpm db:generate`| Generate a migration after changing `packages/db/src/schema.ts`   |
| `pnpm vesper`     | Run the CLI, for example `pnpm vesper list`                       |

## Environment variables

All apps read `.env` at the repo root. Values already set in the shell take priority.

| Name                          | Required | Default                                         | Description |
| ----------------------------- | -------- | ----------------------------------------------- | ----------- |
| `DATABASE_URL`                | Yes      | none                                            | PostgreSQL connection string. `.env.example` points at the Compose service. |
| `REDIS_URL`                   | Yes      | none                                            | Redis connection string for the job queue and progress events. |
| `PORT`                        | No       | `3000`                                          | API port. |
| `HOST`                        | No       | `127.0.0.1`                                     | API bind address. The API has no authentication yet, so keep it on loopback. |
| `CORS_ORIGIN`                 | No       | `http://localhost:5173`                         | Allowed browser origins, comma-separated. |
| `WORKER_CONCURRENCY`          | No       | `2`                                             | Research runs one worker processes in parallel. |
| `VESPER_API_URL`              | No       | `http://127.0.0.1:3000`                         | API address used by the CLI and MCP server. |
| `SCRAPECREATORS_API_KEY`      | No       | none                                            | Unlocks ad libraries, social stats, founders and Reddit. Without it those areas show as "Not checked". |
| `SCRAPECREATORS_MAX_CREDITS`  | No       | `50`                                            | Credit cap per company per run. |
| `AI_PROVIDER`                 | No       | `none`                                          | Default analysis engine: `none`, `anthropic`, `openai`, `openai-compatible`, `claude-code` or `codex`. |
| `AI_MODEL`                    | No       | Provider default                                | Model for the chosen provider. Required for `openai-compatible`. |
| `ANTHROPIC_API_KEY`           | For `anthropic` | none                                     | Anthropic API key. |
| `OPENAI_API_KEY`              | For `openai`    | none                                     | OpenAI API key. |
| `OPENAI_COMPATIBLE_BASE_URL`  | For `openai-compatible` | none                             | Base URL of an OpenAI-compatible server, such as OpenRouter or Ollama. |
| `OPENAI_COMPATIBLE_API_KEY`   | No       | none                                            | Key for the OpenAI-compatible server, if it needs one. |
| `VESPER_MCP_ALLOW_RESEARCH`   | No       | unset                                           | Set to `1` to let MCP clients start new research. |
| `VESPER_WEB_PORT`             | No       | `8080`                                          | Host port for `web` when you [run with Docker](#run-with-docker). |

## Analysis engines

Vesper always runs a rule-based analysis. An AI engine, when configured, adds positioning and cross-source insights on top. The AI only sees normalized evidence, must cite evidence refs for every claim, and claims that cite refs that don't exist are discarded. If the AI call fails, the rule-based result is used.

| `AI_PROVIDER`       | How it runs                                             | Billing                    |
| ------------------- | ------------------------------------------------------- | -------------------------- |
| `none`              | Rule-based only                                         | Free                       |
| `anthropic`         | Anthropic Messages API with structured output           | Per token                  |
| `openai`            | OpenAI Chat Completions with a JSON schema              | Per token                  |
| `openai-compatible` | Any OpenAI-compatible server at `OPENAI_COMPATIBLE_BASE_URL` | Depends on the server |
| `claude-code`       | Your installed `claude` CLI, with no tools or MCP servers | Your Claude subscription |
| `codex`             | Your installed `codex` CLI in a read-only sandbox       | Your ChatGPT subscription  |

For `claude-code` and `codex`, Vesper removes `ANTHROPIC_API_KEY` and `OPENAI_API_KEY` from the CLI's environment so your subscription login is used. You can also pick an engine per research under **Advanced options** in `web`, or with `--ai` in the CLI.

## Project structure

```text
.
├── apps/
│   ├── api/        Hono API and BullMQ worker
│   ├── cli/        vesper CLI and read-only MCP server
│   └── web/        Vue web app
├── packages/
│   ├── core/       Collectors, analysis, AI providers, shared types
│   └── db/         Drizzle schema and migrations
├── deploy/
│   └── nginx.conf  nginx config for the web image
├── Dockerfile      api and web images
├── docker-compose.yml
├── DESIGN.md       Visual direction for web
└── turbo.json
```

## Related docs

- [api README](apps/api/README.md): routes, worker and progress events
- [cli README](apps/cli/README.md): commands and MCP setup
- [web README](apps/web/README.md): pages and design tokens
- [core README](packages/core/README.md): research pipeline and evidence model
- [db README](packages/db/README.md): data model and migrations
- [DESIGN.md](DESIGN.md): palette, typography and motion

## License

MIT, see [LICENSE](LICENSE). The collectors in `packages/core/src/collect` include code adapted from a third-party MIT project; its license is in `packages/core/LICENSE.reverse-engineer-marketing`.
