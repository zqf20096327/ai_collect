# AI Exposure of the US Job Market

[![Live Demo](https://img.shields.io/badge/Live_Demo-arosstale.github.io/jobs-blue?style=for-the-badge)](https://arosstale.github.io/jobs/)
[![Stars](https://img.shields.io/github/stars/arosstale/jobs?style=for-the-badge)](https://github.com/arosstale/jobs/stargazers)
[![Forks](https://img.shields.io/github/forks/arosstale/jobs?style=for-the-badge)](https://github.com/arosstale/jobs/forks)

> **How susceptible is every occupation in the US economy to AI and automation?**

Interactive treemap analyzing **342 occupations** from the Bureau of Labor Statistics. Area = employment. Color = AI exposure. Hover for details.

**[Launch the visualization →](https://arosstale.github.io/jobs/)**

![AI Exposure Treemap](jobs.png)

## Key Findings

- **Average AI exposure:** 5.3/10 across all 342 occupations
- **Highest risk:** Software developers, data analysts, translators, paralegals (8-9/10)
- **Lowest risk:** Roofers, landscapers, construction laborers (0-1/10)
- **The signal:** If the job can be done entirely from a home office on a computer, AI exposure is inherently high

## How It Works

```
Scrape BLS → Parse to Markdown → Score with LLM → Build treemap
```

1. **Scrape** — Playwright downloads all 342 occupation pages from BLS
2. **Parse** — BeautifulSoup converts HTML to clean Markdown
3. **Score** — Gemini Flash scores each occupation's AI exposure (0-10) with rationale
4. **Visualize** — D3 treemap where area = jobs and color = exposure

## Run It Yourself

```bash
uv sync && uv run playwright install chromium
echo "OPENROUTER_API_KEY=your_key" > .env

uv run python scrape.py          # download BLS pages
uv run python process.py         # HTML to Markdown
uv run python make_csv.py        # extract structured data
uv run python score.py           # LLM scoring
uv run python build_site_data.py # build site data
cd site && python -m http.server  # view at localhost:8000
```

## Want a generalized version?

Check out **[universal-analyzer](https://github.com/arosstale/universal-analyzer)** — same engine, works with any dataset.

## Data

| File | What |
|------|------|
| `occupations.csv` | 342 occupations with pay, education, job count, growth |
| `scores.json` | AI exposure scores (0-10) with LLM rationales |
| `site/data.json` | Merged data for the treemap visualization |

## License

MIT
