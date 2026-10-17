# Smart Rename

> **中文**: 右键任何文件 → AI 自动给它起一个有意义的中文名
> **English**: Right-click any file → AI gives it a meaningful Chinese name

把 `IMG_20240315_8473829.jpg` 一键变成 `京都岚山_竹林晨光_2024-03-15.jpg`。
Turn `IMG_20240315_8473829.jpg` into `京都岚山_竹林晨光_2024-03-15.jpg` in one click.

支持 **图片 / 视频 / PDF / Word / Markdown / TXT / 文件夹**。
Supports **images / videos / PDFs / Word / Markdown / TXT / folders**.

<p align="center">
  <img src="docs/demo.gif" alt="Smart Rename Demo" width="720" />
</p>

---

## 📦 5 秒看价值 / Five-second value

```
红发雀斑女孩_蓝衣围巾肖像_2026-04-25.png   ← IMG_0023.jpg
公众号文章发布_SOP_视觉规范_2026-04-25.md  ← note.md
机器学习_监督学习_线性回归_2026-04-25.pdf  ← scan.pdf
奇幻巨树小镇_飞鸟掠过街道_2026-04-25.mp4   ← video_20240412_001.mp4
2026年Q1业绩回顾_2026-04-25                ← randomfolder
```

**中文**: 100 张图改名约 1 分钟（Gemini Flash 3 路并发），成本约 $0.01。多数人 free tier 足够。
**English**: ~1 minute for 100 images (Gemini Flash, 3-way parallel). Cost ~$0.01. Free tier suffices for most users.

---

## 🚀 30 秒装 / 30-second install

**前提 / Requirements**: macOS Monterey (12.0) 或更新 / or newer

```bash
git clone https://github.com/Jane-xiaoer/smart-rename.git
cd smart-rename
./install.sh
smart-rename --setup     # 粘贴你的 Gemini API key / paste your Gemini API key
```

完事 / Done.

---

## 🖱️ 怎么用 / How to use

**中文**:
1. 在 Finder 里**选中**你想改名的文件（一个或多个）
2. **右键** → 在弹出菜单里找到 **「快捷操作」/「Quick Actions」** 子菜单（或 **「服务」/「Services」**）
3. 在子菜单里点 **改名 (Smart Rename)**
4. 系统通知"正在分析…"，几秒后弹出**预览对话框**（旧名 → 新名）
5. 点 **「确认改名」** → 完成

**English**:
1. **Select** files in Finder (one or many)
2. **Right-click** → look for the **"Quick Actions"** submenu (or **"Services"** on older macOS)
3. Click **改名 (Smart Rename)** inside the submenu
4. System notification: "Analyzing…", then a preview dialog pops up (old → new)
5. Click **「确认改名」 (Confirm)** → Done

> **关键 / Important**: "改名" **不在右键根菜单**，**在子菜单里**。第一次找会以为没装好，其实只是要多点一层。
> **Important**: "改名" lives **inside the Quick Actions submenu**, NOT directly in the right-click root. First-timers often miss this.

