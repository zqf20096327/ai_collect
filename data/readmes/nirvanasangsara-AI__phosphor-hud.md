<h1 align="center">Φ Phosphor</h1>

<p align="center">
  <b>Every AI coding plan you pay for, in one always-on-top HUD — and exactly when you'll hit the limit.</b><br>
  Native SwiftUI for macOS. Claude Code, Codex, Google AI, Grok, Copilot and 30+ more. No cookies scraped, ever.
</p>

<p align="center">
  <img src="docs/assets/menubar.png" width="140" alt="Phosphor menu bar item showing Φ 74% live usage in the macOS menu bar"><br>
  <sub>Menu bar indicator (<code>Φ 74%</code>) — click to toggle the floating HUD, or keep it always on top.</sub>
</p>

<p align="center">
  <img src="docs/assets/hero.gif" width="420" alt="Live Phosphor HUD in English: Claude Code, Codex, Google AI, Grok, Copilot, Elite glow, weekly sparklines, and burn-rate / depletion lines">
</p>

<p align="center">
  <a href="#install">Install</a> · <a href="#features">Features</a> · <a href="#privacy">Privacy</a> · <a href="docs/GUIDE.md">Full guide</a> · <a href="#한국어">한국어</a>
</p>

---

## Why

You're on Claude Max, ChatGPT Pro, Google AI and a couple more. Each one hides its limits on a different
settings page, with a different reset clock. Phosphor puts all of them in one small floating panel, works
out your burn rate, and tells you **`▲ limit 15:20 · in 1h 21m`** before you hit the wall, not after.

## Features

- **30+ providers, auto-detected.** Claude Code, Codex / ChatGPT, Antigravity, Gemini CLI, Grok CLI, GitHub Copilot,
  Muse Code, Cursor, Windsurf, Cline, Roo Code, Aider, Kiro, Warp, Amp, OpenRouter, Ollama, LM Studio, OpenAI and
  Anthropic API spend, and more. Phosphor finds installed CLIs, apps and logs and turns the right rows on. Toggle any of them.
- **Burn rate and run-out time on every quota bar.** Two recent samples are enough to fit a slope (last hour for 5-hour windows, last 6 hours for weekly ones).
  You get `+3.2%/h` and the time you'll hit 100 % (in the warning colour if that comes before the reset), or `≈ 83% at reset` if you'll make it. When a slope can't be fitted yet the line stays up as `measuring pace`, `steady · 0%/h`, `▲ limit reached`, or `no active session`.
