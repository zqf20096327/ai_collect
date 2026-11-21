<div align="center">

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg/960px-Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg" height="230" alt="Mona Lisa — Leonardo da Vinci's Sfumato" />
  &nbsp;&nbsp;
  <img src="https://upload.wikimedia.org/wikipedia/commons/c/c5/Leonardo_Design_for_a_Flying_Machine%2C_c._1488.jpg" height="230" alt="Design for a Flying Machine, c. 1488" />
  &nbsp;&nbsp;
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Da_Vinci_Vitruve_Luc_Viatour.jpg/960px-Da_Vinci_Vitruve_Luc_Viatour.jpg" height="230" alt="Vitruvian Man — Cross-Domain Proportion" />
</p>

# 🎨 Sfumato

### *Dissolve domain boundaries. Break the Artificial Hivemind. Unlock Test-Time Scaling for Exploration Diversity.*

<p>
  <a href="./README.md"><strong>English</strong></a> · <a href="./README.ko.md">한국어</a> · <a href="./README.ru.md">Русский</a> · <a href="./README.zh-CN.md">简体中文</a>
</p>

<p>
  <img src="https://img.shields.io/badge/Diversity_Across_9_Runs-9%2F9_Undefeated_(60_vs_34)-B83B2A?style=for-the-badge" alt="9/9 Diversity Undefeated" />
  <img src="https://img.shields.io/badge/K=12_Scaling-3.0%C3%97_(18_vs_6)-8E2F21?style=for-the-badge" alt="3.0x Scaling" />
  <img src="https://img.shields.io/badge/Claude_Opus_5.5-0_Refusals_(safe--profile)-2F5D62?style=for-the-badge" alt="Claude 0 Refusals" />
  <img src="https://img.shields.io/badge/Dependencies-Zero_(Pure_Stdlib)-5C4E3F?style=for-the-badge" alt="Zero Dependencies" />
</p>

> *"Sfumato" (Italian: evaporated like smoke) is Leonardo da Vinci's painting technique of dissolving harsh outlines so entirely new forms emerge. Leonardo didn't stay inside one discipline — he ported anatomy, fluid dynamics, fortification, and optics into each other.*
>
> **Sfumato** is an ultra-lightweight agent skill (`/sfumato`, `/sfm`) that does the same for frontier LLMs — **4 plain-text files, zero external RAG, zero fine-tuning, and zero third-party dependencies.**

</div>

---

## 🔥 The Problem: Standard LLMs Hit an *Artificial Hivemind* Wall

For coding and strict reasoning, **clean, strictly relevant context** is king. Irrelevant context distracts attention and kills accuracy.

**For brainstorming, the exact opposite happens.**

When you ask an LLM to brainstorm a hard open-ended problem — even across 12 completely isolated sessions — it collapses into the same 3–6 safe textbook clichés (*Artificial Hivemind*, NeurIPS 2025). Raising `temperature` breaks coherence before it creates real conceptual leaps. Multi-agent debate makes it *worse* (*Diversity Collapse*, 2026).

> **🧪 Real Smoking Gun from Our Pilot (`OSS-PR`):**
> Across isolated runs solving *"how to stop AI-generated slop PRs in open-source repos"*, **three completely separate sessions** (`Direct Baseline 1`, `Direct Baseline 2`, and even an `Explicit Thermodynamics` session) **independently invented the exact same example package string: `pkg@pr-4821` / `pkg@patch-4821`.**
>
> **Zero** sessions in Sfumato's **Blind Isomorphic Masking** track touched `4821` — or any Baseline cliché.

---

## 📈 Test-Time Scaling for Exploration Diversity (Real Measured Data, `K = 1..12`)

We ran **12 completely isolated sessions (24 ideas each)** on a classic hard product problem — *stopping buyer-seller disintermediation (off-platform cash deals) in two-sided marketplaces without chat surveillance, fines, or deficit subsidies* — using strict deduplication of underlying causal mechanisms:

<p align="center">
  <img src="./assets/scaling_curve.svg" alt="Test-Time Scaling for Creativity: Sfumato vs. Direct Best-of-N" width="100%" />
</p>

