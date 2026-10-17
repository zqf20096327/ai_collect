# 企业微信智能客服 (WeCom Auto Reply)

> 基于截图 RPA + PaddleOCR + RAG 知识库的企业微信 1 对 1 私聊自动回复系统。
> **不依赖企业微信 API，不需要企业管理员权限，开箱即用。**

## 它能做什么

- 🔴 自动检测未读消息（红点识别）
- 📸 截图 + OCR 提取客户消息（支持语音转文字）
- 🧠 RAG 知识库检索 + DeepSeek AI 生成回复
- ✅ 三级分流：自动发送 / 人工确认 / 人工处理
- 📦 一键打包为 Windows 可执行程序（~3GB，无需 Python 环境）

## 为什么不用企业微信 API

| 方案 | 需要 API 权限 | 需要企业审批 | 适用场景 |
|------|:---:|:---:|------|
| 企业微信官方客服 | ✅ | ✅ | 大中型企业 |
| 第三方 SCRM (微伴/尘锋等) | ✅ | ✅ | 中型企业 |
| **本项目 (截图 RPA)** | ❌ | ❌ | **小微企业 / 个人 / 无权限场景** |

## 技术栈

| 模块 | 选型 | 说明 |
|------|------|------|
| 截图 | mss | 内存级截图 |
| 红点检测 | PIL 像素扫描 | 左侧 5% 区域，R>90, G/B<130 |
| 文字提取 | **PaddleOCR** (PP-OCRv4) | 中文小字识别 |
| 气泡检测 | 蓝泡/灰泡/文字行 | 像素级颜色分析 |
| 知识库 | Qdrant + BGE Embedding | 本地文件模式，无需 Docker |
| AI 回复 | DeepSeek API | LLM 生成 + 质量门控（三态） |
| 键鼠控制 | pynput + ctypes Win32 API | 剪贴板操作 + 回车发送 |
| 配置管理 | config.json (100+ 参数) | 热更新支持 |

## 快速开始

### 方式一：直接运行（需要 Python 环境）

```bash
# 1. 安装依赖
pip install paddlepaddle paddleocr mss pynput pywin32 pillow numpy \
    qdrant-client sentence-transformers python-dotenv openai pyautogui

# 2. 配置
copy .env.example .env
# 编辑 .env: 填入 DEEPSEEK_API_KEY

# 3. 启动
python main.py
```

### 方式二：打包为可执行程序（免 Python 环境）

```bash
# 一键构建
python scripts/build.py

# 输出: dist/WeComBot/
# 分发: zip dist/WeComBot/ → 用户解压 → 编辑 .env → 双击 启动.bat
```

打包后的程序约 3GB（包含 PyTorch + PaddleOCR + BGE 模型），用户无需安装任何依赖。

## 架构

```
tkinter mainloop + root.after() 定时器:
  scan_tick (每 3 秒, 后台线程):
    1. Scanner   → 聚焦窗口 + 截图 col2
    2. Detector  → 红点检测 + 名字 OCR (@微信 判定)
    3. Scanner   → 点击客户 → 截图 col3 聊天区
    4. Detector  → 气泡扫描 (蓝泡阻断 / 灰泡 / 文字行)
    5. Detector  → PaddleOCR 提取文字
    6. Guard     → 消息去重 → 冷却检查
    7. Responder → RAG 检索 → DeepSeek 生成 → 质量门控
    8. 分流决策:
       ├─ auto_send    (cosine > 0.7 + guard pass) → 自动发送
       ├─ human_confirm (0.4 ≤ cosine ≤ 0.7)       → 弹窗确认
       └─ human_handle  (cosine < 0.4 或 guard block) → 人工处理
  _process_send_queue_tick (每 500ms, 主线程):
    9. 出队 → 切窗口 → ctypes 剪贴板 → Ctrl+V → Enter → 切回
```

## 模块结构

