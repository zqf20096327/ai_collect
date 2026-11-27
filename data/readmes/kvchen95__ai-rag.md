# ai-rag · 企业级零幻觉知识库

私有化 PDF 知识库问答：答得上就答，答不上就说不知道，每条结论可点回原文。

![问答工作台演示：基于长鑫科技、寒武纪财报的带引用问答](figures/qa-workbench-demo.png)

## 文档

| 文件 | 内容 |
|---|---|
| `架构图集.md` | 分层架构、时序、状态机、部署拓扑（Mermaid 图集） |
| `概要设计.md` | 目标、边界、原则、技术栈、评测口径 |
| `详细设计.md` | 12 章 + 7 附录：对象、摄取、存储、检索、门控、生成、校验、权限、验收 |

**改代码前先读 `详细设计.md` 第 2 章**（四个对象）与第 10.5 节（事件流约定）。

## 快速开始

```bash
cp .env.example .env          # 填 LLM_BASE_URL / LLM_API_KEY / LLM_MODEL
docker compose up -d          # 7 个服务：PG / Qdrant / embedding / rerank / api / worker / web
docker compose ps             # 等全部 healthy（首次启动要下模型，约 2 分钟）

make scan                     # 扫 samples/，建待转正版本
make ingest-status            # 看版本与切片状态
make promote-all              # 一次性转正所有 pending 版本
curl -s localhost:8000/healthz
```

打开 http://localhost:5173 是问答工作台。

## 关键命令

| 命令 | 作用 |
|---|---|
| `make up` / `make down` | 起停全部服务 |
| `make scan` | 扫描 `samples/` 建版本 |
| `make ingest-status` | 版本/切片/同步/漂移一览 |
| `make promote-all` | 转正所有 pending（评测前必做） |
| `make reconcile` | 以 PG 为准修向量库漂移 |
| `make eval` | 跑黄金 50 题 + 四条红线 |
| `make test` | 后端全量测试 |
| `make web-build` | 构建前端到 `web/dist`（web 容器挂的是它） |

## 样本目录约定

- `samples/{doc_key}.pdf` — 参与扫描
- `samples/_excluded/` — **不参与扫描**（`_` 开头的目录整棵跳过），放损坏件、扫描件、暂不处理的文档
- `doc_key` 由文件名生成：中文转拼音、机构名单独成段。`【上海证券】中芯国际…` → `shang-hai-zheng-quan-zhong-xin-guo-ji…`

改文件名会改 `doc_key`，等于换了一份文档。要改请先删旧版本。

## 排障

| 现象 | 原因 | 处理 |
|---|---|---|
| 所有题都拒答 | 没有 active 版本 | `make ingest-status` 看 `active`；`make promote-all` |
| `make eval` 报拿不到凭证 | 宿主缺 `AUTH_JWT_SECRET` | 在 `.env` 加一行，或用 `docker compose exec -T api python eval/run_eval.py` |
| 应答题全 `model_timeout` | LLM 网关不通或余额不足 | 直接 curl 网关确认；402 是余额，401 是 key |
| 图表切片没转译文字 | `VLM_*` 未配 | 补三项环境变量后重建 api |
| `doc_key` 是长中文名 | 容器里没装 pypinyin | 重建镜像（`docker compose build api`） |
| 前端整页空白 | 样本 PDF 缺 `/Widths`，pdf.js 画不出字 | 用 `scripts/make_samples.py` 重新生成样本 |

## 设计红线

改任何东西之前先确认不破坏这四条：

1. 陷阱题拒答率 100%
2. 数值准确率 ≥ 96%
3. 角标可点回率 ≥ 98%
4. 忠实度优先于覆盖率

`make eval` 的退出码：0 全过 / 1 不达标 / 2 有不可测项（**不得据此发布**）/ 3 评测器失败。
