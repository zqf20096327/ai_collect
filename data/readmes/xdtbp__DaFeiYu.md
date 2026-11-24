# 大肥鱼（Big Fat Fish）

> **作者的碎碎念**
>
> 本项目本质上重复造轮子。但在本项目立项之时，开源社区仍然没有出现一款适合手机用户、模仿 DeepSeek 官方 App 的软件，而官方也仅仅放出了网页版 demo——这个 demo 对于移动设备极其不友好，甚至略显简陋。
>
> 你问我为什么不用 dsh-go？我的回答是：dsh-go 太重了，它要运行一整个 dsh 核心，启动时长按秒计算；而且 dsh 有太多附加功能是普通对话用不上的，增加了上下文管理压力，费 token。
>
> 在 26.11.18 的中午我被限额了，且无法在手机上找到合适的替代品，遂开始制作这个项目。
>
> 简单介绍下我的使用场景：我是一名在校大学生，因为学业原因经常使用 AI 解答问题。DS 有非常方便的「拍照后马上圈画问答」的功能，加上 DeepSeek 官方 App 非常简洁流畅，问答效率明显高于其他国产 AI 软件。
>
> 在本项目中，我全程使用 AI 进行制作，并开了安卓虚拟机给 AI 进行 debug；在官方放出的网页版项目下进行二次开发，使其更适合移动端，也还原了很多 DeepSeek 官方 App 的操作，让老用户可以很快地适应。
>
> 本项目经过多次迭代和完善，我对当前的状况已经比较满意了。除了我自己需要外，应该不会再更新了；各位开源的朋友可以按自己的需求进行定制。

---

> 基于 DeepSeek 官方前端示例（`chat-demo`）改造的安卓客户端，应用显示名为「大肥鱼」，与官方品牌无关联。原生 WebView 壳 + 前端资源内置，配合一组原生能力桥，得到接近官方 App 的移动端体验。

<p>
  <img alt="license" src="https://img.shields.io/badge/license-MIT-blue.svg" />
  <img alt="platform" src="https://img.shields.io/badge/platform-Android%208.0%2B-3ddc84.svg" />
  <img alt="language" src="https://img.shields.io/badge/Kotlin-2.x-7f52ff.svg" />
  <img alt="frontend" src="https://img.shields.io/badge/React-18-61dafb.svg" />
</p>

