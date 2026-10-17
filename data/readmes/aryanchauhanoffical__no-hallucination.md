# no-hallucination

Three measured experiments on reducing hallucination in document Q&A (RAG), including the first public evaluation
of TypeSafe's **Jev** model inside a retrieval pipeline and a head-to-head against IBM Research's **STAIR**
(structure-aware retrieval).

Every number here comes from a run in this repo. All raw API responses are included, so any result can be replayed
without spending a cent.

## TL;DR

| What was tested | Result |
|---|---|
| Forcing answers to quote their source, and string-checking the quote | **The hallucination defence that worked.** 5.3% on SQuAD 2.0; refused 50/50 unanswerable questions on textbooks |
| Jev as a guard that blocks unsupported answers | **No effect.** It agreed with all 8 remaining errors (confidence 0.82–1.0) |
| Jev / STAIR / table-of-contents routing as retrievers | **Lost to ordinary hybrid search** (39.2% and 36.5% vs 73.2% Recall@1) |
| Combining STAIR + ToC routing + hybrid search | **Retrieved better (92% vs 90%), answered worse (72.5% vs 78%)** |
| Jev as triage deciding when to retry a refusal | **The one clear win: 78.0% → 81.0% correct**, refusals 17.5% → 13.5% |

The single most useful finding: **Recall@k is the wrong thing to optimise.** What sits *next to* the right chunk
decides whether an answer comes out at all.

## The experiments

| # | Question | Data | Report |
|---|---|---|---|
| 01 | Does Jev reduce hallucination in RAG? | SQuAD 2.0, 150 questions (50 unanswerable) | [experiments/01-squad2-jev-hallucination](experiments/01-squad2-jev-hallucination/REPORT.md) |
| 02 | Does combining IBM's STAIR with search and Jev help? | SearchTome, 6 textbooks, 518 retrieval + 200 answer questions | [experiments/02-searchtome-stair-jev](experiments/02-searchtome-stair-jev/REPORT.md) |
| 03 | Can the resulting over-refusal be fixed? | same 200 questions | [experiments/03-over-refusal](experiments/03-over-refusal/REPORT.md) |

### Experiment 01 — Jev vs. a structured RAG baseline (SQuAD 2.0)

| Setup | Correct | Hallucinated | Wrongly refused | Right section |
|---|---|---|---|---|
| baseline (BM25 + embeddings → cross-encoder → quote-forced answer) | 87.3% | 5.3% | 7.3% | 96% |
| + Jev "is the answer here?" gate (0.7) | 85.3% | 5.3% | 9.3% | 96% |
| + Jev citation check (≥0.8) | 86.7% | 5.3% | 8.0% | 96% |
| + Jev pairwise re-ranking (per TypeSafe's cookbook) | **90.0%** | 6.0% | 4.0% | **98%** |
| Jev table-of-contents routing (the original idea) | 72.7% | 3.3% | 24.0% | 69% |

### Experiment 02 — structure + search + Jev (SearchTome textbooks)

Retrieval, 518 questions: hybrid search **73.2% R@1 / 88.8% R@3**; combined + cross-encoder 73.4 / 88.6;
combined + Jev 71.2 / 87.6; zero-shot Jev ToC routing 39.2 / 57.7; fine-tuned STAIR 36.5.

Answers, 150 answerable + 50 unanswerable: hybrid **78.0% correct / 4.5% hallucinated**; the combination
72.5% / 6.5% — despite retrieving the gold section *more* often.

### Experiment 03 — fixing over-refusal

| Strategy | Correct | Hallucinated | Wrongly refused |
|---|---|---|---|
| base | 78.0% | 4.5% | 17.5% |
| looser prompt | 77.5% | 7.5% | 15.0% |
| always retry with more context | 79.5% | 6.5% | 14.0% |
| **retry only when Jev says the answer is there** | **81.0%** | 5.5% | **13.5%** |

Why it works — Jev's probabilities separate the two kinds of refusal cleanly:

| | refusals | Jev said "the answer is there" | median probability |
|---|---|---|---|
| should have answered | 35 | 24 | 0.74 |
| genuinely unanswerable | 50 | 1 | 0.02 |

## Reproduce

```sh
uv venv -p 3.11 .venv
uv pip install -p .venv/bin/python rank-bm25 sentence-transformers rapidfuzz python-dotenv requests

# keys: TYPESAFE_API_KEY (console.typesafe.ai), GEMINI_API_KEY (aistudio.google.com/apikey)
cp .env.example .env   # then edit

# experiment 01 (downloads SQuAD 2.0 dev into data/)
curl -sL -o data/dev-v2.0.json --create-dirs https://rajpurkar.github.io/SQuAD-explorer/dataset/dev-v2.0.json
.venv/bin/python run_eval.py --n 150

# experiments 02 and 03 (SearchTome: see experiments/02-.../REPORT.md for the dataset files)
.venv/bin/python run_exp02.py
.venv/bin/python run_exp03.py
```

Every API call is cached under `.cache/`, so re-runs are free and an interrupted run resumes. To replay published
results without any API key, unzip an experiment's `raw_api_responses.zip` into `.cache/`.

## Setup notes

- New Google AI Studio keys must use the **Interactions API**; `generateContent` returns 404 for them.
- Answering model: `gemini-3.5-flash-lite`. Judge: `gemini-3.6-flash`. Jev: `jev-1.13.0`.
- Total API cost across all three experiments: **under $1**.

## Credits and caveats

- **Jev / System One** by [TypeSafe AI](https://typesafe.ai); the re-ranking, hierarchical-classification and
  citation-check setups follow their [cookbooks](https://docs.typesafe.ai/).
- **STAIR** by IBM Research ([arXiv 2609.03874](https://arxiv.org/abs/2609.03874)). IBM's own artifacts have
  expired, so experiment 02 uses the community rebuild
  [SGK86/searchtome-subset](https://huggingface.co/datasets/SGK86/searchtome-subset), whose STAIR is much weaker
  than the published one (32.5% vs 82.6% Recall@1). "STAIR loses here" is **not** a verdict on the published system.
- That rebuild's questions reuse their source section's wording, which favours keyword search.
- Sample sizes are small: 150–518 questions per experiment, one answering model, one judge.

MIT licensed. Corrections and replications welcome — open an issue.
