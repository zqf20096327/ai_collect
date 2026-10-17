# SciTeX Automated Research Demo

Demonstration of AI-driven autonomous research workflow: from synthetic data generation to peer-reviewed manuscript.

[![Video Demo](docs/scitex-automated-research-demo-thumbnail.png)](https://scitex.ai/media/videos/scitex-automated-research-demo.mp4)
*Click to watch video demo*

## Demo: Sleep-Cognition Study

<table>
<tr>
<td align="center" width="50%">
<strong>Manuscript</strong><br>
<a href="scitex/writer/paper/01_manuscript/manuscript.pdf"><img src="docs/manuscript_page1-01.png" width="400" alt="Manuscript"/></a>
</td>
<td align="center" width="50%">
<strong>Revision Response</strong><br>
<a href="scitex/writer/paper/03_revision/revision.pdf"><img src="docs/revision_page1-1.png" width="400" alt="Revision"/></a>
</td>
</tr>
</table>

**Title:** Age-Dependent Effects of Sleep Quality on Cognitive Performance

**Design:** 3×3 factorial (Age × Sleep Quality), N=180

**Key Finding:** Older adults show disproportionate memory vulnerability to poor sleep (interaction p<.001)

## Pipeline

```
1. Data Generation    → scripts/01_generate_data.py
2. Statistical Analysis → scripts/02_statistical_analysis.py
3. Figure Creation    → scripts/03_create_figures.py
4. Table Creation     → scripts/04_create_tables.py
5. Manuscript Writing → scitex/writer/paper/01_manuscript/
6. Peer Review Sim    → scitex/writer/paper/03_revision/
```

## Outputs

| Output | Path |
|--------|------|
| Synthetic Data | `data/sleep_cognition_data.csv` |
| Figures (4) | `scitex/writer/paper/01_manuscript/contents/figures/` |
| Tables (4) | `scitex/writer/paper/01_manuscript/contents/tables/` |
| Manuscript PDF | `scitex/writer/paper/01_manuscript/manuscript.pdf` |
| Revision PDF | `scitex/writer/paper/03_revision/revision.pdf` |

## Quick Start

```bash
# Run analysis pipeline
python scripts/01_generate_data.py
python scripts/02_statistical_analysis.py
python scripts/03_create_figures.py
python scripts/04_create_tables.py

# Compile manuscript
cd scitex/writer/paper
env -u BASH_ENV /bin/bash -c './compile.sh manuscript --draft --quiet'
env -u BASH_ENV /bin/bash -c './compile.sh revision --draft --quiet'
```

## Tools Used

- **scitex**: Research framework with session management
- **scitex-writer**: LaTeX manuscript compilation
- **crossref-local**: Reference retrieval via MCP
- **Claude Code**: AI agent orchestration

## Structure

```
auto_research/
├── scripts/                    # Analysis pipeline
├── data/                       # Generated data
├── scitex/
│   └── writer/paper/
│       ├── 01_manuscript/      # Main paper
│       ├── 02_supplementary/   # Supplementary materials
│       └── 03_revision/        # Peer review response
└── README.md
```

---

<p align="center">
  <a href="https://scitex.ai" target="_blank"><img src="docs/scitex-icon-navy-inverted.png" alt="SciTeX" width="40"/></a>
  <br>
  AGPL-3.0
</p>
