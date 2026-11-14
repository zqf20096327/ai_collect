# Vacant

**Describe the brand you want. Vacant suggests names with AI and shows only the domains you can actually register.**

[![CI](https://github.com/martian56/vacant/actions/workflows/ci.yml/badge.svg)](https://github.com/martian56/vacant/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-black.svg)](LICENSE)
[![Container](https://img.shields.io/badge/ghcr.io-vacant-2496ed.svg)](https://github.com/martian56/vacant/pkgs/container/vacant)

Vacant is a free, open-source, self-hostable domain finder. Clone it and run it, or pull the prebuilt container. Nothing is hosted for you and nothing is monetized.

## Screenshots

![Vacant home screen](docs/screenshots/hero.png)

Only-available results, checked live and ranked best first:

![Available domain results](docs/screenshots/results.png)

Patterns are highlighted as you type, so you can see the shape of the name:

![Pattern highlighting](docs/screenshots/patterns.png)

## Features

- **Two ways to search**: describe a brand in plain words, or sketch its shape with patterns.
- **Only available names**: every suggestion is checked against the registries before you see it.
- **Ranked best first**: results are scored for length, pronounceability, and brandability.
- **Live price estimates**: a keyless lookup adds a yearly price to each available name.
- **Save and revisit**: favorites and recent searches are kept locally in your browser.
- **Self-hostable**: one command with Bun, or one container. Bring your own API key.

## How it works

Type in two ways, or mix them:

- **Plain words**: `a calm fintech brand, short and warm`. The AI proposes brandable names.
- **Patterns**: sketch the shape of the name.
  - `(animals)`: a slot the AI fills in.
  - `(com/io)`: exact options, no AI, no guessing.
  - Everything else is literal: `get(action word)app.(com/io)`.

Every suggestion is ranked best-first, then checked for real registration availability. You only see names you can register, each with a live price estimate and a one-click link to a registrar.

Availability is resolved server-side through a cascade that is free and key-optional for most TLDs:

1. **RDAP**: the authoritative registry lookup (from the IANA bootstrap).
2. **DNS**: an existing `A` record proves a domain is taken.
3. **WHOIS**: a fallback for TLDs the first two miss.
4. **Domainr**: an optional final fallback if you supply a key.

Results stream back as each domain resolves, behind a shared cache and a concurrency limit, so a search of dozens of names is one request, not a storm.

## Quick start

Requires [Bun](https://bun.sh).

```bash
bun install
cp .env.example .env.local   # add your OpenRouter key
bun dev
```

Open http://localhost:3000.

## Environment variables

| Variable               | Required | Purpose                                                                         |
| ---------------------- | -------- | ------------------------------------------------------------------------------- |
| `OPENROUTER_API_KEY`   | Yes      | Powers AI suggestions. Get one at https://openrouter.ai/keys.                   |
| `OPENROUTER_MODEL`     | No       | Any OpenRouter model with structured output. Default `google/gemini-3.5-flash`. |
| `DOMAINR_RAPIDAPI_KEY` | No       | Improves availability accuracy on TLDs that RDAP and WHOIS miss.                |

Pricing comes from a public, keyless endpoint, so no extra key is needed for the price estimates.

Pick a fast instruction-tuned model. Heavy reasoning models are slower, cost more, and can fail to return the structured output Vacant needs.

## Run with Docker

Pull and run the published image:

```bash
docker run -p 3000:3000 -e OPENROUTER_API_KEY=sk-... ghcr.io/martian56/vacant:latest
```

Or with Compose, using a local `.env`:

```bash
docker compose up
```

Build the image yourself:

```bash
docker build -t vacant .
docker run -p 3000:3000 -e OPENROUTER_API_KEY=sk-... vacant
```

## Development

```bash
bun run dev          # start the dev server
bun run build        # production build (standalone output)
bun run test         # run the unit tests
bun run lint         # eslint
bun run typecheck    # tsc --noEmit
bun run format       # prettier --write
bun run update-tlds  # refresh lib/tlds.json from the IANA RDAP bootstrap
```

## Stack

Bun · Next.js (App Router) · TypeScript · Tailwind CSS · Vercel AI SDK · OpenRouter.

## Contributing

Issues and pull requests are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and the
[Code of Conduct](CODE_OF_CONDUCT.md) first.

## License

[MIT](LICENSE)
