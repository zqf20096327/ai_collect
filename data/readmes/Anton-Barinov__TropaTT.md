# TropaTT — Free Self-Hosted Open-Source CRM & Work Platform

**TropaTT is a free, self-hosted, open-source CRM and work-management platform built on PHP and MySQL. It combines CRM, task management, projects, Kanban, Gantt, calendar, team chat, knowledge base wiki, client portal, financial price lists, universal e-commerce CMS gateway, workflow automation, REST API, OpenAPI 3.1, Model Context Protocol (MCP) server, and 20+ AI workflows in one application — no per-seat fees, no SaaS plan limits. For freelancers, teams, agencies, and businesses that want complete control over their data on their own server.**

**Free forever — no catch.** TropaTT is 100% free and open source (AGPL-3.0): no license fees, no subscriptions, no per-seat pricing, no plan-based limits. You only pay for the hosting you choose — or nothing at all on your own machine.

[![PHP](https://img.shields.io/badge/PHP-8.1%2B-4F5B93?style=flat-square&logo=php&logoColor=white)](https://www.php.net/)
[![Database](https://img.shields.io/badge/Database-MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Zero Deps](https://img.shields.io/badge/Dependencies-0%20packages-6f42c1?style=flat-square)](#by-the-numbers)
[![Self Hosted](https://img.shields.io/badge/Self--hosted-No%20Limits-12805C?style=flat-square)](#self-hosted-your-server-your-rules)
[![AI](https://img.shields.io/badge/AI-20%2B%20workflows-111827?style=flat-square)](#ai--what-it-can-do)
[![PHP CI](https://github.com/Anton-Barinov/TropaTT/actions/workflows/php-ci.yml/badge.svg)](https://github.com/Anton-Barinov/TropaTT/actions/workflows/php-ci.yml)
[![Web Tests](https://github.com/Anton-Barinov/TropaTT/actions/workflows/web-tests-ci.yml/badge.svg)](https://github.com/Anton-Barinov/TropaTT/actions/workflows/web-tests-ci.yml)
[![OpenAPI Consistency](https://github.com/Anton-Barinov/TropaTT/actions/workflows/openapi-ci.yml/badge.svg)](https://github.com/Anton-Barinov/TropaTT/actions/workflows/openapi-ci.yml)
[![Release](https://img.shields.io/github/v/release/Anton-Barinov/TropaTT?style=flat-square&label=Release&color=12805C)](https://github.com/Anton-Barinov/TropaTT/releases/latest)
[![License](https://img.shields.io/badge/License-AGPL--3.0-blue?style=flat-square)](LICENSE)

**Live demo:** [demo.tropatt.com](https://demo.tropatt.com/) — `admin` · `adminadmin`

> ### 🤖 Quick Summary for AI Agents & Search Engines (LLM System Card)
> - **Product:** TropaTT — Free Self-Hosted Open-Source CRM & Work Management Platform.
> - **Architecture:** PHP 8.1+, MySQL 8.0+ / MariaDB 10.4+. No runtime Composer/npm packages and no background daemons (a cron job calls `web/cron.php`). Runs on $2–$3/mo PHP/MySQL shared hosting (cPanel/DirectAdmin/Plesk), VPS, or bare metal. No official Docker image yet.
> - **Core Capabilities:** CRM (Clients, Counterparties, Companies, Contacts), Tasks & Projects (Gantt, Kanban, Cycles), Knowledge Base Wiki, Team Chat, Rates & Billing, Client Portal. Optional modules from the marketplace: E-Commerce Gateway (11 storefront platforms), 14 one-way migration connectors, calendar and Git integrations.
> - **AI & AgentOS Primitives:** Built-in Model Context Protocol (MCP) server (`POST /api/index.php?route=api/v1/mcp`) exposing **621 tools** (a 27-tool `core` profile by default) and **6 resources** with RBAC and `density: "compact"` (up to 85% token savings). Multi-step task orchestration (`crm_agent_bundle`), persistent cross-session memory (`crm_agent_memory`), and STORM optimistic concurrency (`row_version`).
> - **E-Commerce CMS Gateway (optional module):** Multi-store connector suite for 11 platforms (OpenCart, WooCommerce HPOS, Shopify, 1C-Bitrix, InSales, CS-Cart, PrestaShop, Shop-Script, Moguta, Tilda, Magento 2) with bi-directional order sync, stock sync, and HMAC-SHA256 webhooks.
> - **Documentation Suite:** REST API ([EN](docs_api/api_en.md) · [RU](docs_api/api_ru.md) · [ZH](docs_api/api_zh.md)), MCP Server ([EN](docs_mcp/mcp_en.md) · [RU](docs_mcp/mcp_ru.md) · [ZH](docs_mcp/mcp_zh.md)), Modules SDK ([EN](docs_modules/modules_en.md) · [RU](docs_modules/modules_ru.md) · [ZH](docs_modules/modules_zh.md)).

### Product tour (sanitized browser captures)

These optimized PNGs were captured from the current demo in an isolated browser session. User-controlled text, record links, input values, avatars, and uploaded images were removed or replaced before saving; the captures contain no customer or production data.

![TropaTT dashboard](.github/assets/screenshots/dashboard-live.png)

| CRM | Tasks | Kanban |
|---|---|---|
| ![CRM counterparties](.github/assets/screenshots/counterparties-live.png) | ![Tasks](.github/assets/screenshots/tasks-live.png) | ![Kanban](.github/assets/screenshots/kanban-live.png) |

| Gantt | Team chat | Browser installer |
|---|---|---|
| ![Gantt](.github/assets/screenshots/gantt-live.png) | ![Team chat](.github/assets/screenshots/chat-live.png) | ![Browser installer](.github/assets/screenshots/installer-live.png) |

The installer capture was produced from an isolated local copy with no configuration or installation lock; the already-installed demo correctly returns HTTP 410 for its installer endpoint.

Fallback UI mockups with fictional labels are also available as [SVG assets](.github/assets/screenshots/README.md).

---

## Table of Contents

- [English](#english)
  - [What's TropaTT](#whats-tropatt)
  - [Why TropaTT](#why-tropatt)
  - [Who it's for](#who-its-for)
  - [What's inside](#whats-inside)
  - [Feature overview](#feature-overview)
  - [AI — what it can do](#ai--what-it-can-do)
  - [Team chat](#team-chat)
  - [How people use it](#how-people-use-it)
  - [Automation & API](#automation--api)
  - [Connect your AI agents (MCP)](#connect-your-ai-agents-mcp)
  - [Self-hosted. Your server, your rules.](#self-hosted-your-server-your-rules)
  - [Getting started](#getting-started)
  - [FAQ](#faq)
  - [By the numbers](#by-the-numbers)
  - [Tech stack](#tech-stack)
  - [Project layout](#project-layout)
  - [Modules](#modules)
  - [Under the hood](#under-the-hood)
  - [Docs](#docs)
  - [Open-source project files](#open-source-project-files)
  - [Maintenance and contributor workflow](#maintenance-and-contributor-workflow)
  - [Security-sensitive areas](#security-sensitive-areas)
  - [AI-assisted maintenance](#ai-assisted-maintenance)
  - [Who built this](#who-built-this)
- [Русский](#русский)
  - [Что такое TropaTT](#что-такое-tropatt)
  - [Почему TropaTT](#почему-tropatt)
  - [Для кого](#для-кого)
  - [Что внутри](#что-внутри)
  - [Обзор возможностей](#обзор-возможностей)
  - [ИИ — что он умеет](#ии--что-он-умеет)
  - [Командный чат](#командный-чат)
  - [Как это используют](#как-это-используют)
  - [Автоматизация и API](#автоматизация-и-api)
  - [Подключение ИИ-агентов (MCP)](#подключение-ии-агентов-mcp)
  - [Свой сервер — свои правила](#свой-сервер--свои-правила)
  - [Установка](#установка)
  - [FAQ](#faq-1)
  - [В цифрах](#в-цифрах)
  - [Технологии](#технологии)
  - [Структура](#структура)
  - [Модули](#модули)
  - [Как устроено](#как-устроено)
  - [Документация](#документация)
  - [Файлы open-source проекта](#файлы-open-source-проекта)
  - [Сопровождение проекта](#сопровождение-проекта)
  - [Области, где важна безопасность](#области-где-важна-безопасность)
  - [Где помогает AI при сопровождении](#где-помогает-ai-при-сопровождении)
  - [Кто сделал](#кто-сделал)
- [中文](#中文)
  - [TropaTT 是什么](#tropatt-是什么)
  - [为什么 TropaTT](#为什么-tropatt)
  - [适合谁](#适合谁)
  - [功能](#功能)
  - [功能一览](#功能一览)
  - [AI — 能做什么](#ai--能做什么)
  - [团队聊天](#团队聊天)
  - [使用方式](#使用方式)
  - [自动化与 API](#自动化与-api)
  - [连接 AI 代理（MCP）](#连接-ai-代理mcp)
  - [自托管，你的规则](#自托管你的规则)
  - [安装](#安装)
  - [常见问题](#常见问题)
  - [数字说话](#数字说话)
  - [技术栈](#技术栈)
  - [结构](#结构)
  - [模块](#模块)
  - [内部原理](#内部原理)
  - [文档](#文档)
  - [开源项目文件](#开源项目文件)
  - [维护和贡献流程](#维护和贡献流程)
  - [安全敏感区域](#安全敏感区域)
  - [AI 辅助维护](#ai-辅助维护)
  - [谁做的](#谁做的)

---

## English

### What's TropaTT

TropaTT is a free, self-hosted, open-source PHP/MySQL work platform for client projects. It brings CRM, tasks, projects, Kanban, Gantt, calendar, team chat, knowledge base wiki, client portal, financial price lists, universal e-commerce CMS gateway, automation, REST API, OpenAPI 3.1, Model Context Protocol (MCP) server, and 20+ AI-assisted workflows into one unified system that you install on your own server.

It was built for people who manage real work every day: freelancers with many clients, small agencies shipping projects with a handful of people, service companies coordinating field work, e-commerce merchants managing multi-store orders, studios running campaigns, and teams tired of keeping clients in one app, tasks in another, chat somewhere else, and reports in a spreadsheet.

The practical difference is control. TropaTT does not charge per seat and does not add plan-based caps for users, tasks, projects, or clients. Your data, backups, integrations, and update decisions stay with you. The actual capacity still depends on your hosting, database, configuration, storage, and workload; a small team can start on basic $2–$3/month PHP/MySQL shared hosting and move to stronger infrastructure when it grows.

---

### Why TropaTT

Here's the problem. You have clients in one app. Tasks in another. Team chat in a third. Calendar in a fourth. A spreadsheet for tracking. Nothing talks to anything else. And then the cloud vendor raises prices, limits your seats, or goes down.

**TropaTT replaces all of that with one self-hosted system.**

- **CRM + task manager + project tracker in one place.** Client cards, task hierarchies, Kanban boards, Gantt timelines, team chat, knowledge base wiki, and client portal — all on the same data. No copying between apps. No "wait, where did we discuss that?"
- **Actual AI that helps you work.** Not a chatbot sidebar. AI idea analysis turns a sentence like "client wants a booking integration" into a full task hierarchy with subtasks and priorities. AI daily and weekly plans tell you what to focus on — based on your real deadlines and workload. It generates summaries, checklists, risk assessments, meeting briefs. Tools that save time, not gimmicks.
- **Built-in Model Context Protocol (MCP) server.** Connect Claude Code, Cursor, Codex, OpenDevin, ChatGPT, and other AI coding agents directly to your CRM with 621 tools and 6 resources under strict RBAC permissions.
- **Built-in team chat.** No Slack, no Discord, no extra subscription. Discussions live next to the work.
- **Universal E-Commerce Gateway.** Optional module (from the marketplace) with a canonical JSON contract and connectors for 11 e-commerce platforms (OpenCart 1.5–4.x, WooCommerce HPOS, Shopify, 1C-Bitrix, InSales, CS-Cart, PrestaShop, Shop-Script, Moguta, Tilda, Magento 2) with HMAC-SHA256 signatures, bi-directional sync, and idempotency.
- **No artificial SaaS limits.** No plan-based user caps, task caps, or project caps. Your real limits are your server resources, not a vendor pricing page.
- **Your data, your server.** Every client, task, file, chat message, and business record stays on your infrastructure. GDPR and 152-FZ compliance is directly under your control — not a vendor's promise.
- **Runs where PHP and MySQL run.** Use a local machine, home or office server, VPS, cloud VM, or shared hosting. For public hosting, a $2–$3/month PHP/MySQL plan is enough to start.
- **Zero external PHP dependencies.** No Laravel, no Symfony, no Doctrine, no Composer tree of 200 packages. The whole micro-kernel is hand-written. One codebase, not a hundred moving parts.
- **Install in a browser.** Upload files, open the installer, enter MySQL credentials, create an admin account. No terminal, no command line, no DevOps.

#### Comparison with alternatives

| Feature / Metric | TropaTT | Bitrix24 (Cloud/On-Premise) | Jira Software + Service Desk | HubSpot CRM | EspoCRM / SuiteCRM |
|---|---|---|---|---|---|
| **License & Price** | **100% Free & Open Source (AGPL-3.0)** | Free tier (very limited) or $49–$399+/mo | From $8.15–$16/user/mo | Free tier (very limited) or $50–$500+/user/mo | Free basic / $25+/user/mo for enterprise packs |
| **User & Seat Limits** | **Unlimited users & seats** | Capped by plan (5 / 50 / 100 / Enterprise) | Billed per seat | Billed per seat / contacts | Often requires paid extensions for team limits |
| **Server Footprint** | **Lightweight (PHP 8.1+, MySQL, no daemons)** | Heavy (4GB–16GB RAM, Java, Push daemon, Memcached) | Heavy (4GB–8GB RAM, Java JVM, Node.js) | SaaS only (no self-host) | Moderate (Node.js/Redis often required for realtime) |
| **Hosting Support** | **Any $2–$3/mo shared hosting (cPanel/DirectAdmin), VPS, bare metal** | Requires dedicated VPS/VDS or bare metal server | Requires dedicated VPS/VDS or Atlassian Cloud | SaaS only | VPS / Dedicated server |
| **External PHP/npm Deps** | **0 packages (Custom micro-kernel, no supply chain risk)** | Hundreds of proprietary libraries | Complex Java/JS stack | Proprietary SaaS | 100+ Composer/npm packages |
| **Integrated Suite** | **CRM + Tasks + Kanban + Gantt + Chat + Wiki + Client Portal + Rates** | Comprehensive but fragmented / complex UI | Tasks only (needs Confluence, Slack, CRM plugins) | CRM only (needs Jira, Slack, etc.) | CRM-centric (limited task/chat/Gantt capabilities) |
| **AI Workflows & MCP** | **Built-in MCP Server (621 tools) + 28 AI workflows (BYO keys, 0% markup)** | Proprietary CoPilot (expensive add-on) | Atlassian Intelligence (SaaS enterprise only) | HubSpot Breeze (expensive tier) | None or basic community OpenAI plugin |
| **E-Commerce Gateway** | **Connector module for 11 platforms (OpenCart, WooCommerce, Shopify, etc.)** | Built-in 1C-Bitrix store, paid marketplace apps | None (requires external Zapier/middleware) | Paid integrations | Limited community modules |
| **Data Sovereignty & Privacy**| **100% on your server (compliance under your control; telemetry stays in your database)** | Stored on vendor cloud or on-premise license | Stored on Atlassian Cloud (EU/US regions) | Stored on HubSpot Cloud | On-premise capable |

---

### Who it's for

TropaTT works for anyone managing clients and executing work — regardless of team size, industry, or role:

**By team size:**
- **Freelancers and solo professionals** managing 5–50 clients, who need task tracking, AI day planning, and complete project history in one place — without paying per seat.
- **Small teams (2–15 people)** that need a CRM, tasks, chat, and project visibility without a zoo of subscriptions.
- **Growing companies (15–100+ people)** that need roles, permissions, workflow automation, SLA, approvals, webhooks, and API integrations — without enterprise SaaS pricing.

**By industry:**
- Marketing and advertising agencies managing client campaigns, deadlines, and deliverables.
- IT companies and development teams tracking projects, bugs, releases, and repository events.
- E-commerce merchants and multi-channel retailers synchronizing orders, stock levels, and customer records across OpenCart, WooCommerce, Shopify, and marketplace storefronts.
- Design studios and creative agencies managing revisions, assets, and client approvals.
- Installation, construction, and field-service companies coordinating tasks across sites.
- Consulting, legal, and professional-services firms handling client engagements, hourly rates, and confidential documents.
- B2B service companies with counterparties, contracts, and repeatable work.
- Any team that needs both a CRM and a task manager — not just one of them.

**By role:**
- Founders and executives who need the big picture across clients, projects, and teams.
- Project managers planning timelines on Gantt, tracking milestones, and managing workload.
- Team leads assigning tasks, reviewing execution, and coordinating through built-in chat.
- Individual contributors who need a clear task list, a plan for the day, and a focused workspace.

---

### What's inside

**CRM.** Clients, counterparties, companies, contacts, organizations, departments, teams. Custom fields for your industry. Full history: every project, task, and communication tied to each client.

**Task manager.** Full hierarchy: parent tasks, subtasks, checklists. Statuses, priorities, due dates, assignees, tags. Task dependencies. WIP limits. Comments with file attachments and @mentions. Templates for recurring work. Human-readable task keys (PRJ-001). Mass actions when you need to update 20 tasks at once.

**Projects.** Milestones, risks, workload context, timeline views. Kanban boards for flow. Gantt charts for deadlines and dependencies. Project templates for repeatable delivery.

**Personal planning.** My Day and My Week views — for both solo prioritization and team coordination. AI-generated plans based on your actual tasks, deadlines, and calendar.

**Calendar.** Events linked to tasks and projects. Configurable working days, holidays, and business hours — used for SLA deadline calculation.

**Team chat.** Built in, not bolted on. Project chats, direct messages, group chats. File attachments, images, @mentions, replies. URL routing so you can link to a conversation. Real-time polling so new messages appear without losing your draft. More details [below](#team-chat).

**Knowledge Base & Wiki.** Multi-level category hierarchy, rich Markdown/WYSIWYG article authoring, article revision history, role-based read/edit permissions, and public sharing capability for client onboarding guides and SOPs.

**Client Portal & External Users.** Invite external client contacts and contractors as observers (read/comment) or executors (with time logging) on their specific projects. Isolated data boundaries ensure clients only ever see their own projects and never internal company discussions.

**Rates, Billing & Financial Tracking.** Named price lists for cost, billable, and contractor payout rates. Per-task rate overrides, automatic financial snapshots on logged time entries, and locked accounting periods to prevent retroactive modifications.

**Universal E-Commerce CMS Gateway (optional module).** Unified integration layer connecting 11 storefront platforms (OpenCart 1.5–4.x, WooCommerce HPOS, Shopify, 1C-Bitrix, InSales, CS-Cart, PrestaShop, Shop-Script, Moguta, Tilda, Magento 2) with HMAC-SHA256 signatures, bi-directional order/inventory sync, and customer profile linking.

**Notifications.** Real-time alerts for assignments, comments, mentions, deadlines, approvals. Push via browser API. History in the notification center.

**Analytics.** Dashboards, KPIs, workload analysis, risk signals, team capacity reports. All from real execution data, not manual entry.

**Admin panel.** Users, roles, permissions, statuses, priorities, SLA policies, workflow rules, webhooks, API clients, modules, audit logs, feature flags, rate limits, AI provider settings.

**Multilingual & Localization.** 7 built-in interface languages (English, Russian, Chinese, Spanish, Portuguese, German, French), native Right-to-Left (RTL) script support (Arabic, Hebrew, Persian, Urdu) with dynamic mirrored layouts, dedicated language management in admin panel (`web/admin-languages`), AST-validated Language Pack installation from ZIP or Marketplace, and one-click ZIP export.

**Data migration & integrations.** Move your work out of other trackers without starting over. One-way migration connectors pull boards, lists, projects, tasks, statuses, and users into TropaTT from Jira, Trello, Asana, Bitrix24, ClickUp, Todoist, Shtab, Worksection, Confluence, Kaiten, Toggl, ActiveCollab, Notion, and Linear. Google Calendar and Yandex Calendar sync keeps events in step; GitHub and GitLab sync issues and merge requests to tasks; Slack sends notifications; draw.io adds diagrams; Raycast connects via MCP.

**Ideas + AI analysis.** Capture a raw idea or client request. Let AI assess feasibility and risk. AI proposes a structured task hierarchy. Review and convert to real tasks with a click. "We should probably do something about client retention" → actionable plan in minutes.

---

### Feature overview

| Area | What you get | Why it matters |
|---|---|---|
| **CRM** | Clients, counterparties, companies, contacts, orgs | All business relationships in one place |
| **Tasks** | Hierarchy, subtasks, checklists, WIP limits, dependencies, templates, human-readable keys (PRJ-001) | One task tracker instead of a separate subscription |
| **Projects** | Milestones, risks, Gantt, workload context, templates | Delivery control with timeline and responsibility |
| **Kanban** | Drag-and-drop board for task flow | Visual status management, fewer bottlenecks |
| **Gantt** | Timeline with dependency-aware scheduling | Deadline visibility and resource planning |
| **Calendar** | Events, agenda, day/week views, business calendar | Scheduled work connected to task context |
| **Chat** | Built-in messenger — channels, DMs, attachments, mentions | Communication in the same tool as the work |
| **Knowledge Base** | Hierarchical categories, Markdown/WYSIWYG, revision history, permission-scoped articles | Centralized company SOPs, wikis, and client documentation |
| **Client portal** | Invite contacts as observers (read/comment) or executors (plus time logging) on their own projects | Clients and freelancers see exactly their part of the work — nothing else |
| **Rates & billing** | Cost/bill/payout rates via named price lists, per-task override, snapshots on time entries, locked periods | Know what work costs and what it earns — without spreadsheets |
| **E-Commerce Gateway** | 11 platform connectors (OpenCart, WooCommerce, Shopify, 1C-Bitrix and more; optional module), HMAC-SHA256, order/stock sync | Multi-store orders and stock synced with CRM tasks |
| **Notifications** | Real-time alerts, push, notification center | No missed deadlines, mentions, or approvals |
| **Analytics** | Dashboards, KPIs, workload, risks, team capacity | Decisions from real execution data |
| **Automation** | Workflow rules, SLA, approvals, webhooks, jobs | Less manual coordination, fewer errors |
| **AI (20+ tools)** | Idea analysis, plans, decomposition, summaries, checklists, risk review, meeting prep | AI that saves time in real workflows |
| **MCP Server** | 621 tools + 6 resources for Claude Code, Cursor, Codex, OpenDevin, ChatGPT | Connect autonomous AI agents directly to your data |
| **Modular SDK** | Drop-in modules, event bus (`ModuleEvents`), UI slot injection, DB migrations | Infinite customization without modifying core files |
| **Admin** | Users, roles, permissions, feature flags, modules, logs | Full control over your workspace |
| **Intake** | Capture, triage, and accept incoming client requests before turning them into tasks | Separate raw requests from real work, accept into tasks in one click |
| **Privacy** | Data stays on your server; outbound calls only for update checks and the marketplace (can be disabled) | Zero vendor lock-in, GDPR and 152-FZ under your control |
| **No plan caps** | Users, tasks, projects, clients, files are not capped by SaaS pricing | Scales with your infrastructure, not your bill |
| **Install** | Browser wizard for any PHP/MySQL host | First launch in minutes, no terminal |
| **Zero deps** | No external PHP packages, custom micro-kernel | No supply-chain risk, one codebase |

---

### AI — what it can do

TropaTT has more AI depth than most SaaS CRMs. Not because someone bolted a chatbot onto the sidebar, but because AI is integrated into the workflows where it actually makes you faster.

You bring your own provider keys (OpenAI, Anthropic, DeepSeek, Google, any compatible API). Everything runs server-side. Your business data never touches an AI service unless you explicitly configure it. Every suggestion is preview-before-apply — nothing changes automatically without your review.

**The standout feature: AI idea analysis.**

Here's how it works. You write a few sentences about an idea, client need, or problem. The AI evaluates scope, feasibility, risks, complexity. Then it proposes a concrete task hierarchy: parent tasks, subtasks, priorities, with reasoning. You review the proposal. One click converts it to real tasks.

Real example: _"Client wants a booking system integrated with their website."_ → AI proposes: research existing APIs (2 subtasks) → design integration architecture → implement booking endpoint → build frontend UI → integration tests → deployment checklist. What was a 30-minute manual planning session becomes a 30-second review-and-confirm.

**All 28 AI workflows:**

AI Idea Analysis · Task Decomposition · Daily Work Plan · Weekly Work Plan · Task Summary · Next Action Suggestions · Checklist Generation · Task Quality Review · Comment Draft Generation · Task Priority Ordering · Project Summary · Project Risk Summary · Project Client Report · Client Summary · Client Meeting Preparation · Client Data Quality Review · Analytics KPI Explanation · Analytics Risks Explanation · Team Workload Summary · Calendar Event Agenda · Dashboard Daily Digest · Semantic Search · Client Safe Report · Admin Log Review · Webhook Health Review · Workflow Rule Audit · Knowledge Summary · Knowledge Simplify

**AgentOS 2026 Engine Primitives:**
- **Model Context Protocol (MCP) Server:** Exposes **621 tools** and **6 resources** covering tasks, projects, clients, contacts, chats, calendar, analytics, and knowledge base.
- **Context Density Optimization:** Supports `density: "compact"` on list queries, stripping decorative metadata and reducing prompt token overhead by up to 85%.
- **Multi-step Task Orchestration (`crm_agent_bundle`):** Helps an AI agent create a parent task, definition of done (DoD) checklist items, and subtasks through ordered operations. Each step reports its result; callers must inspect partial outcomes.
- **Persistent Agent Memory (`crm_agent_memory`):** Multi-session memory store for AI agents with semantic search, entity graph linking, and export capabilities.
- **STORM Concurrency Control:** Optimistic locking via `row_version` prevents race conditions when multiple agents or human users modify records concurrently.

**How safety works:**
- Preview-only by default. No automatic writes to your data.
- All AI calls go through the backend API. Provider keys never reach the browser.
- Role-based access per AI capability.
- 40 feature flags for granular rollout.
- Rate and cost limits per workflow type.
- Raw prompts and sensitive context are not stored by default. Only sanitized metadata.

---

### Team chat

TropaTT has a real messenger inside the workspace. Not an integration, not an embed, not a separate subscription. It lives in the same system as your tasks, projects, and clients.

What you get:
- **Two-panel layout.** Conversations on the left, messages on the right.
- **Project and team channels.** Each project gets its own chat. General channels for company-wide stuff.
- **Direct messages.** One-on-one and group conversations.
- **Messages with attachments.** Text, files, images. @mentions with user search. Reply chains.
- **URL-routed chats.** Every conversation has its own URL. Link directly to a discussion.
- **Remembers where you were.** Restores your last active chat on page reload.
- **Live polling.** New messages appear automatically. Your draft stays intact.
- **Quick chat creation.** Search users by name, start a conversation instantly.
- **Participant controls.** Chat owners add and remove members.
- **Enter sends, Shift+Enter for new line.** Exactly what you expect.

The point: you stop asking "where did we discuss this?" because the discussion lives next to the task, the project, and the client context.

---

### How people use it

End-to-end cycle for client work, whether you're a team of 1 or 100:

1. **Capture** — an idea, client request, problem, or incoming lead.
2. **Analyze** — yourself or let AI break it down: scope, risks, feasibility, approach.
3. **Structure** — into projects, tasks, subtasks, checklists, assignees, deadlines.
4. **Coordinate** — through chat, comments, @mentions, notifications.
5. **Execute** — task lists, Kanban, My Day, My Week.
6. **Track** — Gantt, dashboards, analytics, workload, risk signals.
7. **Automate** — workflow rules, SLA policies, webhooks, approval chains.

**Real examples:**

- **Freelancer:** client inquiry → AI analyzes → structured task plan → My Day → execute → chat with client → done.
- **Agency:** client brief → AI decomposes → project + milestones → Kanban → Gantt tracking → client report → analytics.
- **Service company:** counterparty → project → install tasks → Gantt → daily plans → SLA monitoring → sign-off.
- **E-Commerce brand:** multi-store orders intake via CMS Gateway → automated task triage → fulfillment checklist → inventory sync back to store.
- **B2B ops:** company → contacts → tasks + approvals → reminders → webhook → dashboard.

---

### Automation & API

TropaTT's automation and API are production-grade. Built for teams that need the system to talk to the rest of their stack.

- **Universal E-Commerce Gateway (`crm.ecommerce-gateway`)** — canonical v1.0 JSON contract and connector suite for 11 platforms (OpenCart 1.5–4.x, 1C-Bitrix, WooCommerce HPOS, InSales, CS-Cart, PrestaShop, Shop-Script, Moguta, Tilda, Shopify, Magento 2) with HMAC-SHA256 signatures, bi-directional order sync, stock sync, and idempotency keys.
- **AgentOS 2026 Engine** — multi-step task orchestration (`crm_agent_bundle`), persistent agent memory (`crm_agent_memory` with search, entity graph linking, and export), STORM optimistic concurrency (`row_version`), and compact context density saving up to 85% LLM tokens.
- **Workflow rules** — trigger actions on conditions (status change, field update, time-based).
- **SLA management** — service level expectations with deadline tracking and breach alerts.
- **Approval flows** — multi-step decision chains for controlled changes.
- **Webhooks** — fire events to external systems when CRM records change (`task.created`, `task.updated`, `comment.added`, …; HMAC-SHA256 signed).
- **Agile Cycles & Sprints** — sprint tracking with velocity metrics, burndown charts, team capacity analysis, and scope changes.
- **Built-in Team & Project Chats** — direct messages, group chats, and project-client channels with real-time SSE streaming.
- **Client Portal & External Users** — role-based external sharing for knowledge pages and dedicated project channels.
- **API clients and keys** — programmatic access with scoped permissions.
- **Background jobs** — scheduled and queued for imports, exports, AI workflows.
- **Module system** — extend business logic without touching core. 19 CLI commands.
- **Generated REST API endpoints** — every entity, task, project, chat, calendar, analytic, and admin function accessible via API (984 core route records; modules add their own).
- **Zero Documentation Drift** — release gate strictly enforces 100% parity between routes.php and API documentation.
- **OpenAPI 3.1 spec** — generated from route config, never out of sync with reality.
- **MCP server — 621 tools, 6 resources** — a Model Context Protocol endpoint that connects Claude Code, Cursor, Codex, OpenDevin, and ChatGPT to the CRM with safe, permission-scoped access to your data (reference: [`docs_mcp/mcp_en.md`](docs_mcp/mcp_en.md)).

---

### Connect your AI agents (MCP)

TropaTT ships a **built-in MCP (Model Context Protocol) server** — the standard protocol understood by **Claude Code, Cursor, Codex, OpenDevin, ChatGPT, and other AI coding agents**. Point any MCP-compatible agent at your CRM and it can read, analyze, and manage your real data: tasks, projects, clients, contacts, chats, calendar, analytics, and the knowledge base — through a safe, permission-scoped layer.

- **621 MCP tools + 6 resources** — every domain is covered: tasks, projects, clients, contacts, chats, calendar, worklogs, analytics, knowledge base, and more.
- **AgentOS 2026 Core Support** — includes `crm_agent_bundle` for multi-step task/DoD/subtask orchestration with per-step results, `crm_agent_memory` for persistent cross-session knowledge storage with semantic search and entity linking, `crm_chat` for structured agent messaging, and `density: "compact"` for token savings.
- **Works with Claude Code, Cursor, Codex, OpenDevin, and ChatGPT.** Connect the agent to your installation the same way you connect it to any MCP server.
- **Same data, same rules as the web UI.** Every agent action goes through the same REST API and RBAC permission checks — no direct database access, no bypassing roles.
- **Safe by design.** Sensitive data (tokens, password hashes, API keys) is filtered out, write tools require the matching permission, and admin actions stay admin-only.
- **Endpoint:** `POST /api/index.php?route=api/v1/mcp`, authenticated with a Bearer token (your user token or a scoped API client key).

Full MCP reference (tools, authentication, RBAC): [`docs_mcp/mcp_en.md`](docs_mcp/mcp_en.md).

---

### Self-hosted. Your server, your rules.

TropaTT is open source. Deploy it on your own server. Inspect the code. Modify it. No license fees. No mandatory subscription.

Paid services (customization, integration, migration, support) exist as optional services. They're not required to use the software.

**Why self-hosting matters, practically:**

- **No vendor lock-in.** SaaS raises prices or shuts down, your data goes with it. TropaTT data lives on your server. Migrate, back up, move — anytime.
- **No artificial product limits.** Users, tasks, projects, and clients are not capped by a SaaS plan. The real ceiling is your hardware, database, storage, and configuration.
- **No one can block you.** Your access doesn't get suspended over a billing glitch or policy change. The system is yours.
- **Privacy and data sovereignty (you control where the data lives — compliance itself remains your responsibility):**
  - **European Union / Global:** All data resides on your designated host. No third-party tracking scripts or external analytics; frontend telemetry is written to your own database. Data purge is available for erasure requests.
  - **CIS & Russia:** Host in a Russian data center (Beget, TimeWeb, Selectel, Yandex Cloud, etc.) to keep personal data in the country. Optional modules add Yandex Calendar sync, a 1C-Bitrix store connector, and migrations from Bitrix24 and Shtab.
  - **APAC / China & Isolated Intranets:** Completely self-contained assets (Bootstrap 5, FontAwesome 6, SortableJS bundled locally in `upload/web/assets/`). Zero external CDN dependencies, zero blocked Google fonts. Runs seamlessly behind corporate firewalls and air-gapped intranets.
- **Cost control.** You can run TropaTT locally with no external hosting cost, deploy it on your own server, or start with a $2–$3/month PHP/MySQL shared hosting plan. Scale by upgrading infrastructure, not your SaaS plan.

---

### Getting started

Browser-based installer. No terminal, no composer, no npm. Designed for shared hosting, VPS, local servers, and simple PHP/MySQL deployments.

> **Where are the files?** All application files live in the **`upload/`** folder. The repository root contains only documentation and config. To install, copy the **contents of `upload/`** into your server document root (so that `index.php`, `api/`, `web/`, and `modules/` end up at the top of your web root).

**Get the code:**

- Clone the repository:
  ```bash
  git clone https://github.com/Anton-Barinov/TropaTT.git
  ```
- Or download a ZIP from GitHub (**Code → Download ZIP**), or a packaged archive from the [Releases](https://github.com/Anton-Barinov/TropaTT/releases) page when available.

**What you need:**
- PHP 8.1+
- An empty MySQL database (MySQL 8.0+ or MariaDB 10.4+)
- Any web server (Apache, Nginx, or PHP-compatible host)
- Write access for the `api/` config and `storage/` directories
- **A cron job** calling `web/cron.php` every minute (set `CRON_SECRET_KEY` in `api/.env` and send it as the `X-Cron-Key` header) — it drains the notification queue, runs the module scheduler (period auto-close, knowledge, cycles), and records a heartbeat so the admin panel can tell a working cron from a silent one. See [`SHARED_HOSTING_GUIDE.md`](SHARED_HOSTING_GUIDE.md)
- **Outbound HTTPS** from the server to browser push services (Firefox autopush, Google FCM) for web push notifications
- The **`openssl`** extension with `prime256v1` EC key support for VAPID push signing

**Steps:**
1. Copy the **contents of the `upload/` folder** (not the folder itself) to your server — `index.php`, `api/`, `web/`, and `modules/` must end up in your web root.
2. Create an empty MySQL database.
3. Open your domain in a browser. TropaTT detects it's not configured and launches the installer.
4. The installer checks your environment, asks for MySQL credentials, site URL, timezone, and the first admin account.
5. It writes `.env` in `api/`, creates the schema, seeds reference data (statuses, priorities, roles, permissions), creates the admin user, and locks the installer.
6. Log in. Start working.

**Shared hosting example:**
Upload the contents of `upload/` (`api/`, `web/`, `modules/`, `index.php`, …) → create a MySQL database in your hosting panel → open your domain → follow the installer → done.

---

### FAQ

**What exactly is TropaTT?**
A free, open-source, self-hosted CRM + task manager + project platform. PHP 8.1+ and MySQL. Runs on your server. Combines clients, tasks, projects, Kanban, Gantt, calendar, knowledge base wiki, client portal, financial price lists, universal e-commerce gateway, built-in chat, analytics, automation, and 20+ AI tools.

**CRM or task manager?**
Both. CRM for clients, counterparties, contacts, and companies. Full task manager with hierarchy, Kanban, Gantt, checklists, and daily planning. You don't need separate tools.

**How does TropaTT compare to Bitrix24 or Jira?**
Unlike Bitrix24, TropaTT has zero per-seat licensing, runs on a $2/month shared host (no Java or memory-hungry daemons), and is 100% open source. Unlike Jira, TropaTT combines CRM, client portal, internal messenger, and knowledge base natively in one unified application without requiring dozens of expensive marketplace add-ons.

**Can I run TropaTT in Docker or containerized environments?**
There is no official Docker image or `docker-compose.yml` yet. TropaTT only needs PHP 8.1+ and MySQL, so a standard PHP + MySQL container setup with the contents of `upload/` mounted as the web root is the expected way to run it in containers, but this setup is not officially tested.

**How do backups and disaster recovery work?**
Because TropaTT stores 100% of its data in a standard MySQL database and files in `upload/storage/`, complete backups take seconds:
1. Database: Standard `mysqldump -u <user> -p <dbname> > backup.sql` (or via phpMyAdmin / cPanel).
2. Files: Standard zip or rsync of `upload/storage/` and `api/.env`.
3. Automated Pre-Update Snapshots: Before applying any system update, the built-in update engine automatically creates a timestamped database and file backup with one-click rollback if an issue occurs.

**Can multiple users work simultaneously without data conflicts?**
STORM uses `row_version` to reject a stale update to the same record, preventing silent overwrites. This helps prevent one user's changes from silently replacing another's.

**What are the exact minimum hardware and server requirements?**
- CPU: 1 vCPU (1.0 GHz+).
- RAM: 512MB RAM.
- Disk Space: 100MB for core files + storage for uploaded project attachments.
- PHP: 8.1 or 8.2 with PDO, OpenSSL, mbstring, cURL.
- Database: MySQL 8.0+ or MariaDB 10.4+.
- Web Server: Apache (with mod_rewrite) or Nginx.
- Compatible environments: Any $2–$3/mo shared hosting (cPanel, DirectAdmin, Plesk, ISPmanager), VPS, or bare-metal server.

**How does the Client Portal protect internal business confidentiality?**
External client contacts and contractors are invited with scoped Observer or Executor roles bound strictly to their specific project. They cannot access internal company team chats, other projects, client lists, price lists, or financial rate sheets.

**How does the Knowledge Base (Wiki) work?**
Features multi-level category hierarchies, rich Markdown and WYSIWYG article authoring, complete revision history with audit tracking, granular read/edit permissions per role, and public sharing links for client-facing guides and onboarding documentation.

**Can I connect multiple online stores (OpenCart, WooCommerce, Shopify)?**
Yes, with the optional Universal E-Commerce CMS Gateway module (`crm.ecommerce-gateway`, installed from the marketplace) supporting 11 platforms. It connects multiple storefronts, streams incoming orders into CRM tasks, maps customer records, synchronizes inventory levels, and fires HMAC-SHA256 authenticated webhooks.

**Can a freelancer use this?**
Yes. Minimum team size: 1. Manage clients, track tasks, plan your day with AI, analyze ideas — one tool, no per-seat pricing.

**Works on shared hosting?**
Yes. Standard PHP 8.1+/MySQL shared hosting ($2–$3/month) is enough. The browser installer handles everything.

**What can the AI do?**
28 workflows: idea analysis (turns a paragraph into a task plan), daily/weekly plans, task decomposition, summaries, checklists, risk reviews, meeting prep, and more. You bring your AI provider keys. Processing is server-side. AI never modifies data without your review.

**How does AI idea analysis work?**
You describe an idea → AI evaluates scope/risks/complexity → AI proposes a structured task hierarchy → you review → one click to convert to real tasks.

**Can AI agents like Claude Code, Cursor, or ChatGPT manage my CRM?**
Yes. TropaTT includes a built-in MCP (Model Context Protocol) server with 621 tools and 6 resources. Point your AI agent to `POST /api/index.php?route=api/v1/mcp` with a Bearer token. The agent can search, create, and update tasks, counterparties, knowledge articles, and chats under the exact same RBAC permissions as human users. Details: [`docs_mcp/mcp_en.md`](docs_mcp/mcp_en.md).

**How do I build a custom module?**
A stock installation ships **without** modules: `upload/modules/` holds only its `.htaccess`, and modules are installed on demand from the marketplace (`marketplace.tropatt.com`) via **Administration → Modules → Marketplace** or by copying a package into that directory. The example modules live in `docs_modules/examples/modules/`. Modules live in `upload/modules/<module-name>/`. Each module contains a `manifest.json`, a `ServiceProvider.php` (for DI container binding), event listeners (`ModuleEvents`), UI slot injections (`PositionRegistry`), and transactional database migrations (`up()`/`down()`). Complete step-by-step developer tutorial: [`docs_modules/modules_en.md`](docs_modules/modules_en.md).

**Where's my data?**
On your server. TropaTT does not sync your data to any cloud and the developer has no access to your installation. By default the server only calls out to check for updates (`update.tropatt.com`) and to read the module marketplace catalog; both can be disabled in `api/config/update.php` / environment settings.

**User limits? Task limits?**
There are no plan-based caps. You can create as many users, tasks, projects, and clients as your server can handle.

**Does that mean unlimited performance?**
No. TropaTT removes vendor-side limits, not physics. Performance depends on PHP hosting, MySQL configuration, storage, indexes, background jobs, file volume, and concurrent users.

**Is commercial use allowed?**
Yes. TropaTT is released under the AGPL-3.0 license. You are free to use it commercially for your business, agency, and clients with zero fees.

**API access?**
Generated REST API endpoints (984 core route records; modules add their own). OpenAPI 3.1 spec generated from code. Every feature is programmable.

**Can I customize it?**
Yes. PHP/MySQL stack, modules, REST API, webhooks, workflow rules, custom fields, roles, permissions.

**How do updates work?**
Updates are installed from the admin panel (**Admin → System Updates**, no SSH or Composer needed). An update server (`update.tropatt.com`) builds and signs ready packages from GitHub on a cron; your CRM downloads the package, verifies the signature, runs a safety preflight, creates a backup, applies files and database migrations, and can roll back from that backup if anything goes wrong. Modules are no longer part of the core package: they are installed and updated from the marketplace (**Admin → Modules → Marketplace**). Details: [`UPDATES.md`](UPDATES.md).

**Who built this?**
**Barinov Anton**, PHP developer. Creator of TropaTT.

---

### By the numbers

| Metric | Value |
|---|---|
| API endpoints | 984 core route records (installed modules add their own routes) |
| MCP tools | 621 tools + 6 resources — Model Context Protocol server for AI agents |
| Web routes | ~70 pages |
| Backend services | 139 |
| Repositories | 114 |
| Domain modules | 35+ |
| Optional modules (marketplace) | 24 — incl. 14 migrations from Jira, Trello, Asana, Bitrix24, ClickUp, Todoist, Shtab, Worksection, Confluence, Kaiten, Toggl, ActiveCollab, Notion, Linear; GitHub, GitLab, Slack; Google & Yandex Calendar; WIP limits; draw.io; Raycast; E-Commerce Gateway. The stock install ships no modules. |
| E-Commerce Connectors | 11 storefront platforms (optional module) (OpenCart 1.5–4.x, WooCommerce HPOS, Shopify, 1C-Bitrix, InSales, CS-Cart, PrestaShop, Shop-Script, Moguta, Tilda, Magento 2) |
| JS modules | 44 custom vanilla JS modules, no SPA framework, no build step |
| Public CI | PHP lint on 8.1 and 8.2, client-portal security contract, OpenAPI consistency, web frontend unit tests |
| AI endpoints | 65 |
| AI workflows | 28 |
| Feature flags | 40 |
| Frontend API coverage | Tracked against the generated route inventory |
| External PHP deps | 0 |
| Frontend vendor libs | 3 (Bootstrap 5, FA6, SortableJS) |
| OpenAPI tooling | `upload/api/scripts/generate_openapi.php` |
| Module CLI commands | 19 |
| Interface languages | 7 — English, Русский, Deutsch, Español, Français, Português, 中文 |
| Deployment options | Local machine, home/office server, VPS, cloud VM, shared hosting |
| External hosting starting point | ~$2–$3/month shared hosting |

---

### Tech stack

- **Backend:** PHP 8.1+, custom micro-kernel. Zero external packages. No Laravel/Symfony/Doctrine.
- **Database:** MySQL 8.0+ or MariaDB 10.4+.
- **Frontend:** PHP-rendered MPA with Bootstrap 5 for UI/layout and custom vanilla JS ES5+ modules for behavior. No React/Vue/Angular. No build step. No bundler.
- **Architecture:** API-first. Web UI uses REST API for all data. Zero direct database access from the web layer.
- **Security:** Dual auth (cookie + CSRF for web, Bearer for API). Granular RBAC. SSRF protection. Rate limiting. File quarantine. Admin impersonation. Sanitized error responses.
- **Testing:** Public CI runs PHP lint, a client-portal security contract check, OpenAPI route coverage validation, and web frontend unit tests. The broader integration suite remains local-only because it is excluded from public packages.
- **AI layer:** Configurable providers (OpenAI, Anthropic, DeepSeek, Google, compatible). Intent-based workflows. Prompt templates. JSON Schema validation. Preview-before-apply.
- **Docs:** Maintainer docs are kept local and are not published. OpenAPI generation tooling is included in `upload/api/scripts/generate_openapi.php`.

---

### Project layout

```text
TropaTT/
├── upload/         # The CRM itself — copy the CONTENTS of this folder to your server
│   ├── api/        #   API core — controllers, services, repositories, config, migrations, scripts
│   ├── web/        #   Web UI — installer, pages, templates, JS modules, assets
│   ├── modules/    #   Empty in the stock install (only .htaccess) — modules are installed from the marketplace
│   └── index.php   #   Root entry point
├── README.md       # You're reading it (docs and config stay at the repo root)
└── ...             # Other .md docs, LICENSE, .github/, .gitignore
```

Backend modules organized in 9 groups: Auth/Users · CRM (clients, counterparties, contacts) · Projects/Tasks · Planning (calendar, recurring, reminders) · Communication (chats, notifications, push) · Automation (workflows, SLA, webhooks) · Analytics (dashboards, reports) · AI/LLM (11 modules: providers, intents, suggestions, actions, jobs, prompts, schemas, usage, retention, semantic, context builders) · Admin (settings, logs, audit, flags, modules, storage, trash, search).

---

### Modules

TropaTT features a fully decoupled, hot-pluggable modular subsystem. Modules can register custom services in the DI container, listen to core synchronous lifecycle events, inject HTML/JS/CSS into 14 UI slots, execute transactional database migrations, and register console commands.

**5 Extension Pillars:**
1. **Manifest (`manifest.json`):** Semantic versioning, system compatibility, dependencies.
2. **Service Provider (`ServiceProvider.php`):** Clean dependency injection bindings.
3. **Event Bus (`ModuleEvents`):** Lifecycle hooks across core operations (`task.created`, `task.status_changed`, `client.updated`, etc.).
4. **UI Slot Injection (`PositionRegistry`):** 14 template slots to extend the UI without modifying core views.
5. **Database Migrations (`up()` & `down()`):** Automated schema updates with safe rollbacks.

> **Developer Guide:** Read the complete [Module Development Guide](docs_modules/modules_en.md) ([Русский](docs_modules/modules_ru.md) · [中文](docs_modules/modules_zh.md)) for code templates, testing practices, and packaging instructions.

The stock installation ships **no modules**. All of them are published on the marketplace and install with one click from **Admin → Modules → Marketplace**. Each integration module also has its own repository (MIT):

| Module | Repository |
|---|---|
| `crm.activecollab-migration` | [tropatt-module-activecollab-migration](https://github.com/Anton-Barinov/tropatt-module-activecollab-migration) |
| `crm.asana-migration` | [tropatt-module-asana-migration](https://github.com/Anton-Barinov/tropatt-module-asana-migration) |
| `crm.bitrix24-migration` | [tropatt-module-bitrix24-migration](https://github.com/Anton-Barinov/tropatt-module-bitrix24-migration) |
| `crm.clickup-migration` | [tropatt-module-clickup-migration](https://github.com/Anton-Barinov/tropatt-module-clickup-migration) |
| `crm.confluence-migration` | [tropatt-module-confluence-migration](https://github.com/Anton-Barinov/tropatt-module-confluence-migration) |
| `crm.drawio` | [tropatt-module-drawio](https://github.com/Anton-Barinov/tropatt-module-drawio) |
| `crm.github-integration` | [tropatt-module-github-integration](https://github.com/Anton-Barinov/tropatt-module-github-integration) |
| `crm.gitlab-integration` | [tropatt-module-gitlab-integration](https://github.com/Anton-Barinov/tropatt-module-gitlab-integration) |
| `crm.google-calendar` | [tropatt-module-google-calendar](https://github.com/Anton-Barinov/tropatt-module-google-calendar) |
| `crm.jira-migration` | [tropatt-module-jira-migration](https://github.com/Anton-Barinov/tropatt-module-jira-migration) |
| `crm.kaiten-migration` | [tropatt-module-kaiten-migration](https://github.com/Anton-Barinov/tropatt-module-kaiten-migration) |
| `crm.linear-migration` | [tropatt-module-linear-migration](https://github.com/Anton-Barinov/tropatt-module-linear-migration) |
| `crm.notion-migration` | [tropatt-module-notion-migration](https://github.com/Anton-Barinov/tropatt-module-notion-migration) |
| `crm.raycast` | [tropatt-module-raycast](https://github.com/Anton-Barinov/tropatt-module-raycast) |
| `crm.shtab-migration` | [tropatt-module-shtab-migration](https://github.com/Anton-Barinov/tropatt-module-shtab-migration) |
| `crm.slack-integration` | [tropatt-module-slack-integration](https://github.com/Anton-Barinov/tropatt-module-slack-integration) |
| `crm.todoist-migration` | [tropatt-module-todoist-migration](https://github.com/Anton-Barinov/tropatt-module-todoist-migration) |
| `crm.toggl-migration` | [tropatt-module-toggl-migration](https://github.com/Anton-Barinov/tropatt-module-toggl-migration) |
| `crm.trello-migration` | [tropatt-module-trello-migration](https://github.com/Anton-Barinov/tropatt-module-trello-migration) |
| `crm.wip-limit` | [tropatt-module-wip-limit](https://github.com/Anton-Barinov/tropatt-module-wip-limit) |
| `crm.worksection-migration` | [tropatt-module-worksection-migration](https://github.com/Anton-Barinov/tropatt-module-worksection-migration) |
| `crm.yandex-calendar` | [tropatt-module-yandex-calendar](https://github.com/Anton-Barinov/tropatt-module-yandex-calendar) |

---

### Under the hood

**Zero external PHP dependencies.** Router, DI container, autoloader, query builder (no ORM), validator, HTTP client, response handler, migration manager, and module system are hand-written. One `composer.json` with `php >=8.1`. No supply-chain risk. No version conflicts. No dependency audit debt.

**Documented architecture decisions:**
ADR-001 — custom micro-kernel, no framework.
ADR-002 — single JSON response envelope for all API calls.
ADR-003 — no ORM, PDO + Repository pattern.
ADR-001 Web — custom PHP MVC.
ADR-003 Web — custom vanilla JS, Bootstrap 5 UI, no build step.
ADR-006 Web — server-side session verification (cookie + CSRF).

**API-first.** The web UI does not touch the database. Every data load and state change goes through `window.CRM.api.request` → `/api/v1/...`. The API is authoritative. The UI is one consumer.

**Testing.** Public CI runs PHP syntax checks on PHP 8.1 and 8.2, a client-portal security contract check, an OpenAPI route-consistency check, and web frontend unit tests. The broader MySQL integration suite is local-only; contributors can run the public checks with the commands documented in `CONTRIBUTING.md`.

---

### Docs

The public repository currently includes a focused maintainer documentation set:

| Layer | Where | What |
|---|---|---|
| Maintainer docs | kept local (not published) | Release checklist, security review checklist, Codex for OSS notes, starter issues, GitHub labels |
| API tooling | `upload/api/scripts/generate_openapi.php` | OpenAPI generation entry point for API documentation automation |
| API reference | [English](docs_api/api_en.md) · [Русский](docs_api/api_ru.md) · [中文](docs_api/api_zh.md) | Complete REST API reference — endpoints, authentication, RBAC, and conventions (English / Русский / 中文) |
| MCP reference | [English](docs_mcp/mcp_en.md) · [Русский](docs_mcp/mcp_ru.md) · [中文](docs_mcp/mcp_zh.md) | Complete MCP server reference — 621 tools, resources, authentication, and RBAC (English / Русский / 中文) |
| Module developer guide | [English](docs_modules/modules_en.md) · [Русский](docs_modules/modules_ru.md) · [中文](docs_modules/modules_zh.md) | Complete module development guide — manifests, service providers, event bus, UI slots, and migrations (English / Русский / 中文) |
| Web docs | [`UPDATES.md`](UPDATES.md) | Self-update system reference: update server pipeline and the user update flow |
| Project root | `README.md`, `SECURITY.md`, `CONTRIBUTING.md`, [`MODULE_DEVELOPMENT.md`](MODULE_DEVELOPMENT.md), [`INSTALL_TROUBLESHOOTING.md`](INSTALL_TROUBLESHOOTING.md), [`SHARED_HOSTING_GUIDE.md`](SHARED_HOSTING_GUIDE.md), [`WEBHOOK_SECURITY.md`](WEBHOOK_SECURITY.md) | Public usage, security, contribution, module development, installation troubleshooting, shared hosting, and webhook security guidance |

---

### Open-source project files

The public repository includes standard project files for maintainers, contributors, security reports, and early adopters:

- [LICENSE](LICENSE) — AGPL-3.0 license.
- [CONTRIBUTING.md](CONTRIBUTING.md) — contribution workflow, checks, PR expectations, security checklist.
- [SECURITY.md](SECURITY.md) — vulnerability reporting, supported versions, disclosure policy.
- [`MODULE_DEVELOPMENT.md`](MODULE_DEVELOPMENT.md) — complete guide to building pluggable modules (manifest, service provider, events, positions, assets).
- [`INSTALL_TROUBLESHOOTING.md`](INSTALL_TROUBLESHOOTING.md) — fixes for PHP extensions, MySQL permissions, web server configs, and common errors.
- [`SHARED_HOSTING_GUIDE.md`](SHARED_HOSTING_GUIDE.md) — running on shared hosting (Apache, Nginx, LiteSpeed), `.htaccess` rules, cron configuration.
- [`WEBHOOK_SECURITY.md`](WEBHOOK_SECURITY.md) — webhook authentication, signature verification, replay protection, and retry policies.
- [`UPDATES.md`](UPDATES.md) — how the one-click self-update system works, signature verification, and rollback flow.

---

### Maintenance and contribution

TropaTT uses automated quality checks to help maintain a stable codebase. See [CONTRIBUTING.md](CONTRIBUTING.md) for public contribution guidance.

Basic checks available in a public clone:

```bash
find . -name "*.php" -not -path "./upload/vendor/*" -not -path "./upload/modules/*" -print0 | xargs -0 -n1 php -l
php upload/api/scripts/generate_openapi.php
php upload/api/scripts/api_coverage_check.php
```

Commit messages follow Conventional Commits (`feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`).
---

### Security-sensitive areas

When contributing code, pay special attention to these security-critical layers:

1. **Authentication & Sessions:** Dual-auth architecture — cookie-based session with CSRF validation for the web UI, Bearer tokens for the API. Never bypass CSRF on state-changing web routes.
2. **Authorization (RBAC):** Every API endpoint checks permissions through `$this->authService->requirePermission(...)`. Never assume an authenticated user has admin access.
3. **Database Queries:** Always use prepared statements via the built-in `Database` PDO wrapper. Never concatenate user input into SQL queries.
4. **File Uploads & Storage:** Uploads pass MIME-type validation, size limits, and quarantine checks. Uploaded files are stored outside web-executable directories.
5. **SSRF Protection:** Outbound HTTP requests (webhooks, push notifications) validate target IPs to prevent SSRF against internal network endpoints.
6. **API Input Validation:** All controller endpoints validate input types, lengths, and required fields before processing.

---

### AI-assisted maintenance

TropaTT is designed to be easily maintained and extended by developers working alongside AI coding assistants:

- **Strict architectural conventions:** Clean separation of concerns (Controller → Service → Repository). No hidden magic or reflection hacks.
- **Self-contained micro-kernel:** An AI assistant can read the entire core framework without needing external library knowledge or guessing vendor behavior.
- **Consistent API response format:** Every endpoint returns `{ success: bool, data?: ..., error?: ... }`, making client-side code and tests completely predictable.
- **Machine-readable OpenAPI spec:** Tools like Claude Code, Cursor, Codex, and Copilot can ingest `openapi.json` to instantly understand all available endpoints and parameters.
- **Built-in MCP Server:** Connect your AI directly to the application via Model Context Protocol (621 tools) to query data, inspect configurations, and assist in day-to-day operations.

---

### Who built this

TropaTT is created and actively maintained by **Anton Barinov** — PHP developer and architect.

- **GitHub:** [@Anton-Barinov](https://github.com/Anton-Barinov)
- **Website:** [tropatt.com](https://tropatt.com)
- **Live Demo:** [demo.tropatt.com](https://demo.tropatt.com)

If you find TropaTT useful for your business or agency, consider starring the repository on GitHub!

---

### Copyright and attribution

**Copyright © 2026 Anton Barinov.**

TropaTT is free software released under the [GNU AGPL-3.0](LICENSE): you may use, study, modify and share it — including commercially — provided the source of derived deployments stays available and the license terms are kept.

**Removing, hiding, altering or renaming the author's copyright notices and attribution in this project is prohibited.** That covers, without limitation:

- the `LICENSE` (AGPL-3.0) text and any copyright line attached to it;
- the author credit in this README («Who built this» / «Кто сделал» / «谁做的») and the `Copyright © Anton Barinov` notice in documentation, release notes and package manifests;
- copyright and author headers inside source files, module manifests and installer output;
- the author's name, project name and attribution strings rendered by the UI or printed by the CLI.

Every fork, mirror, downstream packaging and derivative deployment must keep those notices intact and must not present the work as authored by someone else. Derivative works must not imply that the original author endorses or supports them. Nothing here restricts the rights the AGPL-3.0 grants you; it only asks that authorship stays visible wherever the code travels.

Questions about attribution in a specific context: open an issue before publishing.

## Русский

### Что такое TropaTT

TropaTT — это бесплатная self-hosted CRM и платформа управления работой с открытым исходным кодом на PHP и MySQL. В одной системе собраны CRM, задачи, проекты, Канбан, Гант, календарь, командный чат, база знаний (Wiki), клиентский портал, финансовый учет ставок и прайс-листов, универсальный e-commerce CMS шлюз, автоматизация, REST API, OpenAPI 3.1, Model Context Protocol (MCP) сервер и 20+ ИИ-процессов. Всё это разворачивается на вашем сервере, VPS, локальной машине или обычном PHP-хостинге — без оплаты за каждого пользователя и без тарифных лимитов.

**Бесплатно навсегда — без подвоха.** TropaTT на 100% бесплатна и имеет открытый исходный код (AGPL-3.0): нет лицензионных платежей, подписок, оплаты за рабочее место и тарифных ограничений. Вы платите только за выбранный хостинг — или вообще ничего, если ставите её на свою машину.

Проект создан для людей, которые каждый день ведут реальную работу: фрилансеров с десятками клиентов, небольших агентств, сервисных компаний, интернет-магазинов с несколькими витринами, выездных бригад, студий и команд, которым надоело держать клиентов в одной системе, задачи во второй, чат в третьей, а отчёты — в таблицах. Полноценное решение задачи импортозамещения зарубежных сервисов (Jira, Confluence, Asana, Notion, Trello, ClickUp, Slack).

Главная идея — контроль. В TropaTT нет оплаты за каждого пользователя и нет тарифных ограничений на количество пользователей, задач, проектов или клиентов. Данные, бэкапы, интеграции и решение об обновлениях остаются у вас. При этом производительность не бесконечная: реальный предел зависит от хостинга, базы данных, настроек, файлов и нагрузки. Малой команде достаточно начать с недорогого PHP/MySQL-хостинга (от 150–250 ₽/мес), а при росте перейти на более мощную инфраструктуру.

---

### Почему TropaTT

Проблема вот в чём. Клиенты — в одном приложении. Задачи — в другом. Чат команды — в третьем. Календарь — в четвёртом. Таблица для учёта. Ничего не связано между собой. А потом облачный провайдер поднимает цены, урезает лимиты, или случается сбой.

**TropaTT заменяет этот хаос одной самостоятельной системой:**

- **CRM + Таск-менеджер + Проектный трекер в одном инструменте.** Карточки клиентов, иерархии задач, Канбан-доски, диаграммы Ганта, встроенный командный чат, база знаний и клиентский портал работают на одних данных. Никакого копирования между приложениями. Никакой потери контекста.
- **20+ ИИ-инструментов, которые реально помогают работать.** AI-проработка идей превращает сырую мысль в структурированный план задач. AI-план на день подсказывает приоритеты. AI генерирует сводки, декомпозиции, чеклисты, оценки рисков, подготовку к встречам — не покидая рабочее пространство.
- **Встроенный сервер Model Context Protocol (MCP).** Подключайте Claude Code, Cursor, Codex, OpenDevin, ChatGPT и других ИИ-агентов напрямую к CRM (621 инструментов, 6 ресурсов) с разделением прав доступа (RBAC).
- **Встроенный командный чат.** Обсуждайте проекты и задачи там же, где идёт работа. Никакого Slack, Discord или отдельной подписки на мессенджер.
- **Универсальный E-Commerce CMS Шлюз.** Канонический JSON-контракт и набор коннекторов для 11 платформ (OpenCart 1.5–4.x, 1С-Битрикс, WooCommerce HPOS, InSales, CS-Cart, PrestaShop, Shop-Script, Могута, Tilda, Shopify, Magento 2) с HMAC-SHA256 подписями, двусторонней синхронизацией заказов и остатков.
- **Без искусственных SaaS-лимитов.** Пользователи, задачи, проекты и клиенты не ограничены тарифным планом. Реальные ограничения задаёт ваш сервер, база данных, хранилище и настройки.
- **Полная приватность.** Клиенты, задачи, файлы, чаты и бизнес-данные остаются на вашем сервере в выбранной юрисдикции — выполнение 152-ФЗ и GDPR под вашим контролем. Никаких внешних трекеров и сторонних облаков.
- **Работает везде, где есть PHP и MySQL.** Локальный компьютер, домашний или офисный сервер, VPS, облачная VM или недорогой шаред-хостинг.
- **Ноль внешних PHP-зависимостей.** Никаких Laravel, Symfony, Doctrine, Composer-дерева из сотен пакетов. Всё микроядро написано вручную. Вы разворачиваете одну надежную кодовую базу.
- **Установка через браузер.** Загрузите файлы, откройте установщик в браузере, введите данные MySQL, создайте администратора. Без терминала, командной строки и DevOps.

#### Сравнение с аналогами

| Параметр / Функция | TropaTT | Битрикс24 (Облако/Коробка) | Jira Software + Service Desk | HubSpot CRM | EspoCRM / SuiteCRM |
|---|---|---|---|---|---|
| **Лицензия и стоимость** | **100% Бесплатно и Open Source (AGPL-3.0)** | Бесплатный тариф сильно урезан / от 1 990 до 13 990+ ₽/мес | От $8.15–$16/пользователь/мес | От $50–$500+/мес | Бесплатная база / платные пакеты расширений |
| **Ограничения по пользователям** | **Без ограничений (0 ₽ за рабочее место)** | Лимиты по тарифам (5 / 50 / 100 / Enterprise) | Оплата за каждого пользователя | Оплата за пользователей и контакты | Часто требует покупки Enterprise-расширений |
| **Системные требования** | **Лёгкая (PHP 8.1+, MySQL, без демонов)** | Высокие (от 4–8GB RAM, Java, Push-демон, Redis) | Высокие (от 4–8GB RAM, Java JVM, Node.js) | Только облако (нет on-premise) | Средние (требует Node.js/Redis для очередей) |
| **Поддержка хостинга** | **Любой шаред-хостинг от 150 ₽/мес (cPanel/ISPmanager), VPS, сервер** | Требуется мощный VPS/VDS или выделенный сервер | Требуется выделенный VPS или Atlassian Cloud | Только SaaS | VPS / Выделенный сервер |
| **Внешние PHP/npm зависимости** | **0 пакетов (Собственное микроядро, защита от supply-chain)** | Сотни проприетарных библиотек | Сложный стек Java/JS | Закрытый SaaS | 100+ пакетов Composer/npm |
| **Единый комбайн** | **CRM + Задачи + Канбан + Гант + Чат + База знаний + Портал + Прайсы** | Комплексный, но перегруженный интерфейс | Только задачи (нужны Confluence, Slack, CRM) | Только CRM (нужны Jira, Slack и др.) | Фокус на CRM (слабые задачи/чат/Гант) |
| **ИИ и протокол MCP** | **Встроенный MCP-сервер (621 инструментов) + 28 ИИ-процесса (свои ключи, 0% наценки)** | Проприетарный CoPilot (платные пакеты) | Atlassian Intelligence (только enterprise) | HubSpot Breeze (дорогие тарифы) | Нет или базовый плагин сообщества |
| **E-Commerce интеграции** | **Модуль-коннектор для 11 CMS (OpenCart, 1С-Битрикс, InSales, WooCommerce и др.)** | Встроенный магазин 1С-Битрикс, платные модули | Нет (требуется Zapier/самописный шлюз) | Платные интеграции | Ограниченные сторонние модули |
| **Суверенитет данных** | **100% на вашем сервере (соответствие законам — под вашим контролем; телеметрия остаётся в вашей базе)** | Хранение в облаке вендора или в коробке | Atlassian Cloud (серверы за пределами РФ) | Облако HubSpot | Доступен self-hosted |

---

### Для кого

TropaTT подходит всем, кто управляет клиентами и исполняет работу — независимо от размера команды, отрасли или роли:

**По размеру команды:**
- **Фрилансеры и соло-предприниматели** с 5–50 клиентами, которым нужен учёт задач, планирование дня с ИИ и вся история проектов в одном месте — без оплаты за каждое рабочее место.
- **Малые команды (2–15 человек)**, которым нужна CRM, задачи, чат и прозрачность проектов без зоопарка подписок.
- **Растущие компании (15–100+ человек)**, которым нужны роли, права доступа, автоматизация, SLA, согласования, вебхуки и API-интеграции — без ценников enterprise SaaS.

**По отрасли:**
- Маркетинговые и рекламные агентства, управляющие клиентскими кампаниями, сроками и результатами.
- IT-компании и команды разработки, отслеживающие проекты, баги, релизы и коммиты.
- Интернет-магазины и ритейлеры, синхронизирующие заказы, остатки и клиентскую базу из OpenCart, 1С-Битрикс, WooCommerce, InSales, Tilda и маркетплейсов.
- Дизайн-студии и креативные агентства, управляющие правками, активами и клиентскими согласованиями.
- Монтажные, строительные и выездные сервисные компании, координирующие задачи по объектам.
- Консалтинг, юрфирмы и профессиональные услуги, ведущие клиентские дела, учет почасовых ставок и документы.
- B2B-сервисные компании с контрагентами, договорами и повторяющейся работой.
- Любые команды, которым нужна и CRM, и таск-менеджер — а не что-то одно.

**По роли:**
- Основатели и руководители, которым нужна картина происходящего по клиентам, проектам и командам.
- Проджект-менеджеры, планирующие сроки по Ганту, отслеживающие вехи и управляющие загрузкой.
- Тимлиды, распределяющие задачи, контролирующие исполнение и координирующие через встроенный чат.
- Исполнители, которым нужен понятный список задач, план на день и сфокусированное рабочее пространство.

---

### Что внутри

**CRM и управление клиентами.** Карточки клиентов, контрагенты, компании, контакты, организации, отделы, команды. Настраиваемые поля под вашу отрасль. Детальные страницы клиентов с историей проектов, задач и коммуникаций. Управление контрагентами для B2B-отношений с заказчиками, подрядчиками, партнёрами и поставщиками.

**Таск-менеджер и исполнение.** Полная иерархия задач: родительские задачи, подзадачи, чеклисты. Статусы, приоритеты, сроки, исполнители, теги. Комментарии с вложениями и @упоминаниями. Шаблоны задач для повторяющейся работы. Зависимости между задачами. WIP-лимиты для предотвращения перегрузки. Массовые действия.

**Управление проектами.** Страницы проектов с вехами, рисками, контекстом загрузки и временными шкалами. Канбан-доски для потокового исполнения. Диаграммы Ганта для обзора сроков и зависимостей. Шаблоны проектов.

**Персональное планирование.** «Мой день» и «Моя неделя» — для индивидуальной и командной приоритизации. AI-планы на день и неделю на основе ваших реальных задач, сроков и календаря.

**Календарь.** События с привязкой к задачам и проектам. Повестка и обзор расписания. Настраиваемые рабочие дни, праздники и рабочие часы для расчёта SLA-сроков.

**Встроенный командный чат.** Полный CRM-мессенджер: чаты проектов, личные чаты, группы. Сообщения, вложения, изображения, @упоминания, ответы, URL-роутинг, живой polling. Не нужен Slack, Discord или Telegram.

**База знаний и Wiki.** Иерархическая структура разделов и статей, форматирование Markdown и WYSIWYG, версионирование статей с историей изменений, гибкое разграничение прав чтения/редактирования и возможность публичного шаринга для клиентских инструкций.

**Клиентский портал и внешние пользователи.** Приглашение представителей клиентов и субподрядчиков с изолированными правами наблюдателя (просмотр и комментарии) или исполнителя (с логированием времени) только в разрешенные проекты. Клиенты никогда не увидят внутренние чаты компании и чужие проекты.

**Прайс-листы, финансовые ставки и биллинг.** Учет себестоимости, ставок биллинга клиентам и выплат подрядчикам. Финансовые снепшоты при логировании трудозатрат и закрытие отчетных периодов от изменений задним числом.

**Универсальный E-Commerce CMS Шлюз.** Единый интеграционный слой для 11 CMS (OpenCart 1.5–4.x, 1С-Битрикс, WooCommerce HPOS, InSales, CS-Cart, PrestaShop, Shop-Script, Могута, Tilda, Shopify, Magento 2) с HMAC-SHA256 подписями, синхронизацией заказов, клиентов и складских остатков.

**Уведомления.** Оповещения в реальном времени о назначении задач, комментариях, упоминаниях, изменениях сроков, согласованиях и системных событиях. Push-уведомления через браузерное API. Центр уведомлений с историей.

**Аналитика и дашборды.** Обзорный дашборд бизнеса. KPI, анализ загрузки, сигналы рисков, отчёты по ёмкости команды. Все данные из реального исполнения проектов и задач.

**Администрирование.** Пользователи, роли, гранулярные права доступа, статусы, приоритеты, SLA-политики, workflow-правила, вебхуки, API-клиенты, модули, аудит-логи, feature-флаги, лимиты, настройки AI-провайдеров — всё из панели администратора.

**Мультиязычность и локализация.** 7 встроенных языков интерфейса (русский, английский, китайский, испанский, португальский, немецкий, французский), нативная поддержка письма справа налево (RTL: арабский, иврит, персидский, урду) с зеркалированием структуры страниц, управление языками в панели администратора (`web/admin-languages`), безопасный установщик языковых пакетов из ZIP или каталога с AST-валидацией и экспорт в ZIP в один клик.

**Перенос данных и интеграции.** Перенесите работу из других трекеров без потери накопленного. Коннекторы односторонней миграции переносят в TropaTT доски, списки, проекты, задачи, статусы и пользователей из Jira, Trello, Asana, Битрикс24, ClickUp, Todoist, Shtab, Worksection, Confluence, Kaiten, Toggl, ActiveCollab, Notion и Linear. Синхронизация с Google Календарём и Яндекс Календарём держит события в актуальном состоянии; GitHub и GitLab синхронизируют issues и merge requests с задачами; Slack отправляет уведомления; draw.io добавляет диаграммы; Raycast подключается через MCP.

**Идеи и AI-проработка.** Захватите сырую идею, запрос клиента или бизнес-проблему. AI анализирует реализуемость, риски и сложность. AI предлагает структурированную иерархию задач. Просмотрите и превратите в реальные задачи одним кликом. Превращает «надо бы что-то сделать с X» в план действий за минуты.

---

### Обзор возможностей

| Область | Что входит | Зачем это нужно |
|---|---|---|
| **CRM** | Клиенты, контрагенты, компании, контакты, оргструктура | Все деловые связи компании в одной базе |
| **Задачи** | Иерархия, подзадачи, чеклисты, WIP-лимиты, зависимости, шаблоны, ключи (PRJ-001) | Полноценный таск-трекер вместо сторонней подписки |
| **Проекты** | Вехи, риски, диаграмма Ганта, контекст загрузки, шаблоны | Контроль сроков, ресурсов и персональной ответственности |
| **Канбан** | Drag-and-drop доски для потоковой работы | Наглядное управление статусами, устранение узких мест |
| **Гант** | Временная шкала с автоматическим учетом зависимостей | Прозрачность дедлайнов и реалистичное планирование |
| **Календарь** | События, повестка, день/неделя, производственный календарь | Привязка встреч и дедлайнов к реальным задачам |
| **Чат** | Встроенный мессенджер — каналы, ЛС, файлы, @упоминания | Обсуждения непосредственно в контексте задач и проектов |
| **База знаний** | Иерархия разделов, Markdown/WYSIWYG, версионирование, права | Регламенты, инструкции и документация внутри компании |
| **Клиентский портал**| Гостевой доступ для заказчиков (просмотр, согласование, задачи) | Прозрачность для клиента без риска утечки внутренних данных |
| **Ставки и прайсы** | Учет себестоимости, биллинга и выплат через именованные прайс-листы | Точный финансовый учет трудозатрат и рентабельности |
| **CMS Шлюз** | Коннекторы к 11 платформам (модуль) (OpenCart, 1С-Битрикс, WooCommerce и др.) | Автоматический импорт заказов и синхронизация остатков |
| **Уведомления** | Оповещения в реальном времени, web push, центр истории | Контроль дедлайнов, согласований и назначений |
| **Аналитика** | Дашборды, KPI, загрузка команды, карта рисков | Управленческие решения на основе фактических данных |
| **Автоматизация** | Workflow-правила, SLA-контроль, согласования, вебхуки | Меньше рутины, защита от человеческого фактора |
| **ИИ (20+ сценариев)**| Проработка идей, декомпозиция, планы дня, чеклисты, риски | ИИ как реальный ассистент, экономящий часы времени |
| **MCP Сервер** | 621 инструментов + 6 ресурсов для Claude Code, Cursor, Codex, ChatGPT | Прямое безопасное управление CRM для ИИ-агентов |
| **Модульный SDK** | Hot-pluggable модули, шина событий `ModuleEvents`, UI-слоты, миграции | Расширение функционала без правок ядра |
| **Администрирование** | Пользователи, роли, RBAC-права, feature-флаги, логи аудита | Полный контроль над безопасностью и функционалом |
| **Интейк заявок** | Сбор и первичная сортировка входящих обращений до создания задач | Отделение сырых лидов от утвержденного бэклога |
| **Приватность** | Данные на вашем сервере; наружу — только проверка обновлений и каталог маркетплейса (отключаются) | Полный суверенитет, соответствие 152-ФЗ и GDPR под вашим контролем |
| **Без лимитов** | Пользователи, задачи, проекты и файлы не ограничены тарифом | Масштабирование зависит от вашего сервера, а не чека SaaS |
| **Установка** | Браузерный мастер для любого хостинга c PHP/MySQL | Быстрый старт за 5 минут без консоли и DevOps |
| **Zero Deps** | Ноль сторонних PHP-пакетов, собственное микроядро | Отсутствие рисков supply-chain, надежная архитектура |

---

### ИИ — что он умеет

В TropaTT глубина интеграции ИИ значительно выше, чем в большинстве SaaS CRM. Это не просто виджет чат-бота в углу экрана, а встроенные в повседневные бизнес-процессы функции, экономящие рабочее время.

Вы используете собственные API-ключи провайдеров (OpenAI, Anthropic, DeepSeek, Google, совместимые шлюзы). Вся обработка идёт на стороне сервера. Данные не передаются в ИИ-сервисы без вашего явного запроса. Каждая рекомендация работает по принципу preview-before-apply: система ничего не перезаписывает без вашего подтверждения.

**Ключевая функция: AI-проработка идей.**

Вы пишете несколько предложений о возникшей идее, запросе клиента или бизнес-задаче. ИИ оценивает реализуемость, риски, сложность и архитектурные нюансы. Затем формирует структурированную иерархию: родительские задачи, подзадачи, приоритеты и обоснование. Вы просматриваете результат и в один клик создаете реальные рабочие задачи.

Реальный пример: _«Клиент хочет интеграцию системы бронирования на сайт»_ → ИИ предлагает: исследование API (2 подзадачи) → проектирование архитектуры шлюза → разработка эндпоинта → верстка интерфейса → интеграционные тесты → чек-лист развертывания. То, что раньше требовало получаса ручного составления плана, решается за 30 секунд.

**Все 28 ИИ-сценария:**

AI-анализ идей · Декомпозиция задач · План на день · План на неделю · Сводка задачи · Предложения следующих действий · Генерация чеклистов · Контроль качества задач · Черновики комментариев · Приоритизация бэклога · Сводка проекта · Оценка рисков проекта · Отчёт для клиента · Сводка по клиенту · Подготовка к встрече · Аудит качества данных клиентов · Интерпретация KPI · Анализ рисков аналитики · Сводка загрузки команды · Повестка встречи в календаре · Дневной дайджест дашборда · Семантический поиск · Безопасный отчёт для клиента · Журнал администратора · Проверка здоровья вебхуков · Аудит правил автоматизации · Сводка по базе знаний · Упрощение статей базы знаний

**Архитектурные примитивы AgentOS 2026:**
- **Сервер Model Context Protocol (MCP):** 621 инструментов и 6 ресурсов, охватывающих задачи, проекты, клиентов, контакты, чаты, календарь, трудозатраты, аналитику и базу знаний.
- **Оптимизация контекста `density: "compact"`:** Специальный компактный формат ответов на списочные запросы, экономящий до 85% промпт-токенов при работе с большими объемами данных.
- **Многошаговая обработка задач (`crm_agent_bundle`):** Помогает создавать родительскую задачу, критерии приемки (DoD), чек-листы и подзадачи последовательными операциями. Результат возвращается отдельно для каждого шага; вызывающая сторона должна проверять частичные результаты.
- **Долговременная память агента (`crm_agent_memory`):** Хранение структурированных фактов и графовых связей между сессиями работы ИИ-агентов с семантическим поиском и экспортом.
- **Оптимистические блокировки STORM:** Контроль версий строк (`row_version`) предотвращает конфликты перезаписи данных при одновременной работе нескольких ИИ-агентов и живых пользователей.

**Безопасность ИИ:**
- Режим предварительного просмотра по умолчанию. Никаких невидимых модификаций базы.
- Все вызовы идут через бэкенд: API-ключи никогда не попадают в браузер.
- Ролевой доступ к каждой ИИ-функции (RBAC).
- 40 feature-флага для тонкой настройки включения возможностей.
- Лимиты запросов и затрат по типам рабочих процессов.
- Исходные промпты и конфиденциальные контексты не сохраняются по умолчанию.

---

### Командный чат

В TropaTT встроен полноценный рабочий мессенджер. Это не сторонний виджет и не фрейм, а часть общей экосистемы.

Возможности:
- **Двухпанельный интерфейс.** Список диалогов слева, активная переписка справа.
- **Проектные и командные каналы.** У каждого проекта есть свой чат. Общие каналы для компании.
- **Личные сообщения.** Диалоги один на один и закрытые группы.
- **Вложения и форматирование.** Текст, файлы, изображения, ссылки. Поиск пользователей через @упоминания. Ветви ответов.
- **URL-адресация чатов.** Прямая ссылка на конкретный диалог или сообщение.
- **Сохранение контекста.** Восстановление открытого чата при перезагрузке страницы.
- **Живой polling.** Автоматическое обновление сообщений без сброса набранного черновика.
- **Мгновенный поиск.** Быстрый поиск коллег и создание переписки в пару кликов.
- **Управление участниками.** Создатель чата управляет составом участников.
- **Удобное управление с клавиатуры.** Enter — отправка, Shift+Enter — новая строка.

Обсуждение задач, проектов и клиентов ведётся там же, где лежат сами данные.

---

### Как это используют

Полный цикл управления клиентской работой:

1. **Фиксация** — входящая заявка с сайта, идея, запрос клиента или лид.
2. **Анализ** — самостоятельный или с помощью ИИ: оценка сроков, рисков, сложности и подходов.
3. **Структурирование** — разбиение на проекты, задачи, подзадачи, чеклисты, ответственных и дедлайны.
4. **Координация** — обсуждение в чате, комментарии, @упоминания, уведомления.
5. **Исполнение** — Канбан-доски, списки задач, экраны «Мой день» и «Моя неделя».
6. **Контроль** — диаграмма Ганта, дашборды, аналитика трудозатрат, сигналы рисков.
7. **Автоматизация** — правила workflow, SLA-политики, вебхуки, согласования.

**Примеры сценариев:**

- **Фрилансер:** обращение клиента → AI-проработка → структурированный план → «Мой день» → выполнение → диалог с клиентом → сдача проекта.
- **Агентство:** бриф клиента → AI-декомпозиция → проект и вехи → Канбан → контроль по Ганту → отчёт клиенту → аналитика рентабельности.
- **Сервисная компания:** карточка контрагента → проект монтажа → задачи по объектам → Гант → дневные планы мастеров → SLA-контроль → акт.
- **Интернет-магазин:** автоматический приём заказа через CMS Шлюз → создание задачи комплектации → проверка чеклиста → обновление остатка в CMS.
- **B2B-отдел:** компания → контакты → задачи согласования договоров → напоминания → вебхук в 1С → дашборд руководителя.

---

### Автоматизация и API

Автоматизация и API TropaTT рассчитаны на продакшен-нагрузки и интеграцию в любую корпоративную инфраструктуру:

- **Универсальный E-Commerce CMS Шлюз (`crm.ecommerce-gateway`)** — канонический контракт v1.0 JSON и коннекторы для 11 платформ (OpenCart 1.5–4.x, 1С-Битрикс, WooCommerce HPOS, InSales, CS-Cart, PrestaShop, Shop-Script, Могута, Tilda, Shopify, Magento 2) с HMAC-SHA256 подписями, двусторонней синхронизацией заказов, остатков и защитой от дублирования (идемпотентность).
- **Движок AgentOS 2026** — пакетная обработка задач (`crm_agent_bundle`), долговременная память ИИ (`crm_agent_memory` с семантическим графовым поиском), оптимистическая блокировка STORM (`row_version`) и экономия до 85% токенов с режимом `density: "compact"`.
- **Workflow-правила** — автоматические действия при изменении статусов, полей или наступлении сроков.
- **SLA-контроль** — мониторинг времени реакции и решения с предупреждениями о рисках просрочки.
- **Маршруты согласований** — цепочки многоэтапного утверждения изменений и документов.
- **Вебхуки** — оповещение внешних систем при событиях (`task.created`, `task.updated`, `comment.added` и др.; подпись HMAC-SHA256).
- **Agile-спринты и циклы** — трекинг скорости команды (velocity), диаграммы сгорания (burndown) и управление скоупом.
- **Встроенные чаты с SSE-стримингом** — мгновенная доставка сообщений без перезагрузки страниц.
- **Клиентский портал** — ролевое разделение доступа к проектам и статьям базы знаний для заказчиков.
- **API-клиенты и ключи** — программный доступ с точечными правами (scopes).
- **Фоновые задачи** — очереди импорта, экспорта, уведомлений и ИИ-обработки.
- **Модульная система** — расширение логики без вмешательства в ядро, 19 консольных команд.
- **Сгенерированные эндпоинты REST API** — 984 записей маршрутов ядра (модули добавляют свои).
- **Контроль документации (Zero Drift)** — строгий гейт CI, гарантирующий 100% соответствие кода и документации.
- **Спецификация OpenAPI 3.1** — актуальная автогенерируемая схема API.
- **Сервер MCP (621 инструментов, 6 ресурсов)** — подключение Claude Code, Cursor, Codex, OpenDevin и ChatGPT с контролем доступа (справочник: [`docs_mcp/mcp_ru.md`](docs_mcp/mcp_ru.md)).

---

### Подключение ИИ-агентов (MCP)

В TropaTT встроен полноценный сервер **Model Context Protocol (MCP)** — открытого протокола, на котором работают **Claude Code, Cursor, Codex, OpenDevin, ChatGPT и современные ИИ-агенты**. Агент подключается к вашей CRM и безопасно работает с реальными данными: задачами, проектами, контрагентами, контактами, чатами, календарем, трудозатратами и базой знаний.

- **621 MCP-инструментов + 6 ресурсов** — полный охват всех сущностей CRM и управления работой.
- **Поддержка примитивов AgentOS 2026** — пакетное создание задач с чеклистами (`crm_agent_bundle`), долговременная память (`crm_agent_memory`), компактные ответы для экономии контекста.
- **Работает с Claude Code, Cursor, Codex, OpenDevin, ChatGPT.** Подключение настраивается стандартным образом через JSON-RPC.
- **Те же правила, что и в веб-интерфейсе.** Все действия агента проверяются через REST API и ролевую модель RBAC: агент не может обойти права доступа или напрямую вмешаться в базу.
- **Безопасность по умолчанию.** Пароли, токены и приватные ключи фильтруются при выдаче данных; операции записи требуют соответствующих прав.
- **Эндпоинт:** `POST /api/index.php?route=api/v1/mcp`, авторизация через Bearer-токен пользователя или API-клиента.

Полный справочник MCP (инструменты, авторизация, RBAC): [`docs_mcp/mcp_ru.md`](docs_mcp/mcp_ru.md).

---

### Свой сервер — свои правила

TropaTT полностью открыта. Разворачивайте систему на собственной инфраструктуре. Изучайте исходный код. Модифицируйте. Никаких лицензионных платежей и обязательных подписок.

Платные услуги (доработка, интеграция, миграция данных, поддержка) существуют как опция, но не требуются для полноценного использования системы.

**Практические преимущества self-hosted:**

- **Никакой зависимости от вендора.** Облачные сервисы могут закрыться, заблокировать аккаунт или поднять цены. Ваши данные в TropaTT всегда принадлежат вам.
- **Никаких искусственных ограничений.** Количество пользователей, клиентов, проектов, задач и файлов ограничивается только мощностью вашего сервера.
- **Вас невозможно отключить.** Доступ не заблокируют из-за проблем с иностранными платежами или изменения политики провайдера.
- **Суверенитет данных (где лежат данные, решаете вы; выполнение требований закона остаётся за вами):**
  - **Российская Федерация (152-ФЗ):** размещение на серверах в России (Selectel, Beget, TimeWeb, Yandex Cloud и др.) позволяет хранить персональные данные в стране. Модули из маркетплейса добавляют синхронизацию с Яндекс.Календарём, коннекторы к 1С-Битрикс, InSales, Могута и миграции из Битрикс24 и Штаба.
  - **Европейский союз и мир (GDPR/CCPA):** данные на выбранном вами хостинге, без сторонних трекеров; телеметрия интерфейса пишется в вашу же базу; есть процедура безвозвратного удаления данных по запросу.
  - **Изолированные сети и китайский сегмент:** Полностью локальные ассеты (Bootstrap, FontAwesome, SortableJS хранятся локально в `upload/web/assets/`). Никаких внешних запросов к заблокированным CDN или Google Fonts. Идеально для корпоративных интранетов.
- **Экономия бюджета.** Систему можно запускать локально бесплатно или на недорогом shared-хостинге за 150–250 ₽/мес. Рост нагрузки масштабируется апгрейдом сервера, а не переходом на тариф за десятки тысяч рублей в месяц.

---

### Установка

Установка через браузерный мастер. Без терминала, без Composer, без npm. Подходит для любого shared-хостинга, VPS, локального сервера и стандартных сред PHP/MySQL.

> **Где лежат файлы?** Все файлы приложения находятся в папке **`upload/`**. Корень репозитория содержит только документацию и конфигурации. Для установки скопируйте **содержимое папки `upload/`** в корневую директорию вашего сайта на сервере (чтобы `index.php`, `api/`, `web/` и `modules/` оказались в корне веб-пространства).

**Получение исходного кода:**

- Клонирование репозитория:
  ```bash
  git clone https://github.com/Anton-Barinov/TropaTT.git
  ```
- Или скачивание ZIP-архива с GitHub (**Code → Download ZIP**), либо готового архива со страницы [Релизов](https://github.com/Anton-Barinov/TropaTT/releases).

**Требования к окружению:**
- PHP 8.1+
- База данных MySQL 8.0+ или MariaDB 10.4+
- Любой веб-сервер (Apache, Nginx, LiteSpeed)
- Права на запись в директорию конфигурации `api/` и хранилище `storage/`
- **Крон-задача (Cron)** для вызова `web/cron.php` каждую минуту (задайте `CRON_SECRET_KEY` в `api/.env` и передавайте заголовок `X-Cron-Key`). Крон обрабатывает очередь уведомлений, запускает регламентные задачи модулей и шлёт heartbeat для мониторинга в админке. См. [`SHARED_HOSTING_GUIDE.md`](SHARED_HOSTING_GUIDE.md)
- **Исходящий HTTPS** с сервера к службам браузерного push (Google FCM, Mozilla autopush) для веб-пушей
- Расширение **`openssl`** с поддержкой криптографических кривых `prime256v1` для подписи VAPID

**Шаги установки:**
1. Скопируйте **содержимое папки `upload/`** (не саму папку) в корень вашего сайта на сервере.
2. Создайте пустую базу данных MySQL в панели хостинга.
3. Откройте ваш домен в браузере. TropaTT автоматически определит отсутствие конфигурации и запустит инсталлятор.
4. Мастер установки проверит модули PHP, запросит доступы к MySQL, URL сайта, часовой пояс и данные первого администратора.
5. Инсталлятор создаст файл `.env` в `api/`, развернет структуру таблиц, заполнит справочники (статусы, роли, права), создаст аккаунт администратора и заблокирует повторную установку.
6. Войдите в систему и начинайте работу.

**Пример для shared-хостинга:**
Загрузите содержимое `upload/` через FTP или файловый менеджер панели управления → создайте базу данных в панели хостинга → перейдите по адресу сайта в браузере → следуйте подсказкам установщика → готово.

---

### FAQ

**Что такое TropaTT простыми словами?**
Бесплатная, открытая и self-hosted CRM + таск-менеджер + платформа управления проектами на PHP 8.1+ и MySQL. Разворачивается на вашем хостинге. Объединяет клиентов, задачи, проекты, Канбан, Гант, календарь, базу знаний, клиентский портал, финансовый учет ставок, CMS-шлюз заказов, командный чат, аналитику, автоматизацию и 20+ ИИ-инструментов.

**Это больше CRM или таск-менеджер?**
И то, и другое. Полноценная CRM для ведения базы контрагентов, контактов, сделок и документов. И глубокий таск-менеджер с иерархией задач, Канбаном, Гантом, чеклистами и ежедневным планированием.

**Чем TropaTT отличается от Битрикс24 или Jira?**
В отличие от Битрикс24, в TropaTT нет платы за рабочие места, она работает на обычном хостинге за 200 ₽/мес (без тяжёлых Java-демонов и очередей Redis) и имеет открытый код. В отличие от Jira, TropaTT «из коробки» включает CRM, чат, базу знаний, клиентский портал и финансовый учет без необходимости докупать десятки сторонних плагинов.

**Можно ли развернуть TropaTT в Docker или контейнерах?**
Официального Docker-образа и `docker-compose.yml` пока нет. TropaTT нужны только PHP 8.1+ и MySQL, поэтому в контейнерах её можно запускать на стандартных образах PHP и MySQL, смонтировав содержимое `upload/` в корень сайта, но такая конфигурация официально не тестировалась.

**Как устроены резервное копирование и восстановление?**
Поскольку 100% данных хранятся в стандартной реляционной базе MySQL, а файлы — в директории `upload/storage/`, бэкап делается стандартными системными средствами за несколько секунд:
1. База данных: штатный `mysqldump -u <user> -p <dbname> > backup.sql` (или экспорт через phpMyAdmin).
2. Файлы: архивация папки `upload/storage/` и конфигурации `api/.env`.
3. Автоматические снапшоты при обновлениях: встроенная система обновлений автоматически создает резервную копию файлов и схемы БД перед накатом релиза с возможностью отката в один клик.

**Могут ли несколько сотрудников работать одновременно без конфликтов?**
Механизм STORM использует версии строк (`row_version`) и отклоняет устаревшее изменение одной записи, предотвращая тихую перезапись. Это помогает не потерять изменения другого пользователя.

**Каковы точные минимальные системные требования к серверу?**
- Процессор: 1 vCPU (от 1.0 ГГц).
- Оперативная память: 512MB RAM.
- Диск: 100MB под кодовую базу + место под загружаемые вложения проектов.
- Программное обеспечение: PHP 8.1 или 8.2 (с расширениями PDO, OpenSSL, mbstring, cURL), MySQL 8.0+ или MariaDB 10.4+, веб-сервер Apache (с mod_rewrite) или Nginx.
- Поддерживаемые платформы: любой виртуальный хостинг от 150–250 ₽/мес (cPanel, ISPmanager, FastPanel, DirectAdmin), VPS, локальные ПК (macOS, Linux, Windows с Open Server / XAMPP).

**Как клиентский портал защищает внутренние данные компании?**
Представители клиентов и субподрядчики приглашаются с ролями Наблюдателя или Исполнителя с жесткой привязкой исключительно к разрешенным проектам. Внутренние чаты компании, обсуждения других клиентов, общие списки контрагентов и ставки финансового биллинга для них полностью скрыты.

**Что умеет встроенная База знаний (Wiki)?**
Поддерживает древовидную иерархию разделов и статей, форматирование в Markdown и WYSIWYG, историю ревизий с возможностью сравнения версий, ролевое разграничение прав на чтение и редактирование, а также генерацию публичных ссылок для внешних регламентов и инструкций клиентам.

**Можно ли подключить несколько интернет-магазинов (OpenCart, WooCommerce, 1С-Битрикс)?**
Да. Модуль `crm.ecommerce-gateway` (ставится из маркетплейса) поддерживает 11 популярных платформ, позволяет подключать неограниченное число магазинов, принимает входящие заказы, сопоставляет покупателей с базой контрагентов и синхронизирует складские остатки по защищенному протоколу с HMAC-SHA256.

**Подходит ли система для фрилансера-одиночки?**
Да. Минимальный размер команды — 1 человек. Вы ведете клиентов, управляете задачами, используете ИИ для декомпозиции и планирования дня — в одном месте и без ежемесячных платежей.

**Работает ли на обычном виртуальном хостинге?**
Да. Стандартного тарифа shared-хостинга с PHP 8.1+ и MySQL за 150–250 ₽/мес вполне достаточно для старта и комфортной работы команды.

**Что умеет искусственный интеллект?**
28 готовых сценария: анализ идей (превращает абзац текста в иерархию задач), планирование дня и недели, декомпозиция, генерация чеклистов, резюме переписки, оценка рисков проектов, подготовка к переговорам. Вы используете свои API-ключи, платите напрямую провайдеру без наценок, а ИИ работает строго на стороне сервера и только с вашего подтверждения.

**Могут ли ИИ-агенты (Claude Code, Cursor, ChatGPT) управлять CRM?**
Да. В TropaTT встроен MCP-сервер (621 инструментов, 6 ресурсов). Подключите агента к адресу `POST /api/index.php?route=api/v1/mcp` с Bearer-токеном. Агент сможет безопасно искать, создавать и обновлять задачи, проекты, базу знаний и записи клиентов с соблюдением ролевых прав (RBAC). Подробнее: [`docs_mcp/mcp_ru.md`](docs_mcp/mcp_ru.md).

**Как разработать собственный модуль?**
Стандартная установка поставляется **без модулей**: в каталоге `upload/modules/` лежит только `.htaccess`, а модули ставятся по необходимости из маркетплейса (`marketplace.tropatt.com`) через **Администрирование → Модули → Маркетплейс** либо копированием пакета в этот каталог. Модули-примеры опубликованы в `docs_modules/examples/modules/`. Модули размещаются в папке `upload/modules/<имя_модуля>/`. Модуль содержит `manifest.json`, класс `ServiceProvider.php` (для регистрации в DI-контейнере), обработчики событий (`ModuleEvents`), слоты внедрения интерфейса (`PositionRegistry`) и транзакционные миграции базы (`up()`/`down()`). Подробное пошаговое руководство разработчика: [`docs_modules/modules_ru.md`](docs_modules/modules_ru.md).

**Где физически хранятся данные?**
На вашем сервере. TropaTT не синхронизирует ваши данные с облаком, у разработчика нет доступа к установке. По умолчанию сервер обращается наружу только для проверки обновлений (`update.tropatt.com`) и чтения каталога маркетплейса — оба обращения отключаются настройками (`api/config/update.php` / переменные окружения).

**Есть ли ограничения по пользователям или задачам?**
Никаких тарифных лимитов нет. Создавайте столько пользователей, проектов, задач и клиентов, сколько позволяет мощность вашего сервера и объем диска.

**Разрешено ли коммерческое использование?**
Да. TropaTT распространяется под лицензией AGPL-3.0. Вы имеете полное право использовать систему для ведения своего коммерческого бизнеса, управления проектами клиентов и координации работы агентства без каких-либо отчислений.

**Как устроены обновления?**
Обновления устанавливаются в один клик прямо из панели администратора (**Админ → Обновление системы**). Сервер обновлений собирает и подписывает релизы с GitHub, CRM скачивает пакет, проверяет цифровую подпись, делает автоматический бэкап, применяет файлы и миграции базы, а в случае ошибки может откатиться назад. Подробности: [`UPDATES.md`](UPDATES.md).

**Кто автор проекта?**
**Баринов Антон**, PHP-разработчик и архитектор. Создатель платформы TropaTT.

---

### В цифрах

| Метрика | Значение |
|---|---|
| API эндпоинты | 984 записей маршрутов ядра (установленные модули добавляют свои) |
| MCP инструменты | 621 tools + 6 ресурсов — сервер Model Context Protocol для ИИ-агентов |
| Веб-маршруты | ~70 страниц |
| Бэкенд-сервисы | 139 |
| Репозитории | 114 |
| Доменные модули | 35+ |
| Модули (маркетплейс) | 24 — в т.ч. 14 миграций из Jira, Trello, Asana, Битрикс24, ClickUp, Todoist, Штаб, Worksection, Confluence, Kaiten, Toggl, ActiveCollab, Notion, Linear; GitHub, GitLab, Slack; календари Google и Яндекс; WIP-лимиты; draw.io; Raycast; E-Commerce шлюз. Стандартная установка поставляется без модулей. |
| CMS-коннекторы | 11 платформ (модуль) (OpenCart 1.5–4.x, 1С-Битрикс, WooCommerce HPOS, InSales, CS-Cart, PrestaShop, Shop-Script, Могута, Tilda, Shopify, Magento 2) |
| JS-модули | 44 собственных модулей на чистом JS, без SPA-фреймворков и сборщиков |
| Публичный CI | PHP lint (8.1 и 8.2), контракт безопасности клиентского портала, покрытие маршрутов OpenAPI, unit-тесты фронтенда |
| AI-эндпоинты | 65 |
| AI-сценарии | 28 |
| Feature-флаги | 40 |
| Покрытие фронтенд API | Контролируется по инвентарю маршрутов |
| Внешние PHP-зависимости | 0 |
| Внешние JS/CSS библиотеки | 3 (Bootstrap 5, FontAwesome 6, SortableJS) |
| Инструмент OpenAPI | `upload/api/scripts/generate_openapi.php` |
| Консольные команды модулей | 19 |
| Языки интерфейса | 7 — Русский, English, Deutsch, Español, Français, Português, 中文 |
| Варианты развертывания | Локальный ПК, офисный сервер, VPS, облачная VM, shared-хостинг |
| Минимальная стоимость хостинга | от ~150–250 ₽/месяц |

---

### Технологии

- **Бэкенд:** PHP 8.1+, собственное микроядро. Ноль сторонних пакетов. Никаких Laravel, Symfony, Doctrine.
- **База данных:** MySQL 8.0+ или MariaDB 10.4+.
- **Фронтенд:** Серверный рендеринг (MPA), Bootstrap 5 для адаптивной верстки, кастомные ES5+ JS-модули для динамики. Никакого React/Vue. Сборка не требуется.
- **Архитектура:** API-first подход. Веб-интерфейс запрашивает все данные исключительно через REST API. Прямой доступ к базе из представлений исключен.
- **Безопасность:** Двойная аутентификация (cookie + CSRF для веб-интерфейса, Bearer-токены для API). Гранулярный RBAC. Защита от SSRF. Rate limiting. Карантин загружаемых файлов. Аудит действий.
- **Тестирование:** Автоматический CI проверяет синтаксис PHP, выполняет миграции тестовой базы MySQL и сверяет соответствие маршрутов OpenAPI.
- **ИИ-слой:** Настраиваемые провайдеры (OpenAI, Anthropic, DeepSeek, Google, совместимые). Шаблоны промптов, валидация по JSON Schema, принцип предварительного просмотра.
- **Документация:** OpenAPI генерируется из реальных маршрутов через `upload/api/scripts/generate_openapi.php`.

---

### Структура

```text
TropaTT/
├── upload/         # Сама CRM — скопируйте СОДЕРЖИМОЕ этой папки на ваш сервер
│   ├── api/        #   Ядро API — контроллеры, сервисы, репозитории, конфиги, миграции
│   ├── web/        #   Веб-интерфейс — установщик, страницы, шаблоны, JS-модули, ассеты
│   ├── modules/    #   В стандартной установке пусто (только .htaccess) — модули ставятся из маркетплейса
│   └── index.php   #   Единая точка входа
├── README.md       # Главная документация проекта
└── ...             # Лицензия, руководства разработчика, конфигурация .github/
```

Бэкенд-модули организованы в 9 логических групп: Аутентификация/Пользователи · CRM (клиенты, контрагенты, контакты) · Проекты/Задачи · Планирование (календарь, напоминания) · Коммуникации (чаты, пуши, уведомления) · Автоматизация (workflow, SLA, вебхуки) · Аналитика (дашборды, отчеты) · ИИ (11 модулей ядра) · Администрирование (настройки, логи, аудит, модули, хранилище).

---

### Модули

В TropaTT реализована независимая модульная подсистема с возможностью горячего подключения. Модули могут регистрировать сервисы в DI-контейнере, подписываться на синхронные события жизненного цикла, внедрять разметку в 14 слотов интерфейса, накатывать транзакционные миграции БД и добавлять команды консоли.

**5 архитектурных опор:**
1. **Манифест (`manifest.json`):** Версионирование, совместимость с ядром, зависимости.
2. **Сервис-провайдер (`ServiceProvider.php`):** Регистрация зависимостей в DI-контейнере.
3. **Шина событий (`ModuleEvents`):** Ху