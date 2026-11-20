<!--
Use repository-root paths for local files (docs/images/logo.png, LICENSE) so they open on every
branch. Link to the guides in this README with absolute GitHub URLs so the npm copy opens the
rendered guides and their section links. Put pictures in docs/images/, which the npm package
carries. Write links and pictures as inline Markdown links or as src and href attributes in double quotes.
Double-quoted srcset attributes are also rewritten, preserving each image candidate's descriptor.
Other forms are not rewritten for npm.
npm resolves no relative path, so the release rewrites each one in the packaged copy
(apps/backend/src/release/npm-readme.ts): a file the package carries opens from
https://unpkg.com/alpacawork@<version>/<path>, any other file from
https://github.com/alpacakit/alpacawork/blob/main/<path>.
The setup guide an AI downloads uses a GitHub raw URL so the AI can read the Markdown directly.
GitHub plays a video only from the URL it gives when the file is uploaded on github.com, written on
a line of its own; it drops a <video> tag that points anywhere else, and npm shows such a URL as
plain text.
The name at the top is a picture (wordmark.png, wordmark-dark.png for dark pages) so that it shows
larger than a heading can; its alt text carries the name.
The pictures show made-up data. This file and its translations use the dark-theme pictures
(*-dark.png); README.ja.md shows the Japanese screen (*-dark-ja.png), the others the English one.
README.ja.md, README.zh-CN.md, README.es.md and README.pt-BR.md are translations: keep all five with
the same sections and content, and change them in the same commit. Each links to the guides in its
own language (this file to docs/, the others to docs/ja/, docs/zh-CN/, docs/es/, docs/pt-BR/).
Each guide links back to the install heading of the README in its language (docs/getting-started.md
to README.md#install): keep those headings, or change the links with them.
-->

<p align="center">
  <b>English</b> · <a href="README.ja.md">日本語</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.es.md">Español</a> · <a href="README.pt-BR.md">Português (Brasil)</a>
</p>

<h1 align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/images/wordmark-dark.png">
    <img src="docs/images/wordmark.png" alt="alpacawork" width="380">
  </picture>
</h1>

<h3 align="center">Let AI manage your AI.</h3>

<p align="center">
  It assigns work to Claude Code and Codex<br/>and tracks their progress.<br/>
  You no longer have to sit at your PC to work.
</p>

<p align="center">
  <a href="#install"><b>Install</b></a> ·
  <a href="https://github.com/alpacakit/alpacawork/blob/main/docs/getting-started.md">Getting started</a> ·
  <a href="https://github.com/alpacakit/alpacawork/blob/main/docs/concept.md">How it works</a>
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/alpacawork"><img alt="npm" src="https://img.shields.io/npm/v/alpacawork?style=flat-square"></a>
  <a href="LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/license-MIT-blue?style=flat-square"></a>
</p>

<!-- The intro video goes here once it is uploaded on github.com: one line holding the URL GitHub gives. Then move the picture below to the end of the features list. -->

<p align="center">
  <img src="docs/images/pc-phone-dark.png" alt="alpacawork in a PC browser, with a list of ten tasks in progress and three awaiting review beside an open task's report, and a phone on the right showing the same report" width="820">
</p>

alpacawork is a tool (an AI harness) that runs the Claude Code and Codex agents already installed on your PC and assigns work to them. Write what you want in one chat box, and your point of contact, an AI called the coordinator, turns it into tasks, assigns them to other AIs and tracks progress. You do three things: ask, answer questions, and check the results. You can use it from your phone in the same way.

## Install

Paste the following text into Claude Code or Codex on your PC. The AI installs alpacawork, and the setup screen opens in your browser.

```text
Download the guide below, read all of it, and follow it to install alpacawork on this PC.
https://raw.githubusercontent.com/alpacakit/alpacawork/main/skills/alpacawork/references/setup.md
```

To install with commands, run these two lines in a terminal, in order.

```sh
npm install -g alpacawork
alpacawork setup
```

- **Requirements:** macOS (Apple silicon), Linux (x64) or Windows (inside WSL2). You need an AI agent you are signed in to, such as Claude Code or Codex, and Node.js 24.16 or later (if an AI does the install, it installs Node.js when it is missing). [Full requirements](https://github.com/alpacakit/alpacawork/blob/main/docs/getting-started.md#requirements)
- **After installing:** [Make your first request](https://github.com/alpacakit/alpacawork/blob/main/docs/getting-started.md#2-make-your-first-request). To use it from your phone, connect to your PC over a VPN such as Tailscale ([Use it from your phone](https://github.com/alpacakit/alpacawork/blob/main/docs/getting-started.md#5-use-it-from-your-phone)).
- **Stopping and uninstalling:** [Stop, update or uninstall](https://github.com/alpacakit/alpacawork/blob/main/docs/getting-started.md#7-stop-update-or-uninstall)

## What it does

- **Write every request in one chat box.** The coordinator turns each request into a task and hands it to an AI. You never have to switch chats or AIs from one job to the next.
- **AI manages several AIs at once.** To add to or change work in progress, you only tell the coordinator. Write "For all three tasks in progress, also check the phone layout," and the coordinator gives that instruction to each AI working on them.
- **Describe a workflow in words, and the AIs carry it out together.** Even an involved one, such as "Make three proposals, each with a different model. Combine them into one, have another AI review it, and fix it before you report," is carried out as you described it: AI manages the steps, and the AIs hand work to one another.
- **Questions from the AI come with options and a recommendation.** Questions and reports arrive with images and videos. Pick an option to answer.
- **A screen built for phones.** Swipe right to answer a question or to mark a result done. You can take a task from request to done on your phone alone. The same screen also works in a browser on your PC.
- **It runs in your usual setup.** `AGENTS.md`, `CLAUDE.md`, skills, MCP and hooks work unchanged. You don't need an account or an API key for alpacawork.

## Good to know

- **It is free (MIT License).** AI usage is billed under your existing Claude Code, Codex or other plan.
- **It runs on your PC.** The AI runs on your PC, so keep the PC on and set it not to sleep while you use alpacawork.
- **It starts AI agents in the same no-approval mode as Claude Code's `bypassPermissions` and Codex's `danger-full-access`, so they don't stop to ask.** You can write what the AI should not do, or should ask you about first, in the [project policy](https://github.com/alpacakit/alpacawork/blob/main/docs/getting-started.md#4-write-the-ground-rules-for-the-ai).
- **Tasks, conversations and result files are kept on your PC.** alpacawork does not send them to any outside server run by its developers. Your instructions to the AI, and what the AI reads, are sent to the AI's provider, just as when you use each AI agent directly ([more on how data is handled](https://github.com/alpacakit/alpacawork/blob/main/docs/getting-started.md#what-is-stored-and-what-is-sent-out)).

## Documentation

- [Getting started](https://github.com/alpacakit/alpacawork/blob/main/docs/getting-started.md): from installing to your first request, using it from your phone, updating and uninstalling
- [The ideas behind alpacawork](https://github.com/alpacakit/alpacawork/blob/main/docs/concept.md): how one request moves along, and the design principles
- [Troubleshooting](https://github.com/alpacakit/alpacawork/blob/main/docs/getting-started.md#troubleshooting): when something doesn't work. Please report bugs in [Issues](https://github.com/alpacakit/alpacawork/issues)

## License

[MIT License](LICENSE)
