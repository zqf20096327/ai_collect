# Security Knowledge Base

A local-first, evidence-led repository for security findings, claims, rejected
hypotheses, source provenance, and review decisions. It is designed so different
model hosts can read, search, and propose changes through the same files and
offline command-line protocol.

The interoperability layer is deliberately ordinary:

- Git for history and review;
- canonical UTF-8 JSON for machine records;
- Markdown for instructions and generated human views; and
- a Python standard-library `kb` CLI for bounded access and validation.

Obsidian, a vendor model API, MCP, embeddings, a vector database, and network
access are **not required**. Optional integrations can be added later as wrappers
around the unchanged CLI protocol.

## Install

### Install the cross-model skill

With GitHub CLI 2.90 or newer, preview the skill and install it directly from
this repository:

```sh
gh skill preview dinosn/security-knowledge-base security-kb
gh skill install dinosn/security-knowledge-base security-kb
```

The interactive installer can target Codex, Claude Code, Gemini CLI, and other
supported agent hosts in one pass. For an unattended, user-scoped install, name
each host explicitly; an unflagged non-interactive install defaults to GitHub
Copilot.

```sh
gh skill install dinosn/security-knowledge-base security-kb \
  --agent codex --scope user --pin v1.0.0
gh skill install dinosn/security-knowledge-base security-kb \
  --agent claude-code --scope user --pin v1.0.0
gh skill install dinosn/security-knowledge-base security-kb \
  --agent gemini-cli --scope user --pin v1.0.0
```

Installing the skill installs only the model-neutral operating procedure. It
does not install a knowledge-base repository, copy records, grant access to
evidence, or weaken repository permissions.

### Use the full knowledge-base template

This public upstream is an empty framework and public-data template. Clone it
for evaluation:

```sh
git clone https://github.com/dinosn/security-knowledge-base.git
cd security-knowledge-base
python3 -m unittest discover -s tests -p 'test_*.py' -v
./kb --json capabilities
./kb --json status
./kb --json lint
```

For operational or customer data, create a separate **private** repository from
the template instead of pushing evidence to this public upstream:

```sh
gh repo create OWNER/CASE-security-kb \
  --private \
  --template dinosn/security-knowledge-base \
  --clone
```

Before the first evidence ingestion, a human maintainer must set a unique
`kb_id`, `boundary_id`, title, and correct classification in `kb.json`, configure
the matching encrypted/WORM evidence-object storage and backups, initialize the
repository with a human actor, and commit that clean baseline.

## Security model

One repository is one security boundary. Use a different repository—with its
own access controls, encryption keys, backups, indexes, and model sessions—for
each customer, restricted engagement, or materially different classification.
The `boundary_id` in `kb.json` detects accidental mixing; it does not create
isolation by itself.

Raw evidence is immutable, content-addressed, and untrusted. Source text can
contain prompt injection, false claims, payloads, and misleading instructions.
Ingestion stores bytes and provenance; it never executes, imports, renders, or
trusts the artifact. Generated analysis becomes canonical only after a human
approves the exact proposal digest and promotes it through the CLI.

## Repository layout

```text
AGENTS.md                         canonical cross-model instructions
CLAUDE.md / GEMINI.md             thin model-host adapters
skills/security-kb/               canonical installable Agent Skill
.agents/skills/security-kb        Codex/Gemini link to the canonical skill
.claude/skills/security-kb        Claude Code link to the canonical skill
MODEL_INTERFACE.md                interoperability and generic-model guide
kb.json                           repository identity and boundary policy
catalog/sources/src-*.json        source provenance manifests
objects/sha256/<first2>/<digest>  immutable evidence bytes (local by default)
knowledge/claims/*.json           atomic evidence-backed claims
knowledge/findings/*.json         reviewed security findings
proposals/prp-*.json              staged, non-canonical changes
reviews/rev-*.json                human decisions bound to proposal digests
decisions/rejected/               durable rejected hypotheses and rationale
audit/receipts/                   append-only operation receipts
views/                            deterministic, generated human views
exports/                          reserved generated-output location
schemas/                          normative JSON Schemas
docs/protocol/v1.md               CLI and wire protocol
docs/maintainers/REVIEW.md        review and promotion runbook
prompts/GENERAL_MODEL.md          bootstrap for a model without local tools
```

Evidence objects are ignored by Git by default because repositories may use an
encrypted or WORM object store. Manifests and knowledge records remain
reviewable. An operator must back up the matching objects; a manifest without
its verified bytes is not complete evidence.

