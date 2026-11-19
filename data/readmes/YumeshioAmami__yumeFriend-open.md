# yumeFriend

一个本地优先、可扩展的 AI 朋友应用。

yumeFriend 在自己的设备上运行，聊天、记忆、人格和媒体默认保存在本机。
它支持独立人格、OpenAI 兼容模型、可选的语音 / 图片 / Live2D、3D 小世界，
以及独立的 Android 手机 / 平板端。

## 功能

- 创建有独立人格的朋友，聊天、记忆和切换普通 / 入戏 / 工具模式；
- 接入 OpenAI 兼容、Anthropic 兼容或 Gemini 兼容的模型服务；
- 本地保存聊天、记忆、人格、设置和媒体文件；
- 记忆检索、日程、知识库、主动消息和表达学习；
- 可选的语音输入 / 回复、图片生成和角色表现；
- Live2D 模型导入与运行时下载：用户阅读并同意官方许可后，由应用从 Live2D
  官方地址获取运行时；
- 3D 小世界：房间、角色活动、物件编辑和房间内对话；
- Minecraft 多版本陪伴：适配器代码通用，版本数据按服务器版本按需下载；
- 桌面、手机和平板手动同步；手机端也可以完全独立使用。

## 快速开始

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r backend\requirements.txt

cd frontend
npm install
npm run build
cd ..

.\start_yumeFriend.bat
```

后端默认只监听 `127.0.0.1:8001`。首次使用时在设置里配置聊天模型，然后创建
朋友即可。

## 手机 / 平板

Android 端是独立单机应用，不需要电脑常开。源码构建需要 JDK、Android SDK、
Gradle 和 Node.js，具体步骤见 [Android 手机端](docs/mobile.md)。

手机端第一次打开会显示使用教程，之后可以从朋友列表右上角的 `?` 或设置页再次
打开。

## 文档

- [快速开始](docs/getting-started.md)
- [功能概览](docs/features.md)
- [架构说明](docs/architecture.md)
- [Android 手机端](docs/mobile.md)
- [数据与隐私](docs/data-and-privacy.md)
- [教程与用户指南](docs/tutorials.md)
- [开发与测试](docs/development.md)
- [本地 API 概览](docs/api.md)

## 数据在哪里

聊天记录、记忆、人格、图片、语音缓存、模型设置和 API Key 默认保存在本机的
`user_data/` 目录。这个目录不属于源码，也不应该提交到 Git。

API Key 当前在本机 SQLite 中明文保存。请自行保护设备账户和备份文件。

## 隐私与边界

- 本项目不内置遥测；
- 只有你主动配置或触发的能力才会访问第三方模型、语音、搜索、更新或同步服务；
- 第三方服务如何处理数据，由对应服务商决定；
- 请遵守适用法律法规和托管平台规则。

详见 [PRIVACY.md](PRIVACY.md)、[TERMS_OF_USE.md](TERMS_OF_USE.md) 和
[CONTENT_POLICY.md](CONTENT_POLICY.md)。

## 参与

第一阶段只接受 issue，不接受代码 PR。请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可证

项目代码采用 Apache-2.0。第三方模型、动画、依赖和 SDK 各自保留自己的许可证，
详见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

本项目与 pixiv / VRoid、Minecraft 或其他第三方厂商没有隶属关系。
