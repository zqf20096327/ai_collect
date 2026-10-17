# ecom-rag-lab

电商知识库 RAG：稠密检索 + 中文关键词检索 → RRF 融合 → 交叉编码器重排 → 带引用的答案生成（资料不足时拒答），并附带一套在黄金集上复现的检索评估与消融矩阵。

> 仓库名是 `ecom-rag-lab`；Python 包与命令行仍是 `ecom-rag`（`uv run ecom-rag …`）。

## 速览

- **链路**：两路检索（稠密管语义、jieba + bm25s 管字面）→ 自研 RRF 融合 → bge-reranker-v2-m3 重排 → DeepSeek 生成带引用答案；每一环都能单独开关、单独度量。
- **技术栈**：Python 3.12 · FastAPI + SSE · Qdrant · Infinity（一个容器同时承载 bge-m3 嵌入与 bge-reranker-v2-m3 重排）· bm25s + jieba · Docker Compose（CPU 默认 / GPU 可选）。
- **评估**：85 题黄金集（80 可回答 + 5 不可回答）+ 7 行消融矩阵（Recall@5 / Recall@10 / MRR / nDCG@10）。检索指标不调用 LLM，CPU 路径整套约 42 分钟；评估表由 `ecom-rag evaluate` 自动写回本文件。
- **控制台**：单文件零构建 `web/ecom-rag-console.html`，双击即可离线回放真实抓取的 SSE 事件流，也可用 `?mode=live` 连本机后端。
- **规模**：164 篇文档 / 434 个 chunk / 约 41K 字符；46 个 pytest 用例，界面 21 项断言。

![检索链路控制台](data/shots/02-reranked.png)

上图是控制台的重排对照视图：左列是 RRF 融合排名，右列是重排后的排名，连线标出位次变化 ≥ 3 的候选。图中的数据来自真实运行——离线样本由 `ecom-rag capture-replay` 从同一条管线抓取，打开 HTML 即可回放。

## 快速开始

### 两条部署路径（互斥，切换前先停另一条）

| 路径 | 命令 | 说明 |
| --- | --- | --- |
| **CPU（默认）** | `docker compose -f docker/compose.yaml up -d` | 不要求显卡；**README 里的评估数字由这条路径产出**（整套评估约 42 分钟） |
| GPU（可选） | `docker compose -f docker/compose.gpu.yaml up -d` | 需要 NVIDIA 驱动 + WSL2 后端；本机实测比 CPU 快 4~36 倍（倍数取自扩容前的语料，见 [ADR 0002](docs/decisions/0002-cpu-default-and-torch-engine.md)） |

两条路径的容器名与端口相同，所以互斥；它们共享同一个模型缓存卷，切换不会重新下载模型。

```bash
# 从 CPU 切到 GPU（或反向）
docker compose -f docker/compose.yaml down
docker compose -f docker/compose.gpu.yaml up -d
```

### 步骤

```bash
# 1) 起服务；首次启动 Infinity 会下载约 4.3GB 模型
docker compose -f docker/compose.yaml up -d

# 2) Python 环境
uv sync

# 3) 配置环境变量：把 .env.example 复制成 .env，再填入自己的 LLM_API_KEY
cp .env.example .env             # Windows PowerShell：Copy-Item .env.example .env

# 4) 确认服务就绪
uv run ecom-rag health

# 5) 建索引：434 个 chunk
uv run ecom-rag build-index

# 6) 提问（需要LLM_API_KEY）
uv run ecom-rag ask "无理由退货要在多久内申请？"

# 7) 复现评估表：7 行消融 × 85 题
uv run ecom-rag evaluate
```

### 环境变量（`.env`）

代码读取的是项目根目录下的 `.env`，它已列入 `.gitignore`，不会进版本库；取值优先级：环境变量 > `.env` > 代码默认值。

