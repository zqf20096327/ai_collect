# Newt

Newt is a Swift package that answers multiple-choice, graded, and yes/no questions
about a piece of text with an on-device language model, and returns a probability for
each option.

Newt is named after Isaac Newton, similar to how TypeSafe named its model Jev after William
Stanley Jevons.

## Status

Newt picks the right answer on clear-cut inputs. On ambiguous ones it is still
near-certain, and wording can flip the result. Example: for "Is there any way to speak
to someone about my invoice?", asked whether the customer wants a human agent, Newt
gave 0.9996 with its first prompt and 0.0000004 with the current one. TypeSafe gives
0.84. Treat Newt's numbers as a ranking, not as probabilities to threshold. The
[full results](RESULTS.md) compare Newt with TypeSafe on every published example.

## Example

```swift
import Newt

let newt = try await Newt(resourcesAt: URL(filePath: "/path/to/qwen3_4b_4bit_dynamic"))
let answers = try await newt.ask(
    state: "My running shoes arrived in the wrong size. Can I swap them for a size 10?",
    questions: [
        "department": .choice("Which team should handle this?", criteria: [
            "returns": "Exchanges, wrong or damaged items",
            "shipping": "Delivery status, delays, lost packages",
            "billing": "Charges, invoices, payment problems",
        ]),
    ])

let department = answers["department"]!
print(department.choice!)
print(department.probabilities!.sorted { $0.value > $1.value })
print(department.confidence!, department.coverage)
```

Output from a release build on Qwen3-4B:

```
returns
[(key: "returns", value: 0.9999999999999998), (key: "shipping", value: 1.7237152888580243e-16), (key: "billing", value: 4.356925952507399e-19)]
0.9999999999999997 0.9999714259424044
```

## Requirements

- An Apple silicon Mac with macOS 27 and Xcode 27. Core AI doesn't exist on Linux.
- About 2.1 GB of disk for the Qwen3-4B export. Qwen3-0.6B (336 MB) also runs, but it
  fails half the fixture tests; use 4B.
- iOS 27: Newt builds for iOS, but it hasn't been run on a device. iPhone needs an
  export made with `--platform iOS`, and whether the 4B model fits in iPhone memory
  hasn't been tried.

## Try it

