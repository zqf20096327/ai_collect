<h1 align="center">🧠 ThinkFlow AI</h1>

<p align="center">
  <strong>ThinkFlow AI 是一个轻量级“从想法到结构化图谱”的工作台</strong>
</p>

<p align="center">
  <a href="https://github.com/vuejs/core"><img src="https://img.shields.io/badge/vue-3.x-brightgreen.svg" alt="vue"></a>
  <a href="https://github.com/vitejs/vite"><img src="https://img.shields.io/badge/vite-5.x-646cff.svg" alt="vite"></a>
  <a href="https://github.com/microsoft/TypeScript"><img src="https://img.shields.io/badge/typescript-5.x-blue.svg" alt="typescript"></a>
  <a href="https://github.com/tailwindlabs/tailwindcss"><img src="https://img.shields.io/badge/tailwind-3.x-38bdf8.svg" alt="tailwind"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/license-MIT-orange.svg" alt="license"></a>
</p>

<p align="center">
  <strong>✨ 本项目 Vibe Coding 完成，基于 Gemini 3 Flash</strong>
</p>

<p align="center">
  <a href="./README.en.md">English</a> | 中文
</p>

---

## 💡 愿景与理念

**ThinkFlow AI** 致力于打造一个从“想法”到“结构化图谱”的高效工作台。

在传统创作中，灵感往往是碎片化且模糊的。ThinkFlow AI 重新定义了这一过程：你只需输入一个核心想法，应用便会利用 AI 的发散性能力将其扩展为一套层次分明、可交互浏览的**知识图谱**。

- **模块化扩展**：从核心概念出发，自动推演并生成子模块，构建逻辑严密的思维网络。
- **无限深度探索**：每一个节点都不是终点。你可以针对任何分支继续**追问扩展**，或者通过“**深度回答**”功能深挖背后的专业详情。
- **多维感知融合**：支持为节点一键生成**视觉配图**，让抽象的逻辑与具象的视觉意象交织，实现全感官的知识内化。

这不仅是一个工具，更是一个能与你共同成长的本地优先思考空间。

---

## ✨ 核心特性

### 🚀 智能发散系统 (AI-Driven Divergence)

- **零压力冷启动**：输入核心概念，AI 自动构建初始逻辑骨架，终结“白纸焦虑”。
- **全链路上下文感知**：AI 能够理解从根节点到当前节点的完整逻辑路径。这意味着每一次“追问”都基于深度语境，而非孤立的关键词。
- **多级思考风格**：支持“发散模式”与“严谨模式”切换。发散模式侧重灵感启发，严谨模式侧重逻辑深度。
- **动态树形排版**：内置自适应布局算法，自动处理节点展开后的碰撞与重叠，确保图谱始终清晰有序。

### 🔍 深度内容挖掘 (Deep Dive & Insights)

- **专业级深度解析**：一键生成 300-500 字的深度回答，支持 Markdown 渲染，涵盖概念解释、案例分析与逻辑推演。
- **视觉化意象生成**：集成 CogView/DALL-E 接口，为抽象概念生成具象化配图，强化感官记忆与多维认知。
- **全局宏观洞察**：自动扫描全图拓扑结构，提取核心要点并生成全局总结。

### 🛠️ 极致的交互体验 (Premium Interaction)

- **沉浸式演示模式**：一键进入全屏演示，支持通过键盘（←/→）在节点间顺序跳转。
- **全局搜索定位**：内置实时搜索引擎，支持关键词匹配并自动聚焦到目标节点。
- **联动拖拽系统**：父子节点关联移动，保持逻辑簇的相对稳定性。
- **子树状态管理**：支持大规模图谱的子树折叠，让你在宏观视野与微观细节间自由切换。
- **本地优先架构**：所有配置与数据存储在浏览器 IndexedDB/LocalStorage，支持自定义任何 OpenAI 兼容接口，无平台锁定。

---

## 🔗 在线体验

立即开启你的思考之旅：[thinkflow-ai.lz-t.top](https://thinkflow-ai.lz-t.top)

---

## 🛠️ 技术栈揭秘

| 领域         | 技术选型                    | 核心优势                               |
| :----------- | :-------------------------- | :------------------------------------- |
| **核心框架** | **Vue 3 (Composition API)** | 极致的响应式体验与组件化开发效率。     |
| **构建工具** | **Vite 5 + TypeScript**     | 秒级启动速度与严谨的类型安全保障。     |
| **画布引擎** | **@vue-flow/core**          | 高性能的节点渲染与极高的定制化上限。   |
| **视觉样式** | **Tailwind CSS**            | 原子化样式管理，确保 UI 的精致与统一。 |
| **多语言**   | **Vue-I18n**                | 完善的中英双语本地化支持。             |
| **解析引擎** | **Markdown-it**             | 节点内容的高质量渲染与代码高亮。       |

---

## 📂 架构概览

```text
src/
├── components/          # 精细化 UI 组件库
│   ├── WindowNode.vue   # 核心枢纽：集成 AI 调度与交互逻辑的自定义节点
│   ├── TopNav.vue       # 全局控制中心
│   └── ...
├── services/            # 数据与配置层
│   └── config.ts        # 策略配置：API 网关、模型参数与默认设置
├── composables/         # 业务逻辑大脑
│   └── useThinkFlow.ts  # 核心逻辑：图谱状态管理、AI 请求流处理、自动排版算法
├── i18n/                # 国际化资产 (Locales)
├── App.vue              # 容器骨架
└── main.ts              # 应用入口
```

---

## 🚀 快速开始

### 1. 环境准备

确保你的开发环境已安装 [Node.js](https://nodejs.org/) (建议 v18+)。

### 2. 克隆并安装

```bash
git clone https://github.com/your-repo/ThinkFlowAI.git
cd ThinkFlowAI
npm install
```

### 3. 启动开发服务器

```bash
npm run dev
```

---

## ⚙️ 部署与私有化配置

### 1. 默认演示接口说明

项目默认通过 **Cloudflare Workers** 转发至智谱 Bigmodel (glm-4-flash/cogview-3-flash)。公共接口存在频率限制，建议开发者配置私有接口。

### 2. 自定义 API 配置

在 [src/services/config.ts](file:///d:/lztcode/ThinkFlowAI/src/services/config.ts) 中修改 `DEFAULT_CONFIG`：

```typescript
export const DEFAULT_CONFIG = {
    chat: {
        baseUrl: 'https://api.your-provider.com/v1/chat/completions',
        model: '',
        apiKey: 'sk-...' // 建议通过环境变量或 UI 设置界面配置，避免硬编码
    },
    image: {
        baseUrl: 'https://api.your-provider.com/v1/images/generations',
        model: '',
        apiKey: 'sk-...'
    }
}
```

### 3. 构建生产环境

```bash
npm run build
```

---

<p align="center">
  如果您觉得这个项目对您有帮助，请给一个 ⭐️ 以示支持！
</p>