| Metric (`K = 12` isolated runs, 24 ideas each) | Direct Best-of-N | **Sfumato Dual-Track** | Delta |
|---|---:|---:|---:|
| **Unique Structural Mechanisms Discovered** | `6 / 24` (`25.0%`) | **`18 / 24` (`75.0%`)** | **3.0×** |
| **New Mechanisms in Runs 9–12 (last 8 ideas)** | `0` *(hard plateau)* | **`+5` *(still climbing)* ** | **No plateau** |
| **Track B (Blind) Uniqueness / Baseline Overlap** | — | **`83.3%` / `0` overlaps** | Zero cliché gravity |
| **Order-Swapped Blind A/B Judge (`AB` & `BA`)** | `0–2` *(21:24, 20:23)* | **`2–0` Win *(24:21, 23:20)*** | Position-debiased |

> **Key Takeaway:** Swinging harder with **Direct Best-of-N** doesn't work — it flatlines at `6` mechanisms (75% repetition). **Sfumato unlocks Test-Time Scaling for Exploration Diversity:** every additional swing probes an orthogonal mechanism cluster, widening the frontier of non-obvious candidates available to your selector.

---

## 🌍 Multi-Problem & Cross-Model Benchmark (`9 / 9` Undefeated on Diversity)

Does this hold outside marketplace game theory — including **emotional UX design**, **open-web anti-scraping**, **software architecture**, and **other frontier models** like **Claude Opus 5.5**?

We ran **Iso-Candidate-Budget benchmarks** (`4 isolated Stage-1 solvers × 2 ideas = 8 candidate ideas/method`, order-swapped `AB`/`BA` Blind Judges) across **7 public hard problems** on Gemini 4 Neon plus **2 cross-model replications** on **Claude Opus 5.5** using `--safe-profile claude` (which excludes 8 sensitive bio/CBRN/cyber/espionage domains so Claude hits **0 safety refusals across 24 isolated calls**). *(Note: Sfumato uses the same 8-idea Stage-1 candidate budget, plus extra coordinator masking/back-translation and Stage 2a/2b evaluation calls — see the Compute Budget table below.)*

<p align="center">
  <img src="./assets/multi_problem_benchmark.svg" alt="Multi-Problem and Cross-Model Benchmark: 9/9 Undefeated on Diversity" width="100%" />
</p>

### Primary Runs (Exact Match with `python tools/summarize_benchmarks.py benchmarks/v2 --strict`)

| Public Hard Problem | Model | Direct Unique/8 | Sfumato Unique/8 | Gain | Primary Blind `AB · BA` (30pt) | Verdict |
|---|---|---:|---:|---:|---|---|
| **`MKT-DIS`** *(Marketplace Disintermediation)* | Gemini 4 Neon | 3 / 8 | **7 / 8** | **2.33×** | **24:21 · 23:20** | **Sfumato 2–0 Win** |
| **`UX-ONBOARD`** *(Blank-Canvas Fear · Emotion/UX, v2.0)* | Gemini 4 Neon | 4 / 8 | **7 / 8** | **1.75×** | **25:20 · 24:21** | **Sfumato 2–0 Win** |
| **`WEB-SCRAPE`** *(Open Web vs. Mass AI Scrapers)* | Gemini 4 Neon | 6 / 8 | **7 / 8** | **1.17×** | **22:18 · 20:18** | **Sfumato 2–0 Win** |
| **`OSS-PR`** *(Open-Source AI-Slop PR Flood)* | Gemini 4 Neon | 2 / 8 | **5 / 8** | **2.50×** | **21:17 · 18:21** | **Split 1–1** |
| **`AI-ARCH`** *(AI Agent Architectural Erosion)* | Gemini 4 Neon | 4 / 8 | **7 / 8** | **1.75×** | **23:22.5 · 22.5:24** | **Split 1–1** |
| **`DOC-ROT`** *(Self-Healing Org Doc Rot, v1.2 primary)* | Gemini 4 Neon | 2 / 8 | **6 / 8** | **3.00×** | 22:24 · 21:24 | Direct 2–0 *(see v2.0 ablation)* |
| **`GAME-SNOWBALL`** *(Snowball vs. Rubber-Banding, v1.2)* | Gemini 4 Neon | 5 / 8 | **7 / 8** | **1.40×** | 22:23 · 21:23 | Direct 2–0 *(see v2.0 ablation)* |
| **`MKT-DIS`** *(Cross-Model · `--safe-profile claude`)* | **Claude Opus 5.5** | 4 / 8 | **7 / 8** | **1.75×** | 18:19 · **20:17** | **Split 1–1** *(0 refusals)* |
| **`DOC-ROT`** *(Cross-Model · `--safe-profile claude`)* | **Claude Opus 5.5** | 4 / 8 | **7 / 8** | **1.75×** | 20:22 · 20:22 | Direct 2–0 *(no Anchor · 0 refusals)* |
| **Grand Total (9 primary runs · 72 ideas/method)** | **2 models** | `34 / 72` (`47.2%`) | **`60 / 72` (`83.3%`)** | **1.76×** | **9 Sfumato : 9 Direct** | **9/9 Diversity · 3W / 3T / 3L** |

