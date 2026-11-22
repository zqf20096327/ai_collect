# RegLens

**Ask EU credit risk regulation a question and get an answer you can check:** every claim
cites the article or paragraph it comes from, says whether that source is law, a supervisory
expectation or an interpretation, and states the "as of" date of the texts. When the corpus
does not support an answer, RegLens says so instead of guessing.

Built for credit risk modellers and validators working with the IRB approach, the standardised
approach, credit risk mitigation and the definition of default.

There is no hosted demo; run it locally (below).

Next steps: [roadmap](docs/ROADMAP.md). Development history: [archived handoff](docs/archive/HANDOFF-2026-11-14.md).

> **Disclaimer.** Personal open-source project. Not affiliated with any employer, supervisor or
> regulator. Not legal or regulatory advice. Always check the official texts.

## What an answer looks like

> **What PD input floors apply to retail exposures under CRR3?**
>
> For retail exposures, the PD used as an input to the risk-weighted exposure amount and
> expected loss formulae is the higher of the one-year PD of the grade or pool and the
> applicable PD input floor [1]:
>
> - **0,1 %** for QRRE revolvers [1]
> - **0,05 %** for retail exposures that are not QRRE revolvers [1]
>
> Where an exposure is covered by an eligible guarantee from a central government, central bank
> or the ECB, the floor does not apply to the covered part [2].
>
> *Answered 31 Oct 2026 from: CRR consolidated version of 26 Jun 2026*
>
> [1] CRR Art. 163(1) — law · [2] CRR Art. 159a — law · Mechanical citation checks: 4/4 claims passed

Try questions like:

- *Can a bank use own LGD estimates for a large corporate under A-IRB?*
- *How long is the probation period after a distressed restructuring?*
- *What happens to downturn LGD if no downturn can be observed in the bank's data?*
- *Which output floor factor applies in 2026?*
- *Does the ECB guide to internal models apply to less significant institutions?*

## What it covers

| Source | Legal level |
|---|---|
| CRR (Regulation (EU) No 575/2013), consolidated version including CRR3: definitions, own funds requirement and output floor, standardised approach, IRB approach, credit risk mitigation | law |
| RTS on IRB assessment methodology, default materiality threshold, economic downturn | law (RTS) |
| EBA Guidelines on definition of default, PD/LGD estimation, downturn LGD, CRM for A-IRB, loan origination and monitoring | EBA guideline |
| EBA Single Rulebook Q&A on CRR credit risk (243 final Q&As) | EBA Q&A |
| ECB guide to internal models (overarching principles, credit risk); ECB validation reporting instructions | ECB supervisory expectation |

English only, public sources only. Not covered: market risk, counterparty credit risk,
operational risk, securitisation, liquidity, leverage, IFRS 9, national rules.

## How it works

1. **Ingestion from official sources:** the law via the EU Publications Office API (consolidated
   version in force), guidelines and the ECB guide via Docling. Every chunk is one legal unit
   (article paragraph, point, guideline paragraph, Q&A) labelled with its place in the
   hierarchy, e.g. `CRR › Part Three › Title II › Chapter 3 › Art. 178(1)`.
