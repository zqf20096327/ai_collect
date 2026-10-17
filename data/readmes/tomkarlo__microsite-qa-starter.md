# Micro-site Q&A starter

A one-page site that answers questions about a fixed set of documents, and nothing else.
Retrieval runs server-side over documents you supply, Claude answers from what retrieval finds,
and the answer streams back. Visitors need no account, and the API key never reaches the browser.

Built for a local council consultation, where neighbours needed to understand a 91-page feasibility
study before a deadline. It suits anything with a similar shape: a planning application, a school
admissions policy, an HOA rulebook, a set of race regulations — a bounded set of documents that
people need answers from and won't read in full.

**What it is:** one static page plus three small serverless functions, deployed free on Vercel.
No database, no build step, no framework. You supply the documents.

**What it isn't:** a general chatbot, or a RAG system for a large corpus. Retrieval is keyword-based
and tuned for tens of documents, not thousands. See *Notes on the machinery* below.

**Designed to be honest about its limits.** It answers only from the supplied material, says so
when the documents don't cover something, and the prompt is written to explain rather than
persuade — which matters when the subject is contested and you want to be trusted by people who
disagree with you.

## Costs

You pay Anthropic per question, roughly 1.25 cents on Sonnet. Everything else fits in free tiers.
There are three independent caps — per-IP, per-day site-wide, and a spend limit on the key itself —
because a public page with a metered backend behind it is a bill waiting to happen. Read
*What a question costs* before you share a link.

## What's here

```
public/index.html   the page — markup, palette, streaming client, all of it
api/ask.js          answers a question (rate limit → retrieval → Claude → SSE stream)
api/search.js       plain keyword search over the documents, no model call, free
lib/retrieve.js     retrieval, the KEY_FACTS block, and the system prompt
lib/limits.js       per-IP rate limiting and a daily question cap
data/corpus.js      the documents, extracted and chunked
```

## Building a new site

In rough order of how much each one matters.

**1. `data/corpus.js` — the documents.** `pdftotext -layout` each source, split into chunks of
roughly 1,500–1,800 characters, break on headings rather than mid-sentence, and emit
`{s: source, h: heading, t: text}`. Retrieval quality depends far more on sensible chunk
boundaries than on chunk count: a chunk should be able to answer a question on its own.

**2. `lib/retrieve.js` — `KEY_FACTS`.** The handful of facts that must be right in every answer,
sent with every question regardless of what retrieval finds. Retrieval can miss; this can't.
Keep it to ten or so lines — it competes with the extracts for attention.

**3. `lib/retrieve.js` — `SYSTEM`.** Replace the `<SUBJECT>`, `<AUDIENCE>` and
`<FALLBACK CONTACT>` placeholders. The length rules are tuned: a hard word limit plus explicit
permission not to be complete is what keeps answers short and stops them truncating.

**4. `lib/retrieve.js` — `AUTHORITY`.** Names must match `s` in your corpus. This mildly boosts
documents that are authoritative on process, so "when is the deadline" isn't answered from a
technical annexe. Keep the boosts small.

**5. `public/index.html` — the `CONFIG` block** near the top of the script holds the deadline and
the CTA link. Then the copy: title, meta description, header, the two optional cards, the
`SUGGESTIONS` chips, the invite block and the footer. Everything to change is marked.

**6. `RATE_LIMIT_PREFIX`.** Set this per site. Two sites sharing one Upstash database with the
same prefix would share each other's rate limits.

## Deploy

```bash
npm i -g vercel
vercel                                        # links the project, deploys a preview
vercel env add ANTHROPIC_API_KEY production   # paste the key; never commit it
vercel --prod
```

Get the key at console.anthropic.com → API Keys. **Set a monthly spend limit on it while you're
there.** That is the only cap that survives a bug in this code.

## Before sharing the link

**Add Upstash Redis.** `vercel integration add upstash/upstash-kv`, free tier. Without a shared
store the limiter only counts within a single serverless instance, which a determined visitor
walks straight past.

Note the Vercel integration injects `KV_REST_API_URL` / `KV_REST_API_TOKEN`, not
`UPSTASH_REDIS_REST_*`. `lib/limits.js` accepts either — but check which store is actually live,
because the fallback is silent:

```bash
curl -sD - -o /dev/null -X POST https://YOUR-SITE/api/ask \
  -H 'Content-Type: application/json' -d '{"question":"test"}' | grep -i x-rate-store
```

