<h1 align="center">scicraft</h1>

<p align="center"><b>A registry of 40 hard skills for research with Claude Code.</b><br>
Figures, papers, experiments and audits. Every skill comes with its scripts and its tests.</p>

<p align="center">
  <a href="LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/badge/license-Apache--2.0-blue"></a>
  <a href="https://github.com/EliHei2/scicraft/actions/workflows/gate.yml"><img alt="Gate" src="https://github.com/EliHei2/scicraft/actions/workflows/gate.yml/badge.svg"></a>
  <a href="https://github.com/EliHei2/scicraft/blob/traffic/downloads.json"><img alt="Downloads" src="https://github.com/EliHei2/scicraft/raw/traffic/badge.svg"></a>
</p>
<!-- PUBLIC BADGES: these two read the repository through shields.io and work only once it is public.
     At publication, move them into the paragraph above and delete this comment.
  <a href="https://github.com/EliHei2/scicraft/releases"><img alt="Release" src="https://img.shields.io/github/v/release/EliHei2/scicraft"></a>
  <a href="https://github.com/EliHei2/scicraft/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/EliHei2/scicraft"></a>
-->

<p align="center"><img src="docs/assets/demo-data-figure.png" alt="A three-panel results figure made by the data-figures skill" width="92%"></p>
<p align="center"><sub>One request to the <code>data-figures</code> skill: three panels at print size, composed in exact millimeters. Synthetic data.</sub></p>