| 变量 | 默认值 | 什么时候需要改 |
| --- | --- | --- |
| `LLM_API_KEY` | 空 | OpenAI Key |
| `LLM_BASE_URL` |空 |  OpenAI BaseURL |
| `LLM_MODEL` |空 | 同上 |
| `QDRANT_URL` / `INFINITY_URL` | `http://localhost:6333` / `http://localhost:7997` | 服务不在本机，或改了端口时 |
| `EMBEDDING_MODEL` / `RERANKER_MODEL` | `BAAI/bge-m3` / `BAAI/bge-reranker-v2-m3` | 必须与 `docker/compose.yaml` 里的 `--model-id` 一致 |
| `DENSE_TOP_K` / `SPARSE_TOP_K` / `RERANK_TOP_K` / `CONTEXT_TOP_K` | `20` / `20` / `8` / `5` | 检索参数，同时也是消融实验的旋钮 |
| `DEPLOYMENT_LABEL` | `CPU（docker/compose.yaml）` | 在 GPU 路径上跑 `evaluate` 时改成 GPU，避免两条路径的数字混着报 |

`LLM_TEMPERATURE`（默认 `0.0`）没有写进 `.env.example`，需要时同样可以加进 `.env`。

> 复现提示：克隆下来的仓库已带语料与黄金集（`data/corpus/`、`data/golden/`），
> 但索引产物 `data/index/` 被 gitignore，所以要先跑第 5 步。忘了也不会迷路：
> `evaluate` 会先检查前置条件，缺什么就告诉你该跑哪一步。

### 测试

```bash
uv run pytest          # 46 个用例，两秒内跑完
```

覆盖五类不依赖外部服务的部分：合成语料的一致性校验（含「数值+单位」错配）、结构感知切分、
语料编号唯一性（`doc_id` / `chunk_id` 是引用校验与黄金集标注的键）、自研 RRF 融合
（叠加项获胜 / 权重翻转冠军 / k 拉平差距）、引用抽取与拒答判定。指标实现用手算样例固定。

## 架构

```text
问题 ─┬─> 稠密检索 (bge-m3 → Qdrant)      ─┐
      └─> 关键词检索 (jieba + bm25s)       ─┴─> RRF 融合 ─> 交叉编码器重排 ─> 上下文组装 ─> LLM 生成（带引用 / 可拒答）
```

两条检索路径由本项目自己编排：稠密侧负责语义，关键词侧用 jieba 分词后自己算 BM25，融合用自己实现的
RRF（`score(d) = Σ wᵢ / (k + rankᵢ(d))`）。这样每一环都能在评估里单独开关，选择理由见
[ADR 0001](docs/decisions/0001-hybrid-retrieval-own-rrf.md)。

生成前的上下文会先做一次近重复折叠（阈值 0.55）：同一事实在语料里往往有多处表述，整份塞进上下文
会让模型把同一句话引用多遍。折叠后与引用校验共用同一个集合，避免"模型看到的"和"允许引用的"不一致。

## 评估

评估回答一个问题：**加了哪一环，指标涨了多少**。因此在同一套黄金集上跑多行配置，从单路检索一路加到重排，并附融合权重的对照行。

| 指标 | 含义 |
| --- | --- |
| Recall@5 / Recall@10 | 前 k 条里命中了多少比例的相关 chunk（能不能找到） |
| MRR | 第一条相关结果的倒数排名（多快找到第一条） |
| nDCG@10 | 考虑排名位置的增益（相关结果排得够不够靠前） |

黄金集用构造法标注：抽一个 chunk 当源，让 LLM 写一个"答案恰好落在该 chunk 里"的问题，源 chunk 即标准答案，
与源 chunk 近重复的 chunk 一并标为相关。标注还要过两道闸门：每道可回答题的源 chunk 对它自己那道题的
重排分必须 ≥ 0.5（反向校验，在上一版 34 题的黄金集上抓出过 4 道标注污染），5 道不可回答题的最高重排分必须 < 0.15。

<!-- EVAL_TABLE:START -->
_由 `uv run ecom-rag evaluate` 生成于 2026-09-14；黄金集 85 题（可回答 80 / 不可回答 5），检索指标在可回答问题上计算；部署路径：CPU（docker/compose.yaml）_

