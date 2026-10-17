# 小说工厂 · StarT-Novel

一个在自己电脑上运行的 AI 长篇小说创作工具：从找题材、定设定，到分章写作、三位审稿员审稿，再到导出 Word，一条流水线完成。

*A desktop app for writing long-form Chinese web novels with AI — genre radar, story bible, chapter-by-chapter writing with self-check and story memory, three-reviewer editing pass, and Word export. Bring your own API keys; everything stays on your computer. The interface is currently Chinese only.*

![写作车间](docs/images/workshop.png)

## 它能做什么

| 模块 | 做什么 |
|---|---|
| **题材雷达** | 联网搜索起点、晋江、番茄的近期榜单和读者讨论，找出正在上升的细分题材，附来源链接 |
| **选卡建书** | 从雷达题材，或从你自己的构思出发，生成书名、主角、金手指、世界观、配角和分卷大纲；每张卡片可以换一批，也可以直接编辑 |
| **写作车间** | 分卷细化章纲，逐章写作；每章自检（问题分大小、定向修改），维护故事记忆（人物状态、伏笔、已确立事实），防止前后矛盾 |
| **审稿** | AI 痕迹、逻辑、读者体验三位审稿员先按卷通读找跨章问题，再逐章细审；小问题自动修改，大问题由你确认；可按章节范围审稿 |
| **裁判（可选）** | 接入 TypeSafe System One，复核每条意见是否成立，并给每章的开头、钩子、节奏、AI 腔打分 |
| **写作规则** | 每写完一本书，从审稿意见中提炼经验规则，下一本书从第一章开始生效 |
| **书库** | 导出投稿版 / 存档版 Word；导入你已写好的作品（.txt / .docx / .md）继续写或审稿；导出"设定包"带到其他 AI 平台继续写 |

其他：平台文风（番茄 / 起点 / 晋江 / 自由写作）与自定义文风、全书批量替换名词、按版本回退、四套界面主题、简繁切换、书稿放 OneDrive 多台电脑共用（Windows 和 Mac 可以混用）、Windows 免安装版一键升级。

![审稿](docs/images/review.png)

## 下载与使用

### 直接下载（Windows）

到 [Releases](https://github.com/AceSpike/StarT-Novel/releases) 下载 `StarT-Novel-版本号-win-x64.zip`，解压到一个普通文件夹（例如 `D:\Programs\小说工厂`，不要放在 `Program Files` 里），运行 `小说工厂.exe`。

> 资源管理器里 `小说工厂.exe` 显示的是 Electron 的原子图标，这是有意为之：免安装版直接使用 Electron 官方原版程序，以免被 Windows 11 的"智能应用控制"拦截。软件运行后窗口和任务栏是笔尖图标。原因详见 [使用说明书](docs/user-guide.md) 的常见问题。

### 直接下载（Mac）

到 [Releases](https://github.com/AceSpike/StarT-Novel/releases) 下载 `StarT-Novel-版本号-mac-arm64.dmg`（M 系列芯片），双击后把"小说工厂"拖进"应用程序"。软件没有经过苹果公证，第一次打开的方法见 [使用说明书](docs/user-guide.md)；Intel 芯片的 Mac 请按 [开发者指南](docs/developer-guide.md) 自己打包。

### 从源码运行

需要 [Node.js](https://nodejs.org) LTS 版本。

```bash
git clone https://github.com/AceSpike/StarT-Novel.git
cd StarT-Novel
npm install
npm run dev
```

国内网络如果下载 Electron 很慢，先设置镜像：

```bash
# Windows
set ELECTRON_MIRROR=https://npmmirror.com/mirrors/electron/
# macOS / Linux
export ELECTRON_MIRROR=https://npmmirror.com/mirrors/electron/
```

如果 `npm run dev` 提示 `Electron uninstall`，执行一次 `node node_modules/electron/install.js`。打包、项目结构等详见 [开发者指南](docs/developer-guide.md)。

### 第一次使用

1. **设置 → 模型**：填入你自己的 API Key，点"测试连接"。支持 Gemini、Claude、OpenAI、DeepSeek、通义千问、Kimi、豆包，以及任何兼容 OpenAI / Anthropic 接口格式的平台；
2. **设置 → 模型 → 模型分工**：给每个岗位选模型。建议写作和自检用不同家的模型，题材雷达的搜索模型需要支持联网；
3. 海外模型在国内需要代理：**设置 → 模型 → 网络代理**，保持"跟随系统代理"，点"检测"。

完整的使用说明见 [使用说明书](docs/user-guide.md)：从安装设置、快速上手，到每个模块的用法和常见问题。

## 数据与隐私

- **没有服务器，没有统计。** 软件只会连接你自己配置的模型接口。
- **API Key** 由系统加密后保存在本机（Windows 在 `%APPDATA%\小说工厂`，macOS 在 `~/Library/Application Support/小说工厂`），不在项目文件夹里。
- **书稿** 默认也保存在上面的目录，可以在设置里迁移到 OneDrive 等同步文件夹。
- 调用模型时，书稿内容会发送给你选择的模型服务商，请留意各服务商的数据使用政策。

## 使用须知

- 生成内容的质量取决于所用模型。软件提供自检、审稿和裁判来发现问题，但**事实性、法律和技术常识方面的错误仍需要人工把关**。
- 各网文平台、出版方对 AI 生成或 AI 辅助的内容有各自的规定，并且在不断变化。投稿或发布前，请自行确认目标平台的最新要求。
- 你对用本软件创作和发布的内容负责。请勿用于生成违法、侵权或违反所用模型服务条款的内容。

## 项目结构

```
src/
  main/       主进程：模型调用、题材雷达、建书、写作、审稿、裁判、导入导出、升级
  preload/    主进程与界面之间的接口
  renderer/   界面（React）
  shared/     两边共用的类型和规则
scripts/      免安装版打包脚本
docs/         使用说明书（user-guide.md）、开发者指南、截图
i18n-draft/   英文界面翻译草稿（未启用）
```

技术栈：Electron + React + TypeScript + electron-vite。常用命令：

| 命令 | 作用 |
|---|---|
| `npm run dev` | 开发模式运行 |
| `npm run typecheck` | 类型检查 |
| `npm run dist:win-zip` | 打包 Windows 免安装版（`dist/win-portable` 和一键升级用的 zip） |
| `npm run dist:mac` | 打包 Mac 版（需在 Mac 上执行） |

## 参与贡献

欢迎提交 [Issue](https://github.com/AceSpike/StarT-Novel/issues) 和 Pull Request。提交问题时请附上软件版本号（左下角）、所用模型和"运行日志"里的相关内容；**截图和日志里不要包含你的 API Key**。

## 许可证

本项目以 [GNU General Public License v3.0](LICENSE) 发布：你可以自由使用、修改和分发，但发布修改后的版本时，也必须以 GPL-3.0 开源并提供源代码。

Copyright © 2026 Spike
