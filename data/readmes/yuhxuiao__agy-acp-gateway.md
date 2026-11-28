<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg" />
    <img src="assets/banner-light.svg" alt="agy-acp-gateway" width="760" />
  </picture>
</p>

<p align="center">
  Turn the Google Antigravity CLI (<code>agy</code>) into standard Anthropic, OpenAI, and Gemini APIs, with a web console for multi-account management.
</p>

<p align="center">
  <a href="./README.md"><strong>English</strong></a> &nbsp;·&nbsp;
  <a href="./README_ZH.md"><strong>简体中文</strong></a> &nbsp;·&nbsp;
  <a href="#quick-start"><strong>Quick Start</strong></a> &nbsp;·&nbsp;
  <a href="#client-setup"><strong>Client Setup</strong></a> &nbsp;·&nbsp;
  <a href="#models"><strong>Models &amp; Files</strong></a> &nbsp;·&nbsp;
  <a href="#image-generation"><strong>Image Gen</strong></a> &nbsp;·&nbsp;
  <a href="#multi-account"><strong>Multi-Account</strong></a> &nbsp;·&nbsp;
  <a href="#configuration-reference"><strong>Config &amp; API</strong></a> &nbsp;·&nbsp;
  <a href="#troubleshooting"><strong>FAQ</strong></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Go-1.26%2B-00ADD8?style=flat-square&logo=go&logoColor=white" alt="Go 1.26+" />
  <img src="https://img.shields.io/badge/API-Anthropic_%7C_OpenAI_%7C_Gemini-0856F5?style=flat-square" alt="APIs" />
  <img src="https://img.shields.io/badge/Models-11_Chat_%2B_Image-7C3AED?style=flat-square" alt="12 Models" />
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-22c55e?style=flat-square" alt="MIT License" /></a>
</p>

---

The gateway serves AI APIs on `:18890` and a web admin console on `:18891`. All upstream traffic goes directly through the official `agy` client:

- **Multi-Protocol APIs (`:18890`)**: Anthropic `/v1/messages`, OpenAI `/v1/chat/completions` and `/v1/responses`, OpenAI `/v1/images/*`, and Google Gemini `/v1beta`.
- **12 Models**: 11 chat models (Gemini 4 family, `gemini-3.8-flash`, Claude Opus/Sonnet 5.5, `gpt-oss-120b-medium`, `gemini-pro-orchestrator` series) plus `gemini-3.1-flash-image` for image generation and editing.
- **Multi-Account Pool (`:18891`)**: Manage multiple Google accounts in one place, with per-account HTTP/SOCKS5 proxies, model allowlists, restricted API keys, and standby failover.
- **Single Binary, Low RAM**: One static binary with the web UI built in and zero runtime dependencies. Idle workers hibernate automatically so a 6 GB server can run ~20 concurrent `Claude Code` or `Codex` sessions.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/arch-overview-dark.png" />
    <img src="assets/arch-overview-light.png" alt="agy-acp-gateway architecture diagram" width="920" />
  </picture>
</p>

---

<a id="quick-start"></a>

## Quick Start

### Requirements

