# Recruit OS

**English** | [简体中文](README.zh-CN.md)

## Help every interviewer conduct better interviews

**Know what to ask, when to probe, and how to make evidence-based decisions.**

[MIT License](LICENSE) · [GitHub](https://github.com/xinxing870126-prog/recruit-os)

Recruit OS is an **AI-assisted interview workspace**. It brings together role requirements, candidate experience, and evidence from earlier interviews to help interviewers prepare questions, follow up during the conversation, and review evidence afterward. Interviewers make the final decisions.

Our goal is to make the preparation, questioning, and verification practices of experienced interviewers accessible to everyone conducting an interview.

The project is already used at the author's company. This community release shares product design and engineering shaped by real hiring workflows, for teams to deploy, study, and improve. The campus recruiting module is still in development and is not included in this release.

**Language support:** The project overview, quick start, and interview walkthrough are available in English and Simplified Chinese. The application UI, demo data, and screenshots are currently primarily in Simplified Chinese. A complete English UI and language switcher are not yet available.

## At the core: the interview workspace

| Stage | The interviewer's question | How the workspace helps |
| --- | --- | --- |
| Before | I've read the resume. What should I ask in this round? | Candidate context, round objectives, a prioritized interview plan, primary questions, and conditional follow-ups. Later rounds build on earlier evidence. |
| During | That sounds promising. What should I probe next? | Questions organized around the current topic, follow-up suggestions informed by the live conversation, and a retained history of follow-ups. |
| After | How do I turn my impressions into a supported assessment? | Conversation records, evidence and risk summaries, and AI feedback drafts. Interviewers submit their own feedback and confirm conclusions. |

### A concrete example: from an outcome to the work behind it

A candidate says: “We redesigned the commission scheme, saving an estimated RMB 2.2 million annually.”

The workspace prepares two follow-ups for this kind of answer:

- **When the answer only describes a team achievement:** Which part did you own independently? Give an example of a decision you made that changed the original proposal.
- **When the answer only gives a headline number:** What baseline did you use? How much has actually been saved, and how much is an annualized projection?

These questions help separate individual contribution from team results, and realized outcomes from forecasts. The interviewer can then record the evidence obtained and what still needs verification.

The screenshots below show the actual application running locally. Interview plans, dialogue, and feedback are **handwritten fictional demo snapshots**, intended to explain the workflow rather than demonstrate model quality. Live audio and AI advice require configured services; live operation is not demonstrated in these screenshots. English captions explain the Chinese UI.

**Question guide and conditional follow-ups**

The expanded “回答模糊时怎么追” section means “How to follow up when an answer is vague.” It shows when to ask about personal ownership and when to check the claimed savings.

![Interview plan with primary questions and conditional follow-ups, shown in the Chinese UI](docs/images/interview-followups.png)

**Before the interview: establish objectives and verification priorities**

“本轮目标” identifies the round's objective. “面试路线” organizes topics by priority and suggested duration.

![Interview workspace showing the round objective, candidate context, and prioritized plan](docs/images/interview-workspace.png)

**After the interview: review an AI draft and enter a human conclusion**

The left column contains the demo assessment; the right column is the interviewer's own conclusion and feedback. The example remains unsubmitted.

![Demo feedback draft alongside the interviewer's conclusion form](docs/images/interview-feedback.png)

[Read the full walkthrough: plan → follow-ups → conversation evidence → human conclusion](docs/interview-workspace.md)

## The recruiting workflow around the interview

**Define a role → Import a resume → Prepare the interview → Interview and probe → Confirm evidence and conclusions → Follow up**

- Role definition and calibration: organize hiring needs, requirements, and evaluation criteria.
- Candidate analysis: combine the resume and role to identify supporting evidence and open questions.
- Decisions and follow-up: carry interview feedback forward and record the next actions.
- Enterprise integration: independent deployment, organization permissions, Feishu calendar and identity integration, model configuration, and background jobs.

<details>
<summary>View role and candidate screens</summary>

These screens also use fictional data and demo snapshots. The UI is in Simplified Chinese.

![Role workspace](docs/images/roles.png)

![Candidate list](docs/images/candidates.png)

![Candidate analysis detail](docs/images/candidate-detail.png)

</details>

## Quick start

Prerequisites: Node.js 22, npm, and Docker Compose. Ports 3000, 5432, and 6379 must be available.

Clone this repository and enter its directory, then run:

```bash
npm ci
cp .env.example .env.local
docker compose -p recruit-community up -d --wait
```

Temporarily add the following settings to `.env.local`. Replace the password placeholder with your own password of at least 12 characters:

```dotenv
BOOTSTRAP_ADMIN_EMAIL=admin@example.com
BOOTSTRAP_ADMIN_PASSWORD=replace-with-your-own-password
```

Then run:

```bash
npm run admin:bootstrap
npm run demo:seed
npm run dev
```

Open <http://localhost:3000> and sign in with the credentials you just configured. After creating the account, remove both `BOOTSTRAP_ADMIN_*` settings from `.env.local`. Bootstrap only works when the database has no users; create subsequent accounts through the application's account management interface.

The demo includes fictional roles, candidates, role profiles, candidate analysis snapshots, and a **complete finance business partner interview example**: a plan, conditional follow-ups, dialogue records, and a feedback draft awaiting confirmation. The seed command prints a `/interview-sessions/demo_interview_...` path. After signing in, open that path on your local server to explore the workspace.

The example interview is assigned to the first user in the database, so use the administrator you just created. Running the seed command again appends roles and candidates. Use a dedicated demo database.

**Demo scope:** Browse interview plans, expand follow-ups, inspect fictional dialogue and feedback evidence, and explore role profiles and candidate analysis. Snapshots are labeled “演示数据” (demo data) and do not represent real model assessments. Regenerating plans or assessments, live advice, and other AI interactions require a configured model. Feishu scheduling and speech transcription require their respective services. The demo does not simulate live recording or external service workflows.

If the default ports are occupied, choose separate ports and update the connection URLs in `.env.local` to match:

```bash
DEV_POSTGRES_PORT=55439 DEV_REDIS_PORT=56389 docker compose -p recruit-community up -d --wait
# In .env.local, change DATABASE_URL to port 55439 and REDIS_URL to port 56389.
npx next dev -H 127.0.0.1 -p 3317
```

With these settings, open <http://localhost:3317>.

To stop the local database and Redis, run `docker compose -p recruit-community down`. Data remains in that Compose project's volumes.

## Connect real services

- Models: configure compatible providers and task routing in the admin interface. Environment variables provide development configuration options. Real AI calls may incur provider charges.
- Feishu: configure your organization's application and authorization for identity, calendar, or meeting features.
- Speech: configure the automatic speech recognition (ASR) service and relay. Browser recording requires localhost or valid HTTPS.
- Company content: company name, contact details, on-site location, and transcription vocabulary are configurable. See the [configuration guide (Chinese)](docs/configuration.md).

## Production deployment

Deploy a separate instance for each organization. Production services include the Next.js web application, background worker, role generation worker, ASR relay, Postgres, Redis, and S3-compatible object storage.

`DEMO_LLM` is prohibited in production. Postgres is the application database. SQLite remains only for legacy compatibility tests and is not a production option.

Read the [production deployment guide (Chinese)](docs/production/README.md) before deploying.

## Verification

```bash
npm run verify:community
npm run verify:release
```

`verify:community` checks community configuration, invitation content, transcription vocabulary, release provenance, and TypeScript. `verify:release` includes dependency auditing, runtime boundaries, permissions, and a production build. Run verification against an isolated development database, not a real business database.

## Project layout

```text
src/                     Application and business logic
scripts/worker.ts        General background worker
scripts/role-generation-worker.ts
scripts/qwen-asr-relay.ts
scripts/bootstrap-admin.ts
scripts/seed.ts          Explicitly labeled fictional demo data
docs/                    Community configuration and deployment guides
compose.production.yml   Production service definitions
docker-compose.yml       Local development database and Redis
```

## Maintenance and contributions

Issues and pull requests are handled as maintainer time permits. There is no commitment to fixed response times, hosted services, or implementation support. Reproducible bug reports, documentation improvements, and broadly useful features are welcome. See the [contribution guide (Chinese)](CONTRIBUTING.md).

## Author and license

Maintained by [幸鑫 (Xingxin)](https://github.com/xinxing870126-prog) and project contributors.

Recruit OS is released under the [MIT License](LICENSE), allowing commercial use, modification, and redistribution subject to retaining the copyright and license notices. Third-party dependencies retain their own licenses; see the [dependency license inventory](docs/dependencies.md).
