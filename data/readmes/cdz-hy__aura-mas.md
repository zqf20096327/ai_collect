<div align="center">

# AURA-MAS 个性化多智能体学习系统

## Adaptive User-centric Resource Architecture — Multi-Agent System

基于 **LangGraph 多智能体协作**，面向学习计划、资源生成、知识管理与学习分析的一体化平台。

[![License](https://img.shields.io/badge/License-MIT-2563EB.svg)](LICENSE)
[![Java](https://img.shields.io/badge/Java-21-E76F00.svg)](Java-backend)
[![Spring Boot](https://img.shields.io/badge/Spring_Boot-3.2.5-6DB33F.svg)](Java-backend)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB.svg)](Python-backend)
[![Vue](https://img.shields.io/badge/Vue-3.5-42B883.svg)](Vue-frontend)
[![Kotlin](https://img.shields.io/badge/Kotlin-2.1-7F52FF.svg)](Android-app)

[功能概览](#功能概览) · [界面预览](#界面预览) · [动态演示](#动态演示) · [系统架构](#系统架构) · [快速开始](#快速开始) · [部署说明](#部署说明)

[项目仓库](https://github.com/cdz-hy/aura-mas) · [问题反馈](https://github.com/cdz-hy/aura-mas/issues)

</div>

---

AURA-MAS 覆盖 Web、Android、业务服务与 AI 智能体引擎，通过 RAG、多模态生成、质量审查和用户画像持续生成适配学习目标的内容。

## 功能概览

| 能力 | 说明 |
| --- | --- |
| 多智能体协作 | 主控调度、任务分解、RAG 检索、内容编排、质量审查及异常回退协同执行 |
| 多模态学习资源 | 支持图文、题目、教学动画、视频、思维导图、播客等资源 |
| 个性化学习计划 | 结合学习目标与用户画像生成计划，跟踪模块进度和学习行为 |
| 对话式学习 | 通过 SSE 流式呈现回答、生成状态与智能体处理过程 |
| 知识管理 | 提供知识树、知识图谱、笔记、闪卡及错题辅导能力 |
| 学习分析 | 汇总学习时长、活跃度、掌握情况和效率趋势 |
| 多端访问 | 提供 Vue 3 Web 应用和 Jetpack Compose Android 应用 |
| 管理能力 | 支持用户、知识库、AI 补充资源、Token 用量和系统日志管理 |

---

## 界面预览

> 图片来自项目实际 Web 界面。点击图片可查看原图。

### 用户端

<p align="center">
  <a href="Vue-frontend/public/pictures/用户首页.png">
    <img src="Vue-frontend/public/pictures/用户首页.png" alt="用户首页" width="920" />
  </a>
  <br />
  <sub>用户首页</sub>
</p>

<table>
  <tr>
    <td width="50%" align="center">
      <a href="Vue-frontend/public/pictures/用户计划界面.png"><img src="Vue-frontend/public/pictures/用户计划界面.png" alt="用户计划界面" width="100%" /></a><br />
      <sub>学习计划</sub>
    </td>
    <td width="50%" align="center">
      <a href="Vue-frontend/public/pictures/用户计划详情界面-图文资源.png"><img src="Vue-frontend/public/pictures/用户计划详情界面-图文资源.png" alt="图文资源" width="100%" /></a><br />
      <sub>图文学习资源</sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center">
      <a href="Vue-frontend/public/pictures/用户计划详情界面-题目资源.png"><img src="Vue-frontend/public/pictures/用户计划详情界面-题目资源.png" alt="题目资源" width="100%" /></a><br />
      <sub>题目资源</sub>
    </td>
    <td width="50%" align="center">
      <a href="Vue-frontend/public/pictures/用户计划详情界面-动画资源.png"><img src="Vue-frontend/public/pictures/用户计划详情界面-动画资源.png" alt="动画资源" width="100%" /></a><br />
      <sub>教学动画资源</sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center">
      <a href="Vue-frontend/public/pictures/用户计划详情界面-视频资源.png"><img src="Vue-frontend/public/pictures/用户计划详情界面-视频资源.png" alt="视频资源" width="100%" /></a><br />
      <sub>网络教学视频</sub>
    </td>
    <td width="50%" align="center">
      <a href="Vue-frontend/public/pictures/用户计划详情界面-导图资源.png"><img src="Vue-frontend/public/pictures/用户计划详情界面-导图资源.png" alt="导图资源" width="100%" /></a><br />
      <sub>思维导图资源</sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center">
      <a href="Vue-frontend/public/pictures/用户计划详情界面-播客资源.png"><img src="Vue-frontend/public/pictures/用户计划详情界面-播客资源.png" alt="播客资源" width="100%" /></a><br />
      <sub>播客资源</sub>
    </td>
    <td width="50%" align="center">
      <a href="Vue-frontend/public/pictures/用户笔记界面与闪卡.png"><img src="Vue-frontend/public/pictures/用户笔记界面与闪卡.png" alt="笔记与闪卡" width="100%" /></a><br />
      <sub>笔记与闪卡</sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center">
      <a href="Vue-frontend/public/pictures/用户学习分析界面.png"><img src="Vue-frontend/public/pictures/用户学习分析界面.png" alt="学习分析" width="100%" /></a><br />
      <sub>学习分析</sub>
    </td>
    <td width="50%" align="center">
      <a href="Vue-frontend/public/pictures/用户学习画像界面.png"><img src="Vue-frontend/public/pictures/用户学习画像界面.png" alt="学习画像" width="100%" /></a><br />
      <sub>学习画像</sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center">
      <a href="Vue-frontend/public/pictures/用户知识图谱界面.png"><img src="Vue-frontend/public/pictures/用户知识图谱界面.png" alt="知识图谱" width="100%" /></a><br />
      <sub>知识图谱</sub>
    </td>
    <td width="50%" align="center">
      <a href="Vue-frontend/public/pictures/用户设置界面.png"><img src="Vue-frontend/public/pictures/用户设置界面.png" alt="用户设置" width="100%" /></a><br />
      <sub>用户设置</sub>
    </td>
  </tr>
</table>

### 管理端

<p align="center">
  <a href="Vue-frontend/public/pictures/管理员首页.png">
    <img src="Vue-frontend/public/pictures/管理员首页.png" alt="管理员首页" width="920" />
  </a>
  <br />
  <sub>管理后台首页</sub>
</p>

<table>
  <tr>
    <td width="50%" align="center">
      <a href="Vue-frontend/public/pictures/管理员pdf知识库管理界面.png"><img src="Vue-frontend/public/pictures/管理员pdf知识库管理界面.png" alt="PDF知识库管理" width="100%" /></a><br />
      <sub>PDF 知识库管理</sub>
    </td>
    <td width="50%" align="center">
      <a href="Vue-frontend/public/pictures/管理员AI生成补充资源管理界面.png"><img src="Vue-frontend/public/pictures/管理员AI生成补充资源管理界面.png" alt="AI补充资源管理" width="100%" /></a><br />
      <sub>AI 补充资源管理</sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center">
      <a href="Vue-frontend/public/pictures/管理员token调用界面.png"><img src="Vue-frontend/public/pictures/管理员token调用界面.png" alt="Token调用统计" width="100%" /></a><br />
      <sub>Token 调用统计</sub>
    </td>
    <td width="50%" align="center">
      <a href="Vue-frontend/public/pictures/管理员日志界面.png"><img src="Vue-frontend/public/pictures/管理员日志界面.png" alt="系统日志" width="100%" /></a><br />
      <sub>系统日志</sub>
    </td>
  </tr>
</table>

---

## 动态演示

> 动图文件较大，按需展开查看。

<details>
<summary><strong>图文学习资源</strong></summary>
<br />
<img src="Vue-frontend/public/show/图文学习资源.gif" alt="图文学习资源演示" width="100%" />
</details>

<details>
<summary><strong>对话式资源生成</strong></summary>
<br />
<img src="Vue-frontend/public/show/对话式资源生成.gif" alt="对话式资源生成演示" width="100%" />
</details>

<details>
<summary><strong>播客类型资源</strong></summary>
<br />
<img src="Vue-frontend/public/show/播客类型资源.gif" alt="播客资源演示" width="100%" />
</details>

<details>
<summary><strong>教学动画资源</strong></summary>
<br />
<img src="Vue-frontend/public/show/教学动画资源.gif" alt="教学动画资源演示" width="100%" />
</details>

<details>
<summary><strong>测验作答与个性化错题辅导</strong></summary>
<br />
<img src="Vue-frontend/public/show/测验作答与个性化错题辅导.gif" alt="测验与错题辅导演示" width="100%" />
</details>

<details>
<summary><strong>网络教学视频</strong></summary>
<br />
<img src="Vue-frontend/public/show/网络教学视频.gif" alt="网络教学视频演示" width="100%" />
</details>

<details>
<summary><strong>随学更新知识图谱</strong></summary>
<br />
<img src="Vue-frontend/public/show/随学更新知识图谱.gif" alt="知识图谱更新演示" width="100%" />
</details>

---

## 系统架构

```mermaid
graph TB
    subgraph Client["客户端"]
        Web["Vue 3 Web"]
        Android["Android App"]
    end

    subgraph Business["Java 业务服务 - Spring Boot"]
        API["认证 / 计划 / 资源 / 笔记 / 统计 / 管理 API"]
        MySQL[("MySQL")]
        Redis[("Redis")]
        MQ[("RabbitMQ")]
        API --> MySQL
        API --> Redis
        API --> MQ
    end

    subgraph AI["Python AI 引擎 - FastAPI + LangGraph"]
        MainGraph["个性化学习主图"]
        KnowledgeGraph["知识图谱更新子图"]
        VectorDB[("Qdrant")]
        Models["LLM / Embedding / TTS / 图像生成"]
        MainGraph --> VectorDB
        MainGraph --> Models
        MainGraph -.->|"异步触发"| KnowledgeGraph
    end

    Web -->|"REST / SSE"| API
    Android -->|"REST / SSE"| API
    API -->|"Ticket / AI 请求"| MainGraph
    MainGraph -->|"状态与资源持久化"| API
    KnowledgeGraph -->|"知识图谱持久化"| API
```

### LangGraph 主工作流

主图由主控智能体动态识别意图，并在任务分解、RAG 检索、内容生成、并行审查、人工确认与异常回退之间路由。

```mermaid
graph TD
    START(["开始"]) --> Controller["主控智能体"]
    Controller --> Intent{"意图与状态路由"}

    Intent -->|"复杂资源任务"| Decomposer["任务分解"]
    Intent -->|"简单问答"| Answer["简答智能体"]
    Intent -->|"题目生成/批改"| Quiz["测验智能体"]
    Intent -->|"指定类型资源"| Typed["类型资源/动画生成"]
    Intent -->|"追问"| Wait["等待用户回复"]

    Decomposer -->|"多模块"| Confirm["人工确认"]
    Decomposer -->|"单模块"| RAG["RAG 检索"]
    Confirm -->|"确认"| RAG
    Confirm -->|"修改意见"| Controller

    RAG --> Quality{"检索质量"}
    Quality -->|"充足"| Orchestrator["内容编排"]
    Quality -->|"充足，并行"| Reviewer["质量审查"]
    Quality -->|"不足"| Generator["自主生成"]

    Orchestrator --> Merge["审查编排汇合"]
    Reviewer --> Merge
    Merge --> Review{"审查结果"}
    Review -->|"通过"| END(["结束"])
    Review -->|"优化/降级"| Controller

    Generator --> END
    Answer --> END
    Quiz --> END
    Typed --> END
    Wait -->|"用户回复"| Controller
```

### 知识图谱更新子图

图文资源生成完成后，辅助工作流在后台完成领域识别、旧图加载、概念融合和持久化，不阻塞主对话响应。

```mermaid
graph LR
    START(["开始"]) --> Classify["领域分类"]
    Classify --> Fetch["获取现有图谱"]
    Fetch --> Merge["概念提取与融合"]
    Merge --> Persist["持久化"]
    Persist --> END(["结束"])
```

---

## 技术栈

| 层级 | 主要技术 |
| --- | --- |
| Web 前端 | Vue 3.5、TypeScript 5.7、Vite 6、Pinia、Tailwind CSS、ECharts、Mermaid |
| Android | Kotlin 2.1、Jetpack Compose、Hilt、Room、Retrofit、OkHttp |
| Java 后端 | Java 21、Spring Boot 3.2.5、Spring Security、MyBatis-Plus、JWT |
| Python 后端 | FastAPI、LangGraph、LangChain、Qdrant Client、FastEmbed |
| 数据与消息 | MySQL、Redis、RabbitMQ、Qdrant |
| AI 与多媒体 | DashScope、MiMo、Volcengine Ark、MinerU、七牛云、Playwright、FFmpeg |
| 测试 | JUnit、Vitest、Playwright、Pytest、Android Instrumentation |

## 项目结构

```text
AURA-MAS/
├── Android-app/       # Kotlin + Jetpack Compose 移动端
├── Java-backend/      # Spring Boot 业务服务与数据持久化
├── Python-backend/    # FastAPI、LangGraph、RAG 与多模态生成
├── Vue-frontend/      # Vue 3 Web 用户端与管理端
├── deploy/            # 通用及 Ubuntu 部署文档
├── docs/              # 补充项目文档
├── docker-compose.yml # Redis、RabbitMQ、Qdrant
└── README.md
```

---

## 快速开始

### 环境要求

| 依赖 | 建议版本 | 用途 |
| --- | --- | --- |
| JDK | 21+ | Java 后端 |
| Maven | 3.9+ | Java 构建 |
| Python | 3.11+ | AI 引擎 |
| Node.js | 18+ | Web 前端 |
| MySQL | 8.0+ | 核心业务数据 |
| Docker / Compose | 推荐 | 快速启动 Redis、RabbitMQ、Qdrant |
| Android Studio | 最新稳定版 | Android 构建与调试 |

> FFmpeg 与 Playwright Chromium 仅在导出 H.264/AAC 教学动画视频时需要。

### 1. 获取项目

```bash
git clone https://github.com/cdz-hy/aura-mas.git
cd aura-mas
```

### 2. 准备 MySQL

创建数据库，Java 后端启动时会通过 `schema.sql` 与 `data.sql` 初始化结构和基础数据。

```sql
CREATE DATABASE learning_system
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
```

Java 本地配置可参考：

```text
Java-backend/src/main/resources/application-example.yml
```

请至少配置数据库密码、JWT 密钥和内部服务密钥；Java 的 `INTERNAL_SECRET` 必须与 Python 的 `JAVA_SERVICE_SECRET` 保持一致。

### 3. 启动基础服务

```bash
docker compose up -d
```

该命令启动 Redis、RabbitMQ 与 Qdrant。MySQL 不包含在当前 Compose 文件中，需单独准备。

### 4. 启动 Java 后端

```bash
cd Java-backend
mvn spring-boot:run
```

默认地址：`http://localhost:8080`

### 5. 启动 Python AI 引擎

```bash
cd Python-backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
cp .env.template .env
# 编辑 .env，将 PORT 设为 8002
python main.py
```

> Vue 前端与 Java 后端均默认连接 `localhost:8002`，Python `.env` 中 `PORT` 必须设为 `8002`。

FastAPI 文档：`http://localhost:8002/docs`

如需动画视频导出，再安装以下运行时：

```bash
python -m playwright install chromium
```

同时确保系统已安装 `ffmpeg` 与 `ffprobe`。

### 6. 启动 Web 前端

```bash
cd Vue-frontend
npm ci
npm run dev
```

默认地址：`http://localhost:5173`

### 7. 构建 Android 应用

```bash
cd Android-app
./gradlew assembleDebug
```

Windows 也可执行：

```powershell
gradlew.bat assembleDebug
```

Android 应用支持在设置界面调整 Java 与 Python 服务地址。

---

## 常用命令

| 模块 | 开发 / 运行 | 测试 / 构建 |
| --- | --- | --- |
| Vue | `npm run dev` | `npm run test` / `npm run test:e2e` / `npm run build` |
| Java | `mvn spring-boot:run` | `mvn test` / `mvn package` |
| Python | `python main.py` | `pytest` |
| Android | Android Studio | `./gradlew test` / `./gradlew assembleDebug` |

## API 与服务

| 服务 | 默认地址 | 说明 |
| --- | --- | --- |
| Vue Web | `http://localhost:5173` | 用户端与管理端 |
| Java API | `http://localhost:8080` | 核心业务 API；Swagger 路径受安全配置约束 |
| Python AI | `http://localhost:8002` | 推荐本地联调端口 |
| FastAPI Docs | `http://localhost:8002/docs` | Python API 文档 |
| RabbitMQ 管理台 | `http://localhost:15672` | 仅绑定本机 |
| Qdrant | `http://localhost:6333` | 向量数据库 |

Python 路由主要分为：

- `/api/ai/*`：对话、计划、资源、知识树、知识图谱、闪卡和动画等 AI 能力
- `/api/v1/kb/*`：知识库管理
- `/api/analytics/*`：学习分析

---

## 配置说明

- 不要提交 `.env`、生产密钥、邮箱授权码或云存储凭证。
- Python 配置模板位于 `Python-backend/.env.template`。
- Java 配置模板位于 `Java-backend/src/main/resources/application-example.yml`。
- Redis 不可用时，部分验证码、限流及缓存能力可降级；RabbitMQ 不可用会影响异步任务；Qdrant 不可用会影响 RAG 与知识库能力。
- 七牛云用于头像、文档及多媒体资源上传；相关功能需配置有效的 Bucket 与访问域名。

## 部署说明

- [通用部署指南](deploy/DEPLOY_GUIDE.md)
- [Ubuntu 部署指南](deploy/DEPLOY_UBUNTU.md)

## 许可证

本项目基于 [MIT License](LICENSE) 开源。

## 反馈与贡献

欢迎通过 [Issues](https://github.com/cdz-hy/aura-mas/issues) 提交问题或建议，也欢迎发起 Pull Request。