> ⚠️ 本项目为第三方开源项目，**与 DeepSeek 官方无关**，未获得官方背书。项目名与图标仅用于说明用途，发布前请自行评估商标风险（详见 [免责声明](#免责声明)）。

---

## 目录

* [截图](#截图)
* [功能](#功能)
* [仓库结构](#仓库结构)
* [架构](#架构)
* [快速开始](#快速开始)
* [原生能力桥](#原生能力桥)
* [免责声明](#免责声明)
* [许可证](#许可证)

---

## 截图

|对话首页|设置|圈画标注|
|-|-|-|
|![welcome](docs/images/welcome.png)|![settings](docs/images/settings.png)|![editor](docs/images/editor.png)|

---

## 功能

### 对话

* 流式输出、停止生成、重新生成、分支切换（来自官方前端）
* 深度思考：**可设置默认折叠**，只显示「已思考（用时 N 秒）」，点标题展开
* 联网搜索（官方 `deepseek_web_search` 工具）
* Markdown / 代码高亮 / KaTeX 公式 / Mermaid 图表
* 每条回复显示 token 用量（输入 / 输出）
* 模型切换：`API Key` 或 `Harness 账号` × `DeepSeek-V4.1-Flash` / `DeepSeek-V4-Pro`
* 推理强度（`output_config.effort`）与最大输出长度（`max_tokens`）可调

### 输入与附件

* 快捷面板：拍照 / 相册 / 文件
* 相册**多选**（系统选择器），最近照片支持**多选即传、取消即删**
* 点击缩略图可**全屏预览**，预览页右下角**编辑**直接进入圈画
* 语音输入：原生 `AudioRecord` 录音 + 官方 ASR（账号令牌同样可用）

### 圈画标注

* 全屏编辑器，底色跟随亮 / 暗主题
* 右下角确认（√）；裁切模式提供「取消 / 应用裁切」
* 双指缩放 + 平移；多指按下不会在两指间画出直线

### 账号与计费

* Harness 账号登录（OAuth PKCE + 本机回环接收回调），登录后无需填 API Key 即可对话
* 侧边栏底部显示头像、昵称、余额；设置页内余额卡片可手动刷新
* 也支持手动填写 API Key（`platform.deepseek.com` 开放平台）

### 数据

* 导入 / 导出官方导出的历史 ZIP（`export_format_version: 3`）
* 导入容错：单条会话不兼容只跳过该条，不再整包失败
* 导入 / 导出**进度条**（百分比 + 已处理数量）
* 导出按 512KB 分块流式写入系统「下载」目录，避免百兆级数据 OOM

### 移动端体验

* 侧边栏平移推开主界面（不是覆盖），支持左右滑动开合
* 返回键分级：先关弹层 / 侧边栏 / 搜索，再退出
* 内容不侵入状态栏，键盘弹出时输入框上移
* 暗色模式、字体大小、界面缩放
* 生成期间持有 `PARTIAL_WAKE_LOCK`，退到后台不会中断流式输出

## 仓库结构

```
.
├── web/                      # 前端（fork 自 DeepSeek chat-demo，React + rspack）
│   ├── src/
│   │   ├── app/              # 应用外壳、主题、视口与手势
│   │   ├── components/       # 会话、消息、输入框、设置、标注编辑器
│   │   ├── services/         # API、会话存储、账号、语音、导入导出
│   │   └── i18n/             # 中英文案
│   ├── rspack.config.ts
│   └── package.json
├── ds-app/                   # 安卓壳（Kotlin + WebView）
│   └── app/src/main/
│       ├── java/com/dschat/app/
│       │   ├── MainActivity.kt   # WebView、文件选择、下载、录音、相册桥
│       │   └── DshAuth.kt        # Harness 账号 OAuth（PKCE + 回环回调）
│       ├── res/                  # 图标、主题、FileProvider 配置
│       └── assets/www/           # 构建时由 web/dist 同步（不提交）
├── docs/                     # 架构、构建、排错文档与截图
├── scripts/                  # 一键构建脚本
└── .github/workflows/        # 前端类型检查与构建 CI
```

---

## 架构

```
┌──────────────────────────────────────────────┐
│ Android (Kotlin)                             │
│  MainActivity                                │
│   ├─ WebView + WebViewAssetLoader            │
│   │     https://appassets.androidplatform.net│
│   ├─ WebChromeClient：文件选择 / 麦克风授权   │
│   ├─ JavascriptInterface 桥（见下表）         │
│   └─ WindowInsets：状态栏 / 键盘适配          │
└───────────────┬──────────────────────────────┘
                │ 加载内置静态资源
┌───────────────▼──────────────────────────────┐
│ Web (React + rspack)                         │
│  UI：会话 / 消息 / 输入框 / 设置 / 标注编辑器 │
│  服务：API 客户端、IndexedDB 会话、附件上传   │
└───────────────┬──────────────────────────────┘
                │ HTTPS
┌───────────────▼──────────────────────────────┐
│ api.deepseek.com                             │
│  /anthropic/v1/messages（流式对话）           │
│  /v1/tools/asr、/v1/tools/tts、/user/balance │
│  platform.deepseek.com（账号 OAuth）          │
└──────────────────────────────────────────────┘
```

更详细的模块说明见 [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)。

---

## 快速开始

### 1. 构建前端

需要 Node.js 22+、pnpm（通过 corepack）。

```bash
cd web
corepack pnpm install
corepack pnpm build          # 产物在 web/dist
```

> Windows 下若 `pnpm build` 因 `NODE_ENV=` 前缀报错，可直接执行：
> `NODE_ENV=production node node_modules/@rspack/cli/bin/rspack.js build -c rspack.config.ts`
> （在 Git Bash 中运行）

### 2. 同步到安卓资源目录

```bash
bash scripts/sync-assets.sh
```

### 3. 构建 APK

需要 JDK 17 与 Android SDK（`ANDROID_HOME` 指向 SDK 根目录）。

```bash
cd ds-app
./gradlew assembleDebug
# 产物：ds-app/app/build/outputs/apk/debug/app-debug.apk
```

完整步骤、签名发布与常见报错见 [docs/BUILD.md](docs/BUILD.md)。

---

## 原生能力桥

|JS 接口|作用|
|-|-|
|`AndroidMedia.getRecentPhotos` / `getPhotoData`|读取相册最近照片与缩略图（快捷面板、选中即上传）|
|`AndroidTheme.setStatusBar`|状态栏 / 系统栏配色跟随主题|
|`AndroidAuth.*`|Harness 账号登录、令牌、资料与余额|
|`AndroidFile.begin/write/end` 等|导出历史时把 `blob:` 分块写入「下载」目录|
|`AndroidFile.pickArchive/archiveState`|导入历史：原生选包 → 复制到私有目录 → 前端轮询读取|
|`AndroidPower.begin/end`|生成期间持有唤醒锁，退后台不中断|
|`AndroidVoice.*`|原生录音（AudioRecord）→ WAV → 官方 ASR|

## 

## 免责声明

* 本项目为个人学习与自用目的开发的第三方客户端，**与 DeepSeek 官方无任何关联**，不代表官方立场。
* 项目中的产品名称、图标等素材版权归其权利人所有；正式发布前请替换为自己的品牌素材，以规避商标风险。
* 使用 Harness 账号令牌访问官方接口属于非公开用法，可能随官方策略变化而失效，请自行评估账号风险。
* 本项目按 MIT 协议「按现状」提供，不对数据丢失、账号异常等后果承担责任。

---

## 许可证

本项目以 **MIT** 协议开源，详见 [LICENSE](LICENSE)。

前端部分基于 DeepSeek 官方 `chat-demo`（MIT, Copyright © 2026 DeepSeek）修改，原始许可证保留在 [web/LICENSE](web/LICENSE)，第三方说明见 [NOTICE.md](NOTICE.md)。

