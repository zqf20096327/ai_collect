# xhs-trending-cards

Generate XiaoHongShu / social media ranking cards from structured list data.

This skill creates polished card sets for GitHub Trending, AI tools, NPM packages,
knowledge cards, launch posters, and developer/project rankings. It supports
HTML preview, one-click PNG export, and publish-ready copywriting.

## Styles

The canonical style registry is `assets/styles.json`.

| ID | Name | Size | Template | Best for |
| --- | --- | --- | --- | --- |
| A | Dark Tech | 1242x1660 | `card_template.html` | GitHub Trending, AI tools, technical rankings |
| B | Apple Minimal | 1242x1660 | `style_b_apple.html` | product launches, major announcements |
| C | White Editorial | 1242x1660 | `card_template.html` + `style-white` | tutorials, comparisons, editorial posts |
| D | Pastel Card | 1242x1660 | `card_template.html` + `style-pastel` | lifestyle, warm topics, light science |
| E | Magazine | 1242x1660 | `card_template.html` + `style-mag` | long-form analysis, industry reports |
| F | Dark Cinematic | 1242x1660 | `card_template.html` + `style-cinematic` | dramatic reveals, frontier tech |
| G | macOS Skill Card | 1080x1440 | `style_g_macos_skill.html` | developer picks, project reviews, scoring |
| H | Compact macOS Card | 420px wide | `style_h_compact_macos.html` | web embeds, small sharing cards |

## One-command style preview

Generate one preview card for every style plus a combined overview:

```bash
node scripts/preview_all_styles.js
```

Optional output folder:

```bash
node scripts/preview_all_styles.js ./tmp/style-previews
```

The script writes:

- `all_styles_preview.html`
- `all_styles_overview.png`
- `style-a.png` through `style-h.png`

The PNG export uses Playwright. If the browser runtime is missing, run:

```bash
npx playwright install chromium
```

## Input data shape

Use an array of objects. Keep values short enough for a vertical social card.

```json
[
  {
    "name": "Project Name",
    "desc": "One-line description",
    "stars": "351K",
    "url": "github.com/org/repo",
    "tags": ["TypeScript", "AI"],
    "rank": 1
  }
]
```

For Style G/H scoring cards, include evidence-backed scores:

```json
{
  "scores": {
    "starGrowth": 92,
    "heat": 88,
    "innovation": 90,
    "monetization": 82,
    "influence": 95
  },
  "scoreEvidence": [
    "7-day stars grew by 860",
    "Clear developer-tool monetization path"
  ]
}
```

## Workflow

1. Collect or parse the ranking data.
2. Choose a style from `assets/styles.json`.
3. Render a cover card and detail cards using the matching template.
4. Preview in browser.
5. Export PNGs with html2canvas or Playwright.
6. Ask whether the user wants matching copywriting.

## Copywriting follow-up

After card generation, ask the user:

> 卡片已经生成完毕，需要我帮你写一版配套文案吗？
> A. 小红书文案（标题选项 + 正文 + 20 个标签）
> B. 微头条文案（严格 150 个中文字符）
> C. 不需要

If the user chooses B, count the characters before delivering.

## Maintenance notes

- Keep `assets/styles.json` as the source of truth for style metadata.
- Add new style templates under `assets/`.
- Update `scripts/preview_all_styles.js` whenever a new style is added.
- Prefer Playwright `element.screenshot()` or the preview script for QA.
- Check PNG file size and visible output after export to catch blank renders.
