# Decision Models Under Pressure

Eight systems do the same job: take a piece of text, a question, and a list of
candidate answers, and return a probability over those candidates. I measured
them against each other as that job gets harder in the three ways it gets harder
in production. The candidate list grows, the option order changes, and the wrong
answers stop being obvious.

**Short version.** Two hosted APIs sit at the top of this, and they tie.
OpenAI's [Decisions](https://developers.openai.com/api/docs/guides/decisions)
loses accuracy at the same rate as TypeSafe's
[Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) as the
list grows, and costs 17% less for the same work. Shuffle the option order,
though, and Decisions changes its answer on one decision in three where Jev
changes one in seven. Hold the order fixed and Decisions never changes its
answer at all, so every one of those flips is the order. Jev still changes one
in twenty-three, because it does not repeat itself. The open models that never
flip are the ones that fall off fastest as the list grows. Nothing here is good
at both.

| at 64 to 128 candidates | Decisions | Jev | [Laya](https://huggingface.co/convaiinnovations/laya) | best open |
| --- | --- | --- | --- | --- |
| accuracy at 128 candidates | 59% | **60%** | 39% | 41% |
| accuracy lost per doubling of the list | -0.043 | **-0.043** | -0.073 | -0.048 |
| accuracy lost when distractors get hard | -0.185 | **-0.105** | -0.345 | -0.235 |
| answers changed by reordering alone | 34.0% | 14.6% | 49.4% | **0.0%** |
| answers changed with the order held fixed | **0.0%** | 4.3% | **0.0%** | **0.0%** |
| cost per 1,000 decisions | **$0.029** | $0.035 | runs locally | runs locally |

"Best open" is a different model in every row: `deberta-large` for accuracy and
hard distractors, `gte-large` for the slope, `bge-large` for the flip rate.
That is the point of the row rather than a gap in it.

Jev's makers call it a new class of model. Laya's author has said publicly that
he published the same idea a year earlier. On the first claim the numbers are
not kind to the marketing, and on the second they are not kind to Laya: the idea
does look older than Jev, and Jev is still the better implementation of it by a
wide margin. A second hosted API arriving at the same scaling curve makes the
"new class" claim harder to sustain rather than easier.

The other five models are open ones I added so those numbers would mean
something. Most comparisons of these systems report one accuracy number at one
candidate-set size, which hides most of what matters, because the ranking
changes depending on how many options you offer.

Everything ran on one frozen dataset, with the comparisons and the pass/fail
rules written down before the first call ([PLAN.md](PLAN.md)). n is 200 items per
domain, which is enough to separate the large effects below and not enough for
the small ones. Every caveat is load-bearing.

## What came out of it

Every model gets worse as the candidate list grows. The difference is how fast.

![Accuracy against candidate-set size](docs/figures/k-curve.png)

Jev and Decisions start highest and stay highest, and they trace almost the
same line. At 128 candidates Jev answers 60% correctly and Decisions 59%, where
Laya manages 39% and the best open model 41%. Chance at that list length is
0.8%, so everything here is doing real work; the question is how much of it
survives a longer list.

The two hosted APIs share the shallowest decline per doubling of the list, and
both are shallower than the embedding scorers whose design is supposed to help
them scale. Measured over the same range for every model (K=2 to 128, since
both hosted APIs refuse more than 255 options):

| model | accuracy lost per doubling of the candidate list |
| --- | --- |
| Jev | **-0.043** |
| Decisions | **-0.043** |
| gte-large | -0.048 |
| bge-large | -0.051 |
| gliclass | -0.064 |
| deberta-large | -0.070 |
| deberta-base | -0.070 |
| Laya | -0.073 |

Those two are -0.0425 and -0.0427, a gap of 0.0002 and well inside the noise on
800 items. They do not get there the same way, though. Decisions beats Jev on
emotional tone at six of the seven list lengths, by six points at 128, and
loses to it on both intent-routing domains at nearly all of them. Two different models, one
slope.

Notice how little a single-number benchmark would tell you. At two candidates
Laya sits second of eight and trails Jev by two points. At 128 it has fallen to
fifth and trails by twenty-two.

Next the wrong answers had to get harder. Every item exists in two versions: one
where the distractors come from unrelated domains, and one where they are the
right answer's nearest neighbours, so `create alarm` competes against
`delete alarm` and `snooze alarm` rather than against `musical work`. I matched
the surface shape of the words between the two versions so only meaning
separates them. The gap between them is how much a model was leaning on the
wrong answers being obvious.

![Accuracy lost when distractors are nearly right](docs/figures/near-distractors.png)

At 64 candidates Jev drops from 96.8% to 86.3%, losing about a tenth of what it
had. Decisions drops from 96.0% to 77.4%, losing about a fifth, which puts it
between Jev and every open model in the study. Laya drops from 90.5% to 56.0%
and gliclass from 87.0% to 51.2%, each losing something closer to four tenths. That is the widest spread in the whole
experiment and the one I'd care most about in production, where candidate sets
are full of near misses.

Then I shuffled the options. Same question, same candidates, five different
orderings, and I counted how often the answer changed.

This is where it helps to know how each model reads its candidate list, because
that single design choice predicts the result almost perfectly:

| model | how it reads the candidates |
| --- | --- |
| Decisions | undisclosed, and the same tell, more strongly |
| Jev | undisclosed, but its answers depend on the order, so not one at a time |
| Laya | all candidates in one pass, as a set |
| `gliclass-large-v3.0` | the same |
| `deberta-v3-base-zeroshot-v2.0` | one pass per candidate, each scored against the text alone |
| `deberta-v3-large-zeroshot-v2.0` | the same, larger |
| `bge-large-en-v1.5` | embeds the text once, compares it to cached candidate vectors |
| `thenlper/gte-large` | the same, different encoder |

A model that scores each candidate on its own cannot notice that two candidates
are similar, and the order you list them in cannot reach it. A model that reads
them as a set gets the first ability and the second problem together.

That design choice predicts the flip rate and nothing else. It does not predict
the K curve: Decisions and Laya both read the list as a set and sit at opposite
ends of the scaling table, -0.043 against -0.073. Whatever separates those two
is not whether they see the options together.

![Answers that change when only the order changes](docs/figures/order-flips.png)

Two of the four candidate-at-a-time models never flip: `bge-large` and
`deberta-large` are exactly 0.0000 across 1,600 decisions each, which is what
scoring each option in isolation should give you. It doubles as a check that the
harness isn't shuffling something it shouldn't.

The other two are not quite zero. `deberta-base` flips on 0.2% of decisions and
`gte-large` on 2.0%, and both turned out to be exact scoring ties broken by
position rather than a real order effect: all 32 of gte's flipping items at 64
candidates have two options tied to within 1e-9. Structural invariance holds. Ties
are the crack in it, and if you are picking a model because order cannot reach
it, 2% is still 2%.

Against that baseline, Jev's 14.6% at 64 candidates is a real cost and about a
third of Laya's rate, which changes its answer on half of its decisions at the
same list length. Decisions sits between them at 34.0%, worse than Jev by a
factor of more than two.

How much of that is the order, though, and how much is the model not repeating
itself? Five calls that differ in option order also differ in being five calls.
The control is to hold the order fixed and call five times anyway, so I ran it
for both hosted arms (8,000 calls each,
`results/published/rq2_determinism.json` and `decisions_summary.json`):

| | shuffled order | fixed order | gap | 95% CI |
| --- | --- | --- | --- | --- |
| Jev, K=64, n=1600 | 14.6% | 4.3% | +10.2 | [+8.6, +11.9] |
| Decisions, same items | 34.0% | **0.0%** | +34.0 | — |
| Laya, same items | 49.4% | **0.0%** | +49.4 | — |

![How much of the flip rate is the order](docs/figures/flip-decomposition.png)

So roughly ten points of the fourteen belong to the order, and every one of the
eight domain-and-tier cells clears zero on its own. The remaining 4.3% is Jev
disagreeing with itself: same item, same options, same order, five calls. The
two effects overlap rather than stack, so the gap is the right statistic and
subtraction is not: of the 248 items that flipped under either arm, 179 flipped
only when shuffled, 15 only under a fixed order, and 54 under both.

Laya's zero is exact, over 3,200 items and 16,000 calls, which is what a local
model under `no_grad` with no sampling in the path should give. It is also what
rules out the harness as the source of anyone's instability.

Decisions returns an exact zero too, over 1,592 items, which is the more
surprising of the two because it is a hosted API with no seed parameter and no
temperature control. That leaves Jev as the only arm in the study that fails to
repeat itself. I checked the obvious alternative explanation, that the API is
replaying a cached response rather than recomputing: five serial repeats of one
item all reported `cached_tokens: 0`, and a variant with one extra trailing
space, so 366 input tokens instead of 365, came back with the same choice and
slightly different probabilities. It recomputes and agrees with itself.

The clean consequence is that Decisions' whole 34.0% is order and nothing else,
with no noise floor underneath it. Jev's 14.6% does not decompose that way.

The flips are not spread evenly, and the spread matters more than the headline:

| where | Jev, unrelated | Jev, near-neighbour | Decisions, unrelated | Decisions, near-neighbour |
| --- | --- | --- | --- | --- |
| request routing (clinc) | 1.5% | 9.0% | 2.0% | 27.9% |
| request routing (mtop) | 3.0% | 12.5% | 12.2% | 35.7% |
| financial topics | 5.0% | 22.0% | 12.0% | 55.5% |
| emotional tone | 30.5% | 33.0% | 53.7% | 73.2% |

Intent routing with easy distractors is the best case and it is genuinely stable
on both. Intent routing with plausible competing options, which is what a real
router faces, runs four to six times worse on Jev. On Decisions it runs three
times worse on MTOP and fourteen times worse on CLINC, which is a wider spread
than Jev shows anywhere. Anything subjective is worse again, and barely improves when the
distractors get easy.

### What makes an answer flip

A flip rate says how often reordering changes the answer. It does not say why,
and two explanations fit the headline equally well. Either the model flips where
it was lost anyway, or it flips because the list holds something that looks like
the answer. The two are confounded, because the near-neighbour cells and the
emotional-tone domain have both the worst accuracy and the most flips.

Separating them takes conditioning rather than more calls, so this re-reads the
3,170 cells already in the Decisions ledger. Jev's per-call ledger is not in
this repo, so this runs on one of the eight arms and the rest of the section
should be read that way.

**It is not simply the model being wrong.** Of the 199 cells at 64 candidates
that Decisions never got right across five calls, 48 returned the same wrong
answer five times out of five. In the other direction, 385 of the 536 flipped
cells have the right answer among the five given. The usual flip is a model that
holds the right answer and loses it to a reshuffle, and 60% of flips are a
two-way oscillation rather than a scatter.

**The competing option matters even where the model is right.** Near tier
against far, on the same items:

| subset of cells, K=64 | near | far | difference | 95% CI |
| --- | --- | --- | --- | --- |
| all | 48.2% | 19.7% | +28.4 | [+24.0, +33.0] |
| the model's majority answer is correct | 30.9% | 12.7% | +18.2 | [+13.3, +22.9] |
| correct on 4 or 5 of the 5 calls | 17.2% | 7.4% | +9.8 | [+5.8, +13.8] |
| the model's majority answer is wrong | 86.2% | 82.3% | +4.0 | [-4.8, +13.6] |

The effect survives on the cells it gets right and disappears on the cells it
gets wrong. A logistic fit over all 3,170 cells puts the same thing in odds:
being right makes a flip about eight times less likely, and a near-neighbour in
the list makes it about three times more likely after correctness, list length
and domain are all held fixed.

**And a third thing neither explanation predicts.** Shuffling randomises where
the right answer sits inside the list, which makes this a randomised contrast
rather than an observational one.

![Accuracy by where the right answer sits](docs/figures/primacy.png)

Within a single cell, holding the item and the option set fixed, the right
answer sits a fifth of the list earlier in the calls where the model picked it.
The sharpest version restricts to cells that produced exactly two distinct
answers, where the pair is fixed and only the order moves:

| K | the two candidates | the earlier one wins | 95% CI |
| --- | --- | --- | --- |
| 64 | one of them is right | 64.1% | [61.3, 66.8] |
| 64 | both are wrong | 61.6% | [56.9, 66.3] |
| 16 | one of them is right | 56.4% | [53.1, 59.5] |
| 16 | both are wrong | 54.8% | [47.1, 62.6] |

Pairs of two wrong labels behave like pairs holding the right one, so this is a
preference for position and not anything about correctness. It strengthens as
the list grows.

So a flip needs three things at once: a competitor close enough to be
confusable, a model that is not decisively settled, and a reshuffle to tip it.
Remove any one and it does not happen, which is why the reported margin between
the top two options predicts flips so sharply. The bottom quartile by margin
flips 83.8% of the time and the top quartile flips 0.0%.

Three fixes are available to anyone deploying these today, and the two controls
change what each is worth. Present the options in a fixed canonical order: on
Laya and on Decisions that buys exact reproducibility, on Jev it removes ten of
the fourteen points and leaves 4.3% that no amount of canonical ordering will
reach. Note what it does not buy. Position still carries a preference, so a
canonical order does not neutralise it, it freezes one arbitrary winner and
hands a standing advantage to whatever you sorted to the top.

Or ask the same question under several orderings and take the majority, which
costs several calls per decision and is the only one of the three that helps
with a model that will not repeat itself.

Or gate on the reported margin and drop the decisions that are about to be
unstable. On Decisions at 64 candidates, keeping only cells with a margin of
0.50 or better covers 66% of them at a 10.3% flip rate, 0.70 covers 54% at 3.2%,
and 0.90 covers 36% at 0.0%. The probabilities come back at two decimals, so
those thresholds are coarse by construction.

Worth separating the two properties when you choose, because they do not travel
together. Laya is perfectly reproducible and the most order-sensitive thing
here, and Decisions is the second-most while also being perfectly reproducible.
Jev is the only arm that trades the other way. If you need the same input to
give the same answer twice, that is a different question from whether the list
order reaches the model, and only one of them is fixed by sorting your
options.

One more thing fell out of the logs after the fact. Confidence and correctness
come apart badly as the list grows, and not for everyone:

| model | calibration error at K=2 | at K=256 |
| --- | --- | --- |
| deberta-large | 0.064 | 0.070 |
| deberta-base | 0.066 | 0.075 |
| bge-large | 0.099 | 0.197 |
| gte-large | 0.048 | 0.299 |
| gliclass | 0.150 | 0.327 |
| Laya | 0.032 | **0.573** |

Laya is the best-calibrated model in the set at two candidates and by far the
worst at 256. If you are gating on a confidence threshold, that is the number
that decides whether the gate works. Both hosted APIs are missing from this
table because they round probabilities to two decimals, which is too coarse to
measure calibration. 98% of Jev's responses and 90% of Decisions' contain at
least one option at exactly 0.00.

## What it costs and how fast

Both hosted arms ran the same 29,600 calls, so the bill is a like-for-like
comparison:

| | Decisions | Jev |
| --- | --- | --- |
| the same 29,600-call grid | **$0.864** | $1.040 |
| per 1,000 decisions | **$0.029** | $0.035 |
| list price | $0.10 / 1M input tokens | $0.042 / 1M input tokens |
| measured tokens per call | 97 + 4.4 per option | 284 + 13 per option |
| fixed overhead per call | **$9.7e-6** | $11.9e-6 |
| marginal cost per option | **$0.44e-6** | $0.55e-6 |

Decisions costs 17% less for identical work, and the higher list price is
misleading. Jev bills roughly three times the tokens per option at 0.42 times
the rate, so Decisions is cheaper at both ends of the formula and there is no
list length where that reverses. The ratio runs from 0.86 at two candidates to
0.81 at 255.

Latency needs more care. Jev reaches the network through OpenRouter, which is a
proxy hop that a direct call to OpenAI does not pay, and the two arms ran a
month apart at different concurrency. Jev averaged 238ms at 5 workers and
Decisions 197ms at 12, which looks like a gap until you normalise: 4.6 calls per
second per worker against 5.2. Treat them as close.

One number is worth having on its own, because it is the property the rest of
this study never touches. Decisions' median latency does not move with the
length of the candidate list:

| candidates | 2 | 4 | 8 | 16 | 32 | 64 | 128 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| median ms | 175 | 174 | 174 | 162 | 174 | 162 | 170 |

Sixty-four times the options for the same wall-clock time. A cross-encoder pays
one forward pass per candidate and cannot do that. The means by list length
wobble between 183ms and 259ms, but they track which batch a call ran in rather
than K, so the median is the honest statistic here.

One operational note that is not in the API guide. 110 of our 37,600 calls came
back as `{"type": "refusal"}` instead of a choice, which is an answer type the
documentation does not mention. Re-sending all 110 produced a refusal every
time, so it is deterministic per item rather than sampling noise, and it
concentrates on GoEmotions, then MTOP and CLINC, where the items carry personal
names or charged language. At 0.3% of calls it changes no result in this study,
and accuracy is published both with those calls dropped and with them scored
wrong. If you are deploying against this endpoint, handle the case.

## What this cannot tell you

Neither hosted model's training data is disclosed. The items come from public
datasets, so "trained better" and "has seen these before" cannot be told apart
here. The one hint available points both ways: Jev is steadiest on exactly the
intent-style domains a decision product would plausibly be trained on, and
shakiest on the domain furthest from that. The problem is worse for Decisions,
not better, because a general model has had more opportunity to meet five
public datasets than a narrow one. Nothing here settles it, and no outside test
can settle it while the training data stays private.

No architecture claim is available for either. OpenAI has published nothing
about how the endpoint scores options, so this measures a product and not a
design.

The Jev comparison was also not part of the original plan. I wrote the
pre-registration around the three open architecture families and listed Jev as a
conditional extra if I got API access. I did, it went in, and it reversed the
conclusion I had been heading toward, which was that reading candidates as a set
carries costs and buys nothing. Jev reads candidates as a set and carries much
smaller costs. So the honest version is that the costs belong to those two open
checkpoints rather than to the architecture. I've left the original reasoning in
[EXPERIMENTS.md](EXPERIMENTS.md) rather than quietly rewriting it.

The Decisions arm is further outside the plan than that. It was added on
2026-10-19, after the three questions had been answered and published, against
a protocol that was frozen before it existed. Nothing in PLAN.md moved to
accommodate it and it is reported against the same pass/fail bars, but read it
as a fourth column on a finished table rather than as evidence the plan
anticipated it.

The section on what makes an answer flip runs on the Decisions ledger alone.
Jev's per-call records are not in this repo, so one arm of eight has a
mechanism and the other seven have a rate. Whether the same three ingredients
explain Jev's 14.6% is untested.

The determinism control was run after the fact, on 2026-09-25, and was not part
of the pre-registration. I should have planned it: the original flip measure
varied two things at once and I only noticed when someone would obviously have
asked. It covers K=64 only, so the K=16 flip rates in EXPERIMENTS.md still carry
an unmeasured noise component.

The latency comparison is the weakest number in this README. Jev reached the
network through OpenRouter and Decisions went direct to OpenAI, a month apart,
at different concurrency. The per-worker throughput figures are the closest to
like-for-like I can offer and they are still not a controlled measurement.

Three smaller limits. The near-distractor comparison rests on two domains, both
of which every model here has plausibly seen. Both hosted APIs cap candidate
lists at 255 options, so the head-to-head stops at 128; the open models run to
256 and those numbers are in `results/published/`. And n is 200 items per
domain, with bootstrap intervals on everything in EXPERIMENTS.md, which is
enough to separate the large effects here and not enough for anything
subtle.

## Reproducing it

```bash
python -m venv .venv
.venv/bin/pip install torch transformers datasets sentence-transformers scikit-learn

.venv/bin/python -m harness.run.local --rq rq3    # run one question
.venv/bin/python -m harness.analyze.rq3
```

The dataset ships complete, so there is no rebuild step. To rebuild it from the
upstream sources anyway:

```bash
.venv/bin/python -m harness.build --n 200         # build and run the checks
.venv/bin/python -m harness.build.export
```

The two hosted arms cost $1.04 and $0.86 for the full grid of 29,600 calls
each. Both runners keep an append-only ledger, so a resumed run never re-sends
a call that was already paid for, and both refuse to start a call that would
cross the spend cap:

```bash
export OPENROUTER_API_KEY=sk-or-...
.venv/bin/python -m harness.run.jev --rq rq3 --cap 2.00

export OPENAI_API_KEY=sk-...
.venv/bin/python -m harness.run.decisions --rq rq3 --cap 2.00
```

The Decisions arm needs no extra dependencies. It is standard library only.

## Data

`dataset/v3/` holds 1,000 items across five domains, with the item text, the
gold label, both distractor pools and every derived field. It is published under
**CC BY-SA 4.0**, because MTOP is CC BY-SA 4.0 and ShareAlike carries over. If
you reuse it, your version inherits that too. The code is MIT.

| domain | source | licence |
| --- | --- | --- |
| clinc | [CLINC-150](https://huggingface.co/datasets/clinc/clinc_oos) | CC BY 3.0 |
| goemotions | [GoEmotions](https://huggingface.co/datasets/google-research-datasets/go_emotions) | Apache 2.0 |
| mtop | [MTOP](https://huggingface.co/datasets/WillHeld/mtop) | CC BY-SA 4.0 |
| dbpedia | [DBpedia Classes](https://huggingface.co/datasets/DeveloperOats/DBPedia_Classes) | CC0 1.0 |
| fintopic | [Twitter Financial News](https://huggingface.co/datasets/zeroshot/twitter-financial-news-topic) | MIT |

Full attribution, the upstream papers, what I changed, and the GoEmotions
content warning are in [`dataset/v3/README.md`](dataset/v3/README.md). Texts are
verbatim; every item carries a SHA-256 of its text so you can check it against
the original source. If you use this data, cite the upstream papers, not this
repo.

## What is in here

| path | contents |
| --- | --- |
| `dataset/v3/` | 1,000 items, the 902-option label universe, per-question splits, the checks, datacard |
| `harness/build/` | how the dataset is made: label universe, items, distractor tiers, the eight checks |
| `harness/models/` | model adapters, one per family, plus the two hosted clients |
| `harness/run/` | the local runner, the two hosted runners, and the refusal re-probe |
| `harness/analyze/` | one analysis per question, the flip decomposition, and the figures |
| `results/published/` | the aggregates every table and figure is built from |
| `PLAN.md` | what I decided to measure, and the pass/fail rules, before anything ran |
| `EXPERIMENTS.md` | every run, including the ones that went against what I expected |

## How the dataset was checked

An earlier version of this produced confident results that did not survive
review. Auditing it turned up three things that mattered: a classifier with no
access to the item text could identify the right answer from label formatting
alone, an option's position was a function of its label rather than the item, and
one model's apparent context ceiling was an artifact of how my harness passed
options to it.

I rebuilt the dataset around those failures, and the checks that caught them now
run as assertions before any model does. Eight of them: no option string may
appear in the prompt's own wording, surface features must not separate near
distractors from far ones, a text-blind classifier must stay under twice chance,
gold position must depend on the item, the near tier must be measurably nearer,
every item must be usable in both tiers at every list size, no adjudicated
ambiguous pair may sit together, and each option set must be well formed.

Seven of the eight pass. The one that does not is the text-blind classifier,
which still beats chance on some cells: 0.260 on DBpedia against a chance rate of
0.0625 and a 0.125 gate. That means some accuracy on those cells comes from label
formatting rather than from reading the text, and it inflates the level of the
curves without changing their shape. Per-cell numbers are in
`dataset/v3/gates.json` rather than described away. Two fixes were tried and
rejected, with their numbers recorded: coarser matching reopens the formatting
check, and dropping the affected items shrinks the sample while making the
residual worse.

Two rules I'd written in advance fired against me during the run. One voided a
family-level comparison when the two models inside a family disagreed more than
the families did. The other required the order-invariant models to score exactly
zero, which two of four did, with the other two traced to scoring ties.

## Licence

The dataset in `dataset/v3/` is CC BY-SA 4.0, inherited from MTOP. Per-source
licences, credits and what I changed are in
[`dataset/v3/README.md`](dataset/v3/README.md).

The code carries no licence, which under default copyright means you may read it
but not reuse it. That is deliberate rather than an oversight: the point of this
repo is the method and the numbers, both of which you are welcome to take. If
you want to reuse the code itself, ask and I'll add a licence.