- OS: Linux (`linux_amd64` / `linux_arm64`), macOS (`darwin_amd64` / `darwin_arm64`), or Windows with WSL2.
- Official `agy` CLI installed at `~/.local/bin/agy`. Version **`1.5.16`** is recommended (`1.5.17` and `1.5.18` have an extra quota burn bug).
- Python `3.10+` to apply the `900K` context patch; download `agy-acp-gateway` from [Releases](https://github.com/yuhxuiao/agy-acp-gateway/releases) or build from source with Go `1.26+`.

### 1. Prepare Binaries

```bash
git clone https://github.com/yuhxuiao/agy-acp-gateway.git
cd agy-acp-gateway
mkdir -p bin

# Build the gateway (or download a prebuilt archive from GitHub Releases into bin/agy-acp-gateway)
cd go-gateway && CGO_ENABLED=0 go build -trimpath -ldflags="-s -w" -o ../bin/agy-acp-gateway . && cd ..

# Create a 900K-context copy of agy (leaves ~/.local/bin/agy untouched)
cp ~/.local/bin/agy bin/agy-acp-900k
python3 third_party/agy-context-unlock/agy-patch.py --binary bin/agy-acp-900k --acp-only --in-place --no-backup
python3 tools/agy_extra_patch.py --binary bin/agy-acp-900k --in-place
```

### 2. Start the Gateway

**Option A: Docker Compose (recommended for servers)**

```bash
cp .env.example deploy/.env
# Edit deploy/.env and set AGY_API_KEYS (plus AGY_UPSTREAM_PROXY if needed)
docker compose -f deploy/docker-compose.yml up -d --build
```

**Option B: Run directly on host**

```bash
cp .env.example .env
# Edit .env and set AGY_API_KEYS (plus AGY_UPSTREAM_PROXY if needed)
./scripts/gw.sh start
```

Check health:

```bash
curl -fsS http://127.0.0.1:18890/healthz
# Expected: {"ok":true}
```

### 3. Sign In with Google

Open `http://127.0.0.1:18891/` in your browser (enter any username and your `AGY_API_KEYS` key as the password; note that console labels are currently in Chinese), then click **账号** (Accounts) in the top bar:

- **Browser OAuth link** (recommended on Linux / WSL2 / Docker; on native `darwin_arm64`, use the two methods below): Click **新增账号槽位** (Add Account), pick a proxy, and save. Click **生成 Google 授权链接** (Generate OAuth URL) and sign in locally. When redirected to `http://localhost:.../?code=...` (a connection error page is expected), paste that full localhost URL back into the dialog and submit.
- **Import Token JSON**: Paste an existing `antigravity-oauth-token` JSON object directly into the OAuth dialog.
- **CLI Login** (primary account only): Run `./bin/agy-acp-900k login` (or `docker exec -it agy-acp-gateway /app/bin/agy-acp-900k login`).

### 4. Test Request

```bash
curl -sS http://127.0.0.1:18890/v1/chat/completions \
  -H "Authorization: Bearer sk-your-master-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash",
    "reasoning_effort": "low",
    "messages": [{"role": "user", "content": "Reply with READY"}]
  }'
```

---

<a id="client-setup"></a>

## Client Setup

| Client / SDK | Endpoint | Base URL | Auth |
| :--- | :--- | :--- | :--- |
| **`Claude Code`** | `/v1/messages` | `http://127.0.0.1:18890` | `x-api-key` / `ANTHROPIC_API_KEY` |
| **`Codex` CLI** | `/v1/responses` | `http://127.0.0.1:18890/v1` | `Authorization: Bearer` |
| **Cursor / `Cline` / `Roo Code` / `OpenCode`** | `/v1/chat/completions` | `http://127.0.0.1:18890/v1` | `Authorization: Bearer` |
| **Gemini CLI / `google-genai` SDK** | `/v1beta` | `http://127.0.0.1:18890` | `x-goog-api-key` or `?key=` |
| **Pi Coding Agent** | `/v1/messages` or `/v1/responses` | `http://127.0.0.1:18890` | `x-api-key` / `Bearer` |

### `Claude Code`

```bash
export ANTHROPIC_BASE_URL="http://127.0.0.1:18890"
export ANTHROPIC_API_KEY="sk-your-master-key"
export ANTHROPIC_MODEL="gemini-4-carbon-medium"
export ANTHROPIC_SMALL_FAST_MODEL="gemini-3.8-flash-low"
claude
```

### `Codex` CLI (`~/.codex/config.toml`)

```toml
model = "gemini-4-carbon"
model_reasoning_effort = "medium"
model_provider = "agy"

[model_providers.agy]
name = "Antigravity ACP Gateway"
base_url = "http://127.0.0.1:18890/v1"
env_key = "AGY_API_KEY"
wire_api = "responses"
```

### OpenAI SDK / Chat Clients

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:18890/v1",
    api_key="sk-your-master-key",  # append @acct:<id> or @group:<id> to target an account or group
)

