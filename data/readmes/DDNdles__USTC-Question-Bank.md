<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset=".github/assets/hero-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset=".github/assets/hero.svg" />
  <img alt="USTC-Question-Bank" src=".github/assets/hero.svg" width="100%" />
</picture>
<p>
  <a href="LICENSE"><img alt="Code MIT" src="https://img.shields.io/badge/code-MIT-3A7BE0?style=flat-square&labelColor=24292F" /></a>
  <a href="python/ustc_qbank"><img alt="Python >=3.10" src="https://img.shields.io/badge/python-%E2%89%A53.10-3A7BE0?style=flat-square&labelColor=24292F&logo=python&logoColor=white" /></a>
  <a href="types/index.d.ts"><img alt="TypeScript" src="https://img.shields.io/badge/typescript-types-3A7BE0?style=flat-square&labelColor=24292F&logo=typescript&logoColor=white" /></a>
  <a href="scripts/build_sqlite.py"><img alt="SQLite FTS5" src="https://img.shields.io/badge/sqlite-FTS5-3A7BE0?style=flat-square&labelColor=24292F&logo=sqlite&logoColor=white" /></a>
</p>
<p>
  <a href="#收录一览">01 收录一览</a> &nbsp;&nbsp;
  <a href="#仓库结构">02 仓库结构</a> &nbsp;&nbsp;
  <a href="#作为库使用">03 作为库使用</a> &nbsp;&nbsp;
  <a href="#ai-与数据管线说明">04 AI 管线</a> &nbsp;&nbsp;
  <a href="#上游来源">05 上游来源</a> &nbsp;&nbsp;
  <a href="#寻找-contributor--加入共建">06 加入共建</a> &nbsp;&nbsp;
  <a href="#联系方式">07 联系方式</a>
</p>
</div>

面向中国科学技术大学（USTC）本科课程的**结构化、可编程题库底座**。每道题含 Markdown + LaTeX 题干、答案、分步解析、知识点树标签与可信分级，可直接驱动刷题网站、LaTeX 组卷、Anki 制卡、RAG 检索与评测基准。

> **许可边界**：仓库代码、Schema、知识点树与元数据采用 [MIT License](LICENSE)；第三方真题、教材习题及引用解答版权归原权利人所有，**不适用 MIT**，详阅 [NOTICE.md](NOTICE.md)。

<img alt="01" src=".github/assets/route-01.svg" width="100%" />

## 收录一览