2. **Retrieval:** keyword (Postgres full-text) + embeddings (BGE-M3) fused, reranked by a cross-encoder, with
   a practitioner glossary ("A-IRB", "DoD", "MoC" → the regulation's own wording). All local.
3. **Routing:** a small model decides whether the question needs one lookup or several
   provisions. Simple questions get a single grounded answer; multi-step questions go to an
   **agent** that searches, follows cross-references and reads definitions and EBA Q&As
   (bounded: at most 10 tool calls). A quick answer that reports missing information is retried
   with the agent.
4. **Checking:** code verifies that every claim cites a passage it was given and that its numbers
   appear in that passage, before you see the answer.

The corpus tools are also available as an **MCP server**, so Claude Desktop or any MCP client
can query the regulation directly. Design choices and evidence: [docs/DESIGN.md](docs/DESIGN.md).

## How well it works

Measured on 120 golden questions, drafted with an LLM and checked and corrected against the
source texts by a credit risk practitioner, graded by an LLM judge against the expert answers
([first 80](docs/results/golden-phase3.md), [40 harder ones](docs/results/golden-120.md)):

| 104 in-scope questions | |
|---|---|
| Correctness (fully / partly / wrong) | **0.89** (82 / 22 / **0**) |
| Citation recall (expected sources cited) | 0.89 |
| Claims passing the mechanical citation checks¹ | 0.99 |
| Out-of-scope questions declined | 15 / 16 |

¹ Code checks that each claim cites a passage it was given, that its numbers appear in that
passage, and that claims labelled law cite law. It does not check that the passage supports the
meaning of the claim; correctness above is graded separately against expert answers.

These 120-question figures were measured before the 8 November 2026 review fixes (stricter
citation rules, structured citation metrics, reproducible run manifests). After the first round
of fixes, and before the second-review fixes (window-level evidence checks, not yet
re-measured), the 30-question smoke set was re-measured from a run manifest
(`20261108-151941-routed-phase0`):
correctness **0.90** on 25 in-scope questions (20 fully / 5 partly / **0** wrong), 5/5 out of
scope declined, citation recall 0.87, mechanical checks passed 0.97. Four judge verdicts are
flagged as internally inconsistent and await a hand check. The research agent now
reads more before answering, so a deep answer costs 60–180k tokens; a full 120-question
re-measure is pending a cost reduction ([review plan](docs/REVIEW-PLAN.md)).

Multi-step questions are where the research agent earns its cost. On the 11 newest multi-hop
questions, a single retrieval pass scores 0.59 and the routed agent 0.86. See
[the agent results](docs/results/agent-phase3.md).

## Also included: policy gap analysis

A second use case, shown on a **synthetic** Model Validation Policy of a fictitious bank: an
obligation register of 752 atomic obligations extracted from the regulation (each with a
verified quote), matched against the policy clause by clause into a coverage matrix (covered /
partial / missing / contradicted) with evidence. It finds all 15 deficiencies planted in the
policy; see [the results and caveats](docs/results/gap-phase4.md).

## Run it locally

```bash
uv sync --extra ml --extra db --extra api --extra mcp  # Docling, BGE-M3, Postgres client, API, MCP
docker compose up -d                                   # Postgres + pgvector on 127.0.0.1:5433
uv run reglens download                                # sources: EU Publications Office, EBA, ECB
uv run reglens parse && uv run reglens index
uv run reglens ask --route "Can a bank use own LGD estimates for a large corporate under A-IRB?"
```

### Start the web UI

Once the corpus is indexed (the steps above, done once), the following processes run the UI. Each
command goes in its own terminal and starts from the repository root.

1. **Database.** Docker Desktop must be running.

   ```bash
   docker compose up -d
   ```

2. **Inference and API.** For agent runs, start one shared GPU service in its own terminal:

   ```bash
   uv run uvicorn reglens.inference:app --host 127.0.0.1 --port 8001 --workers 1
   ```

   Set `REGLENS_INFERENCE_URL=http://127.0.0.1:8001` in the API terminal (PowerShell:
   `$env:REGLENS_INFERENCE_URL='http://127.0.0.1:8001'`). Agent subprocesses inherit this setting.
   Then start the **API** on http://localhost:8000. `/api/ready` reports actual model/database
   readiness; application startup alone does not establish model readiness. Without this setting,
   each process loads its own models, which is suitable only for simple single-process use.

   ```bash
   uv run uvicorn reglens.api.app:app --port 8000
   ```

3. **Web UI** on http://localhost:3000. Run `npm install` only the first time.

   ```bash
   cd web && npm install && npm run dev
   ```

Then open http://localhost:3000. If port 3000 is taken or reserved (on Windows, Docker/WSL can
reserve a range that includes it: `netsh int ipv4 show excludedportrange protocol=tcp`), run
`npm run dev -- -p 3200` instead; the API accepts the web UI on any `localhost` port.

Answers are generated with your **Claude subscription** (the `claude` CLI must be installed and
logged in), or with your **own Anthropic API key**: choose "Your API key" in the UI. The key
stays in the page's memory and goes, via your local RegLens API, only to the Anthropic API.
Quick answers take a few
seconds. Research-agent answers take up to a minute or two, with each step shown live.

To stop, press Ctrl+C in the API, inference-service and web terminals, then run `docker compose stop`.

More on the front end: [web/README.md](web/README.md). The earlier Streamlit UI still works as a fallback
(`uv sync --extra ui`, then `uv run streamlit run src/reglens/ui/app.py`).

A GPU is recommended for indexing (embeddings and reranker run locally).

**API key:** the web UI takes your own Anthropic API key. It stays in the page's memory (gone on
reload); with each question it goes from your browser to your local RegLens API, which passes it
to the Anthropic API and nowhere else. It is never logged or stored. A quick answer costs about 6k tokens;
an agent answer 40–90k.

**Evaluation:** `reglens eval-retrieval` (no LLM calls), `reglens eval-answers` and
`reglens judge` (dry run unless `--yes`; cached). Every LLM call is logged; `reglens usage`
reports tokens per phase, model and purpose. The whole project so far, development and
evaluation, used about 10.6M tokens (≈ €19 at API prices; 8 Nov 2026).

**Optional Codex subscription evaluation:** local development can select
`reglens --config config.codex.yaml ...` after `codex login` with ChatGPT. This uses
`gpt-6.1-sol` through the Codex CLI and the bounded RegLens research loop; the default
configuration remains Claude. No OpenAI API key is used. See the
[30-question comparison](docs/results/codex-claude-smoke30-2026-11-13.md) and
[initial three-question run](docs/review/CODEX-SUBSCRIPTION-FOLLOWUP-2026-11-13.md)
for results, usage and reproduction steps. The subsequent
[completeness fixes and focused runtime checks](docs/review/COMPLETENESS-FOLLOWUP-2026-11-13.md)
record the evidence-selection changes and remaining limitations. The subsequent
[full 118-question Codex benchmark](docs/results/codex-frozen118-2026-11-14.md) scored 86.4%
across 103 in-scope questions, with 15/15 out-of-scope refusals;
[review findings](docs/review/CODEX-FULL118-FINDINGS-2026-11-14.md) document the remaining gaps.
These are automated development-set scores. Codex API-equivalent prices are unconfigured;
unpriced ledger entries do not mean zero subscription usage or a zero-cost API run.

## Licence

MIT. The regulatory texts remain subject to their publishers' reuse terms (see `sources.yaml`).
