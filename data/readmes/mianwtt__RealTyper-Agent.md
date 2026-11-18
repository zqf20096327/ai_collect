<p align="center">
  <img src="docs/assets/hero.svg" alt="RealTyper-Agent · Real Typing, Not Text Insertion." width="100%">
</p>

<h1 align="center">RealTyper-Agent</h1>

<p align="center">
  <strong>Real Typing, Not Text Insertion.</strong><br>
  让 Agent 规划词组、敲入拼音、核对上屏结果，完成中文录入。
</p>

<p align="center">
  An intelligent typing agent that performs real keystroke and IME interactions,<br>
  with semantic input planning, candidate selection, and automatic error correction.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-1.1.1-2563eb" alt="版本 1.1.1">
  <img src="https://img.shields.io/badge/platform-Windows-0078d4" alt="Windows">
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776ab" alt="Python 3.9 或以上">
  <img src="https://img.shields.io/badge/IME-微软拼音-059669" alt="微软拼音输入法">
</p>

<p align="center">
  <a href="#demo">实际演示</a> ·
  <a href="#quickstart">快速开始</a> ·
  <a href="#features">核心能力</a> ·
  <a href="#how-it-works">工作原理</a> ·
  <a href="#compatibility">兼容范围</a> ·
  <a href="docs/USAGE.md">完整文档</a>
</p>

---

**RealTyper-Agent 是一个 Windows 中文智能录入工具。** 它读取剪贴板里的原文，将文字规划成词组，通过微软拼音按键与候选确认输入，再回读本次新增内容，发现差异时局部回删、重输。

日常使用只有一个入口：**Ctrl + Alt + V**。词典可独立完成规划，也可以结合本机 Qwen；输入框已有文字时，从当前光标处继续。

<a id="demo"></a>

## 先看它怎样输入

![微软拼音实际录制：组合多字拼音，再确认候选上屏](docs/assets/pinyin-demo.gif)

*真实输入录像节选，展示 `mo'ren`、`mo'shi` 的拼音组合与上屏。录制使用 V1 原生输入适配器；当前版本为 v1.1.1。*

```text
原文        大模型的作用就是为了提高生产力
词组示例    大模型 / 的 / 作用 / 就是 / 为了 / 提高 / 生产力
拼音示例    da'mo'xing / de / zuo'yong / jiu'shi / wei'le / ti'gao / sheng'chan'li
执行        拼音按键 → 候选确认 → 回读比较 → 继续或局部修正
```

*分词示例用于说明流程，实际边界受词典、上下文与模型规划影响。*

<a id="quickstart"></a>

## 快速开始

需要 **Windows、Python 3.9+ 和已启用的微软拼音中文全拼**。从 GitHub 下载并解压项目，在项目文件夹打开 PowerShell；也可以先克隆仓库：

```powershell
git clone https://github.com/mianwtt/RealTyper-Agent.git
cd RealTyper-Agent
```

```powershell
python -m pip install --target .deps -r requirements.txt
python -m realtyper_agent --quick
```

环境准备好后，日常直接双击 **[快捷输入.cmd](快捷输入.cmd)**。

### 复制 → 定位 → 快捷键

1. **复制**想要输入的文字。
2. **点击**目标输入框中的插入位置，无需清空原有文字。
3. **按 Ctrl + Alt + V**，保持输入框焦点，等待完成。

<p align="center">
  <img src="docs/assets/quick-mode.png" alt="快捷模式窗口：快捷键、规划方式、运行状态和置顶选项" width="472">
</p>

*快捷模式真实截图。窗口默认置顶，最小化后快捷键仍可使用。*

| 操作 | 快捷键 |
| --- | --- |
| 开始 / 暂停 / 继续 | **Ctrl + Alt + V** |
| 停止 | **Ctrl + Alt + Q** |

暂停在当前片段完成后的检查点生效。任务完成后，**仅本次新增结果**会复制到剪贴板，光标留在新增内容末尾。切换窗口或输入框会停止任务。

**没有模型也能用：**

```powershell
python -m realtyper_agent --quick --offline
```

默认 `--hybrid` 先生成本地词典计划，再尝试本机 Ollama 的 `qwen3.5:9b`。模型请求最多等待 20 秒；不可用或计划不合格时继续使用本地计划。程序不会自动下载模型。超过 400 字符的原文直接使用本地规划。

