# PhraseSplice

### 用语言，把素材剪成作品。

**把想法说清楚，让 AI 帮你剪；时间线上的修改，能看、能改、能撤销。** PhraseSplice 是面向创作者的 AI 剪辑工作台，用日常语言编排素材、剪口播、加字幕、套模板，得到可以继续编辑的多轨工程。

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](COPYING)
[![Unit tests](https://github.com/John201-del/phrasesplice/actions/workflows/ci.yml/badge.svg)](https://github.com/John201-del/phrasesplice/actions/workflows/ci.yml)
![Windows preview](https://img.shields.io/badge/Windows-x64%20preview-2563eb)

[快速开始](#快速开始) · [可以这样说](#可以这样说) · [云端功能](#云端功能) · [功能与依赖](#功能与依赖) · [验证记录](docs/VALIDATION.md) · [English](README.en.md)

> **开发预览版，首先支持 Windows x64。** 手工剪辑不需要 AI 账号；语言助手可选择 Codex、兼容 API 或本地 Ollama，也能通过 MCP 让 WorkBuddy 控制剪辑。云端服务使用你自己的账号及额度，本地模型按需安装。

![PhraseSplice 实际界面：风景视频、多轨时间线与 AI 助手](docs/assets/localcut-desktop.jpg)

*PhraseSplice 实际工作界面：播放器显示瀑布素材，时间线与 AI 助手同时可见。[播放／下载有声 MP4 成片](docs/assets/localcut-demo.mp4) · [下载原始示例片段](examples/localcut-nature.mp4)，导入后即可体验。素材来源与许可见 [第三方说明](docs/THIRD_PARTY.md)。*

从旧版升级时，请另选安装目录。原有工程可以继续通过「文件 → 打开」使用。

## 为什么做 PhraseSplice

想剪一段视频，却不知道该点哪个按钮。PhraseSplice 把这个起点变成一句话：

```text
把这些视频按顺序接起来，保留原声。
第一个镜头在第 2 秒剪开，把后半段移到结尾。
字幕用白字黑边，放在底部。最后导出 MP4。
```

**导入素材 → 描述要求 → 检查时间线 → 导出作品。** 助手把修改落到可保存、可撤销、可继续编辑的原生工程里。先说出想法，再按预览调整，开始剪辑不必先记住一套按钮。

| 亮点 | 对使用者有什么用 |
| --- | --- |
| **自然语言指令 → 原生时间线** | 插入、分割、修剪、移动、字幕和效果调整落到实际片段上 |
| **AI 由你选择** | Codex、DeepSeek、通义千问、豆包火山方舟、Ollama 或自定义兼容接口；WorkBuddy 通过 MCP 接入 |
| **一批修改，一次撤销** | 编辑前核对工程状态；批量失败回滚，改错了可以退回 |
| **8 个内置剪辑模板** | 照片故事、产品展示、旅行章节、知识步骤、口播包装等，可套自己的素材 |
| **本地图片与视频处理** | 磨皮、小瑕疵修复、抠图换背景、人声分离、卡通头像跟脸，生成新文件 |
| **从照片开始创作** | 照片推拉运镜；可选照片＋语音口型视频；可选云端视频生成 |
| **从自动剪辑到手工精修** | 多轨时间线、关键帧、效果与渲染都保留，需要调整细节时可直接接手 |

## 快速开始

先使用 **Windows 11 x64、可写的英文目录**。本预览版的 MLT 运行路径暂不支持中文；不要求 D 盘。建议预留至少 3 GB 用于基础安装及下载缓存，可选模型另需数 GB。

```powershell
git clone https://github.com/John201-del/phrasesplice.git
cd phrasesplice
.\Start-PhraseSplice.cmd
```

也可以点 GitHub 的 **Code → Download ZIP**，解压到英文目录后双击 `Start-PhraseSplice.cmd`。

首次启动会下载固定版本的应用组件和官方依赖，逐一验证 SHA-256。需要能连接 GitHub、KDE 下载站。安装不会修改系统 PATH，不捆绑账号、个人工程或模型。普通使用**不用编译 C++，也不用安装 Python**。

1. 点击 **选择素材**，导入视频、音频或图片。第一次可以直接用仓库自带的 [风景实拍示例视频](examples/localcut-nature.mp4)。
2. 手工编辑可直接开始。要用语言控制，点 **连接 AI**，选择已有 Codex 登录、云端 API 或本地 Ollama；WorkBuddy 选择 MCP 外部控制。
3. 选择 Codex、兼容 API 或 Ollama 时，在助手输入框写要求；选择 WorkBuddy 时，在 WorkBuddy 中输入。先从“按顺序排列，保留原声”这样的小任务开始。
4. 查看时间线和预览，满意后点 **导出**。助手默认把工程和成片保存在 `runtime/userdata/projects` 与 `runtime/userdata/exports`。

不同 AI 的配置见 [AI 接入指南](docs/AI_PROVIDERS.md)。可选模型、目录说明和故障处理见 [使用指南](docs/QUICKSTART.md)。开发者见 [源码构建](docs/BUILD.md)。

## 可以这样说

**剪辑与包装**

```text
把素材库的视频依次放到时间线，保留原声。
把第一个视频在第 2 秒分成两段。
找出长静音，先告诉我准备删哪些位置。
字幕放大一些，白字黑边，放在底部。
```

**照片成片**：新建空时间线，导入至少 3 张照片。

```text
按我导入的顺序，用照片故事模板做 12 秒成片，
三段标题分别是“开场”“经过”“结尾”。
```

**修图与卡通跟脸**：先安装对应本地运行环境，导入所需素材。

```text
给这张照片做自然磨皮，保留五官细节，导出 PNG。
用这张卡通头像遮住视频里的脸，跟着移动，保留原声。
用内置立体青蛙头像遮脸，跟随转头和嘴部张合，保留原声。
用这张人像照片和这段语音生成口型同步的说话视频。
```

立体卡通是**立体风格的二维绘制与人脸跟踪**。照片推拉是运镜动画。照片说话另用本地数字人模型。三者的效果、耗时和输入要求不同，见 [功能边界](docs/QUICKSTART.md#功能边界)。

## 云端功能

| 功能 | 入口与服务 | 使用条件 |
| --- | --- | --- |
| **用语言剪辑** | **连接 AI** → Codex、DeepSeek、通义千问、豆包火山方舟或自定义兼容 API。也可以在 WorkBuddy 中通过 MCP 控制时间线 | Codex 使用自己的登录与额度。兼容 API 需要自己的 Key 和支持工具调用的模型。WorkBuddy 的账号与额度由其服务决定 |
| **文生视频** | **生成视频 → LTX**，输入提示词，生成约 4–8 秒的片段 | 使用 [Lightricks 公共 Space](https://huggingface.co/spaces/Lightricks/ltx-video-distilled) 的共享额度，无需 Key，可能排队或限流 |
| **文生视频、首帧图生视频** | **生成视频 → Seedance**，根据文字生成，也可添加一张首帧图 | 需要开通火山方舟相应模型并填写自己的 API Key，按服务计费 |
| **普通话配音** | 在助手中说“把这段文字生成普通话配音并导入”。每次最多 200 字 | 使用 [k2-fsa 公共 Space](https://huggingface.co/spaces/k2-fsa/text-to-speech)。共享服务的可用性与额度可能变化 |
| **在线素材** | 助手可在 Wikimedia Commons 搜索、下载并导入图片。原生在线资源面板可接入 Freesound、Pexels 和 Pixabay | Commons 搜索无需 Key。其他素材服务使用自己的凭据，下载后按素材许可保留署名 |

剪辑指令由选定的 AI 理解，时间线修改和导出在本机执行。免费公共视频通道失败后不会自动切换到付费接口。模板套用和照片口型同步分别使用内置模板和可选本地模型。详见 [AI 接入指南](docs/AI_PROVIDERS.md) 与 [验证范围](docs/VALIDATION.md)。

## 功能与依赖

| 能力 | 在哪里处理 | 需要什么 |
| --- | --- | --- |
| 原生手工剪辑、预览、导出 | 本机 | 基础运行包 |
| 语言助手、自动编排、模板套用 | 所选 AI 理解指令，本机执行编辑 | Codex、支持工具调用的兼容 API／Ollama，或 WorkBuddy MCP |
| 修图、降噪、抠像、人声分离 | 本机 | 可选 local-ai 运行环境；自然语言入口需配置助手 |
| 本地语音转字幕 | 本机 | 独立 Whisper 环境与模型；见使用指南 |
| 照片说话、立体卡通跟脸 | 本机 | 可选 local-avatar 环境与模型；CPU 会较慢 |

**隐私说明：** 指令、工程信息、转写文字和请求查看的缩略图可能发送给你选择的 AI。WorkBuddy 决定其所选模型的处理方式；Ollama 只有使用本地模型时才是本机推理。使用云配音/生成时，相关文字或图片会发送给所选服务。API Key 仅保留在本次程序会话内，不写入工程或仓库。

## 稳定性怎么核对

本仓库保留自动化测试、固定依赖清单、运行包校验和人工验收记录。测试通过的范围、可选模型、云服务和未验证平台在 [验证记录](docs/VALIDATION.md) 分开说明。

遇到问题时先运行：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\check-runtime.ps1
```

然后提交 [Bug 报告](https://github.com/John201-del/phrasesplice/issues/new?template=bug_report.yml)，附系统版本、操作步骤和经过脱敏的错误文字。源码可编译不等于所有显卡、媒体格式及外部 AI 服务都已验证。

## 一起把“说话剪辑”做实用

欢迎提交短小、可复现的剪辑需求、失败样例和 PR。优先方向是安装可靠性、更多自然语言编辑覆盖、任务进度与错误恢复，以及更多设备上的验收。见 [贡献指南](CONTRIBUTING.md)。

如果你也想用一句话开始剪辑，欢迎 **Star**，关注后续版本。把你最想交给 AI 的剪辑任务写进 Issue，或带着可复现的样例一起改进它。

## 来源与许可证

应用采用 [GPL v3](COPYING)。逐文件许可见 [LICENSES](LICENSES) 与 [REUSE.toml](REUSE.toml)，原作者署名见 [AUTHORS](AUTHORS)。有关上游来源、项目修改和依赖许可，见 [第三方说明](docs/THIRD_PARTY.md)。
