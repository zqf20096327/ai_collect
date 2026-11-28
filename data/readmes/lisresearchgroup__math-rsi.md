<div align="center">

# <picture><source media="(prefers-color-scheme: dark)" srcset="figures/mathrsi/branding/mark-c-dark.png"><img src="figures/mathrsi/branding/mark-c-light.png" width="76" height="38" align="middle" alt=""></picture> MathRSI<br><sub><sup><em>SII MathRSI Team</em></sup></sub>

**A self-improving agent harness for mathematical discovery and proof.**<br>Readable Markdown skills and domain verifiers for Claude Code and Codex.

[![Website / EN + 中文](figures/mathrsi/badges/visual-tour.svg)](https://lisresearchgroup.github.io/math-rsi/ "Website / EN + 中文")&nbsp; [![Quick Start / Start here](figures/mathrsi/badges/quick-start.svg)](#quick-start)&nbsp; [![Results / 7 cases](figures/mathrsi/badges/results.svg)](case-studies/README.md)&nbsp; [![Agent Guide / Workflow + wiki](figures/mathrsi/badges/agent-guide.svg)](docs/WORKFLOWS.md)&nbsp; [![Contributors / Team](figures/mathrsi/badges/contributors.svg)](#contributors)&nbsp; [![CN / 中文](figures/mathrsi/badges/lang-cn.svg)](README.zh-CN.md)

</div>

MathRSI pairs a shared base workflow with domain plugins and a per-problem research wiki, guiding Claude Code and Codex from literature survey and route selection through proof development, review, verification, and handoff. Validated results and diagnosed failures feed back to refine both the workflow and plugins.

[![Historical MathRSI v0 through v6 homepage evolution](figures/mathrsi/media/evolution.gif?v=6-q7-20261120)](figures/mathrsi/media/evolution.mp4?v=6-q7-20261120)

*Historical v0 → v6 homepage replay; “Current” in the recording refers to v6 at that time. Click for MP4; [interactive homepage](https://lisresearchgroup.github.io/math-rsi/) · [seven case studies and verification status](case-studies/README.md).*

**43-bit code research replay**

[![MathRSI workbench overview](figures/mathrsi/media/workbench-en.webp)](figures/mathrsi/media/workbench-en.mp4)

*Explore the [interactive workbench](https://lisresearchgroup.github.io/math-rsi/workbench/index.html?lang=en#wb-demo) · [watch the English MP4](figures/mathrsi/media/workbench-en.mp4). Three research roles retrace the completed proof using its archived generator matrix and rejection witnesses.*

<a id="news"></a>

## 📢 News

[November 2026 mathematical results](https://lisresearchgroup.github.io/math-rsi/november-2026.html)


- **Alon–Jaeger–Tarsi (AJT) preprint** · 2026-11-27 — SII MathRSI Team proves the AJT theorem for every invertible n × n matrix over every prime field Fₚ with p ≥ 5 and n ≤ 11, with Lean formalization. Over F₅, this extends the cited n ≤ 9 result to dimensions 10 and 11. Over F₅, the general 12-dimensional case remains open, while symmetric 12 × 12 matrices are covered. [Preprint (PDF)](case-studies/ajt/paper.pdf) · [Case & Lean source](case-studies/ajt/README.md) · [Discussion](https://github.com/lisresearchgroup/math-rsi/pull/67)
- **[v8](https://github.com/lisresearchgroup/math-rsi/releases/tag/v8)** · 2026-11-23 — Download binary linear codes for 18 improved lower bounds. On the upper-bound side, 32 new deductions settle nine optimal distances. Two further entries await final acceptance in the source project.
- **[v7](https://github.com/lisresearchgroup/math-rsi/releases/tag/v7)** · 2026-11-22 — The working proof now extends every matching in the seven-dimensional cube to a Hamilton cycle. The Happy Ending manuscripts give ES(8) ≤ 294, ES(9) ≤ 1,100 and ES(10) ≤ 3,980.
- **[v6](https://github.com/lisresearchgroup/math-rsi/releases/tag/v6)** · 2026-11-20 — The Q₇ matching threshold fell from 57 edges to 56. For square-free subgraphs of Q₈, the maximum number of edges was narrowed to 682 or 683.

<details>
<summary>Earlier versions (v1–v5)</summary>

- **[v5](https://github.com/lisresearchgroup/math-rsi/releases/tag/v5)** · 2026-11-14 — In Q₇, every matching with at least 57 edges was shown to extend to a Hamilton cycle. The proof showed how to reuse a theorem by choosing a different representation of the same matching.
- **[v4](https://github.com/lisresearchgroup/math-rsi/releases/tag/v4)** · 2026-11-08 — Convex polygon proofs taught the workflow to trace which inequalities must be tight together. The degree–diameter plugin gained methods for constructing larger graphs.
- **[v3](https://github.com/lisresearchgroup/math-rsi/tree/v3)** · 2026-11-04 — Three new plugins brought MathRSI to six domains, adding square-free subgraphs of cubes, matching extension in cubes, and convex polygons.
- **[v2](https://github.com/lisresearchgroup/math-rsi/tree/v2)** · 2026-11-03 — The degree–diameter plugin joined MathRSI. It was the first plugin used to test a new maintenance workflow for turning research findings into changes to the shared base.
- **[v1](https://github.com/lisresearchgroup/math-rsi/tree/v1)** · 2026-11-03 — Property B and coding theory supplied the first shared workflow, from defining a problem and exploring proof routes to checking and handing off a proof.

</details>


<a id="quick-start"></a>

## 1. 🚀 Quick Start

**Launch the mathematics workbench.** With Git, Python 3.10+, [pipx](https://pipx.pypa.io/stable/installation/) and a signed-in agent CLI, run this in your terminal:

```sh
git clone --depth 1 https://github.com/lisresearchgroup/math-rsi.git
pipx install "git+https://github.com/wanshuiyin/SuperARIS.git"
mathrsi
```

Choose your problem directory in the wizard. For the MathRSI repository, select the `math-rsi` folder you cloned, then choose your team and models. Next time, just run `mathrsi`.

**Use Claude Code or Codex directly.** Open the cloned `math-rsi` folder in your client and grant it access to your problem directory. In Claude Code, enter `/mathrsi-research Study the problem in ../my-problem/problem.md`. In Codex, use `$mathrsi-research` with the same request.

**Add an independent reviewer (optional).** For example, Claude Code can ask Codex to review a proof via MCP. [Connect a reviewer](docs/REVIEWER_MCP.md) · [Setup, proof checks and resuming a study](docs/QUICKSTART.md)

<a id="six-mathematical-frontiers"></a>

## 2. 🧮 Mathematical Results

Seven mathematical case studies supply results and reusable methods across six domain plugins. AJT draws on methods from the ECC plugin. [Public homepage](https://lisresearchgroup.github.io/math-rsi/) · [Local viewing instructions](docs/HOMEPAGE.md). The **[bilingual visual tour](https://lisresearchgroup.github.io/math-rsi/)** shows their problems, results and evolution; the **[seven-case index](case-studies/README.md)** links proofs, verification scopes and runnable tools.

[![Historical six-case mathematical results overview](figures/mathrsi/results-overview/results-overview.en.svg?v=8-ecc)](case-studies/README.md)

*The figure shows the six earlier cases. AJT appears in the list below.*

- **Property B:** bounds for $k=5,\ldots,12$ and exponentially growing additive gains for every $k\ge12$. [Results & proof scope](case-studies/property-b/README.md)
- **Error-correcting codes.** Download generators for 18 improved lower bounds. Of 37 supported upper-bound updates, 13 meet the distance of a known code and settle the optimum. Two further entries await final acceptance in the source project. [Codes and matrices](https://lisresearchgroup.github.io/math-rsi/ecc-intervals.html#lower) · [Upper bounds and proofs](https://lisresearchgroup.github.io/math-rsi/ecc-intervals.html#upper)
- **Degree–diameter:** our constructions reach 2,567 vertices at $(10,4)$, 37,632 at $(11,5)$, 42,433 at $(12,5)$ and 16,416 at $(16,4)$. [Constructions, dated comparisons & scope](case-studies/degree-diameter/README.md)
- **Erdős Problem 86:** a square-free subgraph of $Q_7$ has [at most 304 edges, and the bound is attained](https://arxiv.org/abs/2611.27284), $682\le\mathrm{ex}(Q_8,C_4)\le683$, and asymptotic density improved from $0.60318$ to $\le0.5912405943$ (`T3`) / $\le0.5912405942$ (`T4`). [Results & verification scope](case-studies/erdos-86/README.md)
- **Ruskey–Savage:** a complete author working proof covers every matching in $Q_7$, including empty and perfect matchings; the universal $Q_6$ result is retained. External peer review pending; no Lean. [Proof, local checks & release history](case-studies/ruskey-savage-q7/README.md)
- **Happy Ending & $N(m,r,s)$:** new same-input sector-deficit manuscripts give working planar corollaries $\mathrm{ES}(7)\le77$, $\mathrm{ES}(8)\le294$, $\mathrm{ES}(9)\le1100$ and $\mathrm{ES}(10)\le3980$; independent mathematical review remains incomplete. Earlier replayable finite certificates retain their separate scope and provenance. [Current results, evidence & replay](plugins/happy-ending/archive/nmrs-20261120/HANDOFF.md) · [Case guide](case-studies/happy-ending/README.md)
- **Alon–Jaeger–Tarsi (AJT):** Lean proofs cover every invertible matrix over prime fields $\mathbb F_p$ with $p\ge5$ in dimensions $n\le11$, extending the cited $\mathbb F_5$ result to dimensions 10 and 11. The general 12-dimensional case over $\mathbb F_5$ remains open. [Case & Lean source](case-studies/ajt/README.md) · [Preprint (PDF)](case-studies/ajt/paper.pdf)

<a id="three-layers"></a>

## 3. 🧩 Three Layers

![MathRSI: the base workflow calls domain methods and reads, updates and reuses each task workspace; separate maintenance improves the base and plugins](figures/mathrsi/architecture-three-layers.svg)

**Base** (`base/`) supplies general research logic. **Domain plugins** (`plugins/`) supply specialized mathematics and checkers. **Task workspaces** hold each problem's specification, wiki, proofs, certificates and recovery state. [Architecture & plugin contract](docs/PLUGIN_CONTRACT.md) · [Editable source & GPT Image variant](figures/mathrsi/README.md)

<a id="how-research-runs"></a>

## 4. 🔬 How Research Runs

The main [`mathrsi-research`](base/skills/mathrsi-research/SKILL.md) skill coordinates **Prepare → Route → Prove → Verify → Handoff**, entering from current evidence and reading each returned artifact. The task wiki is read, updated and reused throughout; scoped collaborators and cross-model reviewers support the work.

| What you need | Start here |
| --- | --- |
| Formulate a new question and investigate the literature | [Prepare](base/skills/mathrsi-prepare/SKILL.md) |
| Resume research or an unfinished proof | [Route iteration](base/skills/mathrsi-route-loop/SKILL.md) · [Proof construction](base/skills/mathrsi-prove/SKILL.md) |
| Check and repair a candidate proof or certificate | [Verify](base/skills/mathrsi-verify/SKILL.md) · [Proof-repair example](examples/proof-repair/README.md) |
| Deliver established results and make them reusable | [Handoff](base/skills/mathrsi-handoff/SKILL.md) |

[Detailed workflow & return paths](docs/WORKFLOWS.md) · [Six-domain routing](docs/DOMAIN_ROUTING.md) · [Workspace & memory](docs/WORKSPACE.md)

<a id="research-improves-the-workflow"></a>

## 5. 🔄 Research Improves the Workflow

![Research evidence feeds separate maintenance, which improves shared base behavior and domain methods](figures/mathrsi/research-to-capabilities.svg)

Two tracks evolve together: **shared base behavior** becomes stronger, while **domain plugins** expand and deepen. Separate [`mathrsi-meta-evolve`](base/skills/mathrsi-meta-evolve/SKILL.md) maintenance turns research evidence into implemented changes.

- **v8 base and ECC plugin.** Carry a construction through to the exact parameters being reported, keep the strongest witness for each setting, and test rarely reached rejection rules on inputs that should fail. The ECC plugin exports all 18 generator matrices and links every upper-bound deduction to its premises. [Methods and examples](docs/V8_CHANGES.md)

- **v6 base:** test candidate case splits on the hardest open branch before adopting them, and measure net-new coverage on the same input; run primal–dual coevolution that keeps the proof goal separate from the search target, rotates four normalized signed residual channels, and tests candidate cuts against the full graph archive; stop floating-point SDP/CP loops once gains fall to the rounding-repair residual.
- **Deeper domain plugins:** `hypercube-extremal` adds asymptotic COP + $m=1024$ degree-potential bounds (`T3` / `T4`), same-subgraph 3-measure pullbacks ($Q_8 \le 683$), $Q_7$ 304 constructions + source report, and the reusable `cube_coevolve` engine; `hypercube-hamilton` completes $Q_7$ E16 ($\ge 56$ edges across all $\mu=0..4$) with parameterized $Q_6$ $\Delta=2$ double bridges, $Q_6$ $A_8$, and $S_6$ large-face tables paired with symbolic small-face holes; `happy-ending` adds cross-platform checkers and curated archives for $m=7,8,9$ signotope capacities ($N(8,6,6)\le 61$ shared-label CEGAR, $N(9,8,8)\le 688$ & $D_9\le 458$ generative sparse integer duals, and relaxation-ceiling stopping; developed with **Trellis + ARIS + v3**, integrated in `main` maintenance; fixed `v6` tag unchanged).
- **Q₇ follow-up · 2026-11-20:** `main` absorbs the full R7 author working proof accepted in the source project on 19 November. The research used v3 with local adaptations; fixed v5 (≥57 edges) and v6 (≥56 edges) snapshots remain unchanged. [Proof guide](https://github.com/lisresearchgroup/math-rsi/blob/main/plugins/hypercube-hamilton/knowledge/q7-closure-proof.md) · [Recomputation scope](https://github.com/lisresearchgroup/math-rsi/blob/main/plugins/hypercube-hamilton/archive/q7-closure/README.md)
- **Inherited behavior:** v5's controlled auxiliary choices, cross-representation theorem reuse and consuming returned results before dispatching new work, together with v4's equality-to-witness steps, global progress checks and ECC branch reuse.

**[MathRSI v8 is the latest release](https://github.com/lisresearchgroup/math-rsi/releases/tag/v8).** [Release notes](docs/V8_CHANGES.md) · [Download v8](https://github.com/lisresearchgroup/math-rsi/archive/refs/tags/v8.zip) · [Download main](https://github.com/lisresearchgroup/math-rsi/archive/refs/heads/main.zip) · [Evolution records](development/README.md) · [Maintenance guide](docs/EVOLUTION_WORKFLOW.md)

v0 records the Property B and coding research that preceded the shared workflow. Version tags begin at v1. [Version news](#news) · [Historical architecture diagrams](figures/mathrsi/README.md#historical-diagrams)

<a id="documentation--provenance"></a>

## 6. 📚 Documentation

**[Choose a reading path](docs/README.md)** · [Seven research cases](case-studies/README.md) · [Repository map](docs/README.md#repository-map) · [Validation records](development/README.md#validation-and-implementation) · [Skill acceptance](docs/SKILL_ACCEPTANCE.md) · [Contributing](CONTRIBUTING.md)

Built on **[ARIS](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)** and the research artifacts preserved in the plugins and cases. The bundled ARIS snapshot is `c485faa59a68e51c6575dea67ca57abc7a6a2b9c`. [Provenance](docs/PROVENANCE.md) · [Snapshot manifest](base/ARIS_SNAPSHOT.json) · [Bridge sources](mcp-servers/SOURCE.md)

Workflow and scripts are **[MIT licensed](LICENSE)**. Archived papers and third-party materials retain their original copyrights.

<a id="contributors"></a>

## 7. 👥 Contributors

### Core Contributors

Ruofeng&nbsp;Yang<sup>&#42;</sup>, Haitong&nbsp;Ma<sup>&#42;</sup>, Kaitao&nbsp;Qiu, Zuhao&nbsp;Zhang, Jiaxuan&nbsp;Sun, Tianzhi&nbsp;Ren, Zheli&nbsp;Zhou, Shuai&nbsp;Li<sup>#</sup>

<sup>&#42;</sup> Equal contribution. <sup>#</sup> Corresponding author.

### Contributors

Listed alphabetically by surname.

Haitham&nbsp;Bou&nbsp;Ammar, Dimitris&nbsp;Tsaras, Rasul&nbsp;Tutunov, Jun&nbsp;Wang, Kuan&nbsp;Yang, Qiaosheng&nbsp;Zhang, Zhinuo&nbsp;Zhou

<a id="acknowledgements"></a>

### 🙏 Acknowledgements

Thank you to [@mizopl](https://github.com/mizopl) and the we\* project (PROOFER) for contributing ten square-free graphs of the 8-cube, an independent checker for Case 5A, and Lean 4 counting lemmas. [Explore the contribution](plugins/hypercube-extremal/tools/q8-forcing/README.md) · [Issue #60](https://github.com/lisresearchgroup/math-rsi/issues/60)
