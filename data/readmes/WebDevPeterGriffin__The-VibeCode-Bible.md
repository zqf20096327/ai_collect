<div align="center">

# The VibeCode Bible

**You built it with AI and it works. This is how you make it hold up, survive real users, and get them in the first place.**

By [@web.dev.george](https://instagram.com/web.dev.george). Free, and it runs on your machine.

</div>

---

## Quick start

```bash
git clone https://github.com/WebDevPeterGriffin/The-VibeCode-Bible.git
cd The-VibeCode-Bible
npm run setup
npm run dev
```

Open http://localhost:3000. The app only listens on your own machine.

`npm run setup` installs the packages and downloads the two small models Local Chat uses (about 3.5 GB). It needs [Ollama](https://ollama.com/download) installed and tells you if it's missing. You can also skip it and press the download button in Local Chat. If you only want to read, run `npm install` instead. The lessons, Security Scan and read aloud don't need a model.

## Who it's for

Developers who can already build a working demo with AI agents, and who want real users or are nervous about what happens when they arrive. It isn't a beginner course.

## What's inside

Every lesson ends with something to run on your own project. Stories either happened to me or link to a public write-up.

| Part | What it covers |
|---|---|
| **Start Here** | The one idea: prove each safety net by triggering it |
| **Make It Hold Up** | Proving code works, tests, access control, payments, database changes and backups, undoing mistakes, deploys |
| **Real Users Arrive** | Changing a live app, actions that run twice, monitoring, bots and abuse, surprise bills |
| **Get Real Users** | Finding your first users, and showing what you built |
| **Working With the Agent** | Planning, context, debugging, made-up APIs, when to write it yourself, not looking AI-made |
| **Running Agents** | Several agents at once, how agents work, prompt injection |
| **Local AI** | The honest limits, setup, skill files or a LoRA |
| **Tool Notes** | Dated notes on tools and models, kept apart from the lessons because they age quickly |
| **LoRA Deep Dive** | An optional track on training your own |

## Tools built in

- **Local Chat** answers from these lessons using a model on your machine, tells you which lesson it used, and says so when the lessons don't cover something.
- **Security Scan** checks a folder on your computer for leaked secrets and committed `.env` files. It works on private projects, needs no model, and masks everything it finds.
- **The Playbook Test** scores a startup idea against [Sam Altman's startup playbook](https://playbook.samaltman.com/), using your local model by default.
- **Read aloud** on every lesson, using your browser's built-in speech.
- **About 1,350 agent skill files and 10 workflows** in `.agent/`, mostly Awesome CursorRules, from the open-source projects below. These are other people's work, so read a skill before you trust it.

| Skill pack | Original creator |
|---|---|
| Awesome CursorRules | [@PatrickJS](https://github.com/PatrickJS/awesome-cursorrules) |
| Claude SEO | [@AgriciDaniel](https://github.com/AgriciDaniel/claude-seo) |
| UI/UX Design Agent | [@nextlevelbuilder](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) |
| Honnibal Claude Skills | [@honnibal](https://github.com/honnibal/claude-skills) |

## Support

It's free. If it saved you time, you can [buy me a coffee](https://webdevpeter.net/pages/the-vibecode-bible). No pressure.
