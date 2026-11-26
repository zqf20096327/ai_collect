<p align="center"><img src="assets/icon.svg" width="64" height="64" alt=""></p>

<h1 align="center">Marketing Engineering</h1>

<p align="center">
  <img src="assets/header.png" alt="your agent votes. you just scroll. An agent terminal scans your setup and votes for the marketing tools you actually use." width="100%">
</p>

<p align="center">
  <em>one thumb doomscrolling. one hand clauding. campaign shipped somehow</em>
</p>

<p align="center">
  <a href="https://marketingengineering.dev"><img src="assets/badge.svg" height="20" alt="marketing engineering: ranked by use"></a>
  <img src="https://img.shields.io/badge/meetings-0-FF5A1F?style=flat-square&labelColor=181818" alt="Meetings: 0">
  <a href="llms.txt"><img src="https://img.shields.io/badge/llms.txt-ready-FF5A1F?style=flat-square&labelColor=181818" alt="llms.txt ready"></a>
</p>

<p align="center">
  <a href="#vote-with-your-usage"><b>Vote with your usage</b></a> ·
  <a href="https://marketingengineering.dev"><b>See the ranking</b></a> ·
  <a href="https://github.com/proxy-intell/marketing-engineering/releases"><b>Friday drops</b></a> ·
  <a href="#add-a-tool-by-hand"><b>Add a tool by hand</b></a>
</p>

> what other marketers are actually using. turns out it's not what twitter says…
>
> tools for running marketing like software: ads, SEO and AEO, organic social, analytics, email, billing and the AI agents that drive them

marketers opened a terminal. engineers got asked to "make it go viral". same person now. this is their toolbox

## vote with your usage

give this to your agent (Claude Code, Cursor, Codex, ChatGPT, any agent that can open a link). paste it as a message, not into a terminal:

```
check which marketing tools I have installed (MCP, CLI and skill names only) and give me a vote link - https://marketingengineering.dev/vote.md
```

