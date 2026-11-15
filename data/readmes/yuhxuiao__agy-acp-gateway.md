# agy-acp-gateway

<p align="center">
  <strong>High-Performance, Pure-Go Multi-Protocol API Gateway & Real-Time Observability Suite for Google Antigravity CLI (<code>agy acp</code>)</strong><br/>
  <strong>基于 Google 官方 <code>agy acp</code> 的纯 Go 高性能多协议网关与实时可观测面板</strong>
</p>

<p align="center">
  <a href="#english">English</a> •
  <a href="#简体中文">简体中文</a> •
  <a href="#architecture--core-capabilities">Architecture</a> •
  <a href="#quick-start--快速开始">Quick Start</a> •
  <a href="#api--client-configuration--客户端接入">Client Config</a> •
  <a href="#upstream-maintenance--safe-upgrade--上游安全升级">Safe Upgrader</a>
</p>

---

<a name="english"></a>

## English

`agy-acp-gateway` is a zero-CGO (`CGO_ENABLED=0`), single-binary Go gateway that turns the official Google Antigravity CLI (`agy acp`, JSON-RPC 2.0 over stdio) into standard **Anthropic Messages (`/v1/messages`)**, **OpenAI Chat Completions (`/v1/chat/completions`)**, **OpenAI Responses (`/v1/responses`)**, and **Google Gemini REST (`/v1beta/models/...`)** HTTP/SSE endpoints.

Unlike naive HTTP/OAuth proxies that reverse-engineer private Google protobuf endpoints and risk immediate account suspension, `agy-acp-gateway` communicates **exclusively through the official `agy acp` process**. All TLS fingerprints, OAuth token refreshes, checkpointing, and context management remain 100% inside the official binary. This reduces protocol-level risk; it is not a guarantee against account restrictions, which still depend on the upstream terms of service and how the account is used.

### Key Highlights

1. **Quad-Protocol Native Compatibility**:
   - **Anthropic `/v1/messages` & `/v1/messages/count_tokens`**: Full support for Claude Code, including streaming `thinking` + `signature` blocks, `tool_use` / `tool_result` parking & resumption, `max_tokens` truncation propagation, and prompt cache hit accounting.
   - **OpenAI `/v1/chat/completions`**: Full support for Cursor, Cline, Continue, and standard OpenAI SDKs (`reasoning_content`, `reasoning_tokens`, `tool_calls`, `finish_reason: "length"`, streaming `include_usage`).
   - **OpenAI `/v1/responses`**: Native Codex CLI / Responses API compatibility (streaming & non-streaming `reasoning` output items, `response.reasoning_summary_text.delta`, `reasoning_tokens`, `response.function_call_arguments.delta`, `incomplete` `max_output_tokens` handling, and `previous_response_id` stateful resumption).
   - **Google Gemini `/v1beta/models/...`**: Native support for `@google/genai` SDK, `gemini-cli`, and upstream Gemini pass-through proxies (`:generateContent`, `:streamGenerateContent?alt=sse`, `:countTokens`, `thinkingConfig`, `MAX_TOKENS`, and `functionCall` / `functionResponse` with or without explicit call IDs).
2. **Real-Time SQLite `gen_metadata` Accounting, Dual TPS & Quota Guardrails**:
   - Directly decodes the `gen_metadata` and `steps` protobuf blobs from `agy`'s per-session SQLite database (`modernc.org/sqlite` read-only fast path, **0.44 ms/op**).
   - Tracks `LastSeenGenMetaIdx` independently of `LastSeenDbStepIdx`, delivering exact per-turn input/cached/output token billing, aligned streaming TTFT, time-weighted end-to-end throughput (`tps`), and pure post-TTFT streaming decode speed (`decodeTps`, `.1.12`).
   - Built-in quota bleed protections: caps orphan `tool_use` MCP relays (`AGY_MAX_TOOL_RELAYS=2`, `AGY_PARKED_TTL_SEC=300`) by hibernating abandoned sessions while preserving `session/resume` state for late `tool_result` recovery, and emits non-blocking `X-Agy-Cache-Warning` alerts when `>=200K` context sessions hit consecutive zero-cache steps.
