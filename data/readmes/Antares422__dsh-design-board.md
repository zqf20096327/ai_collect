# dsh-design-board

[![CI](https://github.com/Antares422/dsh-design-board/actions/workflows/ci.yml/badge.svg)](https://github.com/Antares422/dsh-design-board/actions/workflows/ci.yml)
[![npm](https://img.shields.io/npm/v/dsh-design-board?color=0071e3)](https://www.npmjs.com/package/dsh-design-board)
[![License: MIT](https://img.shields.io/badge/License-MIT-1d1d1f.svg)](LICENSE)
[![DSH](https://img.shields.io/badge/DSH-%3E%3D0.2.0--0%20%3C0.3.0-0071e3.svg)](https://github.com/deepseek-ai/deepseek-harness)

中文 | [English](README.en.md)

**给 DeepSeek Harness 装上一块设计画布。**

从内置的 165 套设计体系里挑好风格，说一句需求，可交互的页面就会在右侧画布直接展开。支持单页精修，也能把多个方案同屏并排对比；哪里不满意，直接在画布上点选或框选元素留句话就能改——不用来回切浏览器，也不用再截图圈位置了。

![dsh-design-board 演示](docs/assets/demo.gif)

## 核心功能

- **165 套内置设计体系**：涵盖 Apple、Linear、Airbnb、Stripe、Notion、Vercel 等风格，每套均包含设计规范、CSS 变量表与参考组件。在右上角预览并选用后，AI 即按该规范直接出稿；未指定时默认使用 Apple 规范。
- **右侧无限画布与并排对比**：自动渲染 Agent 生成的交互式 HTML 设计稿，支持同屏对比多个方案、滑块或方向键缩放、分页签与全屏查看。
- **点选元素与文字批注**：直接点击或拖拽框选页面内的 DOM 元素并添加备注，精准 CSS 选择器与批注会在下一轮对话自动回传给 Agent 原地更新，无需截图描述。
- **真实交互与深浅主题**：可切换至 Play 模式直接操作页面内的按钮、筛选与标签切换，一键切换浅色或深色主题。
- **质量校验与会话隔离**：自动检测交互可用性、双主题支持与运行时报错，问题静默回传原地修复；每个会话独立使用 `design/<sessionId>/` 目录，互不串台。
- **多格式导出**：支持单帧或整页导出为 PNG、多页 PDF 或单文件 HTML 画廊。

## 界面预览

### 内置 165 套设计体系
![内置 165 套设计体系](docs/assets/presets.jpg)

### 多方案并排对比
![多方案并排对比](docs/assets/canvas-compare.jpg)

### 画布内点选与框选元素
![画布内点选与框选元素](docs/assets/element-pick.jpg)

## 安装

### 在 DSH 应用内安装

打开 **插件 → 添加插件**，输入包名并安装启用：

```text
dsh-design-board
```

或者直接在对话框发送：

```text
帮我安装这个插件：https://github.com/Antares422/dsh-design-board
```

### 通过 CLI 安装

```bash
# 从 npm 安装
dsh plugin --profile web add dsh-design-board

# 从 GitHub 安装
dsh plugin --profile web add "github:Antares422/dsh-design-board"
```

使用 DSH 桌面端时建议直接在应用内的「插件 → 添加插件」安装，以免装入 `web` 配置目录。仓库与 npm 均包含预构建产物，安装后无需本地编译。

## 使用示例

安装启用后直接正常对话即可：

- 「给我两个不同方向的 AI 接口用量监控面板」
- 「用 Linear 风格设计一个 API 配额管理台」
- 点右上角「设计体系」选中任意风格后，发：「按我选的风格再出一版」
- 在画布内点选或框选目标元素并添加批注后，发：「按我圈的改一下」

## 快捷键

| 快捷键 | 说明 |
| --- | --- |
| `V` | 选择与框选元素 |
| `H` | 拖拽平移画布 |
| `T` | 添加文字批注 |
| `E` | 橡皮擦 |
| `I` | Play 交互模式 |
| `←` / `→` | 缩小 / 放大画布 |
| `Esc` | 退出全屏或清空选中 |

## 隐私与安全

全部预设读取、画布渲染、元素捕获与文件导出均在本机运行，无遥测、无外部数据上报、无需登录任何账号。源码完全公开，CI 自动运行全部 136 项单元测试。

## 本地开发

```bash
npm install
npm run build
npm test
```

## 许可协议

[MIT](LICENSE)