### v2.0 Stage 2b Equal-Hardening Ablations (Both Gains & Regressions Reported)

| Problem | v1.2 Primary (`S:D`) | v2.0 Equal-Hardening (`S:D`) | Sfumato Delta | Verdict & Lesson |
|---|---:|---:|---:|---|
| **`DOC-ROT`** | `43 : 48` *(0–2)* | **`46 : 48`** *(23:22 · 23:26)* | **+3** | **Split 1–1** — Repairing a strong cross-domain gem (`thermodynamics_cryogenics`) closed the gap |
| **`GAME-SNOWBALL`** *(v1.2 pool, forced graft)* | `43 : 46` *(0–2)* | `39 : 45` *(20:22 · 19:23)* | **−4** | **Direct 2–0** — Proved forcing a polarity-mismatched domain graft hurts; never override a stronger Anchor |
| **`GAME-SNOWBALL`** *(Pool v2.0: 74 domains / 11 clusters)* | `43 : 46` *(0–2)* | **`46 : 39`** *(8/8 unique)* | **+3** | **Sfumato 2–0 Win** — Adding cognition, materials & grid clusters fixed the polarity mismatch ([log](./benchmarks/v2/ablations/game_snowball_pool_v2_results.json)) |

### Independent Cross-Model Blind Judge Audit (Eliminating Same-Model Judge Bias)

To guard against same-model self-preference, we ran **Claude Opus 5.5** as an independent, read-only order-swapped (`AB`/`BA`) blind judge over all **7 primary Gemini 4 Neon champion pairs** ([`benchmarks/v2/cross_model_judges/claude_on_gemini.json`](./benchmarks/v2/cross_model_judges/claude_on_gemini.json)):

- **Cross-Model Judge Result:** **3 Wins (`MKT-DIS` 2–0, `WEB-SCRAPE` 2–0, `AI-ARCH` 2–0), 1 Split (`GAME-SNOWBALL` 1–1), 3 Losses (`UX-ONBOARD`, `OSS-PR`, `DOC-ROT` v1.2)** — **7 Sfumato vs. 7 Direct** (with 6/7 problems showing zero order bias).
- **What the data honestly proves:**
  - **Model-invariant proven strength:** **9 / 9 undefeated exploration diversity (`1.76×` at K=4, `3.0×` at K=12)**, consistently unlocking structurally distinct mechanisms that Direct prompting never generates — and winning `2–0` across *both* Gemini and Claude judges on `MKT-DIS` and `WEB-SCRAPE` (plus `AI-ARCH` under Claude).
  - **Honest limitations (`n=1` seed per problem):** Single-shot Top-1 win rate against a strong 4-run Direct Best-of-N baseline is near parity (`9:9` primary, `7:7` cross-model), and Track B Blind wins Top-1 less often than Track A Explicit (acting primarily as a zero-cliché wildcard and reframing generator). That is why **Sfumato v2.2 includes a Direct Anchor by default** in `dual-track` and `deep` modes — locking your quality floor (`≥ Direct`) while giving you 1.7–3.0× wider structural exploration.
