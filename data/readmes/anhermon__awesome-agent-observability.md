# Awesome Agent Observability [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Tools, standards, and benchmarks for tracing and evaluating AI products (LLM apps, agents, coding-agent harnesses, Agent Skills, and MCP servers), with evaluations graded by LLM judges or deterministic checks.

For engineers who build or run AI agents and need to see what a run did, what it cost, and whether it was right. It covers OpenTelemetry conventions, tracing platforms, coding-agent telemetry, eval frameworks, agent and harness benchmarks, skill and MCP server testing, and guardrails. Every entry is held to the list's [requirements](CONTRIBUTING.md#requirements): alive, maintained, and at least 8 weeks old, and new entries are run hands-on before they are added; the next paragraph says which older entries could not be run.

Entries say what a project does, not what it markets, and carry its license where that is not plainly open source. Projects that were dormant, end-of-life, out of scope, or too young to judge were left out. Most entries were installed or built and run against a mock backend at the 2026-10-04 audit; a few could not be run (for example Kong, SigNoz, and anything needing Docker or a hosted account), so this list does not claim every entry was exercised. Entries added at the 2026-11-15 evals expansion, and in the follow-up later that day, were each run on a Linux box with local models or mocks only, and the commands and output are in [`evidence/`](evidence/). A weekly job re-checks that each repository still exists, is not archived, and has a recent commit.

## Contents

