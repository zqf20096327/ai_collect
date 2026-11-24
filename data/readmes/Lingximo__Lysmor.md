# Lysmor

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](LICENSE)
[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Platform: Windows](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](#环境要求)

**可自托管的 AI 伴侣系统（开源参考实现）。**

Lysmor 把一套完整的「AI 伴侣」系统拆成可复用的模块：长期记忆、情绪与生理状态、多端界面（聊天 / 视频通话 / 生命面板 / 记忆星图 / 3D 房间 / 画廊 / 控制台），以及一套灾后备份与复活工具。

所有数据、账号与密钥都只存在于使用者自己的电脑上——不依赖任何云端服务，也不收集任何用户数据。

---

## 功能特性

### 记忆与人格
- **长期记忆库**：文档 + 向量检索 + 图记忆，按重要度 / 相关度 / 时间召回；
- **记忆维护**：只归档不物理删除，支持快照与去重；
- **情绪与生理层**：情绪、饥饿、口渴、睡眠、精力等状态，驱动语气与行为。

### 界面
| 界面 | 说明 |
|---|---|
| 网页聊天 | 浏览器直接访问，不依赖 IM |
| 视频通话 | 实时视频 + 语音 + Live2D 挂件（形象素材自备） |
| 生命面板 | 生理 / 情绪状态可视化，只读仪表与曲线 |
| 记忆星图 | 记忆按主题聚类的可视化星图 |
| 3D 大平层 | 角色"家"的等距 3D 房间，可旋转 / 点击家具 |
| 画廊 | 角色作品陈列与过程展示 |
| 控制台 | 一页总览所有状态 |

### 通道与工具
- **IM 通道**：经 AstrBot + NapCat 接入 QQ（QQ 本体需使用者自行安装）；
- **灾后复活**：定期整包备份 + 分片上传云端 + 换机一键恢复（`tools/nirvana/`）；
- **可视化装机向导**：账号清单、自动装机（Python / Ollama / ffmpeg / 模型）、声纹与人脸登记、素材导入、一键配置与自动体检（`setup/` + `configure.py`）。

---

## 快速开始

### 环境要求
- Windows 10 / 11
- [Python 3.12](https://www.python.org/downloads/)（安装时勾选 **Add to PATH**）
- [Ollama](https://ollama.com/)（本地模型：视觉 `qwen3-vl:4b`、向量 `bge-m3`）
- [AstrBot](https://github.com/AstrBotDevs/AstrBot)（聊天大脑外壳）
- ffmpeg（视频功能）
- 一个 DeepSeek API Key（`platform.deepseek.com`）

> 完整依赖与可选组件见 [`docs/模型需求清单.md`](docs/模型需求清单.md)。

### 三步启动

```text
1. 装环境    按 docs/模型需求清单.md 安装（或直接用向导里的「🔧 自动装机」）
2. 备账号    按 docs/登入清单.md 准备账号与密钥
3. 配置启动  双击 一键配置.cmd →（可选：写「🧬 身份词」→ 点「✨ 用我的 API 优化成提示词」→ 保存）→ 点「⚡ 一键自动配置」→ 双击 打开入口.cmd
```

首次配置完成后，日常使用只需双击 **`打开入口.cmd`**：自动启动服务、自动体检、自动打开总入口。

---

## 素材导入

Live2D 模型、表情包、视频通话背景、桌宠形象都需使用者自备（本项目不附带任何角色形象素材）。打开 **`一键配置.cmd`** → 页面里的 **「🎨 素材导入」** 可直接导入：

| 素材 | 导入位置 |
|---|---|
| Live2D 模型（.moc3 + .model3.json + 贴图文件夹） | `code/video/static/live2d/` |
| 表情包 | `code/assets/stickers/` |
| 视频通话背景（图片 / 视频） | `code/video/static/backgrounds/` |
| 桌宠形象 | `code/app/petweb/whale/` |

素材只保存在本地数据目录，不会上传到任何地方。

---

## 桌面入口（可选）

`code/app/launch_with_check.py` 提供一个带体检的桌面入口：

```bash
python code/app/launch_with_check.py
```

启动前先检查各依赖服务（可视化窗口列出每个服务的在线状态），缺失的自动拉起，
全部就绪后自动打开总入口；有服务未就绪时可以选择「重新检查」或「打开入口」。

---

## 看门狗（可选，推荐）

`code/tools/watch_servers.ps1` 每 3 分钟检查一次：页面服务挂了自动拉起；
同时刷新「情绪真实化」的周期状态（构造情绪 / 预期差）。

**安装一次即可**（右键「以管理员身份运行」）：

```bat
code\tools\install_watchdog.cmd
```

它会注册计划任务 `Companion-Watchdog`（每 3 分钟）。卸载：

```bat
code\tools\install_watchdog.cmd /uninstall
```

> 不做这一步也能跑，只是页面挂了要手动 `restart_bot.ps1`，且「构造情绪」会退回固定标签。

---

## 文档

| 文档 | 内容 |
|---|---|
| [配置清单](docs/配置清单.md) | 从下载到跑起来的完整步骤 |
| [模型需求清单](docs/模型需求清单.md) | 本地模型、软件环境与可选工具 |
| [登入清单](docs/登入清单.md) | 需要准备的账号与密钥 |
| [架构总览](docs/架构总览.md) | 模块关系与数据流 |
| [界面设计](docs/界面设计.md) | 各页面的设计说明 |

---

## 目录结构

```text
├─ README.md               本文件
├─ LICENSE                 许可协议（AGPL-3.0）
├─ SECURITY.md             安全红线与发布前自查
├─ CHANGELOG.md            版本历史
├─ configure.py            一键配置（命令行版）
├─ 一键配置.cmd            双击打开可视化配置向导
├─ 打开入口.cmd            日常入口：起服务 + 自动体检 + 打开总入口
├─ config.example.json     主配置模板（真值在 config.json，不进仓库）
├─ setup/                  可视化配置向导（含素材导入）
├─ docs/                   配置清单、架构、模型、登入、界面设计
├─ code/                   完整参考实现代码
├─ tools/nirvana/          灾后复活工具（打包/上传/恢复/自检/应急包）
├─ services/               可运行的最小示例（聊天/生命/记忆星图/大平层/画廊/控制台）
└─ scripts/                启动脚本模板
```

---

## 常见问题

**双击 `打开入口.cmd` 没反应？**
确认已安装 Python 3.12 并勾选 Add to PATH；也可以先双击 `一键配置.cmd` 查看体检结果。

**页面打不开 / 白屏？**
入口会自动体检并停在体检页，按页面提示逐项修复即可。

**Live2D 形象不显示？**
确认模型已导入 `code/video/static/live2d/`，且目录内含 `.model3.json` 与 `.moc3` 文件。

**只有「控制台」能用，其他卡片全是灰的？**
日常请用 `打开入口.cmd`（或 `scripts\start-all.cmd`）启动正式栈：Hub / 网页聊天 / 视频通话 / 生命面板 / 记忆星图 / 大平层。
Hub 里的「控制台」卡片只是 AstrBot 管理面板，其他卡片需要对应服务在跑；`services\` 下是可独立运行的最小示例，不是日常入口。

**提示 QQ / NapCat 版本不对，要去装旧版本？**
本项目不锁版本，也不附带 NapCat 启动脚本。NapCat 与 QQ 本体请按官方文档安装，并选互相兼容的版本；QQ 通道是可选的，不装也能用网页聊天 / 视频 / 生命面板。

**视频通话怎么「一键部署」？**
`打开入口.cmd` 已经包含视频服务（默认 8003），不需要单独部署。Live2D 形象、通话背景等素材需自备，用配置向导的「🎨 素材导入」导入。

**换电脑了怎么办？**
用 `tools/nirvana/` 恢复：把备份包恢复后运行 `restore.py`，再重新配置即可。

---

## 贡献

欢迎提交 Issue 与 Pull Request。提交前请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 与 [SECURITY.md](SECURITY.md)。

---

## 许可

本项目按 **GNU Affero General Public License v3.0（AGPL-3.0）** 发布，详见 [LICENSE](LICENSE)：

- 可以自由使用、修改、分发；
- 修改后的版本必须同样以 AGPL-3.0 开源；
- 如果把它作为网络服务提供给他人使用，也必须提供对应源码。

第三方组件（模型、Python、AstrBot、Ollama、ffmpeg、QQ、NapCat 等）不属于本项目，各自遵循其官方授权；内置的桌宠表现层代码来自 AGPL 项目，详见 [NOTICE-pet.md](code/app/petweb/NOTICE-pet.md)。

---

## 免责声明

- 本项目不附带任何角色记忆、人格设定、日记或形象素材；
- 使用者在本地养成的角色、产生的数据与账号，完全属于使用者自己；
- 本项目按"现状"提供，维护者不对使用后果承担责任。