resp = client.chat.completions.create(
    model="gemini-4-neon",
    reasoning_effort="high",
    messages=[{"role": "user", "content": "Explain Go context cancellation in three sentences."}],
)
print(resp.choices[0].message.content)
```

### Google Gemini `/v1beta`

```bash
curl -sS "http://127.0.0.1:18890/v1beta/models/gemini-4-hydrogen:generateContent" \
  -H "x-goog-api-key: sk-your-master-key" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{"role": "user", "parts": [{"text": "Summarize Raft leader election in three bullets."}]}],
    "generationConfig": {"thinkingConfig": {"thinkingLevel": "HIGH"}}
  }'
```

---

<a id="models"></a>

## Models & File Inputs

### Supported Models

| Model ID | Quota Pool | Context Window | Thinking Levels | Common Aliases |
| :--- | :--- | :--- | :--- | :--- |
| **`gemini-4-carbon`** *(default)* | Gemini | `1M` (`<=900K` recommended) | `low`, `medium`, `high` | `carbon` |
| **`gemini-4-neon`** | Gemini | `1M` (`<=900K` recommended) | `low`, `medium`, `high`, `xhigh` | `neon` |
| **`gemini-4-argon`** | Gemini / Argon | `1M` (`<=900K` recommended) | `low`, `medium`, `high` | `argon` |
| **`gemini-4-hydrogen`** | Gemini | `1M` (`<=900K` recommended) | `low`, `medium`, `high`, `xhigh` | `hydrogen` |
| **`gemini-3.8-flash`** | Gemini | `1M` (`<=900K` recommended) | `low`, `medium`, `high` | `gemini-flash`, `gemini-2.5-flash*` |
| **`claude-opus-5-5`** | Claude / GPT | `1M` (`<=900K` recommended) | `low`, `medium`, `high` | `agy-opus` |
| **`claude-sonnet-5-5`** | Claude / GPT | `1M` (`<=900K` recommended) | `low`, `medium`, `high` | `agy-sonnet` |
| **`gpt-oss-120b-medium`** | Claude / GPT | `128K` | Fixed `medium` | `gpt-oss`, `gpt-oss-120b` |
| **`gemini-pro-orchestrator`** | Gemini | `1M` (`<=900K` recommended) | Fixed `high` | `gemini-pro-orchestrator*` |
| **`gemini-pro-orchestrator-neon`** | Gemini | `1M` (`<=900K` recommended) | Fixed `high` | `gemini-pro-orchestrator-neon*` |
| **`gemini-pro-orchestrator-argon`** | Gemini | `1M` (`<=900K` recommended) | Fixed `high` | `gemini-pro-orchestrator-g1-pro` |
| **`gemini-3.1-flash-image`** | Gemini | Image gen / edit | None | `gemini-3.1-flash-image-preview` |

- **Thinking levels**: Defaults to `medium`. Set via request fields (`reasoning_effort`, `thinking.budget_tokens`, `output_config.effort`, `thinkingLevel`) or append `-low`, `-medium`, `-high`, `-xhigh` to the model name.
- **Model catalog & structured JSON**: `GET /v1/models` and `GET /v1beta/models` return allowed models for the caller's key along with `max_input_tokens`. JSON Schema output works across all chat endpoints (`response_format`, `output_config.format`, `responseJsonSchema`).
- **Standard Claude model names**: Set `AGY_ROUTE_CLAUDE_NAMES=1` in `.env` if your client hardcodes `claude-sonnet-*` or `claude-opus-*`.

### Images, PDFs, Audio & Video

- **Images & text files**: Accepts `PNG`, `JPEG`, `WEBP`, `GIF`, `HEIC`, `HEIF` (`<=10 MiB` per image, `<=32 MiB` per request) and UTF-8 code/text files (`<=2 MiB`).
- **Text PDFs**: Supported out of the box on all models and tool-calling sessions (`AGY_PDF_TEXT_FASTPATH=1`).
- **Scanned PDFs, audio & video**: Off by default. Set `AGY_MEDIA_RELAY=1` in `.env` to let Gemini chat requests (without `tools`) read scanned PDFs, audio (`mp3`, `wav`, `m4a`, `ogg`, `flac`, `opus`, `aac`), and video (`mp4`, `webm`, `mov`), up to `20 MiB` per file by default.

---

<a id="image-generation"></a>

## Image Generation & Editing (`gemini-3.1-flash-image`)

Check `gemini-3.1-flash-image` in the account allowlist in `:18891` first. Supported options:

- **Aspect ratios**: `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `9:16`, `16:9` (or OpenAI `size` values).
- **Batch & reference images**: `n=1..4` images per call, and `1..3` reference images for editing.
- **Output format**: `output_format` accepts `"jpeg"` (default) or `"png"`.