- [Where to start](#where-to-start)
- [Recipes](#recipes)
- [Standards and instrumentation](#standards-and-instrumentation)
- [Tracing and observability platforms](#tracing-and-observability-platforms)
- [Trace backends](#trace-backends)
- [Coding-agent telemetry](#coding-agent-telemetry)
- [Evaluation and testing](#evaluation-and-testing)
- [Agent and harness benchmarks](#agent-and-harness-benchmarks)
- [Skill evaluation](#skill-evaluation)
- [Guardrails and security](#guardrails-and-security)
- [Gateways and proxies](#gateways-and-proxies)
- [MCP server testing](#mcp-server-testing)
- [Model Context Protocol](#model-context-protocol)
- [Agent frameworks with built-in tracing](#agent-frameworks-with-built-in-tracing)
- [Related lists](#related-lists)

## Where to start

Find what you are evaluating or observing; the entries named are in the sections below.

| You want to                                                | Start with                                                                       |
| ---------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Trace an LLM or agent app you build                        | OpenLLMetry or OpenInference into Langfuse, Phoenix, or a trace backend          |
| See what a coding agent did and what it cost               | Claude Code monitoring, AI Observer, ccusage, ctxlens                            |
| Score outputs with an LLM judge                            | DeepEval, Promptfoo, OpenEvals, Inspect                                          |
| Score outputs deterministically                            | Inspect, Promptfoo, OpenEvals, SWE-bench, Harbor                                 |
| Check an agent's tool-call path                            | AgentEvals, DeepEval                                                             |
| Compare models or coding-agent harnesses on the same tasks | Harbor, Inspect SWE, coder-eval, τ²-bench                                        |
| Evaluate an Agent Skill                                    | skill-creator, coder-eval                                                        |
| Trace MCP tool calls                                       | ToolHive, Agentgateway, MCP Context Forge; TypeScript, Python, C# SDK spans      |
| Test an MCP server                                         | MCP Conformance, MCP Inspector, MCPMark, MCP-Atlas; MCP Scanner for security     |
| Red-team an app or agent                                   | Promptfoo, garak, DeepTeam, PyRIT                                                |
| Trace token use from CLI harnesses                         | LiteLLM into an OpenTelemetry Collector (see Recipes)                            |
| Score a model's function calls                             | BFCL, AgentEvals, DeepEval                                                       |

## Recipes

Short patterns that use tools already on this list. Each was run on a Linux box with local models only; commands and output are in [`evidence/recipes.md`](evidence/recipes.md).

**Trace any CLI harness through a gateway.** Point Claude Code (through `ANTHROPIC_BASE_URL`), OpenCode, Pi, or another CLI that accepts a custom Anthropic- or OpenAI-compatible base URL at a LiteLLM proxy with the `otel` callback writing into an OpenTelemetry Collector. You get spans with per-request input and output token counts, model, latency, and user agent, without harness-specific instrumentation. Claude Code's own monitoring can send to the same collector, but on local models it may report a phantom cost and only session-level metrics.

**Run MCP Conformance through a proxy.** Point MCP Conformance at the proxy or gateway in front of the server, not only at the server itself, so buffering and protocol bugs in the middle layer show up as failures that the direct run does not have.

**Run a harness eval without Docker.** Harbor and Inspect SWE expect container sandboxes. Inspect can also run a task with no sandbox, or with its built-in `local` sandbox (the host file system, no isolation), so a custom solver can shell out to each CLI on the host and score with hidden tests and `model_graded_qa`; the agent then runs with your user's permissions.

**Promptfoo Node version.** Promptfoo 0.122 and later require Node 22.22 or newer (`engines.node`). Node 22.20 fails; use a newer Node if `npx promptfoo` errors on startup.

## Standards and instrumentation

MCP carries W3C trace context in each request's `params._meta` as unprefixed `traceparent`, `tracestate`, and `baggage` keys, per [SEP-414](https://modelcontextprotocol.io/community/seps/414-request-meta) (Final). As of 2026-11-16, the official [TypeScript](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/advanced/opentelemetry.md), [Python](https://github.com/modelcontextprotocol/python-sdk/blob/main/src/mcp/shared/_otel.py), and [C#](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol.Core/Diagnostics.cs) SDKs inject and extract it with OpenTelemetry, the [PHP](https://github.com/modelcontextprotocol/php-sdk/blob/main/src/Schema/RequestMeta.php), [Rust](https://github.com/modelcontextprotocol/rust-sdk/blob/main/crates/rmcp/src/model/meta.rs), and [Ruby](https://github.com/modelcontextprotocol/ruby-sdk/blob/main/lib/mcp/trace_context.rb) SDKs read and pass the keys without emitting spans themselves, and no support was found in the Go or Java SDK source.

- [OpenTelemetry GenAI Semantic Conventions](https://github.com/open-telemetry/semantic-conventions-genai) - Repository that now owns the GenAI spans, metrics, and events, moved out of the main semantic-conventions repo.
- [OpenTelemetry MCP semantic conventions](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/mcp.md) - Client and server span and metric conventions for MCP requests, naming spans after the method and target (such as `tools/call get-weather`) and carrying trace context in `params._meta`; status Development.
- [OpenTelemetry GenAI agent spans](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md) - Span conventions for creating an agent (`create_agent {gen_ai.agent.name}`) and invoking one (`invoke_agent`), with their attributes; status Development.
- [OpenTelemetry Semantic Conventions](https://github.com/open-telemetry/semantic-conventions) - Parent repo for all OTel conventions, including the HTTP, RPC, and database spans an agent stack also emits.
- [OpenTelemetry GenAI Observability SIG](https://github.com/open-telemetry/community/blob/main/projects/gen-ai.md) - Charter and scope of the OTel project group driving GenAI telemetry; the place to track where the conventions are heading.
- [OpenTelemetry Python GenAI instrumentation](https://github.com/open-telemetry/opentelemetry-python-genai) - Upstream instrumentation packages for OpenAI, Anthropic, Google GenAI, LangChain, Bedrock, and several agent frameworks.
- [OpenLLMetry](https://github.com/traceloop/openllmetry) - OpenTelemetry-based auto-instrumentation for Python LLM apps, exporting to any OTel backend.
- [OpenLLMetry-JS](https://github.com/traceloop/openllmetry-js) - The same instrumentation for TypeScript and Node.js applications.
- [OpenInference](https://github.com/Arize-ai/openinference) - OpenTelemetry-compatible tracing spec and instrumentation libraries for Python, JavaScript, Java, and Go from the Arize Phoenix team.
- [OpenLIT](https://github.com/openlit/openlit) - OTel-native auto-instrumentation SDK for LLM, vector-database, and GPU calls, with a self-hosted UI to read the resulting traces.

## Tracing and observability platforms

Last verified 2026-11-16 from each project's docs or repository; the source for every cell is in [`evidence/comparison-table.md`](evidence/comparison-table.md). "Not documented" means the docs checked do not say, not that the feature is missing. OTel GenAI conventions means the platform documents reading `gen_ai.*` span attributes on ingest.

| Platform         | Licence                               | Self-host              | OTLP ingest    | OTel GenAI conventions | Evals built in |
| ---------------- | ------------------------------------- | ---------------------- | -------------- | ---------------------- | -------------- |
| Langfuse         | MIT, open-core (`ee/`)                | Yes                    | Yes            | Yes                    | Yes            |
| Arize Phoenix    | Elastic License 2.0                   | Yes                    | Yes            | Yes                    | Yes            |
| LangSmith        | Closed; MIT SDKs                      | Enterprise add-on      | Yes            | Yes                    | Yes            |
| Opik             | Apache-2.0                            | Yes                    | Yes            | Yes                    | Yes            |
| LangWatch        | Apache-2.0, open-core (`enterprise/`) | Yes                    | Yes            | Not documented         | Yes            |
| Laminar          | Apache-2.0                            | Yes                    | Yes            | Yes                    | Yes            |
| Agenta           | MIT, open-core (`ee/`)                | Yes                    | Yes            | Not documented         | Yes            |
| Pydantic Logfire | Closed; MIT SDK                       | Enterprise plan        | Yes            | Yes                    | Yes            |
| W&B Weave        | Apache-2.0                            | With a W&B licence     | Yes            | Yes                    | Yes            |
| MLflow Tracing   | Apache-2.0                            | Yes                    | Yes            | Yes                    | Yes            |
| Braintrust       | Closed                                | Data plane only (BYOC) | Yes            | Yes                    | Yes            |
| AgentOps         | MIT SDK; app Elastic License 2.0      | Yes                    | Not documented | Not documented         | Not documented |
| Noveum Trace     | Apache-2.0 SDK; hosted backend        | Not documented         | Not documented | Not documented         | Not documented |
| Agnost AI        | Closed; MIT SDKs                      | Not documented         | Yes            | Yes                    | Yes            |

- [Langfuse](https://github.com/langfuse/langfuse) - Self-hostable tracing, prompt management, datasets, and evals; ingests OTel as well as its own SDKs; open-core, MIT outside the `ee/` directories.
- [Arize Phoenix](https://github.com/Arize-ai/phoenix) - Trace viewer and eval workbench that runs locally in a notebook or as a server; source-available under the Elastic License 2.0.
- [LangSmith](https://docs.langchain.com/langsmith/observability) - Hosted tracing and eval product from LangChain; the [Python](https://github.com/langchain-ai/langsmith-python) and [JavaScript](https://github.com/langchain-ai/langsmith-javascript) client SDKs are open source, the backend is not.
- [Opik](https://github.com/comet-ml/opik) - Comet's open-source tracing and evaluation platform for LLM and agent workflows.
- [LangWatch](https://github.com/langwatch/langwatch) - OTel-based platform pairing production monitoring with pre-deploy agent simulation, plus an AI gateway and coding-agent tracking; open-core, Apache-2.0 outside the `enterprise/` directory.
- [Laminar](https://github.com/lmnr-ai/lmnr) - Open-source tracing and eval platform for agent runs, with a Rust backend.
- [Agenta](https://github.com/Agenta-AI/agenta) - Self-hostable open-core workspace for building, versioning, and running agents, with tracing of model and tool calls and evaluation support.
- [Pydantic Logfire](https://github.com/pydantic/logfire) - OTel-based observability with first-class Python, Pydantic, and agent instrumentation; the SDK is open source, the backend is hosted and closed.
- [W&B Weave](https://github.com/wandb/weave) - Weights & Biases toolkit for logging, comparing, and evaluating LLM app versions; [docs](https://docs.coreweave.com/products/wandb/weave).
- [MLflow Tracing](https://mlflow.org/docs/latest/genai/tracing/) - GenAI tracing built into [MLflow](https://github.com/mlflow/mlflow), so agent traces sit next to model runs and registries.
- [Braintrust](https://docs.braintrust.dev/instrument) - Hosted eval and tracing platform; see [Autoevals](https://github.com/braintrustdata/autoevals) below for its open-source scorers.
- [AgentOps](https://github.com/AgentOps-AI/agentops) - Python SDK for session replay, cost tracking, and tracing across CrewAI, OpenAI Agents SDK, LangChain, AG2, and others; the SDK is MIT, the self-hostable app is Elastic License 2.0.
- [Noveum Trace](https://github.com/Noveum/noveum-trace) - Python SDK whose context managers trace operations, LLM calls, and agent steps and send them over HTTPS to the hosted Noveum platform or a custom endpoint; the SDK is Apache-2.0, the backend is hosted.
- [Agnost AI](https://docs.agnost.ai/online-evals) - Hosted platform that has an LLM judge each finished agent conversation against plain-English rules, labels user intent, and sends Slack or email alerts that can open a fix pull request; ingests OpenTelemetry, the Python and TypeScript conversation SDKs are MIT, the backend is hosted and closed source.

## Trace backends

General-purpose OpenTelemetry backends that GenAI spans can be sent to when you do not want an LLM-specific product.

- [OpenTelemetry Collector](https://github.com/open-telemetry/opentelemetry-collector) - Vendor-neutral pipeline to receive, process, filter, and fan out traces before they reach a backend.
- [SigNoz](https://github.com/SigNoz/signoz) - OTel-native, self-hostable traces, metrics, and logs in one UI; open-core, MIT outside the `ee/` and `cmd/enterprise/` directories.
- [Jaeger](https://github.com/jaegertracing/jaeger) - CNCF distributed tracing backend that stores spans and serves trace search and a waterfall UI over them.
- [Grafana Tempo](https://github.com/grafana/tempo) - High-volume trace store backed by object storage, queried from Grafana; AGPL-3.0.

## Coding-agent telemetry

Telemetry, usage, and cost analysis for CLI coding agents such as Claude Code, Codex CLI, Gemini CLI, and OpenCode, whether you use them day to day or are evaluating them.

- [Claude Code monitoring](https://code.claude.com/docs/en/monitoring-usage) - Claude Code's built-in OpenTelemetry export, turned on with `CLAUDE_CODE_ENABLE_TELEMETRY=1` and an OTLP exporter setting, which sends session, token, and estimated-cost metrics and prompt, API-request, and tool-result events to any OTLP endpoint, plus per-prompt traces when the beta `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1` is also set, with prompt and tool content redacted unless you opt in; Claude Code itself is proprietary.
- [AI Observer](https://github.com/tobilg/ai-observer) - Single-binary OTLP receiver with a DuckDB store and web dashboard for Claude Code, Codex CLI, Gemini CLI, Copilot, and OpenCode telemetry, which can also import past session files and price their token use; MIT.
- [AgentsView](https://github.com/kenn-io/agentsview) - Local-first session search, analytics, and token-use statistics for the Claude Code, Codex, and other coding-agent session archives on your machine; it analyses the agents you use, not apps you build.
- [ccusage](https://github.com/ccusage/ccusage) - CLI that reads the local session logs of Claude Code, Codex, OpenCode, and other coding-agent CLIs and reports token use and estimated cost by day, week, month, or session, and for Claude Code by 5-hour billing block; MIT.
- [ctxlens](https://github.com/AgentPostmortem/Ctxlens) - Parses Claude Code, Codex, and generic OpenAI-chat session transcripts and reports per-turn context composition, a waste ratio from duplicate content, oversized tool results, stale outputs, and oversized tool definitions, and recommendations, with a CI flag that fails when waste exceeds a threshold; MIT.
- [Verovo](https://github.com/roy-tong/Verovo) - Local CLI, formerly AgentMeasure, whose `check` command reads Codex and Claude Code session logs and reports duplicate records, retry chains, and repeated tool failures, marking what the logs cannot decide as UNPROVABLE; most of its other commands audit AI vendor bills against usage records; MIT.

## Evaluation and testing

- [Ragas](https://github.com/vibrantlabsai/ragas) - Metrics and test-set generation for RAG and agent pipelines.
- [DeepEval](https://github.com/confident-ai/deepeval) - Pytest-style eval framework with G-Eval, hallucination, and relevancy metrics, a tool-correctness metric that compares an agent's tool calls with the expected ones, and MCP metrics that judge whether an agent used an MCP server's tools to complete a task.
- [Promptfoo](https://github.com/promptfoo/promptfoo) - Declarative CLI that runs test cases against prompts, models, and agent providers, including the Claude Agent SDK and OpenAI Codex SDK, and grades them with deterministic and model-graded assertions, plus LLM red-teaming and vulnerability scanning in CI; MIT, now part of OpenAI.
- [TruLens](https://github.com/truera/trulens) - Instrumentation plus feedback functions that score app internals, not just final output.
- [Evidently](https://github.com/evidentlyai/evidently) - Python framework for evals, drift detection, and monitoring across tabular, text, and GenAI systems.
- [Inspect](https://github.com/UKGovernmentBEIS/inspect_ai) - UK AI Security Institute's eval framework for agentic tasks, tool use, and sandboxed execution, with exact, pattern, and model-graded scorers; CLI coding agents run in it through [Inspect SWE](#agent-and-harness-benchmarks).
- [Inspect Scout](https://github.com/meridianlabs-ai/inspect_scout) - Scans agent transcripts from Inspect eval logs and other sources with LLM, grep, or custom scanners and writes queryable results, for finding failure patterns across runs; MIT.
- [Giskard](https://github.com/Giskard-AI/giskard-oss) - Checks and red-team scans for LLM agents: multi-turn scenarios, LLM-judge checks, and probes for prompt injection and harmful content (v3; v2 is unmaintained).
- [Scenario](https://github.com/langwatch/scenario) - Simulates multi-turn users against an agent so conversations, not single calls, can be asserted on.
- [Autoevals](https://github.com/braintrustdata/autoevals) - Standalone library of model-graded and heuristic scorers usable outside Braintrust.
- [OpenEvals](https://github.com/langchain-ai/openevals) - Readymade evaluators for LLM apps: LLM-as-judge prompts, exact and string-distance matchers, and structured-output checks, as functions that return scored results and plug into pytest or LangSmith, in Python and TypeScript.
- [AgentEvals](https://github.com/langchain-ai/agentevals) - Evaluators that score an agent's tool-call trajectory against a reference with strict, unordered, subset, or superset matching, or with an LLM judge; MIT.
- [BFCL](https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard) - Evaluates a model's function calling on single-turn, live, multi-turn, and agentic web-search and memory tasks, checking single-turn calls by AST match and running multi-turn and agentic calls against the benchmark's API backends; Apache-2.0, part of the Gorilla repository.
- [HermesGate](https://github.com/roli-lpci/hermes-gate) - Runs a repository's own checks and stores a receipt keyed to the content and tool versions checked; in `fast` and `review` modes an identical receipt is reused as a PASS and any change re-runs the checks, giving an agent's own PR a repeatable pre-review result.
- [NovaFabric](https://github.com/MSKazemi/novafabric) - Self-hosted CLI whose `nova capture` wraps any command, such as an agent script, and records the run as a portable Run Capsule that you can replay and structurally diff against another run; Apache-2.0, pre-1.0.
- [LEEVAR Battery](https://github.com/forevercrab321-svg/leevar-battery) - Grades agent conversation transcripts on 18 tests across six dimensions with a judge model you configure, reports tests the transcript cannot evidence as NOT TESTED and leaves them out of the score, and issues no letter grade when two thirds or fewer of the tests have evidence; MIT, and the same authors run an optional hosted scan.
- [Agent-Causality](https://github.com/Psionic-labs/Agent-Causality) - Records LangGraph and OpenCode agent runs as event graphs with declared causal parents, so a failing event can be sliced to the earlier events it structurally depends on and agent state rebuilt at any event with a SHA-256 state hash, and decisions recorded through its Python SDK can be replayed with changed inputs to test which ones flip the outcome; AGPL-3.0.

## Agent and harness benchmarks

Harnesses that run an agent, or a whole CLI coding agent, on tasks in a sandbox and grade the outcome, usually with tests the agent cannot see; use them to compare models, harnesses, and configurations on the same tasks.

- [Harbor](https://github.com/harbor-framework/harbor) - Runs agents, including Claude Code, Codex CLI, Gemini CLI, OpenCode, and Cursor CLI, on containerized tasks and scores each trial with the task's own test script, so harnesses and models can be compared on the same tasks, with Terminal-Bench and other datasets in its registry; Apache-2.0.
- [τ²-bench](https://github.com/sierra-research/tau2-bench) - Runs a tool-using customer-service agent against an LLM-simulated user, who also has tools in some domains such as telecom, through tasks in airline, retail, telecom, and other domains, and by default scores each trial by whether the database ends in the gold state and whether required information was communicated, in text or voice; MIT.
- [Inspect SWE](https://github.com/meridianlabs-ai/inspect_swe) - Wraps Claude Code, Codex CLI, Gemini CLI, OpenCode, and other CLI coding agents as Inspect agents that run in an Inspect sandbox with their model calls routed through Inspect, so any Inspect model, scorer, and log viewer applies to them; MIT.
- [coder-eval](https://github.com/UiPath/coder_eval) - Runs Claude Code, Codex, OpenCode, and other CLI coding agents on YAML tasks in a sandbox and grades the workspace and trajectory with deterministic checks such as file contents, commands, and whether a given skill was loaded, or with LLM judges, including A/B runs across agents, models, and skills; Apache-2.0.
- [SWE-bench](https://github.com/SWE-bench/SWE-bench) - Harness that applies a candidate patch to a real GitHub repository inside a per-issue Docker image and runs the repository's held-out FAIL_TO_PASS and PASS_TO_PASS tests to decide whether the issue is resolved; MIT.
- [Inspect Evals](https://github.com/UKGovernmentBEIS/inspect_evals) - Ready-made Inspect tasks for published benchmarks, from GSM8K to agentic and cybersecurity suites, run against any Inspect-supported model with one `inspect eval` command; MIT.
- [YYLO Benchmark](https://github.com/yylo-dev/yylo-benchmark) - Runs coding prompts and tasks across models and harnesses on fresh checkouts, keeps every output unchanged, and lets you re-evaluate them later with new checks or judges.
- [AgentDojo](https://github.com/ethz-spylab/agentdojo) - ETH Zurich benchmark and framework for tool-using agents against prompt injection, with task suites and attack and defense pipelines that report utility and attack success.
- [ClawBench](https://github.com/TIGER-AI-Lab/ClawBench) - Live-web benchmark for evaluating browser and computer-use agents on about 280 everyday tasks, with request interception and recorded execution evidence.

## Skill evaluation

Tools that check whether an Agent Skill is loaded when it should be and whether it improves results over running without it. coder-eval, listed under Agent and harness benchmarks, also checks whether a given skill was loaded and runs A/B comparisons with and without skills.

- [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) - Anthropic's skill for building Agent Skills, whose scripts run `claude -p` on should-trigger and should-not-trigger queries to measure how often a skill's description makes Claude load it, and aggregate with-skill and baseline runs into pass-rate, time, and token deltas; Apache-2.0 per the skill's LICENSE.txt.

## Guardrails and security

- [Guardrails AI](https://github.com/guardrails-ai/guardrails) - Runs input/output validators around a model call and enforces structured output.
- [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) - NVIDIA toolkit for input, output, dialogue, and tool rails defined in Colang and Python.
- [OpenAI Guardrails](https://github.com/openai/openai-guardrails-python) - Drop-in OpenAI client wrapper that runs configurable input and output checks (keywords, secret keys, PII, URLs, moderation, jailbreak and prompt-injection detection) and raises on a tripwire; preview release.
- [garak](https://github.com/NVIDIA/garak) - LLM vulnerability scanner probing for jailbreaks, prompt injection, and data leakage.
- [PyRIT](https://github.com/microsoft/PyRIT) - Microsoft AI Red Team's toolkit that sends single-turn or adaptive multi-turn attacks, optionally transformed by converters such as Base64, to a model, an HTTP endpoint, or a browser-driven app, and scores the responses with deterministic or LLM-judge scorers, from Python, a CLI scanner, or a web GUI; MIT.
- [DeepTeam](https://github.com/confident-ai/deepteam) - Red-teaming framework that simulates jailbreaks, prompt injection, and related attacks against LLM and agent apps, built on DeepEval.
- [PurpleLlama](https://github.com/meta-llama/PurpleLlama) - Meta's safety repository: Llama Guard and Prompt Guard classifier models, LlamaFirewall, which runs Prompt Guard, alignment-check, regex, and CodeShield scanners over agent inputs and outputs and returns allow, block, or human review, CodeShield's Semgrep and regex rules for insecure generated code, and the CyberSecEval benchmarks; code is MIT, the models use Llama community licenses.
- [Presidio](https://github.com/data-privacy-stack/presidio) - PII detection, redaction, and anonymisation for text and images; useful for scrubbing traces before export.
- [Snyk agent-scan](https://github.com/snyk/agent-scan) - Security scanner for MCP servers, agents, and skills, formerly Invariant Labs' `mcp-scan`; `inspect` lists what a config exposes locally, while `scan` needs a Snyk token and calls Snyk's hosted API.
- [MCP Scanner](https://github.com/cisco-ai-defense/mcp-scanner) - Scans MCP servers' tools, prompts, resources, and instructions for poisoning and exfiltration patterns using YARA rules, optional LLM and behavioural analyzers, and a Cisco API analyzer; Apache-2.0.

## Gateways and proxies

- [LiteLLM](https://github.com/BerriAI/litellm) - SDK and proxy exposing 100+ providers behind the OpenAI API, with cost tracking, logging, and callbacks to most platforms above; open-core, MIT outside the `enterprise/` directory.
- [Portkey AI Gateway](https://github.com/Portkey-AI/gateway) - Routing gateway with retries, fallbacks, caching, and inline guardrails.
- [Bifrost](https://github.com/maximhq/bifrost) - Go gateway that fronts multiple LLM providers behind one OpenAI-compatible API, with key load balancing, fallbacks, and Prometheus and OpenTelemetry telemetry; guardrails are enterprise-only.
- [Agentgateway](https://github.com/agentgateway/agentgateway) - Linux Foundation proxy for agent-to-LLM, agent-to-MCP, and agent-to-agent (A2A) traffic with routing, guardrails, and RBAC, which, with tracing configured, exports an OTLP span per upstream MCP call carrying `mcp.method.name` and `gen_ai.tool.name`, plus per-tool call counters as Prometheus metrics.
- [Traceloop Hub](https://github.com/traceloop/hub) - Small Rust LLM gateway from the OpenLLMetry authors, with OTel emission built in.
- [Kong](https://github.com/Kong/kong) - API gateway whose AI plugins add LLM routing, token metrics, and request logging to an existing gateway deployment.
- [Recued](https://github.com/recued/recued) - Self-hosted MCP gateway between AI agents and the owner's mail, calendar, files and CRM that checks each tool call against a per-agent contract and holds writes for the owner's approval by default, and documents no OpenTelemetry export; AGPL-3.0.

## MCP server testing

Tools that check what an MCP server does: protocol conformance, manual calls, and agent task benchmarks over real servers. Security scanners are under Guardrails and security.

- [MCP Conformance](https://github.com/modelcontextprotocol/conformance) - Official test suite that connects to a running MCP server, or drives an MCP client, and checks its tools, resources, prompts, elicitation, transport, and wire messages against a spec version, reporting pass or fail per scenario; pre-1.0, Apache-2.0, with some contributions still MIT.
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector) - Official UI for calling an MCP server's tools by hand and reading the raw JSON-RPC traffic.
- [MCPMark](https://github.com/eval-sys/mcpmark) - Benchmark of tasks over real Filesystem, GitHub, Notion, PostgreSQL, and Playwright MCP servers, each run from a fresh copy of its environment and checked by a per-task verification script, with models called through LiteLLM; Apache-2.0.
- [MCP-Universe](https://github.com/SalesforceAIResearch/MCP-Universe) - Salesforce framework and benchmark that runs agents against real MCP servers for maps, finance, GitHub, browser, and other tasks and grades their outputs with rule-based evaluators; Apache-2.0.
- [MCP-Atlas](https://github.com/scaleapi/mcp-atlas) - Runs an agent against 36 real MCP servers (20 without API keys) in a Docker sandbox on 500 public tasks and scores the final answer with an LLM judge on claim coverage, plus a diagnostic taxonomy of tool-call and cognitive failures; MIT.

## Model Context Protocol

- [Model Context Protocol](https://github.com/modelcontextprotocol/modelcontextprotocol) - The specification itself; the source of truth for what a compliant client, server, and transport must do.
- [MCP Registry](https://github.com/modelcontextprotocol/registry) - Official, community-owned registry service for publishing and discovering MCP servers; still in preview.
- [ToolHive](https://github.com/stacklok/toolhive) - Runs MCP servers in containers with permission policies, secrets handling, and audit logging, and its proxy exports OpenTelemetry traces and metrics for each MCP request with MCP semantic-convention attributes such as `mcp.method.name`.
- [MCPJungle](https://github.com/mcpjungle/MCPJungle) - Self-hosted registry and single gateway endpoint for the MCP servers an organisation runs, exposing Prometheus metrics through OpenTelemetry but documenting no traces.
- [MCP Context Forge](https://github.com/IBM/mcp-context-forge) - Gateway and registry that federates MCP servers and REST APIs behind one endpoint, with auth, plugins, and a `tool.invoke` OpenTelemetry span per tool call; Apache-2.0.
- [Docker MCP Gateway](https://github.com/docker/mcp-gateway) - Docker CLI plugin that fronts multiple MCP servers behind one gateway with container isolation, and starts an `mcp.tool.call` OpenTelemetry span per tool call on the Docker CLI's tracer provider, which its code does; its README mentions call tracing but not OpenTelemetry.
- [Aident Loadout](https://docs.aident.ai/loadout/overview) - Proprietary hosted service, with an MIT-licensed client skill, that gives agents a CLI and MCP endpoint for actions on connected apps, with vault-held credentials, a pre-run cost estimate, and an audit of recent actions with status and, where applicable, cost.

## Agent frameworks with built-in tracing

- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) - Tracing is on by default and exports to OpenAI; custom processors send it to third-party platforms.
- [Google ADK](https://github.com/google/adk-python) - Agent toolkit with built-in evaluation and OpenTelemetry-based tracing.
- [Pydantic AI](https://github.com/pydantic/pydantic-ai) - Agent framework with opt-in OpenTelemetry instrumentation (`Agent.instrument_all()`), viewable in Logfire or any OTel backend.
- [Cognipeer Agent SDK](https://github.com/Cognipeer/agent-sdk) - TypeScript agent runtime with opt-in tracing whose `otlpSink` or `otelTracing` plugin exports each run as OpenTelemetry GenAI spans (`invoke_agent`, `chat`, `execute_tool`) over OTLP/HTTP to any collector; MIT.

## Related lists

[awesome-agent-orchestration](https://github.com/anhermon/awesome-agent-orchestration), this list's sister, maps tools for orchestrating agents and running software factories. Outside it, [awesome-llm-observability](https://github.com/ContextJet-ai/awesome-llm-observability) covers LLM observability with a comparison table, [Awesome-LLMOps](https://github.com/tensorchord/Awesome-LLMOps) covers the wider LLM operations stack, and [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) lists MCP servers to test with the tools here.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Suggestions and corrections welcome, especially for anything on this list that has gone stale.

Maintained by Angel Hermon (https://anhermon.dev): AI agent and MCP observability.

To the extent possible under law, Angel Hermon has waived all copyright and related or neighboring rights to this work. CC0 1.0, 2026.
