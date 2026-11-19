# AgroAI | Field Shift

**Crop-rotation decision support for small and mid-size farmers, powered by NASA Earth observations.**

Built for the **NASA Space Apps Challenge 2026**, challenge **Field Shift: Adapting Farms with NASA Data**.

**Live demo (no password):** https://demo-agroai.mateusmoreira.dev  |  **Demo video (30 s):** https://www.youtube.com/watch?v=Do6FTY6CYfc  |  **Documentation:** [`docs/`](docs/README.md)

---

## The problem

Shifting temperatures, irregular rain, water shortages and declining soil health make it hard for farmers to choose **what to plant and when**. NASA has decades of free data about every field on Earth, but it is spread across portals, in technical formats, and out of reach for most farmers.

## What AgroAI does

A mobile-first website, in English and Portuguese, for farmers in Brazil and the United States:

1. **Short questionnaire** about the farm, the crops, what the farmer knows about the soil, and the farmer's priorities.
2. **Dashboard** with the farm's climate history (NASA POWER), recent satellite readings (SMAP soil moisture, MODIS NDVI, GPM IMERG rain), terrain slope (SRTM), a soil portrait (SoilGrids + the farmer's observations) and the forecast.
3. **Rotation comparison:** the current rotation vs. the 2 best alternatives, each with *why it was suggested, evidence, benefits, risks, confidence and information gaps*.
4. **Chat assistant** that explains the comparison, the farm's climate and the crops in plain language, and cites the source and period of every number.

> AgroAI **supports, it does not decide**. Every number has a source, and the AI never computes or invents a number. The final word belongs to the farmer and the local expert.

## NASA data

| Dataset | Used for |
|---|---|
| **NASA POWER** | 1991-2020 climate normals, frost, heat, heavy rain, dry spells, evapotranspiration (FAO-56) |
| **SRTM 30 m** | Field slope for the erosion score |
| **SMAP L4** (SPL4SMGP) | Dashboard: today's surface and root-zone soil moisture vs. the same day in past years |
| **MODIS MOD13Q1** | Dashboard: NDVI (how green the field is) over the last 12 months |
| **GPM IMERG** (Late, daily) | Dashboard: rain over the last 30 days |

Also used: **SoilGrids** (soil properties) and **Open-Meteo** (7-day forecast, since NASA does not publish forecasts). SMAP, MODIS and GPM IMERG are read live from NASA Earthdata (the server needs an Earthdata token) and are shown **on the Dashboard only**: the rotation engine and the chat do not use these numbers yet. Without the token, the rain card falls back to NASA POWER.

Details in [NASA Data](docs/03-nasa-data.md). How the scores are built: [Methodology](docs/04-methodology.md).

## Run it

Requirements: Python 3.12+, [uv](https://docs.astral.sh/uv/), Node 20+, Docker.

```bash
docker run -d --name agroai-dev -p 127.0.0.1:55432:5432 \
  -e POSTGRES_USER=agricultura_app -e POSTGRES_PASSWORD=dev -e POSTGRES_DB=agricultura \
  pgvector/pgvector:pg17

cd agroai/api && uv sync
env $(grep -v '^#' .env.dev) uv run alembic upgrade head
env $(grep -v '^#' .env.dev) uv run uvicorn app.main:app --reload --port 8000

# in another terminal
cd agroai/web-demo && npm install && npm run dev   # http://localhost:5174
```

Optional key (Gemini) and tests: [Run Locally](docs/08-run-locally.md).

## Documentation

| | |
|---|---|
| [Overview](docs/01-overview.md) | Problem, users, solution, how it answers the challenge |
| [How It Works](docs/02-how-it-works.md) | Farmer's journey, architecture, stack |
| [NASA Data](docs/03-nasa-data.md) | Each dataset, version, resolution and use |
| [Methodology](docs/04-methodology.md) | Rotation comparison and where every number comes from |
| [Limitations and Roadmap](docs/05-limitations-roadmap.md) | What works, what is partial, what is next |
| [References](docs/06-references.md) | Other data, libraries, images, licenses |
| [Tools and Data Sources](TOOLS.md) | NASA data, team-prepared data and external services, with URLs |
| [Use of AI](docs/07-ai-use.md) | AI in the product, in development and in media |
| [Run Locally](docs/08-run-locally.md) | How to run the app on your computer |
| [Demo Video](docs/09-demo-video.md) | The 30-second video and its AI disclosure |
| [Submission](docs/submission/SUBMISSION.md) | The Space Apps project form, field by field |

## Tech stack

React, Vite, TypeScript, Tailwind CSS, Leaflet, Python, FastAPI, SQLAlchemy, Alembic, PostgreSQL + pgvector, Google Gemini (language only), Docker

## Use of AI

- **Code and data:** developed with AI assistance (Claude Code, Anthropic): code, tests, data scripts, documentation and the research of the crop-parameter catalog, where every value keeps its cited source. Reviewed and tested by the team.
- **Demo video:** generated with Claude Opus 5.5 (Anthropic); narrator voice by Chatterbox TTS (Resemble AI), cloned from a team member's voice with his consent; "Dona Marta" voice by Microsoft Ava neural TTS. A visible "AI-generated (SI)" watermark is on every frame. Details: [Demo Video](docs/09-demo-video.md).
- **Product:** Google Gemini reads free text and powers the chat. It never computes or invents numbers.

Full statement: [Use of AI](docs/07-ai-use.md).

## Team

**Team: NOME DO GRUPO** (yes, that is our real team name: it means "GROUP NAME" in Portuguese)

- Arthur Miranda
- Augusto Aparecido
- Guilherme Melo
- Mateus Oliveira
- Yury Turatti
- Pedro Otavio Barbosa