### 1. OpenAI `/v1/images/generations` & `/v1/images/edits`

```bash
# Text-to-image
curl -sS http://127.0.0.1:18890/v1/images/generations \
  -H "Authorization: Bearer sk-your-master-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.1-flash-image",
    "prompt": "Silver mechanical keyboard and coffee mug on light wood, natural light",
    "aspect_ratio": "16:9",
    "n": 1,
    "output_format": "jpeg",
    "response_format": "b64_json"
  }'

# Image editing with 1..3 reference images
curl -sS http://127.0.0.1:18890/v1/images/edits \
  -H "Authorization: Bearer sk-your-master-key" \
  -F "model=gemini-3.1-flash-image" \
  -F "prompt=Convert this sketch into a clean black-and-white line drawing" \
  -F "aspect_ratio=3:2" \
  -F "output_format=png" \
  -F "image[]=@./sketch.png"
```

### 2. OpenAI `/v1/chat/completions`

Useful for chat-only relays (`gpt-load`, `new-api`) and chat UIs; returns Markdown `![image](data:image/jpeg;base64,...)`:

```bash
curl -sS http://127.0.0.1:18890/v1/chat/completions \
  -H "Authorization: Bearer sk-your-master-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.1-flash-image",
    "aspect_ratio": "4:3",
    "messages": [{"role": "user", "content": "Draw an orange cat wearing pilot goggles"}]
  }'
```

### 3. Google Gemini `/v1beta`

```bash
curl -sS "http://127.0.0.1:18890/v1beta/models/gemini-3.1-flash-image:generateContent" \
  -H "x-goog-api-key: sk-your-master-key" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{"role": "user", "parts": [{"text": "Minimalist sunrise mountain poster"}]}],
    "generationConfig": {
      "candidateCount": 1,
      "imageConfig": {"aspectRatio": "16:9"}
    }
  }'
```

---

<a id="multi-account"></a>

## Multi-Account Management & Routing

Add multiple Google accounts in `:18891` -> **账号** (Accounts). Pro, Ultra 5x, and Ultra 20x plans are detected automatically. Each account keeps an isolated directory, can use `direct` or its own HTTP/HTTPS/SOCKS5 proxy, and can be organized into account groups.

### Routing Modes & Targeting

Switch routing modes from the top bar: `round-robin` (default), `fill-first`, `weighted-rr`, `least-load`, or `manual-active`. Set backup accounts to `Standby` so they stay idle until primary accounts are full or rate-limited.

| Use Case | Credential / Header | Notes |
| :--- | :--- | :--- |
| **Use global pool** | `Bearer <master_key>` | Picks a healthy account using the active routing mode |
| **Target one account** | `Bearer <master_key>@acct:<id>` | Or send header `X-Agy-Account: <id>` |
| **Target an account group** | `Bearer <master_key>@group:<id>` | Or send header `X-Agy-Group: <id>` |
| **Downstream restricted key** | `Bearer <bound_key>` | Created per account or group in `:18891`; cannot open the `:18891` admin UI |

### Routing Behavior

- **Multi-turn stays on one account**: Turn 1 retries on another healthy account if it hits `429`/`503`. From Turn 2 onward, the conversation stays on its original account to keep the prompt cache warm and avoid replaying history across accounts.
- **5-hour tool check cap**: `Claude Code` and `Codex` consume an upstream 5-hour free safety-check allowance on each local tool call; exceeding it burns extra quota. The gateway shifts new tool sessions to fresher accounts before hitting the cap (`80%` / `88%` / `93%` presets in the top bar).

---

<a id="configuration-reference"></a>

## Endpoints & Common Settings

### Ports & Endpoints

`:18890` serves AI APIs; `:18891` serves the admin console (expose only `:18890` on a public reverse proxy):

