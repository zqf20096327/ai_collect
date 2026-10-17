# MCAA - Minecraft AI Agent

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE.txt) [![Minecraft](https://img.shields.io/badge/Minecraft-1.21.11-brightgreen.svg)](https://www.minecraft.net/) [![Fabric](https://img.shields.io/badge/Mod_Loader-Fabric-orange.svg)](https://fabricmc.net/) [![Java](https://img.shields.io/badge/Java-21+-red.svg)](https://adoptium.net/)

> **注意：这是一个学习性质的项目，作者不再主动维护，但欢迎社区贡献和改进**

将 AI Agent 智能集成到 Minecraft 中 - 通过大语言模型让 AI 理解游戏世界、执行任务、与玩家对话、自主建造。

[English](#english) | [中文文档](#中文文档)

---

## 中文文档

### 简介

MCAA (Minecraft AI Agent) 是一个 Fabric 模组，将大语言模型 (LLM) 的强大能力带入 Minecraft 世界。通过多 Agent 协作架构，AI 可以理解游戏环境、执行复杂任务、与玩家对话，甚至自主建造结构。

### 特性

#### 多 Agent 架构
- **Master Agent** - 主控 Agent，负责理解玩家意图并协调其他 Agent
- **Commander Agent** - 指挥 Agent，执行命令和脚本查询
- **Builder Agent** - 建造 Agent，负责方块放置和结构建造
- **Scout Agent** - 侦查 Agent，收集环境信息和截图

#### 丰富的工具集
| 类别 | 工具 | 功能 |
|------|------|------|
| 侦查 | `scan_area` | 扫描指定区域的方块信息 |
| 侦查 | `get_block_detail` | 获取特定方块的详细信息 |
| 侦查 | `get_player_status` | 获取玩家状态（生命值、位置等）|
| 侦查 | `get_inventory_content` | 查看物品栏内容 |
| 侦查 | `get_environment_info` | 获取环境信息（天气、时间等）|
| 侦查 | `find_path` | 寻路到指定位置 |
| 侦查 | `capture_screenshot` | 捕获游戏截图 |
| 建造 | `build_structure` | 根据蓝图建造结构 |
| 建造 | `fill_region` | 填充区域 |
| 建造 | `undo_last_build` | 撤销上次建造 |
| 指挥 | `execute_command` | 执行 Minecraft 命令 |
| 指挥 | `execute_script` | 执行 JavaScript 脚本 |
| 指挥 | `query_knowledge` | 查询内置知识库 |
| 主控 | `delegate_agent` | 委托任务给特定 Agent |
| 主控 | `reply_to_player` | 回复玩家消息 |

#### JavaScript 脚本支持
内置 Mozilla Rhino JavaScript 引擎，提供安全的沙箱执行环境：
- `BlockApi` - 方块操作
- `PlayerApi` - 玩家操作
- `WorldApi` - 世界操作
- `EntityApi` - 实体操作
- `InventoryApi` - 物品栏操作
- `CommandApi` - 命令执行
- `UtilityApi` - 工具函数

#### 其他特性
- Web UI 配置界面 (http://localhost:9178)
- 可视化记忆系统
- 内置 Minecraft 知识库
- 支持多种 LLM API（OpenAI 兼容接口）
- 关键词触发（默认 `@AI`）
- 断路器保护机制

### 安装

#### 前置要求
- Minecraft 1.21.11
- Fabric Loader 0.18.4+
- Fabric API
- Java 21+

#### 安装步骤
1. 安装 Fabric Loader（参考 [Fabric 官网](https://fabricmc.net/use/)）
2. 下载 [Fabric API](https://modrinth.com/mod/fabric-api)
3. 下载 MCAA 最新版本
4. 将模组放入 `.minecraft/mods` 目录

### 配置

#### 首次使用
1. 启动游戏
2. 在浏览器打开 http://localhost:9178
3. 配置以下信息：
   - **API 端点** - LLM API 地址（如 OpenAI、本地 Ollama 等）
   - **API Key** - 认证密钥
   - **模型 ID** - 要使用的模型名称

#### 配置文件
配置文件位于 `.minecraft/config/mcaa.json`，支持热重载。

### 使用方法

#### 命令方式
```
/mcaa <你的问题或指令>
```

#### 关键词触发
在聊天框中输入包含触发词的消息（默认 `@AI`）：
```
@AI 帮我在当前位置建造一座小房子
```

### 开发

#### 环境搭建
```bash
# 克隆仓库
git clone https://github.com/enabot81/MCAA.git
cd MCAA

# 构建项目
./gradlew build
```

#### 项目结构
```
src/
├── main/
│   ├── java/org/ena/mcaa/
│   │   ├── agent/          # Agent 实现
│   │   ├── api/            # LLM API 客户端
│   │   ├── config/         # 配置管理
│   │   ├── interaction/    # 交互处理
│   │   ├── knowledge/      # 知识库
│   │   ├── memory/         # 记忆系统
│   │   ├── network/        # 网络通信
│   │   ├── script/         # 脚本引擎
│   │   ├── tool/           # 工具实现
│   │   ├── webui/          # Web 界面
│   │   └── ...
│   └── resources/
│       ├── assets/         # 资源文件
│       ├── web/            # Web UI 资源
│       └── fabric.mod.json
└── client/                 # 客户端专用代码
```

### 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 提交 Pull Request

### 许可证

本项目基于 [MIT 许可证](LICENSE.txt) 开源。

---

## English

### Introduction

MCAA (Minecraft AI Agent) is a Fabric mod that brings the power of Large Language Models (LLM) into Minecraft. Through a multi-agent collaborative architecture, the AI can understand the game environment, execute complex tasks, chat with players, and even build structures autonomously.

### Features

#### Multi-Agent Architecture
- **Master Agent** - The orchestrator agent responsible for understanding player intent and coordinating other agents
- **Commander Agent** - The commander agent that executes commands and script queries
- **Builder Agent** - The builder agent handling block placement and structure building
- **Scout Agent** - The scout agent that gathers environment information and screenshots

#### Rich Tool Set
| Category | Tool | Description |
|----------|------|-------------|
| Scout | `scan_area` | Scan block information in a specified area |
| Scout | `get_block_detail` | Get detailed information about a specific block |
| Scout | `get_player_status` | Get player status (health, position, etc.) |
| Scout | `get_inventory_content` | View inventory contents |
| Scout | `get_environment_info` | Get environment info (weather, time, etc.) |
| Scout | `find_path` | Find path to a specified location |
| Scout | `capture_screenshot` | Capture game screenshot |
| Builder | `build_structure` | Build structure based on blueprint |
| Builder | `fill_region` | Fill a region with blocks |
| Builder | `undo_last_build` | Undo the last build operation |
| Commander | `execute_command` | Execute Minecraft commands |
| Commander | `execute_script` | Execute JavaScript scripts |
| Commander | `query_knowledge` | Query built-in knowledge base |
| Master | `delegate_agent` | Delegate task to a specific agent |
| Master | `reply_to_player` | Reply to player messages |

#### JavaScript Scripting Support
Built-in Mozilla Rhino JavaScript engine with secure sandbox execution environment:
- `BlockApi` - Block operations
- `PlayerApi` - Player operations
- `WorldApi` - World operations
- `EntityApi` - Entity operations
- `InventoryApi` - Inventory operations
- `CommandApi` - Command execution
- `UtilityApi` - Utility functions

#### Other Features
- Web UI configuration interface (http://localhost:9178)
- Visual memory system
- Built-in Minecraft knowledge base
- Support for multiple LLM APIs (OpenAI compatible endpoints)
- Keyword triggering (default: `@AI`)
- Circuit breaker protection mechanism

### Installation

#### Requirements
- Minecraft 1.21.11
- Fabric Loader 0.18.4+
- Fabric API
- Java 21+

#### Installation Steps
1. Install Fabric Loader (see [Fabric website](https://fabricmc.net/use/))
2. Download [Fabric API](https://modrinth.com/mod/fabric-api)
3. Download the latest version of MCAA
4. Place the mod in `.minecraft/mods` directory

### Configuration

#### First Time Setup
1. Launch the game
2. Open http://localhost:9178 in your browser
3. Configure the following:
   - **API Endpoint** - LLM API address (e.g., OpenAI, local Ollama, etc.)
   - **API Key** - Authentication key
   - **Model ID** - The model name to use

#### Configuration File
Configuration file is located at `.minecraft/config/mcaa.json`, supports hot reload.

### Usage

#### Command Method
```
/mcaa <your question or command>
```

#### Keyword Trigger
Enter a message containing the trigger word (default `@AI`) in chat:
```
@AI Help me build a small house at my current location
```

### Development

#### Environment Setup
```bash
# Clone the repository
git clone https://github.com/enabot81/MCAA.git
cd MCAA

# Build the project
./gradlew build
```

#### Project Structure
```
src/
├── main/
│   ├── java/org/ena/mcaa/
│   │   ├── agent/          # Agent implementations
│   │   ├── api/            # LLM API client
│   │   ├── config/         # Configuration management
│   │   ├── interaction/    # Interaction handling
│   │   ├── knowledge/      # Knowledge base
│   │   ├── memory/         # Memory system
│   │   ├── network/        # Network communication
│   │   ├── script/         # Script engine
│   │   ├── tool/           # Tool implementations
│   │   ├── webui/          # Web UI
│   │   └── ...
│   └── resources/
│       ├── assets/         # Resource files
│       ├── web/            # Web UI resources
│       └── fabric.mod.json
└── client/                 # Client-only code
```

### Contributing

Issues and Pull Requests are welcome!

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### License

This project is licensed under the [MIT License](LICENSE.txt).

---

Made with ❤️ by ENA