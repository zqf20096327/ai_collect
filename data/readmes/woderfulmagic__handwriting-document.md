# Handwriting Document · AI 仿真手写

![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)
[![MIT License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

**杜绝形式主义，把时间还给真正重要的事。**

文字已经写好了，却还要一笔一画再抄一遍？

把正文交给这个 Skill，它会生成自然的中文仿手写 PDF：可以用默认硬笔字，也可以提供笔迹样本，参考你的字形与书写习惯。排好横线纸，直接预览、保存、打印。

**AI 仿真 · 临摹字迹 · 重复字自然变化 · A4 打印**

![从电子正文到仿手写页面的实际效果对比](docs/assets/before-after.png)

<p align="center">演示文字为虚构示例。右侧是本项目实际输出，并非概念效果图。</p>

## 它能帮你做什么？

- **少做重复誊抄。** 把已经完成的正文转成手写风格，保留你的文字和段落。
- **AI 仿真手写。** 不只是把同一个字随机旋转；字内比例、部件位置和落笔位置也会变化。
- **参考样本临摹字迹。** 支持笔迹图片、手写 PDF、Word 内嵌图片；可调整风格，明确要求后可保存个人预设。
- **一次导出整篇。** 自动分页，输出 A4 PDF、逐页 PNG/JPG 和预览图。
- **生成一半也能接着做。** 已完成的素材保留，失败后可以继续，不必整篇重来。

可以用来做个人文稿的手写排版、日记与书信视觉稿、笔迹风格实验，以及允许电子生成的誊写材料。本文所说的“杜绝形式主义”，是减少只为重复抄写而抄写的劳动。

## 先看真实输出

[打开演示 PDF](examples/demo.pdf) · [查看整页大图](docs/assets/demo-page.png) · [下载演示原文](examples/demo.txt)

<p align="center"><img src="docs/assets/demo-page.png" alt="虚构示例的整页仿手写输出" width="620"></p>

### 同一个字，也有不同的写法

上排是基础笔迹，下排是处理后的实际正文采样，字框已统一大小，方便比较内部变化。

![实际正文中的重复字变化：基础字形与处理后字形对比](docs/assets/repeated-comparison.png)

这些差异用于减少机械重复感，不是“真人识别率”或“100% 骗过检测”的证明。

## 在 Codex 中使用

这是一个包含 `SKILL.md`、脚本和素材的可安装 Skill，也能直接用 Python 命令运行。

用 Git 安装（PowerShell、macOS / Linux 均可）：

```bash
git clone https://github.com/woderfulmagic/handwriting-document.git "$HOME/.agents/skills/handwriting-document"
```

也可以下载 ZIP，解压后将文件夹改名为 `handwriting-document`，放到 `~/.agents/skills/` 下。重新打开 Codex 会话后调用：

```text
使用 $handwriting-document，把下面的内容变成自然的中文仿手写文档。
保留原文，使用细黑色硬笔字和白色横线纸，导出 A4 PDF 和逐页图片。
```

临摹自己的笔迹时，附上样本，再说：

```text
使用 $handwriting-document，参考这张图片里的字迹来处理我的正文。
学习字形、粗细和书写习惯，保持文字准确，不照搬照片的阴影和纸纹。
```

没有样本也可以直接用内置的瘦长硬笔风格。其他支持 `SKILL.md` 的代理可以读取本技能，但需要自行提供 Python 执行与图像生成能力；目前主要验证 Codex 和命令行流程。

安装路径依据 [Codex 官方 Skills 文档](https://developers.openai.com/codex/skills/)。已有 `~/.codex/skills` 安装的用户可继续按自己的客户端配置使用，避免重复安装同名技能。

## 先免费跑通一个离线示例

需要 **Python 3.10+**。在下载后的仓库根目录执行：

```bash
python -m venv .venv
# Windows PowerShell：.venv/Scripts/Activate.ps1
# macOS / Linux：source .venv/bin/activate
python -m pip install -r scripts/requirements.txt

python scripts/prepare_input.py examples/demo.txt --title 心理自传 --out output/demo
python scripts/generate_strips.py output/demo
python scripts/build_document.py output/demo
python scripts/validate_output.py output/demo
```

结果在 `output/demo/handwriting.pdf`。演示正文命中内置缓存，**不需要 API Key，也不会调用生图服务**。新正文通常需要生成新笔迹，并不支持所有内容离线转换。

## 换成你自己的文字

先选择一种生图方式：

| 方式 | 需要什么 |
| --- | --- |
| 独立 Images API | API Key、支持参考图编辑的图像模型；可选自定义服务地址 |
| 已安装的 codex-image | 沿用它已有的配置，指定 `--backend codex-image` |
| 代理自带的生图工具 | 按任务提示词生成图片，再用 `--adopt` 登记 |

独立 API 的 PowerShell 配置示例：

```powershell
$env:OPENAI_API_KEY = Read-Host "输入 API Key" -MaskInput  # PowerShell 7
$env:OPENAI_IMAGE_MODEL = "你的图像编辑模型名称"
# 自定义服务时再设置；默认使用 OpenAI 官方 API：
# $env:OPENAI_BASE_URL = "https://你的服务地址/v1"
```

macOS / Linux 可以用 `read -s OPENAI_API_KEY; export OPENAI_API_KEY` 输入密钥，再设置 `OPENAI_IMAGE_MODEL`。模型名称填写服务商实际支持的**图像编辑模型**，不要填写普通聊天模型。

把正文存成 UTF-8 编码的 `body.txt`，每段占一个源文件行，然后运行：

```bash
python scripts/prepare_input.py body.txt --title 我的文章 --out output/my-document
python scripts/generate_strips.py output/my-document --backend images-api
python scripts/build_document.py output/my-document
python scripts/validate_output.py output/my-document
```

有笔迹样本时，在第一条命令末尾加 `--reference reference.jpg`。调整自然变化幅度可以加 `--variation-strength 0.8 --drift-strength 0.8`；默认均为 `1`，不建议为了“像真人”一味调大。

**生成后仍需核对文字。** 检查条带、全部 PDF 页面和重复字，再记录视觉检查。新正文的模型生成可能出现错字，程序的字符索引检查不能替代目视校对。完整步骤见 [执行与恢复](references/workflow.md) 和 [质量检查](references/quality-checks.md)。PDF 参考提取与最终 PDF 渲染需要 [Poppler](https://poppler.freedesktop.org/) 的 `pdftoppm`。

## 几件事说清楚

**“临摹字迹”是参考风格。** 它学习字形、粗细和倾向，不还原真实笔顺、笔压凹痕，也不保证与某人的字迹完全一致。这里的“AI 仿真”指视觉效果。

**本地组版，按需联网生图。** 文本准备、变形、分页和导出在本地完成；调用生图时，相关正文片段和笔迹参考会发给你配置的服务。服务可能收费，具体价格和隐私政策以服务商为准。私有样本不会自动加入公开仓库或内置风格。

**保留创作乐趣，不冒充身份。** 使用自己的或获准使用的笔迹。请勿用于伪造签名、冒充他人或绕过明确要求本人亲笔完成的评估。

**打印建议：** A4 空白纸、100% 实际大小、黑白高质量，关闭省墨与“适合页面”。数字预览不等于实物打印测试。

## 原理与项目结构

```text
已有正文 + 笔迹参考
        ↓
AI 生成分行笔迹素材
        ↓
字内结构变化 + 连续位置漂移
        ↓
自动分页 → PDF / PNG / JPG → 逐行与逐页核对
```

`SKILL.md` 是代理入口；`scripts/` 提供可复用命令；`assets/styles/default/` 包含合成笔迹参考与演示缓存；`references/` 说明参考处理、恢复和质量检查。更详细的临摹用法见 [自定义参考与预设](references/custom-reference.md)。

## 让更多人少抄一遍

如果它确实帮你省下了重复誊抄的时间，欢迎点一个 **Star ⭐**，让需要的人更容易发现它。

也欢迎提交错字、排版问题和风格建议。复现材料请用虚构文字，别把个人文稿、私有笔迹或密钥贴进公开 Issue。

开发者可用 `python -m unittest discover -s tests -v` 运行4项接口与恢复测试。首版已在 Windows 本地通过测试、离线示例导出和一次真实 API 生图后导出 PDF 的验证。仓库提供 [Windows / Linux 自动检查配置示例](docs/ci-example.yml)，当前未启用 GitHub Actions；有工作流写入权限后可将其放入 `.github/workflows/`。

[MIT License](LICENSE) · [第三方代码与素材说明](THIRD_PARTY_NOTICES.md) · [English](README.en.md)
