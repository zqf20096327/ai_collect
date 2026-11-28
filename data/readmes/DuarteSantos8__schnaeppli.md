<picture>
  <source media="(prefers-color-scheme: dark)" srcset="brand/banner-dark.png">
  <img src="brand/banner.png" alt="Schnäppli: tell it what you want, it finds the Schnäppli">
</picture>

<p align="center">
  <strong>A self-hosted AI shopping agent.</strong><br>
  Tell it what you want to buy. It watches marketplaces, scores every listing against the market, and tells you when something is actually worth it.
</p>

<p align="center">
  <a href="LICENSE"><img alt="License: AGPL-3.0" src="https://img.shields.io/badge/license-AGPL--3.0-1d5fbf"></a>
  <img alt="Python 3.12" src="https://img.shields.io/badge/python-3.12-141414">
  <img alt="Status: early" src="https://img.shields.io/badge/status-early%20(v0.1)-8f8c86">
</p>

<p align="center">
  <img src="docs/screenshots/desktop-deal.png" alt="A listing in Schnäppli with its Deal Score, the price compared with the market range, and the reasons for the score" width="900">
</p>

---

## The name

**Schnäppli** (say it **SHNAP-lee**, [ˈʃnæp.li]: *sch* as in *shop*, the *ä* like the *a* in *cat*, a short *pp*, then *lee*) is Swiss German for a real bargain. Not something cheap: something good that costs less than it should. Spotting those is the whole point of this app.

The logo is the *ä*, winking: the face you make when you find one.

Where an *ä* isn't allowed (the repository, Docker images, environment variables), it's written `schnaeppli`.

## What it does

You write what you're after the way you'd tell a friend:

> “A digital camera under CHF 300. I like vintage Sony Cyber-shots, but an Alpha 6400 or something comparable would also work.”

Schnäppli turns that into a structured search (products, sensible alternatives with a reason for each, exclusions, budget, search terms), asks a question if something important is missing, and shows you what it understood. Nothing is saved until you confirm.

From then on it runs on your schedule:

1. **Collects** new listings from the sources you enabled.
2. **Filters** obvious misses for free (excluded words, "wanted" ads, far over budget).
3. **Analyses** the rest with your AI provider: what the item really is, its condition, what's included, red flags, and an estimated market range. Promising listings get a photo check.
4. **Scores** each one from 0 to 100 in plain code, so a listing can't talk its way into a high score, and every point is explained.
5. **Notifies** you on Telegram for exceptional deals and price drops, and sends a short digest at the times you choose.

<table>
  <tr>
    <td width="33%"><img src="docs/screenshots/phone-deals.png" alt="Deal feed on an iPhone"></td>
    <td width="33%"><img src="docs/screenshots/phone-deal.png" alt="A listing on an iPhone with its score and price ruler"></td>
    <td width="33%"><img src="docs/screenshots/phone-new-search.png" alt="Describing a new search on an iPhone"></td>
  </tr>
</table>

## Features

