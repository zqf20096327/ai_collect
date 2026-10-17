# AI x Medicine Research Agent

An autonomous research agent that finds, ranks, and emails the latest papers on **AI in neuroradiology**, so researchers and clinicians can follow a fast-moving field without manually searching four databases every week.

<p align="center">
  <img src="docs/digest_example.png" alt="Example digest email" width="380">
</p>

## What it does

Each run, the agent:

1. **Plans search queries** from a research profile, expanding them with domain synonyms
2. **Searches four sources**: PubMed, Europe PMC, OpenAlex, and arXiv
3. **Deduplicates** papers found in multiple databases and merges their metadata
4. **Filters** out candidates with missing or too-short abstracts
5. **Ranks semantically** against the research profile using sentence embeddings
6. **Evaluates** the top candidates with a large language model for relevance and quality
7. **Scores** each paper and applies a quality gate
8. **Resolves legal full-text access**, distinguishing open-access papers from paywalled ones
9. **Downloads open-access PDFs** and emails a ranked HTML digest with the PDFs attached

A typical run narrows roughly 90 raw candidates down to the 10 most relevant papers.

## Tech stack

| Component | Tool |
|---|---|
| Language | Python 3.11 |
| Literature sources | PubMed (NCBI E-utilities), Europe PMC, OpenAlex, arXiv |
| Semantic ranking | `sentence-transformers/all-MiniLM-L6-v2` |
| LLM evaluation | `openai/gpt-oss-120b` via the Groq API (free tier) |
| Delivery | Gmail SMTP with an App Password |

## Design choices

- **Legal full text only.** The agent attaches PDFs only for open-access papers. Paywalled papers are listed with a link, never downloaded.
- **Cheap before expensive.** Fast embedding similarity narrows the pool before any LLM call, which keeps runs within free-tier rate limits.
- **Nothing silently dropped.** If a PDF cannot be attached (for example, because of Gmail's 25 MB limit), the digest explains why and gives a direct link.
- **Resilient delivery.** Email sending retries and falls back from port 465 to 587, and logs the full error on failure. If delivery still fails, the digest is saved locally.

## Project structure

├── main.py              # Entry point: runs the full 9-step pipeline
├── config.py            # Research profile and pipeline settings
├── query_planner.py     # Query generation and synonym expansion
├── models.py            # Paper data model
├── sources/             # Clients for PubMed, Europe PMC, OpenAlex, arXiv
├── retrieval/           # Deduplication, filtering, semantic ranking
├── evaluation/          # LLM-based relevance and quality scoring
├── fulltext/            # Open-access resolution and PDF download
├── mailer/              # Digest rendering and Gmail delivery
├── utils/               # Logging and shared helpers
├── tests/               # Tests
└── legacy_v1/           # Original single-source (arXiv-only) version
```

## Setup

**1. Clone and install**

```bash
git clone https://github.com/USERNAME/ai-medicine-research-agent.git
cd ai-medicine-research-agent
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux
pip install -r requirements.txt
```

**2. Get credentials (all free)**

- A **Groq API key** from [console.groq.com](https://console.groq.com)
- A **Gmail App Password**: enable 2-Step Verification on your Google account, then create one under Security → App passwords

**3. Configure**

Copy `.env.example` to `.env` and fill in your own values. Never commit `.env`.

At minimum you need `GROQ_API_KEY`, `GMAIL_ADDRESS`, `GMAIL_APP_PASSWORD`, and `RECIPIENT_EMAIL`. The agent detects values left over from `.env.example` and warns you before starting a long run.

**4. Run**

```bash
python main.py
```

To test the full pipeline without sending an email, use a dry run:

```bash
python main.py --dry-run
```

## Adapting it to your field

Although this instance tracks neuroradiology, the pipeline is field-agnostic. Everything is configured in one place, with this priority: **command-line arguments → environment variables (`.env`) → defaults** (defined in `config.py`).

### Research profile

These settings in `.env` drive query planning, semantic ranking, and the LLM's personal-fit judgement. List values are comma-separated.

| Variable | Purpose | Example |
|---|---|---|
| `RESEARCH_FIELD` | The field the digest is about | `Neuroradiology AI` |
| `KEYWORDS` | Core search terms | `neuroimaging, brain MRI, deep learning` |
| `PRIMARY_INTERESTS` | Topics you care about most | `Medical imaging, Deep learning` |
| `SECONDARY_INTERESTS` | Topics that add value but are not essential | `Explainable AI, Vision Transformers` |
| `CURRENT_RESEARCH` | Your ongoing projects, used to judge personal fit | `Brain tumor segmentation` |

For example, to track AI in cardiology instead:

```dotenv
RESEARCH_FIELD=Cardiology AI
KEYWORDS=echocardiography, ECG, deep learning
PRIMARY_INTERESTS=Cardiac imaging, Arrhythmia detection
```

### One-off overrides from the command line

Any run can override the profile without editing `.env`:

```bash
python main.py --field "Pathology AI" --keywords "whole slide imaging, histopathology" --papers 5
```

### Pipeline tuning

| Variable | Default | Effect |
|---|---|---|
| `PAPERS_PER_DIGEST` | 10 | Papers in the final digest |
| `SEMANTIC_TOP_K` | 30 | Candidates sent to the LLM (one API call each; keep near 30 on Groq's free tier) |
| `MIN_FINAL_SCORE` | 55 | Quality gate on a 0-100 scale |
| `MIN_YEAR` | none | Ignore papers published before this year |
| `ENABLED_SOURCES` | all four | Any of `pubmed, europe_pmc, openalex, arxiv` |

### Scoring weights

Each paper's final score is a weighted combination of six criteria. Weights are normalized automatically, so they only need to be meaningful relative to each other.

| Criterion | Variable | Default |
|---|---|---|
| Relevance to the field | `RELEVANCE_WEIGHT` | 0.30 |
| Fit with your personal interests | `PERSONAL_FIT_WEIGHT` | 0.20 |
| Clinical impact | `CLINICAL_WEIGHT` | 0.15 |
| Methodological quality | `METHOD_WEIGHT` | 0.15 |
| Novelty | `NOVELTY_WEIGHT` | 0.10 |
| Recency | `RECENCY_WEIGHT` | 0.10 |

A clinician might raise `CLINICAL_WEIGHT`; a methods researcher might raise `METHOD_WEIGHT`.

## Roadmap

- Scheduled weekly runs with GitHub Actions
- Persistent memory so papers are never sent twice across runs
- Additional sources (medRxiv, bioRxiv)
- Feedback buttons in the digest to refine future rankings

## Author

## Authors

| Amirali Kordi | Arefeh Ostadtaghizadeh |
|:---:|:---:|
| Medical Student, Tehran University of Medical Sciences | Medical Student, Tehran University of Medical Sciences |
| AI & ML · Medical Imaging | ML & DL in Imaging Data |
| [LinkedIn](https://linkedin.com/in/amirali-kordi-4551bb316) | [LinkedIn](https://linkedin.com/in/arefeh-ostadtaghizadeh-746685224) |

## License

MIT
