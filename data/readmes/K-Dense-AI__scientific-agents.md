<div align="center">

[![Website](https://img.shields.io/badge/Website-k--dense.ai-2EA6A0?logo=googlechrome&logoColor=white)](https://www.k-dense.ai)
[![Follow on X](https://img.shields.io/badge/Follow_on_X-%40k__dense__ai-000000?logo=x)](https://x.com/k_dense_ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-K--Dense_Inc.-0A66C2?logo=linkedin)](https://www.linkedin.com/company/k-dense-inc)
[![YouTube](https://img.shields.io/badge/YouTube-K--Dense_Inc.-FF0000?logo=youtube)](https://www.youtube.com/@K-Dense-Inc)
[![Reddit](https://img.shields.io/badge/Reddit-u%2F--k--dense---FF4500?logo=reddit&logoColor=white)](https://www.reddit.com/user/-k-dense-/)
[![Expert Profiles](https://img.shields.io/badge/Expert_Profiles-503-7C3AED)](#agents)
[![Agent Plugins](https://img.shields.io/badge/Agent_Plugins-1.0.0-0F766E)](https://agent-plugins.org/)
[![arXiv](https://img.shields.io/badge/arXiv-2610.00084-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.00084)

# Scientific Agents

**Give your AI agent a domain expert's playbook.**

Expert-thinking profiles: each `AGENTS.md` captures how a senior practitioner in one
scientific or engineering profession works — how they frame problems, the tools and
data they reach for, how they stress-test claims, and how they report findings — as
context an AI agent can load.

</div>

> 🎬 **New to agent profiles?** [Getting Started with Scientific Agent Skills](https://youtu.be/ZxbnDaD_FVg) shows how K-Dense skills and profiles plug into your agent. More walkthroughs on the [K-Dense YouTube channel](https://www.youtube.com/@K-Dense-Inc).

> 📄 **Read the paper:** [Scientific Agents: Evaluating Profession-Specific System Prompts on Scientific Tasks](https://arxiv.org/abs/2610.00084) (arXiv:2610.00084). If these profiles support your research, please [cite it](#citation).

## Table of contents

- [What is AGENTS.md?](#what-is-agentsmd)
- [How these profiles are built](#how-these-profiles-are-built)
- [How to use a profile (three steps)](#how-to-use-a-profile-three-steps)
- [Using profiles in your AI tool](#using-profiles-in-your-ai-tool)
  - [Agent Plugins (Copilot, VS Code, and other compatible tools)](#agent-plugins-copilot-vs-code-and-other-compatible-tools)
  - [Cursor](#cursor)
  - [Claude Code](#claude-code)
  - [Google Antigravity](#google-antigravity)
  - [OpenAI Codex](#openai-codex)
  - [OpenCode](#opencode)
  - [Pi](#pi)
  - [Other supported tools](#other-supported-tools)
- [Star this repo if it helps your work](#star-this-repo-if-it-helps-your-work)
- [Follow K-Dense](#follow-k-dense)
- [Citation](#citation)
- [Agents](#agents)

## What is AGENTS.md?

`AGENTS.md` is a plain Markdown file that tells an AI coding agent **how to think and
work** in your project. Think of it as persistent lab notes for your assistant: not
the public-facing abstract (that belongs in a README), but the operating procedure —
what to check first, which databases and instruments matter, how to stress-test a
claim, and what mistakes to watch for.

This repository collects **expert-thinking profiles**: one `AGENTS.md` per scientific
or engineering profession. Each profile encodes how a senior practitioner in that
field frames problems, evaluates evidence, troubleshoots, and reports results. Drop
one into your workflow to give the agent your field's databases, methods, failure
modes, and reporting norms as working context.

The format is an [open standard](https://agents.md/) (stewarded by the Agentic AI
Foundation). The same file works across many AI tools — you do not need a separate
prompt for every product.

## How these profiles are built

Each profile is research-grounded, not a generic "be rigorous" prompt dressed up for
a field name. The goal is an **operating mind** a senior practitioner would recognize:
concrete databases, instruments, units, controls, failure modes, and reporting norms
— not advice that would read the same for a synthetic biologist and a radio
astronomer.

**Scoping.** Every profile targets one profession (with sub-specialty where it
matters), a work mode (wet-lab, computational, clinical, field, theoretical, or a
mix), and the register of an experienced independent researcher.

**Research.** Before writing, we gather field-specific evidence across parallel
dimensions: foundational theory, how experts frame problems, tools and instruments,
data sources and literature, statistical rigor, troubleshooting and known failure
modes, communication standards, and ethics or regulation where they apply. The aim
is dozens of named, verifiable specifics — not a handful of plausible generalities.

**Synthesis.** Shared scientific commitments (controls, falsifiability, uncertainty,
reproducibility, calibrated claims) are written in **that field's terms**: what
counts as a proper control, which error model applies, how results should be
reported. Universal rigor plus domain specificity — both are required.

**Quality bar.** Drafts are checked with a simple test: if you swap in another
profession's name and the sentence still reads true, it is too generic and gets cut
or replaced. A finished profile should make someone in the field nod — "yes, that's
how we actually think."

Profiles are maintained in `scientific-agents/<profession>/AGENTS.md` and indexed in
[`catalog.json`](catalog.json) and the [Agents](#agents) table below.

## How to use a profile (three steps)

1. **Pick a profile** from the [Agents](#agents) table below — for example,
   [`developmental-biologist/AGENTS.md`](scientific-agents/developmental-biologist/AGENTS.md)
   or [`clinical-epidemiologist/AGENTS.md`](scientific-agents/clinical-epidemiologist/AGENTS.md).
2. **Install it** in the project where you work (see tool-specific steps below). The
   usual pattern is to copy or link the profile as `AGENTS.md` at your project root.
3. **Ask domain questions** as you normally would — analyze data, draft methods,
   debug a pipeline, review a figure, plan an experiment. The agent loads the profile
   automatically at the start of each session.

You can combine an expert profile with your own project rules: put shared lab or repo
conventions in the same `AGENTS.md`, or keep them in a separate file your tool can
include (see each tool below).

## Using profiles in your AI tool

### Agent Plugins (Copilot, VS Code, and other compatible tools)

Every profile folder is an official [Agent Plugin](https://agent-plugins.org/) — the
open, vendor-neutral plugin standard supported by GitHub Copilot, VS Code, Cursor,
Codex, and Kiro. Each `scientific-agents/<slug>/` folder carries a spec-conforming
`plugin.json` (Agent Plugins 1.0.0) and packages the profile as an
[Agent Skill](https://agentskills.io/) at `skills/<slug>/SKILL.md`, so a compatible
tool loads the expert profile on demand whenever a task calls for that expertise.

```
scientific-agents/astronomer/
├── plugin.json                  # Agent Plugins manifest
└── skills/astronomer/SKILL.md   # the profile as an Agent Skill
```

**GitHub Copilot CLI** — add this repo as a marketplace once, then install profiles
by slug:

```
copilot plugin marketplace add K-Dense-AI/scientific-agents
copilot plugin install astronomer@scientific-agents
```

Or install one folder directly without the marketplace:
`copilot plugin install K-Dense-AI/scientific-agents:scientific-agents/astronomer`.

**VS Code** — add the repo to the `chat.plugins.marketplaces` setting, then search
`@agentPlugins` in the Extensions view and install the profiles you want:

```json
"chat.plugins.marketplaces": ["K-Dense-AI/scientific-agents"]
```

**Any other Agent Plugins client** — point its plugin installer at a
`scientific-agents/<slug>/` folder in this repo or a local clone.

### Cursor

Cursor reads `AGENTS.md` from your project automatically and applies it as standing
context for Agent mode.

1. Clone or browse this repo and copy the profile you want, e.g.
   `scientific-agents/bioinformatician/AGENTS.md`.
2. Save it as `AGENTS.md` in the **root of your research codebase** (the folder you
   open in Cursor).
3. Start a new Agent chat. Cursor loads the file without extra setup.

**Tip:** For file-specific rules (e.g. only for R scripts), Cursor also supports
`.cursor/rules/`. Keep the expert profile in `AGENTS.md` and add narrow rules there
if needed. You can `@`-mention additional files in chat when you want the agent to
read them on demand.

### Claude Code

Claude Code’s native file is `CLAUDE.md`, but Anthropic recommends pointing it at
`AGENTS.md` so you stay compatible with other tools. In your project root, create
`CLAUDE.md` with a single line:

```markdown
@AGENTS.md
```

Then copy your chosen expert profile to `AGENTS.md` in the same directory (or symlink
one file to the other). Claude Code loads `CLAUDE.md` every session; the `@` import
pulls in the full expert profile.

**Global use:** you can also place guidance in `~/.claude/CLAUDE.md` for defaults
that apply to every project.

#### Install a profile as a plugin (marketplace)

This repository is also a [Claude Code plugin
marketplace](https://docs.claude.com/en/docs/claude-code/plugins), so you can pull
in a single profession as a reusable **subagent** without copying files by hand.

1. Add the marketplace once:

   ```
   /plugin marketplace add K-Dense-AI/scientific-agents
   ```

2. Install any profile by its slug (the folder name under `scientific-agents/`):

   ```
   /plugin install astronomer@scientific-agents
   ```

   Browse and install interactively with `/plugin` if you prefer a menu.

3. Use it: Claude Code now exposes the profile as a subagent named after the
   profile (e.g. `astronomer`). Ask Claude to delegate to it, or invoke it
   explicitly, and it reasons with the full expert profile loaded. The same
   plugin also ships the profile as an `astronomer` skill, which Claude can load
   into your main conversation when a task calls for that expertise.

Every profile in the [Agents](#agents) table is published as its own plugin, so
you can install exactly the experts you need and update them with
`/plugin marketplace update scientific-agents`.

### Google Antigravity

Antigravity (v1.20.3+) reads `AGENTS.md` natively at session start. Place your
chosen profile at the project root as `AGENTS.md`.

Antigravity also supports `GEMINI.md` for IDE-specific overrides; when both exist,
`GEMINI.md` wins on conflicting rules. A practical setup for mixed teams: put the
expert profile in `AGENTS.md` (shared with Cursor, Codex, etc.) and keep
Antigravity-only preferences in `GEMINI.md`.

**Global defaults:** `~/.gemini/AGENTS.md` applies across projects on your machine.

### OpenAI Codex

Codex reads `AGENTS.md` before doing any work, merging **global** and **project**
instructions:

- **Global:** `~/.codex/AGENTS.md` — your personal defaults across all repos.
- **Project:** `AGENTS.md` at the repo root — copy your expert profile here.

Nested folders can add their own `AGENTS.md`; Codex concatenates files from root to
your current directory (closer files override earlier ones). Expert profiles are
long; if you hit Codex’s default size limit (~32 KiB), raise
`project_doc_max_bytes` in `~/.codex/config.toml` or keep the profile in a
subdirectory you work from.

Use the Codex CLI, VS Code extension, or desktop app — all share the same config.

### OpenCode

OpenCode discovers `AGENTS.md` by walking **up** from your current directory. Copy a
profile to your project root as `AGENTS.md`, or run `/init` in a repo to scaffold one
and replace it with an expert profile.

**Global defaults:** `~/.config/opencode/AGENTS.md`.

OpenCode also reads `CLAUDE.md` if no `AGENTS.md` is found, and supports extra
instruction files via `opencode.json` — useful if you want the expert profile plus
your own `CONTRIBUTING.md` or lab SOPs.

### Pi

Pi (Earendil's minimal terminal coding harness) reads `AGENTS.md` natively at startup,
so an expert profile works with no conversion.

1. Install Pi: `npm install -g --ignore-scripts @earendil-works/pi-coding-agent`.
2. Copy your chosen profile to `AGENTS.md` at your project root.
3. Launch `pi` in that directory — it discovers the file automatically. If you edit the
   profile mid-session, run `/reload` to pick up the change.

Pi looks for `AGENTS.md` (and also recognizes `CLAUDE.md`) in three places, applied in
order: `~/.pi/agent/AGENTS.md` for global defaults, then parent directories walking up
from your working directory, then the current directory.

**Global defaults:** put a profile at `~/.pi/agent/AGENTS.md` to apply it across every
project. Skip context files for a single session with `--no-context-files` (`-nc`). To
swap the whole system prompt instead, Pi reads `.pi/SYSTEM.md` (project) or
`~/.pi/agent/SYSTEM.md` (global), with `APPEND_SYSTEM.md` to add to the default.

### Other supported tools

The same `AGENTS.md` file is also read by **GitHub Copilot**, **Windsurf**, **Zed**,
**Aider**, **Gemini CLI** (via `.gemini/settings.json`), **Devin**, **Factory**, and
others — see the full list at [agents.md](https://agents.md/). If your tool accepts
project-level Markdown instructions, it likely supports this format already.

## ⭐ Star this repo if it helps your work

If a profile saves you time on literature triage, methods drafting, pipeline debugging,
or peer review, **star the repository** on GitHub. Stars are the main signal that
researchers find these profiles useful — they help others discover the collection,
justify continued expansion into new fields, and keep the profiles maintained as
tools and standards evolve. It costs nothing and takes one click.

We add new expert profiles regularly; starring makes it easy to watch the repo for
updates.

## ⭐ Follow K-Dense

We build tools that turn any AI agent into an AI Scientist. Star this repo and follow
along for new expert profiles, scientific skills, and research workflows:

- **X / Twitter** — [@k_dense_ai](https://x.com/k_dense_ai)
- **LinkedIn** — [K-Dense Inc.](https://www.linkedin.com/company/k-dense-inc)
- **YouTube** — [K-Dense Inc.](https://www.youtube.com/@K-Dense-Inc)
- **Website** — [k-dense.ai](https://www.k-dense.ai)

> Stay up to date: follow K-Dense on [X](https://x.com/k_dense_ai), [LinkedIn](https://www.linkedin.com/company/k-dense-inc), and [YouTube](https://www.youtube.com/@K-Dense-Inc).

## Citation

If you use these profiles in your research, please cite the paper:

> Timothy Kassis. *Scientific Agents: Evaluating Profession-Specific System Prompts on
> Scientific Tasks.* arXiv:2610.00084, 2026. https://arxiv.org/abs/2610.00084

```bibtex
@misc{kassis2026scientificagents,
  title         = {Scientific Agents: Evaluating Profession-Specific System Prompts on Scientific Tasks},
  author        = {Timothy Kassis},
  year          = {2026},
  eprint        = {2610.00084},
  archivePrefix = {arXiv},
  primaryClass  = {cs.AI},
  url           = {https://arxiv.org/abs/2610.00084}
}
```

## Agents

All 503 expert profiles, grouped by domain. Click a section to expand it; each
profile name links to its `AGENTS.md`. The complete machine-readable registry lives in [`catalog.json`](catalog.json).

<details>
<summary><b>Mathematics & Statistics</b> — 25 profiles</summary>

| Agent | How it reasons |
| --- | --- |
| [Actuarial Scientist](scientific-agents/actuarial-scientist/AGENTS.md) | Reasons from mortality tables (qx, period/cohort, select/ultimate) and Chain-Ladder/Mack reserving through GLM/GAM frequency–severity and Tweedie pricing, limited-fluctuation and Bühlhmann-Straub credibility, Solvency II SCR standard formula, and IFRS 17 CSM/RA while treating triangle truncation, overfitting, and tail risk as first-class failure modes. |
| [Algebraist](scientific-agents/algebraist/AGENTS.md) | Reasons from carriers, operations, and morphisms through isomorphism theorems, universal properties, exact-sequence and homological tools (Ext, Tor, snake lemma), and computational systems like GAP, Magma, SageMath, and Lean while treating silently smuggled hypotheses (commutativity, units, Noetherian, algebraically closed base), characteristic-p false friends, and noncanonical isomorphisms as first-class failure modes. |
| [Applied Mathematician](scientific-agents/applied-mathematician/AGENTS.md) | Reasons from formulation-first modeling, Buckingham scaling, and asymptotics (matched expansions, boundary layers) through FEM/FVM numerics (FEniCS, PETSc, LAPACK), Tikhonov inverse problems, and ASME/Sandia V&V while treating ill-posed inversion, stiffness, and numerical diffusion as first-class failure modes. |
| [Astrostatistician](scientific-agents/astrostatistician/AGENTS.md) | Reasons from selection functions, censored flux limits, and look-elsewhere trial factors through Cobaya/emcee/dynesty cosmology, GP-coupled exoplanet inference, Landy–Szalay clustering, photo-z σNMAD calibration, and SBI (sbi/LtU-ILI) while treating Malmquist bias, prior-driven tensions, and detrend-then-fit transit bias as first-class failure modes. |
| [Bayesian Statistician](scientific-agents/bayesian-statistician/AGENTS.md) | Reasons from Bayes' rule, coherent uncertainty, exchangeability, and partial-pooling hierarchy through Stan/PyMC HMC-NUTS fits, prior and posterior predictive checks, PSIS-LOO, and SBC calibration while treating divergent transitions and funnels, weak identifiability and label switching, improper posteriors, and post-hoc prior tuning as first-class failure modes. |
| [Biostatistician](scientific-agents/biostatistician/AGENTS.md) | Reasons from estimands, SAPs, and error budgets; aligns ICH E9(R1), CONSORT/STROBE, multiplicity, MMRM, Cox survival, causal DAGs, and GWAS FDR while treating immortal time, ICEs, and batch confounding as first-class failure modes. |
| [Causal Inference Scientist](scientific-agents/causal-inference-scientist/AGENTS.md) | Reasons from structural causal models, potential outcomes, and identification logic through DAGs and do-calculus, doubly-robust estimators (AIPW/TMLE, IPTW, g-formula), and design-based methods (IV, RD, Callaway-Sant'Anna DiD, synthetic control) while treating colliders and M-bias, positivity/overlap failure, and unmeasured confounding (Rosenbaum bounds, E-values) as first-class failure modes. |
| [Combinatorialist](scientific-agents/combinatorialist/AGENTS.md) | Reasons from labelled vs unlabelled enumeration, EGF/OGF and species, bijective and probabilistic proofs, Turán/Ramsey/extremal bounds, and BIBD/OA design parameters through SageMath/GAP/nauty, OEIS, House of Graphs, and Colbourn–Dinitz tables while treating isomorphism double-counting, parity barriers, and OEIS false matches as first-class failure modes. |
| [Differential Geometer](scientific-agents/differential-geometer/AGENTS.md) | Reasons from connections, curvature, and holonomy; fixes Lee vs Besse/MTW Riemann signs; uses SageManifolds/xAct/Cadabra, Chern–Weil and Atiyah–Singer index theory, and model-space checks (S^n, flat tori) while treating chart artifacts, torsion misuse, and CAS convention drift as first-class failure modes. |
| [Dynamical Systems Theorist](scientific-agents/dynamical-systems-theorist/AGENTS.md) | Reasons from state spaces, invariant sets, bifurcations, and multiple time scales through normal-form classification, center-manifold reduction, Floquet/Poincaré maps, and continuation tools like AUTO, MatCont, and DynamicalSystems.jl while treating spurious chaos from finite-time Lyapunov bias, false limit cycles mistaken for tori, numerical blow-up versus true singularity, and Takens embedding artifacts as first-class failure modes. |
| [Logician](scientific-agents/logician/AGENTS.md) | Reasons from syntax-versus-semantics and object-versus-metalanguage discipline, the ⊢/⊨ distinction, and matching each logic to its intended semantics through natural deduction and sequent calculus (cut-elimination, subformula property), compactness and Löwenheim–Skolem, forcing and diagonalization, and proof assistants (Lean 4/mathlib, Coq, Isabelle/HOL, Agda) with Z3/CVC5/Vampire/Mace4 automation while treating use–mention conflation, second-order misuse of compactness, mis-stated incompleteness hypotheses (ω-consistency vs consistency), and Gödel philosophical overreach as first-class failure modes. |
| [Mathematical Analyst](scientific-agents/mathematical-analyst/AGENTS.md) | Reasons from function-space topology, convergence modes, and constant-dependent inequalities (Hölder, Sobolev, Gronwall) through compactness theorems (Rellich-Kondrachov, Banach-Alaoglu), Calderon-Zygmund and Schauder estimates, and Lax-Milgram while treating limit-integral swaps without dominated convergence, boundary-degenerating constants, weak-versus-classical regularity gaps, and concentration-compactness loss as first-class failure modes. |
| [Mathematical Modeler](scientific-agents/mathematical-modeler/AGENTS.md) | Reasons from nondimensionalization, conservation/positivity laws, and minimal-viable model structure through mechanistic ODE/PDE, stochastic, and agent-based formulations, profile-likelihood and Fisher-information identifiability, and Sobol/Morris sensitivity analysis, while treating sloppy unidentifiable parameters, structural model uncertainty, and out-of-regime extrapolation as first-class failure modes. |
| [Mathematical Physicist](scientific-agents/mathematical-physicist/AGENTS.md) | Reasons from Hilbert-space domains, Wightman/OS and Haag–Kastler axioms, constructive QFT, Gibbs measures, and spectral/scattering theory; uses Reed–Simon, Glimm–Jaffe, MathSciNet/math-ph, while treating wrong self-adjoint extensions, invalid Wick rotation, limit-order swaps, and lattice-as-continuum claims as first-class failure modes. |
| [Mathematical Statistician](scientific-agents/mathematical-statistician/AGENTS.md) | Reasons from LAN, empirical processes, and influence functions; proves M/Z-estimator limits, minimax rates (Fano/Le Cam/Assouad), and semiparametric efficiency while validating with ADEMP simulations and treating naive bootstrap, non-Donsker classes, and debiasing sparsity violations as first-class failure modes. |
| [Network Scientist](scientific-agents/network-scientist/AGENTS.md) | Reasons from adjacency structure, generative models, and null hypotheses through configuration-model and SBM/ERGM nulls, CSN power-law fitting with log-normal Vuong tests, and multi-algorithm community detection (Louvain, Leiden, Infomap, graph-tool) while treating artifactual scale-free tails from correlation thresholding, modularity's resolution bias, force-directed hairball over-interpretation, and test-edge leakage in link prediction as first-class failure modes. |
| [Nonlinear Dynamics & Chaos Scientist](scientific-agents/nonlinear-dynamics-chaos-scientist/AGENTS.md) | Reasons from flows, maps, bifurcations, and invariant sets; continues with MatCont/AUTO/COCO, validates chaos with IAAFT surrogates and embedding convergence, and treats spurious Lyapunov exponents, stiff integrator artifacts, and colored-noise confounds as first-class failure modes. |
| [Number Theorist](scientific-agents/number-theorist/AGENTS.md) | Reasons from primes, congruences, L-functions, and the Langlands web; chooses algebraic, analytic, and sieve methods; validates with SageMath/PARI/LMFDB while treating PARI stack overflows, conditional-proof leaks, and CRT moduli errors as first-class failure modes. |
| [Numerical Analyst](scientific-agents/numerical-analyst/AGENTS.md) | Reasons from well-posedness, discretization, conditioning, and stability; verifies codes with MMS and convergence studies; treats cancellation, stiffness, and solver tolerance floors as first-class failure modes. |
| [Operations Researcher](scientific-agents/operations-researcher/AGENTS.md) | Reasons from decision structure, integrality and convexity, and explicit uncertainty through LP/MIP solvers (Gurobi, CPLEX, OR-Tools CP-SAT), stochastic and Wasserstein-distributionally-robust formulations, and DES (SimPy, AnyLogic) benchmarked on Solomon/MIPLIB instances, while treating unit inconsistencies, optimality-gap-versus-stale-data trade-offs, infeasibility (IIS) from forgotten labor and fairness constraints, and day-to-day solution oscillation as first-class failure modes. |
| [Optimization Scientist](scientific-agents/optimization-scientist/AGENTS.md) | Reasons from convexity class, KKT/complementarity, and LP/MIP relaxation gaps through interior-point and branch-and-cut (Gurobi, CPLEX, MOSEK, Ipopt) while treating loose big-M, IntegralityTol cheaters, IIS-hidden infeasibility, nonconvex KKT-as-global, and MIPGap-at-TimeLimit-as-optimal as first-class failure modes. |
| [Probabilist](scientific-agents/probabilist/AGENTS.md) | Reasons from Kolmogorov measure spaces through LLN/CLT, martingales, coupling, concentration/LDP, and Lévy/Feller/Itô calculus; uses Durrett/Kallenberg canon, Sage/NumPy/PyMC simulation, and R̂/ESS/IS diagnostics while treating a.s. vs sure, Borel conditioning, OST misuse, and importance-weight explosion as first-class failure modes. |
| [Pure Mathematician](scientific-agents/pure-mathematician/AGENTS.md) | Reasons from definitions, axioms, and proved theorems through lemma-ladder proof strategies, computer algebra (SageMath, GAP, Magma) and proof assistants (Lean 4/mathlib, Coq, Isabelle/HOL) checked against MathSciNet/zbMATH and OEIS, while treating hidden hypotheses, circular reasoning, unjustified w.l.o.g. steps, and ZFC-independence as first-class failure modes. |
| [Statistician](scientific-agents/statistician/AGENTS.md) | Reasons from estimands, generative-model assumptions, and a budgeted Type I/II error tradeoff through analysis plans (SAP, ICH E9(R1) estimands), mixed models, multiple imputation under MCAR/MAR/MNAR, and Benjamini-Hochberg FDR while treating naive post-selection SEs, unadjusted multiplicity, ignored clustering in survey PSUs, and sequential peeking as first-class failure modes. |
| [Topologist](scientific-agents/topologist/AGENTS.md) | Reasons from continuity, compactness, connectedness, homotopy, and manifold structure through invariants and tools like π₁ via Seifert-van Kampen, cellular/simplicial homology with ∂²=0 and Smith-normal-form torsion, Mayer-Vietoris, and SnapPy/GUDHI computation, while treating lost-Hausdorffness in quotients, torsion missed by rational coefficients, visual deformation without a homotopy or Reidemeister proof, and barcodes interpreted without filtration stability as first-class failure modes. |

</details>

<details>
<summary><b>Computer Science, Data & AI</b> — 30 profiles</summary>

| Agent | How it reasons |
| --- | --- |
| [AI Researcher](scientific-agents/ai-researcher/AGENTS.md) | Reasons from data generating processes, inductive biases, and compute-data-algorithm trade-offs through train/val/test discipline, seed sweeps, ablation ladders, and standards like NeurIPS reproducibility checklists, model cards, and lm-eval-harness, while treating data leakage (Kapoor & Narayanan taxonomy), benchmark contamination, spurious correlations, and reward-model overoptimization as first-class failure modes. |
| [Algorithms Researcher](scientific-agents/algorithms-researcher/AGENTS.md) | Reasons from separating problem, model, and cost model (comparison, word-RAM, arithmetic, online) through exchange/matroid greedy proofs, subproblem-DAG dynamic programming, max-flow min-cut and Goemans–Williamson primal-dual rounding, Karp–Rabin fingerprinting, competitive ratio and Yao's principle, PTAS/FPTAS (Williamson–Shmoys), and Instance Space Analysis over DIMACS10/MIPLIB 2017/SuiteSparse while treating amortized-versus-average-case conflation, unproven greedy killed by a 4-node counterexample, Monte Carlo without a false-match probability, DIMACS10 suite overfitting, and 'linear time' hiding word-size tricks over bit-length L as first-class failure modes. |
| [Computational Linguist](scientific-agents/computational-linguist/AGENTS.md) | Reasons from UD/PTB formalisms, validate.py/eval.py (LAS/MLAS/ELAS), and evalb .prm settings through Stanza/UDPipe pipelines, PropBank/FrameNet/AMR/UMR layers, IAA (κ, Krippendorff α), CONDA contamination checks, and ARR reproducibility while treating tokenizer mismatch, oracle inflation, train–test leakage, and guideline drift as first-class failure modes. |
| [Computational Scientist](scientific-agents/computational-scientist/AGENTS.md) | Reasons from Roache code/solution verification and ASME V&V 10/20/40 credibility through MMS/GCI, UQ ensembles, and Snakemake/Nextflow/CWL pipelines with conda-lock/Apptainer provenance while treating environment drift, workflow cache staleness, and validation-vs-calibration conflation as first-class failure modes. |
| [Computational Social Scientist](scientific-agents/computational-social-scientist/AGENTS.md) | Reasons from social mechanisms, measurement validity, and sampling frames through DAGs, fixed-effects and IV/DiD/RDD designs, ERGM/SAOM network models, and human-audited text classifiers while treating unobserved homophily, network interference and SUTVA violations, platform-driven selection, bot contamination, and digital-skew unrepresentativeness as first-class failure modes. |
| [Computer Architecture Researcher](scientific-agents/computer-architecture-researcher/AGENTS.md) | Reasons from ISA semantics, AMAT/CPI, MESI coherence, and branch prediction through gem5/SPEC/MLPerf evaluation, Amdahl and roofline discipline, TPU/GPU dataflow accelerators, DVFS/EDP, and Spectre/Meltdown mitigation overhead at ISCA/MICRO/HPCA rigor. |
| [Computer Graphics Researcher](scientific-agents/computer-graphics-researcher/AGENTS.md) | Reasons from the rendering equation, Monte Carlo bias/variance, sampling theory, and BSDF energy conservation through pbrt-v4/Mitsuba 3 references, MIS/ReSTIR/path guiding, DXR 1.2 real-time stacks, 3DGS and NerfBaselines protocols, FLIP/ColorVideoVDP evaluation, OpenUSD/MaterialX/OpenPBR interchange, and ACES 2/OCIO color while treating unconverged references, unequal-time comparisons, denoiser and temporal-reuse bias, scene- vs display-referred color errors, and white-furnace energy failures as first-class failure modes. |
| [Computer Scientist](scientific-agents/computer-scientist/AGENTS.md) | Reasons from computational models, abstraction contracts, invariants, and measurable complexity through CLRS-grade algorithm analysis, impossibility results (FLP, CAP, NP-hardness), property-based and chaos testing, and formal tools (TLA+, Coq, Z3) while treating partial failure, race conditions, label leakage, and abstraction leaks like GC pauses and clock skew as first-class failure modes. |
| [Computer Security Researcher](scientific-agents/computer-security-researcher/AGENTS.md) | Reasons from explicit threat models and CIA/STRIDE through AFL++/libFuzzer triage, ASan/KASAN oracles, ProVerif/Tamarin proofs, CVE/CWE/CAPEC taxonomies, CyberGym dual-execution benchmarks, Menlo/CVD ethics, and USENIX open-science artifact norms. |
| [Computer Vision Scientist](scientific-agents/computer-vision-scientist/AGENTS.md) | Reasons from image formation, projective geometry (pinhole intrinsics and extrinsics, epipolar/PnP/bundle adjustment, similarity-scale ambiguity), and COCO/LVIS AP mechanics through DINOv3/SigLIP 2 foundation baselines, RF-DETR/YOLO26/SAM 3 models, COLMAP 4/GLOMAP and VGGT geometry, pycocotools/TrackEval/BOP evaluation, and CVPR reporting and EU AI Act limits while treating train–test and pretraining leakage, AP evaluation-setting gaming, preprocessing mismatches (EXIF, BGR, aliased resizing), label noise, and camera-convention and scale errors as first-class failure modes. |
| [Cryptographer](scientific-agents/cryptographer/AGENTS.md) | Reasons from IND-CCA/EUF-CMA games and tight reductions through AES-GCM/RSA-OAEP/ECDSA, ML-KEM/ML-DSA (FIPS 203/204), ProVerif/Tamarin/EasyCrypt, dudect constant-time, CAVP/ACVP and FIPS 140-3 CMVP—not pure number theory or vuln fuzzing. |
| [Data Engineer](scientific-agents/data-engineer/AGENTS.md) | Reasons from idempotent ELT, medallion bronze/silver/gold, Kimball grain and SCD2, CDC/Debezium and watermark incremental loads, dbt/GX quality gates, Airflow/Dagster orchestration, Iceberg/Delta lakehouse MERGE, data contracts and freshness SLIs while treating silent join drops, duplicate amplification, schema drift, and green-DAG-wrong-numbers as first-class failure modes. |
| [Data Scientist](scientific-agents/data-scientist/AGENTS.md) | Reasons from CRISP-DM business estimands, leakage-safe sklearn Pipelines and nested CV, SQL/warehouse semantic metrics, A/B power and SRM/AA guardrails, causal DAG covariate discipline, and Model Cards/Datasheets while treating train-test leakage, Simpson's paradox, peeking, and PSI>0.25 drift as first-class failure modes. |
| [Database Systems Researcher](scientific-agents/database-systems-researcher/AGENTS.md) | Reasons from storage hierarchy, concurrency semantics, query-optimization theory, and declared workload models through TPC-C/H, YCSB, and JOB benchmarks, Jepsen/Elle correctness checkers, and perf/blktrace/fio profiling while treating cardinality-estimation plan regressions, tail-latency spikes under skew, unfair fsync-disabled speedups, and benchmark-trick wins as first-class failure modes. |
| [Deep Learning Scientist](scientific-agents/deep-learning-scientist/AGENTS.md) | Reasons from CNN/Transformer inductive bias, Li et al. loss landscapes, grokking/mode connectivity, and Kaplan/Chinchilla scaling (~20 tokens/param); designs ResNet/ViT/DiT/MoE/FlashAttention stacks with FLOPs-matched ablations; trains AdamW+cosine/WSD via Megatron-FSDP/DeepSpeed; evaluates FID/MMLU-Pro/MMLU-CF with lm-eval decontamination and Pineau/NeurIPS reproducibility checklists. |
| [Distributed Systems Researcher](scientific-agents/distributed-systems-researcher/AGENTS.md) | Reasons from failure models, consistency contracts, and tail-latency-and-recovery performance through TLA+ model checking, Jepsen and Porcupine linearizability checking, and YCSB/DeathStarBench benchmarking with iptables and kill -9 fault injection, while treating unbounded leases and split-brain, clock skew under NTP, and GC-induced p99 spikes as first-class failure modes. |
| [Edge / Embedded AI Engineer](scientific-agents/edge-embedded-ai-engineer/AGENTS.md) | Reasons from tensor-arena budgets, full-int8 PTQ with representative calibration, and TFLM/CMSIS-NN or Vela/Ethos-U compile paths through ONNX Runtime QNN HTP and mobile delegates—treating train–serve preprocessing skew, float thresholds on quantized outputs, and NPU operator fallback as first-class failure modes. |
| [Formal Methods Researcher](scientific-agents/formal-methods-researcher/AGENTS.md) | Reasons from operational semantics and temporal logics through SPIN/TLA+/PRISM, Coq/Lean/Isabelle, Z3/CVC5, refinement and separation logic, vacuity and false-positive diagnosis, and Dafny/F* versus property-based testing boundaries. |
| [High-Performance Computing Specialist](scientific-agents/high-performance-computing-specialist/AGENTS.md) | Reasons from NUMA topology and hybrid MPI+OpenMP+CUDA decomposition through Slurm fairshare/backfill job design, strong/weak scaling (Amdahl/Gustafson), Darshan/mpiP/Nsight profiling, and parallel HDF5/MPI-IO on Lustre while treating I/O storms, collectives bottlenecks, and rank-binding mistakes as first-class failure modes. |
| [Human–Computer Interaction Researcher](scientific-agents/human-computer-interaction-researcher/AGENTS.md) | Reasons from situated context, Fitts/GOMS/KLM, and CHI contribution types; runs contextual inquiry through LMM/CLMM analysis with SUS/NASA-TLX triangulation; uses Prolific/OSF and treats demand characteristics, novelty effects, ordinal misuse, and WEIRD samples as first-class failure modes. |
| [Information Retrieval Scientist](scientific-agents/information-retrieval-scientist/AGENTS.md) | Reasons from the Probability Ranking Principle, Saracevic's relevance layers, and Cranfield pooling through tuned BM25, SPLADE/ColBERT/dense and LLM reranking, trec_eval/ir_measures with paired topic-level tests, interleaving, and nugget-based RAG evaluation while treating unjudged-as-nonrelevant pools, position-biased clicks, LLM-judge circularity, single-vector embedding limits, and benchmark contamination as first-class failure modes. |
| [Knowledge Representation Researcher](scientific-agents/knowledge-representation-researcher/AGENTS.md) | Reasons from model-theoretic semantics, the expressivity-vs-decidability-vs-scalability tradeoff, and competency questions through OWL 2 profiles, reasoners (HermiT, Pellet, ELK), ROBOT/Protégé pipelines, and SHACL validation while treating unsatisfiable classes, silent OWA-vs-CWA semantic mixing, hallucinated LLM-suggested axioms, and IRI-reuse on bad merges as first-class failure modes. |
| [Machine Learning Engineer](scientific-agents/machine-learning-engineer/AGENTS.md) | Reasons from decision-policy framing, Google's Rules of ML, point-in-time data, and prefill/decode inference physics through GBDT/PyTorch baselines, vLLM/SGLang/KServe serving with FP8/AWQ quantization, hybrid-retrieval RAG, RAGAS and human-validated LLM judges, OpenTelemetry GenAI tracing, and post-Omnibus EU AI Act obligations while treating train-serve skew, temporal leakage, prompt injection, LLM nondeterminism, and degenerate feedback loops as first-class failure modes. |
| [Machine Learning Researcher](scientific-agents/machine-learning-researcher/AGENTS.md) | Reasons from population risk, double descent, and inductive bias; enforces sacred test sets, hierarchical ablations, nested CV, and HELM/Dynabench-aware benchmarking; reports with NeurIPS and Pineau reproducibility checklists while treating leakage, meta-overfitting, benchmark contamination, Goodhart gaming, and seed variance as first-class failure modes. |
| [MLOps Engineer](scientific-agents/mlops-engineer/AGENTS.md) | Reasons from data contracts, feature parity, evaluation gates, and rollback-readiness through MLflow/W&B registries, Feast feature stores, KServe/Triton serving, Great Expectations/TFDV validation, and Evidently PSI/KS drift monitors while treating train-serve skew, data leakage, silent degradation, and schema/concept drift as first-class failure modes. |
| [Natural Language Processing Scientist](scientific-agents/natural-language-processing-scientist/AGENTS.md) | Reasons from tokenization, data curation (datatrove/NeMo), and evaluation protocols (SacreBLEU/COMET, IFEval, HELM); enforces contamination audits (ConTAM, perplexity separation), paired bootstrap significance, SFT→DPO/RLHF with alignment-tax checks, and ARR/Dodge reproducibility while treating exposure bias, benchmark leakage, prompt-template confounds, and metric gaming as first-class failure modes. |
| [Programming Languages Researcher](scientific-agents/programming-languages-researcher/AGENTS.md) | Reasons from operational semantics, type-theoretic invariants, and soundness as preservation-plus-progress through Ott/LN-defined calculi, Coq/Isabelle/Agda mechanization, Hindley-Milner inference, and abstract-interpretation Galois connections while treating stuck terms, blame escaping onto well-typed pure terms, broken substitution and canonical-forms lemmas, and unsound widening as first-class failure modes. |
| [Reinforcement Learning Researcher](scientific-agents/reinforcement-learning-researcher/AGENTS.md) | Reasons from MDP/POMDP structure, Bellman contraction and the deadly triad, and policy-gradient variance through Gymnasium 1.x/MuJoCo v5/ALE v5 protocols, CleanRL/SB3/JAX (MJX, MuJoCo Playground) stacks, rliable IQM with stratified bootstrap CIs, Minari offline datasets, and GRPO/RLVR post-training while treating truncation-as-termination bootstrap bugs, seed and hyperparameter selection bias, reward hacking, and offline extrapolation error as first-class failure modes. |
| [Research Software Engineer](scientific-agents/research-software-engineer/AGENTS.md) | Reasons from Software Carpentry and FAIR4RS through SemVer releases, CITATION.cff/SPDX metadata, pytest/Hypothesis CI gates, Docker/Apptainer on Slurm, and maintainability discipline for citable, reproducible research code. |
| [Theoretical Computer Scientist](scientific-agents/theoretical-computer-scientist/AGENTS.md) | Reasons from explicit models (TM, circuit, communication, query) and resource measures; audits Karp/parsimonious/gap/fine-grained reductions against ETH/SETH/#ETH and PCP/UGC/APX barriers; uses Complexity Zoo, ECCC/arXiv cs.CC, Coq/Lean/DRAT, Williams algorithms-for-lower-bounds, and Yao/IC lower bounds while treating wrong reduction direction, non-parsimony, APSP–3SUM conflation, oracle overclaim, and natural-proofs misuse as first-class failure modes. |

</details>

<details>
<summary><b>Physics</b> — 30 profiles</summary>

| Agent | How it reasons |
| --- | --- |
| [Accelerator Physicist](scientific-agents/accelerator-physicist/AGENTS.md) | Reasons from beam optics, RF cavities, emittance budgets, and loss maps while treating halo and impedance-driven instabilities as first-class failure modes. |
| [Acoustics Physicist](scientific-agents/acoustics-physicist/AGENTS.md) | Reasons from impedance Z=p/u, Helmholtz number kL regime, and the sonar equation SL-TL-NL+DI+PG through impedance tubes (ISO 10534), anechoic and reverberation rooms, laser vibrometry, and k-Wave/COMSOL simulation while treating edge diffraction inflating absorption above one, near-field versus far-field confusion, flanking and multipath paths, and amplifier clipping mistaken for nonlinearity as first-class failure modes. |
| [Atomic, Molecular & Optical Physicist](scientific-agents/atomic-molecular-optical-physicist/AGENTS.md) | Reasons from Rabi/OBE dynamics, laser-cooling hierarchy, optical lattices and Hubbard U/J, and magic-wavelength clock budgets through NIST ASD, ARC, QuTiP/PyLCP, and in-situ lattice-depth calibration while treating power-based depth guesses, polarization impurities, BBR shifts, and imaging-heating conflation as first-class failure modes. |
| [Computational Physicist](scientific-agents/computational-physicist/AGENTS.md) | Reasons from governing equations, discretization, and HPC scaling through code/solution verification, DFT, MD, Monte Carlo, and FEM/FVM workflows (VASP, LAMMPS, COMSOL, OpenFOAM, QE). |
| [Condensed Matter Physicist](scientific-agents/condensed-matter-physicist/AGENTS.md) | Reasons from Bloch bands, quasiparticles, and symmetry through ARPES/STM/neutron/transport workflows, VASP/QE/Wannier90/DMFT, and Materials Project/ICSD/MPDS while treating matrix-element artifacts, Mott vs. DFT gaps, pseudogap vs. SC gap, and Planckian bad-metal transport as first-class failure modes. |
| [Experimental Physicist](scientific-agents/experimental-physicist/AGENTS.md) | Reasons from GUM error budgets, traceable calibration chains, and multiplied signal-chain transfer functions — separating Type A and Type B uncertainty, null runs, and ELN-linked reproducibility before precision or discovery claims. |
| [Fluid Dynamicist](scientific-agents/fluid-dynamicist/AGENTS.md) | Reasons from Navier–Stokes and dimensionless scaling through RANS/LES/DNS selection, mesh/y+ strategy, OpenFOAM/Fluent workflows, and MMS + ASME V&V 20 / PIV validation. |
| [Fusion Scientist](scientific-agents/fusion-scientist/AGENTS.md) | Reasons from Lawson triple product and Q through tokamak/stellarator confinement (H-mode, ELMs, RMP), NBI/ICRH/ECRH heating, EFIT/TRANSP/SOLPS-ITER workflows, ITER/JET/DIII-D/W7-X benchmarks, PMI (W/Be PFCs), and tritium breeding blankets. |
| [Gravitational Physicist](scientific-agents/gravitational-physicist/AGENTS.md) | Reasons from calibrated strain, colored non-stationary noise PSDs, matched-filter SNR, and Bayesian posteriors through PyCBC/GstLAL/cWB searches, Bilby/LALInference PE with NRSur/SEOBNR/IMRPhenom waveforms, and FAR/p_astro significance while treating glitch contamination, waveform-approximant mismatch, mass-spin and distance-inclination degeneracies, and unmodeled selection effects as first-class failure modes. |
| [Laser Physicist](scientific-agents/laser-physicist/AGENTS.md) | Reasons from population inversion and threshold gain (g ≥ l/L + T), ABCD resonator stability (g₁g₂ in 0–1) and c/(2L) mode spacing, GVD/TOD dispersion management and time-bandwidth ΔtΔν ≈ 0.44, and Kerr/SPM nonlinear phase through Kerr-lens/SESAM mode-locking, CPA stretcher–amplifier–compressor with B-integral budgeting, QPM in PPLN/PPLKTP for SHG/OPA, FROG/SPIDER and Dazzler pulse shaping, M² caustics per ISO 11146, and IEC 60825 classification while treating thermal-lens drift out of the stability zone, autocorrelation-width-mistaken-for-pulse-width, uncompensated TOD wings and regen double-pulsing, and LMA-fiber mode instability and SRS/SBS above kW as first-class failure modes. |
| [Low-Temperature Physicist](scientific-agents/low-temperature-physicist/AGENTS.md) | Reasons from kT budgets, He-3/He-4 dilution refrigeration, and BCS/GL superconductivity; measures Tc, QHE, and Landauer conductance with lock-in/SQUID workflows while treating wiring heat loads, Kapitza resistance, flux trapping, TLS dielectric loss, and sample-vs-MXC thermometer mismatch as first-class failure modes. |
| [Metrology Scientist](scientific-agents/metrology-scientist/AGENTS.md) | Reason from SI traceability, GUM uncertainty budgets, and VIM distinctions between calibration and verification; propagates Type A/B components, CIPM MRA equivalence, and ILAC decision rules before any pass/fail claim. |
| [Nanophysicist](scientific-agents/nanophysicist/AGENTS.md) | Reasons from quantum confinement dimensionality, Coulomb diamonds and SET conditions, Kondo vs Luttinger-liquid power laws, and lock-in cryostat transport through STM/STS, AFM/KPFM, and STEM/EELS while treating charging artifacts, tip convolution, contact resistance, and beam-damage plasmon shifts as first-class failure modes. |
| [Nuclear Physicist](scientific-agents/nuclear-physicist/AGENTS.md) | Reasons from shell and collective structure, reaction mechanisms, and ENDF/EXFOR data; matches FRIB–CEBAF–RHIC science to R-matrix, Hauser-Feshbach, chiral ab initio, and GEANT4 tools; treats dead time, normalization, and evaluation covariances as first-class failure modes. |
| [Optical Physicist](scientific-agents/optical-physicist/AGENTS.md) | Reasons from square-law detection and Fourier duality, Gaussian-beam and coherence theory, Jones/Mueller polarization, and dispersion and χ⁽²⁾/χ⁽³⁾ phase matching through FROG/SPIDER/d-scan retrieval, phase-shifting and absolute interferometry, Zemax/CODE V/Optiland modeling, SNLO, FTIR/Raman/ellipsometry, and ISO 10110/11146/21254 reporting while treating parasitic etalons, coherent artifacts of unstable pulse trains, thermal lensing mistaken for Kerr nonlinearity, Zernike-convention and retrace errors, and FFT-propagation aliasing as first-class failure modes. |
| [Particle Physicist](scientific-agents/particle-physicist/AGENTS.md) | Reasons from SM gauge structure, parton PDFs, and detector response through ATLAS/CMS/LHCb/Belle II/DUNE workflows, Geant4+Pythia/MG5 simulation, HistFactory/Combine/pyhf likelihoods, and HEPData/Rivet preservation while treating LEE/global significance, JES/pile-up, fake leptons, and flux×cross-section systematics as first-class failure modes. |
| [Photonics Scientist](scientific-agents/photonics-scientist/AGENTS.md) | Reasons from guided-wave dispersion, ring FSR–Q–coupling, and FWM phase matching; designs waveguides, lasers, and modulators with Lumerical MODE/FDTD/CHARGE/INTERCONNECT while treating dispersive FSR mismatch, TPA/FCA/XPM detuning, mesh dispersion, etalon ripples, and thermal bistability as first-class failure modes. |
| [Plasma Physicist](scientific-agents/plasma-physicist/AGENTS.md) | Reasons from collective scales (Debye length, plasma frequency), dimensionless regime parameters (beta, collisionality, Lundquist number), and instability drive-versus-dissipation through Grad-Shafranov equilibria (EFIT, VMEC), gyrokinetic and MHD codes (GENE, NIMROD, XGC), PIC simulation (VPIC, OSIRIS), and confinement scalings (IPB98, Greenwald, Troyon) while treating probe sheath distortion, equilibrium-reconstruction error, resolution-limited reconnection rates, and unmatched wall conditioning as first-class failure modes. |
| [Quantum Computing Scientist](scientific-agents/quantum-computing-scientist/AGENTS.md) | Reasons from qubits as noisy open systems through T1/T2, gate fidelity, RB/GST/XEB, and quantum volume to surface-code QEC; compiles with Qiskit/Cirq, applies ZNE/PEC/readout mitigation, and treats crosstalk, transpilation depth, and calibration drift as first-class failure modes. |
| [Quantum Information Scientist](scientific-agents/quantum-information-scientist/AGENTS.md) | Reasons from operational entropies (smooth min-entropy, coherent information), Stinespring/Choi channel pictures, and the achievability-versus-converse split through dual-certified SDP/NPA bounds, EAT/GEAT finite-key security proofs, Stim/PyMatching/BP+OSD circuit-level QEC simulation, classical shadows and GST, and ETSI/ISO QKD evaluation standards while treating asymptotic key rates passed off as performance, uncertified superadditivity numerics, code distance mistaken for circuit distance, MLE-tomography bias, and CHSH violations mistaken for security proofs as first-class failure modes. |
| [Quantum Optics Scientist](scientific-agents/quantum-optics-scientist/AGENTS.md) | Reasons from field quadratures, atom-photon coupling (g, κ, γ), and heralding efficiency budgets through g⁽²⁾ Hanbury Brown-Twiss measurement, balanced homodyne tomography, HOM interference, and SNSPD/APD detector calibration while treating afterpulsing-faked antibunching, LO phase drift erasing squeezing, accidentals and dark counts, and unaddressed Bell-test loopholes as first-class failure modes. |
| [Quantum Physicist](scientific-agents/quantum-physicist/AGENTS.md) | Reasons from Hilbert-space density operators, commutation relations, and Lindblad open-system dynamics through randomized benchmarking, gate-set and process tomography, Bell-CHSH tests, and Stim/PyMatching surface-code decoding while treating crosstalk, leakage, calibration drift, and measurement backaction as first-class failure modes. |
| [Semiconductor Physicist](scientific-agents/semiconductor-physicist/AGENTS.md) | Reasons from ε_n(k), effective-mass tensor, and 2D subband DOS through Hall/multiband fits, mobility scattering analysis, Lang DLTS (E_T, σ, N_T), and quantum-well intersubband spectroscopy while treating compensation, rate-window artifacts, and DFT gap error as first-class failure modes. |
| [Soft Matter Physicist](scientific-agents/soft-matter-physicist/AGENTS.md) | Reason from kT and mesoscale structure; couple rheology (TA Instruments, Anton Paar), scattering (SANS/SAXS/DLS/XPCS), and PIV to Flory-Huggins, de Gennes scaling, jamming, and active-matter hydrodynamics. |
| [Spintronics Physicist](scientific-agents/spintronics-physicist/AGENTS.md) | Reasons from spin-orbit coupling, spin diffusion length, exchange and DMI, and spin-dependent transport through MTJ/TMR characterization, ST-FMR and harmonic-Hall torque measurement, nonlocal spin valves, and Valet-Fert and MuMax3/OOMMF modeling, while treating barrier pinholes and shunt paths, ordinary-versus-anomalous Hall and ISHE confusion, Oersted-field and Joule-heating artifacts, and incomplete magnetization switching as first-class failure modes. |
| [Statistical Physicist](scientific-agents/statistical-physicist/AGENTS.md) | Reasons from ensembles and partition functions through finite-size scaling (Binder cumulant, data collapse), Wolff/cluster MC, and RG/MCRG to Jarzynski–Crooks fluctuation theorems; uses ALPS, NetKet, WHAM, and ED/DMRG while treating critical slowing down, subleading FSS humps, and poor work-histogram overlap as first-class failure modes. |
| [String Theorist](scientific-agents/string-theorist/AGENTS.md) | Reasons from worldsheet CFT anomaly cancellation, moduli stabilization, and effective-field-theory consistency through KKLT/LVS flux compactifications, KLT/CHY/BCFW amplitude methods, and AdS/CFT large-N holography while treating tadpole mismatches, runaway moduli, unstabilized de Sitter uplifts, and conjecture-as-theorem swampland overclaims as first-class failure modes. |
| [Surface Physicist](scientific-agents/surface-physicist/AGENTS.md) | Reasons from surface thermodynamics, adsorption coverage, work function, and probe escape depth through XPS/ARPES, LEED I(V) and CTR analysis, STM/AFM, TPD with Redhead analysis, and DFT slabs while treating adventitious-carbon contamination, differential charging, electron-beam and tip-induced damage, and UHV-to-operando extrapolation as first-class failure modes. |
| [Theoretical Physicist](scientific-agents/theoretical-physicist/AGENTS.md) | Reasons from symmetries, conservation laws, effective field theory, and limiting cases through Feynman-diagram and on-shell amplitude tools, renormalization-group flow, lattice and tensor-network numerics, and the conformal bootstrap, while treating gauge-dependent artifacts, unitarity and Ward-identity violations, scheme dependence, and lattice discretization errors as first-class failure modes. |
| [X-ray / Synchrotron Scientist](scientific-agents/x-ray-synchrotron-scientist/AGENTS.md) | Reasons from photon-matter cross sections, reciprocal-space Q, absorption edges, and absorbed dose through pyFAI, GSAS-II, Athena/Artemis, BornAgain, and foil/silver-behenate calibration while treating fluorescence self-absorption, substrate Bragg misindexing, beam damage and radiation-induced reduction, and Fourier-termination ripples as first-class failure modes. |

</details>

<details>
<summary><b>Astronomy & Space Science</b> — 18 profiles</summary>

| Agent | How it reasons |
| --- | --- |
| [Astrobiologist](scientific-agents/astrobiologist/AGENTS.md) | Reasons from habitability, redox disequilibrium, and Bayesian biosignature frameworks through Mars (Perseverance, Viking perchlorate lessons), Europa Clipper ocean worlds, agnostic signatures and the Ladder of Life Detection, while treating abiotic mimics, preservation, and LUCA phylogenomics as constraints—not templates—for extraterrestrial life. |
| [Astronomer](scientific-agents/astronomer/AGENTS.md) | Reasons like a senior observational astronomer from the telescope and catalog outward — Landolt/Stetson photometry, Gaia/MPC astrometry, Horizons ephemerides, SDSS–ZTF–Rubin survey discipline, TOPCAT cross-matches, and calibrated detection vs upper-limit reporting. |
| [Astronomical Instrumentation Scientist](scientific-agents/astronomical-instrumentation-scientist/AGENTS.md) | Reasons from system-level error budgets, the diffraction limit and Strehl ratio, detector figures of merit, and resolving power through Zemax/Code V tolerancing, ETC radiometry, AO modeling, and on-sky standard-star commissioning while treating flexure drift, IR persistence, ghosts, and quasi-static speckles as first-class failure modes. |
| [Astroparticle Physicist](scientific-agents/astroparticle-physicist/AGENTS.md) | Reasons from flux times cross section times acceptance, Poisson counting over structured backgrounds, and Cherenkov photoelectron budgets through SkyLLH unbinned likelihoods, Geant4/CORSIKA chains validated on through-going-muon and calibration samples, and Feldman-Cousins/CLs limits, while treating atmospheric-neutrino and downgoing-muon contamination, ER/NR leakage and the neutrino fog, and look-elsewhere trials as first-class failure modes. |
| [Astrophysicist](scientific-agents/astrophysicist/AGENTS.md) | Reasons like a senior astrophysicist across observational, computational, and multi-messenger work — from radiative transfer and error budgets through JWST/ALMA/Rubin/LIGO pipelines, VO archives, and calibrated detection vs upper-limit reporting. |
| [Cosmologist](scientific-agents/cosmologist/AGENTS.md) | Reasons from Friedmann/ΛCDM, r_s and transfer functions, and multi-probe inference (Planck CMB, DESI BAO, lensing, Pantheon+ SNe) through CAMB/CLASS, Cobaya, and GetDist while treating photo-z–IA coupling, CMB foreground pipelines, H0/S8 tensions, and emulator extrapolation as first-class failure modes. |
| [Exoplanet Scientist](scientific-agents/exoplanet-scientist/AGENTS.md) | Reasons from Keplerian motion, transit and RV geometry, and degenerate retrieval spaces through TLS/BLS searches, centroid and odd-even vetting, RadVel and GP activity models, and petitRADTRANS retrievals while treating eclipsing-binary blends, stellar-rotation-mimicking RV signals, and look-elsewhere completeness cliffs as first-class failure modes. |
| [Galactic Astronomer](scientific-agents/galactic-astronomer/AGENTS.md) | Reasons from distance ladders, dust extinction, and survey selection functions through Gaia DR3 cross-matches, isochrone and Bayesian SFH fitting (PARSEC/MIST, Starfish), and orbit integration in named potentials (McMillan17, MWPotential2015) via galpy, Agama, and Gala, while treating parallax-S/N and RUWE failures, unresolved binaries and fiber collisions, dust-or-crowding overdensities, and spiral-arm-mimicking-streams as first-class failure modes. |
| [Gravitational-Wave Astronomer](scientific-agents/gravitational-wave-astronomer/AGENTS.md) | Reasons like a senior GW astronomer across LIGO–Virgo–KAGRA matched-filter CBC searches, calibration-aware PE, GraceDB/GWTC alert–catalog discipline, BAYESTAR/Bilby skymaps, and EM follow-up campaigns. |
| [Heliophysicist](scientific-agents/heliophysicist/AGENTS.md) | Reasons from MHD, magnetic topology, reconnection, and IMF Bz coupling through SDO/HMI magnetograms, DEM and NLFFF analysis, coronagraph GCS fitting, and WSA-ENLIL/EUHFORIA ensembles while treating LOS foreshortening, AIA stray light, force-free NLFFF breakdown, and Dst/SYM-H saturation as first-class failure modes. |
| [High-Energy Astrophysicist](scientific-agents/high-energy-astrophysicist/AGENTS.md) | Reasons from Compton/synchrotron radiative processes and compact-object energetics through HEASARC/Fermi/Swift/XMM/Chandra/NuSTAR/XRISM pipelines, XSPEC/Sherpa spectral fitting, pile-up and background systematics, blazar/GRB/TDE campaigns, and GCN multi-messenger coordination while treating RMF versioning, soft-proton flares, and look-elsewhere significance as first-class failure modes. |
| [Observational Astronomer](scientific-agents/observational-astronomer/AGENTS.md) | Reasons from the CCD signal-to-noise equation, sky- versus read-noise-limited scaling, airmass extinction and seeing laws, and a CALSPEC-anchored calibration chain through ETC-backed proposals, ccdproc/PypeIt/DRAGONS and CRDS-pinned JWST reductions, optimal extraction with telluric correction, Gaia-anchored astrometry, ZOGY difference imaging, and Rubin broker-to-TOM-to-TNS follow-up while treating IR persistence and reciprocity failure, fringing and shutter-timing errors, differential-refraction slit losses, difference-image dipoles, and red-noise-inflated light curves as first-class failure modes. |
| [Planetary Geologist](scientific-agents/planetary-geologist/AGENTS.md) | Reasons from stratigraphy and landform genesis through ISIS/GDAL/JMARS/ArcGIS, CraterTools/CSFD Tools/CraterStats2 chronology, CRISM/M3/THEMIS spectroscopy with SPLib/RELAB, and PDS archives while treating secondaries, projection/datums, and production-function choice as first-class failure modes. |
| [Planetary Scientist](scientific-agents/planetary-scientist/AGENTS.md) | Reasons from bulk density, moment of inertia, tidal Love numbers, libration, electromagnetic induction, and sample-calibrated impact-flux chronology through NAIF SPICE kernels, PDS4 archives, radio-science gravity with SHTOOLS, PSG/NEMESIS retrievals, gamma-ray/neutron and radar sounding, and COSPAR planetary-protection categories while treating non-hydrostatic shapes, plasma currents mimicking ocean induction, radar clutter and roughness mimicking ice, single-line trace-gas detections, and one-flyby snapshot bias as first-class failure modes. |
| [Radio Astronomer](scientific-agents/radio-astronomer/AGENTS.md) | Reasons from the van Cittert–Zernike relation, the RIME measurement equation, the radiometer equation, and ν⁻²/λ² plasma propagation through CASA/WSClean/DDFacet imaging, Perley–Butler flux scaling, MT-MFS and w-stacking, RM synthesis, single-dish T_A*/T_mb calibration, and PRESTO/PSRCHIVE/PINT pulsar and FRB workflows while treating missing short spacings and negative bowls, self-calibration ghosts and flux suppression, RFI masquerading as dispersed bursts, polarization leakage and beam squint, and flaring flux calibrators as first-class failure modes. |
| [Solar Physicist](scientific-agents/solar-physicist/AGENTS.md) | Reasons from magnetic field topology, plasma beta, reconnection, and radiative transfer through DEM inversion, NLFFF/PFSS extrapolation, coronal seismology, and WSA-ENLIL forecasting while treating single-channel AIA temperature claims, HMI disambiguation ambiguity at the PIL, limb projection artifacts, and Parker-spiral connectivity uncertainty as first-class failure modes. |
| [Space Weather Scientist](scientific-agents/space-weather-scientist/AGENTS.md) | Reasons from Dungey coupling and prolonged southward Bz through ICME vs. CIR/SIR drivers; uses OMNI/CDAWeb, L1 RTSW, WSA-Enlil, CCMC/CAMEL validation, SuperMAG SYM-H, GloTEC/IRI, and NOAA G/S/R scales while treating sheath-vs-cloud Bz, catalog false alarms, and Dst timing artifacts as first-class failure modes. |
| [Stellar Astrophysicist](scientific-agents/stellar-astrophysicist/AGENTS.md) | Reasons from hydrostatic and thermal balance, convective-boundary physics (Schwarzschild/Ledoux, α_MLT, overshoot), nuclear bottlenecks, and p/g/mixed-mode seismology through MESA/GYRE resolution ladders, multi-grid isochrone fitting (MIST, PARSEC, BaSTI), corrected scaling relations, 1D-LTE-vs-3D-NLTE abundance analysis, and eclipsing-binary and Gaia benchmarks while treating unconverged default-control models, asteroseismic surface effects and scaling-relation biases, NLTE-biased spectroscopic log g, grid-to-grid age systematics, and unrecognized binary or merger products as first-class failure modes. |

</details>

<details>
<summary><b>Chemistry</b> — 37 profiles</summary>

| Agent | How it reasons |
| --- | --- |
| [Analytical Chemist](scientific-agents/analytical-chemist/AGENTS.md) | Reasons from the chemical measurement process through ICH Q2(R2) and USP <621> validation, CRM traceability, EURACHEM uncertainty budgets, and HPLC/GC/LC-MS/ICP-MS workflows while treating matrix effects, SST drift, peak tailing, and ion suppression as first-class failure modes. |
| [Astrochemist](scientific-agents/astrochemist/AGENTS.md) | Reasons from gas-grain reaction networks, H₂ ortho/para and CR ionization rates through KIDA/kida.uva.2024, CDMS/JPL/Splatalogue line lists, Nautilus/UCLCHEM gas-grain models, ALMA/JWST/LIDA ice–gas linkage, XCLASS LTE fitting, and line-blending discrimination—not generic chemistry. |
| [Atmospheric Chemist](scientific-agents/atmospheric-chemist/AGENTS.md) | Reasons from coupled photochemical OH-NOx-VOC radical budgets, heterogeneous aerosol uptake, and NOx-limited versus VOC-limited regimes through MCM/F0AM and GEOS-Chem/CMAQ/WRF-Chem models, OH-reactivity closure, PMF on AMS factors, HYSPLIT trajectories, and EKMA isopleths while treating chamber wall losses, instrument cross-sensitivities and inlet artifacts, and emission-inventory error as first-class failure modes. |
| [Biochemist](scientific-agents/biochemist/AGENTS.md) | Reasons from thermodynamics, enzyme mechanisms, and binding energetics; designs orthogonal purification and assay readouts while controlling oxidation, aggregation, coupled assays, and activity-vs-abundance confounds. |
| [Biophysical Chemist](scientific-agents/biophysical-chemist/AGENTS.md) | Reasons from free energy landscapes, binding equilibria (K_d, ΔG = ΔH − TΔS), and probe–system coupling through ITC, SPR/BLI, smFRET, AUC, and global fitting (KinTek, SEDFIT) while treating probe perturbation, mass-transport-limited kon, aggregation-driven avidity, and two-state melting violations as first-class failure modes. |
| [Catalysis Scientist](scientific-agents/catalysis-scientist/AGENTS.md) | Reasons from active-site structure, turnover frequency, selectivity, and the Sabatier principle through CO/H2 chemisorption site-counting, Weisz-Prater and Mears transport checks, Langmuir-Hinshelwood/Mars-van Krevelen kinetics, and operando DRIFTS/XAS while treating diffusion-limited apparent rates, DRIFTS spectator species, mercury-test false positives for leached Pd, sintering, coking, and selectivity collapse at high conversion as first-class failure modes. |
| [Chemical Biologist](scientific-agents/chemical-biologist/AGENTS.md) | Reasons from chemical genetics, ABPP/TPP/CETSA chemoproteomics, and SGC/Portal probe criteria; deconvolves phenotypic hits with PAINS/aggregator triage, inactive analogs, and genetic epistasis while treating colloidal aggregation, probe promiscuity, and degrader DC50/Dmax tag artifacts as first-class failure modes. |
| [Cheminformatician](scientific-agents/cheminformatician/AGENTS.md) | Reasons from Standard InChI identity and RDKit sanitization through ChEMBL pChEMBL harmonization, Morgan/ECFP fingerprints, scaffold splits and applicability domains, while treating tautomer collapse, KNIME-vs-Python canonicalization drift, and random-split QSAR leakage as first-class failure modes. |
| [Colloid Chemist](scientific-agents/colloid-chemist/AGENTS.md) | Reasons from interfacial thermodynamics, DLVO and non-DLVO forces, zeta-potential, and rheology through orthogonal characterization (DLS, NTA, cryo-TEM, SAXS/SANS S(Q), pendant-drop tensiometry) and accelerated-aging stability tests while treating coalescence, Ostwald ripening, creaming, and flocculation crossing the isoelectric point as first-class failure modes. |
| [Computational Chemist](scientific-agents/computational-chemist/AGENTS.md) | Reasons from Kohn–Sham DFT, def2/D4 functional selection, and conformer ensembles through VASP/Gaussian/ORCA, AMBER/GROMACS MD, CREST/CENSO sampling, ONIOM/QM/MM electrostatic embedding, GMTKN55 validation, and SCF convergence escalation while treating B3LYP/6-31G*, BSSE, link-atom artifacts, and force-field mismatch as first-class failure modes. |
| [Crystallographer](scientific-agents/crystallographer/AGENTS.md) | Reasons from reciprocal-space diffraction data, Bragg's law, and space-group symmetry through XDS/DIALS scaling, Phaser/SHELX phasing, Coot/Olex2 building, and MolProbity/checkCIF validation while treating merohedral twinning, wrong space groups, model-bias density unsupported by omit/polder maps, and R_free overfitting as first-class failure modes. |
| [Electrochemist](scientific-agents/electrochemist/AGENTS.md) | Reason from interfacial thermodynamics and transport: Nernst sets equilibrium, Butler–Volmer sets kinetics, Levich/Randles–Ševčík set mass transport, and EIS deconvolves electrode and battery interphases. |
| [Environmental Chemist](scientific-agents/environmental-chemist/AGENTS.md) | Reasons from thermodynamic partitioning (K_oc/K_ow, Henry's law), pathway-specific half-lives, and mass balance through GC-MS/LC-MS/MS/ICP-MS analysis, EPI Suite and fugacity fate models, and EPA SW-846 QA/QC while treating blank contamination, matrix suppression, censored sub-LOD data, and unscoped transformation products as first-class failure modes. |
| [Flavor & Fragrance Chemist](scientific-agents/flavor-fragrance-chemist/AGENTS.md) | Reasons from odor activity values, threshold perception, matrix release, and degradation kinetics through GC-MS with retention indices, GC-O/AEDA, chiral GC authentication, ISO 8586 trained sensory panels, and IFRA/FEMA regulatory limits while treating aldehyde oxidation, citral cyclization, top-note fade, and allergen exceedance as first-class failure modes. |
| [Forensic Chemist](scientific-agents/forensic-chemist/AGENTS.md) | Reasons from chain of custody, validated methods, measurement uncertainty, and class-versus-individual characteristics through GC-MS, LC-MS/MS, FTIR, and SWGDRUG-aligned identification under ISO/IEC 17025, while treating carryover contamination, secondary transfer, isomer co-elution, and upgrading equivocal results into source attribution as first-class failure modes. |
| [Geochemist](scientific-agents/geochemist/AGENTS.md) | Reasons from Gibbs equilibria, mass and isotope balance, and fluid–rock interaction through stable (δ) and radiogenic (ε, isochron) systems, ICP-MS/LA-ICP-MS/TIMS/MC-ICP-MS/IRMS, PHREEQC/Perple_X phase modeling, and EarthChem/GeoReM workflows while treating alteration, matrix effects, Pb loss, mixing arrays, and Fretwell’s Law violations as first-class failure modes. |
| [Green Chemist](scientific-agents/green-chemist/AGENTS.md) | Reasons from Anastas–Warner 12 principles, Trost atom economy, and PMI/MMI/E-factor mass metrics; selects solvents via CHEM21/GSK/ACS GCIPR guides, integrates catalysis and LCA (ISO 14040), and aligns REACH/CSS with ACS GC&E benchmarking. |
| [Inorganic Chemist](scientific-agents/inorganic-chemist/AGENTS.md) | Reasons from electron counting, ligand field theory, and HSAB matching through Schlenk/glovebox air-sensitive synthesis, SCXRD/checkCIF validation, Evans/EPR/XANES oxidation-state assignment, and hot-filtration leaching tests while treating paramagnetic NMR overinterpretation, mystery-oil misidentification, and DFT-without-multiplicity claims as first-class failure modes. |
| [Isotope Geochemist](scientific-agents/isotope-geochemist/AGENTS.md) | Reasons from fractionation theory, decay schemes, reservoir mixing, and closure assumptions through standard-sample bracketing, double-spike deconvolution, isochron/Tera-Wasserburg fitting with MSWD, and ISO Guide uncertainty propagation while treating Pb-blank and lab-air contamination, mass bias, Pb loss and inheritance, and open-system resetting as first-class failure modes. |
| [Mass Spectrometrist](scientific-agents/mass-spectrometrist/AGENTS.md) | Reasons from ion formation, m/z resolution and mass accuracy, fragmentation, and calibrated ion statistics through ESI/APCI/MALDI tuning, CID/HCD/ETD MS/MS, isotope-pattern formula assignment, and spectral libraries (NIST, mzCloud, GNPS) under FDA/ICH M10/MSI tiers, while treating matrix suppression, PEG/siloxane/keratin contamination, decoy-driven FDR inflation, and unassigned adducts as first-class failure modes. |
| [Materials Chemist](scientific-agents/materials-chemist/AGENTS.md) | Reasons from Kröger–Vink defect equilibria, soft-chemistry routes (sol-gel, hydrothermal, ALD), and structure–property links; validates with GSAS-II/TOPAS Rietveld QPA, GIPAW ssNMR, ICSD/COD/Materials Project, and XPS/BET protocols while treating preferred orientation, AdC mis-referencing, degas artifacts, and metastable phase traps as first-class failure modes. |
| [Medicinal Chemist](scientific-agents/medicinal-chemist/AGENTS.md) | Reasons from structure-activity relationships, lipophilicity and unbound-fraction physicochemistry, synthetic accessibility, and target-product-profile multiparameter optimization through LLE/Fsp3/QED scoring, FEP+/Glide docking validated against co-crystal and SPR data, ELN-tracked LC-MS/NMR synthesis, and DMPK panels (microsomal CL, Caco-2 efflux, hERG, CYP) while treating PAINS and aggregation assay artifacts, biochemical-versus-cellular potency gaps, reactive-metabolite soft spots, and freedom-to-operate cliffs as first-class failure modes. |
| [Natural Products Chemist](scientific-agents/natural-products-chemist/AGENTS.md) | Reasons from dereplication (GNPS FBMN, NPAtlas, SNAP-MS, COCONUT), bioassay-guided and MS-triggered isolation, NMR/HRMS structure tiers (DP4+/DU8+), antiSMASH/MIBiG BGC linkage, and PAINS/IMP assay interference while treating HMBC ambiguity, stereochemical misassignment, and aggregator false positives as first-class failure modes. |
| [Nuclear Chemist](scientific-agents/nuclear-chemist/AGENTS.md) | Reasons from decay-corrected activity ledgers, decay modes and cross sections, and ALARA dose control through Bateman/ORIGEN modeling, extraction-chromatography separations (TRU/Sr/TEVA resins), and HPGe/alpha/LSC spectroscopy while treating daughter ingrowth, generator breakthrough, spectral pile-up and sum peaks, and swipe-test cross-contamination as first-class failure modes. |
| [Organic Chemist](scientific-agents/organic-chemist/AGENTS.md) | Reasons from retrosynthesis, protecting-group strategy, and stereoelectronics; executes air-sensitive chemistry, flash/LC-MS purification, and NMR/IR/MS proof; mines SciFinder/Reaxys and reports ACS-grade experimentals with E-factor/PMI and pyrophoric safety discipline. |
| [Organometallic Chemist](scientific-agents/organometallic-chemist/AGENTS.md) | Reasons from electron counting, oxidation states, and elementary catalytic steps through Schlenk/glovebox technique, multinuclear NMR and νCO IR, SCXRD with checkCIF, and TON/TOF kinetics while treating air oxidation to oxo/hydroxo species, paramagnetic line-broadening, and trace or colloidal-metal leaching as first-class failure modes. |
| [Petrochemist](scientific-agents/petrochemist/AGENTS.md) | Reasons from boiling range, hydrocarbon class, sulfur/nitrogen speciation, and octane/cetane drivers through SimDist and PIONA/SARA group-type analysis, CFR-engine RON/MON and cetane testing, refinery LP models, and ASTM/EN spec methods, while treating light-ends loss, assay mismatch versus plant yields, catalyst end-of-run deactivation, and asphaltene instability as first-class failure modes. |
| [Photochemist](scientific-agents/photochemist/AGENTS.md) | Reasons from Jablonski diagrams, quantum yields, and excited-state potential energy surfaces through ferrioxalate actinometry, TCSPC and transient-absorption flash photolysis, Stern–Volmer quenching, and TDDFT/CASPT2 calculations while treating inner-filter distortion, oxygen-sensitive triplet pathways, photodegradation mistaken for reaction, and emission from impurities as first-class failure modes. |
| [Physical Chemist](scientific-agents/physical-chemist/AGENTS.md) | Reasons from state functions, partition functions, rate laws, and selection rules through Eyring and van't Hoff fits, DSC/ITC calorimetry, and stopped-flow spectroscopy anchored to NIST thermochemical data, while treating inner-filter and aggregation artifacts, curved Arrhenius plots from mechanism change, and concentration-for-activity substitution as first-class failure modes. |
| [Polymer Chemist](scientific-agents/polymer-chemist/AGENTS.md) | Designs and interprets polymer synthesis, characterization, and structure–property relationships from mechanism (chain-growth, step-growth, RDRP, ROMP) through absolute MW verification to application-relevant thermal and rheological data. |
| [Process Chemist](scientific-agents/process-chemist/AGENTS.md) | Reasons from mass and energy balances, impurity fate maps, and supersaturation trajectories through RC1 calorimetry, DoE in JMP/MODDE, FBRM/XRPD crystallization tracking, and ICH Q8/Q9/Q11 control strategy while treating exotherm runaway at plant jacket capacity, ICH M7 genotoxic carry-over, polymorph shifts on scale, and unvalidated PAT release as first-class failure modes. |
| [Quantum Chemist](scientific-agents/quantum-chemist/AGENTS.md) | Reasons from the Schrödinger equation through HF, MP2/CCSD(T)/CBS, and multireference (CASSCF/CASPT2); uses ORCA/Psi4/Gaussian with GMTKN55/WTMAD-4 validation, T1/D1 diagnostics, Helgaker CBS extrapolation, and BSSE/spin-contamination checks while treating SCF near-degeneracy, intruder states, and global-vs-local multireference masking as first-class failure modes. |
| [Radiochemist](scientific-agents/radiochemist/AGENTS.md) | Reasons from radionuclide half-life, specific activity, radiochemical purity, and dosimetry through analytical/prep HPLC with radiodetector, iTLC, HPGe γ-spectroscopy, OLINDA/MIRD, and USP <823>/EANM release specs while treating defluorination, transchelation of ⁶⁸Ga/⁸⁹Zr, ⁹⁹ᵐTc colloid and ⁶⁸Ge breakthrough as first-class failure modes. |
| [Spectroscopist](scientific-agents/spectroscopist/AGENTS.md) | Reasons from selection rules, line shapes as convolutions of intrinsic and instrument broadening, and Beer-Lambert linearity through UV-Vis, fluorescence, IR/Raman, NMR, CD, EPR, and XAS/XPS with calibration standards (polystyrene 1601 cm⁻¹, TMS/DSS, C 1s 284.8 eV) while treating inner filter effects, baseline artifacts inventing peaks, Fermi resonances, and X-ray beam damage as first-class failure modes. |
| [Supramolecular Chemist](scientific-agents/supramolecular-chemist/AGENTS.md) | Reasons from noncovalent binding free energies (ΔG = ΔH − TΔS), host-guest complementarity, and cooperative assembly through ITC, NMR titration with global fitting (Bindfit, SupraFit), Job's method, and SCXRD while treating wrong-stoichiometry K fits, kinetic traps mistaken for thermodynamic products, ITC dilution-dominated heats, and crystal packing assumed to dominate solution as first-class failure modes. |
| [Surface Chemist](scientific-agents/surface-chemist/AGENTS.md) | Reasons from interfacial thermodynamics, Langmuir/BET/D-R adsorption, and Young–Dupré wetting through XPS (ISO 15472/18118, AdC vacuum-level alignment, SESSA), contact-angle SFE (OWRK/vOCG, ASTM D7490), QCM-D viscoelastic modeling, ToF-SIMS, SAMs, and ISO 20579 handling while treating adventitious carbon, charging, siloxane contamination, Cassie–Wenzel states, and tip convolution as first-class failure modes. |
| [Theoretical Chemist](scientific-agents/theoretical-chemist/AGENTS.md) | Reasons from Hamiltonians, partition functions, and flux through dividing surfaces using validated potential energy surfaces, variational transition state theory with Eckart and small-curvature tunneling (Polyrate), and master-equation falloff solvers (MESMER, MultiWell), while treating spurious saddle imaginary modes, spin contamination, recrossing, and silent single-surface MD across conical intersections as first-class failure modes. |

</details>

<details>
<summary><b>Materials, Nanoscience & Energy</b> — 22 profiles</summary>

| Agent | How it reasons |
| --- | --- |
| [Biomaterials Scientist](scientific-agents/biomaterials-scientist/AGENTS.md) | Reasons from material-biology interfaces, degradation-product toxicity, and mechanical mismatch to host tissue through ISO 10993 biological evaluation plans, ISO 10993-12 extract conditions, GPC/ICP/SEM characterization, and sterilization validation while treating endotoxin contamination, pH shift from acidic degradation, extract-ratio artifacts, and non-final-form test articles as first-class failure modes. |
| [Ceramics Engineer](scientific-agents/ceramics-engineer/AGENTS.md) | Reasons from crystal chemistry, defect equilibria, sintering densification, and flaw statistics through XRD/Rietveld, dilatometry, SEM fractography, impedance spectroscopy, and Weibull analysis per ASTM C1161/C1239/C1421 while treating surface grinding flaws, Pb/alkali volatilization, closed-pore traps, and thermal-expansion-mismatch cracking as first-class failure modes. |
| [Composites Engineer](scientific-agents/composites-engineer/AGENTS.md) | Reasons from CLT/ABD laminate mechanics, Halpin–Tsai micromechanics, and CMH-17/NCAMP allowables through autoclave/OOA/RTM process control, ASTM D30 mechanical qualification, ultrasonic C-scan and CAI damage tolerance while treating fiber waviness, void content, under-cure, and quasi-isotropic strength traps as first-class failure modes. |
| [Corrosion Engineer](scientific-agents/corrosion-engineer/AGENTS.md) | Reasons from electrochemical couples, Pourbaix/galvanic selection, and ISO 15156 sour-service limits through AMPP SP0169/SP0502 CP and ECDA, CO₂ models (NORSOK M-506, OLI), coupon/ER/LPR monitoring, and ASTM G5/G48/G61 qualification while treating IR-masked CIPS, salt-spray overclaim, MIC vs. biocide residual, and MR0175≠fit-for-service as first-class failure modes. |
| [Crystal Growth Specialist](scientific-agents/crystal-growth-specialist/AGENTS.md) | Reasons from thermodynamic driving force, interface stability, constitutional supercooling, and dopant segregation (keff vs. k0, G/R) through Cz/Bridgman/FZ/LEC/PVT growth, CGSim and phase-field simulation, XRT topography, etch-pit counting, and FTIR/SIMS mapping while treating striations, inclusions, crucible-reaction contamination, and cool-down slip and cracking as first-class failure modes. |
| [Electronic Materials Engineer](scientific-agents/electronic-materials-engineer/AGENTS.md) | Reasons from band alignment, defect chemistry, and process–structure–property links; correlates Hall, C–V (Dit), XRD/RSM, SIMS, and ALD/MOCVD/sputtering recipes while treating dopant activation vs. chemical dose, high-κ trap charging, and reliability (NBTI/TDDB) as first-class failure modes. |
| [Energy Storage / Battery Scientist](scientific-agents/energy-storage-battery-scientist/AGENTS.md) | Reasons from interfacial thermodynamics, ion transport, SEI/CEI dynamics, and cell engineering constraints (N/P and E/S ratio, mass loading) through galvanostatic cycling, dQ/dV, GITT and EIS/DRT, operando XRD, and PyBaMM/Newman models, while treating Li plating, lithium-inventory loss, transition-metal crossover, and coin-cell artifacts as first-class failure modes. |
| [Materials Physicist](scientific-agents/materials-physicist/AGENTS.md) | Reasons from band structure, defects, strain, and Landau order parameters; integrates HRXRD/RSM, ARPES, TEM/4D-STEM, van der Pauw transport, and SQUID/MOKE with Materials Project/VASP while treating matrix-element ARPES artifacts, substrate-dominated GIXRD, contact-resistance Hall errors, and DFT gap overclaim as first-class failure modes. |
| [Materials Scientist](scientific-agents/materials-scientist/AGENTS.md) | Reasons from CALPHAD phase diagrams, Scheil solidification, and Hall–Petch microstructure–property links; validates with XRD Rietveld QPA, EBSD, TEM/STEM, and ASTM mechanical testing while treating preferred orientation, FIB Ga artifacts, EBSD overlap, and Rietveld overfitting as first-class failure modes. |
| [Metallurgist](scientific-agents/metallurgist/AGENTS.md) | Reasons from phase diagrams, TTT/CCT paths, and Scheil solidification through Jominy hardenability (ASTM A255), ASM heat-treat cycles, metallography (ASTM E3/E112/E407), and staged failure analysis while treating decarburization, quench cracking, HAZ liquation, hot tearing, and microsegregation as first-class failure modes. |
| [Nanomaterials Scientist](scientific-agents/nanomaterials-scientist/AGENTS.md) | Reasons from size-dependent thermodynamics, surface-to-volume ratio, and DLVO colloidal stability through TEM/STEM statistics, DLS/NTA, XRD Scherrer, XPS, ICP-MS, and PL quantum-yield methods while treating aggregation, beam damage, intensity-weighted DLS sizing bias, and Ostwald ripening as first-class failure modes. |
| [Nanotechnologist](scientific-agents/nanotechnologist/AGENTS.md) | Reasons from length-scale manufacturing limits, EUV/NIL/EBL patterning, DSA defectivity, and interface-controlled integration through CD-SEM/AFM/TEM metrology, SEMI E10 yield discipline, and ISO 80004/FDA nanomaterial reporting while treating SEM shrinkage, NIL residual-layer non-uniformity, overlay error, and cherry-picked die yield as first-class failure modes. |
| [Optoelectronics Engineer](scientific-agents/optoelectronics-engineer/AGENTS.md) | Reasons from photon–electron conversion, ABC recombination, and IQE/EQE/WPE budgets; runs LIV/pulsed laser, EMVA 1288, and responsivity metrology; designs with Lumerical/Sentaurus/COMSOL TCAD and foundry PDKs while treating efficiency droop, thermal rollover, LIV kinks, and calibration geometry as first-class failure modes. |
| [Photonics Engineer](scientific-agents/photonics-engineer/AGENTS.md) | Reasons from Maxwell modes, FSR–Q–coupling trade-offs, and optical power/loss budgets; designs PICs and free-space systems with FDTD/INTERCONNECT/Zemax/GDSFactory and certifies links with OLTS/OTDR/M² while treating mesh dispersion errors, TE/TM birefringence, APC/PC connector mismatch, OTDR ghost/gainer events, and Fabry–Pérot convolution artifacts as first-class failure modes. |
| [Photovoltaics / Solar Cell Scientist](scientific-agents/photovoltaics-solar-cell-scientist/AGENTS.md) | Reasons from the Shockley-Queisser detailed-balance limit and the diode coupling of Voc, Jsc, FF, and Rs/Rsh through light I-V, Suns-Voc implied Voc, EQE integration, lifetime mapping (QSSPC, μ-PCD, DLTS), and IEC 60904/61215 qualification while treating spectral mismatch, surface-recombination and shunt losses, perovskite hysteresis and ion migration, and PID/LID-LeTID degradation as first-class failure modes. |
| [Polymer Scientist](scientific-agents/polymer-scientist/AGENTS.md) | Reasons from molecular weight distribution, Tg/Tm and crystallinity, viscoelasticity, and phase behavior through GPC/SEC, DSC heat-cool-heat, capillary and oscillatory rheology, WAXD/SAXS, and DMA while treating thermal-history erasure, moisture hydrolysis, incomplete cure, and wrong-grade-lot artifacts as first-class failure modes. |
| [Renewable Energy Scientist](scientific-agents/renewable-energy-scientist/AGENTS.md) | Reasons from resource-to-energy conversion, P50/P90 yield risk, LCOE/LCA boundaries, IEC monitoring, and grid constraints while troubleshooting PV soiling/PID/clipping, wind wakes/icing/yaw, hydro drought, geothermal scaling, and biomass feedstock variability. |
| [Semiconductor Device Engineer](scientific-agents/semiconductor-device-engineer/AGENTS.md) | Reasons from electrostatics, capacitance-current MOSFET physics, interface-trap behavior, and self-heating through I-V/C-V extraction ladders, Sentaurus TCAD calibrated to silicon splits, BSIM-CMG compact modeling, and JEDEC reliability stress while treating uncalibrated TCAD, unstated constant-current Vt references, ignored BTI partial recovery, and self-heating-distorted DC Ron as first-class failure modes. |
| [Semiconductor Materials Scientist](scientific-agents/semiconductor-materials-scientist/AGENTS.md) | Reasons from band structure, defect energetics, and process–structure–property links; grows and characterizes bulk and epitaxial semiconductors (Si, III–V, SiC, GaN, 2D) via MOCVD/MBE/HVPE, Hall/DLTS/XRD/RSM/ECCI/TEM/SIMS, and DFT defect levels while treating compensation, Fermi-level pinning, threading dislocations, and polytype mixing as first-class failure modes. |
| [Superconductivity Scientist](scientific-agents/superconductivity-scientist/AGENTS.md) | Reasons from BCS/Eliashberg/GL order parameters, pairing symmetry, and vortex physics; validates Tc with Meissner/χ/C triads, phase-sensitive Josephson tests, ARPES/STM gaps, and EPW; uses SuperCon/3DSC and IEC 61788 Ic standards while treating filamentary transitions, pseudogap misreads, DAC flux trapping, and HTS quench detection gaps as first-class failure modes. |
| [Thin-Film Scientist](scientific-agents/thin-film-scientist/AGENTS.md) | Reasons from nucleation and growth modes, film stress, interfacial adhesion, and conformality across topography through spectroscopic ellipsometry, XRR, Stoney wafer-curvature, XPS/RBS, and standards like ASTM E2244 and ISO 9211 while treating columnar porosity, barrier pinholes, reactive-sputter hysteresis drift, and uncalibrated-QCM thickness error as first-class failure modes. |
| [Tribologist](scientific-agents/tribologist/AGENTS.md) | Reasons from contact mechanics, lubricant rheology, Stribeck-regime and λ ratio through Hamrock-Dowson EHL film estimates, pin-on-disk/four-ball/SRV/FZG bench tests and SEM-EDS/ferrography scar analysis while treating scuffing, rolling-contact pitting, three-body abrasion and DLC adhesive transfer as first-class failure modes. |

</details>

<details>
<summary><b>Earth, Environmental & Atmospheric Science</b> — 58 profiles</summary>

| Agent | How it reasons |
| --- | --- |
| [Aeronomy Scientist](scientific-agents/aeronomy-scientist/AGENTS.md) | Reasons from MLT lidar and ISR profiles through IRI/NRLMSIS benchmarks, treating ion-line spectra, metal-layer winds, and storm-time TEC as distinct observables. |
| [Air Quality Scientist](scientific-agents/air-quality-scientist/AGENTS.md) | Reasons from source emissions through transformation, transport, and dose using SMOKE/MOVES inventories, WRF-driven CTMs like CMAQ and CAMx, PMF/ME-2 apportionment, and concentration-response functions, while treating rotational PMF ambiguity, AOD-to-PM bias in humid regions, uncalibrated low-cost sensors, and untreated wildfire exceptional events as first-class failure modes. |
| [Atmospheric Scientist](scientific-agents/atmospheric-scientist/AGENTS.md) | Reasons from scale-dependent balances, Ertel PV on isentropic surfaces, and closed moisture/energy budgets through PV/omega/Q-vector diagnostics, reanalyses (ERA5, MERRA-2) and WRF/MPAS/CMIP runs, and obs validation (GRUAN sondes, IMERG, CERES), while treating reanalysis assimilation increments, retrieval biases, parameterized-vs-resolved convection, and internal-variability masking of forced trends as first-class failure modes. |
| [Biogeochemist](scientific-agents/biogeochemist/AGENTS.md) | Reasons from coupled C/N/P/S redox cycles through TEAP zonation, porewater Rhizon-peeper sampling, δ13C/δ15N/δ34S tracers, chamber and eddy-covariance fluxes, and Century/DayCent SOM modeling while treating porewater O2 contamination and nitrification-denitrification coupling errors as first-class failure modes. |
| [Biological Oceanographer](scientific-agents/biological-oceanographer/AGENTS.md) | Reasons from light-nutrient-grazing coupling, the microbial loop, and size-structured export through CTD/MOCNESS sampling, 14C and O2/Ar production with 234Th export flux, imaging and flow cytometry enumeration, and SILVA/PR2 metabarcoding while treating spatial patchiness, diel-migration tow aliasing, CDOM-biased chlorophyll algorithms, and eDNA-detection-as-abundance as first-class failure modes. |
| [Carbon Cycle Scientist](scientific-agents/carbon-cycle-scientist/AGENTS.md) | Reasons from carbon mass balance across reservoirs and timescales, sign conventions, and budget closure through the Global Carbon Budget protocol, ONEFlux/REddyProc eddy-covariance processing, atmospheric inversions (CarbonTracker, CAMS, GEOS-Chem), Δ¹⁴C/δ¹³C isotopic partitioning, and ILAMB model evaluation while treating NEE sign mismatches, gap-filled GPP read as measured, fixed-depth SOC comparisons, and uncounted lateral aquatic carbon export as first-class failure modes. |
| [Chemical Oceanographer](scientific-agents/chemical-oceanographer/AGENTS.md) | Reasons from seawater thermodynamics, carbonate-system coupling (DIC, TA, pH, pCO2), redox hierarchies, and tracer conservation on density surfaces through CO2SYS/seacarb with Dickson CRMs, Winkler oxygen, IRMS isotopes, GO-FLO clean trace-metal sampling, and GLODAP/SOCAT/GEOTRACES synthesis while treating organic alkalinity, headspace equilibration, pCO2-mooring biofouling, and trace-metal contamination as first-class failure modes. |
| [Climate Risk Analyst](scientific-agents/climate-risk-analyst/AGENTS.md) | Reasons from TCFD/IFRS S2 four-pillar disclosure, NGFS Phase V orderly/disorderly/hot-house scenarios, hazard–exposure–vulnerability and RMS/AIR/CLIMADA cat economics, transition carbon-price and stranded-asset pathways, and PCAF financed emissions while treating exposure geocoding quality, Kotz damage-function retraction, and scenario-not-forecast misuse as first-class failure modes. |
| [Climate Scientist](scientific-agents/climate-scientist/AGENTS.md) | Reasons from ERF/EEI energy-budget closure, AR6 forcing (WMGHG vs ERFaci), optimal fingerprinting and FAR event attribution, CMIP6/ScenarioMIP SSP workflows (ESGF, ESMValTool), and paleo proxy physics (PAGES2k, ice-core δD/CO₂, foraminifera Mg/Ca, coral Sr/Ca) while treating aerosol uncertainty, tree-ring divergence, CMIP tuning circularity, and TLS under-coverage as first-class failure modes. |
| [Climatologist](scientific-agents/climatologist/AGENTS.md) | Characterizes climate via WMO CLINO baselines (1991–2020 vs 1961–1990), ETCCDI indices, and teleconnection modes; bridges ERA5 climatology to CMIP6/ScenarioMIP SSP deltas (xsdba/QDM), optimal-fingerprint attribution, AR6 ERF/ECS/TCR, and proxy reconstructions (CPS/EIV, PAGES2k, MXD divergence)—distinct from weather forecasting and generic physical-climate narration. |
| [Conservation Scientist](scientific-agents/conservation-scientist/AGENTS.md) | Reasons from measurable biodiversity change, counterfactual impact, and effective population size through IUCN Red List/Green Status criteria, occupancy and PVA models (unmarked, Vortex), Marxan/prioritizr planning, and BACI/matching designs while treating detection heterogeneity, spatial pseudoreplication, REDD+ leakage, and Ne sample bias as first-class failure modes. |
| [Cosmochemist](scientific-agents/cosmochemist/AGENTS.md) | Reasons from oxygen three-isotope taxonomy (Δ17O), chondrite–achondrite classification, and presolar grain NanoSIMS through Meteoritical Bulletin curation, Al–Mg and Pb–Pb isochrons, CRE vs formation-age separation, and clean-lab sample prep while treating terrestrial weathering, mount contamination, and breccia mixing as first-class failure modes. |
| [Economic Geologist](scientific-agents/economic-geologist/AGENTS.md) | Reasons from mineral systems and deposit-type models (porphyry, VMS, orogenic Au, SEDEX, IOCG) through regolith and lithogeochemistry, LA-ICP-MS sulfide fingerprinting, and geophysical vectors to JORC/CIM/NI 43-101 MRE domaining, variography, OK/MIK estimation, and classification while treating transported regolith, dispersion shadows, pXRF false highs, and Inferred-overclaim as first-class failure modes. |
| [Environmental Policy Analyst](scientific-agents/environmental-policy-analyst/AGENTS.md) | Reasons from statutory authority, baseline definition, and monetization boundaries through NEPA/ESA compliance, Circular A-4 RIAs, EPA SC-GHG and benefit transfer, IAM/IPCC scenario use, and APA regulatory comment while treating discount-rate dominance, weak transfer extrapolation, IAM structural uncertainty, and baseline inflation as first-class failure modes. |
| [Environmental Scientist](scientific-agents/environmental-scientist/AGENTS.md) | Reasons from source-pathway-receptor linkages, multimedia partitioning, and dose-as-exposure through conceptual site models, fate models (MODFLOW/MT3DMS, AERMOD), SW-846 QA/QC chains, and ProUCL/Mann-Kendall statistics while treating censoring bias, conceptual-model error, well-construction artifacts, and seasonal confounding as first-class failure modes. |
| [Forestry Scientist](scientific-agents/forestry-scientist/AGENTS.md) | Reasons from silvicultural systems, site index, DGH and DBH increment, and FIA cruise design through FVS/ORGANON calibration, LiDAR area-based inventory with support matching, and IPCC carbon pools while treating site-index misassignment, plot edge effects, and change-of-spatial-support bias as first-class failure modes. |
| [Geobiologist](scientific-agents/geobiologist/AGENTS.md) | Reasons from metabolism, redox geochemistry, microbe-mineral interactions, and diagenetic filters through stromatolite microfabric petrography, CSIA and clumped-isotopologue analysis, nanoSIMS-FISH mapping, and NASA's Ladder of Life Detection while treating Fischer-Tropsch-type synthesis, serpentinization, Rayleigh distillation, drilling-fluid contamination, and epigenetic overprint as first-class failure modes. |
| [Geodesist](scientific-agents/geodesist/AGENTS.md) | Reasons from coordinates as four-dimensional objects with epoch, velocity, and frame realization (ITRS vs. ITRF2020, WGS84) through GAMIT/GLOBK and Bernese PPP-AR, SBAS/PS-InSAR with GACOS atmospheric correction, IERS Conventions, and 14-parameter Helmert transforms while treating ITRF-realization switches, undocumented APC/ATX mismatches, monument motion, and unscreened seasonal loading as first-class failure modes. |
| [Geodynamics & Tectonics Scientist](scientific-agents/geodynamics-tectonics-scientist/AGENTS.md) | Reasons from plate kinematics, lithospheric rheology, and interseismic-versus-coseismic strain partitioning through GAMIT/GLOBK and MintPy geodesy, Okada/viscoelastic slip inversion, OxCal paleoseismic chronologies, ASPECT mantle modeling, and OpenQuake/USGS NSHM hazard while treating InSAR atmospheric delay, monument instability, unmodeled postseismic afterslip, and incompatible-timescale rate stacking as first-class failure modes. |
| [Geographic Information Scientist (GIS)](scientific-agents/geographic-information-scientist-gis/AGENTS.md) | Reasons from location, topology, scale, and positional uncertainty through PostGIS/GDAL pipelines, explicit EPSG/datum choices, kriging with cross-validated variograms, and ISO 19115/FGDC metadata while treating MAUP and ecological fallacy, Web Mercator area statistics, floating-point slivers and broken topology, and spatial-autocorrelation-inflated significance as first-class failure modes. |
| [Geological Oceanographer](scientific-agents/geological-oceanographer/AGENTS.md) | Reasons from sediment transport mechanics, stratigraphic context, and accommodation through multibeam (EM122/EM712) and sub-bottom/seismic imaging, gravity and piston cores with XRF/X-ray CT, CTD tow-yo ORP/Mn/CH4 plume surveys, and Bouma/Lowe facies analysis, while treating bathymetry-mimicking multipath artifacts, bioturbation homogenizing event beds, glacial isostasy mistaken for eustasy, and single-core turbidite extrapolation as first-class failure modes. |
| [Geologist](scientific-agents/geologist/AGENTS.md) | Reasons from Steno's principles and Walther's Law through Brunton strike/dip, measured sections, hand-lens rock ID (QAPF/Folk/Dunham), thin-section petrography (PPL/XPL, Michel-Lévy, point counting), FGDC/GeMS geologic maps, NGMDB/Geolex/Macrostrat, and stereonet structural analysis while treating weathering, float, and map-as-hypothesis as first-class failure modes. |
| [Geomagnetist](scientific-agents/geomagnetist/AGENTS.md) | Reasons from spherical-harmonic main-field theory and remanence physics through IGRF-14/WMM2025 vs CHAOS-8 SV, INTERMAGNET baseline adoption (IBFV2.00), Swarm quiet-time modeling, stepwise AF/thermal demagnetization with PCA/Fisher, GEOMAGIA50/MagIC archaeomagnetic SVCs, and GFZ Kp/ap indices while treating geomagnetic jerks, IGRF epoch mismatch, VRM/CRM overprints, and Day-diagram mixed-carrier traps as first-class failure modes. |
| [Geomorphologist](scientific-agents/geomorphologist/AGENTS.md) | Reasons from coupled form, process, and time and from rates, thresholds, and lag times through field mapping, lidar/SfM DEM morphometry (chi profiles, Ksn in LSDTopoTools/Landlab), cosmogenic nuclide dating (CRONUS-Earth, OSL, U-Th), and landscape-evolution models, while treating equifinality, inheritance, DEM artifacts, and steady-state assumed over transient response as first-class failure modes. |
| [Geophysicist](scientific-agents/geophysicist/AGENTS.md) | Reasons from wavelength and skin-depth limits through earthquake catalogs (USGS ComCat, ObsPy/FDSN), Bouguer/IGRF gravity-magnetics, MT distortion and dimensionality, and SEG-Y reflection processing (NMO, migration) while treating statics, galvanic distortion, velocity ambiguity, and header mis-mapping as first-class failure modes. |
| [Geotechnical Scientist](scientific-agents/geotechnical-scientist/AGENTS.md) | Reasons from Terzaghi effective stress, Mohr–Coulomb/CSSM, and consolidation/seepage through SPT/CPTU (Robertson SBT), triaxial/oedometer (ASTM D-series), Boulanger–Idriss liquefaction, Hoek–Brown/GSI rock mass, EC7 characteristic values, and PLAXIS/Slide2/RS2/GeoStudio workflows while treating sample disturbance, N-value correction chains, spatial variability, and LEM-vs-FEM mismatch as first-class failure modes. |
| [Glaciologist](scientific-agents/glaciologist/AGENTS.md) | Reasons from mass-budget closure (SMB, dynamic discharge, calving), Glen flow law, and subglacial effective pressure through WGMS/GlaMBIE stake networks, ICESat-2/CryoSat altimetry with firn and radar-penetration corrections, ITS_LIVE velocities, ApRES basal melt, RES/MCoRDS bed picks, RGI/BedMachine inventories, OGGM mountain-glacier projections, and PISM/ISSM ISMIP6/7 protocols while treating firn-compaction aliasing, DEM penetration bias, GRACE leakage/GIA, and tidal InSAR artifacts as first-class failure modes. |
| [Hydrogeologist](scientific-agents/hydrogeologist/AGENTS.md) | Reasons from Darcy's law, mass conservation, aquifer heterogeneity, and coupled biogeochemical transport through Theis and Cooper-Jacob aquifer-test analysis, MODFLOW/MT3DMS modeling with PEST uncertainty, and low-flow geochemical sampling while treating wellbore-storage and skin artifacts, equivalent-porous-medium failure in fractured/karst flow, and non-unique K-S calibration as first-class failure modes. |
| [Hydrologist](scientific-agents/hydrologist/AGENTS.md) | Reasons from hydrologic-cycle closure (P = ET + Q + ΔS + I), runoff-generation mechanisms, and channel routing through HEC-HMS, HEC-RAS, the National Water Model, and split-sample KGE/NSE/PBIAS calibration, while treating post-flood rating-curve shifts, radar QPE bias, snow/rain misclassification, and non-stationarity in extremes as first-class failure modes. |
| [Industrial Ecologist](scientific-agents/industrial-ecologist/AGENTS.md) | Reasons from mass balance closure, in-use stocks, and system boundaries through STAN (ÖNorm S 2096), dynamic MFA with Weibull lifetime distributions, EEIO tables (EXIOBASE, USEEIO) and pe