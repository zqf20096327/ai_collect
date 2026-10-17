# Market Pilot

Market Pilot is an evidence-grounded market research prototype that turns public market signals into traceable research workflows.

[Live product](https://marketpilot.worldon.ai/) · [中文说明](README.zh-CN.md)

## Why it exists

AI can summarize large amounts of market conversation quickly, but a polished summary is not the same as inspectable evidence. Market Pilot explores a stricter workflow: preserve source-grounded signals, separate direct evidence from inference, mask personal identifiers, and make uncertainty visible in the final report.

## Current capabilities

- Build research panels from collected public signals.
- Generate de-identified persona cards for analysis.
- Route and answer research questions through evidence-aware prompts.
- Summarize consensus, disagreement, limitations, and supporting signals.
- Switch the complete public and authenticated experience between English and Simplified Chinese.
- Read cached report localizations without collecting data or rerunning research.
- Provide a React product interface backed by a FastAPI service.

This repository is a product prototype. Demo data must be labeled as sanitized, and data connectors or model-backed runs require your own authorized provider credentials.

## Architecture

- Frontend: React 18, Vite 6, Tailwind CSS 4
- Backend: FastAPI
- Local routing: the frontend calls `/api`; Vite proxies requests to `http://localhost:8001`
- Research pipeline: collection, masking, panel construction, evidence-aware answering, aggregation, and report rendering
- Localization: unprefixed English public URLs, `/zh` Chinese public URLs, account-aware locale resolution, and a validated report-localization cache

See [docs/architecture.md](docs/architecture.md) for the component map.

## Local setup

Requirements: Node.js 24+, npm 11+, Python 3.13+, and Git.

```powershell
git clone https://github.com/Dgeloe4-yb/market-pilot.git
Set-Location market-pilot
npm.cmd ci
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r collector\requirements.txt
```

Review `.env.example`, then export only the variables you need into the process environment. The application does not auto-load `.env` files.

Start the API:

```powershell
Set-Location collector
..\.venv\Scripts\python.exe -m uvicorn api.app:app --port 8001
```

Start the frontend from the repository root in another terminal:

```powershell
npm.cmd run dev
```

The frontend runs on `http://localhost:5173`. Some research workflows remain unavailable until you provide your own authorized API credentials through the process environment.

## Tests

```powershell
npm.cmd run build
Get-ChildItem collector\test_*.py | ForEach-Object {
  Push-Location collector
  try { ..\.venv\Scripts\python.exe $_.Name } finally { Pop-Location }
  if ($LASTEXITCODE -ne 0) { throw "Failed: $($_.Name)" }
}
```

## Data and privacy

Do not commit credentials, raw scraped data, user images, local databases, or production run outputs. Use only data you are authorized to collect and process. Public examples must be synthetic or explicitly sanitized.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Security reports should follow [SECURITY.md](SECURITY.md).

## License

Apache-2.0. See [LICENSE](LICENSE).