3. **Deterministic `.1.19` Endpoint Routing Telemetry & Canary Visibility**:
   - Extracts the authoritative upstream `servedModel` (`gen_metadata` `.1.19` `modelVersion`) on every turn, exposing `X-Agy-Served-Model` response headers and surfacing canary/variant endpoints in the dashboard without disrupting warm `gemini-4-carbon` sessions, while transparently recovering `gemini-4-argon` shadow-pool (`gemini-4-argon-b`) sessions.
4. **900K Context Unlock, Sibling Tool Batching & Cache-Preserving MCP Bridge**:
   - Includes a deterministic binary patcher (`scripts/agy_upgrade.py`, verified through `agy 1.5.9`) that unlocks the 900K context window (`900,000` input tokens vs. the default `256,000` cap) while preserving binary section sizes.
   - Pre-batches sibling MCP tool calls from `CortexStepPlannerResponse` (`.20.7`) into single multi-tool HTTP turns (eliminating split `0/0` relay turns), enforces a zero-trust structured `session/request_permission` gate (`allow_once`), and handles mid-session deferred MCP tool additions in-place via `[Host tool update]` + `dsh_call_tool` (persisting `InitialToolsCatalog` across gateway restarts so 400K+ implicit prefix caches stay intact).
5. **Post-Compaction Session Continuity & Warm Hibernation (`session/resume`)**:
   - Dual-key identity routing (`sid:` / `fp:` + tenant isolation) with full 64-bit historical message digest matching: when clients compact middle turns, the gateway seamlessly retains the canonical session and triggers a single clean context rollover.
   - Idle workers hibernate via ACP `session/close` and wake in **~0.25s** via `session/resume` without replaying historical stdout chunks.
6. **Dual-Port Isolation & Editorial Warm-Paper Telemetry Console**:
   - **Port `18890` (API Gateway)**: `/v1/messages`, `/v1/chat/completions`, `/v1/responses`, `/v1/models`, `/v1beta/models/*`, `/healthz`.
   - **Port `18891` (Dashboard & Prometheus Metrics)**: Real-time warm-paper telemetry UI (`/`, `/api/dashboard`, `/api/upgrade`, `/health`) and monotonic SQLite-backed Prometheus metrics (`/metrics`) with live worker pool cards, calibrated official `/usage` 5h/weekly pool gauges, canary/cache alerts, and one-click `agy` hot-switch approval.

---

<a name="简体中文"></a>

## 简体中文

`agy-acp-gateway` 是一个**零 CGO 依赖 (`CGO_ENABLED=0`)、单二进制**的高性能 Go 网关，将 Google 官方 Antigravity CLI (`agy acp`，基于 stdio 的 JSON-RPC 2.0 协议) 无缝转换为标准 **Anthropic Messages (`/v1/messages`)**、**OpenAI Chat Completions (`/v1/chat/completions`)**、**OpenAI Responses (`/v1/responses`)** 与 **Google Gemini REST (`/v1beta/models/...`)** 接口，并内置实时监控面板与 Prometheus 指标端点。

与市面上直接逆向 Google OAuth 内部接口裸发 HTTP/Protobuf 请求的方案不同，本网关**100% 严格通过官方 `agy acp` 进程通信**。所有 TLS 指纹、OAuth 令牌刷新、会话快照和上下文状态机完全由官方二进制托管，可降低自行实现上游协议带来的指纹差异与账号风控风险; 这只是降低风险, 不构成账号不会被限制的保证, 账号状态仍取决于上游服务条款与实际使用方式。

### 核心特性

