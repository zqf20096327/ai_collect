# Simple AI Chat

一个基于框架无关 Core SDK 和解耦式架构的 AI 对话解决方案，旨在为开发者提供摆脱繁重组件的最大自定义自由。

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Version](https://img.shields.io/badge/version-v1.0.0-brightgreen.svg)
![Vue](https://img.shields.io/badge/Vue-3.5+-4FC08D?logo=vue.js&logoColor=white)
![Pinia](https://img.shields.io/badge/Pinia-2.0+-ffd859?logo=pinia&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-009688?logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)

<img src="https://cdn.jsdelivr.net/gh/CommentOut64/simple-ai-chat@master/assets/white.png" />

<img src="https://cdn.jsdelivr.net/gh/CommentOut64/simple-ai-chat@master/assets/black.png" />

## 简介

Simple AI Chat 旨在解决将 AI 对话能力集成到现有 Web 应用时面临的普遍痛点：集成困难、性能瓶颈、用户体验差和框架绑定。

与 `vue-advanced-chat` 等繁重的一体式组件不同，`simple-ai-chat` 不是一个简单的聊天界面，而是一套完整的**解耦式解决方案**。

它提供从框架无关的 **Core SDK**、高质量的 **UI 组件库**到**生产级后端服务**的完整技术栈。 项目采用严格的分层架构，确保了极致的灵活性：

- **Vue 开发者:** 可立即使用 `@simple-ai-chat-project/vue-ui` 获得现代化聊天界面。
- **React/Svelte 开发者:** 可单独使用 `@simple-ai-chat-project/core-sdk` 驱动自定义 UI。
- **需快速嵌入:** （未来）可使用 `@simple-ai-chat-project/web-component`。

## 核心特性

### 对话管理

- ✅ 创建、删除、重命名对话
- ✅ 对话固定到顶部
- ✅ 对话关键词搜索（支持标题和内容）

### 消息交互
- ✅ 实时流式输出 (SSE)
- ✅ 断点续传
- ✅ 完善的 Markdown 渲染
- ✅ 多语言代码语法高亮
- ✅ LaTeX 数学公式渲染支持
- ✅ Mermaid 图表渲染支持

### 智能输入

- ✅ 单行/多行模式自适应输入框
- ✅ 草稿自动保存
- ✅ 文件上传支持（需后端实现）
- ✅ 预留语音输入接口

### 界面与体验

- ✅ 深色/浅色主题一键切换
- ✅ 高性能虚拟滚动
- ✅ 自定义字体、行间距等
- ✅ 多种代码高亮主题可选

### 系统与配置

- ✅ Redis 多级缓存
- ✅ 多模型配置支持
- ✅ 临时模型参数配置
- ✅ 智能上下文Token控制与截断
- ✅ Docker 一键部署

## 架构设计

项目采用 **Monorepo** (pnpm Workspace) 管理，并贯彻**严格的分层架构**，确保各层职责清晰、低耦合。

### 1. 分层结构

```

应用层 (Application Layer)
            ↓
表现层 (Presentation Layer) - [Vue UI 组件库]
            ↓
业务逻辑层 (Business Logic Layer) - [Core SDK]
            ↓
API 层 (API Layer) - [FastAPI]
            ↓
服务层 (Service Layer) - [AI 服务, 配置服务]
            ↓
数据访问层 (Data Access Layer) - [SQLModel ORM + Redis Cache]

```

### 2. 核心设计原则

1.  **UI 库纯粹性**
    `vue-ui` 包是一个 100% 纯粹的 Vue 3 组件库。它不依赖 Shadow DOM 或任何 Web Component 特性，仅通过标准的 Props, Emits 和 Pinia 进行状态管理。这保证了其在 Vue 生态中的可复用性和易测性。

2.  **框架无关的核心**
    `core-sdk` 使用纯 JavaScript (ESM) 实现，不依赖任何前端框架。它提供了所有核心业务逻辑（消息管理、SSE 连接、上下文控制），可以被 Vue, React 或任何其他框架调用。

3.  **适配层隔离**
    （未来规划）所有与 Web Component 相关的适配逻辑（如 Shadow DOM 操作、属性解析）将被封装在独立的 `web-component` 包中，确保不污染核心 UI 库。

### 3. Monorepo 结构

```

simple-ai-chat/
├── backend/              \# Python FastAPI 后端
├── packages/
│   ├── core-sdk/         \# 框架无关的核心 SDK
│   ├── vue-ui/           \# 纯粹的 Vue 3 UI 组件库
│   └── web-component/    \# (未来版本提供) Web Component 适配层
└── docker-compose.yml    \# Docker 编排配置

````

## 技术栈

### 后端

* FastAPI
* SQLModel (SQLAlchemy + Pydantic)
* Redis
* SSE-Starlette
* Uvicorn

### 前端 (vue-ui)

* Vue 3 (Composition API)
* Vite
* Pinia
* TailwindCSS
* Radix Vue
* md-editor-v3
* vue-virtual-scroller

### 核心 (core-sdk)

* 纯 JavaScript (ESM)
* EventEmitter3
* @microsoft/fetch-event-source

## 快速开始

`Simple AI Chat` 提供了两种使用方式：作为**最终用户**在您的项目中集成，或作为**贡献者**在本地进行开发。

### 1\. 部署与集成 (终端用户)

此流程适用于希望将 AI 聊天功能**集成到现有应用**的开发者。

**步骤 A: 部署后端服务 (Docker)**

1.  从本仓库的 [Release 页面](https://github.com/CommentOut64/simple-ai-chat/releases)下载最新的后端部署包（或克隆仓库）。

2.  在 `docker-compose.yml` 所在目录 创建 `.env` 文件（可参考 `.env.example`），并填入您的 AI API 密钥。

3.  运行 Docker Compose:

    ```bash
    docker-compose up -d
    ```

4.  后端服务现已在 `http://localhost:8000` (或您配置的端口) 运行。

**步骤 B: 在 Vue 3 项目中集成**

1.  安装 `core-sdk` 和 `vue-ui` 包 (推荐从 npm 安装):
    ```bash
    pnpm install @simple-ai-chat-project/core-sdk @simple-ai-chat-project/vue-ui pinia
    ```
2.  在您的 `main.js` 中配置 Pinia：
    ```javascript
    import { createApp } from 'vue'
    import { createPinia } from 'pinia'
    import App from './App.vue'
    
    const app = createApp(App)
    app.use(createPinia())
    app.mount('#app')
    ```
3.  在组件中使用：
    ```vue
    <script setup>
    import { ChatWindow } from '@simple-ai-chat-project/vue-ui';
    import '@simple-ai-chat-project/vue-ui/style';
    </script>
    
    <template>
      <div style="height: 600px; width: 100%;">
        <ChatWindow
          chat-height="600px"
          user-avatar="/avatar.png"
        />
      </div>
    </template>
    ```

**步骤 C: 在 React/Svelte/原生 JS 中集成**

1.  您只需安装 `core-sdk`：
    ```bash
    npm install @simple-ai-chat-project/core-sdk
    ```
2.  使用 `core-sdk` 提供的 API 来管理您的自定义聊天界面。

### 2\. 本地开发与贡献 (贡献者)

此流程适用于希望**修改源码、贡献功能**的开发者。

1.  **克隆仓库并安装依赖**

    ```bash
    git clone https://github.com/CommentOut64/simple-ai-chat.git
    cd simple-ai-chat

    # 在根目录安装所有依赖
    pnpm install
    ```

2.  **运行后端开发服务器 (FastAPI)**

      * 打开**第一个**终端。
      * (首次) 配置 Python 虚拟环境并安装 `requirements.txt`。

    ```bash
    cd backend
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    pip install -r requirements.txt
    
    # 启动服务 (带热重载)
    uvicorn app.main:app --reload --port 8000 main:app --reload --port 8000
    ```
    
3.  **运行前端开发服务器 (Vue UI)**

      * 打开**第二个**终端。
      * 在**根目录**运行 `vue-ui` 的开发脚本：

    ```bash
    pnpm --filter vue-ui dev
    # pnpm 会自动找到 vue-ui 包并执行其 dev 脚本
    ```
    
4.  **访问**

      * 在浏览器中打开 Vite 提供的地址 (通常是 `http://localhost:5173`)。
      * 前端页面将自动与 `http://localhost:8000` 上的后端服务通信。

**提示：详细的api说明请参考[api文档](docs/api)**

## 适用场景

* **个人博客/网站**：集成智能助手，提升用户交互。
* **企业官网**：作为产品咨询机器人，解答常见问题。
* **在线教育平台**：作为 AI 答疑助手，提供 24/7 支持。
* **开发者工具**：集成代码助手、API 调试等功能。
* **内部管理系统**：用于知识库问答、数据查询助手。

## v1.0.0 版本说明：关于 Web Component

在原始设计中，将整个聊天系统封装为标准 Web Component（Web 组件）是一个核心亮点，旨在实现跨框架（React, Angular, Svelte, 纯 JS）的极致可移植性。

然而，由于技术实现上的挑战，**v1.0.0 版本暂未提供 `web-component` 包**。

**v1.0.0 包含以下内容：**

1.  **`packages/core-sdk`**：框架无关的核心 SDK。
2.  **`packages/vue-ui`**：基于 Vue 3 的纯粹 UI 组件库。
3.  **`backend/`**：基于 FastAPI 的后端服务（附带 Docker Compose 配置）。

对于 Vue 3 技术栈的开发者，您可以立即使用 `vue-ui` 和 `core-sdk` 构建应用。对于其他框架，您可以使用 `core-sdk` 并自行构建 UI。

提供稳定、高质量的 Web Component 封装依然是项目的高优先级目标，它将在未来的版本中发布。

## 路线图

* [ ] **Web Component 封装 (高优先级)**：发布跨框架的 `web-component` 包。
* [ ] **RAG 集成**：预留 LangChain 和 ChromaDB 接口，支持检索增强生成。
* [ ] **国际化 (i18n)**：支持多语言切换。
* [ ] **性能优化**：进一步优化性能。
* [ ] **插件系统**：支持更灵活的功能扩展（如语音识别、文件解析）。
* [ ] **权限系统**：集成用户认证与授权。

## 贡献

欢迎提交 PRs 和 Issues。

## 许可证

本项目基于 [MIT License](LICENSE) 授权。
