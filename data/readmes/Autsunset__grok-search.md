# grok-search

**简体中文** | [English](README.en.md)

`grok-search` 是一个通用 AI agent skill / 脚本包，用轻量 Node.js 脚本提供三类网络访问能力：

- **Search**：通过 Responses 或 Chat Completions 调用 Grok / OpenRouter / 兼容接口，并行返回 Tavily / Firecrawl 独立信源。
- **Fetch**：抓取指定 URL 的可读内容，优先使用 Tavily / Firecrawl，最后 fallback 到无 key 的 Direct Fetch。
- **Map**：发现站点内的候选页面 URL，优先使用 Tavily Map，最后 fallback 到轻量 Direct Map。

## 要求

- Node.js `>=18.17`
- 需要先运行一次 `npm install` 安装 `undici` 传输依赖
- `search.js` 需要配置 `GROK_API_URL` 和 `GROK_API_KEY`

## 快速开始

先安装依赖一次，然后从项目根目录运行脚本：

```bash
npm install
./scripts/search.js "latest Node.js LTS"
./scripts/fetch.js https://example.com
./scripts/map.js https://docs.example.com --limit 20
```

## Agent 安装与配置向导

**给 agent 看的交互式安装流程。** 当用户说「安装 / 配置 / setup grok-search」时，严格按下列步骤执行；不要跳步替用户猜协议或模型，也不要把 API key 回显到聊天里。

技能根目录记为 `SKILL_ROOT`（例如 `~/.claude/skills/grok-search` 或本仓库路径）。配置文件固定为：

```text
~/.config/grok-search/config.json
```

### 步骤 0 — 自查环境（先做，不先问）

在提问前，agent 自己检查并汇报：

| 检查项 | 命令 / 方式 | 通过条件 |
| --- | --- | --- |
| Node.js | `node -v` | `>= 18.17` |
| 技能目录 | `ls "$SKILL_ROOT/scripts/search.js"` | 文件存在 |
| 依赖 | `test -d "$SKILL_ROOT/node_modules/undici"` | 存在；否则在 `SKILL_ROOT` 执行 `npm install` |
| 已有配置 | 读取 `~/.config/grok-search/config.json`（若存在） | 记下是否已有 `apiUrl` / `apiKey` / `searchEndpoint` / `model`（key 只显示前后各 4 位） |
| 代理（可选） | 环境变量 `HTTP(S)_PROXY` / `ALL_PROXY` / `GROK_PROXY` | 仅在后续网络失败时再追问 |

若 Node 版本不够：停下来让用户升级 Node，不要继续写配置。  
若 `npm install` 失败：展示错误摘要，按「依赖安装失败」分支处理。  
若配置已完整且用户只是想「修一下」：先摘要现有配置，再问是覆盖还是只改某一项。

自查结束后，用一两句话告诉用户环境是否就绪，然后进入步骤 1。

### 步骤 1 — 询问搜索协议

只问一次，选项必须说清楚：

1. **`chat`（推荐 grok2api / NewAPI）**  
   - 请求 `{apiUrl}/chat/completions`  
   - 适合 `grok-4.3-fast`、`grok-4.20-fast`、`grok-4.20-0309-non-reasoning`  
   - 多数中转的「快模型联网」走这条  

2. **`responses`（CPA / xAI 风格）**  
   - 请求 `{apiUrl}/responses`  
   - 许多中转上 **只有 `grok-4.5` 一类 CPA 模型** 能真正联网搜索  
   - 官方 xAI / 明确支持 Responses `web_search` 时用这条  

用户说不清时：若对方提到 grok2api、NewAPI、中转、`sk-` 网关 → 默认建议 **`chat`**；若提到 CPA、官方 xAI、`grok-4.5` Responses → 建议 **`responses`**。  
把选择记为 `searchEndpoint`。

### 步骤 2 — 索取 API URL 与 Key

请用户提供（可分两条消息）：

- **apiUrl**：base URL，**不要**带 `/chat/completions` 或 `/responses` 后缀。示例：`https://api.example.com/v1`  
- **apiKey**：Bearer token / `sk-...`  

规则：

- 不要在回复中完整复述 key；写入文件后只回显掩码（如 `sk-1a2b****9z0y`）。  
- 若用户已有配置且只给了新 key，可只更新 `apiKey`。  
- `apiProvider`：URL 含 `openrouter` → `openrouter`；含 `api.x.ai` → `xai`；否则 → `openai-compatible`（中转请写 `openai-compatible`）。  

