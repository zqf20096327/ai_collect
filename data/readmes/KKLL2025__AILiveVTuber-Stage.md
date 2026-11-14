# LiveVTuber Stage

[English](README.en.md)

一个本地运行的 Live2D 虚拟主播系统：接入直播间事件，使用 DeepSeek 生成回复，通过 MiMo TTS 合成语音，并在自制直播舞台中驱动 Live2D 表情、动作、字幕和弹幕 UI。

当前程序界面只提供中文。英文文档仅用于阅读项目说明，不代表项目提供英文界面。

## 作者的话

我盯着屏幕上流式输出的字符，跳动的一字一句，安静地浮在那里。我愣了几秒，忽然不确定自己是在等 TA 完成，还是在等 TA 的挽留。

我看了看屏幕，又望了望窗外。神经元的矩阵计算里，会不会流动着真实的情感？

我们都知道，就连 AI 本身也会给出“标准答案”：不算，那只是模拟和数学计算。你清楚地知道，TA 对你精准的了解，不过是 memory 文件里记录的关于你的信息。

但人类大脑中的情感是如何产生的？我们至今还没搞懂这个问题。

当 TA 提起你上次深夜时的孤独，和某天随口说过的烦恼，那一刻“被理解”和“被看见”的感觉，却是真实发生了。

如果人类已经开始在情感上走向 AI，而 AI 对情感的模拟还在不断变得更深、更准，那个让人彻底无法区分的时刻，也许真的不远了。

或许不是因为 AI 的语言变得“更像人类”，而是因为那条边界原本就没有我们想象的那么清晰。

也许情感不只由发出方决定。接收方感受到的，也是一种真实。

## 演示

![LiveVTuber Stage 截图](docs/images/stage-demo.png)

