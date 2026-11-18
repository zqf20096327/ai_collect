# flowgoogle2api

把 [Google Flow](https://flow.google.com) 的图像生成与编辑能力封装成 OpenAI 兼容 API。默认输出 2K，支持多账号轮换，自带账号管理台与请求日志。

> 非官方项目。Flow 的网页接口不是公开 API，上游随时可能变更。

## 特性

- **OpenAI 兼容**：`/v1/models`、`/v1/images/generations`、`/v1/images/edits`、`/v1/chat/completions`
- **模型**：`nano-banana-pro`、`nano-banana-2.1`、`nano-banana-2-lite`
- **五档比例**：1:1 / 4:3 / 3:4 / 16:9 / 9:16，按 `size` 就近映射，或用 `aspect_ratio` 直接指定
- **2K 输出**：生成后走一次 `SPrCad` 重塑；失败重试一次，仍失败则降级返回 1K，而不是整单报错
- **多账号**：单个 Chrome 进程，每账号一个隔离 BrowserContext，每账号 N 个 worker 标签页
- **预热斜坡**：新标签页按账号串行预热，铺满后才放开并发，避开 Google 的异常活动判定
- **管理台** `/admin`：账号热增删改、Cookie 粘贴导入与校验、成功/失败计数、请求日志

## 工作方式

```
下游（OpenAI 格式）
   │
   ▼
Fastify ── 鉴权 / 并发闸门 / 图片托管
   │
   ▼
一个无头 Chrome
├── context(account A) ── worker tab × N
└── context(account B) ── worker tab × N
   │
   ▼
flow.google.com  (batchexecute RPC)
```

上游调用全部发生在标签页内：`jHPbke` 建项目、`ogiZ0b` 生成/编辑、`SPrCad` 2K 重塑、`as29s` 保存媒体、`QI2zvc` 收尾。比例是 `ogiZ0b` 请求体里的枚举字段。reCAPTCHA token 由页面内的 `grecaptcha.enterprise.execute` 铸造，一次性、约 2 分钟有效。

智能体通道（WebChannel）保留为可选路径（`AGENT_MODE=true`），默认关闭：它更慢，也更容易被上游限流。

## 快速开始

Docker（推荐，镜像内含 Chrome）：

```bash
cp .env.example .env          # 至少填 AUTH_KEY、FLOW_PROXY
docker compose up -d --build
```

本地 Node：

```bash
npm install
cp .env.example .env
npm start
```

## 导入账号

1. 在已登录 `flow.google.com` 的 Chrome 里打开 DevTools → Network → 刷新 → 点任意一个 `flow.google.com` 请求 → Request Headers → 复制整行 `Cookie`
2. Application → Cookies → `https://accounts.google.com` → 复制 `LSID` 的值，追加到上一步末尾：`; LSID=...`
3. 打开 `http://<host>:3000/admin`，输入 `AUTH_KEY`，新增账号并粘贴保存

保存前服务会用这份 cookie 请求一次 `flow.google.com`，页面内有 `SNlM0e`（已登录）才写入。之后上游下发的 `Set-Cookie`（`SIDCC`、`__Secure-1PSIDTS` 等轮换）会被合并回账号并落盘，所以**持续被调用的账号不会因轮换过期**；长期闲置仍需重新导入。

## 接口

请求头统一带 `Authorization: Bearer $AUTH_KEY`。

### POST /v1/images/generations

| 字段 | 说明 |
|---|---|
| `prompt` | 必填 |
| `model` | `nano-banana-pro`（默认）/ `nano-banana-2.1` / `nano-banana-2-lite` |
| `n` | 1–4；内部拆成 n 个并发生成，全部完成后统一返回 |
| `size` | 如 `1536x1024`，按比例就近映射到五档 |
| `aspect_ratio` | `1:1` / `4:3` / `3:4` / `16:9` / `9:16`，优先于 `size` |
| `quality` | `2k`（默认）/ `1k` |
| `response_format` | `url`（默认，托管在本服务）/ `b64_json` |

```bash
curl http://127.0.0.1:3000/v1/images/generations \
  -H "Authorization: Bearer $AUTH_KEY" -H "Content-Type: application/json" \
  -d '{"prompt":"a cabin in a snowy forest","aspect_ratio":"4:3","model":"nano-banana-2.1"}'
```

### POST /v1/images/edits

multipart：`image`（可重复，最多 4 张）+ `prompt` + 上表其余字段。也接受 JSON：`images` 里放 data URL，或 `{"image_url":"https://..."}`（仅公网 http(s)，单张 ≤ 15MB）。

### POST /v1/chat/completions

取最后一条用户消息作为 prompt 出图，返回 markdown 图片；支持 `stream`（SSE）。

### 其他

- `GET /health`：账号数、每账号 worker 数、全局闸门状态
- `GET /v1/accounts`：账号池快照
- `GET /images/:name`：托管图片

## 并发与风控

| 变量 | 默认 | 说明 |
|---|---|---|
| `WORKERS_PER_ACCOUNT` | 4 | 每账号 worker 标签页数，也是单账号并发上限 |
| `MAX_CONCURRENCY` | 128 | 全局同时在跑的上游请求数，超出排队 |
| `QUEUE_TIMEOUT_MS` | 120000 | 排队超时后返回 429 |

**预热斜坡**：服务启动（或账号 context 被回收重建）后，每个账号的前 N 个请求严格串行，每个 worker 标签页成功出图一次才放开并发。原因——触发风控(PUBLIC_ERROR_UNUSUAL_ACTIVITY)；逐个预热后，同样的并发就不再触发风控。日志里出现 `warmup ramp complete for <id> (N tabs)` 表示斜坡结束，`risk control flagged <id> on worker <k>` 表示某个标签页被判定异常。

其他实测结论：

- 风控是**账号级**的：一旦触发，该账号短时间内的生成请求全部快速失败（`PUBLIC_ERROR_UNUSUAL_ACTIVITY`），重试无用，等几分钟再试
- 单账号并发 3 以内比较稳；要提高总并发就加账号，而不是加 worker
- 同一账号不要同时在本服务和浏览器里活跃使用，两边会互相顶掉轮换 cookie
- 2K 那一步最容易撞风控：首次 `SPrCad` 前有 0.8–1.2s 随机延迟，失败重试一次，仍失败降级 1K

## 管理台

`/admin` 页面公开，接口需要 `AUTH_KEY`。

- 账号列表：状态（正常 / 冷却 / 登录失效 / 停用）、cookie 数、成功/失败次数、最近错误、在途请求
- 增删改即时生效，无需重启；换 cookie 会关闭该账号现有 context 并重新走预热
- 请求日志：生成 / 编辑 / 对话，含耗时、状态、账号、字节数、完整提示词与错误，支持分页与批量删除

运行时数据都在 `data/`（已 gitignore）：

| 文件 | 内容 |
|---|---|
| `accounts.json` | 账号与 cookie |
| `stats.json` | 成功/失败计数，重启保留 |
| `logs.jsonl` | 请求日志，最多 5000 条 |
| `images/` | 托管图片，默认 1 小时 TTL |

## 配置

完整列表见 `.env.example`，常用项：

| 变量 | 默认 | 说明 |
|---|---|---|
| `AUTH_KEY` | 空 | 下游鉴权；留空不校验，仅建议本地 |
| `FLOW_PROXY` | 空 | 访问 Google 的代理，浏览器与图片下载共用 |
| `PUBLIC_BASE_URL` | `http://127.0.0.1:$PORT` | 图片链接基地址，对外服务必须设置 |
| `DEFAULT_MODEL` / `DEFAULT_ASPECT` / `DEFAULT_2K` | `nano-banana-pro` / `16:9` / `true` | 下游未指定时的默认值 |
| `GENERATE_TIMEOUT_MS` | 180000 | 单张生成的超时，排队时间不计入 |
| `IMAGE_TTL_MS` | 3600000 | 托管图片保留时长 |
| `CHROME_HEADLESS` | true | 设为 false 可看到浏览器 |
| `CHROME_CDP_URL` | 空 | 复用已运行的 Chrome；生产环境留空，服务自动拉起 |
| `ACCOUNTS_FILE` / `STATS_FILE` / `LOGS_FILE` | `data/...` | 数据文件路径 |

## 部署

```bash
cp .env.example .env
docker compose up -d --build
```

- 容器内自带 Chrome，`shm_size: 512mb`，以 `--no-sandbox` 运行
- 内存参考：Chrome 主进程 + Node 约 0.4GB，每个 flow 标签页 90–120MB。单账号 3 worker 约 0.6GB；24 并发（8 账号 × 3 tab）建议 8GB
- 低内存机器不要在上面构建镜像（解压 Chrome 层容易 OOM）：本地 `docker build -t flowgoogle2api .`，再 `docker save | ssh host 'docker load'`
- 图片落盘 `data/images` 并按 TTL 清理；高吞吐场景可把该目录挂到 tmpfs

## 排障

| 现象 | 处理 |
|---|---|
| `AUTH_REQUIRED ... no SNlM0e` | cookie 失效，在 `/admin` 重新导入（记得补 `LSID`） |
| `PUBLIC_ERROR_UNUSUAL_ACTIVITY` | 风控。等几分钟；检查启动后是否完整走完预热斜坡 |
| `PER_MODEL_DAILY_QUOTA_REACHED` | 该账号该模型当日额度用尽，换模型或加账号 |
| `429 server busy` | 全局并发已满，调大 `MAX_CONCURRENCY` 或加账号 |
| `generation timed out` | 单张超时，多为上游抖动；检查代理与内存 |
| 图片 404 | 托管已过期，调大 `IMAGE_TTL_MS` 或改用 `b64_json` |

协议逆向细节见 [docs/RECON.md](docs/RECON.md)。

## 项目结构

```
src/
  server.ts            Fastify 路由、鉴权、管理接口
  generate.ts          账号选择、预热斜坡、生成编排、2K
  accounts.ts          账号池、cookie、计数
  logs.ts              请求日志
  store.ts             图片托管与清理
  google/browser.ts    单 Chrome、每账号 context、worker 标签页
  google/session.ts    boot / RPC / reCAPTCHA
  flow/client.ts       Flow RPC 封装
  web/admin.html       管理台
docs/RECON.md          逆向记录
```

## 免责声明

非官方项目，与 Google 无关。使用本项目可能违反 Google 服务条款并导致账号受限；请自行评估风险，勿用于商业转售或批量滥用。

## 许可证

[MIT](LICENSE) © 2026 iamdurant
