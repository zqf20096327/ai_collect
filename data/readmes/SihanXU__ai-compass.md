# AI Research Compass · AI 研究立场图谱

A political compass for AI research. Is intelligence built on **language** or on the **world**? Does it live in one end-to-end **monolith**, or in a **harness** of tools, memory and agents? The mainstream recipe or a paradigm shift?

**Site:** https://sihanxu.me/ai-compass/

- **Chart** — 165 ideologies on a 13 × 12 grid with a ring of extreme titles, shaded by paradigm, like the big ideology charts of the political compass world.
- **Tests** — a quick test (10 statements, 9 camps), a full test (50 statements, 5 axes, your exact cell, titles at the extremes), and a pro test (120 statements scored on 13 sub-dimensions, then up to 8 adaptive follow-ups that tell your nearest cells apart, plus a consistency score). Results are shareable links and images.
- **Wiki** — an entry for every ideology in English and Chinese: beliefs, arguments, critiques, representative works, and friends / frenemies / enemies.

给 AI 研究做一张政治图谱：图谱、三套测试（简单版、完整版、专业版）、每个主义的中英文百科词条。

## Run it

```sh
npm install
npm run dev        # http://localhost:4321/ai-compass/
npm run validate   # check every data file
npm run build      # validate, then build to dist/
```

## Where things are

| Path | What |
|---|---|
| `data/ideologies/<id>.yaml` | An ideology: names, motto, paradigm level, place on the chart, parents, relations, works |
| `content/wiki/en/<id>.md`, `content/wiki/zh/<id>.md` | Its wiki entry: `summary`, then `## Beliefs`, `## Arguments`, `## Critiques` (`## 主张`, `## 论据`, `## 批评`) |
| `data/questions.yaml` | Every statement, how agreeing moves each axis, and its sub-dimension on each axis |
| `data/subaxes.yaml` | The sub-dimensions of each axis, scored separately in the pro test |
| `data/tests.yaml` | Which statements each test uses, the pro test's follow-up pool, and the question-bank versions |
| `data/camps.yaml`, `data/axes.yaml`, `data/levels.yaml` | The quick test's nine camps, the five axes, the nine paradigm levels |
| `src/lib/compass.js` | Scoring and matching |
| `scripts/validate.mjs` | The checks every pull request must pass |
| `data/calibration/`, `scripts/calibrate.mjs` | How every ideology was placed: its blind answers, and the script that turns them into the chart |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). In short: everything is a plain file, every change is a pull request, `npm run validate` must pass, both languages move together, and no real person is labelled.

## Inspired by

The Political Compass; 8values and the tests built on it (9Axes, SapplyValues, LeftValues, PolitiScales); and the Polcompball wiki.

## License

Code: MIT. Content (`content/`, `data/`): CC BY-SA 4.0. See [LICENSE](LICENSE).
