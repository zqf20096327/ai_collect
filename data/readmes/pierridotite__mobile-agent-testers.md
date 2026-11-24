# mobile-agent-testers

<a href="https://www.producthunt.com/posts/mobile-agent-testers?utm_source=badge-featured&amp;utm_medium=badge&amp;utm_campaign=mobile-agent-testers"><picture><source media="(prefers-color-scheme: dark)" srcset="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=1326513&amp;theme=dark"><img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=1326513&amp;theme=light" alt="Mobile Agent Testers on Product Hunt" width="250" height="54"></picture></a>
<a href="https://www.linkedin.com/in/pierre-raffalli/"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/linkedin-follow-dark.svg"><img src="assets/linkedin-follow-light.svg" alt="Follow Pierre Raffalli on LinkedIn" width="160" height="54"></picture></a>

**Launching on [Product Hunt](https://www.producthunt.com/posts/mobile-agent-testers?utm_source=github&utm_medium=readme&utm_campaign=launch-day) today.** If it saves you time, your feedback and support on the launch page help a lot.

**20 AI testers on 20 different phones, in parallel, on GitHub's free runners.**

**[Examples](docs/examples.md)** · **[Compare](docs/compare.md)** · **[FAQ](docs/faq.md)** · **[Personas](personas.json)** · **[Contributing](CONTRIBUTING.md)** · **[Releases](https://github.com/pierridotite/mobile-agent-testers/releases)**

English · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Português](README.pt-BR.md)

No test scripts to write. Each tester is a Claude Code agent with its own iOS
Simulator or Android emulator on GitHub Actions. It plays a persona (iPhone SE
in Swedish at the largest text size, Pixel 7 at 200%, iPad in German, Arabic
right to left...), uses your app like a new user (or runs through the feature you
point it at) and writes a bug report with screenshots. Flutter, React Native, Expo, native Kotlin and Swift, Kotlin
Multiplatform, Capacitor and .NET MAUI.

GitHub's runners are free for public repos. You only pay for the model, with your
Claude subscription or API key: about $0.15 to $0.55 per phone in [these runs](docs/runs/).

<p align="center"><a href="assets/localsend-20.mp4"><img src="assets/localsend-20.gif" alt="Real screen recordings of 20 AI testers using LocalSend at the same time: 10 Android emulators and 10 iOS Simulators in 14 languages, from a small Pixel to a 13-inch iPad. When a tester finishes, its phone shows how many issues it found. Opens the video." width="100%"></a><br>
<sub>Real screen recordings of the LocalSend run, idle time cut. <a href="assets/localsend-20.mp4">Full video (MP4)</a> · <a href="docs/runs/localsend-20.md">The run, device by device</a></sub></p>

[![Tests](https://github.com/pierridotite/mobile-agent-testers/actions/workflows/tests.yml/badge.svg)](https://github.com/pierridotite/mobile-agent-testers/actions/workflows/tests.yml)
[![Stars](https://img.shields.io/github/stars/pierridotite/mobile-agent-testers?style=flat)](https://github.com/pierridotite/mobile-agent-testers/stargazers)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
![iOS + Android](https://img.shields.io/badge/platforms-iOS%20%2B%20Android-blue)
![Claude Code plugin](https://img.shields.io/badge/Claude%20Code-plugin-orange)
[![Last commit](https://img.shields.io/github/last-commit/pierridotite/mobile-agent-testers)](https://github.com/pierridotite/mobile-agent-testers/commits/main)

## What it does

One use per run, set with the inputs of [Test your own app](#test-your-own-app).

- **Explore like new users** (the default). Each persona tries to reach its goal and reports what gets in the way, with numbered screenshots.
- **Run one feature end to end.** Your own brief sends every agent through a whole mechanic: a booking in several steps, an editor with undo, a sync between two screens. Agents tap, long press, swipe and type, leave the app and come back, relaunch it to check what was saved, or open a deep link to start right at the feature, and a brief can raise the budget of about 30 actions. [AnkiDroid's](briefs/ankidroid.md) found the Back field of a new card hidden behind the keyboard.
- **Reproduce a bug report** on every phone: give an issue or the steps, and each agent answers yes, no or unclear, with screenshots ([briefs/reproduce.md](briefs/reproduce.md)).
- **Get an improvement report.** Each persona uses the app once, then says where it hesitated, what it expected and what to change first, by area and impact ([briefs/improve.md](briefs/improve.md)).
- **Compare two versions.** The same personas on two branches or builds, then one table: goals reached, actions, scores, issues seen on one version only ([docs/compare-versions.md](docs/compare-versions.md)). A check before a real A/B test, not a replacement for one.
- **Use a cheaper model**: Claude Haiku, or any Anthropic-compatible API (OpenRouter, DeepSeek, Kimi, GLM, MiniMax, Qwen). The findings are only as good as the model's reading of screenshots and its reasoning ([docs/cheaper-models.md](docs/cheaper-models.md)).

Maestro or Appium run the tests you write. These agents look for what nobody thought to test: [how it compares](docs/compare.md).

## Applied examples

Real runs on open-source apps, with nothing planted.

| App | Phones | What the agents found | Time, model usage |
|---|---|---|---|
| [LocalSend](https://github.com/localsend/localsend) (Flutter, 100k stars) | 20: 10 Android, 10 iOS, 14 languages | 46 distinct bugs, 1 blocker: on an iPhone SE in Swedish at the largest text size, you can't send a text message at all | 69 min, $4.62 |
| [AnkiDroid](https://github.com/ankidroid/Anki-Android) (Kotlin, 12k stars, release APK) | 10 Android | 43 distinct issues, among them answer buttons cut in half at 200% font and "Get started" left in English in three languages | under 10 min, $4.69 |
| [Flutter's animations sample](https://github.com/flutter/packages/tree/main/packages/animations/example) | 1 Android, 1 iOS | The same typo, reported by both agents on their own, and an app that ignores dark mode | 19 min, $0.47 |

34 of LocalSend's 46 bugs had nothing to do with text size or accessibility: broken flows, silent failures, missing translations, tablet layouts. Screenshots, every finding and the commands to run them again: [docs/examples.md](docs/examples.md).

## Quick start

```bash
gh repo create my-testers --public --template pierridotite/mobile-agent-testers --clone
cd my-testers && ./setup.sh           # key pair + secrets + Claude token (Windows: .\setup.ps1)
gh workflow run agent-testers.yml     # demo: 2 Android + 2 iOS testers, ~20 min
bash scripts/collect.sh <run id>      # decrypts reports, groups duplicates: runs/<id>/SUMMARY.md
```

The demo app has [11 deliberate bugs](demo-app/BUGS.md). In [one run](docs/runs/), the 4 demo testers found 9 of them (2 to 7 minutes per agent, about 21 minutes for the whole run, builds included), plus real issues nobody planted (a button under the Android nav bar, no data kept after a relaunch). Model usage: $0.87 for the 4.

Or let Claude set it up for your app:

```
/plugin marketplace add pierridotite/mobile-agent-testers
/plugin install mobile-agent-testers@mobile-agent-testers
```

## Test your own app

```bash
gh workflow run agent-testers.yml -f source_repo=you/app -f app_id=com.you.app \
  -f android_personas=anna,malik -f ios_personas=clara,jonas
```

Every input (builds, briefs, bug reports, cheaper models, build arguments, video) and the supported frameworks: [docs/configuration.md](docs/configuration.md).

## Contributing

Ideas where help is welcome. Open an issue first to say which one you take, so two people don't build the same thing. [CONTRIBUTING.md](CONTRIBUTING.md) says where each one starts and how to test it offline.

- **Other agent CLIs**: OpenCode, Codex CLI, Gemini CLI, Goose. The tools are plain scripts and the mission is a Markdown brief, so the agent is one command per platform.
- **Web apps**: the same personas on a mobile browser with Playwright, for PWAs and mobile sites.
- **Physical Android phones** over adb, on a self-hosted runner.
- **New personas**: increased contrast, reduced motion, color blindness filters, a slow or flaky network.
- **Findings to issues**: turn the summary into draft GitHub issues with their screenshots, or a Slack or Discord message.
- **Other CI**: GitLab CI, Bitrise, Codemagic.
- **More build systems**: NativeScript, Unity, Godot, each one case in `scripts/build/`.
- **Translations** of the README and docs.
- **Model comparison**: the demo app's 11 planted bugs make a small benchmark. A table of what each model finds and costs.

## Hosted version for teams (exploring)

The workflow here stays free, open source and complete. I'm exploring a hosted version for teams with private apps: macOS runners included (on a private repo, GitHub counts each macOS minute ten times) and a web dashboard to share the reports with the whole team, product managers included.

Would that help your team? [Answer three questions](https://github.com/pierridotite/mobile-agent-testers/issues/new?template=teams.yml) or [write to me on LinkedIn](https://www.linkedin.com/in/pierre-raffalli/). Already ran it on your app? [Tell me what it found and what got in the way](https://github.com/pierridotite/mobile-agent-testers/issues/new?template=usage-feedback.yml).

## Star history

[![Star History Chart](https://api.star-history.com/svg?repos=pierridotite/mobile-agent-testers&type=Date)](https://star-history.com/#pierridotite/mobile-agent-testers&Date)

## Credits

[Claude Code](https://docs.claude.com/en/docs/claude-code) ·
[AXe](https://github.com/cameroncooke/axe) ·
[android-emulator-runner](https://github.com/ReactiveCircus/android-emulator-runner)

Made by [@pierridotite](https://github.com/pierridotite) ([LinkedIn](https://www.linkedin.com/in/pierre-raffalli/)) · MIT license