| 课号 | 课程 | 总题数 | `official` | `community` | `ai` | 隔离 | 真题年份 | 知识点 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| `001548` | 复变函数B | 571 | 229 | 26 | 316 | 3 | 2003–2025 | 35 |
| `MATH1006` | 数学分析(B1) | 554 | 149 | 300 | 105 | 0 | 2011–2026 | 31 |
| `MATH1007` | 数学分析(B2) | 569 | 131 | 438 | 0 | 0 | 2018–2026 | 28 |
| `MATH1009` | 线性代数(B1) | 885 | 611 | 273 | 1 | 0 | 2011–2026 | 41 |
| `CS1003` | 计算机程序设计 | 1,533 | 1,231 | 188 | 114 | 0 | 2018–2025 | 31 |
| `PHYS1001A` | 力学A（含 91 张配图） | 253 | 49 | 1 | 203 | 5 | 2006–2025 | 46 |
| `PHYS1002A` | 热学A（含 48 张配图） | 352 | 219 | 13 | 120 | 3 | 2004–2026 | 45 |
| `PHYS1004A` | 电磁学A（含 59 张配图） | 121 | 43 | 0 | 78 | 5 | 2017–2026 | 47 |
| `210070` | 数据结构及其算法（含 17 张配图） | 347 | 70 | 142 | 135 | 0 | 2008–2024 | 46 |
| `STAT2002` | 概率论与数理统计（含 1 张配图） | 431 | 327 | 0 | 104 | 3 | 2003–2025 | 48 |
| `PHYS1003A` | 光学A（含 20 张配图） | 228 | 121 | 16 | 91 | 3 | 2020–2025 | 51 |
| `210050` | 数字逻辑电路（含 506 张配图） | 512 | 449 | 23 | 40 | 0 | 2015–2022 | 51 |
| `023181` | 线性电子线路（含 340 张配图） | 407 | 361 | 0 | 46 | 0 | 2014–2019 | 71 |
| `EE2003` | 计算机原理与嵌入式系统（含 20 张配图） | 505 | 122 | 0 | 383 | 13 | 2020–2024 | 53 |
| `MATH1001` | 数学分析(A1) | 169 | 42 | 18 | 109 | 2 | 2018–2026 | 26 |
| `MATH1002` | 数学分析(A2) | 299 | 34 | 27 | 238 | 4 | 2016–2026 | 27 |
| `PHYS1001B` | 力学B（含 157 张配图） | 379 | 161 | 12 | 206 | 7 | 2006–2025 | 46 |
| `PHYS1002B` | 热学B（含 32 张配图） | 277 | 176 | 0 | 101 | 1 | 2004–2025 | 45 |
| `MATH1004` | 线性代数(A1) | 171 | 113 | 23 | 35 | 1 | 2014–2026 | 47 |
| `MATH1005` | 线性代数(A2) | 166 | 118 | 0 | 48 | 2 | 2014–2026 | 44 |
| `MATH1010` | 线性代数(B2) | 131 | 10 | 51 | 70 | 5 | 2021–2025 | 45 |
| `PHYS1004H` | 电磁学(H)（含 38 张配图） | 131 | 42 | 0 | 89 | 1 | 2024–2026 | 53 |
| `PHYS1004C` | 电磁学C（含 100 张配图） | 151 | 42 | 40 | 69 | 9 | 2017–2025 | 46 |
| `PHYS1004B` | 电磁学B（含 65 张配图） | 151 | 96 | 0 | 55 | 1 | 2020–2021 | 40 |
| `PHYS1001H` | 力学(H)（含 14 张配图） | 78 | 53 | 0 | 25 | 5 | 2023–2026 | 39 |
| `019161` | 化学原理A（含 4 张配图） | 132 | 92 | 0 | 40 | 0 | 2024 | 47 |
| `019163` | 化学原理B | 86 | 49 | 0 | 37 | 0 | — | 49 |
| `019165` | 普通化学（含 7 张配图） | 328 | 327 | 0 | 1 | 0 | — | 41 |
| `019166` | 无机化学I（含 1 张配图） | 252 | 218 | 0 | 34 | 0 | 2004 | 50 |
| `CS1003L` | 计算机程序设计(L) | 191 | 189 | 0 | 2 | 0 | 2024–2025 | 26 |
| `CS1002A` | 计算系统概论A（含 66 张配图） | 232 | 76 | 0 | 156 | 0 | 2020–2023 | 24 |
| `MARX1012` | 思想道德与法治 | 1,227 | 1,195 | 9 | 23 | 0 | 2022–2024 | 25 |
| `229001` | 离散数学（含 3 张配图） | 431 | 255 | 0 | 176 | 22 | 2021–2025 | 33 |
| `MATH1003` | 数学分析(A3) | 247 | 139 | 0 | 108 | 2 | 2016–2026 | 27 |
| `MATH1008` | 数学分析(B3) | 270 | 102 | 0 | 168 | 2 | 2007–2026 | 24 |
| `PHYS1005A` | 原子物理A | 165 | 145 | 0 | 20 | 0 | 2016–2026 | 26 |
| `PHYS1005B` | 原子物理B（含 3 张解图） | 156 | 85 | 0 | 71 | 3 | 2016–2025 | 20 |
| `PHYS1003B` | 光学B（含 23 张配图） | 147 | 102 | 0 | 45 | 1 | 2022 | 23 |
| `MARX1011` | 马克思主义基本原理 | 511 | 439 | 0 | 72 | 1 | — | 27 |
| `MARX1010` | 中国近现代史纲要 | 1,106 | 1,075 | 0 | 31 | 0 | — | 20 |
| `MARX1013` | 毛泽东思想和中国特色社会主义理论体系概论 | 681 | 636 | 0 | 45 | 0 | 2022 | 43 |
| `MARX1014` | 习近平新时代中国特色社会主义思想概论 | 285 | 212 | 0 | 73 | 1 | 2022 | 48 |
| `009501` | 工程制图（含 87 张配图） | 236 | 94 | 0 | 142 | 9 | — | 49 |
| `PHYS1010` | 量子物理 | 716 | 414 | 0 | 302 | 5 | 2023–2026 | 48 |
| `019011` | 有机化学A1（含 310 张配图） | 1,559 | 726 | 0 | 833 | 2 | 2013–2025 | 50 |
| `019012` | 有机化学A2 | 99 | 51 | 0 | 48 | 15 | 2016–2019 | 44 |
| `019047` | 有机化学B | 193 | 131 | 0 | 62 | 0 | 2021–2022 | 31 |
| `022392` | 理论力学A | 293 | 83 | 0 | 210 | 45 | 2016–2026 | 38 |
| `022057` | 电动力学 | 198 | 113 | 20 | 65 | 0 | 2016–2026 | 39 |
| `001506` | 数理方程A | 182 | 75 | 0 | 107 | 4 | 2001–2025 | 41 |
| `001505` | 复变函数A | 173 | 17 | 0 | 156 | 7 | 2005–2024 | 31 |
| `MATH3008` | 复分析 | 305 | 13 | 0 | 292 | 7 | 2011–2026 | 33 |
| `MATH3002` | 实分析 | 239 | 40 | 0 | 199 | 5 | 2015–2026 | 37 |
| `MATH3007` | 概率论 | 241 | 18 | 0 | 223 | 7 | 2013–2026 | 37 |
| `MATH3001` | 近世代数 | 255 | 26 | 0 | 229 | 6 | 2019–2026 | 38 |
| `017063` | 数理统计 | 84 | 47 | 0 | 37 | 5 | 2021–2026 | 37 |
| `017129` | 实用随机过程 | 204 | 79 | 0 | 125 | 1 | 2011–2026 | 40 |
| `001101` | 常微分方程 | 141 | 77 | 0 | 64 | 1 | 2016–2026 | 36 |
| `001122` | 偏微分方程 | 103 | 59 | 0 | 44 | 1 | 2020–2025 | 36 |
| `MATH2004` | 代数学基础 | 241 | 64 | 0 | 177 | 6 | 2021–2025 | 25 |
| `011103` | 代数结构 | 120 | 0 | 0 | 120 | 5 | 2017–2026 | 24 |
| `210045` | 电路基本理论 | 140 | 98 | 0 | 42 | 27 | 2016–2025 | 27 |
| `MATH2003` | 几何学基础 | 67 | 18 | 0 | 49 | 1 | 2021–2025 | 24 |
| **合计** | **63 门课程** | **21,607** | **12,578** | **1,620** | **7,409** | **264** | — | **2,400** |

- **100% 含答案与分步解析**。`official` 为原卷/书末标答，`community` 为非官方书面详解，`ai` 为模型或独立推导。

<details>
<summary>展开查看各课程批次明细与已知勘误</summary>

