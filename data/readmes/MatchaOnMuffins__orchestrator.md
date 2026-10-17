<div align="center">

# Orchestrator

A desktop app for running multiple Claude Code agents on the same repo at the same time.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Electron](https://img.shields.io/badge/Electron-35-47848F.svg)](https://www.electronjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-3178C6.svg)](https://www.typescriptlang.org/)

![Orchestrator running 4 agents simultaneously](assets/orchestrator.png)

</div>

## The idea

Sometimes you want multiple Claude Code agents working on different parts of a codebase at the same time. The problem is they'll step on each other if they're all editing the same files in the same directory.

Orchestrator solves this by giving each agent its own git worktree and branch. You can see what all of them are doing, send them follow-up messages, and come back later to pick up where you left off.

## What it does

Each agent gets an isolated copy of the repo via `git worktree`. You can have up to 10 running at once. The interface is split into panes (like tmux) so you can watch several agents work side by side. Every tool call, file edit, and token count shows up in real time.

Sessions are saved to disk, so if you close the app and come back, your agents resume with their full conversation history intact.

## Getting started

You'll need Node 18+ and the [Claude Code CLI](https://www.npmjs.com/package/@anthropic-ai/claude-code) installed and authenticated.

```bash
git clone https://github.com/MatchaOnMuffins/orchestrator.git
cd orchestrator
npm install
npm run dev:electron
```

The app will open and ask you to pick a git repo. From there, click "+ New" to create an agent, type what you want it to do, and it'll start working.

## Built with

Electron, React 19, Zustand, Tailwind CSS, Vite, and TypeScript.

## License

[MIT](LICENSE)
