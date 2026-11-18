# SayFlow 输入法

macOS 上的开源输入法：Rime 打字（全拼整句、小鹤 / 自然码 / 微软双拼、五笔 86、五笔 + 拼音混输）+ 语音输入 + AI 整理 + 选中文字 AI 改写。

- 打字完全在本机，不联网，不记录、不上传按键；
- 语音、AI 整理、AI 改写三个联网功能各自可关，默认关闭；全关时不联网、不申请麦克风；
- Hardened Runtime + App Sandbox，ad-hoc 签名，DMG 分发，安装到 `/Library/Input Methods`。

## 功能

| 功能 | 是否联网 | 默认 |
|---|---|---|
| 打字（全拼、双拼、五笔、五笔 + 拼音混输） | 否 | 开 |
| 语音输入（按住右 Command） | 是 | **关** |
| AI 整理语音结果（去口头禅、补标点） | 是 | 开（只在语音开启时生效） |
| AI 改写选中文字（⌃⌥R） | 是 | **关** |

## 小米遥控器当无线麦克风

搭配 [remote-mic-app](https://github.com/HD838A/remote-mic-app)，可以用小米蓝牙遥控器作为无线麦克风——按住遥控器的麦克风键说话，Mac 上直接出字。

## 编译

需要：Apple 芯片 Mac、命令行工具（`xcode-select --install`）、Homebrew 的 `cmake` 和 `boost`。不需要完整 Xcode。

| 步骤 | 做什么 |
|---|---|
| 双击 `编译打字引擎.command` | 编译 librime（已编过则跳过）→ 下载并处理词库、预编译 → 编译 App、打包 DMG → 安全自查 → 用和输入法相同的方式模拟打字验证。日志：`build/rime.log` |
| 双击 `一键编译并自查.command` | 只重新编译 App、打包、单元检查、安全自查（词库已准备好时用）。日志：`build/build.log` |
| 双击 `安装到本机（开发测试）.command` | 把 `build/SayFlow.app` 装到 `/Library/Input Methods`（需要开机密码），仅开发测试用 |

产物：`build/SayFlow-<版本>-arm64.dmg`、`build/selfcheck.txt`（自查结果）。

`vendor/`（librime 静态库、词库）和 `build/` 不进仓库，由脚本从固定版本的上游源码生成，版本和哈希写在 `vendor/*/VERSIONS.txt`，汇总见 `docs/开源组件.md`。

## 配置语音和 AI

语音识别和 AI 功能需要一个兼容 OpenAI API 格式的后端。在「语音与 AI」设置里填写：

- **网关地址**：任何兼容 OpenAI API 的服务（如自建的 [one-api](https://github.com/songquanpeng/one-api)、[new-api](https://github.com/Calcium-Ion/new-api)，或直接用 OpenAI / Groq / 本地 Ollama 等）
- **语音识别模型**：默认 `qwen3-asr-1.7b`
- **AI 整理/改写模型**：默认 `gemini-3.1-flash-lite`，可换成任何 chat 模型
- **令牌**：你的 API Key

接口格式：
- 语音识别：`POST /v1/audio/transcriptions`（multipart/form-data）
- AI 整理/改写：`POST /v1/chat/completions`（JSON）

## 源码结构

```
Sources/SayFlowCore/       纯逻辑，只依赖 Foundation：网关配置与校验、请求格式、文字过滤、AI 结果长度保护、提示词、按键编码
Sources/SayFlowCoreChecks/ 单元检查（不依赖 XCTest）：swift run SayFlowCoreChecks
Sources/SayFlowIME/        输入法本体（AppKit + InputMethodKit）
  main.swift               入口：IMKServer
  InputController.swift    按键处理、上屏、候选窗、7×7 展开、输入法菜单
  InputEngine.swift        打字引擎接口
  RimeEngine.swift         librime 调用（只用预编译好的方案，运行时不编译、不生成配置）
  CandidatePanel.swift     候选窗（横排 / 竖排 / 展开网格）
  VoiceInput.swift Audio.swift   语音输入（按住右 Command）
  Rewrite.swift            选中文字 AI 改写（预览后确认才替换）
  GatewayClient.swift      网络请求（https、不跟随重定向、有超时）
  SettingsWindow.swift     设置窗口
  SystemAccess.swift       麦克风权限、钥匙串
  TextTarget.swift         通过输入法接口写入文字（过滤控制字符和隐形字符）
Sources/CRime/             librime C 接口
Sources/RimeProbe/         打包验证工具（不进 App）
scripts/                   编译、打包、自查、librime 和词库准备
Resources/                 Info.plist、entitlements、图标
```

## 许可证

本项目以 [GPL-3.0](LICENSE) 许可证开源。

## 致谢

- [Rime / 中州韵](https://rime.im/) — 打字引擎
- [雾凇拼音 rime-ice](https://github.com/iDvel/rime-ice) — 拼音词库和双拼方案
- [rime-wubi](https://github.com/rime/rime-wubi) — 五笔 86 词库
- [remote-mic-app](https://github.com/HD838A/remote-mic-app) — 小米遥控器无线麦克风