- **Reproducible Logs & Execution Trace:**
  - Verify all 9 primary runs + both v2.0 Stage 2b ablations (`v2_ablation_*.json`) locally: `python tools/summarize_benchmarks.py benchmarks/v2 --strict` *(the separate Pool v2.0 run is logged in [`game_snowball_pool_v2_results.json`](./benchmarks/v2/ablations/game_snowball_pool_v2_results.json))*
  - Structured benchmark summaries & judge rationales: [`benchmarks/v2/`](./benchmarks/v2/)
  - Independent cross-model judge audit: [`benchmarks/v2/cross_model_judges/claude_on_gemini.json`](./benchmarks/v2/cross_model_judges/claude_on_gemini.json)
  - Archived v2.1 end-to-end execution trace (`sample_domains.py` → 4 isolated solvers → Stage 2a `PASS/HARDEN/KILL` → Stage 2b Hardening; v2.2 retired the regex leak script shown in that archive in favor of shared-skeleton whole-prompt review): [`benchmarks/v2/transcripts/alert_fatigue_v2_1_full_transcript.md`](./benchmarks/v2/transcripts/alert_fatigue_v2_1_full_transcript.md)

---

## 🏛️ How Sfumato v2.2 Works: The *Domain-Masking Trade-Off*

Most cross-domain prompting papers rely only on **Explicit Analogy** (*"apply biology to solve marketplace churn"*). Because original-domain vocabulary stays in the prompt, the LLM still suffers **partial homogenization** back toward industry clichés.

Conversely, **pure Blind Reframing** (erasing the original domain completely) breaks cliché gravity 100%, but has a lower hit-rate because some abstract solutions lose fidelity during back-translation.

**Sfumato v2.2 pairs a Direct Anchor with both cross-domain tracks in isolated parallel — guarded by polarity-aware code RNG, shared-skeleton native-constraint masking, and Clean-Context Red-Team Triage + Selective Hardening:**

<p align="center">
  <img src="./assets/architecture_codex.svg" alt="Sfumato v2.2 Architecture Diagram" width="100%" />
</p>

1. **Polarity-Aware Cluster-Stratified Code RNG (`sample_domains.py`):** Never ask an LLM to "pick random domains" (it repeats *ants, jazz, and chess*). Sfumato samples from **74 mechanism-rich domains across 11 disjoint macro-clusters** using pure Python `random`, omits `mechanisms` hints by default (preventing intra-domain hint priming; opt-in via `--include-hints`), and supports `--polarity` (`adversarial | cooperative | physical_loop | human_ux | systems_ops`) so at least half of sampled domains share structural affinity while preserving cross-cluster breadth. Pass `--safe-profile claude` on Claude Code to keep **66 Claude-safe domains (exactly 6 per cluster across all 11 clusters)** with **0 safety refusals**.
2. **Direct Anchor *(Default in `dual-track` & `deep` · Floor Guarantee)*:** Includes 1 isolated native-domain solver in the unlabeled pool so `max(Direct, Explicit, Blind) ≥ Direct` — never regressing on tightly coupled engineering or physics loops.
3. **Track A — Explicit Analogy *(High Hit-Rate)*:** Original brief + assigned remote domain → surgical hits against concrete domain attack surfaces.
4. **Track B — Blind Isomorphic Masking *(Max Ceiling · Shared 3-Line Skeleton + Native Constraints)*:**
   - Distill the problem once into a private **3-line domain-neutral Structural Skeleton** (*Actors, Cost-Bearer & Incentive Polarity · Core Asymmetry · Why Static Controls Fail*) and check cost-bearer/polarity fidelity against the brief before fanning out.
   - Rewrite each Blind domain into a standalone practitioner scenario in `{USER_LANGUAGE}`, folding banned clichés directly into native physical/institutional constraints (no separate cliché slot), and reread the complete outgoing prompt for plausibility, zero accidentally pasted source jargon, and polarity preservation.
   - A fresh isolated subagent solves the masked twin purely inside the remote field — **physically incapable of emitting original-domain clichés.**
   - Back-translate only the causal mechanism & trade-off (ruthlessly drop strained fits).