### 步骤 3 — 询问模型

根据步骤 1 推荐，但仍以用户最终输入为准：

| 协议 | 推荐模型 |
| --- | --- |
| `chat` | `grok-4.3-fast`（默认建议）、`grok-4.20-fast`、`grok-4.20-0309-non-reasoning` |
| `responses` | 中转 CPA 常用 `grok-4.5`；官方 xAI 按其文档模型 ID |

明确提醒：**不要**在 chat 路径默认用 `grok-4.5`（CPA）；**不要**在只支持 chat 联网的中转上硬选 responses + 快模型。

### 步骤 4 — 写入配置

```bash
mkdir -p ~/.config/grok-search
chmod 700 ~/.config/grok-search
```

写入 `~/.config/grok-search/config.json`（`chmod 600`），最小可用示例：

**chat / grok2api：**

```json
{
  "apiUrl": "https://用户提供的base/v1",
  "apiKey": "用户提供的key",
  "apiProvider": "openai-compatible",
  "searchEndpoint": "chat",
  "model": "grok-4.3-fast",
  "defaultExtra": 6,
  "sourceChars": 400
}
```

**responses：**

```json
{
  "apiUrl": "https://用户提供的base/v1",
  "apiKey": "用户提供的key",
  "apiProvider": "openai-compatible",
  "searchEndpoint": "responses",
  "model": "grok-4.5",
  "responsesMaxTurns": 3,
  "responsesReasoningEffort": "low",
  "defaultExtra": 6,
  "sourceChars": 400
}
```

可选：用户若有 Tavily key，可再问是否写入 `tavilyApiKey`（非安装必需）。

写完后简短确认：协议、模型、掩码后的 key、配置路径。

### 步骤 5 — 询问是否测试

问用户：是否现在跑一次连通性测试？

- **否** → 说明配置已写入路径，并给出一条示例命令；**安装结束**。  
- **是** → 进入步骤 6。

### 步骤 6 — 连通性测试

在 `SKILL_ROOT` 执行（关闭 extra，只测 Grok 通道）：

```bash
node "$SKILL_ROOT/scripts/search.js" --no-extra "随便搜个新闻"
```

**成功判定（全部满足）：**

- 退出码 `0`  
- stdout JSON **没有** `error` 字段  
- `diagnostics.grok_endpoint` 等于用户选的 `chat` 或 `responses`  
- `answer.text` 非空  
- 理想情况：`sources.grok` 长度 ≥ 1，或 `diagnostics.chat_web_search_calls` / `responses_web_search_calls` > 0（部分上游不回传 citation，只要 answer 明显基于实时检索也可算通过，但要告诉用户「无 citation」）

**成功** → 告知「安装配置完成」，列出配置路径与示例搜索命令；结束。

**失败** → 不要盲目重试同一命令；按步骤 7 分支，**针对原因向用户追问/请用户改配置**。

### 步骤 7 — 失败原因与追问

从 stdout JSON 读 `error.code`、`error.message`、`diagnostics`（HTTP 状态常在 message 的 `HTTP NNN:` 里）。

| 现象 | 可能原因 | Agent 应问 / 应做 |
| --- | --- | --- |
| `GROK_API_URL 未配置` / `GROK_API_KEY 未配置` | 配置路径错误或未写入 | 确认是否写到 `~/.config/grok-search/config.json`；检查权限；重新步骤 2–4 |
| `HTTP 401` / `403` | key 错误、过期、无权限 | 请用户核对/更换 apiKey；确认 key 是否属于该 apiUrl |
| `HTTP 404` 且路径像 `/responses` 或 `/chat/completions` | 协议与网关不匹配，或 base URL 多/少了 `/v1` | 问用户网关文档里搜索走 chat 还是 responses；请用户确认 base 是否应含 `/v1`；可建议切换 `searchEndpoint` |
| `HTTP 422` / 协议不支持 / tool 报错 | 模型或 endpoint 不支持 `web_search` | 问是否换协议；chat 建议换 `grok-4.3-fast`；responses 问是否应改用 `grok-4.5` |
| `model_not_found` / 无可用渠道 | 模型 ID 在该中转不存在 | 请用户从中转后台复制**确切**模型名再写入 `model` |
| `HTTP 402` / `GROK_QUOTA_EXHAUSTED` / 额度、余额 | 欠费或配额用尽 | 请用户检查中转余额；可选配置 Tavily 做 extra 降级（安装本身仍算配置成功但搜索不可用） |
| `HTTP 429` | 限流 | 问是否稍后重试；是否需代理；是否换 key/渠道 |
| 超时 / 网络错误 / `fetch failed` | 代理或出境网络 | 问是否使用代理；可试 `GROK_PROXY=http://127.0.0.1:7890`（端口按用户环境）；或 `GROK_PROXY=off` |
| 退出 0 但 answer 称「无法联网」且无 sources | 请求达模型但未启用搜索 | 确认 `searchEndpoint` 与模型匹配；chat 是否误用 responses-only 模型；请用户确认该模型在中转面板是否开启联网 |
| `GROK_CHAT_EMPTY` / `GROK_RESPONSES_EMPTY` | 上游空响应 | 换模型或协议后重测；把脱敏后的 `diagnostics` 摘要给用户 |
| `npm` / 依赖错误 | 环境问题 | 检查 Node 版本与网络；代理下重装 `npm install` |