1. **四协议原生兼容与外部工具闭环 (MCP Bridge)**：
   - **Anthropic `/v1/messages` & `/v1/messages/count_tokens`**：完整支持 Claude Code（流式 `thinking` + `signature` 签名块、`tool_use` / `tool_result` 挂起与恢复、`max_tokens` 截断状态透传、缓存命中精准统计、Outbound Cleanroom 提示词脱敏）。
   - **OpenAI `/v1/chat/completions`**：完整支持 Cursor、Cline、Continue 与标准 OpenAI SDK（`reasoning_content`、`reasoning_tokens`、`tool_calls`、`finish_reason: "length"`、流式 `include_usage`）。
   - **OpenAI `/v1/responses`**：原生支持 Codex CLI / Responses API（流式与非流式 `reasoning` 输出项、`response.reasoning_summary_text.delta`、`reasoning_tokens`、`response.function_call_arguments.delta`、`incomplete` `max_output_tokens` 状态及 `previous_response_id` 跨轮状态恢复）。
   - **Google Gemini `/v1beta/models/...`**：原生支持 `@google/genai` SDK、`gemini-cli` 与聚合网关 `gemini` 渠道直连（`:generateContent`、`:streamGenerateContent?alt=sse`、`:countTokens`、`thinkingConfig`、`MAX_TOKENS`，以及有/无显式 `id` 的 `functionCall` / `functionResponse` 挂起恢复）。
   - **全量 Eager 工具注入与零信任权限门禁**：内置轻量级 MCP HTTP 桥接器，自动在 `tools/list` 注入 `_meta: {"antigravity/alwaysLoad": true}` 并对 `session/request_permission` 执行结构化工具身份精确放行（`allow_once`）。
2. **SQLite `gen_metadata` 实时双游标计费、双口径 TPS 与额度止血守卫**：
   - 基于纯 Go `modernc.org/sqlite` 只读快速路径（单次查询仅 **0.44 ms**，零锁竞争），直接解析 `agy` 会话库中的 `gen_metadata` 与 `steps` Protobuf 载荷。
   - 独立维护 `LastSeenGenMetaIdx` 与 `LastSeenDbStepIdx` 双游标，精确提取每轮 `input_tokens`、`cache_read_input_tokens`、`output_tokens`、流式首字延迟（TTFT，延迟首帧 `data:` 并以 `: ping` 注释帧保活），并同时统计时间加权端到端均速（`tps`）与纯流式解码速度（`decodeTps`，`.1.12`）。
   - **孤儿接力止血与零缓存告警**：内置挂起工具孤儿接力上限（默认 `AGY_MAX_TOOL_RELAYS=2`、`AGY_PARKED_TTL_SEC=300`），客户端中断未回传 `tool_result` 时自动休眠并保留 `session/resume` 热恢复能力；长上下文（`>=200K`）连续零缓存自动触发非阻断 `X-Agy-Cache-Warning` 告警。
3. **`.1.19` 确定性端点路由识别、灰度透出与同批工具保缓存**：
   - 实时解码 `gen_metadata` `.1.19`（`servedModel`）底层真实路由端点：对 `gemini-4-carbon` 等模型遇到灰度端点时保持热会话不断连并在面板清晰提示，对 `gemini-4-argon` 灰测暗池（`gemini-4-argon-b`）自动换会话自愈。
   - **同批工具合并与跨重启保缓存**：解析 `CortexStepPlannerResponse`（`.20.7`）将同一生成的多个串行 MCP 工具调用合并为单轮并发返回（彻底消除 `0 输入 / 0 输出` 空轮）；中途动态激活延迟 MCP 工具时通过 `[Host tool update]` + `dsh_call_tool` 原地增量生效，并将 `InitialToolsCatalog` 持久化至 `gateway.db`，网关重启亦不丢失几十万 Token 前缀缓存。
