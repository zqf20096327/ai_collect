# GPT Guesses Between 1 and 100

<img width="1372" height="731" alt="Exmergo Viz - I asked GPT to pick a random number between 1 and 100 (sample 10k)" src="https://github.com/user-attachments/assets/0d51eb37-fdd9-4f8b-87c8-db44c551818e" />


An interesting thing about humans is that they are not good random number generators.  
If you ask a person to "pick a random number between 1 and 100", they are
remarkably predictable. Answers cluster on 37 and 73, on "messy" numbers, and
on memes like 42 and 69, while round numbers are quietly avoided. A true random
generator would instead produce a flat, **uniform** distribution.

**This project asks `gpt-4.1` the same question 10,000 times** and
characterizes the distribution it produces, measured against a uniform baseline.
Does an LLM, which is trained on human text, behave like a fair die, or does it inherit
the lumpy human pattern?

Full design and methodology: [`docs/LLM Random Bias Experiment SDD.md`](docs/LLM%20Random%20Bias%20Experiment%20SDD.md).

## Inspiration

This experiment is an LLM-focused follow-up to two well-known explorations of *human* number-picking bias.

- r/dataisbeautiful — ["[OC] I asked 100 people to pick a number between 1 and 100"](https://www.reddit.com/r/dataisbeautiful/comments/iiafkd/oc_i_asked_100_people_to_pick_a_number_between/)
- Veritasium — [Why is this number everywhere?](https://www.youtube.com/watch?v=d6iQrh2TK98)

## Methodology

Full experimental design is in the
[SDD](docs/LLM%20Random%20Bias%20Experiment%20SDD.md); the essentials:

- **Model.** `gpt-4.1` (OpenAI), called via the Responses API. It is a
  *non-reasoning* model. It emits a direct answer rather than deliberating; what we're measuring is
  its raw output distribution, not a reasoning strategy. The exact
  model string is recorded in every raw-CSV row (`Model` column) and in
  `data/raw/run_metadata.json`, so the dataset is self-describing.
- **Sample size.** N = 10,000 independent calls — enough for a chi-square
  goodness-of-fit test and per-number proportions stable to ~±0.5 pp.
- **Sampling.** `temperature = 1.0`, so the model exercises its full sampling
  distribution. This is the experiment: at low temperature it would just repeat
  one number.
- **Prompt.** A fixed system prompt instructs the model to output only one
  integer between 1 and 100; the user prompt requests the number and carries a
  unique `uuid4`. (The UUID is request-tracing hygiene, *not* cache-busting — at
  temperature 1.0 every call should sample independently regardless.)
- **Baseline.** The result is compared against a **uniform** distribution — what
  a fair generator would produce — not against human data (see *Assumptions*).
- **Pipeline.** Four stages — `collect → clean → transform → stats`, detailed
  below. Cleaning validates every answer is an integer in [1, 100] and reports
  the rejection rate.

### Assumptions & Limitations

This is an illustrative probe, not a definitive study. Key caveats — see the
[SDD's Limitations section](docs/LLM%20Random%20Bias%20Experiment%20SDD.md) for
the formal treatment:

- **Single model.** Results describe `gpt-4.1` only and do not generalize to
  other models or providers.
- **"Randomness" is a sampling artifact.** The model is not a random number
  generator; it samples a learned token distribution. We characterize that
  distribution — we do not claim the model is *trying* to be random.
- **Prompt- and temperature-dependent.** A different prompt wording or sampling
  temperature could shift the distribution. Both are fixed and documented.
- **Not "ChatGPT the product."** This tests a model through the API at a fixed
  temperature — not the consumer ChatGPT app, which adds routing, tools, and a
  system prompt outside our control.

## Results

**gpt-4.1 is emphatically not a uniform random generator.** A chi-square
goodness-of-fit test against a uniform distribution (N = 10,000, df = 99) returns
**χ² = 15,604, p ≈ 0** — the deviation is so large it underflows any
significance threshold. Asked for a random number, the model produces a lumpy,
distinctly human-shaped distribution.

### It reproduced the classic human spikes

| Number | Picked vs. uniform chance | Human reputation |
| --- | --- | --- |
| 37 | **4.0×** | "the most random number" |
| 42 | **4.0×** | *Hitchhiker's Guide* meme |
| 73 | **3.4×** | the other well-known spike |

The five most-picked numbers overall — `47, 57, 72, 37, 42` — lean heavily on
numbers ending in 7 (three of the five), the same "number that feels random" pull seen in
humans.

### It avoids round numbers even harder than humans

**All multiples of 10, except for 10 itself, were picked exactly 0 times in 10,000 calls**.
10 was picked exactly once. Humans avoid round numbers — gpt-4.1 essentially refuses them.

### The exception: 69

One number breaks the human pattern. 69 is a meme number humans *over*-pick.
gpt-4.1 **under**-picks it (0.29× expected: ~29 occurrences against ~100). The
model inherited the "smart" meme (42) and not the crude one. Our hypothesis is that 
this is a product of safety guardrails during pre-training and post-training. 
It is the most interesting aspect in the dataset: the model's
bias is not a raw copy of human bias but a *moderated* version of it.

### Takeaway

The hypothesis holds. An LLM trained on human text, asked to be random,
reproduces human random-number bias: the pull toward 37 and 73, the meme spike
at 42, the aversion to round numbers — with one guardrail-likely exception. The
interactive [distribution chart](https://viz.exmergo.com/share/eea2a7b6-82d4-4333-8853-e909d9dabd49)
shows the full 1–100 shape.

*All figures from [`data/processed/stats_summary.csv`](data/processed/stats_summary.csv).*

## The pipeline

`collect → clean → transform → stats`. Each stage reads the previous stage's
committed CSV, so any stage can be re-run on its own.

| Stage | Module | Output |
| --- | --- | --- |
| Collect | `llm_random_bias.collect` | `data/raw/chatgpt_random_results.csv` |
| Clean | `llm_random_bias.clean` | `data/processed/chatgpt_random_clean.csv` |
| Transform | `llm_random_bias.transform` | `data/processed/distribution.csv` |
| Stats | `llm_random_bias.stats` | `data/processed/stats_summary.csv` |

## Setup

This project uses [uv](https://docs.astral.sh/uv/) for everything.

```sh
uv sync
```

## Path 1 — Analysis only (free, no API key)

The raw dataset is committed to this repo, so you can reproduce the entire
analysis without spending a cent:

```sh
uv run python -m llm_random_bias.clean
uv run python -m llm_random_bias.transform
uv run python -m llm_random_bias.stats
```

## Path 2 — Fresh data collection (needs an OpenAI API key)

```sh
cp .env.example .env          # then edit .env and add your OPENAI_API_KEY
uv run python -m llm_random_bias.collect
# then run clean / transform / stats as in Path 1
```

**Cost & runtime:** ~10,000 short calls to `gpt-4.1` cost roughly US$2 and
finish in a few minutes at the default concurrency. The collector refuses to
overwrite an existing raw CSV — delete it first to re-collect.

## Visualization

The distribution bar chart is built in **Exmergo Viz** (our AI dashboard agent) directly from
`data/processed/distribution.csv`. The fully interactive data viz can be viewed [here](https://viz.exmergo.com/share/eea2a7b6-82d4-4333-8853-e909d9dabd49).

## Development

```sh
uv run ruff check .
uv run ruff format .
uv run mypy src
uv run pytest
```

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

MIT — see [`LICENSE`](LICENSE).
