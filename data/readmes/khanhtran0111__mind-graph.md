# mind-graph

**Turn any codebase, document folder or research collection into an interactive mind graph, and a
compact project map that AI agents can reuse instead of re-reading everything.**

<p align="center">
  <img src="docs/demo.gif" width="900"
       alt="mind-graph demo: scanning a repo, exploring the graph, a node flagged because its code changed, and the paper-to-code table">
</p>

`mind-graph` is an [Agent Skill](https://docs.claude.com/en/docs/claude-code/skills) for Claude
(and other agents that can run Python). Point it at a repository, a folder of PDFs, Word files and
slide decks, an Obsidian vault, or a mix of all of these. The agent scans the folder cheaply, reads
the parts that matter and writes down what it learned as a structured graph. Three outputs are
built from that graph:

| Output | For | What it is |
|---|---|---|
| `mindgraph.html` | People | A self-contained, offline mind graph you can collapse, search and click through. Each node has a summary, its source locations (file, line, page, slide, sheet), cross-links and a suggested learning path. |
| `MINDGRAPH.md` | Agents | A 2–4k-token outline that a new session reads *instead of* exploring the project again. |
| `mindmap.mmd` | Docs | A Mermaid mindmap you can paste into a README, Notion or a GitHub issue. |

---

## Why

Understanding a new project is expensive, and agents pay that cost again in every session. A
folder of course slides, papers and meeting notes is just as hard to take in. `mind-graph` puts
that work into one artifact that both people and agents can use:

- **Concepts, not folders.** The graph is organized around the ideas a learner needs (for
  example "Data pipeline", "Method", "Decisions"), and each idea links to the exact files, pages
  and slides that back it.
- **Honest about depth.** Every source path is validated, the files actually read are recorded,
  and uncertain areas are marked as open questions.
- **Self-verifying.** Key nodes carry short quotes from their sources as evidence. When the
  code or the documents change, the map tells you *which nodes* no longer hold, not just which
  files changed.
- **Built for research code.** For a repo that implements a paper, every equation, algorithm
  step and hyperparameter is linked to the code that implements it, and each paper/code
  difference is recorded.
- **Cheap to keep current.** Later sessions load `MINDGRAPH.md`, re-read only the flagged
  nodes, and update only the affected branches.

## What it can read

| Kind | Formats | What the scanner extracts |
|---|---|---|
| Code | Python, JS/TS, Java/Kotlin, Go, Rust, C/C++, C#, and more | Entry points, top-level symbols, internal import graph and hub files, external dependencies, git churn |
| Documents | `.md` `.txt` `.rst` `.tex` `.org` `.adoc` `.html` `.epub` `.rtf` | Title, heading outline, lead sentence, word count, links |
| Office | `.docx` `.pptx` `.xlsx` and OpenDocument `.odt` `.odp` `.ods` | Headings and tables, slide titles and speaker notes, sheet names, sizes and header rows |
| PDF | `.pdf` | Page count, bookmarks or detected section headings, title, text by page |
| Data & notebooks | `.csv` `.tsv` `.ipynb` | Columns and row counts, notebook headings and code cells |
| Notes | Markdown vaults, Obsidian | `[[wiki links]]`, relative links, most-linked notes, unlinked notes, docs that point into code |

Images and diagrams are listed so the agent can look at the important ones. Legacy `.doc`,
`.ppt` and `.xls` files are detected, and the scan tells you how to convert them.

## How it works

```
 folder / repo / files
          │
          ▼
 scan_project.py  ── cheap inventory: tree, outlines, symbols, imports, links  →  scan.json
          │
          ▼
 agent reads selectively  ◄── extract_text.py: one document by page / slide / sheet / section
          │
          ▼
 .mindgraph/graph.json   (written by the agent: pillars → topics → leaves, links, learning path)
          │
          ▼
 build_mindgraph.py  ── validate (ids, links, source paths, coverage) and render
          │
          ├─► mindgraph.html
          ├─► MINDGRAPH.md
          └─► mindmap.mmd
```

The scripts handle the mechanical steps: scanning, text extraction, validation and rendering. The
model spends its tokens on understanding the project.

## Installation

Requires **Python 3.9+**. Core features use only the standard library.

Install the skill for Claude Code by copying the `mind-graph/` folder into a skills directory:

```bash
git clone https://github.com/khanhtran0111/mind-graph.git

# available in every project
cp -r mind-graph/mind-graph ~/.claude/skills/mind-graph

# or only in one project
cp -r mind-graph/mind-graph <your-project>/.claude/skills/mind-graph
```

On claude.ai, zip the `mind-graph/` folder and upload it as a custom skill.

**Optional: better PDF support.** The skill uses the first of these that is installed:

```bash
pip install pymupdf      # fastest, best text and bookmarks
pip install pypdf        # pure Python alternative
# or install poppler so that `pdftotext` is on PATH
```

Without any of them, PDFs are still listed. An agent that can read PDFs natively can then open
them directly.

## Usage

### With an agent

Ask in plain language. The skill also triggers when a `.mindgraph/` folder already exists in the
project.

> Help me understand this codebase and draw a mind map of it.

> Summarize everything in `~/Documents/thesis-materials` as a mind graph. There are papers, slides and my notes.

> Tạo sơ đồ tư duy cho các tài liệu trong thư mục này.

The agent scans the folder, reads the important parts, writes `.mindgraph/graph.json`, builds
the outputs and hands you `mindgraph.html`, with a short overview and the first stops of the
learning path.

### Running the scripts yourself

```bash
SKILL=~/.claude/skills/mind-graph

# 1. Inventory a repo, a folder, one file, or several files/folders
python $SKILL/scripts/scan_project.py ./my-folder --out ./my-folder/.mindgraph/scan.json
python $SKILL/scripts/scan_project.py paper.pdf slides/ notes/ --exclude 'archive/*'

# 2. Read one document a piece at a time
python $SKILL/scripts/extract_text.py report.pdf --outline
python $SKILL/scripts/extract_text.py report.pdf --units 3-5
python $SKILL/scripts/extract_text.py lecture.pptx --section "Markov"
python $SKILL/scripts/extract_text.py results.xlsx --grep "baseline"

# 3. Validate graph.json and render the outputs
python $SKILL/scripts/build_mindgraph.py ./my-folder/.mindgraph/graph.json
python $SKILL/scripts/build_mindgraph.py ./my-folder/.mindgraph/graph.json --check   # validate only
```

The scan summary opens with a **mode** (`CODE`, `DOCUMENTS` or `MIXED`) and shapes its report to
match. A code scan shows entry points and hub files. A document scan groups files by folder and
shows outlines, lead sentences, word counts and links between notes.

## The graph format

`graph.json` is a tree with cross-links. A minimal example:

```json
{
  "meta": { "title": "RL course", "language": "en", "scope": "All files. Skipped: old drafts/." },
  "root": {
    "id": "root", "label": "RL course", "kind": "root",
    "summary": "Course materials on reinforcement learning for robot manipulation.",
    "children": [
      {
        "id": "methods", "label": "Methods", "kind": "concept", "importance": 3,
        "summary": "Policy-gradient and value-based algorithms, and when each is used.",
        "children": [
          {
            "id": "methods.ppo", "label": "PPO", "kind": "doc",
            "summary": "Clips the policy ratio so that each update stays small and stable.",
            "sources": [
              { "path": "papers/ppo.pdf", "page": 4, "section": "§3 Clipped objective" },
              { "path": "slides/lecture5.pptx", "slide": "8-12" }
            ]
          }
        ]
      }
    ]
  },
  "links": [{ "from": "methods.ppo", "to": "code.train", "type": "implements" }],
  "learning_path": [{ "node": "methods", "note": "Every later topic builds on these algorithms." }]
}
```

Node kinds: `concept`, `module`, `file`, `symbol`, `doc`, `data`, `external`, `question`.
Link types: `depends_on`, `calls`, `data_flow`, `explains`, `implements`, `configures`,
`contrasts`, `related`. Sources can point at `lines`, `page`, `slide`, `sheet` or `section`. In
the viewer, local PDFs open at the cited page.

The full specification, quality rules and patterns for each project type (applications, ML
research, libraries, papers, course materials, note vaults, office document folders, meeting
notes, data collections) are in
[`mind-graph/references/graph_schema.md`](mind-graph/references/graph_schema.md).

## Validation

`build_mindgraph.py` refuses to write outputs while errors remain, and it prints warnings for
quality problems:

- duplicate or missing ids, links and learning-path stops that point to nonexistent nodes
- `sources` paths that do not exist: the graph may only cite what is really there
- malformed page and slide locators, and `sources_read` entries that do not exist
- shape problems: too many pillars, nodes with more than 12 children, overly long labels or summaries
- **coverage**: for document folders, which scanned documents no node references and
  `meta.scope` does not list as skipped
- **evidence**: quotes that can't be found in the file they cite (see below)

## Node-level evidence: knowing which parts of the map still hold

Most project maps go stale silently. `mind-graph` lets each important node prove its claim with
a short quote copied verbatim from its source:

```json
{
  "id": "policy.act", "label": "ACT policy",
  "summary": "Predicts a chunk of future actions per step instead of one action.",
  "evidence": [
    { "path": "src/policy/act.py", "quote": "class ACTPolicy(nn.Module):" },
    { "path": "papers/act.pdf", "quote": "predicts a chunk of k future actions" }
  ]
}
```

On the first build, every quote must be found in its file (code, Markdown, PDF, Word,
PowerPoint, Excel, …), so the agent cannot cite something it didn't read. The build then stores
a hash of the text *around* each quote. Every later build or scan compares against it:

| Status | Meaning | What to do |
|---|---|---|
| ✓ ok | Quote found and the text around it is unchanged. Moving it within the file is fine. | Trust the node without re-reading. |
| ⚠ changed | Quote found, but the code or text next to it was edited. | Re-read. If the node is still right, run `build --accept <id>`; otherwise edit it. |
| ⚠ stale | Quote gone, or the file was deleted. | Rewrite the node or remove it. |

Flags appear as red and amber dots in the viewer, with a ring on collapsed branches that hide a
flag. They also appear in a "Needs re-check" list at the top of `MINDGRAPH.md` and in the
`--since-graph` scan. Matching ignores whitespace, line breaks and quote or dash variants, and
falls back to letters-and-digits matching for PDF hyphenation. A plain rebuild never clears a
flag. Only editing the node (which re-verifies it) or `--accept` does.

## Paper ↔ code: mapping a paper onto its implementation

Reproducing a paper means checking, line by line, that the code does what the paper says. For
research repositories, `mind-graph` maps every section, equation, algorithm step and
hyperparameter of the paper to the code that implements it, and records each place where the two
disagree.

```bash
python $SKILL/scripts/paper_code.py paper/ppo.pdf --code .     # also: main.tex or an arXiv source folder
```

```
## Hyperparameters: paper vs code (≠ rows are deviation candidates)
- ≠   hp:clip: paper 0.2 (page 3: “Clipping parameter ε 0.2”) | code 0.1 configs/default.yaml:1
- ≠   hp:learning_rate: paper 0.0003 (page 3: “Adam stepsize 3 × 10−4”) | code 0.00025 ppo/train.py:24
- =   hp:gamma: paper 0.99 (page 3: “discount factor γ = 0.99”) | code 0.99 ppo/train.py:25

## Equations (4)
- eq:2 (page 2): L^CLIP(θ) = E_t[ min( r_t(θ) Â_t , clip(r_t(θ), 1−ε, 1+ε) Â_t ) ]
    cited in code: ppo/loss.py:11
    → ppo/loss.py:10-15 clipped_surrogate_loss() [cites it]
```

The script works from PDF or LaTeX. It extracts the paper's numbered equations, algorithms
(with their steps), tables and stated hyperparameters. It compares each hyperparameter with
same-named settings in code, configs and scripts. It also finds code comments that cite the
paper and ranks candidate functions for each equation.

The agent reads the candidates and writes what it confirms into the graph:

- **Paper nodes** carry a `paper_ref` such as `"Eq. 2"`, `"Alg. 1 L4"`, `"§3.2"` or `"hp:clip"`.
- **Code nodes** link to them with `implements` and a `fidelity`: `exact`, `approx`, `partial`
  or `deviates`.
- **Deviations** become `question` nodes that record what the paper says, what the code does
  and the likely impact. Examples are a different coefficient, a missing step, a changed formula
  or a trick that exists only in the code.

The build turns this into a **Paper ↔ Code** table in the viewer and in `MINDGRAPH.md`:

| Paper | Concept | Code | Status |
|---|---|---|---|
| Eq. 1 | Probability ratio | `probability_ratio()` (ppo/loss.py:5-7) | ✓ exact |
| Eq. 2 | Clipped objective | `clipped_surrogate_loss()` (ppo/loss.py:10-15) | ⚠ deviates — Clip ε 0.1 not 0.2 |
| Eq. 4 | Value loss | — | ∅ not in code |
| Alg. 1 | Algorithm 1 | `train()` (ppo/train.py:6-15) | ◐ partial |

The build also warns about equations and algorithms that no node maps yet, and about
hyperparameter differences that no deviation node explains. Combined with node evidence, a later
session can see when a code change breaks a mapping.

## Comparing versions: what changed, conceptually

A line diff of a large PR shows what changed in the files. A graph diff shows what changed in
the design: which concepts appeared or disappeared, which components moved, and which
relationships changed.

```bash
# review a PR: graph on main vs graph on the branch
python $SKILL/scripts/build_mindgraph.py --diff main:.mindgraph/graph.json .mindgraph/graph.json

# follow a library across releases
python $SKILL/scripts/build_mindgraph.py --diff graphs/v0.1.json graphs/v0.2.json
```

```
Diff main:.mindgraph/graph.json → .mindgraph/graph.json: +1 added · −1 removed · ~3 changed · ↷1 moved nodes; links +1 −1 ~1
  Implementation: 1 added, 2 changed
  Paper vs code: 1 moved, 1 removed
```

This writes two files:

- `mindgraph_diff.html`: the usual viewer with branches that contain changes expanded and the
  rest collapsed.
  - Nodes: added are green (+), removed are red and struck through, changed are amber (~, with
    the old summary in the side panel), and moved are blue (↷).
  - Cross-links are coloured the same way.
  - A **Changes** tab lists everything, grouped by type.
- `DIFF.md`: a Markdown summary for the PR description. It covers the areas most changed, the
  added, removed, changed and moved nodes, relationship changes (including an `implements` link
  whose fidelity went from `approx` to `deviates`), and learning-path and glossary edits.

Nodes are matched by id, so keep ids stable when you update a graph. A node whose id changed but
whose label didn't is reported as "id renamed".

## Keeping it up to date

```bash
python $SKILL/scripts/scan_project.py . --since-graph
python $SKILL/scripts/build_mindgraph.py .mindgraph/graph.json --check             # evidence status, writes nothing
python $SKILL/scripts/build_mindgraph.py .mindgraph/graph.json --accept policy.act # re-baseline after re-reading
```

The scan lists the files that changed since the graph was built and the nodes whose evidence is
now changed or stale. Git repositories use the recorded commit; other folders use file
modification times. The agent re-reads only the flagged nodes, updates them, and keeps node ids
stable, so links and the learning path still work.

To make future sessions start from the map, add this line to your `CLAUDE.md` or `AGENTS.md`:

```
Project map: read .mindgraph/MINDGRAPH.md before exploring; it lists pillars, key files and links.
```

## Repository layout

```
mind-graph/
├── SKILL.md                    # instructions the agent follows
├── scripts/
│   ├── scan_project.py         # inventory of a repo / folder / file set
│   ├── extract_text.py         # read a document by page, slide, sheet or section
│   ├── doc_formats.py          # format extractors (standard library only)
│   ├── evidence.py             # verify node evidence quotes; flag changed / stale nodes
│   ├── paper_code.py           # research repos: paper inventory, hyperparameter diff, code candidates
│   ├── paper_graph.py          # paper ↔ code table, validation and coverage (used by the build)
│   ├── graph_diff.py           # conceptual diff between two graphs (build --diff)
│   └── build_mindgraph.py      # validate graph.json, render HTML / Markdown / Mermaid
├── assets/viewer.html          # interactive viewer template, no external dependencies
└── references/graph_schema.md  # graph.json format, quality rules, patterns by project type
```

## Limitations

- Scanned (image-only) PDFs have no text layer. They are flagged, and you need OCR or a model
  that can read page images.
- Legacy binary formats (`.doc`, `.ppt`, `.xls`) must be converted first, for example with
  `soffice --headless --convert-to docx FILE`.
- PDF headings come from bookmarks when they exist and from a heuristic otherwise. Unusual
  layouts can produce a partial outline. Multi-column text is extracted in reading order.
- Local source links work as long as `mindgraph.html` stays in `.mindgraph/` next to the files.
  Set `meta.repo_url` to link to a code host instead.
- The graph is only as good as what was read. `meta.sources_read` and the coverage report show
  how deep the map goes.