- **Natural-language searches** with a review step: every field the AI filled in is editable.
- **Flexible matching**: if you allow alternatives, Schnäppli considers comparable products across brands and explains why each fits.
- **Deal Score** with an itemised breakdown, market value source and confidence, and a clear line between what the seller states and what the AI assumes.
- **Effective price**: price + shipping, estimated where unknown (and labelled as such). Pickup distances are computed on your server from your postal code.
- **Photo checks** with a vision model, phrased as *possible* issues, never confirmed defects.
- **Multiple independent searches**, each with its own schedule, sources, alerts and history. Pause, resume, duplicate, archive.
- **Wishlist with accessories** that inherit compatibility (a lens knows the camera's mount) and turn into searches in one tap.
- **Budget**: a monthly budget with bought, planned and interested amounts. A found listing never counts as spent.
- **AI cost tracking and limits**: tokens per call as reported by the provider, estimated cost per task, model, search and day; daily and monthly limits that are checked *before* every call; automatic pause.
- **Bring your own key**: Anthropic, OpenAI or Google Gemini, per user, encrypted at rest. Admins can add a shared key, or use **their own Claude plan through Claude Code** on the server ([how](docs/claude-code.md)).
- **Shopping assistant chat** that can see your searches, budget and found listings (and nothing else).
- **Learning from feedback**, transparent and resettable.
- **Installable PWA**, designed for the iPhone first and comfortable on a desktop.

## Marketplaces: what works and what doesn't

Schnäppli only uses official APIs and permitted access. It doesn't scrape sites that forbid it, and it doesn't work around bot protection. The app shows each source's real status.

| Source | Status | Notes |
| --- | --- | --- |
| eBay | ✅ Supported | Official Browse API. Needs a free eBay developer key. Asking prices, not sold prices. |
| Any shop, by link | ✅ Supported | Paste a link; Schnäppli reads it once if robots.txt allows and the shop publishes product data. |
| Galaxus, Digitec | ✅ Supported | Galaxus' official interface for AI assistants. New products and current prices; also the new-price reference for used listings. |
| Ricardo, tutti.ch | ✅ Via alert e-mails | No search API and they block bots, so Schnäppli reads their own saved-search mails: connect your mailbox in Setup (read-only, only their mails). |
| Facebook Marketplace | ✅ Via alert e-mails | No API and scraping is prohibited, so Schnäppli reads your saved-search notification mails. |
| Toppreise | ✅ Via price alerts | API needs permission; Schnäppli reads Toppreise's price-alert mails for products you watch. |
| Your own shops | ✅ You add them | Any shop whose search allows programs and publishes product data (schema.org or WooCommerce). Tested when you add it. |
| Interdiscount | ❌ No search | No public product API. Single products can be added by link. |
| Amazon | 🕓 Planned | The product API needs an Associates account with sales. |

Details in [docs/marketplaces.md](docs/marketplaces.md).

## Quick start

Requirements: Docker with Compose v2, a reverse proxy with TLS for your private network, and an AI provider API key.

```bash
git clone https://github.com/<you>/schnaeppli.git && cd schnaeppli
cp .env.example .env            # set POSTGRES_PASSWORD, SCHNAEPPLI_PUBLIC_URL, SCHNAEPPLI_SETUP_TOKEN
mkdir -p secrets && chmod 700 secrets
echo "k1:$(openssl rand -base64 32)" > secrets/encryption_keys
touch secrets/telegram_bot_token secrets/ebay_client_id secrets/ebay_client_secret secrets/claude_code_bridge_secret secrets/inbox_password
docker compose up -d --build
```

Open the URL, create the admin account with your setup token, then add your AI key under **Settings → AI**. Full guide: [docs/installation.md](docs/installation.md).

> **Keep it private.** Schnäppli is built to run on your own network or behind a VPN. Don't expose it to the internet. See [docs/security.md](docs/security.md).

## Documentation

- [Installation](docs/installation.md) · [Configuration reference](docs/configuration.md)
- [Architecture](docs/architecture.md) · [Security & privacy](docs/security.md)
- [AI providers & costs](docs/ai-providers.md) · [Claude Code with your plan](docs/claude-code.md) · [Telegram](docs/telegram.md) · [Marketplaces](docs/marketplaces.md)
- [Roadmap](ROADMAP.md) · [Changelog](CHANGELOG.md) · [Contributing](CONTRIBUTING.md)

## Stack

FastAPI · SQLAlchemy 2 (async) · PostgreSQL 16 · Redis · arq worker · React 19 · Vite · Tailwind CSS 4 · official Anthropic, OpenAI and Google GenAI SDKs. One modular backend with a separate background worker, no microservices.

## License

[AGPL-3.0-or-later](LICENSE). Everything is open, with no hidden "pro" edition. If you run a modified version as a service for others, the AGPL asks you to share your changes.

Screenshots use invented demo data and openly licensed photos ([credits](docs/screenshots/CREDITS.md)).
