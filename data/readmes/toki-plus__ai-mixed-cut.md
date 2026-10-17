# AI Mixed Cut

[简体中文](./README.md) | [English](./README_en.md)

面向内容再利用场景的 AI 辅助视频工作流案例。

该方案围绕“素材分析—结构化整理—脚本重组—语音生成—视频合成”设计，用于探索内容团队如何在保留人工审核的前提下，提高已有素材的整理与再生产效率。

> 本仓库是经过整理的公开技术案例，包含方案说明和界面展示，不包含完整实现代码。案例中的素材必须具备合法使用和改编权限。

## 问题背景

内容团队积累了大量视频、文案和音频素材，但这些资产通常缺少统一结构。人工寻找可用片段、整理主题、重新编写脚本并完成剪辑，需要在多个工具之间反复切换。

本方案将流程拆分为可独立验证的模块，使素材、脚本、语音和视频输出具备更清晰的输入输出关系。

## 目标用户

- 管理大量历史素材的内容运营团队
- 需要将长内容拆分为多个主题内容的编辑人员
- 希望验证 AI 辅助内容工作流的产品与技术团队

## 方案流程

```text
Authorized source material
    -> Content extraction
    -> Structure analysis
    -> Material library
    -> Script recomposition
    -> Speech generation
    -> Video composition
    -> Human review
```

## 主要模块

### 1. 内容分析与素材库结构化

- 提取可编辑文本和时间信息，保留原始来源，便于回溯和人工核对。
- 按三个维度把视频内容解构为可复用的结构化素材库：
  - **主题解构**：提炼核心选题、目标人群和价值主张，形成 `topics.json`；
  - **框架解构**：抽象叙事结构和内容组织方式，形成 `frameworks.json`；
  - **金句解构**：沉淀具有普适性的高质量句子，形成 `golden_sentences.json`。
- 素材库以 JSON 文件形式落盘，可被后续模块独立读取、人工增删和版本管理。

### 2. 脚本重组与音频生成

- 从素材库中组合"主题 + 框架 + 金句"，在明确的内容约束下由模型生成候选脚本；标题与标签仅作为草稿输出，需人工终审后使用。
- 集成 Edge TTS 合成多语言人声，支持语速、音调、音量调节；生成音频的同时输出时间轴对齐的 `.srt` 字幕。
- 字幕经过二次断句处理，按语义和版面效果优化换行；所有中间文件保留，支持人工修改后重跑后续环节。

### 3. 视频合成

- 按主题管理多个素材目录，支持顺序或随机拼接，每个素材可设定固定时长、随机时长或原始时长。
- 提供可选的画面处理项：LUT 调色、动态缩放、随机旋转、背景模糊、遮罩叠加与 `xfade` 转场，用于二次创作场景下的内容差异化处理。
- 支持 NVIDIA（NVENC）硬件编码加速渲染；提供参数化渲染与批量任务入口，各模块可分步独立运行，便于调试和验证。

## 技术考虑

- 将 AI 输出视为候选结果，而不是最终发布内容
- 对素材来源、授权和处理记录保留可追溯信息
- 将浏览器自动化、模型调用和媒体处理划分为独立边界
- 对外部服务失败、超时和接口变更预留恢复机制

## 📸 软件截图

<p align="center">
  <img src="./images/cover_software.png" alt="软件主界面" width="800"/>
  <br>
  <em>软件主界面：内容分析、脚本重组、音频生成、视频合成的模块化工作流清晰可见。</em>
</p>

## 当前状态

本仓库用于展示工作流设计与产品原型。由于实现中包含第三方服务配置及非公开业务逻辑，完整代码未在此仓库发布。

## 责任边界

- 仅处理获得授权的文本、音频和视频素材。
- AI 生成内容必须经过事实、版权与品牌审核。
- 使用者应遵守平台规则、模型服务条款和当地法律。

## 📂 更多项目

- [video-mover](https://github.com/toki-plus/video-mover) — 多平台内容分发自动化流水线：素材处理、文案生成、定时调度与多平台适配
- [ai-highlight-clip](https://github.com/toki-plus/ai-highlight-clip) — 长视频智能初筛：Whisper 转写 + LLM 评分 + 人工终审，分钟级定位高光片段
- [ai-ttv-workflow](https://github.com/toki-plus/ai-ttv-workflow) — 文案到短视频的桌面工作流，关键节点保留人工确认
- [ai-video-workflow](https://github.com/toki-plus/ai-video-workflow) — 多模型 AIGC 视频生成流水线：文生图、图生视频、文生音乐的异步编排
- [ai-trader-for-mt4](https://github.com/toki-plus/ai-trader-for-mt4) — LLM×MT4 受控执行框架：工具约束、风控规则、状态管理与异步桥接
- [ai-trader-for-mt5](https://github.com/toki-plus/ai-trader-for-mt5) — 面向 MT5 的 AI 交易助手与 EA 工程化框架
- [auto-usps-tracker](https://github.com/toki-plus/auto-usps-tracker) — 跨境电商批量物流追踪与 Excel 报告自动化
- [AB-Video-Deduplicator](https://github.com/toki-plus/AB-Video-Deduplicator) — 基于高帧率抽帧混合的视频再创作实验工具
- [netease-downloader](https://github.com/toki-plus/netease-downloader) — 网易云音乐下载桌面应用：扫码登录、下载队列、ID3 元数据写入

## License

See [LICENSE](./LICENSE).
