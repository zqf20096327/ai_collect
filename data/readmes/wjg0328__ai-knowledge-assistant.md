# 知页 · 个人知识库 AI 助手

一个适合逐步手敲的 Python AI 应用案例。默认无需密钥即可运行离线检索；配置模型服务后支持流式生成式问答。

## 已实现

- 浏览器聊天界面、历史对话恢复、对话导出。
- UTF-8 TXT / Markdown、文字型 PDF 导入；按内容去重、删除文档。
- 文本分块、字符级 TF-IDF 检索；可选使用兼容 Embeddings API 的服务与 Chroma 做语义向量检索。
- 离线模式展示原文摘录，真实模型模式展示流式生成内容。
- 参考片段展开、文档名和文本块位置、耗时及服务商返回的 Token 用量。
- SQLite 本地持久化、无检索证据时跳过模型、网络和认证错误提示。
- 不需要密钥的单元测试与 Streamlit 应用测试。

## 快速启动：Windows PowerShell

需要 Python 3.11 或更高版本及 [uv](https://docs.astral.sh/uv/getting-started/installation/)。已在 Python 3.12 下验证。

```powershell
uv sync --group dev
uv run python -m streamlit run app.py
```

`uv sync --group dev` 会按 `uv.lock` 创建 `.venv` 并安装运行及开发依赖；`uv run` 会在项目环境中执行命令，无需手动激活虚拟环境。

打开终端显示的地址，默认是 http://127.0.0.1:8501 。点击侧栏“载入示例文档”，尝试提问：

1. Python 虚拟环境如何创建？
2. 什么是 RAG？
3. 本项目如何进行文档分块？
4. 火星大气有什么成分？（预期无足够依据）

离线模式只是检索原文，不会调用大模型，不产生模型费用。它不是完整的生成式问答。

## 启用真实模型

```powershell
Copy-Item .env.example .env
```

在本机编辑 `.env`，不要把密钥发给聊天助手或提交到 Git：

```dotenv
AI_MODE=live
CHAT_API_KEY=填写服务商提供的 API Key
CHAT_BASE_URL=填写服务商提供的兼容接口地址
CHAT_MODEL=填写服务商提供的模型名称
CHAT_MAX_TOKENS_PARAMETER=max_tokens
CHAT_INCLUDE_USAGE=false
```

重启应用后选择“真实模型”。聊天调用使用 OpenAI SDK 的 Chat Completions 接口，服务商需提供兼容的流式接口；模型名称和 Base URL 由使用者按服务商文档填写。Base URL 留空时使用 SDK 默认地址。
如果服务使用 `max_completion_tokens`，将 `CHAT_MAX_TOKENS_PARAMETER` 改为该值；只有服务支持流式用量返回时才将 `CHAT_INCLUDE_USAGE` 设为 `true`。不同兼容服务仍可能存在参数差异，遇到错误时应按服务商文档调整并增加 Mock 测试。
旧配置名 `OPENAI_API_KEY`、`OPENAI_BASE_URL` 和 `OPENAI_MODEL` 仍可作为回退读取；新配置请使用 `CHAT_*` 名称。环境变量优先于 `.env`。更改 `.env` 后请重启服务，避免旧值继续生效。

**隐私与费用：真实模型模式会将问题、最近最多 6 条历史消息及本轮命中的文档片段发送到配置的模型服务。**
不要导入敏感资料。请求可能产生费用；Token 显示值为服务商报告值，0 也可能表示服务商未返回用量，并非费用承诺。

## 启用 Embedding 语义检索

Embedding 和聊天模型使用独立配置和 Key。默认检索仍为 TF-IDF；只在需要体验语义检索时安装可选依赖：

```powershell
uv sync --extra embedding --group dev
```

在本机 `.env` 中填写所选服务商提供的兼容 Embeddings API 配置：

```dotenv
RETRIEVAL_MODE=embedding
EMBEDDING_API_KEY=填写服务商提供的 API Key
EMBEDDING_BASE_URL=填写服务商提供的兼容接口地址
EMBEDDING_MODEL=填写服务商提供的 Embedding 模型名称
```

重启后在侧栏选择“语义向量（Embedding）”。第一次提问会将 SQLite 中尚未索引的文本块批量发送到已配置的服务生成向量并保存到本地 `data/chroma/`；后续查询只需嵌入问题。删除文档后，陈旧向量会在下次 Embedding 查询同步时清除。SQLite 是原始资料的主存储，Chroma 索引可从 SQLite 重建。

可以保持 `AI_MODE=demo` 来比较检索结果而不调用聊天模型。注意这不是完全离线：文档块和问题会发送到配置的 Embedding 服务。Embedding 模型可用性、额度和计费以服务商当前说明为准。检索分数是 Chroma cosine 相似度换算值，和 TF-IDF 的分数不可直接比较；两种模式使用独立阈值。

## 目录与职责

```text
ai-knowledge-assistant/
  app.py                         浏览器界面与交互
  knowledge_assistant/
    config.py                    环境变量和路径
    documents.py                 解析文档、切分文本
    store.py                     SQLite 存储
    retrieval.py                 TF-IDF 检索
    embeddings.py                兼容 Embeddings API 与 Chroma 向量索引
    llm.py                       提示词、模型流式调用
    service.py                   组织完整问答流程
  sample_docs/                   两份中文示例资料
  tests/                         核心、模型与界面测试
  docs/LEARN.md                  9 节手敲课程
  docs/ACCEPTANCE.md             手动验收与评估模板
  .env.example                   配置模板，不含密钥
  .streamlit/config.toml         界面及本机服务配置
  pyproject.toml                 项目元数据与依赖
  uv.lock                        锁定依赖解析结果
  data/knowledge.db              首次运行自动生成
  data/chroma/                   使用 Embedding 后生成的本地向量索引
```

## 学习入口

按 [手敲教程](docs/LEARN.md) 从第 1 节开始。完整项目是参考答案，不要先尝试一次理解全部文件。
建议在另一个学习目录里逐节复现，保留这份已测试项目作为对照；遇到问题时提供命令、报错和相关函数，不提供密钥。

## 自动检查

在项目目录执行：

```powershell
uv run --group dev pytest -q
uv run --group dev ruff check .
```

要运行 Chroma 集成测试，先执行 `uv sync --extra embedding --group dev`，再使用同样的 `uv run --group dev pytest -q` 命令。

测试在临时目录使用独立数据库，不会清除你的个人资料，不会访问付费模型 API。
依赖范围声明在 `pyproject.toml`，精确解析结果由 `uv.lock` 固定。修改依赖后运行 `uv lock` 更新锁文件，再运行 `uv sync --group dev` 同步环境；提交代码时应一并保留 `uv.lock`。

## 设计取舍与边界

- 这是本机单用户教学项目，默认仅监听 `127.0.0.1`，无登录、权限隔离或多会话管理。不要直接开放到公网。
- 本机所有浏览器共享同一数据库和一段对话历史，“新对话”会清除当前保存的全部聊天消息，不删除文档。
- 文档、文本块、对话均以明文保存在 `data/knowledge.db`。删除文档会删除其检索块，但不会删除已保存聊天中的引用快照；“新对话”才能移除这些聊天记录。
- 默认使用 scikit-learn TF-IDF 作为词法检索基线；可选 dense Embedding 改善语义召回，但不保证答案正确。
- Embedding 向量按模型名隔离保存在 Chroma；切换 Embedding 模型会重新建立该模型的向量集合。
- 每次查询重新构建 TF-IDF，适合几十份小文档学习；大规模应缓存索引或使用专用检索系统。
- 简单追问使用最近历史辅助检索，不包含完整的独立问题重写。复杂指代可能检索失败。
- 没检索到证据一定不调用模型；检索到文本不等于答案可靠。提示词无法保证消除幻觉或抵御所有提示词注入。
- 仅支持文字型 PDF，不支持 OCR、表格结构恢复、精确 PDF 页码引用；当前引用定位到文本块。
- 单文件限制 10 MB、PDF 最多 200 页、提取文本最多 50 万字符；复杂 PDF 解析仍可能耗时，不适合处理不可信的大量文件。
- 未包含 Agent、工具调用、微调或生产部署；这些应作为学懂本项目后的独立扩展。

## 常见问题

- **没有命中资料**：先尝试文档中的关键词，再检查最低相关度。不要为了有答案无限降低阈值。
- **PDF 没有文字**：可能是扫描件，请先使用可信 OCR 工具处理。
- **认证失败**：在本机检查 API Key、模型权限和 Base URL。不要粘贴密钥到聊天中。
- **请求超时**：检查网络和服务地址；默认超时 45 秒，最多重试 1 次，总耗时可能更长。
- **8501 被占用**：启动时增加 `--server.port 8502`。
- **希望完全重置**：先停止应用，再自行删除 `data/knowledge.db`；这会丢失全部文档和历史。