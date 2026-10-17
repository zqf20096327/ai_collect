# Express GitHub Issue triage agent

An AI agent that triages new GitHub issues. When an issue is opened, a GitHub webhook calls this Express app, the [AI SDK](https://ai-sdk.dev/) classifies the issue, and the agent applies labels and posts a maintainer reply. It deploys to Vercel as a single function with zero configuration and no database.

## How it works

```
GitHub issue opened
  → POST /api/webhooks/github   (signature verified)
  → 202 acknowledged immediately
  → waitUntil: generateObject (AI SDK) classifies the issue
  → Octokit applies labels + posts a reply
     (on failure: labels the issue `needs-triage` instead of failing silently)
```

The app is stateless, and each issue is triaged independently from its webhook payload. Issues the model classifies as spam are labeled but don't get a reply.

## Before you deploy

Have these three values ready. The deploy step sets them as environment variables.

- `AI_GATEWAY_API_KEY`, a [Vercel AI Gateway](https://vercel.com/docs/ai-gateway) key. The default model, `anthropic/claude-haiku-4.5`, runs on the free tier.
- `GITHUB_TOKEN`, a [fine-grained token](https://github.com/settings/personal-access-tokens) with **Issues: Read and write** on the repository you want triaged.
- `GITHUB_WEBHOOK_SECRET`, any random string you choose now. You give the same value to Vercel here and to GitHub when you create the webhook.

## Deploy

Click Deploy, then paste the three values above when Vercel prompts for environment variables.

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/vercel-labs/express-issue-triage-agent-template&env=AI_GATEWAY_API_KEY,GITHUB_TOKEN,GITHUB_WEBHOOK_SECRET&envDescription=AI%20Gateway%20key%2C%20GitHub%20token%2C%20and%20webhook%20secret)

Prefer the command line? Clone the repo, run `npm install`, then `vercel --prod` with the [Vercel CLI](https://vercel.com/docs/cli), and set the same three variables in the project's settings.

Either way, Vercel builds and returns a production URL like `https://your-app.vercel.app`.

## Connect the webhook

In the repository you want triaged, go to **Settings → Webhooks → Add webhook** and set:

- Payload URL: `https://your-app.vercel.app/api/webhooks/github`
- Content type: `application/json`
- Secret: the same `GITHUB_WEBHOOK_SECRET` you set during deploy
- Which events: choose **Let me select individual events**, then check only **Issues**

Open a new issue in that repository. Within a few seconds the agent labels it and posts a triage comment.

## Local development

```bash
vercel dev
```

GitHub needs a public URL to deliver webhooks, so expose your local server with a tunnel (e.g. `ngrok http 3000`) and point the webhook's Payload URL at it while testing.

## Project structure

| File | Purpose |
|------|---------|
| `src/index.ts` | Express app: verifies the webhook signature, filters for opened issues, runs triage in `waitUntil` |
| `src/triage.ts` | AI SDK `generateObject` call with a Zod schema for the triage decision |
| `src/github.ts` | Octokit calls to label the issue and post the reply, plus a `needs-triage` fallback |
| `vercel.json` | Vercel configuration |

## Customize

- **Reply tone and behavior:** the classification and reply come entirely from the prompt in `src/triage.ts`, steered by each field's `.describe()` text. Edit the prompt to change the voice (formal, terse, technical), to require specifics like reproduction steps, or to follow your project's conventions.
- **Triage shape:** edit the Zod schema in `src/triage.ts` to change the fields the model returns.
- **Model:** change the model string in `src/triage.ts` to any model the AI Gateway supports.
- **Skip the Gateway:** to use a provider key directly (no Vercel AI billing), `npm install @ai-sdk/anthropic`, import it, set `model: anthropic('claude-haiku-4-5')`, and set `ANTHROPIC_API_KEY` instead of `AI_GATEWAY_API_KEY`.
- **More events:** subscribe to additional webhook events on GitHub and register another handler, e.g. `webhooks.on('pull_request.opened', ...)`, in `src/index.ts`.

## Learn more

- [How to ship an Express app on Vercel](https://vercel.com/kb/guide/ship-a-express-app-on-vercel)
- [AI SDK documentation](https://ai-sdk.dev/)
- [Vercel Functions](https://vercel.com/docs/functions)
