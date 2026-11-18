# Agentic RAG Knowledge Base

基于 **Agentic RAG** 的企业级智能知识库：文档解析 → 标题层级父子分块 → Dense + Sparse + BM25 混合检索 → Reranker 重排 → LangGraph 路由 Agent（意图识别 / 子问题拆解 / 迭代纠错 / HyDE）→ SSE 流式回答。

## 技术栈

LangChain · LangGraph · FastAPI · Milvus · BGE-M3 · BGE-Reranker-v2-m3 · MinerU · Redis · SQLite · Streamlit · Docker

## 架构

```
                        ┌──────────────── 入库流水线 ────────────────┐
 PDF / MD / TXT ─upload─►  MinerU(版式/表格/OCR) → Markdown            │
 (FastAPI, 异步处理)     │  VLM 图片描述(可选) → 标题层级父子分块        │
                        │  BGE-M3 (dense+sparse) → Milvus + SQLite    │
                        └────────────────────────────────────────────┘

 问题 ─► LangGraph Agent
          analyze   意图识别 + 指代消解 + 子问题拆解
            ├─ chitchat ─► 直接回答
            └─ knowledge
          expand    Query 改写 + 多查询扩展 + HyDE
          retrieve  Milvus 稠密+稀疏混合检索 ┐
                    BM25 (jieba)            ├─► RRF 融合 → 子块映射回父块
          rerank    BGE-Reranker 精排、父块去重
          grade     重排分数快速通道 / LLM 裁判 ──不足──► refine(改写查询) ─┐
            │                                                          │
            └─足够/达到重试上限─► build ◄──────────────────────────────┘
          generate  带 [n] 引用的 SSE 流式回答
```

| 模块 | 位置 |
|---|---|
| PDF 解析 (MinerU / pymupdf4llm 回退) | `backend/app/ingestion/parser.py` |
| VLM 图片描述 | `backend/app/ingestion/captions.py` |
| 标题层级 + 表格保护 + 父子分块 | `backend/app/ingestion/chunker.py` |
| BGE-M3 稠密+稀疏向量 + Redis Embedding 缓存 | `backend/app/retrieval/embedder.py` |
| Milvus 混合检索 (HNSW + SPARSE_INVERTED_INDEX + RRF) | `backend/app/retrieval/milvus_store.py` |
| BM25 / RRF 融合 / 多路召回 | `bm25.py` / `fusion.py` / `retriever.py` |
| BGE-Reranker 重排 | `backend/app/retrieval/reranker.py` |
| LangGraph Agent (路由/拆解/HyDE/纠错) | `backend/app/agent/graph.py` |
| SSE 流式 + 热点 Query 缓存 + 会话历史 | `backend/app/agent/service.py` |
| FastAPI 接口 | `backend/app/main.py` |
| Streamlit 前端 | `frontend/app.py` |
| 检索评测 (Hit@K / MRR / Recall@K) | `eval/run.py` |

## 快速开始 (Docker)

```bash
cp .env.example .env        # 填入 LLM_API_KEY 等
docker compose up -d --build
```

- 前端: http://localhost:8501
- 后端 API 文档: http://localhost:8000/docs

首次启动后端会下载 BGE-M3 与 BGE-Reranker 模型（数 GB），请耐心等待；国内网络可在 `.env` 中加 `HF_ENDPOINT=https://hf-mirror.com`。纯 CPU 可运行但较慢，有 GPU 建议使用带 CUDA 的 PyTorch 环境。

### 关于 MinerU

后端默认通过 `mineru` 命令行解析 PDF（`mineru -p <pdf> -o <outdir>`）。两种用法：

1. 构建镜像时安装：`.env` 里设 `INSTALL_MINERU=true`，再 `docker compose build backend`（镜像较大）；
2. 不安装则自动回退到 `pymupdf4llm`（能处理文字型 PDF 与简单表格，**不支持扫描件 OCR**）。