4. **900K 上下文窗口解锁、四门禁安全升级与无感热切换 (`scripts/agy-upgrade.sh` & `deploy/prod-upgrader`)**：
   - 内置确定性二进制补丁流水线（已适配官方 `agy 1.5.9`），自动解除 `agy` 在 ACP 模式下的 256K 窗口硬编码限制，解锁 **900K (900,000 Tokens)** 上下文窗口。
   - 提供包含 `offline`（静态与补丁门禁）、`fake_e2e`（四协议 + 工具闭环 + UI 零报错）、`contract`（23 项 ACP 协议契约零额度校验）、`live_flash`（单次低成本真实探针）的四门禁原子升级与回滚工具；容器化部署支持面板一键确认后无重启软链热切换 `agy`。
5. **压缩后会话连续性 (Post-Compaction Continuity) 与 0.25s 极速热唤醒**：
   - 当客户端（如 Claude Code `/compact`）压缩中间历史导致消息数组变短时，网关通过完整 64 位历史消息摘要匹配自动识别同源会话，仅执行一次平滑 Rollover 并继承累计 Token 统计。
   - 空闲会话自动休眠释放内存，再次请求时优先通过 ACP `session/resume` 在 **0.25 秒**内热恢复，避免 `session/load` 重放数千行历史块。

---

<a name="architecture--core-capabilities"></a>

## Architecture / 架构概览

```text
  Claude Code / SDK     OpenAI Chat SDK     Codex CLI     Gemini CLI / SDK
          │                     │                │                │
  POST /v1/messages    /v1/chat/completions  /v1/responses  /v1beta/models/*
          └─────────────────────┴────────────────┴────────────────┘
                                     ▼
                    ┌─────────────────────────────────┐
                    │   agy-acp-gateway (Port 18890)  │
                    │  • Auth / CORS / ToS Circuit    │
                    │  • Outbound Prompt Cleanroom    │
                    │  • Session Continuity & Pool    │
                    │  • Ephemeral MCP HTTP Bridge    │
                    │  • .1.19 Endpoint Route Telemetry│
                    └───────────┬──────────┬──────────┘
         JSON-RPC 2.0 (stdio)   │          │  Read-Only SQLite Fast Path
         + Local MCP Callbacks  ▼          ▼  (gen_metadata & steps blobs)
                    ┌─────────────────┐  ┌──────────────────────────┐
                    │ bin/agy-acp-900k│  │ ~/.gemini/antigravity-cli│
                    │  (Official CLI) │─▶│   conversations/*.db     │
                    └─────────────────┘  └──────────────────────────┘
```

### Repository Layout / 目录结构