每轮修复后：只改相关字段 → 再问是否重测 → 用户同意再跑步骤 6。  
连续失败时：汇总已尝试项，避免死循环；请用户提供中转控制台里的「模型 ID + 是否支持 web search」截图/说明（不要 key）。

### 安装完成检查清单

- [ ] Node `>=18.17`，`npm install` 已完成  
- [ ] `~/.config/grok-search/config.json` 权限 `600`  
- [ ] `searchEndpoint` + `model` 与用户网关一致  
- [ ] 用户同意测试时：`--no-extra` 搜索成功且 `grok_endpoint` 正确  
- [ ] 未在聊天中泄露完整 API key  

### 安装后最小命令

```bash
node "$SKILL_ROOT/scripts/search.js" --no-extra "query"
node "$SKILL_ROOT/scripts/fetch.js" https://example.com
node "$SKILL_ROOT/scripts/map.js" https://example.com --limit 5
```

## 在 pi 中使用（示例）

把本目录 clone 或复制到你的 pi skills 位置，然后通过 `SKILL.md` 启用这个 skill。

示例命令仍然是直接运行脚本：

```bash
./scripts/search.js "latest Node.js LTS"
./scripts/fetch.js https://example.com
./scripts/map.js https://docs.example.com --limit 20
```

其他 agent harness 也可以采用同样方式：读取 `SKILL.md`，再按需运行 `scripts/search.js`、`scripts/fetch.js`、`scripts/map.js`。

## 文档

- [架构说明](docs/architecture.md)
- [功能说明](docs/features.md)
- [Responses 搜索协议](docs/responses-mode.md)
- [Chat Completions 搜索协议](docs/chat-mode.md)
- [Smoke Tests](docs/smoke-tests.md)
- [公开 Benchmark](docs/benchmark.md)
- [评测方法研究](docs/web-search-evaluation-research.md)

## 配置

推荐把长期使用的 key 放到：

```text
~/.config/grok-search/config.json
```

可以从示例文件复制：

```bash
mkdir -p ~/.config/grok-search
cp config.example.json ~/.config/grok-search/config.json
chmod 600 ~/.config/grok-search/config.json
```

完整配置示例：

```json
{
  "apiUrl": "https://api.x.ai/v1",
  "apiKey": "your-grok-api-key",
  "apiProvider": "xai",
  "searchEndpoint": "responses",
  "model": "grok-4.3",
  "responsesMaxTurns": 3,
  "responsesReasoningEffort": "low",
  "responsesAllowedDomains": [],
  "responsesExcludedDomains": [],
  "responsesIncludeXSearch": false,
  "responsesAllowedXHandles": [],
  "responsesExcludedXHandles": [],
  "responsesOpenRouterEngine": "auto",
  "defaultExtra": 6,
  "sourceChars": 400,
  "tavilyApiKey": "",
  "tavilyApiUrl": "https://api.tavily.com",
  "firecrawlApiKey": "",
  "firecrawlApiUrl": "https://api.firecrawl.dev/v2",
  "outputDir": ""
}
```

常见填写规则：

- `apiUrl` 填 API base URL；脚本会请求 `{apiUrl}/responses` 或 `{apiUrl}/chat/completions`，不要把路径本身写进去。
- `searchEndpoint` 选择搜索协议：
  - `responses`（默认）：CPA / xAI 风格 agentic search，常见可用模型如 `grok-4.5`。
  - `chat`：Chat Completions + `web_search`，适合 grok2api / NewAPI 等中转；推荐 `grok-4.3-fast`、`grok-4.20-fast`、`grok-4.20-0309-non-reasoning`。
