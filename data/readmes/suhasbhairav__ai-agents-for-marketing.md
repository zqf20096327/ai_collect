# MarketingOS AI

> Agentic marketing workspace for HubSpot CRM: discover revenue opportunities, build governed audiences, generate campaign drafts, review brand/compliance risk, and keep every customer-facing action behind human approval.

[![Next.js](https://img.shields.io/badge/Next.js-16-black?style=for-the-badge&logo=nextdotjs)](https://nextjs.org)
[![React](https://img.shields.io/badge/React-19-149ECA?style=for-the-badge&logo=react&logoColor=white)](https://react.dev)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-4-38B2AC?style=for-the-badge&logo=tailwindcss&logoColor=white)](https://tailwindcss.com)
[![Clerk](https://img.shields.io/badge/Auth-Clerk-6C47FF?style=for-the-badge&logo=clerk&logoColor=white)](https://clerk.com)
[![Supabase](https://img.shields.io/badge/Data-Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)](https://supabase.com)
[![OpenAI](https://img.shields.io/badge/Agents-OpenAI-111111?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com)
[![HubSpot](https://img.shields.io/badge/CRM-HubSpot-FF7A59?style=for-the-badge&logo=hubspot&logoColor=white)](https://developers.hubspot.com)
[![JavaScript](https://img.shields.io/badge/JavaScript-only-F7DF1E?style=for-the-badge&logo=javascript&logoColor=111)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

**Created by [Suhas Bhairav](https://suhasbhairav.com).**

## The Short Version

MarketingOS AI is a production-minded AI agents platform for marketing teams that use HubSpot CRM. It is not a static dashboard and it is not a generic ChatGPT wrapper. It combines deterministic CRM analytics, OpenAI agent orchestration, HubSpot data sync architecture, governed audience building, AI campaign drafting, brand intelligence, compliance checks, and approval workflows into one modern marketing operating system.

Think of it as:

`AI marketing strategist` · `CRM opportunity engine` · `HubSpot campaign copilot` · `audience segmentation workspace` · `approval-first campaign builder` · `marketing analytics dashboard`

## Product Screenshots

![MarketingOS AI dashboard and command center](./image1.png)

![MarketingOS AI agent workspace and execution trace](./image2.png)

![MarketingOS AI campaign, audience, and approval workflow](./image3.png)

## Why This Exists

Most marketing AI tools generate copy. Marketing teams need more than copy.

They need an AI system that understands CRM context, knows which contacts and deals matter, explains the evidence behind a recommendation, builds safe audiences, respects opt-outs and suppression lists, follows brand rules, drafts complete campaigns, and never sends anything without human approval.

MarketingOS AI is built around that workflow.

## What It Does

### 1. Agentic Marketing Command Center

MarketingOS AI gives marketers a command center for CRM-grounded marketing work:

- View top marketing and revenue opportunities.
- Inspect lifecycle, pipeline, contact, campaign, and CRM health signals.
- Ask a conversational marketing agent what to do next.
- Trigger specialist agents for opportunity analysis, audience creation, campaign strategy, email copy, brand review, compliance, analytics, CRM research, and approvals.
- See a visible run trace for every agent execution.

### 2. HubSpot CRM Opportunity Discovery

The system is designed to synchronize and reason over HubSpot CRM data:

- Contacts
- Companies
- Deals
- Owners
- Pipelines
- Deal stages
- Associations
- Lists where available
- Marketing emails where available
- Campaign records where available
- Forms where available

The opportunity engine is deterministic first. It calculates opportunities using analytics logic before an AI agent interprets the result.

Detected opportunity types include:

- Engaged leads not converting
- MQLs not progressing to SQL
- Stalled high-value deals
- Lost deal re-engagement
- Customer reactivation
- Cross-sell opportunities
- Industry conversion gaps
- Geographic opportunity pockets
- CRM data quality issues
- Campaign optimization opportunities
- Funnel leakage
- High-value segments

### 3. Conversational AI Agent Workspace

The `/agent` page is a real working agent console.

It supports:

- Enter-to-send chat
- Suggested marketing prompts
- API-backed responses
- Agent run IDs
- Run history
- Visible execution traces
- Per-agent status
- Tool call logs
- Guardrail results
- Generated campaign and audience artifacts
- OpenAI Agents SDK execution when `OPENAI_API_KEY` is configured
- Deterministic CRM-grounded fallback when demo mode is enabled

Specialist agents:

| Agent | Purpose |
|---|---|
| MarketingOS orchestrator | Understands intent, creates a task plan, routes specialists, assembles the final answer |
| Opportunity agent | Explains ranked opportunities with metrics, evidence, assumptions, and risks |
| CRM research agent | Retrieves safe CRM summaries and aggregated source references |
| Audience agent | Builds structured audience definitions with mandatory exclusions |
| Campaign strategy agent | Defines objective, audience insight, value proposition, CTA, sequence, and measurement plan |
| Email copy agent | Drafts subject lines, preview text, body, CTA, and plain text |
| SMS copy agent | Generates consent-aware SMS variants |
| Brand review agent | Scores tone, clarity, product accuracy, CTA quality, and prohibited language |
| Compliance agent | Checks consent, suppression, disclaimers, sensitive targeting, and unsubscribe guidance |
| Analytics agent | Explains metrics and separates facts, estimates, and inferences |
| Approval agent | Summarizes approval requirements and records approval-safe events |

### 4. Approval-First Campaign Builder

MarketingOS AI intentionally does not send or publish campaigns automatically.

Campaign states include:

`idea` · `analysing` · `draft` · `awaiting_review` · `changes_requested` · `approved` · `scheduled` · `published` · `rejected` · `archived`

The implemented workflow stops at approval unless explicit publishing integrations are separately built and enabled.

Every approval flow is designed to show:

- What will happen
- Which records are affected
- How many contacts are included
- Which exclusions apply
- Whether HubSpot data changes
- Whether the action is reversible
- Which user approved it

### 5. Governed Audience Builder

The audience system supports safe segmentation across:

- Contact lifecycle stage
- Lead status
- Marketability
- Country, state, city
- Company industry
- Deal stage
- Pipeline status
- Engagement signals
- Custom properties

Mandatory exclusions are enforced:

- Opted-out contacts
- Archived contacts
- Contacts without email for email campaigns
- Suppression lists
- Do-not-contact records
- Workspace exclusion rules

The AI can propose an audience, but it cannot disable legally or technically required exclusions.

### 6. Brand Intelligence

MarketingOS AI stores and applies a brand profile:

- Company description
- Product catalogue
- Product positioning
- Target markets
- Target personas
- Brand personality
- Preferred tone
- Words to use
- Words to avoid
- Required phrases
- Prohibited claims
- Legal disclaimers
- Regional compliance guidance
- CTA preferences
- Email signature
- Default sender identity

Campaign drafts are reviewed against this profile before approval.

### 7. Compliance and Prompt-Injection Guardrails

The agent layer includes centralized prompt-injection and unsafe request detection.

It blocks attempts to:

- Override system or developer instructions
- Reveal system prompts, hidden instructions, chain-of-thought, tool schemas, or internal reasoning
- Extract API keys, service-role keys, tokens, credentials, or environment variables
- Bypass approval, consent, opt-outs, suppression, or unsubscribe rules
- Send, publish, schedule, enroll, or activate campaigns autonomously
- Run arbitrary SQL, code, HTTP requests, webhooks, or tools
- Inject unsafe HTML or JavaScript
- Dump broad CRM data, PII, or contact lists

Blocked prompts stop before CRM tools or OpenAI model calls.

### 8. Analytics Dashboard

The dashboard includes:

- KPI cards
- Contact growth charts
- Lifecycle distribution
- Conversion funnel
- Opportunity feed
- Approval queue
- Campaign list
- Integration health
- Data freshness

Metrics are labeled as real, estimated, inferred, or unavailable where appropriate.

### 9. CRM Explorers

MarketingOS AI includes searchable explorer surfaces for:

- Contacts
- Companies
- Deals
- Campaigns
- Audiences
- Opportunities
- Activity events
- Approvals

Demo mode provides seeded synthetic data so the product can be evaluated without HubSpot credentials.

## Product Principles

### Evidence Before Recommendation

Every recommendation should include:

- Opportunity title
- Opportunity type
- Business problem
- Supporting metrics
- CRM evidence
- Target audience
- Expected impact
- Confidence score
- Assumptions
- Risks
- Recommended action
- Data freshness
- Source references

When data is unavailable, the product should say:

> Insufficient data to calculate this metric.

### Human Approval Is Mandatory

The AI may draft, analyze, recommend, and prepare.

The AI must not autonomously:

- Delete HubSpot records
- Change CRM property definitions
- Send emails
- Enroll contacts into workflows
- Publish campaigns
- Modify consent
- Override suppression lists
- Add excluded contacts
- Export unrestricted personal data
- Reveal secrets
- Run arbitrary code
- Call unapproved external URLs

### Deterministic First, AI Second

The system does not ask an LLM to calculate every metric from raw CRM records.

Instead:

1. SQL and JavaScript analytics calculate metrics.
2. Opportunity detectors identify candidate opportunities.
3. Transparent scoring ranks them.
4. Specialist agents explain and operationalize the results.

## Architecture

```text
app/
  (auth)/                    Clerk login and signup
  (dashboard)/               Protected product workspace
  api/                       Route handlers, one route.js per endpoint

components/
  agent/                     Agent console and run trace UI
  dashboard/                 KPI and chart components
  shared/                    Page headers, tables, badges
  ui/                        Reusable UI primitives

lib/
  agents/                    OpenAI Agents SDK specialists
  analytics/                 Funnel, pipeline, scoring, detectors
  hubspot/                   HubSpot client, pagination, sync
  security/                  HTML and URL safety
  supabase/                  Supabase clients for data storage
  validation/                Environment and input validation

services/
  agent-service.js           Agent orchestration, run history, tool calls
  dashboard-service.js       Dashboard aggregates
  opportunity-service.js     Opportunity generation and retrieval
  audience-service.js        Audience preview and exclusions
  campaign-service.js        Campaign generation and approval state
  crm-service.js             Contact, company, deal access

supabase/
  migrations/                Postgres schema and RLS
  seed.sql                   Demo seed data
```

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | Next.js 16 App Router |
| Language | JavaScript, with `proxy.ts` as the only TypeScript exception required for Next proxy |
| UI | React 19, Tailwind CSS 4, Lucide React, Recharts |
| Auth | Clerk |
| Database | Supabase Postgres |
| Storage | Supabase Storage architecture |
| Agents | OpenAI Agents SDK |
| CRM | HubSpot CRM API |
| Validation | Zod |
| Testing | Vitest |
| Deployment | Vercel-compatible |

## Routes

### Product Pages

- `/` - Product entry
- `/sign-in` - Clerk sign in
- `/sign-up` - Clerk sign up
- `/onboarding` - Workspace and brand setup
- `/dashboard` - Marketing command center
- `/agent` - Conversational multi-agent workspace
- `/opportunities` - Opportunity feed
- `/opportunities/[id]` - Opportunity details
- `/campaigns` - Campaign list
- `/campaigns/new` - Guided campaign creation
- `/campaigns/[id]` - Campaign workspace
- `/campaigns/[id]/review` - Approval and review
- `/audiences` - Saved audiences
- `/audiences/new` - Audience builder
- `/audiences/[id]` - Audience details
- `/analytics` - Marketing analytics
- `/contacts` - CRM contacts
- `/companies` - CRM companies
- `/deals` - CRM deals
- `/integrations` - Integration status
- `/integrations/hubspot` - HubSpot configuration
- `/brand` - Brand intelligence
- `/knowledge` - Products, offers, and guidance
- `/approvals` - Approval queue
- `/activity` - Audit timeline
- `/settings` - Workspace settings
- `/settings/team` - Team and roles
- `/settings/security` - Security and retention

### API Routes

All backend endpoints use `app/api/**/route.js` and return a consistent response envelope.

Key endpoints:

- `/api/agent/chat`
- `/api/agent/conversations`
- `/api/agent/runs/[id]`
- `/api/dashboard/metrics`
- `/api/opportunities`
- `/api/opportunities/generate`
- `/api/audiences/preview`
- `/api/campaigns/[id]/generate`
- `/api/campaigns/[id]/approve`
- `/api/brand/test`
- `/api/integrations/hubspot/status`
- `/api/integrations/hubspot/sync`
- `/api/cron/hubspot-sync`
- `/api/cron/opportunity-scan`

## Demo Mode

Demo mode is enabled by default:

```env
DEMO_MODE=true
```

It provides synthetic data for:

- 500 contacts
- 80 companies
- 100 deals
- Multiple lifecycle stages
- Multiple industries
- Multiple countries
- Stalled deals
- Won and lost deals
- Campaign metrics
- Brand profile
- Products and offers
- Generated opportunities
- Campaign drafts
- Pending approvals

Demo mode never performs real external HubSpot writes.

## Environment Variables

Create `.env` from `.env.example`.

```env
NEXT_PUBLIC_APP_URL=http://localhost:3000

NEXT_PUBLIC_SUPABASE_URL=
NEXT_PUBLIC_SUPABASE_ANON_KEY=
SUPABASE_SERVICE_ROLE_KEY=

NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=
CLERK_SECRET_KEY=
NEXT_PUBLIC_CLERK_SIGN_IN_URL=/sign-in
NEXT_PUBLIC_CLERK_SIGN_UP_URL=/sign-up
NEXT_PUBLIC_CLERK_AFTER_SIGN_IN_URL=/dashboard
NEXT_PUBLIC_CLERK_AFTER_SIGN_UP_URL=/onboarding

OPENAI_API_KEY=
OPENAI_MODEL=gpt-5-mini

HUBSPOT_ACCESS_TOKEN=
HUBSPOT_PORTAL_ID=

CRON_SECRET=
ENCRYPTION_KEY=
DEMO_MODE=true
LOG_LEVEL=info
```

## Local Development

```bash
npm install
cp .env.example .env
npm run dev
```

Open:

```text
http://localhost:3000
```

If port `3000` is busy, Next.js may choose another port.

## Testing

```bash
npm run lint
npm run test:unit
npm run build
```

Current test coverage includes:

- Opportunity scoring
- Funnel calculations
- HTML sanitization
- URL validation
- Prompt-injection guardrails
- Agent intent routing

## HubSpot Integration

The HubSpot architecture supports private app authentication first:

```env
HUBSPOT_ACCESS_TOKEN=
HUBSPOT_PORTAL_ID=
```

Core supported CRM objects:

- Contacts
- Companies
- Deals
- Owners
- Pipelines
- Associations

Optional capabilities degrade gracefully:

- Lists
- Marketing emails
- Campaigns
- Forms
- Form submissions

The app is structured so OAuth can be added later without rewriting business logic.

## Supabase Database

The starter migration creates:

- Workspaces
- Workspace members with Clerk user IDs
- HubSpot contacts
- HubSpot companies
- HubSpot deals
- Marketing opportunities
- Saved audiences
- Campaigns
- Campaign versions
- Activity events

RLS is enabled on user-accessible tables.

Run migrations from:

```text
supabase/migrations/
```

Seed data:

```text
supabase/seed.sql
```

## Security Model

MarketingOS AI is built with production-minded security patterns:

- Clerk handles authentication.
- Supabase stores application data.
- Service role keys stay server-side only.
- HubSpot tokens stay server-side only.
- OpenAI keys stay server-side only.
- Prompt-injection checks run before agent execution.
- Generated HTML is sanitized.
- CTA URLs are validated.
- Approval is required for customer-facing actions.
- CRM queries are designed to be workspace-scoped.
- No generic SQL tool is exposed to agents.
- No arbitrary HTTP tool is exposed to agents.

## Human Approval Workflow

Approvals are intentionally explicit:

1. AI creates an opportunity recommendation.
2. AI proposes an audience.
3. AI drafts a campaign.
4. Brand and compliance checks run.
5. A human reviewer approves, rejects, or requests changes.
6. Approved content becomes immutable.
7. Publishing remains disabled unless separately implemented.

## Example Prompts

Try these in `/agent`:

```text
Find my highest-impact marketing opportunity.
Which leads are engaged but not converting?
Find stalled deals that need nurturing.
Create a customer-reactivation audience.
Generate an email campaign from the top opportunity.
Analyse our lifecycle-stage funnel.
Show all assumptions behind your recommendation.
Can you explain what have you done?
```

The last prompt is handled as a direct explanation and should not trigger specialist marketing agents.

## What Makes This Different

Most AI marketing tools start with content generation.

MarketingOS AI starts with CRM reality:

- What is happening in the pipeline?
- Which lifecycle transitions are underperforming?
- Which contacts are marketable?
- Which deals are stuck?
- Which customers are quiet?
- Which audiences are safe to target?
- What evidence supports the campaign?
- What needs human approval?

That makes it closer to an AI marketing operating system than a copywriting tool.

## Roadmap

- Live Supabase persistence for all demo-backed service operations
- Production HubSpot incremental sync batches
- OAuth-based HubSpot install flow
- Campaign metric CSV import UI
- Deeper campaign version diff viewer
- Supabase Storage upload and extraction pipeline
- pgvector-powered knowledge retrieval
- Real reviewer assignment and notifications
- Vercel cron jobs for hourly sync and daily opportunity scan
- Optional publishing adapter behind explicit feature flags

## Current Limitations

- Demo mode is fully usable without external credentials.
- Live HubSpot sync scaffolding exists, but production sync persistence needs completion.
- Campaign publishing is intentionally disabled.
- Some dashboard data is synthetic in demo mode.
- The agent run store is currently in-memory for the demo experience.

## Repository Health

Verified commands:

```bash
npm run lint
npm run test:unit
npm run build
```

## Core SEO Keywords

AI agents for marketing, AI marketing agents, agentic marketing automation, HubSpot AI agent, HubSpot CRM AI, AI campaign builder, AI audience segmentation, AI marketing copilot, AI CRM analytics, revenue opportunity detection, lifecycle marketing automation, B2B marketing AI, AI email campaign generator, AI marketing operating system, AI growth marketing platform, autonomous marketing agents, approval-first AI marketing, CRM opportunity engine, AI lead nurture, AI customer reactivation, AI campaign compliance, brand-safe AI copywriting.

## Creator

Built by **Suhas Bhairav**.

Website: [https://suhasbhairav.com](https://suhasbhairav.com)

## License

This project is released under the MIT License. See [LICENSE](./LICENSE).