_口径提醒：语料共 434 个 chunk，且问题由 chunk 构造而来，因此绝对数值偏乐观。**可回答 80 题意味着 1 题 ≈ 1.2 个百分点**——表格只保留两位小数，行间两题以内的差异属于噪声。这张表的用途是**同一语料内横向比较**每一环的增益，而不是宣称通用效果。_

| 配置 | Recall@5 | Recall@10 | MRR | nDCG@10 |
| --- | --- | --- | --- | --- |
| 仅稠密 | 0.92 | 0.99 | 0.78 | 0.83 |
| 仅关键词 | 0.74 | 0.84 | 0.59 | 0.64 |
| 稠密+关键词+RRF（等权） | 0.84 | 0.97 | 0.70 | 0.76 |
| 稠密+关键词+RRF（权重 2:1） | 0.90 | 0.97 | 0.73 | 0.78 |
| 仅稠密+重排 | 0.89 | 0.98 | 0.74 | 0.80 |
| 稠密+关键词+RRF（等权）+重排 | 0.89 | 0.98 | 0.74 | 0.80 |
| 稠密+关键词+RRF（权重 2:1）+重排 | 0.89 | 0.98 | 0.74 | 0.80 |
<!-- EVAL_TABLE:END -->

CPU 路径上两次运行同一张表，指标逐位一致（最大差异 `0.00e+00`）。同一批数字在控制台的「评估看板」
标签页里画成条形对比：

![评估看板](data/shots/05-eval.png)

三条读表时需要注意的事：

1. **指标不再贴顶**：仅稠密的 Recall@10 是 0.99。扩容前它是 1.00，那是语料太短、单路 top-20 几乎覆盖全库造成的。
2. **等权融合的 Recall@5（0.84）低于仅稠密（0.92）**：关键词一路整体更弱，等权按同等份量掺进来会稀释强信号；
   稠密权重提到 2:1 能追到 0.90，仍低于单路。诊断见 [ADR 0005](docs/decisions/0005-hybrid-did-not-win-honest-ablation.md)。
3. **重排把 Recall@5 从 0.92 降到 0.89**（MRR 0.78→0.74、nDCG@10 0.83→0.80 同向下降），与扩容前相反。
   可能的原因是标注口径：相关集合 = 构造源 + 与之**文本近重复**的 chunk，重排如果挑中"语义更对但文字不同"的
   chunk 就会被判成没命中。要拆开检索质量与标注口径，需要人工扩标"语义等价但文本不同"的相关 chunk，
   这一步还没做，见 [ADR 0007](docs/decisions/0007-corpus-scale-and-eval-resolution.md)。

## 生成：引用与拒答

两条约束由代码校验，不依赖提示词自觉：

| 约束 | 实现 | 实测 |
| --- | --- | --- |
| 每个论断带出处 | 答案正文内联 `[f-001#2]`；服务端用正则抽取，并核对是否真在本次上下文里 | 离线样本三个场景中，编造的引用会被剔除并单独统计 |
| 资料不足就拒答 | 输出固定拒答话术，并返回 `sufficient=false` | 问"线下实体店在北京哪个区"时正确拒答，且重排首位分数只有 **0.0002** |

同一条事实在检索结果里常有多种措辞（FAQ 问法不同、政策条款同义），因此上下文先折叠近重复
（阈值 0.55 由实测定：同一事实的两种措辞相似度 0.564，不同事实之间只有 0.288），提示词再要求
"重复事实合并、只标一条引用"。同一问题从三句重复收敛成一句，流式 token 事件从 88 降到 25。

## 接口

`uv run ecom-rag serve` 起服务（FastAPI，默认 `127.0.0.1:8000`，交互式文档在 `/docs`）：

- `POST /search`：纯检索，返回稠密 / 关键词 / 融合 / 重排四个阶段各自的候选，用于解释"为什么最后是这几条"
- `POST /query`：SSE 流式问答，事件按管线阶段分类型：`retrieved` → `fused` → `reranked` → `token` → `citations` → `done`
- `GET /stats`：控制台用的只读统计（语料规模、索引状态、黄金集、评估结果）；文件缺失时该字段为 `null` 且仍返回 200
- `GET /ui/*`：控制台静态托管（与接口同源，不需要 CORS）

