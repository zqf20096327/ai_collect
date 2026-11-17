<p align="center">
  <img src="assets/brand/github-readme.svg" alt="Markwright — evidence, not verdict" width="100%" />
</p>

<p align="center">
  <a href="LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/badge/license-Apache--2.0-2563EB"></a>
  <img alt="Python 3.11+" src="https://img.shields.io/badge/python-3.11%2B-2563EB">
  <img alt="Tests: 3 tiers" src="https://img.shields.io/badge/tests-110%2B%20%C2%B7%203%20tiers-2563EB">
  <a href="docs/limitations.md"><img alt="Not an AI detector" src="https://img.shields.io/badge/not%20an-AI%20detector-0B1F39"></a>
</p>

**Your models probably watermark their output already, and nobody can prove it later.** SynthID-Text ships inside HF transformers; KGW green-listing is a standard baseline. The missing part is the operations layer: which model version was marked, under which key, with which parameters; how keys rotate without breaking old verifications; and how to report a match as calibrated statistical evidence with a known false-positive rate. Markwright is that layer, an open-source **control plane for LLM text watermarking**. It wraps published schemes and standard KMS/vault primitives; it invents no algorithm and no cryptography of its own.

A result looks like this (there is no "AI: yes/no" form of it):

```
Result: MODERATE EVIDENCE of watermark  (config acme-llm 4.1 / synthid-text v3)
  calibrated p-value    2.1e-05  (95% interval 9.0e-06 to 4.8e-05), corrected for 6 configuration(s) scanned
  false-positive target 1.0e-04  (deployment policy)
  tokens                412 total, 398 scored  (minimum detectable for this config: 180)
  caveats:
    - statistical evidence; some human texts score this high by chance, at the rate shown
    - paraphrase or editing can remove marks; a positive may cover only part of the text
```

## Try it (no cloud, no model download, ~2 minutes)

```bash
uv venv .venv --python 3.12
uv pip install --python .venv/bin/python -e ".[dev,synthid]" -e packages/markwright-scheme-kgw
./scripts/demo.sh
```

The demo runs the whole loop against a live server and checks its own claims: register a model, create a key in the sealed vault, generate marked tokens, calibrate on the bundled null corpus, activate, then verify marked text (moderate evidence), human text (no evidence), and a 30-token snippet (insufficient evidence, which has no p-value at all). It ends by verifying the signed audit chain offline. A second scheme (KGW) then joins from its own package and both are scanned under one multiple-scan correction.

For the step-by-step version with a real model, see [docs/quickstart.md](docs/quickstart.md). For the dashboard: `cd dashboard && npm install && npm run dev` (API on :8000, UI on :3000).

## What you get

- **Registry**: models, schemes and immutable versioned configurations with a draft → active → deprecated → retired lifecycle. A database trigger enforces the immutability.
- **Key custody**: the database stores references; secret bytes live in a `KeyBackend` (local sealed vault for air-gapped use, HashiCorp Vault / OpenBao Transit with in-boundary derivation). Rotated keys keep verifying old text indefinitely; a revoked key stops marking at once and flags every later match.
- **Calibrated verification**: length check → candidates → detect → calibrate → multiple-scan correction → band. Every p-value is mapped through a null model fitted on human text and reported with its 95% interval, the deployment's false-positive target, and caveats. A calibration that cannot resolve the target caps the evidence band and states why.
- **Signed audit**: hash-chained, Ed25519-anchored, survives restarts, and exports as an evidence bundle that verifies offline.
- **Offline verification**: `markwright verify --offline --bundle` runs the same pipeline from an exported bundle with no server and no network.
- **Inference hooks**: HF `generate` and a vLLM logits-processor wrapper; the hook fetches a generation profile and never holds a long-lived secret.

## What this does not do

The long version ships in the product ([docs/limitations.md](docs/limitations.md)); the short version:

