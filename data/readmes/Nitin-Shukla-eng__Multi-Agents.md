# ResearchMind — Multi-Agent AI Research Pipeline

## Live URL

https://multi-agents-jwsbzmdgrtx4i3fetouffz.streamlit.app/

Use your own API keys and start exploring — no setup required beyond that.

ResearchMind is a small multi-agent system that automates the process of researching a topic end-to-end: it searches the web, scrapes the most relevant source, writes a structured report, and then critiques its own output. It's built with **LangChain**, **OpenAI (GPT-4o-mini)**, and **Tavily Search**, and ships with both a CLI runner and a **Streamlit** web UI.

## How It Works

The pipeline runs four collaborating components in sequence, each handing its output to the next:

| Step | Component | Type | Job |
|------|-----------|------|-----|
| 1 | **Search Agent** | LangChain tool-calling agent | Uses Tavily to find recent, reliable sources on the topic (titles, URLs, snippets) |
| 2 | **Reader Agent** | LangChain tool-calling agent | Picks the most relevant URL from the search results and scrapes its text content |
| 3 | **Writer Chain** | Prompt → LLM chain | Drafts a structured report (Introduction, Key Findings, Conclusion, Sources) from the combined research |
| 4 | **Critic Chain** | Prompt → LLM chain | Reviews the report and returns a score out of 10, strengths, areas to improve, and a one-line verdict |

All four share the same underlying model (`gpt-4o-mini`, temperature `0`) but are scoped to different tools/prompts.

## Project Structure

```
Multi-Agents-main/
├── agents.py         # Defines the two agents (search, reader) and two chains (writer, critic)
├── tools.py           # Custom LangChain tools: web_search (Tavily) and scrape_url (BeautifulSoup)
├── pipeline.py         # CLI entry point — runs the full 4-step pipeline for a given topic
├── app.py              # Streamlit web UI ("ResearchMind") with live pipeline status and report display
├── requirements.txt    # Python dependencies
└── .gitignore          # Excludes .env
```

## Prerequisites

- Python 3.12+ (only needed if running locally — the live app needs nothing installed)
- An [OpenAI API key](https://platform.openai.com/api-keys)
- A [Tavily API key](https://tavily.com) (free tier available)

## Installation

Only needed if you want to run the project on your own machine — the [live app](https://multi-agents-jwsbzmdgrtx4i3fetouffz.streamlit.app/) needs no installation.

```bash
git clone <repo-url>
cd Multi-Agents-main

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

## Configuration

**Using the live app (recommended):**
Open the [live demo](https://multi-agents-jwsbzmdgrtx4i3fetouffz.streamlit.app/) and paste your own OpenAI and Tavily API keys directly into the sidebar. Nothing is stored, logged, or billed to anyone but you — each run uses only the keys you enter for that session. No `.env` file is involved at all.

**Running locally instead (CLI or your own copy of the Streamlit app):**
Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

This is only needed if you're running the project yourself. It's never uploaded to GitHub — `.gitignore` already excludes it — and it has nothing to do with the live hosted app, which reads keys from the sidebar instead.

## Usage

**Option 1 — Streamlit web app**

```bash
streamlit run app.py
```

Enter a research topic, click **Run Research Pipeline**, and watch each of the four steps complete live. The final report renders as Markdown and can be downloaded as a `.md` file; raw search/scrape output is available in collapsible panels, and critic feedback is shown alongside the report.

**Option 2 — Command line**

```bash
python pipeline.py
```

You'll be prompted to enter a topic, and progress/output for each step prints to the terminal. (This uses your local `.env` file, not the sidebar.)

## Notes & Limitations

- The Reader Agent scrapes only **one** URL per run (the one it judges most relevant from the search results), and scraped content is truncated to 3,000 characters.
- Search results passed to the Reader Agent are truncated to the first 800 characters.
- `scrape_url` uses a simple `requests` + `BeautifulSoup` fetch — it won't render JavaScript-heavy pages and may fail on sites that block generic user agents.
- No retry/error handling is wired up yet for failed searches or scrapes beyond the try/except in `scrape_url`.

## Possible Improvements

- Let the Reader Agent scrape multiple sources instead of one.
- Feed critic feedback back into the Writer Chain for an automatic revision loop.
- Add caching so repeated topics don't re-hit the search/scrape APIs.
- Swap in a larger model for the Writer/Critic chains for longer, more nuanced reports.
