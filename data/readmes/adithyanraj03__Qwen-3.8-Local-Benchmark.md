# Qwen3.8 local model benchmark — 7 builds, 54 real tasks

<p align="center">
  <a href="https://adithyanraj03.github.io/Qwen-3.8-Local-Benchmark/"><img alt="Live report" src="https://img.shields.io/badge/Live_report-open_in_browser-2bb5a0?style=for-the-badge&logo=googlechrome&logoColor=white&labelColor=202124"></a>
  <a href="https://adithyanraj03.github.io/Qwen-3.8-Local-Benchmark/#leaderboard"><img alt="Top score: M4 8.98" src="https://img.shields.io/badge/Top_score-M4_%C2%B7_8.98-22a882?style=for-the-badge&labelColor=202124"></a>
</p>
<p align="center">
  <img alt="Benchmark time 5 d 5 h" src="https://img.shields.io/badge/benchmark_time-5d_5h-b8891c?style=flat&labelColor=202124">
  <img alt="GPU: RTX 5090" src="https://img.shields.io/badge/GPU-RTX_5090_%C2%B7_64_GB-76b900?style=flat&logo=nvidia&logoColor=white&labelColor=202124">
  <img alt="Engines: NInfer, Strata, Basalt" src="https://img.shields.io/badge/engines-NInfer_%C2%B7_Strata_%C2%B7_Basalt-e0892f?style=flat&labelColor=202124">
  <a href="https://creativecommons.org/licenses/by/4.0/"><img alt="License: CC BY 4.0" src="https://img.shields.io/badge/license-CC_BY_4.0-lightgrey?style=flat&logo=creativecommons&logoColor=white&labelColor=202124"></a>
</p>

Seven Qwen3.8 builds, each run alone through the same 54 hands-on tasks: games and 3D worlds, SVG and shaders, web apps and extensions, C++, Rust and Go, refactors and bug hunts, LaTeX papers and research write-ups. Everything ran on one RTX 5090 with 64 GB of RAM. Every result was rebuilt, run, recorded and scored by hand, and the owner personally played and rated every game, 3D, sound and design task.

**Live report:** [adithyanraj03.github.io/Qwen-3.8-Local-Benchmark](https://adithyanraj03.github.io/Qwen-3.8-Local-Benchmark/). Scores, recordings, notes and playable demos for all 378 runs.

## Final standings

![Final standings: 1 M4 8.98 (29 tasks won), 2 M7 8.89 (22), 3 M6 8.37 (12), 4 M1 8.22 (11), 5 M5 8.19 (8), 6 M2 8.07 (12), 7 M3 8.06 (9)](assets/readme/standings.png)

## How scoring works

Each run is scored on five axes: Visual, Prompt following, Output, Creativity, and Code at half weight. Visual and Creativity are n/a for code-only tasks. Points come off for visual errors and bugs, and every deduction is written on the run's card.

## Settings each build ran with

From the Strata launch files on the host and the inference monitor's request history for the OpenCode runs
(9 Oct – 2 Nov 2026).

[![Settings each build ran with: engine and launch flags for M1 to M7; M6 is the only build with a speed-projection control vector](assets/readme/settings.png)](https://adithyanraj03.github.io/Qwen-3.8-Local-Benchmark/#settings)

- All builds: RTX 5090 + 64 GB RAM, KV cache int8, vision on.
- **M2 ran with MTP, not DFlash2.** The 27B Orca's first DFlash2 run on this machine was on 3 Nov 2026, after the OpenCode runs.
- **M6 is the only build that ran with a control vector** (a speed-projection steering vector on layers 4–44). Keep that in mind
  when reading its speed and its results.
- **Sampling** was not recorded by the server; it comes from the OpenCode config on the test machine: build agent temperature 0.6,
  top_p 0.95, auto-compaction on with 32,768 tokens reserved. Context window given to OpenCode: 200K for the 27B builds,
  250K for M4 and M5, 500K for M6 and for M7 at 512K, 380K for M7 at 384K.

## What's in the report

- Leaderboard, score matrix, category and chart views
- Model profiles and the best run of every task
- Per-run cards with video, stills, requirement checklists and full notes
- Session logs for every run
- Live demos you can play in the browser: web pages, Three.js scenes, Godot games, PDFs
- A hallucination study
- Hardware and engine details
- Raw data (scores, reasons, per-run stats, speed benchmark) as CSV/JSON in [data/](data/)

## Notes

- The two native C++ games (P3 rally, P5 skateboarding) can't run in a browser. Their "Launch game" buttons only work on the owner's machine; on the website, watch their recordings instead.
- The Alibaba-URL fetches in the hallucination section are ordinary URL hallucinations (made-up links), not data leaks. The report explains this.
- The site is static: no tracking, no server, no build step.

## Run it locally

Download or clone this repository and open `index.html` in Chrome or Edge. The repository carries about 575 MB of recordings and demo assets, so expect a large clone.

## Support

If this report is useful to you, consider sponsoring the owner through the **Sponsor** button at the top of the repository.

## License

© 2026 Adithya N Raj. Released under the [Creative Commons Attribution 4.0 International license (CC BY 4.0)](LICENSE). You may copy, modify, redistribute and use everything here, commercially or not, **as long as you give credit**: name Adithya N Raj, link to this repository, and say if you changed anything.

Ready-to-paste credit line:

```
Qwen3.8 local model benchmark by Adithya N Raj (https://github.com/adithyanraj03/Qwen-3.8-Local-Benchmark), licensed under CC BY 4.0.
```

Third-party libraries used by the live demos (Three.js loaded from cdnjs, the bundled PDF.js viewer, the Godot web runtime) keep their own licenses.