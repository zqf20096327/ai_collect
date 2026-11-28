Fan-made project. Not affiliated with or endorsed by Marvel or Disney. All characters and related names are trademarks of their respective owners.

<p align="center">
  <img src="frontend/public/logo.svg" width="96" height="96" alt="Ask the Multiverse logo" />
</p>

<h1 align="center">Ask the Multiverse</h1>

<p align="center">
  <b>Ask anything about the multiverse. Every answer cites its sources.</b><br />
  <a href="https://multiverse.arunangshupramanik.com">Live site</a> ·
  <a href="https://multiverse.arunangshupramanik.com/coverage">Coverage</a> ·
  <a href="https://multiverse.arunangshupramanik.com/credits">Credits</a> ·
  <a href="https://multiverse.arunangshupramanik.com/multiverse/api/v1/docs">API docs</a> ·
  <a href="docs/deploy-gcp.md">Deployment guide</a>
</p>

<p align="center">
  <a href="https://multiverse.arunangshupramanik.com"><img src="https://img.shields.io/website?url=https%3A%2F%2Fmultiverse.arunangshupramanik.com%2Fmultiverse%2Fapi%2Fv1%2Fhealth&label=live" alt="Live site status" /></a>
  <a href="https://github.com/arunangshu01/ask-the-multiverse/actions/workflows/ci.yml"><img src="https://github.com/arunangshu01/ask-the-multiverse/actions/workflows/ci.yml/badge.svg?branch=main" alt="CI" /></a>
  <a href="https://github.com/arunangshu01/ask-the-multiverse/actions/workflows/deploy.yml"><img src="https://github.com/arunangshu01/ask-the-multiverse/actions/workflows/deploy.yml/badge.svg" alt="Deploy" /></a>
  <a href="https://github.com/arunangshu01/ask-the-multiverse/actions/workflows/sync.yml"><img src="https://github.com/arunangshu01/ask-the-multiverse/actions/workflows/sync.yml/badge.svg" alt="Data sync" /></a>
  <img src="https://img.shields.io/badge/code-MIT-blue" alt="Code: MIT" />
  <img src="https://img.shields.io/badge/data-CC%20BY--SA%203.0-lightgrey" alt="Data: CC BY-SA 3.0" />
</p>

A cinematic, cited explorer of every documented reality, dimension and realm in the Marvel multiverse,
and a Q&A bot over a knowledge graph built from the [Marvel Database](https://marvel.fandom.com/) and the
[MCU Wiki](https://marvelcinematicuniverse.fandom.com/) on Fandom (CC BY-SA) and [Wikidata](https://www.wikidata.org/) (CC0).
Ask "Who has fought both Thanos and Galactus?" and an LLM turns the question into a typed graph query or a checked,
read-only DuckDB SELECT. The answer is built only from the returned rows, shows the query it ran, and links to the
exact wiki pages (and revisions) it used. If the data can't answer, it says so.

Live at **[multiverse.arunangshupramanik.com](https://multiverse.arunangshupramanik.com)** (also served at
[ask-the-multiverse.web.app](https://ask-the-multiverse.web.app), the Firebase default domain). The data refreshes
weekly; the footer of every page shows when it was last synced.

## Try these

- Who has fought both Thanos and Galactus?
- What is the origin of Spider-Man?
- Are Thor and Loki enemies?
- When did Spider-Man first fight Venom?
- Who has Wolverine fought in animation?
- Who killed Gwen Stacy?
- Which X-Men have also been Avengers?
- Show every variant of Wolverine
- Who appears in Avengers: Endgame?
- How many film realities are there?

## What's in it

| | Count | Source |
| --- | --- | --- |
| Realities, dimensions and realms | 5,531 | Marvel Database listings and category trees, classified by infobox template |
| Characters (with origin, birthplace, powers, deaths) | 106,838 | Character pages |
| Teams and organisations | 12,142 | Team and organisation pages |
| Events | 387 | Event pages |
| Stories (comics, episodes, films, games, novels) | 77,880 | Story pages |
| Story appearances with roles | 985,849 | Each story's Featured / Supporting / Antagonists lists |
| Sourced relationships | 169,249 | Family, membership, team allies and enemies, event sides, "killed by" |
| Variant groups | 8,030 | The wiki's own disambiguation pages (never guessed by name) |
| MCU timeline | 6 phases, 71 titles, all linked | MCU Wiki phase pages, linked through each film page's own MCU field |

Counts are from the latest weekly sync; the [Coverage](https://multiverse.arunangshupramanik.com/coverage) page lists
every rejected, unclassified or unlinked page with its reason.

**"Fought"** means two characters appear on opposite sides of the same story (one listed as an antagonist, the
other as featured or supporting) or of an event. Mentions, flashback images and visions don't count, and every
answer cites the stories.

## How it works

```
Marvel Database API + MCU Wiki API + Wikidata (1 request/s, cached, resumable)
  -> parse infoboxes and appearance lists -> quality checks -> DuckDB snapshot
  -> GCS bucket (published only if every check passes; weekly GitHub Actions sync)

Browser -> Firebase Hosting (React) --/multiverse/api/**--> Cloud Run (FastAPI, scale to zero)
             question -> resolve names -> plan (Groq gpt-oss-120b, Gemini fallback, rule planner)
             -> typed tool or guarded SQL (single SELECT, whitelisted tables, 200 rows, 3 s)
             -> answer from the rows only -> citations + graph highlight
```

- **Evaluation:** 80 questions with expected plans and answer facts, scored against the real data:
  100% plan / 100% answer with the rule planner and with the LLM planner (`python -m eval.run [--llm]`).
- **Frontend:** React 18 + Vite, no UI or graph libraries; the connections graph is plain SVG with its own force
  layout, and all artwork (including the opening sequence) is generated in code.
- **Deployment:** Firebase Hosting + Cloud Run in `asia-south1`, keyless Workload Identity Federation, deploys only
  after green CI on `main` and a manual approval. See [docs/deploy-gcp.md](docs/deploy-gcp.md).

## Run locally

```bash
# backend (Python 3.12)
cd backend
python3.12 -m venv .venv && .venv/bin/pip install -r requirements-dev.txt
.venv/bin/python -m ingest realities --run-id local          # ~15-20 min at 1 request/s; resumable
.venv/bin/python -m ingest graph-fetch --run-id graph         # ~1.5 h; resumable
.venv/bin/python -m ingest graph --run-id graph --realities-run local   # also fetches the MCU Wiki phase pages
.venv/bin/python -m eval.run                                  # evaluation set (add --llm to score the LLM planner)
.venv/bin/uvicorn app.main:app --port 8000                    # optional: GROQ_API_KEY / GEMINI_API_KEY in backend/.env
.venv/bin/python -m pytest -q                                 # tests

# frontend
cd frontend && npm ci && npm run dev                          # http://localhost:5173
npm test && npm run build

# after a deploy
python3 scripts/smoke.py https://multiverse.arunangshupramanik.com
```

Without LLM keys the Console answers with its rule planner. `prototype/` holds the approved single-file UI preview
and the early data scripts.

## Data and licences

- Code: MIT ([LICENSE](LICENSE)).
- Data: derived from the Marvel Database and MCU Wiki and shared under CC BY-SA 3.0; see [DATA_LICENSE.md](DATA_LICENSE.md).
  Descriptions may be shortened; each record links to the full page and the revision used.
- No Marvel logos, film stills, official artwork or wiki images are used; all artwork is generated.
- Non-commercial: no ads, no paid tiers.

Built by [Arunangshu Pramanik](https://arunangshupramanik.com).