`redis` is good. `memory` means the limits are per-instance and leaky.

**Check the Hobby plan fits.** Vercel restricts Hobby to non-commercial personal use.

## Pausing when there is nothing live

Useful for anything that runs in bursts — a consultation, a planning application, an election, an
enrolment window. The page keeps saying what it was for, without answering questions or spending
money.

`SITE_MODE` controls it, and is the single source of truth: `api/status.js` reads it, the page asks
`/api/status` on load, so the markup and the API cannot drift apart.

| `SITE_MODE` | Behaviour |
| --- | --- |
| unset or `live` | Normal. Anything unrecognised also means live, so a typo cannot silently take the site down. |
| `paused` | `/api/ask` returns 503 before reaching the model, so the site cannot spend anything — including when called directly, bypassing the page. The page hides everything marked `live-only` (question box, deadline, document search, CTA) and shows `.paused-note` instead. The heading, context cards and footer stay, so a visitor can see they reached the right place. |

```bash
printf 'paused' | vercel env add SITE_MODE production --type config
vercel --prod                                    # env changes need a redeploy to take effect
```

Set `PAUSED_MESSAGE` to control what the API returns while paused. Edit the `.paused-note` block in
`public/index.html` to say what the page covered and when it ended.

**To go live again:** `vercel env rm SITE_MODE production --yes`, update the corpus, `KEY_FACTS`
and page copy, redeploy, then check `/api/status` returns `{"mode":"live"}` and ask a real question.

Add `live-only` to any element that should disappear while paused. `/api/search` stays reachable
but unlinked; gate it the same way as `/api/ask` if you want it off too.

## Settings

All optional, set in Vercel → Settings → Environment Variables. Defaults in brackets.

| Variable | What it does |
| --- | --- |
| `CLAUDE_MODEL` | [`claude-sonnet-5`] `claude-haiku-4-5-20251001` is half the price and blunter. |
| `MAX_TOKENS` | [600] Ceiling on answer length, and on cost per question. Leave headroom above your target length so answers finish rather than truncate. |
| `PER_IP_PER_MINUTE` | [5] |
| `PER_IP_PER_DAY` | [40] |
| `DAILY_QUESTION_CAP` | [1500] Site-wide. Search keeps working after this trips. |
| `RATE_LIMIT_PREFIX` | [`site`] Namespaces the counters. Set per site. |
| `CAP_CONTACT_MESSAGE` | Appended when the daily cap trips. Point it somewhere useful. |
| `SITE_MODE` | [`live`] Set to `paused` to switch the Q&A off without taking the page down. |
| `PAUSED_MESSAGE` | What the API returns while paused. |

## What a question costs

Retrieval sends roughly 18,000 characters of extracts, about 5,000 tokens, plus the answer. On
Sonnet at $2/$10 per million tokens, a 250-token answer is about 1.25 cents — roughly $13 per
thousand questions. Multiply your daily cap by that to get your worst case, and check it against
the spend limit on the key. Current rates: https://platform.claude.com/docs/en/about-claude/pricing

## Notes on the machinery

**Retrieval is keyword-based**, not semantic — no embeddings, no vector database. Cheap,
dependency-light and fast, but it can miss a passage phrased differently from the question.
`KEY_FACTS` is the safety net. If your corpus is large or the questions are open-ended, this is
the first thing you'd replace.

**Theming** is CSS custom properties on `:root`, redefined for dark mode. The page pins itself to
light when it detects it's in an iframe, because a dark iframe inside a light host page reads as
broken. Check contrast if you change the palette — a brand colour that passes on a website often
fails as text on a light background.

**Answers render as light markdown.** Everything is escaped first, then bold, italics, lists and
links are added, so nothing from the model can inject HTML.

## Embedding

```html
<iframe src="https://YOUR-SITE/" style="width:100%;height:1400px;border:0"
        title="Descriptive title" loading="lazy"></iframe>
```

Serving the page from the same origin as the API is what keeps this simple — no CORS to configure.

## Licence

MIT — see [LICENSE](LICENSE). Use it, change it, deploy it, sell it; just keep the copyright notice.

No warranty, and that is not boilerplate here: this puts a language model in front of the public
over documents that may be contested. Check what it says before you share the link, keep a spend
limit on your API key, and tell readers plainly that answers are generated and can be wrong.
