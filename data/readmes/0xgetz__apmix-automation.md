<div align="center">

<img src="assets/logo.png" width="150" alt="apmix-automation logo">

# apmix-automation

**End-to-end apmix.ai account + API key automation.**
Fresh temp inbox → magic-link signup → automatic Cloudflare Turnstile → auto-generated API key.

<br>

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Node.js](https://img.shields.io/badge/Node.js-18%2B-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)](https://nodejs.org/)
[![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)](https://playwright.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-6b7280?style=for-the-badge&logo=linux&logoColor=white)](#requirements)

[![Stars](https://img.shields.io/github/stars/0xgetz/apmix-automation?style=flat-square&color=7C5CFF)](https://github.com/0xgetz/apmix-automation/stargazers)
[![Forks](https://img.shields.io/github/forks/0xgetz/apmix-automation?style=flat-square&color=00E0C6)](https://github.com/0xgetz/apmix-automation/network)
[![Issues](https://img.shields.io/github/issues/0xgetz/apmix-automation?style=flat-square&color=5B8CFF)](https://github.com/0xgetz/apmix-automation/issues)
[![Last commit](https://img.shields.io/github/last-commit/0xgetz/apmix-automation?style=flat-square&color=7C5CFF)](https://github.com/0xgetz/apmix-automation/commits)
[![Repo size](https://img.shields.io/github/repo-size/0xgetz/apmix-automation?style=flat-square&color=00E0C6)](https://github.com/0xgetz/apmix-automation)

<br>

<img src="assets/banner.png" width="820" alt="apmix-automation banner">

<br>

[English](README.md) · [Español](docs/README.es.md) · [Français](docs/README.fr.md) · [Deutsch](docs/README.de.md) · [Bahasa Indonesia](docs/README.id.md)

</div>

---

## What it does

`apmix-automation` drives the **entire** apmix.ai onboarding flow in a real
browser and hands you a ready-to-use API key:

| # | Step | Detail |
|---|------|--------|
| 1 | **Temp inbox** | Generates a disposable address on [zenvex.dev](https://zenvex.dev) with a random prefix. |
| 2 | **Signup** | Opens `apmix.ai/login`, accepts the terms, fills the email. |
| 3 | **Captcha** | Waits for the **Cloudflare Turnstile** to self-solve (optional 2captcha fallback). |
| 4 | **Magic link** | Submits *Send magic link*; if apmix rejects the domain as disposable, it tries the next Zenvex domain. |
| 5 | **Sign-in** | Reads the email, follows the link, lands on the dashboard. |
| 6 | **API key** | Creates a key with a **random name** and captures the `apx_live_…` value. |
| 7 | **Output** | Writes `accounts.json`, `accounts.csv`, `accounts.html`. |

Random **first/last names** are generated and stored per account.

> Verified end-to-end: a fresh account was created and produced a working
> `apx_live_…` key during development.

---

## Requirements

- **Linux / macOS / Windows**
- **Python 3.9+** *or* **Node.js 18+**
- A **clean / residential IP** — Cloudflare Turnstile blocks most datacenter IPs
- ~200 MB free disk for the Chromium build

---

## Install

### Python

```bash
pip install playwright requests
python3 -m playwright install --with-deps chromium
```

### Node.js

```bash
npm i playwright
npx playwright install --with-deps chromium
```

---

## Usage

```bash
# Python — recommended on a VPS (headful under Xvfb passes Cloudflare best)
xvfb-run -a python3 scripts/apmix_bulk.py --count 1

# Node.js
xvfb-run -a node scripts/apmix_bulk.js --count 1

# Batch
xvfb-run -a python3 scripts/apmix_bulk.py --count 10 --workers 2 --out my_accounts

# Headless
python3 scripts/apmix_bulk.py --count 3 --headless

# Optional captcha fallback
TWOCAPTCHA_KEY=xxxx xvfb-run -a python3 scripts/apmix_bulk.py --count 3
```

### Options

| Flag | Description | Default |
|------|-------------|---------|
| `--count` | Number of accounts to create | `1` |
| `--workers` | Parallel browsers | `1` |
| `--out` | Output directory | `apmix_accounts` |
| `--headless` | Run without a window | off |
| `--proxy` | Single proxy `host:port` | none |
| `--proxy-file` | File of proxies, one `host:port` per line | none |
| `--fetch-proxies` | Download + test free proxies → `working_proxies.txt`, then exit | off |

---

## Output

`accounts.json`

```json
[
  {
    "email": "ab12cd34@znvx.me",
    "first_name": "Morgan",
    "last_name": "Hayes",
    "api_key": "apx_live_xxxxxxxxxxxxxxxx",
    "key_name": "vps-k3f9a",
    "created_at": "2026-09-28T18:00:00+00:00",
    "status": "ok",
    "error": ""
  }
]
```

Also written: `accounts.csv` and a copy/paste-friendly `accounts.html` table.

---

## Proxies

The scripts support HTTP(S) proxies with **automatic failover** across a pool.
A single bad proxy no longer kills the run.

### Free proxies are tested and do **not** work

`--fetch-proxies` scans ~35,000 public proxies; only **2–5** can even reach the
target sites. An end-to-end run through them produced **0/1 accounts**:

1. Most free proxies cannot tunnel HTTPS → `ERR_TUNNEL_CONNECTION_FAILED`.
2. The survivors are datacenter IPs → Cloudflare Turnstile fails on **both**
   Zenvex and apmix.

**Use a residential / ISP proxy** with `--proxy-file` for scale, or run from a
normal IP with no proxy (works — verified).

---

## Important notes

- **apmix blocks disposable domains.** Gmail, mail.tm and several temp providers
  are refused with *“Temporary inboxes are not accepted.”* The script loops
  through Zenvex's receiving domains until one passes.
- **Zenvex has its own anti-bot check.** From a datacenter IP you see
  *“Verification failed.”* Run headful under `xvfb-run` on a clean IP.
- **One key per free account**, shown **only once** — keep `accounts.json`.
- **Terms of service.** Creating many accounts programmatically may breach
  apmix's terms. Use responsibly and only for accounts you may create.

See **[docs/GUIDE.md](docs/GUIDE.md)** for full troubleshooting and internals.

---

## Project layout

```
apmix-automation/
├── assets/            # logo + banner (SVG/PNG)
├── docs/              # GUIDE.md + 5 README translations
├── scripts/
│   ├── apmix_bulk.py  # Python implementation
│   └── apmix_bulk.js  # Node.js implementation
├── LICENSE
└── README.md
```

---

## Contributing

Issues and pull requests are welcome. Keep changes focused, match the existing
code style, and test against a real run before opening a PR.

## License

Released under the **MIT License** — see [LICENSE](LICENSE).

<div align="center"><sub>Not affiliated with apmix.ai or zenvex.dev. For educational and automation purposes.</sub></div>
