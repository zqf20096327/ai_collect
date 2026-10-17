<div align="center">

<a href="https://ibl.ai"><img src="https://ibl.ai/images/iblai-logo.png" alt="ibl.ai" width="300"></a>

# Financial Services Agents

Drop-in [OpenClaw](https://github.com/iblai/iblai-claw-setup) / [NemoClaw](https://github.com/NVIDIA/NemoClaw) agent configuration for the [ibl.ai](https://ibl.ai) **Financial Services** solution segment — one Advisory Assistant orchestrator plus 12 specialist subagents, packaged so a NemoClaw host can import the whole roster with zero conversion.

[![OpenClaw](https://img.shields.io/badge/OpenClaw-292929?logoColor=white)](https://github.com/iblai/iblai-claw-setup)
[![NemoClaw](https://img.shields.io/badge/NemoClaw-76B900?logo=nvidia&logoColor=white)](https://github.com/NVIDIA/NemoClaw)
[![ibl.ai Platform](https://img.shields.io/badge/ibl.ai_Platform-4A90D9?logoColor=white)](https://ibl.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

This directory is a complete, drop-in OpenClaw configuration for the **Financial Services** solution segment. It contains one parent orchestrator agent and twelve specialist subagents covering the full range of a financial services firm's operational and compliance needs.

## Architecture

The **Advisory Assistant** (`financial-services-assistant`) is the default entry point. It greets staff, interprets intent, and delegates to the appropriate specialist subagent via `sessions_spawn`. Subagents are domain experts that return structured results to the Advisory Assistant for synthesis.

```
financial-services-assistant  (parent, default)
├── compliance-agent
├── risk-assessment-agent
├── client-advisory-agent
├── regulatory-reporting-agent
├── portfolio-analysis-agent
├── employee-training-agent
├── kyc-aml-agent
├── fraud-detection-agent
├── client-onboarding-agent
├── knowledge-agent
├── it-help-desk-agent
└── operations-agent
```

## Agent Roster

| Agent ID | Name | Role |
|---|---|---|
| `financial-services-assistant` | Advisory Assistant | Segment-level entry point; orchestrates all subagents |
| `compliance-agent` | Compliance Monitor | SEC, FINRA, and SOX rule monitoring and exam readiness |
| `risk-assessment-agent` | Risk Analyst | Portfolio risk quantification, stress testing, counterparty exposure |
| `client-advisory-agent` | Client Advisor | Investment research synthesis and suitability review |
| `regulatory-reporting-agent` | Regulatory Reporter | Automated filing preparation and audit trail maintenance |
| `portfolio-analysis-agent` | Portfolio Analyst | Performance attribution and benchmark comparison |
| `employee-training-agent` | Training Coordinator | FINRA CE tracking, compliance certification, and onboarding |
| `kyc-aml-agent` | KYC/AML Specialist | Customer due diligence, sanctions screening, and AML alert triage |
| `fraud-detection-agent` | Fraud Investigator | Transaction monitoring, fraud case investigation, SAR escalation |
| `client-onboarding-agent` | Onboarding Specialist | Account opening, suitability assessment, FATCA/CRS |
| `knowledge-agent` | Knowledge Librarian | Policy search, procedure retrieval, institutional memory |
| `it-help-desk-agent` | IT Help Desk | Technical support, access provisioning, security incident triage |
| `operations-agent` | Operations Specialist | Trade settlement, reconciliation exceptions, corporate actions |

## OpenClaw Import Instructions

### Prerequisites

- A running OpenClaw/NemoClaw instance with the OpenClaw gateway configured.
- The sandbox user has write access to `/sandbox/.openclaw/`.
- You have valid Anthropic API credentials to replace the sample placeholders.

### Steps

**1. Copy the configuration into the sandbox.**

```bash
git clone https://github.com/iblai/financial-services-agents.git
cp -r financial-services-agents/. /sandbox/.openclaw/
```

**2. Verify directory ownership.**

All files under `/sandbox/.openclaw/agents/` must be owned by the sandbox user:

```bash
chown -R sandbox:sandbox /sandbox/.openclaw/agents/
```

**3. Set third-party platform credentials.**

Copy the sample env template to the OpenClaw daemon env file and fill in real API keys for every platform your deployment uses:

```bash
cp /sandbox/.openclaw/.env.example ~/.openclaw/.env
vi ~/.openclaw/.env
```

The OpenClaw daemon reads credentials from `~/.openclaw/.env` at startup. The `.env.example` file documents all required variables grouped by skill.

**4. Replace Anthropic inference credentials.**

Every `agents/<agent-id>/agent/auth-profiles.json` contains a non-functional placeholder API key. Replace the `apiKey` value in each file with a real Anthropic API key (or the appropriate credential for your inference routing setup) before starting the gateway:

```bash
# Example — repeat for all 13 agent directories
vi /sandbox/.openclaw/agents/financial-services-assistant/agent/auth-profiles.json
```

**5. Recompute the config hash.**

After any edit to `openclaw.json`, regenerate `.config-hash`:

```bash
cd /sandbox/.openclaw && shasum -a 256 openclaw.json > .config-hash
```

**6. Reload the OpenClaw gateway.**

```bash
openclaw reload
# or
systemctl restart openclaw
```

The `financial-services-assistant` agent is declared as `"default": true` in `openclaw.json` and will be the entry point for all new sessions.

## File Layout

```
financial-services/
├── README.md
├── openclaw.json               — agent registry and runtime defaults
├── .config-hash                — sha256 of openclaw.json
├── .env.example                — sample OpenClaw daemon env file (copy to ~/.openclaw/.env and fill in real keys)
├── skills/                     — tool skill definitions for third-party platform integrations
│   └── <tool>/
│       └── SKILL.md            — skill definition with frontmatter (name, description, metadata)
├── workspace/
│   └── .gitkeep                — shared writable workspace (mounted at /sandbox/.openclaw/workspace/)
└── agents/
    └── <agent-id>/
        └── agent/
            ├── auth-profiles.json    — credentials (replace before deploying)
            ├── IDENTITY.md           — agent name, role, and vibe
            ├── SOUL.md               — behavioral guidelines and boundaries
            ├── TOOLS.md              — available integrations, platforms, and data sources
            ├── AGENTS.md             — subagent routing map (parent only)
            ├── USER.md               — (optional) user/environment-specific context
            ├── BOOTSTRAP.md          — (optional) one-time first-run setup steps; consumed after initial deployment
            ├── HEARTBEAT.md          — (optional) periodic awareness checklist for agents that monitor on a schedule
            └── MEMORY.md             — (optional) seed long-term facts for regulation-heavy or knowledge-intensive agents
```

## Tool Skills

The `skills/` directory contains one subdirectory per third-party platform, each with a `SKILL.md` file. Each skill describes the platform, its relevant capabilities, the exact API operations agents may call, and declares the required env vars in its `metadata` frontmatter key. Agents reference these skills at runtime to know how to interact with external systems.

All skills draw credentials from `~/.openclaw/.env` on the OpenClaw host. The committed `.env.example` is the sample template — it contains non-functional placeholder values only and is safe to check in. Copy it to `~/.openclaw/.env` and fill in real keys before deploying.

| Skill directory | Description |
|---|---|
| `blackrock-aladdin/` | BlackRock Aladdin risk and portfolio management platform; lets an agent query VaR, factor exposures, stress test scenarios, risk limit utilization, and performance attribution across multi-asset portfolios. |
| `bloomberg-terminal/` | Bloomberg's financial data platform; lets an agent fetch real-time and historical price data, volatility surfaces, rates curves, credit spreads, and sell-side research via the Bloomberg API. |
| `docusign/` | DocuSign electronic signature platform; lets an agent send, track, and retrieve signed documents for client onboarding agreements, advisory contracts, and regulatory disclosures. |
| `factset/` | FactSet financial data and research platform; lets an agent retrieve equity fundamentals, earnings estimates, sell-side research, sector classifications, and benchmark data for investment analysis and reporting. |
| `lexisnexis-worldcompliance/` | LexisNexis WorldCompliance screening platform; lets an agent screen individuals and entities against OFAC SDN, PEP databases, global sanctions lists, and adverse media with confidence-scored match results. |
| `morningstar-direct/` | Morningstar Direct investment research and data platform; lets an agent retrieve fund ratings, ESG scores, performance data, peer universe comparisons, and holdings for advisor due diligence and portfolio construction. |
| `nice-actimize/` | NICE Actimize financial crime platform; lets an agent retrieve fraud and AML transaction monitoring alerts, update dispositions, and route SAR candidates to the BSA Officer. |
| `salesforce-financial-services-cloud/` | Salesforce CRM for financial advisors and wealth management firms; lets an agent read and write client profiles, household data, suitability records, and onboarding workflow state. |
| `servicenow/` | ServiceNow IT service management platform; lets an agent create, update, route, and close IT incidents and fraud investigation cases, track SLA compliance, and retrieve asset and configuration records. |
| `splunk/` | Splunk SIEM platform; lets an agent query authentication logs, endpoint events, and network activity to investigate security incidents, correlate fraud signals, and support threat hunting. |
| `workiva/` | Workiva (Wdesk) financial reporting and compliance platform; lets an agent draft SEC filings, manage XBRL tagging, track reviewer sign-offs, and retrieve SOX workpaper data. |

## Important Notes

- **No investment advice**: All agents are configured to support licensed advisors and compliance officers — they do not independently provide individualized financial advice to end clients.
- **Audit trails**: Every agent is configured to log key actions to `/sandbox/.openclaw/workspace/` for examination readiness.
- **Human escalation**: Each agent's SOUL.md includes explicit escalation rules for situations requiring a human supervisor, CCO, BSA Officer, or CISO.
- **Credentials**: The `auth-profiles.json` files contain sample placeholders only. They are clearly marked and must be replaced before any production use.

---

## License

Released under the [MIT License](LICENSE).
