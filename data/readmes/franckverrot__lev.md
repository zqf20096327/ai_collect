# lev

lev's a clone of [kev](https://github.com/jaredpalmer/kev), Jared Palmer's Jev-style decision model, with the Qwen backbone replaced by LiquidAI's [LFM2.5-350M](https://huggingface.co/LiquidAI/LFM2.5-350M).  Mostly a prototype and a fun weekend experiment, though it was more bumpy than I planned...

Just like Jev, you give it one document / the state and a set of typed questions, and it returns a probability for every option of every question from a single forward pass.  This is not an LLM so it doesn't do any text generation.

![How one request goes through lev](docs/lev-architecture.png)

- Weights: [franckverrot/lev-350m](https://huggingface.co/franckverrot/lev-350m)
- Demo: [huggingface.co/spaces/franckverrot/lev](https://huggingface.co/spaces/franckverrot/lev)

The architecture follows Archer Hume's reconstruction of TypeSafe's Jev in [Jev's Architecture Unmasked](https://archerhume.com/posts/jevs-architecture-unmasked).  The API follows TypeSafe's [System One](https://docs.typesafe.ai/api) contract, so the `typesafe-sdk` works against a local lev server with a `base_url` change.  The data pipeline, the frozen evaluation suites, the experiment runner and the playground come from kev.

## Run it

Requires Python 3.12+, [uv](https://docs.astral.sh/uv/), and Node 20+ for the playground.  Developed on Apple Silicon.

```bash
git clone https://github.com/franckverrot/lev && cd lev
uv sync --extra serve
uv run --extra serve python -m lev.serve --run franckverrot/lev-350m --port 8009
```

The first start downloads the adapter (25 MB) and LFM2.5-350M (710 MB).  Then:

```bash
curl -s localhost:8009/v1/systemone -H 'content-type: application/json' -d '{
  "state": "Shoes arrived two weeks late and in the wrong size. Also I see two charges on my card.",
  "model": "lev-latest",
  "questions": {
    "department":  {"type": "choice", "instructions": "Which team should handle this?",
                    "criteria": {"returns": "Exchanges, refunds, wrong or damaged items",
                                 "shipping": "Delivery status, delays, lost packages",
                                 "billing": "Charges, invoices, payment problems"}},
    "escalate":    {"type": "noul",  "instructions": "Does this need urgent human attention?"},
    "frustration": {"type": "score", "instructions": "How frustrated is the customer?",
                    "criteria": ["Calm", "Frustrated", "Very angry"]}
  }}'
```

```json
{
  "model": "lev-latest",
  "answers": {
    "department":  { "type": "choice", "choice": "returns", "confidence": 0.48,
                     "probabilities": { "returns": 0.653, "shipping": 0.227, "billing": 0.12 } },
    "escalate":    { "type": "noul", "noul": 0.449 },
    "frustration": { "type": "score", "score": 1.35, "confidence": 0.8,
                     "legend": { "0": "Calm", "1": "Frustrated", "2": "Very angry" },
                     "probabilities": { "0": 0.022, "1": 0.605, "2": 0.373 } }
  },
  "usage": { "input_tokens": 108, "output_tokens": 160 },
  "latency_ms": 26.1
}
```

fp32 on an Apple M2 Max.

With the TypeSafe SDK:

```python
from typesafe_sdk import TypeSafeClient, Choice, Noul, Score

client = TypeSafeClient(api_key="local", base_url="http://127.0.0.1:8009", model="lev-latest")
r = client.system_one(
    state="I was charged twice. Please fix this ASAP.",
    questions={
        "billing": Noul(instructions="Is this ticket about billing?"),
        "tone": Choice(instructions="What is the customer's tone?", criteria={"calm": None, "frustrated": None, "angry": None}),
        "urgency": Score(instructions="How urgent is this ticket?", criteria=["can wait", "this week", "today"]),
    },
)
r.nouls["billing"].noul, r.choices["tone"].choice, r.scores["urgency"].score
```



### Playground and x-ray

```bash
cd playground && npm install && npm run dev -- -p 3001
```

[localhost:3001](http://localhost:3001) is kev's playground but a new [/xray](http://localhost:3001/xray) has been added in lev: it traces one request and shows:

- the packed token sequence
- the inputs of each short convolution
- the attention mask next to the measured attention weights
- the per-layer difference between a packed question and the same question run alone
- the effect of skipping each layer
- attention to the state with a sentence-removal check
- the pointer head
- LoRA update sizes

![lev x-ray](docs/xray.png)

## API

`POST /v1/systemone` takes a `state` (string, object or array), a `model` name and a map of `questions`.  Each question has a `type`, `instructions`, and `criteria`.


| Type     | Criteria                                          | Answer                                                            |
| -------- | ------------------------------------------------- | ----------------------------------------------------------------- |
| `noul`   | optional `{true, false}` descriptions             | `noul`: p(yes)                                                    |
| `choice` | `{option: description or null}`, 1 to 255 options | `choice`, `probabilities`, `confidence`                           |
| `score`  | list of 2 to 255 ordered levels                   | `score` (expected level), `legend`, `probabilities`, `confidence` |


Probabilities are served with the checkpoint's calibration temperature (`calibration.json` next to the weights; `GET /v1/models` reports it, `LEV_TEMPERATURE=1` sets it to 1).  Text from the caller is tokenized as plain text; delimiter tokens come only from the server.  Validation errors return `422`.

Other endpoints: `GET /v1/models`, `POST /v1/systemone/permute` (one Choice under N option orders), `POST /v1/systemone/separate` (each question in its own pass), `POST /v1/trace` (the x-ray data).

## Train it yourself!

```bash
# one-minute end-to-end check
uv run python -m lev.train --n_per_source 40 --accum 4 --out runs/smoke

# the released checkpoint: train, calibrate, score, run the isolation checks. About 45 minutes on an M2 Max.
uv run python -m lev.experiment --suite evals/v4/decision-v4 --plan experiments/v4-350m-subset.json \
    --out runs/v4-350m-subset --transfer evals/v4/transfer-v4

# serve it
uv run --extra serve python -m lev.serve --run runs/v4-350m-subset/00-trial-0/checkpoint --port 8009
```

## What changed from kev

kev keeps questions independent with a block-causal attention mask: a token reads the state and its own question.  On Qwen that covers everything, because attention is the only place tokens mix.  LFM2.5-350M has 16 layers (10 gated short convs, 6 attention.)

lev gives every token a `prev` pointer when it packs the sequence.  Inside the state and inside a question it points at the previous token.  The first token of every question points at the last state token.  The convolutions read their window along that chain so every question computes what it would compute alone with the state.

## Results


|                                                      | lev-350m | kev-0.6b | Jev    |
| ---------------------------------------------------- | -------- | -------- | ------ |
| parameters                                           | 361M     | 607M     | hosted |
| accuracy, in-distribution (`decision-v4`)            | 0.773    | 0.805    | 0.845  |
| accuracy, out-of-domain (`transfer-v4`)              | 0.546    | 0.598    | 0.857  |
| confidently wrong out of domain (p ≥ 0.9), as served | 0.8%     | 5.2%     | 3.7%   |
| request with 3 questions                             | 25 ms    | 46 ms    |        |
| 24 questions on one state                            | 110 ms   | 223 ms   |        |
| weights in memory                                    | 1.44 GB  | 2.43 GB  |        |
| training, seconds per record                         | 0.25     | 0.44     |        |


All done on a M2 Max 96GB.

## Credits

[kev](https://github.com/jaredpalmer/kev) by Jared Palmer: the design, the code this started from, the frozen suites and the Jev measurements.  [Archer Hume](https://archerhume.com/posts/jevs-architecture-unmasked) for the architecture reconstruction.  [TypeSafe](https://docs.typesafe.ai/api) for the API contract.  [Liquid AI](https://www.liquid.ai) for the backbone ([LFM2 technical report](https://arxiv.org/abs/2511.23404)).

## License

[Apache-2.0](LICENSE), same as kev.  LFM2.5-350M is distributed by Liquid AI under the LFM Open License v1.0.  Datasets carry their own licenses.