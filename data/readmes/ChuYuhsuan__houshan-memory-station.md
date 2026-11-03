# 厚山忆站 · 复习小助手

> 面向医学考研的资料驱动 AI 复习助手。把遗忘曲线、上传资料、AI 出题、批改与组卷串成一条能每天执行的复习闭环。

![平台](https://img.shields.io/badge/platform-Windows%2010%2F11-0078D4)
![Electron](https://img.shields.io/badge/Electron-44-47848F)
![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/version-3.2.2-2F6F5E)

![厚山忆站智能体界面](docs/screenshots/agent.png)

更多截图：[多维分析](docs/screenshots/analytics.png) · [夜间模式](docs/screenshots/analytics-dark.png) · [组卷](docs/screenshots/paper-builder.png)

## 这是什么

西医综合考研的知识点多、遗忘快，常见的笔记工具、刷题 App 和复习计划彼此割裂：资料在一个地方，题目在另一个地方，错题和掌握度又没有回到计划里。

**厚山忆站**是一款 Windows 桌面复习工具：

- 按 `1 / 2 / 4 / 7 / 15 / 30` 天自动排程，基础轮结束后转入滚动复习
- 每个知识点可以挂 PDF、图片、TXT 资料；PDF 本地提取文字，图片用 Windows OCR
- AI 严格依据资料出选择题，答案附逐项解析；没有资料时按人卫版教材与考纲兜底
- 答完自动批改，按知识点累计掌握度；错题进入错题本，可加入补练
- 多知识点组卷，自定义题量、题型、难度、分值与学校试卷头
- AI 智能体自动完成「感知 → 规划 → 调用资料 → 出题 → 作答 → 批改 → 写回掌握度 → 下一步建议」
- 学习效果支持 7/14/30 天、学科正确率、掌握度分布、学习热力图与答题来源分析
- 支持浅色 / 夜间两套皮肤，夜间关闭鼠标聚光、背景光斑、卡片掠光等光效

> 项目名“厚山忆站”取自郑州大学新校区地标“厚山”，并借用“驿站”的谐音：复习是一场长途，这里是可以停靠、整理、再出发的一站。

## 下载与安装

在 GitHub 的 **Releases** 页面下载：

| 文件 | 说明 |
|---|---|
| `复习小助手3.2.2.exe` | 安装版，当前用户安装，创建桌面/开始菜单快捷方式 |
| `复习小助手3.2.2-便携版.exe` | 免安装单文件，适合临时使用 |

系统要求：Windows 10 / 11 x64。

> 安装包约 114 MB，超过 GitHub 普通仓库的单文件限制，请作为 **Release asset** 上传，不要直接 commit 进仓库。安装包未做代码签名，Windows SmartScreen 可能提示“未知发布者”，可核对 Release 中的 SHA-256。

## 快速开始

1. 安装并打开应用。
2. 进入「复习设置 → AI 服务」，填写兼容 OpenAI Chat Completions 的接口地址、模型与 API Key。
   - 默认接口：`https://api.deepseek.com`
   - 默认模型：`deepseek-chat`
3. 在「添加知识点」中录入知识点，可同时上传资料。
4. 打开「AI 训练 → 智能体」，点「开始今日任务」。
5. 答完题后查看逐项解析与掌握度；可在「学习效果」看多维分析。
6. 需要整卷练习时，进入「AI 训练 → 试卷 → 新建试卷」。

## 功能地图

| 入口 | 作用 |
|---|---|
| 今日复习 | 按遗忘曲线列出今天要复习的知识点 |
| 添加知识点 | 录入知识点，支持创建时上传资料 |
| 我的知识库 | 搜索、筛选、批量管理、导入导出 |
| AI 训练 → 智能体 | 自动选点、调用资料、出题、批改、回写掌握度 |
| AI 训练 → 试卷 | 多知识点组卷、批改、导出 Word / 打印 |
| AI 训练 → 错题 | 错题重练、加入补练、标记掌握 |
| 记忆数据 | 记忆概览、学习效果、掌握度与薄弱点 |
| 复习设置 | 复习节奏、AI 服务、考试命题、数据与隐私 |

## AI 配置与隐私

- API Key 使用 Electron `safeStorage`（Windows DPAPI）加密保存在本机，不写入安装包与源码。
- 应用不上传账号、密码或学校系统数据，也没有遥测。
- 使用 AI 时，会把当前知识点的资料节选、题干、选项与你的追问发送到你配置的模型接口；请确认所用模型服务的数据条款。
- 复习数据、资料、试卷、答题记录、错题本均保存在本机。
- 详细说明见 [PRIVACY.md](PRIVACY.md) 与 [SECURITY.md](SECURITY.md)。

## 数据位置

```
%APPDATA%\复习小助手
  ├─ IndexedDB / Local Storage   复习数据、设置、试卷、答题记录、错题本
  ├─ materials\<知识点ID>\       资料文件与提取文本
  └─ materials\_exam\            样卷 / 历年真题
```

> 从旧版本升级时，应用会尝试迁移 `复习小助手3.0`、`西综艾宾浩斯复习小助手` 等目录；API Key 因系统加密与应用绑定，需要重新填写一次。

## 从源码运行

需要 Node.js 20+ 与 npm。

```bash
npm install
npm start
```

打包 Windows 安装版与便携版：

```bash
npm run dist
```

产物在 `dist/`。如果 Electron 下载较慢，可设置镜像：

```powershell
$env:ELECTRON_MIRROR='https://npmmirror.com/mirrors/electron/'
$env:ELECTRON_BUILDER_BINARIES_MIRROR='https://npmmirror.com/mirrors/electron-builder-binaries/'
npm run dist
```

## 技术栈

- Electron 44 + 单文件 HTML/CSS/原生 JavaScript
- `pdfjs-dist` 本地提取 PDF 文字层
- Windows.Media.Ocr 识别图片文字
- DeepSeek / OpenAI 兼容 Chat Completions，JSON 结构化出题
- IndexedDB / localStorage 本地存储，`safeStorage` 加密 Key

## 已知限制

- AI 生成内容仅作复习提示，医学细节请以教材、指南与原始资料为准。
- 扫描版 PDF 没有文字层，需截图或手动补充文字。
- 图片 OCR 受清晰度影响，可在「文字」中校对。
- 单次组卷 1–20 题，模型单次输出上限约 8000 tokens。
- 试卷、答题记录与错题本保存在本机，不随 JSON 导出。
- 当前没有云端同步与多设备同步。

## 项目背景

本项目为郑州大学首届 AI 智能体创新应用大赛参赛作品，项目名“厚山忆站”。

本项目为个人学习工具，**非郑州大学官方产品**，不代表学校立场；涉及学校名称仅用于项目命名与试卷模板。

## 贡献与安全

- 提交 Issue / PR 前请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 与 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)。
- 发现安全问题时请不要公开 API Key 或用户数据，按 [SECURITY.md](SECURITY.md) 私下报告。

## License

[MIT](LICENSE) © 2026 厚山忆站 contributors