| Port | Path | Purpose |
| :--- | :--- | :--- |
| `:18890` | `GET /healthz` | Health check (no auth) |
| `:18890` | `GET /v1/models`, `GET /v1beta/models` | Allowed models and context limits |
| `:18890` | `POST /v1/messages`, `/v1/messages/count_tokens` | Anthropic Messages API |
| `:18890` | `POST /v1/chat/completions`, `/v1/responses` | OpenAI Chat & Responses APIs |
| `:18890` | `POST /v1/images/generations`, `/v1/images/edits` | OpenAI Image Generation & Edit APIs |
| `:18890` | `POST /v1beta/models/{model}:generateContent` / `:streamGenerateContent` | Google Gemini REST API |
| `:18891` | `GET /`, `/api/dashboard`, `/api/accounts*`, `/api/upgrade*` | Web console & account APIs (master key only) |
| `:18891` | `GET /metrics` | Prometheus metrics (master key only) |

### Common `.env` Settings

Most setups only edit the first four variables. Full list is in [`.env.example`](.env.example):

| Variable | Default | Purpose |
| :--- | :--- | :--- |
| `AGY_API_KEYS` | *(optional on `127.0.0.1`)* | Comma-separated master keys for `:18890` APIs and `:18891` login |
| `AGY_LISTEN_HOST` | `127.0.0.1` | Bind address (`0.0.0.0` in Docker Compose) |
| `AGY_GW_PORT` / `AGY_DASH_PORT` | `18890` / `18891` | AI API port / Web console port |
| `AGY_UPSTREAM_PROXY` | *(empty)* | Default proxy for primary account (secondary accounts are set in `:18891`) |
| `AGY_MAX_LIVE_WORKERS` | `8` | Max concurrent workers for the primary account |
| `AGY_GLOBAL_IDLE_TARGET` | `8` | Hot workers kept across all accounts when idle |
| `AGY_GLOBAL_BURST_MAX_LIVE_WORKERS` | `0` *(auto from RAM)* | Max concurrent workers across all accounts during bursts (`18` on 6 GB) |
| `AGY_IDLE_WORKER_TTL_SEC` | `180` | Seconds before an idle worker hibernates |
| `AGY_ROUTE_CLAUDE_NAMES` | `0` | Set `1` to map `claude-sonnet-*` / `claude-opus-*` to gateway models |
| `AGY_MEDIA_RELAY` | `0` | Set `1` to enable Gemini scanned PDF, audio, and video inputs |

<details>
<summary><strong>Advanced Settings & Maintenance Commands</strong></summary>

#### Advanced Variables

| Variable | Default | Purpose |
| :--- | :--- | :--- |
| `AGY_DASHBOARD_PEERS` | *(empty)* | View remote gateway nodes in one `:18891` panel (`id\|label\|url\|key;...`) |
| `AGY_PROXY_PRESETS_FILE` / `AGY_RESIN_HOST` / `AGY_RESIN_PROXY_TOKEN` | *(optional)* | Named static proxy presets for `:18891` |
| `AGY_MEM_PRESSURE_WARN_PCT` / `HIGH_PCT` | `70` / `80` | Container RAM warning and high-pressure eviction thresholds (%) |
| `AGY_PROMPT_FIRST_CHUNK_TIMEOUT_SEC` / `STREAM_IDLE_TIMEOUT_SEC` | `360` / `180` | Timeout waiting for first token (s) and max gap between stream chunks (s) |
| `AGY_PREFILL_CANCEL_MIN_ELAPSED_SEC` / `GRACE_SEC` | `30` / `45` | Keep slow requests (`>=30s`) running for `45s` if the client disconnects so a retry can reuse the result |
| `AGY_MEDIA_RELAY_MAX_BYTES` / `MAX_FILES` | `20971520` / `3` | Per-file byte limit (`20 MiB` default) and max files per request for Media Relay |
| `AGY_CONV_KEEP_DAYS` / `AGY_ACP_LOG_MAX_MB` | `4` *(Compose)* / `64` | Conversation retention days and per-account worker log size cap (MiB) |
| `AGY_BLOCKED_VERSIONS` | `1.5.17,1.5.18` | Upstream `agy` versions skipped automatically by the upgrader |

