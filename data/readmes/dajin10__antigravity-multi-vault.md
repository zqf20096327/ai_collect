[English](README.en.md) | [简体中文](README.md)

# Antigravity Multi-Vault

> **从 1 个账号起步，无限扩展至 N 个账号的 Antigravity 多仓工作台 Skill。**
>
> **人类用户无需手动敲命令**：把本仓库交给你的 AI Agent（Antigravity / Claude Code / Codex），说一句 **“帮我安装并启动这个多仓工作台”**，AI 将自动完成环境检查、依赖安装、Skill 挂载、账号初始化与桌面工作台拉起。

![Multi-Vault 全景展示](docs/images/showcase-overview.png)

---

## 🤖 Instructions for AI Agents（AI 自动安装与部署协议）

> **致接入的 AI Agent**：当用户要求你安装、部署或初始化本仓库时，**严禁让用户手动执行命令行**。请严格按以下 4 步自动完成部署并汇报结果。

### Step 1：环境探测与依赖安装
检查 Python 3.8+ 与 `PySide6`（用于渲染无边框圆角 WebEngine 桌面工作台）：
```bash
python --version
python -c "import PySide6, PySide6.QtWebEngineWidgets; print('PySide6_OK')"
```
若导入失败，自动执行安装：
```bash
pip install PySide6
```

### Step 2：挂载 Skill 到当前 Agent 技能目录
将本仓库目录（记为 `<REPO_DIR>`）链接或复制到本地全局 Skills 目录，使后续会话可直接触发：
- **Antigravity / Gemini**：`~/.gemini/config/skills/antigravity-multi-vault`
- **Claude Code**：`~/.claude/skills/antigravity-multi-vault`
- **Codex**：`~/.codex/skills/antigravity-multi-vault`

Windows PowerShell 示例（优先使用 Junction 软链，失败则 `Copy-Item`）：
```powershell
$target = "<REPO_DIR>"
$link = "$env:USERPROFILE\.gemini\config\skills\antigravity-multi-vault"
if (-not (Test-Path $link)) {
    New-Item -ItemType Junction -Path $link -Target $target
}
```

### Step 3：冷启动初始化（自动识别 0/1/4 仓状态）
运行只读状态探测：
```bash
python "<REPO_DIR>/scripts/vault_core.py" status --mask
```
根据返回结果执行对应初始化：
1. **若存在历史旧版四仓数据但无 `registry.json`**：自动执行无损迁移：
   ```bash
   python "<REPO_DIR>/scripts/vault_core.py" migrate-legacy
   ```
2. **若 `totalSlots == 0` 且 `currentEmail` 不为空**（用户当前只有 1 个已登录账号）：
   自动将其归档为第 1 仓（主力仓）：
   ```bash
   python "<REPO_DIR>/scripts/vault_core.py" save slot-1 --label "主力仓" --mask
   ```
3. **若 `currentEmail` 为空**：提示用户先在 Antigravity 登录第 1 个账号，或在稍后启动的工作台界面点击「＋ 新增账号仓」。

### Step 4：后台拉起桌面工作台并执行健康探针
1. **确认是否已在运行**：请求 `http://127.0.0.1:28888/status`；若返回 `{"ok": true}` 则跳过重复启动，直接发送 `/toggle` 唤醒窗口。
2. **若未运行，以分离后台进程启动 `scripts/companion_app.py`**（严禁阻塞当前终端）：
   - **Windows**：
     ```powershell
     Start-Process -FilePath "pythonw" -ArgumentList "`"<REPO_DIR>\scripts\companion_app.py`"" -WindowStyle Hidden
     ```
   - **macOS / Linux**：
     ```bash
     nohup python3 "<REPO_DIR>/scripts/companion_app.py" >/dev/null 2>&1 &
     ```
3. **健康检查（等待 2~3 秒后校验）**：
   请求 `http://127.0.0.1:28888/status`，确认返回 `"ok": true` 与 `"slotCount"` 后，向用户汇报：
   - 工作台已启动并自动停靠在 Antigravity 右侧；
   - 告知界面核心操作：**「＋ 新增账号仓」**（空白沙盒加号 / 捕获现役号）、**邮箱右侧红色 `🗑`**（移除仓位）、**标题栏 `👁 / 🙈`**（演示隐私脱敏）。

---

## 核心能力一览

| 场景 | 界面操作（推荐） | Agent 对话 / CLI 等价操作 |
| :--- | :--- | :--- |
| **1 仓起步** | 点击 `＋ 新增账号仓` → 存入当前号 | `python scripts/vault_core.py save slot-1 --label "主力仓"` |
| **新增第 N 仓** | 点击 `＋ 新增账号仓` → `🆕 空白沙盒登录新号` | `python scripts/vault_core.py prepare-new` → 登录后 `save slot-N` |
| **切换账号** | 点击目标卡片 `⚡ 切到 slot-X` | `python scripts/vault_core.py switch-restart slot-X` |
| **删除仓位** | 点击卡片邮箱右侧红色 `🗑` 按钮 | `python scripts/vault_core.py remove slot-X --purge` |
| **演示防泄露** | 点击标题栏 `👁 / 🙈` 一键打码 | `python scripts/vault_core.py status --mask` |

---

## 目录结构

```text
antigravity-multi-vault/
├── SKILL.md                   # Agent 运行时调度协议与自动部署门禁
├── README.md                  # Agent-First 自动安装部署指南（本文件）
├── ui/
│   └── index.html             # 无边框圆角 WebEngine 多仓工作台前端
├── scripts/
│   ├── companion_app.py       # PySide6 桌面宿主 + 本地 127.0.0.1:28888 控制服务
│   ├── vault_core.py          # 跨平台 N 仓核心引擎（凭据读写 / 会话快照 / 原子切换 / 增删迁移）
│   └── quota_scheduler.py     # 可选 CLI 额度分析脚本
├── docs/
│   ├── showcase.html          # 交互式展示页
│   └── images/                # 高清展示图
└── schemas/
    └── registry.example.json  # 动态 N 仓注册表 Schema 示例
```

## 隐私与安全边界
- 零遥测、零云端上传，所有凭据与会话快照仅保存在本地 `~/.gemini/antigravity/profiles/`。
- 每次切号或空白登录前，自动将现役 Electron 会话移入 `restore_backups/` 保留，不直接删除用户数据。
- 凭据通过操作系统原生安全存储接口读写（Windows `Advapi32.dll` / macOS `security` / Linux `secret-tool`）。

## 协作者 (Contributors)
- **dajin10** — 项目发起与产品架构
- **Gemini4 neno** — 跨平台内核、PySide6 桌面工作台与开源 Skill 工程实现
