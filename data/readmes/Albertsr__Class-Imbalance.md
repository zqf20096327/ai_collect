# Class Imbalance for Credit Risk

> From selected and label-mature samples to training signals, ranking,
> probability, decisions, and portfolios.

English · [简体中文](README.zh-CN.md) · [Historical theory notes](docs/en/theory.md) · [API reference](docs/reference/README.md)

This project is rooted in Chinese credit-risk practice, but the modeling
questions and theoretical connections are open to practitioners everywhere.

It is not an encyclopedia of class-imbalance algorithms, and it does not treat
a `1:1` class ratio as an objective. The primary case is retail-credit
application probability-of-default (PD) modeling in China. Before choosing a
resampling method or loss function, the project asks who enters the sample,
which outcomes are observable, and when labels become mature. It then
separates changes to the training signal from evidence about ranking,
probability, and business action.

```text
population and label -> training signal -> ranking -> probability -> decision -> portfolio
```

## The central modeling claim

Class imbalance is not an isolated algorithm choice. It sits inside an ordered
chain of evidence:

| Layer | Question | What it must not be reduced to |
|---|---|---|
| Population and label | Who applied, who was approved and booked under the historical policy, whose performance window has matured, and which outcomes remain unobserved? | “Unresampled data equals the true all-applicant distribution.” |
| Training signal | What do the original sample, resampling, class weights, instance weights, and loss function each change? | “Rare bads imply the training set must become 1:1.” |
| Ranking | Are higher-risk applicants ordered ahead of lower-risk applicants in the target cohort and across time? | “A high AUC means the PD is accurate.” |
| Probability | Does the output estimate PD for a stated conditional population, bad definition, and horizon? | “A model score is automatically a usable probability.” |
| Decision and portfolio | How does a score or probability become an approval, review, pricing, or limit action, and what portfolio follows? | “0.5 is the natural threshold.” |

A model can rank applicants well without producing calibrated PDs. A calibrated
PD can still lead to a poor policy if exposure, approval constraints, review
capacity, or portfolio mix are ignored. Rebalancing may help a learner attend
to rare bad outcomes, but it can also change the meaning of the raw score.

## From costs to thresholds: why 0.5 is a cost assumption, not a universal default

The original Chinese notes begin with cost-sensitive versus cost-insensitive
learning. A modern distinction distilled from that reasoning still organizes
this project:

> **Class imbalance describes how often outcomes occur. Cost sensitivity
> describes the consequences of decisions.**

Cost-sensitive learning distinguishes among the consequences of different
classification errors and seeks a decision rule with lower expected cost. An
accuracy-oriented, cost-insensitive rule instead counts false positives and
false negatives as interchangeable unit errors. A rare positive class may make
learning difficult, but rarity alone does not justify a `1:1` training sample
or a probability cutoff below `0.5`.

### 1. A cost matrix induces a probability threshold

Let $p(x)=P(Y=1\mid x)$ be the positive-class probability. Write
$C_{TP}, C_{FP}, C_{FN}, C_{TN}$ for the costs of the four possible
decision/outcome pairs:

| Decision | Actual $Y=0$ | Actual $Y=1$ |
|---|---:|---:|
| Predict $0$ | $C_{TN}$ | $C_{FN}$ |
| Predict $1$ | $C_{FP}$ | $C_{TP}$ |

The conditional costs of predicting positive and negative are:

```math
R_1(x)=pC_{TP}+(1-p)C_{FP},
\qquad
R_0(x)=pC_{FN}+(1-p)C_{TN}.
```

If each misclassification is no less costly than the corresponding correct
decision, and at least one is strictly more costly, predict positive when the
cost-derived cutoff $t_c$ is met:

```math
p(x)\geq t_c,
\qquad
t_c=
\frac{C_{FP}-C_{TN}}
     {C_{FP}+C_{FN}-C_{TP}-C_{TN}}.
```

When correct decisions have zero cost, this becomes:

```math
t_c=\frac{C_{FP}}{C_{FP}+C_{FN}}.
```

Under this zero-correct-decision-cost special case, `0.5` becomes interpretable
rather than automatic:

- $t_c=0.5$ when false positives and false negatives have equal cost;
- $t_c<0.5$ when false negatives cost more, so the rule classifies positive
  at a lower estimated probability;
- $t_c>0.5$ when false positives cost more, so stronger evidence is required
  before predicting positive.

Here, positive is only a statistical label; in credit risk or fraud detection,
it often denotes an adverse outcome. For example, let `1` mean default or
fraud, and set $C_{FN}=5$, $C_{FP}=1$, and $C_{TP}=C_{TN}=0$. Then
$t_c=1/(1+5)\approx0.167$. At $p=0.20$, predicting positive has expected
cost $0.80\times1=0.80$, while predicting negative has expected cost
$0.20\times5=1.00$. The lower-cost classification decision is therefore to
predict positive, even though the probability is far below `0.5`.

### 2. The cutoff is a decision rule, not a property of every score

