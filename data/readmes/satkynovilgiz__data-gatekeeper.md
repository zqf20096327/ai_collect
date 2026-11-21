# Data Gatekeeper — Automated Data Cleaning & Validation System

[![tests](https://github.com/satkynovilgiz/data-gatekeeper/actions/workflows/tests.yml/badge.svg)](https://github.com/satkynovilgiz/data-gatekeeper/actions/workflows/tests.yml)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A backend engine that **profiles, cleans, and validates** any dataset before it is used.
CadetX AI Engineering & Data Science internship project (12 sprints, see [`docs/sprint_plan.md`](docs/sprint_plan.md)).

```
raw.csv ──► Module 1: Profile ──► Module 2: Clean ──► Module 3: Validate ──► Module 4: Automate
            profiling_report.json   cleaned_data.csv    validation_report.json   CLI + Docker
                                    cleaning_log.json
```

| Module | Status | Output |
|---|---|---|
| 1. Profiling & Metadata Intelligence | ✅ **complete** (v1.2, Sprint 3): CLI + API + JSON Schema, disguised missing, quality score, cleaning suggestions | `profiling_report.json` + charts |
| 2. Cleaning & Transformation | 🔄 **in progress**: Sprint 4 ✅ core pipeline (schema inference, cleaning steps, cleaning log, quality delta) · Sprint 5 ✅ ML cleaning (KNN / regression / iterative imputation + evaluation, IQR + Isolation Forest outliers, fuzzy duplicates) · Sprint 6 transformation + API | `cleaned_data.csv`, `cleaning_log.json`, `schema.json` |
| 3. AI Validation & Anomaly Detection | ⏳ | `validation_report.json` |
| 4. Integration, CLI & Docker | ⏳ | `python pipeline.py --input ... --output ...` |

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python scripts/download_bank_marketing.py    # real finance dataset (UCI Bank Marketing, 41k rows)
python run_profiling.py --input data/raw/bank_marketing.csv --output results/bank   # ~3.5 s
python run_profiling.py --input data/raw/bank_marketing.csv --output results/quick --sample 5000
python run_cleaning.py --input data/raw/bank_marketing.csv \
       --profile results/bank/profiling_report.json --output results/bank   # Module 2
python run_cleaning.py --input data/raw/hr_employees_messy.csv --output results/hr \
       --evaluate-imputers                    # + compare median / knn / regression / iterative
pytest -q                                     # run the tests
```

### Shortcuts (Makefile)
| Command | Does |
|---|---|
| `make install` | install `requirements.txt` |
| `make test` | run all tests (`pytest -q`) |
| `make lint` | check the code with ruff |
| `make profile-sample` | profile the 1,000-row sample → `results/sample/` |

No internet? Use the committed 1,000-row sample `data/raw/bank_marketing_sample.csv`,
or the synthetic HR data (`python scripts/make_sample_data.py`). Dataset details: [`docs/dataset.md`](docs/dataset.md).

### Profiling API
```bash
uvicorn src.api.profiling_api:app --reload        # http://127.0.0.1:8000/docs
curl -F "file=@data/raw/bank_marketing_sample.csv" \
     http://127.0.0.1:8000/profile -o profiling_report.json
```
The report format is a JSON Schema: [`docs/profiling_report.schema.json`](docs/profiling_report.schema.json).

CLI output:
```
results/bank/
├── profiling_report.json     # stats, issues, quality_score, cleaning_suggestions
└── charts/
    ├── missing_heatmap.png
    ├── correlation_heatmap.png
    ├── outlier_distribution.png
    ├── hist_<column>.png     # one per numeric column
    └── bar_<column>.png      # one per categorical column (top 10)
```

### Module 1 results on Bank Marketing (41,188 rows × 21 columns)
| | |
|---|---|
| Empty cells (what pandas sees) | 0.0% |
| **Disguised missing** (`unknown`, `pdays = 999`) | **52,391 cells → true missing 6.06%** in 7 columns |
| Duplicate rows | 12 |
| PII columns | none (anonymised data) |
| Issues | 13 (2 high, 11 medium) → 13 cleaning suggestions |
| **Quality score** | **98.48 / 100** (completeness 93.94, uniqueness 99.97, validity 100, consistency 100) |
| Run time | 2.5 s profiling, 3.5 s with charts |

Details: [`docs/module1_profiling.md`](docs/module1_profiling.md) · slides: [`docs/module1_presentation.md`](docs/module1_presentation.md)

### Module 2 results (Sprints 4–5: cleaning pipeline + ML cleaning)
```bash
python run_cleaning.py --input data/raw/hr_employees_messy.csv --output results/hr   # profiles first
python run_cleaning.py --input ... --imputer knn --outliers cap --fuzzy-threshold 90 --evaluate-imputers
```
Writes `cleaned_data.csv`, `cleaning_log.json` (every change with before → after examples),
`schema.json` (expected type, range, format per column, for Module 3) and, with `--evaluate-imputers`,
`imputer_evaluation.json` + `.png`. The raw file is never changed.

| | Bank Marketing (41,188 × 21) | HR messy sample (523 × 10) |
|---|---|---|
| Rows | 41,188 → 41,176 (12 exact duplicates) | 523 → 508 (15 exact duplicates) |
| Fixed | 4,121 `unknown` → NaN → imputed; `default = unknown` (8,597) **kept as a category**; `pdays 999` → `previously_contacted` | 19 category variants, 52 dates → ISO, 15 `"five"`, 15 bad emails, 10 `age = 230` |
| Fuzzy duplicates | skipped (no name column) | **8 pairs** flagged (8/8 planted, 0 false) |
| Outliers (flagged, values kept) | IQR 6,283 cells · Isolation Forest 412 rows · both 226 | IQR 7 cells · Isolation Forest 6 rows · both 5 (salary 9,999,999) |
| Values imputed (iterative) | 4,120 | 89 |
| **Quality score** | **98.48 → 98.91 (+0.43)** | **88.87 → 99.87 (+11.00)** |
| Run time (whole CLI) | 59 s with iterative (cleaning 49 s) · 13 s with `--imputer median` · 77 s with `--evaluate-imputers` | 4.2 s with `--evaluate-imputers` |

**Imputer evaluation** (hide 10% of known values, refill, compare). Bank Marketing, 9,000 hidden cells:

| | median / mode | knn | regression | **iterative** (default) |
|---|---|---|---|---|
| numeric error, mean NRMSE ↓ | 1.063 | 0.563 | 0.561 | **0.478** |
| categorical accuracy ↑ | 51.8% | 62.4% | 67.2% | **67.5%** |
| time (5,000 rows) | 0.02 s | 3.2 s | 2.0 s | 9.2 s |

![Imputer evaluation on Bank Marketing](docs/img/imputer_evaluation_bank.png)

Details, step order, the `pdays` and `unknown` decisions, how each ML method works:
[`docs/module2_cleaning.md`](docs/module2_cleaning.md) · [`docs/sprint4_summary.md`](docs/sprint4_summary.md) · [`docs/sprint5_summary.md`](docs/sprint5_summary.md)

## Project structure

```
data-gatekeeper/
├── data/raw/                 # input datasets (keep large files out of git — use DVC / Git LFS)
├── docs/                     # sprint plan, dataset, module docs, JSON schema
├── scripts/                  # dataset download + sample data generator
├── src/
│   ├── api/
│   │   └── profiling_api.py  #   FastAPI: POST /profile
│   ├── profiling/            # Module 1
│   │   ├── semantic.py       #   type + meaning detection (email, phone, card, IP, DOB, id, PII)
│   │   ├── profiler.py       #   profile_file / profile_dataset + rule engine -> report dict
│   │   ├── suggestions.py    #   issues -> cleaning suggestions (hand-off to Module 2)
│   │   └── visualize.py      #   backend charts (PNG)
│   ├── quality/
│   │   └── score.py          #   data quality score 0-100 (shared by Module 1 and 2)
│   ├── cleaning/             # Module 2
│   │   ├── schema.py         #   infer_schema: expected type / range / format per column -> schema.json
│   │   ├── cleaner.py        #   12 cleaning steps + cleaning_log.json + quality before/after
│   │   ├── imputers.py       #   median / knn / regression / iterative (MICE) imputation
│   │   ├── evaluation.py     #   imputer evaluation: hide 10%, refill, RMSE / MAE / accuracy + chart
│   │   ├── outliers.py       #   IQR (per column) + Isolation Forest (per row)
│   │   └── fuzzy.py          #   fuzzy duplicates with rapidfuzz
│   └── validation/           # Module 3 (to build)
├── tests/                    # pytest
├── run_profiling.py          # Module 1 CLI
├── run_cleaning.py           # Module 2 CLI
└── requirements.txt
```

## Workflow
- Work on a **branch per sprint/feature** → small commits → **pull request** → review → merge to `main`.
- Weekly meeting + rotating Scrum Master (see `docs/team.md`).
- Each module gets its own short presentation / doc in `docs/`.