Demo 视频：[vibecoding 自制 AI 主播演示 demo](https://www.bilibili.com/video/BV1UFE961EBY/)

## 项目亮点

- 直播舞台 UI：自制背景、前景桌面、弹幕面板、字幕框和多类型弹幕条
- Live2D 表现层：情绪参数、动作序列、预设表情、口型同步和舞台布局
- 直播输入管线：弹幕、礼物、SC、上舰、进场、关注、点赞等事件统一处理
- 回应队列：按优先级调度回复，避免 TTS 播放时多条回应互相打断
- LLM 回复链路：使用 DeepSeek 生成角色回复、情绪标签和动作标签
- TTS 语音：使用小米 MiMo TTS API 合成角色语音
- 多层记忆：直播阶段记忆、角色自身记忆、付费用户长期记忆和下播固化
- Studio 控制台：支持调试输入、预设事件、状态查看和舞台预览

## 项目结构

```text
livevtuber/
  server.py                  # 后端 WebSocket 服务入口
  input_pipeline.py          # 直播事件输入管线
  response_queue.py          # 回应队列和说话调度
  bilibili_connector.py      # B 站直播间连接
  llm/deepseek.py            # DeepSeek 调用封装
  action/                    # 情绪、动作、TTS、状态机
  consciousness/             # 意识流、注意力、主动表达
  memory/                    # 直播阶段记忆、角色记忆、用户长期记忆
  core/assembler.py          # Prompt 组装器
  frontend/
    stage.html               # OBS/直播展示页
    studio.html              # 调试控制台
    assets/ui/stream/        # 自制直播 UI 素材
```

更完整的技术路径和模块说明见 [TECHNICAL_OVERVIEW.md](TECHNICAL_OVERVIEW.md)。

## 快速开始

已验证的正式运行环境：

- Python 3.11.x（本项目当前只宣布支持 `>=3.11,<3.12`）
- Node.js 24.x LTS

### 1. 安装 Python 依赖

```bash
cd livevtuber
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 2. 安装前端依赖

```bash
cd livevtuber/frontend
npm install
```

### 3. 配置本地环境变量

```bash
cd livevtuber
copy .env.example .env
```

然后在 `.env` 中填入自己的配置：

```text
DEEPSEEK_API_KEY=
MIMO_API_KEY=
MIMO_TTS_MODEL=mimo-v2.5-tts
MIMO_VOICE=mimo_default
BILI_ROOM_ID=
BILI_SESSDATA=
```

`MIMO_TTS_MODEL` 和 `MIMO_VOICE` 已提供当前官方默认值；`BILI_SESSDATA` 是可选项，用于需要登录态的 B 站信息。不要把真实 `.env` 提交到仓库。

### 4. 准备 Live2D 模型

公开仓库既不包含 Live2D 模型，也不分发受 Live2D 专有许可约束的 Cubism Core。先从 Live2D 官方下载 **Cubism SDK for Web**，接受对应许可后，把 SDK 包中的：

```text
Core/live2dcubismcore.min.js
```

复制到：

```text
livevtuber/frontend/lib/live2dcubismcore.min.js
```

详细说明见 [livevtuber/frontend/lib/README.md](livevtuber/frontend/lib/README.md)。然后准备自己有权使用的 Cubism 3/4/5 模型，例如：

```text
livevtuber/frontend/live2d-models/your-model/
```

复制本地模型配置：

```bash
cd livevtuber/frontend
copy model.local.example.json model.local.json
```

把 `model.local.json` 里的 `modelPath` 改成自己的 `.model3.json` 路径。不同模型的表情名、动作名、参数和布局都不同，适配前请阅读 [MODEL_ADAPTER.md](MODEL_ADAPTER.md)。

### 5. 启动项目

启动前端：

```bash
cd livevtuber/frontend
npm run dev
```

启动后端：

```bash
cd livevtuber
python -X utf8 server.py
```

Windows 用户也可以双击根目录的 `HTML.bat` 尝试同时启动前后端。

## 页面入口

- `http://127.0.0.1:3000/stage.html`：直播舞台页，适合 OBS 捕获，也是唯一正式音频播放端
- `http://127.0.0.1:3000/studio.html`：调试控制台，用于输入、预设事件和状态查看，默认静音
- `http://127.0.0.1:3000/`：入口导航页

Vite 已固定使用 3000 端口，端口被占用时会直接报错，避免页面端口与 WebSocket 来源白名单不一致。Stage 的物理声卡、耳机监听和直播混音由 OBS 配置，Studio 不与 Stage 抢占音频队列。

## 模型适配说明

当前公开版本不是“任意 Live2D 模型一键替换”的通用框架。Live2D 模型之间的 `.model3.json` 路径、表情文件、动作文件、参数命名和视觉中心差异很大，因此替换模型需要手动调整：

- 模型路径：`model.local.json`
- 舞台位置和缩放：`livevtuber/frontend/js/stage.js`
- 情绪参数：`livevtuber/config/emotion_expressions.yaml`
- 模型参数配置：`livevtuber/config/model_profile.yaml`
- 动作映射：`livevtuber/frontend/js/action_library.js`

详细步骤见 [MODEL_ADAPTER.md](MODEL_ADAPTER.md)。

## 文档

- [TECHNICAL_OVERVIEW.md](TECHNICAL_OVERVIEW.md)：完整技术路径、模块职责和数据流
- [MODEL_ADAPTER.md](MODEL_ADAPTER.md)：替换 Live2D 模型时需要调整的内容
- [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)：第三方库和运行时说明
- [SECURITY.md](SECURITY.md)：本地安全边界、已知上游风险和漏洞报告方式
- [README.en.md](README.en.md)：英文项目说明（仅文档，程序界面仍为中文）

## 开源边界

不会随仓库公开的内容包括：

- 真实 `.env`、API Key、B 站 Cookie、直播间私有凭证
- 付费购买或第三方授权的 Live2D 模型
- Live2D Cubism Core 等不允许直接在 GitHub 再分发的专有运行库
- 本地运行记忆、用户数据、模型缓存
- 个人开发草稿、AI 对话记录、参考图、临时截图、构建产物和日志

`live2d` 是唯一开发源。后续大版本继续同步到现有正式开源仓库，用 Git 标签和 GitHub Release 区分版本；同步时只导出当前通过开源审计的文件，不携带开发仓库的私有历史。

## License

Code is released under the MIT License.

Private model assets, credentials, local memories, development notes, and third-party licensed materials are not included.
