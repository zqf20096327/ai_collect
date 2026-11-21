# Build your own AI code reviewer

<picture>
  <source media="(prefers-color-scheme: dark)" srcset=".github/assets/reviewer-ui-dark.png">
  <img alt="The local reviewer UI: three agents, findings grounded in the diff, cost per run and a FAIL gate" src=".github/assets/reviewer-ui-light.png">
</picture>

Hands-on workshop, GDG DevFest Warsaw 2026 · 45 minutes.

**Slides:** [Talk](https://burnjohn.github.io/ai-code-reviewer-workshop/talk/) · [Workshop](https://burnjohn.github.io/ai-code-reviewer-workshop/workshop/) (sources in [`docs/`](docs/); rebuild the workshop deck with `node docs/workshop/build.mjs`).

You build a reviewer that runs as a GitHub Action, reads the repository (not only the diff), calls a model through OpenRouter, gets **structured** findings back, drops findings that cite lines outside the diff, runs several specialised agents, and decides pass/fail **in code**. A human still merges.

The review target is a real public repo, [`burnjohn/quick-blog`](https://github.com/burnjohn/quick-blog): an analytics-dashboard pull request with planted defects, some of which are visible only against its spec.

```
PR + repo ─► context ─► prompt ─► OpenRouter (json_schema) ─► grounding ─► dedup ─► gate ─► inline review
```

## Setup (5 min)

1. **Use this template → Create a new repository.** Tick **Include all branches** (you need the checkpoint branches). Keep it **public**: your workflow checks it out without a token.
2. Open a Codespace on `main` (or locally: Node 22).
3. Create `.env` from the example and add your OpenRouter key (`.env` is gitignored):

```bash
cp .env.example .env      # then set OPENROUTER_API_KEY=sk-or-...
npm ci
npm test                  # red by design: 29 failed | 16 passed
npm run review:mock       # offline: recorded PR + recorded model answers
npm run review            # real: fetches the PR from GitHub, calls OpenRouter
npm run ui                # the same reviewer in a browser: http://127.0.0.1:3000 (PORT, HOST override)
```

`REVIEW_PR` in `.env` is the default PR (`burnjohn/quick-blog#34`); `--pr owner/repo#N` overrides it. Without a `GITHUB_TOKEN` the GitHub API allows 60 requests per hour per IP, which a room on one Wi-Fi shares; set `GITHUB_TOKEN` in `.env` (a Codespace already has one), or use `npm run review:mock`.

## Steps

Each step has a spec in [`specs/`](specs/README.md) with a prompt for your coding agent. Steps are cumulative: step N starts from the solution of step N-1.

| Step | You change | Spec |
|---|---|---|
| 1 · Findings you can trust | `src/schema.ts`, `src/prompt.ts`, `src/grounding.ts` | [step-1](specs/step-1-findings.md) |
| 2 · Repository context | `src/context.ts` | [step-2](specs/step-2-context.md) |
| 3 · Gate + GitHub Action | `src/gate.ts`, `examples/quick-blog-workflow.yml` | [step-3](specs/step-3-github-action.md) |
| 4 · More reviewers | `.reviewer/agents/*.md`, `src/dedup.ts` | [step-4](specs/step-4-more-reviewers.md) |

Branches: `main` is the starter; each checkpoint branch holds the **solution** of one step. Lost? `git stash && git checkout <branch>`.

| Branch | Contents |
|---|---|
| `main` | starter, start of step 1 |
| `step-1-findings` | solution of step 1 |
| `step-2-context` | solution of step 2 |
| `step-3-gate-action` | solution of step 3 |
| `step-4-more-reviewers` | solution of step 4 |
| `final` | full functionality (= `step-4-more-reviewers`) |
| `stretch/mcp` | `final` + MCP tool |

**No MCP? Use the UI.** `npm run ui` serves a one-page local UI (no build step): pick the PR, agents, model, context on/off, mock on/off, and see findings, dropped findings, the context log, per-agent cost and the gate. It runs the same code as the CLI, never posts to GitHub, and is on every branch; on `main` it shows the starter state.

## Step 3: run it on QuickBlog in your fork

1. Fork `burnjohn/quick-blog`. **Untick "Copy the main branch only"**, otherwise the `analytics` branch is not copied.
2. In the fork, **Actions** tab: enable workflows. Forks start with Actions off.
3. Add your OpenRouter key to the fork: **Settings → Secrets and variables → Actions → New repository secret**, name `OPENROUTER_API_KEY`, value = the same key as in your `.env` (or `gh secret set OPENROUTER_API_KEY -R <you>/quick-blog`). Without it the review step fails.
4. In your fork on GitHub: **Add file → Create new file**, name it `.github/workflows/ai-review.yml`, paste the contents of your `examples/quick-blog-workflow.yml` and commit to `main`. It runs the reviewer from the `final` branch of **your** `ai-code-reviewer-workshop` repo. To run your own code instead, push it to a new branch (`git push origin HEAD:my-reviewer`) and set the Actions variable `REVIEWER_REF=my-reviewer` in the fork.
5. Open a pull request inside your fork: base `main`, compare `analytics`: `gh pr create -R <you>/quick-blog -B main -H analytics -t Analytics -b ""`. Inline comments and a red check appear in about 2–3 minutes (three agents run in parallel).

## Environment variables

| Name | Meaning |
|---|---|
| `OPENROUTER_API_KEY` | OpenRouter key |
| `REVIEW_PR` | default PR, `owner/repo#N` |
| `GITHUB_TOKEN` | optional locally (rate limit); required in CI |
| `REVIEW_MODEL` | overrides the `model:` of every agent |
| `AGENTS=general,security` | run only these agents |
| `CONTEXT_BUDGET` | context size in characters (default 60000) |
| `REVIEWER_REF` | CI only (Actions variable in the fork): branch of your reviewer repo the workflow runs, default `final` |
| `REVIEW_MOCK=1` | no network: recorded PR and answers from `fixtures/quick-blog/` |

CLI flags: `--pr`, `--repo-dir <dir>`, `--no-context`, `--dry-run` (print prompt sizes, call no model), `--ci`, `-v`.

## Maintainer: recording the offline fixtures

`npm run record` stores the PR snapshot (`fixtures/quick-blog/pr.json`, `diff.patch`, `repo/`) and one real model answer per agent, with and without context (`fixtures/quick-blog/answers/`). It needs `OPENROUTER_API_KEY`, and the `final` branch. `npm run record -- --snapshot-only` needs no key. The answers are committed on every branch; re-record them after changing an agent prompt or its model.

## Stretch (at home)

Branch `stretch/mcp` exposes the reviewer as an MCP tool, `review_working_copy`, for your coding agent: `claude mcp add ai-reviewer -- npx tsx mcp/server.ts`.

Core extracted and simplified from [DevDigest](https://github.com/ai-agentic-engineering-neo/dev-digest). MIT.
