<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg" />
    <img src="assets/banner-light.svg" alt="agy-acp-gateway" width="760" />
  </picture>
</p>

<h3 align="center">Turn Google's official Antigravity CLI (<code>agy acp</code>) into a zero-CGO, quad-protocol AI gateway with live telemetry, self-healing WAF cleanroom, and Carbon KV cache protection.</h3>

<p align="center">
  <a href="./README.md"><strong>English</strong></a> &nbsp;·&nbsp;
  <a href="./README_ZH.md"><strong>简体中文</strong></a> &nbsp;·&nbsp;
  <a href="#engineering-pillars"><strong>Engineering Highlights</strong></a> &nbsp;·&nbsp;
  <a href="#client-compatibility"><strong>Clients</strong></a> &nbsp;·&nbsp;
  <a href="#quick-start"><strong>Quick Start</strong></a> &nbsp;·&nbsp;
  <a href="#configuration-reference"><strong>Configuration</strong></a> &nbsp;·&nbsp;
  <a href="#safe-upgrader"><strong>Upgrader</strong></a> &nbsp;·&nbsp;
  <a href="#changelog"><strong>Changelog</strong></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Go-1.26%2B_(CGO__ENABLED%3D0)-00ADD8?style=flat-square&logo=go&logoColor=white" alt="Go 1.26+ Zero CGO" />
  <img src="https://img.shields.io/badge/Protocols-Anthropic_%7C_OpenAI_%7C_Responses_%7C_Gemini_v1beta-0856F5?style=flat-square" alt="Quad Protocol" />
  <img src="https://img.shields.io/badge/Context-900K_Unlocked-0D9488?style=flat-square" alt="900K Context" />
  <img src="https://img.shields.io/badge/Telemetry-Zero--Lock_SQLite_%2B_Prometheus-D97706?style=flat-square" alt="Zero-Lock SQLite and Prometheus" />
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-22c55e?style=flat-square" alt="MIT License" /></a>
</p>

---

**agy-acp-gateway** is a single-binary, pure-Go (`CGO_ENABLED=0`) multi-protocol API gateway and real-time observability suite built strictly on top of Google's official Antigravity CLI (`agy acp`, JSON-RPC 2.0 over stdio).

Instead of reverse-engineering private Google OAuth/Protobuf endpoints and forging raw HTTP packets, **100% of upstream traffic runs inside the official `agy acp` binary**. TLS fingerprints, OAuth token refreshes, trajectory checkpoints, and upstream framing remain natively managed by Google's client, while `agy-acp-gateway` adds quad-protocol translation, 5-layer TPU KV cache survival, reversible semantic cleanroom sanitization, silent shadow-pool detection, and zero-downtime upgrades.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/arch-overview-dark.png" />
    <img src="assets/arch-overview-light.png" alt="agy-acp-gateway quad-protocol architecture diagram" width="960" />
  </picture>
</p>

---

<a id="engineering-pillars"></a>

## Why `agy-acp-gateway`?

Running AI coding agents (`Claude Code`, `Pi`, `Codex CLI`, `Cursor`, `Cline`, `OpenCode`, `Gemini CLI`) against `agy acp` in production exposes failure modes that thin ACP wrappers cannot survive:

| Production Pain Point | Naive ACP / Spoofed Proxy | `agy-acp-gateway` Engineering Fix |
| :--- | :--- | :--- |
| **Forged OAuth protocol risk** | Reverse-engineers internal Protobuf APIs with fragile custom headers | **100% Official `agy acp` Stdio Engine**: TLS, OAuth refresh, and framing stay inside the official binary |
| **Gemini 4 Carbon concurrent 0% cache** | Reuses static empty `sessionID` or leaks mid-turn prefix edits | **Gate 5 binary patch** stamps per-trajectory 64-bit FNV-1a `sessionID`; freezes `system`/`developer` prefix after turn 1 |
| **120-180s prefill disconnect storms** | Fires `session/cancel` on client abort, wiping 150K+ in-flight prefill | **Prefill Soft-Detach (45s grace) + Singleflight** holds compute alive so client retries re-attach seamlessly |
| **Mid-turn deferred tool loading resets** | Restarts ACP worker whenever `ToolSearch` adds MCP tools dynamically | **`TOOLS_UPDATED_IN_PLACE`** refreshes the MCP tool catalog inside parked turns without breaking KV prefix |
| **Multi-tool empty `0/0` hops & loops** | Relays sequential tool calls one round-trip at a time | **`PlannerResponse` sibling batching + `AGY_MAX_TOOL_RELAYS=4`** batches parallel tools and caps orphan relays |
| **Client harness triggers 400/429 WAF** | Crashes or destructively deletes user instructions via naive regex | **3-Stage Cleanroom + HMAC Codec + Flash Bisect** swaps tags losslessly and auto-isolates WAF triggers |
| **Silent canary downgrades & fake TPS** | Reports 350+ tok/s bursts or misses silent Argon/Flash routing shifts | **Pure-Go `.1.19` SQLite Reader** extracts authoritative cached tokens, `servedModel`, aligned TTFT, and pure `decodeTps` |

---

## Core Engineering Capabilities

### 1. 5-Layer Carbon KV Cache Defense & Disconnect Rescue

Long-context Gemini 4 Carbon prefill phases routinely take 90-180 seconds, triggering HTTP client timeouts or mid-flight disconnects that abort cold-start computation in uncoordinated wrappers.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/seq-prefill-dark.png" />
    <img src="assets/seq-prefill-light.png" alt="Prefill Soft-Detach, Singleflight Rescue and Tool Parking Sequence" width="960" />
  </picture>
</p>

