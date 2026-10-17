[English](./README_EN.md) | 中文

---

>本项目基于 Dify 进行二次开发，遵循 Apache License 2.0 协议。非常感谢 Dify 团队提供的优秀开源底座，让构建工作流变得如此简单。

## 💡 1. 项目背景

**"One sentence, one workflow." (一句话，一个工作流)**

### 🔴 痛点 
在使用现有工作流搭建工具的过程中，我发现一个明显问题：它们的交互门槛依然很高，用户得先理解每个节点的意义、输入输出的逻辑，这对运营、销售这些非技术人员来说并不友好。

### 🟢 解决方案

**能不能用户说一句话，工作流就自动生成了呢？**
带着这个思考，我们基于Dify的开源代码开发了 **workflowagent** 功能。它致力于抹平“想法”与“落地”之间的鸿沟。

### ✨ 核心特性

* **对话即搭建**：无需学习复杂的语法或节点逻辑，用大白话就能生成应用。
* **全自动配置**：
    * 自动选择合适的节点（LLM, Code 等）。
    * 自动填写 System Prompt 和参数。
    * 自动完成节点间的连线和变量引用。
* **开箱即用**：生成的结构直接兼容 Dify 标准，导入即可运行，支持在此基础上继续微调。

---

## 📺 2.Demo 演示

### ⚡️ 极速生成
**Case**: 输入 "请生成一个工作流，根据用户输入的url的内容，生成适配小红书、微博、抖音不同风格的推广文案，包括标题和正文。"

如果生成的内容不符合自己的预期，有两种修改方式：
- 继续和助手对话，用自然语言说清楚自己的需求，agent会根据你的需求重新编排并渲染到画布上
- 手动修改

https://github.com/user-attachments/assets/ef3d10ef-a81e-4f9b-bf3a-ecf7f5ef3b19


### 🏃‍♂️ 完美运行 
生成的工作流具备完整的上下文逻辑，无需修改，点击运行即可输出结果。

如果运行过程中出现错误，你可以把错误具体错误发给助手，它会根据错误信息重新编排并渲染到画布上

https://github.com/user-attachments/assets/a40f452b-9c9a-49b3-9f58-4e7b1304c55c

---

## 🚀 3.快速部署

### 📋 系统要求
- Docker & Docker Compose
- 内存 ≥ 4GB
- CPU ≥ 2核

### 🐳 安装 Docker

如果您尚未安装 Docker，请根据您的操作系统选择安装方式：