```text
agy-acp-gateway/
├── go-gateway/                 # Pure-Go gateway source code (CGO_ENABLED=0)
│   ├── main.go                 # Process bootstrap & graceful dual-port server orchestration
│   ├── http_lifecycle.go       # Hardened HTTP server factory & bounded graceful drain
│   ├── config.go               # Environment config, pure-API home & structured log rotation
│   ├── auth.go                 # Constant-time key auth (/v1beta/ ?key= scoped) & CORS/Origin checks
│   ├── http_handlers.go        # Multi-protocol SSE/JSON handlers (/v1/messages, /v1/chat/completions, /v1/responses)
│   ├── gemini_v1beta.go        # Native Google Gemini REST (/v1beta/models/*) adapter & FIFO tool call rebinder
│   ├── protocol_normalize.go   # Prompt/tool-result normalization, utility probe & session key derivation
│   ├── gateway_pool.go         # Worker pool admission, idle/parked reaper & live telemetry collector
│   ├── acp_engine.go           # Shared ACP stdio JSON-RPC multiplexor & turn delta channels
│   ├── acp_capabilities.go     # Upstream ACP initialize capability negotiation parser
│   ├── session_lifecycle.go    # Session boot, strict model/tier pin, warm hibernation & session/resume
│   ├── session_runner.go       # Turn execution, dual-watermark gen_metadata accounting & cache attribution
│   ├── mcp_bridge.go           # Local HTTP MCP server, PlannerResponse sibling batching & tool loop guard
│   ├── tool_catalog.go         # In-place deferred tool delta injection & strict host tool whitelist
│   ├── sqlite_protobuf.go      # Zero-copy protobuf decoder for SQLite steps & gen_metadata (.1.11/.1.12/.1.19)
│   ├── models.go               # Model catalog (default Carbon), aliases, thinking tiers & calibrated pricing
│   ├── store.go                # Persistent SQLite state DB (conversations, turns, usage_steps) & /metrics
│   ├── outbound_cleanroom.go   # Outbound prompt cleanroom, credential redaction & ToS circuit breaker
│   ├── agy_notice.go           # Upstream terminal agent_message_chunk notice detection
│   ├── log_redaction.go        # Bearer, MCP tenant path & secret-field log redaction helpers
│   ├── dashboard.go            # Snapshot-cached /api/dashboard telemetry & official /usage quota view
│   ├── webui.go                # Embedded web dashboard asset loader (dashboard.html & lucide-icons.json)
│   ├── upgrade.go              # Host-agent candidate status & ACP binary hot-switch coordinator
│   ├── webui/                  # Embedded warm-paper telemetry dashboard & Lucide SVG icon set
│   ├── *_test.go               # Unit, race, continuity, HTTP regression & telemetry test suites
│   └── testdata/fakeacp/       # Deterministic fake ACP server for zero-quota offline/E2E testing
├── scripts/
│   ├── gw.sh                   # Multi-instance process supervisor (start / stop / restart / status / logs)
│   ├── agy-upgrade.sh          # Safe upstream agy binary upgrader & rollback entrypoint
│   ├── agy_upgrade.py          # 7-gate 900K binary patcher & 4-stage candidate validator
│   ├── agy_acp_smoke.py        # 23-point zero-quota ACP protocol contract verifier
│   ├── upstream_watch.py       # GitHub Release watcher (default check / --download / --prepare / --official-only)
│   └── e2e_*.py                # Isolated E2E test suites (tool call loop, multi-model, thinking tiers)
├── deploy/
│   ├── Dockerfile              # Production container image definition
│   ├── docker-compose.yml      # Docker Compose deployment stack
│   ├── openresty-acp.conf      # Optional Nginx/OpenResty reverse-proxy snippet
│   └── prod-upgrader/          # Optional Docker-host auto-upgrader & zero-downtime agy symlink switcher
├── .env.example                # Environment variable template
└── LICENSE                     # MIT License
```

---

<a name="quick-start--快速开始"></a>

## Quick Start / 快速开始

### Prerequisites / 前置条件

1. **Go 1.22+** (for building `go-gateway` with `CGO_ENABLED=0`).
2. **Python 3.10+** (for running the `agy` 900K binary patcher and verification scripts).
3. **Google Antigravity CLI (`agy`)**: Installed and logged in (`agy auth login` or existing `~/.gemini/antigravity-cli/antigravity-oauth-token`).

### 1. Build the Gateway & Prepare `bin/agy-acp-900k` / 编译网关与生成 900K 补丁二进制

```bash
# 1. Clone the repository
git clone https://github.com/yuhxuiao/agy-acp-gateway.git
cd agy-acp-gateway

# 2. Build the pure-Go gateway binary
mkdir -p bin backups logs runtime
cd go-gateway
gofmt -l . && go vet ./... && go test -race -count=1 ./...
CGO_ENABLED=0 go build -trimpath -ldflags="-s -w" -o ../bin/agy-acp-gateway .
cd ..

# 3. Prepare and validate the 900K-unlocked agy binary from your local ~/.local/bin/agy
#    (Runs offline static checks + fake E2E + 23-point ACP contract check without consuming quota)
scripts/agy-upgrade.sh --official ~/.local/bin/agy --contract
# Or install directly after candidate verification:
# scripts/agy-upgrade.sh --install --candidate runtime/upgrades/candidates/<candidate-id>
```