```
├── main.py                    # 协调器（tkinter mainloop + 定时器调度）
├── config.json                # 配置文件（100+ 参数）
├── config/manager.py          # ConfigManager（热更新）
├── wxbot/
│   ├── scanner.py             # 窗口管理 + 截图 + 点击
│   ├── detector/              # 检测器包（6 个独立模块）
│   │   ├── red_dot.py         #   红点检测
│   │   ├── bubble.py          #   蓝泡/灰泡/文字行检测
│   │   ├── name_region.py     #   名字区域 + 绿 badge
│   │   ├── customer_id.py     #   客户判定
│   │   ├── ocr_engine.py      #   PaddleOCR 封装
│   │   └── dedup.py           #   去重（图片/消息/冷却）
│   └── sender.py              # 剪贴板 (ctypes) + 发送
├── rag/
│   ├── responder.py           # 三级分流 + 发送 + 日志
│   ├── generator.py           # LLM 回复生成（多轮上下文 + 注入防御）
│   ├── guard.py               # 质量门控（三态: pass/block/low_risk）
│   ├── retriever.py           # Qdrant 检索
│   ├── embed_query.py         # BGE 嵌入（本地模型）
│   └── llm_client.py          # DeepSeek API 调用
├── pipeline/
│   ├── chat_importer.py       # 聊天记录解析（标准导出 + PC 端复制格式）
│   ├── chunker.py             # 文本分块
│   ├── embedder.py            # 向量化 + 存入 Qdrant
│   └── video_transcribe.py    # 视频转录（faster-whisper）
├── gui/main_window.py         # tkinter 主控窗口
├── notify/                    # Toast 通知 + 人工确认弹窗
├── eval/                      # 评估框架（20 条 QA + LLM 裁判）
├── scripts/build.py           # PyInstaller 一键构建
└── tests/                     # ~248 个测试（pytest）
```

## 知识库导入

将聊天记录或文档导入 RAG 知识库：

```bash
# 企业微信聊天记录（PC 端复制到 txt）
python -c "
import os; os.environ['HF_HUB_OFFLINE'] = '1'
from pipeline.run_pipeline import main
import sys; sys.argv = ['run_pipeline.py', '--chat-dir', '导出的聊天记录', '--skip-videos']
main()
"
```

支持两种聊天记录格式：
- **标准导出**：`YYYY-MM-DD HH:MM:SS 角色-姓名`
- **PC 端复制**：`姓名@微信@微信联系人 MM/DD HH:MM:SS`

## 操作

| 操作 | 方式 |
|------|------|
| 暂停/恢复 | 点击 UI 窗口 [暂停] 按钮 |
| 退出 | 点击 UI 窗口 [X]，程序自动终止 |
| 导出记录 | UI 窗口 [导出记录] 按钮 → CSV |
| 运行评估 | `python -m eval.run` → `logs/eval_report.txt` |
| 查看日志 | `logs/monitor.log` |

## 核心配置

所有参数通过 `config.json` 管理，支持热更新：

| 配置组 | 说明 |
|--------|------|
| `detection.red_dot` | 红点颜色阈值、扫描区域 |
| `detection.blue_bubble` | 蓝泡像素判定、高度限制 |
| `detection.gray_bubble` | 灰泡 RGB 范围、边缘阈值 |
| `detection.name_region` | 名字区域检测参数 |
| `crop` | 聊天区/名字行裁切比例 |
| `ocr` | OCR 引擎、关键词、停止词 |
| `ocr_confidence` | 名字/气泡/默认置信度 |
| `rag` | RAG 检索阈值、分流阈值 |
| `timing` | 各步骤延迟 |
| `dedup` | 缓存大小、冷却时间 |

## 已知限制

- 仅支持 1 对 1 私聊（群聊不触发回复）
- 企微窗口必须在前台可见
- 高 DPI 需要 `SetProcessDpiAwareness`
- 窗口尺寸变化后 col2 布局可能偏移

## 测试

```bash
# 日常开发（跳过 embedding 测试，避免 PyTorch DLL 冲突）
SKIP_EMBED_TESTS=1 python -m pytest tests/ -q

# 单独运行 embedding 测试
python -m pytest tests/test_video_qa.py -v
```

## License

MIT