### 可选：本地部署 LLM

安装并打开 [Ollama](https://ollama.com/download)，在 PowerShell 下载模型并检查列表，然后启动 Agent：

```powershell
ollama pull qwen3.5:9b
ollama list
python -m realtyper_agent --quick --url http://127.0.0.1:11434 --model qwen3.5:9b
```

详细图文可参考 **智泊AI产品经理教程** 的 [《〖保姆级教程〗手把手教你用Ollama部署Qwen3-VL大模型，建议收藏！》](https://blog.csdn.net/2301_80239908/article/details/154696963)（CSDN）。该文以 **Qwen3-VL** 为例，供学习 Ollama 安装与本地部署；本项目默认使用 **qwen3.5:9b**。命令与模型信息以 [Ollama 官方文档](https://docs.ollama.com/cli) 和 [模型页](https://ollama.com/library/qwen3.5:9b) 为准。仅使用词典时可跳过这一步。

<a id="features"></a>

## 把输入、选词和校对连起来

| 能力 | 使用时得到什么 |
| --- | --- |
| **按词组规划** | jieba 与自定义词典保留完整词语，Qwen 可补充分词和读音；模型不能随意拆碎已保护的词语。 |
| **经过系统拼音输入法** | 汉字通过拼音字母按键和候选确认上屏，可以观察到组合与选词过程。 |
| **从光标处接着输入** | 保留已有前后文，只对本次新增内容比较、修正与导出；已有选区收起到末尾再输入。 |
| **每段最多尝试 3 次** | 候选重选、英文状态恢复和后续纠错共享次数；额度用完停止，避免反复试选。 |
| **有变化的输入节奏** | 舒缓、自然、较快三档；按键、词间、标点和句末分别加入随机间隔。 |
| **模型可选，本地可用** | `--offline` 完全不调用模型；混合模式中，模型超时、改写或坏计划会回退词典。 |

自然档按键延迟采样基准约 **150 ms**，范围 **55–390 ms**；词间停顿约 **0.20–0.64 秒**。实际耗时还包括输入法响应、回读与重试。这些节奏采用规则采样。

```powershell
# 更慢，便于观察输入过程
python -m realtyper_agent --quick --pace slow

# 更快，保留随机间隔
python -m realtyper_agent --quick --pace brisk
```

## 想先看计划？打开验证台

双击 **[启动.cmd](启动.cmd)**，或运行：

```powershell
python -m realtyper_agent
```

在一个窗口里查看**原文、词组、拼音、实际录入结果和核验记录**。先生成计划，再用自带编辑器试输入，适合检查分词、多音字和候选策略。

![本地验证台：原文与输入计划、系统输入法测试编辑器、候选与核验记录](docs/assets/planner.png)

*RealTyper-Agent v1.1.1 真实截图：使用本地词典生成计划，尚未执行录入；日常默认模式为词典与 Qwen 结合。*

<a id="how-it-works"></a>

## 它怎样处理“发力 / 法力 / 乏力”？

![输入流程：复制与定位、词组规划、拼音与选词、回读核验、完成；差异进入局部重输](docs/assets/workflow.svg)

同样的 `fa'li`，候选排序可能随上下文和输入法自学习变化。Agent **回读实际上屏文字**来确认是否选对。当前微软拼音的主要兼容路径是“确认候选 → 读取结果 → 比对目标”，正常录入不依赖 OCR。

如果结果不一致，会回删本次错误内容，重新输入并改选候选；也可用“方式”取“式”、“注意”取“注”、“回天乏力”取“乏力”。辅助词上屏并核验后，只保留目标部分。每个片段共享 **3 次**确认额度，成功的直接选词序号会缓存，但下次使用仍会核对。

这个过程可能出现错误候选短暂上屏后被回删。范围定位需要可靠的编辑器接口，因此兼容性取决于目标控件。

<a id="compatibility"></a>

## 能在哪些地方使用？

| 输入位置 | 当前支持情况 |
| --- | --- |
| 自带验证台 | 已实测同音词、多音字、混合字符、换行与局部修正。 |
| 原生 Win32 Edit / RichEdit | 已适配；已有正文中间插入、保留前后文已实测。 |
| Edge 普通 textarea | 自有测试页单行原文中间插入已实测，包含 emoji。 |
| Edge `contenteditable` | 自有带 `role="textbox"` 的测试页已实测，包含辅助词取字与混合文本。 |
| Chrome 普通可读编辑框 | 自有测试页单行原文与同音词已实测。 |
| 浏览器中的多行原文 | 暂不支持，输入前提示；可改用已适配的原生多行编辑框。 |
| 密码框、只读框、无法准确读取光标的控件 | 拒绝启动。 |
| Word、复杂网页编辑器、自绘控件 | 需要额外适配或验证。 |

浏览器测试使用自有 localhost 页面，**不代表所有网页聊天框已兼容**。首次使用可先在草稿框测试短句；运行时保持焦点，并让 Agent 完成本次输入。

## 可核对的验证

**v1.1.1：85 项单元与回归测试通过。** 覆盖分词边界、模型计划回退、读音补正、三次尝试上限、辅助选词、英文恢复、范围保护、光标定位与随机节奏。

| 验证层级 | 已有记录 |
| --- | --- |
| 当前自动化测试 | v1.1.1，85 项通过；[验证摘要](docs/evidence/v1.1.1-summary.json)。 |
| 最近实际输入基线 | v1.1.0，自有 Edge 普通框及富文本框中间插入，原有前后文、末尾光标与本次剪贴板结果符合预期。 |
| 更早跨应用验收 | 原生编辑框、Edge、Chrome、暂停继续及焦点停止；[V1 验收摘要](docs/evidence/v1-acceptance.json)、[光标插入摘要](docs/evidence/v1.0.2-caret.json)。 |

实际输入基线与当前自动化测试分别记录；v1.1.1 的节奏调整和第三次尝试通过程序回归验证，未将旧版录像标作本版重新实测。详见 [VALIDATION.md](VALIDATION.md)。

```powershell
python -m unittest discover -s tests -v
```

<details>
<summary><strong>常见问题</strong></summary>

### 它会把剪贴板直接粘进目标框吗？

汉字录入经过拼音字母按键和候选确认；英文、数字、标点和 emoji 使用字符事件。剪贴板用于读取原文和最终导出本次结果。它仍然是软件自动化输入，不能据此证明文字由人工创作，也不保证符合某个平台的提交规则。

### 我的文字会发送到哪里？

`--offline` 不调用模型。默认混合模式将原文规划请求发送到配置的 Ollama 服务，默认地址为本机 `http://127.0.0.1:11434`。原有前后文用于范围定位，不发送给规划模型。本地 `runs/` 日志包含原文、计划和结果；它默认被 Git 忽略。

### 能更换模型或增加专业词吗？

可以。使用 `--url` 和 `--model` 指定 Ollama 服务与已安装模型；编辑 [lexicon.txt](pinyin_agent/lexicon.txt) 增补词语，[pronunciations.json](pinyin_agent/pronunciations.json) 维护特殊读音，[typing_hints.json](pinyin_agent/typing_hints.json) 维护经过验证的辅助词。具体格式与命令见 [使用说明](docs/USAGE.md)。

### 为什么按快捷键没有开始？

确认快捷窗口仍在运行、快捷键未被其他程序占用，并已点击可编辑的输入位置。窗口会显示目标控件、输入法或规划错误。常见故障处理见 [使用说明](docs/USAGE.md#常见问题)。

</details>

## 文档与参与

- [使用说明](docs/USAGE.md)：启动参数、模型配置、选词、节奏及故障排查。
- [发布说明](RELEASES.md)：版本变化。
- [验证记录](VALIDATION.md)：实际输入证据与兼容边界。
- [README 参考研究](docs/README_RESEARCH.md)：参考项目与图像来源。

遇到问题时，请在 Issue 中提供版本、Windows 与输入法版本、控件类型、可公开的最短复现文字，以及错误提示。日志含录入内容，分享前请删去个人信息。

感谢 [jieba](https://github.com/fxsjy/jieba)、[pypinyin](https://github.com/mozillazg/python-pinyin)、[uiautomation](https://github.com/yinkaisheng/Python-UIAutomation-for-Windows) 与 [Ollama](https://github.com/ollama/ollama)。本 README 的组织方式参考 [Browser Use](https://github.com/browser-use/browser-use#readme)、[smolagents](https://github.com/huggingface/smolagents#readme) 等项目；演示与配图来自本项目。

请在允许自动化录入的环境中使用。
