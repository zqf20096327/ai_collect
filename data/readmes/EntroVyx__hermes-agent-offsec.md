<p align="center">
  <img src="assets/banner.png" alt="Hermes Agent Offsec" width="100%">
</p>

# Hermes Agent Offsec ☤
<p align="center">
  <a href="https://github.com/EntroVyx/hermes-agent-offsec">Repository</a> | <a href="https://github.com/EntroVyx/hermes-agent-offsec/tree/main/apps/desktop">Desktop App</a>
</p>
<p align="center">
  <a href="https://github.com/EntroVyx/hermes-agent-offsec/releases"><img src="https://img.shields.io/badge/Releases-GitHub-red?style=for-the-badge" alt="Releases"></a>
  <a href="https://github.com/EntroVyx/hermes-agent-offsec/issues"><img src="https://img.shields.io/badge/Issues-GitHub-red?style=for-the-badge" alt="Issues"></a>
  <a href="https://github.com/EntroVyx/hermes-agent-offsec/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-darkgreen?style=for-the-badge" alt="License: MIT"></a>
  <a href="https://github.com/EntroVyx"><img src="https://img.shields.io/badge/Maintained%20by-EntroVyx-red?style=for-the-badge" alt="Maintained by EntroVyx"></a>
</p>

**Hermes Agent Offsec** is not the same product as the original [Hermes Agent](https://github.com/NousResearch/hermes-agent).

The original Hermes is a general-purpose personal AI agent. Hermes Agent Offsec keeps that strong multi-surface foundation, but reshapes the operator experience around authorized offensive security: bug bounty, pentest, recon, manual testing, exploit chaining, target dossiers, and report-ready evidence.

This fork openly builds on Hermes Agent. It is not a plagiarism mirror or a blind re-upload of upstream. The difference is the mission: **Hermes original is broad AI assistance; Hermes Agent Offsec is an offensive-security operator built for impact-driven hunting.**

---

## What Is Different

Hermes Agent Offsec adds an offsec-first workflow layer:

- **Crown-jewel hunting**: start from the highest-value impact, not a generic checklist.
- **Deep manual attack modes**: focus on business workflows like recovery, billing, GraphQL, imports, exports, roles, support, AI/RAG, and races.
- **Persistent target dossiers**: keep actors, object families, states, request maps, hypotheses, evidence, and chain candidates across sessions.
- **HAR/Burp request importing**: turn captured traffic into endpoint clusters, risky parameters, object IDs, and suggested attack modes.
- **Visible exploit-chain engine**: every primitive is pushed toward `primitive -> pivot -> impact`.
- **Offsec skill library**: recon, Web2/Web3, cloud, CI/CD, OAuth/SAML, GraphQL, SSRF, IDOR, business logic, mobile, AI, reporting, and validation skills.

The core idea is simple: scanners find surface area; Hermes Agent Offsec tries to reason like a manual hunter.

---

## Attack Modes

Inside `hermes`, use the slash modes below:

```text
/crown-jewel <target>
/target-dossier <target>
/request-import <path-to-har-or-raw-request>
/deep-hunt <workflow>
/attack-chain <primitive-or-finding>
```

Recommended flow:

```text
/crown-jewel example.com
/target-dossier example.com
/request-import traffic.har
/deep-hunt billing
/attack-chain "refund succeeds while entitlement stays active"
```

Useful deep-hunt workflows:

```text
recovery, invite, billing, graphql, import, export, roles,
support, ai, race, oauth, saml, upload, webhook, generic
```

What each mode does:

- `/crown-jewel` chooses the highest-impact objective: ATO, tenant breakout, financial impact, data exposure, CI/CD compromise, cloud/control-plane access, or AI/RAG leakage.
- `/target-dossier` creates or updates `.offsec/campaigns/<target>/TARGET.md`, `CAMPAIGN.md`, `request-map.md`, `chains/`, `evidence/`, and `imports/`.
- `/request-import` parses HAR or raw Burp/Caido requests and extracts methods, paths, parameters, auth artifacts, object ID candidates, and suggested deep-hunt modes.
- `/deep-hunt` attacks one workflow across actor, object, state, shape, time, and side-effect boundaries.
- `/attack-chain` converts a primitive into a visible chain card with missing proof, next pivots, chainability score, and reportability direction.

---

## Quick Install

### Linux, macOS, WSL2

```bash
curl -fsSL https://raw.githubusercontent.com/EntroVyx/hermes-agent-offsec/main/scripts/install.sh | bash
hermes
```

The installer clones this fork, installs managed `uv`, provisions Python 3.11,
creates an isolated venv, installs the curated `.[all]` profile there, and
wires the `hermes` command. By default it keeps code and data under
`~/.hermes-offsec/`, separate from the original Hermes Agent.

Kali/Debian direct-user install is available only as an advanced fallback when
you intentionally want Hermes on the VM's Python path instead of an isolated
venv:

```bash
git clone https://github.com/EntroVyx/hermes-agent-offsec.git
cd hermes-agent-offsec
python3 -m pip install --user -e . --break-system-packages
hermes setup
hermes
```

Use `.[all]` inside a virtual environment. For direct Kali installs, the lean
base profile avoids forcing optional gateway, Google, dashboard, and media
dependencies into Kali's shared Python environment. Some resolver warnings that
mention Kali tools such as Faraday, NetExec/CrackMapExec, AutoRecon, or OpenVAS
can still refer to packages already present in Kali; Hermes does not install
those tools.

### Windows (native, PowerShell)

```powershell
iex (irm https://raw.githubusercontent.com/EntroVyx/hermes-agent-offsec/main/scripts/install.ps1)
hermes
```

Windows installs under `%LOCALAPPDATA%\hermes-offsec` unless `HERMES_HOME` is
set.

## Getting Started

```bash
hermes              # Interactive CLI — start a conversation
hermes model        # Choose your LLM provider and model
hermes tools        # Configure which tools are enabled
hermes config set   # Set individual config values
hermes gateway      # Start the messaging gateway (Telegram, Discord, etc.)
hermes setup        # Run the full setup wizard (configures everything at once)
hermes claw migrate # Migrate from OpenClaw (if coming from OpenClaw)
hermes update       # Update to the latest version
hermes doctor       # Diagnose any issues
```

`/update` and `hermes update` now follow this fork's own repository and installer paths.

## Example Session

```text
hermes
> /crown-jewel acme.example
> /target-dossier acme.example
> /request-import ./traffic/acme.har
> /deep-hunt recovery
> /attack-chain "stale invite token can be redeemed after role change"
```

The agent should maintain the dossier, update hypotheses, avoid repeating dead branches, and keep pushing weak primitives toward concrete business impact.

---

## Troubleshooting

For platform-specific installer quirks, first run:

```bash
hermes doctor
```

If the issue is inherited from the upstream Hermes foundation, the original
project's documentation can still be useful as background. For this fork, open
issues here:

- https://github.com/EntroVyx/hermes-agent-offsec/issues

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Keep the virtual environment outside
the repository checkout.

```bash
git clone https://github.com/EntroVyx/hermes-agent-offsec.git
cd hermes-agent-offsec
uv venv ~/.hermes/venvs/hermes-offsec-dev --python 3.11
source ~/.hermes/venvs/hermes-offsec-dev/bin/activate
uv pip install -e ".[all,dev]"
scripts/run_tests.sh
```

---

## License

MIT — see [LICENSE](LICENSE).

Maintained by [EntroVyx](https://github.com/EntroVyx).
