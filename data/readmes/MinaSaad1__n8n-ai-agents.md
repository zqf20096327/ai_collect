# n8n AI Agents

Seventeen production-ready [n8n](https://n8n.io) templates. Every one ships the workflow JSON, a canvas render, an architecture write-up, and a security doc. They share the same conventions, so learning one teaches you the rest.

![n8n](https://img.shields.io/badge/n8n-17_templates-EA4B71?logo=n8n) ![LangChain](https://img.shields.io/badge/LangChain-Tools_Agent-121212) ![Claude](https://img.shields.io/badge/Claude-Sonnet_4.6-D97757) ![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Import the JSON, connect your credentials, run it. Nothing here is a slide-deck demo. Each template is wired end to end, documented on the canvas itself, and every stack line below was read back off the workflow that actually ships.

---

## The library

| # | Template | What it does | Trigger |
|---|---|---|---|
| 1 | [Supabase / Postgres Data Analyst](https://github.com/MinaSaad1/n8n-data-analyst-agent) | Chat with your database. Introspects schema, writes SQL, charts the answer | Chat |
| 2 | [Power BI Data Analyst](https://github.com/MinaSaad1/n8n-powerbi-data-analyst-agent) | Same idea over a semantic model. Writes DAX, respects your measures | Chat |
| 3 | [Firecrawl Lead Hunter](https://github.com/MinaSaad1/n8n-firecrawl-web-crawler-agent) | Finds local businesses with great reviews and bad websites, scores and pitches them | Schedule |
| 4 | [Weekly KPI Briefing](https://github.com/MinaSaad1/n8n-weekly-kpi-briefing) | Monday numbers pulled, formatted, and delivered three ways | Schedule |
| 5 | [Lead Enrichment](https://github.com/MinaSaad1/n8n-lead-enrichment) | Form submission to scored, tagged CRM row in under a minute | Webhook |
| 6 | [Email Triage Agent](https://github.com/MinaSaad1/n8n-email-triage) | Classifies every unread mail and leaves a draft reply waiting | Gmail poll |
| 7 | [Content Repurposing](https://github.com/MinaSaad1/n8n-content-repurposing) | One URL becomes a LinkedIn post, newsletter section, and tweet thread | Webhook |
| 8 | [Meeting Notes to Tasks](https://github.com/MinaSaad1/n8n-meeting-notes-to-tasks) | Transcript to Notion tasks with owners, plus a decisions log | Webhook |
| 9 | [Review Monitoring](https://github.com/MinaSaad1/n8n-review-monitoring) | Polls review sources, flags negatives to Slack within the hour | Schedule |
| 10 | [Invoice PDF to Sheets](https://github.com/MinaSaad1/n8n-invoice-pdf-to-sheets) | Drops an invoice in Drive, gets a spreadsheet row back | Drive watch |
| 11 | [AI-Qualified Booking](https://github.com/MinaSaad1/n8n-ai-qualified-booking) | Gates your calendar behind ICP scoring. Three routes, three emails | Webhook |
| 12 | [Social Mention Digest](https://github.com/MinaSaad1/n8n-social-mention-digest) | Daily brand mentions across web, Reddit, and news, negative first | Schedule |
| 13 | [Customer Onboarding](https://github.com/MinaSaad1/n8n-customer-onboarding) | 30-day email sequence with timed check-ins and an NPS ask | Webhook |
| 14 | [Support Reply Agent](https://github.com/MinaSaad1/n8n-support-reply-agent) | Answers tickets it can cite, escalates the rest. A second model grades the first | Gmail poll / Webhook |
| 15 | [KPI Anomaly Watchdog](https://github.com/MinaSaad1/n8n-kpi-anomaly-watchdog) | Statistics detect the anomaly, an agent only explains it, and never silences it | Schedule |
| 16 | [Invoice Three-Way Match](https://github.com/MinaSaad1/n8n-invoice-three-way-match) | Invoice against PO against goods receipt. The model extracts, arithmetic decides | Gmail / Drive / Webhook |
| 17 | [Inbound Lead Router](https://github.com/MinaSaad1/n8n-inbound-lead-router) | Dedupes before it spends, enriches on a budget, and caps the model at one band | Webhook / Gmail poll |

Four shapes show up here, and the difference is architectural, not a difficulty rating.

**Tool-using agents** (1 to 3) hand the model a toolbox and let it decide what to call. Chat trigger, LangChain Tools Agent, Postgres-backed memory, one sub-workflow per tool. Use these when the model owns the runtime decisions.

**Automations** (4 to 13) keep control flow fixed and spend the model on one bounded step, or skip it entirely. Trigger in, action out. Use these when you already know the steps and just want them to happen.

**Agent pipelines** (14) put an agent inside fixed control flow and then refuse to trust it. The agent gets tools and freedom to research, but its output has to clear an explicit quality gate before it reaches anyone, and failing that gate routes to a human rather than to nothing. Use these when the model is doing real work but the output is going somewhere consequential.

**Decision systems** (15 to 17) go one step further and take the decision away from the model entirely. Deterministic code owns the answer, whether that is a statistical test, a reconciliation against a tolerance policy, or a scoring table, and the model does bounded work around it: explaining, extracting, or classifying free text, always inside a hard cap on how much it can change. Use these when the question has a correct answer that a contract, a policy, or arithmetic already defines, and a plausible answer is worse than useless.

The line between the last two is worth stating plainly. In an agent pipeline the model produces the output and a gate decides whether to trust it. In a decision system the model never produces the output at all.

Pick by problem, not by perceived difficulty. Several of the automations are the ones people actually run every day.

---

## Tool-using agents

### 1. Supabase / Postgres Data Analyst

> Natural-language analytics over any Supabase or Postgres database. The agent introspects your schema, writes SQL, runs it under a row cap, and answers with a chart.

**Stack:** Chat Trigger · LangChain Tools Agent · Claude Sonnet 4.6 (OpenRouter) · Postgres Chat Memory · QuickChart

**Tools:** `list_schema` · `get_table_definition` · `run_sql` · `create_chart` · `search_schema_docs` · `export_to_sheets` · `think`

**[→ Open repo](https://github.com/MinaSaad1/n8n-data-analyst-agent)** · [Architecture](https://github.com/MinaSaad1/n8n-data-analyst-agent/blob/main/docs/ARCHITECTURE.md) · [Security](https://github.com/MinaSaad1/n8n-data-analyst-agent/blob/main/docs/SECURITY.md) · [Demo script](https://github.com/MinaSaad1/n8n-data-analyst-agent/blob/main/docs/DEMO_SCRIPT.md)

Ships five workflows: the main agent plus capped-SQL, chart, and schema-docs sub-workflows, and a scheduled morning briefing. SQL setup and demo data included under `sql/`.

![Supabase Data Analyst canvas](assets/supabase-data-analyst.png)

---

### 2. Power BI Data Analyst

> The same pattern against a Power BI semantic model. The agent writes DAX, calls the REST `executeQueries` endpoint, and uses your existing measures instead of re-deriving them.

**Stack:** Chat Trigger · LangChain Tools Agent · Claude Sonnet 4.6 (OpenRouter) · Postgres Chat Memory · Microsoft OAuth2 service principal · Power BI REST API · QuickChart

**Tools:** `list_tables_and_measures` · `get_table_columns` · `run_dax` · `create_chart` · `refresh_dataset` · `think`

**[→ Open repo](https://github.com/MinaSaad1/n8n-powerbi-data-analyst-agent)** · [Architecture](https://github.com/MinaSaad1/n8n-powerbi-data-analyst-agent/blob/main/docs/ARCHITECTURE.md) · [Security](https://github.com/MinaSaad1/n8n-powerbi-data-analyst-agent/blob/main/docs/SECURITY.md) · [Azure AD setup](https://github.com/MinaSaad1/n8n-powerbi-data-analyst-agent/blob/main/docs/AZURE_AD_SETUP.md)

Reading DAX out of a semantic model needs an Azure AD app registration. The setup doc walks the whole service-principal path.

![Power BI Data Analyst canvas](assets/powerbi-data-analyst.png)

---

### 3. Firecrawl Lead Hunter

> **n8n April 2026 Community Challenge submission, Case 3 (Advanced).** A weekly agent that finds local businesses with thriving reviews but outdated websites, enriches each with 10+ signals, computes a composite lead score, drafts a personalized pitch email, upserts to Postgres, and emails a Monday digest with ready-to-send outreach cards.

**Stack:** Schedule Trigger · LangChain Tools Agent · Claude Sonnet 4.6 (OpenRouter) · Firecrawl v1 API · Postgres CRM with credit ledger and 24h scrape cache · Gmail HTML digest

**Tools:** `search_web` · `map_site` · `scrape_url` · `batch_scrape` · `crawl_site` · `extract_data` · `firecrawl_autopilot` · `browser_session` · `check_credits` · `think`

**[→ Open repo](https://github.com/MinaSaad1/n8n-firecrawl-web-crawler-agent)** · [The case](https://github.com/MinaSaad1/n8n-firecrawl-web-crawler-agent/blob/main/docs/MARCO_CASE.md) · [Architecture](https://github.com/MinaSaad1/n8n-firecrawl-web-crawler-agent/blob/main/docs/ARCHITECTURE.md) · [Security](https://github.com/MinaSaad1/n8n-firecrawl-web-crawler-agent/blob/main/docs/SECURITY.md) · [Credit management](https://github.com/MinaSaad1/n8n-firecrawl-web-crawler-agent/blob/main/docs/CREDIT_MANAGEMENT.md) · [Demo script](https://github.com/MinaSaad1/n8n-firecrawl-web-crawler-agent/blob/main/docs/DEMO_SCRIPT.md)

Twelve workflows in total. The nine Firecrawl operations each live in their own sub-workflow, which is what makes the credit ledger and the scrape cache possible. Chat and webhook variants expose the same toolbox for ad-hoc research.

![Firecrawl Lead Hunter canvas](assets/firecrawl-web-crawler.png)

---

## Automations

### 4. Weekly KPI Briefing

> Stop pulling the same Monday numbers by hand. Runs your KPI queries against Postgres, formats an HTML and plain-text digest, and fans out to Slack, email, and a Sheets log in parallel.

**Stack:** Schedule Trigger (Mondays 06:00) · Postgres · Set / Split Out / Aggregate / Code · Slack · Gmail · Google Sheets

**Flow:** cron fires → `Define KPI Queries` Set node holds an array of `{label, sql}` → one execution per KPI → Postgres `executeQuery` → aggregate → format → three delivery branches

**[→ Open repo](https://github.com/MinaSaad1/n8n-weekly-kpi-briefing)** · [Architecture](https://github.com/MinaSaad1/n8n-weekly-kpi-briefing/blob/main/docs/ARCHITECTURE.md) · [Security](https://github.com/MinaSaad1/n8n-weekly-kpi-briefing/blob/main/docs/SECURITY.md) · [Setup](https://github.com/MinaSaad1/n8n-weekly-kpi-briefing/blob/main/docs/SETUP.md)

No model in this one. Adding your metrics means editing one Set node, and deleting a delivery branch you do not want takes a single keystroke.

![Weekly KPI Briefing canvas](https://raw.githubusercontent.com/MinaSaad1/n8n-weekly-kpi-briefing/main/screenshots/canvas.png)

---

### 5. Lead Enrichment

> A form submission arrives, Claude scores it against your criteria, and a tagged row lands in your sheet with a Slack ping. Under 60 seconds per lead.

**Stack:** Webhook · Claude Sonnet 4.6 (Anthropic) · Basic LLM Chain · Google Sheets · Slack

**Flow:** form webhook → extract fields → qualification prompt → parse response → Sheets row + Slack alert → webhook response

**[→ Open repo](https://github.com/MinaSaad1/n8n-lead-enrichment)** · [Architecture](https://github.com/MinaSaad1/n8n-lead-enrichment/blob/main/docs/ARCHITECTURE.md) · [Security](https://github.com/MinaSaad1/n8n-lead-enrichment/blob/main/docs/SECURITY.md)

![Lead Enrichment canvas](https://raw.githubusercontent.com/MinaSaad1/n8n-lead-enrichment/main/screenshots/canvas.png)

---

### 6. Email Triage Agent

> Polls Gmail for unread mail, classifies each one, and leaves a draft reply sitting in your drafts folder. Urgent items also hit Slack. You review, you do not triage.

**Stack:** Gmail Trigger (unread, inbox) · Claude Sonnet 4.6 (Anthropic) · Basic LLM Chain · Gmail draft · If · Slack

**Flow:** poll unread → extract sender, subject, body → one model call returns category and draft → create Gmail draft → if urgent, Slack alert

**[→ Open repo](https://github.com/MinaSaad1/n8n-email-triage)** · [Architecture](https://github.com/MinaSaad1/n8n-email-triage/blob/main/docs/ARCHITECTURE.md) · [Security](https://github.com/MinaSaad1/n8n-email-triage/blob/main/docs/SECURITY.md)

Categorizing and drafting happen in a single call, which is the difference between this costing cents a day and costing real money.

![Email Triage canvas](https://raw.githubusercontent.com/MinaSaad1/n8n-email-triage/main/screenshots/canvas.png)

---

### 7. Content Repurposing

> POST a URL. Get back a LinkedIn post, a newsletter section, and a tweet thread in a Google Doc, with a Slack ping when it is ready. A two-hour job becomes a ten-minute review.

**Stack:** Webhook · Jina.ai Reader (`r.jina.ai`, no key needed) · Claude Sonnet 4.6 (Anthropic) · Google Docs · Slack

**Flow:** URL webhook → Jina extracts clean article text → one model call returns all three formats → create doc and insert content → Slack notify

**[→ Open repo](https://github.com/MinaSaad1/n8n-content-repurposing)** · [Architecture](https://github.com/MinaSaad1/n8n-content-repurposing/blob/main/docs/ARCHITECTURE.md) · [Security](https://github.com/MinaSaad1/n8n-content-repurposing/blob/main/docs/SECURITY.md)

![Content Repurposing canvas](https://raw.githubusercontent.com/MinaSaad1/n8n-content-repurposing/main/screenshots/canvas.png)

---

### 8. Meeting Notes to Tasks

> Send a transcript, get action items with owners and due dates in Notion, a summary page with the decisions log, and a Slack recap.

**Stack:** Webhook · Claude Sonnet 4.6 (Anthropic) · Basic LLM Chain · Notion (summary page + one page per task) · Split Out · Slack

**Flow:** transcript webhook → structured extraction of actions, decisions, open questions, summary → Notion summary page → split action items → one Notion task each → Slack recap

**[→ Open repo](https://github.com/MinaSaad1/n8n-meeting-notes-to-tasks)** · [Architecture](https://github.com/MinaSaad1/n8n-meeting-notes-to-tasks/blob/main/docs/ARCHITECTURE.md) · [Security](https://github.com/MinaSaad1/n8n-meeting-notes-to-tasks/blob/main/docs/SECURITY.md)

![Meeting Notes to Tasks canvas](https://raw.githubusercontent.com/MinaSaad1/n8n-meeting-notes-to-tasks/main/screenshots/canvas.png)

---

### 9. Review Monitoring

> Every six hours, searches for new reviews and Reddit chatter about your brand, classifies sentiment, and pushes the negatives to Slack while there is still time to respond.

**Stack:** Schedule Trigger (every 6h) · SerpAPI (review search + Reddit search) · Claude Sonnet 4.6 (Anthropic) · Filter · Slack · Google Sheets

**Flow:** cron → two SerpAPI searches → merge → classify sentiment → filter to negatives → Slack alert → log everything to Sheets

**[→ Open repo](https://github.com/MinaSaad1/n8n-review-monitoring)** · [Architecture](https://github.com/MinaSaad1/n8n-review-monitoring/blob/main/docs/ARCHITECTURE.md) · [Security](https://github.com/MinaSaad1/n8n-review-monitoring/blob/main/docs/SECURITY.md) · [Setup](https://github.com/MinaSaad1/n8n-review-monitoring/blob/main/docs/SETUP.md)

![Review Monitoring canvas](https://raw.githubusercontent.com/MinaSaad1/n8n-review-monitoring/main/screenshots/canvas.png)

---

### 10. Invoice PDF to Sheets

> Drop an invoice PDF in a watched Drive folder. Vendor, invoice number, date, line items, subtotal, tax, and total land in your accounting sheet about a minute later, with duplicates caught before they are written.

**Stack:** Google Drive Trigger · Claude Sonnet 4.6 vision via the Anthropic Messages API · Google Sheets · If

**Flow:** Drive watch → download → base64 → vision extraction → parse JSON → duplicate check against existing rows → append or log the duplicate

**[→ Open repo](https://github.com/MinaSaad1/n8n-invoice-pdf-to-sheets)** · [Architecture](https://github.com/MinaSaad1/n8n-invoice-pdf-to-sheets/blob/main/docs/ARCHITECTURE.md) · [Security](https://github.com/MinaSaad1/n8n-invoice-pdf-to-sheets/blob/main/docs/SECURITY.md) · [Setup](https://github.com/MinaSaad1/n8n-invoice-pdf-to-sheets/blob/main/docs/SETUP.md)

This one calls the Anthropic API over HTTP Request rather than the native node, because the vision payload needs a document block the chain node does not expose.

![Invoice PDF to Sheets canvas](https://raw.githubusercontent.com/MinaSaad1/n8n-invoice-pdf-to-sheets/main/screenshots/canvas.png)

---

### 11. AI-Qualified Booking

> Put Claude between your intake form and your calendar. Qualified prospects get the booking link, borderline ones route to you for a look, and the rest get a polite decline with alternatives.

**Stack:** Webhook · Claude Sonnet 4.6 (Anthropic) · Switch (three routes) · Gmail (three templates) · Google Sheets

**Flow:** intake webhook → config node holds your ICP criteria → score → route by score → send calendar link, review notification, or decline → log every outcome to Sheets

**[→ Open repo](https://github.com/MinaSaad1/n8n-ai-qualified-booking)** · [Architecture](https://github.com/MinaSaad1/n8n-ai-qualified-booking/blob/main/docs/ARCHITECTURE.md) · [Security](https://github.com/MinaSaad1/n8n-ai-qualified-booking/blob/main/docs/SECURITY.md) · [Setup](https://github.com/MinaSaad1/n8n-ai-qualified-booking/blob/main/docs/SETUP.md)

Calendly stays out of the workflow on purpose. The gate is that the booking link only goes out on the qualified branch, so any scheduler works.

![AI-Qualified Booking canvas](https://raw.githubusercontent.com/MinaSaad1/n8n-ai-qualified-booking/main/screenshots/canvas.png)

---

### 12. Social Mention Digest

> Every morning at 07:00, sweeps web, Reddit, and news for your brand, classifies each mention, and emails one digest with the negatives at the top.

**Stack:** Schedule Trigger (daily 07:00) · SerpAPI (web, Reddit, news) · Claude Sonnet 4.6 (Anthropic) · Filter · Aggregate · Gmail

**Flow:** cron → three SerpAPI searches → compile → classify each mention → filter to relevant → aggregate into one digest → email

**[→ Open repo](https://github.com/MinaSaad1/n8n-social-mention-digest)** · [Architecture](https://github.com/MinaSaad1/n8n-social-mention-digest/blob/main/docs/ARCHITECTURE.md) · [Security](https://github.com/MinaSaad1/n8n-social-mention-digest/blob/main/docs/SECURITY.md) · [Setup](https://github.com/MinaSaad1/n8n-social-mention-digest/blob/main/docs/SETUP.md)

One email a day, not a notification per mention. That is the whole point.

![Social Mention Digest canvas](https://raw.githubusercontent.com/MinaSaad1/n8n-social-mention-digest/main/screenshots/canvas.png)

---

### 13. Customer Onboarding

> A new customer event fires the sequence: welcome on day 0, check-in day 3, friction survey day 7, a flag for human follow-up day 14, and an NPS plus referral ask on day 30.

**Stack:** Webhook (CRM or Stripe) · Set · Wait × 4 · Gmail × 5

**Flow:** customer webhook → extract customer data → respond immediately → five timed emails separated by Wait nodes

**[→ Open repo](https://github.com/MinaSaad1/n8n-customer-onboarding)** · [Architecture](https://github.com/MinaSaad1/n8n-customer-onboarding/blob/main/docs/ARCHITECTURE.md) · [Security](https://github.com/MinaSaad1/n8n-customer-onboarding/blob/main/docs/SECURITY.md) · [Setup](https://github.com/MinaSaad1/n8n-customer-onboarding/blob/main/docs/SETUP.md)

No model here either. It is a Wait-node sequence, and it is in the catalog because the timing and the copy are the hard part, not the wiring. Swap the email bodies for your own and it is ready.

![Customer Onboarding canvas](https://raw.githubusercontent.com/MinaSaad1/n8n-customer-onboarding/main/screenshots/canvas.png)

---

## Agent pipelines

### 14. Support Reply Agent

> Answers the support tickets it can prove an answer for, and escalates the ones it cannot. A drafting agent writes a grounded reply out of your documentation, then a second model from a different vendor grades it before anything is sent.

**Stack:** Gmail Trigger + Webhook · Claude Opus 5 drafting (OpenRouter) · GPT-5.6 Luna grading (OpenRouter) · Postgres pgvector RAG · OpenAI embeddings · Google Drive · Gmail `sendAndWait` approval

**Segments:** all three on one canvas, one import, no sub-workflow re-linking

| Segment | Trigger | Does |
|---|---|---|
| A | Manual / nightly 02:00 | Drive folder to pgvector, only re-embedding what changed |
| B | Gmail poll / webhook | Ticket in, cited reply or actionable escalation out |
| C | Mondays 07:00 | Auto-answer rate, escalation reasons, and the KB gaps behind them |

**[→ Open repo](https://github.com/MinaSaad1/n8n-support-reply-agent)** · [Architecture](https://github.com/MinaSaad1/n8n-support-reply-agent/blob/main/docs/ARCHITECTURE.md) · [Security](https://github.com/MinaSaad1/n8n-support-reply-agent/blob/main/docs/SECURITY.md) · [Setup](https://github.com/MinaSaad1/n8n-support-reply-agent/blob/main/docs/SETUP.md)

Four things separate this from the usual support-bot demo. The **critic did not write the draft**: two vendors disagree in useful ways, where a model grading its own output mostly agrees with itself. The **gate is an AND of five conditions**, not one averaged score, so a fluent answer with zero citations fails. **Policy routing runs before the model spends anything**, so billing, refunds, security and legal never auto-answer regardless of confidence. And **PII is masked before the first model call** and restored only on the way out, so no direct identifier reaches a vendor and only the masked body is stored.

It is deliberately conservative on a cold start: an empty knowledge base produces zero citations, zero citations fail the gate, and a failed gate reaches a human. It does not guess when it has nothing to cite.

![Support Reply Agent canvas](https://raw.githubusercontent.com/MinaSaad1/n8n-support-reply-agent/main/screenshots/canvas.png)

---

## Decision systems

### 15. KPI Anomaly Watchdog

> Watches the numbers your business runs on and, when one breaks, sends a human an explanation instead of a red square. Statistics decide **whether** something is an anomaly; the model only ever explains **why**.

**Stack:** Schedule + Webhook · Postgres median and MAD baselines · Claude Opus 5 investigator (OpenRouter) · five parameterised read-only Postgres tools · GitHub PR lookup · Slack · Gmail `sendAndWait`

| Segment | Trigger | Does |
|---|---|---|
| A | Manual / nightly 01:00 | Registry SQL to daily observations, then median, MAD and per-weekday medians |
| B | Daily 07:00 | Score, suppress, investigate, check the evidence, route by severity |
| C | Webhook | Humans mark alerts real or false, the only ground truth here |
| D | Mondays 08:00 | Turns those judgements into concrete threshold suggestions |

**[→ Open repo](https://github.com/MinaSaad1/n8n-kpi-anomaly-watchdog)** · [Architecture](https://github.com/MinaSaad1/n8n-kpi-anomaly-watchdog/blob/main/docs/ARCHITECTURE.md) · [Security](https://github.com/MinaSaad1/n8n-kpi-anomaly-watchdog/blob/main/docs/SECURITY.md) · [Setup](https://github.com/MinaSaad1/n8n-kpi-anomaly-watchdog/blob/main/docs/SETUP.md)

Five things separate it from "an AI watches your metrics". Detection is a **deterministic Code node** using median and MAD rather than mean and standard deviation, because two bad days in a 28-day window lift a mean enough to hide the third. Day-of-week medians stop Saturday from being an incident. The agent has **no free-form SQL** at all: five fixed queries with named parameters and row caps in the SQL, not in the prompt. Its explanation must clear an **evidence check** including a set-membership test against metric keys that actually exist, which catches the classic confabulation in three lines of JavaScript. And **failing that check never cancels the alert**: it labels it `unexplained` and sends it anyway, as does a model that errors out entirely.

Suppression caps the blast radius before any spend: a 24-hour cooldown per metric plus a hard cap on incidents per run, ranked by z-score, because a warehouse-wide outage otherwise means one billed investigation per metric all reaching the same conclusion.

![KPI Anomaly Watchdog canvas](https://raw.githubusercontent.com/MinaSaad1/n8n-kpi-anomaly-watchdog/main/screenshots/canvas.png)

---

### 16. Invoice Three-Way Match

> Reads supplier invoices, reconciles each against the purchase order **and** the goods receipt, and pays the ones that agree. The model extracts; it never decides.

**Stack:** Gmail Trigger + Drive Trigger + Webhook · Claude Opus 5 extraction with per-field confidence (OpenRouter) · GPT-5.6 Luna supplier email (OpenRouter) · Postgres tolerance policy · Google Sheets ledger · Gmail `sendAndWait` · Slack

| Segment | Trigger | Does |
|---|---|---|
| A | Gmail / Drive / Webhook | Fingerprint, transcribe with confidence, check the invoice against its own arithmetic |
| B | Chained | Four hard blocks, then line-level match against PO and receipt |
| C | Chained | Post, ask an approver, ask the supplier, or hand it to a human |
| D | 1st of the month | Auto-post rate, and why the rest did not qualify |

**[→ Open repo](https://github.com/MinaSaad1/n8n-invoice-three-way-match)** · [Architecture](https://github.com/MinaSaad1/n8n-invoice-three-way-match/blob/main/docs/ARCHITECTURE.md) · [Security](https://github.com/MinaSaad1/n8n-invoice-three-way-match/blob/main/docs/SECURITY.md) · [Setup](https://github.com/MinaSaad1/n8n-invoice-three-way-match/blob/main/docs/SETUP.md)

The control worth stealing even if you never import this: **bank details that differ from the supplier record are a hard block.** Invoice-redirection fraud is a real supplier, a real delivery, the right price, and a changed account number. It reconciles perfectly, and every check based on "do the numbers add up" passes it. The extraction prompt therefore forbids normalising, correcting or completing the IBAN, because a helpful model defeats the comparison entirely.

Three more: dedupe is by **content fingerprint, not filename**, because paying twice is the expensive failure. Totals are transcribed **exactly as printed even when wrong**, so a model misreading a number and a supplier billing wrongly stay distinguishable. And **field-level confidence gates auto-posting**, scored on how clearly each field could be *read* rather than how plausible it looks.

![Invoice Three-Way Match canvas](https://raw.githubusercontent.com/MinaSaad1/n8n-invoice-three-way-match/main/screenshots/canvas.png)

---

### 17. Inbound Lead Router

> Works out who a lead already is before spending anything on them, fills only the gaps that are missing, grades them on rules sales wrote, and puts a clock on the response.

**Stack:** Webhook + Gmail Trigger · Postgres identity resolution · free-then-paid enrichment waterfall with a daily budget · GPT-5.6 Luna intent classification (OpenRouter) · HubSpot · Slack · Gmail

| Segment | Trigger | Does |
|---|---|---|
| A | Webhook / Gmail poll | Normalise, screen, and find out whether we already know this person |
| B | Chained | Owned history, then the company homepage, then a paid provider, stopping early |
| C | Chained | Rules score fit, a model reads only the message, round-robin assignment |
| D | Every 15 min, Mondays 08:00 | Escalate untouched hot leads, then report whether any of it worked |

**[→ Open repo](https://github.com/MinaSaad1/n8n-inbound-lead-router)** · [Architecture](https://github.com/MinaSaad1/n8n-inbound-lead-router/blob/main/docs/ARCHITECTURE.md) · [Security](https://github.com/MinaSaad1/n8n-inbound-lead-router/blob/main/docs/SECURITY.md) · [Setup](https://github.com/MinaSaad1/n8n-inbound-lead-router/blob/main/docs/SETUP.md)

Lead capture is the most crowded category there is, and this is not another one. **Identity resolution runs before any spend**, across four ranked keys, with normalisation that strips plus-addressing everywhere and dots only on Gmail, because stripping dots on a corporate domain would merge two real colleagues. **Enrichment is a waterfall with a daily budget** checked before the paid call, and every field records which step filled it, so the weekly report can ask whether paying changed any decision.

And the rule that makes it safe to run unattended: **the model can move a lead at most one band.** Fit comes from a scoring table; a separate model reads only the free-text message and never sees firmographics. Above 0.7 confidence it may promote or demote by one band, below it nothing changes, and if it errors nothing changes. It cannot invent an A and it cannot bury a good lead. The single exception is an explicit red flag, because a job application is not a lead however well the domain scores.

![Inbound Lead Router canvas](https://raw.githubusercontent.com/MinaSaad1/n8n-inbound-lead-router/main/screenshots/canvas.png)

---

## Using a template

1. Download the workflow JSON from the repo's `workflows/` folder
2. In n8n, **Workflows → Import from File**
3. Open each node with a credential warning and pick your own credential
4. Fill in the placeholders. They are written in caps, like `YOUR_SLACK_CHANNEL` and `YOUR_GOOGLE_SHEET_ID`
5. Read the sticky notes on the canvas. Every template documents itself there
6. Run once manually before you activate the trigger

Templates with sub-workflows (the three agents) need the sub-workflows imported first, then re-linked in the parent's tool nodes. Their architecture docs cover the order.

## Shared principles

These hold across the catalog, so they live here instead of being copy-pasted into thirteen repos:

- [**Architecture Principles**](docs/architecture-principles.md): the Tools Agent shape, why `run_*` and `create_chart` are sub-workflows, primitive-based chart interfaces, memory handling, why the `think` tool earns its place
- [**Security Framework**](docs/security-framework.md): the layered model: auth, identity passthrough, data-source RLS, scoped roles, PII masking, query guards, audit and rate limits, output filtering, cost caps, memory hygiene
- [**Output Conventions**](docs/output-conventions.md): the strict markdown response format (bold headline, chart, pipe table, query, observations) and number formatting rules
- [**Testing Guide**](docs/testing-guide.md): validating an imported template end to end, common failure modes, debugging through the Executions panel
- [**Contributing**](docs/contributing.md): file structure, required docs, naming conventions, submission checklist

## What makes these different

Most "AI agent in n8n" tutorials wire up one tool and stop. These go further:

- **Schema-aware.** The agents introspect what exists before writing a query. No invented table or column names.
- **Safe by default.** Read-only access, row caps, explicit write authorization. Not production-hardened out of the box, and the security framework is honest about the gap.
- **Visual by default.** The analyst agents answer with a chart most of the time. People read trends faster than they read numbers.
- **Memory that works.** Postgres-backed conversation history keyed by `sessionId`.
- **Self-documenting.** Sticky notes on every canvas, architecture and security docs in every repo, a canvas render in every README.
- **Actually wired.** Every template runs end to end on import. Where a template has no model in it, this README says so instead of dressing it up.

## Roadmap

Open an issue if you want one of these prioritized, or [submit your own](docs/contributing.md):

- [ ] **Snowflake Data Analyst**, same pattern, Snowflake warehouse
- [ ] **BigQuery Data Analyst**, GCP-native
- [ ] **MongoDB Analyst**, aggregation pipeline instead of SQL
- [ ] **HubSpot / Salesforce Analyst**, natural-language CRM queries
- [ ] **Airtable Base Analyst**, for no-code teams
- [ ] **Metabase Question Writer**, the agent writes Metabase questions from prompts
- [ ] **Evaluator workflow**, scores agent responses against ground truth for prompt iteration

## Author

Built by [Mina Saad](https://github.com/MinaSaad1). Issues and PRs welcome on any template repo or here.

## License

MIT, see [LICENSE](LICENSE). Each template repo carries its own MIT license.

---

## Need one of these running in your business?

Every template here is free, MIT, and meant to be forked. Getting one into
production against your real data, your credentials and your edge cases is a
different job, and it is the one I do.

I work out what is actually costing a business, then build whatever fixes it: an
AI agent, an automation, or a full application. Handed over so your team owns it. Repo yours from the
first commit. n8n Ambassador for Cairo.

[Book a call](https://cal.com/minasaad/60min) · [mina-saad.com](https://www.mina-saad.com)
