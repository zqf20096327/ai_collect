<div align="center">

<a href="https://ml4sci.com/en/">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/en/banner-dark.webp">
    <img src=".github/assets/en/banner-light.webp" alt="Machine Learning for Science: an interactive roadmap for researchers who bring machine learning into science" width="100%">
  </picture>
</a>

**English** | [한국어](README.ko.md)

<p>
  <a href="https://ml4sci.com/en/"><img alt="Read online at ml4sci.com" src="https://img.shields.io/badge/read%20online-ml4sci.com-4f46e5?logo=bookstack&logoColor=white"></a>
  <img alt="219 chapters" src="https://img.shields.io/badge/chapters-219-0284c7">
  <img alt="1,358 quiz questions" src="https://img.shields.io/badge/quiz%20questions-1%2C358-7c3aed">
  <img alt="261 graded exercises" src="https://img.shields.io/badge/graded%20exercises-261-059669?logo=python&logoColor=white">
  <br>
  <img alt="Runs in your browser" src="https://img.shields.io/badge/runs%20in-your%20browser-0f766e?logo=webassembly&logoColor=white">
  <img alt="No sign-up" src="https://img.shields.io/badge/sign--up-not%20needed-d97706">
  <img alt="Languages: English and Korean" src="https://img.shields.io/badge/languages-English%20%7C%20%ED%95%9C%EA%B5%AD%EC%96%B4-64748b">
  <img alt="Version 1.0" src="https://img.shields.io/badge/version-1.0-334155">
  <a href="https://github.com/pjmbatman/ml4sci/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/pjmbatman/ml4sci?style=social"></a>
</p>

<p>
  <a href="https://ml4sci.com/en/"><b>Start learning</b></a> ·
  <a href="#-the-learning-loop">Learning loop</a> ·
  <a href="#-features">Features</a> ·
  <a href="#-curriculum">Curriculum</a> ·
  <a href="#-faq">FAQ</a> ·
  <a href="https://github.com/pjmbatman/ml4sci/issues/new/choose">Feedback</a>
</p>

</div>