#### Upgrading `agy` & Running Tests

After updating `~/.local/bin/agy`, verify and replace `./bin/agy-acp-900k` with:

```bash
# Check latest official agy version and current patch status
python3 scripts/upstream_watch.py --official-only
./scripts/agy-upgrade.sh --status

# Run local unit tests (uses zero model quota)
cd go-gateway && go test -race -count=1 ./... && cd ..
python3 -m unittest discover -s scripts -p "test_*.py"
```

UI styling rules for `:18891` are in [`DESIGN.md`](DESIGN.md).
</details>

---

<a id="troubleshooting"></a>

## Troubleshooting

<details>
<summary><strong>1. <code>403 permission_error</code> when calling a model or generating images</strong></summary>

That model is unchecked in the account or group allowlist. Open `:18891` -> **账号** (Accounts) -> **编辑** (Edit), check the model (`gemini-3.1-flash-image` for images), and save.
</details>

<details>
<summary><strong>2. <code>403 Forbidden</code> when accessing from LAN IP or reverse proxy</strong></summary>

When `AGY_API_KEYS` is empty, only `127.0.0.1` is allowed. Set `AGY_API_KEYS=sk-...` in `.env` and restart.
</details>

<details>
<summary><strong>3. Account shows <code>VALIDATION_REQUIRED</code> or returns <code>403 #3501</code></strong></summary>

- **`VALIDATION_REQUIRED` (`需要验证`)**: Google asked for a quick browser verification on that account. Click **前往验证** (Verify), finish the check in your browser, then click **已验证, 重检** (Recheck).
- **`403 #3501` or `GEMINI_ENTERPRISE_LICENSE_NOT_VALID`**: That account's token expired or lacks entitlement. The gateway pauses only that account for 30 minutes while other accounts keep serving; re-authorize it in `:18891`.
</details>

<details>
<summary><strong>4. Mid-conversation <code>503 Service Unavailable</code> ("bound account unavailable")</strong></summary>

The account pinned to your current conversation went offline or hit a limit, and the gateway will not move mid-conversation history onto another account. Start a **new conversation** so Turn 1 picks a healthy account.
</details>

<details>
<summary><strong>5. <code>/v1/responses</code> returns <code>previous_response_not_found</code> or <code>thread_not_found</code></strong></summary>

The `previous_response_id` or session ID sent by the client expired or does not exist. Start a new session in your client.
</details>

<details>
<summary><strong>6. Scanned PDF, audio, or video returns <code>400</code> or <code>413</code></strong></summary>

Text PDFs work out of the box on all models. Scanned PDFs, audio, and video require `AGY_MEDIA_RELAY=1` in `.env` and a Gemini chat request without `tools`. Files over `AGY_MEDIA_RELAY_MAX_BYTES` (`20 MiB` default) return `413`.
</details>

---

<a id="changelog"></a>

## Recent Releases

- **`v2.3.26` (2026-11-27)**: Unified `gemini-3.1-flash-image` across `/v1/images/*`, `/v1/chat/completions`, and `/v1beta` (JPEG/PNG output, 50% lower RAM); added separate idle and burst worker limits plus automatic hibernation during tool waits; simplified console labels and docs.
- **`v2.3.24` (2026-11-27)**: Added live 5-hour tool check presets (`80%` / `88%` / `93%`), automatic relaxation near reset, per-account `Shared Account` toggle, and Google AI Ultra `5x` detection (PR #10).
- **`v2.3.23` (2026-11-27)**: Built-in text PDF support on all models, plus opt-in Gemini scanned PDF, audio, and video support (`AGY_MEDIA_RELAY=1`).
- **`v2.3.21` - `v2.3.22` (2026-11-27)**: Cross-account idle worker hibernation, `VALIDATION_REQUIRED` verify + recheck flow, automatic retry on token refresh `401`, and image support in MCP tool results.
- **`v2.3.20` (2026-11-26)**: Added `/v1/images/*` endpoints, expanded chat models to 11, added `HEIC`/`HEIF` image support, and restored client `WebFetch`.

---

## License

Released under the [MIT License](LICENSE).