前端因此不需要实现任何检索逻辑就能画出"两路召回 → 融合 → 重排"的过程。请求与响应细节见 [`docs/api.md`](docs/api.md)。

## 可视化控制台

`web/ecom-rag-console.html` 是单文件、零构建的控制台，两种打开方式：

```bash
# 方式一：直接双击文件（离线回放，不需要后端、不需要网络）
start web/ecom-rag-console.html          # Windows；macOS 用 open

# 方式二：起服务后同源访问（实时模式）
uv run ecom-rag serve
# 浏览器打开 http://127.0.0.1:8000/ui/ecom-rag-console.html?mode=live
```

界面覆盖：首屏空状态 → 两路召回（各自的候选与分数）→ RRF 融合 → 重排把谁提上来（跨列连线）→
逐字答案 → 引用徽章（点开可看原文片段）→ 资料不足时的拒答，另有评估看板标签页。

![界面演示：从空状态走到引用校验](data/shots/console-walkthrough.gif)

两处实现说明：

- **离线样本是真抓的**：`uv run ecom-rag capture-replay` 直接消费 `/query` 用的那个事件源函数（与线上同一处实现），
  事件流与浏览器实际收到的一致，然后内联进 HTML 的标记块之间。回放模式不能去 `fetch` 同目录 JSON——
  双击打开是 `file://` 协议，会被浏览器拦掉。样本覆盖三个场景：有答案、拒答、跨多处资料（一个答案由两处不同文档拼成）。
- **URL 参数即状态契约**：`?mode=replay|live`、`?scenario=answer|refusal|cross`、
  `?stage=retrieved|fused|reranked|answer|citations`、`?tokens=N`、`?tab=eval`。
  `scripts/capture_shots.py` 靠它把界面定格到任意阶段，不需要模拟点击。

页面把状态写在 `<body data-stage="…" data-mode="…">`，渲染完成后置 `window.__CONSOLE_READY__ = true`；
自动化等这两个信号，不用 `sleep`。

界面质量由脚本核查：`uv run python scripts/check_console.py` 检查 WCAG AA 对比度、640/1024/1440
三个宽度无横向溢出、各状态下该出现的元素、离线样本里没有幻觉引用、以及没有任何外部资源请求
（自包含）。当前 21 项断言全部通过；截图的一致性判据是像素差（固定 viewport、禁用动画、逐通道容差 ±2、
差异像素 ≤ 0.5%），实测关键页两次差异 0.0000%。

## 命令

| 命令 | 作用 |
| --- | --- |
| `ecom-rag health` | 检查 Qdrant / Infinity 与配置 |
| `ecom-rag build-corpus` | 用云 LLM 扩写语料（事实表为唯一数字来源）并结构感知切分 |
| `ecom-rag build-index` | 构建两条索引：稠密进 Qdrant、关键词落盘 bm25s |
| `ecom-rag search "…"` | 只看检索，打印两路 / 融合 / 重排的排名对比 |
| `ecom-rag ask "…"` | 提问，打印带引用的答案（资料不足则拒答） |
| `ecom-rag build-golden` | 构造黄金集（源 chunk 即标准答案 + 反向校验） |
| `ecom-rag evaluate` | 跑消融矩阵并把结果表写回本文件 |
| `ecom-rag capture-replay` | 抓取真实 SSE 样本 + 统计快照，注入控制台（供离线回放） |
| `ecom-rag serve` | 启动 HTTP 服务（含控制台 `/ui`） |

另有两个开发期脚本：

| 脚本 | 作用 |
| --- | --- |
| `python scripts/check_console.py` | 界面质量核查：对比度 / 响应式 / 结构断言 / 幻觉引用 / 自包含（21 项） |
| `python scripts/capture_shots.py` | 生成 README 用的截图与 GIF，并做像素差一致性校验 |