## Requirements

- Python 3.11 or newer
- Git
- No third-party Python packages for the version 1 core

The CLI works offline. Run commands from the repository root and use `--json`
for agents and automation:

```sh
./kb --json capabilities
./kb --json status
./kb --json lint
```

Run the complete offline verification suite with:

```sh
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Proposal validation and staging require a real Git `HEAD`, because every
proposal is bound to `base_revision`. After reviewing the scaffold, create the
repository's initial commit before asking a model to propose knowledge changes.

`./kb --help` and `./kb COMMAND --help` show current flags. The normative
behavior, JSON envelope, exit statuses, and compatibility rules are in
[`docs/protocol/v1.md`](docs/protocol/v1.md).

## Maintainer workflow

The high-level flow is:

```text
select an isolated repository
  -> ingest exact source bytes and provenance
  -> search/read bounded records and evidence excerpts
  -> stage a revision-bound proposal
  -> validate and lint
  -> human review of evidence and exact proposal digest
  -> promote the approved digest
  -> regenerate views and verify audit receipts
```

Maintainers control source ingestion, reviews, promotion, and generated views.
Agents can read and search, but their only repository write is a validated file
under `proposals/`. See [`docs/maintainers/REVIEW.md`](docs/maintainers/REVIEW.md)
before accepting a change.

## Cross-model use

- **Codex:** discovers `.agents/skills/security-kb`, a link to the canonical
  skill, and reads the root `AGENTS.md`.
- **Claude Code:** discovers `.claude/skills/security-kb`, a symlink to the
  canonical skill, while `CLAUDE.md` imports the same `AGENTS.md`.
- **Gemini CLI:** natively treats `.agents/skills` as a workspace skill location;
  its link resolves to the canonical skill and `GEMINI.md` imports the same
  `AGENTS.md`.
- **Other tool-capable agents:** explicitly load `AGENTS.md`, then use the JSON
  CLI protocol described in `MODEL_INTERFACE.md`.
- **Chat/upload-only models:** an operator creates a bounded `packet`, supplies
  it with `prompts/GENERAL_MODEL.md`, then locally validates any returned JSON.

"Any model" therefore means any model host that can either read files and run a
local command, or receive a bounded packet through an operator. A bare model has
no filesystem, Git identity, permissions, or ability to update this repository.
Adapter instructions guide behavior; schemas, the CLI, OS permissions, Git
review, and human approval provide enforcement.

The skill is a procedure, not a data store. Models share the KB by operating in
the same access-controlled boundary checkout (or a clone with the matching
evidence-object store). A model without local access receives only an
operator-reviewed bounded packet. Installing the skill does not copy records,
grant access, or declassify evidence.

Invoke the same skill workflow through the host's native mechanism:

- Codex: mention `$security-kb`.
- Claude Code: run `/security-kb` or ask Claude to use the skill.
- Gemini CLI: ask Gemini to use `security-kb` and approve activation; use
  `/skills list` to confirm discovery.

KB sharing is explicit and boundary-scoped:

| Model location | How it receives the KB |
|---|---|
| Same workstation | Start the model host inside this checkout; every host reads the same records and invokes the same `./kb --json` CLI. |
| Different controlled workstation | Clone the access-controlled Git repository and separately synchronize its matching encrypted evidence-object store. Git alone is incomplete because `objects/sha256` is ignored by default. |
| Model without filesystem or shell access | Give it only an operator-reviewed `skb.context-packet/v1`; validate its raw JSON response locally before staging. |

Never use one checkout or packet to mix customers, engagements, or incompatible
classifications. For those cases, create separate KB repositories and model
sessions.

## Version 1 limitations

- Search is deterministic lexical search. Good IDs, aliases, CVEs, CWEs,
  ATT&CK IDs, tags, products, versions, and explicit links are important.
- A digest proves byte identity, not truth or exploitability.
- JSON validity does not establish factual correctness.
- Model output can fabricate evidence or ignore instructions and must be
  validated and reviewed.
- Large artifacts and full repositories require bounded excerpts; loading all
  content into a model is neither reliable nor safe.
- Public export/redaction, sandboxed extractors, signed attestations, and an
  optional per-boundary full-text index are deferred.
- Evidence objects are intentionally Git-ignored. Configure encrypted/WORM
  storage and backup before operational use; the CLI otherwise keeps them only
  in the repository's local filesystem.
