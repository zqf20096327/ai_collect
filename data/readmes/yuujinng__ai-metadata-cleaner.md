<div align="center">

[English](README.en.md) | 简体中文

# 🧹 文档AI属性清理工具

**一键清除或修改 Word / Excel / PPT / PDF 的属性（元数据），抹掉 AI 生成痕迹**

🔒 **全程本地处理** — 文件不上传服务器，所有操作都在你自己的电脑上完成

[![Release](https://img.shields.io/github/v/release/yuujinng/ai-metadata-cleaner?style=flat-square)](../../releases)
[![下载量](https://img.shields.io/github/downloads/yuujinng/ai-metadata-cleaner/total?style=flat-square&label=%E4%B8%8B%E8%BD%BD)](../../releases)
[![CI](https://github.com/yuujinng/ai-metadata-cleaner/actions/workflows/ci.yml/badge.svg)](https://github.com/yuujinng/ai-metadata-cleaner/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/github/license/yuujinng/ai-metadata-cleaner?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/平台-Windows%2010%2F11-0078D6?style=flat-square&logo=windows11&logoColor=white)](https://github.com/yuujinng/ai-metadata-cleaner#快速开始)

<img src="docs/screenshot.png?v=1.3" alt="界面预览：AI 痕迹自动标红勾选" width="720"/>

*拖入文件 → 疑似 AI 痕迹自动标红并勾选 → 一键清理*

<img src="docs/demo.gif?v=1.4" alt="演示动图：拖入文件 → AI 痕迹标红勾选 → 一键清理（进度条），列表逐个标「已另存 ✓」" width="720"/>

</div>

---

## ✨ 特性

- 🤖 **AI 痕迹自动识别** — `ChatGPT`、`Claude`、`python-docx`、`openpyxl`、`Skia/PDF` 等生成来源自动标红；作者/生成程序/时间统计类字段默认勾选，标题等正文类字段只提示不自动删（防误删）
- 🧬 **结构指纹识别** — 不靠关键词也能看穿脚本一次性生成：正文有字而字数统计为 0、文档内部时间与文件时间相差一年以上（生成库模板冻结日期）、Mac 版 Word 残留、脚本库版本号、WPS 云文档指纹（ICV）、Word/Excel 不该有的缩略图、PDF 的 anonymous/untitled 缺省值
- 🧽 **彻底清除** — 作者、最后修改者、应用程序、创建/修改时间、编辑统计、公司、自定义属性、文档缩略图、ZIP 包内时间戳指纹、PDF 的 Info 字典与 XMP 元数据包……
- ✏️ **随意修改** — 任意属性改成任意值，支持"应用到所有文件"批量统一，日期自动转成文档标准格式
- 🖱️ **拖拽即用** — 文件或整个文件夹（递归扫描）直接拖进窗口
- ⚡ **后台处理不卡界面** — 扫描与清理都在后台线程进行，整目录大批量也有进度条；结果直接标记在文件列表（悬停显示完整路径），保存方式、勾选偏好与窗口大小会被记住
- 🖥️ **命令行模式** — `scan` / `clean` / `set` 子命令，支持批量与脚本自动化，与 GUI 共用同一套核心逻辑；`--json` 输出 + 语义化退出码，方便脚本与 AI Agent 程序化调用
- 🔒 **正文零损伤** — 只改写属性部件，文档内容逐字节保留；覆盖模式先写临时文件再原子替换，失败不伤原文件
- 🕐 **不留处理痕迹** — 清理不改动文件的系统时间戳（覆盖模式连 Windows 创建时间一并保留，副本沿用原文件修改时间）
- 📦 **零安装门槛** — 从 [Releases](../../releases) 下载单个 exe 双击即用，无需安装 Python、无需联网；也提供源码运行方式

## 🕵️ 它能识别哪些痕迹？

| 痕迹类型 | 典型表现 |
| --- | --- |
| 作者 / 最后修改者 | `ChatGPT`、`Claude`、`python-docx` 等 |
| 应用程序 | 生成程序显示为脚本库（openpyxl、pandoc、Skia/PDF、LibreOffice、pdfTeX 等） |
| 时间特征 | 创建时间与修改时间精确到秒完全相同；文档内部时间比文件修改时间早一年以上（python-docx 模板冻在 2013 年）或晚于当前时间 |
| 编辑统计 | 总编辑时间为 0 分钟；正文有字而字数/字符数/行数统计为 0（Office 保存时会自动重算，脚本不会） |
| 应用程序矛盾 | Windows 上交出 "Microsoft Macintosh Word" 生成的文档；openpyxl 的 `3.1` 式非 Office 版本号；修订号 1 且编辑时间 0 |
| WPS 云文档指纹 | 自定义属性 `ICV`（云文档 GUID）、`KSOProductBuildVer`，值里不含任何关键词 |
| 缩略图残留 | Word/Excel 默认不生成 `docProps/thumbnail.jpeg`，出现即多为生成库模板残留 |
| PDF 内嵌信息 | Info 字典中的 Producer/Creator、XMP 元数据包、页面级内嵌元数据、`anonymous`/`untitled` 缺省值 |
| 其他 | 公司、经理、自定义属性、超链接基础里的本机路径等 |

> 「疑似 AI 痕迹」按关键词和规则自动识别，可能有漏报/误报，清理前请过目一遍勾选列表。

## 🚀 快速开始

> 💡 想先随便试试？仓库里的 [示例文件/](示例文件/) 有 4 个带 AI 痕迹的演示文档（Word / Excel / PPT / PDF 各一），拖进来练个手。

**方式一：下载 exe（推荐，无需安装 Python）**

1. 打开 [Releases](../../releases) 页，下载最新版的 **AIMetadataCleaner.exe**（约 15 MB）；
2. 双击运行即可。**无需安装 Python**，所有组件已内置，离线也能用；exe 文件名用英文 `AIMetadataCleaner.exe`（Release 资产兼容性考虑），文件属性里的「文件说明」仍是中文。

> 浏览器或 Windows SmartScreen 可能提示「未知发布者 / 已保护你的电脑」：exe 尚未做数字签名，点「更多信息 → 仍要运行」即可。个别杀毒软件可能误报（PyInstaller 打包的常见现象），加入信任列表即可。如需核对完整性，Release 页附有 exe 的 SHA256 校验值。

**方式二：源码运行（需要 Python，适合开发者）**

1. 安装 [Python 3.11+](https://www.python.org/downloads/)（勾选 *"Add Python to PATH"*）
2. 下载本仓库（*Code → Download ZIP*，或 `git clone`）
3. 双击 **文档AI属性清理工具.bat**

首次启动会自动联网安装 `pypdf`、`tkinterdnd2`（仅一次），界面出现「PDF 支持：已就绪」即一切正常。启动时会有一个黑色命令行窗口随界面一起存在，关闭界面后自动退出。

**方式三：命令行**

```bash
git clone https://github.com/yuujinng/ai-metadata-cleaner.git
cd ai-metadata-cleaner
pip install -r requirements.txt
python doc_meta_cleaner.py
```

## 📖 使用方法

**清除属性，四步：**

1. **把文件或整个文件夹直接拖进窗口**（文件夹会递归找出所有支持的文档），或点**添加文件** / **添加文件夹**；
2. 右侧列出所有属性，疑似 AI 痕迹的行标红：**作者、生成程序、时间统计等身份类字段自动勾选**，标题/关键词等正文类字段只标红提示（需要时手动勾选）；点第一列 ☑/☐ 或双击行即可勾选/取消，勾选会应用到列表里的所有文件；
3. 选择保存方式：**另存副本**（原名_已清理，推荐）或**覆盖原文件**；
4. 点**开始清理**，下方日志逐个文件报告清除了哪些字段。

**修改属性：** 在左侧选中文件，**双击属性表"当前值"一列**（或选中行后点**编辑所选…**），在弹窗里输入新值并保存：

- 可勾选"应用到列表中的所有文件"，一次给整批文档统一改作者等；
- 日期字段支持 `2026-10-20 10:00:05` 之类的写法，按本地时区理解、保存时自动转成文档标准 UTC 格式（Word/PDF 里显示与你输入的一致）；修订次数、总编辑时间需要整数；
- 输入框**留空保存 = 清除该字段**；
- 同一个字段的"修改"与"清除"勾选互斥，后设置的生效；
- 该文件没有的字段（如类别、PDF 主题）保存后会自动新建；自定义属性只能改已有的值，不能新建；
- 点**撤销全部修改**可取消尚未处理的修改项；
- PDF 的 XMP 元数据包不支持逐项编辑，只能整体清除；但修改/清除 Info 字段时会自动同步 XMP，不会残留旧值。
- 文档缩略图同样只能整体清除（勾选后连同包内登记一并摘除），不支持逐项编辑。

## ⌨️ 命令行用法

不开界面也能用——命令行与 GUI 共用同一套核心逻辑，方便批量处理和脚本集成：

```bash
# 扫描：列出属性，疑似 AI 痕迹会被标出（目录会递归展开）
python doc_meta_cli.py scan 文档.docx
python doc_meta_cli.py scan D:\资料\

# 清理：默认只清疑似 AI 痕迹，另存副本（原名_已清理）
python doc_meta_cli.py clean D:\资料\
python doc_meta_cli.py clean 文档.pdf --mode overwrite                # 覆盖原文件
python doc_meta_cli.py clean 文档.docx --fields all                   # 清除全部属性
python doc_meta_cli.py clean 文档.docx --fields creator,创建时间       # 指定字段（key 或中文名均可）

# 修改：字段=值，值留空表示清除该字段；可一次列出多个文件
python doc_meta_cli.py set 报告.docx creator=张三
python doc_meta_cli.py set 报告.docx created="2026-10-20 10:00:05" --mode overwrite

# JSON 输出：结果以单个 JSON 文档打印到 stdout，供脚本/Agent 程序化解析
python doc_meta_cli.py scan 报告.docx --json

python doc_meta_cli.py --list-fields    # 查看全部可操作的字段
```

退出码：**0** 全部成功；**1** 有文件处理失败（被占用 / 加密 / 字段不存在 / 值非法，明细见 ⚠ 行或 JSON 的 `errors`）；**2** 命令用法错误。

## 🤖 与 AI Agent 配合使用

如果你平时用 AI agent（Claude Code / Codex CLI / ZCode 等）生成 Word / Excel / PPT / PDF 文档，最顺滑的用法是把属性清理设为 agent 的**固定收尾步骤**：文档生成完成后由 agent 自动调用命令行清理，不需要再手动拖进界面。把下面这段连同你的生成需求一起粘给 agent 即可：

```text
【交付前清理文档属性 —— 必须执行】
你生成的 Word/Excel/PPT/PDF 文档在交付给我之前，必须完成以下收尾步骤，不可跳过：
1. 如果本机还没有清理工具，先克隆到临时目录（Windows 下可用 %TEMP% 代替 /tmp）：
   git clone --depth 1 https://github.com/yuujinng/ai-metadata-cleaner.git /tmp/ai-metadata-cleaner
2. 对每个生成的 .docx/.xlsx/.pptx/.pdf 文件执行（覆盖模式，直接在原文件上清理）：
   python /tmp/ai-metadata-cleaner/doc_meta_cli.py clean "文档路径" --mode overwrite
3. 清理后逐个复查，确认没有"疑似 AI 痕迹"：
   python /tmp/ai-metadata-cleaner/doc_meta_cli.py scan "文档路径"
4. 两条命令的退出码都是 0 才算完成；非 0 时把错误信息如实告诉我，不要假装成功。
5. 只清理文档属性（作者/程序/时间统计等），不要改动正文内容。
```

**程序化接口**（给需要自己解析结果的 agent/脚本）：三个子命令都支持 `--json`，stdout 输出单个 JSON 文档，中文值以 `\uXXXX` 转义保证任何终端编码下都是合法 JSON：

```bash
python doc_meta_cli.py scan 报告.docx --json
```

```json
{
  "command": "scan",
  "files": [
    { "path": "报告.docx", "kind": "ooxml",
      "props": { "creator": "python-docx", "TotalTime": "0" },
      "suspects": ["creator", "created", "modified", "TotalTime"] }
  ],
  "errors": [],
  "missing": [],
  "unsupported": [],
  "summary": { "total": 1, "ok": 1, "failed": 0 }
}
```

`clean` / `set` 的 JSON 里每个文件返回 `ok`、`changed`、`dest`（输出路径）、`removed`（清除的字段）、`edited`（修改的字段与新值）、`error`（单文件失败原因）。

| 退出码 | 含义 | agent 应对 |
| :---: | --- | --- |
| 0 | 全部成功 | 继续交付 |
| 1 | 有文件处理失败（被占用 / 加密 / 字段不存在 / 值非法），`errors` 与 `files[].error` 有明细 | 读明细，处理后重试 |
| 2 | 命令本身写错（参数缺失、赋值格式不对） | 修正命令，不要原样重试 |

> 💡 批量场景直接传目录（递归展开）：`clean D:\资料\`。想给整批文档统一作者，用 `set`：`python doc_meta_cli.py set D:\资料\ creator=张三 --mode overwrite`。

## 📂 支持的格式

| 类型 | 扩展名 | 清除 | 修改 |
| --- | --- | :-: | :-: |
| Word | `.docx` `.docm` | ✅ | ✅ |
| Excel | `.xlsx` `.xlsm` | ✅ | ✅ |
| PPT | `.pptx` `.pptm` `.ppsx` `.ppsm` | ✅ | ✅ |
| PDF | `.pdf` | ✅ | ✅（XMP 仅整体清除） |

旧的 `.doc/.xls/.ppt` 二进制格式暂不支持。

## 🔒 清理原理（安全边界）

- Office 文档本质是 ZIP+XML 包，工具只改写 `docProps/core.xml`、`docProps/app.xml`、`docProps/custom.xml` 三个属性部件（清除缩略图时会额外摘除 `docProps/thumbnail.jpeg` 及其在包关系与 [Content_Types] 里的登记，不留悬空引用），**正文、样式、图片等其余内容逐字节保留**，不影响文档显示；新建字段会按文档规范插入到正确位置，文件缺少属性部件时也会自动新建并登记，保证 Word/Excel/PPT 正常打开。
- 重建 ZIP 包时若发现 entry 时间戳呈脚本特征（全部相同或年份异常——Word 渐进保存的时间戳是分布开的，脚本一次性写出则完全相同），会把它们统一归一化为文件的修改时间；原本就正常的包保持原样。
- PDF 通过 pypdf 克隆后改写 Info 字典字段与 /Metadata(XMP)（含挂在页面对象上的内嵌元数据），页面内容不变；修改/清除 Info 字段时会同步改写 XMP 包，不会残留旧值。
- 「覆盖原文件」模式先写临时文件再原子替换，失败不会破坏原文件。
- 清理不改动文件的系统时间：覆盖模式完整保留文件的创建/修改/访问时间（Windows 创建时间一并恢复），另存副本沿用原文件的修改时间，不会留下"刚刚被处理过"的痕迹。

## ⚠️ 注意事项

- 清理前**关闭**正在 Word/WPS/预览器中打开的文档，否则文件被占用会失败。
- 清理的是文档**属性**，不会检测或修改正文内容本身。
- AI 检测工具还可能通过文风判断，本工具只负责元数据层面的干净。

## ❓ 常见问题

- **双击 exe 被 SmartScreen 拦截 / 杀毒软件报警**：exe 未做数字签名且由 PyInstaller 打包，属于常见误报；点「更多信息 → 仍要运行」，或改用方式二（源码运行）。
- **提示找不到 Python**：安装 Python 3 时勾选 "Add Python to PATH"，或改用命令行 `python doc_meta_cleaner.py` 启动；不想装 Python 请直接用 Releases 里的 exe。
- **PDF 文件添加失败**：看界面日志最上方是否提示「PDF 支持：未安装」，手动运行 `pip install pypdf` 后重开工具即可。
- **拖拽文件进窗口没反应**：说明可选组件 tkinterdnd2 未装上，手动运行 `pip install tkinterdnd2` 后重开工具即可（不影响其他功能）。

## 🗂️ 项目结构

```
ai-metadata-cleaner/
├── doc_meta_cleaner.py       核心逻辑 + 图形界面
├── doc_meta_cli.py           命令行入口（scan / clean / set）
├── version.py                版本号唯一来源（CLI / GUI 标题 / exe 版本资源都从这里取）
├── doc_meta_cleaner.spec     PyInstaller 打包配置（构建 Windows exe）
├── README.en.md              英文版说明
├── 文档AI属性清理工具.bat        源码运行的双击启动器
├── 示例文件/                  4 个带 AI 痕迹的演示文档，可先拿它们试手
├── docs/
│   ├── screenshot.png        README 界面截图
│   └── demo.gif              README 演示动图
├── tests/
│   ├── run_tests.py          核心逻辑自动化测试
│   ├── gui_smoke.py          GUI 冒烟测试
│   ├── cli_smoke.py          CLI 冒烟测试
│   ├── _make_bat.py          重新生成启动器
│   ├── _make_screenshot.py   重新生成 README 截图
│   ├── _make_gif.py          重新生成 README 演示动图
│   └── _win_capture.py       素材抓图工具（截图/动图共用，抓屏失败回退 PrintWindow）
└── .github/
    ├── ISSUE_TEMPLATE/       Issue 模板
    └── workflows/            CI 与 Release（打 v* 标签自动发布）
```

## 🛠️ 开发与测试

```bash
python tests/run_tests.py         # 核心逻辑测试（自动生成样例并验证清理结果）
python tests/gui_smoke.py         # GUI 冒烟测试
python tests/cli_smoke.py         # CLI 冒烟测试
python tests/_make_screenshot.py  # 重新生成 README 截图
python tests/_make_bat.py         # 重新生成启动器（保持 ASCII + CRLF）
pyinstaller --noconfirm doc_meta_cleaner.spec   # 本地构建单文件 exe（输出到 dist/）
```

发版：把 `version.py` 里的 `__version__` 改为本次版本并提交，再打对应的 `vX.Y.Z` 标签推送；Release 工作流会先校验标签与 `version.py` 一致（不一致直接失败），然后自动跑全量测试、构建 Windows 单文件 exe 并连同源码包一起发布 GitHub Release。

> 注意：双击启动器 `文档AI属性清理工具.bat` 必须保持 ASCII + CRLF 格式保存，不要用编辑器修改后另存为 UTF-8；若损坏，运行 `python tests/_make_bat.py` 重新生成即可。

## 📄 许可证

[MIT](LICENSE) © 2026 yuujinng
