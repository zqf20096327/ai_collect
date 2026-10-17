[简体中文](README.md) | [English](README_EN.md)

# oshwhub-readme-skill

用于 [立创开源广场 (OSHWHUB)](https://oshwhub.com/) 硬件开源项目展示页面生成的 AI Skill。让 AI Agent 自动生成产品级展示页面，包含功能介绍、硬件详解、BOM清单、3D外壳展示等模块。

## 使用前准备

在使用本 Skill 之前，请先在你的项目文件夹中准备好以下文件：

### 1. 图片文件（放入 `img/` 文件夹）

图片使用**中文或英文文字描述命名**，Skill 会根据文件名中的描述自动匹配到对应的页面模块，无需固定命名格式。

命名示例：
```
img/
├── ESP32智能小车正面渲染图.png       → 自动匹配到 Hero 主图
├── 项目组成架构图.png                → 自动匹配到 组成图
├── 蓝牙遥控功能展示.png              → 自动匹配到 功能介绍
├── PCB设计图.png                     → 自动匹配到 硬件详解
├── 原理图截图.png                    → 自动匹配到 硬件详解
├── 3D外壳正面.png                    → 自动匹配到 3D外壳
├── BOM元器件清单截图.png             → 自动匹配到 BOM清单
└── 引脚定义图.png                    → 自动匹配到 引脚说明
```

> 💡 命名建议：使用能描述图片内容的文字，如"产品主图"、"PCB布局"、"功能演示"等。

### 2. 项目源码（放入 `code/` 文件夹）

将你的项目源代码文件放入 `code/` 文件夹。Skill 会自动读取源码结构，在"源码介绍"模块中生成目录树和关键文件说明。

```
code/
├── src/
│   ├── main.cpp
│   └── config.h
├── platformio.ini
└── README.md
```

### 3. 嘉立创EDA 导出文件（放入 `SRC/` 文件夹）

如果你的项目有原理图和 PCB，请从嘉立创EDA中导出以下文件并放入 `SRC/` 文件夹：

- **BOM 表**：嘉立创EDA → 原理图 → 导出 BOM（`.csv` 或 `.xlsx` 格式）
- **网表文件**：嘉立创EDA → PCB → 导出网表（`.enet` 格式，嘉立创EDA专用 JSON 网表）

Skill 会自动读取 BOM 文件，在页面中生成元器件清单表格。

```
SRC/
├── BOM_项目名称.csv
└── 网表_项目名称.enet
```

### 4. 准备完成后

在项目根目录启动 AI Agent，加载 Skill 后即可开始生成展示页面。Skill 会自动扫描上述文件夹，读取并处理所有已准备的文件。

## 功能特性

- 参考专业产品展示风格，生成美观的 HTML 页面
- 仅生成 `<body>` 内容，所有样式使用内联 `style` 属性，无 `<style>` 和 `<script>` 标签
- 自动预留 `<img>` 图片占位符，生成图片清单供用户准备
- 自动创建 `img/`、`code/`、`SRC/` 文件夹结构
- 支持深色模式，使用 `light-dark()` CSS 函数
- 模块化设计：根据项目类型自动选择需要展示的模块

## 安装说明

### 1. 拉取仓库到skill目录

根据你使用的 AI Agent 文档，找到或创建存放 Skill 的目录：

```bash
git clone https://github.com/easyeda/oshwhub-readme-skill
```

例如：

> **Claude Code**
> **用户作用域**：位于 ~/.claude/skills，对本机所有项目生效
> 进入到对应的skills文件夹下
> 在终端执行`git clone https://github.com/easyeda/oshwhub-readme-skill`即可

> **QwenCode**
> **项目作用域**：位于项目根目录下的 .qwen/skills
> **用户作用域**：位于 ~/.qwen/skills，对本机所有项目生效
> 进入到对应的skills文件夹下
> 在终端执行`git clone https://github.com/easyeda/oshwhub-readme-skill`即可

### 2. 使用指定skill

在你的 AI Agent 中确认 Skill 已加载，可通过命令指定skill。

例如：

> **Claude Code**
> 在对话中输入`/oshwhub-readme-skill`或说"帮我生成一个开源项目展示页面"

> **QwenCode**
> **1.进入终端**：在终端中输入`qwen`后回车
> **2.指定skill并发送需求**：在QwenCode的CLI中输入`/skills`回车
> 选择要使用的oshwhub-readme-skill并回车，然后填入你的需求

## 工作原理

Skill 定义了一套工作流，AI Agent 在生成展示页面时会遵循：

| 步骤 | 名称 | 说明 |
|------|------|------|
| 1 | 收集信息 | 通过交互式问答收集项目名称、类型、功能模块等信息 |
| 2 | 确认能力 | 确认项目是否有原理图、PCB、代码、3D外壳 |
| 3 | 创建目录 | 创建 img/、code/ 文件夹，如有原理图+PCB 则创建 SRC/ |
| 4 | 确定图片 | 根据项目类型确定需要的图片列表和命名 |
| 5 | 生成页面 | 生成带图片占位符的 HTML body 内容 |
| 6 | 输出清单 | 提供图片准备清单，告知用户需要准备的图片及要求 |

## 页面模块

根据项目类型自动选择包含的模块：

| 模块 | 说明 | 何时包含 |
|------|------|----------|
| Hero 区域 | 渐变背景，项目名称和简介 | 始终包含 |
| 组成图 | 项目架构/组成概览 | 始终包含 |
| 功能介绍 | 各功能模块详细说明 | 始终包含 |
| 硬件详解 | 硬件模块、引脚定义、技术参数 | 有 PCB 时包含 |
| 3D外壳 | 底壳、顶壳、按键帽展示 | 有 3D 外壳时包含 |
| BOM清单 | 元器件清单表格 | 始终包含 |
| 快速开始 | 环境搭建、编译烧录步骤 | 有代码时包含 |
| 源码介绍 | 代码结构和关键文件说明 | 有代码且放在 code/ 时包含 |
| 相关链接 | 开发资源和技术文档链接 | 始终包含 |

## 设计风格

- 紫色/绿色/蓝色多色主题
- 渐变背景 Hero 区域
- 卡片式功能介绍，圆角 + 阴影
- `light-dark()` 深色模式支持
- 响应式网格布局
- 无空行连续 HTML 输出

## 目录结构

生成后的项目目录结构：

```
project-root/
├── img/              # 用户放置图片
│   ├── hero.png
│   ├── composition.png
│   ├── feature_1.png
│   └── ...
├── code/             # 用户放置项目源码
├── SRC/              # 嘉立创EDA网表和BOM（有原理图+PCB时）
└── index.html        # 生成的展示页面
```

## 已测试的平台

| 平台 | 模型 |
|------|------|
| Claude Code | Claude Opus 4.7 |
| QwenCode | Qwen3-Coder |
| Kiro | Claude Opus4.6 |

