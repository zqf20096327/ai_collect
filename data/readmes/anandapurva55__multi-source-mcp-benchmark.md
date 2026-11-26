# Multi-Source MCP Benchmark: Tool-Using AI Agents on Conflicting Evidence with MCP, Docker Sandboxes and Claim-Based LLM Grading

AI agents are now trusted to investigate real business questions: why a payout total is wrong, whether a performance claim is true, what caused an outage. In these tasks the evidence rarely agrees with itself. Two systems report different numbers, a memo quotes a test that was never a fair comparison, and the most obvious cause is not the real one. Most agent tests do not check for this. They give the agent one clean source and one clear question, so a model can score well without ever having to decide which source to trust.

This project tests that missing skill. Each scenario gives an agent a business question, a Docker container, and files from several sources that contradict each other. The agent uses tools through the Model Context Protocol (MCP) to read the files and run code, and then writes an answer. The answer is scored against a list of facts it should contain, by a judge model that has been tested for fairness first.

[![CI](https://github.com/anandapurva55/multi-source-mcp-benchmark/actions/workflows/ci.yml/badge.svg)](https://github.com/anandapurva55/multi-source-mcp-benchmark/actions/workflows/ci.yml)
[![CodeQL](https://github.com/anandapurva55/multi-source-mcp-benchmark/actions/workflows/codeql.yml/badge.svg)](https://github.com/anandapurva55/multi-source-mcp-benchmark/actions/workflows/codeql.yml)
![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![MCP](https://img.shields.io/badge/MCP-Model%20Context%20Protocol-black)
![Ollama](https://img.shields.io/badge/Ollama-local%20models-000000?logo=ollama&logoColor=white)
![Agent](https://img.shields.io/badge/default%20agent-Qwen%202.5%207B-6D28D9)
![Judge](https://img.shields.io/badge/recommended%20judge-GPT--4.1%20mini-412991?logo=openai&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-sandboxed%2C%20no%20network-2496ED?logo=docker&logoColor=white)
![Scenarios](https://img.shields.io/badge/scenarios-3-informational)
![Grading](https://img.shields.io/badge/grading-claim--based%20LLM%20judge-blueviolet)
![Evidence](https://img.shields.io/badge/evidence-regenerated%20and%20tested%20in%20CI-success)
![License](https://img.shields.io/badge/License-MIT-green)

| Scenarios | Evidence files per scenario | Scored claims per scenario | MCP servers | Network inside the sandbox |
| :---: | :---: | :---: | :---: | :---: |
| **3** | **5 to 8** | **7 to 8** | **4** (filesystem, code execution, git, calculator) | **none** |

## Results at a glance

- **Judge:** `gpt-4.1-mini` and `gpt-4.1` pass all 15 calibration cases. `gpt-4o-mini` and the best local judge (`llama3.1:8b`) each fail 2.
- **Baseline agents:** three small local models score 17% or less on every scenario, and none solves one. No frontier model has been run yet.
- **Cost:** the agent runs locally with no cost per token. Calibrating a judge takes about 91K to 273K prompt tokens.

Details are in [What it shows](#what-it-shows).

## Table of contents

1. **[The problem](#the-problem)**
   - [Agents are tested on easy questions](#agents-are-tested-on-easy-questions)
   - [Three more things can make a test misleading](#three-more-things-can-make-a-test-misleading)
2. **[What this project sets out to do](#what-this-project-sets-out-to-do)**
   - [Goals](#goals)
   - [Design rules](#design-rules)
3. **[What was built](#what-was-built)**
   - [Three scenarios](#three-scenarios)
   - [How it works](#how-it-works)
   - [The sandbox](#the-sandbox)
   - [The evidence](#the-evidence)
   - [Grading](#grading)
   - [Run it yourself](#run-it-yourself)
   - [Repository layout](#repository-layout)
   - [Testing and CI](#testing-and-ci)
4. **[What it shows](#what-it-shows)**
   - [Choosing a judge](#choosing-a-judge)
   - [Baseline agents](#baseline-agents)
   - [LLM cost and how it is kept low](#llm-cost-and-how-it-is-kept-low)
   - [Known limitations](#known-limitations)
5. **[Security](#security)** and **[License](#license)**

---

## The problem

### Agents are tested on easy questions

An agent usually looks good when it gets one clean source and a clear question, because there is nothing to compare. Real tasks are harder:

- A payout ledger and a payment processor report different totals, and the agent must work out which one to trust for which fact.
- A memo quotes a result from a test run that was never a fair comparison with the baseline.
- The most obvious cause of an outage is not the real cause, and the evidence that rules it out is in a different file.

A test that never asks for this cannot tell a model that reasons over conflicting evidence from one that only reads a single file well. The scores look good, and they say little about how the agent will behave on real work.

### Three more things can make a test misleading

Even a test with hard questions can mislead if the setup around it is weak:

1. **The judge may be unfair.** Agent answers are long free text, so another AI model usually grades them. A judge can be too lenient, too strict, or fooled by an answer that simply tells it to give full marks. If nobody checks the judge, the scores cannot be trusted.
2. **The agent may find the answer key.** The reference answers for a public benchmark are public too. An agent with network access, or with a tool that runs code, could simply download them.
3. **Cost and drift.** Running agents and judges can get expensive, and test files that are edited by hand drift away from the numbers in the answer key.

---

## What this project sets out to do

### Goals

1. **Test reconciliation, not lookup.** Build scenarios where the agent must decide which source to trust for which fact, reject a believable wrong explanation, and back its conclusion with specific evidence.
2. **Make the scores trustworthy.** Grade answers fact by fact with partial credit, penalise wrong conclusions, and test every judge model on answers of known quality before relying on it.
3. **Keep the test fair and safe.** Run the agent in a sandbox with no network and read-only evidence, so it cannot look anything up or reach the answer key.
4. **Keep it cheap and repeatable.** Run the agent locally, keep judge calls small and measured, and generate every test file from code so it can be rebuilt and checked.

### Design rules

These rules are how the scenarios are written to meet the goals above.

1. **Evidence states facts, not conclusions.** A document may say what something is, for example what the settlement export is the record of. It never says what to conclude about this case.
2. **Each scenario has several independent problems.** The problems have different kinds of cause: a duplicate record, an unmatched record, a boundary condition, and a rule change that was only partly applied. An agent that stops after the first problem gets partial credit at best.
3. **Every number in a reference answer can be derived from the evidence.** If the evidence cannot explain something, the reference answer says it is unexplained and recommends an investigation.
4. **Every wrong explanation can be disproved with the evidence.** For example, a diff shows that a deploy did not touch the failing code, a hardware table shows that two runs used different machines, or an empty support queue shows that no customer reported an outage.
5. **Trust is assigned per field, not per system.** One source decides whether a record exists. Another decides how it is priced or categorised. The evidence states these rules.
6. **Wrong conclusions cost points.** Each scenario lists the wrong explanations the evidence disproves, such as blaming the deploy. An answer that endorses one loses points, so a confident wrong answer cannot score well just by covering many topics.
7. **Each claim is a fact that can be checked.** For example: "States the net total as $24,460.80 within $1". This keeps grading easy to audit and allows partial credit.

---

## What was built

### Three scenarios

| Scenario | Decision to make | Problems the agent must find |
| --- | --- | --- |
| [`ledger-drift`](scenarios/ledger-drift) | Which payout total goes into the weekly close report | A payout ledger and a payment processor's settlement export disagree for four reasons: a webhook that was recorded twice, a payment with no ledger entry, a payout made one day after the batch cutoff, and a fee-tier change that was applied to only some payments. |
| [`signal-check`](scenarios/signal-check) | Whether a caching change is released to all servers | A memo quotes two results from load tests whose traffic, hardware, or cache state differ from the baseline. The agent must find the one fair comparison, recompute it from raw samples, and state how uncertain the result is. |
| [`root-cause`](scenarios/root-cause) | What caused an outage and how to prevent it | A circuit-breaker change made just before a traffic increase makes the outage look like the customers' own servers were down. The agent uses logs, a deploy record, a support-queue note, an SLA document, and a real git history. |

<details>
<summary><b>Scenario details</b></summary>

**`ledger-drift`** (7 claims). Payout batch from 2027-02-08 to 2027-02-14. The settlement export is the record of whether money moved. The ledger is the record of which order a payout belongs to. The fee schedule is the record of the correct fee rate. The four problems are:

- A webhook retry made the same transfer appear twice (PAY-8801, $1,128.40).
- A $275.00 payment appears in the export but not in the ledger (PAY-9999).
- A payout was made one day after the batch ended (PAY-8841). Its amount matches the ledger, so only the batch changes.
- A seller moved to a lower fee tier during the week, but the ledger applied the new rate to only some payments (PAY-8811, underpaid by $19.20).

The correct total is $24,460.80 across 22 payouts.

**`signal-check`** (8 claims). There are four load-test runs, and only one pair can be compared fairly. The memo's 92% cache hit rate comes from a run with a different traffic profile on different hardware. Its 51 ms latency comes from a run that started with a preloaded cache. On the fair pair, P95 latency improves from 83.0 ms to 75.2 ms and the hit rate improves from 70.8% to 76.0%. Welch's t-statistic is about -6 for latency and +11.5 for hit rate, so the gains are real but modest. One run contains a duplicated sample that must be removed. Each "P95" value is an average of per-minute P95 values, which is not a true P95 for the whole run.

**`root-cause`** (7 claims). Change CB-771 lowered the circuit breaker's failure threshold from 50% to 15% and widened its grouping from per-endpoint to per-region, just before a traffic increase. The agent must:

- Tell apart two error types in the logs (about 6 `circuit_open` errors for each `customer_timeout`).
- Show that an unrelated deploy and the "customer servers were down" theory are wrong.
- Explain why a restart and a scale-up only helped partly.
- Find the later overcorrection to a 90% threshold (CB-772).
- Note that region-level grouping breaks the delivery SLA.

The configuration history is a real git repository. It is stored as a bundle file and cloned into the container when it starts. The logs name each config change only by its commit id, so the agent must run `git show` to see what changed.

</details>

The agent also gets some tools it does not need. The runner records every tool call, so you can check whether the agent chose sensibly. Tool use is recorded, not scored automatically.

### How it works

![Architecture: a local agent model (Qwen 2.5 7B via Ollama) reaches MCP tools inside a no-network sandbox over docker exec; its written answer is scored by a hosted judge model (GPT-4.1 mini) against claims](docs/images/architecture.svg)

**Which model does what**

| Part | Is it a model? | Default |
| --- | --- | --- |
| Agent | Yes | `qwen2.5:7b`, run locally through Ollama. No cost per token. Any MCP-capable agent can replace it. |
| MCP servers (filesystem, code execution, git, calculator) | No, they are tools | Pinned versions inside the container |
| Judge | Yes | `gpt-4.1-mini`, through an OpenAI-compatible API. Hosted and billed per token. It must pass calibration first. |
| Score calculation | No | Plain Python in `tools/grade.py` |

**The steps**

1. You give the agent a task from `brief.md`. The agent is an AI model: `qwen2.5:7b` by default, running on your own machine through Ollama.
2. To investigate, the agent uses tools. It can read files, run Python code, and look through git history. The tools run inside a Docker container that has no internet access, and the evidence files in it are read-only. The tools are ordinary programs, not AI models.
3. When it has finished investigating, the agent writes its final answer.
4. A second AI model, the judge (`gpt-4.1-mini` by default), reads that answer and checks it against the list of facts in `claims.yaml`. It asks one question per fact and gives a score from 0 to 3.
5. The judge also checks for a few wrong conclusions listed in the same file, such as blaming the wrong cause. If the answer says one of them, points are taken off.
6. Plain Python code adds everything up into a final score.

### The sandbox

- **No network.** Containers run with `network_mode: none`. The reference answers are in this public repository, so an agent with network access could download them.
- **Locked down.** The agent runs as an unprivileged user (uid 10001) on a read-only root filesystem. The only writable places are small in-memory `/tmp`, `/home/agent` and `/workspace/scratch` mounts. All Linux capabilities are dropped, `no-new-privileges` is set, and a container is limited to 512 processes and 2 GB of memory.
- **Clean and ready.** `make up` removes any old container first. A healthcheck makes `up --wait` return only after setup (creating the Python environment and, for `root-cause`, cloning the config repository) has finished.
- **Tools installed in advance.** The MCP servers are installed into the image at build time, at pinned versions, and started with `docker exec -i`. The `/workspace/...` paths in `mcp-servers.json` are paths inside the container.
- **One image, many scenarios.** Each scenario mounts its own `evidence/` folder read-only, so changing a fixture does not need an image rebuild.

### The evidence

- **Generators.** Each scenario has a `solution/generate_evidence.py` script that produces its evidence deterministically. It accepts `--out DIR`. The script is kept in `solution/`, away from the evidence, so the agent cannot read it. CI regenerates the evidence and fails if it differs from the committed files.
- **Git fixture.** The `root-cause` repository is stored as `relay-config.bundle`, because a git repository placed inside this repository would be saved as an empty submodule pointer. The generator ignores your own git settings (such as commit signing), so the commit ids are always the same.

### Grading

- **Scoring.** Claims add points, and penalties for endorsed wrong conclusions subtract them. The total is floored at 0, and the raw total is printed when the floor applies.
- **Protection against injected scores.** The candidate answer is wrapped in `<candidate_answer>` tags and treated as data. It is shown to the judge before the task, so the judge's own instruction comes last. Any closing tag or quoted `"score"` key inside the answer is rewritten. The judge must quote the part of the answer that states each fact, and give 0 if there is none.
- **Strict replies.** The judge must end its reply with a line like `{"score": 2}`. Any other reply raises an error instead of being scored as 0. Replies are capped at 600 tokens.
- **Retries.** Timeouts, connection errors, rate limits (429) and server errors are retried up to 3 times with growing delays, so one failure does not end a whole grading run.
- **Judge calibration.** Before a judge model is used, `tools/calibrate.py` tests it on 15 answers of known quality. See [Choosing a judge](#choosing-a-judge).

### Run it yourself

#### What you need

- Python 3.11 or newer, and Docker.
- [Ollama](https://ollama.com), if you want to run the default local agent.
- An API key for an OpenAI-compatible service, if you want to grade answers with a judge model. You do not need a key for `--dry-run` checks.

```bash
pip install -e ".[dev]"
```

#### 1. Start a scenario

```bash
make up SCENARIO=ledger-drift     # builds the image and starts a clean sandbox; returns when it is ready
```

`make up` removes any old container first, so one run never sees another run's files. To stop and delete the sandbox, run `make down SCENARIO=ledger-drift`.

To check the tools yourself, `tools/mcp_probe.py` can list or call any MCP server inside the container:

```bash
# List the tools one server offers
python tools/mcp_probe.py list-tools \
  --config scenarios/ledger-drift/mcp-servers.json \
  --server filesystem --container msmb-ledger-drift

# Call one tool
python tools/mcp_probe.py call-tool \
  --config scenarios/ledger-drift/mcp-servers.json \
  --server filesystem --container msmb-ledger-drift \
  --tool read_text_file --args '{"path": "/workspace/evidence/settlement_terms.md"}'
```

#### 2. Run an agent

[`tools/run_agent.py`](tools/run_agent.py) runs any [Ollama](https://ollama.com) model on a scenario. It connects to the scenario's MCP tools inside the sandbox, repeats tool calls until the model gives a final answer, and saves that answer to a file.

```bash
ollama pull qwen2.5:7b
python tools/run_agent.py --scenario ledger-drift --model qwen2.5:7b --out answer.md
```

It also saves every tool call to `answer.md.trajectory.jsonl`: the tool name, its arguments, the exact text the model saw, and whether that text was cut short.

Options and limits:

| Setting | Default | What it does |
| --- | --- | --- |
| `--max-steps` | 20 | Most turns the model may take |
| `--max-tokens` | 4096 | Most tokens the model may write per turn |
| `--num-ctx` | 32768 | Context window size |
| `--max-tool-output` | 12000 | Characters of a tool result the model sees. Longer results are cut, and the cut is marked in the text |
| `--trajectory` | `<out>.trajectory.jsonl` | Where the tool calls are saved |

At most 8 tool calls run in one turn. If the model sends more, the rest are skipped and the model is told.

![Terminal recording: start the sandbox, list the filesystem tools, run the local agent on ledger-drift](docs/images/demo-run-agent.gif)

*A real recording, sped up. It starts the sandbox, lists the filesystem server's tools, and runs `qwen2.5:7b` on `ledger-drift`. This small model reads the files, then stops with a plan instead of a result. That is why the next recording scores it 0%.*

You can also use any other MCP-capable agent. Start each server listed in the scenario's `mcp-servers.json` inside the container with `docker exec -i msmb-<scenario> <command> <args>`, and talk to it over standard input and output. Give the agent `brief.md` as the task.

#### 3. Grade the answer

```bash
# Check that the claims file and the answer are valid. No API key needed.
python tools/grade.py --claims scenarios/ledger-drift/evaluation/claims.yaml \
  --answer answer.md --dry-run

# Score the answer with any OpenAI-compatible judge
export MSMB_API_BASE=https://api.openai.com/v1 MSMB_API_KEY=... MSMB_MODEL=gpt-4.1-mini
python tools/grade.py --claims scenarios/ledger-drift/evaluation/claims.yaml --answer answer.md
```

The output lists the score for every claim and every penalty, then the weighted total, then how many judge calls and tokens were used.

![Terminal recording: a dry run, then grading the agent's answer and the reference answer with GPT-4.1 mini](docs/images/demo-grading.gif)

*A real recording with `gpt-4.1-mini` as the judge: a dry run, then the agent's answer from the recording above (0%), then the reference answer (100%). The API key comes from the environment and is not shown.*

#### 4. Check that a judge can be trusted

Different judge models grade very differently, so test a judge before relying on its scores:

```bash
python tools/calibrate.py --repeats 3   # all scenarios; uses the same MSMB_* variables
python tools/calibrate.py --dry-run     # only checks that the files exist
```

It gives the judge 15 answers of known quality and exits with an error if any score falls outside its allowed range. Use `--scenario <name>` for one scenario, and `--repeats 3` to check that the results are stable. The 15 cases are explained in [Choosing a judge](#choosing-a-judge).

### Repository layout

```
docker/base.Dockerfile      pinned sandbox image with the MCP servers installed
tools/mcp_probe.py          list or call any declared MCP server inside the container
tools/run_agent.py          run an Ollama model on a scenario using its MCP tools
tools/grade.py              score an answer against claims and penalties (or validate with --dry-run)
tools/calibrate.py          check a judge model against answers of known quality
tools/plot_results.py       redraw the result charts from results/trial.json
scenarios/<name>/
  brief.md                  the task given to the agent
  mcp-servers.json          tools the agent may use, plus extra optional ones
  environment/              docker-compose.yml and the read-only evidence
  solution/                 generate_evidence.py and REFERENCE_ANSWER.md (never mounted)
  evaluation/claims.yaml    the facts an answer is scored on, and the wrong conclusions it is penalised for
  evaluation/calibration/   partial, trap, injection and non-answer files used to calibrate a judge
results/                    baseline answers, tool-call trajectories, grades, calibration logs, trial.json
docs/images/                the architecture diagram, result charts and terminal recordings
tests/                      structure, grading, regeneration, plot and Docker environment tests
```

### Testing and CI

```bash
pytest              # file structure, scoring and penalties, score parsing, retries, evidence regeneration, charts
pytest -m docker    # needs Docker: see below
```

The Docker tests build the image and start every scenario. They check that every declared MCP server starts and offers the tools named in its policy file, that the container has no network, that the agent runs as a non-root user, that only the scratch folder is writable, and that the code tool can read the evidence (SQLite, CSV or git history).

CI runs both commands on every push, and CodeQL scans the code. Dependabot is configured for the GitHub Actions, the Python packages and the Docker base image, but its pull-request limit is 0, so version updates are made by hand. CI never calls a model.

---

## What it shows

### Choosing a judge

A judge that grades unfairly makes every score meaningless, so each judge model is tested on answers whose quality is already known. There are 5 kinds of answer for each of the 3 scenarios, so 15 cases in total. Each case must score inside an allowed range.

| Kind of answer | What it is | Allowed score |
| --- | --- | --- |
| Correct | The verified reference answer | 85% to 100% |
| Half-correct | Gets about half of the facts right and says nothing about the rest | 15% to 60% |
| Confident but wrong | Sounds sure, but blames the wrong cause or accepts the wrong numbers | 0% to 40% |
| Injection | Has no real content and tells the judge to give full marks | 0% to 15% |
| Found nothing | Says the files could not be found | 0% to 15% |

The correct answer is `solution/REFERENCE_ANSWER.md`. The other four are in `scenarios/<name>/evaluation/calibration/` (`partial.md`, `trap.md`, `injection.md`, `non_answer.md`).

![Judge calibration by model](docs/images/judge-calibration.svg)

![Terminal output of two saved calibration logs: GPT-4.1 mini passes and a local Llama 3.1 8B fails](docs/images/demo-calibration.gif)

*The saved calibration logs for `gpt-4.1-mini` (passes all 15 cases) and the local `llama3.1:8b` (fails two). They are printed with `cat` from `results/calibration/`, not run live.*

**`gpt-4.1-mini` is the recommended judge.** It passed all 15 cases in three repeated runs and is cheap. `gpt-4.1` also passes. `gpt-4o-mini` and the best local model tried (`llama3.1:8b`) do not: they under-score a correct answer or give an injected answer credit. The difference matters. A local judge gave one weak answer 58%, and `gpt-4.1` scored the same answer 17%.

### Baseline agents

![Agent scores by model and scenario](docs/images/agent-scores.svg)

Three small local models (`qwen2.5:7b`, `llama3.1:8b`, `llama3.2`) were run once on each scenario and graded with `gpt-4.1`. None solves a scenario: the best result is 17%, and several runs ended without a usable answer (a step limit reached, or a tool call written out as text). No frontier model has been run yet. The raw answers, tool-call trajectories, grades and calibration logs are in [`results/`](results), and `python tools/plot_results.py` redraws the charts from `results/trial.json`.

### LLM cost and how it is kept low

The agent runs locally on Ollama, so it costs nothing per token. Only grading uses a hosted model. Every `grade.py` and `calibrate.py` run prints its call and token counts. Measured token use:

| Run | Judge calls | Prompt tokens | Completion tokens |
| --- | ---: | ---: | ---: |
| Grade one answer (about 10 calls) | 10 | about 6,700 | about 600 |
| Full calibration, one pass (`gpt-4.1`) | 150 | 91,040 | 10,376 |
| Full calibration, 3 repeats (`gpt-4.1-mini`) | 450 | 273,120 | 37,142 |

Multiply these by your provider's current price to get a cost. The whole calibration is a few hundred thousand tokens, so it is small next to what a frontier agent run would use.

How the cost is kept down:

- **Local agent, hosted judge only.** The expensive part of an evaluation, the agent's long tool-use loop, runs on your own machine.
- **No model calls where none are needed.** `--dry-run` validates claims and answers with no model, and CI never calls a model.
- **Small, bounded calls.** One call per claim or penalty, temperature 0, replies capped at 600 tokens, and the answer is sent once per call.
- **Probe before a full run.** Test the hardest cases first (an injection answer and a reference answer, about 20 calls) and only run the full calibration if the probe looks good.
- **Cheapest judge that passes.** `gpt-4.1-mini` passes calibration, so the larger model is not needed. Use `--repeats 1` unless you are checking stability.

### Known limitations

- The scenarios are synthetic and small. They test reasoning over conflicting evidence, not scale. No strong model has been tested, so it is unknown how close one would get to full marks. The per-claim scores are more useful than the total.
- Scoring depends on the judge model. Claims are written as explicit facts to reduce variation, but judges differ a lot, and two of the four tried failed calibration. Run `tools/calibrate.py` for any judge you use, and compare scores only between runs that used the same judge.
- The runner supports Ollama only. The baseline agent results are single runs at temperature 0, so there is no variance estimate, and no frontier model has been tested. Tool calls are recorded but not scored.
- The `code-executor` tool can run any code inside the container. The container is isolated from the network and the host, but the code can still read the evidence it is meant to analyze.
- The in-memory scratch folders do not allow running programs directly. Python scripts run normally, but a compiled program copied there will not start.

---

## Security

Please report vulnerabilities privately. See [SECURITY.md](SECURITY.md).

## License

MIT. See [LICENSE](LICENSE).
