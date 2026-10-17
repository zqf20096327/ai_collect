<p align="center">
  <img src="assets/logo-wordmark.svg" width="560" alt="redditlens">
</p>

<p align="center"><strong>Find real pain points on Reddit. Draft replies that actually get upvoted.</strong></p>

A tiny CLI + [Claude Code](https://claude.com/claude-code) skill that turns Reddit into a market research engine. Ask five questions, get a pain-points report with draft replies you can post.

Built for founders, indie hackers, and marketers who want to find real customers instead of shouting into the void.

## What it does

1. You answer five questions about your product, audience, and tone.
2. `redditlens` searches Reddit via Google (Serper API) for pain language — not brand names.
3. It enriches every match via Reddit's public `.json` endpoint to pull scores and top comments.
4. Your agent clusters the pain points and drafts replies that lead with empathy and value.

No scraping tricks. No Reddit API keys. No database. One dependency (`undici`). MIT licensed.

## Install

```bash
npm install -g redditlens
```

Or run without installing:

```bash
npx redditlens search "notion alternatives" --period month --comments
```

## Requirements

- Node.js 18+
- A Serper API key (free, see below)

## Get a free Serper API key

Serper is a thin wrapper over Google search. The free plan gives you **2500 queries** with no credit card. More than enough to run redditlens for weeks.

1. Go to [serper.dev](https://serper.dev)
2. Sign up with Google or email
3. Copy your API key from the dashboard
4. Export it:

```bash
export SERPER_API_KEY=your_key_here
```

Add it to your shell profile (`~/.zshrc`, `~/.bashrc`) to persist it.

## Usage

### CLI

```bash
# Search for pain points in a niche
redditlens search "prompt engineering" --period month --limit 15 --comments

# Restrict to specific subreddits
redditlens search "notion alternatives" --subreddits productivity,ObsidianMD,PKMS --comments

# Fetch a single post deeply
redditlens post https://reddit.com/r/SaaS/comments/abc123/title/ --comments

# Discover relevant subreddits for a niche
redditlens subreddits "indie hacking"
```

All output is JSON on stdout. Pipe it to `jq`, into a file, or into another tool.

### As a Claude Code skill

Copy `SKILL.md` from this repo into `~/.claude/skills/redditlens/` and restart Claude Code. Then invoke:

```
/redditlens
```

Claude will ask you five questions, run the searches, cluster the pain points, and draft replies. No prompt engineering required on your side.

## Without proxies (polite mode)

By default, redditlens respects Reddit's public `.json` rate limit. It throttles to **1 request/second** with exponential backoff on 429 responses (2s, 4s, 8s, then fail).

This is fine for the target use case — one-shot market research. A typical pain-points search hits 15-30 posts, so expect 30-60 seconds per run.

**Do**: run redditlens when you actually want to do research.
**Don't**: fire off a dozen parallel searches or put it in a tight loop.

## With proxies (high volume)

If you need speed or high volume, provide a proxy list and redditlens will rotate per request (no throttle).

Create a `proxies.txt` file with one proxy per line:

```
1.2.3.4:8080:username:password
5.6.7.8:8080:username:password
9.10.11.12:8080
```

Both authenticated (`ip:port:user:pass`) and unauthenticated (`ip:port`) formats are supported.

Then:

```bash
export PROXIES_FILE=./proxies.txt
redditlens search "pain language" --limit 50 --comments
```

Any HTTP/HTTPS proxy provider works (residential recommended for Reddit — datacenter IPs get blocked fast).

## Use cases

### 1. Validating a product idea

You think founders hate their current invoicing tool. Before you build anything:

```bash
redditlens search "hate invoicing" --subreddits SaaS,Entrepreneur,indiehackers --period month --comments
redditlens search "invoicing alternatives" --period month --comments
```

Read the clusters. If three different pain points keep surfacing, you have a signal. If it's just one loud complainer, you don't.

### 2. Finding customers (the respectful way)

You already built the tool. You want to find threads where you can genuinely help:

```
/redditlens
> What are you researching? My product, a lightweight invoicing tool for freelancers
> Who is your target user? Solo freelancers and contractors
> Subreddits? discover
> Time window? week
> Reply tone? casual, helpful
```

Claude will give you 3-5 threads with draft replies. Review them, post the ones that fit, skip the ones that don't.

### 3. Agent research loop

Let an agent run redditlens as part of a larger research pipeline:

```bash
SERPER_API_KEY=xxx redditlens search "<topic>" --comments | jq '.posts[] | {title, url, score}'
```

JSON output means any agent or script can parse it. Claude, GPT, OpenAI Responses, whatever.

## How it works

```
User question
    │
    ▼
SKILL.md asks 5 questions
    │
    ▼
redditlens search "<pain phrase>"
    │
    ▼
Serper (Google) → Reddit post URLs
    │
    ▼
Reddit .json endpoint → score, comments, body
    │              (throttled or proxy-rotated)
    ▼
JSON to stdout
    │
    ▼
Agent clusters pain points, drafts replies
```

The key insight: Reddit's `.json` endpoint is public and free. No API key, no OAuth. You just need Google search to find the right threads, and you need to not hammer the endpoint.

## CLI reference

```
redditlens search "<query>" [options]
redditlens post <reddit-url> [--comments]
redditlens subreddits "<niche>"
```

### Search options

| Flag             | Description                                      | Default  |
|------------------|--------------------------------------------------|----------|
| `--subreddits`   | Comma-separated subreddit list                   | (all)    |
| `--period`       | Time window: `day`, `week`, `month`, `year`      | `week`   |
| `--limit`        | Max results                                      | `20`     |
| `--comments`     | Include top comments                             | off      |

### Environment

| Variable          | Required | Description                                        |
|-------------------|----------|----------------------------------------------------|
| `SERPER_API_KEY`  | Yes      | Free at [serper.dev](https://serper.dev)           |
| `PROXIES_FILE`    | No       | Path to proxy list for high-volume mode            |
| `REDDITLENS_DEBUG`| No       | Print proxy mode info on startup                   |

## FAQ

**Does this violate Reddit's ToS?**
redditlens uses Reddit's public `.json` endpoint, which is the same data Reddit serves to logged-out web visitors. Respect the rate limit (the CLI enforces it by default) and you're fine. Don't scrape at scale without proper authentication.

**Why Serper and not the Reddit search API?**
Reddit's native search is mediocre and rate-limited. Google finds Reddit threads better than Reddit does. Serper is the cheapest Google search API.

**Why not use an LLM to find pain points directly?**
redditlens *does* use an LLM — the Claude Code skill clusters pain points and drafts replies. But the LLM operates on real Reddit data, not vibes. Grounding matters.

**Can I use this with a different agent / framework?**
Yes. The CLI outputs JSON. Pipe it wherever. The skill is for Claude Code, but the CLI is standalone.

**What about LinkedIn / Twitter / HN?**
Out of scope for redditlens. If you want multi-platform monitoring, that's a different tool. redditlens is deliberately narrow.

## Contributing

PRs welcome. Keep it tiny — the whole point is that this stays a single-purpose tool you can read in one sitting.

## License

MIT. Do whatever you want with it.
