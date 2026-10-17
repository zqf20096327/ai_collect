<p align="center">
  <img src="assets/readme-hero.svg" alt="Post-Training of Large Language Models — Alignment, Reasoning, and Agency" width="100%">
</p>

<p align="center">
  <a href="https://github.com/2218342221/llm-post-training-book/actions/workflows/pages.yml"><img src="https://github.com/2218342221/llm-post-training-book/actions/workflows/pages.yml/badge.svg" alt="GitHub Pages"></a>
  <a href="https://github.com/2218342221/llm-post-training-book/stargazers"><img src="https://img.shields.io/github/stars/2218342221/llm-post-training-book?style=flat&logo=github&label=Stars" alt="GitHub stars"></a>
  <a href="https://github.com/2218342221/llm-post-training-book/commits/main"><img src="https://img.shields.io/github/last-commit/2218342221/llm-post-training-book?label=Updated" alt="Last commit"></a>
  <img src="https://img.shields.io/badge/chapters-26-185b43" alt="26 chapters">
  <img src="https://img.shields.io/badge/references-770-185b43" alt="770 references">
</p>

<p align="center">
  <strong>A mechanism-first graduate textbook on modern LLM post-training.</strong><br>
  From SFT, RLHF, and DPO to reasoning RL, tool use, agentic training, systems, evaluation, and safety.<br>
  一本系统讲解大语言模型后训练的双语研究生教材。
</p>

<p align="center">
  <a href="https://2218342221.github.io/llm-post-training-book/post-training-en.pdf"><strong>Read the English edition</strong></a>
  &nbsp;·&nbsp;
  <a href="https://2218342221.github.io/llm-post-training-book/post-training-zh.pdf"><strong>阅读中文版</strong></a>
  &nbsp;·&nbsp;
  <a href="https://2218342221.github.io/llm-post-training-book/"><strong>Book website</strong></a>
</p>