## 决策记录

实现过程中的取舍记录在 [`docs/decisions/`](docs/decisions/)，每条都带当时的证据与实测数字：

| 文档 | 内容 |
| --- | --- |
| [0001](docs/decisions/0001-hybrid-retrieval-own-rrf.md) | 自己编排两路检索与 RRF，而不用 Qdrant 服务端的融合/全文能力 |
| [0002](docs/decisions/0002-cpu-default-and-torch-engine.md) | 为什么默认 CPU 路径，以及为什么必须用 torch 引擎（optimum 会在 WSL 下把容器挤死） |
| [0003](docs/decisions/0003-golden-set-by-construction.md) | 黄金集用构造法 + 反向校验，不用 LLM 当裁判 |
| [0004](docs/decisions/0004-corpus-consistency-fact-table.md) | 合成语料如何靠事实表与「数值+单位」校验避免自相矛盾 |
| [0005](docs/decisions/0005-hybrid-did-not-win-honest-ablation.md) | 等权融合为何输给单路稠密，以及它的可复现解释 |
| [0006](docs/decisions/0006-console-single-file-artifact.md) | 控制台用零构建单文件、样本内联、截图用像素差而非 hash |
| [0007](docs/decisions/0007-corpus-scale-and-eval-resolution.md) | 语料扩容（扩商品而非 FAQ）与评估分辨率（表格降到两位小数） |
| [0008](docs/decisions/0008-unique-chunk-ids.md) | `doc_id` / `chunk_id` 撞号的定位与修复，含回归测试 |
| [0009](docs/decisions/0009-one-source-for-context-and-citations.md) | 生成上下文与引用校验改为同源；SSE 事件流收敛为单一来源 |

## 目录结构

```text
src/ecom_rag/
├── config.py      # 配置与检索参数（同时是消融旋钮）
├── infinity.py    # Infinity 客户端：/embeddings 与 /rerank
├── replay.py      # 离线样本捕获与注入（供控制台回放）
├── text_utils.py  # 字符二元组相似度（近重复判定）
├── corpus/        # 事实表、种子语料、LLM 扩写、结构感知切分、一致性校验
├── index/         # 两条索引：dense(Qdrant) / sparse(bm25s + jieba)
├── retrieve/      # types / dense / sparse / fusion(RRF) / rerank / pipeline
├── generate/      # 带引用与拒答的生成；流式版本供 SSE 使用
├── evaluate/      # 黄金集构造、指标、消融矩阵、README 表生成
├── api/           # FastAPI + SSE + /stats + 控制台静态托管
└── cli.py         # 上表里的各条命令

web/               # 单文件控制台（零构建、离线可开、可切 live）
scripts/           # 界面质量核查、截图与 GIF 生成
data/replay/       # 抓取下来的真实 SSE 样本与统计快照
data/shots/        # README 用的截图与 GIF
```

## 局限与边界

- 语料是合成的电商知识库（商品 100 / FAQ 60 组 / 政策 4 份，共 164 篇 / 434 个 chunk / 约 41K 字符），
  评估数字只在同一语料内可比；22 条事实平均被重复提到十余次，语料的"有效知识量"远小于 chunk 数
  （见 [ADR 0007](docs/decisions/0007-corpus-scale-and-eval-resolution.md)）
- 评估口径保守：一道题的相关集合 = 构造源 + 与之文本近重复的 chunk。同一事实若在别处以完全不同的措辞出现，
  不会被计入相关集合，因此指标偏低而不是偏高
- 不覆盖多跳问题（需要跨两个 chunk 才能回答的问题无法用构造法自动标注）
- 不做多轮对话、不做查询分解、不做 SQL / 结构化查询
- 默认 CPU 路径以速度换"clone 后能直接复现"，GPU 路径用于本地迭代
- 提交历史集中在一天之内（一次连续实现），它反映的是过程顺序，不是真实的开发周期

## 许可

[MIT](LICENSE) © 2026 RainCongeals