**Contents:** [what it is](#what-it-is), [the registry at a glance](#the-registry-at-a-glance), [install](#install),
[all skills](#all-skills), [what is in a skill](#what-is-in-a-skill), [what is in this repository](#what-is-in-this-repository),
[why it holds up](#why-it-holds-up), [what comes next](#what-comes-next), [cite and credit](#cite-and-credit).

## What it is

A skill is a folder of instructions and small scripts that [Claude Code](https://claude.com/claude-code) loads
when a task needs it. scicraft is a registry of such skills for the work of a research project: making a figure,
writing and revising a paper, answering reviewers, designing an experiment, checking a result before it goes out.

They are hard skills. Each one is a rulebook together with the scripts that enforce it and the tests that check
it. Each rule is there because something went wrong without it: a figure that kept coming back, a sentence a
reviewer attacked, an error that one check would have caught.

## The registry at a glance

<!-- BEGIN GENERATED map: edit tools/catalog.json, then run python3 tools/build_index.py -->
**40 skills, 267 reference files, 238 scripts, 121 test cases with 887 graded checks.** They come as two plugins: `scicraft` (31 skills, any field) and `scicraft-ml` (9 skills, machine-learning research).

The skills follow a research project from the first idea to the release:

| Stage of a project | Skills |
|---|---|
| 1. Start and organize | `research-kickoff`, `project-structure`, `research-code` |
| 2. Design and run experiments | `ml-experiment-design`, `research-design-review`, `cluster-jobs`, `large-data`, `performance-tuning` |
| 3. Read the results | `training-diagnostics`, `ml-evaluation`, `representation-probes`, `embedding-maps`, `distribution-comparison`, `tabular-fm-studies`, `stats-reporting` |
| 4. Make the figures | `figure-development`, `data-figures`, `tikz-figures`, `canvas-schematics`, `design-system` |
| 5. Write | `paper-writing`, `ml-paper-writing`, `nature-methods-writing`, `author-voice`, `humanizer`, `latex-typesetting`, `book`, `research-report` |
| 6. Check before it goes out | `qc`, `integrity-audit`, `adversarial-audit`, `paper-code-parity` |
| 7. Answer reviewers, present, release | `rebuttal`, `poster`, `talk-slides`, `paper-website`, `research-release` |
| 8. Work with agents | `prompt-writing`, `agent-orchestration`, `distill-skills` |
<!-- END GENERATED map -->

Three more sets belong to the registry and are not in this repository:

| Set | Skills | Status |
|---|---|---|
| Spatial omics and single-cell work (`scicraft-bio`) | 5 | follows when the work it comes from is published |
| Large-scale pretraining | in preparation | follows when the work it comes from is published |
| The DKFZ cluster | 1 | private, shared with the Gerstung lab and the Stegle lab |

## Install

```bash
claude plugin marketplace add EliHei2/scicraft
claude plugin install scicraft@scicraft        # research craft for any field
claude plugin install scicraft-ml@scicraft     # machine-learning research
```

Start a new session and work as usual. You do not call a skill. Claude loads it when your request matches, and
the list below gives the kind of request each stage answers to.

Two other ways in: `./install.sh skills` copies single skill folders into `~/.claude/skills`, and
[`docs/CLAUDE.global.md`](docs/CLAUDE.global.md) is a working agreement to copy into your own `CLAUDE.md`.
For a lab or an organization, see [`docs/SHARING.md`](docs/SHARING.md).

## All skills

<!-- BEGIN GENERATED catalog: edit tools/catalog.json, then run python3 tools/build_index.py -->
40 skills, one line each. <sup>ML</sup> marks a skill of the `scicraft-ml` plugin; every other skill is in `scicraft`.

### 1. Start and organize

You say, for example: "turn this idea into a plan", "set this project up properly", "add this without breaking my scripts".

| Skill | What it does |
|---|---|
| [`research-kickoff`](plugins/scicraft/skills/research-kickoff) | Turns an idea into a verified research plan within days. |
| [`project-structure`](plugins/scicraft/skills/project-structure) | Keeps order in a project: code, data, results, governing documents. |
| [`research-code`](plugins/scicraft/skills/research-code) | Changes research software so that your scripts keep working. |

### 2. Design and run experiments

You say, for example: "is this design worth the GPU hours?", "write the job script for the cluster", "this table has a billion rows".

| Skill | What it does |
|---|---|
| [`ml-experiment-design`](plugins/scicraft-ml/skills/ml-experiment-design)&nbsp;<sup>ML</sup> | Plans experiments before compute is spent: plan, configs, gates. |
| [`research-design-review`](plugins/scicraft-ml/skills/research-design-review)&nbsp;<sup>ML</sup> | Decides a model design before compute is spent, and locks it. |
| [`cluster-jobs`](plugins/scicraft/skills/cluster-jobs) | Runs work on a batch cluster (LSF, SLURM) from a laptop. |
| [`large-data`](plugins/scicraft/skills/large-data) | Handles data too big for memory, resumable and honest about coverage. |
| [`performance-tuning`](plugins/scicraft/skills/performance-tuning) | Makes training or a pipeline faster without changing the science. |

### 3. Read the results

You say, for example: "why did this run collapse?", "is this ablation fair?", "what does this embedding hold?".

| Skill | What it does |
|---|---|
| [`training-diagnostics`](plugins/scicraft-ml/skills/training-diagnostics)&nbsp;<sup>ML</sup> | Diagnoses a training run: collapsed or alive, bug or effect. |
| [`ml-evaluation`](plugins/scicraft-ml/skills/ml-evaluation)&nbsp;<sup>ML</sup> | Makes a benchmark, ablation or leaderboard measure what it claims. |
| [`representation-probes`](plugins/scicraft-ml/skills/representation-probes)&nbsp;<sup>ML</sup> | Judges a learned representation against its noise floors. |
| [`embedding-maps`](plugins/scicraft-ml/skills/embedding-maps)&nbsp;<sup>ML</sup> | Renders and judges maps of learned embeddings. |
| [`distribution-comparison`](plugins/scicraft-ml/skills/distribution-comparison)&nbsp;<sup>ML</sup> | Compares two datasets, with a no-difference baseline for each number. |
| [`tabular-fm-studies`](plugins/scicraft-ml/skills/tabular-fm-studies)&nbsp;<sup>ML</sup> | Reference and tested scripts for tabular foundation models. |
| [`stats-reporting`](plugins/scicraft/skills/stats-reporting) | Decides how statistics are computed, drawn and worded. |

### 4. Make the figures

You say, for example: "make figure 2 from results/", "draw the architecture as a TikZ figure", "this plot looks machine-made".

| Skill | What it does |
|---|---|
| [`figure-development`](plugins/scicraft/skills/figure-development) | Takes a results figure from its claim to checked final panels. |
| [`data-figures`](plugins/scicraft/skills/data-figures) | Builds data panels in one house style, composed at exact millimeters. |
| [`tikz-figures`](plugins/scicraft/skills/tikz-figures) | Draws architecture diagrams and schematics in TikZ and PGFPlots. |
| [`canvas-schematics`](plugins/scicraft/skills/canvas-schematics) | Builds method and concept schematics on an HTML canvas. |
| [`design-system`](plugins/scicraft/skills/design-system) | One visual system across figure, slide, poster and web page. |

### 5. Write

You say, for example: "draft the methods section", "this paragraph sounds like AI", "assemble a book from my papers".

| Skill | What it does |
|---|---|
| [`paper-writing`](plugins/scicraft/skills/paper-writing) | Writes a paper from table of contents to final prose, claim by claim. |
| [`ml-paper-writing`](plugins/scicraft-ml/skills/ml-paper-writing)&nbsp;<sup>ML</sup> | Writes and checks papers for NeurIPS, ICML and ICLR. |
| [`nature-methods-writing`](plugins/scicraft/skills/nature-methods-writing) | Writes Online Methods and Supplementary Notes for Nature journals. |
| [`author-voice`](plugins/scicraft/skills/author-voice) | Keeps text that goes out under your name in your own voice. |
| [`humanizer`](plugins/scicraft/skills/humanizer) | Takes the machine out of a text without changing what it says. |
| [`latex-typesetting`](plugins/scicraft/skills/latex-typesetting) | Typesets in LaTeX and builds a PDF that passes a scripted gate. |
| [`book`](plugins/scicraft/skills/book) | Assembles and builds a book-length document from your own papers. |
| [`research-report`](plugins/scicraft/skills/research-report) | Builds the report for a supervisor as one HTML file plus a PDF. |

### 6. Check before it goes out

You say, for example: "check everything before I send it", "does the paper still say what the code does?", "try to break this".

| Skill | What it does |
|---|---|
| [`qc`](plugins/scicraft/skills/qc) | The gate before anything is handed over, with a short report. |
| [`integrity-audit`](plugins/scicraft/skills/integrity-audit) | Checks that the text matches the code, the records and the data. |
| [`adversarial-audit`](plugins/scicraft/skills/adversarial-audit) | Runs a multi-agent adversarial audit before compute or submission. |
| [`paper-code-parity`](plugins/scicraft/skills/paper-code-parity) | Keeps a paper and its code in agreement while both change. |

### 7. Answer reviewers, present, release

You say, for example: "answer reviewer 2", "turn the paper into a poster and a talk", "release the code and the weights".

| Skill | What it does |
|---|---|
| [`rebuttal`](plugins/scicraft/skills/rebuttal) | Writes replies to peer review: rebuttals, revisions, chair notes. |
| [`poster`](plugins/scicraft/skills/poster) | Builds a conference poster from the paper as one A0 page. |
| [`talk-slides`](plugins/scicraft/skills/talk-slides) | Builds a talk from one file: slides, PDF twin, speaker script. |
| [`paper-website`](plugins/scicraft/skills/paper-website) | Builds, checks and deploys the project website of a paper. |
| [`research-release`](plugins/scicraft/skills/research-release) | Releases the code, weights, notebooks and data of a paper. |

### 8. Work with agents

You say, for example: "write the brief for the other session", "run this overnight", "turn my history into skills".

| Skill | What it does |
|---|---|
| [`prompt-writing`](plugins/scicraft/skills/prompt-writing) | Writes the brief another agent works from, with no other context. |
| [`agent-orchestration`](plugins/scicraft/skills/agent-orchestration) | Runs work with AI agents that survives crashes and comes back true. |
| [`distill-skills`](plugins/scicraft/skills/distill-skills) | Turns your own history with an AI agent into installable skills. |
<!-- END GENERATED catalog -->

Every skill has test cases. [`docs/INDEX.md`](docs/INDEX.md) repeats this list with the sentence Claude reads to
decide whether to load each skill, and with the number of reference files, scripts and tests inside it.

<p align="center"><img src="docs/assets/demo-tikz-figure.png" alt="An example figure built by the tikz-figures skill: data tiles on both sides of a training scheme" width="100%"></p>
<p align="center"><sub>An example figure from the <code>tikz-figures</code> skill, on seeded synthetic data: built, audited and size-checked by its own scripts.</sub></p>

## What is in a skill

Every skill is one folder with the same five parts. This is `data-figures`:

```text
data-figures/
├── SKILL.md      the rules, each with what it prevents. Claude reads it when the skill loads.
├── references/   six files, one topic each, read only when the task needs them:
│                 style tokens, chart forms, labels and legends, layout, honest encoding, visual checks
├── scripts/      code that Claude runs instead of writing it again:
│                 compose.py places panels at exact millimeters, check_panel.py checks a rendered panel
├── assets/       files that go into your project: figstyle.py, the style module, and a panel template
└── evals/        test cases with graded checks: a benchmark figure, an ablation plot to fix, a scaling plot
```

Claude keeps only a one-paragraph description of each skill in mind. The rules load when a request matches, and
a reference or a script loads when a step needs it. Installing all of them costs little until one is used.

## What is in this repository

```text
scicraft/
├── plugins/
│   ├── scicraft/           the skills for any field
│   └── scicraft-ml/        the skills for machine-learning research
├── docs/
│   ├── INDEX.md            every skill with the sentence that makes Claude load it
│   ├── AUTHORING.md        the contract every skill is written to
│   ├── SHARING.md          how a lab or an organization installs the registry
│   └── CLAUDE.global.md    a working agreement to copy into your own CLAUDE.md
├── tools/                  check.py is the gate; build_index.py writes the overview above from catalog.json
├── install.sh              installs the plugins, or copies single skill folders
└── LICENSE, NOTICE, CITATION.cff, THIRD_PARTY.md
```

## Why it holds up

- **Rules with their reasons.** A skill says what was asked for, what came back, what was thrown out and what
  replaced it. Claude follows a rule better when it knows what the rule prevents, and so does a person.
- **Scripts that have run.** The scripts do the parts that must not vary: compose a figure at true size, audit a
  deck, check every number of a report against its record. Each answers `--help`.
- **Tested.** Every skill has test cases with graded checks, and a gate fails the build on a broken link, a script
  that does not compile, a private string or machine-made prose. See [`tools/check.py`](tools/check.py).
- **Honest by design.** Where a habit of research conflicts with honest reporting, only the honest form is
  taught: state the weak result and its scope.
- **Nothing phones home.** No telemetry, no tracking. The downloads badge comes from GitHub's own count of clones
  and release downloads of this repository. See [`SECURITY.md`](.github/SECURITY.md).

## How it was made

scicraft was distilled from one researcher's year of daily work with Claude Code on papers, talks, posters
and project websites. The sessions were mined for what was asked, what was corrected and why. The result was
then audited against those records, practice by practice, and repaired until more than 99% of the recorded
practices were covered by a skill. A separate pass removed everything private or unpublished. This repository
holds the general part of that set.
The method is itself a skill: [`distill-skills`](plugins/scicraft/skills/distill-skills) turns your own history
into skills like these.

## What comes next

The registry is released in steps, as the work each set comes from is published. The spatial omics set is next:

| Skill | What it does |
|---|---|
| `spatial-omics-data` | Reads and reshapes spatial transcriptomics data at 10^9 molecules. |
| `segmentation-benchmark` | Evaluates cell segmentation so a comparison measures what it claims. |
| `spatial-downstream-analysis` | Keeps a segmentation error from passing as biology downstream. |
| `fast-celltyping` | Types cells by marker genes, for up to a million cells. |
| `tissue-figures` | Builds publication panels of tissue and cells at print size. |

Skills for large-scale pretraining follow after that.

## Cite and credit

If scicraft saves you a round of revisions, please star the repository and cite it. That is how work of this
kind gets counted.

```bibtex
@software{heidari_scicraft_2026,
  author  = {Heidari, Elyas},
  title   = {scicraft: research craft as skills for Claude Code},
  year    = {2026},
  version = {0.1.0},
  url     = {https://github.com/EliHei2/scicraft}
}
```

scicraft is released under the [Apache License 2.0](LICENSE). You may use, change and share it, also in commercial
work. A copy or a derived work must keep the license and the [`NOTICE`](NOTICE) file, which names the author.
Third-party material is listed in [`THIRD_PARTY.md`](THIRD_PARTY.md).

## Contributing

A rule goes in when something happened that the rule would have prevented. Read
[`CONTRIBUTING.md`](.github/CONTRIBUTING.md) and [`docs/AUTHORING.md`](docs/AUTHORING.md), run
`python3 tools/check.py`, and open a pull request.

## Acknowledgments

scicraft was developed during the author's research at the German Cancer Research Center (DKFZ), in the
Gerstung lab and the Stegle lab, which paid for the Claude subscriptions and the compute behind it.

scicraft is a personal project. It is not a product of, and is not endorsed by, any employer or institution of
the author, or by Anthropic.
