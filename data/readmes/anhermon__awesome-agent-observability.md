# Awesome Agent Observability [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Curated tools, standards, and platforms for tracing, evaluating, and governing LLM and AI-agent applications.

Agents fail in ways ordinary services do not: a run is non-deterministic, spans a dozen model and tool calls, and "wrong" is a quality judgement rather than a status code. The projects below cover the resulting stack — OpenTelemetry conventions for GenAI, tracing backends, evaluation harnesses, guardrails, gateways, and Model Context Protocol tooling.

Entries say what a project does, not what it markets, and carry its license where that is not plainly open source. Projects that were dormant, end-of-life, out of scope, or too young to judge were left out. Most entries were installed or built and run against a mock backend at the 2026-10-04 audit; a few could not be run (for example Kong, SigNoz, and anything needing Docker or a hosted account), so this list does not claim every entry was exercised. A weekly job re-checks that each repository still exists, is not archived, and has a recent commit.

## Contents

- [Standards and instrumentation](#standards-and-instrumentation)
- [Tracing and observability platforms](#tracing-and-observability-platforms)
- [Trace backends](#trace-backends)
- [Evaluation and testing](#evaluation-and-testing)
- [Guardrails and security](#guardrails-and-security)
- [Gateways and proxies](#gateways-and-proxies)
- [Model Context Protocol](#model-context-protocol)
- [Agent frameworks with built-in tracing](#agent-frameworks-with-built-in-tracing)

## Standards and instrumentation

- [OpenTelemetry GenAI Semantic Conventions](https://github.com/open-telemetry/semantic-conventions-genai) - Repository that now owns the GenAI spans, metrics, and events, moved out of the main semantic-conventions repo.
- [OpenTelemetry Semantic Conventions](https://github.com/open-telemetry/semantic-conventions) - Parent repo for all OTel conventions, including the HTTP, RPC, and database spans an agent stack also emits.
- [OpenTelemetry GenAI Observability SIG](https://github.com/open-telemetry/community/blob/main/projects/gen-ai.md) - Charter and scope of the OTel project group driving GenAI telemetry; the place to track where the conventions are heading.
- [OpenTelemetry Python GenAI instrumentation](https://github.com/open-telemetry/opentelemetry-python-genai) - Upstream instrumentation packages for OpenAI, Anthropic, Google GenAI, LangChain, Bedrock, and several agent frameworks.
- [OpenLLMetry](https://github.com/traceloop/openllmetry) - OpenTelemetry-based auto-instrumentation for Python LLM apps, exporting to any OTel backend.
- [OpenLLMetry-JS](https://github.com/traceloop/openllmetry-js) - The same instrumentation for TypeScript and Node.js applications.
- [OpenInference](https://github.com/Arize-ai/openinference) - OpenTelemetry-compatible tracing spec and instrumentation libraries for Python, JavaScript, Java, and Go from the Arize Phoenix team.
- [OpenLIT](https://github.com/openlit/openlit) - OTel-native auto-instrumentation SDK for LLM, vector-database, and GPU calls, with a self-hosted UI to read the resulting traces.

## Tracing and observability platforms

- [Langfuse](https://github.com/langfuse/langfuse) - Self-hostable tracing, prompt management, datasets, and evals; ingests OTel as well as its own SDKs; open-core, MIT outside the `ee/` directories.
- [Arize Phoenix](https://github.com/Arize-ai/phoenix) - Trace viewer and eval workbench that runs locally in a notebook or as a server; source-available under the Elastic License 2.0.
- [LangSmith](https://docs.langchain.com/langsmith/observability) - Hosted tracing and eval product from LangChain; the [client SDKs](https://github.com/langchain-ai/langsmith-sdk) are open source, the backend is not.
- [Opik](https://github.com/comet-ml/opik) - Comet's open-source tracing and evaluation platform for LLM and agent workflows.
- [LangWatch](https://github.com/langwatch/langwatch) - OTel-based platform pairing production monitoring with pre-deploy agent simulation, plus an AI gateway and coding-agent tracking; open-core, Apache-2.0 outside the `enterprise/` directory.
- [Laminar](https://github.com/lmnr-ai/lmnr) - Open-source tracing and eval platform for agent runs, with a Rust backend.
- [Agenta](https://github.com/Agenta-AI/agenta) - Self-hostable open-core workspace for building, versioning, and running agents, with tracing of model and tool calls and evaluation support.
- [Pydantic Logfire](https://github.com/pydantic/logfire) - OTel-based observability with first-class Python, Pydantic, and agent instrumentation; the SDK is open source, the backend is hosted and closed.
- [W&B Weave](https://github.com/wandb/weave) - Weights & Biases toolkit for logging, comparing, and evaluating LLM app versions; [docs](https://docs.coreweave.com/products/wandb/weave).
- [MLflow Tracing](https://mlflow.org/docs/latest/genai/tracing/) - GenAI tracing built into [MLflow](https://github.com/mlflow/mlflow), so agent traces sit next to model runs and registries.
- [Braintrust](https://www.braintrust.dev/docs/instrument) - Hosted eval and tracing platform; see [Autoevals](https://github.com/braintrustdata/autoevals) below for its open-source scorers.
- [AgentOps](https://github.com/AgentOps-AI/agentops) - Python SDK for session replay, cost tracking, and tracing across CrewAI, OpenAI Agents SDK, LangChain, AG2, and others; the SDK is MIT, the self-hostable app is Elastic License 2.0.
- [AgentsView](https://github.com/kenn-io/agentsview) - Local-first session search, analytics, and token-use statistics for the Claude Code, Codex, and other coding-agent session archives on your machine; it analyses the agents you use, not apps you build.
- [AgentMeasure](https://github.com/roy-tong/AgentMeasure) - Local CLI that reads Codex and Claude Code session logs and reports duplicate records, retry chains, and repeated tool failures, marking what the logs cannot decide as UNPROVABLE instead of zero.
- [Noveum Trace](https://github.com/Noveum/noveum-trace) - Python SDK whose context managers trace operations, LLM calls, and agent steps and send them over HTTPS to the hosted Noveum platform or a custom endpoint; the SDK is Apache-2.0, the backend is hosted.

## Trace backends

General-purpose OpenTelemetry backends that GenAI spans can be sent to when you do not want an LLM-specific product.

- [OpenTelemetry Collector](https://github.com/open-telemetry/opentelemetry-collector) - Vendor-neutral pipeline to receive, process, filter, and fan out traces before they reach a backend.
- [SigNoz](https://github.com/SigNoz/signoz) - OTel-native, self-hostable traces, metrics, and logs in one UI; open-core, MIT outside the `ee/` and `cmd/enterprise/` directories.
- [Jaeger](https://github.com/jaegertracing/jaeger) - CNCF distributed tracing backend that stores spans and serves trace search and a waterfall UI over them.
- [Grafana Tempo](https://github.com/grafana/tempo) - High-volume trace store backed by object storage, queried from Grafana; AGPL-3.0.

## Evaluation and testing

- [Ragas](https://github.com/vibrantlabsai/ragas) - Metrics and test-set generation for RAG and agent pipelines.
- [DeepEval](https://github.com/confident-ai/deepeval) - Pytest-style eval framework with G-Eval, hallucination, and relevancy metrics.
- [Promptfoo](https://github.com/promptfoo/promptfoo) - Declarative CLI for prompt/model comparison plus LLM red-teaming and vulnerability scanning in CI; MIT, now part of OpenAI.
- [TruLens](https://github.com/truera/trulens) - Instrumentation plus feedback functions that score app internals, not just final output.
- [Evidently](https://github.com/evidentlyai/evidently) - Python framework for evals, drift detection, and monitoring across tabular, text, and GenAI systems.
- [Inspect](https://github.com/UKGovernmentBEIS/inspect_ai) - UK AI Security Institute's eval framework, built for agentic tasks, tool use, and sandboxed execution.
- [Inspect Scout](https://github.com/meridianlabs-ai/inspect_scout) - Scans agent transcripts from Inspect eval logs and other sources with LLM, grep, or custom scanners and writes queryable results, for finding failure patterns across runs; MIT.
- [Giskard](https://github.com/Giskard-AI/giskard-oss) - Checks and red-team scans for LLM agents: multi-turn scenarios, LLM-judge checks, and probes for prompt injection and harmful content (v3; v2 is unmaintained).
- [Scenario](https://github.com/langwatch/scenario) - Simulates multi-turn users against an agent so conversations, not single calls, can be asserted on.
- [Autoevals](https://github.com/braintrustdata/autoevals) - Standalone library of model-graded and heuristic scorers usable outside Braintrust.
- [OpenEvals](https://github.com/langchain-ai/openevals) - Readymade evaluators for LLM apps: LLM-as-judge prompts, exact and string-distance matchers, and structured-output checks, as functions that return scored results and plug into pytest or LangSmith, in Python and TypeScript.
- [AgentEvals](https://github.com/langchain-ai/agentevals) - Evaluators that score an agent's tool-call trajectory against a reference with strict, unordered, subset, or superset matching, or with an LLM judge; MIT.
- [AgentDojo](https://github.com/ethz-spylab/agentdojo) - ETH Zurich benchmark and framework for tool-using agents against prompt injection, with task suites and attack and defense pipelines that report utility and attack success.
- [ClawBench](https://github.com/TIGER-AI-Lab/ClawBench) - Live-web benchmark for evaluating browser and computer-use agents on about 280 everyday tasks, with request interception and recorded execution evidence.
- [HermesGate](https://github.com/roli-lpci/hermes-gate) - Runs a repository's own checks and stores a receipt keyed to the content and tool versions checked; in `fast` and `review` modes an identical receipt is reused as a PASS and any change re-runs the checks, giving an agent's own PR a repeatable pre-review result.
- [YYLO Benchmark](https://github.com/yylo-dev/yylo-benchmark) - Runs coding prompts and tasks across models and harnesses on fresh checkouts, keeps every output unchanged, and lets you re-evaluate them later with new checks or judges.
- [NovaFabric](https://github.com/MSKazemi/novafabric) - Self-hosted CLI whose `nova capture` wraps any command, such as an agent script, and records the run as a portable Run Capsule that you can replay and structurally diff against another run; Apache-2.0, pre-1.0.

## Guardrails and security

- [Guardrails AI](https://github.com/guardrails-ai/guardrails) - Runs input/output validators around a model call and enforces structured output.
- [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) - NVIDIA toolkit for input, output, dialogue, and tool rails defined in Colang and Python.
- [OpenAI Guardrails](https://github.com/openai/openai-guardrails-python) - Drop-in OpenAI client wrapper that runs configurable input and output checks (keywords, secret keys, PII, URLs, moderation, jailbreak and prompt-injection detection) and raises on a tripwire; preview release.
- [garak](https://github.com/NVIDIA/garak) - LLM vulnerability scanner probing for jailbreaks, prompt injection, and data leakage.
- [DeepTeam](https://github.com/confident-ai/deepteam) - Red-teaming framework that simulates jailbreaks, prompt injection, and related attacks against LLM and agent apps, built on DeepEval.
- [Presidio](https://github.com/data-privacy-stack/presidio) - PII detection, redaction, and anonymisation for text and images; useful for scrubbing traces before export.
- [Snyk agent-scan](https://github.com/snyk/agent-scan) - Security scanner for MCP servers, agents, and skills, formerly Invariant Labs' `mcp-scan`; `inspect` lists what a config exposes locally, while `scan` needs a Snyk token and calls Snyk's hosted API.
- [MCP Scanner](https://github.com/cisco-ai-defense/mcp-scanner) - Scans MCP servers' tools, prompts, resources, and instructions for poisoning and exfiltration patterns using YARA rules, optional LLM and behavioural analyzers, and a Cisco API analyzer; Apache-2.0.

## Gateways and proxies

- [LiteLLM](https://github.com/BerriAI/litellm) - SDK and proxy exposing 100+ providers behind the OpenAI API, with cost tracking, logging, and callbacks to most platforms above; open-core, MIT outside the `enterprise/` directory.
- [Portkey AI Gateway](https://github.com/Portkey-AI/gateway) - Routing gateway with retries, fallbacks, caching, and inline guardrails.
- [Bifrost](https://github.com/maximhq/bifrost) - Go gateway that fronts multiple LLM providers behind one OpenAI-compatible API, with key load balancing, fallbacks, and Prometheus and OpenTelemetry telemetry; guardrails are enterprise-only.
- [Agentgateway](https://github.com/agentgateway/agentgateway) - Linux Foundation proxy for agent-to-LLM, agent-to-MCP, and agent-to-agent (A2A) traffic with routing, guardrails, RBAC, and OpenTelemetry.
- [Traceloop Hub](https://github.com/traceloop/hub) - Small Rust LLM gateway from the OpenLLMetry authors, with OTel emission built in.
- [Kong](https://github.com/Kong/kong) - API gateway whose AI plugins add LLM routing, token metrics, and request logging to an existing gateway deployment.

## Model Context Protocol

- [Model Context Protocol](https://github.com/modelcontextprotocol/modelcontextprotocol) - The specification itself; the source of truth for what a compliant client, server, and transport must do.
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector) - Official UI for calling an MCP server's tools by hand and reading the raw JSON-RPC traffic.
- [MCP Registry](https://github.com/modelcontextprotocol/registry) - Official, community-owned registry service for publishing and discovering MCP servers; still in preview.
- [mcp-trace](https://github.com/anhermon/mcp-trace) - CLI proxy for MCP servers over SSE or Streamable HTTP that emits an OpenTelemetry span per tool call with duration, status, and propagated trace context, including Streamable HTTP tool calls that return `text/event-stream`.
- [ToolHive](https://github.com/stacklok/toolhive) - Runs MCP servers in containers with permission policies, secrets handling, and audit logging.
- [MCPJungle](https://github.com/mcpjungle/MCPJungle) - Self-hosted registry and single gateway endpoint for the MCP servers an organisation runs.
- [MCP Context Forge](https://github.com/IBM/mcp-context-forge) - Gateway and registry that federates MCP servers and REST APIs behind one endpoint, with auth, plugins, and OpenTelemetry tracing of tool calls; Apache-2.0.
- [Docker MCP Gateway](https://github.com/docker/mcp-gateway) - Docker CLI plugin that fronts multiple MCP servers behind one gateway with container isolation.

## Agent frameworks with built-in tracing

- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) - Tracing is on by default and exports to OpenAI; custom processors send it to third-party platforms.
- [Google ADK](https://github.com/google/adk-python) - Agent toolkit with built-in evaluation and OpenTelemetry-based tracing.
- [Pydantic AI](https://github.com/pydantic/pydantic-ai) - Agent framework with opt-in OpenTelemetry instrumentation (`Agent.instrument_all()`), viewable in Logfire or any OTel backend.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Suggestions and corrections welcome, especially for anything on this list that has gone stale.

To the extent possible under law, Angel Hermon has waived all copyright and related or neighboring rights to this work. CC0 1.0, 2026.