**Machine Learning for Science** ([ml4sci.com](https://ml4sci.com/en/)) is an interactive digital book for **scientists and engineers** who want to bring machine learning into their research, and for **AI researchers** who want to work on real scientific problems. You read, move interactive figures, write Python and get it graded, all in your browser. There is nothing to install and no account to create.

<p align="center">
  <a href="https://ml4sci.com/en/"><img src=".github/assets/en/demo.gif" alt="A short demo: a lesson with a quiz, an interactive figure, grading code in the browser and the 3D library" width="100%"></a>
</p>

> [!NOTE]
> The book is available in **English** at [ml4sci.com/en](https://ml4sci.com/en/) and in **Korean** at [ml4sci.com](https://ml4sci.com).

## 🔁 The learning loop

Every chapter is built around the same loop. You read an idea, try it with your hands, write the code yourself and check that you really understood it.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/en/loop-dark.webp">
    <img src=".github/assets/en/loop-light.webp" alt="The learning loop: 1 Read a lesson, 2 Try an interactive figure, 3 Code and grade an exercise in the browser, 4 Check yourself with quizzes that explain each wrong answer" width="100%">
  </picture>
</p>

| Step | What happens | In the book |
|---|---|---|
| **1&nbsp;·&nbsp;Read** | Lessons with math, figures and an outline that tracks your place. | `Learning objectives → Concepts → Lab → Failure cases → Pass criteria` |
| **2&nbsp;·&nbsp;Try** | Sliders and live plots let you test an idea before you read the proof. | Interactive figures throughout the text |
| **3&nbsp;·&nbsp;Code** | Write Python in a built-in editor, press *Grade* and see each test pass or fail. | 261 exercises, run with [Pyodide](https://pyodide.org) |
| **4&nbsp;·&nbsp;Check** | Concept quizzes explain the misconception behind every wrong answer, and missed questions come back for review. | 1,358 questions and a review queue |

## ✨ Features

<p align="center">
  <img src=".github/assets/en/features.webp" alt="Feature cards: Library, Lessons, Figures, Grading, Quizzes, Review and Terminal" width="100%">
</p>

| | |
|---|---|
| 🧭 **A roadmap, not a pile of chapters** | 219 chapters in 33 parts and 12 tracks, arranged in 7 layers. Each chapter declares what it builds on, so you always know what to read next. |
| 🐍 **Python in the browser** | Code cells run in place with Pyodide (NumPy, SciPy, pandas, matplotlib, scikit-learn). PyTorch and GPU examples are shown read-only with a copy button; run them on your own machine with each chapter's downloadable lab files. |
| ✅ **Auto-graded exercises** | A built-in code editor with *Run* and *Grade* buttons and per-test results. Each chapter's lab files also download as a `.zip` to run locally. |
| 🧠 **Quizzes with feedback** | Every wrong answer explains the misconception behind it, and missed questions go to a review queue. |
| 📚 **A 3D library** | Browse the 33 books as a fan you can drag and turn, grouped by field, with your progress on every book. |
| 🖥️ **A learning desktop** | Lessons, review, notes, docs, a code editor, a terminal and a file browser open as windows side by side. A dashboard shows your progress and today's tasks. |
| 🔒 **Private by design** | No login. Progress stays in your browser, and you can export it to a file and import it again. |

## 🧭 Curriculum

Twelve tracks are arranged in seven layers. A track builds only on tracks in the same layer or a lower one.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/en/curriculum-dark.webp">
    <img src=".github/assets/en/curriculum-light.webp" alt="Curriculum map: seven layers from L0 Entry to L6 Integration, with twelve tracks and their part and chapter counts" width="100%">
  </picture>
</p>

<details>
<summary><b>The core question of each track</b></summary>
<br>

| Layer | Track | Core question |
|---|---|---|
| **L0 Entry** | Orientation | What is AI research, and what does the AI-for-science landscape look like? |
| **L1 Foundations** | Research Infrastructure | Where does code run, and in what environment? |
| | Research Software Engineering | How do equations and ideas become correct, maintainable code? |
| | Mathematical Foundations | In what spaces, and through what computations, do models learn? |
| | Probabilistic and Statistical Inference | What can we infer from uncertain data, and how confident should we be? |
| **L2 Core** | Machine Learning Core | How do we build and evaluate predictive models we can trust? |
| **L3 Extension** | Advanced Machine Learning | How do we generate distributions, learn decisions, and know when to trust a prediction? |
| | Machine Learning Systems | How do we track, reproduce and scale experiments? |
| **L4 Methods** | Research Methodology | What makes a good research question, and how do we validate and communicate a claim? |
| | Scientific Machine Learning | How do we combine physical laws, simulations and experiments with learning? |
| **L5 Applications** | Domain Applications | Physics and engineering simulation · Earth and climate · Chemistry and materials · Life sciences · Energy and batteries |
| **L6 Integration** | Capstone Projects | Can you turn what you learned into a research output you can publish? |

</details>

## 🚀 Getting started

1. Open **[ml4sci.com/en](https://ml4sci.com/en/)** (English) or **[ml4sci.com](https://ml4sci.com)** (Korean) in a desktop browser. A phone layout is also available. Switch languages any time with the button on the login screen or the top bar.
2. Enter a display name, or continue as **Guest**. The name stays in your browser and is not an account.
3. On your first visit, a short tour shows you around the desktop. You can replay it any time from the user menu (*Getting-started tour*), and the dashboard on the right always shows where to continue.

## 📈 Status

**Version 1.0 is live** in Korean and English. All 219 chapters, 1,358 quiz questions and 261 auto-graded exercises are online in both languages. The book keeps improving: chapters are reviewed and revised continuously, and reported errors are fixed in place.

## ❓ FAQ

<details>
<summary><strong>Who is this book for, and what background do I need?</strong></summary>
<br>
It is for scientists and engineers who want to use machine learning in their research, for AI researchers who want to work on scientific problems, and for undergraduate and graduate students starting out. Upper-undergraduate math and some programming experience make it comfortable to follow. Gaps are fine: the math foundations, Python and the working environment (servers, Git) are all covered in the book.
</details>

<details>
<summary><strong>Where should I start?</strong></summary>
<br>
Take the <a href="https://ml4sci.com/en/orientation/self-assessment/">self-assessment in 0.4</a> to see where you stand, then pick a reading order for your background in <a href="https://ml4sci.com/en/orientation/learning-paths/">0.3 Learning Paths</a>. It describes different routes for scientists, AI researchers, beginners and people already doing research. Every chapter lists what to read first, and the dashboard shows where to continue.
</details>

<details>
<summary><strong>How long does it take?</strong></summary>
<br>
It depends a lot on your background and how much time you spend. As planning ranges, 0.3 suggests one to two months to a first pipeline and 12 to 24 months to a paper draft from independent research. Measure progress by the output you have at each stage rather than by time. You don't have to read everything either; reading only the chapters you need works too.
</details>

<details>
<summary><strong>Do I need a GPU or a development setup?</strong></summary>
<br>
Mostly not. Code in the text and the exercises run in your browser with Pyodide. Examples that need PyTorch or a GPU come with each chapter's lab files (<code>.zip</code>) to run on your own machine or a lab server. The bundle includes <code>pyproject.toml</code> and <code>uv.lock</code>, so <code>uv</code> recreates the same environment.
</details>

<details>
<summary><strong>The quiz answers and solutions are visible. Is that a problem?</strong></summary>
<br>
No. Quizzes and exercises are designed as learning tools, not exams. Each wrong answer explains the misconception behind it, and missed questions come back in your review list. The real test of a chapter is making the output described in its pass criteria, not picking the right answer.
</details>

<details>
<summary><strong>Is it free? Do I need an account?</strong></summary>
<br>
It is free, and there are no accounts. You can read the whole book, run the code and take the quizzes and exercises without paying or signing up.
</details>

<details>
<summary><strong>Where is my progress stored? Can I continue on another device?</strong></summary>
<br>
Only in your browser's local storage. Nothing is sent to a server, and there are no analytics or cookies. To continue on another device, export a progress file from the settings in <em>My PC</em> and import it there. The English and Korean editions share the same progress, so switching languages keeps your place.
</details>

<details>
<summary><strong>Does it work on a phone?</strong></summary>
<br>
Yes, there is a phone layout. For the code editor and side-by-side windows, a desktop browser is much more comfortable.
</details>

<details>
<summary><strong>Can I use it in a course or a study group?</strong></summary>
<br>
Yes. Share chapter links with your students, and each student's progress and quiz history build up in their own browser. <a href="https://ml4sci.com/en/orientation/study-guide/">0.5 Using This Roadmap for Study Groups and Courses</a> explains how to run one. In slides, explain in your own words and quote the text briefly with a citation. Ask for permission at <a href="mailto:support@ml4sci.com">support@ml4sci.com</a> before redistributing whole chapters, figures or quizzes.
</details>

<details>
<summary><strong>I found an error.</strong></summary>
<br>
Please <a href="https://github.com/pjmbatman/ml4sci/issues/new/choose">open an issue</a> with the <em>Content error</em> form. Factual errors, wrong quiz answers, broken exercises and confusing explanations are all welcome, and confirmed errors are fixed in place.
</details>

<details>
<summary><strong>Is the source code or manuscript available?</strong></summary>
<br>
No. This repository introduces the project and collects feedback. The manuscript and the site code are developed privately.
</details>

## 💬 Feedback and support

- ⭐ **Star this repository** so more scientists and engineers can find the book.
- 🐞 **Report an error** or a confusing explanation: [open an issue](https://github.com/pjmbatman/ml4sci/issues/new/choose). English and Korean are both welcome.
- 💡 **Suggest** a topic, a chapter or a feature the site should have.
- ✉️ **Email** [support@ml4sci.com](mailto:support@ml4sci.com) for permission requests, course use or anything you'd rather not post publicly.
- 🔗 **Share** [ml4sci.com/en](https://ml4sci.com/en/) or [ml4sci.com](https://ml4sci.com) with your lab, study group or class.

## 📜 License

© 2026 pjmbatman. All rights reserved.

The book is free to read at [ml4sci.com](https://ml4sci.com). Free access does not grant permission to copy, modify, redistribute or use the content to train machine-learning models. For permission requests, email [support@ml4sci.com](mailto:support@ml4sci.com). See [LICENSE](LICENSE).

Third-party software and fonts used by the site are listed at <https://ml4sci.com/third-party-notices.txt>.

<br>

<div align="center">
  <a href="https://ml4sci.com/en/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset=".github/assets/logo-dark.svg">
      <img src=".github/assets/logo.svg" alt="Machine Learning for Science logo" width="56">
    </picture>
  </a>
  <br>
  <sub><a href="https://ml4sci.com/en/">Read online</a> · <a href="README.ko.md">한국어</a> · <a href="https://github.com/pjmbatman/ml4sci/issues/new/choose">Feedback</a> · <a href="mailto:support@ml4sci.com">support@ml4sci.com</a></sub>
</div>
