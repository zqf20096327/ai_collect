# 🏭 工业维护知识库 AI Demo

## 基于 RAG（检索增强生成）的智能问答系统

一个最小可运行（MVP）级的工业设备维护知识库 AI 演示项目，采用 **RAG (Retrieval-Augmented Generation)** 技术，让大语言模型基于你的私有文档进行精准问答。

![Tech Stack](https://img.shields.io/badge/React-18-61dafb?style=flat-square&logo=react)
![Tech Stack](https://img.shields.io/badge/FastAPI-0.109-009688?style=flat-square&logo=fastapi)
![Tech Stack](https://img.shields.io/badge/ChromaDB-0.4-orange?style=flat-square)
![Tech Stack](https://img.shields.io/badge/LangChain-0.1-green?style=flat-square)
![Tech Stack](https://img.shields.io/badge/Qwen-API-blue?style=flat-square)

![工业维护知识库智能问答系统](frontend/工业维护知识库智能问答系统-RAG-Demo.png)

---

## 🎯 RAG 工作原理

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   PDF 文档   │ -> │  文本分块   │ -> │  向量化存储  │ -> │  ChromaDB   │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
                                                                │
┌─────────────┐    ┌─────────────┐    ┌─────────────┐           │
│   用户提问   │ -> │  语义检索   │ <- │  相似度匹配  │ <─────────┘
└─────────────┘    └─────────────┘    └─────────────┘
                          │
                          v
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   AI 回答   │ <- │   LLM 生成  │ <- │ 上下文 + 问题│
└─────────────┘    └─────────────┘    └─────────────┘
```

---

## ✨ 功能特性

- 📄 **PDF 文档处理** - 上传设备手册、维护指南等 PDF 文档，自动分块和向量化
- 🔍 **语义检索** - 基于向量相似度的智能检索，找到最相关的文档片段
- 🤖 **多模型支持** - Qwen（推荐）/ OpenAI / DeepSeek / Ollama 本地模型
- 💬 **现代 Chat UI** - 工业风格深色主题界面，支持 Markdown 渲染
- 📊 **来源追溯** - 显示回答的参考来源、页码和相关度评分
- 🚀 **国内直连** - Qwen API 无需代理，开箱即用

---

## 🛠️ 技术栈

### 前端
| 技术 | 说明 |
|------|------|
| **React 18** | 现代前端框架 |
| **Vite** | 快速构建工具 |
| **Lucide React** | 图标库 |
| **React Markdown** | Markdown 渲染 |

### 后端
| 技术 | 说明 |
|------|------|
| **FastAPI** | 高性能 Python Web 框架 |
| **Pydantic** | 数据验证 |
| **LangChain** | PDF 加载和文本分块 |
| **Requests** | HTTP API 调用 |

### RAG 核心
| 技术 | 说明 |
|------|------|
| **ChromaDB** | 向量数据库（本地持久化） |
| **Qwen Embedding API** | 文本向量化（阿里云） |
| **Qwen LLM API** | 大语言模型（阿里云） |

### 支持的 LLM
| 提供商 | 模型 | 网络需求 |
|--------|------|---------|
| **Qwen 通义千问** | qwen-plus | 国内直连 ✅ |
| **DeepSeek** | deepseek-chat | 国内直连 ✅ |
| **OpenAI** | gpt-3.5-turbo | 需要代理 |
| **Ollama** | llama2 等 | 完全离线 ✅ |

---

## 🏗️ 项目结构

```
industrial_agent_mini_demo/
├── backend/
│   ├── main.py              # FastAPI 主入口
│   ├── rag_pipeline.py      # RAG 核心逻辑（检索+生成）
│   ├── config.py            # 配置管理
│   ├── env_template.env     # 环境变量 ⚠️ 需配置 API Key
│   └── requirements.txt     # Python 依赖
├── frontend/
│   ├── src/
│   │   ├── App.jsx          # 主应用（Chat UI）
│   │   ├── App.css          # 应用样式
│   │   ├── index.css        # 全局样式（工业风主题）
│   │   └── main.jsx         # 入口文件
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
├── start_backend.bat/.sh    # 一键启动脚本
├── start_frontend.bat/.sh
└── README.md
```

---

## 🚀 快速开始

### 1. 环境准备

- **Conda** (Anaconda / Miniconda) - Python 环境管理
- **Node.js** - 前端运行环境（通过 conda 安装，无需单独下载）
- (可选) Ollama - 用于本地模型

### 2. 创建 Conda 环境

打开 **Anaconda Prompt**，执行：

```bash
# 创建虚拟环境
conda create -n agent_mini_demo python=3.10 -y

# 激活环境
conda activate agent_mini_demo

# 安装 Node.js (前端需要)
conda install -c conda-forge nodejs -y
```

### 3. 配置 API Key

编辑 `backend/env_template.env` 文件，填写你的 API Key：

```env
# 默认使用 Qwen (通义千问) - 国内直连，无需代理
LLM_PROVIDER=qwen
QWEN_API_KEY=sk-你的API密钥    # ⚠️ 替换为真实的 API Key
```

> 获取 Qwen API Key: https://bailian.console.aliyun.com/cn-beijing/?tab=model#/api-key

### 4. 启动后端

在 **Anaconda Prompt** 中执行（确保已激活 `agent_mini_demo` 环境）：

```bash
# 进入后端目录
cd E:\你的项目路径\industrial_agent_mini_demo\backend

# 安装 Python 依赖
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 启动后端服务
python main.py
```

✅ 后端启动成功后访问：http://localhost:8000/docs

### 5. 启动前端

**新开一个 Anaconda Prompt 窗口**，执行：

```bash
# 激活环境
conda activate agent_mini_demo

# 进入前端目录
cd E:\你的项目路径\industrial_agent_mini_demo\frontend

# 安装依赖 (首次运行)
npm install

# 启动前端
npm run dev
```

✅ 前端启动成功后访问：http://localhost:3000

---

## 📖 使用说明

1. **上传文档**: 点击顶部「上传文档」按钮，选择 PDF 文件
2. **提问**: 在底部输入框输入问题，按回车或点击发送
3. **查看来源**: AI 回答下方会显示参考来源和相关度
4. **清空知识库**: 点击垃圾桶图标清空所有已导入的文档

---

## 🔧 LLM 配置选项

在 `backend/env_template.env` 中修改 `LLM_PROVIDER` 切换模型：

### Qwen 通义千问 (默认推荐)

```env
LLM_PROVIDER=qwen
QWEN_API_KEY=sk-xxx
QWEN_MODEL=qwen-plus
```

> 获取 API Key: https://dashscope.console.aliyun.com/

### DeepSeek

```env
LLM_PROVIDER=deepseek
DEEPSEEK_API_KEY=sk-xxx
DEEPSEEK_MODEL=deepseek-chat
```

### OpenAI

```env
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-xxx
OPENAI_MODEL=gpt-3.5-turbo
```

### 本地模型 (Ollama)

```bash
# 首先安装并启动 Ollama
ollama pull llama2
```

```env
LLM_PROVIDER=local
LOCAL_MODEL=llama2
```

---

## 🔌 API 接口

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/` | 服务状态 |
| GET | `/health` | 健康检查 |
| POST | `/upload` | 上传 PDF 文件 |
| POST | `/query` | RAG 问答 |
| GET | `/stats` | 知识库统计 |
| DELETE | `/clear` | 清空知识库 |
| GET | `/files` | 列出已上传文件 |

### 示例请求

```bash
# 问答
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"question": "如何进行日常维护检查?"}'

# 上传文件
curl -X POST http://localhost:8000/upload \
  -F "file=@设备手册.pdf"
```

---

## 📝 开发说明

- 知识库数据存储在 `backend/chroma_db/` 目录
- 上传的 PDF 文件保存在 `backend/uploads/` 目录
- 环境配置文件：`backend/env_template.env`
- 前端开发时会自动代理 API 请求到后端

---

## ❓ 常见问题

### Q: 提示 "QWEN_API_KEY 未设置"
A: 编辑 `backend/env_template.env`，填写正确的 API Key（不要加引号）

### Q: npm not found
A: 在 conda 环境中安装 Node.js：`conda install -c conda-forge nodejs -y`

### Q: 上传 PDF 后报错
A: 确保在正确的 conda 环境中运行后端：`conda activate agent_mini_demo`

---

## 📜 License

MIT License
