<div align="center">

# <picture><source media="(prefers-color-scheme: dark)" srcset="figures/mathrsi/branding/mark-c-dark.png"><img src="figures/mathrsi/branding/mark-c-light.png" width="76" height="38" align="middle" alt=""></picture> MathRSI<br><sub><sup><em>SII MathRSI Team</em></sup></sub>

**A self-improving agent harness for mathematical discovery and proof.**<br>Readable Markdown skills and domain verifiers for Claude Code and Codex.

[![Website / EN + 中文](figures/mathrsi/badges/visual-tour.svg)](https://lisresearchgroup.github.io/math-rsi/ "Website / EN + 中文")&nbsp; [![Quick Start / Start here](figures/mathrsi/badges/quick-start.svg)](#quick-start)&nbsp; [![Results / 6 domains](figures/mathrsi/badges/results.svg)](case-studies/README.md)&nbsp; [![Agent Guide / Workflow + wiki](figures/mathrsi/badges/agent-guide.svg)](docs/WORKFLOWS.md)&nbsp; [![Contributors / Team](figures/mathrsi/badges/contributors.svg)](#contributors)&nbsp; [![CN / 中文](figures/mathrsi/badges/lang-cn.svg)](README.zh-CN.md)

</div>

[![Actual MathRSI v0 through v6 homepage evolution](figures/mathrsi/media/evolution.gif?v=6-nmrs-20261117)](figures/mathrsi/media/evolution.mp4?v=6-nmrs-20261117)

*Actual v0 → v6 homepage replay, ending at v6 Current. Click for MP4; [interactive homepage](https://lisresearchgroup.github.io/math-rsi/) · [six case studies and verification status](case-studies/README.md).*

MathRSI pairs a shared base workflow with domain plugins and a per-problem research wiki, guiding Claude Code and Codex from literature survey and route selection through proof development, review, verification, and handoff. Validated results and diagnosed failures feed back to refine both the workflow and plugins.

<a id="quick-start"></a>

## 1. 🚀 Quick Start

After completing [setup](docs/QUICKSTART.md), open this repository in **Claude Code** or **Codex** with access to your task directory. In Codex, replace `/skill` with `$skill`. Replace the example paths below with your own.

**Start from a mathematical problem**

```text
/mathrsi-research Study edge-count lower bounds for k-uniform hypergraph two-coloring; work in ../my-problem/
```

Connects literature research, route exploration, proof work, verification and handoff, reusing the task wiki throughout. If you already have a problem statement, you can pass `../my-problem/problem.md` instead.

**Check a candidate proof or local lemma**

```text
/mathrsi-verify Check ../my-problem/proof.tex
```

Checks the proof or a specific obligation, repairs local omissions and identifies substantive mathematical gaps that need further proof work.

**Resume an existing study** (Codex example)

```text
$mathrsi-research Continue the study in ../my-problem/
```

Reads the task's existing specification, wiki and resumption notes, then continues from the current evidence. In Claude Code, use `/mathrsi-research`.

<a id="six-mathematical-frontiers"></a>

## 2. 🧮 Mathematical Results

Research across six domains supplies results and reusable methods. [Public homepage](https://lisresearchgroup.github.io/math-rsi/) · [Local viewing instructions](docs/HOMEPAGE.md). The **[bilingual visual tour](https://lisresearchgroup.github.io/math-rsi/)** shows their problems, results and evolution; the **[six-case index](case-studies/README.md)** links proofs, verification scopes and runnable tools.

[![Six-domain mathematical results overview](figures/mathrsi/results-overview/results-overview.en.svg?v=6-nmrs-20261117)](case-studies/README.md)

- **Property B:** bounds for $k=5,\ldots,12$ and exponentially growing additive gains for every $k\ge12$. [Results & proof scope](case-studies/property-b/README.md)
- **Error-correcting codes:** three gaps dating to 1985 closed; four exact values (one from literature) and one narrowed range. [Results, methods & open case](case-studies/README.md#error-correcting-codes)
- **Degree–diameter:** our constructions reach 2,567 vertices at $(10,4)$, 37,632 at $(11,5)$, 42,433 at $(12,5)$ and 16,416 at $(16,4)$. [Constructions, dated comparisons & scope](case-studies/degree-diameter/README.md)
- **Erdős Problem 86:** $Q_7$ at $304$ (304-edge construction verified; 304 upper bound as reported in the source package, not re-verified in this pass), $682\le\mathrm{ex}(Q_8,C_4)\le683$, and asymptotic density improved from $0.60318$ to $\le0.5912405943$ (`T3`) / $\le0.5912405942$ (`T4`). [Results & verification scope](case-studies/erdos-86/README.md)
- **Ruskey–Savage:** every $Q_6$ matching and every $Q_7$ matching with at least 56 edges (complete E16 across all $\mu\in\{0,1,2,3,4\}$) extends to a Hamilton cycle. [Results, methods & open scope](case-studies/README.md#ruskeysavage-q6)
- **Happy Ending & $N(m,r,s)$:** replayed CNF+DRAT and native-trace integer duals give $N(8,6,6)\le 61$ and $N(9,8,8)\le 688, D_9\le 458$; combined with structural working proofs (independent review pending), they yield signotope $N(8,8,8)\le 318$ (planar $\mathrm{ES}(8)\le 319$ is Schroeder's bound) and working planar corollaries $\mathrm{ES}(7)\le 77$ and $\mathrm{ES}(9)\le 1148$ (vs. $1508$ / $1501^*$). [Results & status](case-studies/happy-ending/README.md)

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

- **v6 base:** test candidate case splits on the hardest open branch before adopting them, and measure net-new coverage on the same input; run primal–dual coevolution that keeps the proof goal separate from the search target, rotates four normalized signed residual channels, and tests candidate cuts against the full graph archive; stop floating-point SDP/CP loops once gains fall to the rounding-repair residual.
- **Deeper domain plugins:** `hypercube-extremal` adds asymptotic COP + $m=1024$ degree-potential bounds (`T3` / `T4`), same-subgraph 3-measure pullbacks ($Q_8 \le 683$), $Q_7$ 304 constructions + source report, and the reusable `cube_coevolve` engine; `hypercube-hamilton` completes $Q_7$ E16 ($\ge 56$ edges across all $\mu=0..4$) with parameterized $Q_6$ $\Delta=2$ double bridges, $Q_6$ $A_8$, and $S_6$ large-face tables paired with symbolic small-face holes; `happy-ending` adds cross-platform checkers and curated archives for $m=7,8,9$ signotope capacities ($N(8,6,6)\le 61$ shared-label CEGAR, $N(9,8,8)\le 688$ & $D_9\le 458$ generative sparse integer duals, and relaxation-ceiling stopping; developed with **Trellis + ARIS + v3**, integrated in `main` maintenance; fixed `v6` tag unchanged).
- **Inherited behavior:** v5's controlled auxiliary choices, cross-representation theorem reuse and consuming returned results before dispatching new work, together with v4's equality-to-witness steps, global progress checks and ECC branch reuse.

**[v6 is the current workflow on `main`](docs/V6_CHANGES.md).** Download the [v6 snapshot ZIP](https://github.com/lisresearchgroup/math-rsi/archive/refs/tags/v6.zip) or [`main` ZIP](https://github.com/lisresearchgroup/math-rsi/archive/refs/heads/main.zip), or clone the repository. Release tags `v1`–`v6` remain fixed snapshots; record the commit hash when handing off a reproducible run. [Evolution & implementation records](development/README.md) · [Maintenance guide](docs/EVOLUTION_WORKFLOW.md)

<details>
<summary>Release history (v0–v6)</summary>

- **v0:** standalone Property B and ECC research tools prior to the shared harness (no Git tag).
- **[v1](https://github.com/lisresearchgroup/math-rsi/tree/v1):** five solving stages, three-layer separation, adversarial route iteration and initial plugins.
- **[v2](https://github.com/lisresearchgroup/math-rsi/tree/v2):** separate maintenance workflow, Degree–Diameter plugin, evidence transfer and shared coverage checks. [Changes](docs/V2_CHANGES.md)
- **[v3](https://github.com/lisresearchgroup/math-rsi/tree/v3):** full-domain counterexample checks, marked-object transport, finite universal certificates and explicit Lean-premise checks; upgraded ECC and three new domains. [Changes](docs/V3_CHANGES.md)
- **[v4](https://github.com/lisresearchgroup/math-rsi/tree/v4):** turning tight equalities into usable witnesses, plus Happy Ending and Degree–Diameter methods. [Changes](docs/V4_CHANGES.md)
- **[v5](https://github.com/lisresearchgroup/math-rsi/tree/v5):** controlled auxiliary choices, theorem reuse across legal representations and finite-plan coverage; deeper Hamilton and DD D5 methods. [Changes](docs/V5_CHANGES.md)
- **[v6](https://github.com/lisresearchgroup/math-rsi/tree/v6):** hardest-branch split probes, primal–dual coevolution and repair-residual stopping; deeper hypercube extremal and complete $Q_7$ E16 Hamilton methods. [Changes](docs/V6_CHANGES.md)

[Historical v2/v3 architecture diagrams](figures/mathrsi/README.md#historical-diagrams)

</details>

<a id="documentation--provenance"></a>

## 6. 📚 Documentation

**[Choose a reading path](docs/README.md)** · [Six research cases](case-studies/README.md) · [Repository map](docs/README.md#repository-map) · [Validation records](development/README.md#validation-and-implementation) · [Skill acceptance](docs/SKILL_ACCEPTANCE.md) · [Contributing](CONTRIBUTING.md)

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
