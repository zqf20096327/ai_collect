<img src="assets/banner.svg" alt="Motion Graphics Prompts: copy a prompt, paste it into your coding agent, get a finished product video" width="100%">

# Motion Graphics Prompts

**Make a polished product video without opening a video editor.**

No After Effects. No Premiere. No stock music. You paste one prompt into a coding agent inside your project folder. It reads your code, rebuilds your real screens, animates them, writes its own soundtrack and exports the video.

This repo is that prompt, plus 23 versions of it for different shapes, lengths, products and goals. Copy any of them. They are free to use.

If this saves you a week of work or a designer's invoice, a star helps other people find it.

## Contents

- [Quick start](#quick-start)
- [The master prompt](#the-master-prompt)
- [Pick your prompt](#pick-your-prompt)
- [Filled-in examples](#filled-in-examples)
- [After the first render](#after-the-first-render)
- [Why this works](#why-this-works)
- [Questions](#questions)
- [Contributing](#contributing)

## Quick start

1. Open your coding agent inside your project folder. These were written for and tested with [Claude Code](https://claude.com/claude-code). Other agents that can read files and run commands should work too.
2. Copy the master prompt below and replace everything in `[SQUARE BRACKETS]`.
3. Paste it, check the timing plan it shows you, and let it render.

You need Node.js installed. Everything else the agent sets up itself. The full guide is in [docs/how-to-use.md](docs/how-to-use.md).

## The master prompt

This one makes a product demo in both wide (16:9) and vertical (9:16) formats.

```text
You are my motion designer. Make a product demo video for [PRODUCT NAME], a [ONE LINE: what it is and who it's for].

You have access to this repo. Before designing anything, read it so the video shows the real product:
- the actual screens, in the order a real user meets them
- the exact words on those screens. Do not invent copy
- the brand: colours, fonts, logo, spacing. Use them everywhere

Imagine you are a [TYPE OF USER, e.g. new paid user]. Walk through the product as they would:
1. [FIRST THING THEY DO, e.g. sign up and see the welcome screen]
2. [FEATURE 2]
3. [FEATURE 3]
4. [FEATURE 4]
5. [FEATURE 5]
6. [THE RESULT OR PAYOFF THEY GET]

How to build it:
- Use Remotion (React), so every frame is code and it renders to MP4 with no extra installs.
- Before writing any animation, decide how many seconds each feature gets and show me the plan. Keep it fast. Nothing slow or boring.
- Rebuild the product's interface inside a device frame. Show real interaction: typing, taps with a visible touch, messages arriving, notifications sliding in.
- Build the layout so one timeline renders both a wide and a vertical version.
- Move the camera. Push in on what matters, pull back between steps.
- Put a short caption with each step: a number, a label, a headline, one supporting line. Large enough to read on a phone.
- Open on the logo and tagline. Close on the logo, what the product does in three words, and a call to action: [YOUR CTA AND LINK].
- Make the very first frame a finished cover image, because most apps use it as the thumbnail.

Sound:
- Write an original soundtrack in code so there is nothing to license. Pick a tempo and start every section on a bar, so cuts land on the beat.
- Add interface sounds: taps, typing, send, incoming message, notification. Time them from the same file that times the visuals, so they can never drift apart.

Quality:
- Render review frames of every scene and check them yourself before the final export. Fix anything cropped, overlapping or too small to read.
- Export 1920x1080 for desktop and 1080x1920 for Instagram and X, at high quality so it survives compression.
- Use example data for any numbers and tell me which ones are examples. Never show private data: no keys, no real users, no real accounts.

Use your best motion design judgement throughout. I'm attaching [A REFERENCE VIDEO / MY LOGO] to show the level of polish I want. Do not copy it.
```

## Pick your prompt

Every prompt below is complete. You can copy it on its own without reading the others.

### By shape

| Prompt | Size | Best for |
|---|---|---|
| [16:9 landscape](prompts/by-format/16x9.md) | 1920x1080 | YouTube, websites, X on desktop |
| [9:16 vertical](prompts/by-format/9x16.md) | 1080x1920 | Reels, TikTok, Shorts, X on mobile |
| [1:1 square](prompts/by-format/1x1.md) | 1080x1080 | LinkedIn, Instagram feed, X feed |
| [4:5 feed](prompts/by-format/4x5.md) | 1080x1350 | Instagram and Facebook feed |

### By length

| Prompt | Use it when |
|---|---|
| [15 second teaser](prompts/by-length/15s.md) | You have one impressive moment to show |
| [30 second cut](prompts/by-length/30s.md) | You need an ad slot or a quick announcement |
| [60 second video](prompts/by-length/60s.md) | You are launching and have five or six features |
| [90 second walkthrough](prompts/by-length/90s.md) | You want the full tour, in chapters |

### By product

| Prompt | For |
|---|---|
| [Web app or SaaS](prompts/by-product/web-app.md) | Anything that runs in a browser |
| [Mobile app](prompts/by-product/mobile-app.md) | iOS, Android, React Native, Flutter |
| [Chat bot](prompts/by-product/chat-bot.md) | Telegram, Discord, WhatsApp, Slack |
| [CLI or developer tool](prompts/by-product/cli-tool.md) | Anything that lives in a terminal |
| [API or SDK](prompts/by-product/api.md) | Request in, response out |
| [Online store](prompts/by-product/ecommerce.md) | Storefronts and carts |
| [Browser extension](prompts/by-product/browser-extension.md) | Chrome, Firefox, Safari |
| [No code access](prompts/by-product/no-repo.md) | Screenshots or a recording instead of a repo |

### By goal

| Prompt | What it makes |
|---|---|
| [Launch video](prompts/by-goal/launch-video.md) | The one you post on launch day |
| [Feature announcement](prompts/by-goal/feature-announcement.md) | One new feature, shown properly |
| [Paid social ad](prompts/by-goal/paid-ad.md) | A hook, proof, an offer, sound off |
| [Changelog video](prompts/by-goal/changelog.md) | What shipped this week or month |
| [Tutorial](prompts/by-goal/tutorial.md) | One task, step by step |
| [Investor teaser](prompts/by-goal/investor-teaser.md) | A short reel to send before the deck |
| [App store preview](prompts/by-goal/app-store-preview.md) | The video on your store listing |

### Extras

| File | What is in it |
|---|---|
| [Style blocks](prompts/styles.md) | Seven looks you can add to any prompt |
| [Follow-up prompts](prompts/follow-ups.md) | The feedback you will want to give after the first render |

Need a mix, such as a 15 second vertical ad for a chat bot? [How to combine prompts](docs/how-to-use.md#combining-prompts).

## Filled-in examples

Brackets are easier to fill in once you have seen it done. These use made-up products.

| Example | Mix |
|---|---|
| [Habit app ad](examples/habit-app-vertical-ad.md) | Mobile app, paid ad, 9:16, 15 seconds |
| [Telegram bot launch](examples/telegram-bot-launch.md) | Chat bot, launch video, both shapes, 60 seconds |
| [CLI walkthrough](examples/cli-tool-walkthrough.md) | CLI, demo, 16:9, 60 seconds |
| [SaaS feature announcement](examples/saas-feature-announcement.md) | Web app, one feature, both shapes, 30 seconds |

## After the first render

The first video is a draft. Give feedback the way you would to a designer:

```text
The smaller text is hard to read on a phone. Raise the minimum text size, increase the contrast, and re-check every scene so nothing overlaps or gets cropped.
```

```text
The cover image is not strong enough. Design a new first frame: the logo, one line that says what the product does, and one screen from the product. Change nothing else in the video.
```

More in [prompts/follow-ups.md](prompts/follow-ups.md). Each fix takes minutes.

## Why this works

Four lines in the prompt do most of the work.

- **It reads your repo first.** Every screen and every word in the video is real, because it comes from your code.
- **It plans the timing before animating.** You approve how long each part gets while changing it is still cheap.
- **One file times both picture and sound.** Cuts land on the beat and the tap sounds match the taps.
- **It checks its own frames before exporting.** Cropped text and overlapping captions get caught before you see them.

## Questions

**Does it cost anything?**
The prompts are free. You pay for whatever coding agent you use. Remotion, the tool that renders the video, is free for individuals and small teams and needs a paid licence for larger companies. [Check their licence](https://www.remotion.dev/docs/license).

**Do I need to know how to code?**
You need a project the agent can read, and Node.js installed. You do not need to write or read the video code yourself.

**Which agents does it work with?**
It was written for and tested with Claude Code. Nothing in the prompts is specific to it, so other coding agents that can read files and run commands should work. If you try one, open an issue and say how it went.

**I do not have a repo. Can I still use it?**
Yes. Use the [no code access](prompts/by-product/no-repo.md) prompt with screenshots or a screen recording.

**Will it show my private data?**
Every prompt tells the agent to use example data and never show keys, real users or real accounts. Watch the final video once before posting anyway.

**Can I use the videos commercially?**
The video is yours. The soundtrack is generated in code, so there is nothing to license. The Remotion licence above is the one thing to check.

## Contributing

Made a video with one of these? Wrote a version for a product type that is missing? Pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

[MIT](LICENSE). Use the prompts for anything, including client work.

Made by [@thegreatola](https://x.com/thegreatola).
