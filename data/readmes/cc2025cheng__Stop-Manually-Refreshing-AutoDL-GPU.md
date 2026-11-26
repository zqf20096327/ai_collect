<p align="center">
  <img src="docs/banner.png" alt="AutoDL 候机室：设好条件并授权，空闲 GPU 一出现就自动开机" width="100%">
</p>

<p align="center">
  <b>把等待空闲 GPU 的时间交给候机室。</b><br>
  在自己的电脑上监测 AutoDL。设好 GPU 型号、卡数与地区，发现符合条件的资源后可只收提醒，也可自动创建或同地区克隆并开机。
</p>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License: MIT">
  <img src="https://img.shields.io/badge/node-22%2B-339933?logo=nodedotjs&logoColor=white" alt="Node.js 22+">
  <img src="https://img.shields.io/badge/platform-Windows%20%7C%20macOS-0078D6" alt="Windows 与 macOS">
  <img src="https://img.shields.io/badge/local%20GPU-not%20required-76B900?logo=nvidia&logoColor=white" alt="本机无需 GPU">
  <img src="https://img.shields.io/badge/AI-optional%20%C2%B7%20your%20own%20key-8A2BE2" alt="AI 可选，用自己的 Key">
</p>

<p align="center">
  <a href="#-v040-更新">v0.4.0 更新</a> ·
  <a href="#-快速开始">快速开始</a> ·
  <a href="#-使用步骤">使用步骤</a> ·
  <a href="#-界面预览">界面预览</a> ·
  <a href="#-ai-选卡">AI 选卡</a> ·
  <a href="#-如何更新">如何更新</a> ·
  <a href="#-常见问题">常见问题</a> ·
  <a href="docs/USER_GUIDE.md">详细说明</a>
</p>

## ✨ 它能做什么

- **新建实例**。按你选的型号、卡数、地区和镜像持续监测库存。支持官方镜像、我的镜像和社区镜像。
- **同地区克隆**。从已关机的源实例复制系统盘到同地区的空闲 GPU，可换型号，也可勾选复制数据盘。源实例始终只读。
- **AI 选卡（可选）**。选择项目文件夹或填写需求，用自己的 DeepSeek Key 获取建议。程序核验型号、显存与版本要求，确认后可把建议填入任务草稿。
- **提交保护**。点击前记录提交意图，点击后核对实例列表。结果不明时进入待核对状态，保留已有记录。
- **通知**。支持站内、桌面、AutoDL 微信和 Webhook 提醒。

## 🆕 v0.4.0 更新

<p>
  <a href="https://github.com/cc2025cheng/Stop-Manually-Refreshing-AutoDL-GPU/releases/tag/v0.4.0"><img src="https://img.shields.io/badge/%E7%89%88%E6%9C%AC-v0.4.0-805574" alt="查看 v0.4.0"></a>
  <a href="TEST_REPORT.md"><img src="https://img.shields.io/badge/%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95-446%20%E9%A1%B9%E9%80%9A%E8%BF%87-396E60" alt="446 项自动化测试通过"></a>
  <a href="TEST_REPORT.md"><img src="https://img.shields.io/badge/%E9%A1%B5%E9%9D%A2%E5%9B%9E%E5%BD%92-8%20%E7%BB%84%E9%80%9A%E8%BF%87-455C84" alt="8 组本地页面回归通过"></a>
</p>

### 🎨 界面与任务

- 右上角的「主题背景」可切换**六款全页主题**。下次用同一浏览器打开同一地址时，会恢复上次选择。
- **任务队列**集中展示进度、日志和待处理任务，**消息中心**汇总任务进展与结果。

### 💳 价格与余额

- **首次同步 GPU 单价**后，选好型号和地区就能查看已读单价。预估费用随卡数和预计时长更新，调价后可手动刷新单价。
- 连接余额 Token 后可查看余额。开启**余额检查**的任务会在点击前按当时的完整报价核对。

### 🔄 监测与登录

- 点击前确认候选主机售罄或消失时，新建和克隆可**按原配置继续监测**。点击后须确认本次提交被明确拒绝、原表单恢复可用，且两次完整对账均未发现新实例，才会恢复监测。结果不明时保留提交记录并继续对账。
- 官网提示**图片验证失败**时，回到原专用浏览器标签页继续手动验证。

完整变更见 [更新日志](CHANGELOG.md)。

