# AI Code Reviewer

A GitHub Actions bot that automatically reviews pull requests using the Claude API. When a PR is opened or updated, the bot fetches the diff, sends each changed file to Claude for analysis, and posts inline comments and a summary directly on the PR.

The bot is based on the following guide: [cloudflare tutorials](https://developers.cloudflare.com/sandbox/tutorials/code-review-bot/)

A demo is available in the following pull request: [demo](https://github.com/MoaKK/AI-Code-Reviewer/pull/1)

---

## Setup

### 1. Copy the workflow file

Copy `.github/workflows/code-review.yml` into your target repository.

### 2. Copy the scripts folder

Copy the entire `scripts/` folder into the root of your target repository.

### 3. Add the API key secret

In your repository go to **Settings → Secrets and variables → Actions** and add:

| Secret name | Value |
|---|---|
| `ANTHROPIC_API_KEY` | Your API key from [console.anthropic.com](https://console.anthropic.com) |

`GITHUB_TOKEN` is provided automatically by GitHub Actions, you do not need to add it.

### 4. That's it

Open a pull request and the bot will trigger automatically.

---

## What the bot reviews

- Only files changed in the PR
- On a re-push to an existing PR, only files changed in that specific push (not the whole PR again)

## What the bot skips

- `package-lock.json` and all `*.lock` files
- Anything inside a `dist/` directory

To add more exclusions, edit the `IGNORED_FILES` regex in `scripts/src/constants.ts`.

---

## Customising the review instructions

The prompt that controls what Claude focuses on lives in `scripts/src/constants.ts` as `REVIEW_INSTRUCTIONS`. Edit it to change the tone, focus areas, or output format.

---

## Project flow

### Entry point

GitHub Actions triggers the workflow in `.github/workflows/code-review.yml` whenever a PR is opened or a new commit is pushed to one. The workflow checks out the code, installs dependencies, and runs:

```
npm start  →  tsx src/review.ts
```

### `scripts/src/review.ts` — orchestrator

This is where execution begins. `main()` calls the other modules in order:

1. `getPRFiles()` — fetch the files to review
2. `reviewFile()` — send each file to Claude
3. `postReview()` — post inline comments on the PR
4. `postSummary()` — post a top-level summary comment

### `scripts/src/github.ts` — GitHub API

Handles all communication with GitHub:

- **`getPRFiles()`** — decides which files to fetch. On a new PR (`opened`) it fetches all changed files via `listFiles`. On a re-push (`synchronize`) it uses `compareCommits` between the previous and new SHA so only the files touched in that push are reviewed. Both paths filter out ignored files and parse each patch into a `DiffFile`.
- **`parseValidLines()`** — reads the raw unified diff and builds a `Set<number>` of line numbers that actually exist in the new version of the file. Used to drop any comment Claude returns that references a line outside the diff.
- **`postReview()`** — posts all inline comments as a single GitHub review. If the batch call fails (e.g. one bad line number slipped through), it falls back to posting each comment individually so the rest are not lost.
- **`postSummary()`** — posts a top-level PR comment with a count of issues found per file, or a "no issues found" message if Claude had nothing to say.

### `scripts/src/claude.ts` — Claude API

Contains a single function `reviewFile()` which:

1. Sends the file path and its diff patch to `claude-sonnet-4-6` with the review instructions as a cached system prompt
2. Strips any markdown fences from the response (Claude sometimes wraps JSON in fences despite being told not to)
3. Parses the JSON array of comments
4. Filters out any comment whose `path` doesn't match the file being reviewed or whose `line` is not in the valid line set

### `scripts/src/constants.ts` — static config

Holds three exports used across the other modules:

- `REVIEW_INSTRUCTIONS` — the system prompt sent to Claude on every call
- `IGNORED_FILES` — the regex used to filter out generated and lock files
- `MODEL` — the Claude model name, in one place so it's easy to change

### `scripts/src/types.ts` — shared types

Defines two interfaces used across all modules:

- `DiffFile` — a changed file with its filename, raw patch string, and the set of valid line numbers
- `ReviewComment` — a single comment with a file path, line number, and body text