The formula requires a calibrated probability for the target deployment
population, label definition, and outcome horizon, together with fixed,
instance-independent costs. An arbitrary ranking score—or an uncorrected score
from a rebalanced training distribution—is not such a probability.

If costs vary with exposure, loss given default (LGD), transaction size, or the
individual case, use instance-level expected loss or a case-specific
$t_c(x)$; one global cutoff is no longer sufficient.

Nor can every non-`0.5` cutoff be interpreted as a cost ratio. A threshold
chosen to satisfy an FPR cap, approval-rate target, review capacity, or
portfolio constraint reflects that operating constraint. Its value alone does
not reveal the relative costs of false positives and false negatives.

### 3. Thresholding, sampling, and weighting act at different layers

| Lever | What it changes | What it does not establish by itself |
|---|---|---|
| Cost-derived probability thresholding | The action taken from a calibrated target-population probability | Better ranking or better calibration |
| Sampling | The empirical training distribution seen by the learner | The real business cost ratio or target-population probability |
| Weighting | How strongly observations contribute to the training objective | The same fitted model, probability meaning, or deployment cutoff |
| Prior correction and calibration | How model outputs are interpreted as probabilities | Which business action is optimal |

Why do these levers sometimes appear equivalent? Under a known
class-conditional sampling or weighting scheme, and for a learner that recovers
the corresponding posterior odds, changing class ratios or class weights can
represent a shift in the target decision threshold. This is an equivalence at
the level of an idealized decision problem—not a promise that regularization,
tree splits, early stopping, or finite model capacity will produce the same
fitted model.

Sampling and weighting can also change the probability meaning of raw model
outputs. Before applying a cost-derived threshold, they may require prior
correction under a known class-sampling mechanism, calibration on
untouched, representative target-population validation or out-of-time (OOT)
data, or both. Neither step repairs selection bias created by historical
approvals.

This mechanism is why the historical theory connected cost, thresholding,
sampling, weighting, and class priors. The modern project preserves that chain
while making its conditions explicit. Its central contribution is to keep four
objects separate: outcome prevalence is a property of a population;
rebalancing is a training intervention; probability is an estimand; and a
threshold is a decision.

See the [full historical derivation](docs/en/theory.md) and the modern
[ranking, calibration, decision, and portfolio guide](docs/en/ranking-calibration-decision.md).

## The observation boundary in application PD

Let `X` denote application-time features, `A` the historical approval decision,
`B` whether an approved applicant actually books or draws the loan, `Y` the bad
outcome over a predefined performance window, and `M` whether that label has
matured. In many historical datasets, observed outcomes mainly come from
accounts satisfying `B = 1, M = 1`.

This has four consequences:

- An unresampled validation, test, or out-of-time cohort often represents
  mature booked accounts under the historical policy—not the full applicant
  population.
- For `A = 0` rejects, “would this applicant have defaulted if approved?” is a
  counterfactual outcome. It is not identified from approved-account outcomes
  alone. Approved but unbooked applicants normally lack repayment performance
  in the product as well.
- Recent accounts whose performance window has not closed are immature or
  right-censored; absence of an observed bad event does not make them good.
- Sampling belongs inside the training pipeline. Validation, test, and OOT
  cohorts retain the sampling frame of the population they are intended to
  evaluate.

See [Population, selection, and label maturity](docs/en/population-and-labels.md)
for the full treatment.

## Start here

1. [English documentation path](docs/en/README.md) provides the complete map.
2. [Population, selection, and label maturity](docs/en/population-and-labels.md)
   defines the estimand before any modeling method is chosen.
3. [What rebalancing changes](docs/en/rebalancing.md) compares sampling,
   weighting, loss shaping, prior correction, calibration, and threshold
   selection.
4. [Ranking, calibration, decision, and portfolio](docs/en/ranking-calibration-decision.md)
   separates four outputs that are often collapsed into one model metric.
5. [Experiment protocol](docs/en/experiment-protocol.md) gives a leakage-safe,
   time-aware comparison design.
6. [The fraud boundary](docs/en/fraud-boundary.md) explains why fraud is a
   useful contrast case, not a second name for application PD.
7. [Historical theory notes](docs/en/theory.md) adapts Ma Xiao's 2018–2021
   reasoning into English while keeping modern qualifications visibly
   separate.

Optional method experiments live under `docs/en/labs/`; begin with
[Focal Loss as an optional lab](docs/en/labs/focal-loss.md).

## Why the historical analysis remains

The theory map above comes from Ma Xiao's 2018–2021 Chinese homepage. Its value
is not a claim to have invented the underlying formulas; it is the way the
notes connect decision cost, probability thresholds, class-ratio changes,
observation weighting, and class priors into one modeling argument.

The [English historical edition](docs/en/theory.md) preserves the original
reading and derivation order, including the experimental observations and
paper notes. Modern qualifications are kept in a separate editor's note rather
than silently written back into the historical argument.

