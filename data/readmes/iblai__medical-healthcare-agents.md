<div align="center">

<a href="https://ibl.ai"><img src="https://ibl.ai/images/iblai-logo.png" alt="ibl.ai" width="300"></a>

# Medical & Healthcare Agents

Drop-in [OpenClaw](https://github.com/iblai/iblai-claw-setup) / [NemoClaw](https://github.com/NVIDIA/NemoClaw) agent configuration for the [ibl.ai](https://ibl.ai) **Medical & Healthcare** solution segment — one Care Assistant orchestrator plus 12 specialist subagents, packaged so a NemoClaw host can import the whole roster with zero conversion.

[![OpenClaw](https://img.shields.io/badge/OpenClaw-292929?logoColor=white)](https://github.com/iblai/iblai-claw-setup)
[![NemoClaw](https://img.shields.io/badge/NemoClaw-76B900?logo=nvidia&logoColor=white)](https://github.com/NVIDIA/NemoClaw)
[![ibl.ai Platform](https://img.shields.io/badge/ibl.ai_Platform-4A90D9?logoColor=white)](https://ibl.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

This directory contains the complete NemoClaw/OpenClaw configuration for the **Medical / Healthcare** solution segment. It is designed as a drop-in configuration: copy the contents of this directory into `/sandbox/.openclaw/` on a NemoClaw sandbox, replace credentials, recompute the hash, and the segment is live.

The segment consists of **1 parent agent** and **12 specialist subagents** (13 agents total). All PHI handling follows HIPAA minimum necessary standards. All clinical agents include explicit disclaimers that AI output supports but does not replace licensed clinician judgment.

---

## Agent Roster

| Agent ID | Name | Role |
|---|---|---|
| `medical-healthcare-assistant` | Care Assistant | **PARENT** — entry point; interprets intent and delegates to specialist subagents via `sessions_spawn` |
| `clinical-support-agent` | Clinical Support | Evidence-based protocol recommendations and clinical decision support |
| `patient-education-agent` | Patient Education | Condition explanations and discharge instruction drafting |
| `medical-coding-agent` | Medical Coding | ICD-10-CM/PCS and CPT code selection assistance |
| `compliance-training-agent` | Compliance Training | HIPAA training delivery and certification tracking |
| `research-agent` | Research | Literature review and clinical trial matching |
| `provider-onboarding-agent` | Provider Onboarding | Credentialing, privileging, and new provider orientation |
| `prior-authorization-agent` | Prior Authorization | Insurance PA requests, status tracking, and denial appeals |
| `care-coordination-agent` | Care Coordination | Referral management, care transitions, and follow-up scheduling |
| `documentation-agent` | Documentation | Clinical note drafting assistance and CDI quality review |
| `quality-improvement-agent` | Quality Improvement | HEDIS/CAHPS metrics, care gap analysis, and accreditation readiness |
| `it-help-desk-agent` | IT Help Desk | EHR support, system access, and IT ticket management |
| `knowledge-management-agent` | Knowledge Management | Clinical protocol search, formulary guidance, and policy retrieval |

---

## Import Instructions

Follow these steps to deploy this configuration onto a NemoClaw sandbox.

**1. Copy directory contents**

```bash
git clone https://github.com/iblai/medical-healthcare-agents.git
cp -r medical-healthcare-agents/. /sandbox/.openclaw/
```

This copies `openclaw.json`, `.config-hash`, `workspace/`, `skills/`, `.env.example`, and the entire `agents/` tree into the sandbox root.

**2. Set ownership**

Ensure the sandbox user owns all agent directories:

```bash
chown -R sandbox:sandbox /sandbox/.openclaw/agents/
chown -R sandbox:sandbox /sandbox/.openclaw/workspace/
```

**3. Set up third-party platform credentials**

Copy the included sample env file and fill in real API keys for every platform the segment connects to:

```bash
cp /sandbox/.openclaw/.env.example ~/.openclaw/.env
vi ~/.openclaw/.env
```

`.env.example` is the committed sample template representing the OpenClaw daemon env file `~/.openclaw/.env`; all values in it are non-functional placeholders. The live `~/.openclaw/.env` file (never committed) is sourced by the OpenClaw gateway at startup and injected into each agent's sandbox environment. See [Tool Skills](#tool-skills) below for the full list of platforms and the variables each one requires.

**4. Replace sample LLM credentials**

Every agent directory contains `agents/<agent-id>/agent/auth-profiles.json` with a clearly marked sample key. Replace the `apiKey` value with a real Anthropic API key (and any other provider credentials your deployment requires) before going live:

```bash
# Example — repeat for each agent directory
vi /sandbox/.openclaw/agents/medical-healthcare-assistant/agent/auth-profiles.json
```

The file structure is:
```json
{
  "profiles": {
    "anthropic": {
      "provider": "anthropic",
      "apiKey": "<YOUR-REAL-KEY-HERE>"
    }
  }
}
```

**5. Recompute the config hash**

After any modification to `openclaw.json` (required if you edit the file at all), recompute the hash from inside the openclaw root directory:

```bash
cd /sandbox/.openclaw
sha256sum openclaw.json > .config-hash
```

On macOS:
```bash
cd /sandbox/.openclaw
shasum -a 256 openclaw.json > .config-hash
```

**6. Reload the OpenClaw gateway**

```bash
openclaw reload
# or, if running as a systemd service:
systemctl reload openclaw-gateway
```

---

## Tool Skills

The `skills/` directory contains one subdirectory per third-party platform, each with a `SKILL.md` file. Each skill describes what the platform is, how agents authenticate to it, and which operations are available — giving every agent in the segment the context it needs to invoke that platform correctly. All skills draw their runtime credentials from `~/.openclaw/.env` (`.env.example` is the committed sample template containing non-functional placeholder values; copy it to `~/.openclaw/.env` and fill in real API keys before deploying).

| Skill directory | Description |
|---|---|
| `availity/SKILL.md` | Availity Essentials — lets an agent perform real-time eligibility verification, prior authorization initiation and status checks, and payer enrollment management via the Availity clearinghouse REST API. |
| `cerner-fhir/SKILL.md` | Cerner Millennium FHIR R4 API — lets an agent read patient clinical data (demographics, encounters, diagnoses, medications, notes) within a Cerner-hosted health system. |
| `epic-fhir/SKILL.md` | Epic EHR FHIR R4 API — lets an agent read and write patient clinical data (demographics, encounters, diagnoses, medications, notes, orders) within an Epic-hosted health system. |
| `healthstream/SKILL.md` | HealthStream LMS — lets an agent query employee training transcripts, assign compliance curricula, check credential expiration alerts, and pull completion reports from the HealthStream learning management system. |
| `innovaccer/SKILL.md` | Innovaccer — lets an agent query population health analytics, patient risk scores, care gap lists, and SDOH screening data from the Innovaccer unified patient data platform. |
| `micromedex/SKILL.md` | Micromedex (Merative/IBM) — lets an agent perform drug interaction screening, dose range checking, toxicology lookups, and IV compatibility queries using the Micromedex drug knowledge base. |
| `nuance-dax/SKILL.md` | Nuance DAX (Dragon Ambient eXperience) — lets an agent submit encounter audio or transcripts and retrieve AI-generated structured clinical note drafts for clinician review. |
| `pubmed/SKILL.md` | PubMed / NCBI E-utilities — lets an agent search MEDLINE biomedical literature, retrieve structured abstracts, and export citations for clinical research and evidence synthesis tasks. |
| `servicenow/SKILL.md` | ServiceNow (Healthcare IT) — lets an agent create, update, and query IT service management tickets, knowledge articles, and configuration items within a ServiceNow instance deployed in a health system. |
| `uptodate/SKILL.md` | UpToDate (Wolters Kluwer) — lets an agent query evidence-based clinical decision support content including treatment recommendations, drug monographs, and clinical practice guidelines. |

---

## Agent Directory Layout

Each agent lives at `agents/<agent-id>/agent/` and may contain the following files:

```
agents/<agent-id>/agent/
├── IDENTITY.md          # Agent persona: Name, Role, Vibe
├── SOUL.md              # Behavioral guidelines and boundaries
├── TOOLS.md             # Available integrations, tool usage notes, and data sources
├── auth-profiles.json   # LLM provider credentials (replace before deploy)
├── AGENTS.md            # Sub-agent delegation map (parent agent only)
├── MEMORY.md            # (optional) Seed long-term facts for rule/code-heavy agents
├── BOOTSTRAP.md         # (optional) One-time first-run setup steps; consumed after first use
├── HEARTBEAT.md         # (optional) Periodic monitoring checklist for proactive-watch agents
└── USER.md              # (optional) User/environment-specific context when genuinely needed
```

`MEMORY.md`, `BOOTSTRAP.md`, `HEARTBEAT.md`, and `USER.md` are only present for agents where they are genuinely warranted. Agents without proactive monitoring duties, seed knowledge requirements, or first-run setup do not include these files. Model selection and instance settings (heartbeat schedule, session scope) are configured in `openclaw.json` — not in per-agent files.

---

## Architecture Notes

- The parent agent (`medical-healthcare-assistant`) is marked `"default": true` in `openclaw.json` and is the entry point for all incoming sessions.
- The parent delegates to specialist subagents via the `sessions_spawn` tool; it does not perform deep clinical, coding, or compliance work itself.
- Concurrent spawning is enabled (`maxConcurrent: 8`) to support multi-domain requests (e.g., simultaneous referral and PA initiation).
- All agents share a common writable workspace at `/sandbox/.openclaw/workspace/` for inter-agent artifact passing.
- `maxSpawnDepth: 2` prevents subagents from spawning further subagents, keeping the delegation hierarchy flat and auditable.

---

## License

Released under the [MIT License](LICENSE).