- **Gate 5 Per-Trajectory `sessionID` (`tools/agy_extra_patch.py`, `SPEC_VERSION=2`)**: Patches `codeassistclient.(*CodeAssistClient).getStreamingTextCompletion` across multi-arch ELF and Mach-O binaries (`linux_amd64`, `linux_arm64`, `darwin_arm64`) with post-site register liveness checks so each trajectory carries its own signed 64-bit FNV-1a `sessionID`, isolating concurrent clients on Google's implicit prefix cache index.
- **Sticky Prefix Freeze & Compaction Continuity**: Locks the `system`/`developer` block after turn 1 so dynamic harness reminders do not bust 100K+ cached prefixes, and preserves canonical identity plus cumulative token counters across client `/compact` transcript rollovers (`agy_gateway_compaction_rollovers_total`).
- **In-Place Tool Catalog Updates & Cache-Preserving `tool_choice`**: Updates deferred tools in-place (`TOOLS_UPDATED_IN_PLACE`, e.g. `ToolSearch`) and enforces per-turn `tool_choice` (`"none"`, `"required"`/`"any"`, forced tool, `allowed_tools`, and Gemini `toolConfig.functionCallingConfig`) inside the MCP bridge without stripping declared session tools, keeping 92%+ KV cache hits across tool toggles.
- **Prefill Soft-Detach (`30s` / `45s`) + Singleflight**: Once a request waits past `AGY_PREFILL_CANCEL_MIN_ELAPSED_SEC=30` without output, client disconnects enter a 45-second `AGY_PREFILL_CANCEL_GRACE_SEC` lease (`PREFILL_SOFT_DETACH`) rather than calling `session/cancel`; retrying requests join the live in-flight Singleflight execution (`PREFILL_SOFT_DETACH_JOIN`).
- **Burn Guard & Capacity Degrade Fallback**: Emits non-blocking `X-Agy-Cache-Warning` headers across all 4 protocols once `>= 80,000`-token contexts hit 3 consecutive zero-cache misses (`AGY_CACHE_WARN_MIN_TOKENS`), and automatically switches `gemini-4-carbon-high` sessions to an in-place `medium` capacity fallback after consecutive slow cold misses.
  > **Upstream Note**: Because Gemini 4 Carbon uses backend-managed implicit prefix caching (`daily-cloudcode-pa`), occasional upstream replica switches or congestion spikes can still yield isolated zero-cache turns (`cr=0`) that recover on subsequent hits. The gateway guarantees identical `sessionID` and prefix stability on every local hop so hit rates stay in the 92%-98%+ band under sustained load.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/lifecycle-cache-dark.png" />
    <img src="assets/lifecycle-cache-light.png" alt="Session KV Cache and 4-Gate Upgrader Lifecycle" width="960" />
  </picture>
</p>

### 2. Dual-Channel MCP Tool Bridge & Sibling Batching

