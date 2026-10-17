<div align="center">

<a href="https://ibl.ai"><img src="https://ibl.ai/images/iblai-logo.png" alt="ibl.ai" width="300"></a>

# Enterprise Agents

Drop-in [OpenClaw](https://github.com/iblai/iblai-claw-setup) / [NemoClaw](https://github.com/NVIDIA/NemoClaw) agent configuration for the [ibl.ai](https://ibl.ai) **Enterprise** solution segment — one Workplace Assistant orchestrator plus 12 specialist subagents, packaged so a NemoClaw host can import the whole roster with zero conversion.

[![OpenClaw](https://img.shields.io/badge/OpenClaw-292929?logoColor=white)](https://github.com/iblai/iblai-claw-setup)
[![NemoClaw](https://img.shields.io/badge/NemoClaw-76B900?logo=nvidia&logoColor=white)](https://github.com/NVIDIA/NemoClaw)
[![ibl.ai Platform](https://img.shields.io/badge/ibl.ai_Platform-4A90D9?logoColor=white)](https://ibl.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

This directory is a complete, drop-in OpenClaw/NemoClaw configuration for the **Enterprise** solution segment. It contains one parent orchestrator agent and 12 specialist subagents covering every major enterprise workplace function.

Copy the contents of this directory directly into `/sandbox/.openclaw/` on a NemoClaw sandbox host and the configuration is immediately operational.

---

## Agent Roster

| Agent ID | Name | Role |
|---|---|---|
| `enterprise-assistant` *(default)* | Workplace Assistant | Segment entry point — greets employees, interprets intent, and delegates to specialist subagents |
| `knowledge-agent` | Knowledge Search | Enterprise search across internal wikis, documentation, and knowledge repositories |
| `it-help-desk-agent` | IT Support | Issue resolution, password resets, software access provisioning, and ticket management |
| `sales-enablement-agent` | Sales Navigator | Competitive briefs, deal strategy, prospect research, and outreach templates |
| `customer-support-agent` | Customer Support | Ticket resolution, customer account management, escalations, and follow-up communications |
| `onboarding-agent` | Onboarding Guide | New hire orientation, ramp-up planning, system access setup, and first-week navigation |
| `hr-agent` | HR Assistant | Policy Q&A, benefits guidance, leave management, and people operations support |
| `marketing-agent` | Marketing Strategist | Content creation, campaign planning, SEO guidance, and brand-aligned collateral |
| `engineering-agent` | Engineering Advisor | Code review, technical documentation, architecture guidance, and project onboarding |
| `meeting-agent` | Meeting Scribe | Meeting recaps, action item extraction, follow-up drafts, and calendar coordination |
| `training-agent` | Learning Coach | Employee development paths, compliance training deadlines, and course recommendations |
| `data-analysis-agent` | Data Analyst | Business reports, trend analysis, dashboard interpretation, and ad-hoc queries |
| `operations-agent` | Ops Optimizer | Workflow automation, process bottleneck identification, vendor management, and SLA tracking |

---

## Directory Layout

```
enterprise/
├── agents/                        # One directory per agent (13 total)
│   ├── enterprise-assistant/      # Default entry-point orchestrator
│   └── <subagent-id>/             # 12 specialist subagents
│       └── agent/
│           ├── IDENTITY.md        # Required: agent persona (name, role, vibe)
│           ├── SOUL.md            # Required: behavioral guidelines
│           ├── TOOLS.md           # Required: available integrations, usage notes, and data sources
│           ├── auth-profiles.json # Required: Anthropic API key for this agent
│           ├── AGENTS.md          # Optional: subagent routing table (parent only)
│           ├── USER.md            # Optional: user/environment-specific context (rare)
│           ├── BOOTSTRAP.md       # Optional: one-time first-run setup actions
│           ├── HEARTBEAT.md       # Optional: periodic monitoring checklist (schedule-driven agents)
│           └── MEMORY.md          # Optional: seed long-term facts (policy/regulation-heavy agents)
├── skills/                        # Third-party platform skill definitions
│   └── <tool>/
│       └── SKILL.md               # Skill definition with frontmatter and body
├── workspace/                     # Shared workspace files
├── openclaw.json                  # Segment-level gateway configuration
├── .env.example                   # Sample OpenClaw daemon env file (~/.openclaw/.env)
└── README.md
```

---

## Architecture

```
enterprise-assistant (default, entry point)
├── knowledge-agent
├── it-help-desk-agent
├── sales-enablement-agent
├── customer-support-agent
├── onboarding-agent
├── hr-agent
├── marketing-agent
├── engineering-agent
├── meeting-agent
├── training-agent
├── data-analysis-agent
└── operations-agent
```

The parent agent (`enterprise-assistant`) receives all incoming employee messages. It interprets intent using its `AGENTS.md` routing table and delegates to the appropriate specialist via `sessions_spawn`. For requests that span multiple domains (e.g., "set up access for my new hire and send them an onboarding checklist"), it spawns multiple subagents in parallel and synthesizes the results into a single response.

---

## Tool Skills

Each skill in `skills/` is a directory containing a `SKILL.md` file that describes a third-party platform one or more agents in this segment can integrate with — what the platform is, how agents use it, the API operations available, credential requirements, and scope or permission notes. Agents reference the relevant skill documents in their `TOOLS.md` to understand how to interact with each system.

All skills draw their runtime credentials from the OpenClaw daemon env file at `~/.openclaw/.env` on the sandbox host. The `.env.example` file checked into this repository is the committed sample template; every value in it is a non-functional placeholder. Copy it to `~/.openclaw/.env` and fill in real API keys before deploying (see import instructions below).

| Skill directory | Platform description |
|---|---|
| `confluence/` | Confluence team wiki and documentation platform - lets an agent search, read, and create pages across internal knowledge bases, runbooks, technical documentation, and policy spaces. |
| `github/` | GitHub source control and collaboration platform - lets an agent read pull requests, commits, repository metadata, and CI workflow results to support engineering review and documentation. |
| `hubspot/` | HubSpot CRM and Marketing Hub - lets an agent read and update deals, contacts, companies, marketing campaigns, and workflow enrollments across the inbound sales and marketing lifecycle. |
| `jira/` | Jira project and issue tracking - lets an agent create, query, update, and link issues, sprints, and epics across engineering, IT, and operations projects. |
| `okta/` | Okta workforce identity platform - lets an agent verify employee identity, look up user profiles and group memberships, check MFA enrollment status, and support access provisioning workflows. |
| `salesforce/` | Salesforce CRM and Sales Cloud - lets an agent read and write opportunities, accounts, contacts, cases, and activities across the enterprise revenue and support lifecycle. |
| `servicenow/` | ServiceNow ITSM and enterprise service management - lets an agent create, read, update, and route incidents, service requests, HR cases, change records, and knowledge articles. |
| `slack/` | Slack team messaging platform - lets an agent post messages, send direct messages, read channel history, and deliver notifications into employee workflows. |
| `snowflake/` | Snowflake cloud data warehouse - lets an agent execute read-only SQL queries, explore table and schema metadata, and retrieve business intelligence results for reporting and analysis. |
| `workday/` | Workday HCM - lets an agent retrieve employee records, leave balances, onboarding task status, job history, and compensation data in read-only mode to support HR and onboarding workflows. |
| `zendesk/` | Zendesk customer service platform - lets an agent create, read, update, and search support tickets, manage user records, apply macros, and retrieve CSAT survey results. |
| `zoom/` | Zoom video conferencing platform - lets an agent retrieve meeting metadata, participant lists, cloud recording URLs, and auto-generated transcripts to support meeting intelligence workflows. |

---

## NemoClaw Import Instructions

Follow these steps to deploy this configuration on a NemoClaw sandbox host.

**1. Copy the directory contents into the sandbox root.**

```bash
git clone https://github.com/iblai/enterprise-agents.git
cp -r enterprise-agents/. /sandbox/.openclaw/
```

All files must land at `/sandbox/.openclaw/` — not inside a subdirectory of it.

**2. Set correct ownership on agent directories.**

```bash
chown -R sandbox:sandbox /sandbox/.openclaw/agents/
chown -R sandbox:sandbox /sandbox/.openclaw/workspace/
```

**3. Replace the sample credentials in every `auth-profiles.json`.**

Each agent directory contains `/sandbox/.openclaw/agents/<agent-id>/agent/auth-profiles.json` with a clearly marked sample placeholder key. Replace the `apiKey` value with a valid Anthropic API key before starting the gateway.

```bash
# Example: update in place for one agent
vi /sandbox/.openclaw/agents/enterprise-assistant/agent/auth-profiles.json
```

Repeat for all 13 agent directories.

**4. Set up third-party integration credentials.**

Copy the sample env file to `~/.openclaw/.env` on the sandbox host and replace every placeholder value with real API keys for the platforms your deployment uses.

```bash
cp /sandbox/.openclaw/.env.example ~/.openclaw/.env
vi ~/.openclaw/.env
```

The file contains sections for all 12 supported platforms (Salesforce, ServiceNow, Slack, Jira, GitHub, Okta, Snowflake, Workday, Zendesk, Confluence, HubSpot, and Zoom). Remove or leave blank any sections for platforms you are not connecting.

**5. Recompute the configuration hash.**

```bash
cd /sandbox/.openclaw
shasum -a 256 openclaw.json > .config-hash
```

The gateway will refuse to start if the hash does not match `openclaw.json`.

**6. Reload the OpenClaw gateway.**

```bash
openclaw gateway reload
# or, for a full restart:
systemctl restart openclaw-gateway
```

**7. Verify the default agent is active.**

```bash
openclaw agent list
```

The `enterprise-assistant` entry should show `default: true` and status `ready`.

---

## Customization

- **Adding integrations**: Edit the relevant subagent's `TOOLS.md` to add new platforms and data sources. Add a corresponding skill directory under `skills/<tool>/SKILL.md`.
- **Adjusting routing**: Edit `enterprise-assistant/agent/AGENTS.md` to change delegation logic.
- **Model selection**: Edit `openclaw.json` to change the model for any agent. The parent and all subagents default to `anthropic/claude-sonnet-4-5-20250929`.
- **New subagents**: Add a new agent directory, register it in `openclaw.json`, add its ID to the parent's `subagents.allowAgents` array, recompute `.config-hash`, and reload the gateway.

---

## License

Released under the [MIT License](LICENSE).