- `apiProvider` 一次只能填写一个值：
  - `xai`：xAI 官方接口，使用 `web_search`，并可启用 `x_search`。
  - `openrouter`：OpenRouter 接口，改用 `openrouter:web_search`；可通过 `responsesOpenRouterEngine` 选择搜索引擎。
  - `openai-compatible`：支持 xAI 风格 Responses 和/或 Chat Completions `web_search` 的中转、反代或兼容服务。
- `apiProvider` 省略时会按 URL 推断：包含 `openrouter` 视为 `openrouter`，包含 `api.x.ai` 视为 `xai`，其他 URL 视为 `openai-compatible`。中转服务建议显式填写，避免请求格式判断错误。
- `model` 必须填写该 endpoint 实际支持的模型 ID。许多中转上 **Responses 搜索只对 `grok-4.5` 可用**；chat 搜索请用 `grok-4.3-fast` 等，不要默认用 `grok-4.5`（CPA）。`responsesMaxTurns` 是不小于 1 的整数（仅 responses）。`responsesReasoningEffort` 常见值为 `low`、`medium`、`high`，但是否支持取决于具体模型与 provider。
- `responsesAllowedDomains`、`responsesExcludedDomains`、`responsesAllowedXHandles`、`responsesExcludedXHandles` 都是数组，可以填写多个值，例如 `["github.com", "docs.python.org"]`；同一组 allowed 与 excluded 不能同时使用。环境变量中的多值使用逗号分隔。这些过滤对 chat 路径同样生效。
- `responsesOpenRouterEngine` 可选 `auto`、`native`、`exa`、`firecrawl`、`parallel` 或 `perplexity`，仅在 `apiProvider` 为 `openrouter` 时生效。
- `tavilyApiKey` 可留空；`firecrawlApiKey` 也可留空并使用 Firecrawl Keyless。`outputDir` 留空时使用默认目录 `~/.cache/grok-search/outputs/`。

如果使用 OpenRouter，核心字段可改为：

```json
{
  "apiUrl": "https://openrouter.ai/api/v1",
  "apiKey": "your-openrouter-api-key",
  "apiProvider": "openrouter",
  "searchEndpoint": "responses",
  "model": "your-openrouter-model-id",
  "responsesOpenRouterEngine": "auto"
}
```

如果使用 grok2api / NewAPI 等 chat 侧联网中转：

```json
{
  "apiUrl": "https://your-endpoint.example/v1",
  "apiKey": "your-api-key",
  "apiProvider": "openai-compatible",
  "searchEndpoint": "chat",
  "model": "grok-4.3-fast"
}
```

如果使用 Responses-compatible 中转服务：

```json
{
  "apiUrl": "https://your-endpoint.example/v1",
  "apiKey": "your-api-key",
  "apiProvider": "openai-compatible",
  "searchEndpoint": "responses",
  "model": "the-model-id-supported-by-your-endpoint"
}
```

然后编辑复制过去的文件，填入真实 key。环境变量仍然优先于配置文件，适合临时覆盖或 CI 使用。

本项目**不会自动加载 `.env` 文件**。如果你想用环境变量，请自己在 shell 里 export。

### 代理

Node 原生 `fetch` 默认不会可靠读取终端代理变量。本项目会在检测到代理环境变量时自动安装 `undici` 的 `EnvHttpProxyAgent`，让所有出站请求走你的终端代理配置。

支持的变量：

- `HTTP_PROXY` / `http_proxy`
- `HTTPS_PROXY` / `https_proxy`
- `ALL_PROXY` / `all_proxy`
- `NO_PROXY` / `no_proxy`
- `GROK_PROXY`：显式给本工具指定一个代理 URL；设为 `GROK_PROXY=off` 可强制直连

`NO_PROXY` 会被尊重，并且会始终把回环地址（`localhost`、`127.0.0.1`、`::1`）加入绕过列表。