> [!NOTE]
> 登录后的我的镜像与社区镜像、真实新建与克隆、数据盘复制完成提示、DeepSeek 实际效果和 macOS 真机仍待验收。验证范围见 [测试记录](TEST_REPORT.md)。

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
| 1. 连接 AutoDL | 打开右上角「AutoDL 账户」，点「打开登录」。在专用浏览器中登录后，回到控制台点「检查登录状态」。 |
| 2. 选择 GPU | 勾选地区，点「同步 AutoDL 型号」，再选型号和卡数。需要建议时，可在「AI 选卡」里分析需求并填入草稿。 |
| 3. 配置任务 | 新建时选择镜像来源和版本，官方镜像首次需同步菜单，之后可读缓存。克隆时点「同步实例列表」，选一个已关机的源实例。 |
| 4. 开始监测 | 点击「启动自动创建并开机」或「启动自动克隆并开机」即授权按匹配配置执行。只想收到提醒时，先选「只通知，停在提交之前」。 |
| 5. 查看进度 | 在「任务队列」查看详情与日志，在「消息中心」查看任务进展与结果。 |

> [!TIP]
> 监测期间保持电脑联网、不休眠，不要关闭启动窗口。关掉控制台网页不影响后台检查。

## 📸 界面预览

<p align="center">
  <img src="docs/figures/dashboard.png" alt="资源监测首页，展示监测状态、新建实例和迁移克隆入口" width="100%">
  <br><sub><b>资源监测</b> · 粉樱晚霞主题</sub>
</p>

<p align="center">
  <img src="docs/figures/themes.png" alt="主题选择面板，含雾山、林间晨光、蓝紫樱山、粉樱晚霞、红枫山海和晴空云端" width="640">
  <br><sub><b>主题背景</b> · 六款全页主题</sub>
</p>

<p align="center">
  <img src="docs/figures/plan-form.png" alt="AI 环境与选卡表单，包含运行目标、项目文件夹、资料预览和计划卡数" width="100%">
  <br><sub><b>AI 选卡</b> · 填写运行需求与项目资料</sub>
</p>

<details>
<summary>更多界面 · 任务队列、AI 推荐结果和镜像选项</summary>

<p align="center"><img src="docs/task-queue.png" alt="任务队列，集中查看运行进度和待处理状态" width="100%"><br><sub>任务队列</sub></p>
<p align="center"><img src="docs/task-queue-mobile.png" alt="窄屏下的任务队列" width="320"><br><sub>窄屏任务队列</sub></p>
<p align="center"><img src="docs/figures/plan-results.png" alt="AI 选卡结果，显示推荐 GPU 和程序核验依据" width="100%"><br><sub>AI 推荐结果</sub></p>
<p align="center"><img src="docs/figures/custom-images.png" alt="我的镜像与社区镜像的版本选项" width="100%"><br><sub>我的镜像（左）和社区镜像（右）</sub></p>

<sub>折叠区中的实例状态和 AI 推荐结果为合成示例。</sub>

</details>

## 🧠 AI 选卡

等不到某一种卡时，换一张同样能跑的卡往往更快。写下你要做什么，选择项目文件夹并检查资料预览，也可以直接粘贴说明。资料先在本地整理，确认同意后才发送给 DeepSeek；没有 README 也能从依赖、配置和启动代码中提取线索：

- 🤖 **DeepSeek 判断**：用你自己的 DeepSeek API Key，结合 **GPU 知识库**（各架构对 CUDA / PyTorch 的最低版本、显存估算公式，每条有出处）和 **AutoDL 当前型号目录**，判断每张卡能不能跑、建议型号与卡数，也可以由你固定卡数。资料没说清时先问你一两个问题。
- 🛡️ **程序核验**：型号必须在目录里，引用必须是原文，结论不能违反知识库的硬性事实（例如固定 `torch==2.1.0` 的项目不能用 RTX 5090）。不符合的自动改得更保守，并写明原因和出处。
- 🎯 **一键填入任务**：在推荐的型号上点“填入新建任务”，填入型号、卡数和地区，并按核验过的版本要求选择官方镜像；无法确定的镜像由你选择。核对配置后，由你点击启动按钮建立任务。
- 🔒 **AI 只做建议**：不参与监测和下单；本机不需要 GPU。没有 Key 时可以用“按规则估算”作参考。说明见 [docs/AI_ASSISTANT.md](docs/AI_ASSISTANT.md)。

<details>
<summary>工作原理（架构图）</summary>

![总体架构](docs/figures/architecture.png)

</details>

## 🔐 安全与费用

- 点击自动创建或自动克隆的启动按钮即授权该任务按 AutoDL 实际报价执行。页面费用预估只计算 GPU，提交前还会核对磁盘费用。预计运行时长用于估算，关机由你操作。
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
