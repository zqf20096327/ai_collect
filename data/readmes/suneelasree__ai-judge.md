# ⚖️ AI Judge

[![ci](https://github.com/suneelasree/ai-judge/actions/workflows/ci.yml/badge.svg)](https://github.com/suneelasree/ai-judge/actions/workflows/ci.yml) [![npm](https://img.shields.io/npm/v/@suneelasree/ai-judge)](https://www.npmjs.com/package/@suneelasree/ai-judge) [![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

**Give it a user story. It reviews the acceptance criteria, designs test cases, tests your web app in Chrome like a senior QA engineer, judges pass or fail with screenshot evidence, and, once you approve, files the defects in Jira.**

```text
aijudge run PROJ-123

[1/7] Read story                 ✔ PROJ-123: Reset password · 4 acceptance criteria · 2 URLs
[2/7] Acceptance-criteria gate   ✔ All 4 criteria testable
[3/7] Design test cases          ✔ 9 test cases → test-cases.md
[4/7] Execute in Chrome          ✔ TC-01 PASSED  ✖ TC-04 FAILED: no error shown for an unknown email ...
[5/7] Results                    7 passed · 1 failed · 1 blocked · 0 skipped
[6/7] Consolidate defects        2 defect(s)
[7/7] Human gate                 Raise in Jira? all / none / ids (e.g. D-01,D-03): D-01
                                 ✔ D-01 → PROJ-130
```

AI Judge works with any web app and any Jira site, and with stories kept in plain Markdown files. Nothing is specific to one product.

---

## What it does

| Stage | What happens | Output |
|---|---|---|
| 1. Read story | Loads a Jira issue (Cloud or Server/Data Center) or a `.md` / `.txt` / `.json` story file. Pulls out the acceptance criteria and every URL. | `story.json` |
| 2. **AC gate** | **No acceptance criteria → it stops and says so** (no AI call, no tests). If ACs exist, an AI reviewer checks that each one is testable and stops with questions for the story owner when one isn't. `--force` overrides. | `ac-gate.json` |
| 3. Design | Step-by-step test cases (positive, negative, edge) with URLs, test data, expected results, and AC traceability. | `test-cases.md`, `test-cases.json` |
| 4. Execute | An AI agent drives a real Chrome window: reads the page, clicks, types, checks each expected result, and records a screenshot per step. | `screenshots/` |
| 5. Judge | Each case is marked **passed / failed / blocked / skipped**, with the actual result and the reason. | `report.html`, `report.md` |
| 6. Defects | Failures and usability observations are merged into one deduplicated defect list with severity, steps to reproduce, and evidence. | `defects.json` |
| 7. **Human gate** | You choose what to raise: all, none, or specific ids. Only then does it create Jira bugs, link them to the story, and attach the screenshots. | Jira issues |

## Quick start

Requires **Node 22.12+** and Google Chrome (or run `npx playwright install chromium`).

```bash
npm install -g @suneelasree/ai-judge   # or: npx @suneelasree/ai-judge ...
mkdir my-qa && cd my-qa
aijudge init                   # creates aijudge.config.json and .env.example
cp .env.example .env           # fill in your keys
aijudge doctor                 # checks Claude, Jira and the browser

aijudge plan examples/sample-story.md --base-url https://demo.playwright.dev/todomvc   # design only
aijudge run PROJ-123                                                                    # full pipeline
```

### Credentials (`.env`)

| Variable | Needed for |
|---|---|
| `ANTHROPIC_API_KEY` | The AI (Claude). Alternatively, sign in once with `ant auth login`. |
| `JIRA_BASE_URL`, `JIRA_EMAIL`, `JIRA_API_TOKEN` | Jira Cloud. Create a token at id.atlassian.com → Security → API tokens. |
| `JIRA_PAT` | Jira Server / Data Center (with `"deployment": "server"` in the config). |
| `AIJUDGE_SECRET_<NAME>` | Values the agent types **without ever seeing them**, e.g. `AIJUDGE_SECRET_PASSWORD`. |

Secrets live only in environment variables, never in the config file or in reports.

## Commands

```text
aijudge run <story>     Full pipeline. <story> = PROJ-123 | Jira browse URL | story.md
  -u, --base-url <url>    App under test (overrides config)
  --plan-only             Stop after designing test cases
  --force                 Continue when ACs are judged unclear
  --only TC-01,TC-03      Run selected test cases
  --max-cases <n>         Upper bound on designed cases (default 12)
  --reuse-plan <run-dir>  Re-run with the test cases of an earlier run (no redesign, lower cost)
  --headless              No visible browser window (CI)
  --raise ask|all|none    Human gate (default ask; non-interactive runs never raise unless "all")
  --allow-destructive     Let the agent click delete/remove-style controls

aijudge plan <story>    AC gate + test design only
aijudge raise <run-dir> Open the human gate again for a finished run
aijudge doctor          Check credentials, Jira access and the browser
aijudge init            Create starter config files
```

Exit codes: `0` all good · `1` test failures · `2` stopped at the AC gate · `3` error. That makes it easy to use as a CI step.

## Configuration (`aijudge.config.json`)

```jsonc
{
  "baseUrl": "https://staging.example.com",
  "allowedHosts": ["login.example.com"],        // extra hosts the agent may open (e.g. SSO)
  "model": "claude-opus-5-5",
  "effort": "high",                              // low | medium | high | xhigh | max
  "testContext": "Log in as the QA user. Orders over $500 need approval.",
  "jira": {
    "deployment": "cloud",                       // or "server"
    "acceptanceCriteriaField": "customfield_10035", // if your ACs live in a custom field
    "defectProject": "QA",                       // default: the story's project
    "defectIssueType": "Bug",
    "defectLabels": ["ai-judge"],
    "priorityMap": { "critical": "Highest", "high": "High", "medium": "Medium", "low": "Low" },
    "linkType": "Relates"
  },
  "browser": {
    "channel": "chrome",                         // chrome | msedge | chromium
    "headless": false,
    "storageState": "auth.json",                 // reuse a logged-in session (optional)
    "isolateTests": true,                        // fresh cookies/localStorage per test case
    "maxTurnsPerTest": 40,
    "allowDestructive": false
  },
  "outputDir": "aijudge-runs"
}
```

### Writing stories it can read

AI Judge finds acceptance criteria under a heading such as **Acceptance Criteria**, **AC**, or **Definition of Done** (Markdown heading, bold line, or `AC:`), written as bullets, numbered items, Jira checklists, or Given/When/Then scenarios. See [`examples/sample-story.md`](examples/sample-story.md). A story without them is rejected at stage 2. That's deliberate: a test is only as good as its expected result.

## Safety by design

- **Human gate:** nothing is written to Jira without explicit approval.
- **Host allow-list:** the agent can open only the base URL, URLs in the story, and `allowedHosts`.
- **Destructive-action guard:** clicks on delete/remove/purge-style controls and `confirm()` dialogs are refused unless you pass `--allow-destructive`.
- **Hidden secrets:** passwords are typed by name; the AI never sees the value.
- **Prompt-injection hardening:** page content and story text are treated as data, never as instructions.
- **Honest verdicts:** environment problems are reported as *blocked*, not *failed*, and every step carries screenshot evidence.

AI verdicts can be wrong. Review the defects before raising them; that's what the human gate is for.

## Programmatic use

```ts
import { loadConfig, runPipeline } from "@suneelasree/ai-judge";

const { summary, exitCode } = await runPipeline({
  storyRef: "PROJ-123",
  cfg: loadConfig(),
  planOnly: false,
  force: false,
  raise: "none",
  maxCases: 10,
});
console.log(summary.defects);
```

To support another tracker (Azure Boards, Linear, GitHub Issues), implement the `StorySource` interface in [`src/sources`](src/sources/index.ts).

## How it works

- **Stories:** the Jira REST API (v3 Cloud / v2 Server), with Atlassian Document Format converted to Markdown.
- **AI:** Claude via the official Anthropic SDK. Stages 2, 3 and 6 use structured outputs validated by Zod schemas. Stage 4 is a tool-using agent loop with 15 strict browser tools (`navigate`, `snapshot`, `click`, `fill`, `fill_secret`, `record_step`, `finish_test`, ...). The agent reads pages through Playwright's accessibility snapshot and can request screenshots to check visual state.
- **Browser:** Playwright driving installed Chrome; one browser per run and, by default, a fresh context per test case (cookies and localStorage do not leak between cases; `storageState` re-seeds a login each time).

## Development

```bash
git clone https://github.com/suneelasree/ai-judge && cd ai-judge
npm install
npm test            # unit tests + real-browser tool tests (no AI calls)
npm run build
node dist/cli.js --help
```

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE) © Suneela Sadhu
