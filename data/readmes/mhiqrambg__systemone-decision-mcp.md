# systemone-decision-mcp

An MCP server that tells an OpenCode agent which MCP tools and skills a task actually
needs, before the agent starts calling them.

Decisions come from a remote decision model reached over an OpenAI-style API. When that
model is unreachable, a deterministic engine answers instead, and every response says which
engine produced it.

This is a usage guide. Architecture, configuration reference, and benchmark analysis live
in [`docs/`](docs/).

## What it changes

An agent with many MCP servers tends to fail in two ways. It answers a repository question
with built-in grep and never opens the code graph, or it fires a web search at a question
that any engineer could answer from memory. Both cost time and context.

This server makes the routing decision explicit for each task: which tools are worth
calling, which are noise, and what priority each one carries.

## What it does not do

It cannot invoke, filter, or observe other MCP servers. MCP has no primitive for that, and
any tool claiming otherwise is guessing. The agent performs the calls. The agent also
reports them back if it wants an audit.

Recommendations are advice, not permission. OpenCode's own approval prompts still apply to
every tool call.

## Requirements

- Node.js 20 or newer (built and tested on 24.11.1)
- npm 9 or newer
- OpenCode v2
- An OpenAI-style decision endpoint: its URL, a model id, and a bearer token. Without all
  three the server still runs on the rule-based engine and labels every answer.

## Install

```bash
git clone https://github.com/mhiqrambg/systemone-decision-mcp.git
cd systemone-decision-mcp
npm install
npm run build
npm run doctor
```

`npm run doctor` checks the Node version, the environment variables, the endpoint, a
live round trip, the tool catalog, the skill index, and the OpenCode config it can read.
It exits 2 if any check needs attention.

## Configure

Five values matter. Everything else has a default.

```env
SYSTEMONE_API_KEY=
SYSTEMONE_ENDPOINT=https://your-host/v1/your-route
SYSTEMONE_MODEL=your-model-id
SYSTEMONE_DEFAULT_THRESHOLD=0.80
SYSTEMONE_REQUIRED_AT=0.93
```

Copy `.env.example` to `.env` and fill in the key. The server and the CLI scripts load
`.env` automatically, from the working directory first and then from the project root. Real
environment variables always take precedence, so a shell export or OpenCode's `environment`
block overrides the file. Only keys starting with `SYSTEMONE_` are accepted from it,
which stops a cloned `.env` from setting `NODE_OPTIONS` or `PATH`.

`.env` is gitignored. `SYSTEMONE_NO_DOTENV=1` disables loading entirely, which is what the test
suite uses.

Full table: [`docs/CONFIGURATION.md`](docs/CONFIGURATION.md).

## Add it to OpenCode