- **Always on top, natively.** A SwiftUI panel with no web runtime that floats over every Space. Compact mode, opacity, click-through, and a `Φ 94%` menu bar item.
- **Language.** English by default, with in-app language switching (English, Korean, or follow your macOS system language) covering menus, settings, and burn-rate / depletion descriptions.
- **Subscription ROI.** Local Claude Code / Codex / Gemini CLI logs are priced at API list rates (LiteLLM's public table) and set against what your plans cost: `ROI 8.4x`.
  A 14-day stacked chart shows tokens or dollars per tool.
- **GitHub PR efficiency.** Merged PRs and commits for today / 7D / 30D through your existing `gh` login (read-only), plus cost per PR, tokens per PR and velocity.
  A tier badge places your merged-PRs-per-week within the published [LinearB 2026 benchmark](https://linearb.io/resources/engineering-benchmarks) bands.
  There's no fake global leaderboard.
- **Google AI, grouped.** Antigravity, Gemini CLI, Gemini app, Gemini API, Google AI credits and Vertex AI are separate meters at Google.
  Phosphor shows each one under one collapsible *Google AI* header and counts the subscription once.
- **Drag to reorder.** Grab the grip that appears on hover. The order persists, and *Reset Order* is in the menu.
- **Plans, prices, next bill, reset credits.** Hover a row for its plan card. There's also a monthly total across every plan.
  Stale readings are dimmed, and you get alerts at 70 % / 90 %, on reset, a day before billing, and 3 days before credits expire.
- **Service status dots** from each provider's public status page, **multiple accounts** per provider, and a calendar export of upcoming bills.
- **Themes are JSON.** Clean, Retro CRT, Matrix, Glasses HUD, and *Raid Frames* (quota as HP, with a revive animation on reset).
  You can write your own in a few lines.

<p align="center">
  <img src="docs/assets/chart.png" width="360" alt="Phosphor with the 14-day API-equivalent cost chart (demo data)">
  &nbsp;
  <img src="docs/screenshots/themes.gif" width="300" alt="Phosphor cycling through its themes">
</p>

<sub>The hero GIF is a live HUD recording (English). The chart and theme shots below use the built-in demo data (`Phosphor --demo`).</sub>

## Install

```bash
git clone https://github.com/nirvanasangsara-AI/phosphor-hud.git
cd phosphor-hud && ./scripts/build-app.sh --run
```

macOS 14+ and the Xcode Command Line Tools. To try it without logging in to anything, run
`dist/Phosphor.app/Contents/MacOS/Phosphor --demo`.

Prebuilt zips will be attached to Releases. They aren't notarized yet, so the first time you open the app, use right-click → **Open**.
A Homebrew cask template is in [`packaging/homebrew`](packaging/homebrew/phosphor.rb).

## Privacy

- **No cookie or session scraping, no browser automation, no password prompts.** Phosphor reads only what the official tools already keep for you:
  the CLI's own OAuth token (Claude Code, Codex, Copilot via `gh`), an app's own local usage cache, or a provider's documented API with your key.
- **Never prints or stores tokens.** Credentials stay in the Keychain or the tool's own config. Phosphor only reads them, in memory.
- **Local logs are read for numbers only.** Token counts and model names, never prompts or replies. Everything stays on your Mac,
  in `~/Library/Application Support/Phosphor`.
- **The only network calls** go to the providers' usage endpoints, their public status pages, LiteLLM's public price table,
  a public FX rate (for ROI), GitHub search through your `gh` login, and provider icons if you choose to download them. No analytics, no telemetry.
- **No guessed numbers.** If a value can't be read, the row says why instead of making one up.

## Documentation

[docs/GUIDE.md](docs/GUIDE.md) covers every provider and how it's read, custom providers, themes, files, notifications,
extra accounts and building. Themes: [docs/THEMES.md](docs/THEMES.md). Releasing: [docs/RELEASE.md](docs/RELEASE.md).

```bash
swift test                    # PhosphorCore unit tests
./scripts/hero.sh             # regenerate README images from demo data
./scripts/screenshots.sh      # theme screenshots + GIF
```

## 한국어

**Phosphor**는 맥 화면 위에 항상 떠 있는 AI 구독 사용량 HUD입니다.

- Claude Code, Codex, Google AI(Antigravity·Gemini), Grok, Copilot 등 30개 이상의 서비스를 자동으로 찾아 한도 %와 리셋 시각을 한눈에 보여 줍니다.
- 최근 사용 속도로 **언제 한도에 닿는지**(`▲ limit 15:20 · in 1h 21m`)를 미리 알려 줍니다.
- 기본 언어는 영어이며, 앱에서 영어 / 한국어 / macOS 시스템 언어를 고를 수 있습니다. 메뉴, 설정, 소진율·예상 소진 안내가 선택한 언어로 바뀝니다.
- 로컬 로그를 API 정가로 환산해 **구독 ROI**를 계산하고, `gh` 로그인으로 **GitHub PR·커밋 효율**을 보여 줍니다. 등급 배지는 LinearB 2026 공개 벤치마크 기준입니다.
- 쿠키·세션 스크래핑은 하지 않습니다. 각 공식 도구가 이미 저장해 둔 값만 읽고, 토큰은 출력하거나 저장하지 않습니다.

## License

MIT. Not affiliated with Anthropic, OpenAI, Google, xAI, GitHub, LinearB or any provider listed.

---

*For my beloved wife, daughter, and son. ♥*  
*사랑하는 아내와 딸, 아들에게 바칩니다. ♥*
