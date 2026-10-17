# Transformers Projects

A curated Chinese NLP lab built with Hugging Face Transformers. The notebooks cover language
modeling, named entity recognition, machine reading comprehension, multiple choice reasoning,
sentence similarity, dense retrieval, retrieval-augmented chatbot ranking, and abstractive
summarization with T5/GLM-style models.

This repository packages the original learning notebooks from the local `DL` workspace into a
cleaner research portfolio: original notebooks are preserved, heavy checkpoints are excluded, and
the small committed reports summarize the real training artifacts found locally.

## Project Matrix

| Track | Notebook | Dataset / source | Model family | Signal |
| --- | --- | --- | --- | --- |
| Masked LM | `masked_lm.ipynb` | Chinese wiki filtered corpus | `hfl/chinese-macbert-base` | MLM objective and data collator training |
| Causal LM | `casual_lm.ipynb` | Chinese wiki filtered corpus | Causal language model | autoregressive LM training workflow |
| NER | `NER.ipynb` | `lansinuote/peoples-daily-ner` | MacBERT token classification | token alignment, BIO labels, sequence evaluation |
| MRC | `MRC_simpleVer.ipynb`, `MRC_slideVer.ipynb` | CMRC2018 | MacBERT QA | span extraction, sliding window post-processing, CMRC F1/EM |
| Multiple choice | `MultipleChoice.ipynb` | CLUE C3 | MacBERT multiple-choice | Chinese reasoning and option ranking |
| Sentence similarity | `SentenceSimilarity_Crossmodel.ipynb` | Chinese pairwise similarity JSON | Cross-encoder regression/classification | reranking-quality pair scoring |
| Dual encoder | `SentenceSimilarity_Vecormatch.ipynb`, `dual_model.ipynb` | Chinese pairwise similarity JSON | Siamese MacBERT | vector retrieval and cosine training |
| Retrieval chatbot | `Retrieval_chatbot.ipynb` | Law QA / conversation data | FAISS + dual encoder + cross encoder | retrieve-then-rerank response selection |
| Summarization | `T5 summarization.ipynb`, `GLM summarization.ipynb` | NLPCC 2017 summarization | Mengzi-T5 / GLM | sequence-to-sequence summarization |

## Results Snapshot

The table below is generated from local Hugging Face `trainer_state.json` artifacts. Large weights,
optimizers, Arrow caches, and raw datasets are not tracked.

| Experiment | Best / final metric | Notes |
| --- | --- | --- |
| People Daily NER | F1 `0.9529` at epoch 3 | Strong token-classification baseline with MacBERT. |
| Sentence similarity cross encoder | F1 `0.8846`, accuracy `0.9095` | Best checkpoint at step 375. |
| Dual encoder sentence similarity | F1 `0.7449`, accuracy `0.7945` | Vector retrieval model used by chatbot pipeline. |
| T5 summarization | ROUGE-1 `0.5004`, ROUGE-2 `0.3356`, ROUGE-L `0.4239` | Best checkpoint at epoch 3. |
| Masked LM | training loss `1.2747` | Local wiki MLM training run. |
| GLM summarization | training loss `11.9874` | Compatibility-focused GLM training notebook. |

![Trainer artifact summary](reports/figures/trainer_metric_summary.png)

## Second-Pass Review Evidence

The latest maturity iteration turns the notebook collection into an auditable NLP project archive.

| Review artifact | What it checks | Output |
| --- | --- | --- |
| Notebook complexity | 13 notebooks, NLP track, code cells, imports, Trainer usage, metric computation | [`second_pass_notebook_complexity.csv`](reports/results/second_pass_notebook_complexity.csv) |
| Metric leaderboard | Best available metric per training artifact family | [`second_pass_metric_leaderboard.csv`](reports/results/second_pass_metric_leaderboard.csv) |
| Task coverage matrix | Notebook presence, dataset/model/objective metadata, trainer artifact availability | [`second_pass_task_coverage_matrix.csv`](reports/results/second_pass_task_coverage_matrix.csv) |

![Notebook track footprint](reports/figures/second_pass_notebook_track_footprint.png)
![Task coverage](reports/figures/second_pass_task_coverage.png)

## Repository Map

| Path | Purpose |
| --- | --- |
| `notebooks/original/` | Original notebooks and helper files from the local DL workspace. |
| `src/transformers_projects/` | Clean utility code for CMRC scoring, dual-encoder modeling, and artifact summaries. |
| `scripts/` | Reproducible commands for artifact summarization and smoke validation. |
| `configs/` | Task registry describing datasets, models, notebooks, and expected outputs. |
| `reports/` | Experiment summary, data card, model notes, and generated result CSVs/figures. |
| `tests/` | Notebook integrity and utility tests. |

## Quick Start

```powershell
python -m pip install -e ".[dev]"
python -m pytest
python scripts/run_smoke.py
```

To regenerate reports from the original local `DL` folder:

```powershell
python scripts/summarize_artifacts.py --source C:\Users\Yuto\Desktop\Code\CODEX\DL --out reports/results/trainer_state_summary.csv
```

For full notebook execution, install the NLP extras and download the referenced datasets:

```powershell
python -m pip install -e ".[dev,nlp]"
```

## Data And Checkpoint Policy

The local `DL` folder contains multi-GB Hugging Face caches and checkpoints. This repository does not
commit those artifacts. It commits:

- original notebooks
- compact helper code
- task registry metadata
- trainer-state summaries
- report figures
- reproducibility notes

This keeps GitHub usable while still documenting real local training work.