5. **Stage 2a/2b — Clean-Context Red-Team Triage (`PASS / HARDEN / KILL`) & Selective Hardening:**
   - **Stage 2a:** A fresh evaluator strips jargon cosplay, screens for **Adverse Selection**, **Sybil/Gaming exploits**, and **Feasibility**, and classifies every candidate into `PASS`, `HARDEN` (with 1 explicit fixable flaw), or `KILL`.
   - **Stage 2b:** Hardens *only* the Top-1 winner's single diagnosed flaw (optionally grafting 1 practical primitive from a passing runner-up — never force-grafting a polarity-mismatched seed over a stronger Direct Anchor).
   - **Global Language-Neutral Templates:** All prompts in `prompt_templates.md` and `domain_pool.json` are English-first with explicit `Respond in {USER_LANGUAGE}.` directives, so English, Korean, Russian, Chinese, and other users get native-language output with zero hardcoded language drift.

---

## ⚡ Before / After Showcase: Marketplace Disintermediation (`MKT-DIS`)

> **Problem:** Freelancers, tutors, cleaners, and contractors meet buyers on a platform, then move to WhatsApp/cash for repeat jobs to dodge the 10–20% fee. *Banned clichés: chat filtering, fines, simple escrow/insurance, cashbacks, or 0% fees.*

| Method | What It Produced | Why It Differs |
|---|---|---|
| **Direct Best-of-N**<br>*(12 runs, 24 ideas)* | Repeated the same 3 core ideas 18 times: *T+0 Reverse Escrow*, *Transferable Client-Book*, *Idle-Slot Backfill*. | High practical quality, but stuck inside the exact same fintech/ops playbook. |
| **Sfumato · Winner**<br>*(Parasitology · Two-Fold Cost of Sex)* | **🏆 Chimeric Task Recombination** *(2–0 Win under BOTH Gemini & Claude judges)* — Redirect 5–7% of the repeat fee into an independent **3rd-party cross-verification slot every N sessions** (blind mock-exam for tutoring, thermal/level cross-inspection for renovations, senior async review for code). | Direct 1:1 cash deals *physically cannot* replicate independent 3rd-party checks, collapsing the collusion price zone — and **proposing cash off-platform becomes a "Lemon Signal" of dodging quality audit.** |
| **Sfumato · Track B Blind**<br>*(Ombudsman & Cryptographic Whistleblowing)* | **Zero-Knowledge Safe-Harbor Attestation** — Seal pricing/deliverable commits + retaliation-proof whistleblower absence proof so corporate/HOA/team buyers get **audit-proof anti-kickback immunity**. | Reframed disintermediation from "saving 15%" into "eliminating embezzlement/kickback liability for institutional buyers." |
| **Sfumato · Track B Blind**<br>*(Anthropology · Kula Ring)* | **Kula Pedigree Provenance Chain** — On-platform jobs stamp verifiable craftsman lineage onto outputs (boosting home resale value, VC/M&A IP due diligence, or credential portability). | Off-platform work becomes an "unpedigreed nameless artifact" that loses downstream third-party resale value. |
| **Sfumato · Red-Team Catch**<br>*(Fluid Dynamics · Venturi Ejector)* | **Venturi Negative-Fee Capacity Suction** — Charge *-3%* (buyer pays 90, supplier gets 93) funded by ±24–48h shift call-options exercised during urgent B2B spikes (160). | Brilliant physics transfer — **and Sfumato's Red-Team Gate instantly caught its wash-trading arbitrage exploit (90→93)** before it could steal Top-1! |

<details>
<summary><strong>📊 Inspect All 18 Unique Sfumato Mechanisms vs. 6 Direct Mechanisms (Full K = 1..12 Log)</strong></summary>

<br/>

#### Direct Best-of-N (`K = 1..12`, 24 ideas → **6 unique**, flatlined at K=8)
1. **Transferable Client-Book & Succession Royalty** *(appeared 6× across 12 runs)*
2. **T+0 Reverse-Escrow / Maturity Transformation** *(appeared 6×)*
3. **Idle-Slot Backfill & Context-Synced Hot-Swap** *(appeared 6×)*
4. **Anchor-Client Patronage Revenue-Share Equity** *(appeared 4×)*
5. **Perishable-Capacity In-Kind Barter Fee** *(1×)*
6. **B2B Wholesale Input & Tax-Arbitrage Rail** *(3×)*

