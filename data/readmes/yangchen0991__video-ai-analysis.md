# 🎬 视频AI分析 (lapian)

> **面向用户** — 产品介绍、快速开始、主要功能。  
> 开发者详见 [DEVELOPMENT_GUIDE.md](DEVELOPMENT_GUIDE.md) · 完整索引见 [PROJECT.md](PROJECT.md)

> **AI 辅助影视分析平台** — 上传视频，自动检测镜头切换，逐镜提取景别、运镜、构图、色彩、叙事等专业信息。
>
> 项目代号 **Claw** · 状态 v0.8 · 190+ 源文件 · 85 测试用例 · 前后端编译零错误

[![TypeScript](https://img.shields.io/badge/TypeScript-5.9-3178C6?logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![React](https://img.shields.io/badge/React-18-61DAFB?logo=react&logoColor=white)](https://react.dev/)
[![Vite](https://img.shields.io/badge/Vite-5-646CFF?logo=vite&logoColor=white)](https://vitejs.dev/)
[![Express](https://img.shields.io/badge/Express-4.22-000000?logo=express&logoColor=white)](https://expressjs.com/)
[![Node](https://img.shields.io/badge/Node-22-339933?logo=node.js&logoColor=white)](https://nodejs.org/)
[![Tailwind](https://img.shields.io/badge/Tailwind-3-06B6D4?logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)
[![MUI](https://img.shields.io/badge/MUI-5-007FFF?logo=mui&logoColor=white)](https://mui.com/)
[![Zustand](https://img.shields.io/badge/Zustand-4-433E38?logo=zustand&logoColor=white)](https://zustand.docs.pmnd.rs/)
[![Tests](https://img.shields.io/badge/tests-188%20passed-brightgreen)]()
[![License](https://img.shields.io/badge/license-AGPLv3-blue)](LICENSE)

---

## 目录

- [项目定位](#项目定位)
- [系统架构](#系统架构)
- [技术栈](#技术栈)
- [功能特性](#功能特性)
- [快速开始](#快速开始)
- [项目结构](#项目结构)
- [API 概览](#api-概览)
- [AI 分析体系](#ai-分析体系)
- [SSE 流式推送](#sse-流式推送)
- [安全设计](#安全设计)
- [设计系统](#设计系统)
- [测试策略](#测试策略)
- [文档导航](#文档导航)
- [开发工具](#开发工具)
- [许可证](#许可证)

---

## 项目定位

**视频AI分析** 是一个单用户本地 AI 辅助影视分析平台。上传视频后，系统自动检测镜头切换，对每个镜头进行多模态智能拆解，提取景别、运镜、构图、色彩、剪辑节奏、叙事结构等专业信息，生成结构化分镜分析报告。

### 核心价值

| 维度 | 说明 |
|------|------|
| 🎞️ **逐镜拆解** | Canvas 直方图差异检测 + 自适应阈值算法，精准定位每个镜头的时间码 |
| 🔬 **多维分析** | 5 种专业视角，从导演、摄影、剪辑、编剧到 AI 提示词反推 |
| 🤖 **AI 驱动** | 多模态大模型提供深度视频理解，适配器模式支持 6 个供应商自由切换 |
| 🏠 **本地优先** | 单用户本地应用，JSON 文件存储，零数据库依赖，数据完全自主可控 |
| 🔒 **安全第一** | Helmet + CORS 白名单 + 限流 + 路径穿越防护 + 文件上传校验 + 原子写入 |
| 🎨 **Liquid Glass** | Apple WWDC 2025 设计语言，三层玻璃材质叠加，深色/浅色双主题 |

### 目标用户

| 用户画像 | 核心需求 | 使用场景 |
|----------|----------|----------|
| 导演 / 摄影师 | 分析镜头语言、构图逻辑、运镜动机 | 项目筹备期拉片参考 |
| 剪辑师 | 理解剪辑节奏、镜头衔接逻辑、转场技巧 | 日常创作参考 |
| 影视学生 | 系统学习拉片方法、积累分析案例 | 高频学习工具 |
| 内容创作者 | 拆解爆款短视频、仿写脚本结构 | 内容策略分析 |
| AI 提示词工程师 | 反推视频生成参数、构建训练数据 | 提示词逆向工程 |

---

## 系统架构

```
┌───────────────────────────────────────────────────────────────────────┐
│                         视频AI分析 系统架构                             │
├───────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  ┌─────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐ │
│  │  首页    │  │  项目列表 │  │ 播放器   │  │ AI分析   │  │ 知识库   │ │
│  │  /       │  │ /projects│  │ /player  │  │  /ai     │  │/knowledge│ │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘ │
│       └──────────────┴──────────────┴──────┬──────┴──────────────┘     │
│                                            │                           │
│                              ┌─────────────┴─────────────┐             │
│                              │   React Router 6 (SPA)   │             │
│                              └─────────────┬─────────────┘             │
│                                            │                           │
│              ┌─────────────────────────────┼─────────────────────┐     │
│              │              Zustand Stores (7)                   │     │
│              │  projectStore │ playerStore │ analysisStore       │     │
│              │  shotStore │ settingsStore │ knowledgeStore       │     │
│              │  themeStore                                     │     │
│              └─────────────────────────────┬─────────────────────┘     │
│                                            │                           │
│  ┌─────────────────────────────────────────┼─────────────────────┐     │
│  │                       Express Server (port 3456)              │     │
│  │                                                               │     │
│  │  middleware/          routes/              services/          │     │
│  │  ├─ errorHandler     ├─ projects          ├─ projectService   │     │
│  │  ├─ requestLogger    ├─ video             ├─ videoService     │     │
│  │  ├─ videoRange       ├─ shots             ├─ shotService      │     │
│  │  └─ security (helmet, ├─ analysis         ├─ analysisService  │     │
│  │     cors, rate-limit) ├─ knowledge         ├─ knowledgeService │     │
│  │                        ├─ settings         ├─ settingsService  │     │
│  │                        └─ import           ├─ importService    │     │
│  │                                            ├─ screenshotSvc   │     │
│  │                                            └─ storage (JSON)  │     │
│  └──────────────┬──────────────────────────────────┬──────────────┘     │
│                 │                                  │                    │
│      ┌──────────┴──────┐                ┌──────────┴──────────┐        │
│      │  AI Provider    │                │   Data Layer        │        │
│      │  (适配器模式)    │                │                     │        │
│      │                 │                │  data/              │        │
│      │  Gemini ────────┤                │  ├─ projects/       │        │
│      │  GPT-4o ────────┤                │  │   └─ {id}.json   │        │
│      │  Claude ────────┤─── provider ──→│  ├─ screenshots/    │        │
│      │  Qwen ──────────┤   factory      │  ├─ exports/        │        │
│      │  DeepSeek ──────┤                │  └─ knowledge/      │        │
│      │  TokenDance ────┘                │                     │        │
│      └─────────────────┘                │  原子写入:           │        │
│                                          │  tmp → rename       │        │
│                                          └─────────────────────┘        │
└───────────────────────────────────────────────────────────────────────┘
```

---

## 技术栈

### 前端

| 技术 | 版本 | 用途 |
|------|------|------|
| React | 18.x | UI 框架，函数组件 + Hooks |
| TypeScript | 5.9 | 全量类型安全，前后端共享类型定义 |
| Vite | 5.x | 构建工具，HMR 热更新 |
| Tailwind CSS | 3.x | 原子化 CSS，Liquid Glass 主题 |
| MUI (Material UI) | 5.x | 组件库（Dialog、Snackbar、Tooltip 等） |
| Zustand | 4.x | 轻量状态管理，7 个独立 Store |
| React Router | 6.x | SPA 客户端路由 |
| Vitest | — | 单元测试 + 组件测试 |

### 后端

| 技术 | 版本 | 用途 |
|------|------|------|
| Node.js | 22.x | 运行时 |
| Express | 4.22 | HTTP 框架，路由 + 中间件 |
| TypeScript | 5.x | NodeNext 模块解析 |
| tsx | — | 开发热重载 |
| tsup | — | 生产构建打包 |
| helmet | — | 安全 HTTP 头 |
| express-rate-limit | — | 限流 (120 req/min) |
| compression | — | Gzip 压缩 |
| multer | — | 文件上传处理 |

### AI 层

| 供应商 | 模型 | 调用方式 | 适配器文件 |
|--------|------|----------|------------|
| Google Gemini | Gemini 3 Flash / 3.1 Flash Lite | `@google/generative-ai` SDK | `gemini.ts` |
| OpenAI | GPT-4o | `openai` SDK | `openai.ts` |
| Anthropic | Claude 3.5 Sonnet | `@anthropic-ai/sdk` | `claude.ts` |
| 阿里云 | Qwen3-VL Plus | REST API | `qwen.ts` |
| DeepSeek | DeepSeek VL2 | REST API | `deepseek.ts` |
| TokenDance | 词元跳动专有模型 | REST API + SSE 流解析 | `tokendance.ts` |

> **适配器模式**：所有供应商实现统一的 `AIProvider` 接口（定义于 `server/src/ai/types.ts`），通过 `providerFactory.ts` 工厂函数动态创建。新增供应商只需实现接口、注册即可，无需修改调用方代码。

### 存储

| 特性 | 实现 |
|------|------|
| 格式 | JSON 文件系统 |
| 位置 | `data/projects/` 按项目 ID 组织 |
| 写入策略 | 临时文件 + `fs.rename()`（原子写入） |
| 读取策略 | `StorageService` 抽象层，支持缓存失效 |
| 备份 | 导出/导入 JSON 文件 |

---

## 功能特性

### 核心模块

| 模块 | 路由 | 状态 | 描述 |
|------|------|------|------|
| 首页 | `/` | ✅ | 产品介绍、功能卡片、快速入口 |
| 拉片播放器 | `/player` | ✅ | 视频播放、分镜列表、时间轴导航、单帧预览、键盘快捷键 |
| AI 分析 | `/ai` | ✅ | 视频上传、视角/字段配置、SSE 流式分析、结果表格 |
| 项目列表 | `/projects` | ✅ | 创建/编辑/删除、搜索筛选、批量操作 |
| 知识库 | `/knowledge` | ✅ | 分类浏览、术语定义、搜索、导入导出 |
| 教程 | `/tutorial` | ✅ | 使用说明、功能引导 |
| 设置 | `/settings` | ✅ | AI 供应商配置、API 密钥管理、主题切换 |
| 关于 | `/about` | ✅ | 版本信息、技术栈展示 |

### 播放器特性

- 📹 **多格式支持** — HLS (.m3u8)、MP4 等主流视频格式
- 🎞️ **分镜导航** — 左侧分镜列表 + 底部时间轴缩略图，点击跳转
- 🖼️ **单帧预览** — Canvas 渲染当前帧，支持 HiDPI 适配
- ⌨️ **键盘快捷键** — 空格暂停、← → 逐帧进退、↑ ↓ 切换分镜
- ⏱️ **时间码显示** — SMPTE 标准时间码格式，帧精确
- 📊 **直方图分析** — 实时 RGB 直方图，辅助判断画面调性

### AI 分析特性

- 🔍 **镜头检测** — Canvas 直方图差异 + 自适应阈值，精准检测转场
- 🎯 **5 种分析视角** — 综合拉片 / 短视频爆款 / 电影感视听 / AI提示词 / 提示词反推
- 📡 **SSE 流式推送** — 心跳保活、超时重连、断线恢复
- 📋 **结构化输出** — 表格展示分析结果，支持排序和筛选
- 💾 **历史记录** — 本地持久化，随时回看

---

## 快速开始

### 前置要求

- **Node.js** ≥ 22.x
- **npm** ≥ 10.x
- 至少一个 AI 供应商的 API 密钥（Gemini / OpenAI / Claude / 通义千问 / DeepSeek / TokenDance）

### 安装与启动

```bash
# 1. 克隆仓库
git clone https://github.com/yangchen0991/video-ai-analysis.git
cd lapian

# 2. 安装依赖（monorepo，前后端统一安装）
npm install

# 3. 配置环境变量
cp .env.example .env
# 编辑 .env，填写至少一个 AI 供应商的 API 密钥

# 4. 启动开发服务器
npm run dev
```

打开浏览器访问 **http://localhost:5173**。

### 环境变量

```bash
# .env 文件示例（至少配置一个供应商）
GEMINI_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
QWEN_API_KEY=your_key_here
DEEPSEEK_API_KEY=your_key_here
TOKENDANCE_API_KEY=your_key_here
TOKENDANCE_BASE_URL=https://api.tokendance.ai

# SSE 访问控制（可选，留空则不校验）
SSE_ACCESS_TOKEN=

# 服务端口（可选，默认值如下）
SERVER_PORT=3456
CLIENT_PORT=5173
```

### 开发命令

```bash
npm run dev          # 并发启动前后端（推荐）
npm run dev:client   # 仅前端 (Vite, port 5173)
npm run dev:server   # 仅后端 (tsx, port 3456)
npm run build        # 生产构建
npm test             # 运行测试 (85 用例)
```

---

## 项目结构

```
lapian/
├── client/                          # 前端 SPA (React + Vite)
│   ├── src/
│   │   ├── components/              # UI 组件
│   │   │   ├── analysis/            #   AI 分析组件 (配置/进度/结果/行渲染)
│   │   │   ├── common/              #   通用组件 (确认框/空状态/拖拽区/加载)
│   │   │   ├── import/              #   导入组件 (CSV 列映射)
│   │   │   ├── knowledge/           #   知识库组件 (术语提示)
│   │   │   ├── layout/              #   布局组件 (侧边栏/顶栏/外壳)
│   │   │   ├── player/              #   播放器组件 (播放/控制/分镜/帧/单帧)
│   │   │   ├── projects/            #   项目组件 (项目卡片)
│   │   │   ├── settings/            #   设置组件 (供应商卡片)
│   │   │   └── shots/               #   分镜组件 (列表/卡片/详情/时间轴)
│   │   ├── pages/                   # 路由页面 (9 个)
│   │   ├── stores/                  # Zustand 状态管理 (7 个独立 Store)
│   │   ├── hooks/                   # 自定义 Hook (视频播放/SSE/分镜/键盘/帧捕获)
│   │   ├── utils/                   # 工具函数 (时间码/直方图/API/格式化/Canvas)
│   │   ├── styles/                  # 全局样式 + 主题定义
│   │   └── types/                   # 前端类型定义
│   ├── index.html
│   ├── vite.config.ts
│   ├── vitest.config.ts
│   ├── tailwind.config.ts
│   └── package.json
│
├── server/                          # 后端 API (Express + TypeScript)
│   ├── src/
│   │   ├── ai/                      # AI 适配器层
│   │   │   ├── types.ts             #   AIProvider 统一接口定义
│   │   │   ├── providerFactory.ts   #   工厂函数（根据供应商名创建适配器）
│   │   │   ├── prompts.ts           #   Prompt 模板（5 种视角）
│   │   │   ├── streamParser.ts      #   SSE 流解析器
│   │   │   ├── gemini.ts            #   Google Gemini 适配器
│   │   │   ├── openai.ts            #   OpenAI GPT-4o 适配器
│   │   │   ├── claude.ts            #   Anthropic Claude 适配器
│   │   │   ├── qwen.ts              #   阿里通义千问适配器
│   │   │   ├── deepseek.ts          #   DeepSeek 适配器
│   │   │   └── tokendance.ts        #   TokenDance 适配器
│   │   ├── routes/                  # API 路由 (7 个模块, 34 个端点)
│   │   ├── services/                # 业务服务层 (9 个服务)
│   │   ├── middleware/              # 中间件 (错误处理/日志/视频Range/安全)
│   │   ├── config/                  # 配置 (应用配置/Swagger)
│   │   ├── utils/                   # 工具函数 (时间码/直方图/CSV/文件/日志)
│   │   ├── types/                   # 后端类型定义
│   │   ├── app.ts                   # Express 应用入口
│   │   └── index.ts                 # 服务启动入口
│   ├── tsconfig.json
│   ├── vitest.config.ts
│   └── package.json
│
├── shared/                          # 前后端共享类型
│   └── types/
│       ├── index.ts                 # 共享类型定义
│       └── package.json
│
├── docs/                            # 项目文档
│   ├── API.md                       # API 接口参考 (34 个端点)
│   ├── SSE_PROTOCOL.md              # SSE 流式推送协议
│   ├── CHANGELOG.md                 # 版本变更日志
│   ├── class-diagram.mermaid        # 类图
│   ├── sequence-diagram.mermaid     # 时序图
│   └── adr/                         # 架构决策记录 (6 篇)
│       ├── 001-json-file-storage.md
│       ├── 002-ai-provider-adapter.md
│       ├── 003-sse-streaming.md
│       ├── 004-zustand-state-management.md
│       └── 005-shared-types-package.md
│
├── design-output/                   # 设计交付物
│   ├── DESIGN.md                    # Liquid Glass 完整设计令牌
│   └── brand-spec.md                # 品牌规范
│
├── data/                            # 本地数据 (JSON, git-ignored)
│   ├── projects/                    #   项目数据
│   ├── screenshots/                 #   截图
│   ├── exports/                     #   导出文件
│   └── knowledge/                   #   知识库
│
├── .env.example                     # 环境变量模板
├── .gitignore
├── package.json                     # Monorepo 根配置 (npm workspaces)
└── README.md                        # 本文件
```

---

## API 概览

基础路径：`http://localhost:3456/api` · 34 个端点 · 7 个路由模块

### 响应格式

```json
{
  "success": true,
  "data": { },
  "error": "错误描述（仅失败时）"
}
```

### 路由模块

| 模块 | 端点数 | 路径前缀 | 核心功能 |
|------|--------|----------|----------|
| 项目管理 | 5 | `/api/projects` | CRUD + 列表/搜索 |
| 视频管理 | 4 | `/api/video` | 上传/播放/信息/Range 请求 |
| 分镜管理 | 4 | `/api/projects/:projectId/shots` | 查询/更新/详情/列表 |
| AI 分析 | 5 | `/api/analysis` | 启动/状态/结果/流式/取消 |
| 知识库 | 5 | `/api/knowledge` | 条目 CRUD + 搜索/导入/导出 |
| 设置 | 4 | `/api/settings` | AI 配置 CRUD + 密钥管理 |
| 导入 | 4 | `/api/import` | CSV 解析/匹配/预览/确认 |

> 详见 [docs/API.md](docs/API.md)

---

## AI 分析体系

### 5 种分析视角

| 视角 | 键名 | 关注维度 | 典型输出字段 |
|------|------|----------|-------------|
| **综合拉片** | `default` | 画面内容、运镜、景别、剪辑节奏 | 景别、运镜方式、构图、画面内容、镜头时长 |
| **短视频爆款** | `short_video` | 黄金三秒、情绪价值、BGM、节奏感 | 开头吸引力、情绪调性、音乐节奏、转场速度 |
| **电影感/视听** | `cinematic` | 构图、光影、焦段、运镜动机、场面调度 | 构图分析、光源方向、焦段、运镜动机、色彩方案 |
| **AI 提示词** | `narrative` | 景别、运镜、AI 提示词、声音设计 | 景别、运镜、AI 图像提示词、音效建议 |
| **提示词反推** | `prompt_reverse` | 视觉构图、主体、动作、镜头动态 | 视觉构图(中英双语)、主体描述、动作与物理、镜头动态 |

### 适配器模式

所有 AI 供应商实现统一的 `AIProvider` 接口：

```typescript
interface AIProvider {
  name: string;
  analyze(params: AnalyzeParams): Promise<AsyncIterable<AnalysisEvent>>;
  validateConfig(config: AIProviderConfig): boolean;
}
```

通过 `providerFactory` 工厂函数按供应商名称动态创建实例。新增供应商只需：
1. 实现 `AIProvider` 接口
2. 在 `providerFactory.ts` 中注册
3. 无需修改任何调用方代码

### 分析流程

```
视频上传 → 镜头检测(直方图差异+自适应阈值) → 分镜提取 →
时间码校正 → 逐镜 AI 分析(SSE 流式推送) → 前端增量渲染 →
结构化报告 + 历史记录(本地 JSON)
```

### 可配置参数

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `temperature` | 0.7 | AI 生成随机性 (0-2) |
| `maxTokens` | 4096 | 单次响应最大 Token 数 |
| `shotThreshold` | 30 | 镜头检测灵敏度 (1-100) |
| `minShotDuration` | 1.0s | 最小镜头时长 |

所有参数均可在 Settings 页面中按供应商单独配置。

---

## SSE 流式推送

AI 分析通过 **Server-Sent Events** 实时推送到前端。

### 端点

```
GET /api/analysis/tasks/:taskId/stream
```

### 事件类型

| 事件 | 方向 | 说明 |
|------|------|------|
| `shot_start` | 服务端 → 客户端 | 开始分析某个镜头 |
| `analysis_chunk` | 服务端 → 客户端 | 分析结果增量数据 |
| `shot_complete` | 服务端 → 客户端 | 某个镜头分析完成 |
| `task_complete` | 服务端 → 客户端 | 全部镜头分析完成 |
| `error` | 服务端 → 客户端 | 分析出错 |
| `heartbeat` | 服务端 → 客户端 | 每 15 秒心跳保活 |

### 客户端连接

```typescript
// useSSE Hook 自动处理连接生命周期
const { data, isConnected, error } = useSSE({
  taskId: 'task-uuid',
  onShotComplete: (shot) => console.log('镜头分析完成', shot),
  onTaskComplete: () => console.log('全部完成'),
});
```

特性：心跳保活 (15s) · 超时重连 (指数退避) · 断线恢复 · Bearer/Token 双认证

> 详见 [docs/SSE_PROTOCOL.md](docs/SSE_PROTOCOL.md)

---

## 安全设计

| 层级 | 措施 | 说明 |
|------|------|------|
| HTTP 头 | helmet | 自动设置 CSP、HSTS、X-Frame-Options 等安全头 |
| 跨域 | CORS 白名单 | 仅允许配置的域名访问，非全开 |
| 限流 | express-rate-limit | 全局 120 req/min/IP |
| 路径安全 | 双重校验 | `path.basename` + `path.relative` + `startsWith('..')` 防穿越 |
| 文件上传 | Magic Bytes 检测 | 验证文件真实类型，扩展名白名单 |
| 密钥管理 | 环境变量 | API 密钥仅从 `process.env` 读取，磁盘脱敏存储 |
| 数据写入 | 原子写入 | 临时文件 + `fs.rename()`，防崩溃损坏 |
| 请求大小 | Body 限制 | JSON 10MB，urlencoded 10MB |
| 服务超时 | 30 分钟 | 适配 AI 长任务，避免过早断开 |
| 优雅关闭 | 信号处理 | SIGTERM/SIGINT/unhandledRejection/uncaughtException |

---

## 设计系统

### 设计语言

**Apple Liquid Glass (WWDC 2025)** — 三层材质叠加的玻璃拟态效果，深色/浅色双主题。

### 核心参数

| 参数 | 深色主题 | 浅色主题 |
|------|----------|----------|
| 背景色 | `#000000` | `#f5f5f7` |
| 玻璃面板透明度 | `0.04–0.12` | `0.5–0.7` |
| 模糊层级 | nav 25px / modal 20px / card 15px / btn 10px |
| 强调色 | `#3aa0ff` | `#007aff` |
| 圆角 | 24px（LG 标准圆角） |
| 按钮形状 | 药丸形 `9999px` |
| 标题字体 | Playfair Display |
| 正文字体 | Inter |

### CSS 变量体系

全部设计令牌通过 CSS 自定义属性实现，支持运行时主题切换：

```css
:root {
  --glass-opacity: 0.5;
  --glass-blur: 20px;
  --glass-saturate: 180%;
  --color-accent: #007aff;
  --radius-lg: 24px;
}
```

> 完整规范见 [design-output/DESIGN.md](design-output/DESIGN.md)

---

## 测试策略

| 层 | 框架 | 覆盖范围 | 用例数 |
|----|------|----------|--------|
| 前端 Store | Vitest | Zustand Store 单元测试 | 5 个测试文件 |
| 前端 Hook | Vitest | useSSE 连接管理 | 1 个测试文件 |
| 后端 Service | Vitest | 业务逻辑 + 数据存储 | 6 个测试文件 |
| 后端 AI | Vitest | SSE 流解析器 | 1 个测试文件 |
| 后端 Middleware | Vitest | 中间件行为测试 | 1 个测试文件 |

```bash
npm test                 # 运行全部测试
npm test -- --watch     # 监听模式
npm test -- --coverage  # 覆盖率报告
```

---

## 文档导航

| 文档 | 说明 |
|------|------|
| [docs/API.md](docs/API.md) | API 接口参考（34 个端点，完整请求/响应示例） |
| [docs/SSE_PROTOCOL.md](docs/SSE_PROTOCOL.md) | SSE 流式推送协议详解 |
| [docs/CHANGELOG.md](docs/CHANGELOG.md) | 版本变更日志 |
| [docs/adr/](docs/adr/) | 架构决策记录（6 篇 ADR） |
| [design-output/DESIGN.md](design-output/DESIGN.md) | Liquid Glass 完整设计令牌 |

---

## 开发工具

本项目使用 **[WorkBuddy](https://workbuddy.dev)** 作为 AI 辅助开发工具，支持：

- **多智能体协作** — 产品经理 → 架构师 → 工程师 → QA 的 SOP 流水线
- **代码审查** — 自动化质量检查 + 工程保障报告
- **文档生成** — API 文档、ADR、运维手册自动维护
- **测试策略** — 测试用例生成与覆盖率分析

---

## 许可证

本项目采用 **GNU Affero 通用公共许可证 v3.0 (AGPLv3)**。

```
视频AI分析 (lapian) — AI 辅助影视分析平台
Copyright (C) 2026  yangchen0991

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```

完整的许可证文本见 [LICENSE](LICENSE) 文件。

> **AGPLv3 的重要特征**：如果你修改了本软件并通过网络提供服务（包括 SaaS），你必须将修改后的完整源代码以 AGPLv3 协议公开。这确保了软件自由能够延伸到网络服务场景。

---

<p align="center">
  <sub>Built with ❤️ using WorkBuddy · Designed with Apple Liquid Glass · Licensed under AGPLv3</sub>
</p>
