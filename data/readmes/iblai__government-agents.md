<div align="center">

<a href="https://ibl.ai"><img src="https://ibl.ai/images/iblai-logo.png" alt="ibl.ai" width="300"></a>

# Government Agents

Drop-in [OpenClaw](https://github.com/iblai/iblai-claw-setup) / [NemoClaw](https://github.com/NVIDIA/NemoClaw) agent configuration for the [ibl.ai](https://ibl.ai) **Government** solution segment — one Agency Assistant orchestrator plus 12 specialist subagents, packaged so a NemoClaw host can import the whole roster with zero conversion.

[![OpenClaw](https://img.shields.io/badge/OpenClaw-292929?logoColor=white)](https://github.com/iblai/iblai-claw-setup)
[![NemoClaw](https://img.shields.io/badge/NemoClaw-76B900?logo=nvidia&logoColor=white)](https://github.com/NVIDIA/NemoClaw)
[![ibl.ai Platform](https://img.shields.io/badge/ibl.ai_Platform-4A90D9?logoColor=white)](https://ibl.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

This directory is a complete, drop-in NemoClaw/OpenClaw configuration for the **Government** solution segment. It contains one parent agent and twelve specialist subagents covering the full operational surface of a government agency.

## Directory Layout

```
government/
├── agents/                        # One subdirectory per agent
│   ├── government-assistant/
│   │   └── agent/
│   │       ├── IDENTITY.md
│   │       ├── SOUL.md
│   │       ├── TOOLS.md
│   │       ├── AGENTS.md
│   │       └── auth-profiles.json
│   ├── citizen-services-agent/
│   └── ...                        # (all 13 agents)
│       └── agent/
│           ├── IDENTITY.md
│           ├── SOUL.md
│           ├── TOOLS.md           # Tool integrations + data sources
│           ├── USER.md            # (optional) user/environment context
│           ├── AGENTS.md          # (parent agent only)
│           ├── HEARTBEAT.md       # (optional) periodic monitoring checklist
│           ├── BOOTSTRAP.md       # (optional) one-time first-run setup
│           ├── MEMORY.md          # (optional) seed long-term facts
│           └── auth-profiles.json
├── workspace/                     # Shared inter-agent coordination space
├── skills/                        # Tool-skill definitions for third-party platforms
│   ├── congress-gov/
│   │   └── SKILL.md
│   ├── cornerstone-ondemand/
│   │   └── SKILL.md
│   ├── federal-register/
│   │   └── SKILL.md
│   ├── granicus-govdelivery/
│   │   └── SKILL.md
│   ├── microsoft-entra-id/
│   │   └── SKILL.md
│   ├── salesforce-government-cloud/
│   │   └── SKILL.md
│   ├── sam-gov/
│   │   └── SKILL.md
│   ├── servicenow/
│   │   └── SKILL.md
│   ├── usaspending/
│   │   └── SKILL.md
│   └── workday-government/
│       └── SKILL.md
├── .env.example                   # Sample credentials template (non-functional placeholders)
├── openclaw.json                  # Gateway configuration and agent registry
└── .config-hash                   # SHA-256 of openclaw.json, validated at startup
```

## Agent Roster

| Agent ID | Name | Role |
|---|---|---|
| `government-assistant` | Agency Assistant | **PARENT** — entry point; routes to all subagents |
| `citizen-services-agent` | Citizen Services | Public inquiries, permits, case support |
| `knowledge-agent` | Policy & Knowledge | Policy, SOP, and procedure retrieval |
| `it-help-desk-agent` | IT Help Desk | Technical support and system access |
| `employee-training-agent` | Employee Training | Workforce development and upskilling |
| `compliance-agent` | Compliance & Audit | Regulatory reporting and audit readiness |
| `legislative-agent` | Legislative Affairs | Bill tracking and policy analysis |
| `budget-agent` | Budget & Finance | Spending tracking and financial management |
| `hr-agent` | Human Resources | Personnel administration and benefits |
| `procurement-agent` | Procurement | Vendor management and purchasing guidance |
| `onboarding-agent` | Employee Onboarding | New employee orientation |
| `constituent-communication-agent` | Constituent Communications | Public outreach and updates |
| `security-agent` | Security & Access | Security training and access management |

The `government-assistant` is the default entry point (`"default": true` in `openclaw.json`). It interprets intent and delegates to the appropriate subagent via the `sessions_spawn` tool, then synthesizes results for the user.

## Import Instructions

1. **Copy** the contents of this directory into `/sandbox/.openclaw/` on the NemoClaw sandbox host:

   ```sh
   git clone https://github.com/iblai/government-agents.git
cp -r government-agents/. /sandbox/.openclaw/
   cp government/.env.example /sandbox/.openclaw/
   ```

2. **Set ownership** so the sandbox user can read all files:

   ```sh
   chown -R sandbox:sandbox /sandbox/.openclaw/agents/
   chown -R sandbox:sandbox /sandbox/.openclaw/workspace/
   ```

3. **Set up tool-skill credentials** by copying the sample env file and filling in real API keys:

   ```sh
   cp /sandbox/.openclaw/.env.example ~/.openclaw/.env
   # Edit ~/.openclaw/.env and replace every SAMPLE-* placeholder with a live value
   ```

4. **Replace sample credentials** in every `auth-profiles.json`. Each file under `agents/<agent-id>/agent/auth-profiles.json` contains a placeholder API key marked `SAMPLE CREDENTIALS ONLY`. Replace the `apiKey` value with a valid Anthropic API key (or your configured credential) before starting the gateway:

   ```sh
   # Example — replace with your actual key management approach
   find /sandbox/.openclaw/agents -name auth-profiles.json | xargs sed -i \
     's/sk-ant-api03-SAMPLE-PLACEHOLDER-NOT-A-REAL-KEY-0000000000000000000000000000000000000000/<YOUR_KEY>/g'
   ```

5. **Recompute the config hash** after any edits to `openclaw.json`:

   ```sh
   cd /sandbox/.openclaw
   shasum -a 256 openclaw.json > .config-hash
   ```

6. **Reload the OpenClaw gateway**:

   ```sh
   openclaw reload
   # or restart the service
   systemctl restart openclaw
   ```

## Tool Skills

The `skills/` directory contains one subdirectory per third-party platform, each containing a `SKILL.md` file. Each skill describes the platform's purpose, the operations agents can perform against it, required credentials, and usage notes. OpenClaw injects the relevant skill files into an agent's context so agents know how to call external APIs without hard-coding that knowledge in individual workspace files.

All skills draw their credentials from the OpenClaw daemon env file `~/.openclaw/.env`. The committed file `.env.example` is a sample template with non-functional placeholder values — copy it to `~/.openclaw/.env` and fill in real API keys before deploying (see step 3 of Import Instructions).

| Skill | Description |
|---|---|
| `congress-gov` | Official U.S. Congress legislative data API; lets agents search bills, retrieve full text and status, track co-sponsors, committee referrals, and floor votes. |
| `cornerstone-ondemand` | FedRAMP-authorized Learning Management System; lets agents check employee training transcripts, mandatory compliance status, course catalog, and enroll users in required training. |
| `federal-register` | Official U.S. rulemaking and regulatory publication API; lets agents search and retrieve federal rules, proposed rules, notices, and executive orders with full text and comment period data. |
| `granicus-govdelivery` | Government digital communications platform; lets agents draft, schedule, and send subscriber email/SMS bulletins and retrieve delivery analytics. |
| `microsoft-entra-id` | Cloud identity platform for government (Microsoft 365 GCC/GCC High); lets agents look up user accounts, check MFA and compliance status, and initiate supervised access provisioning workflows. |
| `salesforce-government-cloud` | FedRAMP High CRM platform for government; lets agents create, read, and update citizen service cases, constituent records, and SLA compliance data. |
| `sam-gov` | Official U.S. government vendor and contract opportunities registry; lets agents verify vendor registrations, check exclusions, and search contract opportunities. |
| `servicenow` | FedRAMP-authorized ITSM platform; lets agents create/update incidents, service requests, change records, onboarding tasks, and security incidents, and search the knowledge base. |
| `usaspending` | Public federal spending transparency API; lets agents retrieve award history, obligation data, and vendor spend benchmarks for budget and procurement research. |
| `workday-government` | Cloud HRIS and payroll platform for government; lets agents retrieve employee position data, personnel actions, leave balances, pay information, and performance plan status. |

## Notes

- The sandbox writable workspace is `/sandbox/.openclaw/workspace/`. All agents share this path for inter-agent coordination files.
- The `.config-hash` file in this directory was computed at build time. Recompute it whenever `openclaw.json` changes.
- Agent workspace files read by the OpenClaw runtime are: IDENTITY.md, SOUL.md, USER.md, TOOLS.md, AGENTS.md, HEARTBEAT.md, BOOTSTRAP.md, MEMORY.md, and the `skills/` directory. These are injected into each agent's context at runtime.
- Optional workspace files are added only where warranted: USER.md (user/environment-specific context), BOOTSTRAP.md (one-time first-run setup, consumed after initial session), HEARTBEAT.md (periodic monitoring checklist for agents that run on a schedule), and MEMORY.md (seed long-term facts for regulation- or policy-heavy agents). Do not create these files as filler — only add them when the agent genuinely needs them.
- `.env.example` is committed to the repository as a reference template. `~/.openclaw/.env` (with real keys) must never be committed; add it to `.gitignore`.

---

## License

Released under the [MIT License](LICENSE).