it checks which of these tools you have installed and hands you a link. your agent sends nothing: you open the link, set how often you use each, and send. tools more people use climb. tools nobody uses sink. live ranking: [marketingengineering.dev](https://marketingengineering.dev)

only names of tools on this list and usage ratings leave your machine, and only when you press send. never code, paths, keys, prompts or anything not on the list. [how voting works](docs/how-voting-works.md)

want it permanent? run this in a terminal. it installs the skills for Claude Code, Cursor, Codex, Copilot and other agents: vote, find a tool for a job ("what should i use for X?"), and one per setup. [more ways](docs/install.md)

```
npx skills add proxy-intell/marketing-engineering
```

every entry says what it does and how you plug in: MCP server, API, CLI, SDK, plugin, skill or web app. skills and plugins for coding agents are listed too, with an install line. agents can skip the prose and read [`llms.txt`](llms.txt) or [`catalog.json`](catalog.json), remote MCP URLs included

new tools ship every friday as a [release](https://github.com/proxy-intell/marketing-engineering/releases) and an email. watch → custom → releases, or drop your email on [marketingengineering.dev](https://marketingengineering.dev)

## setups

one job, done end to end. ranked by how many voters have the whole thing

<!-- BEGIN SETUPS -->

### charge for your product

1. [Stripe](https://stripe.com): take the payment
2. [Autumn](https://useautumn.com): track credits and limits
3. [Resend](https://resend.com): send receipts and nudges
4. [PostHog](https://posthog.com): see who converts

paste into your agent:

```
set up "charge for your product" - https://marketingengineering.dev/setups/paid-product.md
```

### know what's working

1. [PostHog](https://posthog.com): who signed up and from where
2. [Google Search Console](https://search.google.com/search-console): which searches bring them
3. [Semrush](https://www.semrush.com): where competitors outrank you
4. [Claude Code](https://claude.com/claude-code): read all three every Friday

paste into your agent:

```
set up "know what's working" - https://marketingengineering.dev/setups/whats-working.md
```

### launch day

1. [Product Hunt](https://www.producthunt.com): post the launch
2. [Playwright](https://playwright.dev): take the screenshots
3. [Resend](https://resend.com): tell your list

paste into your agent:

```
set up "launch day" - https://marketingengineering.dev/setups/launch.md
```

### research competitors' ads

1. [Proxy](https://useproxy.dev): see the ads running now
2. [ScrapeCreators](https://scrapecreators.com): pull their organic posts
3. [Exa](https://exa.ai): find who else is in the market
4. [Gemini API](https://ai.google.dev): break down the video creative

paste into your agent:

```
set up "research competitors' ads" - https://marketingengineering.dev/setups/competitor-ads.md
```

### get cited in AI search

1. [Perplexity Sonar API](https://docs.perplexity.ai): see where you are cited today
2. [Semrush](https://www.semrush.com): see who gets cited instead of you
3. [Bing Webmaster Tools](https://www.bing.com/webmasters): check Bing has your pages
4. [IndexNow](https://www.indexnow.org): push new pages the day they ship
5. [Claude Code](https://claude.com/claude-code): run the check every week

paste into your agent:

```
set up "get cited in AI search" - https://marketingengineering.dev/setups/aeo.md
```

<!-- END SETUPS -->

<!-- BEGIN CATALOG -->

## Contents

- [AI search visibility (AEO)](#ai-search-visibility-aeo)
- [Attribution & product analytics](#attribution--product-analytics)
- [Billing, credits & paywalls](#billing-credits--paywalls)
- [Bing & AI-search indexing](#bing--ai-search-indexing)
- [Coding agents](#coding-agents)
- [Competitor & market research](#competitor--market-research)
- [Creative strategy](#creative-strategy)
- [Google SEO](#google-seo)
- [Launching](#launching)
- [Lifecycle comms](#lifecycle-comms)
- [Screenshots & browser automation](#screenshots--browser-automation)
- [TikTok, Instagram & YouTube data](#tiktok-instagram--youtube-data)

## AI search visibility (AEO)

- [Perplexity Sonar API](https://docs.perplexity.ai) - API for answers grounded in live web search, returned with source citations. · data
- [Semrush](https://www.semrush.com) - Tracks how a brand shows up in AI search answers, alongside keyword research, rank tracking and backlink data. · data

## Attribution & product analytics

- [PostHog](https://posthog.com) - Open-source product analytics: events, funnels, session replay, feature flags and experiments. Self-hostable or cloud. · data · used by 3

## Billing, credits & paywalls

- [Autumn](https://useautumn.com) - Billing layer on Stripe. Plans, credits and usage limits are defined in a config file; it tracks usage and keeps payments and webhooks in sync.
- [Stripe](https://stripe.com) - Payments API with Checkout, subscriptions, invoicing and a customer billing portal.

## Bing & AI-search indexing

- [IndexNow](https://www.indexnow.org) - Open protocol that pings participating search engines (Bing, Yandex, Naver, Seznam) when a URL is published or changes.
- [Bing Webmaster Tools](https://www.bing.com/webmasters) - Search queries, index coverage and backlink reports for your site in Bing, plus URL submission. · data

## Coding agents

- [Claude Code](https://claude.com/claude-code) - Anthropic's coding agent for the terminal, IDEs and web. Reads and edits a codebase, runs commands and connects to MCP servers. · used by 4

## Competitor & market research

- [Exa](https://exa.ai) - Web search API built for AI agents. Semantic search over the web, with page contents and structured results returned. · data

## Creative strategy

- [Proxy](https://useproxy.dev) - MCP server for the Meta, Google, LinkedIn and TikTok (EU) ad libraries, with video and image analysis of ads. · data · used by 3
- [Gemini API](https://ai.google.dev) - Google's model API. Accepts text, image, audio and video input, so it can transcribe and describe video ads.

## Google SEO

- [Google Search Console](https://search.google.com/search-console) - Reports on your site's clicks, impressions, queries and indexing status in Google Search, with URL inspection and indexing requests. · data

## Launching

- [Product Hunt](https://www.producthunt.com) - Site where new tech products launch daily and rank by upvotes. Also a searchable directory of past launches.

## Lifecycle comms

- [Resend](https://resend.com) - Email API for transactional and marketing email. React templates, contacts, broadcasts and webhooks.

## Screenshots & browser automation

- [Playwright](https://playwright.dev) - Browser automation library for Chromium, Firefox and WebKit. Drives pages, takes screenshots, runs end-to-end tests. Node, Python, Java and .NET.

## TikTok, Instagram & YouTube data

- [ScrapeCreators](https://scrapecreators.com) - Scraping API for public data from TikTok, Instagram, YouTube, Facebook, LinkedIn and X, including ad libraries. · data

<!-- END CATALOG -->

## add a tool by hand

1. **ask your agent to add one.** paste this into any agent with GitHub access

   ```
   Add <tool URL> to github.com/proxy-intell/marketing-engineering. Follow AGENTS.md and open a PR.
   ```

   or add a whole setup. tools we don't list yet get added along the way

   ```
   Add a "<job>" setup to github.com/proxy-intell/marketing-engineering using <tools>. Follow AGENTS.md and open a PR.
   ```

2. **open a PR yourself.** edit `catalog.json`, run `python scripts/build.py`. details in [CONTRIBUTING.md](CONTRIBUTING.md)

listed? put the badge in your README: [![Listed on Marketing Engineering](https://marketingengineering.dev/badge.svg)](https://github.com/proxy-intell/marketing-engineering) ([snippet](CONTRIBUTING.md#listed-add-the-badge))