Merge this into `opencode.json`. Do not replace the file.

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "systemone-decision": {
      "type": "local",
      "command": ["node", "/absolute/path/to/systemone-decision-mcp/dist/index.js"],
      "enabled": true,
      "environment": {
        "SYSTEMONE_API_KEY": "{env:SYSTEMONE_API_KEY}",
        "SYSTEMONE_ENDPOINT": "{env:SYSTEMONE_ENDPOINT}",
        "SYSTEMONE_MODEL": "{env:SYSTEMONE_MODEL}"
      }
    }
  }
}
```

`{env:SYSTEMONE_API_KEY}` is OpenCode's own substitution, so the key never lands in the config
file. Use the full path to `dist/index.js`. On native Windows, escape the backslashes:
`"C:\\Users\\you\\systemone-decision-mcp\\dist\\index.js"`.

Then copy [`examples/AGENTS.md`](examples/AGENTS.md) into your `AGENTS.md`. That file tells
the agent when to call the router and what to do with the answer. Without it, the agent has
the tools and no reason to use them.

Confirm the server loaded:

```bash
opencode mcp list
```

Eight `systemone_*` tools should appear.

## How to use it

### Before a complex task

Call `systemone_decide_tools` with the user request. Include the servers you know are live in this
session, because OpenCode may enable MCP servers per agent rather than in the config file.

```json
{
  "user_query": "Find the authentication function in my repository and check whether it follows the latest Fastify documentation.",
  "context": {
    "available_mcp_servers": ["context7", "codebase-memory-mcp", "github", "media-9router"]
  }
}
```

A real response, trimmed:

```json
{
  "task_id": "7a3bd74c-e2fa-45c9-9da1-890aa713dfd5",
  "decision_status": "success",
  "decision_source": "model",
  "model_used": "example-model-20260101",
  "recommendations": [
    { "tool_id": "context7", "score": 0.98, "priority": "required", "threshold": 0.8 },
    { "tool_id": "codebase_memory", "score": 0.97, "priority": "required", "threshold": 0.8 },
    { "tool_id": "file_search", "score": 0.97, "priority": "recommended", "threshold": 0.75 },
    { "tool_id": "websearch", "score": 0.88, "priority": "recommended", "threshold": 0.8 }
  ],
  "not_recommended": [
    { "tool_id": "codegraph", "score": 0.46 },
    { "tool_id": "web_fetch", "score": 0.28 }
  ],
  "execution_guidance": [
    "Use Context7 (required) for library_documentation and framework_documentation.",
    "Use Codebase Memory (required) for repository_analysis and code_relationships."
  ],
  "usage": { "input_tokens": 780, "output_tokens": 173, "cost": 0.00003276 }
}
```

Read `recommendations` and stop there. Anything under `not_recommended` is a tool that would
have cost a call without adding evidence.

### During the task

Call the tools marked `required` and `recommended`. Skip `optional` unless the call is cheap
and you expect it to pay off. Never call something listed under `not_recommended` for that
task.

If the response says `decision_status: "no_tools_needed"`, answer directly. That status comes
from the capability classifier finding no requirement at all, which is the normal result for
definitions, explanations, and reasoning.

When you are unsure about one tool, call `systemone_check_tool_need` instead of a full decision. It
costs one question.

### After the task

Report what you actually called:

```json
{
  "task_id": "7a3bd74c-e2fa-45c9-9da1-890aa713dfd5",
  "executed_tools": ["codebase_memory"]
}
```

```json
{
  "recommendation_utilization": 0.25,
  "missed_recommendations": ["context7", "file_search", "websearch"],
  "missed_required": ["context7"],
  "warnings": ["context7 was marked required and was not executed; verify the result carefully."]
}
```

A missed recommendation is a gap in evidence, not proof of failure. The task may have changed
shape halfway through. Treat `missed_required` as a reason to check the answer before handing
it over.

For a fuller report, call `systemone_evaluate_result` with the final answer text and, if the user
gave a verdict, `user_reported_outcome`. Task success stays `unknown` unless someone states
it. Tool-call counts are not treated as evidence of success.

The server remembers `task_id` in memory, so `recommended_tools` is optional within the same
process. After a restart, pass the list explicitly.

## Skill routing

Call `systemone_recommend_skills` when the task looks like authoring, review, research, or a
specialised workflow. The server indexes `SKILL.md` frontmatter from the same directories
OpenCode reads, and returns names with paths.

Real response for a paper-writing request, four of 119 indexed skills:

```json
{
  "decision_source": "model",
  "considered_count": 119,
  "recommendations": [
    { "skill_name": "academic-paper", "score": 0.97, "priority": "required" },
    { "skill_name": "deep-research", "score": 0.96, "priority": "required" },
    { "skill_name": "ml-paper-writing", "score": 0.96, "priority": "required" },
    { "skill_name": "academic-pipeline", "score": 0.86, "priority": "recommended" }
  ]
}
```

Load a recommended skill with OpenCode's native `skill` tool. This server never loads skill
bodies and never runs anything a skill mentions.

## Reading a decision

| Field | Meaning |
|---|---|
| `score` | The model's noul value, clamped to 0..1. A model signal, not a probability. |
| `priority` | `required` at or above `required_at`, `recommended` at or above the threshold, `optional` inside the margin below it |
| `threshold` | The number the score was compared against |
| `threshold_source` | Whether that number came from the tool, the category, or the global default |
| `availability` | `available`, `builtin`, `disabled`, `unavailable`, or `unverified` |
| `decision_source` | `model` or `rule_based_fallback` |
| `explanation_source` | Always `policy_template`: reasons are generated from the score, not written by the model |

A score of 0.94 does not mean the tool is necessary 94 percent of the time. The `required`
label comes from a policy cutoff. If a tool it marked `required` turns out to be unhelpful,
raise `required_at` or the per-category threshold in your settings file.

Availability follows this order: an MCP server listed and enabled counts as `available`, a
server you passed in `available_mcp_servers` overrides the config either way, and built-in
tools stay `builtin`. A tool that is `unavailable` or `disabled` is never recommended.

## Tool reference

| Tool | Use it when |
|---|---|
| `systemone_decide_tools` | A task spans several domains or needs current information |
| `systemone_recommend_skills` | The task resembles a workflow you may already have a skill for |
| `systemone_analyze_task` | You want the requirement breakdown without tool scoring |
| `systemone_check_tool_need` | One tool, one decision |
| `systemone_audit_execution` | After the work, to compare plan against execution |
| `systemone_evaluate_result` | After the work, for metrics plus stated limitations |
| `systemone_get_catalog` | You need to see what is installed and why a tool was skipped |
| `systemone_refresh_catalog` | You changed OpenCode config or added skills mid-session |

`systemone_get_catalog` with `{"type": "tools", "availability": "disabled"}` answers the most
common question during setup: why did nothing get recommended.

## Troubleshooting

Every tool shows `disabled`. The config on disk sets `enabled: false` and the servers are
enabled per agent. Pass `context.available_mcp_servers` with the servers the session actually
has. Observed in practice: a config listing 2 of 17 servers as enabled while the running
session had all 17. The server warns about this when more than 70 percent of the catalog
resolves as disabled.

Every tool shows `unverified`. No OpenCode config was found from the server's working
directory. Set `cwd` in the MCP entry, or pass the server list explicitly.

Nothing is ever recommended. The capability classifier found no requirement. Check
`capabilities.scores` in the response. If a requirement you expected scored below 0.5, lower
`capability_gate` in your settings file.

`decision_source` says `rule_based_fallback`. A required value is missing or the model call failed. The
`warnings` array names the cause. Run `npm run doctor`.

Skills are missing from the index. `SKILL.md` must be capitalised, must sit in
`<root>/<name>/`, and the frontmatter `name` must equal the directory name.

Requests time out. Raise `SYSTEMONE_TIMEOUT_MS` or lower `SYSTEMONE_MAX_QUESTIONS` to shrink the second
stage.

## Platform support

| Platform | Status |
|---|---|
| macOS (arm64, Node 24) | Verified: full suite, live model, benchmark |
| Linux (Debian bookworm, Node 24, container) | Verified: full suite including the stdio integration test |
| Windows via WSL2 | Expected to work. It is the verified Linux path, with the config locations OpenCode documents. |
| Native Windows | Untested. Guards are in place, but no Windows machine was available. |

For native Windows: it reads `%USERPROFILE%\.config\opencode` first and also checks
`%APPDATA%\opencode` and `%LOCALAPPDATA%\opencode`. Config files starting with a UTF-8 BOM are
handled, since Notepad and `Out-File` add one. CRLF endings in config and in `SKILL.md`
frontmatter are handled. OpenCode's own docs recommend WSL, so use WSL unless you have a
reason not to.

## Security

The key stays in memory and appears in no log, record, or error message. Logs go to stderr
with redaction and stdout carries only MCP frames. Inputs are validated and length capped.
Skill and config reads are confined to configured roots with 256 KB and 512 KB limits. Nothing
discovered from a catalog or a skill is executed, and nothing writes to OpenCode
configuration.

## Benchmark

Nineteen tasks, three strategies, ground truth declared per case. The full result files are
committed under [`benchmark-output/`](benchmark-output/), so the numbers below can be checked
against the raw data rather than taken on trust.

Run provenance:

| Field | Value |
|---|---|
| Generated | 2026-11-03T12:33:00Z |
| Endpoint | configured, value not recorded |
| Model | configured, value not recorded |
| Runtime | Node 24.11.1, macOS arm64 |
| Rows | 19 cases x 3 strategies = 57 |
| Report files | [`benchmark.json`](benchmark-output/benchmark.json), [`benchmark.csv`](benchmark-output/benchmark.csv), [`benchmark.md`](benchmark-output/benchmark.md) |

Reproduce it:

```bash
npm run benchmark
```

### Summary

| Strategy | Evaluated | Precision | Recall | F1 | Exact match | Unnecessary rate | Mean latency | Input tokens | Output tokens | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|
| rule_based | 19/19 | 0.792 | 0.983 | 0.829 | 0.579 | 0.105 | 1 ms | 0 | 0 | 0 |
| model | 19/19 | 0.814 | 1.000 | 0.871 | 0.474 | 0.075 | 2065 ms | 11604 | 1970 | 0.0005 |
| adaptive | 19/19 | 0.796 | 1.000 | 0.845 | 0.474 | 0.092 | 1815 ms | 11604 | 1970 | 0.0005 |

### Per-case results, model strategy

| Case | Model recommendation | F1 |
|---|---|---|
| `core-01-general-knowledge` | (none) | 1.00 |
| `core-02-current-price` | websearch | 1.00 |
| `core-03-csv-stats` | python, file_search | 1.00 |
| `core-04-docs-url` | context7, websearch, web_fetch | 0.50 |
| `core-05-database` | database, python | 0.67 |
| `core-06-academic` | semantic_scholar, websearch | 0.67 |
| `core-07-pdf-csv` | python, pdf_processing, file_search | 1.00 |
| `core-08-price-compare` | websearch | 1.00 |
| `core-09-dataset-trends` | websearch, python, file_search | 1.00 |
| `core-10-anomaly` | database | 1.00 |
| `edge-01-ambiguous` | (none) | 1.00 |
| `edge-02-overlap` | context7, codebase_memory, file_search, websearch | 0.67 |
| `edge-03-unavailable` | python | 1.00 |
| `edge-04-disabled` | browser, web_fetch, websearch | 0.50 |
| `edge-05-no-tools` | (none) | 1.00 |
| `edge-06-relevant-not-required` | context7 | 1.00 |
| `edge-07-many-tools` | semantic_scholar, context7, websearch, codebase_memory, python | 0.89 |
| `edge-08-no-repo-tools` | file_search | 1.00 |
| `edge-09-incomplete-catalog` | websearch, context7 | 0.67 |

The CSV holds all 57 rows if you want the rule-based and adaptive results per case.

### What the numbers mean, and what they do not

Precision counts a recommendation as correct only when the case listed it as required. That
is why `core-04` scores 0.50: it found `web_fetch` plus two defensible extras. Recall of 1.000
means no required tool was missed in any case.

Exact match is the strict metric and it sits at 0.474. The router errs by adding a plausible
tool, not by skipping a necessary one.

`edge-04-disabled` is a genuine miss. Asked to summarise a Notion page with Notion
unavailable, it recommended browser tools. The case is left visible rather than removed.

Task success is absent on purpose. Measuring it needs real executions and real user verdicts,
and inventing it would make the rest of the table worthless.

Without a configured endpoint, model id, and key, the two model strategies are recorded as skipped, not scored.
Analysis, weak cases, and the three ground-truth revisions are in
[`docs/BENCHMARK.md`](docs/BENCHMARK.md).

## Resource profile

Routing accuracy and machine cost are separate questions, measured separately. The routing
benchmark answers "did it pick the right tools". This answers "what does the process cost".

```bash
npm run profile
```

The model is disabled for this run. Two sequential API calls per decision would make every
number a measurement of the network. What remains is the cost this server adds on its own:
catalog loading, skill indexing, capability gating, ranking, and record writing.

Latest run on an 8-core arm64 machine, Node 24.11.1:

| Measurement | Value |
|---|---|
| Total startup (catalog, skills, config, discovery, service) | 126 ms |
| DecisionService.create | 50 ms |
| Tool catalog load | 3 ms, 19 entries |
| Skill index build | 69 ms, 119 skills |
| OpenCode config discovery | 1.5 ms, 2 files |
| Rule-based decision, p50 | 0.05 ms |
| Rule-based decision, p95 | 0.13 ms |
| Durability | 16,920 decisions per second |
| CPU per decision | 0.13 ms (user + system) |
| RSS after startup | 93 MB |
| RSS at end of run | 109 MB |
| Peak RSS | 109 MB |
| Heap growth over 200 decisions | 0.16 MB |

Two things in that table need reading carefully.

Startup is dominated by the skill index, not the tool catalog. That is the cost of reading
frontmatter from 119 directories, and it is paid once per process.

RSS rises 16 MB while heap stays flat. That is V8 growing its heap and code cache as the
first decisions run, not a leak. The leak window measures heap used after a forced GC at
iteration 50 and again at 250: 0.16 MB total, which is noise.

Raw data is in [`benchmark-output/resource-profile.json`](benchmark-output/resource-profile.json),
with the same values in CSV and Markdown. Run it yourself before trusting the MB figures:
resident memory depends on the platform allocator and on how many skills you have installed.

```bash
node --expose-gc dist/scripts/profile.js --iterations 200 --leak 1000
```

Without `--expose-gc` the heap figures are noisy, and the report says so in its notes.

## Limitations

- Advisory only. No dynamic tool filtering and no automatic execution capture. Both need
  OpenCode plugin hooks that do not exist yet.
- Two sequential model calls behind each decision, measured at 1.2 to 2.3 seconds per
  decision across runs.
- Tool metadata is partly hand-written, because OpenCode config exposes server enablement and
  nothing about individual tools.
- The adaptive strategy did not beat the model strategy on the current dataset.
- Audit state is per process.

## Commands

```bash
npm install
npm run build
npm test          # unit, stdio integration, and a live model call when configured
npm run benchmark
npm run profile   # local CPU and memory cost, model disabled
npm run doctor
npm run typecheck # src + tests, no emit
npm run lint      # ESLint with typescript-eslint recommended rules
```

## Documentation

| File | Contents |
|---|---|
| [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) | Decision pipeline, availability model, what is not implemented |
| [`docs/CONFIGURATION.md`](docs/CONFIGURATION.md) | Every environment variable, catalog schema, skill roots |
| [`docs/BENCHMARK.md`](docs/BENCHMARK.md) | Metrics, results, weak cases, how to recalibrate |
| [`examples/AGENTS.md`](examples/AGENTS.md) | Agent instructions to paste into your `AGENTS.md` |
| [`examples/opencode.json`](examples/opencode.json) | MCP entry to merge into your config |

## License

MIT. See [`LICENSE`](LICENSE).
