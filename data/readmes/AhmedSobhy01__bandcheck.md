# BandCheck

An IELTS Writing marker. Upload a screenshot of the question, paste your answer, and get band scores, marked
mistakes and a plan for the next band.

Supports Task 1 Academic, Task 1 General Training and Task 2.

![Results page](docs/screenshots/results-overview.png)

## Features

### Band scores

- A band for each criterion: Task Response/Achievement, Coherence and Cohesion, Lexical Resource, Grammatical
  Range and Accuracy
- Scored against the public IELTS band descriptors
- Overall band rounded the IELTS way
- One band off the task criterion for answers under 150 / 250 words

### Marked script

- Every mistake highlighted in your text
- Six categories: sentence structure, word form, word choice, mechanics, grammar, vocabulary
- Correction and explanation for each mistake

![Marked script](docs/screenshots/results-marked-script.png)

### Language and organisation

- Error-free sentences and sentence types
- Repeated words, weak verbs, collocations, idioms
- Linking words and paragraph-by-paragraph comments

<table>
  <tr>
    <td width="50%"><img src="docs/screenshots/results-language.png" alt="Language tab"></td>
    <td width="50%"><img src="docs/screenshots/results-organisation.png" alt="Organisation tab"></td>
  </tr>
</table>

### Next band

- Steps to reach the next band, ordered by impact
- Before and after examples from your own answer
- Optional rewrite of the whole answer at the next band

![Next band tab](docs/screenshots/results-next-band.png)

### Progress

- Every answer and its feedback is saved
- Band over time and average per criterion
- Recurring mistakes with examples from your answers
- A study plan built from all your answers

![Progress page](docs/screenshots/progress.png)

### Also

- 20 / 40 minute exam timer
- Light and dark themes
- Mobile layout
- Save as PDF

<table>
  <tr>
    <td width="72%"><img src="docs/screenshots/home-dark.png" alt="Dark mode"></td>
    <td width="28%"><img src="docs/screenshots/mobile.png" alt="Mobile"></td>
  </tr>
</table>

## Getting started

Requires Node.js 20.9+ and an [OpenAI API key](https://platform.openai.com/api-keys).

```bash
npm install
cp .env.example .env.local   # add your OpenAI API key
npm run dev                  # http://localhost:3000
```

Production: `npm run build && npm start`

## Configuration

`.env.local`:

| Variable                  | Default        | Description                                                                |
| ------------------------- | -------------- | -------------------------------------------------------------------------- |
| `OPENAI_API_KEY`          |                | Required. Server-side only.                                                |
| `OPENAI_MODEL`            | `gpt-5.4-mini` | Needs vision and structured outputs. `gpt-5.5` is stricter but costs more. |
| `OPENAI_REASONING_EFFORT` | `low`          | `minimal`, `low`, `medium` or `high` (GPT-5 models).                       |
| `DATA_DIR`                | `./data`       | Where answers and feedback are saved, one JSON file per answer.            |

## How it works

- Marking runs as three parallel requests: band scores, language check, organisation. Results appear as each one
  finishes.
- Word, sentence and paragraph counts are computed in code, not by the model.
- Each mistake gets a rule name (e.g. "Subject-verb agreement"), used to find recurring mistakes across answers.

## Storage

Answers are saved as files in `DATA_DIR`. This needs a persistent disk. For serverless hosts like Vercel, replace
the functions in `lib/server/store.ts` with a database.

There are no user accounts. Anyone with access to the app sees all saved answers.

## Disclaimer

Bands are estimates for practice. Not affiliated with IELTS, the British Council, IDP or Cambridge University
Press & Assessment.

## License

[MIT](LICENSE)
