# awesome-x-ops

A curated map of modern X-Ops: AI Ops, LLM/Agent Observability, Platform Engineering, GitOps, DataOps, FinOps, DevSecOps, and production-grade open-source operations tooling.

Languages: English | [简体中文](README.zh-CN.md)

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

## Why awesome-x-ops?

Operations work is no longer just infrastructure monitoring or CI/CD glue. Modern teams need a practical map across AI-native applications, LLM observability, platform engineering, software delivery, cloud cost, security, and developer experience.

This list focuses on tools that help teams build, run, observe, secure, and optimize production systems.

## Featured Maps

- [LLM and Agent Observability Stack](#llm-and-agent-observability): tracing, prompt monitoring, evaluation, feedback, and production telemetry for LLM and agent systems.
- [LLM Knowledge](#llm-knowledge): open-source platforms for turning documents into RAG knowledge bases, autonomous reasoning agents, and self-maintaining wikis.
- [AI Infrastructure](#ai-infrastructure): web crawling, AI-ready extraction, search intelligence, and RAG data acquisition.
- [Platform Engineering Stack](#platform-engineering): internal developer platforms, IAM, IaC, artifacts, API tooling, CI/CD, and testing.
- [GitOps and Kubernetes Operations Stack](#kubernetes-operations): cluster networking, autoscaling, deployment, and runtime operations.
- [FinOps Stack](#finops): cloud and Kubernetes cost visibility, allocation, and forecasting.
- [DevSecOps and Supply Chain Stack](#security-and-supply-chain): policy, runtime security, SBOM, scanning, and software supply-chain risk management.
- [DataOps Stack](#dataops): dataflow, orchestration, and data asset lifecycle tooling.

## Who is this for?

- Platform engineering teams building internal developer platforms.
- DevOps, SRE, and infrastructure teams modernizing operations stacks.
- AI engineering teams operating LLM, RAG, and agent applications in production.
- Engineering leaders looking for reliable open-source options before buying or building.
- Open-source maintainers who want their production-grade operations tools to be discoverable.

## How to use this map

Start with the operational failure you need to control, not the most fashionable project: use **LLM and Agent Observability** for trace and evaluation evidence, **AI Serving and Inference Operations** for rollout and runtime capacity, **AI Infrastructure** or **LLM Knowledge** for ingestion and retrieval, and **Security and Supply Chain** for policy, isolation, and audit. Then compare the smallest set of tools that covers your rollback, ownership, and data-retention requirements.

## Curation Principles

- Keep entries concise, efficient, accurate, and relevant.
- Prefer GitHub links when a reliable project repository exists.
- Include only proven, reliable, and high-quality projects.
- Ignore duplicates or projects already covered by an equivalent entry.
- Add or refine categories when useful, but avoid unrelated content.
- Prefer production-grade open source over demos, abandoned experiments, or vendor-only marketing pages.

## Growth and Contribution

This project aims to become a practical open-source map for modern X-Ops. Contributions are welcome if they improve accuracy, coverage, or navigation without turning the list into a link dump.

- Suggest a missing project via [Issues](https://github.com/xlabs-club/awesome-x-ops/issues).
- Open a focused pull request using [CONTRIBUTING.md](CONTRIBUTING.md).
- Keep descriptions short and explain why the project belongs in an operations/platform context.

## LLM and Agent Observability

Tools for tracing, evaluating, debugging, and operating LLM, RAG, and agent applications in production.

**Selection guidance:** Prefer tools that connect traces to prompts, model versions, evaluations, and cost or latency signals; for RAG, favor evaluation workflows that measure retrieval and answer quality without requiring brittle golden-answer sets; use gateway, security, and serving tools in their dedicated sections when observability is not their primary operational purpose. For agent-specific tooling, verify that tool calls, state transitions, failures, and operator actions remain inspectable—not merely that a dashboard exists.

**Production checklist:** Before adopting a tool, verify OpenTelemetry or an exportable trace format, retention and redaction controls, reproducible evaluation runs, framework coverage, and a clear path from an alert to the underlying prompt, tool call, model, and cost. A dashboard without failure evidence is just a very colorful shrug.

**Regression gate:** Keep a small, versioned evaluation set in CI, compare retrieval and answer-quality metrics separately, and define rollback thresholds before changing prompts, models, retrievers, or gateway policies. “It looked good in the demo” is not a release strategy.

**EvalOps selection guidance:** Prefer evaluation tools that separate retrieval, generation, tool-use, safety, latency, and cost signals; support fixed datasets plus sampled production traces; and emit machine-readable results for CI or release gates. LLM-as-a-judge is useful evidence, not ground truth—pin the judge model and rubric, sample human review, and keep failed cases replayable.

**Operational evidence checklist:** For production rollouts, record the trace and evaluation schema, sampling and PII-redaction policy, owner for each alert, retention and replay limits, and the rollback trigger. For coding agents and other opaque runtimes, pair application traces with process, network, and resource signals so failures remain diagnosable when SDK instrumentation is missing. If a tool cannot export evidence that another system can inspect, it is an integration risk—not just a missing checkbox.

**Gateway boundary:** Treat routing, rate limits, budgets, retries, and provider failover as gateway concerns; keep tracing, evaluation, and prompt or response analysis here only when they are the tool’s primary operational purpose. This avoids counting one gateway as three observability platforms with different hats.

**Gateway selection guidance:** Choose the smallest control surface that covers provider abstraction, routing policy, quotas, retries, and auditability. Before production rollout, verify streaming behavior, timeout and fallback semantics, tenant isolation, secret rotation, cost attribution, and metrics or traces that remain useful when an upstream provider is degraded.

- [LiteLLM](https://github.com/BerriAI/litellm): OpenAI-compatible LLM gateway with routing, budgets, logging, and provider abstraction.
- [Switchyard](https://github.com/NVIDIA-NeMo/Switchyard): LLM traffic router for selecting models and providers, benchmarking performance, and optimizing cost while preserving OpenAI and Anthropic API compatibility.
- [Langfuse](https://github.com/langfuse/langfuse): Open-source LLM engineering platform for traces, prompt management, evaluations, and metrics.
- [Candela](https://github.com/candelahq/candela): OpenTelemetry-native LLM observability platform for tracing, cost tracking, and evaluation with local or cloud storage backends.
- [Litefuse](https://github.com/litefuse/litefuse): Open-source LLM engineering platform for collaboratively developing, monitoring, evaluating, and debugging AI applications with self-hosted deployment.
- [DeepEval](https://github.com/confident-ai/deepeval): LLM evaluation framework for testing RAG, agents, and model outputs in CI or production workflows.
- [Ragas](https://github.com/vibrantlabsai/ragas): Evaluation framework for RAG pipelines and LLM applications.
- [Arize Phoenix](https://github.com/Arize-ai/phoenix): Open-source observability and evaluation platform for LLM, RAG, and ML systems.
- [OpenInference](https://github.com/Arize-ai/openinference): OpenTelemetry instrumentation and semantic conventions for tracing LLM, RAG, and agent applications.
- [Agent Telemetry Semantic Conventions](https://github.com/agent-telemetry-spec/atsc): Vendor-neutral, OpenTelemetry-compatible semantic conventions for interoperable AI agent observability.
- [OpenLLMetry](https://github.com/traceloop/openllmetry): OpenTelemetry-based observability for LLM applications and agent workflows.
- [Helicone](https://github.com/Helicone/helicone): Open-source observability platform for LLM usage, latency, cost, caching, and request logs.
- [OpenLIT](https://github.com/openlit/openlit): OpenTelemetry-native AI engineering platform for LLM observability, evaluations, guardrails, prompt management, and GPU monitoring.
- [Grafana AI Observability SDK](https://github.com/grafana/agento11y): Open-source SDKs and coding-agent plugins for sending production agent and LLM telemetry to Grafana AI observability.
- [LangWatch](https://github.com/langwatch/langwatch): Open-source platform for LLM monitoring, evaluations, traces, and agent testing.
- [ClaudeSec](https://github.com/aanjaneyasinghdhoni/ClaudeSec): Fully local observability and security dashboard for AI coding agents, with OpenTelemetry traces, command auditing, threat detection, and optional enforcement.
- [Opik](https://github.com/comet-ml/opik): Open-source platform for tracing, evaluating, and monitoring LLM applications, RAG systems, and agent workflows.
- [ClawMetry](https://github.com/vivekchand/clawmetry): Local-first observability and governance dashboard for 26 AI agent runtimes, with sessions, tool calls, token costs, alerts, approvals, and OpenTelemetry export.
- [Exgentic](https://github.com/Exgentic/exgentic): General agent evaluation framework for standardized, reproducible testing across agents, benchmarks, and domains.
- [promptfoo](https://github.com/promptfoo/promptfoo): Open-source CLI and platform for prompt testing, LLM evaluations, red teaming, and CI/CD regression checks.
- [Langtrace](https://github.com/Scale3-Labs/langtrace): OpenTelemetry-based observability platform for tracing, evaluating, and monitoring LLM applications.
- [Future AGI](https://github.com/future-agi/future-agi): Self-hostable platform for evaluating, observing, and improving LLM and AI agent applications.
- [CozeLoop](https://github.com/coze-dev/coze-loop): AI agent optimization platform covering development, debugging, evaluation, and production monitoring workflows.
- [Judgeval](https://github.com/JudgmentLabs/judgeval): Continuous-improvement stack for agents, combining environment data and evaluations to improve and monitor agent behavior.
- [Acontext](https://github.com/memodb-io/Acontext): Open-source memory layer for AI agents that turns reusable agent skills and context into an operational service.
- [Agenta](https://github.com/Agenta-AI/agenta): Open-source LLMOps platform for prompt management, playgrounds, evaluations, and observability.
- [abtop](https://github.com/graykode/abtop): htop-style terminal monitor for AI coding agent sessions, tokens, context windows, rate limits, and ports.
- [agenttrace](https://github.com/luoyuctl/agenttrace): Local-first TUI for inspecting AI coding agent cost, tokens, latency, failures, and reports.
- [agentacct](https://github.com/mikehasa/agentacct): Local-first terminal dashboard that joins coding-agent session usage with recorded work steps, checks, provider limits, and estimated cost.
- [agentglass](https://github.com/SirAllap/agentglass): Local-first cockpit for monitoring coding-agent sessions, tool calls, tokens, costs, and latency through hooks or OpenTelemetry, with optional approval controls.
- [OpenTelemetry MCP Server](https://github.com/traceloop/opentelemetry-mcp-server): Unified MCP server for querying OpenTelemetry traces across Jaeger, Tempo, Traceloop, and other backends so AI agents can investigate distributed systems.
- [Langfuse MCP Server](https://github.com/avivsinai/langfuse-mcp): MCP server and agent skill for querying Langfuse traces, debugging agent runs, inspecting sessions, and managing prompts from AI coding clients.
- [Agent Diff](https://github.com/agent-diff-bench/agent-diff): Interactive, sandboxed replicas of third-party APIs for deterministic AI agent evaluation and reinforcement-learning experiments without external side effects.
- [MCP State Twin](https://github.com/augety121/MCP-State-Twin): Deterministic, forkable, stateful MCP test worlds for reproducible AI agent evaluation without side effects in production systems.
- [SCALE-CUA](https://github.com/THUDM/SCALE-CUA): Open framework for computer-use agents with verifiable task synthesis, online reinforcement learning, and OSWorld or ScienceBoard evaluation.
- [ClawLens](https://github.com/nk3750/clawlens): Local OpenClaw observability plugin with tool-call audit logs, risk scoring, live sessions, and operator-controlled guardrails.
- [Opik OpenClaw](https://github.com/comet-ml/opik-openclaw): OpenClaw plugin that exports agent traces to Opik for monitoring behavior, errors, tokens, and cost.
- [Opik MCP](https://github.com/comet-ml/opik-mcp): MCP server for reading Opik traces, logging evaluation scores, and managing prompts from AI coding clients.
- [NeMo Relay](https://github.com/NVIDIA/NeMo-Relay): Multi-language agent runtime and middleware library for managing execution scopes, lifecycle events, and tool or LLM call telemetry.
- [Kitaru](https://github.com/zenml-io/kitaru): Production AI agent recording and replay toolkit for analyzing runs and improving agent behavior.
- [ax](https://github.com/Necmttn/ax): Local-first telemetry and memory graph for AI coding agents, covering costs, tools, skills, sessions, and OTLP events.
- [Mindwalk](https://github.com/cosmtrek/mindwalk): Visualization tool that replays coding-agent sessions on a 3D map of your codebase for debugging and understanding agent behavior.
- [TensorZero](https://github.com/tensorzero/tensorzero): Open-source LLMOps platform that combines an LLM gateway, observability, evaluations, optimization, and experimentation. (Archived upstream.)
- [cascadeflow](https://github.com/lemony-ai/cascadeflow): Cascading runtime for AI agents that makes cost, latency, quality, and policy decisions inside the agent loop.
- [Evidently](https://github.com/evidentlyai/evidently): Open-source ML and LLM observability framework for evaluation, testing, monitoring, and data quality checks.
- [RagaAI Catalyst](https://github.com/raga-ai-hub/RagaAI-Catalyst): Agent AI observability and evaluation SDK for tracing, debugging, and monitoring multi-agent LLM systems.
- [Pydantic Logfire](https://github.com/pydantic/logfire): AI observability platform for tracing and monitoring production LLM and agent systems.
- [Laminar](https://github.com/lmnr-ai/lmnr): Open-source observability platform purpose-built for AI agents and LLM applications.
- [whylogs](https://github.com/whylabs/whylogs): Open-source data logging library for profiling ML and LLM data quality, drift detection, and telemetry monitoring in production pipelines.
- [MLflow](https://github.com/mlflow/mlflow): Open-source AI engineering platform for debugging, evaluating, monitoring, and optimizing agents, LLMs, and ML models.
- [Giskard](https://github.com/Giskard-AI/giskard-oss): Open-source evaluation and testing framework for LLM applications and AI agents.
- [ZenML](https://github.com/zenml-io/zenml): AI platform for production ML, LLM, and agent pipelines with orchestration, tracking, and deployment workflows.
- [Guardrails](https://github.com/guardrails-ai/guardrails): Framework for validating LLM outputs and enforcing safety, quality, and structured response checks.
- [Plano](https://github.com/katanemo/plano): AI-native proxy and data plane for agentic applications with routing, safety, orchestration, and observability.
- [AgentSight](https://github.com/eunomia-bpf/agentsight): eBPF-based system-level tracing for observing AI agent execution without application instrumentation.
- [AgentOps](https://github.com/AgentOps-AI/agentops): Python SDK for monitoring AI agents, tracking LLM costs, benchmarking runs, and integrating with common agent frameworks.
- [LLM Gateway](https://github.com/theopenco/llmgateway): Open-source gateway for routing, managing, and analyzing LLM requests across multiple providers through one API.
- [AI Proxy](https://github.com/labring/aiproxy): High-performance AI gateway with OpenAI-, Claude-, and Gemini-compatible protocols, multi-channel management, rate limiting, multi-tenant isolation, and monitoring.
- [LLMIO](https://github.com/atopos31/llmio): Go-based LLM gateway with weighted provider routing, an admin UI, request tracing, latency and token metrics, cost tracking, and failure handling.
- [OpenZiti LLM Gateway](https://github.com/openziti/llm-gateway): Zero-trust, OpenAI-compatible gateway with identity-based access, semantic routing, and load balancing across hosted and self-hosted model providers.
- [Portkey AI Gateway](https://github.com/Portkey-AI/gateway): AI gateway for routing LLM traffic, applying guardrails, and centralizing model access for production applications.
- [Ferro AI Gateway](https://github.com/ferro-labs/ai-gateway): Go-native AI gateway for multi-provider routing, caching, guardrails, A/B testing, and cost controls.
- [Braintrust AI Proxy](https://github.com/braintrustdata/braintrust-proxy): Self-hostable unified AI model proxy with provider-neutral access, response caching, and request observability hooks.
- [Shepherd Model Gateway (SMG)](https://github.com/smg-project/smg): High-performance, engine-agnostic LLM gateway with cache-aware routing, HTTP/gRPC workers, multi-tenant controls, MCP support, and OpenTelemetry metrics and traces.
- [GoModel](https://github.com/ENTERPILOT/GoModel): Go-based AI gateway with OpenAI and Anthropic-compatible APIs, provider routing, failover, observability, cost tracking, and multi-tenant controls.
- [Traceloop Hub](https://github.com/traceloop/hub): High-performance Rust LLM gateway with a unified provider API, OpenTelemetry traces, Prometheus metrics, and configurable request pipelines.
- [New API](https://github.com/QuantumNous/new-api): Unified AI model gateway for aggregating providers, normalizing OpenAI/Claude/Gemini-compatible APIs, and managing enterprise model access.
- [Manifest](https://github.com/mnfst/llm-gateway): Provider-agnostic runtime that connects agents and agent harnesses to model providers through a unified interface.
- [OmniRoute](https://github.com/diegosouzapw/OmniRoute): Self-hosted AI gateway that unifies many model providers behind one endpoint with automatic fallback, routing, MCP/A2A support, and token-saving compression.
- [Otari](https://github.com/mozilla-ai/otari): Open-source, OpenAI-compatible LLM gateway from Mozilla AI with one endpoint for 40+ providers, virtual keys, budgets, and usage tracking.
- [1flowbase](https://github.com/taichuy/1flowbase): Self-hosted AI gateway for composing multi-model workflows behind OpenAI-compatible virtual models with traces, token usage, latency, and cost visibility.
- [BISHENG](https://github.com/dataelement/bisheng): Open LLM DevOps platform for enterprise AI applications, with GenAI workflows, RAG, agents, model management, evaluation, datasets, and observability.
- [OpenObserve](https://github.com/openobserve/openobserve): Open-source observability platform for logs, metrics, traces, frontend monitoring, pipelines, and LLM observability.
- [Kubeshark](https://github.com/kubeshark/kubeshark): eBPF-powered Kubernetes network observability with L4/L7 traffic context, TLS visibility, and an MCP interface for AI-assisted investigation.
- [MCP Gateway](https://github.com/IBM/mcp-context-forge): AI gateway, registry, and proxy for MCP, A2A, and API tools with centralized discovery, guardrails, and management.
- [Supergateway](https://github.com/supercorp-ai/supergateway): Lightweight bridge that runs MCP stdio servers over SSE and converts SSE connections back to stdio for interoperable deployments.
- [NVIDIA NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails): Toolkit for adding programmable safety, dialog, and policy guardrails to LLM-based conversational systems.
- [Llama Guard](https://github.com/meta-llama/PurpleLlama): Meta's open trust and safety toolkit for evaluating and filtering LLM inputs, outputs, and model risks.
- [LLM Guard](https://github.com/protectai/llm-guard): Security toolkit for sanitizing LLM inputs and outputs, detecting prompt injection, blocking harmful content, and reducing data leakage. (Archived upstream.)
- [garak](https://github.com/NVIDIA/garak): LLM vulnerability scanner for probing prompt injection, jailbreaks, data leakage, hallucination, and other generative AI risks.
- [agentic-security](https://github.com/msoedov/agentic_security): Open-source LLM vulnerability scanner and AI red teaming kit for fuzzing and testing LLM guardrails against adversarial attacks.
- [SlowMist Agent Security](https://github.com/slowmist/slowmist-agent-security): Agent security review framework for adversarial environments, centered on treating every external input as untrusted until verified.
- [Superagent](https://github.com/superagent-ai/superagent): Open-source AI security SDK for protecting LLM applications against prompt injections, data leaks, and harmful outputs.
- [PINT Benchmark](https://github.com/lakeraai/pint-benchmark): Open-source benchmark for evaluating prompt injection detection systems across diverse attack vectors. (Archived upstream.)
- [FuzzyAI](https://github.com/cyberark/FuzzyAI): Apache-2.0 LLM fuzzing tool for finding and mitigating jailbreak vulnerabilities in LLM APIs.
- [OpenEvals](https://github.com/langchain-ai/openevals): Ready-made evaluators for testing and regression-checking LLM applications in development and CI workflows.
- [RAGEval](https://github.com/BytePioneer-AI/RAGEval): Open-source RAG evaluation system for automating dataset-based quality checks across retrieval and generation workflows.
- [TruLens](https://github.com/truera/trulens): Evaluation and tracking framework for LLM experiments and AI agents with feedback functions, guardrails, and iterative improvement workflows.
- [OpenCompass](https://github.com/open-compass/opencompass): LLM evaluation platform supporting a wide range of models across 100+ datasets with reproducible benchmarks.
- [Lighteval](https://github.com/huggingface/lighteval): Modular toolkit for reproducible LLM evaluations across multiple backends, tasks, metrics, and distributed execution environments.
- [OpenAI Evals](https://github.com/openai/evals): Framework for evaluating LLMs and LLM systems with an open-source registry of benchmarks and evaluation workflows.
- [Hugging Face Evaluation Guidebook](https://github.com/huggingface/evaluation-guidebook): Practical guide to LLM evaluation metrics, methods, and lessons from operating large-model evaluation programs.
- [AgentBench](https://github.com/THUDM/AgentBench): Apache-2.0 benchmark for evaluating LLMs as agents across diverse environments and tasks.
- [Olmes](https://github.com/allenai/olmes): Reproducible and flexible framework for evaluating language models across configurable benchmarks and evaluation workflows.
- [PromptWizard](https://github.com/microsoft/PromptWizard): Task-aware, agent-driven prompt optimization framework that uses iterative critique and evaluation to improve prompts for repeatable LLM workflows.
- [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai): MIT-licensed framework for building, running, and analyzing reproducible evaluations of large language models.
- [One-Eval](https://github.com/OpenDCAI/One-Eval): Agent-based evaluation framework that turns natural-language requirements into traceable, interruptible, and scalable LLM evaluation workflows and reports.
- [MASEval](https://github.com/maseval/MASEval): Agent-agnostic evaluation infrastructure for benchmarking multi-agent systems with adapters, lifecycle hooks, tracing, logging, and metrics.
- [Aleph Alpha Eval-Framework](https://github.com/Aleph-Alpha-Research/eval-framework): Apache-2.0 framework for distributed LLM evaluation across 90+ benchmarks, with extensible models, tasks, metrics, perturbation testing, and statistical reports.
- [HELM](https://github.com/stanford-crfm/helm): Open-source framework for holistic, reproducible, and transparent evaluation of language and multimodal models.
- [Agent Router](https://github.com/theagentrouter/agent-router): Envoy-based control plane for AI and agent traffic that gives application teams one OpenAI-compatible API across hosted providers, self-hosted inference, and MCP servers, while platform teams centralize credentials, routing, quotas, and failover. Formerly Envoy AI Gateway.
- [Higress](https://github.com/higress-group/higress): AI-native API gateway built on Envoy for unified LLM provider access, canary routing, rate limiting, and multi-model observability.
- [Bifrost](https://github.com/maximhq/bifrost): High-performance enterprise AI gateway with adaptive load balancing, guardrails, cluster mode, and 1000+ model support.
- [TokenHub](https://github.com/astaxie/TokenHub): Enterprise AI gateway for unified model access, request governance, traceability, and usage attribution.
- [CliRelay](https://github.com/kittors/CliRelay): Self-hosted AI gateway for coding CLIs with a unified endpoint, multi-tenant console, request logs, and spend quotas.
- [My Free Code](https://github.com/hkqr/my-free-code): Open-source multi-provider gateway for Claude Code and other coding agents, with streaming, tool calls, health-aware routing, fallbacks, and local model support.
- [Adaline Gateway](https://github.com/adaline/gateway): Fully local TypeScript gateway SDK for calling 300+ LLMs with batching, retries, caching, callbacks, and OpenTelemetry integration.
- [Inference Gateway](https://github.com/inference-gateway/inference-gateway): Cloud-native LLM gateway for unifying providers, routing inference traffic, and exposing OpenTelemetry-friendly operations on Kubernetes.
- [OneAIFW](https://github.com/funstory-ai/aifw): Lightweight local AI firewall for anonymizing sensitive data before LLM calls and restoring it after responses.
- [Microsoft MCP Gateway](https://github.com/microsoft/mcp-gateway): Reverse proxy and management layer for operating MCP servers with session-aware routing and Kubernetes lifecycle support.
- [CoAI](https://github.com/coaidev/coai): Multi-tenant AI platform with a unified LLM gateway, provider routing, cost management, billing, and model cache for enterprise deployments.
- [Kong](https://github.com/Kong/kong): Cloud-native API, LLM, and MCP gateway with advanced AI traffic management, multi-provider routing, semantic security, and rich plugin ecosystem.
- [Apache APISIX](https://github.com/apache/apisix): Apache dynamic API and AI gateway with LLM proxying, token-based rate limiting, MCP bridge, and plugin-based AI traffic control.
- [LangKit](https://github.com/whylabs/langkit): Open-source toolkit for monitoring LLMs by extracting signals from prompts and responses, including text quality, relevance, sentiment, and prompt injection detection.
- [AxonHub](https://github.com/looplj/axonhub): Open-source AI gateway with failover, load balancing, cost control, and end-to-end tracing across 100+ LLM providers.
- [MCP Gateway & Registry](https://github.com/agentic-community/mcp-gateway-registry): Enterprise MCP gateway and AI asset registry with OAuth, semantic search, audit trails, and unified governance for agents, skills, and MCP servers.
- [Weights & Biases](https://github.com/wandb/wandb): AI developer platform for experiment tracking, model management, and monitoring ML/LLM workflows from training to production.
- [ClearML](https://github.com/clearml/clearml): Open-source MLOps/LLMOps platform for experiment management, data pipelines, orchestration, and model serving.
- [Helicone AI Gateway](https://github.com/Helicone/ai-gateway): Fast, lightweight Rust-based AI gateway with smart routing, caching, rate limiting, and built-in observability across 100+ LLM providers.
- [EleutherAI LM Eval](https://github.com/EleutherAI/lm-evaluation-harness): Standardized framework for few-shot and zero-shot evaluation of language models across hundreds of tasks and benchmarks.
- [Weave](https://github.com/wandb/weave): Toolkit for tracing, evaluating, and improving LLM applications with automatic versioning and interactive debugging workflows.
- [Pezzo](https://github.com/pezzolabs/pezzo): Open-source LLMOps platform for prompt management, version control, A/B testing, troubleshooting, and observability.
- [Latitude](https://github.com/latitude-dev/latitude-llm): Open-source AI monitoring and evaluation platform for production LLM applications with collaborative debugging, dataset management, and CI/CD integration.
- [TraceRoot](https://github.com/traceroot-ai/traceroot): Open-source observability and self-healing layer for AI agents, providing real-time monitoring and automated remediation.
- [SkillOpt](https://github.com/microsoft/SkillOpt): Microsoft's text-space optimizer that trains reusable natural-language skills for frozen LLM agents through trajectory-driven edits and validation-gated updates.
- [AgentField](https://github.com/Agent-Field/agentfield): Control plane for building, running, and scaling observable, auditable, identity-aware AI agents as APIs and microservices.
- [Prompty](https://github.com/microsoft/prompty): Markdown-based prompt format and tooling for creating, managing, debugging, and evaluating portable LLM prompts.
- [Databuff](https://github.com/databufflabs/databuff): AI-native OpenTelemetry APM with multi-agent root-cause analysis across traces, metrics, and service topology.
- [RocketplaneIO](https://github.com/olemeyer/rocketplaneIO): Self-hosted AI SRE for Kubernetes with zero-instrumentation eBPF observability and guardrailed, self-verifying remediation.
- [AgentProvenance](https://github.com/ByteYellow/AgentProvenance): Security-oriented observability for sandboxed AI agents, combining model intent, application context, and runtime telemetry into verifiable evidence graphs.
- [AgentCanvas](https://github.com/vstorm-co/agentcanvas): Interactive HTML diagrams for visualizing Pydantic AI agent workflows from Logfire traces, including tools, nested agents, tokens, and cost.
- [Kaito](https://github.com/kaito-project/kaito): Kubernetes AI Toolchain Operator for simplifying model deployment and AI workload management on Kubernetes.
- [OME](https://github.com/ome-projects/ome): Kubernetes operator for LLM serving, GPU scheduling, and model lifecycle management across SGLang, vLLM, TensorRT-LLM, and Triton.
- [AURA](https://github.com/mezmo/aura): Production-oriented harness for safe AI SRE agents, with guardrails, state management, authentication, streaming, and operational tool integrations.
- [ongrid](https://github.com/ongridio/ongrid): Ops AI agent that investigates infrastructure root causes and performs guarded remediation through common team-chat interfaces.
- [Agents Observe](https://github.com/simple10/agents-observe): Real-time observability dashboard for Claude Code and Codex agents with session replay, filtering, and token usage statistics.
- [Pi Agent Observability](https://github.com/disler/pi-agent-observability): Local observability stack for the Pi coding agent, streaming turns, tool calls, model changes, and token-cost telemetry into a dashboard for replay and comparison.
- [Open RAG Eval](https://github.com/vectara/open-rag-eval): Open-source RAG evaluation toolkit for measuring retrieval and answer quality without requiring golden answers.
- [RAG Arena](https://github.com/firecrawl/rag-arena): Open-source RAG evaluation workflow that uses user feedback to compare answer quality and improve retrieval systems.
- [Axon](https://github.com/langchain-tracer/Axon): OpenTelemetry-native LLM observability CLI for viewing LLM and agent traces in real time.
- [EvalScope](https://github.com/modelscope/evalscope): LLM evaluation framework for capability benchmarks, agent-loop evaluation with recorded traces, inference performance testing, and interactive result analysis.
- [Kiln](https://github.com/Kiln-AI/kiln): Open-source workbench for building and improving AI systems with collaborative evals, prompt optimization, RAG, agents, synthetic data, and production deployment support.
- [Google ADK Python](https://github.com/google/adk-python): Code-first Python toolkit for building, evaluating, and deploying production-oriented AI agents with flexible orchestration and tool integration.
- [Google ADK Go](https://github.com/google/adk-go): Code-first Go toolkit for building, evaluating, and deploying production-oriented AI agents with flexible orchestration and tool integration.
- [AssetOpsBench](https://github.com/IBM/AssetOpsBench): Benchmark and framework for building, orchestrating, and evaluating domain-specific industrial AI agents across reproducible asset-operations scenarios.
- [Observal](https://github.com/Observal/Observal): Local registry and analytics platform for governing and understanding AI agents, MCP servers, and reusable agent skills.
- [Agent Prism](https://github.com/evilmartians/agent-prism): React components for visualizing AI agent traces and making multi-step agent execution easier to inspect.
- [Dash0 Agent Skills](https://github.com/dash0hq/agent-skills): OpenTelemetry skills and reference material for AI coding assistants, covering instrumentation patterns and telemetry quality.
- [tma1](https://github.com/tma1-ai/tma1): Local-first observability for coding agents that records LLM calls and exposes logs, metrics, traces, and cost data through hooks and MCP.
- [VictoriaMetrics MCP Server](https://github.com/VictoriaMetrics/mcp-victoriametrics): MCP server for querying VictoriaMetrics from AI assistants and agents, bringing time-series observability context into operational investigations.
- [AgentLens](https://github.com/dreadnode/agent-lens): Harness for running multi-session Claude Code and Codex trajectories with standardized traces, file-change attribution, and replay for agent behavior research.
- [BigQuery Agent Analytics SDK](https://github.com/GoogleCloudPlatform/BigQuery-Agent-Analytics-SDK): Open-source Python SDK for analyzing, evaluating, and curating production agent traces stored in BigQuery.
- [Claude Code Hooks Multi-Agent Observability](https://github.com/disler/claude-code-hooks-multi-agent-observability): Real-time monitoring and visualization for Claude Code agent swarms through hook event tracking, session filters, and live updates.
- [MC Agent Toolkit](https://github.com/monte-carlo-data/mc-agent-toolkit): Agent skills and plugins that bring data lineage, monitoring, validation, alerting, and metadata checks into AI coding workflows.
- [AgentOps Accelerator](https://github.com/Azure/agentops): Open-source CLI and framework for continuous agent evaluation, safety testing, observability, and release-readiness evidence.
- [Smithers](https://github.com/smithersai/smithers): Agent workflow orchestrator with live run observability, human approval gates, and rewind, fork, and replay support across coding-agent runtimes.
- [agent-inspect](https://github.com/rajudandigam/agent-inspect): Local TypeScript agent debugging and regression-testing toolkit that turns runs into execution trees, deterministic contracts, CI gates, and safe evidence bundles.
- [brain0](https://github.com/Brain0-ai/brain0): Offline decision graph for AI-written code that links commits to agent prompts and read context, with drift detection, DLP auditing, risk signals, and signed provenance.
- [TokenTelemetry](https://github.com/VasiHemanth/tokentelemetry): Local dashboard for tracking tokens, costs, tool calls, sessions, and reasoning across coding and autonomous agents.
- [Agent-Blackbox](https://github.com/TaewoooPark/Agent-Blackbox): Local-first flight recorder and context-efficiency profiler for coding agents, with replayable session maps, cost analysis, and task-outcome signals.
- [Mira](https://github.com/everruns/mira): Rust-first evaluation framework for multi-turn, tool-using, long-running agent trajectories with operational budgets and CI-native reports.
- [aws-bench](https://github.com/aws-bench/aws-bench): Benchmark for evaluating coding agents on real AWS tasks in disposable environments, with verifiers for diagnosis, provisioning, and operations.
- [claw-swe-bench](https://github.com/TokenRhythm/claw-swe-bench): Adapter framework for evaluating OpenClaw-style agent harnesses on reproducible SWE-bench issue-resolution tasks.
- [OpenAgent Eval](https://github.com/OpenAgentHQ/openagent-eval): Local-first, framework-agnostic evaluation framework for RAG systems and AI agents with CLI, SDK, and multiple metrics.
- [OpenJudge](https://github.com/agentscope-ai/OpenJudge): Open-source evaluation framework for AI applications with reusable graders, scenario-specific rubrics, scalable runs, and reward signals for continuous optimization.
- [AgentEval (.NET)](https://github.com/AgentEvalHQ/AgentEval): .NET toolkit for evaluating AI agents with tool-use validation, RAG quality metrics, stochastic testing, and model comparison.
- [LLM Space](https://github.com/deer-flow/llm-space): Local-first desktop workspace for prototyping agents, inspecting harness steps, replaying failures, and evaluating agent performance.
- [NeMo Gym](https://github.com/NVIDIA-NeMo/Gym): Open framework for evaluating and improving models and agents through configurable environments and evaluation workflows.
- [Agent Evaluation](https://github.com/awslabs/agent-evaluation): Generative AI evaluation framework for concurrent multi-turn virtual-agent testing, custom targets, hooks, and CI/CD integration.
- [AgentArk](https://github.com/P90-RushB/AgentArk): Open environment framework for reproducible multimodal-agent evaluation, replay, and reinforcement-learning workflows with verifiable task feedback.
- [Intellagent](https://github.com/plurai-ai/intellagent): Framework for diagnosing and optimizing agents through realistic simulated interactions and repeatable evaluation workflows.
- [Rhesis](https://github.com/rhesis-ai/rhesis): Open-source collaboration layer where domain experts annotate agent behavior and engineering teams turn findings into evaluation and improvement loops.
- [o11y-bench](https://github.com/grafana/o11y-bench): Open benchmark for evaluating AI agents on observability tasks in reproducible Harbor environments.
- [Dokimos](https://github.com/dokimos-dev/dokimos): Java and Kotlin LLM and agent evaluation framework with JUnit and CI integration, tool-call validation, quality metrics, and cost or latency tracking.
- [eval-guide](https://github.com/microsoft/eval-guide): Microsoft toolkit for planning agent evaluations, generating test cases, interpreting results, and triaging failures in Copilot Studio workflows.
- [NVIDIA SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator): Apache-2.0 framework for validating, security-scanning, deduplicating, and live-evaluating AI agent skills with deterministic quality gates and reproducible reports.
- [AgentEval](https://github.com/canwhite/AgentEval): Agent evaluation framework for testing tool use, task completion, and behavior across repeatable scenarios.
- [Bananalyzer](https://github.com/reworkd/bananalyzer): Open-source framework for evaluating AI agents on web tasks with reproducible test environments and result analysis.
- [Nasiko](https://github.com/Nasiko-Labs/nasiko): AI agent developer control plane for registry, deployment, routing, health monitoring, observability, and lifecycle operations.
- [Nexent](https://github.com/ModelEngine-Group/nexent): Zero-code platform for generating production-oriented AI agents with governed tools, skills, memory, orchestration, feedback loops, and control planes.
- [numbat](https://github.com/perplexityai/numbat): Local endpoint visibility for AI agent activity with hook-based monitoring, CEL detections, optional pre-action blocking, and forensic reconstruction.
- [continuous-eval](https://github.com/relari-ai/continuous-eval): Open-source data-driven evaluation framework for LLM-powered applications, covering retrieval, generation, and end-to-end pipeline quality metrics.
- [UQLM](https://github.com/cvs-health/uqlm): Apache-2.0 Python package for uncertainty quantification in LLMs, detecting hallucinations and low-confidence outputs in production agent workflows.
- [APIPark](https://github.com/APIParkLab/APIPark): Cloud-native AI and API gateway for unified LLM provider management, request routing, load balancing, multi-model failover, usage analytics, and API governance.
- [Universal LLM API Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy): Self-hosted OpenAI- and Anthropic-compatible proxy with multi-provider translation, intelligent load balancing, key rotation, failover, and usage controls.
- [GPT-Load](https://github.com/tbphp/gpt-load): Self-hosted AI gateway for consolidating multi-channel credentials behind one endpoint, with scheduling, failover, request logs, and usage accounting.
- [opencodex](https://github.com/lidge-jun/opencodex): MIT-licensed universal provider proxy that points Codex CLI, Codex App/SDK, and Claude Code at any LLM provider or local Ollama model, centralizing credentials, routing, and failover for coding-agent traffic.
- [LeanCTX](https://github.com/yvgude/lean-ctx): Apache-2.0 context gateway for AI systems that controls which context an agent can see and exposes context-selection policies plus the evidence behind each decision, instead of leaving prompt assembly implicit.
- [SaaS-Bench](https://github.com/UniPat-AI/SaaS-Bench): Apache-2.0 benchmark for evaluating computer-use agents on realistic, locally deployable SaaS workflows with state-based task verification.
- [Inspect Sandboxing Toolkit](https://github.com/UKGovernmentBEIS/aisi-sandboxing): Open-source toolkit for safely running agentic evaluations in isolated Docker, Kubernetes, or Proxmox environments with guidance on tooling, host, and network isolation.
- [Any Agent](https://github.com/mozilla-ai/any-agent): Apache-2.0 framework providing a single interface to use and evaluate different agent frameworks across standardized benchmarks.
- [ClawBench](https://github.com/TIGER-AI-Lab/ClawBench): Apache-2.0 benchmark for evaluating browser AI agents on everyday real-world tasks with reproducible evaluation workflows.
- [AgentLens (agentkitai)](https://github.com/agentkitai/agentlens): MIT-licensed, MCP-native observability and audit-trail platform for AI agents, with tamper-evident event logging and a real-time dashboard.
- [EvalForge](https://github.com/jsdhwfmax/EvalForge): MIT-licensed evaluation-evidence and policy-gate toolkit for RAG applications and AI assistants, exporting portable JSON, JUnit, and SARIF reports for CI regression checks.
- [Every Eval Ever](https://github.com/evaleval/every_eval_ever): MIT-licensed shared schema, validation, and converter ecosystem for storing comparable, reproducible AI evaluation results from Inspect AI, HELM, lm-evaluation-harness, and local runs.
- [Tracely](https://github.com/Jwuthri/Tracely-ai): Trace-native CI/CD for AI agents that turns production failures into hermetic regression cases, replays them in CI, and blocks regressions without model spend.
- [agenttrail](https://github.com/sodiumsun/agenttrail): Local-first observability for coding agents that turns filesystem activity, plans, and supported agent events into live project and task views without running the agents itself.
- [LMMs-Eval](https://github.com/EvolvingLMMs-Lab/lmms-eval): Unified multimodal evaluation toolkit covering 100+ text, image, video, and audio benchmark tasks, with reproducible pipelines and async serving for large-scale model evaluation.
- [LiveBench](https://github.com/LiveBench/LiveBench): Contamination-free LLM benchmark with frequently refreshed questions, objective ground-truth scoring, and no LLM-as-judge, giving operators a signal less likely to be gamed by training-data leakage.
- [ThinkWatch](https://github.com/ThinkWatchProject/ThinkWatch): Self-hosted AI API and MCP gateway for organizations, with SSO and RBAC, per-user identity for MCP tool calls, PII redaction, budgets, rate limits, and audit logs.
- [agentevals](https://github.com/agentevals-dev/agentevals): Apache-2.0 evaluation framework that scores agent behavior directly from existing OpenTelemetry traces (Jaeger JSON or native OTLP), so graders can be re-run over recorded runs without replaying expensive LLM calls.

- [OpenTelemetry GenAI Semantic Conventions](https://github.com/open-telemetry/semantic-conventions-genai): Official OpenTelemetry conventions for GenAI spans, metrics, and events, covering GenAI clients, MCP, and provider-specific attributes so LLM and agent telemetry stays portable across backends.

## AI Serving and Inference Operations

Tools for deploying, scaling, routing, and operating AI model inference workloads in production.

**Selection guidance:** Separate the serving engine from the control plane: choose engines for throughput, latency, batching, and hardware support; choose operators and gateways for rollout safety, routing, quotas, autoscaling, and telemetry. Prefer projects with reproducible benchmarks and an explicit upgrade or rollback path.

**Rollout gate:** Before shifting production traffic, record a baseline for throughput, tail latency, error rate, GPU utilization, and cost per request; canary model and runtime changes with representative prompts; and keep the previous artifact and routing policy ready for rollback. A faster token/sec number is not a release if the p99 or failure recovery got worse.

- [GenAI Factory](https://github.com/GoogleCloudPlatform/genai-factory): Production-oriented blueprints for deploying generative AI infrastructure on Google Cloud with infrastructure as code and security best practices.
- [GenAI on EKS Starter Kit](https://github.com/aws-samples/sample-genai-on-eks-starter-kit): Kubernetes deployment blueprint combining an AI gateway, LLM serving, vector databases, embedding models, and observability on Amazon EKS.
- [Ray Serve](https://github.com/ray-project/ray): Scalable model serving library in Ray for building distributed online inference APIs and LLM serving workloads.
- [KubeTorch](https://github.com/run-house/kubetorch): Python-native Kubernetes control layer for distributing and running AI workloads across cluster resources.
- [ModelPlane](https://github.com/modelplaneai/modelplane): Open-source control plane for deploying, routing, and operating AI inference workloads.
- [Polyaxon](https://github.com/polyaxon/polyaxon): Open-source AI infrastructure and orchestration platform for managing reproducible ML and LLM workloads across development and production.
- [MLRun](https://github.com/mlrun/mlrun): Apache-2.0 MLOps platform that turns code into serverless functions and pipelines, adding a feature store, model serving, and production monitoring on Kubernetes.
- [Triton Inference Server](https://github.com/triton-inference-server/server): Optimized inference server for deploying AI models across GPUs, CPUs, and cloud or edge environments.
- [KServe](https://github.com/kserve/kserve): Kubernetes-native platform for standardized, scalable generative and predictive AI inference serving.
- [Seldon Core](https://github.com/seldonio/seldon-core): MLOps framework for packaging, deploying, monitoring, and managing thousands of production ML models on Kubernetes.
- [LitServe](https://github.com/Lightning-AI/LitServe): Minimal Python framework for building custom AI inference servers with explicit control over batching, request logic, and scaling.
- [AIBrix](https://github.com/vllm-project/aibrix): Cloud-native infrastructure components for cost-efficient, scalable GenAI and LLM inference operations.
- [Dynamo](https://github.com/ai-dynamo/dynamo): Distributed inference serving framework for datacenter-scale LLM and generative AI workloads with Kubernetes-oriented routing and scaling.
- [dstack](https://github.com/dstackai/dstack): Vendor-agnostic control plane for provisioning GPUs and orchestrating training, inference, and agent workloads across clouds, Kubernetes, and bare metal.
- [llm-d](https://github.com/llm-d/llm-d): Kubernetes-native distributed inference stack for high-performance LLM serving with intelligent routing on modern accelerators.
- [GPUd](https://github.com/leptonai/gpud): GPU monitoring and diagnostics tool that automates health checks and issue identification for AI infrastructure.
- [KubeAI](https://github.com/kubeai-project/kubeai): Kubernetes-native inference operator for deploying and scaling LLMs, VLMs, embeddings, rerankers, and speech-to-text models with OpenAI-compatible APIs.
- [Kthena](https://github.com/volcano-sh/kthena): Kubernetes-native AI serving platform for scalable model serving and production inference operations.
- [SkyPilot](https://github.com/skypilot-org/skypilot): Multi-cloud and Kubernetes control plane for running, scaling, and managing AI workloads across heterogeneous GPU infrastructure.
- [GPUStack](https://github.com/gpustack/gpustack): GPU cluster manager for high-performance AI model serving with vLLM and SGLang, plus on-demand GPU instances.
- [KubeRay](https://github.com/ray-project/kuberay): Kubernetes operator and toolkit for deploying and managing Ray clusters and distributed AI workloads.
- [SGLang](https://github.com/sgl-project/sglang): High-performance serving framework for large language models and multimodal models with efficient attention and structured outputs.
- [vLLM](https://github.com/vllm-project/vllm): High-throughput and memory-efficient inference and serving engine for LLMs with continuous batching and quantization.
- [GuideLLM](https://github.com/vllm-project/guidellm): Benchmarking tool for evaluating LLM deployments with real-world latency, throughput, and performance measurements.
- [Ollama](https://github.com/ollama/ollama): Local-first LLM runner for getting started quickly with models locally, on edge, or in development environments.
- [llama.cpp](https://github.com/ggml-org/llama.cpp): High-performance C/C++ LLM inference engine with quantization, powering many local and server-side AI backends.
- [LocalAI](https://github.com/mudler/LocalAI): Self-hosted, OpenAI-compatible local AI API for running LLMs, image generation, and audio models with container-based deployment.
- [LoRAX](https://github.com/predibase/lorax): Multi-LoRA inference server for hosting thousands of fine-tuned LLMs on shared base model infrastructure.
- [NVIDIA GPU Operator](https://github.com/NVIDIA/gpu-operator): Kubernetes operator for automating NVIDIA GPU driver installation, configuration, and lifecycle management.
- [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit): Build and run GPU-accelerated containers with NVIDIA CUDA support in Docker and Kubernetes environments.
- [Volcano](https://github.com/volcano-sh/volcano): CNCF batch scheduling system for AI/ML, big data, and HPC workloads with gang scheduling, queue management, and fair-share policies.
- [KAI Scheduler](https://github.com/kai-scheduler/KAI-Scheduler): Apache-2.0 Kubernetes-native scheduler for AI workloads that combines gang scheduling, queue quotas, fair-share policies, and dynamic GPU sharing so training and inference jobs can co-exist on the same cluster.
- [Kubeflow Trainer](https://github.com/kubeflow/trainer): Kubernetes-native operator for distributed AI/ML model training and LLM fine-tuning with PyTorch, JAX, and MPI support.
- [Kubeflow Pipelines](https://github.com/kubeflow/pipelines): Kubernetes-native MLOps pipeline platform for authoring, scheduling, and tracking reproducible ML and LLM workflows with per-step artifacts and lineage.
- [OpenLLM](https://github.com/bentoml/OpenLLM): Run any open-source LLM as an OpenAI-compatible API endpoint with built-in chat UI, model catalog, and cloud deployment workflows.
- [Oumi](https://github.com/oumi-ai/oumi): Open-source platform for fine-tuning, evaluating, and deploying any open-source LLM or VLM with production-ready training and deployment workflows.
- [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM): NVIDIA's official LLM inference optimization framework with state-of-the-art GPU optimizations and efficient runtime orchestration for production deployments.
- [Text Generation Inference](https://github.com/huggingface/text-generation-inference): HuggingFace's production-grade inference server for LLMs with tensor parallelism, continuous batching, and quantization support. (Archived upstream.)
- [Text Embeddings Inference](https://github.com/huggingface/text-embeddings-inference): Blazing-fast inference server for text embedding and reranking models with production-ready performance.
- [OpenVINO Model Server](https://github.com/openvinotoolkit/model_server): Scalable inference server for OpenVINO-optimized models, exposing production-friendly APIs for deploying AI models.
- [Axolotl](https://github.com/axolotl-ai-cloud/axolotl): Open-source LLM fine-tuning framework with support for LoRA, QLoRA, and full-parameter training across popular model architectures.
- [LLaMA-Factory](https://github.com/hiyouga/LlamaFactory): Unified framework for LLM fine-tuning with 100+ models and 50+ methods, supporting LoRA, QLoRA, and full-parameter training with web UI workflows.
- [Unsloth](https://github.com/unslothai/unsloth): Open-source library for 2-5x faster LLM fine-tuning with significant memory reduction, supporting major model architectures and training workflows.
- [HAMi](https://github.com/Project-HAMi/HAMi): Heterogeneous GPU sharing middleware for Kubernetes with device memory isolation and multi-tenant scheduling.
- [Tensor Fusion](https://github.com/NexusGPU/tensor-fusion): GPU virtualization and pooling layer for Kubernetes that slices and shares accelerators across workloads so training and inference jobs stop reserving whole cards.
- [MatrixHub](https://github.com/matrixhub-ai/matrixhub): Self-hosted, Hugging Face-compatible model registry for enterprise inference with pull-once caching, air-gapped delivery, tag locking, and multi-region sync for vLLM and SGLang clusters.
- [AISIX](https://github.com/api7/aisix): Rust-native AI gateway that puts one OpenAI-compatible API in front of OpenAI, Anthropic, Gemini, and Bedrock with routing, guardrails, caching, rate limits, and observability.
- [AIHelms](https://github.com/beizhu-1209/AIHelms): Enterprise AI resource governance platform combining a unified AI gateway, token quota scheduling, MCP tool and skill registry, cost attribution, and audit reporting.
- [Llama Deploy](https://github.com/run-llama/llama_deploy): Production deployment framework for LlamaIndex agentic workflows with asynchronous task orchestration and service management.
- [Semantic Router](https://github.com/vllm-project/semantic-router): System-level intelligent runtime for Mixture-of-Models, enabling dynamic model selection and intelligent routing across edge, data center, and cloud environments.
- [FastChat](https://github.com/lm-sys/FastChat): Open platform for training, serving, and evaluating LLMs. Release repo for Vicuna and Chatbot Arena.
- [text-generation-webui](https://github.com/oobabooga/textgen): Open-source desktop app for running LLMs locally with text, vision, tool-calling, and OpenAI/Anthropic-compatible API support.
- [DS4](https://github.com/antirez/ds4): High-performance local inference engine for DeepSeek 4 Flash and PRO, optimized for Metal, CUDA, and ROCm platforms.
- [RouteLLM](https://github.com/lm-sys/RouteLLM): Framework for serving and evaluating LLM routers that direct requests to cheaper models while preserving response quality.
- [Rig](https://github.com/0xPlaygrounds/rig): Rust framework for building modular, scalable LLM applications with composable components and provider integrations.
- [Agent Lightning](https://github.com/microsoft/agent-lightning): Framework for training and optimizing AI agents by connecting agent execution with reinforcement learning and other training methods.
- [verl](https://github.com/verl-project/verl): Flexible and efficient reinforcement-learning framework for post-training large language models and optimizing reasoning or agent workloads.
- [aikit](https://github.com/kaito-project/aikit): Kubernetes-native toolkit for fine-tuning, building, and deploying open-source LLMs with buildkit-based image construction and GPU-accelerated inference.
- [NVIDIA NVCF](https://github.com/NVIDIA/nvcf): Platform for deploying and routing GPU-accelerated inference, streaming, and batch workloads at scale.
- [Grove](https://github.com/ai-dynamo/grove): Kubernetes enhancements for topology-aware gang scheduling and autoscaling of distributed AI workloads.
- [llm-d Router](https://github.com/llm-d/llm-d-router): Kubernetes-oriented intelligent inference router with load- and prefix-cache-aware routing, request prioritization, and Gateway API integration.
- [Cube Studio](https://github.com/data-infra/cube-studio): Cloud-native AI platform for Kubernetes with MLOps workflows, distributed training, GPU virtualization, inference serving, and LLMOps capabilities.
- [InferenceX](https://github.com/SemiAnalysisAI/InferenceX): Open-source continuous inference benchmark platform for comparing LLM serving performance across hardware including GB200, MI355X, B200, and Ascend.
- [LMDeploy](https://github.com/InternLM/lmdeploy): Toolkit for compressing, deploying, and serving LLMs with high-throughput inference, quantization, and long-context support.
- [Xinference](https://github.com/xorbitsai/inference): Unified production inference API for running open-source LLM, speech, and multimodal models on cloud, on-prem, or laptops.
- [vLLM Production Stack](https://github.com/vllm-project/production-stack): vLLM's Kubernetes-native reference stack for cluster-wide deployment, routing, and observability of LLM serving.
- [Gateway API Inference Extension](https://github.com/kubernetes-sigs/gateway-api-inference-extension): Kubernetes SIG project that extends Gateway API with inference-aware routing for model-serving backends.
- [LeaderWorkerSet](https://github.com/kubernetes-sigs/lws): Kubernetes API for deploying a group of pods as a single replication unit, used to run multi-node inference and training workloads reliably.
- [KitOps](https://github.com/kitops-ml/kitops): CNCF tool that packages and versions AI/ML models, datasets, code, and configuration as OCI artifacts for reproducible model delivery.
- [FlashInfer](https://github.com/flashinfer-ai/flashinfer): Attention and GEMM kernel library for LLM serving, used by engines such as vLLM and SGLang to cut inference latency.
- [LMCache](https://github.com/LMCache/LMCache): KV cache management layer that stores and reuses LLM key-value cache across CPU memory, local disk, and peer instances to cut prefill cost and time to first token for multi-turn, RAG, and agentic serving.
- [Mooncake](https://github.com/kvcache-ai/Mooncake): KVCache-centric serving platform behind Moonshot AI's Kimi that disaggregates prefill and decode and pools KV cache across CPU, DRAM, SSD, and peer instances to raise GPU utilization and serving throughput.
- [DeepSpeed](https://github.com/deepspeedai/DeepSpeed): Deep learning optimization library providing ZeRO memory partitioning, mixed precision, and CPU or NVMe offloading so large models can be trained and served with far less GPU memory.
- [vLLM-Omni](https://github.com/vllm-project/vllm-omni): Omni-modality serving framework from the vLLM project that extends the same stack to text, image, audio, video, and action models, including diffusion and TTS pipelines, behind an OpenAI-compatible API.
- [NVIDIA DCGM Exporter](https://github.com/NVIDIA/dcgm-exporter): Prometheus exporter for NVIDIA GPU metrics built on DCGM, exposing utilization, profiler counters, and health signals for monitoring AI serving and training fleets.
- [oMLX](https://github.com/jundot/omlx): LLM inference server for Apple Silicon with continuous batching, tiered KV caching, and an OpenAI-compatible API managed from the macOS menu bar.
- [nvtop](https://github.com/Syllo/nvtop): GPU and accelerator process monitor for NVIDIA, AMD, Intel, Apple, Huawei, and Qualcomm devices, showing utilization, memory, and per-process usage in real time.
- [Microsoft PAI](https://github.com/microsoft/pai): Resource scheduling and cluster management platform for shared AI training and inference clusters, covering GPU allocation, quotas, and job lifecycle operations.
- [RamaLama](https://github.com/containers/ramalama): Container-native tool that pulls, quantizes, and serves AI models from OCI registries, so teams can run local or self-hosted inference with standard container workflows.
- [LightLLM](https://github.com/ModelTC/LightLLM): Python inference and serving framework for LLMs with token-level memory management, built for high-throughput and low-latency online serving.
- [FastDeploy](https://github.com/PaddlePaddle/FastDeploy): High-performance inference and deployment toolkit for LLMs and VLMs in the PaddlePaddle ecosystem, with multi-hardware and multi-backend support.
- [vLLM Ascend](https://github.com/vllm-project/vllm-ascend): Community-maintained hardware plugin that runs the vLLM serving stack on Huawei Ascend NPUs, so Ascend clusters keep the same OpenAI-compatible API, quantization options, and rollout path used for GPU fleets.
- [Chitu](https://github.com/thu-pacman/chitu): High-performance LLM inference framework with native support for Huawei Ascend, NVIDIA, MetaX, Moore Threads, and Hygon accelerators, including prefill-decode disaggregation and multi-node deployment launched from a single binary.
- [GPTCache](https://github.com/zilliztech/GPTCache): Semantic cache library for LLM queries that stores prompt-response pairs in vector storage and serves semantically similar requests from cache, cutting API cost and latency on high-repetition traffic.
- [Kubeflow Katib](https://github.com/kubeflow/katib): Kubernetes-native AutoML system for hyperparameter tuning and neural architecture search, so model tuning runs as reproducible cluster jobs instead of ad-hoc scripts on a shared GPU box.
- [Kubeflow Hub Model Registry](https://github.com/kubeflow/hub): Metadata service that indexes models, versions, and artifacts across the MLOps lifecycle, giving serving platforms a catalog to promote, compare, and audit model releases. (Alpha upstream.)
- [RTP-LLM](https://github.com/alibaba/rtp-llm): LLM inference acceleration engine from Alibaba's Foundation Model Inference Team, serving Taobao, Tmall, Cainiao, Amap, and other internal business units, with prefill-decode separation and multi-hardware backends.
- [xLLM](https://github.com/xLLM-AI/xllm): High-performance inference engine for LLM, VLM, DiT, and recommendation models across diverse AI accelerators, donated to the OpenAtom Foundation and shipping day-0 support for newly released open models.
- [InfiniStore](https://github.com/bytedance/InfiniStore): High-performance KV store for LLM inference clusters that transfers and reuses KV cache between prefill and decode nodes, integrated with vLLM through LMCache and usable as a standalone cross-node cache pool.
- [Truss](https://github.com/basetenlabs/truss): CLI that packages a model's serving logic, dependencies, and GPU configuration into a reproducible container, so the same artifact runs with vLLM, SGLang, TensorRT-LLM, or plain PyTorch in development and production.
- [OptiLLM](https://github.com/algorithmicsuperintelligence/optillm): OpenAI-compatible optimizing inference proxy that applies 20+ inference-time techniques such as chain-of-thought, mixture-of-agents, and best-of-N, so teams can raise reasoning accuracy without retraining or changing application code.
- [kvcached](https://github.com/ovg-project/kvcached): KV cache daemon that brings OS-style virtual memory to LLM serving, decoupling GPU virtual addressing from physical allocation so shared GPUs scale accelerator cache elastically with live load across vLLM and SGLang.
- [MLPerf Inference](https://github.com/mlcommons/inference): Reference implementations of the MLPerf inference benchmarks, providing reproducible, industry-standard latency and throughput measurements for comparing serving engines, hardware, and quantization choices.
- [Hugging Face Inference Benchmarker](https://github.com/huggingface/inference-benchmarker): Apache-2.0 benchmarking tool for LLM inference servers that runs standardized throughput, latency, and concurrency tests against OpenAI-compatible endpoints for cross-engine comparisons and regression gates.
- [SIE](https://github.com/superlinked/sie): Self-hosted inference server and cluster for the open models agents depend on, serving embeddings, rerankers, SPLADE, and structured-output models behind one OpenAI-compatible API with on-demand model loading, LRU eviction, and shipped Helm, KEDA, and Grafana deployment assets.
- [LLMLingua](https://github.com/microsoft/LLMLingua): Prompt-compression toolkit that removes non-essential tokens and compresses KV cache before inference, cutting prompt tokens and serving cost by up to 20x with minimal accuracy loss, with integrations for LangChain, LlamaIndex, and Prompt flow.
- [ServerlessLLM](https://github.com/ServerlessLLM/ServerlessLLM): Serverless LLM serving system that loads model checkpoints 6-10x faster than SafeTensors and migrates live inference sessions between GPUs, so a shared accelerator can host many models without paying cold-start latency on every scale-up.
- [Parallax](https://github.com/GradientHQ/parallax): Decentralized inference engine that pipeline-shards one model across heterogeneous, physically distributed nodes over P2P transport with scheduler-driven routing, letting a platform team assemble a private inference cluster from the GPUs it already owns instead of renting uniform accelerators.

- [NVIDIA Device Plugin for Kubernetes](https://github.com/NVIDIA/k8s-device-plugin): Kubernetes device plugin that advertises NVIDIA GPUs to the kubelet so GPU workloads schedule normally, with MIG, time-slicing, and CDI support for sharing accelerators across AI workloads.
- [KTransformers](https://github.com/kvcache-ai/ktransformers): Heterogeneous CPU+GPU inference and fine-tuning framework for MoE models that keeps attention on the GPU and expert weights in CPU memory, so large sparse models can be served and tuned on hardware a team already owns instead of a full GPU node per replica.
- [MLC-LLM](https://github.com/mlc-ai/mlc-llm): Compilation-based universal LLM deployment engine that lowers one model definition to CUDA, ROCm, Metal, Vulkan, WebGPU, iOS, and Android runtimes, so edge, desktop, and server targets share a validated engine instead of maintaining separate serving stacks.

## AIOps

- [Netdata](https://github.com/netdata/netdata): Distributed real-time monitoring for infrastructure metrics, visualization, and alerting.
- [Apache HertzBeat](https://github.com/apache/hertzbeat): Apache real-time observability and monitoring system with agentless collection, alerting, status pages, and AI-assisted operations.
- [PostHog](https://github.com/PostHog/posthog): Open-source product analytics platform for user behavior tracking and product metrics.
- [SREWorks](https://github.com/alibaba/SREWorks): Cloud-native DataOps and AIOps platform for operating Kubernetes-based applications and infrastructure.
- [OpenSRE](https://github.com/Tracer-Cloud/opensre): Open-source toolkit for building AI SRE agents with observability, incident management, alerting, and automated root-cause analysis.
- [Keep](https://github.com/keephq/keep): Open-source AIOps and alert management platform for correlating, enriching, and automating incident response across monitoring tools.
- [AiSOC](https://github.com/beenuar/AiSOC): Open-source AI-powered Security Operations Center for alert fusion, agent-assisted triage, purple-team drills, and MITRE ATT&CK investigation workflows.
- [APO](https://github.com/CloudDetail/apo): AI-powered observability platform combining OpenTelemetry, eBPF, and LLM agentic workflows for automated root-cause analysis and intelligent troubleshooting.
- [HolmesGPT](https://github.com/HolmesGPT/holmesgpt): CNCF Sandbox SRE agent that investigates alerts and operational incidents using cluster context, runbooks, and observability data.
- [K8sGPT](https://github.com/k8sgpt-ai/k8sgpt): Kubernetes troubleshooting tool that applies codified SRE analyzers to diagnose and triage cluster issues with optional AI backends.
- [kagent](https://github.com/kagent-dev/kagent): Kubernetes-native framework for building, deploying, and managing AI agents with MCP tools and OpenTelemetry tracing for infrastructure operations.
- [Metaflow](https://github.com/Netflix/metaflow): Human-centric framework for developing, versioning, scaling, and deploying production AI/ML systems from prototypes to reliable workflows.
- [Chaterm](https://github.com/chaterm/Chaterm): Open-source AI terminal for cloud and infrastructure management, enabling natural-language deployment, troubleshooting, and automation across SSH, Kubernetes, and cloud services.
- [Versus Incident](https://github.com/VersusControl/versus-incident): Self-hosted AI SRE agent that learns normal system behavior and routes novel or unexpected incidents to chat and on-call platforms.
- [Flawless](https://github.com/William-Lu-stack/Flawless): AI-native SRE control plane for Kubernetes and cloud infrastructure, connecting evidence, human approval, controlled remediation, rollback, and recovery verification in an auditable loop.
- [Nudgebee](https://github.com/nudgebee/nudgebee): Open-source SRE copilot for Kubernetes and major clouds, combining observability, FinOps, runbook automation, incident response, and ChatOps workflows.
- [AIOpsLab](https://github.com/microsoft/AIOpsLab): Holistic framework for designing, developing, and evaluating autonomous AIOps agents against reproducible operations scenarios.
- [SREGym](https://github.com/SREGym/SREGym): Benchmark and experimentation framework for evaluating whether AI agents can diagnose and resolve production incidents in reproducible SRE environments.
- [ANOLISA](https://github.com/agentic-os-org/ANOLISA): Agentic OS with runtime, security, observability, and tokenless response compression for lowering token usage and cost in production AI agent deployments.
- [OpenOcta](https://github.com/openocta/openocta): Desktop IT ops agent for Windows and macOS that wires monitoring, logs, cloud platforms, databases, and scripts into an auto-inspection, alert-analysis, and remediation loop driven by natural language.
- [OpenDerisk](https://github.com/derisk-ai/OpenDerisk): AI-native risk intelligence system for application operations that performs deep root-cause analysis over logs, traces, and code, and exposes a visualized evidence chain behind every diagnosis.
- [StackStorm](https://github.com/StackStorm/st2): Event-driven automation platform that turns alerts into versioned, auditable actions, combining a rules engine, workflows, 160+ integration packs, and ChatOps for auto-remediation and incident response.
- [Valqore](https://github.com/valqore/valqore): Safety-first guardrail engine for AI-driven cloud and Kubernetes operations that applies policy checks, change gating, and cost or carbon signals so autonomous operations actions stay within approved boundaries.

## AI Infrastructure

Infrastructure for web crawling, AI-ready extraction, search intelligence, and RAG data acquisition workflows.

**Selection guidance:** Separate acquisition from retrieval: crawlers and parsers should expose provenance, incremental refresh, rate-limit controls, and failure visibility; vector or hybrid search layers should make indexing, filtering, access control, and relevance evaluation explicit. Prefer components that can be operated independently rather than opaque end-to-end demos.

- [MinerU](https://github.com/opendatalab/MinerU): High-accuracy document parsing engine that converts PDFs, Office files, and images into structured Markdown or JSON for LLM, RAG, and agent workflows.
- [MetaMCP](https://github.com/metatool-ai/metamcp): Self-hosted MCP aggregator, orchestrator, middleware, and gateway for composing and governing tool servers.
- [Firecrawl](https://github.com/firecrawl/firecrawl): Web search, scraping, crawling, and extraction API that turns web data into LLM-ready Markdown and structured outputs.
- [anydoc](https://github.com/firecrawl/anydoc): Fast Rust library with Node.js, Python, and WebAssembly bindings for converting office documents, PDFs, and other files into clean, LLM-ready Markdown.
- [Crawl4AI](https://github.com/unclecode/crawl4ai): Open-source LLM-friendly web crawler and scraper for building RAG, agent, and web data pipelines.
- [Jina Reader](https://github.com/jina-ai/reader): URL-to-LLM converter that turns any web page into clean, LLM-friendly Markdown with a simple prefix.
- [Open SEO](https://github.com/every-app/open-seo): Open-source SEO and search intelligence platform for keyword research, site audits, backlink analysis, and Google Search Console MCP workflows.
- [Milvus](https://github.com/milvus-io/milvus): Cloud-native vector database for billion-scale similarity search and unstructured data retrieval in RAG and AI pipelines.
- [Qdrant](https://github.com/qdrant/qdrant): High-performance vector search engine with rich filtering, payload storage, and production-ready scalability for AI applications.
- [Chroma](https://github.com/chroma-core/chroma): Embedding-first vector database for building LLM applications with simple local development and client-server deployment.
- [Unstructured](https://github.com/Unstructured-IO/unstructured): Open-source ETL library for converting PDFs, HTML, Word, and other documents into clean structured data for RAG and LLM pipelines.
- [MarkItDown](https://github.com/microsoft/markitdown): Microsoft's open-source tool for converting files and Office documents to Markdown for LLM and RAG data pipelines.
- [Docling](https://github.com/docling-project/docling): IBM's open-source document understanding toolkit for converting PDFs, DOCX, PPTX, images, and HTML into LLM-ready structured formats at scale.
- [Chonkie](https://github.com/feyninc/chonkie): Lightweight ingestion and chunking library with token, sentence, semantic, recursive, and code-aware chunkers so RAG preprocessing stays reproducible and benchmarkable.
- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR): Open-source OCR toolkit for converting PDFs and images into structured data for multilingual AI and RAG pipelines.
- [Pathway LLM App](https://github.com/pathwaycom/llm-app): Ready-to-run templates for production RAG, AI pipelines, and enterprise search with live data connectors and Docker-friendly deployment.
- [Cognita](https://github.com/truefoundry/cognita): Open-source modular RAG framework for building production applications with configurable data ingestion, retrieval, and serving components. (Archived upstream.)
- [SuperDuper](https://github.com/superduper-io/superduper): Open-source framework for building custom AI applications and agents directly on existing data stores, with integrated model, data, and deployment workflows.
- [Weaviate](https://github.com/weaviate/weaviate): Open-source vector database combining vector search with structured filtering and generative AI integrations.
- [pgvector](https://github.com/pgvector/pgvector): Open-source vector similarity search extension for PostgreSQL, widely used for RAG and AI embedding storage.
- [LanceDB](https://github.com/lancedb/lancedb): Developer-friendly embedded vector database for multimodal AI search with serverless architecture and zero-copy retrieval.
- [zvec](https://github.com/alibaba/zvec): Lightweight, lightning-fast in-process vector database from Alibaba for embedded AI search and retrieval, Apache-2.0.
- [LEANN](https://github.com/StarTrail-org/LEANN): Graph-based vector index for on-device RAG that cuts index storage by up to 97% while keeping retrieval fast and private.
- [Manticore Search](https://github.com/manticoresoftware/manticoresearch): Open-source search database for full-text, vector, and hybrid search with real-time indexing and SQL.
- [USearch](https://github.com/unum-cloud/USearch): Fast, compact open-source vector search and clustering engine with bindings for multiple languages.
- [txtai](https://github.com/neuml/txtai): All-in-one AI framework for semantic search, LLM orchestration, and language model workflows with embeddings and pipelines.
- [Feast](https://github.com/feast-dev/feast): Open-source feature store for AI/ML that serves features consistently for model training and online inference.
- [Instructor](https://github.com/567-labs/instructor): Structured outputs for LLMs with Pydantic validation, automatic retries, and provider-agnostic API.
- [pgai](https://github.com/timescale/pgai): Open-source suite for building RAG, semantic search, and AI applications directly on PostgreSQL with vector and AI tooling. (Archived upstream.)
- [Browser Use](https://github.com/browser-use/browser-use): Open-source web automation toolkit that enables AI agents to browse websites, extract data, and automate online tasks at scale.
- [Agent-Reach](https://github.com/Panniantong/Agent-Reach): Give your AI agent eyes to see the entire internet — read and search Twitter, Reddit, YouTube, GitHub, Bilibili, and more via one CLI with zero API fees.
- [Steel Browser](https://github.com/steel-dev/steel-browser): Open-source headless browser sandbox for AI agents and applications, providing production-ready web automation infrastructure.
- [E2B](https://github.com/e2b-dev/E2B): Open-source secure cloud sandbox for running AI agent code with isolated environments, file system access, and real-world tool execution.
- [headroom](https://github.com/headroomlabs-ai/headroom): Compress tool outputs, logs, files, and RAG chunks before reaching the LLM — 60-95% fewer tokens, same answers.
- [fastmcp](https://github.com/PrefectHQ/fastmcp): The fast, Pythonic way to build MCP servers and clients for AI agent tool infrastructure.
- [Stagehand](https://github.com/browserbase/stagehand): Open-source SDK for building browser agents with AI-powered web automation, extraction, and interaction at scale.
- [FlagEmbedding](https://github.com/FlagOpen/FlagEmbedding): Open-source toolkit for embedding and reranking models (BGE series) powering retrieval-augmented LLM applications.
- [Open WebUI](https://github.com/open-webui/open-webui): Self-hosted LLM chat interface with RAG, web search, tool integration, model management, and multi-user deployment for internal AI platforms.
- [InsForge](https://github.com/InsForge/InsForge): Open-source backend platform for agentic coding that provides database, authentication, storage, compute, hosting, and an AI gateway for full-stack applications.
- [Label Studio](https://github.com/HumanSignal/label-studio): Open-source data labeling platform for images, text, audio, video, and time series in ML and LLM training workflows.
- [Argilla](https://github.com/argilla-io/argilla): Open-source collaboration platform for building, curating, and versioning high-quality datasets for LLM fine-tuning and evaluation.
- [NVIDIA NeMo Curator](https://github.com/NVIDIA-NeMo/Curator): GPU-accelerated data curation toolkit for LLM pipelines, covering deduplication, quality filtering, and dataset preparation.
- [FiftyOne](https://github.com/voxel51/fiftyone): Open-source dataset curation and quality platform for visual and multimodal AI, providing embedding-based exploration, annotation review, and label-error detection before training or evaluation.
- [llmware](https://github.com/llmware-ai/llmware): Unified open-source framework for enterprise LLM applications with integrated RAG, parsing, embedding, and vector database orchestration.
- [AgentGateway](https://github.com/agentgateway/agentgateway): Next-generation agentic proxy for AI agents and MCP servers, providing secure access, routing, and policy management for agent tool integrations.
- [Zilla](https://github.com/aklivity/zilla): Lightweight, multi-protocol gateway for event-driven applications and AI agents, governing Kafka, MQTT, APIs, and MCP with shared routing, security, schema, and observability.
- [Lunar.dev](https://github.com/TheLunarCompany/lunar): Open-source gateway for governing and optimizing third-party API and MCP traffic from applications and AI agents with visibility, policy enforcement, and traffic shaping.
- [Jarvis Registry](https://github.com/ascending-llc/jarvis-registry): Enterprise MCP and A2A gateway with identity-aware access control, tool discovery, OpenTelemetry tracing, and Prometheus metrics.
- [Maxun](https://github.com/getmaxun/maxun): Open-source no-code platform for web scraping, crawling, search, and AI data extraction, turning websites into structured APIs for RAG and AI pipelines.
- [GPT-Researcher](https://github.com/assafelovic/gpt-researcher): Autonomous AI agent for comprehensive web research, report generation, and knowledge synthesis using multi-source data retrieval.
- [rtk](https://github.com/rtk-ai/rtk): CLI proxy that reduces LLM token consumption by 60-90% on common dev commands, lowering AI infrastructure costs in development workflows.
- [Context7](https://github.com/upstash/context7): MCP server that provides up-to-date code documentation and library references to LLMs and AI code editors at inference time.
- [Pathway](https://github.com/pathwaycom/pathway): Python ETL framework for stream processing, real-time analytics, LLM pipelines, and RAG with unified batch-and-streaming execution.
- [MindsDB](https://github.com/mindsdb/mindshub): AI database platform that connects models to data sources, enabling AI-powered queries, automations, and agent workflows.
- [Open Connector](https://github.com/oomol-lab/open-connector): Open-source auth gateway connecting 1000+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAPI.
- [MCP Use](https://github.com/mcp-use/mcp-use): Fullstack MCP framework for building MCP applications, servers, and agent tools for ChatGPT, Claude, and other AI assistants.
- [Composio](https://github.com/ComposioHQ/composio): Agent tool-integration platform with managed toolkits, tool search, authentication, context management, and sandboxed execution.
- [PageIndex](https://github.com/VectifyAI/PageIndex): Vectorless, reasoning-based document indexing system for retrieval-augmented generation over long documents.
- [Onyx](https://github.com/onyx-dot-app/onyx): Open-source AI platform for enterprise search and AI chat, combining retrieval, connectors, agent workflows, and self-hosted deployment.
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector): Developer tool with a web client and proxy for interactively testing and debugging MCP servers across supported transports.
- [MCP Router](https://github.com/mcp-router/mcp-router): Unified MCP server management application for discovering, configuring, and operating MCP servers from one interface. (Archived upstream.)
- [MCP Registry](https://github.com/modelcontextprotocol/registry): Community-driven registry service that publishes, discovers, and governs MCP servers, giving agent tool integrations a verifiable source of truth instead of copy-pasted local configuration.
- [DB-GPT](https://github.com/eosphoros-ai/DB-GPT): Open-source agentic AI data assistant for building data products, Text-to-SQL, RAG, and multi-agent workflows over private data.
- [BoxLite](https://github.com/boxlite-ai/boxlite): Daemonless micro-VM runtime for AI agents — hardware-isolated, OCI-native execution environments embeddable as a library or deployed as a server.
- [Docker MCP Gateway](https://github.com/docker/mcp-gateway): Docker CLI plugin and gateway for securely running, deploying, and managing MCP servers in local or production workflows.
- [Unla](https://github.com/AmoyLab/Unla): Lightweight MCP gateway that exposes existing MCP servers and APIs through a managed endpoint with Docker deployment and a management UI.
- [HelixDB](https://github.com/HelixDB/helix-db): Rust-built graph-vector database for knowledge graphs, AI memory, and unified access to relational, document, key-value, and vector data.
- [RocketRide](https://github.com/rocketride-org/rocketride-server): Open-source AI pipeline builder and runtime with a C++ core, extensible nodes, vector database integrations, and IDE/CLI workflows for production AI systems.
- [Golf](https://github.com/golf-mcp/golf): Production-ready MCP server framework with authentication, observability, debugging, telemetry, and runtime capabilities for deploying secure agent infrastructure.
- [Airweave](https://github.com/airweave-ai/airweave): Open-source context retrieval layer that syncs diverse data sources into searchable context for AI agents and applications. (Archived upstream.)
- [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox): Secure, fast, and extensible sandbox runtime for isolating AI agent code and tool execution.
- [Kubernetes Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox): Kubernetes API and controller for managing isolated, stateful, singleton workloads such as AI agent runtimes.
- [KARS](https://github.com/Azure/kars): Microsoft’s Kubernetes reference stack for running AI agents with hardened per-agent sandboxes, governed egress, and encrypted inter-agent communication.
- [Pullrun](https://github.com/pullrun/pullrun): AI agent sandbox runtime that boots OCI images in Firecracker microVMs, Linux containers, or Apple Silicon VMs with native MCP support.
- [AgentENV](https://github.com/kvcache-ai/AgentENV): Distributed platform for running large numbers of snapshot-backed Firecracker agent environments with fast startup, pause, fork, and E2B-compatible APIs.
- [AgentOS](https://github.com/rivet-dev/agentos): Library that gives AI agents an operating-system-like runtime in an existing backend using WebAssembly and V8 isolates.
- [Cua](https://github.com/trycua/cua): Open-source computer-use infrastructure with cross-platform drivers, fleets, and benchmarks for agent training, evaluation, and data generation.
- [Apache Doris](https://github.com/apache/doris): Real-time analytics and hybrid-search database for AI agents and operational data workloads.
- [Dormice](https://github.com/BitMiracle-AI/Dormice): Self-hosted, E2B-compatible agent sandbox runtime where sandboxes persist indefinitely and idle costs nothing.
- [Agent-Sandbox](https://github.com/agent-sandbox/agent-sandbox): Enterprise-grade sandbox platform for AI agents, supporting secure execution of untrusted LLM-generated code, browser use, and computer use.
- [OpenKruise Agents](https://github.com/openkruise/agents): Kubernetes operator and best-practice guide for rapid, cost-effective agent sandbox lifecycle management at scale.
- [ArtifactFS](https://github.com/cloudflare/artifact-fs): FUSE filesystem driver that mounts large git repos instantly with on-demand hydration, eliminating clone latency for agents, sandboxes, and containers.
- [Docker Compose for Agents](https://github.com/docker/compose-for-agents): Docker Compose examples for running open-source LLMs, tools, and agent runtimes as reproducible local or deployment workflows.
- [MCPHub](https://github.com/samanhappy/mcphub): Self-hosted MCP gateway and management platform with unified endpoints, access control, health checks, routing, logs, and hot-swappable server configuration.
- [Mirage](https://github.com/strukto-ai/mirage): Virtual terminal and filesystem sandbox for AI agents that mounts S3, Slack, Redis, and other sources under one POSIX root, with allow/ask/deny profiles and a scriptable policy engine.
- [clawk](https://github.com/clawkwork/clawk): Gives coding agents a disposable Linux VM with the repository mounted in, so guest-root tooling and network allow-lists keep the host filesystem, keychain, and credentials out of reach.
- [Containarium](https://github.com/FootprintAI/Containarium): Self-hosted agent runtime that gives each agent an SSH-reachable box with per-tenant network isolation, eBPF egress policy, GPU passthrough, and MCP-native tooling on Kubernetes and LXC.
- [OpenLake](https://github.com/openlake-project/openlake): Rust storage engine for GPU workloads that offloads KV cache and checkpoints to durable storage with million-IOPS random reads, targeting lower inference cost and less accelerator idle time.
- [VectorChord](https://github.com/supervc-stack/VectorChord): Scalable, disk-friendly vector search extension for PostgreSQL from the pgvecto.rs lineage, powering RAG and embedding retrieval directly inside Postgres.
- [Infinity](https://github.com/infiniflow/infinity): AI-native database from the InfiniFlow (RAGFlow) team that unifies dense vector, sparse vector, tensor, and full-text search over structured and unstructured data, giving RAG and search pipelines one retrieval engine instead of several glued-together stores.
- [microsandbox](https://github.com/superradcompany/microsandbox): Apache-2.0 microVM runtime and library that runs untrusted workloads such as AI agent code, plugins, CI jobs, and scrapers in fast local sandboxes with per-run isolation.
- [PixelRAG](https://github.com/StarTrail-org/PixelRAG): Pixel-native retrieval that indexes rendered page screenshots instead of parsed text, so RAG pipelines can search documents and web pages by visual layout and stop losing information to brittle HTML or PDF extraction.
- [VexDB-Lite](https://github.com/VexDB-THU/VexDB-Lite): Vector similarity search engine from Tsinghua that ships as an extension for PostgreSQL, DuckDB, and SQLite, sharing one graph index, SIMD distance dispatch, and PQ/RaBitQ quantization path across embedded, analytical, and server-side deployments.
- [sqlite-vec](https://github.com/asg017/sqlite-vec): Zero-dependency vector search extension that runs inside SQLite wherever SQLite runs, giving local RAG pipelines and agent memory brute-force k-NN ranking without operating a separate vector database service.

## LLM Knowledge

Open-source platforms for building, managing, and querying LLM-powered knowledge bases from unstructured documents.

**Selection guidance:** Treat ingestion, retrieval, evaluation, and serving as separate failure domains. Prefer projects with incremental re-indexing, source citations, connector or parser coverage, access-control boundaries, and measurable retrieval or answer-quality checks. A chatbot that cannot explain where an answer came from is a demo wearing a production badge.

**RAG release gate:** Keep ingestion, retrieval, and generation metrics separate; pin parser, embedding, and reranker versions; retain source and chunk identifiers for replay; and canary index or prompt changes against a fixed evaluation set before full rollout. If retrieval quality regresses, roll back the index or retriever first instead of compensating with a larger model.

- [Graphify](https://github.com/Graphify-Labs/graphify): Zero-server code intelligence engine that builds an explorable knowledge graph from code, documentation, schemas, configs, and PDFs for agent-assisted code understanding.
- [Agentset](https://github.com/agentset-ai/agentset): Open-source platform for building, evaluating, and shipping production-ready RAG and agentic applications with ingestion, vector indexing, citations, hosting, and developer APIs.
- [RAGFlow](https://github.com/infiniflow/ragflow): Leading open-source RAG engine that combines deep document understanding, knowledge base management, and agent capabilities for enterprise knowledge workflows.
- [FastGPT](https://github.com/labring/FastGPT): Knowledge-based LLM application platform with out-of-the-box data processing, model invocation, RAG, and visual workflow orchestration.
- [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm): Local-first document chat and agent platform that turns any document into a context-aware LLM knowledge base.
- [WeKnora](https://github.com/Tencent/WeKnora): Open-source LLM knowledge platform that turns raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki.
- [MaxKB](https://github.com/1Panel-dev/MaxKB): Open-source enterprise platform for building knowledge base agents with RAG, multi-model support, and visual workflow design.
- [GraphRAG](https://github.com/microsoft/graphrag): Microsoft's modular graph-based RAG system for extracting knowledge graphs from documents and improving retrieval quality.
- [HippoRAG](https://github.com/OSU-NLP-Group/HippoRAG): RAG framework inspired by human long-term memory that combines knowledge graphs and personalized PageRank for continuous knowledge integration.
- [Mem0](https://github.com/mem0ai/mem0): Universal memory layer for AI agents with multi-level memory, entity linking, and temporal reasoning for personalized interactions.
- [Zep](https://github.com/getzep/zep): Open-source memory layer for AI agents providing long-term recall, user facts, and knowledge graph capabilities for persistent agent memory.
- [Graphiti](https://github.com/getzep/graphiti): Open-source engine for building temporally aware, real-time knowledge graphs that give AI agents structured, continuously updated context.
- [Memori](https://github.com/MemoriLabs/Memori): LLM-agnostic memory infrastructure that turns agent execution and conversations into persistent, structured state for production systems.
- [Memvid](https://github.com/memvid/memvid): Serverless, single-file memory layer for agents that provides local-first retrieval without the operational overhead of a multi-service RAG stack.
- [AutoRAG](https://github.com/Marker-Inc-Korea/AutoRAG): Open-source framework for RAG evaluation and optimization with AutoML-style automation for pipeline tuning.
- [MemoryBench](https://github.com/supermemoryai/memorybench): Unified benchmark for evaluating conversational memory and RAG across multiple datasets.
- [MemPalace](https://github.com/MemPalace/mempalace): Open-source AI memory system with best-in-class benchmarks, providing persistent knowledge storage for AI agents and LLM applications.
- [LightRAG](https://github.com/HKUDS/LightRAG): Simple and fast RAG framework with graph-based retrieval, supporting incremental updates and efficient knowledge graph construction.
- [Kotaemon](https://github.com/Cinnamon/kotaemon): Open-source RAG-based document QA tool with multi-model support and a customizable UI for chatting with documents.
- [Quivr](https://github.com/The-Vibe-Company/quivr): Opinionated RAG platform for integrating GenAI into applications, supporting any LLM, vector store, and file type.
- [R2R](https://github.com/sciphi-ai/r2r): Production-ready AI retrieval system with agentic RAG and a RESTful API for enterprise knowledge workflows.
- [Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat): RAG and Agent application platform based on LangChain and local LLMs such as ChatGLM, Qwen, and Llama with knowledge base management.
- [Semantica](https://github.com/semantica-agi/semantica): Graph-native infrastructure for connecting context, knowledge, and accountable evidence in AI systems.
- [Cognee](https://github.com/topoteretes/cognee): Open-source AI memory platform that gives agents persistent long-term memory through a self-hosted knowledge graph and vector database engine.
- [OpenViking](https://github.com/volcengine/OpenViking): Self-evolving context database for AI agents that unifies agent memory, knowledge RAG, and skills into a single retrieval surface.
- [DocsGPT](https://github.com/arc53/DocsGPT): Self-hosted private AI platform for enterprise search, document analysis, agent building, and multi-model assistants.
- [LLM Wiki](https://github.com/nashsu/llm_wiki): Cross-platform document workspace that incrementally builds an organized, interconnected knowledge base instead of re-answering from scratch on every query.
- [SurfSense](https://github.com/MODSetter/SurfSense): Open-source NotebookLM alternative for researching live web sources through a self-hosted application, API, or MCP server.
- [Vespa](https://github.com/vespa-engine/vespa): Production AI search and serving platform for combining vector, lexical, and structured retrieval with real-time ranking and recommendations.
- [Yuxi](https://github.com/xerrors/Yuxi): Self-hosted, multi-tenant knowledge-agent platform combining RAG, knowledge graphs, multi-agent workflows, MCP/Skills, sandboxing, and access control.
- [DeepSearcher](https://github.com/zilliztech/deep-searcher): Deep research engine for private data that combines vector retrieval with reasoning to produce cited answers, so internal document sets can be queried without shipping them to a hosted research service.
- [ParadeDB](https://github.com/paradedb/paradedb): Postgres-based search and analytics engine (AGPL-3.0) that adds BM25 full-text and vector retrieval to an existing Postgres, letting RAG pipelines avoid operating a separate search cluster alongside their relational data.
- [SkillCorpus](https://github.com/EverMind-AI/SkillCorpus): Open-source pipeline that turns scattered `SKILL.md` files into a retrieval-ready agent skill corpus, covering source aggregation, safety and license gates, quality evaluation, and task-specific skill matching.
- [CocoIndex](https://github.com/cocoindex-io/cocoindex): Incremental indexing engine for AI data pipelines that reprocesses only changed deltas, keeping RAG stores and agent context continuously fresh from code, documents, Slack threads, and PDFs.
- [UltraRAG](https://github.com/OpenBMB/UltraRAG): Low-code RAG pipeline framework that declares retrieval, generation, and evaluation stages as MCP-based components instead of hand-wired scripts, with a benchmark set for measuring pipeline changes.
- [Khoj](https://github.com/khoj-ai/khoj): Self-hostable knowledge assistant (AGPL-3.0) that indexes documents and web sources into one searchable base, then layers custom agents, scheduled research automations, and local or hosted model backends on top.
- [RAG-Anything](https://github.com/HKUDS/RAG-Anything): All-in-one multimodal RAG framework that indexes text, images, tables, and equations from documents such as PDFs and Office files into one knowledge base, closing the gap where text-only pipelines silently drop visual content.
- [Hindsight](https://github.com/vectorize-io/hindsight): MIT-licensed agent memory service that learns from recorded outcomes and feedback instead of retrieval alone, with local or hosted deployment, published benchmarks, and integrations for common agent frameworks.
- [XERJ](https://github.com/xerj-org/xerj): Rust autoindex engine that makes code, docs, logs, and PDFs searchable through BM25, kNN, and hybrid queries, and exposes an Elasticsearch-compatible API so existing clients and agent memory workflows can share one index instead of re-reading files.
- [TencentDB Agent Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory): Team-level memory hub that turns conversations, documents, and code into governed, reusable assets — chat memory, skills, LLM wiki, and code graph — shared across agents and frameworks from a single memory server.
- [Moss](https://github.com/usemoss/moss): BSD-2-Clause semantic search runtime that embeds retrieval in-process through Python, TypeScript, Elixir, C, and WebAssembly SDKs, giving agent applications sub-10 ms hybrid search without operating a separate vector database cluster.
- [EverOS](https://github.com/EverMind-AI/EverOS): Apache-2.0 portable memory layer for AI agents that keeps context as user-owned local Markdown, so agent memory stays inspectable, portable, and self-hosted across apps and tools instead of locked inside one framework.

## Agentic Workflow

- [Paperclip](https://github.com/paperclipai/paperclip): Open-source control plane for coordinating teams of AI agents with goals, org charts, approvals, budgets, persistent work, and audit trails.
- [LoopX](https://github.com/loopx-project/loopx): Provider-neutral, local-first control plane for long-horizon agents with durable state, governance, recovery, evidence, and human-agent collaboration.
- [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT): Autonomous AI agent framework that can break down and execute complex tasks.
- [Atmosphere](https://github.com/Atmosphere/atmosphere): Portable JVM agent runtime that unifies model providers and agent frameworks with streaming, tool calls, human approvals, governance, and MCP or A2A support.
- [Google AX](https://github.com/google/ax): Open-source distributed agent runtime for coordinating agent applications across scalable execution environments.
- [AgentScope Runtime](https://github.com/agentscope-ai/agentscope-runtime): Production-oriented runtime for agent applications with secure tool sandboxing, Agent-as-a-Service APIs, scalable deployment, and full-stack observability.
- [Nuwax](https://github.com/nuwax-ai/nuwax): Self-hostable agent operating platform for building and running private agents, covering agent creation and distribution, knowledge base management, model proxying, memory, and a plugin ecosystem.
- [Langflow](https://github.com/langflow-ai/langflow): Graphical builder for LangChain-style LLM workflows.
- [Dify](https://github.com/langgenius/dify): Open-source LLM application development platform with visual agent workflows and AI app deployment.
- [LangChain](https://github.com/langchain-ai/langchain): Framework for building LLM-powered applications, including agent workflow orchestration.
- [Flowise](https://github.com/FlowiseAI/Flowise): Low-code LLM workflow 