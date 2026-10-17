# Basilic

Domain-agnostic starter. API, web, agents, Expo mobile, and the documentation site. The web app is a minimal Generative UI shell (header prompt and canvas).

## Start a product

Use GitHub **Use this template** for a clean git history, or clone this repository:

```bash
git clone https://github.com/blockmatic/basilic.git
cd basilic
pnpm setup
pnpm dev
```

`pnpm dev` does not start Expo.

```bash
pnpm --filter @repo/mobile start
```

Fork [blockmatic/basilic](https://github.com/blockmatic/basilic) only to contribute upstream.

## Setup

```bash
pnpm setup
pnpm dev
```

## Hosts

Local:

- https://basilic.localhost
- https://api.basilic.localhost
- https://agents.basilic.localhost
- https://email.basilic.localhost
- https://docu.basilic.localhost

Production:

- https://basilic-web.vercel.app
- https://basilic-api.vercel.app
- https://basilic-docs.vercel.app

Local Postgres is `127.0.0.1:54422`. Tests use PGlite.

## Auth

Browser sessions use cookies. API keys are hashed, shown once, and sent as `Bearer bask_…` or `X-API-Key`. A `bask_` key is not an eve access JWT. Mobile stores magic-link JWTs in `expo-secure-store` and refreshes with `POST /auth/session/refresh`.

| Client | API URL |
| --- | --- |
| iOS simulator | `https://api.basilic.localhost` |
| Android emulator or a physical device | tunnel or LAN URL, never `.localhost` |

## Checks

```bash
pnpm qa
```
