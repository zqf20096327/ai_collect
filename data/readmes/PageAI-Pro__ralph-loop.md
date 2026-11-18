# A Ralph Wiggum Loop implementation that works™

[![@pageai/ralph-loop version](https://img.shields.io/npm/v/@pageai/ralph-loop?label=npm&style=flat)](https://www.npmjs.com/package/@pageai/ralph-loop)

📚 Full docs: [ralphloop.sh](https://ralphloop.sh)

Ralph is a long-running AI agent loop. Ralph automates software development tasks by iteratively working through a task list until completion. This allows for long running agent loops, effectively enabling AI to code for days at a time.

This is an implementation that actually works, containing a hackable script so you can configure it to your env and favorite agentic AI CLI. It's set up by default to use Claude Code in Docker Sandboxes, and supports [multiple Docker Sandboxes agents](#running-with-a-different-agentic-cli).

#### 👉 [Watch the video](https://www.youtube.com/watch?v=3TL8Ez66I3o) for an in-depth walkthrough.

[![Ralph Wiggum Loop](https://github.com/user-attachments/assets/be94b8ba-b073-489d-b07e-d11db975a907)](https://www.youtube.com/watch?v=3TL8Ez66I3o)

- [Getting Started](#getting-started)
  - [(Optional) Set up your app](#optional-set-up-your-app)
  - [1️⃣ Step 1: Install Ralph](#1️⃣-step-1-install-ralph)
  - [2️⃣ Step 2: Create a PRD + task list](#2️⃣-step-2-create-a-prd--task-list)
  - [3️⃣ Step 3: Set up Docker Sandboxes](#3️⃣-step-3-set-up-docker-sandboxes)
  - [4️⃣ Step 4: Run Ralph](#4️⃣-step-4-run-ralph)
- [Running the Ralph Loop with custom options](#running-the-ralph-loop-with-custom-options)
  - [(Optional) Adjusting to your language/framework](#optional-adjusting-to-your-languageframework)
- [How It Works](#how-it-works)
- [How Is This Different from Other Ralphs?](#how-is-this-different-from-other-ralphs)
- [Steering the Agent](#steering-the-agent)
- [Support](#support)
  - [Promise Tags](#promise-tags)
  - [Exit Codes](#exit-codes)
- [Structure](#structure)
- [Continued Development](#continued-development)
- [Skills](#skills)
  - [Available Skills](#available-skills)
  - [Skills Directory Structure](#skills-directory-structure)
- [Reference](#reference)
  - [Docker Sandboxes](#docker-sandboxes)
  - [Playwright configuration](#playwright-configuration)
  - [Vitest configuration](#vitest-configuration)
  - [Running with a different agentic CLI](#running-with-a-different-agentic-cli)
  - [Starting from scratch](#starting-from-scratch)
- [Debugging](#debugging)
  - [How to inspect the sandbox and debug](#how-to-inspect-the-sandbox-and-debug)
  - [Allowing network access](#allowing-network-access)
  - [Authentication issues in Sandboxes / Login not persisting](#authentication-issues-in-sandboxes--login-not-persisting)
- [License](#license)

---------------------------------

## Getting Started

### (Optional) Set up your app

Starting fresh? Scaffold an app first, so Ralph has a working app, linter and tests to build on. Run this from your project folder:

```bash
# TanStack Start (React, Biome, TanStack Form + Query, Nitro)
npx @tanstack/cli@latest create lib --framework React --toolchain biome --deployment nitro --add-ons form,tanstack-query --no-examples --no-git --no-intent --non-interactive
cd lib && npx biome check --write && cd ..

# or Next.js
npx create-next-app@latest lib --typescript --tailwind --eslint --app
```

This creates the app in a `lib` subfolder. Stay in the project folder for the next steps.

> [!TIP]
> Prefer a minimal start? Try `npx create-vite@latest src --template react-ts`, or see [Starting from scratch](#starting-from-scratch).

### 1️⃣ Step 1: Install Ralph

Run this in your project folder (the parent of your app folder):

```bash
npx @pageai/ralph-loop
```

It asks a few quick questions: where your code lives, your dev server URL and which agent you use.

### 2️⃣ Step 2: Create a PRD + task list

Describe what you want to build, and the `prd-creator` skill turns it into a plan (PRD) and a task list. Do this in your usual agent (Claude Code, Cursor…), not in Ralph. Open the agent in your project, **switch to plan mode** and paste a prompt like this:

```
Use the prd-creator skill to help me create a PRD and task list for the requirements below.

An app is already set up with React, Tailwind CSS and TypeScript.

Requirements:
- A finance app for freelancers: track income and expenses, send invoices, see reports.
- Use shadcn/ui for components, Stripe for payments and Supabase for the database.
- Env variables (SUPABASE_URL, STRIPE_SECRET_KEY, etc.) are in .env.example.
```

<details>
<summary><strong>✨ Tips for writing requirements</strong></summary>

- Mention the libraries and frameworks you want to use.
- Mention env variables (DB, API keys…). Keep them in `.env`, and make sure `.env` is in `.gitignore`.
- Describe user flows and journeys.
- Put relevant docs and UI references in `/docs` and mention them in the requirements.
- Be as descriptive as possible.
- It's fine to write in your own language.

For a realistic example, watch [the video](https://www.youtube.com/watch?v=3TL8Ez66I3o&t=403s).

</details>

Then answer the skill's questions. It checks with you before each step.

> [!IMPORTANT]
> Read through each task before you start the loop. A few minutes here saves hours later.

<details>
<summary><strong>What the skill walks you through</strong></summary>

1. **Requirement summary**: confirm the scope before going into detail
2. **Prerequisites**: confirm the keys, accounts, test users and database the app needs (listed in `.agent/prd/PREREQUISITES.md`)
3. **PRD**: a short summary, then the full PRD with user flows and diagrams
4. **Task outline**: choose priorities, scope (MVP / MVP+ / full) and what to defer, then confirm before task files are written

Each task is one small feature that works end to end, with its own tests. Anything you defer goes to the Backlog.

</details>

### 3️⃣ Step 3: Set up Docker Sandboxes

Ralph runs your agent in a Docker sandbox, so it can work unattended without touching the rest of your machine.

**1. Install `sbx` and sign in to Docker** (one time)

```bash
# macOS
brew trust docker/tap && brew install docker/tap/sbx

# Linux (Ubuntu)
curl -fsSL https://get.docker.com | sudo REPO_ONLY=1 sh && sudo apt install docker-sbx

# Windows (PowerShell)
winget install -h Docker.sbx

# then sign in to Docker
sbx login
```

> [!TIP]
> Requirements and other install options: [Install Docker Sandboxes](https://docs.docker.com/ai/sandboxes/install).

**2. Sign in to your agent** (one time per project)

```bash
./ralph.sh --login                 # Claude Code (default)
./ralph.sh --login --agent codex   # or another agent
```

This opens the agent in its sandbox. Sign in when it asks, then exit. In Claude Code, run `/login` if it doesn't prompt you, and choose **Yes** for *Bypass Permissions mode* (it's safe because it runs inside the sandbox).

<details>
<summary><strong>More: viewing the app, sandbox names, API keys</strong></summary>

- **See the app in your browser**: after the first run, run `./ralph.sh --ports`. It uses the dev server port you chose during install (change it with `RALPH_DEFAULT_PORTS` in `ralph.sh`).
- **Sandbox names**: each project and agent gets its own sandbox, named `ralph-<agent>-<current-dir>-<hash8>`. Print it with `./ralph.sh --print-name`.
- **API keys**: you can give agents API keys instead of signing in, but it's usually more expensive. See Docker's [supported agents docs](https://docs.docker.com/ai/sandboxes/agents/).
- **Other agents**: see [Running with a different agentic CLI](#running-with-a-different-agentic-cli).

</details>

### 4️⃣ Step 4: Run Ralph

```bash
./ralph.sh -n 50   # work through tasks, up to 50 rounds
```

Each round, Ralph picks one task, builds it, tests it and commits it. You can leave it running.

> [!NOTE]
> The first round sets up the sandbox, so it takes about 5 minutes.

## Running the Ralph Loop with custom options

```bash
# Run the agent loop (default: 10 iterations)
./ralph.sh

# Run with custom iteration limit
./ralph.sh 5
./ralph.sh -n 5
./ralph.sh --max-iterations 5

# Run exactly one iteration
./ralph.sh --once

# Run with a different supported agent
./ralph.sh --agent codex
./ralph.sh -a cursor -n 5

# Log in to an agent inside Ralph's deterministic sandbox
./ralph.sh --login
./ralph.sh --login --agent cursor

# Publish the configured dev port to the selected agent sandbox
./ralph.sh --ports
./ralph.sh --ports --agent codex

# Print the deterministic sandbox name
./ralph.sh --print-name
./ralph.sh --print-name --agent codex

# Pass extra options to the selected agent
./ralph.sh --agent codex -- --model gpt-5.5
./ralph.sh -a gemini -- --model pro

# Show help
./ralph.sh --help
```

> NB: you might need to run `chmod +x ralph.sh` to make the script executable.

> The default "mode" is "implementation". Depending on your use case, you might want to change `.agent/PROMPT.md` to a different mode, e.g. "refactor", "review", "test" etc.

⚠️ If you want to use a different language or testing framework, see below.

### (Optional) Adjusting to your language/framework

This script assumes the following are installed:
- [Playwright](https://playwright.dev/) for e2e testing
- [Vitest](https://vitest.dev/) for unit testing
- [TypeScript](https://www.typescriptlang.org/) for type checking
- [ESLint](https://eslint.org/) for linting
- [Prettier](https://prettier.io/) for formatting

If you'd like to use a different language, testing framework etc. please adjust `.agent/PROMPT.md` to reflect your setup, server ports and startup commands etc.

👉 The loop is controlled by this prompt, which will be sent to the agent each iteration.

---------------------------------

## How It Works

Each iteration, Ralph will:
1. Pick the first incomplete task in `.agent/tasks.json` whose dependencies pass (array order = priority)
2. Check the prerequisites the task needs in `.agent/prd/PREREQUISITES.md`
3. Work through the task steps defined in `.agent/tasks/TASK-{ID}.json`
4. Smoke test every task: UI changes with [agent-browser](https://github.com/vercel-labs/agent-browser) (falling back to the Playwright MCP, then a throwaway Playwright script), with a clean console and a screenshot; CLIs and APIs by running or curling them. UI tasks also get a happy-path Playwright e2e spec
5. Run tests, linting, and type checking
6. Update task status, log progress and commit changes
7. Repeat until all tasks pass or max iterations reached

If the app can't be smoke tested for environmental reasons (no smoke option can open it, or the dev server or port is unreachable because of missing system deps, a port conflict or the sandbox network), Ralph outputs `BLOCKED` and doesn't mark the task done. A dev server that fails on a code error, or an app that loads but is broken, is a bug that Ralph fixes.

## How Is This Different from Other Ralphs?

This was kept hackable so you can make it your own.<br/>
The script follows the original concepts of the Ralph Wiggum Loop, working with fresh contexts and providing clear verifiable feedback.

It also works generically with any task set.

<details>
<summary><strong>✨ Features</strong></summary>

- **PRD generation** - Creates a PRD and task list from requirements
- **Task lookup table generation** - Creates a task lookup table from the PRD
- **Task breakdown + step generation** - Breaks down each task into manageable steps
- **Iteration tracking** - Shows progress through iterations with timing
- **Stream preview** - Shows live output from the Agent
- **Step detection** - Identifies current activity (Thinking, Implementing, Testing, etc.)
- **Screenshot capture** - Captures a screenshot of the current screen
- **Notifications** - Alerts when human input is needed
- **History logging** - Saves clean output from each iteration
- **Timing** - Shows timing metrics for each iteration and total time
- **Steering** - Allows prioritizing critical work that needs to be done before the loop can continue
</details>

<br/>
Besides that:

- it allows you to dump unstructured requirements and have the agent create a PRD and task list for you.
- it uses a task lookup table with individual detailed steps → more scalable as you get 100s of tasks done.
- it's sandboxed and more secure
- it shows progress and stats so you can keep an eye on what's been done
- it instructs the agent to write and run automated tests and screenshots per task
- it provides observability and traceability of the agent's work, showing a stream of output and capturing full historical logs per iteration

## Steering the Agent

In some cases, you might notice the agent is having trouble, slowed down or struggling to overcome a blocker.

While the loop is running, you can edit the `.agent/STEERING.md` file to add critical work that needs to be done before the loop can continue.

The agent will check this file each iteration and if it finds any critical work, it will skip tasks and complete the critical work first.

## Support

The `ralph.sh` script is designed to be hackable.
It is configured to use Claude Code in Docker Sandboxes by default, and you can select another supported agent with `--agent`.
Each run uses a deterministic sandbox name in the form `ralph-<agent>-<current-dir>-<hash8>`, so different agents get separate sandboxes for the same project. On exit or double Ctrl+C, Ralph stops only the named sandbox for the current invocation.

> NB: skills and `AGENTS.md` work across all major agentic AI CLIs (Claude Code, Codex, Cursor, Gemini CLI, OpenCode, Copilot, Amp, etc.) via two symlinked skills dirs.

### Promise Tags

Ralph uses semantic tags to communicate status:
- `<promise>COMPLETE</promise>` - All tasks finished successfully
- `<promise>BLOCKED:reason</promise>` - Agent needs human help
- `<promise>DECIDE:question</promise>` - Agent needs a decision

### Exit Codes

| Code | Meaning                        |
| ---- | ------------------------------ |
| 0    | COMPLETE - All tasks finished  |
| 1    | MAX_ITERATIONS - Reached limit |
| 2    | BLOCKED - Needs human help     |
| 3    | DECIDE - Needs human decision  |

## Structure

```
.agent/
├── PROMPT.md           # Prompt sent to Agent each iteration
├── STRUCTURE.md        # Directory map, one line per entry (seeded on install, never overwritten)
├── tasks.json          # Task lookup table (required; seeded on install, never overwritten)
├── tasks/              # Individual task specs (TASK-{ID}.json)
├── prd/
│   ├── PRD.md          # Product requirements document
│   ├── PREREQUISITES.md # Approved prerequisite ledger (keys, accounts, test users, infra)
│   └── SUMMARY.md      # Short project overview sent to Agent each iteration
├── logs/
│   └── LOG.md          # Progress log (seeded on install, never overwritten)
├── history/            # Iteration output logs
└── skills/             # Shared skills (source of truth)
```

## Continued Development

As Ralph implements tasks, you might notice that you want some tweaks, features or even bug fixes.<br/>
To do so, you need to continue using the `prd-creator` skill to update the PRD and task list.

For example:

```
I would like to expand the PRD. Use the prd-creator skill to create these tasks:

- there is a bug in X that should be fixed by doing Y
- create a new feature that implement Z

etc.
```

It's fine to add multiple tasks at once. The skill shows an outline of the new tasks for you to steer and confirm before writing them.

To pick up something you deferred earlier, ask the skill to promote it from the PRD's Backlog:

```
Use the prd-creator skill to promote "CSV export" from the Backlog into tasks.
```

## Skills

Skills are reusable agent capabilities that provide specialized knowledge and workflows. The canonical source is `.agent/skills/`, which is symlinked into the two directories agents actually scan.

### Available Skills

| Skill                         | Description                                             |
| ----------------------------- | ------------------------------------------------------- |
| `agent-browser`               | Browser automation; Ralph's default smoke-test tool (screenshots, console checks) |
| `component-refactoring`       | Patterns for splitting and refactoring React components |
| `e2e-tester`                  | End-to-end testing workflows                            |
| `frontend-code-review`        | Code quality and performance review guidelines          |
| `frontend-testing`            | Unit and integration testing patterns                   |
| `grill-me`                    | Stress-test a plan or design through relentless questioning |
| `mysql`                       | MySQL/InnoDB schema, indexing, query tuning, and ops    |
| `postgres`                    | PostgreSQL best practices and query optimization        |
| `prd-creator`                 | Create PRDs and task breakdowns for Ralph               |
| `shadcn`                      | Manage shadcn components, registries, and UI composition |
| `skill-creator`               | Create new skills                                       |
| `vercel-react-best-practices` | React/Next.js performance patterns                      |
| `vitest-best-practices`       | Vitest structure, assertions, mocks, async tests, and performance |
| `web-design-guidelines`       | UI/UX design principles                                 |

### Skills Directory Structure

Skills are symlinked from `.agent/skills/` into the two directories agents scan:

```
# Source of truth
.agent/skills/
    ├── component-refactoring/
    ├── e2e-tester/
    ├── postgres/
    ├── ...

# Symlinks -> .agent/skills/*
.agents/skills/*   # Codex, Cursor, Gemini CLI, OpenCode, Copilot, Amp, Windsurf, Droid
.claude/skills/*   # Claude Code (also read by Cursor, OpenCode, Copilot, Cline)
```

Project instructions live in `AGENTS.md`, which every supported agent reads natively except two:
- **Claude Code** reads `CLAUDE.md`, which imports `@AGENTS.md`.
- **Gemini CLI** reads `GEMINI.md` by default, so the installer adds `AGENTS.md` to `context.fileName` in `.gemini/settings.json`.

To add your own skill, create `.agent/skills/<name>/SKILL.md` and symlink it into both dirs (or re-run the installer).

## Reference

### Docker Sandboxes

Docker Sandboxes runs coding agents in isolated microVMs. Ralph uses the standalone `sbx` CLI and starts agents with a deterministic `--name` so the sandbox can be reused and stopped cleanly.

Use `./ralph.sh --login` to authenticate inside the correct named sandbox. Use `./ralph.sh --print-name` if you only need the deterministic sandbox name for debugging.

Useful Docker references:
- [Docker AI overview](https://docs.docker.com/ai-overview/) explains how Docker Sandboxes fits with Gordon, Model Runner, MCP Toolkit, and Docker Agent.
- [Docker Sandboxes](https://docs.docker.com/ai/sandboxes/) covers installation, usage, security, credentials, and troubleshooting.
- [Supported Docker Sandboxes agents](https://docs.docker.com/ai/sandboxes/agents/) lists the agent CLIs Docker supports.

### Playwright configuration

If you are using Playwright, here is a recommended configuration:

```typescript:playwright.config.ts
import { defineConfig, devices } from '@playwright/test';

/**
 * See https://playwright.dev/docs/test-configuration.
 */
export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  globalTimeout: 30 * 60 * 1000,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 1,
  workers: process.env.CI ? 3 : 6,
  reporter: 'html',
  use: {
    baseURL: 'http://localhost:3000',
    trace: 'on-first-retry',
  },


  // NB: only chromium will run in Docker (arm64).
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    }
  ],
});
```

### Vitest configuration

If you are using Vitest, here is a recommended configuration:

```typescript:vitest.config.ts
import { defineConfig } from "vitest/config";
import react from "@vitejs/plugin-react";
import path from "path";

export default defineConfig({
  plugins: [react()],
  test: {
    environment: "node",
    globals: true,
    include: ["lib/**/*.test.ts", "lib/**/*.test.tsx"],
    // setupFiles: ['./vitest.setup.ts'], // Include this if using Next.js
  },
  resolve: {
    alias: {
      "@": path.resolve(__dirname),
    },
  },
});

```

If you are using Next.js, you'll also need a `vitest.setup.ts` file to mock the `next/image` and `next/link` components.

```typescript:vitest.setup.ts
import '@testing-library/jest-dom/vitest'
import { vi } from 'vitest'
import React from 'react'

// If using Next.js, mock next/image
vi.mock('next/image', () => ({
  default: ({ src, alt, ...props }: { src: string; alt: string }) => {
    return React.createElement('img', { src, alt, ...props })
  },
}))

// If using Next.js, mock next/link
vi.mock('next/link', () => ({
  default: ({
    children,
    href,
    ...props
  }: {
    children: React.ReactNode
    href: string
  }) => {
    return React.createElement('a', { href, ...props }, children)
  },
}))
```

### Running with a different agentic CLI

Ralph can run several Docker Sandboxes agents without editing the script:

```bash
./ralph.sh --agent claude    # default
./ralph.sh --agent codex
./ralph.sh --agent copilot
./ralph.sh --agent cursor
./ralph.sh --agent gemini
./ralph.sh --agent opencode
```

You can also pass agent-specific options after Ralph's `--` separator:

```bash
./ralph.sh --agent codex -- --model gpt-5.3-codex
./ralph.sh --agent gemini -- --model pro
```

Ralph currently supports: `claude`, `codex`, `copilot`, `cursor`, `gemini`, and `opencode`.
See Docker's full list of supported agentic AI CLIs in [Docker's docs](https://docs.docker.com/ai/sandboxes/agents/).
Because the agent name is part of Ralph's sandbox name, switching agents creates or reuses that agent's own sandbox for the project.

### Starting from scratch

For AI to actually verify its implementation and for the loop to work, you need a way to verify it.

To that end, at the minimum you'll need an end-to-end test framework and a unit test framework.

For example, you can use the following commands to install Playwright and Vitest:

```bash
npm i @playwright/test vitest jsdom typescript eslint prettier -D

# If using React, also recommend installing:
npm i @vitejs/plugin-react @testing-library/dom @testing-library/jest-dom @testing-library/react @testing-library/user-event -D
```

It is recommended that you add skills for your specific language and framework. See [skills.sh](https://skills.sh) to discover existing skills.

## Debugging

### How to inspect the sandbox and debug

You might be wondering... if this is not a Docker container, how can you see what's going on inside Docker!?
How to debug/install things?

That's quite straightforward.

You first need to run:

```bash
sbx ls
```

Note down the name of the sandbox for the agent you ran, e.g. `ralph-claude-my-app-a1b2c3d4`. Ralph also prints this name when it starts.

And then you can run bash into any of the sandboxes like so:
```bash
sbx exec -it <sandbox-name> bash # e.g. sbx exec -it ralph-claude-my-app-a1b2c3d4 bash
```

And you have full control over the sandbox, just like a regular container. You can install packages, run commands, etc.

You can also run the agent CLI inside the sandbox (make sure to navigate to the project directory first).

```bash
sbx exec -it <sandbox-name> bash
cd /path/to/your/project # this is the same path as the path in the root machine, e.g. /Users/your-username/Documents/your-project
claude # or codex, copilot, cursor, gemini, opencode
```

Re-running `./ralph.sh`, `./ralph.sh --login`, or `./ralph.sh --ports` is safe at any point — Ralph probes `sbx ls` and emits `sbx run --name ... <agent> .` only when the sandbox doesn't exist yet, and `sbx run <sandbox-name>` to reattach afterwards. The first form is create-only and would otherwise error with `--name can only be used when creating a new sandbox`. See the [sandbox debugging guide](https://ralphloop.sh/blog/debug-inside-an-agent-sandbox/#reattach-a-stopped-sandbox-with-sbx-run) for the full lifecycle.

### Allowing network access

Docker Sandboxes block outbound HTTP/HTTPS by default (deny-by-default, or a "Balanced" allowlist depending on the policy you chose at install). If the agent can't reach a host it needs — `npm install` fails, an API call is refused, package downloads hang — grant access with `sbx policy`. Changes take effect immediately and persist across sandbox restarts.

Use the sandbox name from `sbx ls` (or `./ralph.sh --print-name`), e.g. `ralph-claude-my-app-a1b2c3d4`.

Allow a single domain for one sandbox:

```bash
sbx policy allow network <my-sandbox> api.example.com
```

Allow all outbound traffic for one sandbox (use sparingly — this opts that sandbox out of network filtering):

```bash
sbx policy allow network <my-sandbox> "**"
```

Allow several domains at once with a comma-separated list (handy when package installs are blocked):

```bash
sbx policy allow network <my-sandbox> "*.npmjs.org,*.pypi.org,files.pythonhosted.org,github.com"
```

Apply a rule to every sandbox on the machine with the global flag `-g` instead of a sandbox name:

```bash
sbx policy allow network -g api.example.com
```

Inspect and manage rules:

```bash
sbx policy ls                                  # list active rules
sbx policy log                                 # inspect connection history
sbx policy deny network <my-sandbox> ads.example.com   # block a host
```

Domain matching notes:
- `example.com` matches only the exact domain (any port); it does **not** match subdomains.
- `*.example.com` matches subdomains like `api.example.com` but **not** the root `example.com` — specify both to cover both.
- Append a port to scope the rule, e.g. `example.com:443`.
- If a domain matches both an allow and a deny rule, the deny rule wins.

See Docker's [Policies](https://docs.docker.com/ai/sandboxes/security/policy/) and [Network policies](https://docs.docker.com/ai/sandboxes/network-policies/) docs for the full reference.

### Authentication issues in Sandboxes / Login not persisting

Agentic CLIs might change their auth mechanism over time and Docker Sandboxes might fail persisting OAuth tokens (when you perform `/login` inside the sandbox shell).

Fortunately, Docker Sandboxes also forward env variables **when you create a sandbox**.

Here's how to set up authentication using an API key:

1. Important 🚨: delete the sandbox that needs authentication. Env vars are only picked up when you create a new sandbox.

2. Go to [Docker security credentials](https://docs.docker.com/ai/sandboxes/security/credentials/) to find each env variables you need. For example, anthropic needs `ANTHROPIC_API_KEY`, OpenAI need `OPENAI_API_KEY`, Cursor needs `CURSOR_API_KEY`, etc.

3. Export the env variables in your shell. For example:

```bash
export ANTHROPIC_API_KEY=your-anthropic-api-key
export OPENAI_API_KEY=your-openai-api-key
export CURSOR_API_KEY=your-cursor-api-key
```

> If you use bash, you can export the env variables in your `.bashrc` file, or if you use zsh, you can export the env variables in your `.zshrc` file.

4. Recreate the sandbox by running `./ralph.sh --login` again.

## License

MIT
