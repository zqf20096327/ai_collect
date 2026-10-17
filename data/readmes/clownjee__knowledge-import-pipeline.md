# Knowledge Import Pipeline

面向义务教育教材的 AI 知识抽取与知识图谱构建平台：从 PDF 中提取教材、目录和知识点，生成向量表示与跨教材前置依赖关系，并通过交互式 Web 界面和 MCP 工具提供查询能力。

> [!IMPORTANT]
> 本网站为非官方教育知识图谱项目，与各教育出版社不存在隶属、合作、授权、赞助或背书关系。出版社相关名称仅用于客观说明知识点所参考的教材版本。网站不提供教材 PDF、页面图片、课文、习题、OCR 全文或其他可替代教材阅读的内容。公开展示的知识点摘要和依赖关系由本项目独立整理生成。

## 功能演示

搜索并选中知识点后，可查看其直接前置、直接后续及知识图谱中的上下游路径。

![知识点前置与后续关联演示](docs/assets/knowledge-graph-demo.gif)

在线示例：[https://clownjee.top:1443](https://clownjee.top:1443)

该地址仅用于浏览和查询演示，不提供 PDF 上传、关系构建、科目维护或其他数据修改权限。

## 功能特性

- **教材导入流水线**：上传 PDF 后，异步完成教材信息识别、目录解析和知识点抽取，并记录每一步的任务状态。
- **知识依赖构建**：使用 Embedding 向量召回候选知识点，再由大语言模型判断直接前置关系、置信度及原因。
- **知识宇宙可视化**：按学科、年级、教材和置信度浏览知识点网络，支持搜索、缩放、旋转及上下游路径聚焦。
- **多教材关系管理**：配置教材之间的先后关系，构建同学科跨年级、跨学期的知识依赖。
- **MCP 查询服务**：为 AI 客户端提供只读工具，可查询学科、教材、课时、知识点及其直接前置与后续关系。
- **模型服务可配置**：LLM、视觉模型和 Embedding 模型均通过环境变量接入 OpenAI-compatible API。

## 工作流程

```text
PDF 上传
  └─ 教材信息解析
      └─ 目录识别与页码定位
          └─ 课时知识点抽取
              └─ Embedding 向量化
                  └─ 候选知识点召回
                      └─ LLM 关系判断
                          └─ 知识图谱展示 / MCP 查询
```

流水线只保存结构化教材元数据、独立生成的知识点摘要及依赖关系。原始 PDF 用于本地处理，不通过公开浏览界面提供。

## 技术栈

| 模块 | 技术 |
| --- | --- |
| 前端 | Vue 3、TypeScript、Vite、原生 Canvas |
| 后端 | Java 21、Spring Boot 3、MyBatis-Plus、Spring State Machine |
| AI | LangChain4j、OpenAI-compatible API、Freemarker Prompt |
| 数据 | PostgreSQL 18、pgvector、Redis |
| 协议 | REST API、Model Context Protocol (MCP) |
| 部署 | Docker Compose、Nginx、TLS |

## 快速开始

### 前置条件

- Docker 与 Docker Compose
- 可用的 OpenAI-compatible LLM、视觉模型和 Embedding 模型服务
- 可用的 OpenDataLoader PDF 服务
- 一个域名或本地域名，以及对应的 TLS 证书和私钥

当前数据库向量字段为 `VECTOR(1024)`，请确保所配置的 Embedding 模型输出 **1024 维向量**。如使用其他维度，需要同步修改数据库表结构。

### 1. 配置环境变量

```bash
cp .env.example .env
```

至少需要修改以下配置：

- `POSTGRES_PASSWORD`、`REDIS_PASSWORD`
- `NGINX_SERVER_NAME`、`TLS_CERT_PATH`、`TLS_KEY_PATH`
- `MCP_AUTH_TOKENS`：至少 32 个字符的随机令牌
- `MODEL_LLM_*`、`MODEL_LVM_*`、`MODEL_EMBEDDING_*`
- `OPEN_DATA_LOADER_URL`

不要提交 `.env`、TLS 私钥、模型 API Key 或导入的教材文件。仓库已通过 `.gitignore` 排除这些内容。

### 2. 启动服务

```bash
docker compose up -d --build
```

首次启动时，PostgreSQL 会自动执行 `db_schema/knowledge_import_tables.sql` 创建表结构。服务启动后访问：

```text
https://<NGINX_SERVER_NAME>:<HTTPS_PORT>
```

查看运行状态或日志：

```bash
docker compose ps
docker compose logs -f knowledge
```

停止服务：

```bash
docker compose down
```

如需同时删除 PostgreSQL、Redis 和上传文件的 Docker volumes，请明确确认数据不再需要后再执行：

```bash
docker compose down -v
```

## 本地开发

### 后端

要求 Java 21 和 Maven 3.9+。先启动 PostgreSQL、Redis 和 OpenDataLoader，并让环境变量指向对应服务，然后运行：

```bash
cd knowledge
mvn spring-boot:run
```

执行后端测试：

```bash
cd knowledge
mvn test
```

### 前端

要求 Node.js 22+：

```bash
cd frontend
npm ci
npm run dev
```

默认情况下，Vite 开发服务器会将 `/api` 请求代理到 `http://localhost:8080`。也可以不启动后端，直接访问带演示参数的页面：

```text
http://localhost:5173/?demo=1
```

执行生产构建：

```bash
cd frontend
npm run build
```

## MCP 接入

服务启用后，MCP 端点为：

```text
https://<NGINX_SERVER_NAME>:<HTTPS_PORT>/mcp
```

请求需携带 Bearer Token：

```http
Authorization: Bearer <MCP_AUTH_TOKENS 中配置的令牌>
```

可以使用公开验证端点 [http://8.137.168.202:8888/mcp](http://8.137.168.202:8888/mcp) 测试 MCP 查询能力：

```text
http://8.137.168.202:8888/mcp
```

以支持 Streamable HTTP 的 MCP 客户端为例，配置结构如下；不同客户端的配置字段可能略有差异：

```json
{
  "mcpServers": {
    "knowledge-review": {
      "type": "streamable-http",
      "url": "http://8.137.168.202:8888/mcp",
      "headers": {
        "Authorization": "Bearer <通过邮件申请的 Token>"
      }
    }
  }
}
```

验证服务只提供只读 MCP 工具，不开放数据修改能力。Token 不在仓库中公开，请发送邮件至 [269873721@qq.com](mailto:269873721@qq.com?subject=MCP%20Token%20申请) 申请。

> [!WARNING]
> 上述验证端点使用明文 HTTP，仅适合临时验证；Bearer Token 会随请求发送。不要在不可信网络中使用，正式接入应改用 HTTPS。

接入支持 MCP 的 AI 客户端后，可以基于教材、课时和知识点关系开展分学科复习与诊断：

![通过 MCP 使用知识库进行课程复习](docs/assets/mcp-review-example.png)

目前提供以下只读工具：

| 工具 | 用途 |
| --- | --- |
| `list_subjects` | 列出学科及教材、知识点数量 |
| `list_textbooks` | 按学科、年级和学期筛选教材 |
| `list_lessons` | 查询指定教材的全部课时 |
| `get_lesson_review_context` | 查询课时知识点及一层上下游关系 |
| `get_knowledge_point_context` | 查询单个知识点及一层上下游关系 |

生产环境应使用高强度随机令牌，并通过 `MCP_ALLOWED_ORIGINS` 限制允许的浏览器来源。

## 项目结构

```text
.
├── db_schema/                 # PostgreSQL / pgvector 表结构
├── frontend/                  # Vue 3 前端与静态资源镜像
├── knowledge/                 # Spring Boot 后端、Prompt 和测试
│   └── src/main/resources/
│       ├── mapper/            # MyBatis XML Mapper
│       └── prompts/           # AI 提示词模板
├── docker-compose.yml         # 完整服务编排
├── nginx.conf                 # HTTPS 网关及 MCP 反向代理
└── .env.example               # 部署配置模板
```

## 数据与版权边界

- 请仅处理你有权使用的教材或资料，并遵守所在地法律法规及内容权利人的授权条件。
- 请勿将教材 PDF、页面截图、OCR 全文或其他可能替代原作的内容提交到仓库或公开部署。
- 使用者需自行评估模型服务、数据处理和公开展示行为的合规性。

## 许可证

开源许可证以仓库根目录中的 `LICENSE` 文件为准。第三方依赖及通过本项目处理的输入内容仍分别受其自身许可证或权利条款约束。
