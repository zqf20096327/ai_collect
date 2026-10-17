<div align="center">

# 🎯 Screen Skills - Screenshot Automation

**让 AI 助手自动化你的截图工作流 | Automate Screenshot Workflows with AI**

[![macOS](https://img.shields.io/badge/macOS-Supported-blue.svg)](https://www.apple.com/macos/)
[![Windows](https://img.shields.io/badge/Windows-Supported-blue.svg)](https://www.microsoft.com/windows/)
[![Linux](https://img.shields.io/badge/Linux-Supported-blue.svg)](https://www.linux.org/)
[![Python](https://img.shields.io/badge/Python-3.x-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/LangQi99/screen-skills/pulls)

> 写一个计算 pi 的小论文 写 md 记得把代码运行截图也写到 md 里面 @skill.md

<!-- <p align="center">
  <img src="image/README/1767172997101.png" alt="Demo 1" width="45%" style="display:inline-block;margin-right:3%;">
  <img src="image/README/1767172959058.png" alt="Demo 2" width="45%" style="display:inline-block;">
</p> -->

<p align="center">
  <img src="image/README/1767172997101.png" alt="Demo 1">
  <img src="image/README/1767172959058.png" alt="Demo 2">
</p>

[English](#english) | [中文](#chinese)

</div>

---

## <a name="chinese"></a>🇨🇳 中文文档

### 📖 项目简介

**Screen Skills** 是一个专为 LLM（大语言模型）设计的技能库，使 AI 助手能够智能地捕获 macOS 屏幕截图。这个项目特别适合需要在文档、论文或演示中嵌入实时截图的场景。正在开发中，欢迎 star 和 fork，预计支持 Windows 和 Linux。

通过简单的提示词，AI 助手可以：

- 🤖 **自动运行代码**并截取终端输出
- 📸 **智能识别窗口**并精准截图
- 📝 **直接嵌入**截图到 Markdown 文档
- ⚡ **零人工干预**完成整个工作流

### ✨ 核心特性

#### 🎨 智能截图能力

- **全屏截图** - 捕获整个屏幕
- **窗口截图** - 精准捕获特定应用窗口（Chrome、终端、VSCode 等）
- **窗口识别** - 自动列出所有可用窗口，支持中英文应用名
- **模糊匹配** - 智能匹配窗口名称（如"Safari"匹配"Safari 浏览器"）

#### 🚀 实用场景

##### 📚 学术论文与作业

- 自动运行实验代码并截取结果
- 生成包含运行截图的完整实验报告
- 适用于数值分析、算法设计等课程作业

##### 🎓 技术文档

- 自动化 API 调用演示
- 截取命令行工具的输出结果
- 生成带截图的教程文档

##### 🎬 产品演示

- 捕获软件界面的实时状态
- 创建包含实际运行截图的演示文稿
- 自动化测试结果文档

##### 💻 代码示例

- 展示程序实际运行效果
- 验证算法正确性
- 创建交互式代码教程

### 📦 快速开始

#### 安装依赖

```bash
# 克隆仓库
git clone https://github.com/LangQi99/screen-skills.git
cd screen-skills
```

**macOS:**

```bash
# Python 3.x（默认已安装）
# Swift编译器（默认已安装）
```

**Windows:**

```bash
# Python 3.x（从 python.org 下载安装）
# 安装依赖
pip install pywin32 pillow
```

**Linux:**

```bash
# Python 3.x（通常已预装）
# 安装依赖
pip3 install python-xlib

# 安装截图工具（至少安装一个）
sudo apt-get install scrot imagemagick  # Ubuntu/Debian
# 或
sudo dnf install scrot ImageMagick      # Fedora/RHEL
# 或
sudo pacman -S scrot imagemagick        # Arch Linux
```

#### 权限设置

首次使用时，macOS 可能会要求授予以下权限：

- ✅ **屏幕录制权限** - 用于截取屏幕
- ✅ **系统事件控制** - 用于检测活动窗口

前往 `系统偏好设置 > 安全性与隐私 > 隐私` 进行授权。

#### 基础用法

**macOS:**

```bash
# 1. 列出所有窗口
python3 capture-screen-macos/window_info.py list

# 2. 全屏截图
python3 capture-screen-macos/screenshot.py full output.png

# 3. 窗口截图
python3 capture-screen-macos/screenshot.py window "终端" terminal.png
```

**Windows:**

```bash
# 1. 列出所有窗口
python capture-screen-windows/window_info.py list

# 2. 全屏截图
python capture-screen-windows/screenshot.py full output.png

# 3. 窗口截图
python capture-screen-windows/screenshot.py window "Chrome" chrome.png
```

**Linux:**

```bash
# 1. 列出所有窗口
python3 capture-screen-linux/window_info.py list

# 2. 全屏截图
python3 capture-screen-linux/screenshot.py full output.png

# 3. 窗口截图
python3 capture-screen-linux/screenshot.py window "Firefox" firefox.png
```

### 🎯 实战案例

#### 案例一：AI 自动生成论文

只需一条提示词，AI 即可完成从代码编写到截图嵌入的全流程：

```
写一个计算pi的小论文（蒙特卡洛方法）
写成md格式，记得把代码运行截图也写到md里面
使用skill自动截图，记得打开一个原生终端去运行
```

**AI 会自动完成：**

1. ✍️ 创建 Python 计算脚本
2. 🖥️ 在终端中运行代码
3. 📸 列出窗口并截取终端输出
4. 📄 生成包含截图的完整论文

查看完整示例：[examples/cal.md](examples/cal.md)

#### 案例二：自动化测试文档

```python
# AI可以自动运行测试并截图
python3 run_tests.py

# 然后自动截取测试结果窗口
python3 capture-screen-macos/screenshot.py window "终端" test_results.png
```

### 🛠️ 技术细节

#### 窗口识别原理

项目使用 Swift 的 `Accessibility API`和 `CGWindowListCopyWindowInfo`获取窗口信息：

- 精确获取窗口 ID、标题、位置、大小
- 支持多语言应用名称
- JSON 格式输出，易于解析

#### 截图技术

使用 macOS 原生的 `screencapture`命令：

- 高质量 PNG 格式
- 支持特定窗口 ID 截图
- 零外部依赖

### 📚 文档

- [完整使用指南](capture-screen-macos/skill.md)
- [示例项目](examples/)
- [API 参考](capture-screen-macos/)

### 🤝 贡献指南

我们欢迎所有形式的贡献！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

### 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

### 🌟 致谢

- 感谢 OpenAI 和 Anthropic 推动 LLM 技术发展
- 感谢所有贡献者和使用者

---

## <a name="english"></a>🇺🇸 English Documentation

### 📖 Introduction

**screen Skills** is a skill library designed for LLMs (Large Language Models) to intelligently capture screenshots across **macOS**, **Windows**, and **Linux** platforms. This project is particularly useful for scenarios requiring embedded real-time screenshots in documents, papers, or presentations.

With simple prompts, AI assistants can:

- 🤖 **Automatically run code** and capture terminal output
- 📸 **Intelligently identify windows** and take precise screenshots
- 📝 **Directly embed** screenshots into Markdown documents
- ⚡ **Zero manual intervention** for the entire workflow

### ✨ Key Features

#### 🎨 Smart Screenshot Capabilities

- **Full Screen Capture** - Capture the entire screen
- **Window Capture** - Precisely capture specific application windows (Chrome, Terminal, VSCode, etc.)
- **Window Recognition** - Automatically list all available windows, supporting both English and localized app names
- **Fuzzy Matching** - Intelligently match window names (e.g., "Safari" matches "Safari 浏览器")

#### 🚀 Use Cases

##### 📚 Academic Papers & Assignments

- Automatically run experimental code and capture results
- Generate complete experiment reports with runtime screenshots
- Suitable for numerical analysis, algorithm design coursework

##### 🎓 Technical Documentation

- Automate API call demonstrations
- Capture command-line tool outputs
- Generate tutorial documents with screenshots

##### 🎬 Product Demonstrations

- Capture real-time software interface states
- Create presentations with actual runtime screenshots
- Automate test result documentation

##### 💻 Code Examples

- Show actual program execution results
- Verify algorithm correctness
- Create interactive code tutorials

### 📦 Quick Start

#### Installation

```bash
# Clone repository
git clone https://github.com/LangQi99/screen-skills.git
cd screen-skills
```

**macOS:**

```bash
# Python 3.x (pre-installed)
# Swift compiler (pre-installed)
```

**Windows:**

```bash
# Python 3.x (download from python.org)
# Install dependencies
pip install pywin32 pillow
```

**Linux:**

```bash
# Python 3.x (usually pre-installed)
# Install dependencies
pip3 install python-xlib

# Install screenshot tools (install at least one)
sudo apt-get install scrot imagemagick  # Ubuntu/Debian
# or
sudo dnf install scrot ImageMagick      # Fedora/RHEL
# or
sudo pacman -S scrot imagemagick        # Arch Linux
```

#### Permissions Setup

On first use, macOS may request the following permissions:

- ✅ **Screen Recording** - For capturing screens
- ✅ **System Events Control** - For detecting active windows

Navigate to `System Preferences > Security & Privacy > Privacy` to authorize.

#### Basic Usage

```bash
# 1. List all windows
python3 capture-screen-macos/window_info.py list

# 2. Full screen capture
python3 capture-screen-macos/screenshot.py full output.png

# 3. Window capture
python3 capture-screen-macos/screenshot.py window "Terminal" terminal.png
```

### 🎯 Real-World Examples

#### Example 1: AI-Generated Paper

With a single prompt, AI completes the entire workflow from code writing to screenshot embedding:

```
Write a short paper about computing pi (Monte Carlo method)
Format as markdown, include code execution screenshots
Use skill for automatic screenshots, open a native terminal to run
```

**AI automatically:**

1. ✍️ Creates Python calculation script
2. 🖥️ Runs code in terminal
3. 📸 Lists windows and captures terminal output
4. 📄 Generates complete paper with embedded screenshots

View complete example: [examples/计算 π 的蒙特卡洛方法.md](examples/计算π的蒙特卡洛方法.md)

### 🛠️ Technical Details

#### Window Recognition Mechanism

Uses Swift's `Accessibility API` and `CGWindowListCopyWindowInfo`:

- Precisely retrieves window ID, title, position, size
- Supports multilingual application names
- JSON format output for easy parsing

#### Screenshot Technology

Uses macOS native `screencapture` command:

- High-quality PNG format
- Supports specific window ID capture
- Zero external dependencies

### 📚 Documentation

- [Complete Usage Guide](capture-screen-macos/skill.md)
- [Example Projects](examples/)
- [API Reference](capture-screen-macos/)

### 🤝 Contributing

We welcome all forms of contributions!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details

### 🌟 Acknowledgments

- Thanks to OpenAI and Anthropic for advancing LLM technology
- Thanks to all contributors and users

---

<div align="center">

**如果这个项目对你有帮助，请给我们一个 ⭐️**

**If this project helps you, please give us a ⭐️**

Made with ❤️ for the AI community

</div>
