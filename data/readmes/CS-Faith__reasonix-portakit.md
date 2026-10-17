# Reasonix PortaKit

把 Reasonix 装进口袋。U盘一插，记忆和工具全在——换电脑零配置。

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Reasonix](https://img.shields.io/badge/Reasonix-Ecosystem-58a6ff)](https://github.com/CS-Faith/reasonix-ecosystem)

---

## 一句话定位

| 输入 | 输出 |
|------|------|
| Reasonix 装在 C 盘 | Reasonix 跟随 U 盘，任何电脑即插即用 |

---

## 零配置

**无需修改任何 Reasonix 配置。** 双击启动，PortaKit 自动完成一切。

---

## 为什么不用 dotfiles / Nix / Docker？

| 方案 | 能做什么 | 不能做什么 |
|------|---------|-----------|
| dotfiles | 同步配置文件 | Reasonix 用**路径哈希命名项目**，只同步配置不解决会话找不到的问题 |
| Nix | 可复现构建 | 太重，不是给 AI 对话工具设计的 |
| Docker | 完整环境打包 | 体积 2GB+，无法 U 盘即插即用 |

**PortaKit 1 秒钟完成便携**——它只改路径、合并记忆、修补配置。足够小，不入侵。

---

## 路径对比（迁移前 vs 迁移后）

```
迁移前（C 盘固定路径）:
  C:\Users\username\.reasonix\projects\abc123\memory\

迁移后（PortaKit 便携路径）:
  E:\PortaKit\projects\my-awesome-project\memory\
```

---

## 版本选择

| 版本 | 适用 | 原理 | 文件 |
|------|:---:|------|------|
| **PortaKit for 0.5X** | Reasonix 0.5X | `HOME` / `USERPROFILE` 重定向 | bat + ps1 + js |
| **PortaKit for 1.X** | Reasonix 1.X | NTFS Junction（`mklink /J`） | 仅一个 bat |

---

## PortaKit for 0.5X - 解决了什么

0.5X 版 Reasonix 有四个路径硬伤，换电脑就全没了：

| 问题 | 根因 |
|------|------|
| 记忆消失 | 项目记忆按工作区路径哈希命名；路径变了 → 哈希变了 → 找不到 |
| 对话历史空白 | 会话元数据存了旧路径；路径不匹配 → 侧边栏全空 |
| Skill / MCP 失效 | config.json 里 MCP 路径硬编码了旧盘符（`E:\Reasonix`） |
| 数据读不到 | Reasonix 默认从 `C:\Users\...` 取数据，不读当前目录 |

---

## PortaKit for 0.5X - 做了什么

```
双击 启动Reasonix.bat
  │
  ├─ 1. 自动检测当前所在路径（不管在哪个盘、哪个文件夹）
  ├─ 2. 设置 HOME / USERPROFILE 指向当前目录
  ├─ 3. SHA1(路径) → 项目哈希 → 创建/合并记忆目录
  ├─ 4. 融合本机已有的 Reasonix 数据（只合并更新的，不覆盖）
  ├─ 5. 修补 config.json 里的旧路径 → 当前路径
  ├─ 6. 修复所有会话元数据（BOM 清理 + JSON 转义 + 路径对齐）
  └─ 7. 启动 Reasonix
```

---

## Next Step

升级 Reasonix 版本怕丢数据？ → [**Migration Assistant**](https://github.com/CS-Faith/reasonix-migration-assistant) 一键迁移 0.53 → 1.X

想让历史 AI 会话也能跨设备讨论？ → [**Conversation Distiller**](https://github.com/CS-Faith/conversation-distiller) 把对话蒸馏成便携的知识文章

---

<details>
<summary>English Version</summary>

**Reasonix PortaKit** — Carry Reasonix in your pocket. Plug in — same context, same tools, zero setup.

Your AI coding assistant shouldn't be stuck on one machine. PortaKit makes Reasonix truly portable — USB drive, sync folder, any PC. Double-click and go: all your conversations, memories, MCP config, and skills follow you.

### Two Modes
- **For 0.5X**: `HOME`/`USERPROFILE` redirect via batch launcher
- **For 1.X**: NTFS Junction (`mklink /J`) with automatic config repair + data merge

### Key Features
- Zero-config path detection — works on any drive letter
- Incremental data merge from host machine (non-destructive)
- Lazy dependency install from portable `installers/` directory

</details>

## License
MIT © 2026 [CS-Faith](https://cs-faith.github.io)
