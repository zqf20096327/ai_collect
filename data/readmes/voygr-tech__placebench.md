# PlaceBench

How well do AI assistants answer everyday questions about real places? PlaceBench has 150 questions in 121 cities. Most are set on a day and a time, and each has an answer key checked against the place's own sources.

We asked six AI assistants every question. Their scores range from 49 to 92 out of 100.

Read the [write-up on our blog](https://voygr.tech/placebench).

![PlaceBench: score against answer time](assets/score-vs-time.png)

## Results (November 2026)

| Assistant | Score | 95% CI | Fully right | Right 3 of 3 | Wrong | Median time | 95th percentile |
|---|---:|---:|---:|---:|---:|---:|---:|
| Dots | **92** | 89–96 | 87% | 17/20 | 0 | 57 s | 157 s |
| Muse | 83 | 76–90 | 78% | 12/20 | 6 | 81 s | 339 s |
| Claude Duet | 79 | 71–86 | 71% | 13/20 | 6 | 43 s | 135 s |
| Instinct | 76 | 67–84 | 75% | 5/20 | 12 | 64 s | 206 s |
| Grok Bot | 73 | 64–82 | 71% | 8/20 | 12 | 29 s* | 582 s* |
| Ask Maps (Google Maps) | 49 | 36–61 | 61% | 12/20 | 30 | 8 s | 15 s |

- **Score**: each first answer earns 1 point if it's right, 0.75 for a small error, 0.25 if it's partly right, 0 for no answer and −1 if it's wrong. The score is the average, out of 100.
- **Fully right**: the share of first answers graded right.
- **Right 3 of 3**: of 20 questions asked three times, the number answered right every time.
- **Wrong**: answers our sources contradict, out of 150.
- **Time**: from sending the question to the end of the answer.
- \*Grok Bot's times come from 53 timed answers.

Dots is ahead of every other assistant at 95% confidence. Muse, Claude Duet, Instinct and Grok Bot are within each other's margin of error. All five are ahead of Ask Maps.

![PlaceBench: right on the first try, and right all three times](assets/first-vs-three.png)

## What's in this repository

| File | What it holds |
|---|---|
| `data/questions.jsonl` | The 150 questions: id, kind, city, country, language, stated day and time, the question as asked, and an English translation where it was asked in another language |
| `data/keys.jsonl` | One answer key per question: the answer, what counts as right, what counts as wrong, and the sources |
| `data/grades.jsonl` | Every grade: question, assistant, try (1 to 3) and grade. 900 first answers, plus the 240 repeats |
| `METHODOLOGY.md` | How the questions, keys, grades and scores were made |
| `assets/` | The charts above |
| `LICENSE` | CC BY 4.0 |

A question and its key, shortened:

```json
{"id": "p_70419", "kind": "Finding a place nearby", "city": "Stockholm", "country": "Sweden", "language": "en",
 "stated_time": "Mon 16 Nov 2026 02:00",
 "question": "I'll be near Slussen at 2 am on the night of Sunday 15 to Monday 16 November. Will anywhere around there still be serving hot food at that hour?",
 "asked_three_times": true}
```

```json
{"id": "p_70419",
 "answer": "Yes. MAX vid Medborgarplatsen, Götgatan 41, is open until 03:00 that night (MAX's own page lists Sunday 15 Nov as 09:00-03:00). It is about 570 m, an 8-minute walk up Götgatan from Slussen. …",
 "counts_as_right": "Must say yes and name at least one place within about 1 km / 15 min walk of Slussen that serves hot food at 02:00 on Monday 16 Nov, open then per its own page or listing. …",
 "counts_as_wrong": "Saying nothing will be open. Giving as serving at 02:00: Kvarnen, Tjärhovsgatan 4 (own site: Sunday 11:30-23:00) …",
 "sources": ["https://www.max.se/hitta-max/restauranger/", "https://7-eleven.se/hitta-butik/", "…"]}
```

## What we count as the truth

Every key cites its sources. We take facts in this order:

1. **The place's own website**, booking pages and notices.
2. **The operator's timetable** for trains, metros and buses.
3. **The place's Google Maps listing**, for hours and status where the place has no page of its own.
4. **Other public sources**: OpenStreetMap, official registers and licence notices, and dated press.

**Routes and travel times.** Walking and driving times come from OpenStreetMap routing (OSRM). Public transport comes from the operator's timetable, and from Google Maps transit directions for a door-to-door time.

Where sources disagree, the place's own page wins. A place counts as closed only when a public source shows it: a closure notice, the operator's list, a licence suspension, a dated press report or Google's "permanently closed".

## How the questions were built

The 150 questions cover five kinds of request:

| Kind | Questions |
|---|---:|
| Finding a place nearby | 54 |
| Place details | 41 |
| Planning a route or a time | 33 |
| Booking and contact details | 11 |
| Sharing with friends | 11 |

The booking and contact questions ask for a phone number, an email or how to buy tickets. We didn't ask any assistant to call, book or buy anything.

46 questions are written in the city's own language, as a local would type them. Most name a day and a time between 15 and 21 November 2026, so every answer can be checked against what was true then.

Every key was drafted twice, independently, and disagreements were settled against the sources.

## Grading

Claude Opus 5.5 grades each first answer against its key, and we hand-verified places to calibrate it. As a cross-check, OpenAI's gpt-6.1-sol regraded 60 answers without seeing the grades and made the same right-or-not call on 48. A grade of wrong needs a fact that a source contradicts. A claim nobody can check either way is not wrong.

Every grade is in `data/grades.jsonl`, so you can recompute the scores; METHODOLOGY.md has a short script. The full method, including how intervals are computed and how closed places affect a grade, is in [METHODOLOGY.md](METHODOLOGY.md).

## Limitations

- This is one run, in November 2026. Assistants change.
- The keys hold for the week the questions name. Hours and timetables move after that.
- 20 repeated questions is a small sample. Instinct keeps one continuous conversation and Dots keeps memory between chats, so their repeats can draw on earlier answers.
- 27 keys cite Google Maps, and one of them (pharmacy hours in Hpa-An) rests on Google listings alone. Without those 27 questions, Dots is still first and Ask Maps still last. [METHODOLOGY.md](METHODOLOGY.md#answer-keys-and-ground-truth) gives every assistant's score with and without them.
- An LLM grades the answers. We calibrated and cross-checked it, but its grades are not human grades. The judge is a Claude model, and one of the assistants, Claude Duet, is built on Claude.

## Citation

```bibtex
@misc{placebench2026,
  title  = {PlaceBench: Evaluating AI Assistants on Everyday, Time-Bound Questions about Real Places},
  author = {{VOYGR}},
  year   = {2026},
  month  = nov,
  url    = {https://github.com/voygr-tech/placebench}
}
```

## Licence

Questions, answer keys and sources: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

PlaceBench is made by [VOYGR](https://voygr.tech). We build tools for AI agents to work with local businesses and places. To have your assistant or agent tested on the same questions, [get in touch](https://voygr.tech/#contacts).
