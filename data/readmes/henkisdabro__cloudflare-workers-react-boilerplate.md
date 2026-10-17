# Cloudflare Workers + React Boilerplate

[![CI and Deploy](https://github.com/henkisdabro/cloudflare-workers-react-boilerplate/actions/workflows/deploy.yml/badge.svg)](https://github.com/henkisdabro/cloudflare-workers-react-boilerplate/actions/workflows/deploy.yml)
[![Release](https://img.shields.io/github/v/release/henkisdabro/cloudflare-workers-react-boilerplate?style=flat)](https://github.com/henkisdabro/cloudflare-workers-react-boilerplate/releases)
[![Licence](https://img.shields.io/github/license/henkisdabro/cloudflare-workers-react-boilerplate?style=flat)](LICENSE)
[![Use this template](https://img.shields.io/badge/Use_this-template-2EA44F?style=flat&logo=github)](https://github.com/henkisdabro/cloudflare-workers-react-boilerplate/generate)

[![React](https://img.shields.io/badge/React-19-61DAFB?style=flat&logo=react&logoColor=black)](https://react.dev)
[![Vite](https://img.shields.io/badge/Vite-8-646CFF?style=flat&logo=vite&logoColor=white)](https://vite.dev)
[![TypeScript](https://img.shields.io/badge/TypeScript-6-3178C6?style=flat&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Node.js](https://img.shields.io/badge/Node.js-24-5FA04E?style=flat&logo=nodedotjs&logoColor=white)](https://nodejs.org/)
[![pnpm](https://img.shields.io/badge/pnpm-12-F69220?style=flat&logo=pnpm&logoColor=white)](https://pnpm.io)
[![Cloudflare Workers](https://img.shields.io/badge/Cloudflare-Workers-F38020?style=flat&logo=cloudflare&logoColor=white)](https://developers.cloudflare.com/workers/)
[![Claude Code](https://img.shields.io/badge/Built_for-Claude_Code-D97757?style=flat&logo=claude&logoColor=white)](https://claude.com/claude-code)

**For sites that do things, not just show them.** The moment your site needs to keep a secret or
remember something - an AI feature, a form that saves, a page only your clients see - it needs code on
a server. This GitHub template gives you one: a React app and its `/api/*` back end on a single
Cloudflare Worker, set up with [Claude Code](https://claude.com/claude-code) and running on the free
plan.

Site: <https://henkisdabro.github.io/cloudflare-workers-react-boilerplate/>

## Is this for you?

Most sites don't need it. Pick by what your site has to do:

| Your site... | Use |
|---|---|
| **shows things** - portfolio, brochure, landing page, docs | Plain files on [Workers static assets](https://developers.cloudflare.com/workers/static-assets/), or [Astro](https://developers.cloudflare.com/workers/framework-guides/web-apps/astro/). Not this. |
| **lives on search** - blog, content-led shop, anything where ranking and link previews come first | A server-rendered framework: [Astro](https://developers.cloudflare.com/workers/framework-guides/web-apps/astro/), [React Router](https://developers.cloudflare.com/workers/framework-guides/web-apps/react-router/) or [TanStack Start](https://developers.cloudflare.com/workers/framework-guides/web-apps/tanstack-start/). Not this. |
| **does things** - calls an AI model with your key, saves what people send, shows each client their own data | **This template.** |

It is built for one person or a small team shipping an app with Claude Code: a paid AI tool, a
booking or waitlist form backed by a database, a client portal, an internal dashboard. Workers run
per request, so it is not the place for a long-running Node.js server.

### Why not `pnpm create cloudflare`?

Cloudflare's own starter gives you the same React and Worker setup in one command - use it if you are
happy wiring up the rest yourself. This template adds the parts a solo builder otherwise spends their
first week on:

- **Guided setup** - `/start` takes you through Cloudflare credentials, GitHub secrets, a custom
  domain and the first deploy.
- **A safety net** - CI tests every pull request and deploys `main` only after lint, types, tests and
  build pass.
- **The hard parts, done once** - working examples for AI calls with hidden keys, forms saved to D1
  and sessions in KV.
- **An agent that knows the project** - `AGENTS.md`, slash commands and guides written for Claude
  Code.

Sign-in is not built in. The KV sessions example covers the cookie side; for a client portal,
[Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/applications/configure-apps/self-hosted-public-app/)
in front of the app is the quickest route.

## What you get

- **Vite 8 + React 19 + TypeScript 6** with `@vitejs/plugin-react` and the
  [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/), so `pnpm dev`
  runs your Worker in the real `workerd` runtime alongside hot reload.
- **A Worker back end** (`worker/index.ts`) with `GET /api/health`, a catch-all `/api/*` route and
  security headers on API responses. Everything else is served as static assets with SPA fallback.
- **Vitest 5 + Testing Library** with jsdom, and **ESLint 10** flat config.
- **CI and deploy** in `.github/workflows/deploy.yml`: lint, type-check, test and build on every pull
  request and push to `main`, then deploy from `main`.
- **Claude Code commands** for setup, planning and adding Cloudflare features - see
  [below](#claude-code-commands).
- **Supply-chain defaults**: exact-pinned dependencies and a three-day `minimumReleaseAge` in
  `pnpm-workspace.yaml`, so a version published in the last three days refuses to install.

## Quick start

You need [Node.js 24](https://nodejs.org/en/download) (pinned in `.nvmrc`), a free
[Cloudflare account](https://dash.cloudflare.com/sign-up), a GitHub account and pnpm. No pnpm yet? Run
`npx get-pnpm` once and open a new terminal; from then on pnpm switches to the version pinned in
`packageManager` by itself.

1. Click **Use this template** on GitHub.
2. Clone, install and run - swap in your repository's URL and folder name, and leave it running:

   ```bash
   git clone https://github.com/you/your-app.git && cd your-app && pnpm install && pnpm dev
   ```

   The app is at <http://localhost:5173>, the API at `/api/health`.
3. In a second terminal, open the project in Claude Code the way you usually do - `cd your-app && claude`,
   the desktop app or your editor's extension.
4. Type `/start` into Claude Code, or follow [Manual setup](#manual-setup).

`/start` renames the project from its placeholder name, replaces the template's `AGENTS.md` with a
project version, collects your Cloudflare account ID and API token, adds the GitHub secrets, optionally
sets up `@claude` on GitHub and a custom domain, and deploys.

### Manual setup

1. **Rename the project.** `name` in `package.json` and `wrangler.jsonc` both ship as `init`; the
   Wrangler name becomes your Worker's name and its `workers.dev` address.
2. **Replace the agent file.** Copy `docs/PROJECT-AGENTS-TEMPLATE.md`'s starter block over `AGENTS.md`
   and fill it in. The template's own `AGENTS.md` describes the template, not your project.
3. **Get credentials.** Your
   [account ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/) and
   an [API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) made
   from the **Edit Cloudflare Workers** template. Add D1 edit permission if you will use D1.
4. **Add GitHub secrets** under **Settings > Secrets and variables > Actions**:
   `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`.
5. **Clean up the template's own files.** Delete `CHANGELOG.md` and the promotional site
   (`docs/index.html`, `docs/404.html`, `docs/.nojekyll`, `docs/css/`, `docs/js/`, `docs/README.md`).
   `LICENSE` is the template's MIT licence in its author's name - put your own name in it, or delete it.
6. **Push to `main`.** The workflow deploys and prints the URL. If it ran before the secrets existed,
   re-run it from the Actions tab.

## Project structure

```
.
├── src/                    # React app (App.tsx, main.tsx, test/setup.ts)
├── worker/index.ts         # Worker: /api/* routes and security headers
├── public/                 # Static files copied as-is
├── examples/               # Copy-in reference code: ai/ and database/
├── docs/                   # Beginner guides, plus the GitHub Pages site (index.html)
├── PRPs/                   # Plans written by /generate-prp
├── .claude/                # Slash commands, /start branches, templates and settings
├── .github/workflows/      # deploy.yml (CI and deploy)
├── wrangler.jsonc          # Worker config: assets, observability, commented binding examples
├── worker-configuration.d.ts  # Generated by `pnpm cf-typegen` - commit it
├── vite.config.ts          # React + Cloudflare plugins
├── vitest.config.ts
├── tsconfig.*.json         # Separate projects for app, worker and node tooling
├── AGENTS.md               # Agent instructions (CLAUDE.md imports it)
├── .mcp.json               # Cloudflare API MCP server for Claude Code
├── CHANGELOG.md            # Template release notes - /start deletes it
└── LICENSE                 # MIT - /start asks whether to keep it
```

## Scripts

| Command              | What it does                                                    |
| -------------------- | --------------------------------------------------------------- |
| `pnpm dev`           | Vite dev server with the Worker running in `workerd`            |
| `pnpm build`         | Type-check all projects (`tsc -b`) and build                    |
| `pnpm preview`       | Build, then serve the production output locally                 |
| `pnpm lint`          | ESLint                                                          |
| `pnpm test`          | Vitest once (`pnpm test:watch` to watch, `pnpm test:coverage` for a report) |
| `pnpm run deploy`    | Build, then `wrangler deploy` (`pnpm deploy` is a pnpm built-in) |
| `pnpm cf-typegen`    | Regenerate `worker-configuration.d.ts` after any binding change |

Before pushing, run `pnpm lint && pnpm test && pnpm build`. CI runs the same three, plus
`wrangler types --check`.

Wrangler is a dev dependency, so call it through pnpm: `pnpm exec wrangler tail`,
`pnpm exec wrangler secret put NAME`, `pnpm exec wrangler d1 migrations apply DB --remote`.

## Deploying

Pick one way to deploy to production. They can all coexist with local `pnpm run deploy`.

### GitHub Actions (default)

`.github/workflows/deploy.yml` has two jobs:

- **verify** runs on every pull request and push to `main`: frozen-lockfile install,
  `wrangler types --check`, lint, test, build.
- **deploy** runs after verify on pushes to `main` only, using
  [`cloudflare/wrangler-action`](https://github.com/cloudflare/wrangler-action). It is skipped in the
  template repository itself and runs once your generated repository is no longer a template.

It needs two repository secrets: `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`. Node and pnpm
versions come from `.nvmrc` and `packageManager`, so CI matches your machine.

### Workers Builds (Cloudflare's Git integration)

[Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/) builds and deploys from
Cloudflare when you push, posts preview URLs on pull requests and needs no GitHub secrets. To switch:

1. Delete the `deploy` job from `.github/workflows/deploy.yml`. Keep `verify` so pull requests are still
   checked.
2. In the Cloudflare dashboard, open **Workers & Pages**, create or select the Worker and connect the
   repository. The Worker name must match `name` in `wrangler.jsonc`.
3. Set the build command to `pnpm run build`, and add a `PNPM_VERSION` build variable matching
   `packageManager` - the build image ships an older pnpm by default.

See [limits and pricing](https://developers.cloudflare.com/workers/ci-cd/builds/limits-and-pricing/)
for build minutes on each plan.

### From your machine

```bash
pnpm exec wrangler login   # once
pnpm run deploy
```

Alternatively, put `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID` in `.env` (see `.env.example`).

### Bindings and auto-provisioning

`wrangler.jsonc` carries commented D1, KV, R2 and Workers AI bindings. KV, D1 and Queues bindings may
leave out their ID, and R2 its bucket name: `wrangler deploy` creates the resource and writes the ID
back to `wrangler.jsonc`
([automatic provisioning](https://developers.cloudflare.com/workers/wrangler/configuration/#automatic-provisioning)).
Run that first deploy from your machine and commit the result - a CI deploy creates the resource but
writes the ID only into the runner's throwaway checkout. The API token needs edit permission for each
product it provisions.

Run `pnpm cf-typegen` after any binding change, or CI's `wrangler types --check` fails.

## Free tier

The template runs on the Workers Free plan: 100,000 requests a day and 10 ms of CPU per request, with
free tiers for D1, KV and R2. Workers Logs are on by default (`observability` in `wrangler.jsonc`) and
move to Cloudflare Observability pricing from 2026-12-01. Check
[Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/) and
[limits](https://developers.cloudflare.com/workers/platform/limits/) for current figures, and
[docs/cloudflare-products-explained.md](docs/cloudflare-products-explained.md) for a plain-English
overview.

## Secrets

- **Local:** `cp .dev.vars.example .dev.vars` and fill it in. Values appear on the Worker's `env`
  during `pnpm dev`. `.dev.vars` is gitignored.
- **Production:** `pnpm exec wrangler secret put ANTHROPIC_API_KEY`.
- **CI:** repository secrets, as above.

## Claude Code commands

| Command                   | Use it to                                                          |
| ------------------------- | ------------------------------------------------------------------ |
| `/start`                  | Set up a new project from the template - run this first            |
| `/generate-prp <feature>` | Research a feature and write a plan to `PRPs/`                     |
| `/execute-prp <file>`     | Implement a plan and run its validation gates                      |
| `/add-ai-feature`         | Add Claude API, Workers AI or AI Gateway features                  |
| `/setup-database`         | Add D1 or KV, with migrations and types                            |
| `/add-binding`            | Add R2, Queues, Durable Objects and other bindings                 |
| `/setup-sandbox`          | Add the Cloudflare Sandbox SDK for isolated code execution         |

Details are in [.claude/README.md](.claude/README.md). `.mcp.json` connects the
[Cloudflare API MCP server](https://developers.cloudflare.com/agents/model-context-protocol/mcp-servers-for-cloudflare/),
which lets Claude Code inspect and manage resources in your Cloudflare account.

To have Claude answer `@claude` mentions on pull requests and issues, see
[docs/GITHUB_ACTIONS_CLAUDE.md](docs/GITHUB_ACTIONS_CLAUDE.md).

## Documentation

| Guide                                                                      | Covers                                                  |
| -------------------------------------------------------------------------- | ------------------------------------------------------- |
| [CLOUDFLARE_WORKERS.md](CLOUDFLARE_WORKERS.md)                             | Bindings, Worker patterns and operations                |
| [AI_INTEGRATION.md](AI_INTEGRATION.md)                                     | Claude API, Workers AI and AI Gateway                   |
| [SANDBOX.md](SANDBOX.md)                                                   | Sandbox SDK                                             |
| [examples/README.md](examples/README.md)                                   | Copying the AI and database examples into your app      |
| [docs/GITHUB_ACTIONS_CLAUDE.md](docs/GITHUB_ACTIONS_CLAUDE.md)             | `@claude` in GitHub pull requests and issues            |
| [docs/choosing-deployment.md](docs/choosing-deployment.md)                 | Deployment options in plain English                     |
| [docs/cloudflare-products-explained.md](docs/cloudflare-products-explained.md) | Workers, KV, D1 and R2 for beginners               |
| [docs/glossary.md](docs/glossary.md)                                       | Terms used in these docs                                |
| [docs/CONVENTIONS.md](docs/CONVENTIONS.md)                                 | Spelling and punctuation conventions                    |

## Contributing

Issues and pull requests are welcome on
[henkisdabro/cloudflare-workers-react-boilerplate](https://github.com/henkisdabro/cloudflare-workers-react-boilerplate).
Read [AGENTS.md](AGENTS.md) first: every file here is copied into every generated project, so changes
must hold true in projects you have never seen.

## Licence

[MIT](LICENSE).
