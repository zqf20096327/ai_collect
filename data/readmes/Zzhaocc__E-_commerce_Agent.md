# CrossBorderOps · 跨境电商运营 Agent 平台

> 把商品项目从「能不能做」推进到「可直接交付的素材包」：7 个 Agent、13 个确定性工具、
> 双契约与三级护栏、版本化闭环。

[![Version](https://img.shields.io/badge/version-0.7.0-blue?style=flat-square)](CHANGELOG.md)
[![Python](https://img.shields.io/badge/Python-3.11%20%7C%203.13-3776AB?style=flat-square)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115%2B-009688?style=flat-square)](https://fastapi.tiangolo.com/)
[![CI](https://github.com/Zzhaocc/E-_commerce_Agent/actions/workflows/ci.yml/badge.svg)](https://github.com/Zzhaocc/E-_commerce_Agent/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-MIT-yellow?style=flat-square)](LICENSE)

---

## 产品定位

面向**跨境运营团队与代运营服务商**的运营自动化平台。它不是一个文案生成器，而是一条有输入契约、
有质量闸门、有版本记录的运营流水线：每个商品项目进来，出去的是一套可以交付给平台的素材与一份可追溯的诊断记录。

| 维度 | 说明 |
|---|---|
| 目标用户 | 跨境电商运营团队、代运营服务商、品牌出海团队 |
| 核心价值 | 把「数字口径」和「格式合规」从人的经验变成可执行、可回归的代码约束 |
| 交付形态 | 服务端应用 + Web 控制台 + REST API；Docker / Compose / 裸机三种部署 |
| 业务范围 | 市场进入判断、定价与 SKU 结构、Listing 与图文素材、广告与评论诊断回流 |
| 不覆盖 | 平台 API 直连、真实出图/出视频、多租户与计费（见 [Roadmap](#roadmap)） |

一条流水线走完，产出六类资产：市场报告、策略书、Listing 包、图片包、视频包、发布包；
广告与评论诊断会生成可追溯的回流事件，驱动素材迭代出新版本。

---

## 能力矩阵

| 环节 | 能力 | 确定性工具 | 产物 |
|---|---|---|---|
| 01 市场分析 | 类目可否进入、从哪个价格带切入 | `market_metrics` `platform_rules` | 市场报告 |
| 02 产品策略 | 定位、唯一卖点、定价、SKU 四角色 | `unit_economics` `sku_ladder` | 策略书 |
| 03 Listing 创意 | 关键词分层、葡语标题、五点、详情页 | `title_lint` `spec_consistency` | Listing 包 |
| 04 主图/详情图 | 9 图规划、出图 Prompt、像素合规 | `check_main_image` | 图片包 |
| 05 短视频 | 钩子、分镜、口播、字幕时长校验 | `video_timing` | 视频包 |
| 06 广告优化 | 漏斗诊断、盈亏线、P0/P1/P2 动作 | `ad_metrics` `budget_realloc` | 诊断计划 |
| 07 评论分析 | 八类归因、可修复率、页面修补 | `review_stats` `selling_point_rank` | 评论洞察 |
| 质量闸门 | 输入/输出契约、三级护栏、逐项自检 | 全部工具 | checks + guardrails |
| 闭环迭代 | 诊断 → 回流事件 → 素材 v2 → 第二窗口复测 | 复用上述工具 | 版本化产物 |

**闭环路径**（与一次性生成的分界）：

```text
01 市场 ──► 02 策略 ──► 03 ∥ 04 ∥ 05 ──► 人工审批 ──► 发布包
                            ▲                              │
                            │                      06 广告诊断
                            │                      07 评论归因
                            └──── FeedbackEvent ◄──────────┘
                                  （P0/P1 分级、可追溯）
                                        │
                                  素材 v2 + 第二窗口复测
```

---

## 快速开始

不需要 API key。

### Docker（推荐）

```bash
git clone https://github.com/Zzhaocc/E-_commerce_Agent.git
cd E-_commerce_Agent
docker compose up -d --build
```

打开 <http://127.0.0.1:8000>。数据落在具名卷 `app-data`，`docker compose down` 不会丢。

### 本地

```bash
git clone https://github.com/Zzhaocc/E-_commerce_Agent.git
cd E-_commerce_Agent
pip install -r requirements.txt
python -m uvicorn app.main:app --port 8000
```

Windows 也可以直接双击 `start.bat`，或运行 `.\scripts\run.ps1 -Port 8000`。

### 命令行验证

```bash
python scripts/demo.py      # 端到端跑完整链路，打印每一步的自检与成本
```

内置两个示例项目（Shopee 电动滑板车 / Mercado Livre 宠物航空箱），
点「运行完整流水线」即可看到 7 个 Agent 依次产出市场报告、定价方案、葡语 Listing、9 图规划、短视频脚本。

---

## 控制台

![控制台 · 市场分析](docs/screenshots/console-market.jpg)

左侧选项目、顶部看运行状态、中间是 7 个 Agent 的流水线与产物、右侧是本次运行的成本与自检。
点任意 Agent 卡片可切到对应产物页；「闭环迭代」会跑完整条诊断→回流→v2→复测链路。

| 广告诊断（含复测） | 评测门禁 |
|---|---|
| ![广告](docs/screenshots/console-ads.jpg) | ![评测](docs/screenshots/console-eval.jpg) |

更多截图见 [`docs/screenshots/`](docs/screenshots/)：策略、Listing、9 图、视频、评论、Trace、发布包、平台指标。

---

## 架构

```text
                    ┌──────────────────── 接入层 ────────────────────┐
                    │  REST /api  ·  Web 控制台  ·  Swagger /docs     │
                    │  中间件：CORS → X-Request-ID → 安全响应头       │
                    └───────────────────────┬──────────────────────┘
                                            │
        ┌───────────────────────────────────▼───────────────────────────────────┐
        │                         工作流引擎 RunEngine                           │
        │  状态机 queued→running→[awaiting_approval]→completed/failed          │
        │  五条路径：full_pipeline · creative_only · single · diagnose · loop  │
        │  断点字段 context / 步骤级 StepRun / 产物版本 Artifact.version        │
        └───────┬───────────────────────────────┬───────────────────────────────┘
                │                               │
     ┌──────────▼──────────┐         ┌──────────▼──────────┐
     │   Agent 运行时       │         │    确定性工具层      │
     │ 契约校验→证据→循环   │◄────────►│ 13 个纯函数工具      │
     │ →输出校验→护栏      │         │ Pydantic 参数校验    │
     └──────────┬──────────┘         └─────────────────────┘
                │
     ┌──────────▼──────────┐         ┌─────────────────────┐
     │   LLM Provider 层    │         │   可观测 / 评测      │
     │ mock / openai 兼容   │         │ TraceSpan · 结构化日志│
     └─────────────────────┘         │ 66 tests · golden   │
                                     └─────────────────────┘
```

### 一次 Agent 调用的完整轨迹

```text
输入契约校验 ── 缺字段 → 直接失败（不生成、不猜）
      │
      ▼
证据工具预计算 ── market_metrics → CR4/HHI/价格带（带 trace span）
      │
      ▼
LLM + function calling 循环 ── 上限 3 轮，防死循环烧钱
      │
      ▼
输出契约校验 ── 失败 → 带着错误信息自动重试 1 次
      │
      ▼
事后护栏 ── 标题超长→截断(repair)｜命中禁用词→阻塞发布(block)｜溯源性不足→告警(warn)
      │
      ▼
落库 ── StepRun + Artifact(version) + TraceSpan + 运行指标
```

分层、状态机、契约细节见 [架构与设计决策](docs/ARCHITECTURE.md)。

---

## 关键设计

### 1. 双契约：格式由代码约束

```python
class MarketInput(InputModel):  # extra="allow"
    competitor_rows: list[CompetitorRow] = Field(min_length=3)  # 少于 3 条直接拒绝


class MarketOutput(StrictModel):  # extra="forbid"
    precheck: PrecheckOut  # verdict 只能是 GO/CAUTION/NO_GO
    confidence: float = Field(ge=0, le=1)
```

- 输入侧：缺字段 → `422`，数据不足不开工；
- 输出侧：多一个字段即校验失败 → 自动带错误信息重试一次；
- 枚举/范围约束把越界值挡在落库之前。

### 2. 数字交给脚本，模型只做解读

`unit_economics` 的反解公式写在代码里，可以手算复现：

```text
net = P·(1 − commission − payment − ad_rate − coupon) − (cogs + freight)
盈亏价 P* = cost / (1 − rate_sum − coupon)
目标价 P  = cost / (1 − rate_sum − coupon − target_margin)
券余量    = 目标价下的净利（= 最多还能让多少钱）
```

价格带波谷由脚本计算：在 p25–p75 内找 **SKU 密度局部最低且仍有成交** 的带宽。

### 3. 三级护栏

| 级别 | 例子 | 行为 |
|---|---|---|
| `repair` | 标题 128 字符 > 上限 120 | 按词边界截断，记录修复事件，落库为已通过 |
| `block` | 标题命中 `original` / `melhor do mundo` | `compliance.passed=false`，**禁止生成发布包** |
| `warn` | 参数溯源率 80%、视频字幕语速偏快 | 记录并放行，进入人工审批视野 |

护栏是代码，不依赖 Prompt 里的一句「请注意合规」。

### 4. 版本化闭环

`Artifact` 带 `version` 与 `status`（draft / approved / superseded）。
闭环时旧的 Listing 变 `superseded`，新的 v2 记录 `applied_feedback`：
改了哪一条、来自哪个 Agent 的哪条证据，全部可回溯。

### 5. 可观测与评测

- 每次 LLM / 工具 / 护栏调用都落 `TraceSpan`，带 token、成本、延迟；
- 结构化日志（`text` / `json`）带 `request_id`，响应头 `X-Request-ID` 与日志可对齐；
- 运行级指标：步骤数、checks 通过率、护栏分布、wall time；
- golden eval 10 条，其中 2 条是负向用例：缺竞品数据、费率不可达时必须失败。

更多取舍见 [设计问答](docs/DESIGN_FAQ.md)。

---

## 配置

全部通过环境变量注入，完整清单见 [`.env.example`](.env.example) 与 [运维手册](docs/OPERATIONS.md)。

| 变量 | 默认 | 说明 |
|---|---|---|
| `LLM_PROVIDER` | `mock` | `mock`（离线）/ `openai_compatible`（真实模型） |
| `LLM_BASE_URL` `LLM_MODEL` `LLM_API_KEY` | — | OpenAI 兼容网关接入参数 |
| `DATABASE_URL` | `sqlite:///./data/studio.db` | 换 PostgreSQL 只改这一行 |
| `HUMAN_APPROVAL` | `true` | 素材发布前是否必须人工审批 |
| `MAX_TOOL_STEPS` / `MAX_ATTEMPTS` | `4` / `2` | 工具轮次与输出重试上限 |
| `CORS_ORIGINS` | `*` | 生产填具体域名 |
| `LOG_LEVEL` / `LOG_FORMAT` | `INFO` / `text` | `json` 用于日志采集 |
| `DOCS_ENABLED` | `true` | 生产建议关闭 `/docs` |

---

## API 与集成

完整接口见 [`docs/API.md`](docs/API.md)，`examples/` 下是可直接执行的 JSON / `.http`。

```bash
# 探针与能力目录
curl http://127.0.0.1:8000/api/health
curl http://127.0.0.1:8000/api/ready
curl http://127.0.0.1:8000/api/meta/catalog

# 跑完整流水线（异步，返回 run_id 轮询）
curl -X POST http://127.0.0.1:8000/api/projects/prj_demo_scooter/runs \
  -H "Content-Type: application/json" -d '{"mode":"full_pipeline"}'

# 查询运行 + trace + 回流事件
curl http://127.0.0.1:8000/api/runs/{run_id}
curl http://127.0.0.1:8000/api/runs/{run_id}/trace
curl http://127.0.0.1:8000/api/runs/{run_id}/feedback

# 人工审批后发布
curl -X POST http://127.0.0.1:8000/api/runs/{run_id}/approve

# 单 Agent 预览（带 checks / guardrails / trace）
curl -X POST http://127.0.0.1:8000/api/agents/03_listing_creative/preview \
  -H "Content-Type: application/json" -d @examples/listing_preview.json

# 直接调确定性工具（口径可复算）
curl -X POST http://127.0.0.1:8000/api/tools/unit_economics/invoke \
  -H "Content-Type: application/json" -d @examples/tool_unit_economics.json
```

所有错误响应统一为 `{"detail": ..., "request_id": ...}`，排查时按 `request_id` 检索日志。

### 接入真实模型

```bash
LLM_PROVIDER=openai_compatible
LLM_BASE_URL=https://api.deepseek.com/v1
LLM_API_KEY=sk-xxx
LLM_MODEL=deepseek-chat
```

`app/llm/openai_compat.py` 是标准的 `/chat/completions` 实现，DeepSeek / Qwen / vLLM /
Ollama 等 OpenAI 兼容网关都可以接入。所有 Agent 只依赖 `chat()` 一个方法，换模型不动业务代码。

配置写错时不会静默降级：`/api/health` 会返回 `provider_error` 说明原因。

---

## 部署与运维

```bash
make install-dev     # 安装开发依赖
make test            # 测试 + 覆盖率
make lint            # ruff 静态检查
make eval            # golden 评测
make smoke           # 对已启动的服务做端到端冒烟
make docker-build    # 构建镜像
```

- **探针**：`/api/health`（存活，不查库）、`/api/ready`（就绪，查库与注册表）；
- **日志**：`LOG_FORMAT=json` 接采集平台，按 `request_id` 关联一次请求；
- **备份**：`sqlite3 data/studio.db ".backup ..."`，恢复步骤见运维手册；
- **扩容**：单机走线程池，多机需换 PostgreSQL + 任务队列；内置接口不带鉴权，对外须置于网关之后。

部署形态、故障排查表与上线检查清单见 [运维手册](docs/OPERATIONS.md)，
安全边界与漏洞报告流程见 [SECURITY.md](SECURITY.md)，
版本策略与发布流程见 [版本与发布](docs/RELEASE.md)。

---

## 运行指标

本机实测（mock provider，单机，Python 3.13 / SQLite）：

| 指标 | 数值 | 测量方式 |
|---|---|---|
| 全量流水线耗时 | ~0.1–0.2 s（5 个 Agent，含 3 路并行） | `scripts/demo.py` |
| 单次流水线 token | ~14.6k | 运行级 `metrics.tokens` |
| 单次流水线成本 | ~$0.0066（按配置单价） | 运行级 `metrics.cost_usd` |
| 自检项 | 31 项，31 通过 | `metrics.checks_passed` |
| 测试 | 66 passed | `pytest` |
| golden eval | 10/10，score 1.0 | `python -m app.eval.runner` |

数字随机器、依赖版本与文案长度波动，可用 `python scripts/demo.py` 复现。

---

## 版本与支持

- **版本号**：语义化版本（`MAJOR.MINOR.PATCH`），当前 `0.7.0`，变更记录见 [CHANGELOG](CHANGELOG.md)；
- **发布流程**：分支策略、发布检查清单与回滚步骤见 [版本与发布](docs/RELEASE.md)；
- **质量门禁**：CI 跑 ruff + pytest（3.11 / 3.13）+ golden eval + HTTP 冒烟，见 [`.github/workflows/ci.yml`](.github/workflows/ci.yml)；
- **支持渠道**：缺陷与需求走 [Issues](https://github.com/Zzhaocc/E-_commerce_Agent/issues)，
  安全问题走 [Security Advisory](SECURITY.md)（不公开披露细节）。

---

## 已知边界

- `mock` provider 是规则型实现，用于无 key 运行与回归基线；真实模型下文案质量取决于模型，
  契约、护栏、评测、闭环链路完全一致；
- 不接通平台 API、不产出真实图片/视频 —— 只留适配位；
- 内置接口不带鉴权，多租户与权限仍在 Roadmap；
- SQLite 为单写者，高并发写入需换 PostgreSQL。

---

## Roadmap

| 版本 | 内容 | 状态 |
|---|---|---|
| v0.7 | 生产化加固：结构化日志与 request_id、探针、容器化、运维与安全文档 | 已交付 |
| v0.8 | 平台 API 适配器（Shopee / Mercado Livre 拉数与回写） | 规划中 |
| v0.9 | 向量记忆：跨项目复用同类目的历史诊断 | 规划中 |
| v1.0 | 批量任务与定时调度（每日自动诊断，只把 P0 推给人） | 规划中 |
| v1.1 | 多租户 + 权限 + PostgreSQL + 对象存储 | 规划中 |

---

## 文档

| 文档 | 内容 |
|---|---|
| [架构与设计决策](docs/ARCHITECTURE.md) | 分层、状态机、契约、护栏、闭环、可观测、安全边界 |
| [设计问答](docs/DESIGN_FAQ.md) | 为什么这么设计、每个取舍的代价 |
| [API 参考](docs/API.md) | 全部端点、错误契约与示例 |
| [运维手册](docs/OPERATIONS.md) | 部署形态、探针、日志排障、备份、扩容、上线清单 |
| [版本与发布](docs/RELEASE.md) | 版本策略、分支与合并、发布检查清单、回滚 |
| [安全策略](SECURITY.md) | 安全边界与漏洞报告流程 |
| [贡献指南](CONTRIBUTING.md) | 本地开发、PR 前检查、如何新增 Agent |

---

## 许可

MIT License，见 [LICENSE](LICENSE)。示例数据为脱敏样本，不含真实店铺、账号与买家信息；
业务口径来源见文末致谢。

<details>
<summary>业务口径来源</summary>

7 个 Agent 的职责划分与业务口径来自开源项目
[AI-Cross-Border-Ecommerce-Agent-Toolkit](https://github.com/heqiangdiao-wq/AI-Cross-Border-Ecommerce-Agent-Toolkit)。
</details>
