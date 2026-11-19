<p align="center">
  <img src="docs/banner.png" alt="AutoDL 候机室：设好条件并授权，空闲 GPU 一出现就自动开机" width="100%">
</p>

<p align="center">
  <b>别再手动刷新 AutoDL 了！</b><br>
  你设好 GPU 型号、地区和镜像并授权，空闲 GPU 一出现就自动创建并开机；不知道该等哪张卡，选择项目文件夹，查看 GPU 和卡数建议。
</p>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License: MIT">
  <img src="https://img.shields.io/badge/node-22%2B-339933?logo=nodedotjs&logoColor=white" alt="Node.js 22+">
  <img src="https://img.shields.io/badge/platform-Windows%20%7C%20macOS-0078D6" alt="Windows 与 macOS">
  <img src="https://img.shields.io/badge/local%20GPU-not%20required-76B900?logo=nvidia&logoColor=white" alt="本机无需 GPU">
  <img src="https://img.shields.io/badge/AI-optional%20%C2%B7%20your%20own%20key-8A2BE2" alt="AI 可选，用自己的 Key">
</p>

<p align="center">
  <a href="#-v030-更新">v0.3.0 更新</a> ·
  <a href="#-快速开始">快速开始</a> ·
  <a href="#-使用步骤">使用步骤</a> ·
  <a href="#-ai-选卡">AI 选卡</a> ·
  <a href="#-如何更新">如何更新</a> ·
  <a href="#-常见问题">常见问题</a> ·
  <a href="docs/USER_GUIDE.md">详细说明</a>
</p>

## ✨ 它能做什么

- ⚡ **空闲即开机**：按你设的型号、卡数和地区（可多选），默认每秒检查一次，发现空闲 GPU 立即创建并开机。
- 🔁 **同地区克隆换卡**：把已关机的实例克隆到同地区的空闲 GPU，可以换型号、复制数据盘；源实例只读，不会被改动。
- 🖼️ **镜像任选**：官方基础镜像、我的镜像或社区镜像都能用；提交前精确核对名称、版本与 CUDA，不会自动换成别的镜像。
- 🧠 **AI 选卡（可选）**：选择项目文件夹并检查资料预览，DeepSeek 结合 GPU 知识库和 AutoDL 当前型号建议 GPU 与卡数，程序逐条核验，一键填入任务草稿。
- 🛡️ **防重复付费**：点击前把提交意图写入磁盘，点击后对账实例列表；结果不明就停下核对，不再点击。
- 🔔 **多渠道通知**：站内、桌面、AutoDL 微信、Webhook。
- 💻 **门槛低**：本机不需要 GPU，Windows 双击启动，macOS 用终端启动。AI 可选。

> [!NOTE]
> **真实账号验证**：2026-10-29 至 10-30 完成 4 次自动新建并开机、2 次同地区克隆；2026-11-19 AutoDL 前端更新后已完成适配，复测通过。当前源码通过 438 项自动化测试和 8 组本地页面回归。macOS 启动脚本通过模拟测试，真机兼容性待验证。详见 [测试记录](TEST_REPORT.md)。

## 🆕 v0.3.0 更新

