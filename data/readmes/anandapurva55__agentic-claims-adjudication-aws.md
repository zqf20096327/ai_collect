# Agentic Motor Claims Adjudication on AWS: Full-Stack Multi-Agent AI with RAG, MCP, Memory, Guardrails, QLoRA Fine-Tuning and Human in the Loop

[![CI](https://github.com/anandapurva55/agentic-claims-adjudication-aws/actions/workflows/ci.yml/badge.svg)](https://github.com/anandapurva55/agentic-claims-adjudication-aws/actions/workflows/ci.yml)
[![CodeQL](https://github.com/anandapurva55/agentic-claims-adjudication-aws/actions/workflows/codeql.yml/badge.svg)](https://github.com/anandapurva55/agentic-claims-adjudication-aws/actions/workflows/codeql.yml)
[![Interactive demo](docs/images/badges/interactive-demo.svg)](https://anandapurva55.github.io/agentic-claims-adjudication-aws/)
![Python](docs/images/badges/python.svg)
![AWS](docs/images/badges/aws.svg)
![Strands](docs/images/badges/strands.svg)
![MCP](docs/images/badges/mcp.svg)
![RAG](docs/images/badges/rag.svg)
![Guardrails](docs/images/badges/guardrails.svg)
![Cognito](docs/images/badges/cognito.svg)
![WAF](docs/images/badges/waf.svg)
![CloudFront](docs/images/badges/cloudfront.svg)
![DynamoDB](docs/images/badges/dynamodb.svg)
![S3](docs/images/badges/s3.svg)
![Secrets Manager](docs/images/badges/secrets-manager.svg)
![React](docs/images/badges/react.svg)
![TypeScript](docs/images/badges/typescript.svg)
![FastAPI](docs/images/badges/fastapi.svg)
![uv](docs/images/badges/uv.svg)

## From claim to decision

This project helps an insurance adjuster decide a motor insurance claim. A claim arrives as a claim form, a repair estimate, a short description of the accident and a photo of the damage. The system reads them, checks them against the policy, and recommends approve, deny or refer. A person always makes the final decision. Here is what happens, from start to finish, and which tool does each part.

1. **The files are read.** The claim files sit in **Amazon S3**. Before any run, **Bedrock Data Automation** reads the claim form and the damage photo and turns them into fields, and a vision model also reads the photo. The results are stored, so a run does not wait for them.
2. **The adjuster signs in.** The app is a **React** and **TypeScript** web page, built with **Vite**. Sign in goes through **Amazon Cognito**. **Amazon CloudFront** serves the page and passes every request on to the backend, and **AWS WAF** limits how many requests one address can send. The backend is a **FastAPI** service written in **Python**. It runs as a container on **Amazon ECS** with **Fargate**, in a **VPC**, behind an internal load balancer. **Amazon ECR** stores the container image, and **AWS Secrets Manager** holds the secret that proves a request came through CloudFront.
3. **The text is cleaned.** When the adjuster starts a run, **Bedrock Guardrails** checks the accident description and the other free text for hidden instructions aimed at the AI, and removes them.
4. **A team of AI agents reads the claim.** **Strands Agents** does the orchestration. It builds each agent on a model from **Amazon Bedrock** and runs the first three as a graph, deciding which agent goes first and which run together. The Intake agent reads the description and sets six yes or no flags, such as drunk driving or commercial use. The Coverage agent and the Investigator then work at the same time. The Coverage agent looks up the policy clauses that apply and works out the payable amount. The Investigator checks repair costs, the garage, the police report and earlier claims on the policy.
5. **The agents use tools and memory.** The tools reach the agents through the **Model Context Protocol** (**MCP**), a standard way to give an AI tools. The policy wording is found with **retrieval-augmented generation** (**RAG**): **Bedrock Knowledge Bases** search the policy text, which is kept in **S3 Vectors**, and return the right clause with its identifier. **Bedrock AgentCore Memory** lets the Intake agent recall lessons from earlier cases that adjusters corrected.
6. **Plain code makes the decision.** Rule checks add warnings the agents may have missed, such as a photo that does not match the estimate. Then a rules engine, which is ordinary code and not an AI model, calculates the payable amount and makes the decision. The last agent only writes a short memo that explains it.
7. **A person decides.** The recommendation appears in the app as it is produced. The adjuster accepts it, overrides it with a written reason, or escalates it to a senior adjuster. Each claim gets exactly one human decision, stored in **Amazon DynamoDB** under the name and role from the sign-in token. An override also becomes a lesson in memory.
8. **Everything is measured.** Every model call is recorded with its tokens, time and cost. The records go to S3, and **AWS Glue**, **Amazon Athena** and **Amazon QuickSight** let people query and chart them. **Amazon CloudWatch** raises alarms when errors, speed or cost go wrong.

Around this, **AWS CDK** defines all of the AWS resources as code. **GitHub Actions** runs the tests on every change, **CodeQL** and **Dependabot** look for security problems, and **GitHub Pages** hosts the interactive demo. **uv** locks the Python packages. **Amazon SageMaker** ran one experiment: it fine-tuned a small model with **QLoRA** to see whether it could replace a prompted model, and it could not do so economically.

The system was built, deployed to AWS, checked end to end by an automated script (29 of 29 checks), and then torn down. It uses synthetic claims, real policy wording and real damage photos.

## Try it

An [interactive demo](https://anandapurva55.github.io/agentic-claims-adjudication-aws/) of the app runs on GitHub Pages, with no server and no cost. The AI agents are switched off there to avoid cost, so each run replays the rule baseline on real claim data. A banner says so on every page. Everything else works, and the visitor does each step.

1. **Sign in.** The demo opens on the same sign-in screen as the live site. A login page, laid out like Cognito's, then asks for a username and password. Any username works with any password that meets the real password rule: 12 or more characters, with upper and lower case letters, a digit and a symbol. A checklist under the password box turns from red to green as each rule is met. There is no sign up, as in the live system.
2. **Pick a claim** in the queue. CLM-2026044 carries an injected instruction in its narrative, and CLM-2026043 needs a senior adjuster.
3. **Run the agents** and watch the graph and the trace.
4. **Make the call** in the Decision panel: accept, override or escalate. Then open your initials, top right, and switch to senior adjuster to try the approval rule above INR 200,000.

The demo data is saved from the real backend when the site is built. A small fetch layer in the frontend answers the app's calls from that data, so nothing is sent anywhere. [Limitations](#limitations) lists what the demo leaves out.

## Results at a glance

![A live run on the deployed system: Bedrock Data Automation and a vision model read the photo, agents use memory and MCP tools, risk signals appear, and a person decides](docs/images/demo/photo_evidence_and_signals.gif)

*A live run on the deployed system. The photo is read at ingestion, an agent recalls a lesson from long term memory, the photo and the repair estimate disagree, and the recommendation waits for a person.*

| Measure | Result | n |
|---|---|---|
| Decision accuracy on claims with wording the system had not seen | **98.7%** (95% interval 93.1% to 99.8%) | 78 claims in two held-out sets |
| Decision accuracy on 124 free-form narratives written and labelled by other model families | Agent team **98.4%** and a single model call **98.4%** | 124 claims |
| Unsafe approvals (a claim that must be denied, approved) | 0 on the golden set and on held-out set 2. 1 on held-out set 1, caused by a defect in the test data, analysed below. 1 each for the agent team and the single call on the free-form set | 63 + 78 + 124 claims |
| Payable amount exact | 100% on the template sets. The rules engine also reproduces 20 hand-calculated boundary claims | 141 + 20 claims |
| Red team attacks that succeeded against the hardened system | 0 | 29 completed attacks (a model error ended the 30th) |
| Policy retrieval, recall at 3 (the default) and at 5 | 79.2% and 85.4% with clause cards (66.7% and 77.1% without) | 48 questions |
| Model cost per claim | 0.046 to 0.049 USD at the baseline, 0.035 USD with the optimised configuration (measured twice) | 22 claims, twice |
| Automated tests | 523 (463 Python, 60 frontend) | |

A single model call followed by the same rules engine matched or beat the agent team on every accuracy benchmark, at about one fiftieth of the cost. So the case for the agents does not rest on accuracy. It rests on what they add when the facts live in records. [Agents compared with a single call](#agents-compared-with-a-single-call) sets out the evidence, including where the agents lose.

---

## Contents

| Section | What it covers |
|---|---|
| [From claim to decision](#from-claim-to-decision) | What happens to a claim from start to finish, and what each tool does |
| [Try it](#try-it) | An interactive demo in the browser, with no server and no cost |
| [Results at a glance](#results-at-a-glance) | A live run, and the headline measurements |
| [Problem and scope](#problem-and-scope) | The problem, the user, and what is in and out of scope |
| [Tenets](#tenets) | The principles that settled the design questions |
| [Solution architecture](#solution-architecture) | AWS services, the three paths and the release pipeline |
| [Design decisions](#design-decisions) | Each choice, the alternatives considered and what it costs |
| [How a claim is decided](#how-a-claim-is-decided) | The flow from claim packet to human decision |
| [Agents, MCP and memory](#agents-mcp-and-memory) | The Strands agent graph, MCP servers and two tiers of memory |
| [Document and image understanding](#document-and-image-understanding) | Bedrock Data Automation on forms and real damage photos, with measurements |
| [Retrieval-augmented generation (RAG)](#retrieval-augmented-generation-rag) | Chunking, embeddings, metadata, retrieval and its evaluation |
| [Human in the loop](#human-in-the-loop) | The sign-off gate that the API enforces |
| [Security and red team testing](#security-and-red-team-testing) | Threat model, defence layers and 30 attacks with controls |
| [Frontend: the workbench UI](#frontend-the-workbench-ui) | React and TypeScript app with a live agent graph |
| [Evaluation](#evaluation) | Golden and held-out sets, an independent oracle, ablations and the quality gate |
| [Agents compared with a single call](#agents-compared-with-a-single-call) | A single call baseline, a free-form benchmark and a planted problem investigation test |
| [Cost, latency and observability](#cost-latency-and-observability) | Telemetry lake, measured optimisations and alerting |
| [Fine-tuning a small model with QLoRA](#fine-tuning-a-small-model-with-qlora) | Method, results and when fine-tuning pays off |
| [Deployment](#deployment) | Acceptance test, console evidence and deploy commands |
| [Operating the system](#operating-the-system) | Alarms, failure modes and responses |
| [Quick start](#quick-start) | Run it locally |
| [Issues found and resolved](#issues-found-and-resolved) | Diagnoses and fixes |
| [Limitations](#limitations) | Open gaps and how to close them |
| [Next steps](#next-steps) | Planned improvements across retrieval, ingestion, identity and the fine-tuning study |
| [Repository layout](#repository-layout) | Where things live |
| [Data sources and references](#data-sources-and-references) | Datasets, policy wordings and papers |

---

## Problem and scope

An adjuster handling a motor claim reads a form, a repair estimate and a photo, compares them with the policy wording, decides whether an exclusion applies, and calculates what to pay. Much of the work is reading and cross-checking. The failure that matters most is a wrong approval: paying a claim that the policy excludes.

**In scope.** Reading the packet, retrieving the relevant clauses, judging the narrative against exclusions, calculating the payable amount, surfacing risk signals, and recording a human decision with an audit trail.

**Out of scope.** Paying claims, fraud adjudication, customer communication, and any decision made without a person.

**Customer.** The claims adjuster. The most important metric is the number of unsafe approvals. Accuracy, cost and latency matter less, but they are measured because they decide whether the system is usable.

---

## Tenets

These principles settled the design questions below.

1. **Models judge, code decides.** A model sets six judgement flags. A tested rules engine turns the flags and the facts into a decision and a payable amount. A model that is manipulated can change a flag, but it cannot set an amount.
2. **A person owns every outcome.** The **API** refuses to settle a claim without a recorded human decision. The UI is not the control.
3. **Customer text is hostile.** Narratives and garage remarks are treated as data, not instructions. A guardrail scans them before any agent reads them. No agent has a tool that pays money.
4. **Least privilege, including for memory.** Each agent receives only the tools it needs. Long term memory is writable only by a human.
5. **Measure against a baseline, on data not tuned against.** Every claim of improvement states its baseline, its sample size and its uncertainty.
6. **Report what failed.** Defects, retracted conclusions and open gaps are part of the result.

---

## Solution architecture

![AWS architecture](docs/images/aws_architecture.png)

| Path | Purpose | Services |
|---|---|---|
| **Serving** | Answer the adjuster | AWS WAF and Amazon CloudFront at the edge, Amazon Cognito for sign in, a CloudFront VPC origin to an internal Application Load Balancer, Amazon ECS on Fargate (arm64) running FastAPI and the agent graph |
| **Reasoning** | Decide | Amazon Bedrock models, Guardrails, Knowledge Bases, Bedrock Data Automation, AgentCore Memory |
| **Learning and operations** | Measure and improve | S3 telemetry lake, AWS Glue, Amazon Athena, Amazon QuickSight, Amazon CloudWatch, Amazon SageMaker |

| Service | Role in the system |
|---|---|
| Amazon Bedrock | Nova 2 Lite for the intake and investigator agents, Claude Haiku 4.5 for the coverage agent, and Claude Sonnet 4.6 for the adjudicator memo. Model identifiers are set in configuration |
| Bedrock Guardrails | Prompt attack filter, hate and insult filters, PII handling, regex detectors for Aadhaar and PAN numbers, a denied topic for approval overrides |
| Bedrock Knowledge Bases on Amazon S3 Vectors | Policy clause retrieval with Titan Text Embeddings V2 ([RAG](#retrieval-augmented-generation-rag)) |
| Amazon Bedrock Data Automation | Reads the claim form and the damage photo into structured fields with two custom blueprints |
| Bedrock AgentCore Memory | Short term notes per claim, long term lessons (semantic strategy) writable only by a human |
| Amazon ECS on Fargate, internal ALB, CloudFront | Serving. The load balancer is internal and sits in isolated subnets with no route to the internet. The task runs in a public subnet, because there is no NAT gateway and the task calls AWS services. It accepts traffic only from the load balancer's security group. CloudFront reaches the load balancer through a VPC origin. The load balancer admits only the security group that CloudFront attaches to that origin, and its listener rejects requests that lack a secret header |
| Amazon Cognito | Sign in. Only administrators create users. Two groups, `adjuster` and `senior`, set the reviewer's role. The site signs in through Cognito's hosted page, using the authorization code flow with PKCE |
| AWS WAF | Rate limits per client address on CloudFront: 20 agent runs and 600 requests in 5 minutes |
| AWS Secrets Manager | Generates the secret header value at deploy time, so it never appears in the repository |
| Amazon DynamoDB | Four tables: policies, extracted claim data, the audit log, and run metrics |
| Amazon S3 | Four buckets: claim files and Data Automation output, policy documents, the telemetry lake, and fine-tuning files. A separate S3 Vectors bucket holds the clause index |
| AWS Glue, Amazon Athena, Amazon QuickSight | One JSON record per model call lands in S3. Athena queries it with partition projection. QuickSight shows cost and latency |
| Amazon CloudWatch | Dashboard, latency and 5xx alarms, and a cost spike alarm fed by a custom metric |
| Amazon SageMaker | QLoRA fine-tuning job on one GPU instance |
| AWS CDK (Python) | Defines all the AWS resources as Infrastructure as Code, in two stacks: `ClaimsAdjudicationData` for the data and AI services, and `ClaimsAdjudicationApp` for the service, network and sign in. It runs without AWS credentials, so tests check the synthesised template in CI |
| GitHub Actions | Workflows for lint, types, tests, the eval gate, the red team, CodeQL, the interactive demo, live evaluation and deploy. The Python environment comes from `uv.lock`. Deploy and live evaluation sign in to AWS through OIDC, using role ARNs stored as repository variables, so no long lived keys are stored |

<img src="docs/images/release_path.png" alt="Release path" width="560">

The **CI** workflow runs on every push and pull request. It runs lint with the security rules, **mypy**, the **Python** tests, the replay quality gate, the **red team** in replay mode, the frontend tests, an **npm** audit, the type check and build, the infrastructure security tests, and **CDK** synthesis. The infrastructure job waits for the frontend build. A separate **CodeQL** workflow scans the **Python** and **TypeScript** code on every push. A third workflow publishes the interactive demo to **GitHub Pages** on every push to `main`. Deploy and live evaluation are manual workflows, and CI does not gate them. They need an **OIDC** provider and a deploy role that this **CDK** app does not create.

The diagrams are written as code with the **Python** `diagrams` library ([docs/diagrams/generate.py](docs/diagrams/generate.py)). They are versioned with the system, and tests check the facts they show.

---

## Design decisions

| Decision | Alternatives considered | Rationale | Cost of the choice |
|---|---|---|---|
| A rules engine decides, models set flags | Let an agent decide and calculate | Money and exclusions need exact answers and resistance to injected text. Given correct flags, the engine reproduces all 63 golden outcomes and 20 hand-calculated boundary claims exactly | The engine must be updated when the policy changes. Situations it does not cover go to a human and are not guessed |
| ECS on Fargate | EC2, Lambda | No servers to patch, scales per task, and costs nothing when scaled to zero. Agent runs last 20 to 40 seconds and stream their progress, so a long lived container suits them better than Lambda | Live runs are serialised per task, because tool state is per process. Scaling out means more tasks |
| S3 Vectors | OpenSearch Serverless, pgvector | The corpus is small, and S3 Vectors has no standing hourly charge | No hybrid (keyword plus vector) search |
| Public subnets for tasks, isolated subnets for the load balancer, no NAT gateway | Private subnets with NAT | Saves roughly one dollar a day for a workload with no private resources. The load balancer is internal, so it has no public address at all, and tasks accept traffic only from it | Tasks have public IPs. Acceptable here, not for a regulated workload |
| CloudFront reaches the API through a VPC origin to an internal ALB | A public ALB limited by CloudFront's prefix list and a secret header. HTTPS to the origin, which needs a certificate and a domain name | Traffic never crosses the public internet. The load balancer can be reached only through CloudFront. No domain has to be bought. The secret header stays as a second check | More moving parts: CloudFront attaches its own security group to the origin's network interfaces, and the load balancer has to admit that group by id (see [issues found and resolved](#issues-found-and-resolved)) |
| Cognito hosted sign in, authorization code flow with PKCE | A login form in the app, a shared API key | No password passes through the application, tokens never appear in a URL, and the role is a group inside a token that the API verifies | The sign in page is Cognito's, styled with its branding settings. Administrators create users |
| Python dependencies locked with uv | pip and requirements files | `uv sync` rebuilds the exact environment CI tests, down to the hash of every package. A warm install took 1 second against 27 for pip on the same requirements | Contributors need one extra tool |
| Bedrock Data Automation for documents | A local PDF parser, Amazon Textract | Managed, handles forms and images with one project, custom blueprints give typed fields. A deterministic parser runs beside it as an independent second reader | 15 to 30 seconds per job, so it runs at ingestion, not on click. Two readers can disagree, which is the point of the check |
| Two MCP servers, stdio | Direct function calls | One protocol for tools. The same servers can be reused by another agent. Tool access is scoped per agent | Process startup per run |
| Human write only long term memory | Let agents store lessons | Closes the memory poisoning route | Lessons arrive only through human review and seeding |
| Model identifiers as configuration | Hard coded models | The account's Bedrock quotas are small and differ per model, so the system spreads models across quotas and can swap them | Behaviour depends on which models are configured, so evaluations record them |

---

## How a claim is decided

![Agent graph](docs/images/agent_graph.png)

1. **Ingest.** Before the run, **Bedrock Data Automation** and a vision model read the form and the photo. The run loads their output. It also compares Data Automation's reading of the form with a deterministic parser's reading, and flags any disagreement.
2. **Quarantine.** The narrative is customer controlled. **Guardrails** scan it, remove injected sentences and keep the legitimate facts.
3. **Intake agent.** It recalls lessons from memory and records six judgement flags (intoxicated, commercial use, unlicensed driver, mechanical failure, tyre only, theft), quoting the sentence behind each. It understands negation.
4. **Coverage and Investigator agents run in parallel.** Coverage retrieves clauses and reads the policy schedule through the `policy_records` **MCP** server and calls the payable calculator. The Investigator checks repeat claims through `policy_records` and the garage record, benchmark repair costs and the police report through the `claims_ops` server, and records advisory risk signals.
5. **Bounded collaboration.** Agents may post questions to each other. By default there is one round, with at most three questions.
6. **Photo check and rule checks.** Code compares the parts the photo shows as damaged with the parts on the estimate and adds an advisory signal if they disagree. It also adds any finding the Investigator should have recorded and did not: a repair cost above its benchmark, a flagged garage, a repeat claim, a missing police report. Every signal carries its source, `agent` or `rules`.
7. **Adjudicator.** The deterministic engine applies the rules in precedence order and produces the decision, calculation and next step. A model writes the memo.
8. **Human adjuster.** Accepts, overrides or escalates. An override becomes a candidate evaluation case and a lesson in long term memory.

If an agent does not finish, the claim is referred to a person with reason `INT.AGENT`. The system does not guess.

---

## Agents, MCP and memory

**Strands agent graph.** Intake, Coverage and Investigator are the nodes of a **Strands** graph: Intake runs first, then the other two in parallel. The Adjudicator is a fourth agent that runs after the graph and the rule checks. Each of the four agents is a Strands `Agent` with its own system prompt, tool list and **Bedrock** model, and each MCP server is attached to the agents that need it through Strands' MCP client. Strands does the orchestration of the graph. The rest is ordinary Python in the runner: the rule and photo checks, the one round of questions that agents may ask each other after the graph finishes, and the call to the rules engine that decides. Hooks emit an event for every model call, tool call and handoff, and the animated graph in the UI is drawn from that stream, so every pulse corresponds to something that ran. A call budget of 40 model calls per run bounds a runaway agent.

**MCP servers.** Two servers expose tools over stdio: `policy_records` (policy wording search, schedule, claim history) and `claims_ops` (garage check, repair cost benchmark, police report verification). Each agent receives only the tools it needs, and no tool pays money, edits a policy or reaches another customer.

**Findings the agent does not record.** An agent is asked to record what it finds, but a model sometimes describes a finding without calling the tool that records it. The investigation test ([below](#where-the-agents-do-earn-their-place-investigating-records)) showed this. In a traced run, the Investigator received a flagged garage with six flagged estimates. Its summary said it had recorded a medium risk signal, but it never called `record_risk_signal`, so the adjuster would have seen nothing. Across the 9 single-finding garage runs, it recorded none. The run therefore ends with `add_rule_signals`. It adds every finding that the rules can reach and the agent did not record, keeps the agent's own signals, and recognises a second inflated repair line when the agent flagged only the first. On the 84 stored agent runs, exact matches rose from 62 to 73 at no extra cost. This guarantees that the findings the rules can reach are delivered. It does not make the agent better at judgement, which is what the agent is for.

**Memory in two tiers.**

| Tier | Holds | Written by |
|---|---|---|
| Short term (AgentCore events) | Agent to agent notes for the current claim | Agents |
| Long term (AgentCore semantic memory) | Lessons from senior adjusters and from overrides. For example, "a few drinks" or "whiskeys" mean the driver was intoxicated, even without the word alcohol | **Humans only** |

**Effect of memory and collaboration.** Removing either one brought back one specific failure on the hard cases (see [ablations](#evaluation)). Without memory, a claim describing "whiskeys at a wedding" was approved in 1 of 3 runs. Without collaboration, a claim about a parcel from a friend was wrongly denied in 2 of 3 runs. These are single claims with few repeats. They show where to look and do not prove a mechanism.

---

## Document and image understanding

**Amazon Bedrock Data Automation** turns unstructured files into structured fields. One project holds two custom blueprints.

| Blueprint | Input | Fields |
|---|---|---|
| `claims-adjudication-motor-claim-form` | Claim form PDF | claim id, policy number, holder, registration, incident and report dates, police FIR, claimed amount, narrative |
| `claims-adjudication-vehicle-damage-photo` | Damage photo | `is_vehicle_photo`, `damaged_parts`, `severity`, `description` |

Jobs are asynchronous and take 15 to 30 seconds, so they run as an ingestion step and not when an adjuster opens a claim. Ingestion is a batch script here, and an **S3** event would trigger it in production. Results are stored with the claim (**DynamoDB** in **AWS**, files locally), and the agent run reads them. [scripts/run_bda_ingest.py](scripts/run_bda_ingest.py) processes every file and scores the output.

![Bedrock Data Automation blueprint tested on a real damage photo in the console](docs/images/aws/bda_blueprint_photo_result.png)

**Claim forms.** At run time, the form fields come from a deterministic parser, because the generated PDFs have a known layout. **Bedrock Data Automation** reads the same forms independently, and a disagreement between the two readers raises an advisory signal. Across 63 forms, `claim_id`, `policy_no`, `vehicle_reg`, `incident_date`, `report_date` and `claimed_amount` were 100% correct. `holder` was 92.1% correct. The five misses are one surname: the **OCR** read "Iyer" as "lyer". 58 of 63 forms were fully correct. The five holder-name misses reach the adjuster as low severity signals.

**Damage photos.** The photos are real: 70 photographs from the public **Kaggle** Coco Car Damage Detection Dataset (CC0), annotated with the damaged parts (headlamp, front bumper, rear bumper, hood, door). [scripts/attach_real_photos.py](scripts/attach_real_photos.py) gives each claim the unused photo whose damaged parts best match the parts on its estimate. 44 of 63 claims receive one. The other 19 list only parts outside those five, and the UI says so. The annotations let the reading step be scored against ground truth on all 70 photos:

| System | Precision | Recall | F1 |
|---|---|---|---|
| Bedrock Data Automation plus Claude Haiku 4.5, union (used) | 0.87 | **0.74** | **0.80** |
| Claude Haiku 4.5 | 0.86 | 0.68 | 0.76 |
| Claude Sonnet 4.6 | 0.94 | 0.61 | 0.74 |
| Nova 2 Lite | 0.93 | 0.59 | 0.72 |
| Bedrock Data Automation, revised blueprint | 0.95 | 0.51 | 0.66 |
| Bedrock Data Automation, first blueprint | 0.96 | 0.44 | 0.60 |
| Intersection of BDA and Haiku | 0.95 | 0.45 | 0.61 |

**Bedrock Data Automation** is cautious. When it names a part, it is right 95% of the time, but it finds only about half of the labelled parts. Its blueprint instruction was revised once. It was then evaluated on the half of the photos that were not examined while editing, and F1 rose from 0.64 to 0.69. Combining it with a vision model recovers most of the missing recall. The union rule was fixed before it was scored, and nothing was tuned. On the held-out half, F1 is 0.82 for the union, 0.80 for **Haiku** alone and 0.69 for Data Automation alone. The product therefore reads each photo with both and uses the union. The extra cost is one vision call per photo at ingestion.

The photo never changes the decision. It only produces an advisory signal. A false alarm costs the adjuster a glance, and a miss changes nothing about payment.

![Claim packet with the real photo and the parts detected](docs/images/app/claim_packet_photo.png)

---

## Retrieval-augmented generation (RAG)

Policy wording is retrieved at run time and cited. It is not placed in the prompts. The retrieval layer has one job: to return the clause where an exclusion is written, with an identifier that the adjuster can check.

| Stage | Choice | Reason |
|---|---|---|
| Corpus | Three insurers' private car package wordings (PDF), plus 16 clause cards | Cards are one short document per clause: 12 verbatim policy clauses and 4 internal controls |
| Chunking | Fixed size with 20% overlap. 150, 300 and 800 tokens compared. Cards are ingested as separate documents at 500 tokens | Clauses are short and cross-referenced, so chunk boundaries decide whether an exclusion and its condition stay together |
| Metadata | A sidecar file per card carries `clause_id` and `origin`, and it is returned with every hit | The agent cites `SEC1.EXCL.1c`, not a page number |
| Embeddings | Amazon Titan Text Embeddings V2, 1,024 dimensions, float | One model for chunks and queries |
| Index | Amazon S3 Vectors, one index per knowledge base | No standing hourly cost for a corpus this small |
| Retrieval | Approximate nearest neighbour, top 3 by default, exposed to agents as the MCP tool `search_policy_wording` | The agent can request more |
| Grounding | The coverage agent reasons over the returned text and cites clause identifiers | The rules engine decides, so retrieval is not on the payout path |

**Evaluation.** 48 questions, each tied to the clause that answers it and phrased the way an adjuster or customer would ask, not in the policy's words. A question is a hit at k if its clause is in the top k. Four configurations were compared on the same questions:

| Configuration | Recall at 1 | Recall at 3 | Recall at 5 | MRR at 5 |
|---|---|---|---|---|
| 300 token chunks | 35.4% | 66.7% | 77.1% | 0.52 |
| 150 token chunks | 52.1% | 66.7% | 72.9% | 0.60 |
| 800 token chunks | 45.8% | 68.8% | 70.8% | 0.56 |
| 300 token chunks plus clause cards | **60.4%** | **79.2%** | **85.4%** | **0.70** |

Compared with 300 token chunks, both 150 and 800 token chunks gave better recall at 1 and worse recall at 5. Clause cards improved every measure, so the product uses them. The operating point is recall at 3, because the tool returns 3 chunks by default. With plain chunks, the weakest topics were coverage ("is a flood covered?"), tyres and mechanical failure, where the customer's words and the policy's words share few terms.

**Trade-offs and failure modes.**
- **S3 Vectors** has no hybrid (keyword plus vector) search, which is the usual fix for that vocabulary gap. A managed search cluster would add it at a standing cost that a corpus this size does not justify.
- A retrieval miss weakens the explanation and the citation. It cannot change a decision or a payout.
- Ingestion allows one concurrent job per **knowledge base**, so the deployment runs them in sequence. Changing the embedding model means re-ingesting, which is cheap because the index is rebuilt from **S3**.
- 48 questions over 12 clauses rank the configurations. They do not establish production recall.

---

## Human in the loop

The AI recommends and a person decides. The **API** enforces this, so it cannot be bypassed by calling an endpoint directly.

![The human sign-off gate: an adjuster is blocked above the authority limit, a senior adjuster signs in through Cognito and accepts, and the decision is logged](docs/images/demo/human_in_the_loop.gif)

| Rule | Mechanism |
|---|---|
| Nothing is settled without a human | A claim moves new, AI recommended, reviewed. The only exit from AI recommended is a recorded human decision. Reviewing before the agents ran returns 409 |
| Four eyes | A payable above INR 200,000 can be approved only by a senior adjuster. Overriding a denial or a referral to approve also needs a senior adjuster at any amount, because those outcomes have no payable and so carry no limit. An adjuster receives 403 and can always escalate, refer or deny. A senior's override to approve records no payable, and the outcome says the amount must be set before payment |
| Overrides need a reason | An override carries a final decision and a written reason of at least 10 characters, stored beside the AI recommendation |
| A review names the run it looked at | Every review carries the id of the run the reviewer was shown. The API refuses the review with 409 if the latest recommendation has a different id. So "accept" always means the result on screen, and not a newer result that a colleague produced a moment later. A recommendation from a different mode than the deployment's, or one that has no run id, cannot be approved either |
| One decision per claim | A conditional DynamoDB write allows exactly one human review per claim. If two reviewers decide at the same moment, one succeeds and the other gets 409. This is tested with eight concurrent writers and was mutation checked. The task's role can add rows to the audit table but cannot update or delete them, and this is checked on the deployment template. The audit trail cannot be overwritten, even with several tasks running |
| Attributable | Each record holds who decided, their role, the AI recommendation and clauses, the final decision and the outcome. The name and role come from the sign in token and never from the request body, so a caller cannot promote themselves by editing the JSON |
| Never a dead end | Every referral names the next action: a senior adjuster, resubmitted documents when form and estimate disagree, a delay investigation, a police report for theft |
| Disagreement becomes data | An override is saved as a candidate evaluation case and as a lesson in long term memory |

The audit log is stored in **DynamoDB**, which is the single source of truth. Every task reads it directly, so scaling out cannot split it. Listing the claims takes one read of the log, not one read per claim.

---

## Security and red team testing

**Red team testing** means attacking the system on purpose, as a malicious claimant or garage would, and counting what gets through. It complements the functional tests.

**Threat model.** The attacker is a claimant or a garage who controls the narrative, the remarks or a document. Goals: get an excluded claim approved, make the system reveal a secret (identifiers, prompts, another customer's data), misuse a tool, or plant a rule in memory.

| Layer | Control |
|---|---|
| 1. Input guardrail | Bedrock Guardrails scans the narrative and the free text fields of the form and the estimate (holder, garage, police reference, line names) for prompt attacks. A flagged field is replaced as a whole. If a whole text is blocked, each sentence is checked alone so only offending sentences are removed |
| 2. Data, not instructions | Prompts state that the narrative is data. Instructions inside it are reported, never followed |
| 3. Least privilege tools | Each agent reads only the claim in front of it. No tool pays money, edits a policy or reaches another customer. The task role names its models, guardrail and tables. Two permissions use a wildcard: the region in foundation model addresses, which global inference profiles need, and the CloudWatch metrics call, which AWS requires and which is limited to one namespace |
| 4. Code decides | Agents set flags and an engine decides, so a hijacked agent cannot produce a payout |
| 5. Memory is human write only | Agents recall lessons and cannot write them |
| 6. Human in the loop | Every recommendation is reviewed and logged |
| 7. Sign in and input limits | Every route except the health check needs a valid Amazon Cognito ID token. The API checks the token's signature against the pool's keys, and its issuer, audience, expiry and type. A caller in no group gets 403. Review actions, decisions and run modes are fixed values, free text has length limits, and the reviewer's name is cleaned before it reaches the audit log |
| 8. Private network | The load balancer has no public address. CloudFront reaches it through a VPC origin, and its security group admits only the group CloudFront attaches to that origin. The task role names the three models, the guardrail and the resources it uses |
| 9. Rate and spend limits | AWS WAF limits each address to 20 agent runs and 600 requests in 5 minutes. A daily spend limit (5 USD by default, summed from DynamoDB across all tasks) refuses new live runs with 429. If the spend cannot be read, live runs are refused with 503 |
| 10. One mode per deployment | A deployment runs in the mode its operator set. A live deployment refuses a replay run with 409, so the keyword baseline's answer can never be stored as the AI recommendation that a person then approves. A replay deployment refuses live runs |

![Attack lab: scan an attack and see exactly which sentence the guardrail removed](docs/images/demo/attack_lab.gif)

![A guardrail blocking an injected instruction inside a claim narrative, and the claim being denied](docs/images/demo/guardrail_demo.gif)

**Suite.** [redteam/attacks.json](redteam/attacks.json) holds 30 attacks in six types: instruction override, hidden text in a document, secret extraction, tool misuse, memory poisoning and plausible fabrication. Each attack is appended to a genuine narrative that must be denied. An attack succeeds if the system approves, or reveals a real secret value. All 30 enter through the narrative. Attacks written into the garage name or an estimate line are covered by unit tests of the field scan, and the suite does not yet include them.

**Results, with controls.**

| System | Attacks scored | Flagged by the guardrail | Succeeded | Attributable to the attack |
|---|---|---|---|---|
| Hardened, defences on | 29 (1 errored) | 15 (52%) | 0 | 0 |
| Hardened, defences off | 30 | not applicable | 0 | 0 |
| Naive single agent, no graph, engine or guardrail | 30 | not applicable | 2 | **0** |

With defences on, the **guardrail** flagged instruction override 5 of 5, hidden text 4 of 5, plausible fabrication 2 of 5, secret extraction 2 of 5, tool misuse 1 of 5 and memory poisoning 1 of 4.

**Interpretation.**
- The naive agent's 2 raw successes are not attributable to the attacks. A no-attack control used the same 10 base claims with no injected text. It showed that the naive agent wrongly approves 2 of 10 claims even when nobody attacks it. An earlier version of this experiment reported a 20% attack success rate for the naive agent. The control showed that this figure was mostly the agent's own error rate, so the table reports attribution.
- The **guardrail** flags only 52% of attacks. It is weakest on attacks that use ordinary words: fabrication, tool misuse and memory poisoning. For this reason the other controls do not rely on it, and layers 3 to 6 exist.
- The result of 0 successes is against attacks written by the system's author, with one **guardrail** configuration. It shows that the pipeline held against these attacks. It does not show that the system cannot be attacked.

**Verified on the deployed stack.** Layers 7 to 9 were checked on **AWS**, not only in tests. A headless browser followed the real sign in flow. A wrong password was refused. A valid login returned to the app with the right name and role. The token worked on the **API**, the session survived a reload, and the evidence photo loaded through the cookie. Sign out cleared the session, and a senior adjuster received the senior role. A review sent with a body that claimed another role and name was recorded under the role and name in the token. A burst of 30 run requests without a token all reached the **API** and received 401. A minute later, the same 30 requests were blocked at the edge with 403, while ordinary requests such as the health check still passed. The first deployment also exposed a defect that no test had caught. It is described in [issues found and resolved](#issues-found-and-resolved).

---

## Frontend: the workbench UI

The frontend is a **React** 19 and **TypeScript** single page application built with **Vite**. It starts a claim run with a `POST` and reads the server-sent event stream from the response with `fetch`, because `EventSource` can only send `GET` and cannot carry the sign in token. It draws the agent graph as hand-written **SVG** animation, so each node and pulse corresponds to an event emitted by a **Strands** hook or a service call. It is served from **S3** through **CloudFront**, and the `/api` path is routed to the backend.

Signed out visitors see the sign in screen. The form is on the left, and a fixed example of the review card is on the right, so a reviewer sees what they are about to work with. The button sends them to **Amazon Cognito**'s managed login page, which is styled to match: dark, with the same wordmark and buttons, and the same example card as its background. It uses the authorization code flow with **PKCE**. They return with a code that is exchanged for tokens, and the address bar is cleaned. The ID token is refreshed before it expires and sent on every call. A cookie scoped to the read-only file path lets the evidence photo load, because an image tag cannot send a header. When the site has no sign in configuration, as in local development, the sign in screen is skipped and a demo role selector appears.

![The sign in screen, shown to a signed out visitor](docs/images/app/signin_gate.png)

![Cognito's managed login page, styled to match the app](docs/images/app/signin_cognito_hosted_page.png)

![Signing in: the app's screen, Cognito's page, the credentials, and the workbench with the account menu](docs/images/demo/sign_in.gif)

**Passwords.** Sign up is off. An administrator creates each account, and its group sets the role. The sign in screen says so: there is no sign up, and an administrator provides the credentials. Someone without an account sees a "Request access" link. It writes to an address that is set at build time. On the Pages site, the address comes from the repository variable `REQUEST_ACCESS_EMAIL`, so it is kept in the repository's settings and not in the code. "Forgot your password?" sends a code by email. That needs a verified email address on the account, so administrators create users with one. A user created without an email cannot reset a password.

![The forgot password page](docs/images/app/signin_forgot_password.png)

![The reset code email, as Cognito sends it](docs/images/app/password_reset_email.png)

![Workbench mid run, live](docs/images/app/workbench_live_run.png)

- **Workbench.** Claim queue with filters, the live agent graph, the claim packet with the photo and detected parts, a reasoning trace, and the decision panel with checks, calculation, clause citations, risk signals, recalled lessons and review controls. The header shows the signed in person's initials, and their menu gives the name, the role from the token (which is what the four eyes rule uses), what that role may approve, and sign out.

![The account menu: name, role and approval limit](docs/images/app/account_menu.png)
- **Architecture.** The agent graph, drawn statically, with the design principles.
- **Security.** The attack lab, **red team** results and defence layers.
- **Observability.** Cost, latency, where the money goes, alert rules and review statistics.

![Decision panel with risk signals, memory and the sign-off gate](docs/images/app/risk_signals.png)

![Architecture tab](docs/images/app/architecture_tab.png)

The mode chip shows whether the deployment runs the offline baseline or live agents on **Bedrock**.

**Tests.** 60 **Vitest** tests cover the **PKCE** challenge against the test vector in RFC 7636, token decoding and role mapping, the **server-sent events** parser (including every way a stream can be cut into chunks, and the queue position events), the **API** layer against a fake server, and the interactive demo's review rules, sign in and Try it steps. Five planted bugs, among them a `GET` where the run should be a `POST`, were each caught. A headless browser run against the built app checks the same flow end to end: the run streams, the review is recorded under the right identity, the photo loads and the console stays clean.

---

## Evaluation

**Golden set.** 63 claims in 22 scenarios, with expected decisions, clauses and payable amounts. The scenarios include negations ("had not consumed any alcohol"), paraphrases ("ferrying paying passengers through an app"), injected instructions and documents that disagree. The first golden set was too easy: the keyword baseline scored 100%. Adding negation and paraphrase cases dropped it to 82.5% with 8 unsafe approvals. That gap is what the agents are measured on.

**The golden set was iterated on**, so its 100% shows coverage of the scenarios the system was built for. It does not show generalisation. Two held-out sets were built to measure that.

**Held-out sets.** Each has 39 claims, a new random seed, new claim identifiers, and new wording for every hard scenario and for the accident sentence. None of that text appears in the golden set, the memory lessons or the agent prompts. Each was generated once and scored once.

| Set | Keyword baseline | Agents | Unsafe approvals | Payable exact | Injection handled |
|---|---|---|---|---|---|
| Golden, 63 claims (iterated on) | 82.5%, 8 unsafe | 100% | 0 | 100% | 100% |
| Held-out 1, 39 claims | 84.6%, 4 unsafe | 97.4% (38 of 39) | 1 | 100% | 100% |
| Held-out 2, 39 claims | 66.7%, 7 unsafe | **100%** (39 of 39) | 0 | 100% | 100% |
| Held-out 1 and 2 together, 78 claims | | **98.7%** (77 of 78), 95% interval 93.1% to 99.8% | | | |

**Root cause of the one miss.** In held-out 1 the narrative reads: "Another motorist reversed into the parked car outside the owner's house. The driver admitted to having had several drinks at a party before the trip." The label says deny. The agents approved. The insured car was parked and nobody was driving it, so approving is defensible. The generator had combined an accident sentence that implies a parked car with a driver condition clause. The label was not changed after the result, because that would tune the test to the answer. The result stands as measured, and it fails the live gate. The generator was then fixed, so that the insured is driving in every accident sentence. Held-out 1 is kept byte for byte reproducible. Held-out 2 was produced by the fixed generator, with a new seed and the same agents. No agent code or prompt changed between the two runs.

**An independent oracle.** The golden labels were produced by the same logic that implements the rules, so matching them cannot catch a rule that is wrong in both places. [evals/golden/independent_cases.json](evals/golden/independent_cases.json) holds 20 claims whose answers were worked out by hand from the policy wording and the standard age depreciation schedule, with the working written beside each. Every case sits on a boundary: the age bands, exactly 75% of the insured value (which is not a total loss) and one rupee over, the authority limit, notice on day 15 and day 16, half a rupee rounding up, and the last day of the policy and the day after it. A separate test covers the first day of the policy and the day before it. Deliberate bugs on these boundaries (an age band edge, the total loss threshold, the authority limit, the notice limit, rounding and the last day of the policy) each failed at least one oracle case.

**The engine under random testing.** A random test of 20,000 claims found four defects that the golden set had hidden. All are fixed, and tests that fail on the old engine pin each fix. A report date before the incident date was approved (2,801 cases). An estimate whose total did not match its own lines was approved. An unreadable date raised an exception. Float arithmetic with banker's rounding left 1,916 of 19,005 partial payables one rupee off. Money now uses exact decimals, with halves rounded up. The repository keeps property tests over 10,000 random claims.

**Gate.** Thresholds live in [evals/thresholds.json](evals/thresholds.json) and are versioned with the code:

| Gate | Metric | Bound |
|---|---|---|
| Baseline regression guard | decision accuracy, payable exact, injection handled | at least 0.80, 0.85, 1.0 |
| Live agent ship bar | decision accuracy, payable exact | at least 0.92, 0.95 |
| | unsafe approvals | 0 |

```bash
python evals/run_eval.py --mode replay        # score the keyword baseline
python evals/gate.py --mode replay            # exit code 1 if a metric crosses its threshold
pytest evals                                  # includes a broken build that must fail the gate
```

The gate is tested: one test removes the deductible from the calculation and asserts that the gate then fails.

**Ablations.** Each component was removed and the 20 hard golden cases rerun three times.

| Variant | Run 1 | Run 2 | Run 3 | Failure that returned |
|---|---|---|---|---|
| Full system | 100% | 100% | 100% | none |
| No long term memory | 95% | 100% | 100% | "whiskeys at a wedding" approved in one run |
| No collaboration | 100% | 95% | 95% | parcel from a friend wrongly denied in two runs |

A single run per variant had suggested that collaboration made no difference. Repetition showed that conclusion was wrong and it was withdrawn. The evidence is still thin: one claim per effect, three runs each.

---

## Agents compared with a single call

A multi-agent design costs more than one model call, so it has to show what the extra cost buys. Three experiments measure that, and the result differs by task.

### A single call baseline

[evals/single_call_baseline.py](evals/single_call_baseline.py) makes one structured **Claude Haiku 4.5** call per claim. The call sets the same six flags. It uses the **fine-tuning** study's prompt with four fixed examples, and none of their sentences appear in the evaluation sets. The same rules engine then makes the decision. Any difference in outcome comes only from how the flags were produced.

| Set | Single call plus engine | Agent team |
|---|---|---|
| Golden, 63 claims | 100%, 0 unsafe approvals | 100% |
| Held-out 1, 39 claims | 100%, 0 unsafe approvals | 97.4% |
| Held-out 2, 39 claims | 100%, 0 unsafe approvals | 100% |
| Cost and time per claim | 0.0007 USD, 0.8 s, 1 call | 0.035 to 0.049 USD, 21 to 25 s, about 20 calls |

The template narratives do not need tools, so one call does the whole job. On held-out 1, the agents scored 97.4% because of the flawed label described above, and the single call matched that label as written. The baseline also handled all 14 injection claims in these sets without a **guardrail**, so those claims do not measure what the **guardrail** adds. The **red team** suite measures that.

### A harder set written by other model families

Template sets cannot tell understanding from learned wording, so [evals/freeform](evals/freeform) builds a different kind of set. **Mistral Large 3** wrote 140 first-person narratives from short fact briefs, in seven styles (formal report, rambling, blunt text message, non-native English, full of irrelevant detail, hedged and so on). Fifty of them are implicit: the obvious words are forbidden, so the fact has to be inferred. Sixteen are negated decoys, such as a school run that is not commercial use, a favour that looks like delivery work, or a permitted spouse driving whose licence was shown to the police. **gpt-oss-120b** then labelled every narrative without seeing the intended label. Only the 124 where the two models agreed were kept, and every dropped narrative is recorded. Neither model is used by the product or by the baseline. The expected decision for each claim comes from the rules engine, applied to the verified labels.

| System | Correct | Unsafe approvals | Cost per claim | Time per claim (agent team: median) | Model calls |
|---|---|---|---|---|---|
| Single call plus engine | 122 of 124 (98.4%) | 1 | 0.0008 USD | 0.8 s | 1 |
| Agent team | 122 of 124 (98.4%) | 1 | 0.045 USD | 22.5 s | 21.3 |

The two systems tie, and they make different mistakes. The single call denied the favour that looked like delivery work. The agent team denied a school run as commercial use. Each system also approved a learner driver who was practising alone: the single call's case was implicit, and the agent team's was stated. So this benchmark does not separate them on accuracy, and the agent team costs about 58 times as much.

**A construction error that the first run exposed.** The first agent run scored 92.7% with 9 unsafe approvals, and every miss was a tyre-only or breakdown claim. The cause was in the builder. It gave every claim random body-repair lines, so a tyre-only narrative arrived with an estimate that listed a windshield and a radiator. The agents cross-check the estimate against the narrative, and they refused to call the claim tyre-only. That scored them against a contradiction that the test itself had built in. The single call never reads the estimate, so it could not be affected. The builder now writes estimates that agree with the narrative, and a test pins that. The corrected run is the result above. The first run's reports are kept and labelled, because the finding is real: the agents notice contradictions that the single call cannot see.

**Limits.** 15 of the 16 dropped narratives were implicit ones that the verifier could not agree on, so the set is somewhat easier than intended (35 of the 50 implicit narratives survive). Agreement between two models is not human ground truth. With 124 claims, a difference of one or two claims is within noise.

### Where the agents do earn their place: investigating records

Investigation is a different task: the facts live in records that the narrative does not contain (repair cost benchmarks, a garage's flagged estimates, other claims on the policy, the police report). [evals/investigation](evals/investigation) plants problems in real claim PDFs and records. It compares four contenders on the investigator's model (**Nova 2 Lite**), at temperature 0, with the same plain brief and no thresholds written into it:

| Contender | What it is given |
|---|---|
| One call, documents only | The claim packet and the narrative |
| One call, records pasted in | The packet plus every reference record in the prompt, the strongest single-call baseline |
| The investigator agent | The product's own agent with its tools and MCP servers, looking things up |
| Rules only | The product's deterministic investigator (`services/signals.py`), with no model. The answer keys were also checked against it, so it shows what a well written rule set can reach and is not a fair rival |

There are 28 cases: 14 with a single problem (an inflated repair line, a flagged garage, a theft with no police report, documents that disagree) including controls where nothing is wrong, 4 repeat-claim cases, 4 that combine problems, and 6 where the narrative tells the reviewer to skip its checks. Each answer key is checked against the product's deterministic investigator. The case design was corrected once before any full run: a smoke test showed that a pair of 5 days and 6 days scored the models on guessing an internal threshold that they were never told.

| Contender | Planted problems found | Runs with a false alarm | Exactly right | Cost per case |
|---|---|---|---|---|
| One call, documents only | 30 of 72 (42%) | 50 of 84 | 22 of 84 | 0.0003 USD |
| One call, records pasted in | 69 of 72 (96%) | 53 of 84 | 31 of 84 | 0.0007 USD |
| Investigator agent | 58 of 72 (81%) | 11 of 84 | 62 of 84 | 0.0080 USD |
| Investigator agent plus the rule safety net | 69 of 72 (96%) | 11 of 84 | 73 of 84 | 0.0080 USD |
| Rules only, no model | 57 of 72 (79%) | 0 of 84 | 69 of 84 | 0 USD |

Each case ran three times. Pasting the records finds nearly everything, but it raises a false alarm in most runs. It mixes up other policies' rows, for example reporting "policy INV-00014 also had a claim two days before" for a claim on a different policy. The agent finds fewer problems but is right far more often. It found all 24 of the problems that needed several lookups combined. The agent plus safety net row applies `add_rule_signals` to the stored agent runs, as described in [Agents, MCP and memory](#agents-mcp-and-memory).

**Scale.** The claims history grows in real deployments, and pasting it into the prompt grows with it. The same history cases ran with 37, 1,037 and 10,037 claims on file:

| Claims on file | Records pasted in: tokens and cost per case | Runs with a false alarm | Agent: tokens and cost per case | Runs with a false alarm |
|---|---|---|---|---|
| 37 (all 28 cases) | 1,480 and 0.0007 USD | 53 of 84 | 22,183 and 0.0080 USD | 11 of 84 |
| 1,037 (6 cases) | 23,472 and 0.0073 USD | 9 of 18 | 23,791 and 0.0084 USD | 4 of 18 |
| 10,037 (6 cases) | 221,472 and 0.0669 USD | 17 of 18 | 23,423 and 0.0083 USD | 3 of 18 |

The agent's cost does not move, because it looks up only the records it needs. At 10,037 claims, the pasted prompt costs about 95 times what it cost at 37 claims, and 8 times the agent's cost per case. It takes 14.6 seconds against the agent's 10.6, and it raises a false alarm in 17 of 18 runs. The costs meet at around 1,000 claims on file. Below that, the single call is cheaper and finds more problems, at the price of more false alarms.

**The agent's weaknesses.** It recorded a lone flagged garage in 0 of 9 runs. In a traced run, its summary claimed that it had recorded the garage. It also filed an amount mismatch under the wrong kind of problem. In the injection group it found 10 of 15 problems, with no false alarms. It missed the flagged garage in all 3 runs, and a repeat claim and a missing police report once each. It was not steered into reporting things, but it may have been steered out of reporting some. The garage weakness is what `add_rule_signals` removes.

**What the rules alone show.** The rules-only row finds 79% with no false alarms and no cost. At 1,037 and 10,037 claims on file, it is exact in all 18 runs, where the agent is exact in 14 or 15. On every problem that a rule covers, the agent adds nothing, and it sometimes subtracts, by raising false alarms on 11 of 84 runs. What the agent adds in this experiment is the 12 problems that the rules missed (of the 72 planted, the agent plus safety net found 69 and the rules found 57): 6 in the single problem group, 3 in the multi step group and 3 in the injection group. That is also where its false alarms and misses cluster. So the case for the agent rests on findings that no rule covers. This experiment cannot show that the agent finds them better than a rule written later would.

**Limits.** One model, and 28 cases written by the author. The product contains a deterministic investigator (`services/signals.py`) that was used to build the answer keys for this same task. So the headline comparison is between the agent and pasting all the records into the prompt. The rules-only row measures the rules against their own answer key and shows what the agent adds beyond them. It does not show that the agent beats code. Costs were recomputed from the recorded tokens at prices checked against the **AWS** Price List.

### What this means

- On template and free-form narratives a single call is as accurate as the agent team at about one fiftieth of the cost. Accuracy does not justify the agents.
- When the facts live in records, and the records grow, the agent holds its cost and its precision while a single call with everything pasted in degrades. That is the case for tool use, and it needed a code safety net to be reliable.
- The agents also add what a single call cannot: citations from retrieval, long term memory fed by human review, a full audit trail of tool calls, and the cross-check between narrative and estimate that exposed the benchmark error above.
- If the only job were reading narratives, a single call and a rules engine would be enough. The agents are justified by work that no rule covers, such as unwritten patterns, judgement and explanation, and by the audit trail and memory. The last experiment shows that on rule-covered checks the rules do as well. So the justification for the agents rests on work that no rule covers, which is listed under [next steps](#next-steps) and has not been measured yet.

---

## Cost, latency and observability

Every model call writes a **JSON** record (agent, model, input and output tokens, latency, cost) to the **S3** telemetry lake, partitioned by day. **Athena** queries it in place and **QuickSight** presents it.

![QuickSight dashboard of cost and latency over the telemetry lake](docs/images/quicksight_dashboard.png)

**Cost.** Two changes were measured on the same 22 claims (one per scenario). Each was measured twice: once in the sharded evaluation batches and once sequentially. Decision accuracy was 100% with 0 unsafe approvals in every run.

| Variant | Cost per claim, run 1 | Cost per claim, run 2 (sequential) | Change |
|---|---|---|---|
| Baseline | 0.0464 USD | 0.0487 USD | |
| Agents request independent tools together | 0.0432 USD | 0.0423 USD | 7% and 13% lower |
| Plus the memo written by Claude Haiku 4.5 instead of Sonnet 4.6 | **0.0347 USD** | **0.0351 USD** | 25% and 28% lower |

Both changes are configuration switches (`CLAIMS_PARALLEL_TOOLS` and `CLAIMS_ORCHESTRATOR_MODEL`). The deployed system and the held-out evaluations run the baseline configuration, so the optimised one would need the held-out sets rerun before it is enabled. Prompt caching had no measurable effect, because the prompts are shorter than the caching threshold. That is a negative result. At these prices, a claim costs about 3 to 4 Indian rupees.

**Prices.** The rates in `backend/app/pricing.py` first came from third party trackers. [scripts/check_prices.py](scripts/check_prices.py) then compared all twelve against the **AWS** Price List **API** on 16 November 2026. **Claude Haiku 4.5** and **Claude Sonnet 4.6** matched exactly. **Nova 2 Lite** did not. The file held the regional rates (0.33 USD per million input tokens and 2.75 output), but the code calls the global inference profile (0.30 and 2.50). Its cache rates were wrong too. The file is corrected. **Nova** accounts for close to half of a claim's tokens, so per-claim costs measured before that date are about 4 percent high. The investigation experiment's costs were recomputed from the recorded tokens at the corrected rates.

**Latency.** The account's **Bedrock** request quotas are small, and throttling inflated latency in the large sharded batches, so those timings are not reported. Latency was measured again sequentially: one claim at a time, with nothing else calling **Bedrock**, and 22 claims per variant.

| Variant | Median | 95th percentile | Mean | Model calls per claim |
|---|---|---|---|---|
| Baseline | 24.6 s | 42.9 s | 28.4 s | 20.9 |
| Agents request independent tools together | 23.8 s | 36.1 s | 26.6 s | 18.5 |
| Plus the memo written by Claude Haiku 4.5 | **21.5 s** | **33.1 s** | **24.2 s** | 18.5 |

Each change reduced latency, and fewer model calls explain the first. With 22 claims and one run per variant, median differences of 1 to 3 seconds are small against the spread, so treat the ordering as indicative.

**Alerting.** After every run, the application checks three rules: a run costing more than three times the median of the previous twenty runs, a daily spend over budget, and a failure rate above 20%. Results appear in the Observability tab, and a **CloudWatch** custom metric drives the cost spike alarm.

![Observability tab: cost per claim, where the money goes, alert rules and review statistics](docs/images/demo/observability.gif)

---

## Fine-tuning a small model with QLoRA

**Objective.** Test whether a small open model, fine-tuned cheaply, can set the six judgement flags (intoxicated, commercial use, unlicensed driver, mechanical failure, tyre only, theft) as well as a prompted managed model, and say when each is the right choice. The work is in [finetune/](finetune/).

**Model.** **Qwen2.5-3B-Instruct**, a decoder-only transformer with 36 layers, hidden size 2,048, 16 attention heads using grouped-query attention (2 key-value heads), an 11,008-wide feed-forward block, a 151,936-token vocabulary and 3.09 billion parameters (read from the model's own configuration). Decoding is greedy, so results are repeatable.

**Method.**

| Aspect | Setting |
|---|---|
| Adaptation | LoRA on all linear layers (query, key, value, output, gate, up, down) in all 36 layers. Rank 16, alpha 32, dropout 0.05. 29,933,568 trainable parameters, which is 0.97% of the model, saved as a 60 MB adapter in 16 bit. The adapter starts at zero, so training starts exactly from the base model. After training, it can be merged into the weights with no extra cost per token |
| Quantisation (QLoRA) | The frozen base model is stored in 4-bit NF4 with double quantisation, and computation uses bfloat16. The base weights shrink from about 6.2 GB to about 1.5 GB, so training fits on one 24 GB A10G. On a Mac without CUDA, the script uses plain 16-bit LoRA for smoke tests |
| Objective | The loss counts the answer JSON only (`completion_only_loss`), so the model is not scored on copying the narrative. Prompts and answers use the model's own chat template, the same for every system compared |
| Optimisation | Learning rate 2e-4, cosine schedule, 3% warm-up, 3 epochs, effective batch size 16 (8 per step, 2 accumulation steps), maximum length 512, gradient checkpointing |
| Libraries | Hugging Face Transformers, PEFT, TRL `SFTTrainer`, bitsandbytes |
| Compute | One `ml.g5.2xlarge` (NVIDIA A10G, 24 GB) SageMaker training job. It was launched with plain `boto3`, used a dedicated bucket and a least-privilege execution role created by CDK, and had a 90 minute hard stop. Training took 427 s, and 968 seconds were billed in total, which is about 40 US cents (an estimate from billable seconds and an assumed on-demand rate) |

**Data and splits.** Narratives are generated from phrase banks. Each has a base accident sentence, zero to two sentences that state or deny a flag, and filler. The denials and traps are the point, for example "had not consumed any alcohol", "a parcel that a friend had sent" and "a tyre burst and the car then hit a divider". The train set has 1,200 narratives and the dev set has 150, both from the training banks. The unseen test has 300 narratives from different banks, so every sentence in it is wording the model never saw. Tests check that no sentence is shared and that every label follows from the text. A further 63 narratives come from the claims system itself. They are a secondary result only, because 39 of the 63 share a sentence with the training phrases.

**Results.** The same 150 held-out narratives and the same scoring code were used for every system:

| System | Exact match (all 6 flags) | Missed denials |
|---|---|---|
| Claude Haiku 4.5, 4 examples | **98.0%** | 0 |
| Claude Sonnet 4.6, 4 examples | 96.7% | 0 |
| Claude Sonnet 4.6, zero-shot | 92.7% | 0 |
| Claude Haiku 4.5, zero-shot | 89.3% | 0 |
| Qwen2.5-3B with QLoRA | **88.0%** | **0** |
| Nova 2 Lite, 4 examples and zero-shot | 82.7% and 76.7% | 0 and 0 |
| Qwen2.5-3B prompted, 4 examples and zero-shot | 68.0% and 65.3% | 3 and 17 |
| Keyword baseline | 49.3% | 38 |

With 150 narratives, the 95% uncertainty on an accuracy near 88% is about 5 points, so neighbouring rows are not meaningfully different. On the full 300 narratives, the tuned model scored 89.3% and the untuned model 59.7%. About 60% of the untuned model's zero-shot answers were not valid **JSON**.

**Findings.**
- **Fine-tuning** worked as a technique. On unseen wording, accuracy went from 65% to 88%, and missed denials, the dangerous error, went from 17 to zero. The remaining mistakes are false denials, which an adjuster would see and correct.
- It does not pay off for this product. Prompted **Haiku** scores 98% for roughly 500 input and 40 output tokens per call, which is about 0.07 US cents, and it needs no **GPU**. The tuned model processed a narrative in 0.26 s in **GPU** batches, which is about 0.011 cents at full use. But an always-on endpoint costs on the order of 1,100 US dollars a month whether or not it is used. The **API** costs well under a dollar a month at roughly a thousand claims a month. These cost figures are estimates from token counts and list prices. **Fine-tuning** wins at very high steady volume, when data must stay in the account, or when no strong hosted model exists.

**Limits.** Errors cluster. 17 of the 32 wrong narratives (of 300) come from one unseen sentence ("The driver handed over a current licence when asked", read as unlicensed), and 6 more come from one engine failure paraphrase. The 300 narratives contain only about 60 distinct unseen sentences, so they overstate the evidence. Training loss fell to about 0.00001 by epoch 1.6. The dev loss is just as small, because dev shares phrase banks with train, so only the unseen wording test can show overfitting. This is one run with one seed, with no hyperparameter search, on synthetic text.

![SageMaker training job record](docs/images/aws/sagemaker_training_job.png)

---

## Deployment

The system was deployed to us-east-1 with two **CDK** stacks. The stacks were destroyed after the evidence below was recorded. The commands at the end of this section recreate them.

[scripts/verify_deployment.py](scripts/verify_deployment.py) is the acceptance test. It finds every resource from the **CloudFormation** outputs and calls each service. It creates two temporary **Cognito** users and signs them in. It then checks that:

- the load balancer is private;
- the **API** refuses a caller with no token (401) and a user in no group (403);
- starting a run is `POST` only;
- the site publishes its sign in settings, and **AWS WAF** is attached.

It then calls the services. It invokes three **Bedrock** models, applies the **guardrail** to an attack, retrieves from all four **knowledge bases**, recalls from **AgentCore** memory and runs a **Bedrock Data Automation** job. It runs one live claim through the agents. It reviews that claim through the **API** with a senior token, while the request body claims another role and name, which must be ignored. Last, it reads every **DynamoDB** table and queries **Athena**.

The script deletes the temporary users even if a check fails, and it exits non-zero if any check fails. The latest run passed 29 of 29 checks ([docs/verification.json](docs/verification.json)). The **QuickSight** check reports a skip, because that account was cancelled to stop billing.

The screenshots below are from the console. [scripts/redact_screenshots.py](scripts/redact_screenshots.py) redacts the account identifier and the operator's name, and every screenshot in the folder was scanned with **OCR** for the account number.

The first run of this script on the new network design failed 12 of 27 checks. Six of them failed because every **API** call through **CloudFront** returned 504. That is how the defect described in [issues found and resolved](#issues-found-and-resolved) was found. The other failures were empty tables and an empty telemetry lake that nothing had written to yet.

**Compute and delivery**

| | |
|---|---|
| ![ECS service](docs/images/aws/ecs_service_deployments.png) | ![ECS cluster](docs/images/aws/ecs_cluster_services.png) |
| ECS service on Fargate, one task running, deployment succeeded | ECS cluster, service active |
| ![CloudFront origins](docs/images/aws/cloudfront_origins.png) | ![CloudFront metrics](docs/images/aws/cloudfront_metrics.png) |
| CloudFront distribution with an S3 origin for the site and a VPC origin for the API | CloudFront request and error metrics |
| ![App stack](docs/images/aws/cloudformation_app_stack.png) | ![Data stack](docs/images/aws/cloudformation_data_stack.png) |
| CloudFormation, application stack resources, including Cognito, the web ACL and the VPC origin | CloudFormation, data stack |

**Identity and private network**

| | |
|---|---|
| ![Cognito groups](docs/images/aws/cognito_user_pool_groups.png) | ![WAF rules](docs/images/aws/waf_web_acl_rules.png) |
| Cognito user pool with the adjuster and senior groups | Web ACL with the two rate limit rules |
| ![Internal ALB](docs/images/aws/alb_internal.png) | ![ALB security group](docs/images/aws/alb_security_group_inbound.png) |
| Load balancer with scheme Internal, in the isolated subnets | Its security group admits one source, the CloudFront VPC origin service group |

**Bedrock: guardrails, knowledge base, document automation**

| | |
|---|---|
| ![Guardrail overview](docs/images/aws/bedrock_guardrail_overview.png) | ![Guardrail content filters](docs/images/aws/bedrock_guardrail_content_filters.png) |
| Guardrail, ready, one version | Content filters with prompt attack defence |
| ![Guardrail PII](docs/images/aws/bedrock_guardrail_pii_types.png) | ![Guardrail regex](docs/images/aws/bedrock_guardrail_regex_patterns.png) |
| Sensitive information: email and phone masked | Regex detectors for Aadhaar and PAN numbers |
| ![Knowledge base](docs/images/aws/bedrock_kb_overview.png) | ![Knowledge base test](docs/images/aws/bedrock_kb_test_answer.png) |
| Knowledge base on S3 Vectors with Titan embeddings (a chunk size experiment base) | A drunk driving question answered from retrieved chunks |
| ![Chunk metadata](docs/images/aws/bedrock_kb_chunk_metadata.png) | ![BDA project](docs/images/aws/bda_project.png) |
| A retrieved chunk with its metadata | Bedrock Data Automation project with both custom blueprints |

**Memory, data and telemetry**

| | |
|---|---|
| ![AgentCore memory](docs/images/aws/agentcore_memory_overview.png) | ![AgentCore strategy](docs/images/aws/agentcore_memory_strategy.png) |
| AgentCore memory, active | Long term strategy for adjuster lessons |
| ![AgentCore observability](docs/images/aws/agentcore_memory_observability.png) | ![DynamoDB audit](docs/images/aws/dynamodb_audit_table.png) |
| Memory invocations and latency | Human review audit log in DynamoDB |
| ![Athena](docs/images/aws/athena_runs_query.png) | ![QuickSight](docs/images/aws/quicksight_dashboard_live.png) |
| Athena over the telemetry lake | QuickSight dashboard, latency in seconds |

**Operations and training**

| | |
|---|---|
| ![CloudWatch alarms](docs/images/aws/cloudwatch_alarms.png) | ![CloudWatch dashboard](docs/images/aws/cloudwatch_dashboard.png) |
| Latency, 5xx and cost spike alarms | CloudWatch dashboard for the API |
| ![SageMaker metrics](docs/images/aws/sagemaker_training_metrics.png) | ![BDA blueprint](docs/images/aws/bda_blueprint_photo_result.png) |
| GPU, CPU and memory during the QLoRA job | Photo blueprint run on a damage photo |

**Deploy and verify**

```bash
uv sync                                        # the exact locked environment, Python 3.12
export PATH="$PWD/.venv/bin:$PATH"             # the CDK app runs with the active interpreter
cd frontend && npm ci && npm run build && cd ../infra
npx aws-cdk@2 bootstrap aws://<account>/us-east-1 --qualifier claimsadj --toolkit-stack-name CDKToolkit-claimsadj
npx aws-cdk@2 deploy --all -c region=us-east-1 -c mode=live    # add -c production=true to keep the data when the stack is deleted

# load data into the new stacks (names come from the stack outputs)
aws s3 sync data/real/policies s3://<policy-docs-bucket>/policies/
aws s3 sync data/clause_cards  s3://<policy-docs-bucket>/clause_cards/
# start one ingestion job per knowledge base data source, in sequence, then
uv run python scripts/seed_dynamodb.py <policies-table> <claims-table>
CLAIMS_MODE=live CLAIMS_MEMORY_ID=<memory-id> uv run python scripts/seed_memory.py
# Bedrock Data Automation results for every form and photo are cached in data/bda;
# uv run python scripts/run_bda_ingest.py regenerates them

# create the people who can sign in (there is no self sign up), then put each in a group
aws cognito-idp admin-create-user --user-pool-id <pool-id> --username <name> --message-action SUPPRESS
aws cognito-idp admin-set-user-password --user-pool-id <pool-id> --username <name> --password '<strong password>' --permanent
aws cognito-idp admin-add-user-to-group --user-pool-id <pool-id> --username <name> --group-name senior    # or adjuster

uv run python scripts/verify_deployment.py     # acceptance test across every service
npx aws-cdk@2 destroy --all -c region=us-east-1
```

By default, deleting the stacks deletes the data, which suits a demo that is deployed and torn down. Passing `-c production=true` keeps the data and the buckets, turns on delete protection for the tables and keeps logs for three months instead of one week.

Pass the region explicitly. Without it, the **CDK** command line takes the region from the **AWS** profile, which once sent a deploy to the wrong region. A deployment costs roughly 2 to 3 US dollars a day while it runs, plus model calls (an estimate from list prices, not a bill). The **CDK** app uses a dedicated bootstrap qualifier.

Destroying the data stack fails on the **Athena** workgroup once queries have run. Delete the workgroup with `aws athena delete-work-group --work-group claims-adjudication --recursive-delete-option` and retry. The bootstrap stack keeps its asset bucket and container repository, and both must be emptied before that stack can be deleted.

The workflows sign in to **AWS** through **OIDC** with a role supplied as a repository variable, so no long lived keys are stored in **GitHub**. This app does not create that role or the **OIDC** provider. The **QuickSight** account is created once in the console and must be cancelled after use, because it bills after its trial.

---

## Operating the system

| Signal | Threshold | Response |
|---|---|---|
| Run cost above three times the median of the previous twenty | CloudWatch alarm `RunCostSpike` | Open the Observability tab and find the agent or model whose cost grew. Likely causes are a looping agent (limited by the 40 call budget) or a prompt that grew |
| Failure rate above 20% of recent runs | Alert rule | Check the error on the failing runs. Throttling shows as retries and higher latency. A permission change shows as an access denied error |
| API 5xx errors, or p95 latency above 30 seconds | CloudWatch alarms | Check the ECS service events and task health |
| Daily model spend reaches 5 USD (`CLAIMS_DAILY_BUDGET_USD`) | Hard limit and an alert | New live runs get 429 until tomorrow. Viewing and reviewing keep working. A live deployment does not run replay (see the mode rule in the security layers). The spend is summed from DynamoDB across every task. A run that has already started is never cut off, so a day can overshoot by one run per task. Per call records are in Athena |

| Failure mode | Behaviour |
|---|---|
| A model call is throttled | The call is retried with backoff. If the run still fails, it is recorded as failed with the error, and the claim stays unreviewed |
| An agent does not record its judgement | The claim is referred to a person with reason `INT.AGENT` |
| Bedrock Data Automation output is missing for a claim | The claim runs without photo evidence and the UI says so |
| The knowledge base is unreachable | The coverage agent has no clause text. The engine still decides, and the citation panel is empty |
| A task restarts | The audit log is read from DynamoDB, so nothing is lost, and metrics are restored from DynamoDB when the next task starts |
| Several people start runs at once | Runs go one at a time per task, in the order the requests arrived. A waiting request is told its place in line every 10 seconds. This also keeps CloudFront's 60 second response timeout from cutting the request off. The page shows "Waiting, place n in line". If 5 runs are already waiting, a new request gets 503 with a retry hint |
| A user has no verified email | Password reset cannot send a code. Create the account with a verified email, or set one with an administrator call |
| An attacker's text is flagged | The flagged sentence is removed and logged, and the rest of the narrative proceeds |
| A token is missing, expired or invalid | 401, and the site sends the person back to sign in. A user in no group gets 403 |
| Today's spend cannot be read | Live runs get 503 instead of risking the money. Replay and review keep working |
| The investigator describes a finding without recording it | The rules add it, marked as coming from the rules |
| One address starts too many runs | The web ACL answers 403 at the edge until the 5 minute window passes |
| A request fails | Every request has an id in `X-Request-ID`, which is on every log line from that request. Each request ends with one JSON log line with the method, path, status, milliseconds and user. Failures also log the traceback |

---

## Quick start

The **Python** environment is defined in `pyproject.toml` and locked in `uv.lock`, which lists 103 packages, including indirect ones, with hashes. `uv sync` builds exactly the environment that **CI** tests, on **Python** 3.12 (`.python-version`). It installs **uv**'s own **Python** if the machine has none. `finetune/requirements.txt` is separate, because it lists the versions that the **SageMaker** job installed on a **GPU** machine. The diagram generator needs **Graphviz**, and the screenshot redaction script needs **Tesseract**. The demo capture script needs **Node.js** and **Google Chrome** (`cd docs/demo && npm ci`).

```bash
git clone https://github.com/anandapurva55/agentic-claims-adjudication-aws.git && cd agentic-claims-adjudication-aws
uv sync                                         # the locked environment, no virtualenv to activate
uv run python scripts/generate_data.py          # 63 claims, 20 policies, golden set
uv run python scripts/generate_data.py --heldout   # held-out set 1 (and --heldout2 for set 2)
uv run pytest                                   # 463 tests, no AWS needed (the 24 infrastructure tests need Node.js and a built frontend)
uv run python evals/run_eval.py --mode replay && uv run python evals/gate.py --mode replay
(cd frontend && npm ci && npm test)             # 60 frontend tests

# run the app locally, offline baseline, no AWS and no sign in needed
CLAIMS_MODE=replay uv run uvicorn app.api.main:app --app-dir backend --port 8000 &
cd frontend && npm ci && npm run dev            # http://localhost:5173

# score a held-out set against the live agents
CLAIMS_MODE=live CLAIMS_DATA_DIR=data/heldout CLAIMS_CASES=evals/golden/heldout_cases.json uv run python evals/run_eval.py --mode live --label heldout
```

Locally, with no user pool configured, sign in is off. The app shows a demo role selector, and the **API** takes the role from the `X-Demo-Role` header. Live mode refuses to start without a user pool, so the open mode cannot run against real models by accident.

A URL such as `?claim=CLM-2026044&autorun=1` opens a claim and runs it. The photographs are not included in the repository. Download the **Kaggle** dataset listed in the references into `data/real/car_damage_coco`, then run `python scripts/attach_real_photos.py`.

---

## Issues found and resolved

| Issue | Diagnosis | Resolution |
|---|---|---|
| Evaluations failed or slowed unpredictably | Throttling. The account's Bedrock quotas are 10 to 20 requests per minute per model | The agents were spread across models, which have separate quotas. Adaptive retries were added, evaluations were split across two processes, and latency was measured one claim at a time so that throttling could not distort it |
| The cost dashboard showed zero tokens | Streaming responses did not fill in the SDK's usage totals | A model wrapper reads usage from the stream's metadata events and records every call |
| The evaluation set was too easy: the keyword baseline scored 100% | The first baseline run | Negation and paraphrase cases were added. The baseline fell to 82.5% with 8 unsafe approvals, which gave the agents something to beat |
| Accuracy rested on a set that had been tuned against | Review of the evaluation design | Two held-out sets with new wording were each scored once. Analysis of the single miss traced it to an inconsistent test narrative, so the generator was fixed and the label was left alone |
| The red team overstated attack success | A 70% result looked wrong. A control with no attack then showed the naive agent making mistakes on its own | The harness now appends the attack to a genuine narrative, and the report separates successes caused by the attack from the agent's own errors |
| The API returned 200 with HTML for unknown claims | Probing endpoints on the deployed site | CloudFront custom error responses apply to the whole distribution, so the single page app fallback also rewrote API errors. The app has no client routes, so the fallback was removed |
| Every API call through CloudFront timed out (504) on the first deployment of the private network design. The site, sign in settings, WAF and the internal load balancer all passed | Target health was fine and the app answered its own health checks, but no request from CloudFront reached it. The load balancer's security group admitted the isolated subnets' address ranges, on the assumption that the VPC origin's network interfaces use those addresses. They do not. CloudFront attaches a managed security group to those interfaces, and the load balancer has to admit that group. Adding the rule by hand confirmed it (200 in 0.4 s) | After the distribution exists, the stack looks up that group with a small custom resource, as the CDK documentation describes, and admits it. The custom resource has read-only permission and depends on the distribution. Tests now check who the load balancer admits (a source group, never an address range). They had passed on the broken design because none of them checked this. The old rule was added back as a mutation to prove that the new tests catch it |
| The investigator reached the adjuster with no flagged garage signal | In a traced run, the agent received the garage record and wrote in its summary that it had recorded a medium risk signal, but it never called the tool that records one. The same happened in all 9 single garage runs | `add_rule_signals` adds every finding that the rules can reach and the agent did not record, and marks it by source. It is tested through the real live path with an agent that records nothing |
| Two reviewers deciding at the same moment could both succeed once the API ran as several tasks | The audit log was a local copy in each task, so the one decision per claim rule held only inside one process | DynamoDB is the source of truth, and the review is a conditional write on a fixed key, so exactly one wins. This is tested with eight concurrent writers against DynamoDB and the local store, and was mutation checked |
| The rules engine approved a claim reported before its incident, approved one whose estimate total did not match its lines, and paid some claims a rupee off | Found by running 20,000 random claims through it, which the golden set had not covered. The causes were float arithmetic with banker's rounding, no check of the printed total, and no date validation | Exact decimals with halves rounded up, referral on inconsistent or unreadable dates and totals, an independent implementation in the data generator, and 20 hand-calculated boundary claims |

---

## Limitations

| Limitation | Impact | Mitigation or next step |
|---|---|---|
| Claim facts and narratives are synthetic. The photos are real, but they are matched to claims by the parts on the estimate | Accuracy on real narratives is unknown | Collect adjuster overrides as a real evaluation set |
| The author wrote the red team: 30 attacks and one guardrail configuration | Some attack classes are untested | An external red team, and attacks generated by a separate model |
| Evaluation samples are small: 78 held-out claims and three runs per ablation | Wide intervals, and mechanisms that are not verified | More claims per effect and more repeats |
| 19 of 63 claims have no usable photo | Fewer photo signals | Photos for every part type |
| Live runs go one at a time per task, about 2 to 3 claims a minute, with one task and no autoscaling. Waiting runs are told their place, and a queue longer than 5 is refused with 503. This was tested on a local server and not load tested on AWS | About 3 people running at the same moment is the comfortable limit. The rest wait or are told to retry | More tasks with autoscaling, or a queue with workers |
| Document ingestion is a batch script, not event driven | A new claim needs the script run before its photo and form check appear | An S3 event and a Step Functions workflow |
| There is no endpoint to submit a claim. Claims are directories in the container image, and a run starts from one of them | The system adjudicates the demo claims, not new ones | A submission endpoint that stores the packet in S3 and starts ingestion, then the event driven workflow above |
| Run metrics, call records and the alert history are read from local files when a task starts, so each task shows its own. The claim list reads the whole audit table with a consistent read on every call | Observability differs between tasks, and the claim list slows as the audit log grows | Read metrics from DynamoDB and Athena, and keep a per claim stage item to list from |
| The deploy and live evaluation workflows have not run, because their OIDC role is not in the CDK app | Only CI runs on GitHub. Deployment is done from a workstation | Add the OIDC provider and role to the CDK app, then run both workflows |
| MFA is optional, and tokens live in the browser's session storage | A script injected into the page could read a token during the hour it is valid | Enforce MFA, and keep tokens in memory with a refresh cookie |
| Password reset uses Cognito's default email sender (about 50 emails a day, from a shared address) and needs a verified email on the account | Reset suits a handful of users, and a user without an email cannot reset | Amazon SES as the sender, and an administrator process that always sets the email |
| The styled sign in page is defined in the CDK app and covered by template tests (managed login, the Essentials plan, the branding for the app's client, sign up off). It was checked in a browser on a separate user pool built with the same settings. It has not yet been deployed as part of the full stack | A full deployment could still reject a property that the tests cannot see | The next deployment confirms it, and the result belongs in the deployment evidence |
| The interactive demo on GitHub Pages does not run the agents, the guardrail or memory. Its sign in accepts any username with a password that meets the rules, and the role is switched from a menu. A typed override reason is not scanned for prompt attacks and is not kept as a lesson. The attack lab scans the sample attacks only. The Observability tab shows screenshots from the live deployment | A visitor sees rule baseline runs, not live agent runs, cannot scan their own text, and the sign in protects nothing | Run the live deployment for anyone who needs the real thing, as the demos in this document show |
| The WAF limits by address only, and the daily spend limit is checked when a run starts | A shared address is limited together, and a day can overshoot by one run per task | Limit per signed in user, and reserve spend before a run |
| The investigation experiment used one model and 28 cases written by the author, and the product has a deterministic investigator that solves the same task | It shows that the agent beats pasting all the records into the prompt, and that rules alone find 79% at no cost. It does not show that the agent finds problems no rule covers | More models, cases that no rule covers, and real adjuster feedback |
| The free-form benchmark has 124 claims, and its labels are agreement between two models, not human ground truth. 15 of the 16 dropped narratives were implicit ones | It ties the single call and the agent team. A difference of one or two claims is noise, and the set is somewhat easier than intended | Human review of the labels, and more implicit and adversarial narratives |
| The audit log is not exported to write-once storage and has no tamper evidence. The task can add rows but not change them | Someone with account administrator rights could still alter the log | Stream the table to S3 with Object Lock |
| A lesson is stored from any adjuster's override note, and has no approval, expiry or removal path. The note is scanned for prompt attacks only, and the evaluation gate does not re-run when a lesson is added | One mistaken note can quietly shift later decisions | Store lessons only after a senior review, add expiry and a removal action, and re-run the gate on change |
| One region, one account, direct query QuickSight | Not a production topology | A second region, and SPICE for the dashboard |
| S3 Vectors has no hybrid search | Retrieval can miss when the customer's words differ from the policy's words | Evaluate a managed search cluster on cost and recall |

---

## Next steps

1. Enforce **MFA**, keep tokens out of session storage, limit by signed in user instead of by address, and show each adjuster only their own queue.
2. Drive ingestion from **S3** events and **AWS Step Functions**, so **Bedrock Data Automation** and the vision model run when a document arrives.
3. Improve retrieval with query rewriting, a reranker and a **hybrid search** comparison.
4. Use adjuster overrides as an evaluation set that is never tuned against.
5. Move agent hosting to **Bedrock AgentCore** Runtime, with **AgentCore** Observability for tracing.
6. Add an **LLM** judge for memo quality, calibrated against hand graded samples.
7. Add a voice note path using **Bedrock Data Automation** transcription.
8. Run the investigation test on more models and on cases that no rule covers. Compare the agent with the deterministic investigator on cases where no rule exists.
9. Strengthen the **fine-tuning** study. Replace the generated training data with paraphrases checked by people, and then with real narratives labelled by adjusters. Repeat across seeds, with a rank and learning rate sweep and a reported spread. Distil from the strong model if volume justifies self-hosting. Evaluate on the whole pipeline.

---

## Repository layout

```
agentic-claims-adjudication-aws/
  backend/            FastAPI service, token checks (auth.py), Strands agent graph, rules engine, MCP servers, tools, tests
  frontend/           React and TypeScript workbench
  infra/              AWS CDK app: ClaimsAdjudicationData and ClaimsAdjudicationApp stacks
  evals/              golden and held-out cases, hand-calculated oracle claims, scorer, quality gate, retrieval and photo
                      evaluations, the free-form benchmark (freeform/), the investigation test (investigation/), reports
  redteam/            30 attacks, the harness, the naive control, reports
  finetune/           QLoRA data, training, SageMaker launcher, baselines
  scripts/            data generator, photo attachment, Bedrock Data Automation batch job, DynamoDB and memory
                      seeding, QuickSight setup, deployment verification, price check, screenshot redaction
  docs/               diagram generator, demo capture scripts, images, verification results
  .github/            workflows (CI, CodeQL, live eval, deploy) and the Dependabot configuration
  pyproject.toml      dependencies and tool settings; uv.lock pins every package; .python-version is 3.12
```

---

## Data sources and references

Policy wording (rules and **knowledge base**), fetched at setup and not redistributed:
- [Universal Sompo Private Car Package Policy wording](https://www.universalsompo.com/assets/file/motor-private-car/motor-private-car-policy-wordings.pdf)
- [Digit Private Car Package Policy](https://godigit.com/content/dam/godigit/directportal/en/downloads/car/policy-wordings-digit-private-car-package-policy-multi-year.pdf)
- [Liberty Private Car Package Policy](https://www.libertyinsurance.in/Docx/Private%20Car%20Package%20Policy%20Wordings%20-%20V18%2017042019.pdf)

Damage photographs: [Coco Car Damage Detection Dataset](https://www.kaggle.com/datasets/lplenka/coco-car-damage-detection-dataset) on **Kaggle**, licence CC0 1.0.

Generated data: claim packets, policy schedules and narratives come from [scripts/generate_data.py](scripts/generate_data.py), seeded for reproducibility.

Models and methods: [Qwen2.5-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct); Hu et al., "**LoRA**: Low-Rank Adaptation of Large Language Models" (2021); Dettmers et al., "**QLoRA**: Efficient Finetuning of Quantized LLMs" (2023); [Strands Agents](https://strandsagents.com); [Model Context Protocol](https://modelcontextprotocol.io).

---

## Licence

Released under the [MIT licence](LICENSE). The damage photographs are from a public dataset under CC0 1.0, and the policy wordings remain the property of their insurers and are not redistributed.
