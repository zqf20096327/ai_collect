<h1 align="center">Code Capsule</h1>

<p align="center">
  Describe an app. Watch it get written, then run — live, in a sandbox, in the browser.
</p>

<p align="center">
  <a href="https://www.youtube.com/watch?v=BOS7pP7KyWc"><img src="https://img.shields.io/badge/watch%20the%20build-YouTube-FF0000?logo=youtube&logoColor=white" alt="Watch the build"></a>
  <img src="https://img.shields.io/badge/E2B-sandboxes-FF8800" alt="E2B">
  <img src="https://img.shields.io/badge/Vercel%20AI%20SDK-000000?logo=vercel&logoColor=white" alt="Vercel AI SDK">
  <img src="https://img.shields.io/badge/Next.js-000000?logo=nextdotjs&logoColor=white" alt="Next.js">
</p>

<p align="center">
  <a href="https://www.youtube.com/watch?v=BOS7pP7KyWc">
    <img src="https://img.youtube.com/vi/BOS7pP7KyWc/maxresdefault.jpg" width="720" alt="Build a Code Capsule — instantly generate and preview UI code with AI">
  </a>
</p>

---

## What it does

You type what you want. A model writes the code, streaming it into the editor as it goes. The result is
then **executed in a real E2B sandbox** — a fresh container with the dependencies already installed — and
the running app is streamed back into an iframe beside the code.

Not a preview of what the code might do. The actual thing, running.

**19 models across 8 providers.** OpenAI (`o1-preview`, `o1-mini`, `gpt-4o`, `gpt-4o-mini`, `gpt-4-turbo`),
Anthropic (`claude-3-5-sonnet`), Google (`gemini-1.5-pro-002`, `gemini-1.5-flash-002`), Mistral, Groq,
Fireworks, Together AI, and local models through Ollama.

**Four sandbox templates**, each a prebuilt E2B image: Next.js, Vue/Nuxt, Streamlit and Gradio.
Next.js is the one wired up in `lib/templates.json` — the other three are built and ready, and enabling
one is a single entry in that file.

**Rate limiting** through Vercel KV, so a public deployment does not become someone else's free inference.

## Stack

| | |
|---|---|
| Framework | Next.js App Router, TypeScript |
| Model routing | Vercel AI SDK — `@ai-sdk/openai`, `@ai-sdk/anthropic`, `@ai-sdk/google`, `@ai-sdk/mistral`, `ollama-ai-provider` |
| Execution | `@e2b/code-interpreter` — one sandbox per generation |
| Auth | Supabase (optional, off by default) |
| Rate limiting | Vercel KV |
| Analytics | PostHog (optional, off by default) |
| UI | Tailwind CSS, Radix UI |

## Running it locally

```bash
git clone https://github.com/kuluruvineeth/codecapsule.git
cd codecapsule
npm install
```

Create `.env.local`. Only the E2B key and one model provider are required:

```bash
E2B_API_KEY=                     # https://e2b.dev/docs/getting-started/api-key
ANTHROPIC_API_KEY=               # or any one of the providers below
OPENAI_API_KEY=
GROQ_API_KEY=
FIREWORKS_API_KEY=
TOGETHER_AI_API_KEY=
GOOGLE_GENERATIVE_AI_API_KEY=
MISTRAL_API_KEY=

# optional
KV_REST_API_URL=                 # rate limiting
KV_REST_API_TOKEN=
RATE_LIMIT_MAX_REQUESTS=
RATE_LIMIT_WINDOW=
NEXT_PUBLIC_ENABLE_SUPABASE=false
NEXT_PUBLIC_ENABLE_POSTHOG=false
```

```bash
npm run dev
```

Open <http://localhost:3000>.

### Building your own sandbox template

Each template in `sandbox-templates/` is a Dockerfile plus an `e2b.toml`. To build and register one:

```bash
cd sandbox-templates/streamlit-developer
e2b template build
```

Then add its entry to `lib/templates.json`.

## Watch it being built

**[▶ Build a Code Capsule: Instantly Generate & Preview UI Code with AI](https://www.youtube.com/watch?v=BOS7pP7KyWc)**

---

Built by [**@kuluruvineeth**](https://www.youtube.com/@kuluruvineeth) — I build AI products and take them apart on camera.
