# Adjudge

> **Verified findings, not confident guesses.** Adjudge triages noisy security-scanner output — dedupes it, correlates the same issue across tools, kills the false positives, and labels every survivor **TOOL-CONFIRMED**, **AI-INFERRED**, or **COULD-NOT-VERIFY**, traceable to the exact source line. The core never sends a packet.

<p>
<a href="https://pypi.org/project/adjudge/"><img alt="PyPI" src="https://img.shields.io/badge/pypi-adjudge-blue"></a>
<img alt="Python" src="https://img.shields.io/badge/python-3.11%2B-blue">
<a href="https://github.com/Kasumiki/adjudge/actions"><img alt="CI" src="https://img.shields.io/badge/CI-passing-brightgreen"></a>
<img alt="Tests" src="https://img.shields.io/badge/tests-152%20passing-brightgreen">
<img alt="Typed" src="https://img.shields.io/badge/typed-mypy%20clean-blue">
<img alt="Lint" src="https://img.shields.io/badge/lint-ruff%20clean-blue">
<img alt="License" src="https://img.shields.io/badge/license-MIT-green">
<a href="https://github.com/Kasumiki/adjudge/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/Kasumiki/adjudge?style=social"></a>
</p>

> *If Adjudge saves you from one hallucinated finding, [star it](https://github.com/Kasumiki/adjudge).*

<p align="center">
  <img src="assets/adjudge-demo.gif" alt="Adjudge: noisy scanner output in, a defensible verdict out — every finding labeled TOOL-CONFIRMED, AI-INFERRED, or COULD-NOT-VERIFY" width="100%">
</p>

<p align="center"><sub><b>noise in → a verdict you can defend.</b> Real run: dedupe → triage → opt-in verify → labeled, source-traced report.</sub></p>

---

## See it first

What a labeled run looks like as text:

```console
$ adjudge triage nuclei.jsonl semgrep.sarif trivy.json gitleaks.json -o report.md

  Adjudge · run r_7f3a9c2b81 · model claude-sonnet · $0.11 / $5.00 ceiling
  ──────────────────────────────────────────────────────────────────
  ingest      4 sources · 218 raw findings
  dedupe      218 → 91 unique
  correlate   91 → 77   (14 merged across tools, confidence ↑)
  triage      77 classified · 12 dropped as false-positive
  ──────────────────────────────────────────────────────────────────
  🟡 AI-INFERRED  65          ✗ false-positives dropped  12

  → run `adjudge verify --scope <hosts>` to confirm the safe ones,
    promoting them to 🟢 TOOL-CONFIRMED (or honest ⚪ COULD-NOT-VERIFY).

  ✔ wrote report.md  ·  manifest pinned (sha256 + model + cost)
```

A sample excerpt from the report **after a triage + an opt-in `verify` pass** — deduped, severity-sorted, every claim labeled and sourced:

```markdown
### F-0042 · Missing Strict-Transport-Security header          🟢 TOOL-CONFIRMED
- Target:     https://app.example.com/login
- Severity:   medium  ·  confidence: high
- Sources:    nuclei (http/missing-headers/hsts) + httpx — correlated, 2 tools agree
- Provenance: nuclei.jsonl:117 · httpx.json:4
- Proof:      opt-in GET sent (scope-gated, IP-pinned) → no HSTS header in response

### F-0051 · Possible IDOR on /api/users/{id}                  🟡 AI-INFERRED
- Severity:   high  ·  confidence: medium
- Provenance: semgrep.sarif:runs[0].results[22] → app/routes/users.py:53
- Note:       judged likely-real by triage; no tool confirmed exploitability.

### F-0058 · Possible SQL injection in /search                 ⚪ COULD-NOT-VERIFY
- Provenance: nuclei.jsonl:201
- Reason:     DESTRUCTIVE — Adjudge will never send an attack payload. Verify manually.
```

That's the whole pitch: **you can read it, trust it, and trace it.** Now the why.

---

## The problem

You run nuclei, then Burp, then ZAP, then semgrep, Trivy, gitleaks. Now you have **hundreds of findings** — half duplicates of each other, most of them noise, and a Sunday night to figure out which handful are real.

So you reach for one of the shiny new **"autonomous AI hacker"** tools. It hands you a beautifully formatted report full of **confident, hallucinated vulnerabilities** — CVEs that don't apply, "criticals" it never reached, exploit chains it imagined. You don't find out until a client, a triager, or a maintainer does.

> **A confident wrong finding is the single most expensive failure in security.** It burns your credibility, the reviewer's time, and the trust of everyone downstream.

Scanners are loud. AI bolted onto scanners is loud **and** unaccountable. That gap is the one Adjudge closes.

---

## The trust thesis

Adjudge is a **verified-findings triage & report engine**. Its law is simple: **assert nothing that wasn't confirmed — and say so out loud when you're unsure.** Every finding carries exactly one verification label:

| Label | Meaning |
|---|---|
| 🟢 **TOOL-CONFIRMED** | An opt-in confirming request demonstrated the issue (e.g. the missing header really is missing on a live `GET`). |
| 🟡 **AI-INFERRED** | The LLM judged it likely real from the evidence, but it was **not** independently confirmed. Marked as inference, never dressed up as proof. Confidence rises when multiple tools agree. |
| ⚪ **COULD-NOT-VERIFY** | Adjudge declined to assert it, with one of four honest reasons: *unsupported*, *out-of-scope*, *destructive*, or *error*. |

The core is **analyze-first**: it never sends a packet to a target. The LLM **only classifies** — it never chooses an action, never picks a tool, never sends a request. All scanner text is treated as untrusted, sanitized input (prompt-injection defended). Nothing is asserted that was not confirmed, and every finding is **traceable to the exact source line** that raised it.

No competitor leads with verified, reproduction-backed findings **plus** explicit non-verification. That honesty *is* the product.

---

## How it works

```
  ┌──────────┐   ┌─────────────┐   ┌────────────┐   ┌──────────────┐   ┌────────┐
  │  INGEST  │ → │ DEDUPLICATE │ → │ CORRELATE  │ → │  LLM TRIAGE  │ → │ REPORT │
  └──────────┘   └─────────────┘   └────────────┘   └──────────────┘   └────────┘
  nuclei JSONL    collapse          same issue        classify only —    md · json
  SARIF/semgrep   duplicate         across tools       NEVER acts         sarif · pdf
  CodeQL · Trivy  findings          merges; agreement  tool text          H1 blocks
  gitleaks·httpx                    raises confidence  sanitized          + manifest
  ─────────────────────────────────────────────┊─────────────────────────────────
        core never sends a packet               ┊   opt-in · consent + scope gated:
                                                ┊   verify / scan
```

1. **Ingest** — JSON-first adapters normalize each tool's output onto one canonical finding model with a single severity scale.
2. **Deduplicate** — identical and near-identical findings collapse to one.
3. **Cross-tool correlate** — when multiple tools flag the same issue, they merge and **confidence rises on agreement.**
4. **LLM false-positive triage** — the model classifies likely-real vs likely-false. It classifies *only*; it never selects an action. All tool text is sanitized untrusted data (prompt-injection defended).
5. **Report** — labeled, provenance-pinned findings out to your format of choice.

---

## Quickstart

```bash
# Install — the analyze-first core needs no scanner binaries
pipx install adjudge          # or: uvx adjudge ...   /   pip install adjudge

# Point any one provider at it (LLM-agnostic, auto-detected)
export ANTHROPIC_API_KEY=sk-ant-...   # or OPENAI_API_KEY / GEMINI_API_KEY / OPENROUTER_API_KEY

adjudge doctor                        # check config + provider; fail loud if not ready
adjudge triage nuclei.jsonl --dry-run # see the cost before you spend a cent
adjudge triage nuclei.jsonl semgrep.sarif -o report.md   # ingest → triage → report
```

Want independent confirmation on the ones that matter? Opt in, scoped:

```bash
adjudge verify <run-id> --scope app.example.com -o report.md
```

```text
Active verification will send confirming requests to targets within scope: app.example.com.
Proceed? [y/N]: y
✔ verified 9 · refuted 4 · could-not-verify 18 · skipped 42
```

---

## Supported inputs

JSON-first adapters, out of the box — no scanner binaries needed for the core:

| Adapter | Tool / format |
|---|---|
| `nuclei` | nuclei JSONL |
| `sarif` | SARIF — semgrep, CodeQL |
| `trivy` | Trivy JSON |
| `gitleaks` | gitleaks JSON |
| `httpx` | httpx JSON |

> Adding the next adapter is the highest-value, lowest-barrier contribution — see [Star, fork, contribute](#star-fork-contribute).

---

## Command surface

| Command | What it does |
|---|---|
| `adjudge triage <files…>` | The core. Ingest → dedupe → correlate → LLM false-positive triage → report. Sends no packets. `--dry-run` ingests + dedupes and prints a cost estimate, spending nothing. |
| `adjudge verify <run-id> --scope <hosts>` | **Opt-in**, scope-gated, IP-pinned *confirming* requests. Missing header → `GET`; open port → TCP connect; reflected-XSS → inert sentinel. Destructive classes are **permanently hard-blocked**. |
| `adjudge review <run-id>` | Human override of triage, recorded with machine-vs-human attribution. Can **never** fabricate a verification verdict. |
| `adjudge ask <run-id> "<question>"` | Natural-language Q&A over a run. Grounded in the findings, cites finding ids, injection-defended, budget-metered. |
| `adjudge scan <target> --scope <hosts>` | **Opt-in** active scanning (curated nuclei/httpx) behind consent + scope. **You pick the tools — never the LLM.** Output flows through the same ingest → triage pipeline. |
| `adjudge runs` | List and inspect prior runs and their pinned manifests. |
| `adjudge doctor` | Verify config, provider, and dependencies — fail loud if not ready. |
| `adjudge init` | Scaffold a starter `.env`. |

---

## Safety model

Adjudge is built so the safe path is the default path.

- **Analyze-first core.** `triage`, `review`, `ask`, and report generation **never send a packet to a target.** Triaging a report can never touch prod.
- **`verify` and `scan` are strictly opt-in** — gated by **explicit consent + declared scope.** No scope, no packets.
- **Scope guard defeats rebinding & metadata theft.** A target is in scope only inside an authorized CIDR, or matching the domain allowlist *with every resolved IP public*. Private, loopback, link-local, or cloud-metadata addresses (e.g. `169.254.169.254`) are refused; `verify` egress is **pinned to the vetted IP**, and redirects are re-checked on every hop.
- **Confirming requests are minimal and inert** — a missing-header check is a plain `GET`; an open-port check is a TCP connect; a reflected-XSS check uses an **inert sentinel**, never a working payload.
- **Destructive classes are PERMANENTLY hard-blocked** — SQLi, RCE, command injection, SSRF, deserialization and peers. Adjudge **confirms or declines; it never exploits**, returning `COULD-NOT-VERIFY (destructive)`. There is no flag to turn this off.
- **The user picks tools and actions. The LLM never does.** The model only classifies.
- **Cost ceiling enforced** per run (USD) — the run stops loud rather than overspending.
- **Fail-loud.** Adjudge never fakes success. No provider, no run. Can't verify, says so.

---

## Trust & provenance engineering

These aren't features bolted on — they're the reason Adjudge exists.

- **Per-run USD cost ceiling** — enforced; runs stop before they overspend, with a labeled partial result.
- **Provenance manifest** — every input pinned by `sha256`, plus the model, prompt hash, and exact cost. Any finding walks back to the exact source line; a run is auditable and re-runnable. (LLM output is non-deterministic, so re-runs may differ — the manifest records *what produced* a result, honestly.)
- **Prompt-injection defense** — all tool-supplied text is sanitized and fenced as untrusted; the model is handed data, never instructions, and classifies only.
- **Eval harness** — triage quality and verify-safety are tested, not assumed.
- **Fail-loud** — no silent failures, no faked success.

---

## Reports

Markdown · JSON · SARIF · PDF · **HackerOne submission blocks**. Every report is backed by the run manifest, so a reviewer can see exactly what produced it — and SARIF drops straight into CI / code scanning.

```bash
adjudge triage nuclei.jsonl -o report.md -o report.sarif -o report.pdf
```

---

## Configuration

Adjudge is **LLM-agnostic** — OpenAI, Anthropic, Gemini, OpenRouter, or any OpenAI-compatible endpoint. Set one provider key and you're running.

```bash
adjudge init                          # scaffold a .env template
export ANTHROPIC_API_KEY=sk-ant-...   # or OPENAI_API_KEY / GEMINI_API_KEY / OPENROUTER_API_KEY
export ADJUDGE_BASE_URL=https://your-endpoint/v1   # …or any OpenAI-compatible endpoint
```

Configuration resolves in exactly one place — **CLI flags → process env → `.env` → defaults.**

| Setting | Env var | Default |
|---|---|---|
| Provider | `ADJUDGE_PROVIDER` | auto-detected from key |
| Model | `ADJUDGE_MODEL` | provider default |
| API key (by env-var name) | `ADJUDGE_API_KEY_ENV` | conventional (`OPENAI_API_KEY`, …) |
| Custom endpoint | `ADJUDGE_BASE_URL` | — |
| Cost ceiling (USD) | `ADJUDGE_COST_CEILING_USD` | `5.0` |
| Local run database | `ADJUDGE_DB_PATH` | `adjudge.db` |
| Rate limit (req/s) | `ADJUDGE_RATE_LIMIT_RPS` | `2.0` |

Keys are detected in priority order: `OPENROUTER_API_KEY` → `ANTHROPIC_API_KEY` → `OPENAI_API_KEY` → `GEMINI_API_KEY`. Secrets are referenced **by env-var name** and never live in argv or config files.

Install extras only when you need them:

```bash
pip install "adjudge[llm]"      # provider SDKs (lazy-loaded at run time)
pip install "adjudge[report]"   # PDF rendering
pip install "adjudge[dev]"      # pytest, ruff, mypy
```

---

## Who it's for

- **Pentesters & consultants** — turn a pile of scanner output into a defensible, source-cited, client-ready deliverable, with the false positives already gone.
- **Bug-bounty hunters** — stop submitting noise. Ship findings with a verdict and export a **HackerOne submission block** straight from a run.
- **AppSec engineers** — wire scanners into CI, correlate across tools, and gate on SARIF you can trust — without anything ever touching prod.

In CI:

```yaml
# .github/workflows/triage.yml
- name: Adjudge triage
  run: |
    pipx install adjudge
    adjudge triage nuclei.jsonl semgrep.sarif -o report.sarif
  env:
    ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
    ADJUDGE_COST_CEILING_USD: "2.0"
```

---

## Adjudge vs. the alternatives

| | Raw scanners | "Autonomous AI hacker" | **Adjudge** |
|---|---|---|---|
| Output | hundreds of overlapping findings | confident prose | **verdict-labeled findings** |
| False positives | yours to sort | hidden behind confidence | **triaged out** |
| Hallucination risk | low (mechanical) | **high** | LLM **classifies only**, sanitized input |
| Says "I don't know" | — | almost never | **COULD-NOT-VERIFY**, four honest reasons |
| Independent confirmation | — | claimed, rarely real | **opt-in, safe, scope-gated** |
| Traceability | per tool | weak | **every finding → source line + sha256** |
| Sends packets by default | no | yes | **no** (analyze-first) |
| Exploits destructive classes | no | yes | **never** (hard-blocked) |
| Provenance manifest | no | rarely | **yes** (sha256 · model · cost) |

---

## Project facts

- **Python 3.11+**, **MIT** licensed, **fully typed** (ships `py.typed`).
- **~3,900 lines**, **152 tests**, **ruff** + **mypy** clean.
- Installable via **pip / pipx / uvx**. The analyze-first core needs **no scanner binaries** and no LLM SDK at import time — heavy and optional pieces are lazy extras.
- Guiding law: **advertise nothing the code lacks, and never assert what wasn't confirmed.**

### Roadmap

> The following are **planned, not yet shipped**. Adjudge advertises nothing the code lacks; these are flagged so you know the difference.

- Additional ingest adapters (Burp, ZAP, nmap, …) and safe, confirming-only verifier recipes.
- A richer interactive review TUI; continuous / recurring runs.
- Expanded eval-harness coverage and triage-quality benchmarks.

---

## Star, fork, contribute

If you've ever submitted a finding that turned out to be noise — or watched an "AI security tool" invent a vulnerability with total confidence — Adjudge is the antidote.

- ⭐ **Star it** to follow a tool whose entire premise is *honest uncertainty over confident nonsense* — and to track new adapters and verifier classes as they land.
- 🍴 **Fork it** to add an ingest adapter, a safe verifier, or a report format. The pipeline is small (~3,900 lines), fully typed, ruff + mypy clean, with 152 tests to keep you honest.

Adding a new **ingest adapter** is the lowest-barrier, highest-value contribution — open an [issue](https://github.com/Kasumiki/adjudge/issues) with scanner output that got mis-triaged so we can grow the eval harness, then send a PR.

```bash
git clone https://github.com/Kasumiki/adjudge
cd adjudge
pip install -e ".[dev]"
ruff check adjudge tests && mypy adjudge && pytest    # 152 tests, ruff + mypy clean
```

Contributions welcome — see [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`SECURITY.md`](SECURITY.md). The bar is the project's law: **advertise nothing the code lacks, and never assert what wasn't confirmed.**

> **Found Adjudge useful? Star it and tell one pentester.**

## License

[MIT](LICENSE) © Adjudge contributors.