### 2. Configure & Start Locally / 配置与启动服务

```bash
# Copy the environment template if you want API key authentication
cp .env.example .env

# Start the gateway (18890) and dashboard (18891)
scripts/gw.sh start

# Check instance health and listening ports
scripts/gw.sh status

# Tail live gateway logs
scripts/gw.sh logs
```

- **API Gateway Liveness**: `http://127.0.0.1:18890/healthz`
- **Live Dashboard UI**: `http://127.0.0.1:18891/`
- **Gateway Pool Stats**: `http://127.0.0.1:18891/health`
- **Prometheus Metrics**: `http://127.0.0.1:18891/metrics`

### 3. Docker Compose Deployment / Docker 容器化部署

```bash
# Ensure bin/agy-acp-gateway and bin/agy-acp-900k are built and present in ./bin/
cp .env.example deploy/.env
docker compose -f deploy/docker-compose.yml up -d --build

# Check container health
docker ps --filter name=agy-acp-gateway
curl -fsS http://127.0.0.1:18890/healthz
```

---

<a name="api--client-configuration--客户端接入"></a>

## API & Client Configuration / 客户端接入指南

### Supported Models / 支持的模型与别名

| Canonical Model ID | Supported Aliases (Examples) | Thinking Tiers | Max Context |
| :--- | :--- | :--- | :--- |
| `gemini-4-carbon` *(default)* | `carbon`, `gemini-4-carbon-*` (requires agy >= 1.5.5) | `low`, `medium`, `high` | **900,000** |
| `gemini-4-argon` | `gemini-4-pro`, `argon`, `gemini-4-argon-*` | `low`, `medium`, `high` | **900,000** |
| `gemini-4-hydrogen` | `hydrogen`, `gemini-4-hydrogen-*` | `low`, `medium`, `high`, `xhigh` | **900,000** |
| `gemini-3.8-flash` | `gemini-flash`, `gemini-3.8-flash-*` | `low`, `medium`, `high` | **900,000** |
| `claude-opus-5-5` | `agy-opus`, `claude-opus-5-*` | `low`, `medium`, `high` | **900,000** |
| `claude-sonnet-5-5` | `agy-sonnet`, `claude-sonnet-5-*` | `low`, `medium`, `high` | **900,000** |

> **Tip**: `/v1/models` and `/v1beta/models` list the 6 canonical model IDs (`AGY_EXPOSE_TIER_MODELS=1` restores `-low`/`-high`/`-xhigh` entries). Requests still accept `-low`, `-medium`, `-high`, or `-xhigh` (Hydrogen only) suffixes (e.g., `gemini-4-argon-high`, `gemini-4-hydrogen-xhigh`, `gemini-3.8-flash-low`), or standard protocol fields (`thinking.budget_tokens` in Anthropic, `reasoning_effort` in OpenAI Chat, `reasoning.effort` in OpenAI Responses, `generationConfig.thinkingConfig` with `thinkingLevel` / `thinkingBudget` and opt-in `includeThoughts: true` in Gemini `/v1beta`).

### 1. Claude Code (`/v1/messages`)

```bash
export ANTHROPIC_BASE_URL="http://127.0.0.1:18890"
export ANTHROPIC_API_KEY="sk-agy-replace-with-your-secret-key"
export ANTHROPIC_MODEL="gemini-4-argon-high"
export ANTHROPIC_SMALL_FAST_MODEL="gemini-3.8-flash-low"

claude
```

### 2. Anthropic Messages API (`curl`)

```bash
curl -sS http://127.0.0.1:18890/v1/messages \
  -H "Content-Type: application/json" \
  -H "x-api-key: $AGY_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "gemini-3.8-flash-low",
    "max_tokens": 1024,
    "messages": [
      {"role": "user", "content": "Explain how ACP session/resume works in two sentences."}
    ]
  }'
```

