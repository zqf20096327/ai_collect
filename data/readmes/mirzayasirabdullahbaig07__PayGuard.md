# PayGuard

**Know who you're invoicing before you send the quote.**

PayGuard is a risk-assessment tool for freelancers and independent contractors. Type what you know about a prospective client — payment history, communication style, anything you've heard — and PayGuard analyzes it for concrete red flags, assigns a risk level, and, when the risk is real, drafts a protective email proposing safer payment terms before you start work.

Built for **AI Factory — Native.builder Hackathon** (lablab.ai × NativelyAI), August 2026.

---

## The problem

Freelancers and small agencies routinely take on clients who turn out to be slow payers, non-payers, or difficult to work with — and there's rarely a fast way to check a client's reputation before committing time and effort. PayGuard gives freelancers a quick, structured way to sanity-check a new client using whatever information they already have.

## Who it's for

Freelancers, contractors, and small agencies (dev, design, writing, consulting) vetting a new client before signing on.

## How it works

1. **Enter a client name** and **describe what you know about them** — a warning from another freelancer, notes from a call, anything relevant.
2. A Supabase Edge Function sends this to an AI model (via **Groq**), which:
   - Extracts only concrete red flags actually present in the text (never invents risk that isn't there)
   - Assigns an overall risk level: **Low / Medium / High / Insufficient Data**
   - Gives 2–4 practical recommendations
   - If risk is Medium or High, **automatically drafts a protective email** proposing a deposit, milestone payments, or escrow
3. Results are shown immediately — no login, no data saved, fully stateless.

## Tech stack

- **[native.builder](https://nativebuilder.ai)** — application platform, used to generate the UI, wire the Supabase backend, and deploy the app
- **[Groq](https://groq.com)** — fast LLM inference for the risk-analysis step (`llama-3.3-70b-versatile`)
- **Supabase Edge Functions** — serverless backend that keeps API keys secure and off the client
- **React + TypeScript + Tailwind** — frontend, generated and refined via native.builder

## Why it's a real workflow, not just a static page

PayGuard isn't a single AI call bolted onto a form. It's a small automated pipeline:

**Input → AI reasoning (extract + score + decide) → conditional action (drafted email only when warranted) → structured output**

The email draft only appears when the risk level actually justifies it — the system makes a judgment call, not just a lookup.

## Local development

```bash
npm install
npm run dev
```

The Edge Function (`supabase/functions/analyze-voice`) requires a `GROQ_API_KEY` secret set in your Supabase project — get a free key at [console.groq.com](https://console.groq.com).

## Privacy

No client data, transcripts, or assessment history is stored anywhere. Each session is independent.

## Hackathon submission

- **Problem solved:** helping freelancers vet clients before taking on risky work
- **Target user:** freelancers, contractors, small agencies
- **Built primarily with:** native.builder, with Groq for AI reasoning