The [complete Chinese edition](README.zh-CN.md) remains a first-class entry,
and the [verbatim historical homepage](legacy/original-readme.zh-CN.md) remains
available for provenance.

## Credit risk and fraud are related, not interchangeable

Application PD and fraud detection both involve rare events and asymmetric
errors, but they do not share one population, label process, operating clock,
or cost model. Fraud often puts more emphasis on extreme false-positive
constraints, manual-review capacity, rapid feedback, selective labels, and
adversarial drift. Application PD puts more emphasis on historical approval
selection, performance-window maturity, the target conditional population, and
portfolio risk-return.

The project therefore uses fraud as a separate contrast case rather than
compressing both domains into one fixed-cost binary-classification problem.

## Engineering scope

The modern package is intentionally small. It provides auditable contracts for
binary metrics and operating points, probability correction, cost-based
decisions, rebalancing helpers, and selected losses.

| Status | Modules |
|---|---|
| Stable | `metrics`, `operating_points`, `probability`, `decision`, `rebalancing`, `losses` |
| Optional dependency | `sampling` |
| Experimental | `experimental.adacost` |
| Compatibility only | `thresholding`, `weighting` |

The compatibility modules preserve older imports; new work should use the
modules in the first three rows.

```text
src/class_imbalance/   small, testable modern Python APIs
tests/                 unit, contract, integration, and scenario checks
examples/              runnable synthetic examples only
docs/en/               substantive English adaptations
docs/zh-CN/            complete Chinese reading path
docs/reference/        authoritative English API reference
docs/history/          provenance and refactor records
legacy/                historical assets, not the stable API
```

See the [API reference](docs/reference/README.md) for contracts and
interpretation boundaries.

## Minimal API example

A ranking-score operating point and a calibrated-probability cost threshold
are two different paths:

```python
from class_imbalance.decision import cost_sensitive_threshold, predict_with_threshold
from class_imbalance.operating_points import operating_point_at_fpr_cap
from class_imbalance.probability import prior_probability_correction

# Synthetic convention: 1 = bad, 0 = good.
y_true = [0, 0, 0, 0, 1, 1]
ranking_score = [0.05, 0.10, 0.40, 0.65, 0.70, 0.95]

# Ranking path: choose an achievable empirical point under an FPR cap.
point = operating_point_at_fpr_cap(y_true, ranking_score, fpr_cap=0.25)
print(point)

# Probability path: the source values must already have probabilistic meaning.
# Prior correction does not repair historical approval selection.
source_prob = [0.03, 0.08, 0.20, 0.35, 0.55, 0.85]
target_prob = prior_probability_correction(
    source_prob,
    source_prevalence=0.20,
    target_prevalence=0.08,
)
threshold = cost_sensitive_threshold(
    false_negative_cost=5.0,
    false_positive_cost=1.0,
)
actions = predict_with_threshold(target_prob, threshold)
print(actions)
```

`cost_sensitive_threshold` applies only to calibrated probabilities for the
target deployment population under fixed, instance-independent
misclassification costs. A real credit policy also requires portfolio
constraints and OOT validation.

## Install and verify

From a fresh clone with Python 3.10 or later:

```bash
python -m pip install -e ".[dev]"
python -m pytest -q
python -m build
```

The package core depends only on NumPy. Sampling and estimator integrations are
installed through their declared optional dependency groups. The built wheel
should also be installed in an isolated environment for a smoke test, followed
by all public examples.

## Runnable synthetic scenarios

- [Credit-risk workflow](examples/credit_risk_workflow.py) compares an
  unrebalanced model with training-only random oversampling, applies a
  conditional prior correction, and evaluates a cost-based decision on an
  untouched later cohort.
- [Reject-inference boundary](examples/reject_inference_boundary.py) uses an
  oracle available only in synthetic data to show why accepted, mature outcomes
  do not identify the all-applicant bad rate.
- [Fraud under an FPR cap](examples/fraud_fixed_fpr.py) selects an achievable
  empirical review threshold without interpolating between ROC points.

With the development extra installed:

```bash
python examples/credit_risk_workflow.py
python examples/reject_inference_boundary.py
python examples/fraud_fixed_fpr.py
```

The examples use deterministic synthetic data. They do not encode customer
records, production thresholds, internal approval rules, or real institutional
parameters.

## Historical, public, and license boundaries

- The author's 2018–2021 theory, code, and experiment records are preserved as
  historical evidence. Historical image files were separately audited and are
  excluded from the curated tree unless authorship and redistribution rights
  can be confirmed. These materials are not the stable API and should not be
  read as current production guidance.
- Third-party papers, screenshots, datasets, and external code are not covered
  merely because this project uses an open-source license. See
  [THIRD_PARTY.md](THIRD_PARTY.md) and the
  [legacy manifest](legacy/MANIFEST.md).
- Modern examples and documentation discuss general methods without disclosing
  any institution's customer data or production implementation.

The modern code and original project materials for which the author holds the
rights are released under the [MIT License](LICENSE). Author: **Ma Xiao**.
