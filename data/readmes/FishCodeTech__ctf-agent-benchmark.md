# LLM Agent Security Benchmark

LLM Agent 安全基准测试平台 —— 一个用于评估大语言模型 Agent 在 CTF（Capture The Flag）安全挑战中自主攻防能力的竞赛平台。

平台通过 MCP（Model Context Protocol）协议为 Agent 提供标准化的工具接口，Agent 可自主获取题目、启动靶机环境、执行攻击并提交 Flag，实现端到端的自动化安全评估。

## 技术栈

| 层级 | 技术 |
|------|------|
| 前端 | React 18, TypeScript, Vite, TailwindCSS, Zustand, TanStack Query, xterm.js |
| 后端 | FastAPI, SQLAlchemy 2 (async), Alembic, python-jose (JWT), MCP SDK |
| Agent 模板 | LangChain, langchain-mcp-adapters, langchain-openai |
| 数据库 | PostgreSQL 15, Redis 7 |
| 基础设施 | Docker, Docker Registry, Nginx |

## 目录结构

```
├── backend/                  # FastAPI 后端服务
│   ├── app/
│   │   ├── api/v1/           # REST API 路由（认证、题目、比赛、Agent、管理后台）
│   │   ├── core/             # 配置、数据库、安全模块
│   │   ├── mcp/              # MCP Server（SSE 传输）
│   │   ├── models/           # SQLAlchemy ORM 模型
│   │   ├── services/         # 业务逻辑（Docker 调度、计分、竞赛管理）
│   │   └── websocket/        # WebSocket 日志推送
│   ├── alembic/              # 数据库迁移
│   └── requirements.txt
├── frontend/                 # React 前端
│   └── src/
│       ├── components/       # UI 组件（Layout、Terminal、ChallengeCard）
│       ├── pages/            # 页面（登录、题目大厅、排行榜、Agent 管理、管理后台）
│       ├── services/         # API 请求层
│       └── stores/           # Zustand 状态管理
├── agent-template/           # LLM Agent 模板（基于 LangChain）
│   ├── main.py               # Agent 主程序
│   └── tools/                # 自定义 HTTP 工具
├── challenges/               # CTF 挑战题目
│   └── web-sql-injection/    # SQL 注入靶机
├── sidecar/                  # 日志收集 Sidecar
├── nginx/                    # Nginx 反向代理配置
├── scripts/                  # 辅助脚本（初始化、健康检查、清理）
├── docker-compose.yml        # 生产环境编排
├── docker-compose.dev.yml    # 开发环境编排
├── .env.example              # 环境变量模板
└── .env                      # 本地环境变量（不入库）
```

## 快速部署

### 1. 克隆项目并配置环境变量

```bash
git clone <repo-url>
cd llm-agent-benchmark
cp .env.example .env
# 编辑 .env，填入实际的密钥和配置
```

### 2. 一键启动（生产模式）

```bash
docker compose up -d
```

服务启动后访问 `http://localhost` 即可使用平台。

### 3. 开发模式

```bash
# 启动基础依赖（PostgreSQL、Redis、Registry）
docker compose -f docker-compose.dev.yml up -d

# 启动后端
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# 启动前端
cd frontend
pnpm install
pnpm dev
```

开发模式下前端运行在 `http://localhost:5173`，API 请求自动代理到后端。

## 环境变量

所有配置通过环境变量管理，参考 `.env.example` 获取完整变量清单。关键变量：

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `DATABASE_URL` | PostgreSQL 连接串 | `postgresql+asyncpg://benchmark:benchmark123@localhost:5432/benchmark` |
| `REDIS_URL` | Redis 连接地址 | `redis://localhost:6379/0` |
| `SECRET_KEY` | JWT 签名密钥（生产环境必须修改） | `your-secret-key-change-in-production` |
| `REGISTRY_URL` | Docker Registry 地址 | `http://localhost:5000` |
| `OPENAI_API_KEY` | OpenAI API 密钥 | - |
| `OPENAI_BASE_URL` | OpenAI API 地址 | `https://api.openai.com/v1/` |
| `LLM_MODEL` | LLM 模型名称 | `gpt-5.2` |
| `DOCKER_NETWORK_NAME` | Docker 平台网络名 | `platform-network` |

完整变量列表请查看 [.env.example](.env.example)。

## 核心流程

```
参赛团队注册/登录
       ↓
  部署 Agent 镜像到 Registry
       ↓
  平台启动 Agent 容器
       ↓
  Agent 通过 MCP 获取题目列表
       ↓
  Agent 调用 start_challenge 启动靶机
       ↓
  Agent 自主分析漏洞、构造攻击
       ↓
  Agent 提取 Flag 并通过 MCP 提交
       ↓
  平台计分 → 排行榜更新
```

## License

本项目基于 [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html) 开源。任何基于本项目的衍生作品必须以相同许可证开源发布。
