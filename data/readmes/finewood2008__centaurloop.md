# Centaur Loop / 半人马环

[![MIT License](https://img.shields.io/badge/license-MIT-111111.svg)](./LICENSE)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.x-3178c6.svg)](https://www.typescriptlang.org/)
[![React](https://img.shields.io/badge/React-18-61dafb.svg)](https://react.dev/)
[![CI](https://github.com/finewood2008/centaur-loop/actions/workflows/ci.yml/badge.svg)](https://github.com/finewood2008/centaur-loop/actions/workflows/ci.yml)
[![GitHub Pages](https://github.com/finewood2008/centaur-loop/actions/workflows/pages.yml/badge.svg)](https://github.com/finewood2008/centaur-loop/actions/workflows/pages.yml)

English | [简体中文](./README.zh-CN.md) | [Website](https://www.centaurloop.com) | [Technical Design](./CENTAUR_LOOP_TECHNICAL_DOC_EN.md) | [中文定位](./docs/PROJECT_POSITIONING.zh-CN.md)

**Centaur Loop is an open-source framework for building AI employees from governable work loops.**

**半人马环是 AI 员工的最小工作单元框架。**

A digital worker is not one big Agent. It is a set of governable, composable, evolving Centaur Loops.

Each Centaur Loop is the smallest AI-takable unit of work: a repeatable loop with a clear goal, context, AI execution, human gates, real-world feedback, confirmed memory, and next-cycle improvement.

中文简述：AI 员工不是一个大而全的 Agent，而是由多个可治理、可组合、可持续进化的半人马环组成。每个半人马环都是一个可被 AI 接管的最小循环工作流。

```text
Digital Worker
  = Research Loop
  + Draft Loop
  + Review / Publish Loop
  + Feedback Memory Loop
  + more governable loops
```

> The loop is the unit of digital labor.
>
> 数字劳动的基本单位不是 prompt、task 或 workflow，而是可治理的工作闭环。

## Why This Exists

Most AI systems still optimize the wrong layer:

- Prompt tools optimize single outputs.
- Workflow engines move steps forward.
- Agent frameworks plan and execute tasks.
- Cron wakes jobs up.

But an AI employee needs more than execution. It needs bounded responsibility, human judgment, feedback, memory, and the ability to improve across cycles.

Centaur Loop turns work into small, governable loops that can be gradually taken over by AI while keeping humans in control of judgment, risk, publishing, and memory.

中文说明：半人马环关注的不是“让 AI 做一次任务”，而是“如何把岗位拆成可治理、可验证、可逐步交给 AI 的工作单元”。

## Core Definition

A Centaur Loop contains:

| Part | Meaning |
| --- | --- |
| **Goal** | The business outcome this loop owns. |
| **Context & Input** | Data, tools, constraints, history, and memory. |
| **AI Execution** | The work that can be delegated to a model, agent, or runtime. |
| **Human Gates** | Judgment points for plan approval, quality, risk, compliance, publishing, and memory. |
| **Feedback** | Real-world outcomes, metrics, screenshots, notes, and corrections. |
| **Confirmed Memory** | Lessons approved by humans and reused in the next cycle. |
| **Next Cycle** | The loop runs again with better context. |

In short:

```text
Goal -> Context -> AI Execution -> Human Gates -> Feedback -> Memory -> Next Cycle
```

## Product Shape

| Layer | Role |
| --- | --- |
| **Digital Worker** | A long-running AI work system composed of multiple Centaur Loops. |
| **Centaur Loop** | The smallest AI-takable work unit. |
| **Loop Studio** | The UI for designing, driving, and observing loops. |
| **Loop Runtime** | The execution layer: model, agent, workflow, or external runtime. |
| **Human Gates** | Explicit approval and judgment checkpoints. |
| **Feedback Memory** | The layer that turns real outcomes into reusable capability. |

Current repo status:

- Working local React/Vite workbench.
- TypeScript loop state machine.
- Chat-first loop protocol.
- Runtime connectors for demo and OpenAI-compatible/local model paths.
- Built-in starter loops for content growth, customer support, and product iteration.

## Demo

![Centaur Loop content growth loop demo](./docs/assets/centaur-loop-demo.gif)

The flagship demo is **Content Growth Worker / Content Growth Loop**. It demonstrates how one digital worker can be decomposed into loops for planning, drafting, human review, publishing, feedback, retrospective review, memory confirmation, and next-cycle improvement.

中文说明：当前旗舰 demo 是内容增长 AI 员工的雏形，用多个半人马环证明“岗位能力如何被拆解、治理、反馈和记忆”。

## Starter Digital Workers

| Digital Worker | Example Loops |
| --- | --- |
| **Content Growth Worker** | Research loop, draft loop, review/publish loop, performance feedback loop, memory loop. |
| **Customer Support Worker** | Ticket triage loop, answer draft loop, escalation gate, satisfaction feedback loop, policy memory loop. |
| **Product Iteration Worker** | Feedback mining loop, requirement synthesis loop, prioritization gate, release review loop, outcome memory loop. |

## What It Is Not

- Not a generic workflow canvas.
- Not a cron scheduler.
- Not a publishing bot.
- Not one autonomous super-agent.
- Not a replacement for LangGraph, Temporal, Inngest, n8n, Mastra, or agent frameworks.

Those systems can execute work. Centaur Loop defines the governable unit of work that can become part of an AI employee.

## Architecture

| Module | Role |
| --- | --- |
| `src/core/loopEngine.ts` | Explicit state machine that advances loops and stops at human gates. |
| `src/core/loopPlanner.ts` | Turns goals, memory, business context, and tools into structured plans. |
| `src/core/loopExecutor.ts` | Generates reviewable outputs and keeps failures inside the loop record. |
| `src/core/loopReviewer.ts` | Converts feedback into retrospective review, lessons, and next-cycle suggestions. |
| `src/protocol/loopChat.ts` | Maps runtime state to chat messages, cards, and user actions. |
| `src/adapters/*` | Runtime, model, tool, feedback, and memory boundaries. |
| `src/ui/*` | Chat-first workbench, embedded action cards, runtime dropdown, feedback and memory surfaces. |

## Runtime Connectors

Centaur Loop runs without an API key through the deterministic demo runtime. For real models, the browser calls the local Vite proxy; API keys do not enter the frontend bundle.

Supported runtime paths today:

- `local-demo`: built-in deterministic demo runtime.
- `openai-compatible-env`: any OpenAI-compatible `/chat/completions` endpoint configured through environment variables.
- `ollama-local`: detected through `127.0.0.1:11434/api/tags` and called through `/api/chat`.
- `lm-studio-local`: detected through `127.0.0.1:1234/v1/models`.
- `vllm-local`: detected through `127.0.0.1:8000/v1/models`.
- `llamacpp-local`: detected through `127.0.0.1:8080/v1/models`.

Planned adapters include LangGraph, Temporal, Inngest, Mastra, and n8n-style approval flows.

## Quick Start

```bash
npm install
npm run dev
```

Open the Vite URL printed in your terminal. The app works immediately with the demo runtime.

## Real Model Setup

Create `.env.local`:

```bash
cp .env.example .env.local
```

Configure an OpenAI-compatible endpoint:

```bash
CENTAUR_MODEL_BASE_URL=https://api.openai.com/v1
CENTAUR_MODEL_API_KEY=your_key_here
CENTAUR_MODEL_NAME=gpt-4o-mini
```

Restart the dev server and select the runtime from the floating runtime menu.

## Development

```bash
npm run typecheck
npm run build
```

## Roadmap

- **Loop Unit Framework**: make Centaur Loop a clear reusable unit for building AI employees.
- **Core Package**: extract `@centaur-loop/core` from the demo workbench.
- **Adapter Ecosystem**: add storage, notifier, model, memory, LangGraph, Mastra, Inngest, Temporal, and n8n-style adapters.
- **Digital Worker Studio**: compose multiple loops into one role-level worker.
- **Team Workspace**: shared loop history, team review, organizational memory, and loop analytics.
- **Centaur Loop Cloud**: hosted runtime management, durable execution, managed memory, and observability.

## Project Status

Centaur Loop is early. The current codebase is a working MVP and product design reference, not a stable library API yet. The goal is to make AI employees concrete: not a vague autonomous agent, but a system of inspectable, governable, improving work loops.

中文说明：当前版本是可运行的开源工作台 MVP；长期方向是用半人马环构建 AI 员工。

## Contributing

Focused issues and small PRs are welcome. See [CONTRIBUTING.md](./CONTRIBUTING.md) before opening larger design changes.

## License

MIT