| 环境变量 | 配置文件 key | 是否必需 | 用途 | 说明 |
| --- | --- | --- | --- | --- |
| `GROK_API_URL` | `apiUrl` | search 必需 | `search.js` | API base URL。 |
| `GROK_API_KEY` | `apiKey` | search 必需 | `search.js` | `GROK_API_URL` 对应的 API key。 |
| `GROK_API_PROVIDER` | `apiProvider` | 否 | `search.js` | 选择 tool 请求格式，而不是额外的搜索源；可选 `xai`、`openrouter` 或 `openai-compatible`。未配置时按 URL 推断。 |
| `GROK_SEARCH_ENDPOINT` | `searchEndpoint` | 否 | `search.js` | `responses`（默认）或 `chat`。 |
| `GROK_MODEL` | `model` | 否 | `search.js` | 默认 `grok-4.3`；chat 搜索常用 `grok-4.3-fast`。 |
| `GROK_RESPONSES_MAX_TURNS` | `responsesMaxTurns` | 否 | Responses | 默认 `3`，控制 Responses agentic turn 上限。 |
| `GROK_RESPONSES_REASONING_EFFORT` | `responsesReasoningEffort` | 否 | Responses | 默认 `low`。 |
| `GROK_RESPONSES_ALLOWED_DOMAINS` | `responsesAllowedDomains` | 否 | Responses / Chat | 逗号分隔 domain allow-list，最多 5 个；与 excluded 互斥。 |
| `GROK_RESPONSES_EXCLUDED_DOMAINS` | `responsesExcludedDomains` | 否 | Responses / Chat | 逗号分隔 domain deny-list，最多 5 个；与 allowed 互斥。 |
| `GROK_RESPONSES_INCLUDE_X_SEARCH` | `responsesIncludeXSearch` | 否 | Responses / Chat | 是否启用 direct xAI `x_search`。默认 `false`。 |
| `GROK_RESPONSES_ALLOWED_X_HANDLES` | `responsesAllowedXHandles` | 否 | Responses / Chat | X handle allow-list；与 excluded 互斥。 |
| `GROK_RESPONSES_EXCLUDED_X_HANDLES` | `responsesExcludedXHandles` | 否 | Responses / Chat | X handle deny-list；与 allowed 互斥。 |
| `GROK_RESPONSES_OPENROUTER_ENGINE` | `responsesOpenRouterEngine` | 否 | OpenRouter | `auto`、`native`、`exa`、`firecrawl`、`parallel` 或 `perplexity`。默认 `auto`。 |
| `GROK_DEFAULT_EXTRA` | `defaultExtra` | 否 | `search.js` | Tavily 与 Firecrawl 合计的默认 extra source 数量。默认 `6`。 |
| `GROK_SOURCE_CHARS` | `sourceChars` | 否 | `search.js` | 每条 source stdout snippet 长度。默认 `400`；`0` 表示不输出 snippet。 |
| `TAVILY_API_KEY` | `tavilyApiKey` | 否 | `search.js`、`fetch.js`、`map.js` | 启用 Tavily Search / Extract / Map。没有它时，search/fetch 仍可使用 Firecrawl Keyless，map 使用 Direct Map。 |
| `TAVILY_API_URL` | `tavilyApiUrl` | 否 | Tavily 路径 | 默认 `https://api.tavily.com`。 |
| `FIRECRAWL_API_KEY` | `firecrawlApiKey` | 否 | `search.js`、`fetch.js` | 可选。未配置时使用 Firecrawl Keyless；配置后使用独立账户额度和更高限流。 |
| `FIRECRAWL_API_URL` | `firecrawlApiUrl` | 否 | Firecrawl 路径 | 默认 `https://api.firecrawl.dev/v2`。 |
| `GROK_OUTPUT_DIR` | `outputDir` | 否 | 所有脚本 | 覆盖长输出落盘目录。默认 `~/.cache/grok-search/outputs/`。 |
| `GROK_DEBUG` | — | 否 | 所有脚本 | 仅环境变量。设为 `true` 时把重试 / 清理 / 代理调试日志写到 stderr。 |
| `GROK_PROXY` | — | 否 | 所有脚本 | 仅环境变量。显式代理 URL，或设为 `off` / `direct` 禁用代理。 |

OpenRouter 使用 `openrouter:web_search` server tool，不会给模型名追加 `:online`。

## 输出 schema

当前版本使用命令原生 JSON 输出。这是相对旧版 `ok` / `kind` envelope 的 **breaking change**。

失败时每个脚本都会返回：

```json
{
  "error": {
    "message": "...",
    "code": "FETCH_ERROR"
  },
  "diagnostics": {
    "warnings": [],
    "provider_attempts": []
  }
}
```

