<div align="center">

<img src="app/web/assets/icon-256.png" width="112" alt="Adaptive Subs">

# Adaptive Subs

看 B 站和 YouTube 的英语视频时，字幕保持英文，只给你**不认识的词**配中文。

[![最新版本](https://img.shields.io/github/v/release/LuoYu2233/adaptive-subs-app?include_prereleases&label=%E6%9C%80%E6%96%B0%E7%89%88%E6%9C%AC)](https://github.com/LuoYu2233/adaptive-subs-app/releases)
[![下载次数](https://img.shields.io/github/downloads/LuoYu2233/adaptive-subs-app/total?label=%E4%B8%8B%E8%BD%BD)](https://github.com/LuoYu2233/adaptive-subs-app/releases)
[![Windows](https://img.shields.io/badge/Windows-10%20%7C%2011-0078D4)](#下载安装)
[![Chrome / Edge](https://img.shields.io/badge/Chrome%20%2F%20Edge-%E6%8F%92%E4%BB%B6-4285F4)](#下载安装)
[![B 站 · YouTube](https://img.shields.io/badge/B%20%E7%AB%99%20%C2%B7%20YouTube-%E6%94%AF%E6%8C%81-FB7299)](#快速开始)
[![License: MIT](https://img.shields.io/github/license/LuoYu2233/adaptive-subs-app)](LICENSE)

**[⬇ 下载 Windows 程序](https://github.com/LuoYu2233/adaptive-subs-app/tags)** · [使用指南](docs/使用指南.md) · [开发说明](docs/开发说明.md)

</div>

## 一分半钟看懂

https://github.com/user-attachments/assets/221990b0-7ff8-42eb-b053-d14300c0efad


## 为什么做这个

<p align="center"><img src="docs/images/intro.png" width="420" alt="效果示意：只给 boring 标了中文"></p>

想通过看英文原声视频沉浸式学英语，字幕却怎么选都别扭：开中英双语，眼睛会不由自主地去读中文；只开英文，一句话里有两个生词就整句听不懂。

Adaptive Subs 提出了一种新方法：**字幕整句都是英文，只在你可能不认识的单词、短语和"熟词僻义"上方标一个简短的中文**。它先通过考试成绩和词汇测试了解你的水平，再结合每句话的上下文判断该标哪些词、该怎么解释。


## 功能

- **按你的水平注释**：填考试成绩（高考 / 四六级 / 考研 / 雅思 / 托福）、做 3 分钟自适应词汇测试，生成你的熟词库，熟词库里的词不再注释
- **结合上下文**：注释是这句话里的意思；能标出短语、习语和熟词僻义（认识 upset，也会解释 "upset the order" 里的"打乱"）
- **点单词**：点字幕里任意一个词，看它在这句里的意思和词典释义，一键标「我认识」或「我不认识」，以后自动按你的标记来
- **听不懂时偷看一眼**：按住 Z 临时显示这一句的中文，松开就消失；按 B 在自适应 / 纯英文 / 中英对照之间切换
- **B 站和 YouTube 都能用**：插件直接显示在网站自己的播放器上，切换视频、全屏都跟着走
- **没有英文字幕也能用**：语音识别生成英文字幕，边下载边识别，几秒钟出第一句；被接口审核拒绝的句子由本机模型补上
- **画面里印着字幕的视频**：按 P 打开一块可拖动的遮挡板，盖住原来的中文字幕，眼睛只看英文
- **只用你自己的 key**：注释模型可选 DeepSeek / 小米 MiMo / OpenAI，key 只保存在你的电脑上；生成过的视频会保存，再看不花钱

## 下载安装

到 **[Releases](https://github.com/LuoYu2233/adaptive-subs-app/releases)** 下载最新的 `AdaptiveSubs-Windows.zip`（约 180 MB），解压后有：

| 文件 | 作用 |
|---|---|
| `程序/AdaptiveSubs.exe` | 本地程序：生成注释、语音识别，看视频时保持运行（可以最小化） |
| `浏览器插件/` | Chrome / Edge 插件：在 B 站和 YouTube 的播放器上显示字幕和注释 |
| `使用说明.txt` | 离线版使用说明 |

**系统要求**：Windows 10 / 11（需要系统自带的 Edge WebView2，Windows 11 已内置），Chrome 或 Edge 浏览器，一个注释模型的 API key。

## 快速开始

<p align="center"><img src="docs/images/panel.png" width="760" alt="程序窗口"></p>

1. **打开程序**：解压后双击 `程序/AdaptiveSubs.exe`
   - Windows 提示"已保护你的电脑"时，点「更多信息」→「仍要运行」（程序没有数字签名）
2. **填 API key**：在程序窗口点「填写 API key」，选一个注释模型，填入你自己的 key（国内推荐 [DeepSeek](https://platform.deepseek.com/api_keys)），点「保存并测试」
   - 想用语音识别，再填一个[小米 MiMo](https://platform.xiaomimimo.com) 的 key（可选）
3. **装插件**：浏览器打开 `chrome://extensions`（Edge 是 `edge://extensions`），打开「开发者模式」，点「加载已解压的扩展程序」，选 `浏览器插件` 文件夹
4. **建立英语画像**：在程序窗口「准备情况 → 英语画像」点「开始」，填考试成绩、做词汇测试（约 3 分钟，可以跳过，之后再做）
5. **看视频**：打开一个英语视频
   - **B 站**：先登录（B 站只把字幕给登录用户）。有英文字幕的马上显示纯英文，点视频左上角的「生成注释」开始注释（边看边生成）
   - **YouTube**：程序去取英文字幕（上传者的或 YouTube 自动生成的），几秒后显示纯英文，同样点「生成注释」开始注释
   - 没有英文字幕：点视频左上角的「语音识别英文字幕」

更多用法（插件设置、遮挡板、点词、语音识别、常见问题）见 **[使用指南](docs/使用指南.md)**。

<p align="center"><img src="docs/images/popup.png" width="300" alt="插件弹窗"></p>

## 费用与隐私

- **费用**：按你自己的 key 计费。注释每 10 分钟视频约 ¥0.1–0.3（看模型），语音识别每 10 分钟约 ¥0.1，都只在你点了「生成注释」/「语音识别英文字幕」后才用；本机模型补识别不花钱
- **隐私**：key、英语画像、生成过的视频都只保存在你的电脑上（`%LOCALAPPDATA%\AdaptiveSubs`）；程序只在本机 `127.0.0.1` 运行；你的 B 站、YouTube 登录信息不会离开浏览器

## 常见问题

**插件提示"程序没开"**：确认 Adaptive Subs 程序开着（可以最小化），然后刷新视频页面。

**YouTube 提示"连不上 YouTube"**：YouTube 的字幕由程序去取，程序要能连上 YouTube。用代理软件的话，打开它的「系统代理」，再点「重试」。

**字幕和画面里原有的字幕重叠了**：看视频时按 P 打开遮挡板，把它拖到原字幕的位置，按 UP 主记住；再按 P 关掉。

**有些词我认识却被注释了 / 不认识却没注释**：点那个词，选「我认识」或「我不认识」；或者在程序里重新做一次词汇测试。

更多问题见[使用指南 · 常见问题](docs/使用指南.md#常见问题)。

## 从源码运行

需要 Python 3.12，在命令提示符（cmd）里运行：

```bat
git clone https://github.com/LuoYu2233/adaptive-subs-app.git
cd adaptive-subs-app
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python -m spacy download en_core_web_sm
start.bat
```

目录结构、打包、重新生成数据和发布新版本的步骤见 **[开发说明](docs/开发说明.md)**。

```
app/          本地程序（Python 服务器 + 程序窗口的网页）
extension/    浏览器插件（B 站、YouTube）
docs/         使用指南、开发说明
packaging/    打包成 Windows 程序
tools/        生成考试词表、题库、图标、在线演示的脚本
```

## 致谢

- [ECDICT](https://github.com/skywind3000/ECDICT)：考试词表和词典释义（MIT）
- [faster-whisper](https://github.com/SYSTRAN/faster-whisper) / [Whisper](https://github.com/openai/whisper)：本机语音识别
- [spaCy](https://spacy.io)、[wordfreq](https://github.com/rspeer/wordfreq)：分词、词形还原和词频
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)、[PyAV](https://github.com/PyAV-Org/PyAV)：音频获取和解码
- [pywebview](https://github.com/r0x0r/pywebview)：程序窗口
- 界面设计参考了 [React Bits](https://github.com/DavidHDev/react-bits)、[Magic UI](https://magicui.design) 的交互效果

程序图标和入场动画里的插画不在 MIT 许可范围内，版权归原作者所有。

## 许可证

代码以 [MIT License](LICENSE) 开源。