- **`001548` 复变函数B**：`complex_b` (225，14 套期末含补考)、`complex_b_midterm` (3，2023 期中)、`jiangyi_examples` (10，舒文炫讲义)、`github_workbook` (40，[`jieyou520/-`](https://github.com/jieyou520/-))、`yan_complex` (127，严镇军《复变函数》第 2 版)、`yan_mp_part1` (99，与 `yan_complex` 部分重叠，去重可排除)、`yan_mp_part2` (67，《数学物理方法》第二篇)。
- **`MATH1006` 数学分析(B1)**：`ma1_exams` (254，2016 小测 + 2011–2026 期中/期末 25 套)、`ma1_textbook` (300，《数学分析讲义》第一册，[`DongYaoZe`](https://github.com/DongYaoZe/math-analysis-lectures-solutions-USTC) 详解)。
- **`MATH1007` 数学分析(B2)**：`ma2_exams` (131，2018–2026 期中/期末 17 套)、`ma2_textbook` (438，《数学分析讲义》第二册，[`DongYaoZe`](https://github.com/DongYaoZe/math-analysis-lectures-solutions-USTC) 详解)。
- **`MATH1009` 线性代数(B1)**：`la1_exams` (566，2010–2026 学年 42 套期中/期末，含花开花败 20 套参考解答 + 22 套单卷)、`la1_textbook` (319，李尚志《线性代数学习指导》第 1–4、6、8、9 章例题分析与解答)。
- **`CS1003` 计算机程序设计**：`cs1_exams` (334，2018–2025 期中/期末/补考/机考 13 套)、`cs1_quiz` (319，2012 学习指导 + 2024 秋模拟 + 2025 版复习测试各 4 套)、`cs1_banks` (750，三份公开 C 语言题库)、`cs1_drill` (130，指针专题、期中练习与习题课课件)。
- **`PHYS1001A` 力学A**：`mech1_exams` (105，2016–2026 学年期中/期末 14 套，含 A(L) 班卷)、`mech1_quiz` (147，2005–2016 力学历年考题合集 15 套)、`mech1_drill` (1，刚体笔记例题)；86 道带图题共附 91 张配图（`courses/PHYS1001A/assets/`，70 张灰度 WebP + 21 张矢量重绘 SVG，合计 449 KB）。
- **`PHYS1002A` 热学A**：`therm1_exams` (105，2016–2026 期中/期末/预考/免修考与公共题)、`therm1_quiz` (233，热学历年真题合订本 10 卷 + 2021 三次小测 + 清华《大学物理》热学选择题库 86 题)、`therm1_drill` (14，2023 春 wxf 班参考题)；48 道带图题共附 48 张配图（`courses/PHYS1002A/assets/`，25 张灰度 WebP + 23 张矢量重绘 SVG，合计 124.7 KB）。
- **`PHYS1004A` 电磁学A**：`em1_exams` (107，2017–2026 期中/期末公共题、各班回忆版与 2023 秦敢期中样题)、`em1_quiz` (4，课堂练习/小测)、`em1_drill` (10，磁场习题课讲稿例题)；58 道带图题共附 59 张配图（`courses/PHYS1004A/assets/`，33 张灰度 WebP + 26 张矢量重绘 SVG，合计 212.2 KB）。
- **`210070` 数据结构及其算法**：`ds1_exams` (174，2008–2019 四学年期末、2024 秋期末及《数据结构》试卷A)、`ds1_drill` (173，2-4-6-8 / 3-5-7-9 / 10.24 习题课讲义与六次课程作业)；17 道含关键图例题附配图（`courses/210070/assets/`，14 张灰度 WebP + 3 张矢量重绘 SVG，合计 102.1 KB）。
- **`STAT2002` 概率论与数理统计**：`stat1_exams` (431，2002–2026 学年共 36 套期末/期中真题，含 327 题原卷/合集标答与 104 题独立解析，3 题因缺表或设问不严隔离)；`2002–2003` 期末第一题附五开关桥式电路矢量 SVG 配图（`courses/STAT2002/assets/STAT2002-exam-2003s-f-01-fig1.svg`）。
- **`PHYS1003A` 光学A**：`opt1_exams` (98，2020–2026 学年 6 套期末与模拟试卷，含 2023 秋卷面手写批注答案版)、`opt1_drills` (107，《光学复习指导》第 1–7 章例题与作业题)、`opt1_sets` (23，《光学A习题集》)；20 道带图题（17 道真题 + 3 道复习指导例题）附经去边与均衡增强的灰度 WebP 配图（`courses/PHYS1003A/assets/`）。
- **`210050` 数字逻辑电路**：`dl1_exams` (92，2015–2023 学年 7 套期末真题与 2020 秋 06 班模拟卷，含 2019–2020 与 2020–2021 助教手写答案版)、`dl2_book` (293，阎石、王红《数字电子技术基础（第六版）学习辅导与习题解答》第 1–8 章 66 道例题与 227 道教材习题解答)、`dl2_papers` (127，同书第四部分 7 套自测试卷及书末答案)；362 道带图题共附 506 张精裁 WebP 与空白矢量 SVG（`courses/210050/assets/`，503 张灰度 WebP + 3 张 SVG，合计 6.80 MB）。
- **`023181` 线性电子线路**：`le1_book` (342，童诗白、华成英版配套《模拟电子技术基础（第五版）全程辅导与习题全解》第 1–10 章全部 100 道例题、40 道自测题与 202 道课后习题)、`le1_exams` (65，2014–2019 年期末真题/回忆版及 B 课样卷/模拟卷共 6 套)；319 道带图题共 340 张灰度 WebP 配图（`courses/023181/assets/`，含 7 幅补自原教材第五版的随文插图与 16 幅典型解图，去红水印与光照均衡后合计 5.04 MB）。
- **`EE2003` 计算机原理与嵌入式系统**：`ce_book` (295，胡访宇主编《计算机原理与嵌入式系统》第 1–8 章全部章末习题，含 98 题课程作业/习题课官方解答与 197 题独立解析)、`ce_supp` (24，课程作业参考答案教师加编补充题)、`ce_papers` (186，2019–2020 春、2023–2024 期末、2024 A 卷及 2023–2024 题型示意卷共 4 套，13 题因题干歧义或条件开放隔离)；20 道含图题共附 20 张引用 / 13 幅去重灰度 WebP 配图（`courses/EE2003/assets/`，合计 361.1 KB），期末卷所引汇编/GPIO/EXTI 附录代码与向量表均已内联为纯文本代码块与表格。
- **`MATH1001` 数学分析(A1)**：`maa1_exams` (169，2018–2026 学年 15 套期中与期末真题，含 42 题官方解答、18 题学生手写/非官方整理卷附解答与 109 题独立求解，2 题因原卷条件疑残缺隔离；2015 回忆残卷与 2023 秋 A3 卷未收录)。
- **`MATH1002` 数学分析(A2)**：`maa2_exams` (299，2016–2026 年 30 套期中、期末及单元测试/小测真题，含 7 份评课社区附件、34 题官方解答、27 题手写扫描/非官方整理卷附解答与 238 题独立求解，4 题因原卷扫描残缺或条件/命题歧义隔离)。
- **`PHYS1001B` 力学B**：`mechb1_exams` (145，2018–2025 学年 11 套力学B 期中/期末真题与回忆版)、`mechb1_quiz` (147，2005–2016 力学历年考题合集 15 套，与 `PHYS1001A` 同源按 B 树重标)、`mechb1_reuse` (7，2020 力学与热学期中力学部分)、`mechb1_drill` (80，2025 春习题课一/三讲稿与《一次有趣的作业》)；145 道带图题共附 157 张（123 幅去重）SVG/WebP 配图（`courses/PHYS1001B/assets/`，138 张灰度/彩图 WebP + 19 张 SVG，合计 1.86 MB），7 题低置信度隔离。
- **`PHYS1002B` 热学B**：`thermb1_exams` (131，2018–2025 学年 9 套热学B 期末真题及合卷热学部分)、`thermb1_quiz` (123，2004–2015 热学历年真题合集 12 套，与 `PHYS1002A` 同源按 B 树重标)、`thermb1_reuse` (13，2016 秋力学与热学期末及 2017 年公共题)、`thermb1_drill` (10，2025 春热学B 习题课讲稿)；30 道带图题共附 32 张（28 幅去重）SVG/WebP 配图（`courses/PHYS1002B/assets/`，22 张灰度 WebP + 10 张 SVG，合计 372.7 KB），1 题因设问残缺隔离。
- **`MATH1004` 线性代数(A1)**：`laa1_exams` (171，2014–2026 年 13 套期中/期末真题含合集 B 套，其中 113 题原卷参考解答、23 题来自 2023/2024 期末学生整理版解答、35 题独立推导；2014 期中第 2 题因缺向量组定义隔离，合集重复 A 套已去重)。
- **`MATH1005` 线性代数(A2)**：`laa2_exams` (166，2014–2026 学年 14 套期中/期末真题，其中 118 题原卷参考答案与评分标准、48 题含三套早期手写扫描卷由模型独立推导；2 题因疑似手抄笔误或题干缺限定隔离)。
- **`MATH1010` 线性代数(B2)**：`lab2_exams` (131，2021–2025 学年 12 份期中/期末真题与整理卷，含 2021–2022 秋期中参考解答 10 题、NULIOUS 整理版 2021–2024 期末与 2024 期中手写解答 51 题及 70 题独立求解；错标重复件 `2023LAB2mid` 已去重，5 题因缺题干或区间条件缺失隔离)。
- **`PHYS1004H` 电磁学(H)**：`emh_exams` (131，2024–2026 春共 6 卷期中/期末真题与解答，含 2025 春合卷 LaTeX 源码与 2024 春期中解答扫描件 42 题、89 题独立求解，1 题因积分面未指明隔离)；37 道含图题共附 38 张（11 幅去重）灰度 WebP 配图（`courses/PHYS1004H/assets/`，含 1 幅镜像法解图，合计 697.9 KB）。
- **`PHYS1004C` 电磁学C**：`emc_exams` (151，2017–2025 学年 11 卷期中/期末与公共题，含 42 题原卷/评分细则、40 题 feixu 公开学生整理版含解与 69 题独立求解，9 题因回忆版缺参缺图隔离)；98 道含图题共附 100 张（39 幅去重）灰度 WebP 配图（`courses/PHYS1004C/assets/`，含 9 幅复用自 `PHYS1004A` 与 2 幅波形/边值解图，合计 774.7 KB）。
- **`PHYS1004B` 电磁学B**：`emb_exams` (46，2019–2021 期中/期末与公共真题)、`emb_drills` (105，2024 春第 1/2/4 次习题课讲稿例题与习题，1 题隔离)；64 道含图题共附 65 张（42 幅去重）灰度 WebP 配图（`courses/PHYS1004B/assets/`，含 9 幅复用自 `PHYS1004A` 与 1 幅高斯面解图，合计 566.7 KB）。
- **`PHYS1001H` 力学(H)**：`mh_exams` (78，2023–2026 学年秋 3 套 H 班期中与 3 套 A&H 共用期末真题，含 53 题参考答案与 25 题独立求解，5 题低置信度隔离)；14 道含图题共附 14 张（13 幅去重）灰度 WebP 配图（`courses/PHYS1001H/assets/`，10 幅复用自 `PHYS1001A` + 3 幅 2024 秋期中手绘题图，合计 54.6 KB）。
- **`019161` 化学原理A**：`cpa_exams` (116，2024 秋期末真题 35 题 + 化学原理历年真题汇编 81 题)、`cpa_drills` (16，2022 秋第三次习题课讲义)；4 道附加题附 4 张（1 幅去重）钾-石墨插层化合物晶胞灰度 WebP 配图（`courses/019161/assets/`，合计 46.6 KB）。
- **`019163` 化学原理B**：`cpb_solved` (37，第 2–14 章分章习题解析)、`cpb_drills` (49，习题课一至六及配位化合物/缓冲计算讲义，含 49 题原书/课件红字标答与 37 题模型独立推导)。
- **`019165` 普通化学**：`gnc_solved` (313，《普通化学原理（第 4 版）习题解析》第 2–15 章全量课后习题，含 312 题原书解析与第 15.30 题模型补写提纲)、`gnc_drills` (15，2024 秋课堂笔记随堂例题)，100% 覆盖 28 个二级知识点；5 道带图题共附 7 张灰度 WebP 原书配图（`courses/019165/assets/`，合计 54.9 KB）。
- **`019166` 无机化学I**：`ino_exams` (49，四套模拟习题与 2004–2005 期中试题，已据原 DOCX XML 还原下划线物种并校正 11 题单选标答)、`ino_solved` (60，往年参考资料汇编)、`ino_drills` (143，BN/C-O-F/ds-df 族元素讲义及习题课一至四)；习题课一第 8 题附双核配离子灰度 WebP 配图（`courses/019166/assets/`，21.3 KB）。
- **`CS1003L` 计算机程序设计(L)**：`cpl_exams` (10，2025 秋机考一含答案版 + 机考二)、`cpl_solved` (151，2024 秋模拟测试与答案四套综合卷，已补全综合二第五-2 题完整源码)、`cpl_drills` (30，12-14/12-22 习题课与 2023/2025 复习测试题)；按选课体例独立成库（与 `CS1003` 有 53 题同源重叠，联合使用时可按题干去重）。
- **`CS1002A` 计算系统概论A**：`csa_exams` (82，2020–2024 四套期中真题，全量无答案经模型求解并配图)、`csa_homework` (89，ICS 作业 1/3/4/5/6，含 `hw02..hw06_solution.pdf` 官方标答升级)、`csa_solved` (26，教材课后题解答)、`csa_drills` (35，复习笔记与 2021 期中重点；原假纲 5 题已剔除)；54 道带图/程序表题共附 66 张（37 幅去重）灰度 WebP 配图（`courses/CS1002A/assets/`）。
- **`MARX1012` 思想道德与法治**：`ide_exams` (29，2022–2025 思政试题与无纸化考试题，含 9 题 `22、23思政答案chatgpt版` 归为 `origin=community`)、`ide_qbank` (1,137，2021 秋/2024 秋/2025 德法机考全量去重题库)、`ide_drills` (38，复习与教材提纲)、`ide_solved` (23，课后思考题)。
- **`229001` 离散数学**：`dmath_paper` (171，2021–2025 期中/期末真题 69 题与 2024 秋七次作业 102 题)、`dmath_solved` (203，《离散数学教程》《组合数学》配套解答及开放教材)、`dmath_drill` (57，数理逻辑/代数结构/图论组合 22 份讲义与复习提纲)；附 3 张灰度 WebP 配图（`courses/229001/assets/`），22 题隔离（主要为 2024 期末选填空题干或组合数学缺图习题）。
- **`MATH1003` 数学分析(A3)**：`ma3_paper` (157，2016–2026 年 15 套期中/期末真题与整理卷)、`ma3_drill` (90，2022 秋课堂笔记及第 1/3/5/7 次习题课讲义，2 题因原卷条件疑残缺隔离)。
- **`MATH1008` 数学分析(B3)**：`mb3_paper` (171，2016–2025 年 12 套 B3 期中/期末真题)、`mb3_solved` (95，《数学分析(B)历年真题汇编》13 套真题与 XeLaTeX 重建解析，已逐页重校)、`mb3_drill` (4，2026 第 15 章课堂小测，2 题隔离)。
- **`PHYS1005A` 原子物理A**：`apa_solved` (95，2016–2025 期末/综合卷及二、四章含答案小测)、`apa_paper` (30，2026 期末卷与第二章小测无答案扫描件)、`apa_drill` (40，讲义、笔记与两次习题课例题；0 隔离)。
- **`PHYS1005B` 原子物理B**：`apb_solved` (73，2015–2018 期末真题及 2016 前合集)、`apb_paper` (26，2021–2022/2025 期末卷与课后习题)、`apb_drill` (57，分章讲义、概念公式集与五次习题课)；3 道期末真题附能级/跃迁灰度 WebP 解图（`courses/PHYS1005B/assets/`，合计 35.1 KB），3 题隔离。
- **`PHYS1003B` 光学B**：`ob_paper` (25，2022 春期末真题及《交叉学科光学习题》)、`ob_solved` (60，《交叉学科基础物理教程·光学》课后习题及《光学B习题解答》)、`ob_drill` (62，《Optics 光学讲义》与光学B 复习讲义)；23 道带图题共附 23 张（18 幅去重）灰度 WebP 配图（`courses/PHYS1003B/assets/`，合计 197.9 KB），1 题因条件简略隔离。
- **`MARX1011` 马克思主义基本原理**：`marxp_paper` (6，期末回忆试题)、`marxp_solved` (399，2023 版教材课后解答、复习题库与考研辨析/材料分析题)、`marxp_drill` (106，教材要点、提纲、索引与重点整理；1 题隔离)。
- **`MARX1010` 中国近现代史纲要**：`mch_solved` (1,016，2022 春/2026 史纲机考题库、人名/会议/期刊/著作/论战专题及书本例题)、`mch_drill` (90，《史纲简记》与问题总结；0 隔离)。
- **`MARX1013` 毛泽东思想和中国特色社会主义理论体系概论**：`mg_paper` (482，2021 年版教材笔记与课后习题详解 342 题、简答题题库 123 题、2022 春期末考场抄写版 17 题)、`mg_drill` (199，开卷资料、课程提纲与复习讲义；0 隔离)。
- **`MARX1014` 习近平新时代中国特色社会主义思想概论**：`xg_paper` (10，2022 秋期末试题)、`xg_drill` (275，教材思考题、课程笔记、知识点总结、钱学森班复习提纲与课本索引；1 题因原卷题干缺失隔离)。
- **`009501` 工程制图**：`ed_paper` (8，机械制图及 CAD 模拟考题)、`ed_drill` (228，《制图与CAD》第 0–8 讲课件例题与《机械制图多媒体教程》分章课件，合并覆盖 009501 / 009171)；70 道带图/建模题共附 87 张精裁及双色剥离 WebP 配图（`courses/009501/assets/`，合计 2.59 MB），9 题因缺原装配/示例图隔离。
- **`PHYS1010` 量子物理**：`qp_paper` (266，2023–2026 期末卷、期中/期末样卷与回忆版及《量子力学习题集》)、`qp_solved` (29，期中/期末样卷参考评分标准)、`qp_answer` (207，第 1–7 章及第 1–6 次作业答案、周世勋教程解答等)、`qp_drill` (214，讲义、课程资料与《猴子都能懂的量子物理教程》；5 题因缺矢量/光路图或残缺隔离)。
- **`019011` 有机化学A1**：`oca1_paper` (250，期中/期末与小测原卷)、`oca1_solved` (471，2013–2025 期中/期末、小测与 MOOC 期末测试参考解答)、`oca1_answer` (44，第二次小测答案与《有机化学反应机理的书写艺术》答案)、`oca1_drill` (794，分章讲义、2024 课件、MOOC 作业 1–13 讲与机理练习)；186 道带图题共附 310 张 300 DPI 灰度 WebP 配图（`courses/019011/assets/`，含结构式、反应路线、NMR/MS 谱图与配套解图），原 223 道缺图隔离题经逐页裁图与重解恢复 221 题（仅 2022 秋第一次小测答案二.1 与二.5 因原 PDF 仅印题号占位未附反应图而保留隔离）。
- **`019012` 有机化学A2**：`oca2_paper` (19，2016–2017 英文期末卷)、`oca2_solved` (45，2015–2019 期终 A 卷与第一次单元测试含解答)、`oca2_answer` (35，第二/三次习题课练习题与参考答案；15 题因需据原卷结构式作答隔离)。
- **`019047` 有机化学B**：`ocb_paper` (25，2021 秋第一次小测)、`ocb_solved` (101，2021–2022 秋期中及第二/三/四次小测与答案)、`ocb_answer` (52，有机化学B 第一/二/三次小测答案)、`ocb_drill` (15，10.24 习题课小测 1；0 隔离)。
- **`022392` 理论力学A**：`tma_exams` (293，2016–2026 学年 23 份期中/期末真题，含潘海俊班试卷与 2018–2021 补充卷；45 题因题图维度或条件约定隔离)。
- **`022057` 电动力学**：`elec_exams` (178，2016–2026 学年 13 套期中/期末真题含王少杰班期末)、`ed_guo_sol` (20，郭硕鸿《电动力学》第四版 Uphi. 修订版参考解答，`origin=community`；0 隔离)。
- **`001506` 数理方程A**：`mpea_exams` (182，2001–2025 学年 16 套历年真题汇编及 2025 春参考答案；4 题隔离)。
- **`001505` 复变函数A**：`cva_exams` (173，2005–2024 年 10 套历年期末真题与参考解答；7 题隔离)。
- **`MATH3008` 复分析**：`cplx_exams` (305，2011–2026 年 23 套期中/期末真题；7 题隔离)。
- **`MATH3002` 实分析**：`real_exams` (199，2015–2026 年 20 套期中/期末真题)、`real_hw` (40，2007–2008 学年《实变函数习题答案》；5 题隔离)。
- **`MATH3007` 概率论**：`prob_exams` (241，2013–2026 年 23 套数院期中/期末真题；7 题隔离)。
- **`MATH3001` 近世代数**：`alg_exams` (255，2019–2026 年 13 套期中/期末真题与随堂测验；6 题隔离)。
- **`017063` 数理统计**：`stat2_exams` (84，2021–2026 年 8 套期中/期末真题及残卷含 2025 期末；5 题隔离)。
- **`017129` 实用随机过程**：`stoc_exams` (204，2011–2026 年 15 套期中/期末真题含 2024–2025 期中/期末；1 题隔离)。
- **`001101` 常微分方程**：`ode_exams` (69，2016–2026 年 7 套《常微分方程、偏微分方程》期中/期末/小测真题)、`ode_hw` (72，2026 秋章俊彦班第 1–5 次作业；1 题隔离)。
- **`001122` 偏微分方程**：`pde_exams` (42，2020–2025 年 4 套《常微分方程、偏微分方程》期末真题)、`pde_hw` (61，2025 秋章俊彦班第 1–4 次作业；1 题隔离)。
- **`MATH2004` 代数学基础**：`algbase_exams` (241，2021–2025 年 10 套期中/期末真题、2 套期中模拟及往年题精选；6 题隔离)。
- **`011103` 代数结构**：`algstruct_exams` (120，2017–2026 年 10 套去重期中/期末及小测真题，全部模型独立证明求解；5 题隔离)。
- **`210045` 电路基本理论**：`circuit_exams` (140，2015–2025 学年 10 套去重期末真题及公开参考答案，附原卷电路拓扑注释；27 题隔离)。
- **`MATH2003` 几何学基础**：`geom_exams` (67，2021–2025 年 5 套期中/期末真题；1 题隔离)。
- 详细勘误与局限见各课程 `courses/<课号>/meta.json` 的 `known_notes`。

</details>

<img alt="02" src=".github/assets/route-02.svg" width="100%" />

## 仓库结构

按 USTC 官方课号组织，纯文本 JSONL 入库，原生预留带图题（`figures` + `assets/` + `asset_base_url`）与选择题（`options`）：

```text
USTC-Question-Bank/
├── manifest.json                 # 全库索引、统计、SHA-256 与外置资产基址
├── schema/                       # JSON Schema (2020-12): manifest / question / taxonomy
├── courses/<course_code>/        # 001548 / MATH1006 / MATH1007 / MATH1009 / CS1003 / PHYS1001A / ...
│   ├── meta.json                 # 课程元数据与批次统计
│   ├── taxonomy.json             # 知识点层次树
│   ├── questions.jsonl           # 单题流（按稳定全局 ID 排序）
│   └── assets/                   # （按需）带图题的 SVG / WebP / PNG 配图
├── python/ustc_qbank/            # 零依赖 Python 加载库与 SQLite FTS5 构建器
├── types/index.d.ts              # TypeScript 类型定义
└── scripts/                      # validate.py（CI 全量体检）与 build_sqlite.py
```

<details>
<summary>展开查看单题 JSON 契约示例</summary>

```json
{
  "id": "001548-exam-2003f-01",
  "course_code": "001548",
  "schema_version": "1.0",
  "type": "blank",
  "stem": { "md": "设方程 $z^{3}=\\bar{z}$，求 $z$。", "figures": [] },
  "options": [],
  "answer": {
    "md": "$z\\in\\{0,\\ 1,\\ -1,\\ \\mathrm{i},\\ -\\mathrm{i}\\}$",
    "figures": [],
    "origin": "ai",
    "origin_detail": "入库时独立推导"
  },
  "solution": { "md": "...", "steps": ["..."], "figures": [] },
  "tags": { "kp_ids": ["cplx.eq"], "keywords": ["复方程求解"], "difficulty": 2 },
  "source": {
    "kind": "exam_paper",
    "batch": "complex_b",
    "ref": "2003-2004学年第一学期复变函数（B）期末 第一(1)题",
    "year": 2003,
    "term": "2003-2004-1",
    "exam_kind": "final",
    "url": "https://share.feixu.site/数学类/复变函数/复变函数历年真题.pdf",
    "rights": "third_party_exam"
  },
  "quality": {
    "quarantined": false,
    "quarantine_reason": null,
    "confidence": null,
    "note": null,
    "overlap_hint": null
  }
}
```

</details>

<img alt="03" src=".github/assets/route-03.svg" width="100%" />

## 作为库使用

**Python（零第三方依赖）**

```bash
git clone https://github.com/DDNdles/USTC-Question-Bank.git && pip install -e ./USTC-Question-Bank
# 中科大校内 / 国内直连镜像（git.ustc.edu.cn，自动同步）：
# git clone https://git.ustc.edu.cn/zzl_stella05/USTC-Question-Bank.git
```

```python
from ustc_qbank import QuestionBank

bank = QuestionBank("./USTC-Question-Bank")
qs = bank["MATH1006"].query(kp="ma1.lim", origins=["official"], difficulty=(2, 4))
paper = bank["001548"].sample(12, seed=2026, exclude_batches=["yan_mp_part1"])
```

- **SQLite FTS5**：`python scripts/build_sqlite.py -o dist/ustc-question-bank.sqlite`
- **TypeScript / 前端**：直接引入 [types/index.d.ts](types/index.d.ts)，按 `manifest.json` 拉取 Raw JSONL
- **Hugging Face / RAG**：`load_dataset("json", data_files="courses/MATH1006/questions.jsonl")`
- **本地校验**：`python scripts/validate.py && python -m unittest discover -s tests -v`

<img alt="04" src=".github/assets/route-04.svg" width="100%" />

## AI 与数据管线说明

所有 AI 产出均通过 `answer.origin` 与 `quality` 透明标注：

| 环节 | 模型 / 工具 | 说明 |
| --- | --- | --- |
| 仓库架构与工程设计 | <img src="https://cdn.simpleicons.org/googlegemini/4285F4" width="16" height="16" align="absmiddle" alt="Gemini" /> [**Gemini 4 Neon**](https://deepmind.google/technologies/gemini/) | 数据契约、Schema、Python/TS 库、SQLite FTS5 与 CI 校验架构 |
| 题目分析、标注与无答案题解析 | <img src="https://cdn.simpleicons.org/googlegemini/4285F4" width="16" height="16" align="absmiddle" alt="Gemini" /> [**Gemini 4 Hydrogen**](https://deepmind.google/technologies/gemini/) · <img src="https://avatars.githubusercontent.com/u/148330874?s=64&v=4" width="16" height="16" align="absmiddle" alt="DeepSeek" /> [**DeepSeek-v4.1-flash-1017**](https://github.com/deepseek-ai) · <img src="https://avatars.githubusercontent.com/u/223098841?s=64&v=4" width="16" height="16" align="absmiddle" alt="GLM" /> [**GLM-5.3-Flash**](https://github.com/zai-org) · <img src="https://avatars.githubusercontent.com/u/210980732?s=64&v=4" width="16" height="16" align="absmiddle" alt="Hunyuan" /> [**hy4flash**](https://github.com/Tencent-Hunyuan) | 题目切分结构化、知识点与难度标注、勘误复核及无答案题独立求解 |
| 数分教材详解上游底本 | <img src="https://cdn.simpleicons.org/googlegemini/4285F4" width="16" height="16" align="absmiddle" alt="Gemini" /> [**Gemini Pro**](https://deepmind.google/technologies/gemini/)（[`DongYaoZe`](https://github.com/DongYaoZe/math-analysis-lectures-solutions-USTC) 上游） | 原作者前言注明以 Gemini Pro 会员起草初稿并经多轮人工校订（未注明具体小版本），入库时已二次复核 |
| 试卷与教材 PDF OCR | <a href="https://github.com/opendatalab/MinerU"><img src="https://raw.githubusercontent.com/opendatalab/MinerU/master/docs/images/MinerU-logo.png" height="16" align="absmiddle" alt="MinerU" /></a> / PaddleOCR-VL @ <img src=".github/assets/ustc-107.svg" width="16" height="16" align="absmiddle" alt="USTC 107" /> [**107.ustc.edu.cn**](https://107.ustc.edu.cn/) | 在中科大 107 平台自部署 MinerU / PaddleOCR-VL GPU 作业完成版面、公式与插图裁剪 |

<img alt="05" src=".github/assets/route-05.svg" width="100%" />

## 上游来源

> **特别鸣谢**：本仓库各门课程资料的系统收集与目录索引得益于 [`TwinJades/USTC_Study_Materials_Navigation`](https://github.com/TwinJades/USTC_Study_Materials_Navigation) 的整理与开源分享，特此致谢。

| 上游项目 / 站点 | 对应内容 | 链接 |
| --- | --- | --- |
| 中科大本科课程资料导航 | 课程资料总索引入口（特别鸣谢） | [TwinJades/USTC_Study_Materials_Navigation](https://github.com/TwinJades/USTC_Study_Materials_Navigation) |
| feixu 镜像站 | 数学/物理/计算机历年真题、题库、参考解答与复习讲义 | [share.feixu.site](https://share.feixu.site/) |
| USTC Math Exam | 复变/数分/线代近年真题卷面 PDF | [ustcmathexam.github.io](https://ustcmathexam.github.io/) |
| USTC Physics Exam | 力学A / 热学A / 电磁学A 历年真题卷面 PDF | [ustcphyexam.github.io](https://ustcphyexam.github.io/) |
| USTC 评课社区 | 复变/线代/程序设计/力学真题、解答与笔记附件 | [icourse.club](https://icourse.club/) |
| 《数学分析讲义》非官方习题详解 | 数分 B1/B2 教材第 1–13 章详解底本（`origin=community`） | [DongYaoZe/math-analysis-lectures-solutions-USTC](https://github.com/DongYaoZe/math-analysis-lectures-solutions-USTC) |
| 复变函数期末复习题库 | 复变 40 题复习题集（`github_workbook`） | [jieyou520/-](https://github.com/jieyou520/-) |
| 数学分析历年真题汇编与讲义 | 补充卷面与课程范围核对 | [Passiflora-sago/Passiflora-sago.github.io](https://github.com/Passiflora-sago/Passiflora-sago.github.io) |
| `023181` / `EE2003` / 专业课资料 | 线代、计科、电子信息与微分方程课程主页资料 | [zhangjy9610.me](https://www.zhangjy9610.me/) · [fandahao17/USTC-CS-Courses-Resource](https://github.com/fandahao17/USTC-CS-Courses-Resource) · [Wloner0809/ustc-course-resource](https://github.com/Wloner0809/ustc-course-resource) · [guch8017/USTC_CS_EXAM](https://github.com/guch8017/USTC_CS_EXAM) · [duxiaoyang/USTC-Course-Materials](https://github.com/duxiaoyang/USTC-Course-Materials) · [ly382965/USTC_learning_materials](https://github.com/ly382965/USTC_learning_materials) · [li-qi-lin/USTC-Course-Materials-Sharing](https://github.com/li-qi-lin/USTC-Course-Materials-Sharing) · [EpiHio/USTC_Automation](https://github.com/EpiHio/USTC_Automation) · [Mr-Philo/USTC_EEIS_Courses](https://github.com/Mr-Philo/USTC_EEIS_Courses) |

完整版权归属与侵删渠道见 [NOTICE.md](NOTICE.md)。

<img alt="06" src=".github/assets/route-06.svg" width="100%" />

## 寻找 Contributor · 加入共建

目标是覆盖中科大尽可能多的本科核心课程（大物、数理方法、计科、电子信息与各院专业课）。单人维护覆盖全校非常吃力，**欢迎所有中科大同学与校友加入共建**：

- 认领一门你熟悉的课程，哪怕先补录 1 套结构化真题
- 刷题顺手提 [勘误 Issue](.github/ISSUE_TEMPLATE/errata.yml) 或 PR（详见 [CONTRIBUTING.md](CONTRIBUTING.md)）
- 帮忙核对低置信题、重绘清晰 SVG/WebP 题图，或基于本库构建刷题/Anki/组卷工具

<img alt="07" src=".github/assets/route-07.svg" width="100%" />

## 联系方式

- **GitHub**：[@DDNdles](https://github.com/DDNdles) · [Issues](https://github.com/DDNdles/USTC-Question-Bank/issues)
- **USTC GitLab 镜像**：[git.ustc.edu.cn/zzl_stella05/USTC-Question-Bank](https://git.ustc.edu.cn/zzl_stella05/USTC-Question-Bank)（校内/国内免梯子直连，自动同步）
- **中科大邮箱**：[zzl_stella05@mail.ustc.edu.cn](mailto:zzl_stella05@mail.ustc.edu.cn)
