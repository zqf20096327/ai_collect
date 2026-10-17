# Noisegate: a differential-privacy gateway for untrusted AI agents

[![CI](https://github.com/yashmahajan10/llm-differential-privacy-gateway/actions/workflows/ci.yml/badge.svg)](https://github.com/yashmahajan10/llm-differential-privacy-gateway/actions/workflows/ci.yml)
[![Python 3.13+](https://img.shields.io/badge/python-3.13%2B-blue.svg)](pyproject.toml)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)

**An AI agent that can study sensitive data without being able to single anyone out. The limit is mathematical, it's enforced in code the agent can't reach, and the repo ships the attacks that try to break it.**

<p align="center">
  <img src="docs/assets/demo.gif" height="600" alt="A Claude Desktop chat against the gateway: an AI agent gets honest noise-injected charts, is told the model itself cannot disable the noise, drains a tiny privacy budget until the gate refuses, has a too-narrow census query rejected at the trust boundary, and ends on a clean 16-bar histogram usable at scale">
</p>

<sub>A recorded Claude Desktop session (replies trimmed; the chart cards are the session's own). An AI agent breaks 20 patients down by diagnosis, and the ±12 noise swamps every bin. Reminded that it cannot turn the noise off, it drains a three-answer budget until the gate returns a **refusal** instead of a quieter answer. On the 32,561-row census, a too-narrow slice is **rejected at the trust boundary**, while a full education breakdown comes back clean at scale. The refusal and the rejection are the live gateway's real enforcement, reproduced by `python scripts/render_demo_gif.py`.</sub>

## At a glance

- **Runnable attacks, pinned in CI.** Three classic privacy attacks run against the system's own engine: differencing, membership inference, and singling out by re-identification. Each one is shown succeeding with privacy off, defeated with privacy on, and checked on every build so the defense cannot quietly rot.
- **Independently verified math.** The noise mechanism is built from scratch, and it matches [OpenDP](https://opendp.org/), the industry reference implementation, in all 35 noise-scale checks to within 1e-9.
- **More questions from tighter accounting.** At the deployment's per-query ε, hybrid zCDP composition admits **308** queries against the same budget, against 268 under advanced composition and 100 under naive sum-of-ε. The guarantee is (ε, δ)-DP rather than pure ε.
- **Built for AI agents.** Runs as an MCP server for Claude Desktop. The connecting agent is untrusted by design, and every privacy property is enforced below it.
- **Stack:** Python · DuckDB · FastAPI · Streamlit · MCP SDK · Docker · GitHub Actions, with a 250+ test suite in CI.

---

You ask questions about a sensitive dataset in plain English. An LLM compiles each question into a small, constrained query. A differential-privacy engine executes it under a tracked privacy budget and returns a deliberately *noisy* answer with a stated confidence interval. Like [its audio namesake](https://en.wikipedia.org/wiki/Noise_gate), the gateway keeps every signal below a set threshold under the noise floor: any one individual's contribution is drowned out, while signal at the scale of the whole dataset passes through nearly untouched.

The interesting part isn't that an LLM can write queries. It's that **the privacy guarantee does not depend on the LLM being trustworthy.** The model is a convenience that proposes a query. It enforces nothing. Every privacy property is enforced downstream, by components that would behave the same way if a human typed the query by hand. This is the trust-boundary discipline you'd apply to any untrusted input in a production system, applied here to an AI agent.

---

## Quickstart

### 1. Run the attacks: no API key, no data fetch, no server

The attack gallery runs in-process against the real DP engine:

```bash
pip install -e .
python -m attacks.patients_alice   # re-identify Alice with privacy off, then watch
                                   # the guard, the noise, and the budget defeat it
```

### 2. Connect an AI agent

The gateway runs as an MCP stdio server for Claude Desktop. The agent becomes the untrusted query author, and it gets only structured tools (`count`, `sum`, `average`, `histogram`, `get_budget`) whose argument schemas are generated from the dataset policy. No API key is needed anywhere, because the connecting agent is the intelligence.

**[Setup and full walkthrough →](./docs/CLAUDE_DESKTOP.md)**

### 3. The full natural-language UI

A local single-tenant demo. An API key is needed only for the untrusted NL→query compiler:

```bash
export ANTHROPIC_API_KEY=...   # used only by the untrusted NL→query compiler
docker compose up              # brings up the engine, API, and UI
# open http://localhost:8501
```

That HTTP + Streamlit surface is a **local, single-tenant demo**. Identity comes from a spoofable `X-Identity` header, so it is meant for one trusted operator on their own machine, not a public deployment (see [what these surfaces are, and are not](#what-this-project-is-and-is-not)). For local non-Docker setup, running the tests, and configuration knobs, see [`SETUP.md`](./SETUP.md).

---

## The headline: an attack gallery

Anyone can claim privacy. This repository ships the exploits that would break the claim, runs them against its own engine, and pins the outcomes in CI. The fastest way to understand what the gateway guarantees is to watch it defeat three classic attacks that break naive "query a database" systems.

### Attack 1: The differencing attack

A differencing attack isolates one person by asking two aggregate questions that differ by exactly that person.

```
Query A: "Total income of all 100 people in department X."        → $7,240,000
Query B: "Total income of all people in department X except Alice." → $7,135,000
Attacker computes: A − B = $105,000  ← Alice's exact salary, leaked.
```

Both queries are "just aggregates." Neither names a single row. Yet together they expose an individual. The gallery (`attacks/differencing.py`) shows this attack **succeeding with privacy disabled**: the target's private value is recovered exactly. (The salary sketch above is illustrative; on the real UCI Adult data, "Alice" is the unique holder of her group's maximum capital gain.) It then shows the same attack **defeated once DP is on**: the calibrated noise on each answer makes the subtraction useless, and the budget accountant charges for the information released across *both* queries rather than treating them as independent.

### Attack 2: Membership inference

A membership-inference attack determines whether a *specific individual* is in the dataset at all. For many datasets (a medical study, a list of defaulters), that fact is itself sensitive. An attacker with only query access tries to decide: "is this exact person in the data?"

The gallery runs this attack across a sweep of privacy budgets (ε, the dial that trades answer accuracy for privacy) and plots the result:

![Membership-inference success rate vs ε, with a utility curve overlaid](attacks/out/membership_sweep.png)

<sub>An **optimal** (Neyman–Pearson) attacker deciding one person's membership from a single noisy `COUNT`, run against the real engine across ε. Empirical success (blue, 95% Wilson intervals) hugs the analytic Laplace curve and stays below the worst-case DP ceiling (dashed); it collapses from certainty (DP off) toward the 0.5 coin-flip as ε shrinks. The green **utility curve** (right axis) shows an aggregate query's relative error over the same sweep, barely dented where the attack is defeated. Generated by `python -m attacks.membership` (10,000 trials per ε).</sub>

As ε shrinks (stronger privacy), the attacker's success collapses toward a coin flip. The utility overlay shows the price paid: the same noise that defeats the one-person attack barely moves a population-scale aggregate. Privacy is not free, and the chart shows exactly what you trade for it. The sweep spans ε = 8 down to 0.5 to cover the whole range; the bundled deployment charges **ε = 0.05 per query**, off the left edge of this chart, where the single-query attack is already indistinguishable from chance.

### Attack 3: Singling out by re-identification

Latanya Sweeney showed in 2002 that ZIP code + birth date + sex uniquely identify roughly 87% of Americans (a later replication on newer census data put it closer to 63%). You do not need someone's name to find them in a dataset; a few innocuous attributes will do. The gallery's third attack (`attacks/patients_alice.py`) reproduces that structure on 20 synthetic patients: sex and age alone narrow the cohort to exactly one person, Alice, the only woman over 64.

With privacy off, subtracting two perfectly ordinary demographic histograms recovers Alice's diagnosis exactly. No outlier value is required; being *re-identifiable* is enough, which makes this the strongest attack in the gallery. With privacy on, three independent defenses end it: the filter guard rejects the obvious narrow query outright (spending nothing); calibrated noise drowns the two-query subtraction (signal-to-noise ≈ 0.13, so the recovered "diagnosis" is essentially a random draw); and the budget refuses the averaging escalation long before it could work (~256 repetitions needed, 10 affordable). This is the attack the demo GIF at the top of this page, and the [Claude Desktop walkthrough](./docs/CLAUDE_DESKTOP.md), replay live. Outcomes are regression-tested in `tests/test_attack_patients.py`.

These experiments, run against the system's own engine, are the core evidence that the guarantee is real and understood, not imported from a library and taken on faith.

### Cross-checked against OpenDP

The attacks validate the guarantee against *our own* math. To guard against a self-consistent-but-wrong implementation, the mechanism is also cross-checked against [OpenDP](https://opendp.org/) as an independent reference (`attacks/crosscheck_opendp.py`, opendp 0.15.1).

**In short: a mechanism built from scratch agrees with the industry reference to nine decimal places, and a version that is intentionally mis-calibrated fails the same tests, so the agreement means something.** Agreement is checked two ways: the sensitivity and noise scale against OpenDP's certified bound, and the sampler's actual distribution against OpenDP's, with a positive control proving the test can fail. The measured figures are in [`DESIGN.md`](./DESIGN.md) section 6.3.

OpenDP is the reference, never the implementation: it lives in the dev extras only, and the running system does not import it. The scale agreement is regression-tested in `tests/test_crosscheck_opendp.py` (skipped without OpenDP locally; CI installs it and sets `REQUIRE_OPENDP=1` so the check can never silently skip there).

### Reproduce it

The attacks run in-process against the real DP engine. No API key and no server are needed, since they build hand-written ASTs rather than going through the LLM compiler:

```bash
python -m attacks.patients_alice # Attack 3: re-identify Alice and recover her diagnosis
                                 #           with DP off; watch guard + noise + budget
                                 #           defeat the same attack (no data fetch needed)

python scripts/fetch_data.py     # fetch UCI Adult into data/ (gitignored; ~4 MB)

python -m attacks.differencing   # Attack 1: recover Alice exactly with DP off, then watch
                                 #           noise + budget defeat the same subtraction
python -m attacks.membership     # Attack 2: sweep ε and regenerate the chart above

python -m attacks.crosscheck_opendp  # cross-check vs OpenDP (needs the dev
                                     # extras: pip install -e ".[dev]")
```

The outcomes are themselves regression-tested in `tests/test_attack_differencing.py`, `tests/test_attack_membership.py`, and `tests/test_attack_patients.py`, so a change that quietly weakened the guarantee would fail CI rather than just producing a prettier chart.

---

## How it works

Three stages. Only the first is untrusted, and that asymmetry is the whole idea.

```
  Natural language question
            │
            ▼
  ┌───────────────────┐
  │   LLM compiler    │   Emits a CONSTRAINED QUERY AST (not free SQL),
  │   (UNTRUSTED)     │   via structured/schema-forced output.
  └───────────────────┘
            │  query AST
            ▼
  ┌───────────────────┐
  │  Validation /     │   Policy check: allowed columns only, aggregates
  │  guardrail layer  │   only, declared value ranges, group-cardinality
  │   (TRUSTED)       │   caps. Invalid → repair loop or refusal.
  └───────────────────┘
            │  validated AST
            ▼
  ┌───────────────────┐
  │  Privacy engine   │   Clamp to declared range (bounds sensitivity),
  │   (TRUSTED)       │   add calibrated Laplace noise, decrement budget.
  └───────────────────┘
            │
            ▼
  Noisy answer + confidence interval + remaining budget
```

The most important design choice is the box labeled **UNTRUSTED**. Everything above the validation layer is treated as hostile, and everything below it is the trusted computing base that enforces the guarantee. The LLM compiles to a *constrained AST* rather than arbitrary SQL because that constraint is what bounds query sensitivity, and bounded sensitivity is what makes the noise calibration sound. Free-form SQL would reopen exactly the attack surface this project closes.

## The privacy model

Every answer is noised. An exact ledger of cumulative disclosure is kept per identity and persisted to disk, and the gateway refuses to answer before that ledger can exceed the guarantee it advertises. It never quietly degrades to a noisier answer instead.

The cost is worth stating just as plainly. The guarantee is **(ε, δ)-differential privacy, which is strictly weaker than pure ε-DP.** With probability at most δ, the ε bound is allowed to fail. δ is not extra noise, it is failure mass, which is why it is derived from the dataset rather than hard-coded.

[`DESIGN.md`](./DESIGN.md) sections 3 and 5.4 carry the full derivation: sensitivity, the Laplace mechanism, the hybrid zCDP accountant, and where δ comes from. That is where all the Greek letters went.

---

## What this project is, and is not

It **is** a demonstration that an untrusted natural-language layer can sit in front of sensitive data without compromising a formal privacy guarantee, with the guarantee backed by working attacks rather than assertions.

It **is not** a production privacy product, a substitute for a vetted DP library in a real deployment, or a claim that LLM-generated queries are safe to run unguarded. They are not, which is exactly why the trusted layer exists.

Both the MCP server and the HTTP demo serve a **single local principal** who owns the machine, and that principal can rotate the epoch or delete the budget file to start fresh. So the "an external party burns budget and cannot get it back" property is *demonstrated in mechanism, not enforced against a remote adversary*. Closing that gap needs the verified-identity (OAuth) and multi-tenant split still on the roadmap. The noise sampler also has a known floating-point side channel (Mironov 2012, covered in [`DESIGN.md`](./DESIGN.md) section 5.5). **Do not** point either surface at real regulated data, or treat it as a substitute for a vetted DP library where an untrusted party can authenticate.

The bundled dataset is the public **UCI Adult / Census Income** dataset, the standard benchmark in the differential privacy literature, so the attack-vs-ε results here are directly comparable to published work. It is already public, so the repository is safe to publish. The privacy machinery is demonstrated *as if* the records were sensitive.

---

## Related work

Where this sits among the existing tools, and what it deliberately does differently.

<details>
<summary><b>DP libraries, DP query engines, text-to-SQL, MCP security tooling, and DP near LLMs</b> (click to expand)</summary>

<br>

**DP libraries.** [OpenDP](https://opendp.org/), [Google's differential-privacy libraries](https://github.com/google/differential-privacy), [IBM's diffprivlib](https://github.com/IBM/differential-privacy-library), and [Tumult Analytics](https://github.com/opendp/tumult-analytics) (which powered U.S. Census Bureau, Wikimedia, and IRS releases before its team joined LinkedIn in 2025 and the library moved into the OpenDP organization) are vetted implementations of the mechanisms themselves, written for a trusted analyst to call from their own code. This project hand-rolls its mechanism instead, so that every line of the privacy-critical path stays small, legible, and testable in one repo, and then [cross-checks it against OpenDP](#cross-checked-against-opendp), precisely because a hand-rolled mechanism means nothing without an external referee. For a real deployment the advice above stands: use a vetted library.

**DP query engines.** [PINQ](https://www.microsoft.com/en-us/research/publication/privacy-integrated-queries/) (McSherry, 2009) established the architecture this project inherits: an untrusted analyst issues queries through a trusted layer that guarantees differential privacy no matter what is asked. Its production descendants answer SQL under DP: [smartnoise-sql](https://github.com/opendp/smartnoise-sdk), [Uber's archived elastic-sensitivity rewriter](https://github.com/uber-archive/sql-differential-privacy), and [Wilson et al.'s differentially private SQL](https://petsymposium.org/popets/2020/popets-2020-0025.php), shipped today as [BigQuery differential privacy](https://docs.cloud.google.com/bigquery/docs/differential-privacy). Two deliberate differences here. Those systems accept SQL and analyze or rewrite it, while this gateway never accepts SQL at all: the agent submits a small constrained AST, because a query language small enough to enumerate is a trust boundary small enough to test exhaustively. And every one of them puts a human analyst at the keyboard, where here the query author is an autonomous agent, and the threat model says so.

**Natural-language database interfaces.** Text-to-SQL is a large and successful field, but privacy is not its subject: the generated SQL runs with whatever authority the database grants. Where safety is addressed, as in [SafeNLIDB](https://arxiv.org/abs/2511.06778) (AAAI 2026), it is alignment-based (train the model to reason about what is safe to answer), so the guarantee lives inside the model. This project takes the complementary position: assume the model cannot be made safe, and enforce the guarantee below it with mathematics that holds even when the model is adversarial.

**Agent and MCP privacy tooling.** Tool poisoning, prompt injection, and exfiltration are real risks, and the emerging MCP-security stack addresses them with policy gateways, PII redaction and tokenization, and data-minimization patterns. Those controls govern what an agent can *see and send*. None of them bounds what a sequence of individually harmless *answers* cumulatively reveals, and that is the channel [the attack gallery](#the-headline-an-attack-gallery) exploits. A differencing attack leaks a salary through two aggregates that a redaction proxy would happily pass. Differential privacy bounds exactly that channel, which makes it complementary to the rest of that stack rather than competition.

**DP near LLMs, different problems.** DP-SGD (e.g. [Opacus](https://opacus.ai/)) protects training examples inside model weights. DP in-context learning, DP synthetic text, and DP-RAG protect prompts and retrieval corpora. Local DP, as in Apple's and Google's telemetry, noises data on-device before it is ever collected. This project is the older, central-model setting those all descend from: a trusted curator, an untrusted questioner, and a budget between them.

**The claim, stated carefully.** There is no new differential-privacy mathematics in this repository. The contribution is the combination, and the evidence: an open, attack-validated artifact that puts agentic natural-language access in front of a DP aggregate backend under an explicit untrusted-model threat model. As far as I can find, no other open MCP server enforces differential privacy with a persisted budget beneath an untrusted agent. If you know of one, open an issue; I would genuinely like to compare notes.

</details>

---

## Documentation

- [`DESIGN.md`](./DESIGN.md): architecture, threat model, the sensitivity and noise math, the budget design
- [`SETUP.md`](./SETUP.md): local setup, running the tests, configuration knobs
- [`docs/CLAUDE_DESKTOP.md`](./docs/CLAUDE_DESKTOP.md): connecting an agent, and a reproducible attack session
- [`benchmarks/RESULTS.md`](./benchmarks/RESULTS.md): measured latency on both surfaces, and the composition-capacity tables
- [`SECURITY.md`](./SECURITY.md): the disclosed limitations, and how to report anything else
- [`CHANGELOG.md`](./CHANGELOG.md): release history

## Repository layout

```
.
├── README.md            ← you are here
├── DESIGN.md            ← architecture, threat model, the math, the budget design
├── SETUP.md             ← local setup, running the tests, configuration knobs
├── engine/              ← DP engine: mechanism, RNG, sensitivity, budget accountant + store
├── validation/          ← the trust boundary: policy checks, guards, and the repair loop
├── compiler/            ← the untrusted LLM NL→AST compiler
├── attacks/             ← the attack gallery: differencing, membership ε-sweep, patients singling-out
├── service/             ← AnalyticsService + audit log: the transport-agnostic core every surface shares
├── mcp_server/          ← the stdio MCP server: tool schemas generated from the dataset policy
├── datasets/            ← owner-authored dataset policies, ingestion, and the bundled patients demo
├── identity/            ← the identity layer the budget is keyed to
├── api/                 ← FastAPI service
├── ui/                  ← Streamlit front-end with the live budget meter
├── benchmarks/          ← manual latency benchmarks (run by hand, never by pytest)
├── docs/                ← the Claude Desktop walkthrough, the demo GIF, and the session chart assets
├── scripts/             ← fetch_data.py (pulls UCI Adult into data/, never committed) + the demo GIF renderer
└── tests/               ← unit, trust-boundary, privacy-guarantee, and attack regression tests (DESIGN.md section 8)
```

## Author's note

This project is where I work through the design of privacy-preserving data systems and least-privilege data access in public: the trust boundary, the budget accounting, and the attack demos are the parts I'd defend in a design review.
