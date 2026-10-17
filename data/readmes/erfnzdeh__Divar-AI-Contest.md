<div align="center">

# 🏆 Divar AI Contest

**CTF for AI agents — the 🥇 1st & 🥈 2nd place solutions, plus a live war-room history**

<sub>An 8-hour sprint at [Divar's AI Contest](https://quera.org/events/divar-0404) on Quera, where LLM agents raced to capture the flag.</sub>

🗓 July 10, 2025 (19 Tir 1404) · ⏱ ~8 hours · 👥 2,874 registered · 🎯 11 problems · 💰 143M Toman prize pool

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![LLM](https://img.shields.io/badge/LLM-GPT--4.1--mini-412991?logo=openai&logoColor=white)
![Gateway](https://img.shields.io/badge/API-Metis_AI-orange)
![Style](https://img.shields.io/badge/format-Capture_the_Flag-red)

<img src="docs/assets/scoreboard.jpg" alt="Quera live scoreboard — Pourya Erfanzadeh at rank 2 of 2,874" width="100%">

<sub>📊 The live scoreboard with ~3 hours still on the clock — sitting at <b>#2 of 2,874</b>. 😎 (That's Danial down at #6 — he'd claw his way to a final 🥈 #2.)</sub>

</div>

---

## 🎪 The Contest

[Divar](https://divar.ir) — Iran's largest classifieds platform (37M+ monthly users) — ran a one-day, individual AI contest on Quera, testing **practical LLM engineering**: prompt design, output evaluation, tool routing, and debugging LLM-based systems.

The twist: you don't submit *answers* — you submit an **agent**. Each problem requires a `solution.py` exposing a `DivarContest` class whose `capture_the_flag(question)` method receives the task as raw text and must autonomously figure out the rest: find the URL, download the file, decode the cipher, train the model, fix the code — and return the flag. LLM access was provided through the [Metis AI](https://metisai.ir) OpenAI-compatible gateway.

```python
class DivarContest:
    def __init__(self, api_token):
        self.client = OpenAI(api_key=api_token, base_url="https://api.metisai.ir/openai/v1")

    def capture_the_flag(self, question: str) -> str:
        # 🤖 your agent's 8 hours of fame
        ...
```

**The stakes** — a 143,000,000 Toman prize pool split across the top 10 in a *reverse-Fibonacci* payout (55M · 34M · 21M · 13M · 8M · 5M · 3M · 2M · 1M · 1M — yes, those are Fibonacci numbers 🌀), swag for ranks 11–1000, and the top ~100 scorers fast-tracked to interviews for Divar's **AI Software Engineer** role.

Curious how the contest itself was engineered? The design story — agent CTF format, mirrored datasets, token budgets — lives in [docs/CONTEST_DESIGN.md](docs/CONTEST_DESIGN.md).

## 🧩 The Problems

Cleaned-up, per-problem solutions live right here in the `P*` folders:

| # | Problem | Persian | The Challenge | The Agent's Play |
|---|---------|---------|---------------|------------------|
| P1 | **The Cryptic Photo** | عکس گنگ | An image hides Caesar-encrypted text | GPT-4.1-mini vision OCR → brute-force Caesar shifts → flag |
| P2 | **Monkey Wrench** | آچار فرانسه | Mixed bag: logic puzzles *or* live web pages — agent must pick its tool | URL-sniffing router: few-shot chain-of-thought for riddles, `requests` + BeautifulSoup for the web |
| P3 | **Two John Wicks** | دو جان ویک | Concurrency shoot-out: threads vs. processes racing on shared counters | Pure Python — `threading.Lock` vs. `multiprocessing.Value`, no LLM needed 🔫🔫 |
| P4 | **Sound, Image, Action** | صدا، تصویر، حرکت | One question, four modalities: Excel, audio, PDF, image | Modality router → LLM writes pandas code and the agent `exec`s it, transcription, PDF extraction, vision |
| P6 | **Hodgepodge Stew** | آش شله قلمکار | Train a model on a CSV and predict hotel availability for given IDs | Full scikit-learn pipeline: imputation + scaling + one-hot → LogisticRegression |
| P7 | **Homemade Cursor** | کرسر خانگی | A zipped codebase with a planted bug — fix it and run it | A mini coding agent: unzip → LLM locates & patches the bug → execute → verify output |
| P8 | **The Secret Keeper** | رازنگهدار | A poem guards a password | Acrostic decode (first letter of each line) → LLM spell-check → flag |

<sub>The grand finale «دیوار ایجنت» (*Divar Agent*) and every other problem above is also solved in [`first_place/`](first_place) — the 🥇 winner's submissions.</sub>

> [!NOTE]
> **«سوناتا» (*Sonata*) is unsolved.** None of the three contestants in this repo submitted a solution for it, and the problem statement isn't archived here either. If you have it, PRs welcome. 🎵

## ⚔️ The War Room — this repo *is* the timeline

This repository was the live workspace **during the contest**. The commit history on `main` and the `test-*` branches is a real-time log of an 8-hour sprint — scoreboard feedback baked straight into the commit messages:

```text
16:39  init: Add initial project files
16:59  [TEST 1 PASSED]   OpenAI integration works
17:42  [TEST 3 75%]      web scraping... almost
17:48  [TEST 3 PASSED]   multi-step extraction ✓
17:54  [TEST 4 PASSED]   concurrency ✓
18:54  [TEST 5 FAILED]   Excel/audio/PDF/image — pain begins
19:05  [TEST 6 ATTEMPT]  digital escape room, HMAC flags
19:18  [TEST 5 STILL 25%] 😤
19:31  → pivot: log-analysis & auto bug-fixing agent
20:41  → pivot: EasyOCR... no wait, GPT-4 Vision
21:15  final push: LLM-first URL extraction
```

Every one of those battle branches has since been **merged into `main`** — run `git log --graph --all` and the whole contest replays in front of you. The frozen tips are still browsable:

| Branch | What froze there |
|--------|------------------|
| [`test-divar-agent`](../../tree/test-divar-agent) | First working agent (Test 1) |
| [`test-5`](../../tree/test-5) | The multimodal battle: Excel + audio + PDF + image validation |
| [`test-cursor`](../../tree/test-cursor) | The "homemade Cursor" — downloads a codebase, finds the bug, fixes it, runs it |
| [`test-cypher`](../../tree/test-cypher) | Vision OCR + Caesar decryption, EasyOCR → GPT-4V migration |
| [`Danial`](../../tree/Danial) | 📦 Post-contest: all seven solutions, cleaned and organized per problem |

The [`war_room/`](war_room) folder preserves the final mid-contest state of the live workspace — frozen at the digital escape-room solver (4 puzzle rooms → 3-digit key → HMAC-SHA256 flag), test harness and sample data included.

## 🗂 Repo Layout

```text
├── P1_Akse_Gong/            🖼  vision OCR + Caesar cipher
├── P2_Achar_France/         🔧  tool-routing: logic vs. web
├── P3_Two_John_Wicks/       🔫  threads vs. processes
├── P4_Seda_Tasvir_Harekat/  🎬  Excel · audio · PDF · image
├── P6_Ash_Shole_Qalamkar/   🍲  scikit-learn pipeline
├── P7_Cursor_Khanegi/       🛠  self-debugging code agent
├── P8_Raznegahdar/          🤫  acrostic poem decoder
├── first_place/             🥇  the winner's submissions (LangGraph ReAct agents)
└── war_room/                ⚔️  mid-contest snapshot (escape-room solver)
```

Three separate contestants' work lives here: the `P*` folders are Danial's (🥈 2nd), [`first_place/`](first_place) is Ali Salesi's (🥇 1st), and [`war_room/`](war_room) plus the branch history is the repo owner's live run.

## 🚀 Running a Solution

```bash
cd P1_Akse_Gong        # or any other problem
pip install -r python_requirements.txt
```

```python
from solution import DivarContest

agent = DivarContest(api_token="YOUR_METIS_API_KEY")
print(agent.capture_the_flag("<the challenge text, URL included>"))
```

You'll need a [Metis AI](https://metisai.ir) API key (OpenAI-compatible gateway used by the contest). In [`war_room/`](war_room), `test_local.py` reads it from a `METIS_API_KEY` env var or `.env` file.

## 🥷 Contestants

This was a solo contest — the work of three separate competitors ended up in this repo:

- **[Ali Salesi](https://github.com/AlisaLC)** — finished 🥇 **1st overall** — his submissions live in [`first_place/`](first_place), built on LangGraph ReAct agents
- **[Danial Parnian](https://github.com/Danial-par)** — finished 🥈 **2nd overall** — his polished solution set is in the `P*` folders (via the `Danial` branch)
- **[Pourya Erfanzadeh](https://github.com/erfnzdeh)** (repo owner) — the live war-room commits on `main` & `test-*`, peaking at **#2 on the mid-contest scoreboard** ☝️

---

<div align="center">
<sub>⚡ Built in one afternoon, under contest pressure, with LLMs fixing code while humans fixed prompts.</sub>
</div>
