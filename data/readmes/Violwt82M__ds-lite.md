# DS Lite

**一个用起来更顺手的 DeepSeek 安卓客户端。** 基于 DeepSeek 官方开源前端 [chat-demo](https://github.com/deepseek-ai/chat-demo)（MIT）适配打包，不是官方产品。

<p align="center">
  <img src="docs/cover.png" width="360" alt="DS Lite" />
</p>

> 免费 · 开源 · 无广告 · 无内购 · 不收集任何数据
>
> 这不是 AI 服务，只是一个客户端：**不含 API Key、不代理请求、没有服务器**。你得用自己的 key，所有对话都由你自己的账号和 DeepSeek 官方接口产生。

## 为什么做这个

官方开源的前端本来是网页版，手机上用着不太像"一个 App"。于是我把它做成了安卓 APK，并把几处用起来别扭的地方打磨了一遍：长对话的上下文占用看得见、记忆笔记会自动整理、界面文案更贴近原生使用习惯。**目标不是做一个 RP 专用客户端，而是做一个"正常聊天用起来很顺"的客户端**，角色卡只是顺手支持。

## 功能

**基础（来自上游 chat-demo）**

- 多会话：自动标题、重命名、删除、搜索；编辑提问、重新生成、多分支切换
- 流式输出、深度思考、联网搜索与来源引用、停止 / 继续生成
- 上传、粘贴、拖拽附件；语音输入、朗读；Markdown、代码高亮、KaTeX 公式、Mermaid 图表
- 中英双语、明暗主题、移动端布局、对话导入导出

**DS Lite 的改动**

- **上下文占用常驻显示**：蓝 / 橙 / 红 / 黄黑四档，随时看还剩多少；可一键"立即整理"，越早整理越省 token
- **长期记忆笔记（覆盖式）**：自动把长对话压缩成一份可读的笔记，每次整理都重写成最新一版，不会越堆越多；你自己手写、手改过的笔记会被保留
- **角色卡**：支持导入酒馆（SillyTavern）v2 角色卡
- **用量与花费估算**：按 API 返回的 usage 估算，区分峰谷价（以平台用量信息为准）
- 聊天历史导入更稳（导入不再卡住）、可追加导入

## 下载与安装

前往 [Releases](../../releases/latest) 下载最新的 `DS-Lite-vX.Y.Z-release.apk`。

1. 下载 APK，点击安装；如果提示"未验证的应用"，选「仍要安装」
2. 打开 App → 设置 → 填入你的 API Key
3. 开始聊天

详细步骤（含 Key 怎么申请、旧版本怎么迁移）：[安卓安装说明.md](安卓安装说明.md)

- 最低要求 Android 7.0（API 24）+ 系统 WebView（Chromium 内核）87 以上，2020 年以后出厂的手机基本都满足
- 安装包约 5 MB
- 数据只存在你自己手机上（localStorage + IndexedDB），卸载即清空，**卸载前记得导出对话**

### 网页版（iPhone / iPad 用这个）

不想装 APK 也能用：[https://Violwt82M.github.io/ds-lite/](https://Violwt82M.github.io/ds-lite/) （由 GitHub Actions 部署，就是同一套前端跑在浏览器里）

- **iPhone / iPad**：用 Safari 打开 → 分享 → **添加到主屏幕**，桌面就有图标，点开是全屏
- **第一次成功打开后，界面文件会缓存在你手机上**：以后即使这个站点连不上，也能正常打开（只有发消息需要联网）
- 想自己存一份、或者换到自己喜欢的服务器上：下载 Releases 里的 `DS-Lite-web-*.zip`，解压就是一个完整的静态站点

详细说明（含打不开怎么办、本地自托管）：[网页版说明.md](网页版说明.md)

## 从源码构建

需要 Node.js 22.12+、pnpm。

```sh
git clone https://github.com/Violwt82M/ds-lite.git
cd ds-lite
pnpm install

# 网页版开发
pnpm dev          # http://localhost:8090

# 网页版构建（产物在 dist/）
pnpm build

# 类型检查 / 代码检查
pnpm type
pnpm lint
```

### 构建安卓 APK

需要 JDK 21 与 Android SDK（compileSdk 36）。

```sh
pnpm build
npx cap sync android
cd android
./gradlew assembleDebug      # 产物：app/build/outputs/apk/debug/
./gradlew assembleRelease    # 需要自备签名配置，见下
```

发布签名：在 `android/keystore.properties` 填写 `storeFile / storePassword / keyAlias / keyPassword`，并把 keystore 放到 `android/keystore/`（这两个路径已在 .gitignore 里，**不要提交**）。没有该文件时 `assembleRelease` 会退化为未签名包。

### 构建鸿蒙 HAP（可选）

仓库内 `harmonyos/` 是一个 HarmonyOS 原生外壳：用 ArkWeb 加载随 HAP 打包的同一套 React 前端，复用原有聊天与本地数据逻辑，不是用 ArkUI 重写的官方客户端，也不是华为或 DeepSeek 官方产品。

要求：DevEco Studio / HarmonyOS SDK **API 26**（本工程 `targetSdkVersion` / `compatibleSdkVersion` 为 `26.0.0`）。需要能被 `hdc` 识别的设备（已在一台 OpenHarmony / HarmonyOS API 26 的平板上由开发者自行签名安装做过部分手工验证）。**HarmonyOS 4.x 等仍走 ADB、不能被当前 `hdc` 列出的设备不适用于这个包。**

```sh
pnpm install
pnpm build:harmonyos
# 然后在 harmonyos/ 目录用 DevEco 或 hvigor 构建 debug HAP
# Windows 示例（仅当前终端设置 JDK，勿写入系统环境变量）：
#   $env:JAVA_HOME = "<DevEco Studio 的 jbr 目录>"
#   $env:DEVECO_SDK_HOME = "<DevEco Studio 的 sdk 目录>"
#   $env:PATH = "$env:JAVA_HOME\bin;" + $env:PATH
#   hvigorw --no-daemon assembleHap -p product=default -p buildMode=debug
```

前端资源由 `pnpm build:harmonyos` 同步到 `harmonyos/entry/src/main/resources/rawfile/web/`（该目录已忽略，勿提交构建产物）。未配置签名时产物为 unsigned debug HAP。

本机调试签名：若你在 DevEco 里配置过签名，完整配置会备份在已忽略的 `harmonyos/build-profile.local.json5`。仓库里提交的 `harmonyos/build-profile.json5` **不含**签名材料。需要本机签名打包时，将该备份复制回 `harmonyos/build-profile.json5`（不要把备份或 `.p12` / `.p7b` / 证书密码提交到公开仓库）。签名与安装请自行在本机完成。

更完整的实现说明、验证命令和未验证项见 [harmonyos/说明.md](harmonyos/说明.md)。

**已验证 / 尚未验证（请勿扩大理解）：** 仓库维护者在真机上自行签名安装后，口头反馈聊天、主题、字号、图库选择、API 输入、模型切换、思考强度、预览/刷新/关于/更新页面可用。这是用户报告，不是自动化测试，也**不能**等同于 HAP 升级测试或全部模型/接口的请求测试。导入、角色扮演、持久化、导出与系统分享尚未完整验证。AI 流式与 CORS 在个别设备上的表现仍取决于该设备 Web 内核与接口跨域策略。

## 与上游 chat-demo 的差异

| | 上游 chat-demo | DS Lite |
|---|---|---|
| 形态 | 纯静态网页 | 安卓 APK（Capacitor 外壳）+ 网页 + 可选鸿蒙 HAP（ArkWeb 外壳） |
| 上下文占用 | 无提示 | 四档常驻提示 + 一键整理 |
| 长期记忆 | 无 | 覆盖式自动笔记（可手写） |
| 角色卡 | 无 | 支持酒馆 v2 角色卡 |
| 花费估算 | 无 | 有（峰谷价区分） |
| 中文文案 | 通用 | 针对手机端重写 |

## 已知限制

- 花费是按 `usage` 估算的，**以 [平台用量信息](https://platform.deepseek.com/usage) 为准**；"继续生成"按原回复的时间计费
- 已有会话无法强制刷新，导入时同 id 会话会被跳过
- 没有跨设备同步、没有云备份（这是刻意的：不做服务器）
- 没有 RAG / 向量检索（1M 上下文够用），也没有世界书等重度 RP 机制

## 免责声明

- 本项目**不是 DeepSeek 官方产品**，与深度求索公司无隶属关系
- 本项目**不提供任何 AI 服务**，不代理、不中转、不存储你的请求与 Key
- 使用本客户端产生的所有费用由你自己的 API 账号承担；使用需遵守 DeepSeek 的服务条款
- 本项目免费提供，不接受捐赠、不投放广告、不设内购；请勿用于任何违法用途

## 许可

[MIT](LICENSE)。上游 [deepseek-ai/chat-demo](https://github.com/deepseek-ai/chat-demo) 亦为 MIT，版权声明已保留在 LICENSE 中。