#### Sfumato Dual-Track (`K = 1..12`, 24 ideas → **18 unique**, still climbing at K=12)
| Run | Track · Remote Domain | New Unique Mechanisms Discovered | Cum. |
|---:|---|---|---:|
| 1 | Explicit · `fluid_microfluidics` | ① Venturi Negative-Fee Shift-Option Suction · ② Laminar Co-Flow Unbundling | 2 |
| 2 | Blind · `maritime_trade_guilds` | ③ Multilateral Giro Netting Ledger · ④ Manifest Co-Loading & Third-Party Lien Shield | 4 |
| 3 | Explicit · `parasitology_coevolution` | ⑤ **Chimeric Cross-Recombination (🏆 2–0 Winner)** · ⑥ Reverse-Escrow Metabolic Decoupling | 6 |
| 4 | Blind · `horology_escapement` | ⑦ Differential Remontoir Income/Capacity Smoothing *(1 discarded: translation loss)* | 7 |
| 5 | Explicit · `disaster_triage` | ⑧ Dynamic Retriage Scope-Creep Shield *(1 overlapped Co-Flow)* | 8 |
| 6 | Blind · `container_port_logistics` | ⑨ Dual-Cycling Return-Leg Backhaul Chaining · ⑩ Buffer-Yard Drop-and-Hook Async Decoupling | 10 |
| 7 | Explicit · `siege_fortification` | ⑪ Metered Tool-License & Unused-Material Return Magazine *(1 overlapped Backup)* | 11 |
| 8 | Blind · `ombudsman_whistleblower` | ⑫ Zero-Knowledge Anti-Kickback Safe-Harbor · ⑬ Threshold Anonymous Subcontractor Early-Warning | 13 |
| 9 | Explicit · `architectural_wayfinding` | ⑭ Open-Atrium Live Work-Log Showroom (CPTED Natural Surveillance) *(1 overlapped Backhaul)* | 14 |
| 10 | Blind · `electronic_warfare_pls` | ⑮ Global Conflict-Aligned Multi-Party Schedule Multiplexing *(1 discarded: translation loss)* | 15 |
| 11 | Explicit · `mycorrhizal_plant_defense` | ⑯ Tri-Trophic External Insurer/Lender Priming Signal *(1 overlapped Clearing)* | 16 |
| 12 | Blind · `gift_economy_reciprocity` | ⑰ Kula Pedigree Resale-Value Provenance · ⑱ Potlatch/Hau Generalized Triadic Time-Bank Ring | **18** |

</details>

---

## 🚀 Installation & Usage (4 Plain-Text Files · Zero Dependencies)

Everything Sfumato needs lives in [`skill/sfumato/`](./skill/sfumato/) — just **4 inspectable files**:
- `SKILL.md` — skill instructions, multi-agent guide (Claude Code / Antigravity / Codex CLI) & workflow
- `references/prompt_templates.md` — language-neutral (`{USER_LANGUAGE}`) Anchor, Explicit, Blind, Stage 2a Triage, and Stage 2b Hardening templates
- `resources/domain_pool.json` — 74 curated mechanism-rich domains across 11 macro-clusters (`66` Claude-safe, balanced 6/cluster) with polarity affinities
- `scripts/sample_domains.py` — pure Python stdlib stratified polarity-aware sampler (zero network calls, zero file writes)

Clone, inspect the files, and copy `skill/sfumato` into your agent's global skills directory:

```bash
git clone https://github.com/Excelsus4/sfumato.git && cd sfumato

# Claude Code (+ optional /sfm and /sfm-max shortcuts with --safe-profile claude)
cp -r skill/sfumato ~/.claude/skills/sfumato
cp commands/*.md ~/.claude/commands/

# Antigravity (agy)
cp -r skill/sfumato ~/.gemini/config/skills/sfumato

# Codex CLI
cp -r skill/sfumato ~/.codex/skills/sfumato
```

<details>
<summary>Optional local copy helper (<code>--dry-run</code> supported, after cloning)</summary>

```bash
# macOS / Linux
bash tools/install.sh --dry-run
bash tools/install.sh --target claude   # or agy | codex | all | auto
```

```powershell
# Windows PowerShell
.\tools\install.ps1 -DryRun
.\tools\install.ps1 -Target claude      # or agy | codex | all | auto
```