### 3. OpenAI Chat Completions (`/v1/chat/completions`)

```bash
curl -sS http://127.0.0.1:18890/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AGY_API_KEY" \
  -d '{
    "model": "gemini-4-argon",
    "reasoning_effort": "high",
    "stream": true,
    "messages": [
      {"role": "user", "content": "Write a concurrent worker pool in Go."}
    ]
  }'
```

### 4. OpenAI Responses API (`/v1/responses`)

```bash
curl -sS http://127.0.0.1:18890/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AGY_API_KEY" \
  -d '{
    "model": "gemini-3.8-flash",
    "reasoning": {"effort": "low"},
    "input": "Summarize the benefits of pure-Go SQLite readers."
  }'
```

### 5. Google Gemini API & Gemini CLI (`/v1beta`)

```bash
export GOOGLE_GEMINI_BASE_URL="http://127.0.0.1:18890"
export GEMINI_API_KEY="sk-agy-replace-with-your-secret-key"

curl -sS "http://127.0.0.1:18890/v1beta/models/gemini-4-carbon:streamGenerateContent?alt=sse" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "generationConfig": {"thinkingConfig": {"thinkingLevel": "HIGH"}},
    "contents": [{"role": "user", "parts": [{"text": "Explain ACP warm session resumption briefly."}]}]
  }'
```

---

<a name="upstream-maintenance--safe-upgrade--上游安全升级"></a>

## Upstream Maintenance & Safe Upgrade / 上游维护与安全升级

When Google releases a new version of `agy`, use the built-in 4-gate upgrade pipeline to patch, validate in complete isolation, and atomically switch with instant rollback support:

```bash
# 1. Check the latest official GitHub Release of google-antigravity/antigravity-cli
#    (read-only, zero quota; writes runtime/upgrades/upstream-latest.json)
python3 scripts/upstream_watch.py --official-only

# 2. Download the new stable release, verify its SHA-256 and build a candidate in an isolated
#    directory (Ports 18892/18893): offline + fake E2E + ACP contract, zero prompts
python3 scripts/upstream_watch.py --prepare
#    Or build from a binary you already have; --live-flash adds one authorized Flash request
scripts/agy-upgrade.sh --official ~/.local/bin/agy --contract --live-flash

# 3. Atomically install a verified candidate (automatically backs up current binaries)
scripts/agy-upgrade.sh --install --candidate runtime/upgrades/candidates/<candidate-id>

# 4. One-command rollback if ever needed
scripts/agy-upgrade.sh --rollback backups/<backup-dir>
```

### Running Tests / 运行测试套件

All unit tests, race detector suites, and multi-protocol E2E tests run against the deterministic `fakeacp` harness with **zero model quota consumption**:

```bash
# 1. Go static analysis, race detector, and coverage suite
cd go-gateway
gofmt -l .
go vet ./...
go test -race -count=1 -cover ./...
cd ..

# 2. Upgrader isolation & manifest binding unit tests
python3 -m unittest discover -s scripts -p "test_*.py" -v
```

---

## Security & Privacy Design / 安全与隐私设计

- **Official Transport Only**: Never makes raw HTTP calls to Google internal endpoints; all model traffic flows through `agy acp`.
- **Outbound Prompt Cleanroom**: Automatically strips third-party client attribution headers (`x-anthropic-billing-header`, client harness boilerplate, `<system-reminder>` wrappers) before forwarding to `agy acp`, while preserving user project instructions (`CLAUDE.md`, `AGENTS.md`, workspace paths, and skills).
- **Structured Credential Redaction**: Automatically scrubs API keys, Bearer tokens, and OAuth secrets from gateway logs and optional debug recordings (`0600` file permissions).
- **ToS Circuit Breaker**: Immediately latches into a fail-closed state if upstream ever reports an account-level Terms of Service restriction, preventing retry storms.

---

## License / 开源协议

Released under the [MIT License](LICENSE).
