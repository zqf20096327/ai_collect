# 知渊 · 企业知识库问答

[![CI](https://github.com/wangyuchao-dev/zhiyuan/actions/workflows/ci.yml/badge.svg)](https://github.com/wangyuchao-dev/zhiyuan/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.12-blue)
![Tests](https://img.shields.io/badge/tests-126-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-75%25-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

把几十页制度 PDF 变成「问一句话、答案带出处」的知识库。
核心不是把文档塞进向量库，而是**把检索做准**：意图先分流、双路召回、按名次融合、精排压噪、阈值兜底，每一步的收益都用同一套 34 题评测集量化过。

```
文档上传 → 切分 → 向量入库（cosine）
    ↓
提问 → 意图识别（规则快判优先）→ 查询改写（按需）
    ↓
双路召回：稠密向量 + BM25  →  RRF 按名次融合（0.7 / 0.3）
    ↓
精排（qwen3-rerank）→ 相关性阈值 0.3 → 拼上下文
    ↓
生成答案（标注出处条款）→ SSE 流式返回
```

## 效果

| 指标 | 纯向量基线 | 混合检索 | 说明 |
|---|---|---|---|
| 34 题命中率 | 28/34（82.4%） | **31/34（91.2%）** | 判定口径：召回首条命中期望关键词 |
| 编号密集型 | 5/8 | **8/8** | 纯向量召不回 `E1017` 这类纯符号，BM25 精确命中 |
| 语义类 | 11/13（85%） | 11/13（85%） | 持平——混合检索不是万灵药 |
| 典型问答耗时 | 7 s | **2.3 s** | 规则快判意图省一次模型调用 + 无指代词时跳过改写 |

单元测试 **126 个**，`pytest` **不联网、不花钱、不依赖数据库**，约 6 秒跑完，覆盖率 75%。

## 目录

```
config/       setting.py（全部可调参数 + 环境分层）· prompts.py（6 块提示词）· version.py（版本单一来源）
indexing/     clean（清洗与质量门槛）· hash_calculate（MD5 指纹）· upload_split（PDF 切分）
              parent_child（父子分块，已实现未启用，原因见文件头）· vector_storage · indexing_pipeline
querying/     query_rewrite · vector_retriever · bm25_retriever · rrf · hybrid_retriever
              retrank（精排）· answer（生成）· pipeline（串联）· eval_retrieval / eval_single_doc（评测）
agent/        intent（意图）· chat_history_manager · facts_manager · summary_manager
              memory（中枢）· persistence（SQLite）· orchestrator（主流程）
              plan（显式计划 + 有界重试）· memory_policy（四类记忆与严格检索）
core/         errors（五类错误 + 重试策略）· context_budget（上下文分级预算）
              cache（Redis 优先，自动降级）· postcheck（后置校验：抓编造）· logging（结构化日志）
tools/        registry（function calling 注册表）· mcp_adapter（MCP 描述互转）
skills/       registry（懒加载）· fault-code-lookup/SKILL.md（示例技能）
eval/         七维评测框架（见下方「评测」）
api/          main（装配）· deps（懒加载）· middleware（请求 ID）· schemas
              routes/ops（health / ready / version）· routes/chat · routes/documents
tests/        test_core · test_wiring · test_agent_infra · test_data_pipeline · test_logging（共 126 例）
samples/      样例语料（6 份 PDF，见 samples/README.md）：常规文档 / 错误码手册 / 带页眉页脚 / 扫描件 / 长文档
web/          index.html（Vue 3 单页）
scripts/      check.ps1（与 CI 同款）· lint.ps1 · test.ps1 · make_samples.py（重新生成样例）
.github/      workflows/ci.yml · workflows/release.yml · PR 与 Issue 模板
```

## 快速开始

```powershell
# 1. 环境
uv venv --python 3.12 .venv
uv pip install --python .venv\Scripts\python.exe -r requirements-dev.txt

# 2. 配置密钥（.env 已被 .gitignore 忽略）
copy .env.example .env      # 然后填入 DASHSCOPE_API_KEY

# 3. 起服务：双击 start.bat，或
.\start.bat                 # http://127.0.0.1:8000（前端与接口同端口）
```

也可以容器起（自带健康检查与数据卷）：

```bash
docker compose up -d --build
```

传一份 PDF 到 `uploads/`（或走 `POST /api/documents` 上传），系统会切分、向量化、写入 `indexing/chroma_db/`。
首次没有向量库也能起服务：`/api/health` 只看进程活着，`/api/ready` 会逐项告诉你缺什么（密钥 / 向量库 / 运行目录）。

> 仓库自带 6 份样例语料在 `samples/`（见 `samples/README.md`），上传其中任意一份即可复现。
> 向量库不随仓库提供（体积大、可重建），首次入库会自动生成。

## 工程化

一个人开发也按团队流程走 —— 不是流程本身重要，而是**任何一次上线都能回答「这个版本在 test 上验过吗」**。

### 分支模型

```
feature/xxx ──┐
              ├─> develop ──> test ──> main
hotfix/xxx ───┘         (CI)     (CI)    (CI + 打 tag 出镜像)
```

| 分支 | 用途 | 规则 |
|---|---|---|
| `main` | 生产，随时可发版 | 只接受来自 `test` 的 PR，禁止直推 |
| `test` | 验收环境 | 只接受来自 `develop` 的 PR |
| `develop` | 日常开发主线 | 功能分支从这里切、合回这里 |
| `feature/*` / `hotfix/*` | 单功能 / 线上急修 | hotfix 修完要同时回合并 `main` 与 `develop` |

提交信息用 Conventional Commits（`feat` / `fix` / `refactor` / `docs` / `ci` …），正文写**为什么**。
细节见 [CONTRIBUTING.md](CONTRIBUTING.md)。

### CI 与质量门槛

`.github/workflows/ci.yml` 在 PR 与三个主分支上跑四个任务：

| 任务 | 内容 | 不过会怎样 |
|---|---|---|
| `quality` | `ruff check` + `ruff format --check` | 挡住不合规的代码进主干 |
| `test` | `pytest --cov`，**覆盖率门槛 65%**（当前 73%） | 挡住「新加一堆没测的代码」 |
| `docker` | 镜像可构建 | 挡住「本地能跑、镜像起不来」 |

依赖 `quality` 通过才构建镜像 —— 镜像构建慢，没必要给不合规的代码排队。

测试**全部离线**：不调模型、不连数据库、不需要 API Key。哪天某个测试开始依赖外部服务，CI 上会立刻暴露。

### 本地与 CI 同款

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\check.ps1
```

三条命令：`ruff check` → `ruff format --check` → `pytest --cov`。提交前跑一次，就不会出现「推上去才发现红」。
装了 `pre-commit` 之后，commit 时也会自动跑 ruff 与 `detect-private-key`（拦 API Key、私钥）。

### 环境分层

`APP_ENV` 取 `development` / `test` / `production`：

| 环境 | 日志 | 用途 |
|---|---|---|
| `development` | 可读文本，带 request_id 前 8 位 | 本地调试 |
| `test` | 同开发 | 验收环境 |
| `production` | **JSON 一行一条**，带 request_id | 接 Loki / ELK 采集 |

敏感值只从环境变量读，代码里没有任何默认 Key。`QaConfig.load()` 支持 `CHAT_MODEL`、`MIN_SCORE` 等覆盖，方便按环境切便宜模型或临时调阈值。

### 运维端点

| 端点 | 回答什么问题 | 依赖挂了会怎样 |
|---|---|---|
| `/api/health` | 进程还活着吗 | **仍返回 200** —— 否则编排系统会反复重启一个没坏的进程 |
| `/api/ready` | 现在能接流量吗 | 返回 503，让负载均衡先把流量摘走 |
| `/api/version` | 跑的是哪个版本 | — |

`/api/ready` 只检查必要条件（Key 是否配、向量库目录是否在），**不真的调一次模型** —— 它会被每几秒打一次，调模型既费钱又会被限流。

## 主链路：一次问答经过哪些环节

每条线都是一个可单测的模块，不是散在路由函数里的 if-else：

| 环节 | 做什么 | 失败时 |
|---|---|---|
| 清洗（入库时） | 页眉页脚按整篇识别、页码/目录/全角字符逐页清 | 清洗后不足 50 字或丢失超 70% → **拒收**（400），不灌脏数据 |
| 切分 | 在句号/问号/分号后切，不腰斩句子 | — |
| 意图 | 规则快判（寒暄/投诉/文档特征词）→ 判不出才调模型 | 模型超时 → 按「需要查文档」处理 |
| 改写 | 有指代词才改写，否则跳过（省一次调用） | 改写失败 → 用原问题检索 |
| 召回 | 向量 + BM25 **并行**，RRF 按名次融合（0.7/0.3） | 单路异常 → 只用另一路，记 `last_degraded` |
| 精排 | qwen3-rerank + 阈值 0.45 | 接口抖动 → 退化为召回顺序，不过阈值 |
| 阈值降级 | 严格阈值下为空、但最高分 ≥0.35 → 放宽一次只取 top-1 | 最高分不够格 → 保持「未找到」，绝不硬答 |
| 预算 | 超总预算的证据整条丢弃，编号重排 | — |
| 生成 | 只依据上下文，标注 `[N]` 出处；命中技能时按其格式作答 | — |
| 校验 | 错误码/带单位数字/日期必须在证据里；引用越界只移除编号 | 不通过 → 换保守话术（不自动改数字） |

### 实测（单文档，本机）

| 指标 | 数值 | 说明 |
|---|---|---|
| 检索段耗时（冷） | 308–707 ms | 含向量召回 + BM25 + 精排；首次含 BM25 建索引 |
| 检索段耗时（命中缓存） | < 2 ms | 进程内缓存；换 Redis 约一次网络往返 |
| 完整问答（冷 → 热） | 2958 ms → 1689 ms | 缓存省掉检索，生成仍要调模型 |
| 技能命中 | 468 字注入 | 「E1017 是什么错误」命中 `fault-code-lookup`，未命中的问题注入 0 字 |
| 上下文预算 | 2600 token | 实测单次用 614–693 token，4 条证据全部装下、丢弃 0 条 |
| 校验拦截 | 见测试 | 「保留 99 年」拦下；「三年」与「3 年」都放行（归一化后一致） |
| 阈值调优 | 0.3 → 0.45 | 0.3 下 20 道题 **0 道被过滤**（等于没过滤）；0.45 下 5 道为空，靠降级救回 |

## 四个我认为值得说的设计

### 1. 意图先用规则快判，判不了才调模型

`agent/intent.py` 里有三类意图：文档问答、闲聊、投诉。规则能判的直接走对应提示词（省一次模型调用，约 3 秒）；
判不了才让模型分类。

**为什么一个意图一块提示词**：投诉那条根本不需要查文档，走 RAG 反而会拿制度条款去回应情绪；文档问答必须严格要求「只依据材料回答」。

### 2. 三层记忆，各管一段

| 层 | 存什么 | 为什么单独一层 |
|---|---|---|
| 历史 | 最近若干轮原文 | 保证指代消解（「那它呢」能接上） |
| 事实 | 用户说过的稳定信息（部门、岗位） | 反复问同一件事不该反复说 |
| 摘要 | 更早对话的压缩摘要 | 长对话不爆上下文，又不完全丢信息 |

三张表落 SQLite，重启不丢；换 Redis 只改 `agent/persistence.py`。

### 3. 阈值 0.3 是「精排分」的阈值，不是向量相似度

建库时强制 **cosine 距离** —— 只有这样 0.3 才有明确含义（换 L2 之后同一个数值含义完全不同）。
精排分数低于 0.3 的片段直接丢，宁可答「材料里没有」，也不拿不相关段落凑上下文。

### 4. 多文档：一份文档一个集合，跨文档用 RRF 而不是分数相加

不同集合的相似度分数**不可比**（各自的分布不同），所以跨文档只能按**名次**融合 —— 这正是 RRF 的适用场景。

## 评测怎么做

`querying/eval_retrieval.py` 读 34 题（21 道精确编号类 + 13 道语义类），覆盖 4 份文档 42 个片段，
判定「召回首条是否包含期望关键词」，输出按题型分组的命中率。

> 只看总数会骗人：编号类从 5/8 到 8/8 是结构性改善，语义类持平说明混合检索解决的不是语义泛化问题。

## 评测（七维）

不报单一「准确率」，而是拆七维：**结果 / 检索 / 证据 / 过程 / 稳定性 / 成本 / 安全**。
用例 39 条（静态 20 / 动态 8 / 安全 6 / 故障 5），可离线跑、不花钱。

```bash
python eval/runner.py --suite all --runs 5 --adapter mock --variant hybrid-v1   # 验证链路
python eval/runner.py --suite static --adapter live --doc <file_hash>           # 真跑
python eval/report.py eval/results/a.json eval/results/b.json > report.md       # 版本对比
```

- 设计口径：[docs/eval-framework.md](docs/eval-framework.md)（七维怎么定义、静态/动态为什么分开、TSR 为什么只取首次）
- 跑法与用例格式：[eval/README.md](eval/README.md)
- 样例报告：[eval/results/sample-report.md](eval/results/sample-report.md) —— **mock 生成，只验证链路，数字不可引用**


## 已知边界

- 34 题样本量小，看趋势不看绝对值；扩文档后要重跑
- 单机 SQLite，没有并发压测；多 worker 下会话绑定仍在进程内存里（代码注释里写明了）
- BM25 用 bi-gram 切词（不依赖 jieba），中文长词召回略弱于分词方案
- 精排依赖 DashScope，离线环境会退化成「只用 RRF 排序」

## 配套文档

| 文档 | 内容 |
|---|---|
| [docs/agent-design.md](docs/agent-design.md) | 十个绕不开的设计问题：ReAct/Plan、Agent/Workflow、工具失败、多 Agent、MCP 与 Function Calling、记忆、召回、MCP/SKILL、评估、上下文 |
| [docs/eval-framework.md](docs/eval-framework.md) | 七维评测的口径与局限，以及「表面对」为什么会骗人 |
| [docs/data-and-storage.md](docs/data-and-storage.md) | 四个判断：要不要加 Redis、要不要换 Milvus、要不要做后置覆盖、要不要单独清洗（含 68 万字压测数据） |
| [eval/README.md](eval/README.md) | 评测框架怎么跑、用例怎么写 |