</details>

### Usage & Compute Budget

```text
/sfm Design a non-obvious mechanic to prevent snowballing in a 3-faction asymmetric RTS
/sfumato deep mode: How do we defend open-source repos from AI-slop PR floods without paywalls?
/sfm-max Exhaustively sweep all 11 clusters to design a non-linear 3-year retention moat
```

| Mode | Stage 1 Solvers | Total Isolated Calls | Est. Token Cost (vs. 1 Direct Call) | Best For |
|---|---|---:|---:|---|
| `fast` | `3 Explicit` (`--k 3 --mode explicit-only`) | `4` *(3 + Stage 2a)* | ~4–5× | Quick practical cross-domain ideas under tight token budgets |
| `dual-track` *(default)* | `1 Direct Anchor + 2 Explicit + 1 Blind` (`--k 3`) | `5–6` *(4 + Stage 2a + opt. 2b)* | ~6–8× | Everyday high-ceiling brainstorming (matches primary benchmark composition; guarantees `≥ Direct` floor) |
| `deep` | `1 Direct Anchor + 3 Explicit + 3 Blind` (`--k 6`) | `8–9` *(7 + Stage 2a + opt. 2b)* | ~10–12× | High-stakes strategic/architecture breakthroughs needing maximum exploration width |
| `sweep` *(opt-in)* | `1 Direct Anchor + 11 domains` (`--k 11`, 1/cluster) | `13–14` *(12 + Stage 2a + opt. 2b)* | ~15–18× | Full 11-cluster coverage in one wave without selector overload |
| `max` (`/sfm-max`, *opt-in*) | **All 66 (Claude) / 74 domains** (`--all`) + **1 Direct Anchor** → **2-Round Tournament** | `79–80` / `87–88` | ~80–90× | Exhaustive high-budget brainstorming *(always confirms session count before running)* |

---

## 📚 Research Foundations

Sfumato builds directly on four converging lines of 2025–2026 LLM creativity research:
- **Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)** — Liwei Jiang et al., *NeurIPS 2025 D&B* ([arXiv:2510.22954](https://arxiv.org/abs/2510.22954)): documents intra- and inter-model homogenization on open-ended ideation.
- **Diversity Collapse in Multi-Agent LLM Systems: Structural Coupling and Collective Failure in Open-Ended Idea Generation** — Nuo Chen et al., 2026 ([arXiv:2604.18005](https://arxiv.org/abs/2604.18005)): shows dense debate/consensus topologies crush semantic diversity; motivates Sfumato's strict **zero-crosstalk** parallel Stage 1.
- **Unlocking LLM Creativity in Science through Analogical Reasoning** — Andrew Shen, Shaul Druckmann, James Zou, 2026 ([arXiv:2605.11258](https://arxiv.org/abs/2605.11258)): demonstrates substantial diversity and novelty gains from structural cross-domain analogies.
- **Assessing the Effect of Cross-Domain Mapping on Creativity in Humans and Large Language Models** — Qiawen Ella Liu, Marina Dubova, Henry Conklin, Takumi Harada, Thomas L. Griffiths, 2026 ([arXiv:2603.19087](https://arxiv.org/abs/2603.19087)): shows frontier LLMs benefit from cross-domain mapping specifically when source domains are sufficiently remote and transfer relational/structural properties.
- **Sfumato's Engineering Contribution:** Operationalizes the **Domain-Masking Trade-Off** between *Explicit Analogy* (high hit-rate, partial homogenization) and *Blind Isomorphic Masking* (lower hit-rate, zero cliché gravity, heavy-tail reframings), unified with a **Direct Anchor floor**, **polarity-aware code RNG**, **shared-skeleton native-constraint masking**, and **Clean-Context Red-Team Triage + Selective Hardening**.

---

<div align="center">

<img src="https://upload.wikimedia.org/wikipedia/commons/5/5f/Codex_Atlanticus.jpg" width="460" alt="Leonardo da Vinci — Codex Atlanticus" />

*“Where the spirit does not work with the hand, there is no art.” — Leonardo da Vinci*

<sub>All Leonardo da Vinci artworks are Public Domain via Wikimedia Commons.</sub>

</div>