- **It does not detect AI text in general.** It measures evidence for registered marks only. Unmarked models (most of the world's) produce "no evidence", and so does marked text after enough paraphrasing. "No evidence" is never evidence of human authorship, and the result says so.
- **It does not give verdicts.** There is no boolean anywhere in the API; `bool(result)` raises. Text that is too short or too predictable returns *insufficient evidence* before any statistic is computed.
- **It does not prove authorship.** A published detector discloses key material; anyone holding it can forge a mark. Such results carry `spoofing_not_excluded`, permanently.
- **It does not resist determined removal.** Paraphrase, translation and open-weight re-sampling defeat every scheme it wraps, and the result page says so.

## Your text stays yours

Submitted text is never stored: the server keeps a salted digest and the statistics, with a retention policy the admin sets and the UI displays. Audit entries structurally reject text, prompts and secrets. The API never sees prompts or completions at generation time either: the inference hook runs inside *your* serving stack and fetches only configuration and sealed key material. Fully air-gapped deployment is a supported profile, not an afterthought.

## Architecture

```
markwright/
├── src/markwright/
│   ├── schemes/        # SchemeAdapter contract + SynthID-Text adapter
│   ├── keys/           # KeyBackend protocol, HKDF derivation, sealed vault, Vault Transit
│   ├── stats/          # null model (ECDF + GPD tail), bands, calibration math — pure
│   ├── verify/         # scheme-agnostic pipeline + offline bundle verifier
│   ├── registry/       # SQLite/PostgreSQL store behind one interface
│   ├── calibration/    # null-corpus loading + calibration runs
│   ├── audit/          # hash-chained, Ed25519-signed log + evidence bundles
│   ├── api/            # FastAPI — the single surface; everything else is a client
│   ├── inference.py    # hook helpers: generation profiles, vLLM wrapper
│   └── cli/            # markwright CLI (thin API client + offline core)
├── packages/
│   └── markwright-scheme-kgw/   # schemes are SEPARATE packages via entry points —
│                                #   adding one changes zero core lines (tested)
├── schemas/            # JSON Schema wire contract; responses validate against these
├── dashboard/          # React + TS: Verify + Registry screens
├── data/null/          # bundled starter null corpora (provisional-grade, documented)
├── hooks/              # inference-side examples (HF generate, vLLM)
└── docs/               # quickstart, limitations, plan, implementation log
```

New schemes register the `markwright.schemes` entry point from their own package: the wizard lists them, the registry validates their parameters, and the verify pipeline treats their statistic like any other. `packages/markwright-scheme-kgw` is the worked example.

The data model behind all of this is specified as **OWM 0.1 (Open Watermark Manifests)** in [docs/spec/owm-0.1.md](docs/spec/owm-0.1.md): machine-readable scheme descriptors, deployment manifests, signed repo declarations (`watermark.owm.json` for a model repository), and a binding model that computes which serving stacks can run which schemes. The spec is modality-neutral; [docs/spec/extending.md](docs/spec/extending.md) walks through extending it to images with three real schemes (Stable Signature, Tree-Ring, DWT-DCT) shipped as specification-only descriptors.

## Honesty rules (enforced in code, not docs)

Every rule below has a test that fails if it regresses: no boolean result fields anywhere; the length and predictability check runs before any statistic; calibrated p-values with bootstrap intervals, never the analytic value alone; Bonferroni (multiple-scan) correction over every configuration scanned; band capping when the calibration cannot resolve the false-positive target; identical visual treatment for "no evidence" and "insufficient evidence", with one hue and no red or green anywhere; a tokenizer mismatch refuses to score instead of guessing; submitted text never stored.

## Community

- [CONTRIBUTING.md](CONTRIBUTING.md): dev setup, the three test tiers, how work is phased
- [SECURITY.md](SECURITY.md): coordinated disclosure; a key-material leak is the most severe finding
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- Brand assets and usage rules: [assets/brand/](assets/brand/BRAND_GUIDE.md)

## Status

Working POC through v1 infrastructure slice: registry, calibration path, key lifecycle, signed audit + offline evidence, detector publishing, batch verify, offline bundles, OIDC, SQLite/PostgreSQL, local vault + Vault Transit, SynthID-Text + KGW, 2-screen dashboard. See [docs/poc-plan.md](docs/poc-plan.md) for every checkbox and [docs/IMPLEMENTATION_LOG.md](docs/IMPLEMENTATION_LOG.md) for the full build history.

## Licence

Apache-2.0. Contributions under the DCO.
