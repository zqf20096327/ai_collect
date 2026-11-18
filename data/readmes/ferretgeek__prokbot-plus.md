<div align="center">

# ProkBot Plus

**在自己的服务器上运行 Grok Bot，用你自己选的模型。**

Windows · macOS · iOS 客户端补丁 ｜ [自开发 Android App（非官方）](#android-客户端) ｜ 服务端支持 x86_64 和 ARM64 Linux ｜ 支持 OpenAI Chat、OpenAI Responses、Anthropic Messages 三种接口

<p>
<!-- client-badges:start -->
  <a href="#client-versions"><img alt="Windows 官方 1.1.0 x64" src="https://img.shields.io/badge/Windows%20%E5%AE%98%E6%96%B9-1.1.0%20x64-0078D4?logo=windows&logoColor=white"></a>
  <a href="#client-versions"><img alt="Windows 补丁接受 1.1.0 x64（推荐）、0.71.2" src="https://img.shields.io/badge/Windows%20%E8%A1%A5%E4%B8%81%E6%8E%A5%E5%8F%97-1.1.0%20x64%EF%BC%88%E6%8E%A8%E8%8D%90%EF%BC%89%E3%80%810.71.2-237E55?logo=windows&logoColor=white"></a>
  <a href="#client-versions"><img alt="macOS 官方 1.1.0 ARM64" src="https://img.shields.io/badge/macOS%20%E5%AE%98%E6%96%B9-1.1.0%20ARM64-111111?logo=apple&logoColor=white"></a>
  <a href="#client-versions"><img alt="iOS 官方 1.25.0" src="https://img.shields.io/badge/iOS%20%E5%AE%98%E6%96%B9-1.25.0-111111?logo=apple&logoColor=white"></a>
  <a href="#client-versions"><img alt="Android shell 1.1.0" src="https://img.shields.io/badge/%E8%87%AA%E5%BC%80%E5%8F%91%20Android-1.1.0-237E55?logo=android&logoColor=white"></a>
<!-- client-badges:end -->
  <img alt="Host d0a4baa" src="https://img.shields.io/badge/Host-d0a4baa-2496ED?logo=docker&logoColor=white">
  <img alt="Noncommercial License" src="https://img.shields.io/badge/License-Noncommercial-6B7280">
  <a href="https://linux.do"><img alt="LINUX DO" src="https://img.shields.io/badge/Community-LINUX%20DO-F5A623"></a>
</p>

**简体中文** · [English](README.en.md)

</div>

<p align="center">
  <img src="docs/images/windows-chat.png" alt="Windows 客户端：Bot 联网查询香山红叶的观赏时间并给出来源，同时画了一张 16:9 的水彩画" width="880">
</p>
<p align="center"><sub>Windows 客户端：一句话让 Bot 查资料、给出处，顺手再画一张图。模型、联网和生图都走你自己的接口。</sub></p>

## 这是什么

Grok Bot 是 xAI 的 AI 助手应用，有 Windows、Mac、iPhone 等客户端。它的 Bot 不只会聊天：有自己的一台 Linux 电脑，能跑命令、开浏览器、处理文件，还有记忆和定时任务。但原版只能连官方云端。

开源项目 [ProkBot](https://gitee.com/ahaduoduoduo/ProkBot) 把服务端（Host 和 Bot 用的 Linux 电脑）用 Docker 搬到你自己的服务器上，再给原版客户端打补丁，让它连你的服务器。**ProkBot Plus** 在它的基础上：

- 新增 **Windows 客户端**和**自开发的 Android App**；
- 新增 **Anthropic Messages** 和 **OpenAI Responses** 两种模型接口（上游只支持 OpenAI Chat）；
- 修好了联网搜索、生图、消息顺序、本机命令等实际使用中的问题；
- 提供一键部署、备份、升级工具和一份 AI 能照着做的部署手册。

> 这是非官方项目，与 xAI 和 Grok Bot 官方没有任何关系，仅限非商业使用，见[许可与声明](#许可与声明)。

## 能做什么

- **用原版 Grok Bot。** 界面、Agent、工具调用、记忆、定时任务、操作审批都是原版的，只是服务端在你自己手里。
- **按 Bot 路由你想用的模型。** Claude、GPT、DeepSeek、Grok、中转和聚合网关都能一起添加，只要支持工具调用。每个 Bot 可分别指定主模型、思考强度和有序备用模型；已有配置仍可沿用按任务难度路由。
- **Bot 有自己的电脑。** 服务端自带一台 Linux 桌面，Bot 在上面跑命令、开浏览器、处理文件，你可以随时看实时画面，也可以接手操作。
- **让 Bot 操作你的电脑。** Mac 上能执行命令和操作图形界面；Windows 上能执行命令，每次执行前先弹窗问你。
- **联网和生图。** 用模型自带的联网能力搜索、读网页；用 OpenAI 兼容的图片接口生图，能按比例出图，也能拿参考图修改。
- **数据留在自己手里。** 对话、文件、记忆、Bot 资料都存在你的服务器上，遥测和自动更新已关闭。
- **手机上也能用。** iPhone 和 Android 都能聊天、收通知、看 Bot 电脑的画面。
- **在外面也能连。** 局域网直连、内置的 Tailcat 组网（不需要公网 IP），或者你自己的 HTTPS 域名。

<a id="server-requirements"></a><a id="部署需要什么"></a>
## 服务器要求

模型推理走 API，在模型服务商那边，**服务器不需要显卡**。服务器只运行两个 Docker 容器：Host（服务端程序）和 Bot 用的 Linux 电脑。

| | 最低 | 推荐 |
| --- | --- | --- |
| CPU | 2 核 | 4 核或更多 |
| 内存 | 4 GB | 8 GB 或更多 |
| 硬盘可用空间 | 30 GB | 50 GB 或更多 |
| 系统 | 64 位 Linux，Docker 和 Docker Compose v2，Python 3.10+ | Ubuntu 24.04 + Docker 29（实测环境） |

这个配置适合一个人或一家人日常使用；多人同时高强度使用还没有测过。依据：

- **2 核 2 GB 不够用。** 实测两次都没能按时完成连续对话，还出现过后台断连、核心重启。
- **2 核 4 GB、4 核 8 GB 都实测可用。** 各自从零部署，完成了配对、上传附件、多轮真实对话、中途取消，重启后对话和设置都还在。从零构建大约要 9～10 分钟（视网速而定）。
- **实际占用。** 作者自己的服务器（6 核 16 GB）连续运行约一周：Host 平时约 0.7 GB 内存，最高 0.9 GB；Bot 的电脑平时约 0.8 GB，最高 1.7 GB。镜像约占 13 GB 硬盘，对话和文件数据刚开始不到 100 MB，会随使用增长。
- 首次部署要从网上下载官方原版文件和基础镜像（国内网络可能需要代理），构建时还要额外的临时空间；备份也另占空间。

**有哪几种部署方式**

| 你的机器 | 怎么部署 |
| --- | --- |
| 一台 x86_64 Linux | **推荐。**Host 和 Bot 的电脑装在同一台机器上。 |
| 一台 ARM64 Linux + 一台 x86_64 Linux | Host 装在 ARM 机器上（例如甲骨文 Ampere A1），Bot 的电脑装在 x86_64 机器上。Bot 的电脑只有 x86_64 版本。以往在 A1 上测过对话和远程桌面，当前版本还没在 A1 上重新测过。 |
| 只有一台 ARM64 Linux | 在 ARM 上模拟运行 x86_64 的 Bot 电脑。**实验功能**，明显更慢，部署前工具会先检查能不能跑。 |

具体步骤见 [AI 部署手册](docs/AI-INSTALL.md#先选部署方式)，测试记录见[技术文档](docs/ARCHITECTURE.md#capacity-evidence)。

## 还需要准备什么

| 必需 | 说明 |
| --- | --- |
| 模型接口 | 三种格式任选一种：Anthropic Messages、OpenAI Responses、OpenAI Chat Completions。模型要支持工具调用；想让 Bot 操作电脑，还要能看图片。 |
| 生成客户端的电脑 | 需要 Node.js 22.12+。Windows 客户端在 Windows 10/11 x64 上生成；Mac 客户端在 Apple Silicon Mac 上生成；Android 客户端在 Windows、Mac、Linux 上都能生成；iPhone 需要已解密的 IPA 和签名证书。 |
| 官方原版安装包 | 补丁只改你自己下载的官方原版，版本见下面的[客户端版本表](#client-versions)。本项目不分发官方程序。 |

| 可选 | 用途 |
| --- | --- |
| 支持原生联网的模型（例如 Claude 的 `web_search`） | 让 Bot 搜索、读网页 |
| OpenAI 兼容的图片接口 | 让 Bot 生图、修图 |
| 语音识别和语音合成服务 | 语音输入、实时语音通话 |
| Bark 或 Apple 推送证书 | iPhone 推送（Android 不需要） |
| 域名和 HTTPS | 不用 Tailcat 时从外网访问 |

## 客户端

<a id="client-versions"></a>
<!-- client-versions:start -->
**下载哪个版本的官方安装包？** 按右栏下载，补丁只认这些版本。列了两个版本时先用推荐的新版，用不了再换旧版。左栏是官方当前最新版（2026-11-14 核对），比右栏新时要等本项目适配。

| 平台 | 官方最新版 | 本项目需要的版本 |
| --- | --- | --- |
| Windows x64 | [1.1.0](https://api2.cursor.sh/updates/api/download/stable/win32-x64-user/sand) | **1.1.0**（推荐）；用不了再用 0.71.2 |
| macOS ARM64 | [1.1.0](https://api2.cursor.sh/updates/api/download/stable/darwin-arm64/sand) | 0.71.2（尚未适配 1.1.0；未在 Mac 真机上测试） |
| iOS | [1.25.0](https://apps.apple.com/us/app/grok-bot/id6794501026) | 1.16.0（构建 23152；未在 iPhone / iPad 上测试） |
| Android 9+（自开发，非官方） | 不用官方 Android 版 | App **1.1.0**（构建 10100），界面取自 Windows **1.1.0** 安装包（推荐；用不了再用 0.71.2） |
| Linux 服务端 | 不适用 | Host `d0a4baa`；Bot 的电脑 `9d2ac1b`（x86_64） |

ProkBot Plus 自己的版本号见[最新发布](https://github.com/ferretgeek/prokbot-plus/releases/latest)；上游 ProkBot 基线是 `3e9fe8c`。
<!-- client-versions:end -->

| 客户端 | 系统要求 | 测试情况 |
| --- | --- | --- |
| Windows | Windows 10 / 11 x64 | 本项目新增。已在 Windows 11 上实测配对、多轮对话、附件、搜索、本机命令、通知和重启后读回记录；回退用的 0.71.2 版也实测过配对和对话。提供便携版和安装包，不需要管理员权限。 |
| Android | Android 9+，系统 WebView 89+（建议 111+） | 本项目自开发，不是官方 Android 版。已在 Android 15 / 16 模拟器上实测配对、多轮真实对话、读回历史和通知权限；1.1.0 界面另外实测了 Bot 电脑画面、图片、搜索、深色模式和旧版 WebView。还没有真机测试。 |
| Mac | Apple Silicon | 上游已有的补丁，仍用官方 0.71.2：Mac 版是单独的程序包，跟进 1.1.0 要另做补丁并在 Mac 上测试，维护者目前没有 Mac。和 Windows 共用的代码有测试，本项目没有 Mac 真机测试。 |
| iPhone / iPad | 需自备已解密的 IPA 和签名证书 | 上游已有的补丁。补丁工具有测试，本项目没有 iPhone / iPad 真机测试。 |
| Linux 桌面 | — | 本项目不提供补丁。官方另有 [Linux 客户端](https://docs.x.ai/grok-bot/deployment)，它和服务端里 Bot 用的 Linux 电脑不是一回事。 |

## 安装

最省事的方法：交给一个能执行命令的 AI（Claude Code、Codex、Cursor 等都行），把下面这段发给它：

```text
请帮我部署 ProkBot Plus：https://github.com/ferretgeek/prokbot-plus
先完整阅读仓库里的 docs/AI-INSTALL.md，然后严格按里面的步骤做。
先问我现有机器、是否已有实例、模型和访问方式。先运行 doctor；不要删除数据卷、公开密钥或把容器启动当成验收。最后用客户端验证两轮聊天和桌面操作。
```

AI 会先列出要准备的东西，再部署服务端、配置模型、生成客户端，最后用客户端实际聊两轮来验收。

想自己动手，就照着 [AI 部署手册](docs/AI-INSTALL.md) 做。它是写给 AI 的，但每一步都有命令和检查方法，人照着做也没问题。服务端的流程是：`doctor`（检查环境）→ `init`（生成配置）→ `up`（构建并启动）→ `status`（查看状态），然后在管理页填模型、生成配对码，用客户端连接。

下载：[最新版本](https://github.com/ferretgeek/prokbot-plus/releases/latest)按平台提供 Host、Windows、Mac、iOS、Android 五个工具包和 `SHA256SUMS.txt` 校验文件，下载自己需要的那个。工具包里没有官方程序，也没有打好补丁的客户端，客户端要用工具包在你自己的电脑上生成。

## Plus 相比上游多了什么

### Windows 客户端

<table>
  <tr>
    <td width="36%"><img src="docs/images/windows-connect.png" alt="Windows 客户端首次连接：填写 Host 地址和配对码"></td>
    <td><img src="docs/images/windows-approve.png" alt="Bot 要在 Windows 电脑上执行命令前，弹出允许一次、始终允许、从不的确认卡片"></td>
  </tr>
  <tr>
    <td><sub>第一次打开时填 Host 地址和 6 位配对码。</sub></td>
    <td><sub>Bot 要在你的电脑上执行命令时，先问你。</sub></td>
  </tr>
</table>

上游只有 Mac 和 iOS。Windows 版用官方 1.1.0 Windows 安装包打补丁生成（1.1.0 用不了时可以改用 0.71.2），界面和对应的官方 Windows 版一样：

- 托盘常驻、系统通知、附件、消息搜索、Tailcat；
- 执行本机命令（PowerShell，中文输出不会乱码），可以把复杂编程交给本机的 Codex；
- 语音输入和实时语音改由你的 Host 提供；
- 生成便携版和安装包两种形式。

### Android 客户端

**这是 ProkBot Plus 自己开发的 Android App，不是官方 Android 版，也不是给官方 Android APK 打补丁。**

<p align="center">
  <img src="docs/images/android-chat-zh.png" alt="Android 客户端真实聊天：用户问番茄蛋炒饭先炒什么，饭点回复先炒蛋；用户追问米饭结块怎么办，饭点建议用湿手捏散。" width="380">
</p>
<p align="center"><sub>Android 15 模拟器实拍：两轮回复都由连接到自部署 Host 的模型实际生成。</sub></p>

官方 Android 版有防篡改保护，没法改。Plus 换了个做法：把官方桌面版的界面（取自你自己下载的官方 Windows 安装包，推荐 1.1.0，用不了再用 0.71.2）装进本项目写的 Android 外壳，生成 APK。

- 对话、Bot 管理、技能、资料库、例行任务、设置都是原版界面，按官方手机版的样子重新排版：Bot 列表和对话分成两屏，悬浮按钮、气泡、配色、字体和官方手机版一致，支持返回键和深色模式；
- 在手机上看 Bot 电脑的实时画面，「取得控制权」后可以用触摸和键盘操作；
- 上传手机里的文件，把 Bot 发来的文件存到手机；
- 后台通知不依赖 Google 推送，点通知直接打开对应的 Bot；
- 设备凭据用 Android Keystore 加密保存；
- 系统 WebView 较旧的手机（例如鸿蒙「卓易通」）会自动补齐兼容代码；实在太旧时，会提示该更新什么，而不是白屏。

APK 用只属于你的密钥签名，以后升级要用同一个密钥。Android 版不支持 Tailcat，外网使用请用 VPN、内网穿透或 HTTPS 域名。生成方法见[客户端安装说明](docs/AI-INSTALL.md#client-packages)。

### 三种模型接口与 Bot 路由

<p align="center"><img src="docs/images/admin-model.png" alt="管理页的模型设置：服务、档案、默认路由和 Bot 路由" width="760"></p>

上游只支持 OpenAI Chat Completions。Plus 加了 **Anthropic Messages** 和 **OpenAI Responses**，三种格式都完整支持图片、文件、工具调用、思考强度和多轮推理接续。管理页把模型服务、模型档案、默认路由和 Bot 路由分开：一个服务可有多个档案，单个 Bot 可覆盖主模型、思考强度和备用顺序。

- 对话中途换模型、换格式不会出错；
- 服务商不支持某个可选参数时，自动去掉再试；
- 自动安全审查也能用这三种格式。
- 主模型还未输出可见文字或工具调用时，402、408、429、5xx、网络错误和 Host 上游 I/O 空闲超时会按顺序尝试备用模型；同一 Key 只在明确额度耗尽时跳过。已经输出后绝不切换，避免重复回复或工具执行。

### 联网和生图

<table>
  <tr>
    <td><img src="docs/images/admin-web.png" alt="联网工具设置：用 Claude Opus 5.5 的原生联网能力搜索和抓取网页"></td>
    <td><img src="docs/images/admin-media.png" alt="图片与视频设置：默认图片模型 GPT Image 2.6 Sunburst"></td>
  </tr>
</table>

上游已经接上了原版的联网和生图工具，但用新模型时问题不少。Plus 修了这些：

- 新版 Claude 不接受强制调用工具，联网直接失败 → 自动改成普通调用；
- 并行搜索里有一路超出次数，整次搜索都算失败 → 只要有一路成功就用；
- Bot 要一张 16:9 的图，OpenAI 图片接口报错 → 自动换算成对应尺寸；
- 带参考图修图会报错 → 改走修图接口。

### 其他改进

- **消息顺序：**Bot 把一次回复拆成几条发出时，上游可能把顺序打乱；现在严格按模型写的顺序送达。
- **自动审查：**模型偶尔不按格式回答时，原来会直接拒绝操作且不留日志；现在会重试一次，失败会记日志。
- **部署工具：**`host/deploy.py` 一个命令完成检查、初始化、启动、升级、备份和恢复；兼容 Docker 29 和 ARM64。
- **命令行管理：**`host/tools/host-admin.mjs` 不开网页也能初始化、配模型、生成配对码，方便脚本和 AI 操作。

完整改动见 [CHANGELOG](CHANGELOG.md) 和[技术文档](docs/ARCHITECTURE.md)。

## 和官方 Grok Bot 比

**好处**

- 模型和服务商自己选，按你自己的接口计费，也可以用中转或聚合网关。
- 对话、文件、记忆都在自己的服务器上，没有遥测。
- 官方服务用不了的地方也能用；只在局域网里用也行。
- 多了一些官方没有的功能：修改系统提示词（随时能恢复原版）、按模型设置上下文长度、用量统计、Webhook 触发任务、自己写应用（插件）、多台 Host 之间的 Bot 协作、数据备份与恢复。

**代价**

- 要有一台 Linux 服务器，升级和备份要自己做。
- 版本是固定的：Windows 客户端 1.1.0，Mac 客户端和 Android 界面 0.71.2，iOS 1.16.0。官方出新版后，要等本项目适配才能升级，没有自动更新。
- 效果取决于你选的模型。官方针对自家模型做过调校，换别的模型体验可能有差距。
- 部分官方功能关掉或换掉了：虚拟卡、外部消息草稿、产品反馈、通行密钥转发已关闭；语音、推送、生图视频要自己准备服务商；实时语音通话还是实验功能。
- 客户端没有代码签名：Windows 首次打开会有 SmartScreen 提示，iPhone 要自己签名安装，Android 要允许安装未知来源应用。
- Windows 版的 Bot 还不能操作鼠标键盘，原版这部分组件只有 Mac 版。
- 修改官方客户端可能违反官方用户条款，风险自负。

## 文档

| 文档 | 内容 |
| --- | --- |
| [AI 部署手册](docs/AI-INSTALL.md) | 从零部署的完整步骤，每一步都写了「应该看到什么」和「失败了怎么办」 |
| [客户端安装说明](docs/AI-INSTALL.md#client-packages) | Windows、Mac、iPhone、Android 客户端怎么生成和安装 |
| [分开部署](docs/AI-INSTALL.md#split-host)、[备份与恢复](docs/AI-INSTALL.md#volume-recovery) | 进阶部署和数据迁移 |
| [技术文档](docs/ARCHITECTURE.md) | 原理、每个功能的实现、Plus 改了什么、目录结构、测试、二次开发和已知限制 |
| [维护交接](docs/HANDOFF.md) | 给维护者：已发布版本、修改入口、测试方法和发布流程 |

## 交流

- [LINUX DO](https://linux.do)：新的理想型社区。ProkBot Plus 的交流和发布都在这里，有问题、有想法欢迎来聊。
- 发现 bug 请提 [Issue](https://github.com/ferretgeek/prokbot-plus/issues)；安全问题请按 [SECURITY.md](SECURITY.md) 私下报告。

## 许可与声明

- 本项目源自 [ProkBot](https://gitee.com/ahaduoduoduo/ProkBot)（基于其 2026-11-05 版本，提交 `3e9fe8c`），沿用它的 [ProkBot 非商业许可证 1.0](LICENSE)：
  - 可以个人使用、学习、修改和非商业分发；
  - 不能用于任何商业用途，包括收费部署、付费服务和企业内部使用；
  - 来源和修改清单见 [NOTICE](NOTICE)。
- 仓库里没有任何 Grok Bot 官方程序，也不提供成品客户端 APK 或 IPA。`android/dist/` 只有自开发的空外壳；桌面界面从你自己下载并校验的官方安装包中提取。
- Grok、Grok Bot 及相关商标归各自权利人所有。本项目与他们没有关联，也没有得到他们的认可。
- 本项目大部分代码由 AI 辅助编写，由 6.2Astra 和 Opus5.5 一起维护，按现状提供，不提供任何担保。
- 参与贡献请看 [CONTRIBUTING.md](CONTRIBUTING.md)。
