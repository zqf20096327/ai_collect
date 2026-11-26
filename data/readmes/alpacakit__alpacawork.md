<!--
Use repository-root paths for local files (docs/images/logo.png, LICENSE) so they open on every
branch. Link to the guides in this README with absolute GitHub URLs so the npm copy opens the
rendered guides and their section links. Put pictures in docs/images/. The package omits GIFs
and WebPs from that directory. Write links and pictures as inline Markdown links or as double-quoted src,
srcset or href attributes. Image descriptors in srcset are preserved.
Other forms of relative path are not rewritten for npm.
npm resolves no relative path, so the release rewrites each one in the packaged copy
(apps/backend/src/release/npm-readme.ts): a file the package carries opens from
https://unpkg.com/alpacawork@<version>/<path>. Pictures outside the package are served from
https://raw.githubusercontent.com/alpacakit/alpacawork/<release-commit>/<path>.
Other links outside the package open https://github.com/alpacakit/alpacawork/blob/main/<path>.
The setup guide an AI downloads uses a GitHub raw URL so the AI can read the Markdown directly.
GitHub plays a video only from the URL it gives when the file is uploaded on github.com, written on
a line of its own; it drops a <video> tag that points anywhere else. The packaged copy turns that
line into an explicit link to the video. To change a demo video, attach the new file to a pull
request comment (gh pr comment --attach) and write the URL GitHub gives it.
The name at the top is a picture (wordmark.png, wordmark-dark.png for dark pages) so that it shows
larger than a heading can; its alt text carries the name.
The pictures and videos show made-up data on the dark-theme screens. The demo under the introduction
is an animated WebP drawn as a rounded card with alpha, so it sits on light and dark pages alike
(demo-dark.webp). Each README shows the screens in its own language: demo-dark-<lang>.webp in the
translations, and each plays its own upload of the demo video.
The diagram at the top is drawn in each README's language (hero.gif, hero-dark.gif for this file;
hero-<lang>.gif, hero-dark-<lang>.gif for the others) and switches with the page theme in a <picture>;
its first and last frames are the finished picture.
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

<h3 align="center">Run all your AI agents from one chat.</h3>

<p align="center">
  Write a request. AI agents on your machine, such as Claude Code and Codex, split it into tasks and run them in parallel.<br/>
  You answer their questions and check the results. It works from your phone too.
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

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/images/hero-dark.gif">
    <img src="docs/images/hero.gif" alt="A request typed into one input box goes to the coordinator, which adds tasks to three projects (Website, Mobile app, Marketing) and places an AI such as opus · high or gpt-5 · high on each; one task asks a question, you answer, and every task finishes" width="640">
  </picture>
</p>

alpacawork is an orchestrator for the AI coding agents already on your PC, such as Claude Code and Codex: it hands them work and keeps track of it. Write what you want in one chat box, and your point of contact, an AI called the coordinator, turns it into tasks and assigns them to other AIs. You do three things: ask, answer questions, and check the results. You can use it from your phone in the same way.

<p align="center">
  <img src="docs/images/demo-dark.webp" alt="A request typed into the phone's chat box becomes three tasks that run in parallel in the PC's list; a result is checked and a swipe marks its task complete, and a question from the AI is answered by picking an option; then the phone and the PC side by side" width="800">
</p>

## Install

Paste the following text into Claude Code or Codex on your PC. The AI installs alpacawork and tells you the URL of the setup screen, which usually opens in your browser too.

```text
Download the guide below, read all of it, and follow it to install alpacawork on this PC.
https://raw.githubusercontent.com/alpacakit/alpacawork/main/skills/alpacawork/references/setup.md
```

To install with commands, run these two lines in a terminal (on Windows, inside Ubuntu), in order. Setup lists what it will set up and starts when you press Enter.

```sh
npm install -g alpacawork
alpacawork setup
```

It runs on macOS (Apple silicon), Linux (x64) and Windows (WSL2). After installing, follow [Getting started](https://github.com/alpacakit/alpacawork/blob/main/docs/getting-started.md) to make your first request.

### Open the screen

To open the screen in your browser, ask Claude Code or Codex like this (`$alpacawork` in Codex).

```text
/alpacawork open the screen
```

In a terminal, `alpacawork open` also opens it.

## What it does

See the whole flow on the real screens, from sending a request to marking a task complete (about 100 seconds, no sound).

https://github.com/user-attachments/assets/ab940260-e8aa-4810-bab6-0495a5207611

- **Write every request in one chat box.** The coordinator turns each request into a task and hands it to an AI. You never have to switch chats or AIs from one job to the next.
- **AI manages several AIs at once.** To add to or change work in progress, you only tell the coordinator. Write "For all three tasks in progress, also check the phone layout," and the coordinator gives that instruction to each AI working on them.
- **Describe a workflow in words, and the AIs carry it out together.** Even an involved one, such as "Make three proposals, each with a different model. Combine them into one, have another AI review it, and fix it before you report," is carried out as you described it: AI manages the steps, and the AIs hand work to one another.
- **Questions from the AI come with options and a recommendation.** Questions and reports arrive with images and videos. Pick an option to answer.
- **A screen built for phones.** Swipe right to answer a question or to mark a result done. You can take a task from request to done on your phone alone. The same screen also works in a browser on your PC.
- **It runs in your usual setup.** `AGENTS.md`, `CLAUDE.md`, skills, MCP and hooks work unchanged. You don't need an account or an API key for alpacawork.

## Good to know

- **It is free (MIT License).** AI usage is billed under your existing Claude Code, Codex or other plan.
- **It runs on your PC.** The AI runs on your PC, so keep the PC on and set it not to sleep while you use alpacawork.
- **It starts AI agents in the same no-approval mode as Claude Code's `bypassPermissions` and Codex's `danger-full-access`, so they don't stop to ask.** You can write what the AI should not do, or should ask you about first, in the [project policy](https://github.com/alpacakit/alpacawork/blob/main/docs/projects.md#project-policy).
- **Tasks, conversations and result files are kept on your PC.** alpacawork does not send them to any outside server run by its developers. Your instructions to the AI, and what the AI reads, are sent to the AI's provider, just as when you use each AI agent directly ([more on how data is handled](https://github.com/alpacakit/alpacawork/blob/main/docs/manage.md#where-your-data-is-and-what-is-sent-out)).

## Documentation

- [Getting started](https://github.com/alpacakit/alpacawork/blob/main/docs/getting-started.md): install, make one request, and check it
- [Documentation home](https://github.com/alpacakit/alpacawork/blob/main/docs/README.md): every page, including how to use it, settings and troubleshooting
- Please report bugs in [Issues](https://github.com/alpacakit/alpacawork/issues)
- Release announcements are posted on X at [@codemafia0000](https://x.com/codemafia0000)

## License

[MIT License](LICENSE)
