<div align="center">
  <img src="./docs/imgs/readme/logo.png" width="120" height="120" alt="随风画布">
  <h1>随风画布 · Suifeng Canvas</h1>
  <h3>基于节点画布的 AI 分镜工作台，一站式完成图片生成、编辑与分镜流程</h3>

  [![Release](https://img.shields.io/github/v/release/rickSF/Suifeng-Canvas?style=flat&color=blue)](https://github.com/rickSF/Suifeng-Canvas/releases/latest)
  [![License](https://img.shields.io/github/license/rickSF/Suifeng-Canvas?style=flat)](./LICENSE)
</div>

---

## 简介

**随风画布**（Suifeng Canvas）是一款面向 AI 内容创作者的桌面工具，基于可视化节点画布，将文生图、图生图、图片编辑、分镜生成等 AI 能力串联成一条流畅的创作流水线。

无论是制作短剧分镜、概念设计还是多模态内容探索，随风画布都能让你的想法快速落地。

---

## 下载

Windows 请下载 `.exe`，macOS 请下载 `.dmg`

[![Download Latest Release](https://img.shields.io/github/v/release/rickSF/Suifeng-Canvas?style=for-the-badge&color=blue&label=立即下载)](https://github.com/rickSF/Suifeng-Canvas/releases/latest)

> Windows 用户若启动时报错，请先安装 [WebView2 运行时](https://developer.microsoft.com/zh-cn/Microsoft-edge/webview2#download)

---

## 功能亮点

- **节点画布**：基于 `@xyflow/react` 的可视化节点编辑，所见即所得
- **多模型接入**：支持 Seedream、Gemini、Nano Banana、GRSai 等主流图像生成模型
- **图片编辑节点**：裁剪、缩放、旋转、标注一体化
- **分镜生成**：将参考图自动拆分为故事板分镜，适合短剧 / 漫剧创作
- **文生图 / 图生图**：统一 API 层，轻松扩展新模型
- **自动持久化**：SQLite 本地存储，无需手动保存
- **明暗主题**：内置明暗双主题切换
- **中英文双语**：完整 i18n 支持

---

## 技术栈

| 层级 | 技术 |
|------|------|
| 前端框架 | React 18 + TypeScript |
| 状态管理 | Zustand 5 |
| 画布引擎 | @xyflow/react 12 |
| 样式 | TailwindCSS 3 |
| 桌面容器 | Tauri 2 |
| 后端 | Rust |
| 数据库 | SQLite（rusqlite，WAL 模式）|
| 国际化 | react-i18next + i18next |

---

## 开发环境准备

**依赖：**
- Node.js 20+
- npm 10+
- Rust stable（含 Cargo）
- Tauri 2 平台依赖

平台安装指引见：[基础工具安装配置（Windows / macOS）](./docs/development-guides/base-tools-installation.md)

---

## 快速开始

```bash
# 安装依赖
npm install

# 纯前端预览
npm run dev

# Tauri 联调（推荐）
npm run tauri dev
```

---

## 常用命令

```bash
# TypeScript 类型检查
npx tsc --noEmit

# Rust 快速检查
cd src-tauri && cargo check

# 前端构建
npm run build

# 构建桌面安装包
npm run tauri build
```

---

## 一键发布

```bash
# patch 版本递增，写入本次更新说明
npm run release -- patch "修复 xx bug；优化 xx 体验"

# 或指定完整版本号
npm run release -- 1.1.0 "新增分镜批量裁剪工具"
```

执行后会自动同步版本号、创建 tag、触发 GitHub Actions 构建并发布 Release。

---

## 项目结构

```
src/
  features/canvas/     # 画布主流程（节点、工具、模型、UI）
  stores/              # 全局状态与自动持久化
  commands/            # 前端 → Tauri 命令桥接
  i18n/                # 国际化入口与语言包
src-tauri/src/
  commands/            # Rust 命令实现（含 SQLite 持久化）
  lib.rs               # Tauri 命令注册入口
docs/development-guides/  # 开发与扩展文档
```

---

## 扩展开发

### 新增模型
1. 在 `src/features/canvas/models/image/<provider>/` 新建模型文件
2. 声明 `displayName`、`providerId`、`resolveRequest`

### 新增工具
1. `tools/types.ts` 声明能力
2. `tools/builtInTools.ts` 注册
3. `ui/tool-editors/` 写编辑器 UI
4. `application/toolProcessor.ts` 接入执行

### 新增节点
1. `canvasNodes.ts` 增加类型
2. `nodeRegistry.ts` 注册
3. `nodes/index.ts` 注册渲染组件

详细文档：
- [项目开发环境与注意事项](./docs/development-guides/project-development-setup.md)
- [供应商与模型扩展指南](./docs/development-guides/provider-and-model-extension.md)

---

## 数据说明

- 自动持久化，无需手动保存
- SQLite 文件位于 Tauri `app_data_dir/projects.db`
- 图片通过 `imagePool + __img_ref__` 去重编码，同一张图只存一次

---

## Star History

如果本项目对你有帮助，欢迎 ⭐ Star 支持！
