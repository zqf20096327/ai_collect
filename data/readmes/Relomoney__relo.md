# Relo Money

Get paid to code with AI.

Relo is an open-source developer monetization platform that pays developers for their attention while using AI coding tools like Claude Code, Cursor, and Codex.

Developers already spend hundreds of dollars every month on AI tools. Relo helps offset those costs by allowing developers to earn money from sponsored messages displayed while their AI models are working.

Instead of interrupting your workflow with traditional ads, Relo uses the natural waiting periods during AI inference to connect developers with relevant products, tools, and services.

## How It Works

1. **Install Relo.** Integrate Relo into your existing AI coding workflow.
2. **Keep coding.** Continue using your favorite AI development tools without changing how you work.
3. **View sponsored messages.** Relevant advertisements appear during AI processing and waiting periods.
4. **Earn money.** Receive compensation for verified 10-second sponsored views.
5. **Track your earnings.** Monitor verified views, earnings, and payouts through your dashboard.

```
npx relo-money init
```

Earnings: https://relo.money/dashboard

## Built for Developers

Relo is designed around a simple principle: developer attention has value, and developers should benefit from it.

- **Earn while coding:** Monetize time already spent working with AI tools.
- **No workflow disruption:** Sponsored messages appear during natural waiting periods.
- **Transparent earnings:** Track verified views and payouts in your dashboard.

## What's in this repository

- `cli/` — the `relo-money` command. `init` copies it to `~/.relo/relo.js` and configures the tools it finds.
- `cursor-extension/` — shows the current sponsored line in the Cursor status bar. It reads `~/.relo/state-cursor.json`, which the CLI writes. It does not talk to the network itself.

## Privacy

Relo does not read your code, prompts, or conversations. Hooks may pass prompt text on stdin so the process does not stall; that input is discarded and never sent.