MinerU 的版本、安装方式和输出目录会变化，请以其官方仓库（opendatalab/MinerU）的 README 为准；本项目递归查找输出的 `.md`，不依赖固定目录名。

## 本地开发

```bash
# 依赖服务
docker compose up -d etcd minio milvus redis

# 后端
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp ../.env.example .env
uvicorn app.main:app --reload --port 8000

# 前端
cd ../frontend && pip install -r requirements.txt && streamlit run app.py

# 单元测试 (不需要任何外部服务)
cd ../backend && pytest -q
```

## API

| 方法 | 路径 | 说明 |
|---|---|---|
| POST | `/api/v1/documents` | 上传文档 (`file`, `namespace`)，立即返回，后台异步处理 |
| GET | `/api/v1/documents?namespace=` | 文档列表与处理状态 |
| DELETE | `/api/v1/documents/{doc_id}` | 删除文档 (同步清理向量/BM25/缓存) |
| POST | `/api/v1/query` | 非流式问答 |
| POST | `/api/v1/query/stream` | **SSE 流式问答** |
| POST | `/api/v1/retrieve` | 只检索不生成 (评测用) |

```bash
curl -N -X POST http://localhost:8000/api/v1/query/stream \
  -H "Content-Type: application/json" \
  -d '{"query": "出差住宿费的报销标准是什么？", "namespace": "default", "session_id": "demo"}'
```

SSE 事件：`status`（Agent 每一步进度）→ `token`（增量文本）→ `sources`（引用）→ `done`（`first_token_ms` / `latency_ms` / `cached`）。

设置了 `API_KEY` 后，请求需带 `X-API-Key` 请求头。`namespace` 之间的知识相互隔离。

## 评测

```bash
cp eval/dataset.example.jsonl eval/dataset.jsonl   # 按你的文档编写问题与期望命中的关键片段
python eval/run.py --dataset eval/dataset.jsonl --namespace default --k 5
```

输出 Hit Rate@K、MRR、Recall@K。**请用你自己的文档和数据集跑出真实结果**，不要直接沿用他人的数字。

## 主要配置项 (`backend/app/config.py`，均可用环境变量覆盖)

| 变量 | 默认 | 说明 |
|---|---|---|
| `RECALL_TOP_K` / `RERANK_TOP_K` | 20 / 5 | 召回数 / 重排后保留数 |
| `RRF_K` | 60 | RRF 平滑常数 |
| `RERANK_FAST_THRESHOLD` | 0.5 | 重排最高分达标则跳过 LLM 评估 |
| `MAX_RETRIES` | 2 | 召回不足时的纠错重试上限 |
| `MULTI_QUERY_N` / `ENABLE_HYDE` | 2 / true | 多查询条数 / 是否启用 HyDE |
| `PARENT_MAX_CHARS` / `CHILD_MAX_CHARS` | 1500 / 400 | 父块 / 子块大小 (字符) |
| `QUERY_CACHE_TTL` | 3600 | 热点问答缓存 TTL (秒) |

## 设计说明

- **父子分块**：小块检索保证精度，命中后返回所在父块给 LLM，兼顾上下文完整性；表格作为整体，超长表格按行拆分并重复表头。
- **缓存**：Embedding 缓存按文本哈希；问答缓存按「命名空间版本号 + 问题哈希」，文档变更后版本号自增，旧缓存自动失效；仅对无历史上下文的独立问题生效。Redis 不可用时自动降级。
- **纠错重试**：重排最高分低于阈值时由 LLM 判断召回是否足够，不足则换角度改写查询重新检索，最多 `MAX_RETRIES` 次。
- **鲁棒性**：所有 LLM 的 JSON 输出解析失败时回退到默认值，Agent 流程不会中断。

## 致谢

整体架构思路参考了开源项目 [hiveden/toolref](https://github.com/hiveden/toolref)（MIT）与 [Progress-infinitely/DocNest](https://github.com/Progress-infinitely/DocNest) 的公开说明；本仓库代码为独立实现。

## License

MIT
