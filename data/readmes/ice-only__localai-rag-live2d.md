# AI+2+RAG -- 二次元本地 RAG 聊天助手

基于量化千问 4B 模型 + 本地 RAG 文档检索 + Live2D 二次元形象的桌面 AI 伴侣。

![运行截图](screenshot.png)

## 特性

- **Live2D 二次元角色桌面显示**：透明无边框窗口，角色可拖动，支持触摸交互
- **本地 LLM 推理**：Qwen3.5-4B GGUF 量化模型，Vulkan GPU 加速，CPU 亦可流畅运行
- **RAG 本地文档检索**：扔文件进 `docs/` 目录自动索引，支持 txt / md / pdf
- **对话记忆持久化**：JSON 存储，多用户隔离，Token 预算自动裁剪
- **多平台适配**：桌面本地 + QQ OneBot v11，适配器模式可扩展
- **透明无边框桌面窗口**：PyQt5 置顶窗口，暗色主题，系统托盘控制
- **.env 配置驱动**：开箱即用，适配不同显卡

## 快速开始

### 环境要求

- Python 3.10+
- 内存 8GB+（推荐 16GB）
- 磁盘约 5GB（含 3.4GB 模型文件）

### 安装与运行

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 配置环境
cp .env.example .env
# 编辑 .env：纯 CPU 设 N_GPU_LAYERS=0；多显卡设 GGML_VK_VISIBLE_DEVICES=1

# 3. 下载模型
# 将 Qwen3.5-4B GGUF 文件放入 ai/ 目录（程序自动扫描）
# 模型安装方法{
    macOS:
        curl -LsSf https://llama.app/install.sh | sh
        llama serve -hf unsloth/Qwen3.5-4B-GGUF:UD-Q4_K_XL
        llama cli -hf unsloth/Qwen3.5-4B-GGUF:UD-Q4_K_XL
    windows:
        winget install llama.cpp
        llama serve -hf unsloth/Qwen3.5-4B-GGUF:UD-Q4_K_XL
        llama cli -hf unsloth/Qwen3.5-4B-GGUF:UD-Q4_K_XL
#}

# 4. 启动
python main.py
```

首次启动加载模型约 30 秒，后续运行模型常驻内存。

## 配置文件 (.env)

| 字段 | 说明 | 默认值 |
|------|------|--------|
| `N_CTX` | 上下文窗口大小 | 4096 |
| `N_THREADS` | CPU 推理线程数 | 8 |
| `N_GPU_LAYERS` | GPU 加速层数：-1=全部，0=纯 CPU，或指定数值 | -1 |
| `TEMPERATURE` | 生成温度 (0-1) | 0.7 |
| `GGML_VK_VISIBLE_DEVICES` | Vulkan GPU 选择：留空自动，0/1 指定显卡 | 1 |
| `WINDOW_WIDTH` | 窗口宽度 | 480 |
| `WINDOW_HEIGHT` | 窗口高度 | 520 |
| `ONEBOT_WS_URL` | QQ OneBot WebSocket 地址（可选） | ws://127.0.0.1:3001 |
| `ONEBOT_ACCESS_TOKEN` | QQ OneBot 鉴权 Token（可选） | 空 |

环境变量以 `AI_RAG_` 前缀的同名字段会覆盖 .env 中的值。

## 目录结构

```
ai+2+rag/
├── main.py                    # 入口
├── requirements.txt           # Python 依赖
├── .env.example               # 配置模板
├── src/
│   ├── ui/                    # PyQt5 前端
│   │   ├── app.py             # 应用启动与组装
│   │   ├── main_window.py     # 透明无边框主窗口
│   │   ├── live2d_widget.py   # Live2D 渲染（QWebEngineView）
│   │   ├── chat_widget.py     # 对话气泡叠加层
│   │   ├── input_widget.py    # 输入组件
│   │   └── tray.py            # 系统托盘
│   ├── core/
│   │   └── pipeline.py        # 核心流水线（消息调度中枢）
│   ├── model/
│   │   ├── loader.py          # GGUF 模型加载器
│   │   ├── inference.py       # 推理引擎（流式 / RAG 增强）
│   │   └── prompt.py          # 提示词管理
│   ├── memory/
│   │   ├── store.py           # JSON 记忆持久化
│   │   └── manager.py         # 记忆管理（历史 / Token 裁剪）
│   ├── adapters/
│   │   ├── base.py            # 适配器抽象基类
│   │   ├── desktop.py         # 桌面本地适配器
│   │   └── qq_adapter.py      # QQ OneBot v11 适配器
│   └── utils/
│       ├── config.py          # 配置中心（.env + 环境变量）
│       └── logger.py          # 日志
├── rag/
│   ├── system.py              # RAG 系统外观（组装入口）
│   ├── embedder.py            # 嵌入模型（BAAI/bge-small-zh-v1.5）
│   ├── indexer.py             # ChromaDB 索引管理
│   ├── retriever.py           # 语义检索
│   └── watcher.py             # watchdog 文件监控（自动索引）
├── live2d/                    # Live2D Cubism Web SDK + 角色资源
├── prompt/                    # 角色提示词模板
├── ai/                        # GGUF 模型存放目录
├── docs/                      # RAG 文档目录（拖入即索引）
├── chat_history/              # 对话历史持久化
└── note/                      # 开发笔记
```

## 架构说明

```
┌──────────────────────────────────────────┐
│              UI Layer (PyQt5)            │
│  MainWindow · Live2DWidget · ChatWidget  │
└──────────────────┬───────────────────────┘
                   │