<sub>2026-11-20 · 完整列表见 [CHANGELOG](CHANGELOG.md) · 下载见 [Releases](https://github.com/cc2025cheng/Stop-Manually-Refreshing-AutoDL-GPU/releases)</sub>

| | 更新 | 说明 |
| :---: | --- | --- |
| 🖼️ | **我的镜像 · 社区镜像** | 新建实例不再只能用官方镜像：从“我的镜像”列表同步自己的镜像，或按完整名称搜索社区镜像并选版本，CUDA 自动带入 |
| 🤖 | **AI 选卡重做** | DeepSeek 结合带出处的 GPU 知识库和 AutoDL 当前型号目录，判断每张卡能不能跑、要几张；资料没说清时先追问 |
| 🛡️ | **程序核验 AI 结论** | 型号必须在目录里、引用必须是原文；显存或架构不满足的自动改判，只会改得更保守，并写明原因和出处 |
| 📁 | **选择整个项目文件夹** | 在浏览器本地筛选依赖、配置和启动代码，预览可删改，同意后才发送；上万个文件的大项目也能整理 |
| 💾 | **官方镜像菜单缓存** | 记住上次选择和已读菜单，重新打开页面直接恢复 |
| 🍎 | **macOS 启动脚本** | 终端一条命令启动，使用独立的 `.runtime-macos/` 运行目录（模拟测试通过，真机待验证） |
| 🧩 | **适配 AutoDL 新版页面** | 适配 2026-11-19 更新后的实例列表与型号筛选，真实账号复测通过 |

<p align="center">
  <img src="docs/figures/custom-images.png" alt="镜像来源：我的镜像（左）与社区镜像（右）" width="88%">
  <br><sub>新建实例的镜像来源：我的镜像（左）与社区镜像（右）。截图为合成数据。</sub>
</p>

> [!WARNING]
> 我的镜像与社区镜像已在合成页面上通过回归，尚未在登录后的真实页面验证。首次使用请先建“只通知”任务，确认选中的镜像无误后再开启自动创建。

**从 v0.2.x 升级**：先暂停监测再更新（见 [如何更新](#-如何更新)）。AI 选卡现在只接 DeepSeek，以前保存的百炼等接口配置会停用，需要重新填写 DeepSeek 的 Key。

## 🚀 快速开始

**需要** Windows 10/11 或支持 Playwright Chromium 的 macOS、[Node.js 22+](https://nodejs.org) 和自己的 AutoDL 账号。

1. 下载项目。推荐用 git，以后一条命令就能更新：

   ```powershell
   git clone https://github.com/cc2025cheng/Stop-Manually-Refreshing-AutoDL-GPU.git
   ```

   没装 git 也可以点仓库上方绿色的 **Code → Download ZIP** 并解压。
2. 进入项目文件夹。Windows 双击 **`启动监测台.cmd`**，macOS 在终端运行以下命令。脚本按需安装依赖，macOS 脚本也会补装 Chromium。

   ```bash
   bash ./启动监测台.command
   ```

3. 在浏览器打开终端显示的地址，默认是 `http://127.0.0.1:8787`。

<details>
<summary>Windows 命令行启动与常见安装问题</summary>

```powershell
npm.cmd install
npm.cmd start
```

- 依赖下载慢：`npm.cmd install --registry=https://registry.npmmirror.com`
- 提示找不到浏览器：`npm.cmd run browser:install`（没有时程序也会尝试本机 Edge）
- 8787 端口被占用：先运行 `$env:PORT='8788'`，再在同一窗口运行 `npm.cmd start`
- 停止服务：在启动窗口按 Ctrl+C，或运行 `npm.cmd run stop`

</details>

## 🧭 使用步骤

| 步骤 | 操作 |
| --- | --- |
| 1️⃣ 连接 AutoDL | “资源监测 → 连接 AutoDL”点“打开登录”，在弹出的专用浏览器中自己登录；回到控制台点“检查登录状态”，显示“会话可用”即可 |
| 2️⃣ 同步型号 | 勾选地区，点“同步 AutoDL 型号”，看到各地区有哪些 GPU、空闲多少 |
| 3️⃣ 选卡（可选,一般不需要用这个功能） | 打开“AI 环境与选卡”，填好自己的 DeepSeek Key，写下要做什么、选择项目文件夹并检查资料预览，卡数可让 AI 建议或自行固定，点“AI 分析并选卡”，在推荐的型号上点“填入新建任务” |
| 4️⃣ 建立任务 | **新建实例**：选型号、卡数、地区，首次点“同步官方镜像”并手动补读、逐级选环境，之后恢复缓存选择，需要更新时再手动刷新；也可改用“我的镜像”或按完整名称搜索“社区镜像”（尚未在真实页面验证）；**迁移克隆**：点“同步实例”，选一个已关机的源实例 |
| 5️⃣ 开始监测 | 勾选费用授权后点“开始真实库存监测”；只想收到提醒就选“只通知，停在提交之前” |

> [!TIP]
> 监测期间保持电脑联网、不休眠，不要关闭启动窗口。关掉控制台网页不影响后台检查。

## 📸 界面预览

<table>
  <tr>
    <td width="50%"><img src="docs/figures/dashboard.png" alt="控制台：建立监测任务"></td>
    <td width="50%"><img src="docs/figures/plan-results.png" alt="AI 环境与选卡：各型号是否能跑"></td>
  </tr>
  <tr>
    <td align="center">控制台：建立监测任务</td>
    <td align="center">AI 环境与选卡：各型号是否能跑</td>
  </tr>
</table>

<sub>截图为隔离测试中的合成数据，型号库存是虚构的。</sub>

## 🧠 AI 选卡

等不到某一种卡时，换一张同样能跑的卡往往更快。写下你要做什么，选择项目文件夹并检查资料预览，也可以直接粘贴说明。资料先在本地整理，确认同意后才发送给 DeepSeek；没有 README 也能从依赖、配置和启动代码中提取线索：

- 🤖 **DeepSeek 判断**：用你自己的 DeepSeek API Key，结合 **GPU 知识库**（各架构对 CUDA / PyTorch 的最低版本、显存估算公式，每条有出处）和 **AutoDL 当前型号目录**，判断每张卡能不能跑、建议型号与卡数，也可以由你固定卡数。资料没说清时先问你一两个问题。
- 🛡️ **程序核验**：型号必须在目录里，引用必须是原文，结论不能违反知识库的硬性事实（例如固定 `torch==2.1.0` 的项目不能用 RTX 5090）。不符合的自动改得更保守，并写明原因和出处。
- 🎯 **一键填入任务**：在推荐的型号上点“填入新建任务”，填入型号、卡数和地区，并按核验过的版本要求选择官方镜像；无法确定的镜像由你选择，仍需你勾选费用授权才会提交。
- 🔒 **AI 只做建议**：不参与监测和下单；本机不需要 GPU。没有 Key 时可以用“按规则估算”作参考。说明见 [docs/AI_ASSISTANT.md](docs/AI_ASSISTANT.md)。

<details>
<summary>工作原理（架构图）</summary>

![总体架构](docs/figures/architecture.png)

</details>

## 🔐 安全与费用

- 💳 勾选费用授权后，程序会真实创建实例，费用由 AutoDL 收取；提交前会重新核对库存与结算费用。
- 👤 只在你本人登录的专用浏览器中操作可见页面，不调用私有接口，不代过验证码。
- 🏠 服务只监听本机 `127.0.0.1`。运行资料保存在 Windows 的 `.runtime/` 或 macOS 的 `.runtime-macos/`。请保护这些目录，并仅在本机使用控制台。
- 📜 本项目与 AutoDL 官方无隶属关系，使用前请对照 AutoDL 用户协议。详见 [docs/SECURITY.md](docs/SECURITY.md)。

## 🔄 如何更新

> [!IMPORTANT]
> 更新前先暂停监测，等提交或核验结束。在原启动窗口按 Ctrl+C，或在项目目录运行停止命令（Windows 用 `npm.cmd run stop`，macOS 用 `npm run stop`）。若自定义了端口或运行目录，停止命令需使用相同的设置。

| 下载方式 | 更新步骤 |
| --- | --- |
| `git clone` | 在项目文件夹运行 `git pull`，再用对应系统的启动脚本启动。依赖变化时 Windows 用户先运行 `npm.cmd ci`。 |
| Download ZIP | 解压新源码。同一台电脑更新时，后台停止后可将旧的运行目录完整迁入新目录，再用对应系统的脚本启动。 |

- macOS 可在专用浏览器保留 AutoDL 登录。DeepSeek Key、余额 Token 和通知凭据在后台退出后需重新填写。更多说明见 [安装与使用说明](安装与使用说明.md)。
- 想第一时间知道新版本：点仓库右上角 **Watch → Custom → 勾选 Releases → Apply**。每个版本改了什么见 [CHANGELOG.md](CHANGELOG.md) 或 [Releases](https://github.com/cc2025cheng/Stop-Manually-Refreshing-AutoDL-GPU/releases)。

## ❓ 常见问题

<details>
<summary>网页提示“本地后台仍是旧版本”？</summary>

请按上面的步骤正常停止后台，再用当前源码启动并刷新网页。保留运行目录、运行锁和浏览器资料。

</details>

<details>
<summary>点“打开登录”提示网络访问受限？</summary>

这说明专用浏览器访问网页被启动环境或网络策略拒绝了，和账号密码无关。退出旧服务后，在普通 Windows 环境双击 `启动监测台.cmd` 重启；也可以运行只读的网络诊断 `npm.cmd run diagnose:network`。

</details>

<details>
<summary>登录失效或要人工验证？</summary>

回到专用浏览器自己完成登录或验证，再点“检查登录状态”。程序不会代过验证码。

</details>

<details>
<summary>点击“创建并开机”后结果不明？</summary>

程序会停下来只读核对实例列表，不会再点一次。请在 AutoDL 页面核对；不要删除 `.runtime`，也不要新建同样的任务来重试。

</details>

## 🔧 检查和项目结构

```powershell
npm.cmd run check          # 语法检查
npm.cmd test               # 单元与接口测试
npm.cmd run test:plan-ui   # 选卡页面回归（其余页面回归见详细说明）
```

这些检查只用合成数据，不登录 AutoDL、不租卡、不调用模型。

| 目录 | 内容 |
| --- | --- |
| `src/` | 本地服务、任务引擎、AutoDL 网页适配器、AI 选卡（`gpu-advisor.mjs`）、GPU 知识库（`gpu-knowledge.mjs`）、规则估算（`env-plan.mjs`）、DeepSeek 接入 |
| `public/` | 控制台网页 |
| `tests/` · `scripts/` | 自动化测试、页面回归与诊断脚本 |
| `eval/` | 选卡规划评测集与结果 |

## 📄 许可证

[MIT](LICENSE) © 2026 cc2025cheng。第三方组件及其许可见 [docs/THIRD_PARTY.md](docs/THIRD_PARTY.md)。

如果它帮你少刷了几次页面，欢迎点个 ⭐ Star。