| 操作系统 | 安装方式 |
|---------|---------|
| **Windows** | 下载并安装 [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/)。安装后启动 Docker Desktop，等待右下角图标显示 "Docker is running"。 |
| **macOS** | 下载并安装 [Docker Desktop for Mac](https://docs.docker.com/desktop/install/mac-install/)。支持 Intel 和 Apple Silicon 芯片。 |
| **Linux (Ubuntu/Debian)** | 运行以下命令：<br>`curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh` |

> 💡 **提示**：安装完成后，运行 `docker --version` 和 `docker-compose --version` 验证安装成功。

### 🔧 部署配置

> ⚠️ **重要提示**：本项目使用**预构建的 Docker 镜像**，包含完整的 Workflow Agent 功能。

> 首次启动时会从 Docker Hub 拉取镜像，根据网络速度可能需要 **5-10 分钟**。后续启动会很快。

> **建议优先使用具备较强规划能力、工具调用能力和schema输出稳定性的模型**，例如：Claude Opus 4.1 / 4.5、Claude Sonnet 4.5。上述模型已在本项目中完成测试，在相对复杂的任务中一次生成成功率很高。使用能力较弱的模型可能会显著增加调试与迭代成本（时间&token）。注：不同模型在 schema 遵循与稳定性上存在差异，实际效果以测试结果为准。

#### 🪟 Windows 用户 (推荐一键启动)

1.  **获取代码**
    ```bash
    git clone https://github.com/guoxinxin20252025/workflowagent.git
    cd workflowagent
    ```

2.  **运行一键启动脚本**
    双击运行 `setup.bat`，脚本会自动：
    - ✅ 检查 Docker 环境
    - ✅ 修复 Windows 常见的 Docker 凭证问题
    - ✅ 创建并配置 `.env` 文件（自动修复网络配置，设置 `GUNICORN_TIMEOUT=600` 防止超时）
    - ✅ **引导配置 Agent 模型**（分别输入 Base URL, API Key, Model Name）
    - ✅ **从 Docker Hub 拉取预构建镜像**（包含 Workflow Agent 功能）
    - ✅ 启动所有服务并验证健康状态

#### 🐧 Linux / macOS 用户 (推荐一键启动)

1.  **获取代码**
    ```bash
    git clone https://github.com/guoxinxin20252025/workflowagent.git
    cd workflowagent
    ```

2.  **运行一键启动脚本**
    ```bash
    chmod +x setup.sh
    ./setup.sh
    ```
    脚本功能与 Windows 版本相同，会自动从 Docker Hub 拉取预构建镜像并启动服务。

#### 🌐 访问应用

当脚本显示 `[SUCCESS] All services are up and running!` 时，打开浏览器访问：👉 **http://localhost**

1. **首次登录**：需要设置管理员账户。
2. **Workflow Agent**：登录后，创建一个“工作流”应用，在编辑器右下角即可看到“Workflow Agent”对话框。


#### ⚙️ 手动配置 (高级用户)

如果您不想使用自动脚本，可以手动配置：

1.  **进入 Docker 目录**: `cd docker`
2.  **创建环境变量文件**: `cp .env.example .env`
3.  **修改 .env**:
    - 配置 `AGENT_MODEL_BASE_URL`, `AGENT_MODEL_API_KEY`, `AGENT_MODEL_NAME`。
    - **关键修复**: 将以下变量中的 `localhost` 或 `127.0.0.1` 更改为 Docker 服务名称：
        - `REDIS_HOST=redis`
        - `DB_HOST=db_postgres`
        - `WEAVIATE_ENDPOINT=http://weaviate:8080`
        - `INTERNAL_FILES_URL=http://api:5001`
        - `CELERY_BROKER_URL=redis://:difyai123456@redis:`
        - `CODE_EXECUTION_ENDPOINT=http://sandbox:8194`
        - `PLUGIN_DAEMON_URL=http://plugin_daemon:5002`
    - 清空前端 URL 以使用相对路径：
        - `CONSOLE_API_URL=`
        - `SERVICE_API_URL=`
    - **设置超时**: `GUNICORN_TIMEOUT=600`
4.  **构建自定义镜像**:
    确保根目录下的 `docker/docker-compose.override.yaml` 存在，它指向 `../api` 和 `../web`。
5.  **启动服务**:
    ```bash
    docker-compose --profile postgresql --profile weaviate up -d --build
    ```

### ❓ 常见问题 (Troubleshooting)

**Q1. 浏览器显示 502 Bad Gateway 或 401 Unauthorized**
如果启动成功但浏览器报错，通常是因为旧缓存或认证过期：
1.  **清除浏览器缓存和 Cookie**（极力推荐）。
2.  尝试使用 **无痕模式 (Incognito Mode)** 访问。
3.  如果仍然 502，可能是 Docker 性能问题导致 API 响应慢。`setup.bat` 已自动将超时时间设置为 600秒 (10分钟)，请耐心等待服务初始化。

**Q2. 构建镜像失败 (Network Error / 403 Forbidden)**
这通常是由于网络问题无法拉取基础镜像。
- 尝试配置 Docker 镜像加速器。
- 对于中国大陆用户，可能需要科学上网环境。

**Q3. "Agent 模型调用失败"**
请检查 `docker/.env` 文件中的 `AGENT_MODEL_*` 配置是否正确：
- `AGENT_MODEL_BASE_URL`: 是否完整 (例如 `.../v1/chat/completions`)
- `AGENT_MODEL_API_KEY`: 是否有效
- `AGENT_MODEL_NAME`: 模型名称是否正确 (如 `gpt-4o`)

---


## 🖱️ 4.使用指南

1. **登录系统**：
   完成部署后，创建管理员账号并登录。
   
2. **创建应用**:
   创建一个新的应用，目前支持 **"工作流 (Workflow)"** 和 **"Chatflow"** 两种类型。

3. **输入需求**:
   进入编辑器后，在页面右侧找到 **“工作流编排助手”** 弹窗。
   在输入框中用自然语言描述你的需求，例如：帮我创建一个工作流，能支持中英文互译。

4. **一键运行**:
   等待画布生成完成后，可通过右上角 「测试运行（Run）」 查看执行效果。

5. **配置LLM节点**
   在使用之前，可以点击右上角头像->设置->模型供应商进行供应商和model的配置。（用于workflow中需要使用模型的节点中使用）
   >💡 提示：每个供应商下都有很多model，建议只勾选你日常使用、效果稳定的模型，Agent 会在所选模型范围内进行自动选择。

---
## ⚙️ 5.系统架构

### 📐 架构设计
Workflowagent 采用经典的 Agent + Tools 架构，通过 LLM 的推理能力和工具调用机制，实现自然语言到工作流的自动转换。
 ```
  ┌─────────────────────────────────────────────────────────┐
  │                    用户输入自然语言                        │
  └─────────────────────────────────────────────────────────┘
                            ↓
  ┌─────────────────────────────────────────────────────────┐
  │              前端 (Next.js + React)                      │
  │  • 聊天界面 (WorkflowAgentChat)                          │
  │  • 实时消息流 (SSE)                                       │
  │  • 自动画布刷新                                           │
  └─────────────────────────────────────────────────────────┘
                            ↓
  ┌─────────────────────────────────────────────────────────┐
  │              后端 Agent 引擎 (Flask)                      │
  │  ┌───────────────────────────────────────────────────┐  │
  │  │  WorkflowAgentEngine (核心引擎)                     │  │
  │  │  • 对话管理                                         │  │
  │  │  • Agent迭代循环                                    │  │
  │  │  • 工具调用协调                                      │  │
  │  └───────────────────────────────────────────────────┘  │
  │         ↓                    ↓                    ↓     │
  │  ┌──────────┐      ┌──────────────┐      ┌──────────┐   │
  │  │ LLM      │      │ Tool         │      │ Database │   │
  │  │ Adapter  │      │ Manager      │      │          │   │
  │  └──────────┘      └──────────────┘      └──────────┘   │
  └─────────────────────────────────────────────────────────┘
                            ↓
  ┌─────────────────────────────────────────────────────────┐
  │                      LLM API                            │
  └─────────────────────────────────────────────────────────┘
```
### 📂 核心代码结构
💡 带有 ⭐ 的为核心逻辑文件，建议优先阅读。
 ```
  api/
  ├── agent/
  │   ├── engine.py              # ⭐ Agent 核心引擎
  │   │                          #    - ReAct 循环 (最多 10 轮迭代)
  │   │                          #    - 对话历史管理与持久化
  │   │                          #    - 工具调用协调
  │   ├── service.py             # 会话服务层
  │   │                          #    - Session 生命周期管理
  │   │                          #    - Agent 实例创建与缓存
  │   ├── llm_adapter.py         # ⭐ LLM 多模型适配器
  │   │                          #    - 支持 OpenAI / Claude / Gemini
  │   │                          #    - 自动检测 API 类型 (默认 OpenAI)
  │   │                          #    - 统一请求/响应格式转换
  │   └── tools/
  │       ├── manager.py         # 工具管理器 (注册与分发)
  │       ├── update_workflow.py # ⭐ 核心工具：工作流更新
  │       │                      #    - 接收 LLM 生成的工作流 JSON
  │       │                      #    - 多层验证 (格式/连接性/Pydantic)
  │       │                      #    - 保存到数据库并触发前端刷新
  │       └── get_available_nodes.py  # 节点查询工具
  │                              #    - 返回所有可用节点及其 Schema
  ├── controllers/console/app/
  │   └── workflow_agent.py      # REST API 控制器 (SSE 流式响应)
  └── models/
      └── workflow_agent.py      # 数据模型 (Session + Message)

  web/
  └── app/components/workflow-agent/
      ├── components/
      │   └── workflow-agent-chat.tsx  # ⭐ 聊天界面组件
      ├── hooks/
      │   └── use-workflow-agent.ts    # ⭐ 前端核心 Hook
      │                                #    - SSE 流式消息处理
      │                                #    - 状态管理与自动刷新
      └── api.ts                       # API 调用封装
```

### 💡 设计亮点

1. ⭐**Agent 自主决策**
   最最核心的一点，完全依靠现在 agent model的能力，LLM 自己决定何时调用哪个工具，无需硬编码规则。**因此大家使用的时候一定要配置在规划能力和工具调用能力上表现优秀的模型，比如Claude opus 4.1/4.5，GPT 5/5.1**
2. 多层验证机制：确保生成的工作流配置正确可用
3. 多模型支持：通过适配器模式轻松切换不同 LLM
4. 实时反馈：用户可以看到 Agent 的完整思考过程
5. 对话持久化：支持断点续聊，复杂需求可分多次完成
---
  
## 💛 6.社区入口&反馈渠道
我们非常欢迎社区的参与！  
无论你是 **开发者 / 产品经理 / 运营 / Agent 玩家**，只要你在真实使用 WorkflowAgent 的过程中有需求、有想法、有问题，都可以参与进来，一起把它打磨好 🚀

### 🎯 我们目前需要帮助的方向
- **测试用例**：真实的自然语言需求 + 你期望生成的 workflow行为
- **功能想法**：真实使用场景下的需求或改进建议
- **Bug 反馈**：异常行为、生成错误、不符合预期的结果
- **代码贡献**：功能开发、工具集成、Prompt / 逻辑优化

### 🤝 如何参与？
- 反馈bug
   - 创建 **Issue**，使用 `bug` 标签
   - 提供：输入内容 + 实际结果 + 期望结果
- 贡献测试用例（无需写代码）
   - 创建 **Issue**，使用 `test` 标签
   - 内容包括：
      - Input Prompt（你的自然语言需求）
      - Expected Behavior（你期望生成的 workflow 行为）
- 功能想法 / 需求讨论
    - **Discussions → Ideas**
    - 描述你的使用场景和痛点即可（不需要写解决方案）
- 直接贡献代码 
  - Fork 本仓库：点击右上角的 Fork 按钮。
  - 创建分支：git checkout -b feature/your-feature-name
  - 提交PR
 
>所有 Issue / Discussion 都会被阅读和回复，但不保证所有需求都会被实现。

---
## 📄 7.License & Disclaimer (协议与声明)
本项目基于 Dify (1.10.0)进行二次开发，遵循 Apache License 2.0 协议。 您可以免费用于商业或非商业用途，但请保留原始协议声明。

⚠️ 提醒
- AI 生成的不确定性：本功能由 LLM 驱动，生成的工作流配置可能存在逻辑错误、参数缺失或非最佳实践。
- 人工审查：在将生成的工作流投入生产环境之前，请务必进行人工审查和测试。
- 数据安全：请勿在 Prompt 中输入敏感的个人隐私或密钥信息。

---
## 👥 8.Contributors (贡献者)

本项目由以下开发者共同创建：
- [@guoxinxin20252025](https://github.com/guoxinxin20252025)
- [@Shiyao-Huang](https://github.com/Shiyao-Huang)

我们欢迎社区贡献！请查看 [社区入口&反馈渠道](#-6社区入口反馈渠道) 了解如何参与。

---
## ❤️ 9.Acknowledgements (致谢)
特别感谢 Dify 团队提供的优秀开源底座，让构建工作流变得如此简单。
  
  







