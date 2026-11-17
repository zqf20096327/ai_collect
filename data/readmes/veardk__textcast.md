<div align="center">
  <img src="assets/icon.png" alt="Textcast" width="120">
  <h1>Textcast</h1>
  <p><strong>Read podcasts and videos instead of watching them, and talk with your agent while you read.</strong></p>
  <p>
    <a href="LICENSE"><img src="https://img.shields.io/github/license/veardk/textcast?style=flat-square" alt="License"></a>
    <a href="https://github.com/veardk/textcast/releases"><img src="https://img.shields.io/github/v/release/veardk/textcast?style=flat-square" alt="Release"></a>
    <a href="https://github.com/veardk/textcast/stargazers"><img src="https://img.shields.io/github/stars/veardk/textcast?style=flat-square" alt="Stars"></a>
    <a href="#install"><img src="https://img.shields.io/badge/Agent-Skill-1B365D?style=flat-square" alt="Agent Skill"></a>
  </p>
  <p><strong>English</strong> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a></p>
</div>

Textcast turns a podcast or video into text you can actually read: the full transcript, translated into your language, organised into topics with analysis, in one reading page. You read at your own pace instead of scrubbing through an hour of audio.

The page is live. It opens in a reading window with your agent beside it: select any sentence to ask about it, or ask for a change, and the agent answers and updates the page while you read. Click any line and the video plays from that moment in a small floating player, so you can always hear how it was said.

Long articles and documents work too. Textcast is an Agent Skill: your agent does the reading and translating itself, and the scripts handle captions, timing and checks, so no line is ever summarised away.

## Install

Pick one route per agent. Installing the same Skill twice (for example as a plugin and with `npx skills`) gives your agent two copies.

### Any agent (recommended)

```bash
npx skills@latest add veardk/textcast -g
```

`-g` installs it for your user, so it works in every folder. Add `-a <agent>` to choose the agent up front (`claude-code`, `codex`, `cursor`, `opencode`, `windsurf`, …), or leave it out and pick from the list. To update, run `npx skills@latest update textcast`.

<details>
<summary><strong>Claude Code</strong> (plugin)</summary>

```bash
claude plugin marketplace add veardk/textcast
claude plugin install textcast@veardk
```

To update, run `claude plugin marketplace update veardk`, then `claude plugin update textcast@veardk`.

</details>

<details>
<summary><strong>Codex</strong> (plugin)</summary>

```bash
codex plugin marketplace add veardk/textcast
codex plugin add textcast@veardk
```

Updates itself at startup.

</details>

<details>
<summary><strong>GitHub Copilot</strong> (CLI and VS Code)</summary>

```bash
copilot plugin marketplace add veardk/textcast
copilot plugin install textcast@veardk
```

In VS Code, run **Chat: Install Plugin From Source** and enter `https://github.com/veardk/textcast`.

</details>

<details>
<summary><strong>Gemini CLI</strong></summary>

```bash
gemini skills install https://github.com/veardk/textcast.git --path skills/textcast
```

Run it again to update.

</details>

<details>
<summary><strong>Manual</strong> (git clone)</summary>

Clone the repository and copy the Skill folder into your agent's skills folder. For Claude Code:

```bash
git clone https://github.com/veardk/textcast.git
cp -R textcast/skills/textcast ~/.claude/skills/
```

To update, pull and copy it again.

</details>

## Use

Ask your agent, for example:

> /textcast https://www.youtube.com/watch?v=…

> Turn https://www.youtube.com/watch?v=… into a Textcast page in Chinese.

The agent fetches the source, translates it, groups it into topics, publishes the page and opens it in a reading window where you can ask about any sentence.

## Features

- **Read instead of watch**: the full transcript of a YouTube or Bilibili podcast or video, every line in order, nothing left out.
- **In your language**: original, translation or side-by-side bilingual reading, translated by your agent.
- **Talk while you read**: the page opens in a reading window ([textcast-chat-axi](https://github.com/veardk/textcast-chat-axi)) with a live conversation panel. Select any text to ask your agent about it, or ask for a change, and the page updates in place.
- **Floating video player**: click any line and the video plays from that moment in a small window beside the text, so you can listen and keep reading.
- **Topics and analysis**: the transcript is grouped into topic cards, each with the agent's explanation, plus an optional summary page.
- **Timestamps you can trust**: every time comes from the captions, never guessed.
- **Any long text, too**: subtitle files (`.srt`, `.vtt`, `.json`), Markdown or text, or text from a PDF or web page.
- **Your own library**: pages are grouped into categories with an index page, in light, dark or sepia, with labels in 17 languages.

## Where the pages go

Pages are written to `./textcast/output/` inside the folder where you run your agent, not into the skill folder:

```text
textcast/output/
├── index.html                      # the library
├── <category>/NN-<slug>.html       # transcript page
├── <category>/NN-<slug>-summary.html
└── .work/                          # intermediate files (captions, translations)
```

Every page is a single HTML file that also works when opened directly.

## Requirements

- Python 3.10 or later (standard library only)
- Node.js 22 or later, for the caption fetchers and the reading window (`npx` downloads it on first use)
- `yt-dlp` (optional), used automatically when the YouTube fetcher fails
- Bilibili captions need a logged-in session. The fetcher reads the cookie from your browser or offers a QR login, and saves it in `~/.textcast/`.

Local audio or video transcription is not supported yet. For such files, provide a subtitle file.

## Feedback

Open an [issue](https://github.com/veardk/textcast/issues) for bugs or ideas. Problems with the reading window itself belong in [textcast-chat-axi](https://github.com/veardk/textcast-chat-axi/issues).

## Acknowledgements

The page design and colours are inspired by [Kami](https://github.com/tw93/Kami).

## License

[MIT](LICENSE)
