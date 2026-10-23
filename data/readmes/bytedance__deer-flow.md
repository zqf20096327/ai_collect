# 🦌 DeerFlow - 2.0

English | [中文](./README_zh.md) | [日本語](./README_ja.md) | [Français](./README_fr.md) | [Русский](./README_ru.md) | [Português](./README_pt.md) | [한국어](./README_ko.md)

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)](./backend/pyproject.toml)
[![Node.js](https://img.shields.io/badge/Node.js-22%2B-339933?logo=node.js&logoColor=white)](./Makefile)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

<a href="https://trendshift.io/repositories/14699" target="_blank"><img src="https://trendshift.io/api/badge/repositories/14699" alt="bytedance%2Fdeer-flow | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
> On February 28th, 2026, DeerFlow claimed the 🏆 #1 spot on GitHub Trending following the launch of version 2. Thanks a million to our incredible community — you made this happen! 💪🔥

DeerFlow (**D**eep **E**xploration and **E**fficient **R**esearch **Flow**) is an open-source **super agent harness** that orchestrates **sub-agents**, **memory**, and **sandboxes** to do almost anything — powered by **extensible skills**.

https://github.com/user-attachments/assets/a8bcadc4-e040-4cf2-8fda-dd768b999c18

> [!NOTE]
> **DeerFlow 2.0 is a ground-up rewrite.** It shares no code with v1. If you're looking for the original Deep Research framework, it's maintained on the [`1.x` branch](https://github.com/bytedance/deer-flow/tree/main-1.x) — contributions there are still welcome. Active development has moved to 2.0.

## Official Website

Learn more and see **real demos** on our [**official website**](https://deerflow.tech).
The landing-page case studies open as allowlisted, read-only showcases without requiring a sign-in.

## Sister Projects

<img width="446" height="280" alt="image" align="middle" src="https://github.com/user-attachments/assets/077edef4-d560-41af-bb0d-d0a5f14fcc20" />

- [**LLM Space**](https://github.com/deer-flow/llm-space) - Meet our secret weapon behind DeerFlow — one desktop tool to prototype agent ideas, inspect each harness step, replay failures, and benchmark performance.

## Coding Plan from ByteDance Volcengine

- We strongly recommend using Doubao-Seed-2.0-Code, DeepSeek v3.2 and Kimi 2.5 to run DeerFlow
- [Learn more](https://www.byteplus.com/en/activity/codingplan?utm_campaign=deer_flow&utm_content=deer_flow&utm_medium=devrel&utm_source=OWO&utm_term=deer_flow)
- [中国大陆地区的开发者请点击这里](https://www.volcengine.com/activity/codingplan?utm_campaign=deer_flow&utm_content=deer_flow&utm_medium=devrel&utm_source=OWO&utm_term=deer_flow)

## InfoQuest

InfoQuest reader, web search, and image search use a 30-second HTTP connect/read
inactivity timeout. The crawl `timeout` and `navigation_timeout` settings remain
separate server-side options; they do not control the local HTTP timeout.

DeerFlow has newly integrated the intelligent search and crawling toolset independently developed by BytePlus — [InfoQuest (supports free online experience)](https://docs.byteplus.com/en/docs/InfoQuest/What_is_Info_Quest)

<a href="https://docs.byteplus.com/en/docs/InfoQuest/What_is_Info_Quest" target="_blank">
  <img
    src="https://sf16-sg.tiktokcdn.com/obj/eden-sg/hubseh7bsbps/20251208-160108.png"   alt="InfoQuest_banner"
  />
</a>

---

## Table of Contents

- [🦌 DeerFlow - 2.0](#-deerflow---20)
  - [Official Website](#official-website)
  - [Sister Projects](#sister-projects)
  - [Coding Plan from ByteDance Volcengine](#coding-plan-from-bytedance-volcengine)
  - [InfoQuest](#infoquest)
  - [Table of Contents](#table-of-contents)
  - [One-Line Agent Setup](#one-line-agent-setup)
  - [Quick Start](#quick-start)
    - [Configuration](#configuration)
    - [Running the Application](#running-the-application)
      - [Deployment Sizing](#deployment-sizing)
      - [Option 1: Docker (Recommended)](#option-1-docker-recommended)
      - [Upgrading an existing checkout](#upgrading-an-existing-checkout)
      - [Option 2: Local Development](#option-2-local-development)
      - [Startup Modes](#startup-modes)
      - [LangGraph Studio (Optional)](#langgraph-studio-optional)
      - [Docker Production Deployment](#docker-production-deployment)
    - [Advanced](#advanced)
      - [Sandbox Mode](#sandbox-mode)
      - [MCP Server](#mcp-server)
      - [IM Channels](#im-channels)
      - [Request Trace Correlation](#request-trace-correlation)
      - [LangSmith Tracing](#langsmith-tracing)
      - [Langfuse Tracing](#langfuse-tracing)
      - [Monocle Tracing](#monocle-tracing)
      - [Using Multiple Providers](#using-multiple-providers)
      - [Existing-Run Stream Actions](#existing-run-stream-actions)
      - [Personal Access Tokens](#personal-access-tokens)
  - [From Deep Research to Super Agent Harness](#from-deep-research-to-super-agent-harness)
  - [Core Features](#core-features)
    - [Skills \& Tools](#skills--tools)
      - [Exporting Custom Skills](#exporting-custom-skills)
      - [Claude Code Integration](#claude-code-integration)
    - [Private Knowledge Retrieval (RAGFlow)](#private-knowledge-retrieval-ragflow)
    - [Chat Archive](#chat-archive)
    - [Session Goals](#session-goals)
    - [Manual Context Compaction](#manual-context-compaction)
    - [Sub-Agents](#sub-agents)
    - [Sandbox \& File System](#sandbox--file-system)
    - [Agentic Browser Control](#agentic-browser-control)
    - [Context Engineering](#context-engineering)
    - [Reading a Referenced Conversation](#reading-a-referenced-conversation)
    - [Current Task Notes](#current-task-notes)
    - [Long-Term Memory](#long-term-memory)
  - [Recommended Models](#recommended-models)
  - [Embedded Python Client](#embedded-python-client)
  - [Projects](#projects)
    - [Project instructions](#project-instructions)
    - [Document shelf](#document-shelf)
    - [Archive read semantics](#archive-read-semantics)
    - [Trash](#trash)
  - [Scheduled Tasks](#scheduled-tasks)
    - [Preview cron occurrences through the API](#preview-cron-occurrences-through-the-api)
    - [Upgrade Notes](#upgrade-notes)
  - [Terminal Workbench (TUI)](#terminal-workbench-tui)
  - [Documentation](#documentation)
  - [⚠️ Security Notice](#️-security-notice)
    - [Improper Deployment May Introduce Security Risks](#improper-deployment-may-introduce-security-risks)
    - [Gateway Admin Is Equivalent to Code Execution](#gateway-admin-is-equivalent-to-code-execution)
    - [External Chat Message Roles](#external-chat-message-roles)
    - [Deployment Defaults](#deployment-defaults)
    - [Security Recommendations](#security-recommendations)
  - [Contributing](#contributing)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)
    - [Key Contributors](#key-contributors)
  - [Star History](#star-history)

## One-Line Agent Setup

If you use Claude Code, Codex, Cursor, Windsurf, or another coding agent, you can hand it the setup instructions in one sentence:

```text
Help me clone DeerFlow if needed, then bootstrap it for local development by following https://raw.githubusercontent.com/bytedance/deer-flow/main/Install.md
```

That prompt is intended for coding agents. It tells the agent to clone the repo if needed, choose Docker when available, and stop with the exact next command plus any missing config the user still needs to provide.

## Quick Start

### Configuration

With `run_events.backend: db`, caller-supplied ISO 8601 event timestamps are normalized to UTC before storage, preserving their instant when SQLite drops timezone information. Timestamps without an offset are treated as UTC. Previously stored timestamps are not rewritten.

Operators can extend lead-agent, subagent, and DeerMem extraction prompts with
literal prepend/append configuration without editing source templates. See
[prompt overlays](backend/docs/CONFIGURATION.md#prompt-overlays).

Optional per-model [`request_admission`](backend/docs/CONFIGURATION.md#model-request-admission)
paces requests to help stay within provider request-per-minute limits.
It is disabled by default; see the linked guide to enable it.
Enabling it disables exposed SDK retries and the Claude and Codex adapters'
internal retry loops so middleware retries pass through request admission again.
Middleware retries also cover HTTP 529 overload responses.
A warning identifies `retry_max_attempts` values overridden by admission.

For Google's official Gemini OpenAI-compatible endpoint, use the
[Gemini reasoning profile](backend/docs/CONFIGURATION.md#gemini-via-googles-openai-compatible-endpoint).

For MindIE XML tool calls, see the
[argument parsing and newline compatibility guide](backend/docs/CONFIGURATION.md#mindie-xml-tool-arguments).
Both synchronous and asynchronous streams retain this compatibility: tool-enabled
streams simulate chunks from a non-streaming response, while no-tool streams stay native.

1. **Clone the DeerFlow repository**

   ```bash
   git clone https://github.com/bytedance/deer-flow.git
   cd deer-flow
   ```

2. **Run the setup wizard**

   From the project root directory (`deer-flow/`), run:

   ```bash
   make setup
   ```

   This launches an interactive wizard that guides you through choosing an LLM provider, optional web search, and execution/safety preferences such as sandbox mode, bash access, and file-write tools. It generates a minimal `config.yaml` and writes your keys to `.env`. Takes about 2 minutes.

   The wizard also lets you configure an optional web search provider, or skip it for now.

   Brave web search preserves valid entries in mixed result lists. Malformed response containers or lists containing no usable entries return a structured format error; missing, null, or empty results keep the existing "No results found" response. Format errors also log the malformed container's path and type, or the absence of usable result objects, without including search queries, credentials, or payload values.

   GroundRoute web search and fetch contain malformed HTTP-success payloads the same way: a non-object payload, a `results` container that is not a list, or a non-empty list with no object entries returns the provider's format error, while non-object entries in an otherwise valid list are skipped in order. Missing, null, or empty results keep the existing "No results found" response.

   DuckDuckGo web search distinguishes execution failures from empty results: rate limits, timeouts, blocked requests, client-setup failures, SDK errors, and a missing `ddgs` dependency return a structured `DuckDuckGo search failed: ...` error instead of "No results found", while a genuinely empty result set keeps the existing "No results found" response. The structured error text lets the harness classify an outage as transient or a configuration problem instead of a query that matched nothing.
   
   Tavily web search and fetch contain malformed HTTP-success payloads the same way: a non-object payload, or a `results`/`failed_results` container that is not a list, returns the provider's format error, and non-object entries in an otherwise valid list are skipped in order. Missing, null, or empty results keep the existing response (`[]` for search, `Error: No results found` for fetch); missing or null search fields (`title`, `url`, `content`) normalize to empty text, and a non-string fetch `raw_content` is coerced to text before the truncation limit.

   Sofya web search and fetch contain malformed HTTP-success payloads the same way: a non-object payload, a `results` container that is not a list, or a non-empty list with no object entries returns the provider's format error, while non-object entries in an otherwise valid list are skipped in order. Missing, null, or empty results keep the existing "No results found" response.

   Serper web and image search preserve valid entries in mixed result lists. A malformed `organic`/`images` container, or a non-empty list holding no object entries, returns Serper's format error; missing, null, or empty containers keep the existing "No results found" / "No images found" response. Format errors log the container field name only, without queries, credentials, or payload values.

   Tencent Cloud WSA web search contains malformed HTTP-success payloads the same way: a `Pages` container that is not a list, or a non-empty container holding no usable page, returns the provider's format error, while malformed page entries in an otherwise valid container are skipped so the valid rows survive. Missing, null, or empty `Pages` keep the existing "No results found" response.

   Serply web search contains malformed HTTP-success payloads the same way in every vertical: a `results`/`entries`/`articles` container that is not a list, or a non-empty list with no object entries, returns the provider's format error, while non-object entries in an otherwise valid list are skipped in order. Missing, null, or empty containers keep the existing "No results found" response.

   SearXNG web search contains malformed HTTP-success payloads the same way: a payload that is not an object, a body that is not JSON, a `results` container that is not a list, or a non-empty list holding no object entries returns the provider's format error, while non-object entries in an otherwise valid page are skipped in order, each skip logged with its entry position, so the valid rows survive and provider-side drift leaves a trace. Missing, null, or empty `results` keep the existing empty result (`[]`). This matters most for a self-hosted instance: one behind a reverse proxy or captive portal answers an HTML or plain-text error page with HTTP 200, and reading that as an empty search ends a research loop as "no hits".

   InfoQuest web and image search contain malformed HTTP-success payloads the same way: a `search_result` envelope that is not an object, or an `organic`/`top_stories.items`/`images_results` container that is not a list or that holds no usable entry, returns the provider's format error, while malformed entries in an otherwise valid payload are skipped so the usable rows survive. Missing, null, or empty containers keep the existing empty result. Format errors log the container or entry position only, without queries or payload values.

   InfoQuest web and image search screen result URLs through the shared public-URL policy and omit rejected rows. Responses without the required `search_result` envelope return a format error instead of exposing the raw provider payload.

   Jina, Browserless, and InfoQuest web fetches resolve relative links and image sources using the requested page URL (or a usable HTML base URL), so returned Markdown includes complete destinations. Link resolution preserves the surrounding HTML source, including malformed-page formatting.

   Self-hosted Browserless, Crawl4AI, Firecrawl, and fastCRW fetch backends require outbound isolation from private, loopback, link-local, and cloud-metadata networks before setting `network_isolation_confirmed: true` on each tool. DeerFlow rejects private or unverifiable backends by default because those services handle redirects, DNS resolution, and subresources themselves. `allow_private_addresses` permits intentional internal target URLs and does not bypass the backend check. See [delegated fetch deployment](backend/docs/CONFIGURATION.md#delegated-fetch-backend-isolation); `make doctor` reports backend configurations that would be refused.

   Jina fetches support opt-in bounded retries via `max_retries` (default `0`) and `retry_budget_seconds` (default `30`) in the tool configuration. Valid `Retry-After` hints set a minimum wait for HTTP 429/503; 429 without a valid hint stays terminal. Hints that cannot fit the remaining budget stop retries. Local backoff remains randomized. Retries may increase upstream requests and cost; see [Jina fetch retries](backend/docs/CONFIGURATION.md#jina-fetch-retries).

   Jina also accepts an opt-in `max_response_bytes` tool setting (positive integer; omitted/null disables it). It stops oversized decoded responses before extraction, with no partial success or retry. This leaves the 4096-character output cap unchanged and does not bound HTTPX decompressor allocations or wire bandwidth; see [response budget](backend/docs/CONFIGURATION.md#jina-response-byte-budget).

   Jina can also bound concurrent HTTP attempts and FIFO waiting with the opt-in `request_admission` tool extra. One immutable budget is shared across clients and agent threads in each process; replicas have independent budgets. See [Jina request admission](backend/docs/CONFIGURATION.md#jina-request-admission).

   Run `make doctor` at any time to verify your setup and get actionable fix hints.
   The setup wizard and health check support legacy terminal encodings, including
   Windows cp936, replacing unsupported characters so both commands can finish.
   If you are opening a GitHub issue about a local setup or runtime problem, run
   `make support-bundle`. The command prints reporter next steps, writes a
   `*-issue-summary.md` file to paste into the issue, a `*-issue-draft.md` file
   for AI-assisted issue filing, and an optional evidence zip under
   `.deer-flow/support-bundles/`. If an AI assistant files the issue, start from
   the draft and replace every REQUIRED placeholder instead of inventing missing
   facts. Attach the zip only if a maintainer asks for it, or if the summary
   alone is not enough. Maintainers and AI triage tools can start with
   `triage.json`; the bundle includes redacted diagnostics and file manifests
   only, and does not include `.env`, raw conversation messages, or user file
   contents. Subprocess diagnostics are captured as UTF-8, with Python helpers
   emitting UTF-8 even on non-UTF-8 hosts and escaping unencodable characters.
   Thread manifests follow the local launcher's runtime paths: checkout `.env`
   values override shell exports, and a project-root override alone still uses
   `backend/.deer-flow` first. Simple variable references such as
   `DEER_FLOW_HOME="$PWD/backend/.deer-flow"` use the checkout as `PWD`;
   single-quoted references remain literal. If the checkout `.env` cannot be read or decoded
   as UTF-8, thread diagnostics retain shell exports and default storage paths. For standalone Gateway launches using `backend/.env`
   or `DEER_FLOW_ENV_FILE`, export the effective `DEER_FLOW_HOME` when collecting
   the bundle and ensure the checkout `.env` does not override it.
   Doctor's internal tool probes also decode UTF-8 with replacement for invalid
   bytes so the remaining diagnostic output stays available.

   When a thread manifest is requested, a nonempty `DEER_FLOW_HOME` selects the
   runtime data directory instead of stale checkout data. External data paths
   appear as `{DEER_FLOW_HOME}` in the report; file contents remain excluded.
   Runtime path settings also come from the checkout `.env`, with shell exports
   taking precedence. Relative paths resolve from the checkout as in `make dev`.
   Without an explicit home, a configured `DEER_FLOW_PROJECT_ROOT` selects its
   `.deer-flow` directory; external paths use that variable name in the report.

   > **Advanced / manual configuration**: If you prefer to edit `config.yaml` directly, run `make config` instead to copy the full template. Optional dependency auto-detection accepts UTF-8 configuration files with or without a byte-order mark (BOM). It checks an existing `DEER_FLOW_CONFIG_PATH` first, then `DEER_FLOW_PROJECT_ROOT/config.yaml`, before the checkout's default locations. Local startup also accepts the project-root configuration when the checkout has no `config.yaml`. See `config.example.yaml` for the complete reference including CLI-backed providers (Codex CLI, Claude Code OAuth), OpenRouter, Responses API, subagent runtime caps such as `subagents.max_total_per_run`, and more.

   Optional per-model pricing must use one currency across all priced models.
   DeerFlow disables Console cost estimates when currencies are mixed rather
   than presenting an invalid aggregate.

   Administrators can open **Settings → Models** to select a provider and enter
   only its **API Key** and **model ID**. Endpoints, authentication and adapters are
   backend presets for OpenAI, Anthropic, DeepSeek, Alibaba Cloud Bailian/Qwen,
   Volcengine/Doubao, Moonshot/Kimi, Zhipu/Z.AI and MiniMax. Region and plan-specific
   entries are explicitly distinguished. Arbitrary model IDs are accepted; internal
   names are generated automatically and remain stable when a model ID changes.
   Newly saved models are enabled and immediately refresh existing chat and Agent
   model selectors, without editing YAML or restarting the Gateway.

   **Custom OpenAI-compatible** still supports existing/custom base URLs and
   unauthenticated endpoints. **Advanced settings** retains display name, token
   limits and vision overrides; unknown IDs do not receive invented capabilities.
   Leave the key blank on edit to retain it for the same connection. Switching
   provider or custom endpoint requires a new key, and preset models must be
   disabled before clearing their key. YAML models remain read-only.

   Connection testing uses the same model factory and protocol as chat, sends a
   bounded streaming tool-call request and never saves the draft. It may incur
   provider charges and does not verify every agent, vision or thinking workflow.
   Official DeepSeek custom endpoints retain their existing adapter; a proxy does
   not become DeepSeek merely because of its model ID. See the
   [Web model registration reference](backend/docs/CONFIGURATION.md#models-registered-through-the-web)
   for presets, compatibility, extension instructions and backup requirements.

   DeepSeek regression tests run offline with the normal backend suite. To verify
   the real provider explicitly, set `DEEPSEEK_TEST_API_KEY` in your environment
   and run from `backend/`:

   ```bash
   DEER_FLOW_RUN_LIVE_TESTS=1 uv run --no-sync pytest tests/test_managed_deepseek_live.py -q
   ```

   These opt-in tests send short requests to DeepSeek and may incur charges;
   they use temporary state, never save credentials to the deployment catalog,
   and are skipped in CI. `DEEPSEEK_TEST_MODEL` optionally selects a different
   DeepSeek model ID (default: `deepseek-flash`). The same tests can be run on
   unfixed and fixed revisions; success is always the expected result.

   YAML models remain read-only in this page and take precedence on name conflicts.
   Managed models are appended after YAML models; edits apply to new configuration
   snapshots, while active runs retain their existing snapshot. Disabling a model
   removes it from future selection/resolution, so update any custom-agent or scheduled
   task definitions that explicitly reference it before disabling it.
   Managed models are shared by the deployment, not personal API-key profiles, and
   remain subject to the existing model authorization policy.

   The encrypted catalog and a generated local encryption key are stored in
   `$DEER_FLOW_HOME/managed-models/` (default `.deer-flow/managed-models/`). Persist
   and back up the **whole directory**, restrict filesystem access, and share it
   across Gateway workers/replicas that should use the same catalog. The local key
   is protected by filesystem permissions; encryption does not protect against
   someone who can read both files. Losing the key requires restoring the backup.
   Reads and writes fail if the catalog cannot be decrypted, rather than replacing it.
   This storage is independent of the SQL backend and works with read-only YAML mounts.

   When several models are configured, open either model picker and use the
   star beside a model to favorite it. Favorites appear first in both the main
   chat and Side Chat pickers without changing either chat's selected or
   default model. They are stored for the signed-in user in the current browser,
   so they do not sync to another browser or device and do not require a startup
   setting. The compact favorites picker intentionally omits search and only
   adds favorite ordering to the two-line model list.

   <details>
   <summary>Manual model configuration examples</summary>

   ```yaml
   models:
     - name: gpt-4o
       display_name: GPT-4o
       use: langchain_openai:ChatOpenAI
       model: gpt-4o
       api_key: $OPENAI_API_KEY

     - name: openrouter-gemini-2.5-flash
       display_name: Gemini 2.5 Flash (OpenRouter)
       use: langchain_openai:ChatOpenAI
       model: google/gemini-2.5-flash-preview
       api_key: $OPENROUTER_API_KEY
       base_url: https://openrouter.ai/api/v1

     - name: opper-claude-sonnet-4-6
       display_name: Claude Sonnet 4.6 (Opper)
       use: langchain_openai:ChatOpenAI
       model: claude-sonnet-4-6
       api_key: $OPPER_API_KEY
       base_url: https://api.opper.ai/v3/compat

     - name: api-route-gpt-6.1-sol
       display_name: GPT 6.1 Sol (API Route)
       use: langchain_openai:ChatOpenAI
       model: gpt-6.1-sol
       api_key: $API_ROUTE_API_KEY
       base_url: https://global.api-route.com/v1

     - name: gpt-5-responses
       display_name: GPT-5 (Responses API)
       use: langchain_openai:ChatOpenAI
       model: gpt-5
       api_key: $OPENAI_API_KEY
       use_responses_api: true
       output_version: responses/v1

     - name: qwen3-32b-vllm
       display_name: Qwen3 32B (vLLM)
       use: deerflow.models.vllm_provider:VllmChatModel
       model: Qwen/Qwen3-32B
       api_key: $VLLM_API_KEY
       base_url: http://localhost:8000/v1
       supports_thinking: true
       when_thinking_enabled:
         extra_body:
           chat_template_kwargs:
             enable_thinking: true
   ```

   OpenRouter and similar OpenAI-compatible gateways should be configured with `langchain_openai:ChatOpenAI` plus `base_url`. If you prefer a provider-specific environment variable name, point `api_key` at that variable explicitly (for example `api_key: $OPENROUTER_API_KEY`).

   [API Route](https://www.api-route.com) is also available in the setup wizard. It saves your key as `API_ROUTE_API_KEY` and uses the Chat Completions endpoint above. Model availability depends on your key's group and permissions; check the authenticated `GET https://global.api-route.com/v1/models` catalog before replacing the model in `config.yaml`, and use its returned ID unchanged without an upstream provider prefix.

   The `write_file` tool's output-budget hint uses the active model's effective `max_tokens`. Missing or unusable limits, including YAML `.inf`, `-.inf`, `.nan`, and values too large for the character estimate, omit this hint without failing tool assembly; provider-specific model validation still applies.

   To route OpenAI models through `/v1/responses`, keep using `langchain_openai:ChatOpenAI` and set `use_responses_api: true` with `output_version: responses/v1`.

   The lead agent also recognizes Responses output-token caps (`status: incomplete` with `incomplete_details.reason: max_output_tokens`), including streaming responses. It suppresses tool execution, removes the suppressed calls from later model requests, and preserves text and reasoning. A capped tool-call response includes a visible notice; other incomplete reasons retain their existing handling.

   When thinking is disabled on a legacy profile, blank `extra_body`, `thinking`, and nested `extra_body.thinking` keys in a `when_thinking_enabled` template are treated as absent during dialect inference. When thinking is enabled, template values are forwarded as configured.

   Models whose provider contract differs from DeerFlow's generic thinking/effort assumptions can declare a per-model mapping-valued `reasoning:` block (thinking `unsupported`/`optional`/`required`, the accepted effort values with aliases and a default, the payload dialect, and the reasoning-history requirement). The setup wizard's Z.AI GLM-5.3-Flash profile uses it: thinking stays on for every foreground and background call, and the effort selector offers the model's own `low`/`high`/`max` levels. Ollama's existing boolean `reasoning: true` remains a native provider setting and is forwarded to ChatOllama. When migrating a profile to a custom effort `path`, remove any old `reasoning_effort` setting from the profile and thinking templates; configuration validation rejects the leftover key. The chat UI drops a remembered provider-specific effort when switching to a legacy model that does not advertise it. Profiles without the block keep their existing provider behavior. See `config.example.yaml` for the shape and the equivalent manual configuration.

   For vLLM 0.19.0, use `deerflow.models.vllm_provider:VllmChatModel`. For Qwen-style reasoning models, DeerFlow toggles reasoning with `extra_body.chat_template_kwargs.enable_thinking` and preserves vLLM's non-standard `reasoning` field across multi-turn tool-call conversations. Legacy `thinking` configs are normalized automatically for backward compatibility, without modifying model defaults or caller-owned `extra_body` dictionaries; a reused dictionary can change the legacy switch between requests. If the endpoint reports a cumulative usage snapshot on every streaming chunk, set `cumulative_stream_usage: true` so DeerFlow converts those snapshots into per-chunk deltas; the option is disabled by default and leaves usage unchanged when a stable completion id is unavailable. Reasoning models may also require the server to be started with `--reasoning-parser ...`. If your local vLLM deployment accepts any non-empty API key, you can still set `VLLM_API_KEY` to a placeholder value.

   When prompt caching is enabled for a model configured with
   `deerflow.models.claude_provider:ClaudeChatModel`, DeerFlow preserves thinking
   and redacted-thinking history without placing cache breakpoints directly on
   those blocks. Extended-thinking tool follow-ups can keep using prompt caching.

   CLI-backed provider examples:

   ```yaml
   models:
     - name: gpt-5.4
       display_name: GPT-5.4 (Codex CLI)
       use: deerflow.models.openai_codex_provider:CodexChatModel
       model: gpt-5.4
       supports_thinking: true
       supports_reasoning_effort: true

     - name: claude-sonnet-4.6
       display_name: Claude Sonnet 4.6 (Claude Code OAuth)
       use: deerflow.models.claude_provider:ClaudeChatModel
       model: claude-sonnet-4-6
       max_tokens: 4096
       supports_thinking: true
   ```

   `ClaudeChatModel` normalizes manual extended-thinking budgets when `auto_thinking_budget: true` (the default). An omitted or null budget gets 80% of `max_tokens`, with a minimum of 1024 tokens. Explicit budgets must be integers of at least 1024 and, for ordinary thinking, strictly below `max_tokens`; output limits of 1024 or less fail locally. For supported manual interleaved thinking, configure tools and `betas: ["interleaved-thinking-2025-05-14"]`: the thinking budget may equal or exceed the positive output limit. See [Anthropic's interleaved-thinking rules](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#interleaved-thinking-in-manual-mode) for supported models. `auto_thinking_budget: false` bypasses this normalization and validation; disabled and adaptive thinking are unchanged.

   - Codex CLI reads `~/.codex/auth.json`
   - Codex function tools preserve explicit `strict: true` or `strict: false` in wrapped or flat dictionary definitions. Missing or null settings keep the provider default. `bind_tools` applies the same conversion to dictionaries and `BaseTool` schemas.
   - Codex honors `tool_choice` in `bind_tools` and direct calls: `auto`, `none`, `required`, or a function name/selection. `any` and `True` mean `required`; `None` and `False` keep the provider default. Per-call choices override the bound policy. Bound choices are validated when binding; direct calls and overrides are validated before HTTP. `required` needs at least one function tool, and named selections must match a supplied function. `auto` and `none` also work without tools.
   - Completed Codex responses still return their text and tool calls when token usage is null, omitted, or empty; usage metadata remains unavailable.
   - The Codex model provider returns completed responses without waiting for the SSE connection to close. Failed or incomplete responses report the provider's error or reason; partial output is not returned as a successful answer. Non-object error details are reported as text.
   - `ClaudeChatModel` honors integer-second and HTTP-date `Retry-After` hints in its provider retry loop. Dates use UTC; past dates retry immediately, while invalid hints or delays beyond 24 hours retain local backoff.

   - Claude Code accepts `CLAUDE_CODE_OAUTH_TOKEN`, `ANTHROPIC_AUTH_TOKEN`, `CLAUDE_CODE_CREDENTIALS_PATH`, or `~/.claude/.credentials.json`
   - `CLAUDE_CODE_OAUTH_TOKEN_FILE_DESCRIPTOR` accepts a UTF-8 token handoff and reuses it for later model instances in the same process. Undecodable handoffs are skipped so Claude Code can still try its override or default credentials file.
   - CLI credential JSON files accept UTF-8 with or without a BOM, independently of the host locale. `make doctor` accepts the same files when checking CLI authentication. Invalid text encoding is treated as an unreadable source; Claude Code can still try its default file after an invalid override.
   - ACP agent entries are separate from model providers — if you configure `acp_agents.codex`, point it at a Codex ACP adapter such as `npx -y @zed-industries/codex-acp`
   - A bare or absolute ACP agent `command` is resolved before the agent starts, so npm-installed launchers work on Windows too: `npx` or `mcode` is spawned as its `npx.cmd`/`mcode.cmd` shim instead of failing with a command-not-found error, and an absolute path such as `C:\Users\me\AppData\Roaming\npm\mcode` resolves to the `mcode.cmd` shim beside npm's extensionless shell script instead of failing with `WinError 193`. The lookup uses the `PATH` the agent subprocess will actually see (`acp_agents.<name>.env.PATH` when set, otherwise the Gateway's) and hands the spawn an absolute path, so a relative `PATH` entry cannot be re-interpreted inside the agent's own workspace. A relative `command` (for example `bin/mcode`) is used as configured, and a command that cannot be resolved is still reported with the install guidance below.
   - Each ACP agent's `timeout_seconds` (default: 1800) is one shared budget for initialization, session creation, and the prompt, starting after the subprocess launches. On timeout, DeerFlow aborts the invocation and closes the subprocess before returning an error. Workspace/MCP preparation and subprocess cleanup are outside this budget. A `TimeoutError` raised by the SDK before this deadline expires retains its own error message.
   - If an ACP agent exits before answering (for example because it is not authenticated or a configured argument is wrong), DeerFlow reports its exit code within a few seconds instead of waiting for `timeout_seconds`, and records the end of the agent's stderr in the Gateway log. Agent stderr is read continuously, so an agent that logs heavily cannot stall on a full pipe.
   - MiniMax Code speaks ACP directly. Install and authenticate it, then add it as an ACP agent:

   ```bash
   npm install --global @minimax-ai/code
   mcode login
   ```

   ```yaml
   acp_agents:
     mcode:
       command: mcode
       args: ["acp"]
       description: MiniMax Code for implementation, refactoring, debugging, and repository tasks
       auto_approve_permissions: false
   ```

   `mcode` must be on the Gateway process's `PATH`; installing it only on the Docker host does not make it available inside the Gateway container. DeerFlow invokes it through `invoke_acp_agent` in a per-thread ACP workspace and forwards enabled MCP servers. Keep `auto_approve_permissions: false` for untrusted tasks; enable it only when mcode must edit files or run commands and you trust the task.
   - On macOS, export Claude Code auth explicitly if needed:

   ```bash
   eval "$(python3 scripts/export_claude_code_oauth.py --print-export)"
   ```

   The exporter rejects malformed credential containers and non-string or blank access tokens before printing a token, emitting a shell export, or writing a credentials file. Valid tokens are exported unchanged, and file exports preserve the full credential container.

   API keys can also be set manually in `.env` (recommended) or exported in your shell:

   ```bash
   OPENAI_API_KEY=your-openai-api-key
   TAVILY_API_KEY=your-tavily-api-key
   ```

   </details>

For an explicit backend dotenv file, export `DEER_FLOW_ENV_FILE` before startup,
alongside `DEER_FLOW_CONFIG_PATH` if needed. For example, from `backend/`:

```bash
DEER_FLOW_ENV_FILE=/srv/deer-flow/stage.env DEER_FLOW_CONFIG_PATH=/srv/deer-flow/stage.yaml make gateway
```

Relative dotenv paths use the backend process working directory; absolute paths
work regardless of that directory. Existing process variables win. An unset
selector preserves default dotenv discovery; a specified empty, missing,
non-file or unreadable path fails startup. Explicit selection also fails when
`PYTHON_DOTENV_DISABLED` disables dotenv loading. Restart after changing the file.
This selects backend dotenv input only: shell launchers, Docker Compose and the
frontend retain their own environment loading. Values they already export win.
It does not select `ENV` profiles or isolate databases, storage or tenants.
See [backend dotenv selection](backend/docs/CONFIGURATION.md#backend-dotenv-selection).

Custom blob storage backends accept `blob_storage.backend: module.Class` or
`module:Class`, including a single `.py` module importable by the Gateway.
The selected class must implement `BlobStore`; backend options go under
`blob_storage.backend_config`. See [blob storage](backend/docs/blob-storage.md).

### Running the Application

#### Deployment Sizing

Use the table below as a practical starting point when choosing how to run DeerFlow:

| Deployment target | Starting point | Recommended | Notes |
|---------|-----------|------------|-------|
| Local evaluation / `make dev` | 4 vCPU, 8 GB RAM, 20 GB free SSD | 8 vCPU, 16 GB RAM | Good for one developer or one light session with hosted model APIs. `2 vCPU / 4 GB` is usually not enough. |
| Docker development / `make docker-start` | 4 vCPU, 8 GB RAM, 25 GB free SSD | 8 vCPU, 16 GB RAM | Image builds, bind mounts, and sandbox containers need more headroom than pure local dev. |
| Long-running server / `make up` | 8 vCPU, 16 GB RAM, 40 GB free SSD | 16 vCPU, 32 GB RAM | Preferred for shared use, multi-agent runs, report generation, or heavier sandbox workloads. |

- These numbers cover DeerFlow itself. If you also host a local LLM, size that service separately.
- Linux plus Docker is the recommended deployment target for a persistent server. macOS and Windows are best treated as development or evaluation environments.
- If CPU or memory usage stays pinned, reduce concurrent runs first, then move to the next sizing tier.

#### Option 1: Docker (Recommended)

Requires Docker Desktop / Docker Engine and **Docker Compose v2.24+**
(`docker compose version`). Older Compose clients cannot parse the optional
`env_file` syntax in `docker/docker-compose.yaml` and `docker/docker-compose-dev.yaml`.

**Development** (hot-reload, source mounts):

```bash
make docker-init    # Pull sandbox image (only once or when image updates)
make docker-start   # Start services (auto-detects sandbox mode from config.yaml)
make docker-logs    # View logs
```

`make docker-start` starts `provisioner` only when `config.yaml` uses provisioner mode (`sandbox.use: deerflow.community.aio_sandbox:AioSandboxProvider` with `provisioner_url`). Direct Compose users can add `--profile provisioner` to the dev command for the same mode; the default stack does not require Kubernetes.

Docker builds use the upstream `uv` registry by default. The gateway image installs with `uv sync --locked`, and `uv.lock` pins `https://pypi.org/simple`, so `UV_INDEX_URL` has to keep that value: exporting a mirror such as `https://pypi.tuna.tsinghua.edu.cn/simple` fails the build with ``The lockfile at `uv.lock` needs to be updated, but `--locked` was provided`` (reproduce in an already-synced environment with `cd backend && UV_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple uv sync --locked --check`; if the environment itself is stale, `--check` reports that instead for either index, so use `uv lock --check` to see it without syncing). Installing from a mirror requires regenerating the lock or dropping `--locked`, and both change what the image installs, so keep the default index for a checkout you intend to contribute back. `NPM_REGISTRY=https://registry.npmmirror.com` is independent of this: it applies to the frontend image's `pnpm` install and to the gateway image's Lark CLI install (`@larksuite/cli`, which `backend/Dockerfile` installs with npm).

Local AIO sandbox control traffic is always direct: loopback/private addresses,
single-label cluster hosts, and Docker/Podman internal hostnames do not inherit
`HTTP_PROXY` or `HTTPS_PROXY`. External sandbox FQDNs and public IPs still
honor environment proxy settings.

Backend processes automatically pick up `config.yaml` changes on the next config access, so model metadata updates do not require a manual restart during development.

Gateway runs use the top-level `recursion_limit` in `config.yaml` when an API
request does not provide one. The default is `100`; valid per-request values
take precedence, and `max_recursion_limit` (default `1000`) caps both. Changes
apply to the next run without restarting the Gateway. This top-level setting
applies to Gateway API runs; IM channel and embedded `DeerFlowClient` runs
retain their own defaults and per-call override paths.

A custom frontend can add an optional `context.client` to a Gateway run request:
a client name, capabilities such as `artifacts` or `charts`, and display
preferences. DeerFlow sanitizes it and passes the values to the agent as
untrusted, request-scoped hints, so skills can pick an output shape the client
can show. It is never an authorization or identity signal. See
[Create Run](backend/docs/API.md#create-run).
Client hints are omitted from stored run configuration and must be sent again
for each run; later runs, including server-started tasks, do not inherit them.
The checkpoint storage settings `database.checkpoint_channel_mode` and
`database.checkpoint_delta.snapshot_frequency` (default `10`) are exceptions:
both are frozen when the process first builds an agent (including through
`DeerFlowClient`) and require a process restart to change safely.

The optional `database.checkpoint_cache` section (delta channel mode only)
caches materialized checkpoint histories: `type` is `memory` (default) or
`redis`, and `max_entries: 0` disables the cache. The `redis` backend is
Gateway/async-only; the sync TUI/embedded path supports `memory` only. The
cache is performance-only — results are identical with it disabled — so it is
never frozen and workers sharing one checkpoint database may safely run
different cache settings. Redis thread cleanup treats a configured `key_prefix`
as literal text, including glob metacharacters, so deletion stays within that
namespace and thread.

Gateway checkpoint cleanup runs when the next run wins durable same-thread
admission, before its first checkpoint read. It checks only the root head and
its parent, removes at most one metadata-only duration leaf without pending
writes, and preserves explicit checkpoint selections and delta replay state.
See [checkpoint operations](https://deerflow.tech/docs/harness/checkpoints/operations)
for the retention constraints.

> [!TIP]
> On Linux, if Docker-based commands fail with `permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock`, add your user to the `docker` group and re-login before retrying. See [CONTRIBUTING.md](CONTRIBUTING.md#linux-docker-daemon-permission-denied) for the full fix.

**Production** (builds images locally, mounts runtime config and data):

```bash
make up     # Build images and start all production services
make down   # Stop and remove containers
```

Access: http://localhost:2026

`make up` waits for the Gateway `/health` endpoint before reporting success.
If the Gateway does not become healthy within the startup window, deployment
exits non-zero and prints the container status plus recent Gateway logs. The
production image starts from its already-built environment and never resolves
or installs Python dependencies at container startup.

If `make up` reports an unwritable runtime home or an unreadable persisted secret
after `make docker-start`, run the printed `sudo chown -R <uid>:<gid> '<home>'`
recovery command and retry. The check honors secret overrides from the shell or
`.env`, accepts readable read-only secret files, and leaves `make down` available
without reading or generating secrets.

Production Docker commands can select a root dotenv profile with
`DEER_FLOW_COMPOSE_ENV_FILE=/srv/deer-flow/stage.env make up`. The same file
feeds Compose interpolation, Gateway/provisioner variables, and deployment
secret checks. YAML and runtime-state locations remain separate selectors;
see [production env files](backend/docs/CONFIGURATION.md#production-compose-env-files).

For persistent deployments, configure `database.backend` as `sqlite` or
`postgres`. The selected backend is shared by the LangGraph checkpointer,
LangGraph Store, and DeerFlow application data. The deprecated `checkpointer`
section, when present, overrides the first two for backward compatibility.

Gateway startup automatically repairs the missing run-change schema affecting
some existing databases (#5516). The repair preserves run history and existing
change positions; downgrading the repair to its predecessor also retains the
schema and positions required by that version.

For lightweight single-process event persistence, `run_events.backend: jsonl`
keeps Unicode message content intact, including line and paragraph separators.
Existing valid JSONL records remain readable without rewriting the files.

For per-call usage audits, an immediate LLM response replay with populated usage
updates both nested usage and top-level token counters, even if initial usage was absent or zero.
The original request, model, and status metadata stay intact; flushed events are
not rewritten. See the [run event contract](contracts/run_event_stream_contract.json).

The unified nginx endpoint is same-origin by default and does not emit browser CORS headers. If you run a split-origin or port-forwarded browser client, set `GATEWAY_CORS_ORIGINS` to comma-separated exact origins such as `http://localhost:3000`; the Gateway then applies the CORS allowlist and matching CSRF origin checks.

When fine-grained authorization is enabled, Live Browser connections require `threads:write` as well as ownership of the thread, even when only viewing frames: the same connection can control the browser. Permission checks run when connecting. Restart Gateway after upgrading to disconnect sessions admitted by older code.

The bundled Docker, local and Helm nginx configs proxy Live Browser WebSocket upgrades with a 600-second read timeout for quiet streams. Helm uses nginx's default connection and send timeouts for the in-cluster Gateway. Any additional Ingress or reverse proxy must also allow WebSocket upgrades.

Browser login uses `HttpOnly` session cookies. The login page offers a "keep me signed in" option that extends the browser session when the request is HTTPS (including trusted `X-Forwarded-Proto: https`) or localhost HTTP. The localhost exception uses the direct request `Host` and ignores forwarded host headers. Public HTTP deployments, including many temporary sandbox URLs, fall back to session cookies by default. DeerFlow never stores the password in browser storage; the UI may remember only the email address.

OIDC/SSO authorization endpoints may include provider query parameters such as `?prompt=login`. DeerFlow preserves those parameters when adding the login request, including for configured `authorization_endpoint` overrides.

Administrators can suspend and restore accounts from **Settings → Users** (admin-only; the section is hidden for ordinary users). The page lists each account's email, role, and status and exposes the same enable/disable operation as `PATCH /api/v1/admin/users/{id}`; the last remaining active admin cannot be disabled, and the Gateway's rejection detail is shown verbatim. A disabled account is rejected by every authentication surface, and its live sessions end on the next request with a login page that states the account has been disabled. Password login for a disabled account deliberately still answers "incorrect email or password" so the state is not disclosed to whoever holds the credentials.

DeerFlow still uses `Forwarded` / `X-Forwarded-*` headers to recover the browser-facing scheme and origin behind a proxy. The bundled nginx sets `X-Forwarded-Proto`, but preserves an upstream HTTPS value and does not overwrite every forwarded header. Configure the outer trusted proxy to replace or strip client-supplied forwarding headers before traffic reaches DeerFlow.

> [!IMPORTANT]
> The Gateway still owns active run tasks in process, so production defaults to a single Gateway worker (`GATEWAY_WORKERS=1`). Multi-worker deployments require Postgres, the Redis stream bridge (`stream_bridge.type: redis`), `run_ownership.heartbeat_enabled: true`, and `run_events.backend: db`; process-local memory/JSONL event stores cannot enforce singleton delivery receipts across workers. Kubernetes replicas run one worker per Pod, which the worker count cannot see: declare them with `deployment.multi_instance: true` (or `DEER_FLOW_MULTI_INSTANCE=1`, which deploy tooling such as a Helm chart can set from its replica count) so the startup gate enforces the same prerequisites instead of staying inert. Declared instances that store credentials (`channel_connections`, or MCP servers using the OAuth `refresh_token` grant, whose rotating tokens they share through the database) must also share one at-rest `DEER_FLOW_CREDENTIALS_KEY` (the Helm chart and `make up` generate it; back it up, see [backend/docs/CONFIGURATION.md](backend/docs/CONFIGURATION.md#credentials-encryption-key-deer_flow_credentials_key)). The bridge shares SSE delivery and bounded `Last-Event-ID` replay across workers. When a trimmed reconnect cursor cannot be verified for complete replay, or a subscriber that already established an empty-stream wait falls behind before its first delivery, Memory and Redis emit a machine-readable SSE `gap` event instead of silently returning a partial replay; the Web UI reloads durable thread/event state and resumes from the retained tail. The Memory bridge can replay without recovery when the cursor is its exact last evicted event: every successor is still retained. Older or unverifiable evicted cursors still trigger recovery. An already-observed Redis stream removed during replay also signals a gap, so slow subscribers reload durable state instead of heartbeating forever after cleanup. Redis also tracks terminal stream producers with a short lease: if a worker dies after committing a terminal run status but before publishing END, SSE and `/wait` finish after the lease expires instead of waiting for the retained stream's TTL. Lease reconciliation marks runs from dead workers as errors, persists their delivery receipts, publishes the terminal stream marker, schedules retained-stream cleanup, and updates the affected thread status. SSE, `/wait`, and internal stream consumers use `stream_bridge.heartbeat_interval_seconds` (default `15`) for idle liveness checks; changing it requires a Gateway restart. Malformed Redis reconnect IDs live-tail new events instead of replaying the retained buffer, and the rolling retained-buffer TTL (`stream_ttl_seconds`) remains a cleanup safety net rather than a run timeout. Failed-login counters and lockouts for `POST /api/v1/auth/login/local` (`auth.local.max_login_attempts` / `lockout_seconds`) are kept in the shared `login_throttle` table whenever the application database is SQLite or Postgres (`auth.local.throttle_storage: auto`, the default), so every replica enforces one lockout per client IP; `memory` keeps the historical per-process counter, which under N replicas hands an attacker N × `max_login_attempts` guesses and logs a startup warning. IM chat-to-thread bindings live in the shared `channel_thread_bindings` table whenever the application database is SQLite or Postgres (an existing `channels/store.json` is imported once at startup and renamed `store.json.migrated`); IM bot credentials entered in the web UI live in the shared `channel_runtime_configs` table, encrypted with `DEER_FLOW_CREDENTIALS_KEY` (an existing `channels/runtime-config.json` is imported once and then deleted), so a save on any instance reaches the provider's connection within one lease renewal; each provider's platform connection is held by one instance through the shared `channel_leases` table — `channels.leader_lease` (default `auto`, on wherever the multi-process signal is) hands it to another instance when the holder dies, and the startup gate refuses `enabled: false` while an IM channel other than GitHub is enabled (see [IM channel leader lease](backend/docs/CONFIGURATION.md#im-channel-leader-lease-channelsleader_lease)); follow-up buffers still need their own multi-worker coordination. To try this topology on one machine, `make dev-multi` starts two Gateways on shared Postgres, Redis and `DEER_FLOW_HOME`, and `make dev-multi-check` runs the cross-instance checks; see the local two-Gateway harness in [backend/docs/CONFIGURATION.md](backend/docs/CONFIGURATION.md#local-two-gateway-harness).
>
> The producer-lease recovery behavior above is gated by `stream_bridge.producer_lease_recovery_enabled`. Keep it disabled while old Gateway binaries or their runs remain; enable it on every instance only after the writer rollout and drain complete.
>
> With run ownership heartbeats enabled, terminal success requires acknowledgment
> from that worker's own durable write. A matching database row alone cannot
> confirm success, and completion metadata cannot retry a rejected terminal
> transition. Each run renews independently, so a stalled store operation does
> not delay other runs. If acknowledgment remains unavailable when the last
> confirmed lease expires, the worker stops conservatively even if its commit
> actually reached the database. Expired leases cannot be renewed.
> Interrupt-and-replace admission acknowledges only the old runs actually claimed
> by its atomic transaction. Rollback keeps renewing its acknowledged interrupted
> row until restoration and the separate final error commit finish. An
> active-only renewal that raced that admission gets one bounded retry after the
> interrupted acknowledgment, without weakening the owner or live-lease checks.
> A failed renewal leaves a local expiry guard armed. Shutdown bounds its wait for orphan
> recovery, but cancellation-resistant storage may still be using its resources.

>
> The local two-Gateway harness disables IM providers under both `channels` and `channel_connections` by default. `DEERFLOW_MI_KEEP_CHANNELS=1` preserves them; `channels.leader_lease` stays as configured.
>
> Cleaning up an in-memory run stream, or closing its bridge, releases retained
> payloads and signals a replay gap to subscribers with unfinished replay. They
> reload durable state instead of waiting on a detached buffer or consuming stale
> history. Established readers that fully consumed a terminal stream retain their
> normal `end` signal. A new reader whose initial attachment loses the race with
> cleanup receives a gap so it can recover the saved result.
>
> During SSE replay-gap recovery, the Web UI preserves a reconnect pointer claimed by another run while durable state is loading. An older recovery cannot overwrite that pointer when it rejoins its own stream. Even a stale foreign pointer is preserved, so the next reload may first check that run before active-run recovery rejoins, adding a reconnect cycle.
>
> Store-only SSE and `/wait` consumers can finish after a heartbeat when run-manager
> or scheduled-task reconciliation recovers a dead worker's run, even if no END
> marker was published. Ordinary completions still wait for END to preserve tail events.
>
> In single-process JSONL deployments, cancelling an admitted event-store mutation waits for its background file I/O, rollback, and bookkeeping to settle before releasing the thread write lock. This prevents an older cancelled write from recreating deleted records or rolling back a later successful write. Cancellation can therefore wait on slow storage; it does not stop an in-flight filesystem operation. Callers still waiting to acquire the lock can cancel without starting a mutation. A batch spanning multiple threads drains its current thread group before propagating cancellation; subsequent thread groups do not start.
>
> After a run publishes its terminal stream marker, its process-local `RunRecord` remains available for the existing five-minute grace period before cleanup; durable run history remains available through `RunStore`, while the stream bridge retains its delivery tail on its separate cleanup schedule.
>
> Run cancellation may land on any Gateway worker. A non-owning worker now persists the interrupt or rollback request for the live owner, which observes it during lease renewal and performs the normal cancellation flow; load-balancer routing alone no longer produces a 409. The first accepted action wins even if a retry lands on the owner, and accepted cancellation competes atomically with owner completion. Dead owners still follow lease takeover and orphan recovery. Cancellation latency is therefore bounded by the lease heartbeat interval.

> Cancelling a model recovery probe, including while it is queued or waiting to retry, lets the next call check whether the provider has recovered. Cancellation does not count as a provider failure or release another call's active recovery probe.
>
> Model retries honor valid provider `Retry-After` hints up to 24 hours, including waits longer than the local backoff cap. Malformed, non-finite, or over-limit hints use normal backoff instead. This applies to numeric and HTTP-date hints in LLM error handling and Codex's retry path, and integer-second hints in Claude's retry path. Codex prioritizes numeric `retry-after-ms` hints; past HTTP-date hints retry immediately.
>
> With lease heartbeat enabled, a transient RunStore renewal error is retried only until the last confirmed lease expires; the stale worker then cancels local execution and suppresses checkpoint, completion-hook, delivery-receipt, and thread-status finalization. A remote tool side effect already in flight may still be outside local cancellation.
>
> Reconciliation uses an atomic takeover claim that re-checks the lease after candidate selection, so a successful owner renewal wins over orphan recovery and only one reconciler can report a run as recovered. When multiple Gateway workers share the Docker/AIO or E2B sandbox backend, also configure `sandbox.ownership.type: redis`; E2B uses the leases during background startup and periodic reconciliation so duplicate/orphan cleanup cannot terminate a live peer's sandbox.

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed Docker development guide.

#### Upgrading an existing checkout

Keep `config.yaml`, `.env`, and `extensions_config.json`. Stop the services you
currently use, run `git pull --ff-only`, then start the same mode again. Do not run
`make config` or `make docker-init` again for a routine source upgrade. If the new
version requires configuration changes, run `make config-upgrade` before restarting.
See [Operations and Troubleshooting](frontend/src/content/en/application/operations-and-troubleshooting.mdx#upgrading-an-existing-checkout)
for the commands for each mode.

When rolling out the resume-command idempotency fix across multiple Gateway
workers or Pods, route **all keyed resume submissions and retries** (`command.resume`
with `Idempotency-Key`, on thread-scoped `/runs`, `/runs/stream`, or `/runs/wait`)
only to upgraded workers until every worker serving these endpoints is upgraded.
Older workers ignore the private resume identity and compare only `input`: with
`input: null`, retrying `deny` can incorrectly reuse an earlier `approve` run.
If the load balancer cannot isolate upgraded workers, pause keyed resume traffic
until the rollout finishes, or stop all old workers before restarting on the new
version. The additive database migration keeps old run-history readers compatible;
it does not make old workers safe for resume admission. An upgraded worker returns
409 when retrying an identity-less legacy resume run, even for the same decision;
inspect that run and the current thread state before deciding to submit a new
action. See the [run API contract](backend/docs/API.md#create-run).

Custom run stores must explicitly support every supplied idempotency field.
Keyed input and resume requests return HTTP 503 before run admission when the
store cannot guarantee that support. The built-in Memory and SQL stores support
both fields; older custom stores with an explicit `idempotency_key` parameter
continue to accept keyed input requests.

#### Option 2: Local Development

If you prefer running services locally:

Prerequisite: complete the "Configuration" steps above first (`make setup`). `make dev` requires a valid `config.yaml` in the project root. Set `DEER_FLOW_PROJECT_ROOT` to define that root explicitly, or `DEER_FLOW_CONFIG_PATH` to point at a specific config file. Runtime state defaults to `.deer-flow` under the project root and can be moved with `DEER_FLOW_HOME`; skills default to `skills/` under the project root and can be moved with `DEER_FLOW_SKILLS_PATH`. Run `make doctor` to verify your setup before starting.

Configuration checks and agent-storage migrations use the installed backend environment through `uv run --no-sync --project backend` from the repository root. This preserves relative runtime paths and installed optional dependencies; see the [setup checks](backend/docs/SETUP.md#steps) and [agent-storage migration](backend/docs/CONFIGURATION.md#agent-storage).

On Windows, run the local development flow from Git Bash. Native `cmd.exe` and PowerShell shells are not supported for the bash-based service scripts, and WSL is not guaranteed because some scripts rely on Git for Windows utilities such as `cygpath`.

The documented root `make` commands invoke repository `.sh` files through Bash
explicitly. They therefore continue to work from source archives or filesystems
that do not preserve POSIX executable bits. When calling a script directly from
such a checkout, use `bash ./scripts/<name>.sh ...`.

1. **Check prerequisites**:
   ```bash
   make check  # Verifies Node.js 22+, pnpm, uv, nginx
   ```

   The local `make check`, `make install`, `make dev`, and `make start` entry points use a direct `pnpm` executable when available and otherwise fall back to `corepack pnpm`. With native Windows Python, the shared runner checks `pnpm.cmd` before the generic `pnpm` lookup, which follows `PATH`/`PATHEXT` and may select an `.exe` or `.bat` in the same or an earlier PATH directory. The Corepack fallback likewise checks `corepack.cmd` before `corepack`. POSIX Python keeps the generic names first, including when running under MSYS/Cygwin. The runner and diagnostics resolve repository paths absolutely, so these checks work regardless of the caller's current directory. Corepack runs from `frontend/`, so it honors the `packageManager` version pinned in `frontend/package.json`; enabling a global pnpm shim is not required.

   `make check` decodes tool diagnostics as UTF-8 and preserves Unicode pnpm
   errors on non-UTF-8 hosts. Invalid output bytes are replaced so the checker
   can report dependency failures instead of aborting while decoding output.

2. **Install dependencies**:
   ```bash
   make install  # Install backend + frontend dependencies + pre-commit hooks
   ```

   Hook setup calls pre-commit through uv, so uv's tool directory need not be on `PATH`.

3. **(Optional) Pre-pull sandbox image**:
   ```bash
   # Recommended if using Docker/Container-based sandbox
   make setup-sandbox
   ```
   Reads the configured sandbox image from UTF-8 `config.yaml`, with or without a leading BOM, using LF or CRLF line endings.
   On macOS, a successful Apple Container pull completes this step even when Docker is not installed. If Docker is available, its image is also pulled.

4. **Start services**:
   ```bash
   make dev
   ```

5. **Access**: http://localhost:2026

6. **(Optional) Load sample memory data for local review**: open `Settings > Memory`, click **Import memory**, and select `backend/docs/memory-settings-sample.json`. The browser imports into the signed-in user's memory.

   To replace memory for every registered user in a disposable review environment:

   ```bash
   cd backend
   uv run python ../scripts/load_memory_sample.py --all-users
   ```

   Bulk mode supports SQLite/PostgreSQL user registries, creates timestamped backups under `.deer-flow/memory-sample-backups/`, and rejects the non-persistent `database.backend: memory` mode. See [backend/docs/MEMORY_SETTINGS_REVIEW.md](backend/docs/MEMORY_SETTINGS_REVIEW.md) for the complete review flow.

Local services always use their internal ports (`8001`, `3000`, and `2026`).
The root `.env` variable `PORT` configures only the published Docker ingress;
it does not change the Next.js port used by `make dev`.

Local startup waits up to 30 seconds for the Gateway port. On a slow cold start,
set a longer wait without editing the launcher:

```bash
DEER_FLOW_GATEWAY_STARTUP_TIMEOUT=240 make dev
```

The value must be a positive integer in seconds. You can also set it in the
root `.env`, whose value takes precedence over the shell. It applies to local
`make dev`, `make start`, and their daemon variants, not Docker health checks
or LLM request timeouts. Check `logs/gateway.log` for startup errors before
increasing the wait; an expired deadline still stops the services.

#### Startup Modes

DeerFlow runs the agent runtime inside the Gateway API. Development mode enables hot-reload; production mode uses a pre-built frontend.

| | **Local Foreground** | **Local Daemon** | **Docker Dev** | **Docker Prod** |
|---|---|---|---|---|
| **Dev** | `./scripts/serve.sh --dev`<br/>`make dev` | `./scripts/serve.sh --dev --daemon`<br/>`make dev-daemon` | `./scripts/docker.sh start`<br/>`make docker-start` | — |
| **Prod** | `./scripts/serve.sh --prod`<br/>`make start` | `./scripts/serve.sh --prod --daemon`<br/>`make start-daemon` | — | `./scripts/deploy.sh`<br/>`make up` |

| Action | Local | Docker Dev | Docker Prod |
|---|---|---|---|
| **Stop** | `./scripts/serve.sh --stop`<br/>`make stop` | `./scripts/docker.sh stop`<br/>`make docker-stop` | `./scripts/deploy.sh down`<br/>`make down` |
| **Restart** | `./scripts/serve.sh --restart [flags]` | `./scripts/docker.sh restart` | — |

Local and Docker development stop commands also stop running sandbox containers
whose names start with `deer-flow-sandbox-`. Containers with that text elsewhere
in their names are left alone.

`make start` and `make start-daemon` rebuild the frontend with `next build` on
every run. To reuse the last build instead, pass `SKIP_FRONTEND_BUILD=1` (or add
`--skip-frontend-build` when calling `./scripts/serve.sh --prod` directly). This
is opt-in: it fails fast when `frontend/.next` has no completed build.

Gateway owns `/api/langgraph/*` and translates those public LangGraph-compatible paths to its native `/api/*` routers behind nginx.

Cold agent imports during run creation use a dedicated worker pool, keeping
unrelated Gateway requests responsive while the agent stack loads. A failed
factory import prevents the run from being admitted.

For a read-only demo without the Gateway, run `make build-static` from `frontend/`,
then `HOSTNAME=127.0.0.1 PORT=3000 node --env-file=.env .next/standalone/server.js`
from the same directory. The build includes public demo assets and resolves
supported demo API reads locally; writes are unavailable. To display the homepage
GitHub star count, set `GITHUB_OAUTH_TOKEN` in `frontend/.env` before starting Node.
The token stays on the server; missing credentials or GitHub failures hide the
count. Restart Node after changing the token; no rebuild is needed.

#### LangGraph Studio (Optional)

The default `make dev` topology uses DeerFlow's Gateway-embedded runtime and
does not require LangGraph Studio. To inspect and test the registered lead-agent
graph with the standalone development server, run the command from `backend/`
so the CLI discovers `langgraph.json`:

```bash
cd backend
uv run langgraph dev --allow-blocking
```

The command prints the local API and Studio UI URLs. This in-memory server is
for development and testing only. The flag permits DeerFlow's synchronous
configuration and graph-factory setup during local Studio requests; it must not
be treated as a production-server setting. Local Studio authentication is
handled automatically, so the connection does not require custom headers. Use
DeerFlow's documented production startup modes or a supported LangSmith
deployment for production workloads. Assistant ownership and provenance in this
standalone mode are server-owned: Studio can discover registered graphs and the
assistants it creates, and normal assistant-version selection remains available.
Before the locked local runtime loads its persisted development store, DeerFlow
repairs legacy assistant rows and version history so historical client metadata
cannot restore server privileges or be discarded by the runtime's startup
cleanup. Keep the backend dependencies synchronized with `uv sync`; this
compatibility path requires the declared LangGraph runtime versions and logs a
warning if the persisted-store contract no longer matches its expectations.
The documented command uses LangGraph's file-based custom-app loader, which is
also covered directly by DeerFlow's regression tests.

Standalone runs using `if_not_exists="create"` retain config and run metadata
on the newly created thread, including searchable tags; run metadata takes
precedence for duplicate keys. Thread ownership and MCP incarnation remain
server-owned, and later runs do not replace the thread's creation metadata.

For workflows that invoke `backend/langgraph.json` through LangGraph Studio or
a direct LangGraph Server, DeerFlow consumes the authenticated identity
published by that runtime and uses it for custom-agent configuration/SOUL, user
skills and skill policy, uploads, thread data, and memory reads/writes. This
keeps authenticated runs out of the shared `default` filesystem bucket, and the
server-owned identity takes precedence over ordinary client-supplied `user_id`
values. External identities such as email addresses are mapped to stable,
collision-resistant directory-safe user IDs before accessing DeerFlow storage.
The default DeerFlow service topology remains the Gateway-embedded runtime
described above.

Gateway runs automatically enforce native delivery for artifacts created or modified under `/mnt/user-data/outputs`: `present_files` must present at least one output produced by the current run, and the terminal `run.delivery` receipt must be durably recorded. Virtual artifact paths are resolved within the same authenticated user and thread scope that produced the output before the output-directory boundary is validated. Runs that do not produce output artifacts keep ordinary conversational behavior.

Thread-scoped `runs.wait()` calls that finish with `status: error` report the current run error instead of an earlier answer. The asynchronous Python LangGraph SDK raises by default; pass `raise_error=False` to inspect the returned status and error.

DeerFlow's built-in custom events are available through both LangGraph streaming interfaces: native clients can continue subscribing to `stream_mode="custom"`, while callback-based integrations can consume the same payloads as `on_custom_event` records from `astream_events(version="v2")`. The callback event name matches the payload's `type` field.

#### Docker Production Deployment

`./scripts/deploy.sh` supports building and starting separately:

```bash
# One-step (build + start)
./scripts/deploy.sh

# Two-step (build once, start later)
./scripts/deploy.sh build       # build all images
./scripts/deploy.sh start       # start pre-built images

# Stop
./scripts/deploy.sh down
```

### Advanced
#### Sandbox Mode

DeerFlow supports multiple sandbox execution modes:
- **Local Execution** (runs sandbox code directly on the host machine)
- **Docker Execution** (runs sandbox code in isolated Docker containers)
- **Docker Execution with Kubernetes** (runs sandbox code in Kubernetes pods via provisioner service)

In Local Execution, `glob` and `grep` can search the skills root (default
`/mnt/skills`) across its mounted categories. Patterns stay relative to that
root, and one result limit covers all categories. User isolation, disabled-skill
filtering and read-only mounts still apply. Configured category mounts such as
`build` or `logs` remain searchable; ignore rules apply inside each mount. A broken
category mount stops the root search, and the Gateway warning log identifies its
virtual path.

Sandbox references in conversation state are server-owned. External run and
thread-state APIs reject caller-supplied `sandbox` values; when restoring a
checkpoint, the runtime resolves the reference against the authenticated user
and thread before a tool can reuse it. A missing runtime thread ID raises an
error even when the referenced sandbox is cached.

When host Bash is enabled for Local Execution, DeerFlow starts OS detection with `uname -s`, then uses `sw_vers` on Darwin. On Linux, it reads host system files such as `/etc/os-release` only when the active sandbox policy permits it. Host filesystem path checks still apply; after a blocked path, the agent is directed to use a permitted command-only probe or virtual path instead of repeating the rejected command.

For Docker development and production, service startup follows the configured
sandbox mode. With `AioSandboxProvider`, an omitted `provisioner_url`, an empty
string (`""` or `''`), or YAML null (`null`, `~`, or a blank value), including
trailing comments, selects `aio`: `provisioner` is not started and the Docker
socket overlay is enabled. This grants the gateway host root-equivalent Docker
access; see the [sandbox security notes](backend/docs/CONFIGURATION.md#sandbox-isolation-and-the-docker-socket-dood).
A nonempty URL selects provisioner mode without that overlay. Quoted `"null"`
and `"~"` are nonempty strings, not YAML nulls; mode detection does not validate
URLs. The default local provider never enables the socket overlay.

Local AIO sandbox port allocation stops at TCP port 65535. If the remaining
ports from the configured starting port are occupied, allocation reports
that no port is available instead of attempting an out-of-range bind.

AIO teardown failures retain a generation-bound cleanup record. Partial shutdown
reports failure and can be retried; retries verify the runtime identity and absence
before completing cleanup. Healthy replacements with the same logical ID remain
reusable, including after background recovery into the warm pool.

See the [Sandbox Configuration Guide](backend/docs/CONFIGURATION.md#sandbox) to configure your preferred mode. For absolute skills paths and custom directory mappings on Linux, macOS, Windows, WSL, or a Docker Gateway, see [Skills and sandbox paths](backend/docs/CONFIGURATION.md#skills-and-sandbox-paths).

Managed async AIO runs can opt into bounded sandbox prewarming to overlap startup
with the first model call. Direct SDK graphs keep lazy acquisition. It defaults off; see the guide and
[sandbox benchmarks](backend/scripts/benchmark/sandbox/README.md) before enabling it on a shared host.

Remote directory listings report traversal failures (for example, unreadable
directories) as incomplete results, even when no entries were returned. A
missing start path is reported separately as “Directory not found.”

The optional [Tenki cloud sandbox provider](backend/packages/harness/deerflow/community/tenki/README.md)
uses Tenki SDK 1.4.0 or newer. Timed-out commands preserve partial output and
report `Exit Code: 124`; unsuccessful health checks cannot reclaim a warm sandbox.
Health probes tolerate login-shell output around the `ok` line, and failures log
the sandbox ID and probe output before replacing the sandbox.

The optional OpenSandbox provider mirrors generated output files to local thread
storage at turn completion for Gateway previews and downloads; see its
[synchronization limits and failure behavior](backend/packages/harness/deerflow/community/opensandbox/README.md#lifecycle-and-contract).
An invalid UTF-8 filename is skipped without blocking other outputs, and
same-size content edits are still copied on release.
Outputs with case- or Unicode-equivalent file or directory names are skipped
before copying, and aliases of existing local paths are rejected, preserving
previous complete copies.

The [sandbox benchmark](backend/scripts/benchmark/sandbox/README.md#opensandbox)
also supports OpenSandbox cold acquisition, warm reuse and concurrent scopes,
using the configured service connection and reporting unconfirmed cleanup as a
failed run. Live runs require a disposable OpenSandbox service and runtime home.

BoxLite shutdown rejects late VM registration and keeps its SDK loop open while
in-flight acquisitions finish. If they cannot drain within five seconds,
shutdown fails with resources still owned and can be retried.

#### MCP Server

In the chat UI, enable **Token Usage → Debug** to inspect generic/MCP tool calls.
Each **Tool details** panel starts collapsed and shows the tool name, call ID,
input, and received result or explicit error. Large previews are truncated;
fields whose names exceed the remaining preview budget are omitted rather than renamed.
Structured previews retain complete JSON syntax, including escaped strings and closing delimiters.
Array previews stop when the text budget cannot display another element; literal ellipsis values are preserved.
Consecutive generated markers at an array's end share one ellipsis indicating an omitted suffix; markers before later values retain their positions.
Text results retain their original representation, including large numeric IDs and duplicate JSON keys, without reparsing. Text exceeding the limit is shown as a prefix with a truncation notice; structured objects and arrays are formatted separately.
Copy actions copy only the displayed preview. This is a frontend view of data
already received by the browser, without an additional secret-redaction layer.

In plan mode, malformed TODO statuses return normal tool-validation errors without aborting token attribution, so the agent can correct the call.

Tool-produced paths and URLs can be retained as short artifact handles across context compaction (`tool_artifacts` in `config.yaml`). Handles distinguish separate tool-result occurrences, even when a provider reuses call IDs. Standard MCP image URLs are captured alongside file references, including results from stdio and HTTP servers. Detected file URLs preserve their query strings and fragments. Free-text sandbox paths retain spaces inside matching ASCII quotes, backticks, or curly quote pairs, including backslash-escaped wrappers. Unterminated spans and delimited values containing a line break or tab are skipped. Free-text artifact references retain balanced ASCII and CJK brackets in literal paths and URLs while trimming surrounding prose punctuation. When PII redaction is enabled, model-visible artifact labels follow that policy; internal references stay intact for tool argument resolution. The configured registry limit retains the newest artifacts, while checkpointed processing identities prevent evicted results from being recaptured after restart. Resolution runs before authorization and write-safety checks; unknown or expired handles return an error without executing the tool. Small unknown structured results may be retained as complete JSON up to 4096 UTF-8 bytes; empty or oversized payloads are skipped. Handles are agent-local: task arguments resolve parent handles to concrete references, and delegated reports must return concrete references rather than child-local handles. A truncated model projection reports how many handles are omitted.

DeerFlow supports configurable MCP servers and skills to extend its capabilities.
When durable MCP background tasks are enabled, agents can use `list_background_tasks(status="failed")` or `status="input_required"` to find failed tasks or tasks awaiting input in the current chat. Other supported statuses are `submitted`, `working`, `completed`, and `cancelled`; omitting the status preserves existing behavior. The database applies the filter before limiting results to the 20 most recent matching tasks. When combined with `active_only=true`, both filters apply: active statuses are `submitted`, `working`, and `input_required`, so terminal statuses return an empty list. `GET /api/threads/{thread_id}/mcp-tasks` supports the same `status` and `active_only` filters before its `limit` (default 50, range 1–100); for example, `?status=failed&limit=20`. Unknown statuses return 422, and omitting the filters preserves the existing response.
For HTTP/SSE MCP servers, OAuth token flows are supported (`client_credentials`, `refresh_token`).
Missing, malformed, or out-of-range token response `expires_in` values use a one-hour default lifetime. This includes lifetimes that cannot be added to the current time without overflowing the expiry timestamp.
Durable HTTP/SSE task status and cancellation calls select configured `user_auth` credentials using the persisted task owner, including after restart; per-request secrets are not retained for background calls. If a request-scoped credential overrides submit authentication, both credentials must authorize access to the same remote task.
For stdio MCP servers, per-tool call timeouts can be configured with `tool_call_timeout`; durable background-task calls honor the same setting for HTTP/SSE servers as well.
Durable background-task status and cancellation calls renew their claims while they run, so a slow response can still be saved after the original lease duration. If ownership is lost or renewal cannot be confirmed, the worker stops its local call and leaves recovery to the durable state. See [control-call leases](backend/docs/mcp-control-leases.md) for recovery and shutdown behavior.
The persistent stdio session pool evicts only idle sessions at capacity. If every pooled session is executing a tool, a new session request fails with a capacity error and can be retried after a call finishes.
For stdio file outputs, a bare filename is linked to a uniquely matching file created or changed by that call. Filenames embedded in unrelated paths, including Windows backslash paths, are left intact. Explicit remote URLs (`scheme://...`) retain their original query parameters and fragments even when these contain a generated file's name or path, including URLs with backslash-escaped quotes or markup delimiters; local references outside the URL still translate normally.
For HTTP/SSE background-task calls, `session_init_timeout` separately bounds connection setup (including the SSE endpoint event) and MCP initialization together; it stops applying once the tool call begins. Initialization deadline errors identify the server and configured time limit.
Ordinary `task` subagents retain the parent run's captured thread incarnation for MCP calls, including legacy threads, so delegation preserves the same lifecycle scope.
MCP tool names are prefixed with `<server_name>_` by default to prevent collisions across servers. If a server already namespaces its own tools, set `tool_name_prefix: false` on that server in `extensions_config.json` to keep the original names. Disable the prefix only when the resulting names remain unique across all enabled servers.
Signed-in users' notification toggle, default model, conversation mode, and reasoning effort are saved to their account and restored on other browsers or after clearing browser storage. Browser notification permission still needs to be granted on each device. Changes retry after network failures; unsent changes survive a reload in the same tab. Concurrent edits to different fields are preserved; for the same field, the last server write wins. Existing unscoped browser preferences are not uploaded automatically because they have no account owner; reselect those settings once after upgrading. Static demos and auth-disabled development keep browser-local settings. Thread-specific model overrides and other display preferences remain local.

In a new chat, the submitted question stays above its streamed reasoning and
tool steps while the server creates the conversation and confirms the message.

Markdown and JSON conversation exports from the chat header or sidebar read all
persisted history pages, including earlier turns outside the loaded view or
compacted model context. A failed history read stops the export instead of
downloading a partial transcript. Public demos export their bundled messages.

Capability Center groups plugins by office collaboration, documents and knowledge, search and research, business and data, and development and operations. The directory includes setup references alongside existing MCP configurations and Lark. Recommended integrations and built-in support do not imply an installed or verified connection; the Installed filter shows configured MCP entries and installed Lark only.

Personal MCP connections configured in the web interface are persisted per user.
Unexpected failures when changing deployment or personal MCP configuration return fixed error messages; exception details stay in server logs.
Deployment tools remain shared. Administrators can add, edit, enable, disable and delete shared MCP servers under **Platform provided**; ordinary users see their status without controls. Personal plugin switches affect only the signed-in user's connections. See [connection ownership](docs/capability-center.md#personal-and-deployment-mcp-configuration).

For plugin manifests, adapter registration, and Agent capability selection, see
[Capability Center integration contract](docs/capability-center.md).

DingTalk and WeCom group notifications and HubSpot CRM are bundled configurable
plugins. Administrators supply robot credentials or a HubSpot private app token;
Agents can then send requested group notifications, list companies, or create
contacts. Saving configuration performs no external write. These plugins reuse
the existing MCP lifecycle and require no separate plugin service. See the
integration contract above for required fields, scopes, and feature boundaries.

Plugin brand icons are bundled locally. When adding or editing one personal MCP plugin, users can upload a PNG, JPG, or WebP image (up to 2 MB), preview it, or restore the default icon. Changes take effect only after Save; custom icons persist across browsers as a normalized 128px PNG in the server entry's display-only `presentation.icon` metadata. They are not sent to the MCP transport.

Capability Center > Plugins adds, replaces, and deletes one MCP server at a time through targeted mutations that preserve concurrent sibling changes; deletes use a bodyless URL-addressed request. An invalid stdio command on one server no longer blocks toggling another, while enabling that invalid server remains protected by the command allowlist and surfaces the backend validation message in the UI.
Targeted updates accept both DeerFlow's `type` field and the MCP-spec `transport` field for SSE/HTTP servers.
Runtime MCP and skill updates replace `extensions_config.json` atomically, so an interrupted write cannot leave the shared configuration truncated or partially written. Every Gateway worker or instance that reads the same file picks up a new revision on its next read (the cache checks the file's content signature), so MCP and skill changes made through one replica apply to the others without a restart; a missing, truncated, or invalid revision keeps the previous configuration until a complete one lands, including when the file disappears during a reload.
The admin MCP cache reset advances a durable generation marker in the writable config directory. Every Gateway worker mounting that same directory retires its own cached tools and pooled sessions before the next lookup; replicas with independent filesystems are not implicitly covered. If no config path is available, the API reports a process-local reset instead.
The parsed extensions configuration and its recorded content digest come from the same read, so a racing edit followed by a timestamp-preserving backup restore cannot leave a different revision cached indefinitely.
Changes to the global `mcpInterceptors` chain rebuild every server's tool wrappers,
including when a server configuration is edited at the same time.

`extensions_config.json` accepts UTF-8 with or without a leading byte-order mark (BOM), including files saved as UTF-8 with BOM by an editor.

When deferred MCP tool discovery is enabled, `tool_search` supports opt-in literal keyword queries such as `keywords:notebook jupyter`. Keywords match names and descriptions in any order, ranked by distinct term coverage and then name hits; ties retain catalog order. This mode uses the first 256 characters after the prefix and at most 16 unique whitespace-separated terms, returning up to five tools. Punctuation stays literal. Bare queries and `+required` ranking keep their existing regular-expression semantics; `select:tool_a,tool_b` still fetches all exact, case-sensitive name matches.

MCP routing hints can also prefer a specific MCP tool for matching requests without forbidding other tools. When `tool_search` defers MCP schemas, matching routing metadata can auto-promote up to `tool_search.auto_promote_top_k` deferred schemas before the model call.

Deferred MCP schema promotions last for the current user turn. They remain active across that turn's model/tool loop and checkpoint resume, then become deferred again when a new user message starts the next turn; the next turn must discover them again through `tool_search` or match their routing hints. Resuming a legacy in-flight checkpoint preserves previously searched tools even when routing hints also match that turn.

Deferred `tool_search` regex queries share a 100 ms execution budget across the catalog, including `+required` ranking. Patterns are limited to 256 characters and searchable names/descriptions to 65,536 characters each. Queries that exceed a limit return a retry hint without promoting partial results; use a simpler pattern, `keywords:`, or `select:` with exact names. Oversized catalog fields are reported with the tool name, field and length, and logged with the MCP server name when available; use `keywords:` or `select:` because simplifying the pattern cannot shrink a catalog field. Exact selection remains uncapped and bypasses regex limits; the literal `keywords:` mode also bypasses regex limits. Invalid regex syntax still falls back to a literal substring match.

OpenViking users can register the official Streamable HTTP endpoint at `/mcp`
with an owner-bound USER API key. The native `forget` tool is exposed for
capability parity; deletion is irreversible, so it should be called only after
explicit user confirmation. DeerFlow does not enforce that confirmation. This
explicit, model-selected MCP tool path can run alongside the separate automatic
OpenViking memory backend; it does not replace automatic turn capture or recall. See the
[OpenViking MCP tools configuration](backend/docs/MCP_SERVER.md#openviking-mcp-tools).

The Gateway can adapt an MCP server's ordinary `submit` / `status` / `cancel` tools into durable background tasks. The Agent sees only the configured submit tool and a DeerFlow-local task ID; remote IDs are persisted before the submit call returns, while status and cancel stay internal to the runtime. Polling uses cross-worker leases, exponential retry backoff, scoped MCP sessions, bounded result storage, and restart recovery. A status-tool `isError` is retained as a bounded diagnostic and retried; servers report a permanent remote-task outcome through a normal structured result with `status: "failed"`. Remote poll hints are finite positive numbers capped at 24 hours, artifact-reference JSON is limited to 64 KiB, and task/server identifiers are validated against their durable SQL column limits before persistence. Input-required and terminal updates wake the current chat through idempotent Agent runs, while `list_background_tasks` and `cancel_background_task` let the Agent manage tasks without asking users for remote handles. Current-thread tasks are available through `GET /api/threads/{thread_id}/mcp-tasks`, its detail endpoint, and `POST /api/threads/{thread_id}/mcp-tasks/{task_id}/cancel`; when the task runtime actually starts, the Web UI exposes the same safe local view from the chat header with live status refresh, cancellation, and on-demand result, artifact, input-request, status-error, and cancellation-retry details. Default-disabled and memory-backend deployments hide that UI and do not poll the task endpoints. A failed remote cancellation remains queued with backoff, and its latest bounded error and attempt count stay visible in the expanded task card. Enable `mcp_tasks` in `config.yaml`, configure `task_toolsets` with exact raw tool names in `extensions_config.json`, and use a SQL database backend (`sqlite` or `postgres`). Task-enabled server connection, authentication, interceptor, timeout, or binding changes require a Gateway restart so Agent tool discovery and background calls cannot use different configuration versions. `input_required` is notification-only for now: DeerFlow can display the request but cannot yet submit the user's answer back to the remote task.

For deployment-level HTTP/SSE servers with `task_toolsets`, discovery, ordinary
tools, and background task calls share OAuth token state within one Gateway
process, including across tool-cache resets. Rotated refresh tokens stay in
memory; they are not written back to configuration or shared across processes.
After a restart, the configured refresh token must still be valid.

Notification launch and failed Agent-run deliveries use capped exponential backoff with a visible attempt count and stop after five failed attempts. When a bounded ordinary release exceeds its drain deadline, the service retains ownership until it settles. A permanently rejected target such as a deleted chat is dead-lettered immediately instead of retried forever or recreated. Cancellation endpoints return after durably recording the request; the background service owns the potentially slow remote MCP call and its retry schedule.

Notification runs keep their trusted delivery instruction separate from the framed, untrusted remote event payload. The process-started task runtime—not a hot config read—controls whether the task-management tools are exposed, so changing `mcp_tasks` requires a Gateway restart. `list_background_tasks` and `cancel_background_task` are ordinary business tools governed by the agent's own authorization, like every other tool.
See the [MCP Server Guide](backend/docs/MCP_SERVER.md) for detailed instructions.

Security: pass per-request MCP credentials only through `config.context.secrets`;
credentials must never be placed in either run metadata surface
(`metadata.auth_token` or `config.metadata.auth_token`). See [MCP credential migration and cleanup](backend/docs/MCP_SERVER.md#migrating-legacy-mcp-credentials)
for the supported interceptor flow and the required rotation and retained-copy
cleanup when migrating from legacy metadata credentials.

#### IM Channels

DeerFlow supports receiving tasks from messaging apps. Channels auto-start when configured — no public IP required for any of them.

Cancelling a channel restart discards its pending configuration reload, preserving newer runtime settings applied afterward.

Invalid UTF-8 in `channels/store.json` follows the same recovery policy as malformed JSON:
SQL migration warns and skips the file, leaving it unchanged so channels can start; the
memory backend's JSON store warns and starts empty, replacing the file on its next write.

Conversation-binding, runtime channel-credential and WeChat auth-state saves preserve the original
persistence failure when staged-file cleanup also fails. Remaining cleanup still runs, and warnings
identify copies that could not be removed. Buzz keeps failed snapshots available for retry, even if
cleanup or logging fails.

On startup, runtime credential and WeChat auth stores remove their own `.<state-file>.deerflow-*.tmp`
staging files older than 24 hours. Fresh files, symlinks and unrelated files are preserved. Older
anonymous `tmp*.tmp` files require manual inspection because their writer cannot be identified safely.

DeerFlow can also expose user-owned IM channel connections in the workspace UI. When `channel_connections` is enabled, logged-in users can bind Telegram, Slack, Discord, Feishu/Lark, DingTalk, WeChat, WeCom, QQ, or Buzz from the sidebar / Settings > Channels. It reuses the existing outbound `channels.*` transports, so no public IP or provider callback URL is required. Incoming IM messages then run under the connected DeerFlow user account. See [IM Channel Connections](backend/docs/IM_CHANNEL_CONNECTIONS.md) for setup and security notes. Buzz backlog paging stops with a warning if timestamp-based queries cannot advance, and channel removal closes both live and backlog subscriptions.

For Discord and Buzz, the local and Docker launchers detect the required optional
dependencies when both `channel_connections.enabled` and the corresponding
`channel_connections.<provider>.enabled` are `true`. Selecting Discord in
`make setup` sets these flags. A nonempty `UV_EXTRAS` overrides configuration
auto-detection, so include `discord` or `buzz` there if you set it manually.

| Channel | Transport | Difficulty |
|---------|-----------|------------|
| Telegram | Bot API (long-polling) | Easy |
| Slack | Socket Mode | Moderate |
| Feishu / Lark | WebSocket | Moderate |
| WeChat | Tencent iLink (long-polling) | Moderate |
| WeCom | WebSocket | Moderate |
| QQ | WebSocket (text-only C2C and group @mentions; four/five passive replies per source) | Moderate |
| DingTalk | Stream Push (WebSocket) | Moderate |
| Buzz | Nostr relay (WebSocket, NIP-42) | Moderate |

Attachments saved by the shared IM ingestion pipeline or Feishu/DingTalk's
embedded downloads keep distinct filenames, including when concurrent uploads
choose the same name. The final filename is passed to the agent and used for
sandbox sync; an existing conversation file is not overwritten.

Feishu and DingTalk attachment transfers return standalone temporary sandboxes
to the pool after synchronization, without interrupting an active run.

**Configuration in `config.yaml`:**

Discord's `channels.discord.allowed_guilds` accepts one positive numeric guild
ID (quoted or unquoted) or a YAML list. Unset, `null`, `[]`, or a blank string
allows all guilds. Invalid entries are ignored with a warning; any other
configured value yielding no valid ID denies every guild and logs an error.
`allowed_channels` accepts one channel ID (quoted or unquoted) or a YAML list
of IDs exempt from `mention_only`, within allowed guilds. An empty value gives
no exemptions, so `mention_only` applies everywhere when enabled.

Discord inbound attachments have a 25 MiB download limit. Oversized-file notices
show the enforced limit so senders can resize or compress the attachment.

```yaml
channels:
  # LangGraph-compatible Gateway API base URL (default: http://localhost:8001/api)
  langgraph_url: http://localhost:8001/api
  # Gateway API URL (default: http://localhost:8001)
  gateway_url: http://localhost:8001

  # Maximum queued or provider-reserved inbound messages (default: 1000)
  inbound_queue_maxsize: 1000
  # Fixed number of long-lived inbound handler workers (default: 5)
  max_concurrency: 5
  # Seconds to drain accepted work before cancelling active handlers (default: 3)
  shutdown_grace_period_seconds: 3

  # Optional: global session defaults for all mobile channels
  session:
    assistant_id: lead_agent  # or a custom agent name; custom agents are routed via lead_agent + agent_name
    config:
      recursion_limit: 100
    context:
      thinking_enabled: true
      is_plan_mode: false
      subagent_enabled: false

  feishu:
    enabled: true
    app_id: $FEISHU_APP_ID
    app_secret: $FEISHU_APP_SECRET
    # domain: https://open.feishu.cn       # China (default)
    # domain: https://open.larksuite.com   # International

  qq:
    enabled: true
    app_id: $QQ_APP_ID
    client_secret: $QQ_CLIENT_SECRET
    allowed_users: []  # QQ OpenIDs, not QQ account numbers; empty allows all; one ID is one entry

  wecom:
    enabled: true
    bot_id: $WECOM_BOT_ID
    bot_secret: $WECOM_BOT_SECRET
    # Optional: extra host suffixes inbound media downloads may come from, in
    # addition to the built-in qq.com family and WeCom's official COS media
    # host (ww-aibot-img-1258476243.<region>.myqcloud.com); add one here if
    # WeCom rotates to a new COS account or media goes through a proxy
    allowed_media_hosts: []

  slack:
    enabled: true
    bot_token: $SLACK_BOT_TOKEN     # xoxb-...
    app_token: $SLACK_APP_TOKEN     # xapp-... (Socket Mode)
    allowed_users: []               # empty = allow all

  telegram:
    enabled: true
    bot_token: $TELEGRAM_BOT_TOKEN
    