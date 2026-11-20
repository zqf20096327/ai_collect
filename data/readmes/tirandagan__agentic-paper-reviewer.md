<p align="center">
  <img src=".claude-plugin/icon.png" width="128" alt="Agentic Research Paper Reviewer icon">
</p>

<h1 align="center">Agentic Research Paper Reviewer</h1>

<p align="center">
  <em>A Claude Code plugin by <a href="https://github.com/tirandagan">Tiran Dagan</a>.
  Detailed, grounded feedback on your research paper in one sitting instead of one review cycle.</em>
</p>

https://github.com/user-attachments/assets/c25aebaa-cd78-4553-92c7-639c66f1c93e

**[User guide](docs/USER_GUIDE.md)**: install, inputs, reading the score,
recalibration, troubleshooting and privacy.

## Why this exists

Peer review is slow. A paper submitted to a major venue waits months for
feedback, and a rejection often arrives with three short reviews and no clear
path forward. In the [tech overview of paperreview.ai](https://paperreview.ai/tech-overview),
Yixing Jiang and Andrew Ng describe what prompted their reviewer: a student
whose paper was rejected 6 times over 3 years, each round costing about 6
months. Much of that feedback could have come before submission.

paperreview.ai, the **Stanford Agentic Reviewer** from the Stanford ML Group,
showed that an agentic pipeline can produce a useful review. It reads the
paper, searches the literature, reads the closest related work and writes a
grounded critique. On ICLR 2025 its scores agree with a human reviewer about
as well as two human reviewers agree with each other.

This plugin brings that approach into Claude Code, so an author can run it on
their own draft, locally, as often as they like:

- **Before submission:** find the missing baseline, the overclaimed result
  and the uncited competing paper while there is still time to fix them.
- **Between revisions:** re-run and see which dimensions moved.
- **On a rejection:** get a second, more detailed reading of what reviewers
  likely saw.

It is built for **authors seeking feedback on their own work**. It is not a
substitute for peer review, and most venues forbid reviewers from uploading
assigned submissions to AI tools.

## How well it works

The plugin was run blind on real ICLR 2025 submissions. Reviewers saw only
the pre-decision PDF, and literature was limited to what existed at the
submission deadline. Its scores were then compared with the human
reviewers' ratings, using the same measures paperreview.ai publishes for
itself.

![Calibration and ranking quality versus paperreview.ai](calibration/headline.png)

- **Ranking matches the human reviewers.** In both test runs the plugin's
  scores put papers in nearly the same order as the human reviewers'
  ratings (Spearman 0.66 and 0.74). It also told accepted papers from
  rejected ones about as well as a single human reviewer (AUC 0.85 and
  0.82). paperreview.ai reports 0.42 and 0.75 for itself.
- **Scores land on the human scale.** After the rescale, the share of
  papers scored 5.5 or less falls as human ratings rise, as on
  paperreview.ai's own calibration plot. The plugin's average gap from the
  human rating was 0.00 and its average error 1.15 points, measured on
  papers held out of the fit.
- **How much to trust it.** Each run used 14 papers against paperreview.ai's
  147, so the bars on the right are wide. Read these results as "performs
  comparably to paperreview.ai", not "beats it". Single papers can still
  miss by 2–3 points.
  [Calibration](#calibration-against-paperreviewai) below and the
  [full report](calibration/REPORT.md) give the details.

## Credit

The pipeline design, the 7 scoring dimensions and the calibration
methodology are from **paperreview.ai** by **Yixing Jiang and Andrew Ng**
(Stanford ML Group), described at https://paperreview.ai/tech-overview. They
thank Jonathan Chen, Federico Bianchi, Jeremy Irvin and Yuhui Zhang for
discussions and feedback, and Abe Hou, Alan Li, Boyuan Liang, Chen Geng,
Fateme Nateghi, Kameron Collin Black, Livia Sun, Yuejun Shen and Yuming Shi
for testing support.

This plugin is an independent re-implementation from that public
description. It is **not affiliated with or endorsed by** the paperreview.ai
authors, Stanford University or the Stanford ML Group. The site publishes no
code, prompts or regression weights, so everything here that goes beyond the
public description is designed locally and documented as such. If you want
the original service, use https://paperreview.ai.

The pipeline also draws on the research the tech overview cites. Each of
those 16 papers and what it contributed is listed under
[The research behind each rule](#the-research-behind-each-rule).

## Install

**From this repo's marketplace,** in Claude Code (2.1.275 or later):

```
/plugin install agentic-paper-reviewer --marketplace tirandagan/agentic-paper-reviewer
```

On older versions, run `/plugin marketplace add tirandagan/agentic-paper-reviewer`,
then `/plugin install agentic-paper-reviewer@tirandagan-paper-reviewer`.

**Or from a clone,** without a marketplace:

```bash
git clone https://github.com/tirandagan/agentic-paper-reviewer.git ~/.claude-plugins/agentic-paper-reviewer
claude --plugin-dir ~/.claude-plugins/agentic-paper-reviewer
```

It needs `python3` (3.8 or later; standard library only) and access to
arXiv. There are no API keys and no accounts.

## Use

```
/agentic-paper-reviewer:paper-review ~/drafts/my-paper.pdf
/agentic-paper-reviewer:paper-review 2410.06215 NeurIPS
/agentic-paper-reviewer:paper-review ~/drafts/my-paper.pdf ICLR cutoff 2025-09-20
```

Or just ask: *"Review my draft at ~/drafts/my-paper.pdf before I submit it
to ICLR. Is the novelty claim defensible?"*

You get `my-paper-review.md`, a referee report, and
`my-paper-review.scores.json`. The report has these sections:

- Summary
- Strengths
- Weaknesses, each tagged major or minor
- Detailed Comments on novelty, soundness, experiments and clarity
- Questions for Authors
- A 7-dimension score table with a verdict
- Every arXiv paper consulted

[A sample review is in the calibration folder](calibration/sample-review.md).

## How it works: the pipeline

The original pipeline, as the tech overview describes it, maps onto this
plugin's 10 stages:

| # | Stage | What happens | In paperreview.ai |
|---|---|---|---|
| 1 | Ingest and sanity-check | Claude reads the **whole** PDF natively (text, figures, tables, appendices), extracts the title and stops if the document is not a paper | PDF → Markdown with LandingAI ADE (first 15 pages); title extraction and paper check |
| 2 | Private analysis | Notes on claims, methods and experiments, plus an **expected-experiments list**: what a rigorous version *should* contain, diffed against what is there | Not described (from MARG, below) |
| 3 | Query generation | 6–10 arXiv queries at different levels of specificity, covering benchmarks and baselines, the same problem and related techniques | Same: queries "of different levels of specificity" from the same three angles |
| 4 | Related-work search | arXiv API, all terms required, optional **literature cutoff** and self-exclusion | Tavily web search restricted to arXiv |
| 5 | Relevance selection | Each candidate scored 0–3 from title and abstract; the 8–12 most relevant kept; one re-search if too few | Same: relevance judged from metadata, most relevant kept |
| 6 | Evidence gathering | For each kept paper, the agent chooses **abstract only** or **full summary**. Full summaries come from parallel `related-paper-summarizer` subagents guided by named focus areas | Same choice and the same focus-area-guided summaries |
| 7 | Draft the review | Fixed template; **grounding gate** (every point cites the paper or an arXiv ID); novelty judged against named retrieved papers | Review written "following a template" (the template is not published) |
| 8 | Critic pass | One mandatory hostile-editor pass: specific, valid, grounded, non-duplicate, major | Not described (from MARG, Thakkar et al. and ReviewerToo) |
| 9 | Score | 7 dimensions on anchored 1–10 scales, combined with documented weights, then a rescale fitted on 14 ICLR 2025 papers | 7 dimensions, combined by a linear regression fit on ICLR 2025 |
| 10 | Deliver | Review Markdown and scores JSON next to your paper | Review link emailed; web viewer |

The 7 dimensions are the ones paperreview.ai scores:

1. originality
2. importance of the research question
3. whether the claims are well supported
4. soundness of the experiments
5. clarity of writing
6. value to the research community
7. contextualization relative to prior work

## Why the approach is rigorous

An LLM can write a confident, plausible and wrong review. The pipeline guards
against the failure modes that published evaluations of LLM reviewers have
documented:

- **Novelty blind spot.** LLM reviewers raise novelty concerns far less often
  than humans and over-focus on experiments (Liang et al.; Shin et al.). Here
  novelty is a mandatory section, judged against retrieved papers that are
  named and identified by arXiv ID, never from general impressions.
- **Generic comments.** In MARG, a refinement pass cut generic comments from
  60% to 29%. Stage 8 deletes any comment that would apply to any paper in the
  area, and any comment the paper already addresses.
- **Hallucination.** Every weakness must cite a quoted phrase with its
  section, or an arXiv ID, a grounding rule taken from ReviewerToo and from
  Thakkar et al.'s ICLR 2025 study of 20,000 reviews. Anything ungroundable is
  dropped or marked "Unverified impression".
- **Missing baselines.** The expected-experiments diff (MARG) predicts what
  should be there before reading what is.
- **Score drift.** GPT-4-era LLM reviewers inflated scores by 1–2 points
  (The AI Scientist; Agent Laboratory). Dimensions are scored against fixed
  anchors where 5 means a median, rejected ICLR submission. With Claude the
  drift went the other way (scores ran low), so the scoring guidance checks
  both directions. A rescale fitted on human ICLR ratings maps the result
  onto the human scale (see Calibration below).
- **Hindsight.** A literature cutoff keeps later work, including papers that
  build on the one under review, out of the novelty judgment.
- **Sycophancy.** No simulated rebuttal or discussion; in ReviewerToo,
  rebuttal rounds reduced fidelity.

### The research behind each rule

These are the 16 references on the paperreview.ai tech overview, in the
order the page lists them, with what each one put into this plugin. Fuller
notes are in [`design-notes.md`](skills/paper-review/references/design-notes.md).

| # | Reference | What it contributed here |
|---|---|---|
| 1 | Jin et al., *AgentReview: Exploring Peer Review Dynamics with LLM Agents*, [arXiv:2406.12708](https://arxiv.org/abs/2406.12708) | Reviewer biases shifted 37.1% of simulated decisions, and reviewers conform to each other. → An independent single review with no simulated discussion |
| 2 | D'Arcy, Hope, Birnbaum, Downey, *MARG: Multi-Agent Review Generation for Scientific Papers*, [arXiv:2401.04259](https://arxiv.org/abs/2401.04259) | Refinement cut generic comments from 60% to 29%; an "experiments" expert catches missing baselines. → Expected-experiments diff (Stage 2), critic pass (Stage 8), major over minor |
| 3 | Liang et al., *Can Large Language Models Provide Useful Feedback on Research Papers? A Large-Scale Empirical Analysis*, NEJM AI 1(8), 2024, [doi:10.1056/AIoa2400196](https://doi.org/10.1056/AIoa2400196) | GPT-4 feedback overlapped humans about as much as humans overlap each other, but rarely raised novelty and was often generic. → Full-paper reading, figure checks, anti-generic rules |
| 4 | Shin et al., *Mind the Blind Spots: A Focus-Level Evaluation Framework for LLM Reviews*, [arXiv:2502.17086](https://arxiv.org/abs/2502.17086) | LLMs over-focus on validity and neglect novelty (novelty F1 0.126). → Mandatory novelty subsection; fixed facet subsections |
| 5 | Sahu, Larochelle, Charlin, Pal, *ReviewerToo: Should AI Join The Program Committee?*, [arXiv:2510.08867](https://arxiv.org/abs/2510.08867) | Grounding every judgment in the manuscript or the literature; rebuttal rounds made reviews more sycophantic. → Grounding gate; no rebuttal simulation |
| 6 | Thakkar et al., *Can LLM feedback enhance review quality? A randomized study of 20K reviews at ICLR 2025*, [arXiv:2504.09737](https://arxiv.org/abs/2504.09737) | Critic and reliability tests with verbatim quotes as the hallucination control. → Critic checklist; quote grounding; drop rather than publish unverified points |
| 7 | Swanson, Wu, Bulaong, Pak, Zou, *The Virtual Lab*, bioRxiv [10.1101/2024.11.11.623004](https://doi.org/10.1101/2024.11.11.623004) | A recurring critic agent in an agent team. → Reinforces the mandatory critic pass |
| 8 | Si, Yang, Hashimoto, *Can LLMs Generate Novel Research Ideas?*, [arXiv:2409.04109](https://arxiv.org/abs/2409.04109) | Human novelty judgments agree weakly and LLM absolute scores are poorly calibrated. → Anchored scales with written justification; ±1.5 uncertainty |
| 9 | Si, Hashimoto, Yang, *The Ideation-Execution Gap*, [arXiv:2506.20803](https://arxiv.org/abs/2506.20803) | Ideas that look novel often fail on execution. → "Appears novel" is kept separate from "likely to hold up" |
| 10 | Rizvi et al., *Scaling Large Language Models for Next-Generation Single-Cell Analysis*, bioRxiv [10.1101/2025.04.14.648850](https://doi.org/10.1101/2025.04.14.648850) | Context for AI in science; no pipeline rule |
| 11 | Gottweis et al., *Towards an AI co-scientist*, [arXiv:2502.18864](https://arxiv.org/abs/2502.18864) | Generate → critique → refine. → The draft-then-critic structure |
| 12 | Wang et al., *Scientific discovery in the age of artificial intelligence*, Nature 620, 2023, [doi:10.1038/s41586-023-06221-2](https://doi.org/10.1038/s41586-023-06221-2) | Context; no pipeline rule |
| 13 | Lu, Lu, Lange, Foerster, Clune, Ha, *The AI Scientist*, [arXiv:2408.06292](https://arxiv.org/abs/2408.06292) | An LLM reviewer matched human balanced accuracy, with model-dependent inflation. → Critical-reviewer stance; anti-inflation rules |
| 14 | Yamada et al., *The AI Scientist-v2*, [arXiv:2504.08066](https://arxiv.org/abs/2504.08066) | Figure and caption review caught what text review missed. → Every figure checked against the claim made about it |
| 15 | Mitchener et al., *Kosmos: An AI Scientist for Autonomous Discovery*, [arXiv:2511.02824](https://arxiv.org/abs/2511.02824) | Interpretive statements were least accurate (57.9%). → Per-claim provenance; interpretation gets the most scrutiny |
| 16 | Schmidgall et al., *Agent Laboratory*, [arXiv:2501.04227](https://arxiv.org/abs/2501.04227) | Automated review scores ran about 2.3 points above humans. → Scores always shipped with the calibration caveat |

## Comparison with paperreview.ai

| | paperreview.ai | This plugin | Why |
|---|---|---|---|
| Where it runs | Hosted service; review link by email | Your Claude Code session; files next to your paper | Local, repeatable, private |
| PDF reading | LandingAI ADE → Markdown, first 15 pages, 10 MB | Claude reads the whole PDF, figures and appendices included | Figure–claim checks need the figures; appendix evidence counts |
| Literature search | Tavily web search restricted to arXiv | arXiv API, AND-joined terms with fallback | Same corpus, free, no key |
| Literature cutoff | Not described | Optional `--before` date; the paper itself excluded | Avoids hindsight; needed for honest calibration |
| Related-work summaries | Abstract or focus-guided full summary | The same choice; full summaries by parallel subagents | Faithful to the original |
| Review | Template (unpublished) | Published template with a grounding gate and a critic pass | Counters documented LLM-review failures |
| Scoring | 7 dimensions → linear regression fit on 150 ICLR 2025 papers | The same 7 dimensions → documented default weights + anchors, then a two-number rescale fitted on 14 ICLR 2025 papers | Their coefficients are not published; 14 papers support a 2-number fit, not a 7-weight one |
| Score for other venues | Hidden; ICLR only | Shown, labelled "ICLR-calibrated estimate" | The dimension scores stay useful; the label prevents over-reading |
| Model | Not disclosed | Claude, in your session | |

What the original reports, on 147 held-out ICLR 2025 papers:

| | Value |
|---|---|
| Spearman correlation, AI vs one human | 0.42 |
| Spearman correlation, human vs human | 0.41 |
| AUC for predicting acceptance, AI | 0.75 |
| AUC for predicting acceptance, one human | 0.84 |

The page notes that the AUC comparison favours humans, because acceptance
decisions were partly based on the human scores.

## Calibration against paperreview.ai

To check that this re-implementation behaves like the original, it was run
blind on ICLR 2025 submissions and its scores were compared with the human
reviewers' ratings and with paperreview.ai's published calibration plot.

**Setup.**
- Two runs of 14 papers each, drawn at random, 2 from each of the plot's 7
  bins of average human rating. The second run used new papers.
- Each PDF was the pre-decision "Under review" version from OpenReview,
  renamed `paper_NN.pdf`.
- Reviewers never saw the scores, the decision or the paper's identity.
- The literature cutoff was the ICLR 2025 deadline (2024-10-01).

The headline figure is at the top of this page. The full diagnostic plot,
with every paper and both runs, is [`calibration/run2/plot.png`](calibration/run2/plot.png).

| | paperreview.ai (147 papers) | This plugin, run 2 (14 papers) |
|---|---|---|
| Rank agreement with human ratings (Spearman) | 0.42 (one human; human vs. human 0.41) | **0.74** (95% CI 0.34–0.93); run 1: 0.66 |
| Separating accepted from rejected papers (AUC) | 0.75 | **0.82**; run 1: 0.85 |
| Average gap from the human rating | not reported | −1.08 raw → **0.00** after rescale |
| Mean absolute error | not reported | 1.28 raw → **1.15** after rescale (leave-one-out) |

**What this shows.**
- **Ranking: comparable to paperreview.ai.** In both runs the plugin put
  papers in about the same order as human reviewers, at least as well as
  paperreview.ai reports for itself. With 14 papers per run the intervals
  are wide, so this supports "comparable", not "better".
- **Scale: needed a correction.** Raw scores ran low and bunched up: 13 of
  14 papers scored 5.5 or less, Orals included.
  - Softening the scoring guidance between the runs narrowed the gap from
    −1.41 to −1.08 points. It did not close it.
  - So the final score applies a rescale fitted on run 2 (two numbers,
    `−2.71 + 1.81 × raw`), as paperreview.ai fits a regression on human
    ratings.
  - Tested by leaving one paper out at a time, it removes the bias. The
    curve of papers scored ≤ 5.5 now falls with human rating like
    paperreview.ai's.
- **Limits.**
  - 14 papers is a small sample, and the rescale has not yet been tested
    on a third, fresh set of papers.
  - ICLR 2025 papers may be in the model's training data.
  - Individual papers can still miss by 2–3 points.

The method, every number, the per-bin table and the caveats are in the
[calibration report](calibration/REPORT.md). A hand-checked sample review,
with its quotes and citations verified, is in
[calibration/sample-review.md](calibration/sample-review.md).

## Limitations

- **One reviewer's opinion.** A single pass, like the original. Run it two
  or three times and ask for a meta-review when it matters.
- **arXiv grounding.** Novelty checking is strongest where preprints are
  posted (ML, CS, physics, math). In other fields the related-work search can
  miss the key prior paper.
- **The score is an estimate.** Default weights and a rescale fitted on 14
  papers, rather than a regression fitted on 150; read it as ±1.5. See the
  calibration results above.
- **It can be wrong.** Quotes, numbers and citations are checked in the
  critic pass, but the review is AI-generated and can still contain errors.
  Verify before acting on it.
- **English-language papers only.**

## Responsible use

Use this on your own work. Most conferences and journals prohibit reviewers
from uploading submissions they were assigned to review into AI tools. If
the skill can tell that you are reviewing someone else's paper for a venue,
it says so and leaves the decision to you.

## Privacy

Your paper is read inside your Claude Code session and is not uploaded
anywhere by this plugin. Its only network traffic goes to arXiv: short search
queries and downloads of related arXiv papers. Nothing goes to paperreview.ai,
OpenReview or any other service. The optional calibration scripts contact
OpenReview only when you run them, with your own account.

## Development

```bash
bash tests/run.sh          # offline: manifests, skill paths, script unit tests, hygiene
bash tests/run.sh --live   # plus one real arXiv search with a literature cutoff
claude plugin validate .
```

Layout:

```
.claude-plugin/          plugin.json, marketplace.json, icon
skills/paper-review/     SKILL.md (the pipeline), references/, scripts/arxiv_search.py
agents/                  related-paper-summarizer.md
calibration/             ICLR 2025 sampler, analysis, results and report
docs/USER_GUIDE.md
tests/
```

## License

MIT, © 2026 Tiran Dagan. See [LICENSE](LICENSE). paperreview.ai and the
Stanford Agentic Reviewer are the work of their authors; the names are used
only to credit and describe the method this plugin follows.
