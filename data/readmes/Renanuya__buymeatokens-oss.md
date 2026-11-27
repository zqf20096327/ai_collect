<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset=".github/assets/logo-dark.svg">
  <img src=".github/assets/logo.svg" width="72" height="72" alt="buymeatokens logo">
</picture>

# buymeatokens

**Buy Me a Coffee, but for AI tokens.**

Open source developers get a page where supporters fund the AI tokens behind their projects.<br>
Payments go straight to the creator's own Stripe, PayPal or USDC wallet. The platform takes no cut.

[Website](https://buymeatokens.com) · [Roadmap](ROADMAP.md) · [Contributing](CONTRIBUTING.md) · [Local setup](docs/development.md) · [Security](SECURITY.md)

[![CI](https://github.com/Renanuya/buymeatokens-oss/actions/workflows/ci.yml/badge.svg)](https://github.com/Renanuya/buymeatokens-oss/actions/workflows/ci.yml)
[![License: AGPL-3.0](https://img.shields.io/badge/license-AGPL--3.0-1c1c1e)](LICENSE)
[![Good first issues](https://img.shields.io/github/issues/Renanuya/buymeatokens-oss/good%20first%20issue?label=good%20first%20issues&color=5b6cf2)](https://github.com/Renanuya/buymeatokens-oss/labels/good%20first%20issue)

[![Buy me AI tokens](https://buymeatokens.com/api/badge/renanuya?style=pill)](https://buymeatokens.com/renanuya)

</div>

---

## How it works

1. **A creator signs in with GitHub** and claims `buymeatokens.com/<username>`.
2. **They connect a payment method they already own:** a Stripe restricted key, a PayPal email or a USDC address on Base.
3. **Supporters buy "token bundles"** from the creator's page or README badge. The money lands in the creator's account directly; buymeatokens never holds funds.

## Features

| | |
|---|---|
| **Creator pages** | GitHub login and an eight-step guided setup: name, payment method, price, project link with live GitHub stats, description, "where the tokens go", a funding goal and socials. Creators can reply to and like supporters' messages. |
| **Write with AI** | Optional: drafts the project description from the repository's README (Gemini or Groq free tiers, capped per creator and per day). |
| **Stripe** | Checkout runs on the creator's own *restricted* key (Checkout Sessions: write only), stored encrypted with AES-256-GCM. No webhooks needed; pending sessions are reconciled. |
| **PayPal** | Classic "Buy Now" links straight to the creator, confirmed through verified IPN messages. |
| **USDC on Base** | Wallet-to-wallet payments verified from on-chain `Transfer` logs. *Experimental:* see [known limitations](docs/payments.md#usdc-on-base-experimental). |
| **README badges** | `/api/badge/<username>` renders an SVG with the tokens raised, in three styles and four themes, drawn from glyph outlines so it needs no web fonts. |
| **Creator emails** | One welcome and at most one setup reminder, sent by a minute worker with atomic delivery claims. |
| **Fair pricing** | Free today, with no subscriptions. Pages created during early access keep lifetime free access. |
| **Creators' data** | Terms and privacy consent with versioning, a payment history CSV, one-click account deletion, and logs that redact anything shaped like a key. |

## Quick start

You need **Node.js 26** (see [`.nvmrc`](.nvmrc)) and **Docker** for a local Postgres.

```bash
git clone https://github.com/Renanuya/buymeatokens-oss.git buymeatokens
cd buymeatokens
npm ci
docker compose up -d db
cp .env.example .env.local      # then fill it in as described in docs/development.md
npm run dev                     # http://localhost:3000
```

> [!WARNING]
> **Only ever point `POSTGRES_URL` at a local or throwaway database.** The app applies its schema on the first
> connection, so a dev server running against production migrates production. You never need production
> credentials to contribute.

Log in with **"Continue without GitHub"** (enabled by `DEV_LOGIN=true` in development), pick a username, add a
Stripe **test-mode** restricted key and pay with `4242 4242 4242 4242`. The full walkthrough is in
[docs/development.md](docs/development.md).

```bash
npm run typecheck   # TypeScript
npm test            # Vitest against an in-memory PGlite database; touches nothing outside the process
npm run build       # production build
```

## Tech stack

[Next.js 16](https://nextjs.org) (App Router) · React 19 · Tailwind CSS 4 · PostgreSQL (Supabase in production) via
[`postgres`](https://github.com/porsager/postgres) · [PGlite](https://pglite.dev) for tests · Vitest · Vercel

See [docs/architecture.md](docs/architecture.md) for how the pieces fit together.

## Contributing

Contributions are welcome. Bug fixes and docs can go straight to a pull request. **For features, open or pick an
issue labelled [`status: accepted`](https://github.com/Renanuya/buymeatokens-oss/labels/status%3A%20accepted) first**,
so nobody spends a weekend on something we can't merge. Early ideas go to
[Discussions → Ideas](https://github.com/Renanuya/buymeatokens-oss/discussions/categories/ideas), where people vote on them.

Start with [CONTRIBUTING.md](CONTRIBUTING.md) and the
[good first issues](https://github.com/Renanuya/buymeatokens-oss/labels/good%20first%20issue).
Using an AI coding agent? Point it at [AGENTS.md](AGENTS.md).

## Roadmap

The priorities, in order, live in [ROADMAP.md](ROADMAP.md) and on the
[project board](https://github.com/users/Renanuya/projects/7). Up next: contributor foundations (versioned
migrations, demo data, smoke tests for the money paths) and a sturdier USDC flow.

## Security

Please **don't** open public issues for vulnerabilities. Report them privately as described in
[SECURITY.md](SECURITY.md).

## License

buymeatokens is free software under the [GNU Affero General Public License v3.0](LICENSE). You can use, study,
change and self-host it. If you run a modified version as a network service, you have to publish your changes
under the same license.

The **buymeatokens** name and logo are not covered by the license; see [TRADEMARKS.md](TRADEMARKS.md).
