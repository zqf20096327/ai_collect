<div align="center">
  <img src="https://raw.githubusercontent.com/Skull-boy/scyvera/main/assets/scyvera-mark.svg" alt="Scyvera" width="170">

# Scyvera

**Set the boundary once. Get it enforced everywhere. Prove it forever.**

Operational contracts for AI agents: what a system can do, what it can access, and what it must never do — enforced at runtime and provable after the fact.

[![License](https://img.shields.io/github/license/Skull-boy/scyvera)](./LICENSE) [![PyPI](https://img.shields.io/pypi/v/scyvera)](https://pypi.org/project/scyvera/) [![PyPI Downloads](https://static.pepy.tech/personalized-badge/scyvera?period=total&units=INTERNATIONAL_SYSTEM&left_color=RED&right_color=GREEN&left_text=downloads)](https://pepy.tech/projects/scyvera) [![npm](https://img.shields.io/npm/v/@scyvera/scyvera-ts)](https://www.npmjs.com/package/@scyvera/scyvera-ts) [![CI](https://github.com/Skull-boy/scyvera/actions/workflows/validate-contracts.yml/badge.svg)](https://github.com/Skull-boy/scyvera/actions/workflows/validate-contracts.yml) [![Blast Radius](https://img.shields.io/badge/blast%20radius-Shielded-green)](#proof-not-promises) [![Docs](https://img.shields.io/badge/docs-quickstart-blue)](./docs/quickstart.md)
</div>

---

MCP and A2A standardize how agents talk to tools and to each other. Scyvera defines the layer above
them: the boundary those agents run inside. It is framework-independent and domain-independent, and
the contract is a file — not a prompt.

```bash
pip install scyvera && scyvera audit .
```

## See it run

`pip install scyvera && scyvera audit .` inside this repository:

```text
WARN  .
      Blast Radius: 92/100 (Shielded)
      raw (all findings): 82/100 (Controlled)

      MEDIUM    [AU-N8N-001] n8n workflow with external writes
                implementations/n8n/competitor-feature-parity-watcher/workflow.json:169 + 3 more
      MEDIUM    [AU-NET-002] outbound network calls in source
                implementations/langgraph/duplicate-issue-detector/backfill.py:23 + 1 more

      GOVERNED  [AU-CI-002] deploy or publish job detected
                .github/workflows/publish-scyvera-rs.yml:45 + 1 more
                registry:publish declared and approved in contract.yaml
```

Those publish workflows are this repository's own npm and crates.io releases. They are measured and
**governed, not waived**: `contract.yaml` declares `registry:publish` and requires a named approver,
so the findings leave the governed score, stay visible in the report with `governed_by`, and still
count in the raw number ([RFC 0004 Amendment 2](./rfcs/0004-amendment-2-governed-findings.md)). The
scan is read-only; it did not change a file.

The **TypeScript runtime** gates the same contract with no install — the contract is the artifact,
and every runtime reads the same bytes:

```bash
npx scyvera-ts gate --contract contract.yaml --mode full \
  --action github:issues:read --action-type permission
# ALLOWED  github:issues:read
npx scyvera-ts vectors --root vectors     # 33/33 at suite-version 1
```

![Scyvera in 23 seconds: scan, draft, and a blocked action](https://raw.githubusercontent.com/Skull-boy/scyvera/main/assets/scyvera-demo.gif)

## Quickstart

**1. Scan.** What can this environment actually do?

```bash
scyvera audit .
```

**2. Draft.** The scan writes your first contract; you never start from a blank page.

```bash
scyvera audit . --generate contract.yaml
```

```yaml
version: 1.1
system:
  name: research-agent
permissions: [github:issues:read]
side_effects:
  - {resource: github, type: comment}
approvals:
  - {action: github:comment, required: true}
```

**3. Verify.** The draft is schema-valid and lint-clean by construction.

```bash
scyvera validate contract.yaml && scyvera lint contract.yaml
```

**4. Enforce.** Load the contract, gate the tools, and let undeclared calls fail closed.

```python
from scyvera import ContractEnforcer

enforcer = ContractEnforcer.load("contract.yaml")

@enforcer.gate("github:issues:read", "permission")
def read_issue(number: int): ...

@enforcer.gate("github:comment", "side_effect")
def comment(number: int, body: str): ...   # requires approval until enforcer.approve(...)
```

**5. Expose it to an agent host.** The same engines over MCP, no shelling out:

```bash
scyvera serve-mcp   # five tools over stdio — see docs/mcp.md
```

## Capabilities

| You want to… | Use | Docs |
|---|---|---|
| See what a repo can actually do | `scyvera audit` — deterministic AUxxx scan, Blast Radius bands, badge, CI floor | [Quickstart](./docs/quickstart.md) |
| Turn findings into a boundary | `--generate` drafts a schema-valid v1.1 contract; `--pack` starts from a policy | [Policy Packs](./docs/policy-packs.md) |
| Check code against its contract | `scyvera check` — Tier 0 structural, Tier 1 static (n8n, LangGraph) | [Conformance](./docs/conformance.md) |
| Gate Python calls at runtime | `ContractEnforcer` — default-deny, approvals, identity pinning | [Python API](./docs/python-api.md) |
| Bound behavior, not just actions | v1.2 `guardrails` — rate limits, side-effect budgets, fail-closed | [Python API](./docs/python-api.md) |
| Score what an agent actually did | `scyvera eval` — four axes over RFC 0003 traces | [Evals](./docs/evals.md) |
| Prove which contract governed what | Hash-chained registry, time-travel queries, re-seal, human promotion | [Python API](./docs/python-api.md) |
| Expose tools to an agent host | `scyvera serve-mcp` — five MCP tools over stdio | [MCP server](./docs/mcp.md) |
| Gate CI and adopt a runtime | `scyvera-gate` Action, harness skill, per-target kits (n8n, LangGraph) | [Kits](./kits/README.md) |

## How it works

<img src="https://raw.githubusercontent.com/Skull-boy/scyvera/main/assets/hero-flow.svg" alt="Scan, draft, enforce, prove" width="100%">

- **Scan** is pattern-level and review-grade; it tells you what the code can reach, not what it does.
- **Draft** produces one schema-valid contract, the same format hand-authored contracts use.
- **Enforce** is default-deny: undeclared calls raise, approval boundaries stop execution, and every
  decision is written to an audit trail.
- **Prove** is trace + registry: what ran, under which contract, and whether that contract ever
  changed.

## Runtimes

One standard, three native implementations. Every one passes the same shared corpus.

| Runtime | Install | Status | Vectors |
|---|---|---|---|
| **Python** (reference) | `pip install scyvera` | `1.4.0` on PyPI | 33/33 |
| **TypeScript** | `npm install @scyvera/scyvera-ts` | `0.1.1` on npm, OIDC + SLSA provenance | 33/33 |
| **Rust** | `cargo install scyvera-rs` | `0.1.1` on crates.io — OIDC trusted publishing, human-gated, attested `.crate` | 33/33 |

`vectors/` is the acceptance corpus: `suite-version: 1`, 33 vectors across contract-model,
gate-decision, and trace-roundtrip. A runtime that passes a subset is not conformant.

## Use it from your agent host

[`skills/scyvera-governance/`](./skills/scyvera-governance) is an Agent Skill: it teaches a host to
run the CLI and the MCP tools and to report their verdicts unchanged. It grants no authority — the
engines still decide, and a misbehaving agent is caught by the same exit codes.

Copy the folder into the host's skills directory, keeping its name:

| Host | Project path | Global path | Invoke with |
|---|---|---|---|
| **Claude Code** | `.claude/skills/` | `~/.claude/skills/` | `/scyvera-governance` |
| **Codex** | `.agents/skills/` | `~/.agents/skills/` | `$scyvera-governance` |
| **OpenCode** | `.opencode/skills/` or `.agents/skills/` | `~/.config/opencode/skills/` | `@scyvera-governance` |
| **Antigravity** | `.agents/skills/` | `~/.gemini/config/skills/` | `/scyvera-governance` |

```bash
git clone --depth 1 https://github.com/Skull-boy/scyvera /tmp/scyvera

cp -R /tmp/scyvera/skills/scyvera-governance .agents/skills/   # Codex, OpenCode, Antigravity
cp -R /tmp/scyvera/skills/scyvera-governance .claude/skills/    # Claude Code

pip install scyvera   # the skill drives the CLI; it does not bundle a runtime
scyvera --version
```

On Windows, copy the folder by hand. The skill is self-contained (no network, no secrets, no
`sudo`), hash-locked in `skills-registry.json`, and the same `SKILL.md` works in all four hosts.
If your host prefers MCP over skills, register `scyvera serve-mcp` instead — the same five tools
are there ([docs/mcp.md](./docs/mcp.md)).

## Proof, not promises

- **33/33** vectors at suite-version 1 — Python, TypeScript, and Rust, in their own CI.
- **92/100 `Shielded`** is this repository's own governed audit score, with **raw 82/100
  `Controlled`** always reported beside it. Both numbers and the exact scored/governed surface are
  pinned by a covenant test; they move only through an RFC amendment.
- **Signed installs**: `scyvera self-check` verifies 37 shipped files, and releases carry Sigstore
  build provenance plus a CycloneDX 1.5 SBOM.
- **Same suite everywhere**: Linux and Windows on Python 3.10–3.14 gate every pull request (10
  cells, `fail-fast: false`); macOS runs all five versions in a
  [nightly job](.github/workflows/macos-nightly.yml). macOS is not on the merge gate because its
  hosted runners were failing ~45% of the time (measured 2026-11-24) — a gate that random is not a
  gate. The two sets together are still the full 15-cell matrix.

## Honest limits

1. **Gate bypass at call sites (T4)** — enforcement happens at `@enforcer.gate(...)`. Use the gateways
   so credentials and raw clients stay private, and `assert_gated()` in integration tests.
2. **Third-party internals (T6)** — Scyvera verifies declared intent, not a library's background
   calls. There is no bytecode or packet inspection.
3. **Pre-load tampering (T5)** — integrity checks are post-load. The registry, identity pinning, and
   re-seal cover history; they cannot prove a file was clean before it was read.
4. **Install integrity is not a sandbox (T11)** — `self-check` verifies the installed package, not
   your interpreter, your site-packages, or code installed beside it.

5. **Governed is not waived (governed findings)** — a finding your contract declares *and* approves
   leaves the governed score but stays in the report with `governed_by`, and `raw_score` always shows
   what it would be. A provisional contract, an undeclared permission, `required: false`, or a
   nameless approver governs nothing.

Full threat models: [`lifecycle`](./docs/threat-model-lifecycle.md) ·
[`enforcer`](./docs/threat-model-enforcer.md) · [`distribution`](./docs/threat-model-distribution.md).

## Documentation

| Start | Go deeper |
|---|---|
| [Quickstart](./docs/quickstart.md) — audit → draft → enforce | [Python API](./docs/python-api.md) — enforcer, gateways, registry, re-seal |
| [Install & verify](./docs/install.md) — platforms, `self-check`, attestations | [Conformance](./docs/conformance.md) — tiers and `T101`–`T103` |
| [Contract reference](./docs/contract-reference.md) — field-by-field | [Evals](./docs/evals.md) — case format and scoring axes |
| [MCP server](./docs/mcp.md) — host config, five tools | [Roadmap](./docs/roadmap.md) — what shipped, what is next |

Background: [vision](./docs/vision.md) · [design principles](./docs/design-principles.md) ·
[architecture](./docs/architecture.md) · [RFCs](./rfcs) · [SPEC](./WORKFLOW-CONTRACT-SPEC.md).

## Contributing

Contributions are welcome: audit rules with fixtures, Policy Packs, framework reference
implementations, runtime work, and documentation. Start with
[CONTRIBUTING.md](./CONTRIBUTING.md) and the
[`good first issue`](https://github.com/Skull-boy/scyvera/labels/good%20first%20issue) label.

If Scyvera is guarding something real in your stack, add yourself to [ADOPTERS.md](./ADOPTERS.md) —
the honest version of a logo wall.

Security issues: [SECURITY.md](./SECURITY.md).

## License

MIT — see [LICENSE](./LICENSE). Maintained by [Shinjan Das](https://github.com/Skull-boy) and
open-source contributors; see [CONTRIBUTORS.md](./CONTRIBUTORS.md).