成功时，provider attempts、warnings、时间戳和命令选项都放在 `diagnostics` 下。

## Search

```bash
./scripts/search.js "What changed in the latest Node.js LTS?"
./scripts/search.js --search-endpoint chat --model grok-4.3-fast "随便搜个新闻"
./scripts/search.js --platform GitHub "pi coding agent search skill"
./scripts/search.js --extra 10 "latest pi coding agent docs"
./scripts/search.js --no-extra "query"
./scripts/search.js --source-chars 200 "query"
./scripts/search.js --full-sources "debug provider raw"
./scripts/search.js --responses-openrouter-engine exa "strict web-only query"
./scripts/search.js --responses-x-search --responses-allowed-x-handles xai,OpenAI "query"
```

`search.js` 通过 `searchEndpoint` / `--search-endpoint` 选择协议：

- `responses`（默认）：`{GROK_API_URL}/responses`，CPA / xAI 风格 agentic search（常见如 `grok-4.5`）
- `chat`：`{GROK_API_URL}/chat/completions`，适合 grok2api / NewAPI（推荐 `grok-4.3-fast`、`grok-4.20-fast`、`grok-4.20-0309-non-reasoning`）

成功时返回：

- `answer.text`、`answer.chars`、`answer.original_chars`、`answer.truncated`、`answer.full_path`
- `sources.grok`、`sources.extra`、`sources.merged` 短 source card
- `sources.raw_path`，在完整 source / provider raw 落盘时出现
- `sources.raw`，仅在使用 `--full-sources` 时出现
- `diagnostics.grok_endpoint`（`responses` 或 `chat`）、`diagnostics.usage` / `diagnostics.cost_usd`（provider 返回时）、`diagnostics.warnings`、`diagnostics.provider_attempts`、`diagnostics.options`、`diagnostics.searched_at`

默认会同时发起 Grok（Responses 或 Chat）、Tavily Search（配置 key 时）和 Firecrawl Search。三路并行，Tavily/Firecrawl 结果始终作为独立补充信源，不会注入 Grok input。

`--extra N` 表示 Tavily 与 Firecrawl 合计的结果目标数，默认 `6`。两家都可用时平均分配，奇数优先给 Tavily；没有 Tavily key 时全部交给 Firecrawl Keyless。`--no-extra` 会严格关闭两个外部搜索通道。

当 Grok 明确返回额度耗尽，而 extra sources 可用时，命令会返回标记为 `diagnostics.degraded: true` 的降级结果。`answer.text` 会明确说明当前仅为 Tavily/Firecrawl 原始搜索结果，`diagnostics.grok_error` 保留脱敏后的额度错误。其他认证、协议或服务错误不会被伪装成额度降级。

Firecrawl Keyless 提供每月 1,000 credits，并受按 IP 的每日限额约束。配置 `FIRECRAWL_API_KEY` 不会增加免费计划的月度 credits，但能获得更高限流、独立账户额度和更多 API 能力。

Source card 不再输出长 `description` 或 `content` 字段，只输出短 `snippet`。完整 raw 数据可通过 `sources.raw_path` 按需读取。

## Fetch

```bash
./scripts/fetch.js https://example.com
./scripts/fetch.js --provider direct https://example.com
```

fetch 默认只返回 12,000 字符 preview。`--max-chars 50000` 应作为看过 preview 后的显式深读使用，不是常规默认。

```bash
./scripts/fetch.js --max-chars 50000 https://example.com
```

`--provider auto` 的 provider 顺序：

```text
Tavily Extract -> Firecrawl Scrape -> Direct Fetch
```

Direct Fetch 是普通 HTTP(S) 文本页面的 best-effort fallback。它会做简单 HTML 清理、尽量格式化 JSON、记录重定向，并拒绝二进制 / 附件 / 超大响应。

Firecrawl Scrape 无 key 时会使用 Keyless；配置 `FIRECRAWL_API_KEY` 后会自动发送 Bearer token。当前认证模式写入 `diagnostics.firecrawl_auth_mode`。

fetch 成功输出使用 `content.text`、`content.chars`、`content.original_chars`、`content.truncated`、`content.full_path`，provider 相关信息放在 `diagnostics`。

## Map

```bash
./scripts/map.js https://docs.example.com --limit 20
./scripts/map.js --provider direct https://docs.example.com
./scripts/map.js https://docs.example.com --instructions "only API reference pages" --max-depth 2
```