- **In-Memory Parked Execution (`mcp_bridge.go`)**: Advertises host tools via `_meta["antigravity/alwaysLoad"]=true` on an ephemeral HTTP MCP bridge (`ws-bridge`), parking upstream ACP execution the instant the model emits tool calls (`MCP_TOOL_PARKED`).
- **Sibling Tool Coalescing (`MCP_TOOL_SIBLINGS_BATCHED`)**: Inspects `CortexStepPlannerResponse` so parallel sibling calls emitted in a single reasoning step (for example multiple `Read`, `Grep`, `Edit`, or `Bash` calls) coalesce into one downstream HTTP `tool_use` turn, eliminating redundant `0/0`-token relay hops.
- **Orphan Relay Cap & Warm Hibernation**: Bounds hung `ws_await_result` polling (`AGY_MAX_TOOL_RELAYS=4`, `AGY_PARKED_TTL_SEC=300`), hibernates idle workers cleanly (`AGY_IDLE_WORKER_TTL_SEC=1200`, aligned with `agy`'s 270s stateless keepalive), wakes sessions via `session/resume`, preserves 64-bit integer precision (`> 2^53`) on MCP `tools/call` payloads, and falls back to a UTF-8 safe 80K-char re-anchor when upstream state expires.
- **Zero-Cost Keepalive Fast-Ack (`KEEPALIVE_SKIP_BUSY`)**: Short-circuits client background title/ping probes when a sticky session is actively streaming (`keepalive_fast_ack`), incurring zero upstream tokens and zero interruption.

### 3. 3-Stage Semantic Cleanroom, Reversible HMAC Codec & Flash WAF Auto-Bisection

- **Deterministic Semantic Alignment (`outbound_cleanroom.go`)**: Strips client telemetry headers (`x-anthropic-billing-header`) and aligns wrapper identities cleanly to `ws-bridge` semantics while preserving leading code/diff indentation, user project rules, custom instructions, and code paths.
- **Session-Scoped HMAC-SHA256 Codec (`reversible_codec.go`)**: Encodes potentially flagged tool names, MCP `tools/list` parameter keys/descriptions, segment IDs, and XML tags into collision-free fixed-length tokens (`wsseg_*`, `wstag_*`) salted per session key and decodes them symmetrically across streaming deltas and `tools/call` round-trips, paired with Cleanroom docstring scrubbing on Structured Output schemas.
- **Self-Healing Flash WAF Bisection (`waf_autobisect.go`)**: Detects instant first-turn 400/429 retry loops (`WAF_FAST_CANCEL`), runs an automated binary search over system/prompt boilerplate using `gemini-3.8-flash-low` (`util:waf-bisect-*`) without altering user intent, persists isolated trigger patterns to `waf_rewrite_rules.json` (`WAF_AUTOBISECT_HEALED`), and seamlessly retries the user turn (`waf_autobisect_recovery`).

### 4. Authoritative `.1.19` SQLite Telemetry, Argon Recovery & Warm-Paper Console

- **Pure-Go SQLite Protobuf Reader (`sqlite_protobuf.go`)**: Queries local `agy` conversation databases (`steps` and `gen_metadata`) via `modernc.org/sqlite` using `ReadLatestStepFromSQLiteFast` (O(1) tail lookup verified 100% consistent with full protobuf dumps) and dual monotonic watermarks (`LastSeenGenMetaIdx` / `LastSeenDbStepIdx`).
- **Aligned Streaming TTFT & Dual TPS**: Holds client TTFT calibration clean by sending W3C SSE `: ping\n\n` comments pre-`message_start` (and `event: ping` during pauses) instead of polluting visible tokens; tracks end-to-end throughput (`tps = outTokens / totalDuration`) separately from pure decode speed (`.1.12` `decodeTps`), eliminating fake 350+ tok/s SSE burst artifacts.
- **Canary Model Detection & Argon Shadow Recovery**: Decodes `gen_metadata` `.1.19` `servedModel` on every turn; automatically detects silent Argon shadow degradations (`agy_gateway_argon_degradation_detected_total`), recycles the session cleanly in-turn, and recovers (`agy_gateway_argon_degradation_recovered_total`).
- **Accurate Token Accounting & Multi-Client Attribution**: Counts images deterministically at `1,600` tokens each and accounts for Structured Output schemas in `/v1/messages/count_tokens` and `/v1beta/models/*:countTokens` (excluding bloated Base64 byte length); identifies 12+ client harnesses (`Claude Code`, `Pi`, `Codex`, `OpenClaw`, `Kilo Code`, `Roo Code`, `Cline`, `OpenCode`, `Cursor`, `Gemini CLI`, `Aider`, `Cherry Studio`, `DSH`) across headers, cleanroom-stripped prompts, and stored tool catalogs (`client_detect.go`).
- **Editorial Warm-Paper Dashboard & Official Quota Calibration (`dashboard.go`, `webui/`)**: Runs strictly on isolated `:18891` (`AGY_DASH_PORT`), syncing live 5-hour and 7-day official quota windows via `agy -p /usage` alongside strictly read-only Antigravity Desktop App (`~/.gemini/antigravity/conversations`, `AGY_APP_CONV_DIR`) and standalone `agy` CLI step telemetry (`AGY App` / `AGY CLI`), with estimated runnable token budgets (99% steady cache vs 0% cold run), bottleneck alerts (`5h` vs `weekly`), canary/burn banners, and Prometheus `/metrics`.

### 5. Quad-Protocol Native Endpoints (`:18890`), Structured Output & Port Isolation (`:18891`)

| Port | Purpose | Endpoints |
| :--- | :--- | :--- |
| **`:18890`** (`AGY_GW_PORT`) | **Inference API & Liveness** | `POST /v1/messages`, `POST /v1/messages/count_tokens`, `POST /v1/chat/completions`, `POST /v1/responses`, `GET /v1/models`, `GET /v1beta/models`, `POST /v1beta/models/{model}:generateContent`, `:streamGenerateContent`, `:countTokens`, `GET /healthz` |
| **`:18891`** (`AGY_DASH_PORT`) | **Ops Console & Telemetry** | `GET /` (Warm-Paper Console), `GET /api/dashboard`, `GET /api/upgrade`, `POST /api/upgrade/approve`, `GET|POST|DELETE /api/accounts*` (multi-account admin, master key only), `GET /metrics` (Prometheus), `GET /health` |

- **Unified 4-Protocol Structured Output**: Native JSON Schema / JSON Object enforcement across `output_config.format` (`/v1/messages`), `response_format` (`/v1/chat/completions`), `text.format` (`/v1/responses`), and `generationConfig.responseSchema` / `responseMimeType` (`/v1beta`), injected via turn tail directives so sticky system prefixes stay intact across warm turns and parked MCP resumes.
- **Stateful Continuation Guards & Pre-Commit JSON Errors**: `/v1/responses` sets `"store": false`, rejects non-empty `previous_response_id` with `400 previous_response_not_found`, and returns `application/json` (not premature `text/event-stream`) on pre-commit `stream: true` errors; `/v1/messages` and `/v1/messages/count_tokens` reject `thread` with `404 thread_not_found` so clients resend full conversation history cleanly.
- **Strict Dual-Port Isolation**: Admin/telemetry routes (`/`, `/dashboard`, `/api/*`, `/metrics`) return `404` on `:18890`, while inference and MCP bridge routes (`/v1/*`, `/v1beta/*`, `/mcp/*`) return `404` on `:18891`.

### 6. Single-Channel Multimodal v2, Pipe Hardening & Error/License Isolation

- **Unified 3-Stage Multimodal Pipeline (`multimodal_normalize.go`, `image_fetcher.go`)**: Normalizes images (`PNG`/`JPEG`/`WEBP`/`GIF`, 16-byte magic-header verified) and `<= 2MB` UTF-8 text files cleanly across all 4 protocols + 2 `count_tokens` endpoints, including nested tool-result attachments (`tool_result`, `role: "tool"`, `function_call_output`, `functionResponse.parts`). Unexported in-memory sentinel stamping (`canonicalImageStamp`) blocks forged client fields (`decodedBytes`, `digest`, `_canonical`) from bypassing Stage 1 validation, while SHA-256 metadata caching accelerates validated historical inline images and lazy remote fetching runs with a `64MB/15m` LRU cache, `singleflight`, and socket-level `net.Dialer.Control` SSRF protection (including IPv4-mapped/compatible IPv6 transition ranges).
- **Pipe Anti-Deadlock & Memory Guard (`acp_engine.go`, `main.go`)**: Gateway runs with default `GOMEMLIMIT=256MiB` (`AGY_CHILD_GOMEMLIMIT=180MiB` isolated for child `agy`), `128MB` `ReadSlice('\n')` JSON-RPC line framing, `56MB` outbound frame limit, and `-cmd.Process.Pid` `SIGKILL` process-group teardown on exit.
- **License (`#3501` / Enterprise), Quota Fast-Stop & Dynamic `Retry-After`**: Upstream `#3501`, `GEMINI_ENTERPRISE_LICENSE_NOT_VALID`, and `ccpa_ineligible_tier_id` errors map deterministically to `403 permission_error` / `PERMISSION_DENIED` without retry loops, cross-model switching, or ToS circuit tripping. Hard billing/quota caps (spend cap, prepaid, daily/weekly limits) fast-stop in `<1s` without wasteful bisection; transient `429`/`529` responses emit bounded HTTP `Retry-After` headers (`5s..3600s`) parsed from upstream reset hints; safety/policy blocks (`SAFETY`, `PROHIBITED_CONTENT`, `RECITATION`, `SPII`) return non-retriable `400`. The console displays 3-stage latency decomposition (`Queue TTFT / Thinking / Visible Generation`), filtered `Retry xN` badges, and optional 4-gate conversation cleanup (`AGY_CONV_KEEP_DAYS`).

---

<a id="client-compatibility"></a>

## Client Compatibility Matrix

| Client / SDK | Wire Protocol | Verified Capabilities | Session & Cache Behavior |
| :--- | :--- | :--- | :--- |
| **Claude Code** | `POST /v1/messages` | Streaming `thinking` + `signature`, `output_config.format` & `effort`, `tool_use` parking, `/compact` detection | Auto-rotates Cleanroom `<user-excerpt>`; preserves canonical session & cumulative stats post-compaction |
| **Pi Agent** | `POST /v1/messages` | Multi-turn sibling tool batching, `ToolSearch` live tool expansion, implicit thinking tiers | Protected by `TOOLS_UPDATED_IN_PLACE` + 45s Prefill Soft-Detach + Singleflight join across retries |
| **Codex CLI** | `POST /v1/responses` | Streaming `reasoning` & `reasoning_summary_text.delta`, `function_call` & `custom_tool_call`, `text.format` | `store: false` (`400 previous_response_not_found` guard); freezes mid-turn `developer` prefix on sticky sessions |
| **Cursor / Cline / Roo / OpenCode** | `POST /v1/chat/completions` | `reasoning_content`, `response_format` (`json_schema`), `tool_calls`, cache-preserving `tool_choice` | Automatic HMAC reversibility for paths/tags & orphan tool relay protection (`AGY_MAX_TOOL_RELAYS=4`) |
| **Gemini CLI / `@google/genai`** | `POST /v1beta/models/*` | `:generateContent`, `:streamGenerateContent?alt=sse`, `:countTokens`, `responseSchema`, `toolConfig`, `?key=`/`/key=` auth | Deterministic FIFO rebinder for tool calls without explicit IDs & `thoughtSignature` pass-through |

---

## Supported Models & Thinking Tiers

`/v1/models` (with `context_window`, `max_input_tokens`, and `max_tokens: 65536`) and `/v1beta/models` (`inputTokenLimit` & `outputTokenLimit: 65536`) expose the 7 canonical model IDs by default (`AGY_EXPOSE_TIER_MODELS=1` exposes suffixed tier variants). Clients may append `-minimal`, `-low`, `-medium`, `-high`, `-xhigh`, `-max`, or `-ultra` (`-minimal` maps to `low`; `-xhigh`/`-max`/`-ultra` map to `xhigh` on `gemini-4-neon` and `gemini-4-hydrogen` and clamp to `high` on other models), or pass native reasoning fields (`output_config.effort`, `thinking.budget_tokens`, `reasoning_effort`, `reasoning.effort`, `thinkingConfig.thinkingLevel` / `thinkingBudget`):

| Canonical Model ID | Accepted Aliases (Examples) | Thinking Tiers | Max Context (Unlocked) |
| :--- | :--- | :--- | :--- |
| `gemini-4-carbon` *(default)* | `carbon`, `gemini-4-carbon-*` | `low`, `medium`, `high` | **900K+** (`1,048,576` API) |
| `gemini-4-neon` | `neon`, `gemini-4-neon-*` | `low`, `medium`, `high`, `xhigh` | **900K+** (`1,048,576` API) |
| `gemini-4-argon` | `gemini-4-pro`, `argon`, `gemini-4-argon-*` | `low`, `medium`, `high` | **900K+** (`1,048,576` API) |
| `gemini-4-hydrogen` | `hydrogen`, `gemini-4-hydrogen-*` | `low`, `medium`, `high`, `xhigh` | **900K+** (`1,048,576` API) |
| `gemini-3.8-flash` | `gemini-flash`, `gemini-3.8-flash-*` | `low`, `medium`, `high` | **900K+** (`1,048,576` API) |
| `claude-opus-5-5` | `agy-opus`, `claude-opus-5-*` | `low`, `medium`, `high` | **900K+** (`1,048,576` API) |
| `claude-sonnet-5-5` | `agy-sonnet`, `claude-sonnet-5-*` | `low`, `medium`, `high` | **900K+** (`1,048,576` API) |

---

<a id="quick-start"></a>

## Quick Start

### Prerequisites

- **Go 1.26+** (builds single zero-CGO static binary via `CGO_ENABLED=0`)
- **Python 3.10+** (runs Gate 1-5 multi-arch ELF/Mach-O binary patcher on `linux_amd64` / `linux_arm64` / `darwin_arm64` & isolated ACP verification harness)
- **Google Antigravity CLI (`agy`)**: Installed and authenticated locally (`agy auth login` or valid `~/.gemini/antigravity-cli/antigravity-oauth-token`)

### 1. Build Gateway & Patch `bin/agy-acp-900k`

```bash
git clone https://github.com/yuhxuiao/agy-acp-gateway.git
cd agy-acp-gateway
mkdir -p bin backups logs runtime

# Run full unit/race suite & compile single zero-CGO binary
cd go-gateway
gofmt -l . && go vet ./... && go test -race -count=1 ./...
CGO_ENABLED=0 go build -trimpath -ldflags="-s -w" -o ../bin/agy-acp-gateway .
cd ..

# Apply Gates 1-5 patches (900K unlock + trajectory sessionID) & verify offline ACP contracts
scripts/agy-upgrade.sh --official ~/.local/bin/agy --contract
scripts/agy-upgrade.sh --install --candidate runtime/upgrades/candidates/<candidate-id>
```

> Prefer prebuilt binaries? Download `agy-acp-gateway_<version>_<os>_<arch>.tar.gz` (`linux/amd64`, `linux/arm64`, `darwin/amd64`, `darwin/arm64`) + `SHA256SUMS` from [GitHub Releases](https://github.com/yuhxuiao/agy-acp-gateway/releases), place `agy-acp-gateway` into `./bin/`, and patch your local official `agy` binary into `./bin/agy-acp-900k` using `third_party/agy-context-unlock/agy-patch.py` and `tools/agy_extra_patch.py`.

### 2. Configure & Launch Locally

```bash
cp .env.example .env
# Edit .env to set AGY_API_KEYS, proxy, or cache threshold settings

scripts/gw.sh start
scripts/gw.sh status
scripts/gw.sh logs
```

- **Gateway API**: `http://127.0.0.1:18890` (`/healthz`)
- **Telemetry Dashboard**: `http://127.0.0.1:18891/` (`/metrics`, `/health`, `/api/dashboard`)

### 3. Docker Compose Deployment

```bash
# Ensure ./bin/agy-acp-gateway and ./bin/agy-acp-900k exist
cp .env.example deploy/.env
docker compose -f deploy/docker-compose.yml up -d --build
curl -fsS http://127.0.0.1:18890/healthz
```

<details>
<summary><strong>Client Configuration &amp; Curl Examples (Claude Code, Codex, OpenAI Chat, Gemini CLI)</strong></summary>

#### Claude Code (`/v1/messages`)

```bash
export ANTHROPIC_BASE_URL="http://127.0.0.1:18890"
export ANTHROPIC_API_KEY="sk-agy-replace-with-your-secret-key"
export ANTHROPIC_MODEL="gemini-4-carbon-medium"
export ANTHROPIC_SMALL_FAST_MODEL="gemini-3.8-flash-low"
claude
```

#### Codex CLI / OpenAI Responses (`/v1/responses`)

```bash
curl -sS http://127.0.0.1:18890/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AGY_API_KEY" \
  -d '{
    "model": "gemini-4-carbon",
    "reasoning": {"effort": "medium"},
    "input": "Summarize the benefits of pure-Go SQLite readers."
  }'
```

#### OpenAI Chat Completions (`/v1/chat/completions`)

```bash
curl -sS http://127.0.0.1:18890/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AGY_API_KEY" \
  -d '{
    "model": "gemini-4-argon",
    "reasoning_effort": "high",
    "stream": true,
    "messages": [{"role": "user", "content": "Write a concurrent worker pool in Go."}]
  }'
```

#### Google Gemini CLI & REST SDK (`/v1beta`)

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

</details>

---

<a id="configuration-reference"></a>

## Configuration & Metrics Reference

<details>
<summary><strong>Environment Variables (verified from <code>go-gateway/internal/config/snapshot.go</code>, <code>go-gateway/config.go</code> &amp; <code>.env.example</code>)</strong></summary>

| Variable | Default | Description |
| :--- | :--- | :--- |
| `AGY_LISTEN_HOST` | `127.0.0.1` | Bind host for gateway and dashboard HTTP servers |
| `AGY_GW_PORT` / `AGY_DASH_PORT` | `18890` / `18891` | API port and isolated telemetry dashboard port |
| `AGY_API_KEYS` / `AGY_API_KEYS_FILE` | *(empty)* | Comma-separated or file-based keys for `/v1/*`, `/v1beta/*` (`?key=`/`/key=`), and `:18891` (Bearer / `x-api-key` / HTTP Basic Auth password; constant-time compared) |
| `AGY_CORS_ORIGINS` | *(empty)* | Allowed CORS origins (exposes `X-Agy-Served-Model` & `X-Agy-Cache-Warning`) |
| `AGY_ACP_BIN` | `<root>/bin/agy-acp-900k` | Path to Gate 1-5 patched `agy` binary (`linux_amd64`, `linux_arm64`, `darwin_arm64`) |
| `AGY_UPSTREAM_PROXY` | *(empty in binary; `127.0.0.1:7890` in `.env.example`)* | HTTP/HTTPS proxy forwarded to `agy acp` subprocesses & `/usage` refresh |
| `AGY_MAX_LIVE_WORKERS` / `AGY_MAX_CONCURRENT_PROMPTS` | `8` / `6` | Max resident ACP sessions and concurrent upstream LLM prompt executions |
| `AGY_MAX_PROBE_WORKERS` | `1` | Dedicated non-preemptive slot budget for background WAF bisection and `util:` probes |
| `AGY_IDLE_WORKER_TTL_SEC` | `1200` | Idle ACP session hibernation timeout (20 min, aligned with `agy` 270s stateless keepalive) |
| `AGY_PARKED_TTL_SEC` / `AGY_MAX_TOOL_RELAYS` | `300` / `4` | Orphan parked tool deadline & max `ws_await_result` relays before cleanup |
| `AGY_PREFILL_CANCEL_MIN_ELAPSED_SEC` | `30` | Elapsed prefill threshold before client disconnects trigger Soft-Detach |
| `AGY_PREFILL_CANCEL_GRACE_SEC` | `45` | Grace window holding detached prefill compute alive for Singleflight retry join |
| `AGY_CACHE_WARN_MIN_TOKENS` / `AGY_CACHE_WARN_STREAK` | `80000` / `3` | Thresholds for emitting `X-Agy-Cache-Warning` and dashboard burn banners |
| `AGY_WAF_AUTOBISECT` | `true` | Enable automated `gemini-3.8-flash-low` bisection on upstream 400 WAF blocks |
| `AGY_DEFAULT_MODEL` / `AGY_EXPOSE_TIER_MODELS` | `gemini-4-carbon` / `0` | Default fallback model and `/models` tier suffix listing toggle |
| `AGY_USE_G1_CREDITS` | `0` | Set to `1` to enable Google One AI credits fallback when regular quota depletes |
| `AGY_MAX_IMAGES_GEMINI` / `AGY_MAX_IMAGES_CLAUDE` | `200` / `100` | Max images per prompt turn for Gemini and Claude model families |
| `AGY_MAX_IMAGE_BYTES` / `AGY_MAX_PROMPT_IMAGE_BYTES` | `10485760` / `33554432` | Per-image (`10MB`) and per-prompt (`32MB`) decoded binary limits (`413` on overflow) |
| `AGY_MAX_TEXT_FILE_BYTES` / `AGY_FETCH_IMAGES` | `2097152` / `true` | Max unpacked UTF-8 text attachment (`2MB`) and public HTTP(S) image fetch toggle |
| `AGY_CONV_KEEP_DAYS` | `0` *(disabled)* | Optional 4-gate cleanup retention days for synced gateway `.pb`/`.db` bundles |
| `AGY_APP_CONV_DIR` | *(auto on local main; `off` disables)* | Read-only Antigravity Desktop App conversation directory (`~/.gemini/antigravity/conversations`) for live telemetry & quota accounting (never modified or cleaned) |
| `AGY_ACP_RECORD` | *(empty)* | Optional `0700` directory recording redacted NDJSON ACP frames (`0600` files) |

</details>

<details>
<summary><strong>Prometheus Metrics Exported at <code>:18891/metrics</code></strong></summary>

- `agy_gateway_store_ready`
- `agy_gateway_live_workers` / `agy_gateway_max_live_workers` / `agy_gateway_hibernated_sessions`
- `agy_gateway_prompts_inflight` / `agy_gateway_max_concurrent_prompts`
- `agy_gateway_parked_calls`
- `agy_gateway_requests_total`
- `agy_gateway_engine_exits_total` / `agy_gateway_worker_cap_rejections_total` / `agy_gateway_probe_slot_rejections_total`
- `agy_gateway_soft_detach_total{outcome}`
- `agy_gateway_session_reuses_total` / `agy_gateway_compaction_rollovers_total`
- `agy_gateway_argon_degradation_detected_total` / `agy_gateway_argon_degradation_recovered_total`
- `agy_gateway_cache_burn_warnings_total` / `agy_gateway_orphan_relay_caps_total`
- `agy_gateway_waf_autobisect_healed_total` / `agy_gateway_upgrade_state{state}`
- `agy_gateway_turns_total{model,mode,stop_reason,usage_source}`
- `agy_gateway_tokens_total{model,kind}`

</details>

---

<a id="safe-upgrader"></a>

## Architecture & 4-Gate Upgrader

<details>
<summary><strong>Repository Layout &amp; Module Responsibilities</strong></summary>

```text
agy-acp-gateway/
├── .github/workflows/          # Multi-arch Go test & GitHub Release automation
├── go-gateway/                 # Pure-Go gateway (CGO_ENABLED=0)
│   ├── main.go                 # Dual-port bootstrap & bounded 10s graceful drain
│   ├── http_handlers.go        # /v1/messages, /v1/chat/completions, /v1/responses + SSE ping framing
│   ├── http_lifecycle.go       # Startup dependency wiring & graceful shutdown controller
│   ├── gemini_v1beta.go        # Native Google Gemini REST /v1beta/* adapter
│   ├── protocol_normalize.go   # Structured Output, Retry-After, 64-bit JSON & error classification
│   ├── multimodal_normalize.go # 3-stage multimodal validator, sentinel & historical image cache
│   ├── acp_engine.go           # Shared ACP stdio JSON-RPC multiplexor & soft-detach turns
│   ├── acp_capabilities.go     # ACP agent capability & permission negotiation helpers
│   ├── agy_notice.go           # Upstream notice classification (#3501 / enterprise / ToS / capacity)
│   ├── gateway_pool.go         # Worker admission, Singleflight deduplication & idle reaper
│   ├── session_fsm.go          # Root-package wrapper over explicit SessionPhase FSM
│   ├── session_lifecycle.go    # Session boot, parked-tier sync, cold-resume & warm session/resume
│   ├── session_runner.go       # Dual-watermark gen_metadata accounting, burn guard & recovery
│   ├── tool_catalog.go         # Canonical tool digesting & incremental catalog deltas
│   ├── mcp_bridge.go           # Ephemeral MCP HTTP server, sibling batching & cache-preserving tool_choice
│   ├── outbound_cleanroom.go   # 3-stage Cleanroom scrub, credential redaction & ToS fuse
│   ├── reversible_codec.go     # Session-scoped HMAC-SHA256 deterministic tag & tool schema codec
│   ├── waf_autobisect.go       # Automated upstream 400 WAF message bisection
│   ├── sqlite_protobuf.go      # Zero-lock protobuf reader for agy gen_metadata & steps
│   ├── client_detect.go        # Full-path multi-client attribution detector (12+ clients)
│   ├── models.go               # Root facade over canonical model catalog & quota weights
│   ├── store.go                # Persistent SQLite gateway.db (WAL R/W split + conversation_hot) & /metrics
│   ├── dashboard.go            # /api/dashboard telemetry & official /usage quota sync
│   ├── upgrade.go              # Idempotent upgrade status, approval verification & state gauges
│   ├── internal/               # Acyclic layered subpackages (DI boundaries verified by AST DAG tests)
│   │   ├── config/             # Immutable startup Snapshot, env helpers & URL/key redaction
│   │   ├── cleanroom/          # Stem-gated 3-stage Cleanroom, HMAC reversible codec, ToS & WAF rules
│   │   ├── protocol/           # 7-model catalog, unified SSEStreamSession, client detect & tool digests
│   │   ├── acp/                # ACP Engine interface, capabilities & upstream notice definitions
│   │   ├── store/              # SessionStore interface & zero-lock SQLite/protobuf WAL reader
│   │   ├── session/            # Pure SessionPhase FSM, miss classifier & weighted worker LRU
│   │   └── dashboard/          # Embedded web console state & upgrade metadata helpers
│   ├── testdata/fakeacp/       # Offline synthetic ACP 1.5.10/1.5.11 + SQLite gen_metadata harness
│   └── webui/                  # Warm-paper live console (HTML + Lucide SVG icons)
├── deploy/prod-upgrader/       # Container-host 4-gate upgrader & symlink hot-swapper
├── scripts/                    # E2E suites (incl. cache resilience), quota calibration, gw.sh & upstream_watch.py
├── tools/                      # Multi-arch Gate 5 binary patcher (agy_extra_patch.py)
└── third_party/                # Upstream context-unlock patcher (MIT)
```

</details>

### 4-Gate Safe Upgrader & Multi-Arch Zero-Downtime Symlink Swap

When Google releases a new `agy` version (`linux_amd64`, `linux_arm64`, or `darwin_arm64` via GitHub Releases or official auto-updater manifests), every candidate binary passes four isolated gates before touching live sessions:

```bash
# 1. Read-only multi-arch check for latest upstream CLI release (zero quota)
python3 scripts/upstream_watch.py --official-only

# 2. Download, verify SHA-256/SHA-512, apply Gates 1-5, run offline ACP contracts + fake E2E
scripts/agy-upgrade.sh --official ~/.local/bin/agy --contract --live-flash

# 3. Install verified candidate atomically (retains backups/) & rollback in one command if needed
scripts/agy-upgrade.sh --install --candidate runtime/upgrades/candidates/<candidate-id>
scripts/agy-upgrade.sh --rollback backups/<backup-dir>
```

Containerized host deployments (`deploy/prod-upgrader/`) surface verified candidates directly inside the Dashboard header: clicking upgrade swaps `data/agy/current -> <new-version>` once active turns finish, avoiding gateway container restarts during `agy` CLI updates.

### Running Tests (Zero Quota)

```bash
cd go-gateway && gofmt -l . && go vet ./... ./testdata/fakeacp/... && go test -race -count=1 ./... ./testdata/fakeacp/... && cd ..
python3 -W error -m unittest discover -s scripts -p "test_*.py" -v
python3 -W error -m unittest discover -s deploy/prod-upgrader -p "test_*.py" -v
```

---

## Security & Privacy Boundary

- **Official Transport Only**: Zero raw Google OAuth endpoint forging; all inference runs strictly inside official `agy acp`.
- **Fail-Closed ToS Fuse**: Immediately suspends outgoing requests if upstream Terms-of-Service / account risk flags trigger (`AGY_TOS_TRIPPED_FILE`), preventing cascading retries while isolating `#3501` and `GEMINI_ENTERPRISE_LICENSE_NOT_VALID` `403` errors without false ToS trips.
- **0600 Credential Redaction**: Gateway logs (`AGY_GW_LOG`), upstream image fetch error URLs, and optional ACP recordings (`AGY_ACP_RECORD`) strip API keys, Bearer/Basic headers, `?key=`/`/key=` secrets, and signed query strings under restricted `0700`/`0600` permissions.
- **Zero-Trust Port & Tool Gating**: Enforces strict `:18890`/`:18891` route isolation, dual-stack loopback checks on `/mcp/*`, structured `session/request_permission` verification before granting `allow_once`, and constant-time API key comparison with `/v1beta/` scoped `?key=`/`/key=` checks.

---

<a id="changelog"></a>

## Release History

- **2026-11-20 (`v2.2.0` Multi-Account Sandbox Manager, Strict Per-Key Model Allowlists, Federated Dashboard \& `agy 1.5.13` Parity)**:
  - **Single-Container Multi-Account Sandboxes**: `AccountManager` runs one isolated `agy acp` child per account (own `HOME`/`.gemini`, own egress proxy, loopback-only ports), configured from the `:18891` dashboard (`GET/POST/DELETE /api/accounts`, `POST /api/accounts/oauth/start|submit`, `/token`, `/probe-ip`) with a headless Google OAuth web flow (PTY-backed `agy -p /login`) or direct token import. Fresh installs seed exactly one generic `primary` account and no static keys.
  - **Strict Per-Key Model Allowlists**: Each account binds `boundKeys` and `allowedModels`; a bound key can only call its allowed models (`403 model_not_allowed` otherwise), and `/v1/models` / `/v1beta/models` are filtered per caller. `<master-key>@<account-id>` and `X-Agy-Account` select an account for master-key callers only and can never widen a restricted key.
  - **Per-(Session, Model) Sticky Round-Robin**: Accounts sharing a model are load-balanced with sticky sessions (header / `prompt_cache_key` / `metadata.user_id` session / conversation fingerprint) and fail over when a model's 5h window is exhausted.
  - **Federated Dashboard, Per-Plan Quota Caps \& Hardening**: Optional `AGY_DASHBOARD_PEERS` merges remote instances; `/usage` snapshots auto-detect Google AI Pro (`$10/5h`, `$35/wk` Gemini; `$2.50/5h`, `$5/wk` Claude + separate Argon weekly pool) vs Ultra 20x (`$200/5h`, `$800/wk` Gemini; `$25/5h`, `$50/wk` Claude) so dollar usage and runnable token estimates match each account's actual plan; the admin plane (`:18891`, `/api/accounts*`, `/api/upgrade*`, `/metrics`) accepts the master key only; dashboard mutations enforce a CSRF header; proxy URLs and credentials are validated, masked in API output, redacted from errors, and stripped from child environments. Named proxy presets are loaded from an optional `AGY_PROXY_PRESETS_FILE` (JSON array of `{id,label,region,description}`) with the proxy host/token supplied via `AGY_RESIN_HOST` / `AGY_RESIN_PROXY_TOKEN`.
  - **`agy 1.5.13` Zero-Patch SQLite Silent-Retry Sensing**: Adapted to `agy 1.5.13`'s `ShouldShowUser` stream gate (which suppresses `⚠ API error (attempt N)` chunks on ACP while still committing `step_type = 17` rows to `conversations/<sid>.db` WAL) by decoding `CortexStepErrorMessage` directly via the existing read-only session DB connection. Runs a bounded `150ms` / `8.5s` WAL watcher only on WAF bisect probes and cold-start first turns (restoring sub-second `WAF_FAST_CANCEL` and `waf_autobisect`), performs single-query turn-end backfill across normal and parked `tool_use` turns with full `1.5.12`/`1.5.13+` deduplication (restoring `RetryCount` and exact `429`/`503` detail backfill on generic terminal errors), and refreshes `scripts/agy_notice_templates.json` for `agy 1.5.13`.
- **2026-11-19 (`456x Hot-Path Latency & 95% WAL Optimization, Gemini 4 Neon & Parked Thinking-Tier Sync`)**:
  - **Hot-Path Precomputation & SQLite WAL Split**: Eliminated per-turn full-history regex rescanning in `SeedFromConversationOnce` via precomputed cached cleanroom digests, added O(1) keyword stem prefiltering in `internal/cleanroom`, moved `formatParkedToolResultText` and `SystemPromptDelta` out of `s.mu`, lazy-evaluated cancellation history fingerprints, and introduced the `conversation_hot` side table plus WAL mtime/size short-circuiting in `SyncUsageStepsFromDir` (cutting composite warm-path latency ~456x and SQLite WAL write volume by ~95% in benchmarks).
  - **`gemini-4-neon` (`xhigh`) & Parked Thinking-Tier Consistency**: Added canonical `gemini-4-neon` (`low`/`medium`/`high`/`xhigh`, enums `1532..1535`, `2.0x` LRU weight) alongside Desktop `gemini-4-hydrogen` enums; added `PendingThoughtLevel` and authoritative `TurnUsage.ActualTier` decoding from SQLite `steps` so in-flight parked sessions prevent double-step tier jumps and surface upcoming tier switches accurately on the dashboard.
- **2026-11-18 (`agy 1.5.11+ Parity, Acyclic internal/* Refactor, Cache Resilience & Preservation v2`)**:
  - **Architecture Refactor & `agy 1.5.11`+ Support**: Split core packages into an acyclic 7-subpackage `go-gateway/internal/` DAG (`config`, `cleanroom`, `protocol`, `acp`, `store`, `session`, `dashboard`) guarded by AST topology tests and dependency-injection interfaces; added immutable startup `config.Snapshot`, explicit `SessionPhase` finite-state machine, SQLite WAL read/write pool separation with bounded async snapshots, `AGY_MAX_PROBE_WORKERS` probe budget isolation, unified `protocol.SSEStreamSession` streaming, updated `scripts/agy_notice_templates.json` for `agy 1.5.11`, and `.github/workflows/release.yml` for multi-arch binary releases.
  - **Cache Resilience & In-Place Contention Guards**: Unified cache-miss classification (`classifyCacheMissSpec`) with nonzero `cachedReadTokens` cursor tracking; preserved `parked_mcp_resume` sessions on client aborts; added orphan relay streak circuit-breaker, active `promptGen` epoch isolation, all-tier Carbon capacity fallback & `4x` LRU weighting, transient `-32603` in-session backoff retries, `computeFirstUserFingerprint` stripping bounds, and a 12-scenario `scripts/e2e_cache_resilience.py` suite.
  - **Cache Preservation v2 & Desktop Telemetry**: Froze `InitialSystemText`, `InitialAppendPrompt`, and `InitialToolsCatalog` across process restarts and `session/resume`; matched headerless `fp:` continuations across system drift via `(agentScope, cwd, historyFingerprint)` and `acp_<32hex>` parked IDs; added context-aware `PrefillSoftDetach` (`>=120K`, `>=48K`, default), `120s` passive `end_turn` claim holding, and read-only `AGY_APP` B-tree/WAL telemetry (`fork_step_idx` deduplication) plus multi-arch ELF/Mach-O Gate 5 and Linux/macOS `gw.sh` parity.
- **2026-11-17 (`agy 1.5.10, Multimodal v2 Pipeline, Anti-Deadlock Pipe, #3501 403 & 3-Stage Observability`)**:
  - **Upstream `agy 1.5.10` & Anti-Deadlock Base**: Raised gateway `GOMEMLIMIT` to `256MiB`, replaced `bufio.Scanner` with `ReadSlice('\n')` (`128MB` line cap), enforced process-group reap on exit and `56MB` outbound frame guard, and added strict model pinning checks.
  - **3-Stage Multimodal v2 Pipeline & `#3501` 403**: Unified image/text normalization and `count_tokens` across all four protocols, fixed `tool_result` image drops, added lazy unseen-delta HTTP image fetching with `64MB/15m` LRU cache, `16`-byte magic sniffing, kernel-level `net.Dialer.Control` SSRF blocking, and non-tripping `403 permission_error` handling for `#3501` / `GEMINI_ENTERPRISE_LICENSE_NOT_VALID`.
  - **Latency Breakdown & Optional Cleanup**: Exposed queue/upstream TTFT, thinking duration/tokens, visible stream generation, and `Retry xN` counters in dashboard turns/steps, plus opt-in `AGY_CONV_KEEP_DAYS` 4-gate cleanup.
- **2026-11-16 ~ 2026-11-17 (`Gate 5 Per-Trajectory sessionID, Soft-Detach & Stream Speed Alignment`)**: Added Gate 5 machine-code patching (`tools/agy_extra_patch.py`) injecting per-trajectory `sessionID` into `getStreamingTextCompletion`, introduced Prefill Soft-Detach (`30s`/`45s`) + Singleflight, unified Agy native `outTok / streamSeconds` decode speed display, and published bilingual architecture diagrams.

<details>
<summary><strong>Earlier Milestones (2026-11-08 to 2026-11-15)</strong></summary>

- **2026-11-15**: Added semantic fusion, session-scoped `HMAC-SHA256` reversible tag/path/tool codec (`reversible_codec.go`), `ws-bridge` neutral tool namespace, Flash WAF auto-bisection, full-path client attribution (`client_detect.go`), orphan relay capping, and `agy 1.5.9` dynamic terminal error interception.
- **2026-11-14**: Added `agy 1.5.8` / `1.5.9` permission/truncation/reasoning parity, `SHA-512` dual-source manifest verification (`upstream_watch.py`), and long-context zero-cache `X-Agy-Cache-Warning` alerts.
- **2026-11-13**: Launched native Google Gemini REST (`/v1beta`) adapter with scoped `?key=` authentication and `gemini-4-hydrogen` (`xhigh` tier) + canonical `/v1/models` exposure.
- **2026-11-12**: Modularized Go engine into focused components, added in-place deferred tool updates (`TOOLS_UPDATED_IN_PLACE`), SSE heartbeat write-deadline extension, and warm-paper dashboard polish.
- **2026-11-08 ~ 2026-11-11**: Replaced Node prototype with pure-Go (`CGO_ENABLED=0`) gateway, implemented lock-free SQLite `.db` / `.1.19` protobuf telemetry, Argon `.1.19` shadow-routing self-healing, `PlannerResponse` sibling tool batching, and 4-gate safe upgrade pipeline.

</details>

---

## License

Released under the [MIT License](LICENSE).