Export the model with [apple/coreai-models](https://github.com/apple/coreai-models)
(Newt doesn't ship or redistribute weights), then run the comparison with TypeSafe:

```bash
brew install uv
git clone https://github.com/apple/coreai-models.git && cd coreai-models
git checkout 5ed9981    # the commit Newt builds against
uv run coreai.llm.export Qwen/Qwen3-4B --output-dir ~/newt-models/
cd ..

git clone https://github.com/willswire/swift-newt.git && cd swift-newt
NEWT_MODEL_PATH=~/newt-models/qwen3_4b_4bit_dynamic swift test -c release --filter FixtureTests
```

Pass the exported **folder** (`qwen3_4b_4bit_dynamic`), not the `.aimodel` file inside
it. The first load takes 8–12 seconds, because Core AI specializes the model for your
Mac and caches the result; later loads take about a second (see [Performance](#performance)).
A wrong path throws `NewtError.notAModelExport`, whose message names the folder to pass
when Newt can find it.

## Install

```swift
.package(url: "https://github.com/willswire/swift-newt.git", branch: "main"),
```

It has to be `branch:`, not `from:`. Newt pins coreai-models to a commit, because no
coreai-models tag builds with Xcode 27 yet, and SwiftPM won't resolve a version
requirement on a package that itself depends on a commit. Newt will tag releases once
coreai-models does.

## Questions

Newt keeps TypeSafe's names (`state`, `instructions`, `criteria`, Choice, Score, Noul)
and answer field names, so their examples carry over line for line. "Noul" is
TypeSafe's name for a yes/no question.

| Type | Ask with | Answer fields |
|---|---|---|
| Choice | `.choice(instructions, criteria: ["key": "description", …])`, 2–255 options, in prompt order | `choice`, `probabilities`, `confidence`, `coverage` |
| Score | `.score(instructions, criteria: ["lowest level", …, "highest level"])`, 2–10 levels | `score`, `legend`, `probabilities` (keyed `"0"`, `"1"`, …), `confidence`, `coverage` |
| Noul | `.noul(instructions, criteria: (true: "…", false: "…"))`, criteria optional | `noul`, `coverage` |

Invalid questions throw `NewtError.invalidQuestion` before any model work runs.

## What the numbers mean

- **`probabilities`** (and **`noul`**, the probability of "yes") are the model's
  preference among the options you listed, normalized to sum to 1. They are not
  calibrated, and they are not the chance that an answer is correct.
- **`confidence`** is `(max p − 1/n) / (1 − 1/n)`: 0 when the options are equally
  likely, 1 when one option has all of it. That formula is Newt's; it reproduces
  TypeSafe's two published values but isn't documented by them. On Qwen3-4B it sits
  near 1.0 on every fixture, so it tells you little.
- **`score`** is Σ level × probability, TypeSafe's formula.
- **`coverage`** is the share of the model's probability that landed on any listed
  option as a complete answer. Low coverage means the model wanted to say something
  else, so distrust the other fields. High coverage means the model answered in the
  expected format, not that the answer is right.

## Performance

Qwen3-4B, release build, Apple M3 Pro with 18 GB, macOS 27.0:

| Step | Time |
|---|---|
| First load (Core AI specializes the model) | 7.6–11.8 s |
| Later loads | ~1.0 s |
| First ask after load (3-option Choice) | ~0.5 s |
| Warm ask (3-option Choice) | ~435 ms |
| Warm ask (two Noul questions) | ~600 ms |

**Measure with release builds** (`swift test -c release`, `swift build -c release`).
Debug builds were 4.5× slower on 4B and 14× slower on 0.6B.

## How it works

Newt scores each option key as the model's complete answer: it sums the log-probability
of the key's tokens plus the end-of-turn token after a fixed prompt, then normalizes
over the options. That's the standard multiple-choice scoring used in eval harnesses,
packaged behind a TypeSafe-shaped Swift API. Apple's built-in Foundation Models don't
expose token probabilities, so Newt runs an open model (Qwen3) through Core AI and
[apple/coreai-models](https://github.com/apple/coreai-models) instead.

Everything runs on-device, and nothing is sent anywhere: the full test suite passes with
outbound network access blocked.

## Limits

- Tested only with Qwen3-4B and Qwen3-0.6B exports, on one Mac. Models whose chat
  template adds a BOS token may double it.
- Options appear in the order given, and small models have position bias. Score shows
  all levels at once; TypeSafe says its model judges each level without seeing the others.
- One `ask` runs at a time per `Newt`, and the questions in an `ask` run one after
  another. Concurrent calls wait their turn.
- Within one `ask`, Newt reuses the model's cache for the shared prompt prefix. On
  Qwen3-4B that matches a cold read within 0.031 nats. On Qwen3-0.6B, one value differs
  by 0.055, over the test's 0.05 limit.
- The cache reuse assumes a pure transformer, which every Qwen3 export is. Newt doesn't
  detect hybrid or state-space models, for which it isn't valid.
- Criteria and instructions are plain strings.

## TypeSafe

Newt is inspired by TypeSafe's primitives ([docs.typesafe.ai](https://docs.typesafe.ai/primitives))
and is not affiliated with TypeSafe. The fixture text and the reference values in the
tests and in [RESULTS.md](RESULTS.md) come from their public docs for
[Choice](https://docs.typesafe.ai/primitives/choice),
[Score](https://docs.typesafe.ai/primitives/score), and
[Noul](https://docs.typesafe.ai/primitives/noul). Newt runs a
general-purpose open model, so its numbers differ from TypeSafe's.

Newt was written with the help of Claude Code, Anthropic's coding agent.

## License

MIT. See [LICENSE](LICENSE).
