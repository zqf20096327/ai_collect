<div align="center">

<h1>
  <a href="hoshi/" title="Meet Hoshi (Star) — Mascot of HshiKoi"><img src="hoshi/Hoshi05.png" alt="Hoshi" height="54" align="absmiddle" /></a>&nbsp;hsMuse
</h1>

**零显存、自进化的本地模块化 AI 绘画提示词工作台（ComfyUI / Flux / Krea 2 / SDXL）**  
**Zero-VRAM Local AI Art Prompt Generator & Danbooru Tag Cleaner for ComfyUI, Flux, SDXL & Krea 2**

[![Release](https://img.shields.io/github/v/release/hshiKoi/hsMuse?include_prereleases&style=for-the-badge&label=Release&color=0DA5E8)](https://github.com/hshiKoi/hsMuse/releases/latest)
[![Platform](https://img.shields.io/badge/Platform-Windows%20x64-1E4E8C?style=for-the-badge)](#)
[![Languages](https://img.shields.io/badge/UI-简%20|%20繁%20|%20EN%20|%20日本語%20|%20한국어-10B981?style=for-the-badge)](#)
[![License](https://img.shields.io/badge/License-All%20Rights%20Reserved-64748B?style=for-the-badge)](TERMS.md)

[简体中文](#-简体中文) • [English](#-english) • [📥 下载最新版 / Download](https://github.com/hshiKoi/hsMuse/releases/latest) • [📋 更新日志 / Changelog](CHANGELOG.md) • [⚖️ 使用条款 / Terms](TERMS.md)

</div>

> [!TIP]
> **下载建议：** 优先下载安装向导版 **`hsMuse_*_Setup.exe`**（`--onedir` 低误报目录架构，冷启动更快，覆盖升级 100% 保留本地数据）；`hsMuse_*.exe` 仅作绿色便携备用。
>
> **Download Note:** Download the setup installer (**`hsMuse_*_Setup.exe`**) first for faster `--onedir` startup, fewer antivirus false positives, and full local data preservation on upgrade. Use the standalone **`hsMuse_*.exe`** for portable single-file use only.

---

## 🇨🇳 简体中文

> **【使用建议】** 推荐优先点击顶栏 **【网页版】**：大屏排版与滚动更流畅，数据与桌面端实时同步。

### 简介
**hsMuse** 是一款纯本地运行、零显存占用的 AI 绘画提示词引擎与资产管理工作台，深度适配 **ComfyUI / Flux / Krea 2 / SDXL**。一键同步输出 **「8 级规范排序 Tag 序列」** 与 **「电影级自然语言长句」**，通过四大世界观隔离、室内外空间锁与自进化词库/角色生态，告别跨时代串戏与提示词凌乱。

### 界面预览

| 暗夜 (Night) | 留白 (Pure) |
| :---: | :---: |
| ![Night](screenshots/theme_01_night.png) | ![Pure](screenshots/theme_02_pure.png) |

| 落樱 (Sakura) | 沧澜 (Cobalt) |
| :---: | :---: |
| ![Sakura](screenshots/theme_03_sakura.png) | ![Cobalt](screenshots/theme_04_cobalt.png) |

<details>
<summary>🎨 点击展开查看随机灵感配色预览（Random Themes）</summary>
<br>
<table>
  <tr>
    <td><img src="screenshots/random_theme_01.png" alt="Random Theme" /></td>
    <td><img src="screenshots/random_theme_02.png" alt="Random Theme" /></td>
  </tr>
  <tr>
    <td><img src="screenshots/random_theme_03.png" alt="Random Theme" /></td>
    <td><img src="screenshots/random_theme_04.png" alt="Random Theme" /></td>
  </tr>
</table>
</details>

### 核心功能亮点
- **可成长的动态角色库**：最高支持 500 位角色（内置 51 位三元组角色：纯净外貌 + 独立原版官服，支持多套官服自动轮换），支持自定义 OC、LoRA 触发词、AI 提炼指令与联网自动去重收录；支持中英文实时搜索与单/双人空间隔离。
- **自进化模块化知识库**：独立 JSON 架构（支持扩展至 40 套、单栏 500 词条），内置 9 套精修美学库（含高通透花庭库 **「晴风花庭」**）与【灵感潮汐】池，支持 10 格可视化编辑、AI 一键造库导入及全库智能混搭。
- **四大世界观隔离 + 空间锁 + 16 套电影机位**：严格隔离「现代 / 东方仙侠 / 物哀哥特 / 自然水畔汤泉」生态及室内外/水系边界，约 6:4 明亮通透光影配比、前景奶油虚化、滑动防重复队列、支持 `{A|B}` 随机通配符与单次最高 100 条批量去重输出。
- **多源并发灵感直采 & 批量清洗转换**：支持 SFW / 纯欲 / R18 分级并发抓取并沉淀至本地池；支持单次最高 200 行批量清洗，按需剥离 LoRA、权重、废词、外貌或基础服装（保留景别与神态词），一键转安全预览 / NSFW 并合成自然语言。
- **高 DPI 全分辨率适配与双端协同**：高 DPI/小屏自适应防裁切、8 向自由缩放、空白区拖拽、记忆尺寸位置与双击/托盘一键复原；桌面端 + 本地 WebUI 实时同步、并发分段四引擎翻译（Youdao / MyMemory / Google / 自定义 AI）、GitHub Private Gist 增量云同步、支持单曲循环（`🔂`）的本地 BGM 播放器与 5 国语言实时切换。

### 快速开始与快捷键
1. 前往 [**Releases 页面**](https://github.com/hshiKoi/hsMuse/releases/latest) 下载最新版安装向导（`hsMuse_*_Setup.exe`）双击安装（免管理员权限，支持自由选盘，覆盖升级/卸载 100% 保留个人数据）。
2. 打开后推荐点击顶栏 **【网页版】** 使用浏览器工作台。
3. 常用快捷键：`F5` 一键抽卡 ｜ `Ctrl + Z` 智能回退 ｜ `Ctrl + D` 收藏 Tag ｜ `Ctrl + M` 切换背景音乐（`🔁/🔀/🔂/🔇`）；双击空白区或右键托盘一键恢复默认窗口尺寸。
4. 想用 AI 扩展自定义词库或角色？请查看 [`templates/`](templates/) 目录中的范例与指令。

### 支持与交流
- **Patreon**：[patreon.com/c/hshiKoi](https://www.patreon.com/c/hshiKoi)
- **Ko-fi**：[ko-fi.com/hshikoi](https://ko-fi.com/hshikoi)
- **Civitai**：[civitai.red/user/HshiKoi](https://civitai.red/user/HshiKoi)
- **社群交流**：QQ 群 `978336169` ｜ 微信群 `hshi2026` ｜ 公众号 `画不出明天`
- **问题反馈**：欢迎直接提交 [GitHub Issues](https://github.com/hshiKoi/hsMuse/issues)

---

## 🌐 English

> **[Tip]** Click **[WebUI]** in the top bar for a smoother widescreen layout and scrolling—synced in real time with the desktop app.

### Overview
**hsMuse** is a 100% local, zero-VRAM visual prompt engine and creative asset studio built for **ComfyUI, Flux, Krea 2, and SDXL**. It generates **8-level sorted Tag sequences** and **cinematic natural language prose** simultaneously in one click, powered by a Four-Era Worldview Isolation Engine, Indoor/Outdoor Space Lock, and a self-growing library of characters and modular knowledge bases.

### Key Highlights
- **Self-Growing Character Archive**: Manages up to 500 profiles (51 built-in presets structured as pure traits + independent canonical outfits with multi-outfit rotation). Supports custom OCs, LoRA triggers, AI trait extraction, live search, canonical-outfit locking, and spatially separated Solo/Dual framing.
- **Modular Knowledge Bases**: Portable JSON packs (up to 40 packs, 500 entries per slot), shipping with 9 refined aesthetic packs (including the airy *Sunlit Garden*) + the dynamic *Muse Tide* pool. Visually edit across 10 slots, import AI-generated packs in seconds, and mix custom packs seamlessly.
- **4-Era Isolation, Space Lock & 16 Adaptive Angles**: Strictly separates *Modern*, *Eastern Fantasy (Xianxia)*, *Wabi-Sabi/Gothic*, and *Nature/Onsen* worlds with indoor/outdoor & water isolation, ~6:4 bright-to-moody balance, foreground bokeh, anti-repeat pooling, `{A|B}` wildcards, and up to 100 unique batch prompts per run.
- **Multi-Source Live Fetch & Batch Cleaner**: Concurrent rating-aware inspiration fetching (SFW / Sensual / R18) and a 200-line batch cleaner that strips LoRAs, weights, quality filler, traits, or base outfits while preserving framing and expressions.
- **High-DPI Ergonomics & Full WebUI Parity**: Auto-fits 125%/150%+ scaling & compact screens; 8-way resize, blank-area drag, window size/position memory & one-click reset; concurrent chunked 4-engine translation (including custom AI LLMs), private GitHub Gist incremental sync, local BGM player with Repeat One (`🔂`), and instant 5-language switching.

### Quick Start & Shortcuts
1. Download the latest setup installer (`hsMuse_*_Setup.exe`) from the [**Releases Page**](https://github.com/hshiKoi/hsMuse/releases/latest) (`--onedir` low-false-positive installer; no admin rights required; personal data is 100% preserved across upgrades).
2. Click **[WebUI]** in the top bar for the smoothest daily workflow.
3. Shortcuts: `F5` Roll ｜ `Ctrl + Z` Smart Undo ｜ `Ctrl + D` Save Tag ｜ `Ctrl + M` Toggle Music (`🔁/🔀/🔂/🔇`); double-click blank area or use tray menu to reset window size.
4. Check [`templates/`](templates/) for sample JSON packs and AI builder prompts.

### Links & Support
- **Patreon**: [patreon.com/c/hshiKoi](https://www.patreon.com/c/hshiKoi)
- **Ko-fi**: [ko-fi.com/hshikoi](https://ko-fi.com/hshikoi)
- **Civitai**: [civitai.red/user/HshiKoi](https://civitai.red/user/HshiKoi)
- **Feedback**: [GitHub Issues](https://github.com/hshiKoi/hsMuse/issues)

---

<div align="center">
Copyright © 2026 HshiKoi. All rights reserved.
</div>