`--provider auto` 的 provider 顺序：

```text
Tavily Map -> Direct Map
```

没有 `TAVILY_API_KEY` 时，Tavily Map 不可用，`map.js` 会 fallback 到 Direct Map。Direct Map 只检查同站点 `/sitemap.xml`，然后提取首页同域名链接。它会忽略 `--instructions`，且只支持 `--max-depth 1`。

map 成功输出使用 `urls` 表示发现的 URL。provider、response time、ignored instructions、warnings、attempts 和 options 都放在 `diagnostics`。

## 输出文件

所有脚本都会保证 stdout 是完整 JSON。长文本字段会以 preview 形式返回，完整内容写入：

```text
~/.cache/grok-search/outputs/
```

设置 `GROK_OUTPUT_DIR` 可以覆盖该路径。每次运行都会 best-effort 清理输出目录中超过 30 天的 `grok-search-*` 文件。

只有 preview 不够时才读取这些路径：

- `answer.full_path`：完整 search answer
- `content.full_path`：完整 fetch 页面正文
- `sources.raw_path`：完整 source / provider raw 数据

## Smoke Tests

不需要 key：

```bash
./scripts/fetch.js --provider direct https://example.com
./scripts/map.js --provider direct https://example.com --limit 5
node tests/sources.test.js
node tests/proxy.test.js
node tests/responses.test.js
node tests/chat.test.js
node tests/argv.test.js
```

搜索需要 Grok 配置：

```bash
export GROK_API_URL="https://your-openai-compatible-endpoint/v1"
export GROK_API_KEY="your-key"
./scripts/search.js "What changed in the latest Node.js LTS?"
# chat / grok2api example
export GROK_SEARCH_ENDPOINT=chat
export GROK_MODEL=grok-4.3-fast
./scripts/search.js --no-extra "随便搜个新闻"
```

## 常见错误

- `GROK_API_URL 未配置`：使用 `search.js` 前需要设置 `GROK_API_URL`。
- `GROK_API_KEY 未配置`：使用 `search.js` 前需要设置 `GROK_API_KEY`。
- `GROK_QUOTA_EXHAUSTED`：Grok 额度耗尽且 extra 被关闭，或 Tavily/Firecrawl 都没有返回可用降级结果。
- `TAVILY_API_KEY 未配置`：显式请求了 `--provider tavily`，但没有配置 Tavily key。
- Direct Fetch 返回二进制 / 附件错误：目标 URL 不是文本页面，或对 direct fallback 来说太大。
- Direct Map 返回很少或 0 个 URL：站点可能依赖 JavaScript、隐藏链接，或没有公开 sitemap。

## 项目边界

当前范围包括：

- `search.js`
- `search.js --extra N`
- 带 Direct Fetch fallback 的 `fetch.js`
- 带 Direct Map fallback 的 `map.js`
- 长输出 preview 和完整输出文件
- `SKILL.md`
- `references/planning.md`
- smoke / fixture tests

不在范围内：

- 浏览器渲染
- PDF / 图片 / 压缩包解析
- Cookie、登录或反爬绕过
- MCP 会话状态，例如 `get_sources`
- CLI 打包或 build 流程

## 致谢与来源

本仓库（[Autsunset/grok-search](https://github.com/Autsunset/grok-search)）在 [BlueOcean223/grok-search](https://github.com/BlueOcean223/grok-search) 的 JS skill 形态上继续维护，并补充了 Chat Completions（grok2api / NewAPI）搜索路径。

原版 JS skill 项目：

- [BlueOcean223/grok-search](https://github.com/BlueOcean223/grok-search)

更早的 Python / MCP 思路来源：

- [GuDaStudio/GrokSearch](https://github.com/GuDaStudio/GrokSearch/)

感谢 [BlueOcean223](https://github.com/BlueOcean223/grok-search) 与 GuDaStudio 提供的原始项目与思路。本项目在保留核心搜索 / 抓取 / 站点映射能力的基础上，继续作为 **纯 JS、脚本直跑** 的 agent skill 分发。

本项目分享于[Linuxdo社区](https://linux.do/)。

## 协议

本项目使用 MIT 协议发布，详见 [LICENSE](LICENSE)。

原项目同样使用 MIT 协议。我们在 `LICENSE` 中保留了原项目版权声明，以遵守 MIT 协议要求。
