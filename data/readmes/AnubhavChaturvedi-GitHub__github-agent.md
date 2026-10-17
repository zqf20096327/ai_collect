# GitHub Agent: Browser-Native AI Assistant for GitHub

> Chat with your GitHub repositories from a local web app. Browse code, search repos, review issues and run repository tasks through an AI assistant that runs entirely in your browser with no backend server.

[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE.txt)
[![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)](https://vitejs.dev/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/docs/Web/JavaScript)
[![No Backend](https://img.shields.io/badge/Backend-None_Required-success?style=for-the-badge)](#)

![GitHub Agent demo](Demo%20Video.gif)

## What it does

GitHub Agent is a single-page app that connects to the GitHub API with your personal access token and puts an AI assistant in front of it. Ask questions about a repository in plain English and get answers grounded in the actual code, issues and commit history.

Because it is browser native, your token never leaves your machine. There is no server to deploy and nothing to trust beyond the code in this repo.

## Features

- **Repository chat**: ask about any repo you can access and get answers from real file contents
- **Code search**: find functions, patterns and files across a repository
- **Issue and PR context**: pull in discussions to inform answers
- **Local first**: your GitHub token stays in the browser, no proxy server
- **Zero deployment**: `npm run dev` and you are working
- **Fast**: built on Vite for instant startup and hot reload

## Getting started

### Prerequisites

- Node.js 18 or newer
- A GitHub personal access token with `repo` scope

### Installation

```bash
git clone https://github.com/AnubhavChaturvedi-GitHub/github-agent.git
cd github-agent
npm install
npm run dev
```

Open the printed localhost URL, paste your token when prompted, and pick a repository.

### Build for production

```bash
npm run build
npm run preview
```

The output in `dist/` is a static bundle you can host anywhere.

## Security note

Create a **fine-grained** personal access token scoped to only the repositories you want the agent to see, and give it read-only permissions unless you specifically need writes. Never commit a token to a repository.

## Tech stack

Vite, vanilla JavaScript, the GitHub REST API, ESLint.

## Contributing

Issues and pull requests are welcome.

## License

Released under the [MIT License](LICENSE.txt).

## Author

**Anubhav Chaturvedi**, founder of [NetHyTech](https://www.youtube.com/@NetHyTech), a developer community of 30,000+ members.

[![YouTube](https://img.shields.io/badge/YouTube-NetHyTech-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/@NetHyTech)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/anubhav-chaturvedi-/)

If this project saved you time, a star on the repo helps other people find it.