┌──────────────────▼───────────────────────┐
│             Core Pipeline                │
│       message -> process -> reply        │
│        (流式输出 · RAG增强 · 记忆存取)      │
└───┬────────────┬──────────────┬──────────┘
    │            │              │
┌───▼────┐ ┌─────▼──────┐ ┌───▼──────────┐
│ Model  │ │  Memory    │ │     RAG      │
│ Loader │ │  Manager   │ │   System     │
│Infer.. │ │  Store     │ │Embed/Index/  │
│Prompt  │ │            │ │Retrieve/Watch│
└───┬────┘ └─────┬──────┘ └───┬──────────┘
    │            │              │
    └────────────┼──────────────┘
                 │
┌────────────────▼────────────────────────┐
│            Adapter Layer                │
│  DesktopAdapter · QQAdapter · (自定义)   │
└─────────────────────────────────────────┘
```

- **UI 层**：PyQt5 透明无边框窗口 + QWebEngineView 渲染 Live2D，暗色 Fusion 主题，系统托盘常驻
- **Core 层**：Pipeline 是唯一入口，协调模型推理、记忆管理和 RAG 检索，支持流式输出
- **Model 层**：llama-cpp-python 加载 GGUF，Vulkan 后端加速，ChatML 格式对话
- **Memory 层**：JSON 文件存储，按 user_id + channel_id 隔离，基于 Token 预算自动裁剪
- **RAG 层**：sentence-transformers (bge-small-zh-v1.5) 嵌入 + ChromaDB 向量库 + watchdog 文件监听，文档增删自动同步
- **Adapter 层**：适配器模式，统一 `send_message` / `send_message_stream` 接口，桌面和 QQ 两端实现

## 技术栈

| 组件 | 技术 |
|------|------|
| 推理引擎 | llama-cpp-python (GGUF, Vulkan GPU) |
| GUI 框架 | PyQt5 + QWebEngineView |
| Live2D | Cubism Web SDK 2.1 |
| RAG 框架 | LangChain + ChromaDB |
| 嵌入模型 | sentence-transformers (BAAI/bge-small-zh-v1.5) |
| 文件监听 | watchdog |
| QQ 适配 | OneBot v11 (WebSocket) |
| 配置管理 | .env + 环境变量覆盖 |

## 使用

- [Qwen](https://huggingface.co/unsloth/Qwen3.5-4B-GGUF) -- 千问大语言模型量化版本
- [llama.cpp](https://github.com/ggerganov/llama.cpp) -- 高效本地推理框架
- [ChromaDB](https://www.trychroma.com/) -- 向量数据库
- [Live2D Cubism SDK](https://www.live2d.com/) -- 二次元角色渲染
- [BAAI/bge](https://huggingface.co/BAAI/bge-small-zh-v1.5) -- 中文嵌入模型
- [LangChain](https://www.langchain.com/) -- RAG 应用框架
- [PyQt5](https://www.riverbankcomputing.com/software/pyqt/) -- Python GUI 框架

##更新

#更多功能正在更新中

##其他
#大家如果愿意的话，可以关注一下这个拼豆网站https://pindousc.cn