> If this book helps your study, teaching, or research, please consider
> [starring the repository](https://github.com/2218342221/llm-post-training-book). It helps more readers discover the project.

## Why this book?

Most resources explain post-training as a list of algorithms. This book instead
starts from the statistical problem each method is trying to solve, derives the
objective, and then examines where its assumptions break.

- **One coherent path from alignment to agency.** The material connects SFT,
  reward modeling, policy gradients, DPO, RLVR, GRPO-family methods, tool RL,
  long-horizon agents, training systems, evaluation, and safety.
- **Mechanism before leaderboard claims.** Chapters explain the estimator,
  source of bias, optimization pathology, and engineering trade-off behind each
  method—not just whether a paper reports an improvement.
- **Evidence-aware presentation.** Empirical claims are attributed; replicated,
  contested, and single-paper findings are distinguished rather than flattened
  into one confident narrative.
- **English and Chinese editions stay synchronized.** Both editions share
  notation, equation numbers, theorem numbers, references, and structure.
- **Built for learning and implementation.** Derivations, algorithms, compact
  PyTorch-style listings, pitfalls, further reading, and exercises appear
  throughout the book.

<details>
<summary><strong>中文简介</strong></summary>

本书不是算法名词的罗列，而是沿着“问题、假设、目标函数、估计方法、失效条件与工程权衡”逐层展开。
内容从监督微调、奖励模型、RLHF 与 DPO 出发，延伸到 RLVR、GRPO 系列方法、推理时计算、
工具调用、长程智能体、多智能体训练、系统效率、评测与安全。

中英文版本共享章节结构、符号体系、公式编号、定理编号和参考文献，适合研究生课程、自学、
科研入门以及工程实践。若本书对你有帮助，欢迎 Star、分享，或通过 Issue 提交技术错误、
引用遗漏和翻译建议。

</details>

## At a glance

| | English | 简体中文 |
| --- | ---: | ---: |
| Read | [Download PDF](https://2218342221.github.io/llm-post-training-book/post-training-en.pdf) | [下载 PDF](https://2218342221.github.io/llm-post-training-book/post-training-zh.pdf) |
| Length | 802 pages | 791 页 |
| Source | [`book/`](book/) | [`zh/`](zh/) |

| Coverage | Count |
| --- | ---: |
| Main chapters | 26 |
| Mathematical and implementation appendices | 4 |
| Bibliography entries | 770 |
| Literature cutoff | 31 July 2026 |

## What is inside

| Part | Topics |
| --- | --- |
| **I · Foundations** | Post-training paradigms, mathematical preliminaries, supervised fine-tuning, and data |
| **II · Alignment from feedback** | Reward models, policy gradients, RLHF, DPO and its descendants, online and game-theoretic alignment |
| **III · Reasoning** | Test-time compute, RLVR, GRPO/DAPO/GSPO/CISPO, credit assignment, process supervision, and non-verifiable rewards |
| **IV · Agency** | Tool-integrated RL, long-horizon training, environments, sandboxes, multi-agent training, and self-play |
| **V · Systems** | Training at scale, train–inference mismatch, efficiency, and cost control |
| **VI · Measurement, safety, and frontiers** | Evaluation, safety alignment, robustness, and open problems |
| **Appendices** | Mathematical background, extended derivations, reference implementations, and glossary |

### Suggested reading paths

- **New to post-training:** Parts I → II → Chapter 10 → Chapter 11.
- **Working on reasoning RL:** Chapters 6 → 10–15 → 22–24.
- **Building agents:** Chapters 16–20 → 22–25.
- **Looking for implementation details:** Chapters 7, 12, 17, and
  [Appendix C](book/appendix/appC_implementation.tex).

## Read, share, and contribute

- **Read:** use the hosted [English](https://2218342221.github.io/llm-post-training-book/post-training-en.pdf)
  or [Chinese](https://2218342221.github.io/llm-post-training-book/post-training-zh.pdf)
  PDF.
- **Share:** link to the [book website](https://2218342221.github.io/llm-post-training-book/)
  so readers always receive the current edition.
- **Report an issue:** open a
  [GitHub issue](https://github.com/2218342221/llm-post-training-book/issues/new)
  for technical errors, missing citations, unclear derivations, or translation
  problems.
- **Contribute:** read [AUTHORING.md](AUTHORING.md) for chapter conventions and
  [TRANSLATION.md](TRANSLATION.md) for Chinese terminology and style.

When reporting a book error, please include the edition, page or chapter,
the current text, and your proposed correction. Focused pull requests are welcome.

<details>
<summary><strong>Build from source</strong></summary>

```bash
./build.sh          # both editions
./build.sh en       # English only (pdflatex)
./build.sh zh       # Chinese only (xelatex)
./build.sh en quick # single pass for fast error checking
```

Requirements: TeX Live with `tcolorbox`, `algpseudocode`, `pgfplots`, `natbib`,
`cleveref`, and `titlesec`; the Chinese edition additionally requires `ctex`,
`xeCJK`, and the Noto Serif/Sans CJK SC fonts.

The build first runs `merge_bib.py`, combining `book/refs_base.bib` with the
per-chapter fragments in `bib/`, removing duplicate entries and normalizing
citation keys that share an arXiv identifier.

</details>

<details>
<summary><strong>Repository layout</strong></summary>

```text
book/          English edition and shared style/macros
zh/            Simplified Chinese edition
bib/           Per-chapter BibTeX fragments
research/      Source notes for recent literature
build/         Compiled English and Chinese PDFs
site/          GitHub Pages landing page
AUTHORING.md   Chapter-writing conventions
TRANSLATION.md Chinese translation conventions
```

</details>

## Editorial standard

Notation is defined once in `book/macros.tex` and the front-matter notation
table. Callout boxes distinguish key ideas, derivations, engineering practice,
pitfalls, and historical context. Benchmark numbers are attributed to sources;
where the literature disagrees, the disagreement is reported.

The field moves quickly. Treat the objectives, estimators, assumptions, and
failure modes as the durable material, and re-check moving-target claims against
the latest literature.

---

<p align="center">
  <strong>Useful? <a href="https://github.com/2218342221/llm-post-training-book">Give the project a star</a> and share it with another reader.</strong>
</p>