**可选热键 / Optional hotkey**: 装了 [Hammerspoon](https://www.hammerspoon.org/) 后，按 `⌥⌘R` 直接触发（不用点子菜单）。
**Optional hotkey**: With [Hammerspoon](https://www.hammerspoon.org/) installed, press `⌥⌘R` to trigger directly (no submenu hunting).

---

## ⚙️ 它怎么工作 / How it works

```
你在 Finder 里选了 N 个文件
You select N files in Finder
  ↓
右键 → "快捷操作 / Quick Actions" 子菜单 → "改名 (Smart Rename)"
Right-click → "Quick Actions" submenu → "改名 (Smart Rename)"
  ↓ (或按 / or press ⌥⌘R if Hammerspoon installed)
macOS Quick Action 触发 wrapper 脚本
macOS Quick Action triggers wrapper script
  ↓
smart-rename CLI (bash + jq) — 3 路并发
smart-rename CLI (bash + jq) — 3-way concurrent
  ↓ 按文件类型路由 / route by file type
analyze.py
  ├─ 图片 / Image    → Gemini Vision
  ├─ 视频 / Video    → ffmpeg 抽 3 帧拼图 / extract 3-frame grid → Gemini Vision
  ├─ PDF             → pdftotext / pdftoppm → Gemini
  ├─ docx            → textutil → Gemini Text
  ├─ md/txt          → 读前 2000 字 / read first 2000 chars → Gemini Text
  └─ 文件夹 / Folder → 列文件名 / list filenames → Gemini Text
  ↓
原生 osascript 弹**预览对话框**(旧名 → 新名) → 你点"确认改名"
Native osascript dialog (preview old → new) → you click "Confirm"
  ↓
原子改名 + JSON log (一键 undo)
Atomic rename + JSON log (one-click undo)
```

---

## 🛠️ CLI 用法 / CLI usage

```bash
smart-rename --preview file1 file2 ...   # 输出 JSON 计划 / output JSON plan
smart-rename --apply <plan.json>         # 执行改名 / execute rename
smart-rename --undo                      # 撤销上一次 / undo last batch
smart-rename --setup                     # 配置 Gemini key / configure key
smart-rename --doctor                    # 健康检查 / health check
```

---

## 🔑 BYOK — 自己带 key / Bring your own key

**中文**: Smart Rename **不打包任何 API key**。你在 [Google AI Studio](https://aistudio.google.com/app/apikey) 申请免费 key（不需要信用卡），然后跑 `smart-rename --setup` 配置。

**English**: Smart Rename ships **no API key**. You get a free one at [Google AI Studio](https://aistudio.google.com/app/apikey) (no credit card required), then run `smart-rename --setup` to configure.

API key 读取顺序 / Key lookup order:
1. `$GEMINI_API_KEY` (env var)
2. `~/.config/smart-rename/config.env`  (推荐 / recommended — `--setup` writes here, `chmod 600`)
3. `~/.shared-skills/api-registry/.env` (PAI 用户兼容 / PAI compat)
4. `~/.smart-rename.env`

详见 / See [BYOK.md](docs/BYOK.md).

---

## 📐 命名规则 / Naming convention

```
<内容关键词>_<YYYY-MM-DD>.<扩展名>
<content-words>_<YYYY-MM-DD>.<ext>
```

**中文**: 内容在前——Finder 列宽窄时只看到前半段，Spotlight 预览也是。日期是消歧用，不是头条。
**English**: Content first — filenames get truncated in narrow columns; date is a disambiguator, not the headline.

日期来源 / Date source: 先读 EXIF `creation` (图片), 否则取文件 mtime / EXIF `creation` first, fallback to file mtime.

---

## 🗑️ 卸载 / Uninstall

```bash
./uninstall.sh
```

只删 CLI / Quick Action / Hammerspoon 模块。**保留** API key 配置和 brew 装的 ffmpeg/poppler。
Removes only the CLI / Quick Action / Hammerspoon module. **Preserves** your API key and brew-installed ffmpeg/poppler.

---

## 📚 文档 / Documentation

| 文件 / File | 内容 / Content |
|------|------|
| [docs/QUICKSTART.md](docs/QUICKSTART.md) | 30 秒上手 / 30-second onboarding |
| [docs/INSTALL.md](docs/INSTALL.md) | 详细安装 / Detailed install |
| [docs/BYOK.md](docs/BYOK.md) | API key 申请 + 配置 / Get & configure API key |
| [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) | 常见问题 / Common problems |
| [docs/CHINA.md](docs/CHINA.md) | **中国大陆用户必读** / **For mainland China users** |
| [docs/EXTEND.md](docs/EXTEND.md) | 扩展开发 / Extending the tool |

---

## 🛣️ Roadmap

- [ ] OCR fallback for scanned PDFs (扫描 PDF 抽全文，不只识别封面)
- [ ] PPT / pptx support
- [ ] English filename option (英文命名选项)
- [ ] Custom naming styles (kebab-case, prefixes, etc.)
- [ ] Cross-platform port (Linux Nautilus / Windows Explorer)

PR / Issues welcome.

---

## 🧱 技术栈 / Tech stack

- Bash + jq (orchestration / 编排)
- Python 3 stdlib (no pip dependencies / 无 pip 依赖)
- Google Gemini Flash (vision + text)
- ffmpeg (video frame extraction)
- poppler (pdftotext + pdftoppm)
- macOS textutil (Word/RTF)
- macOS Quick Actions (NSServices Framework)
- Hammerspoon (optional hotkey + UI / 可选热键)

---

## 📜 License

[MIT](LICENSE)

---

## 📱 关注作者 / Follow Me

如果这个仓库对你有帮助，欢迎关注我。后面我会持续更新更多 AI Skill、做网站、自动化工作流和创意项目。

If this repo helped you, follow me for more AI skills, website building, automation workflows, and creative projects.

- X (Twitter): [@xiaoerzhan](https://x.com/xiaoerzhan)
- 微信公众号 / WeChat Official Account: 扫码关注 / Scan to follow

<p align="center">
  <img src="assets/wechat-qr.png" alt="WeChat QR" width="300" />
</p>

<p align="center">
  <b>中文：</b>欢迎关注我的公众号，一起研究 AI Skill、网站搭建、自动化流程和创意实验。<br/>
  <b>English:</b> Follow my WeChat Official Account for more AI skills, website building, automation workflows, and creative experiments.
</p>
