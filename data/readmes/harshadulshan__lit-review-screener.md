<div align="center">

# 📚 Literature Review Screener

**Screening thousands of abstracts for a systematic review, without reading all of them.**
Active learning puts the relevant papers first, and a statistical test tells you when it is safe to stop.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-app-FF4B4B?logo=streamlit&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-active%20learning-F7931E?logo=scikitlearn&logoColor=white)
![PRISMA](https://img.shields.io/badge/PRISMA-2020-1f6feb)
![Checks](https://img.shields.io/badge/checks-82%20engine%20%2B%2038%20app-2EA44F)
![License](https://img.shields.io/badge/license-MIT-blue)

<img src="docs/banner.svg" alt="Animated banner: shuffled search results reorder so the relevant papers come first, and screening stops safely" width="100%">

<img src="docs/scoreboard.svg" alt="On 27 real reviews: 40% read to find 95% of the relevant papers (random order 95%), median work saved 55%, statistical stopping rule reached 95% recall in 100% of 270 runs, '50 irrelevant in a row' in 21%" width="100%">

</div>

## 🎯 The problem

A systematic review has to find **every** relevant study, so its database searches return thousands of records,
of which often only 1–5% are relevant. Reading every title and abstract, usually by two people, takes weeks. Tools
that rank records by likely relevance help, but leave the hard question open: **when can you stop reading?** Stop too
early and you silently miss studies; never stop and the ranking saved nothing.

## 📸 The app

<img src="docs/screenshots/00_app_screening.png" alt="The app screening the van Dis 2020 review: 2 of 10,246 records screened, the stopping test's p-value, and one record with its abstract" width="100%">

| **1 · Import your database exports** | **2 · Remove duplicates** |
|:---:|:---:|
| ![Import tab: upload RIS, PubMed, Web of Science or CSV/Excel exports, or load the demo or a benchmark review](docs/screenshots/01_import_dedup.png) | ![10,953 records identified, 707 duplicates removed by DOI, exact or near-identical title, 10,246 left to screen](docs/screenshots/06_duplicates.png) |
| Upload RIS, PubMed, Web of Science or CSV/Excel, or load the demo or one of the 27 benchmark reviews | 707 duplicates found by DOI, exact title or near-identical title; every matched pair can be checked |
| **3 · Screen, most likely relevant first** | **4 · Watch the stopping test** |
| ![Screen tab: one record at a time with Relevant, Irrelevant and Undo buttons](docs/screenshots/02_screening.png) | ![Progress and stopping tab: relevant found and the stopping test p-value](docs/screenshots/03_progress_stopping.png) |
| One record at a time: Relevant / Irrelevant / Undo. Add papers you already know to give the model a head start | Relevant found and the test's p-value as you go (here just after starting; the replay below shows a full run) |
| **5 · PRISMA 2020, filled in for you** | **The flow diagram** |
| ![PRISMA tab: full-text counts and exclusion reasons; the diagram is marked as a draft until the rule is met](docs/screenshots/07_prisma_tab.png) | ![PRISMA 2020 flow diagram for the review](docs/screenshots/04_prisma.png) |
| Add the full-text stage yourself; the diagram stays a draft until the stopping rule is met | Downloadable as SVG for the paper |
| **6 · Methods text, references, downloads** | **7 · Benchmark: 27 real reviews** |
| ![A ready-to-edit methods paragraph with references, and CSV, RIS, SVG and project-file downloads](docs/screenshots/08_methods_downloads.png) | ![Benchmark tab: 40% read to find 95%, WSS@95 55%, statistical rule 100% of runs vs 21%](docs/screenshots/05_benchmark.png) |
| A methods paragraph to paste into your paper, with references; decisions as CSV, included records as RIS | The results below, review by review |
| **Three models, two stopping rules** | **One review in detail** |
| ![Naive Bayes, logistic regression and linear SVM compared; recall when each stopping rule said stop](docs/screenshots/09_benchmark_models_stopping.png) | ![Kitchenham 2010: share of relevant records found against share screened, over 10 runs](docs/screenshots/10_benchmark_one_review.png) |
| Logistic regression saves the most (median 62%); every dot is one simulated screening | Kitchenham 2010: the range over 10 runs against random order |

| Tab | What you do there |
|---|---|
| 📥 **Import** | Upload search exports (RIS, PubMed/MEDLINE, Web of Science, Scopus/Excel/CSV). Duplicates across databases are removed by DOI, exact title or near-identical title; uncertain pairs are listed for you to confirm. |
| 🔎 **Screen** | One record at a time, the most likely relevant first. Words that pushed the ranking up or down are highlighted. Relevant / Irrelevant / Undo. Search for papers you already know to give the model a head start. |
| 📈 **Progress & stopping** | Relevant found vs read, the stopping test's p-value over time, what the model has learned, and what other targets would allow. |
| 📝 **PRISMA & export** | PRISMA 2020 flow diagram (SVG), a ready-to-edit methods paragraph with references, and downloads: all decisions (CSV), included records (RIS for Zotero/EndNote), the project file. |
| 🧪 **Benchmark** | The 27-review results below, per review and per model, and a live simulation you can run yourself. |

Projects can be saved and reopened, so a review can be screened over many sessions.

## ⚡ Tested on 27 real systematic reviews

The app was run, in simulation, on **27 published systematic reviews** (79,674 search results, 1,764 relevant)
whose authors' screening decisions are public: medicine, psychology, software engineering and more.

<img src="docs/recall_curves.svg" alt="Animated chart: share of relevant papers found against share of papers read, for 27 reviews" width="100%">

| | Result (Naive Bayes, 10 runs per review) |
|---|---|
| 📖 **Reading needed to find 95% of the relevant papers** | median **40%** of the records (random order: 95%) |
| ⏱️ **Work saved at 95% recall (WSS@95)** | median **55%**; on the 7 reviews with 5,000+ records, 63–92% |
| 🔟 **Relevant papers found in the first 10% read** | median **65%** |

<img src="docs/wss_per_review.svg" alt="Animated bar chart: work saved at 95% recall for each of the 27 reviews, from 92% (software fault prediction) to 4% (antihistamines); median 55%" width="100%">

Big reviews save the most: **63–92%** on the 7 reviews with 5,000+ records, exactly where reading everything hurts. Small
drug reviews whose records all look alike save little.

### When to stop: a rule of thumb vs. a statistical test

<img src="docs/stopping_rules.svg" alt="Animated strip chart: recall reached when each stopping rule said stop, for 270 simulated screenings" width="100%">

| Stopping rule | Reached 95% recall | Relevant papers missed (mean) | Work saved (median) |
|---|---|---|---|
| "Stop after 50 irrelevant in a row" (common practice) | **21%** of runs | 9.7 | 84% |
| **Statistical rule** (95% recall, 95% confidence) | **100%** of 270 runs | 0.45 | 18% |
| Statistical rule, relaxed (90% recall, 90% confidence) | 99% reached 90% | 1.7 | 37% |

> **In plain words:** the ranking finds nearly everything early, but a rule of thumb cannot tell you *that* it has.
> In 4 of 5 runs, "50 irrelevant in a row" stopped before 95% of the studies were found, in the worst case after
> finding almost none. The statistical rule never fell short in 270 runs. Its price is reading more than the
> ranking alone would need, because a guarantee needs evidence. The relaxed setting roughly doubles the work saved.

### Watch one screening

<img src="docs/one_run.svg" alt="Animated replay of one screening of the Kitchenham 2010 review: '50 irrelevant in a row' stops after 322 records with 37 of 45 found; 95% are found after 903; the statistical rule stops after 1,449 with all 45 found and 255 records never read, when the p-value falls below 0.05" width="100%">

One benchmark run of the Kitchenham 2010 review, replayed with the app's own engine. "50 irrelevant in a row" stops
after **322** records, with 8 of the 45 studies still unfound. The statistical test's p-value stays near 1 until long runs
of irrelevant records pile up, and falls below 0.05 at **1,449**, when all 45 have been found and the last 255 records
(15%) never need reading.

## 🧠 How it works

<img src="docs/pipeline.svg" alt="Animated pipeline: import 10,953 records, remove 707 duplicates, rank with active learning, screen (the model retrains after every decision), stopping test p below 0.05, PRISMA 2020 diagram, methods text and exports" width="100%">

| Idea | In plain words |
|---|---|
| **Active learning** | Titles, abstracts and keywords become TF-IDF features. After every decision a classifier is retrained on everything screened so far and re-ranks what is left, so the next record shown is the one most likely to be relevant (the approach of ASReview, van de Schoot et al. 2021). |
| **Balanced training** | Relevant records are rare, so both classes get equal total weight; ties in the ranking are broken at random, never by file order. |
| **Statistical stopping rule** | Callaghan & Müller-Hansen (2020): treat the records read since some point as a sample from what was still unread. If recall were below 95%, at least *K* relevant records would be in that pool; a hypergeometric test asks how likely it is to have seen so few. Below 0.05, recall ≥ 95% with 95% confidence. |
| **PRISMA 2020** | Identification and screening counts are filled in automatically; records left unread after the rule is met are reported as "marked as ineligible by automation tools". |

## 🚀 Quick start

```bash
git clone https://github.com/harshadulshan/lit-review-screener.git
cd lit-review-screener
pip install -r requirements.txt
streamlit run app.py
```

Click **Load the demo** to try it on two overlapping database exports (a real software-engineering review), or
**Load a benchmark review** for any of the 27 (downloaded once and cached).

**For your own review:** export each database search as RIS (or PubMed/.nbib, Web of Science plain text, CSV),
upload them together, check the possible duplicates, and start screening. Choose the target recall and confidence
**before** you begin and report them in your methods.

## ✅ Verified

```bash
python tests/verify_engine.py      # 82 checks, about a minute
python tests/verify_app.py         # 38 checks: runs the app headlessly through every tab
python benchmarks/run_benchmark.py # the 27-review benchmark (about an hour on 2 cores)
```

- **Stopping test**: equals an exact combinatorial count; the fast version (only samples starting after a relevant
  record) gives the same answer as scanning every start on 4,500 random cases; and in 200 simulated reviews with a
  mediocre ranking, recall was ≥ 95% when it said stop in 99.5% of them.
- **No look-ahead**: changing the labels of records not yet screened leaves every earlier ranking decision unchanged.
- **Ranking model**: Naive Bayes scores equal the balanced log-likelihood ratio computed by hand.
- **Metrics**: WSS, RRF and average time to discovery checked by hand; random order gives WSS ≈ 0 and ATD ≈ 50%.
- **Import & duplicates**: RIS, MEDLINE, Web of Science and Scopus CSV parsed field by field; 297 of 300 planted
  duplicates merged and the other 3 flagged, with no different papers merged.
- **Mutation check**: 15 bugs planted one at a time (wrong K_tar, max instead of min p, unbalanced training, ties by
  file order, WSS without the baseline, ...). The tests caught all 15.

## ⚠️ Limitations

- **The ranking changes the order, not the decisions.** Every included record is still judged by a person.
- **The guarantee assumes the ranking is at least as good as random** for the unread records, which held in every
  benchmark run but is not proven for every review.
- **Small or unusual reviews benefit less**: in a few drug reviews with very similar records (e.g. antihistamines,
  300 records) ranking saved almost nothing.
- **Papers with unusual wording are found last.** A broad search and a few known relevant papers as prior knowledge help.
- **One screener.** Many reviews need two independent screeners: export the decisions and compare them.

<details>
<summary><b>📂 Project structure, data & references</b></summary>

```
app.py                     Streamlit interface (6 tabs)
screener/records.py        RIS, MEDLINE, Web of Science, CSV/Excel import; RIS export
screener/dedup.py          duplicate detection across databases
screener/model.py          TF-IDF features, Naive Bayes / logistic regression / linear SVM, ranking
screener/active.py         active-learning loop and benchmark simulation
screener/stopping.py       Callaghan & Müller-Hansen stopping test, heuristic rule
screener/metrics.py        WSS, RRF, average time to discovery
screener/project.py        screening session, save / load
screener/prisma.py         PRISMA 2020 flow diagram (SVG)
screener/report.py         PRISMA counts, methods paragraph
benchmarks/                run_benchmark.py, results.json, demo-file builder
sample_data/               demo exports (RIS + Web of Science) and the Kitchenham (2010) review
tests/                     verify_engine.py, verify_app.py
```

**Data.** Benchmark reviews from the ASReview systematic-review datasets
(github.com/asreview/systematic-review-datasets, CC-BY 4.0 / CC0; the 15 Cohen et al. 2006 reviews under their own
open licence). The demo exports are built from Kitchenham et al. (2010) by `benchmarks/make_demo_exports.py`.

- Callaghan, M. W., & Müller-Hansen, F. (2020). Statistical stopping criteria for automated screening in systematic
  reviews. *Systematic Reviews*, 9, 273. doi:10.1186/s13643-020-01521-4
- van de Schoot, R., et al. (2021). An open source machine learning framework for efficient and transparent
  systematic reviews. *Nature Machine Intelligence*, 3, 125–133. doi:10.1038/s42256-020-00287-7
- Page, M. J., et al. (2021). The PRISMA 2020 statement. *BMJ*, 372, n71. doi:10.1136/bmj.n71
- Cohen, A. M., et al. (2006). Reducing workload in systematic review preparation using automated citation
  classification. *JAMIA*, 13(2), 206–219. doi:10.1197/jamia.M1929
- Ferdinands, G., et al. (2023). Performance of active learning models for screening prioritization in systematic
  reviews. *Systematic Reviews*, 12, 100.
- Kitchenham, B., et al. (2010). Systematic literature reviews in software engineering – a tertiary study.
  *Information and Software Technology*, 52(8), 792–805.

</details>

<div align="center">

**Harsha Dulshan** · BSc (Hons) Management Information Systems, NSBM Green University
[GitHub](https://github.com/harshadulshan) · [LinkedIn](https://www.linkedin.com/in/harsha-kaldera/) · MIT License

</div>
