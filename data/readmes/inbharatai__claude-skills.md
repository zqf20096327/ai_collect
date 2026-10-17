<div align="center">

<br/>

<!-- Animated Typing SVG -->
<a href="https://github.com/inbharatai/claude-skills">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=28&pause=1000&color=CC785C&center=true&vCenter=true&repeat=true&width=700&height=55&lines=183+Skills+for+Claude+AI;The+Most+Complete+Skills+Collection;Built+with+Claude+Code+%F0%9F%A4%96;10x+anthropics%2Fskills" alt="Typing SVG" />
</a>

<br/><br/>

<!-- Badge Row -->
[![Skills](https://img.shields.io/badge/183_Skills-CC785C?style=for-the-badge&logo=anthropic&logoColor=white)](https://github.com/inbharatai/claude-skills/tree/main/skills)
[![Categories](https://img.shields.io/badge/12_Categories-7B5EA7?style=for-the-badge)](https://github.com/inbharatai/claude-skills#-skills-gallery)
[![Platforms](https://img.shields.io/badge/3_Platforms-2563EB?style=for-the-badge)](https://github.com/inbharatai/claude-skills#-platform-support)
[![License](https://img.shields.io/badge/MIT-059669?style=for-the-badge&label=license)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-CC785C?style=for-the-badge)](https://github.com/inbharatai/claude-skills/pulls)

<br/>

<!-- Tech badges -->
![Claude](https://img.shields.io/badge/Claude_AI-CC785C?style=flat-square&logo=anthropic&logoColor=white)
![Claude Code](https://img.shields.io/badge/Claude_Code-1a1a1a?style=flat-square&logo=anthropic&logoColor=CC785C)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=node.js&logoColor=white)
![Anthropic](https://img.shields.io/badge/Anthropic-CC785C?style=flat-square&logo=anthropic&logoColor=white)

<br/>

[**Browse Skills**](#-skills-gallery) &nbsp;·&nbsp; [**Quick Start**](#-quick-start) &nbsp;·&nbsp; [**Build a Skill**](#-build-your-own-skill) &nbsp;·&nbsp; [**Spec**](spec/SKILL_SPEC.md) &nbsp;·&nbsp; [**Template**](template/SKILL.md) &nbsp;·&nbsp; [**Contributing**](#-contributing)

</div>

<br/>

---

<br/>

## 🤖 What are Claude Skills?

**Skills** are plug-and-play instruction sets that make Claude an instant expert in any domain. Drop a `SKILL.md` into Claude's context and it immediately knows the best practices, conventions, examples, and guardrails for that task.

<div align="center">

> *"Give Claude a skill, and it performs like a specialist. Give it 183, and it becomes your entire team."*

</div>

This collection is the **most comprehensive Claude skills library on the internet** — 10× the size of the official `anthropics/skills` repo, with 183 production-ready skills across 12 categories.

<br/>

---

<br/>

## 📊 At a Glance

<div align="center">

<table>
<tr>
<td align="center"><h3>🧩</h3><b>183</b><br/><sub>Total Skills</sub></td>
<td align="center"><h3>📂</h3><b>12</b><br/><sub>Categories</sub></td>
<td align="center"><h3>🖥️</h3><b>3</b><br/><sub>Platforms</sub></td>
<td align="center"><h3>⚡</h3><b>2</b><br/><sub>Required Fields</sub></td>
<td align="center"><h3>🌐</h3><b>∞</b><br/><sub>Possibilities</sub></td>
<td align="center"><h3>🔓</h3><b>MIT</b><br/><sub>License</sub></td>
</tr>
</table>

<br/>

🏆 **10× anthropics/skills** &nbsp;·&nbsp; 🤖 **Built with Claude Code** &nbsp;·&nbsp; 🔌 **Plug-and-play** &nbsp;·&nbsp; 📦 **Zero dependencies** &nbsp;·&nbsp; ✅ **Production-ready**

</div>

<br/>

---

<br/>

## 🚀 Quick Start

### Use a Skill in Claude.ai

1. Open [Claude.ai](https://claude.ai) and start a new conversation
2. Copy the contents of any `skills/<name>/SKILL.md` file
3. Paste it at the start of your conversation or as a system prompt
4. Claude is now an expert — start prompting

### Use a Skill via API

```python
import anthropic

with open("skills/pdf/SKILL.md") as f:
    skill = f.read()

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=4096,
    system=skill,
    messages=[{"role": "user", "content": "Merge these two PDFs and add a watermark"}]
)
print(response.content[0].text)
```

### Use a Skill in Claude Code

```bash
# Add to your CLAUDE.md or paste into any conversation
cat skills/code-reviewer/SKILL.md
```

> [!TIP]
> **Pro tip:** Combine multiple skills by concatenating their `SKILL.md` files — Claude handles multi-skill contexts gracefully.

<br/>

---

<br/>

## 🗂️ Skills Gallery

<br/>

### 📄 Documents & Files — 17 Skills

> Generate, transform, and manipulate every document format imaginable.

| Skill | Description |
|:------|:------------|
| [pdf](skills/pdf/SKILL.md) | Extract, merge, split, rotate, watermark, fill forms, and OCR PDFs |
| [docx](skills/docx/SKILL.md) | Create and edit Word documents with full formatting — TOC, headings, tracked changes |
| [pptx](skills/pptx/SKILL.md) | Build PowerPoint decks — slides, speaker notes, animations, and templates |
| [xlsx](skills/xlsx/SKILL.md) | Read, write, and fix Excel spreadsheets — formulas, charts, and data cleaning |
| [csv-analyzer](skills/csv-analyzer/SKILL.md) | Analyze and summarize CSV files — anomaly detection and statistics |
| [json-formatter](skills/json-formatter/SKILL.md) | Format, validate, diff, and query JSON with JSONPath |
| [xml-parser](skills/xml-parser/SKILL.md) | Parse, transform, validate XML — XPath, XSLT, and JSON conversion |
| [markdown-pro](skills/markdown-pro/SKILL.md) | Generate polished Markdown — READMEs, wikis, changelogs, and docs sites |
| [epub-creator](skills/epub-creator/SKILL.md) | Package ePub 3 e-books with chapters, TOC, and metadata |
| [latex-writer](skills/latex-writer/SKILL.md) | Author LaTeX papers, theses, equations, and Beamer presentations |
| [mail-merge](skills/mail-merge/SKILL.md) | Personalized document generation from templates and data |
| [template-engine](skills/template-engine/SKILL.md) | Render Jinja2/Handlebars templates with dynamic variables |
| [contract-generator](skills/contract-generator/SKILL.md) | Draft NDAs, service agreements, and SaaS terms |
| [invoice-creator](skills/invoice-creator/SKILL.md) | Generate branded PDF invoices with taxes and payment terms |
| [resume-builder](skills/resume-builder/SKILL.md) | Craft ATS-optimized resumes and cover letters |
| [form-filler](skills/form-filler/SKILL.md) | Auto-fill PDF and HTML forms from structured data |
| [report-builder](skills/report-builder/SKILL.md) | Compile data-driven reports with charts and narratives |

<br/>

### 🎨 Creative & Design — 21 Skills

> Design systems, art, UI mockups, and every visual artifact.

| Skill | Description |
|:------|:------------|
| [algorithmic-art](skills/algorithmic-art/SKILL.md) | Generative art — fractals, noise fields, and procedural imagery |
| [canvas-design](skills/canvas-design/SKILL.md) | HTML5 Canvas graphics — illustrations, diagrams, and interactive visuals |
| [brand-guidelines](skills/brand-guidelines/SKILL.md) | Brand identity — logo usage, palettes, typography, and tone-of-voice |
| [theme-factory](skills/theme-factory/SKILL.md) | Complete UI themes — color tokens, type scales, dark/light variants |
| [frontend-design](skills/frontend-design/SKILL.md) | Pixel-perfect HTML/CSS/Tailwind UIs and component libraries |
| [slack-gif-creator](skills/slack-gif-creator/SKILL.md) | Animated GIFs for Slack — reactions, celebrations, mascots |
| [logo-designer](skills/logo-designer/SKILL.md) | SVG logos with primary, monochrome, and favicon variants |
| [icon-generator](skills/icon-generator/SKILL.md) | Consistent SVG icon sets — line, filled, duotone, and PNG exports |
| [color-palette](skills/color-palette/SKILL.md) | Harmonious palettes with WCAG contrast checks and CSS variables |
| [ui-mockup](skills/ui-mockup/SKILL.md) | High-fidelity UI mockups — dashboards, mobile screens, landing pages |
| [wireframe-builder](skills/wireframe-builder/SKILL.md) | Low-fidelity wireframes and user-flow diagrams |
| [design-system](skills/design-system/SKILL.md) | Complete design systems — tokens, Storybook, Figma variables |
| [svg-animator](skills/svg-animator/SKILL.md) | Animated SVGs with GSAP — loaders, icon animations, micro-interactions |
| [css-art](skills/css-art/SKILL.md) | Pure CSS art and interactive CSS-only animations |
| [pixel-art](skills/pixel-art/SKILL.md) | Pixel art sprites, tilesets, and game asset animations |
| [infographic-builder](skills/infographic-builder/SKILL.md) | SVG/HTML infographics — timelines, flows, and comparison charts |
| [chart-designer](skills/chart-designer/SKILL.md) | Publication-quality charts — bar, line, scatter, heatmaps, D3 |
| [data-viz](skills/data-viz/SKILL.md) | Interactive dashboards, maps, network graphs, and Sankey diagrams |
| [typography-guide](skills/typography-guide/SKILL.md) | Typeface pairing, type scales, and CSS typography systems |
| [accessibility-checker](skills/accessibility-checker/SKILL.md) | WCAG 2.2 audits — ARIA, contrast, keyboard navigation, screen readers |
| [dark-mode-converter](skills/dark-mode-converter/SKILL.md) | Convert any UI to dark mode with semantic tokens and transitions |

<br/>

### 💻 Development — 25 Skills

> Build, review, debug, and ship production code faster.

| Skill | Description |
|:------|:------------|
| [claude-api](skills/claude-api/SKILL.md) | Anthropic Claude API — chat, tool use, streaming, vision, multi-turn |
| [mcp-builder](skills/mcp-builder/SKILL.md) | Model Context Protocol servers — tools, resources, prompts |
| [web-artifacts-builder](skills/web-artifacts-builder/SKILL.md) | Interactive HTML/CSS/JS artifacts that run inside Claude |
| [webapp-testing](skills/webapp-testing/SKILL.md) | Unit, integration, E2E tests with Playwright/Cypress and visual regression |
| [api-designer](skills/api-designer/SKILL.md) | OpenAPI specs, schemas, error codes, versioning, and docs |
| [rest-api-builder](skills/rest-api-builder/SKILL.md) | Production REST APIs with auth, rate limiting, and validation |
| [graphql-builder](skills/graphql-builder/SKILL.md) | GraphQL schemas — types, resolvers, subscriptions, and federation |
| [docker-composer](skills/docker-composer/SKILL.md) | Dockerfiles and docker-compose — multi-stage, health checks, volumes |
| [kubernetes-helper](skills/kubernetes-helper/SKILL.md) | K8s manifests — Deployments, Ingress, HPA, and Helm charts |
| [ci-cd-builder](skills/ci-cd-builder/SKILL.md) | CI/CD pipelines — GitHub Actions, GitLab CI, Jenkins, CircleCI |
| [code-reviewer](skills/code-reviewer/SKILL.md) | Thorough reviews — bugs, security, performance, and architecture |
| [refactor-assistant](skills/refactor-assistant/SKILL.md) | Refactor codebases — SOLID, reduce complexity, modernize legacy code |
| [debug-helper](skills/debug-helper/SKILL.md) | Systematic debugging — stack traces, root cause, and fix suggestions |
| [db-schema-designer](skills/db-schema-designer/SKILL.md) | Normalized schemas — ERDs, indexes, constraints, and migrations |
| [sql-builder](skills/sql-builder/SKILL.md) | Complex SQL — JOINs, CTEs, window functions, and query plans |
| [migration-generator](skills/migration-generator/SKILL.md) | Database migrations — Alembic, Flyway, Liquibase, up/down scripts |
| [security-auditor](skills/security-auditor/SKILL.md) | Code security — OWASP Top 10, injection, auth flaws, secrets exposure |
| [perf-optimizer](skills/perf-optimizer/SKILL.md) | Performance — complexity, caching, query optimization, bundle size |
| [cli-builder](skills/cli-builder/SKILL.md) | Polished CLI tools — arg parsing, prompts, progress bars, completions |
| [chrome-extension](skills/chrome-extension/SKILL.md) | Chrome/Edge extensions — manifest v3, content scripts, service workers |
| [vscode-extension](skills/vscode-extension/SKILL.md) | VS Code extensions — commands, language servers, webview panels |
| [react-component](skills/react-component/SKILL.md) | Production React — hooks, context, TypeScript, Storybook |
| [vue-component](skills/vue-component/SKILL.md) | Vue 3 Composition API — composables, Pinia, TypeScript |
| [angular-component](skills/angular-component/SKILL.md) | Angular — services, directives, RxJS, Angular Material |
| [svelte-component](skills/svelte-component/SKILL.md) | Svelte 5 — runes, stores, SvelteKit routing, SSR |

<br/>

### 📊 Data & Analytics — 15 Skills

> Clean, transform, model, and story-tell with data.

| Skill | Description |
|:------|:------------|
| [data-cleaner](skills/data-cleaner/SKILL.md) | Handle missing values, fix dtypes, remove duplicates, flag anomalies |
| [data-transformer](skills/data-transformer/SKILL.md) | Pivot, melt, aggregate, join, and apply business rules to datasets |
| [etl-pipeline](skills/etl-pipeline/SKILL.md) | End-to-end ETL — extract, transform, validate, load to warehouses |
| [sql-analyst](skills/sql-analyst/SKILL.md) | SQL analysis — aggregations, funnels, cohorts, and insight narratives |
| [pandas-helper](skills/pandas-helper/SKILL.md) | pandas mastery — DataFrames, groupby, merge, time-series, memory |
| [spark-builder](skills/spark-builder/SKILL.md) | PySpark and Spark SQL — RDDs, DataFrames, streaming, MLlib |
| [dashboard-builder](skills/dashboard-builder/SKILL.md) | Interactive dashboards — Streamlit, Dash, Grafana, Power BI |
| [kpi-tracker](skills/kpi-tracker/SKILL.md) | KPI frameworks — metrics, targets, tracking templates, reports |
| [ml-pipeline](skills/ml-pipeline/SKILL.md) | End-to-end ML — data prep, training, evaluation, MLflow tracking |
| [model-evaluator](skills/model-evaluator/SKILL.md) | Model evaluation — CV, ROC, confusion matrices, bias audits, SHAP |
| [feature-engineer](skills/feature-engineer/SKILL.md) | ML features — encoding, scaling, embeddings, feature selection |
| [statistical-analyzer](skills/statistical-analyzer/SKILL.md) | Statistics — hypothesis tests, regression, ANOVA, power calculations |
| [ab-test-designer](skills/ab-test-designer/SKILL.md) | A/B tests — sample sizes, significance testing, results interpretation |
| [cohort-analyzer](skills/cohort-analyzer/SKILL.md) | Cohort analysis — retention curves, LTV, churn funnels |
| [data-storyteller](skills/data-storyteller/SKILL.md) | Data narratives — executive summaries and annotated charts |

<br/>

### ✍️ Writing & Communication — 17 Skills

> Write anything, for any audience, in any format.

| Skill | Description |
|:------|:------------|
| [doc-coauthoring](skills/doc-coauthoring/SKILL.md) | Collaborative long-form documents — track changes, review cycles |
| [internal-comms](skills/internal-comms/SKILL.md) | All-hands updates, policy announcements, and executive briefings |
| [email-composer](skills/email-composer/SKILL.md) | Professional emails — outreach, follow-ups, negotiations |
| [newsletter-writer](skills/newsletter-writer/SKILL.md) | Email newsletters — hooks, CTAs, subject line optimization |
| [blog-writer](skills/blog-writer/SKILL.md) | SEO-optimized blog posts that rank and convert |
| [press-release](skills/press-release/SKILL.md) | Professional press releases — headline, dateline, boilerplate |
| [technical-writer](skills/technical-writer/SKILL.md) | API docs, user guides, runbooks, and architecture decision records |
| [copywriter](skills/copywriter/SKILL.md) | High-converting copy — landing pages, ads, taglines |
| [social-media-manager](skills/social-media-manager/SKILL.md) | Platform-specific posts, hashtags, and content calendars |
| [tweet-thread](skills/tweet-thread/SKILL.md) | Viral tweet threads — hooks, narrative arcs, engagement CTAs |
| [linkedin-post](skills/linkedin-post/SKILL.md) | LinkedIn posts — thought leadership and algorithm-friendly format |
| [speech-writer](skills/speech-writer/SKILL.md) | Speeches — keynotes, toasts, eulogies, and commencements |
| [pitch-narrator](skills/pitch-narrator/SKILL.md) | Investor pitch narratives — problem framing, market sizing, Q&A |
| [meeting-summarizer](skills/meeting-summarizer/SKILL.md) | Meeting summaries — decisions, action items, follow-up emails |
| [proposal-writer](skills/proposal-writer/SKILL.md) | RFP responses, project proposals, and partnership agreements |
| [grant-writer](skills/grant-writer/SKILL.md) | Grant applications — needs statements, narratives, budgets |
| [policy-drafter](skills/policy-drafter/SKILL.md) | HR policies, data governance, and compliance documents |

<br/>

### 💼 Business & Productivity — 16 Skills

> Run better projects, meetings, and organizations.

| Skill | Description |
|:------|:------------|
| [project-planner](skills/project-planner/SKILL.md) | WBS, Gantt charts, resource allocation, risk registers |
| [okr-tracker](skills/okr-tracker/SKILL.md) | OKR frameworks — objectives, key results, scoring rubrics |
| [sprint-planner](skills/sprint-planner/SKILL.md) | Agile sprints — backlog refinement, story pointing, retros |
| [meeting-agenda](skills/meeting-agenda/SKILL.md) | Effective agendas — objectives, time boxes, decision frameworks |
| [minutes-writer](skills/minutes-writer/SKILL.md) | Meeting minutes — decisions, action items, next-meeting prep |
| [action-tracker](skills/action-tracker/SKILL.md) | Action item tracking — owners, deadlines, escalation workflows |
| [business-plan](skills/business-plan/SKILL.md) | Business plans — executive summary, market analysis, financials |
| [financial-model](skills/financial-model/SKILL.md) | P&L projections, cash flow, unit economics, DCF valuations |
| [market-analyzer](skills/market-analyzer/SKILL.md) | TAM/SAM/SOM, Porter's Five Forces, SWOT, segmentation |
| [customer-success](skills/customer-success/SKILL.md) | CS playbooks — onboarding, health scoring, churn intervention |
| [support-handler](skills/support-handler/SKILL.md) | Support responses — ticket triage, empathetic replies, macros |
| [feedback-analyzer](skills/feedback-analyzer/SKILL.md) | Sentiment analysis, theme clustering, NPS interpretation |
| [job-description](skills/job-description/SKILL.md) | Inclusive job descriptions with bias-free language |
| [interview-questions](skills/interview-questions/SKILL.md) | Behavioral, technical, and situational interview guides |
| [performance-reviewer](skills/performance-reviewer/SKILL.md) | Performance reviews — self-assessments, 360 feedback, development plans |
| [sop-builder](skills/sop-builder/SKILL.md) | Standard operating procedures — workflows, decision trees |

<br/>

### 🎓 Education & Learning — 14 Skills

> Teach, train, and upskill at scale.

| Skill | Description |
|:------|:------------|
| [course-creator](skills/course-creator/SKILL.md) | Full online courses — objectives, modules, scripts, quizzes |
| [quiz-generator](skills/quiz-generator/SKILL.md) | Quizzes from any content — MCQ, T/F, short answer with keys |
| [flashcard-maker](skills/flashcard-maker/SKILL.md) | Anki-compatible decks — spaced repetition, cloze deletions |
| [lesson-planner](skills/lesson-planner/SKILL.md) | Engaging lessons — objectives, warm-ups, differentiation |
| [curriculum-designer](skills/curriculum-designer/SKILL.md) | Curricula — scope and sequence, standards alignment, pacing |
| [rubric-creator](skills/rubric-creator/SKILL.md) | Assessment rubrics — criteria, levels, point values |
| [explainer-writer](skills/explainer-writer/SKILL.md) | Feynman technique breakdowns for any audience |
| [tutorial-builder](skills/tutorial-builder/SKILL.md) | Step-by-step tutorials with prerequisites and troubleshooting |
| [docs-generator](skills/docs-generator/SKILL.md) | Auto-generate docs from code — docstrings, API refs, READMEs |
| [study-guide](skills/study-guide/SKILL.md) | Study guides — concepts, mnemonics, practice problems |
| [exam-prep](skills/exam-prep/SKILL.md) | Exam preparation — practice tests, drills, timed quizzes |
| [learning-path](skills/learning-path/SKILL.md) | Personalized learning paths — assessment, resources, milestones |
| [concept-mapper](skills/concept-mapper/SKILL.md) | Concept maps and knowledge graphs with Mermaid export |
| [cohort-coach](skills/cohort-coach/SKILL.md) | Cohort-based learning — prompts, peer challenges, projects |

<br/>

### 🔬 Research & Analysis — 12 Skills

> Research deeper, faster, and with more rigour.

| Skill | Description |
|:------|:------------|
| [literature-reviewer](skills/literature-reviewer/SKILL.md) | Summarize papers, extract findings, synthesize themes |
| [citation-manager](skills/citation-manager/SKILL.md) | APA, MLA, Chicago, IEEE, Vancouver, and BibTeX export |
| [research-summarizer](skills/research-summarizer/SKILL.md) | Paper summaries — abstracts, methodology, implications |
| [competitive-analyst](skills/competitive-analyst/SKILL.md) | Competitor analysis — feature matrices, positioning maps |
| [market-researcher](skills/market-researcher/SKILL.md) | Market research — surveys, interviews, synthesis reports |
| [trend-analyzer](skills/trend-analyzer/SKILL.md) | Technology signals, market shifts, and future-back scenarios |
| [fact-checker](skills/fact-checker/SKILL.md) | Verify claims — source credibility, misinformation flagging |
| [source-evaluator](skills/source-evaluator/SKILL.md) | CRAAP test, lateral reading, domain authority, bias assessment |
| [bias-detector](skills/bias-detector/SKILL.md) | Cognitive and statistical biases, logical fallacies |
| [survey-designer](skills/survey-designer/SKILL.md) | Survey design — Likert scales, skip logic, analysis plans |
| [interview-guide](skills/interview-guide/SKILL.md) | Qualitative guides — probing questions, thematic analysis |
| [ux-researcher](skills/ux-researcher/SKILL.md) | UX research — usability tests, journey maps, affinity diagrams |

<br/>

### ⚙️ DevOps & Infrastructure — 13 Skills

> Ship infrastructure as fast as you ship code.

| Skill | Description |
|:------|:------------|
| [dockerfile-builder](skills/dockerfile-builder/SKILL.md) | Optimized Dockerfiles — multi-stage, security hardening, minimal size |
| [compose-creator](skills/compose-creator/SKILL.md) | docker-compose — services, networks, volumes, health checks |
| [terraform-writer](skills/terraform-writer/SKILL.md) | Terraform IaC — providers, modules, state, cloud resources |
| [github-actions](skills/github-actions/SKILL.md) | GitHub Actions — CI, CD, releases, and composite actions |
| [jenkins-pipeline](skills/jenkins-pipeline/SKILL.md) | Jenkins pipelines — declarative, parallel, shared libraries |
| [gitlab-ci](skills/gitlab-ci/SKILL.md) | GitLab CI/CD — stages, caching, artifacts, environments |
| [aws-architect](skills/aws-architect/SKILL.md) | AWS architectures — VPC, ECS, Lambda, RDS, Well-Architected |
| [gcp-architect](skills/gcp-architect/SKILL.md) | GCP architectures — GKE, Cloud Run, BigQuery, Pub/Sub |
| [azure-architect](skills/azure-architect/SKILL.md) | Azure architectures — AKS, Functions, Cosmos DB, Service Bus |
| [monitoring-setup](skills/monitoring-setup/SKILL.md) | Prometheus + Grafana — alerting rules, SLOs, error budgets |
| [alerting-config](skills/alerting-config/SKILL.md) | Alert configs — thresholds, routing, de-duplication, escalation |
| [log-analyzer](skills/log-analyzer/SKILL.md) | Log analysis — pattern detection, error clustering, anomalies |
| [helm-chart-builder](skills/helm-chart-builder/SKILL.md) | Helm charts — templates, values, hooks, tests, OCI publishing |

<br/>

### 🔒 Security — 10 Skills

> Build and audit secure systems.

| Skill | Description |
|:------|:------------|
| [threat-modeler](skills/threat-modeler/SKILL.md) | STRIDE threat modeling — attack trees, DFDs, mitigations |
| [pentest-helper](skills/pentest-helper/SKILL.md) | Authorized pen testing — recon, vulnerability ID, reports |
| [vuln-scanner](skills/vuln-scanner/SKILL.md) | Code vulnerabilities — CVE lookup, SAST findings, remediation |
| [security-policy](skills/security-policy/SKILL.md) | Security policies — incident response, data classification, access control |
| [compliance-checker](skills/compliance-checker/SKILL.md) | ISO 27001, SOC 2, PCI-DSS, HIPAA, and NIST compliance |
| [gdpr-helper](skills/gdpr-helper/SKILL.md) | GDPR compliance — data mapping, DPIAs, consent flows |
| [secret-scanner](skills/secret-scanner/SKILL.md) | Detect hardcoded API keys, tokens, and passwords in code |
| [dependency-auditor](skills/dependency-auditor/SKILL.md) | Package audits — CVEs, license conflicts, upgrade recommendations |
| [owasp-checker](skills/owasp-checker/SKILL.md) | OWASP Top 10 — injection, broken auth, XSS, misconfiguration |
| [soc2-helper](skills/soc2-helper/SKILL.md) | SOC 2 audits — control mapping, evidence, gap analysis |

<br/>

### 🎬 Media & Content — 10 Skills

> Create content that gets seen, shared, and ranked.

| Skill | Description |
|:------|:------------|
| [video-script](skills/video-script/SKILL.md) | YouTube, explainers, ads — scripts with B-roll notes |
| [podcast-outline](skills/podcast-outline/SKILL.md) | Podcast episodes — structure, questions, timing, show notes |
| [youtube-optimizer](skills/youtube-optimizer/SKILL.md) | YouTube — titles, descriptions, tags, chapters, end screens |
| [seo-optimizer](skills/seo-optimizer/SKILL.md) | SEO — keyword research, on-page, meta tags, structured data |
| [content-calendar](skills/content-calendar/SKILL.md) | Content calendars — themes, schedules, repurposing strategies |
| [keyword-researcher](skills/keyword-researcher/SKILL.md) | Keyword research — intent mapping, long-tail, clusters |
| [midjourney-prompter](skills/midjourney-prompter/SKILL.md) | Midjourney prompts — style refs, aspect ratios, v6 parameters |
| [stable-diffusion-helper](skills/stable-diffusion-helper/SKILL.md) | Stable Diffusion — SDXL, LoRA, ControlNet, ComfyUI workflows |
| [image-captioner](skills/image-captioner/SKILL.md) | Alt text, captions, metadata — accessibility and SEO |
| [thumbnail-designer](skills/thumbnail-designer/SKILL.md) | Click-worthy thumbnails — layout, text overlays, A/B variants |

<br/>

### 🔌 Integrations & Automation — 13 Skills

> Connect everything, automate anything.

| Skill | Description |
|:------|:------------|
| [skill-creator](skills/skill-creator/SKILL.md) | Build new Claude skills — SKILL.md authoring and testing |
| [slack-bot-builder](skills/slack-bot-builder/SKILL.md) | Slack bots — Bolt, slash commands, modals, Block Kit |
| [discord-bot](skills/discord-bot/SKILL.md) | Discord bots — slash commands, embeds, voice, roles |
| [teams-integration](skills/teams-integration/SKILL.md) | Microsoft Teams — bots, adaptive cards, Graph API |
| [github-integration](skills/github-integration/SKILL.md) | GitHub — Actions, Apps, webhooks, Octokit automation |
| [jira-helper](skills/jira-helper/SKILL.md) | Jira automation — issues, sprints, JQL, reporting |
| [notion-integration](skills/notion-integration/SKILL.md) | Notion — database queries, page creation, content sync |
| [zapier-workflow](skills/zapier-workflow/SKILL.md) | Zapier automations — triggers, actions, multi-step Zaps |
| [n8n-workflow](skills/n8n-workflow/SKILL.md) | n8n workflows — nodes, expressions, error handling |
| [make-scenario](skills/make-scenario/SKILL.md) | Make scenarios — modules, routers, aggregators |
| [webhook-builder](skills/webhook-builder/SKILL.md) | Webhook handlers — validation, signature, retry, routing |
| [stripe-integration](skills/stripe-integration/SKILL.md) | Stripe — Checkout, subscriptions, webhooks, billing portal |
| [twilio-helper](skills/twilio-helper/SKILL.md) | Twilio — SMS, voice, WhatsApp, video, and Verify 2FA |

<br/>

---

<br/>

## 🏗️ Skill Anatomy

<details>
<summary><b>📋 How a SKILL.md is structured (click to expand)</b></summary>

<br/>

Every skill has two parts: **YAML frontmatter** and a **Markdown body**.

```yaml
---
name: your-skill          # unique kebab-case slug
display_name: Your Skill  # human-readable title
description: One sentence describing what this skill does — start with a verb.
category: Development     # one of the 12 categories
platforms: [claude.ai, claude-code, api]
version: 1.0.0
author: Your Name
tags: [tag1, tag2]
---

# Your Skill

## Overview
What it does and why it exists.

## When to Use This Skill
- Bullet list of trigger scenarios

## Instructions
1. What Claude does first
2. What Claude does second

## Examples
### Example 1 — Basic
**User:** ...
**Claude:** ...

## Guidelines
- Do: ...
- Don't: ...
```

**Only 2 fields are required:** `name` and `description`.

See the full spec in [`spec/SKILL_SPEC.md`](spec/SKILL_SPEC.md).

</details>

<br/>

---

<br/>

## 🛠️ Build Your Own Skill

1. **Copy the template**
   ```bash
   cp template/SKILL.md skills/my-skill/SKILL.md
   ```

2. **Fill in the frontmatter**
   ```yaml
   ---
   name: my-skill
   display_name: My Skill
   description: Does X, Y, and Z — specifically for [audience].
   category: Development
   platforms: [claude.ai, claude-code, api]
   version: 1.0.0
   author: Your Name
   ---
   ```

3. **Write clear instructions** — tell Claude exactly what to do, not just what to know

4. **Add 2–3 examples** — show real user prompts and Claude's ideal response

5. **Test it** — paste your `SKILL.md` into Claude and try 10 different prompts

6. **Submit a PR** — see [Contributing](#-contributing)

> [!TIP]
> The `description` field is the most important — it determines when Claude activates your skill. Write it as: `"[Verb] [object] — [specific capabilities]."`

<br/>

---

<br/>

## 🖥️ Platform Support

<div align="center">

| Platform | How to Use | All Skills? |
|:---------|:-----------|:-----------:|
| **Claude.ai** | Paste `SKILL.md` at conversation start or as a Project instruction | ✅ |
| **Claude Code** | Reference in `CLAUDE.md` or paste inline | ✅ |
| **Anthropic API** | Pass as `system` parameter in `messages.create()` | ✅ |

</div>

<br/>

---

<br/>

## 🤝 Contributing

<div align="center">

**We welcome new skills, improvements, and bug fixes from the community.**

</div>

<br/>

1. 🍴 **Fork** this repository
2. 🌿 **Create** a skill: `mkdir skills/my-skill && cp template/SKILL.md skills/my-skill/SKILL.md`
3. ✏️ **Write** your skill following the [spec](spec/SKILL_SPEC.md)
4. ✅ **Test** it — paste into Claude and try 10+ prompts
5. 💾 **Commit** — `git commit -m "feat: add my-skill"`
6. 📤 **Push** and open a Pull Request

### Contribution guidelines

- One skill per PR
- `description` must be ≤ 120 chars and start with a verb
- Include at least 2 examples
- Follow the `template/SKILL.md` structure
- Skills must be original — no copy-paste from other repos

<br/>

---

<br/>

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

Skills are provided for educational and production use. Some skill implementations may be adapted from community contributions.

<br/>

---

---

<br/>

## 🤖 Built with Claude Code

<div align="center">

<img src="https://img.shields.io/badge/Claude_Code-1a1a1a?style=for-the-badge&logo=anthropic&logoColor=CC785C" height="40"/>

<br/><br/>

> This entire repository — all 183 skills, the spec, the template, and this README — was designed and generated using **[Claude Code](https://claude.ai/claude-code)**, Anthropic's official AI-powered CLI for software engineering.
>
> *Zero manual file editing. Pure AI-driven creation.*

<br/>

[![Built with Claude Code](https://img.shields.io/badge/Built%20with-Claude%20Code-CC785C?style=for-the-badge&logo=anthropic&logoColor=white)](https://claude.ai/claude-code)
[![Powered by Anthropic](https://img.shields.io/badge/Powered%20by-Anthropic-CC785C?style=for-the-badge&logo=anthropic&logoColor=white)](https://anthropic.com)
[![Model](https://img.shields.io/badge/Model-Claude%20Sonnet%204.6-7B5EA7?style=for-the-badge&logo=anthropic&logoColor=white)](https://anthropic.com)

</div>

<br/>

---

<br/>

## 🏷️ Topics

`claude` `anthropic` `claude-ai` `claude-code` `skills` `ai-skills` `llm` `llm-tools` `prompt-engineering` `ai-prompts` `claude-skills` `anthropic-claude` `generative-ai` `ai-assistant` `ai-tools` `productivity` `developer-tools` `automation` `chatbot` `openai-alternative` `claude-api` `mcp` `model-context-protocol` `ai-workflows` `no-code` `low-code` `code-generation` `document-generation` `data-analysis` `machine-learning`

<br/>

---

<div align="center">

<br/>

[![Anthropic](https://img.shields.io/badge/Powered_by-Anthropic_Claude-CC785C?style=for-the-badge&logo=anthropic&logoColor=white)](https://anthropic.com)
[![Made with Claude Code](https://img.shields.io/badge/Made_with-Claude_Code-1a1a1a?style=for-the-badge&logo=anthropic&logoColor=CC785C)](https://claude.ai/claude-code)

<br/>

**Built by [InBharat AI](https://github.com/inbharatai) · 183 skills · 12 categories · 3 platforms**

*The most comprehensive Claude skills collection on the internet.*

<br/>

[![Star this repo](https://img.shields.io/github/stars/inbharatai/claude-skills?style=for-the-badge&logo=github&label=Star%20claude-skills&color=CC785C)](https://github.com/inbharatai/claude-skills)

<br/>

![Claude](https://img.shields.io/badge/Claude_AI-CC785C?style=flat-square&logo=anthropic&logoColor=white)
![Claude Code](https://img.shields.io/badge/Claude_Code-1a1a1a?style=flat-square&logo=anthropic&logoColor=CC785C)
![Anthropic](https://img.shields.io/badge/Anthropic-CC785C?style=flat-square&logo=anthropic&logoColor=white)
![MIT](https://img.shields.io/badge/MIT-059669?style=flat-square&label=license)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-CC785C?style=flat-square)
![Skills](https://img.shields.io/badge/183_Skills-7B5EA7?style=flat-square)
![Categories](https://img.shields.io/badge/12_Categories-2563EB?style=flat-square)

<sub>If this collection helped you, give it a ⭐ — it means the world!</sub>

</div>
