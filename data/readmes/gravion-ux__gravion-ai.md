# gravion-ai

[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-385-brightgreen.svg)](#testing)
[![codecov](https://codecov.io/gh/gravion-ux/gravion-ai/branch/main/graph/badge.svg)](https://codecov.io/gh/gravion-ux/gravion-ai)
[![CI](https://github.com/gravion-ux/gravion-ai/actions/workflows/ci.yml/badge.svg)](https://github.com/gravion-ux/gravion-ai/actions/workflows/ci.yml)

**Gravion AI — one modular AI platform, every kind of AI a startup needs, ready to rename, re-policy and run as your own.**

Startups building an AI product today start from zero: months of plumbing
before the first useful answer. Gravion AI is the base they should start
from instead — a single module system that carries many kinds of AI
(chat, support, coding, website building, music, image, video, security,
agentic tools, and an all-in-one package), offered at four tiers of
readiness, under one licensing and identity layer.

You give it a name (the default is **Gravion**), teach it your company
and your work policy, and run it — on the built-in **Gravion Core**
engine, or on any inference endpoint you operate, with your own API key.

> **Status — read this before expecting magic.** Gravion AI is
> built in pieces, and the piece roadmap in
> [ARCHITECTURE.md](ARCHITECTURE.md) is **complete**: every module
> is implemented, every tier bundle is packaged, and the services
> (licensing authority, governed self-upgrade, training pipelines)
> are built. What the pieces do *not* contain — by design, and
> stated plainly wherever it matters — is trained model weights
> or public hosting: the bundles are the packaging and protocol
> around models the project trains and hosts as operations steps.
> Piece 1 shipped the *foundation*: the core scaffold,
> the module registry with one module (chat) wired end-to-end, the
> Gravion model registry with starter data, and the complete licensing
> subsystem. Piece 2 adds the **support** and **coder** modules, wired
> end-to-end on the same path, and the first trained bundles of
> **Gravion Chat** and **Gravion Code** at Tier 2 (Basic). Piece 3 adds
> the **image** and **music** modules on the same path — each turns a
> request into a structured brief (mode/kind, aspect, duration, mood)
> for its model — and the first trained bundles of **Gravion Vision**
> and **Gravion Audio** at Tier 2 (Basic). Piece 4 adds the **video**
> module on the same path — a structured brief (mode, duration,
> aspect, reference frames) for **Gravion Video**, whose first trained
> bundle ships at Tier 2 (Basic) — plus an offline local renderer
> that turns a request into a real short MP4 for development. The
> long-form pipeline (scene planning and stitching, up to ~1 hour)
> remains **planned** with the higher-tier bundles. Piece 5 adds the
> **website-builder** module on the same path — a structured brief
> (mode, site type, pages, style) for **Gravion Builder**, whose
> first trained bundle ships at Tier 2 (Basic) — plus an offline
> local builder that turns a brief into a real static website
> (HTML, CSS and JS files) for development. Piece 6 adds the
> **cyber** and **agentic** modules on the same path — cyber briefs
> (task, deterministically extracted indicators, stated severity)
> for **Gravion Shield** and agent briefs (task, tools, steps) for
> **Gravion Agent**, whose first trained bundles ship at Tier 2
> (Basic) — plus an offline local planner that writes structured
> agent plan files (plans only; the local planner executes
> nothing). Piece 7 packages the tiers: every specialist model is
> now offered as **Tier 1 (Complete)** and **Tier 3
> (Intermediate)** bundles alongside Tier 2, tier bundles get
> completeness checks and deterministic hashed descriptors
> (`gravion bundles`), and training jobs get a spec + validator
> (`gravion train`) — running one still requires the hosted
> training pipeline and says so. Piece 8 completes the platform:
> the **all-in-one** module (routing by `<module>:` directive,
> chat by default) and **Gravion Omni**, the Tier 4 (Advanced)
> flagship serving every capability — every module is now
> implemented and every tier bundle is complete. What remains on
> the roadmap is services, not modules: the hosted licensing
> authority, the governed self-upgrade service, and the customer
> training pipelines. Piece 9 implements the **hosted licensing
> authority service**: a standard-library HTTP service running the
> §8.4 entitlement protocol (`gravion authority serve`), verified
> end-to-end against a live server in the test suite — where it is
> publicly hosted is an operations decision, not a code one.
> Piece 10 implements the **governed self-upgrade service** (§9):
> a standing operator permission, issuer-signed update packages,
> bugfix/enhancement scope only, changelogs written before
> activation, retained previous versions, and automatic rollback
> on a failed self-check (`gravion upgrade`). Piece 11 completes
> the roadmap with the **training pipelines**: dataset preparation
> for customer fine-tuning — strict validation, deduplication, a
> deterministic train/validation split and a hashed dataset
> report (`gravion train prepare`) — feeding the job pipeline
> from Piece 7.

---

## The four tiers

Tiers are readiness levels over the *same* modules — what changes is
how trained each module is when it reaches you.

| Tier | Name | What you get |
|---|---|---|
| 1 | **Complete** | A complete, ready AI. Name it, teach it your company + policy, use it. |
| 2 | **Basic** | Basic-trained variants of every module — a working base you keep training on your own data. |
| 3 | **Intermediate** | Already trained to a level that takes a startup years to reach in-house. |
| 4 | **Advanced** | The top tier: advanced-trained modules on the full Gravion platform, headroom to go further. |

Every tier: renameable (default name *Gravion*), company-policy
injection, your own endpoint + API key if you want one, and **governed
self-upgrade** — Gravion may propose bug fixes and enhancements, but it
applies them only after your one-time explicit permission, with every
change logged and reversible.

## Modules

| Module | Type | Status |
|---|---|---|
| chat | Chat bot | ✅ implemented (reference module) |
| support | Support bot | ✅ implemented (Piece 2) |
| coder | Coding assistant | ✅ implemented (Piece 2) |
| website-builder | Website builder | ✅ implemented (Piece 5) |
| music | Music generation | ✅ implemented (Piece 3) |
| image | Image generation/editing | ✅ implemented (Piece 3) |
| video | Video generation/editing (long-form pipeline planned) | ✅ implemented (Piece 4) |
| cyber | Cyber/security AI | ✅ implemented (Piece 6) |
| agentic | Agentic tool developer | ✅ implemented (Piece 6) |
| all-in-one | Every module, one deployment | ✅ implemented (Piece 8) |

Modules are sold/used individually (variant packages) or together
(all-in-one). Each module declares the capability it needs; the
**Gravion model registry** resolves which Gravion model serves it.

## The Gravion model registry

Gravion's own models, registered as data (`src/gravion_ai/data/models.json`),
not hardcoded logic: **Gravion Core** (the built-in offline engine —
*available now*), **Gravion Chat** and **Gravion Code** (*available
since Piece 2* as Tier 2 first trained bundles), **Gravion Vision** and
**Gravion Audio** (*available since Piece 3* as Tier 2 first trained
bundles), **Gravion Video** (*available since Piece 4* as a Tier 2
first trained bundle), **Gravion Builder** (*available since
Piece 5* as a Tier 2 first trained bundle), **Gravion Shield** and
**Gravion Agent** (*available since Piece 6* as Tier 2 first
trained bundles),
and **Gravion Omni** (*available since Piece 8*), the all-in-one flagship at the Advanced tier.
Deployments can register private variants by dropping their own
`models.json` into the deployment home — same schema, same validation.

```bash
gravion models list                     # the whole registry
gravion models list --capability video  # only models that serve video
```

## Requirements

- **Python 3.10 or newer** (CI tests 3.10, 3.11 and 3.12).
- **One runtime dependency:** `cryptography>=41`, which provides the
  Ed25519 signatures the licensing subsystem is built on. Everything
  else is the Python standard library.
- **Development mode needs no license and no network** — it runs fully
  offline on the built-in Gravion Core engine. Running against your
  own inference endpoint instead requires that endpoint and your own
  API key.
- **Production use** additionally requires a signed commercial
  agreement (see [Licensing](#licensing--the-short-version)).
- **For the test suite:** `pip install -e ".[dev]"` (adds `pytest`
  and `pytest-cov`).

## Quick start

Requires Python 3.10+.

```bash
git clone https://github.com/gravion-ux/gravion-ai.git
cd gravion-ai
pip install -e .

gravion init --name Gravion --company "Acme Robotics"
gravion status
gravion chat "hello, what are you?"
gravion support "where is my invoice?"
gravion export --out my-deployment.zip
```

Development mode needs **no license** and runs fully offline on
Gravion Core. Edit `policy.md` in the deployment home
(`~/.gravion-ai` by default, or `$GRAVION_HOME`) — that file is your
company policy, injected into every module's system context.

## Usage

Day-to-day commands once a deployment exists:

```bash
gravion models list                       # the Gravion model registry
gravion models list --capability video    # only models that serve video
gravion chat "hello, what are you?"       # the reference module
gravion support "where is my invoice?"    # the support module
gravion modules list                      # installed modules
gravion license identity                  # this deployment's cryptographic identity
gravion license audit verify              # verify the tamper-evident audit chain
gravion export --out my-deployment.zip    # export config, policy, registry and data
```

Your company policy lives in `policy.md` in the deployment home
(`~/.gravion-ai` by default, or `$GRAVION_HOME`) and is injected into
every module's system context — edit it to teach the deployment your
company and your rules.

## Demo

The exact sequence CI runs on every push — development mode, no
license, fully offline on Gravion Core:

```bash
export GRAVION_HOME=$(mktemp -d)
gravion init --name Gravion
gravion status
gravion modules list
gravion chat "hello gravion"
```

## Licensing — the short version

Gravion AI is built to be a commercial platform, and its licensing is
designed in two separate layers (full detail: [docs/LICENSING.md](docs/LICENSING.md)):

- **Legal entitlement.** Development and evaluation are free. Running
  Gravion in **production** requires a signed commercial agreement,
  which includes a negotiated **10–20% equity partnership**. The
  agreement commits Gravion to **no destructive kill switch**: the
  worst outcome of a lapsed agreement is suspension, never data loss.
- **Technical enforcement.** Every deployment has a cryptographic
  identity (Ed25519). Licenses and module manifests are issuer-signed
  and verified before anything runs in production. A server-side
  entitlement protocol (four fields only — deployment id, license
  hash, module, timestamp; no user data, ever) issues short-lived
  signed tokens, with a signed cache for offline grace. Every
  licensing event lands in a **tamper-evident, hash-chained audit
  log**. Suspended? `gravion export` still gives you everything —
  config, policy, registry, audit log and all your data.

```bash
gravion license identity        # this deployment's cryptographic identity
gravion license audit verify    # check the audit chain
```

## Limitations

- **No trained model weights or public hosting ship with this code.**
  The bundles are the packaging and protocol around models; training
  and hosting them are operations steps, as stated in the status note
  at the top of this README.
- **The long-form video pipeline is planned, not implemented.** The
  video module produces structured briefs and a short offline MP4 for
  development; scene planning and stitching up to ~1 hour remains on
  the roadmap.
- **The local agentic planner executes nothing.** It writes structured
  plan files for review — acting on them is a separate, deliberate
  step.
- **Training jobs do not run here.** `gravion train` validates a job
  spec and `gravion train prepare` prepares datasets (validation,
  deduplication, deterministic split), but running a job requires the
  hosted training pipeline, and the CLI says so rather than
  pretending.
- **Production is gated, by design.** Without a signed agreement and
  issuer-signed licenses, a deployment stays in development mode.

## Repository layout

```
src/gravion_ai/
  config.py       deployment config, naming, company-policy injection
  registry.py     the module system (manifest + entrypoint, catalogue)
  catalog.py      the Gravion model registry (loader + validation)
  bundles.py      tier bundles: completeness checks + hashed descriptors
  upgrades.py     governed self-upgrade (§9): permission, signed
                  update packages, self-check, rollback
  training/       training jobs: spec, validation, honest run refusal
  data/models.json  the registry's starter data
  providers.py    Gravion Core (built-in) + generic endpoint plumbing
  runtime.py      gate → verify → resolve → run; export
  modules/chat/   the reference module, wired end-to-end
  modules/support/  support bot: policy-grounded answers, human escalation
  modules/coder/    coding assistant: generate / review / explain tasks
  modules/image/    image generation/editing: generate / edit briefs
  modules/music/    music generation: track / jingle / score briefs
  modules/video/    video generation/editing: generate / edit briefs
                    + the local MP4 render pipeline
  modules/website_builder/  website building: build / iterate briefs
                    + the local static-site builder
  modules/cyber/    defensive security: analyse / triage / report
                    briefs with indicator extraction
  modules/agentic/  tool-using agents: plan / build / run briefs
                    + the local plan writer
  modules/all_in_one/  every module under one deployment: routing
                    by directive to the target module
  licensing/      identity, signed licenses, signed modules, audit log,
                  entitlement protocol + gate — the licensing subsystem;
                  authority_server.py is the hosted authority service
docs/LICENSING.md       licensing design + protocol specification
LICENSE-COMMERCIAL.md   commercial agreement template (summary terms)
ARCHITECTURE.md         the full vision and piece-by-piece roadmap
```

## Testing

```bash
pip install -e ".[dev]"
python -m pytest -q
```

385 tests cover the licensing subsystem end-to-end (identity, signed
licenses, tamper rejection, audit-chain verification, the entitlement
protocol and its pinned privacy field set, gate states, suspension,
export-while-suspended), the Piece 2 support and coder modules
(grounding addendum, human escalation that never reaches the model,
coder task detection, Tier 2 bundle resolution, production runs of
both modules under signed manifests), the Piece 3 image and music
modules (mode/kind detection, aspect/duration/mood brief parsing,
Tier 2 bundle resolution for Gravion Vision and Gravion Audio), the
Piece 4 video module (mode/duration/aspect/reference-frame brief
parsing, the local MP4 render pipeline — real renders verified with
ffprobe, missing-frame and long-form refusals — and Tier 2 bundle
resolution for Gravion Video), the
Piece 5 website-builder module (mode/site-type/pages/style brief
parsing, the local static-site builder — real HTML/CSS/JS sites
written to disk, determinism, empty-brief refusals — and Tier 2
bundle resolution for Gravion Builder), the
Piece 6 cyber and agentic modules (task detection, indicator
extraction and severity parsing for cyber briefs; tool/step
parsing and the local plan writer — honest plan files, never
executions — for agent briefs; Tier 2 bundle resolution for
Gravion Shield and Gravion Agent), the
Piece 7 tier bundles (completeness per tier, deterministic hashed
descriptors, the honest Tier 4 refusal) and training jobs (spec
validation against the catalog, the no-backend run refusal), the
Piece 8 all-in-one module (directive routing with the target
module's own briefs, self-routing refusal, Omni-only model
resolution for the package) and Tier 4 completeness, the
Piece 9 authority service (health + entitlement over real HTTP,
malformed/unknown-license refusals, a production gate running
against the live service), the
Piece 10 governed self-upgrade (permission refusals, tampered /
unsigned / out-of-scope package refusals, changelog-before-
activation, retained backups, automatic rollback on a failed
self-check, manual rollback, grant/revoke persistence), the
Piece 11 dataset preparation (strict line validation, dedupe,
deterministic hashed splits, directory sources, refusal of
invalid or empty datasets), plus
config, providers, registry, catalog and the CLI.

## Author

Priyanshu Kumar Thakur — [github.com/gravion-ux](https://github.com/gravion-ux)

## Licence

Source code: MIT (see [LICENSE](LICENSE)). Production deployments are
additionally governed by the commercial agreement —
[LICENSE-COMMERCIAL.md](LICENSE-COMMERCIAL.md).

## Sponsors

Sponsorship pays for the maintenance, triage and release time behind this tool. Sponsors are
listed here by name, and name placement starts at the $25 a month Sponsor tier or the $50
one-time Sponsor tier.

- [Sponsor on GitHub](https://github.com/sponsors/gravion-ux)

Sponsorship supports the open-source source code. Commercial deployments remain governed by
the commercial licence agreement.
