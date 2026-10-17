<div align="center">

# 🌫️ PLUME

## Physically conditioned correction and ordered uncertainty<br>for multiday particulate forecasting over East Asia

<b>PLUME</b> &nbsp;·&nbsp; <b>P</b>hysics-guided <b>L</b>ead-conditioned <b>U</b>ncertainty-aware <b>M</b>ixture <b>E</b>stimator

<br>

[Inha Kang](mailto:rkswlsj13@kaist.ac.kr)<sup>1,†</sup> &nbsp;·&nbsp;
[Wonjeong Ryu](mailto:petac@kaist.ac.kr)<sup>1,†</sup> &nbsp;·&nbsp;
[Sung-Chul Hong](mailto:schong@korea.kr)<sup>2</sup> &nbsp;·&nbsp;
[Jae-Bum Lee](mailto:gercljb@korea.kr)<sup>2</sup> &nbsp;·&nbsp;
[SooJin Ban](mailto:halfjjang@korea.kr)<sup>2</sup><br>
[Seongeun Jeong](mailto:atmos1214@ajou.ac.kr)<sup>3</sup> &nbsp;·&nbsp;
[Yoon-Hee Kang](mailto:ykang@ajou.ac.kr)<sup>4</sup> &nbsp;·&nbsp;
[Soontae Kim](mailto:soontaekim@ajou.ac.kr)<sup>3</sup> &nbsp;·&nbsp;
[Hyunjung Shim](mailto:kateshim@kaist.ac.kr)<sup>1,\*</sup>

<sub>
<sup>1</sup> Kim Jaechul Graduate School of AI, Korea Advanced Institute of Science and Technology, Seoul 02455, Republic of Korea<br>
<sup>2</sup> Air Quality Forecasting Center, National Institute of Environmental Research (NIER), Incheon 22689, Republic of Korea<br>
<sup>3</sup> Department of Environmental and Safety Engineering, Ajou University, Suwon 16499, Republic of Korea<br>
<sup>4</sup> Department of Environmental Institute, Ajou University, Suwon 16499, Republic of Korea<br>
<br>
<sup>†</sup> Equal contribution &nbsp;·&nbsp; <sup>*</sup> Corresponding author
</sub>

<br>

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Dataset on HF](https://img.shields.io/badge/%F0%9F%A4%97%20dataset-2na--97%2FPLUME-yellow)](https://huggingface.co/datasets/2na-97/PLUME)

</div>

---

PLUME forecasts surface PM<sub>2.5</sub> and PM<sub>10</sub> exceedance over East Asia from +6 h to +120 h, on a 0.25° grid, **without running a chemistry–transport forecast at the target valid time**. It advances a small, bounded *decision state* between valid times instead of recycling a predicted concentration field — so forecast error cannot accumulate the way it does under an autoregressive rollout.

With **10.4 M parameters** — roughly two orders of magnitude below the foundation models it is compared against — it takes the strongest chance-corrected exceedance skill in all six pollutant–region targets we evaluate.

<div align="center">
<img src="assets/teaser.png" width="100%" alt="PLUME versus operational and foundation-model forecasts, episode by episode"/>
</div>

---

## Table of contents

- [What the model does](#what-the-model-does)
- [Method](#method)
  - [The decision state](#the-decision-state)
  - [One hop: draft and refine](#one-hop-draft-and-refine)
  - [The correction state — and what "physically conditioned" means](#the-correction-state--and-what-physically-conditioned-means)
  - [The ordered uncertainty state](#the-ordered-uncertainty-state)
  - [What crosses the gap](#what-crosses-the-gap)
  - [Three products from one distribution](#three-products-from-one-distribution)
- [Results](#results)
- [Installation](#installation)
- [Data](#data)
- [Training](#training)
- [Evaluation](#evaluation)
- [Analysis: inspecting the decision state](#analysis-inspecting-the-decision-state)
- [Repository layout](#repository-layout)
- [Reproducing the paper](#reproducing-the-paper)
- [Citation](#citation)

---

## What the model does

An exceedance forecast is a **threshold decision**, not a regression. What a decision maker needs at +54 h is not the most likely concentration — it is (i) the change to the field that the issue-time evidence actually supports, and (ii) the higher-concentration alternative that the same evidence leaves unresolved.

Existing approaches answer neither well:

| Approach | What it advances between valid times | Failure mode |
|---|---|---|
| Autoregressive rollout | the predicted concentration field | error is unbounded and compounds over 20 steps |
| Cascade | the field, with intermediate correction | slows accumulation, does not remove the feedback |
| Direct decoding | nothing — each lead solved in isolation | discards everything an earlier lead established |
| **PLUME** | **a bounded decision state** | — |

PLUME keeps direct decoding as the backbone (we show below that it is the right one) and adds exactly one thing: a small typed state, built at an earlier lead, advected to the target valid time, and read there. **The concentration field it was extracted from is discarded.**

<div align="center">
<img src="assets/ar_vs_direct.png" width="78%" alt="Autoregressive rollout versus direct decoding"/>
<br><sub>Applying one set of weights recurrently is a stress test of field feedback, and it fails as such a test should — over Korea, RMSE rises from 26.4 to 107.7 µg/m³.</sub>
</div>

---

## Method

<div align="center">
<img src="assets/framework.png" width="100%" alt="PLUME model overview"/>
</div>

A lead-conditioned dilated residual trunk decodes each lead from observation history, the CMAQ analysis with its speciated aerosol and gas fields, and an issue-time motion estimate. A **physics-guided correction head** emits a typed, bounded correction state; an **ordered mixture head** emits a two-component uncertainty state. Together they form the decision state — and it is the decision state, not the predicted concentration field, that travels from the draft lead to the target lead.

### The decision state

All fields are handled in log space, `z = log(1 + c)` with `c` in µg/m³, so a correction is multiplicative in concentration and the loss stays finite across the four orders of magnitude the domain spans.

```math
S_k = (A_k,\; U_k)
```

with $A$ the correction state and $U$ the ordered uncertainty state. Both are small groups of bounded spatial maps, and **neither is a concentration**. The concentration field is a product *read from* the state, not a part of it — which is why it never has to re-enter the model.

The single network $f_\theta$ takes everything available at issue time $X_0$, a lead index $k$, and the two groups of transfer channels:

```math
Y = f_\theta(X_0,\, k,\, \tilde A,\, \tilde U)
```

Setting $\tilde A = \tilde U = 0$ recovers plain direct decoding — the baseline every controlled experiment compares against.

### One hop: draft and refine

A target lead is produced in two passes:

```math
D_j = \mathrm{sg}\, f_\theta(X_0,\, j,\, 0,\, 0) \qquad \text{(draft)}
```
```math
(\tilde A_{j\to k},\, \tilde U_{j\to k}) = \mathcal{W}_{j\to k}\big(A[D_j],\, U[D_j]\big) \qquad \text{(transport)}
```
```math
Y_k = f_\theta(X_0,\, k,\, \tilde A_{j\to k},\, \tilde U_{j\to k}) \qquad \text{(refine)}
```

Three properties each close a route by which a predicted field could return:

1. **Both passes read the same issue-time inputs** $X_0$ — the refine pass is conditioned on a decision state and on no predicted concentration.
2. **The draft is itself a plain direct decode** with its transfer channels held at zero — the recursion ends after one hop rather than extending to a chain.
3. **The draft is taken under stop-gradient** — the refine loss never trains the network through the transfer path.

The single hop is a design choice, not a truncated recurrence. What depth would have bought is recovered in training instead: at inference $j = \lceil k/2 \rceil$, but during training $j$ is drawn uniformly from $\{\lceil k/2 \rceil, \dots, k-1\}$, so the transfer is exercised across a range of transport distances. The distance is capped at eight steps (48 h).

### The correction state — and what "physically conditioned" means

> Physical evidence is usually supplied as extra input channels, which widens what a network sees but leaves a residual head free to write any increment anywhere. An increment of unknown size cannot be handed to another valid time without reintroducing the accumulation this framework exists to avoid. **We therefore constrain the output rather than the input.**

For each cell and pollutant the head emits a distribution $\boldsymbol\alpha = \mathrm{softmax}(\ell) \in \Delta^{R-1}$ over $R = 6$ **typed correction rungs** and applies their probability-weighted combination:

```math
\Delta z^{\mathrm{act}}_p = s_p\, a \sum_{r=1}^{R} \alpha_r\, g_r, \qquad a = \tfrac12 + \sigma(h_a) \in (\tfrac12, \tfrac32)
```

```math
(g_1,\dots,g_6) = \big(0,\;\; -\tfrac12\sigma(u_1),\;\; +\tfrac12\gamma\,\sigma(u_2),\;\; \tanh u_3,\;\; -\sigma(u_4),\;\; +\gamma\,\sigma(u_5)\big)
```

for `KEEP`, `SUPP`, `AMPL`, `FINE`, `SUPP⁺⁺`, `AMPL⁺⁺`. Five of the six rungs have a **fixed sign** — what the head selects is a signed choice from a ladder rather than an unconstrained number, and that is what another valid time can read.

Since $\boldsymbol\alpha$ is a convex combination and every rung satisfies $|g_r| < 1$:

```math
\big|\Delta z^{\mathrm{act}}_p\big| < \tfrac{3}{2}\,|s_p|
```

**The composition gate.** The amplifying rungs are gated by the issue-time coarse-particle fraction through a smooth gate:

```math
\phi = \frac{[c_{10} - c_{2.5}]_+}{c_{10} + 1}, \qquad \gamma(\phi) = \sigma\!\left(\frac{\phi - \phi_0}{\tau}\right), \quad \phi_0 = 0.35,\; \tau = 0.1
```

This yields the precise content of the *physically conditioned* claim — a bound holding at **every cell, every lead, for every input and every parameter value of the head**:

```math
0 \;\le\; \Delta z^{\mathrm{ampl}}_p \;\le\; \tfrac{3}{2}\, s_p\, \gamma(\phi)
```

Because $\gamma$ is strictly increasing, **the set of corrections the model is *able* to apply is a monotone function of a measured physical state.** With the fitted $s_{10} = 1.28$, at $\phi = 0$ no input can raise PM<sub>10</sub> by more than **+5.8 %**, against a ceiling of **+577 %** at $\phi = 0.9$. That is a structural property of the architecture, not an outcome of fitting.

> [!IMPORTANT]
> **What PLUME is not.** PLUME is not a chemistry–transport solver. It closes no mass budget over emissions and flux divergence, integrates no reaction kinetics, and minimises no governing-equation residual. Physical knowledge enters at five points — a hard constraint on the output space (above), a soft constraint in the objective ($\mathcal{L}_{\mathrm{regime}} = \mathbb{E}[\alpha_{\mathrm{ampl}}(1-\gamma)]$, the penalty form of an out-of-regime amplification budget), the speciated analysis as leak-safe conditioning, supervision distilled from the reanalysis's own implied tendency, and the transport operator below. The gate is an **admissibility constraint, not an event detector**: at $\phi_0 = 0.35$ it admits 68 % of cells, and it is in the fine-dominated tail that it binds.

Three training terms shape the policy: a divergence to a `KEEP`-favoured usage prior, a penalty on amplification outside the dust gate, and a supervision signal read from whether the reanalysis grows or decays the field between issue time and the valid time.

### The ordered uncertainty state

A model emitting one value per cell absorbs neither the imperfectly known initial state nor what happens before the valid time — deterministic training pulls that value toward the conditional mean and damps the upper outcomes the decision depends on. A standard mixture supplies a second centre, but its components are **exchangeable by construction**, so neither is identified in advance with the higher-concentration outcome. That is what rules a standard mixture out here: exchangeability prevents a component-specific channel from keeping a stable meaning when carried to another cell or lead.

We fix the identity in the parameterisation rather than resolving it afterwards:

```math
\mu^{\mathrm{lo}} = z^0 + \Delta z^{\mathrm{act}}, \qquad \mu^{\mathrm{up}} = \mu^{\mathrm{lo}} + \delta, \qquad \delta = \mathrm{softplus}(h_\delta) > 0
```

Because $\delta > 0$ by construction, $\mu^{\mathrm{up}} > \mu^{\mathrm{lo}}$ at **every** cell and lead. Ordering is a property of the parameterisation, not an outcome of training — so no label switching arises and $\pi$ means the same thing wherever it is read, which is precisely what lets $\pi$ and $\delta$ be transferred.

Two quantities follow:

```math
\mu = \mu^{\mathrm{lo}} + \pi\,\delta \qquad\qquad \sigma^{\mathrm{b}} = \sqrt{\pi(1-\pi)}\;\delta
```

The **between-component spread** $\sigma^{\mathrm{b}}$ is the part of the predictive variance arising from the two components being separated rather than from either being wide — the part a single Gaussian cannot represent. It is largest where the evidence is most undecided.

### What crosses the gap

From the draft decode the model reads **fourteen channels**:

```math
A[D_j] = \big[\alpha_{\mathrm{amp}},\; \alpha_{\mathrm{sup}},\; \alpha_{\mathrm{amp}}-\alpha_{\mathrm{sup}},\; 1-\alpha_{\textsc{keep}},\; \{p^{\mathrm{ev}}_p\},\; \{\Delta z^{\mathrm{act}}_p\}\big]
```
```math
U[D_j] = \big[\{\pi_p\},\; \{\tanh\delta_p\},\; \{p^{\mathrm{raw}}_{\mathrm{exc},p}\}\big]
```

All twelve probability and polarity channels lie in $[-1,1]$ by construction and the two increment channels are clipped. ***The absolute predicted concentration field is not among them.***

Each map is advected before it is read, by a one-shot backward-characteristic (semi-Lagrangian) step:

```math
\mathcal{W}_{j\to k}[M](\mathbf{x}) = M\big(\mathbf{x} - \mathbf{v}_p(\mathbf{x})\,(k-j)\,\Delta t\big), \qquad \Delta t = 6\,\mathrm{h}
```

This is the first-order discretisation of the pure advection equation $\partial_t M + \mathbf{v}\cdot\nabla M = 0$, exact for spatially uniform $\mathbf{v}$, with no diffusion and no source term — so what the refine pass reads at a cell is the draft's decision for the air *arriving* there. The physics enters the transfer as transport; the content being transported is estimated from data.

### Three products from one distribution

| Product | Formula | Scored by |
|---|---|---|
| **Concentration forecast** | $\hat c = \exp(\mu) - 1$ | RMSE, MAE, mean bias |
| **Exceedance probability** | closed form (two-Gaussian mixture, below) | Brier, log score, reliability, coverage |
| **Decision score** | $\hat z^{\mathrm{dec}} = \mu + \kappa_{p,k}\,\sigma^{\mathrm{b}}$ | CSI, ETS, SEDI, POD, SR |

```math
p^{\mathrm{raw}}_{\mathrm{exc}} = (1-\pi)\,\overline\Phi\!\left(\frac{\log(1+\tau) - \mu^{\mathrm{lo}}}{\sigma_{\mathrm{lo}}}\right) + \pi\,\overline\Phi\!\left(\frac{\log(1+\tau) - \mu^{\mathrm{up}}}{\sigma_{\mathrm{up}}}\right)
```

The decision score is an **upward risk adjustment**, not an estimate of the conditional mean. It moves the decision only where the two components genuinely separate (since $\sigma^{\mathrm{b}} \to 0$ as $\pi \to 0$ or $1$), and the softplus makes it one-directional so the decision can buy sensitivity but never sell it. Because it raises the field, **the concentration forecast and the decision score are reported separately throughout**.

---

## Results

Evaluation is at station locations pooled over all twenty leads, with exceedance at PM<sub>10</sub> > 80 and PM<sub>2.5</sub> > 35 µg/m³. External systems are produced on their own native grids (0.4° for Aurora-AP, 27 km for FAKER-Air<sub>GRPO</sub>) and sampled to our 0.25° station cells by nearest neighbour, so that comparison is contextual rather than strictly matched; the causal claims rest on the matched internal experiments.

### Against operational and foundation-model forecasts (2023)

<table>
<tr><th>Region</th><th>Model</th><th>POD ↑</th><th>SR ↑</th><th>CSI ↑</th><th>ETS ↑</th><th>SEDI ↑</th><th>RMSE ↓</th><th>MB → 0</th></tr>
<tr><td colspan="9" align="center"><i>(a) PM<sub>10</sub></i></td></tr>
<tr><td rowspan="4"><b>East Asia</b><br><sub>20.4 % base rate</sub></td><td>CAMS forecast</td><td>42.71</td><td>51.09</td><td>30.31</td><td>20.74</td><td>49.10</td><td>67.35</td><td>−7.21</td></tr>
<tr><td>Aurora-AP</td><td>50.48</td><td>53.67</td><td>35.16</td><td>25.17</td><td>56.64</td><td>64.88</td><td>−3.66</td></tr>
<tr><td>FAKER-Air<sub>GRPO</sub></td><td>49.05</td><td><b>56.29</b></td><td>35.52</td><td>24.98</td><td>55.46</td><td>70.43</td><td>−11.59</td></tr>
<tr><td><b>PLUME</b></td><td><b>74.55</b></td><td>53.70</td><td><b>45.38</b></td><td><b>35.31</b></td><td><b>75.96</b></td><td><b>59.42</b></td><td><b>+1.45</b></td></tr>
<tr><td rowspan="4"><b>Korea</b><br><sub>6.7 %</sub></td><td>CAMS forecast</td><td>13.46</td><td>32.02</td><td>10.47</td><td>8.47</td><td>33.14</td><td>31.58</td><td>−4.53</td></tr>
<tr><td>Aurora-AP</td><td>12.14</td><td>37.85</td><td>10.12</td><td>8.49</td><td>34.71</td><td>30.49</td><td>−2.75</td></tr>
<tr><td>FAKER-Air<sub>GRPO</sub></td><td>15.52</td><td>45.36</td><td>13.08</td><td>10.70</td><td>37.40</td><td>36.90</td><td>−14.72</td></tr>
<tr><td><b>PLUME</b></td><td><b>29.39</b></td><td><b>47.14</b></td><td><b>22.11</b></td><td><b>19.89</b></td><td><b>54.46</b></td><td><b>26.30</b></td><td><b>−1.98</b></td></tr>
<tr><td rowspan="4"><b>CN dust corridor</b><br><sub>36.8 %</sub></td><td>CAMS forecast</td><td>36.63</td><td>60.23</td><td>29.50</td><td>13.99</td><td>35.26</td><td>114.93</td><td>−27.39</td></tr>
<tr><td>Aurora-AP</td><td>26.97</td><td><b>70.87</b></td><td>24.28</td><td>13.35</td><td>37.84</td><td>112.30</td><td>−37.38</td></tr>
<tr><td>FAKER-Air<sub>GRPO</sub></td><td>31.83</td><td>59.54</td><td>26.17</td><td>11.92</td><td>31.47</td><td>112.52</td><td>−34.09</td></tr>
<tr><td><b>PLUME</b></td><td><b>85.63</b></td><td>56.03</td><td><b>51.22</b></td><td><b>29.64</b></td><td><b>68.28</b></td><td><b>109.08</b></td><td><b>+0.45</b></td></tr>
<tr><td colspan="9" align="center"><i>(b) PM<sub>2.5</sub></i></td></tr>
<tr><td rowspan="4"><b>East Asia</b><br><sub>28.0 %</sub></td><td>CAMS forecast</td><td>68.92</td><td>52.95</td><td>42.74</td><td>26.01</td><td>60.30</td><td>27.60</td><td>+3.04</td></tr>
<tr><td>Aurora-AP</td><td>74.76</td><td>53.70</td><td>45.46</td><td>28.51</td><td>65.29</td><td>26.23</td><td>+5.66</td></tr>
<tr><td>FAKER-Air<sub>GRPO</sub></td><td>55.06</td><td><b>57.48</b></td><td>39.12</td><td>23.45</td><td>52.60</td><td>29.46</td><td>−6.18</td></tr>
<tr><td><b>PLUME</b></td><td><b>79.67</b></td><td>55.70</td><td><b>48.77</b></td><td><b>34.09</b></td><td><b>73.81</b></td><td><b>22.44</b></td><td><b>+2.39</b></td></tr>
<tr><td rowspan="4"><b>Korea</b><br><sub>10.1 %</sub></td><td>CAMS forecast</td><td>45.88</td><td>32.56</td><td>23.53</td><td>17.52</td><td>52.38</td><td>13.61</td><td>+1.91</td></tr>
<tr><td>Aurora-AP</td><td><b>49.28</b></td><td>37.46</td><td>27.04</td><td>21.31</td><td>58.39</td><td>13.11</td><td>+3.33</td></tr>
<tr><td>FAKER-Air<sub>GRPO</sub></td><td>20.54</td><td>44.83</td><td>16.40</td><td>11.61</td><td>34.67</td><td>20.09</td><td>−8.95</td></tr>
<tr><td><b>PLUME</b></td><td>43.75</td><td><b>44.65</b></td><td><b>28.37</b></td><td><b>24.22</b></td><td><b>60.29</b></td><td><b>11.60</b></td><td><b>+0.15</b></td></tr>
<tr><td rowspan="4"><b>CN dust corridor</b><br><sub>34.9 %</sub></td><td>CAMS forecast</td><td>56.08</td><td>57.33</td><td>39.57</td><td>20.41</td><td>47.26</td><td>35.31</td><td>−3.54</td></tr>
<tr><td>Aurora-AP</td><td>52.12</td><td><b>62.62</b></td><td>39.75</td><td>22.62</td><td>50.40</td><td>31.87</td><td>−7.52</td></tr>
<tr><td>FAKER-Air<sub>GRPO</sub></td><td>37.11</td><td>50.99</td><td>27.35</td><td>10.64</td><td>27.58</td><td>38.66</td><td>−11.09</td></tr>
<tr><td><b>PLUME</b></td><td><b>84.29</b></td><td>53.77</td><td><b>48.87</b></td><td><b>28.20</b></td><td><b>67.05</b></td><td><b>30.86</b></td><td><b>+3.22</b></td></tr>
</table>

PLUME takes the strongest chance-corrected exceedance skill (ETS) in all six targets — **+10.14** over East-Asian PM<sub>10</sub>, **+9.19** over Korean PM<sub>10</sub>, **+15.65** in the dust corridor — and the strongest CSI, SEDI, RMSE and mean bias in all six as well.

> **Detection can always be bought by lowering a threshold, so we separate the two readings.** Detection did rise together with alarm frequency: frequency bias over East-Asian PM<sub>10</sub> is 1.39 against 0.84–0.94 for the baselines. What makes the exchange favourable is that **SEDI already prices it** — SEDI is built from the detection rate and the false-alarm rate and is invariant to the base rate, and it improves by +19.32, +17.06 and +30.44 on PM<sub>10</sub>. Success ratio is the one column we do not lead; we report the deployed operating point as it is rather than at unit bias.

### Where the gain sits in lead time

<div align="center">
<img src="assets/per_lead_gain_pm10.png" width="100%" alt="Effect of the decision state by lead and region, PM10"/>
</div>

Over Korea the detection gain averages **+9.16** points and peaks at **+20.01** at +42 h, while the chance-corrected gain peaks later and larger — **+12.12 CSI, +11.07 ETS, +15.49 SEDI at +54 h**.

This is where the framework should help *by construction*. At short leads the anchor already contains the answer and a draft has nothing to add. In the 42–54 h band the outcome is still determined by air the issue-time analysis has seen, but no longer by the anchor value at the target cell — and it is exactly there that a state carrying what the evidence settled and what it left open has something to say. Beyond that band the state has nothing left to carry. **The peak therefore falls between two regimes in which decision transfer cannot help, and not at the shortest leads where a rollout would gain most.**

<div align="center">
<img src="assets/per_lead_time.png" width="100%" alt="Skill against lead time, 2023"/>
</div>

### Where the gain lands geographically

<div align="center">
<img src="assets/per_region_kr.png" width="49%" alt="Per-province skill over Korea"/>
<img src="assets/per_region_dust_corridor.png" width="49%" alt="Per-prefecture skill in the CN dust corridor"/>
</div>

For PM<sub>10</sub> the improvement is **universal**: all 24 regions gain, by +3.64 CSI and +6.87 POD on average, and every Korean province gains on SEDI as well — so the extra detections survive their alarm cost at province scale and not only in the pooled figure. PM<sub>2.5</sub> is weaker and not universal (21 of 24 regions gain, by +1.19 CSI on average).

### Second test year (2024)

2024 is evaluated **once**, with the model, the decision rule and the calibration unchanged. Station observations in the archive end on 16 July 2024, so these scores cover 2 January to 16 July.

| Target | CSI | ETS | SEDI | POD | RMSE | MB |
|---|---|---|---|---|---|---|
| EA · PM<sub>10</sub> | 41.07 | 31.47 | 71.69 | 69.57 | 51.68 | +4.23 |
| KR · PM<sub>10</sub> | 16.99 | 15.30 | 49.15 | 23.69 | 26.54 | +2.13 |
| Dust corridor · PM<sub>10</sub> | 47.30 | 22.29 | 56.87 | 83.03 | 114.30 | +3.07 |
| EA · PM<sub>2.5</sub> | 45.45 | 29.95 | 68.48 | 76.23 | 24.51 | +2.70 |
| KR · PM<sub>2.5</sub> | 19.27 | 14.59 | 46.96 | 37.49 | 12.69 | +2.19 |
| Dust corridor · PM<sub>2.5</sub> | 49.08 | 24.81 | 59.89 | 82.34 | 32.65 | +2.99 |

> [!NOTE]
> **Evaluation protocol, stated plainly.** The network is trained on 2016–2021, and the checkpoint is selected on 2022. 2023 and 2024 are independent test years: neither contributes to fitting or checkpoint selection, and both use the same weights and decision rule. All internal comparisons share one grid, one station mask, one truth field, one batch size and one hardware configuration, so a difference between two rows is attributable to the change between them.

---

## Installation

```bash
git clone https://github.com/kaist-cvml/PLUME.git
cd plume

conda create -n plume python=3.10 -y
conda activate plume

pip install -r requirements.txt
# optional: map basemaps for plume/viz.py
# conda install -c conda-forge cartopy
```

Verify:

```bash
python -c "from models.model import build_model, DUST_COARSE_FRAC_THR; print('ok, gate phi0 =', DUST_COARSE_FRAC_THR)"
```

**Hardware.** The deployed configuration trains on a single NVIDIA A6000 (48 GB) at batch size 12. Multi-GPU works through `torchrun`; batch size and `--max-train-samples` stay global.

---

## Data

The preprocessed archive lives on the HuggingFace Hub:

### 🤗 [**2na-97/PLUME**](https://huggingface.co/datasets/2na-97/PLUME)

It supersedes [`2na-97/FAKER-Air`](https://huggingface.co/datasets/2na-97/FAKER-Air) (27 km grid) with a **0.25° East-Asia grid, 117 × 222 cells**, hourly, 2016–2024.

| Tree | Contents | Size |
|---|---|---|
| `cmaq_asia_1h_0p25/` | CMAQ reanalysis: 12-species speciated aerosol + gas/column fields, surface proxy stack | 9.3 GB/yr download · 17 GB/yr on disk |
| `obs_asia_1h_0p25/` | Ground-station observations gridded to the same cells, with validity and region masks | 0.4 GB/yr download · 5 GB/yr on disk |
| `checkpoints/` | Trained PLUME weights, deployed configuration & 4 seeds | 158 MB |

Each year is one `.tar.zst` shard per tree, so you can fetch only what you need.

### Download

```bash
# Evaluation years only -- enough to reproduce every reported number (19 GB download, 44 GB on disk)
python scripts/download_data.py --years 2023 2024

# The full training record (88 GB download, 196 GB on disk)
python scripts/download_data.py --all

# One tree, one year (0.4 GB download, 5 GB on disk)
python scripts/download_data.py --years 2023 --tree obs

# The released checkpoints (158 MB)
python scripts/download_data.py --checkpoints
```

Re-running is safe — a year already extracted is skipped, and the Hub download resumes.

<details>
<summary><b>Manual download with <code>huggingface_hub</code></b></summary>

```python
from huggingface_hub import hf_hub_download

shard = hf_hub_download(
    repo_id="2na-97/PLUME",
    repo_type="dataset",
    filename="obs_asia_1h_0p25/2023.tar.zst",
)
# then:  tar --use-compress-program=unzstd -xf $shard -C data/obs_asia_1h_0p25
```

Or grab whole subtrees:

```python
from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="2na-97/PLUME", repo_type="dataset",
    allow_patterns=["cmaq_asia_1h_0p25/2023.tar.zst", "obs_asia_1h_0p25/2023.tar.zst"],
    local_dir="downloads",
)
```
</details>

### Layout after extraction

```
data/
├── cmaq_asia_1h_0p25/YYYY/MM/DD/NIER_27_01/
│   ├── YYYYMMDD_x_aurora_surf.npy      float32 [25, 13, 117, 222]  surface stack (memory-mapped)
│   ├── YYYYMMDD_x_cmaq_cams_sp12.npy   float16 [25, 12, 117, 222]  speciated aerosol + gas
│   ├── YYYYMMDD_meta.json
│   └── cams_lat.npy, cams_lon.npy, cams_grid_meta.json
└── obs_asia_1h_0p25/YYYY/MM/DD/NIER_27_01/
    ├── YYYYMMDD_y_obs_cams.npz         keys: obs_values, obs_mask, obs_count,
    │                                         region_id, source_id, station_count, lat, lon
    ├── YYYYMMDD_y_obs_cams_pmvals.npy  float32 [25, 2, 117, 222]  PM2.5, PM10 in ug/m3
    ├── YYYYMMDD_y_obs_cams_pmmask.npy  uint8   [25, 2, 117, 222]  1 where a station reported
    ├── YYYYMMDD_y_obs_cams_region.npy  int16   [25, 117, 222]     region ID per cell
    ├── YYYYMMDD_obs_meta.json
    ├── YYYYMMDD_station_map.csv        station-to-cell assignment for that day
    └── cams_lat.npy, cams_lon.npy, cams_grid_meta.json
```

The leading `T = 25` axis is a day's 00–23 hourly slots plus one wrap slot. `*_x_cmaq_cams_sp12.npy` is the precomputed 12-channel selection the model reads; the full 24-channel concentration stack (`*_x_cmaq_cams.npz`) is retained for one sample day per year only, and `data/dataset.py` falls back to it when the `sp12` file is absent.
 Channel orders are defined in [`plume/gridio.py`](plume/gridio.py) (observations) and [`plume/species.py`](plume/species.py) (CMAQ concentrations).

> [!WARNING]
> **CMAQ at the target valid time is never a model input.** It appears only as a training-time teacher label. Everything in $X_0$ is available at issue time, so the system does not wait on a chemistry–transport forecast cycle. The dataset loader enforces this; see the `--causal-student` flag.

---

## Training

```bash
# The deployed recipe -- reproduces the paper checkpoint
bash configs/train_plume.sh

# Another seed
SEED=20260703 bash configs/train_plume.sh

# Four GPUs (batch size stays global)
LAUNCH="torchrun --standalone --nproc_per_node=4" bash configs/train_plume.sh

# Data somewhere else
DATA_ROOT=/mnt/plume-data bash configs/train_plume.sh
```

[`configs/train_plume.sh`](configs/train_plume.sh) is annotated block by block — trunk, inputs, correction state, uncertainty state, one-hop transfer, event shaping. Every flag it passes is validated against `train.py`.

### The objective

```math
\mathcal{L} = \underbrace{\mathcal{L}_{\mathrm{field}}}_{\text{concentration}} + \underbrace{\mathcal{L}_{\mathrm{dist}}}_{\text{uncertainty state}} + \underbrace{\mathcal{L}_{\mathrm{event}}}_{\text{decision}} + \underbrace{\mathcal{L}_{\mathrm{struct}}}_{\text{correction state and transfer}}
```

| Group | What it does | Key flags |
|---|---|---|
| $\mathcal{L}_{\mathrm{field}}$ | robust regression on the mixture mean, up-weighted on exceedance cells and the spring dust season, plus distillation toward the reanalysis where no station reports | `--event-weight`, `--mam-event-weight`, `--lambda-teacher` |
| $\mathcal{L}_{\mathrm{dist}}$ | mixture likelihood fixing $\pi$, $\delta$ and the component scales; an **unweighted** Brier score so it stays proper; the same likelihood against the reanalysis teacher on unobserved cells | `--lambda-nll`, `--lambda-brier`, `--lambda-nll-teacher` |
| $\mathcal{L}_{\mathrm{event}}$ | auxiliary exceedance cross-entropy and a soft threshold-detection term — the only event-weighted terms acting on the decision | `--lambda-event`, `--lambda-soft-f1` |
| $\mathcal{L}_{\mathrm{struct}}$ | correction-policy terms, transport consistency, asymmetric PM<sub>10</sub> under-bias guard | `--lambda-regime`, `--lambda-action-prior`, `--lambda-action-distill`, `--lambda-action-consist` |

Gradient routing follows the graph: the draft decode is under stop-gradient, and $\sigma^{\mathrm{b}}$ is detached inside $\mathcal{L}_{\mathrm{event}}$ so the event terms move the operating point $\kappa$ without reshaping the distribution.

> Stations cover ~2.3 % of the grid, so `--lambda-nll-teacher` matters more than its coefficient suggests: without it the transferred uncertainty maps are trained only where a station reports and carry no usable structure elsewhere.

---

## Evaluation

```bash
# Full-year regional metrics from a checkpoint
python evaluate.py \
  --checkpoint checkpoints/plume_s20260702/best_composite.pth \
  --val-start 2023010100 --val-end 2023123123 \
  --out-dir runs/eval_2023

# Second test year
python evaluate.py --checkpoint <ckpt> --val-start 2024010100 --val-end 2024123123 --out-dir runs/eval_2024

# Per-region breakdown (19 KR provinces + CN dust-corridor prefectures)
python scripts/eval_regions.py --ckpt <ckpt> --out runs/regions_2023.json
```

Outputs are JSON plus a per-region CSV. Metric definitions live in [`plume/metrics.py`](plume/metrics.py); field metrics are computed from $\mu$ and categorical metrics from $\hat z^{\mathrm{dec}}$, reported separately throughout.

### Lesion studies

`scripts/eval_regions.py` accepts `--lesion` to ablate the transferred state at inference on frozen weights:

| Lesion | What it does |
|---|---|
| `none` | baseline |
| `P` / `U` / `PU` | zero the correction / uncertainty / both transfer groups |
| `Pshuf` / `Ushuf` | keep the maps, destroy their spatial alignment |
| `Pswap` | exchange the amplify and suppress recommendations, negate polarity |
| `Pact05` / `Pact20` | dose the typed action channels ×0.5 / ×2 |
| `noadvP` / `noadvU` | skip advection, read the draft's maps in place |

---

## Analysis: inspecting the decision state

Two scripts probe whether the state means what it is named.

**Physical grounding of the correction state.** Bins the model's own action probabilities by the issue-time composition proxy $\phi$ and by season, giving $P(\textsc{ampl} \mid \phi, \text{season})$ curves:

```bash
python scripts/action_grounding.py \
  --ckpt checkpoints/plume_s20260702/best_composite.pth \
  --year 2023 --stride 3 --grounding-only \
  --out runs/grounding_2023.npz
```

Measured on the deployed checkpoint over the broad domain, amplification usage falls from **0.342** in the upper quintiles to **0.062** in the bottom coarse-fraction quintile — a 5.5× drop — while `KEEP` rises to **0.889**, so the head goes near-inert where the gate binds. Within the two event regions, where $\phi$ spans the gate, usage rises **monotonically** with $\phi$ (Korea $r = +0.99$ over q1–q4). Both reproduce on the held-out year.

Drop `--grounding-only` to add the **commanded-action intervention**: the typed channels are re-injected at levels $c \in \{-1, -\tfrac12, 0, +\tfrac12, +1\}$ with content channels untouched, and the target decision margin must respond monotonically if the state is an action representation rather than an arbitrarily named latent.

**Do the chemistry channels steer the decision?** Ablates a channel group at inference (batch-shuffled, so each channel's marginal is preserved while spatial alignment is destroyed) and reports how far the action distribution moves:

```bash
python scripts/action_attribution.py --ckpt <ckpt> --out runs/attrib --max-batches 60
```

Read the numbers *relative to the controls*: `coords` (lat/lon/time — should matter) and `none` (exactly 0 by construction, a plumbing check).

> [!NOTE]
> This is a falsifiable test that we report rather than an assumed property. As a plain concatenated input, chemistry is largely redundant given the PM initialisation field — shuffling all 18 chemistry channels moves the action distribution by KL 0.003. The physical conditioning that **does** carry weight is the composition gate and the regime penalty, both of which are structural and measurable (see [the correction state](#the-correction-state--and-what-physically-conditioned-means)).

---

## Repository layout

```
plume/
├── plume/                      # self-contained support package (no external model deps)
│   ├── gridio.py               # date hierarchy, grid boxes, OBS channel order
│   ├── species.py              # CMAQ speciated-concentration channel order
│   ├── metrics.py              # CSI / ETS / SEDI / POD / SR / field metrics
│   ├── loader.py               # load a checkpoint -> dataset + model
│   ├── viz.py                  # per-lead spatial map panels
│   └── vizbase.py              # colormaps, basemaps, cropping
├── models/
│   ├── model.py                # trunk, ActionResidualHead, ObjectActionHead, wrappers
│   ├── uncertainty.py          # ordered two-component mixture head
│   └── transport.py            # semi-Lagrangian advection + state assembly
├── data/
│   └── dataset.py              # DirectLeadDataset: issue-time inputs, leak-safe
├── train.py                    # training loop and the full objective
├── evaluate.py                 # full-year evaluation and region vocabulary
├── configs/train_plume.sh      # the deployed recipe, annotated
├── scripts/
│   ├── download_data.py        # fetch data / checkpoints from HuggingFace
│   ├── eval_regions.py         # regional metrics + lesion studies
│   ├── action_grounding.py     # physical grounding + commanded-action response
│   └── action_attribution.py   # channel-group attribution on the action decision
└── assets/                     # paper figures
```

### Key entry points in the code

| What | Where |
|---|---|
| The composition gate $\gamma(\phi)$ | [`models/model.py`](models/model.py) · `dust_gate_from_coarse_frac` |
| The typed correction ladder | [`models/model.py`](models/model.py) · `ActionResidualHead.forward` |
| The ordered mixture | [`models/uncertainty.py`](models/uncertainty.py) · `TwoComponentMDNHead` |
| Semi-Lagrangian transport | [`models/transport.py`](models/transport.py) · `advect_field` |
| The 14 transferred channels | [`models/transport.py`](models/transport.py) · `build_uncertainty_feedback` |
| The regime penalty | [`train.py`](train.py) · `compute_loss`, `lambda_regime` block |
| Action distillation from CMAQ | [`train.py`](train.py) · `compute_loss`, `lambda_action_distill` block |

---

## Reproducing the paper

```bash
# 1. data
python scripts/download_data.py --all

# 2. train the deployed configuration (4 seeds as reported)
for s in 20260702 20260703 20260704 20260705; do SEED=$s bash configs/train_plume.sh; done

# 3. first test year
python evaluate.py --checkpoint checkpoints/plume_s20260702/best_composite.pth \
  --val-start 2023010100 --val-end 2023123123 --out-dir runs/eval_2023

# 4. second test year, model and decision rule unchanged
python evaluate.py --checkpoint checkpoints/plume_s20260702/best_composite.pth \
  --val-start 2024010100 --val-end 2024123123 --out-dir runs/eval_2024

# 5. decision-state diagnostics
python scripts/action_grounding.py --ckpt checkpoints/plume_s20260702/best_composite.pth \
  --year 2023 --grounding-only --out runs/grounding_2023.npz
```

To skip training, fetch the released weights with `python scripts/download_data.py --checkpoints`.

**Ablations.** The component factorial is reached by dropping flags from `configs/train_plume.sh`:

| Row | Change |
|---|---|
| D (direct decoding) | drop `--action-head`, `--unc-mdn`, `--action-feedback`, `--transfer-uncertainty` |
| D + P | drop `--unc-mdn`, `--transfer-uncertainty` |
| D + U | drop `--action-head`, `--action-feedback` |
| D + P + U | the full recipe as shipped |
| no composition gate | drop `--gated-action` and set `--lambda-regime 0` |
| tighter gate | add `--dust-thr 0.60` (or `0.75`) |

> Transport requires a wind field, so the three cells that transfer a state also see the issue-time motion estimate while the row with neither does not — part of what separates that row from the others is an input rather than a head.

---

## Citation

```bibtex
@article{plume2025,
  title   = {Physically conditioned correction and ordered uncertainty
             for multiday particulate forecasting over East Asia},
  author  = {Kang, Inha and Ryu, Wonjeong and Hong, Sung-Chul and
             Lee, Jae-Bum and Ban, SooJin and Jeong, Seongeun and
             Kang, Yoon-Hee and Kim, Soontae and Shim, Hyunjung},
  year    = {2025},
  note    = {Code: https://github.com/kaist-cvml/PLUME}
}
```

Related: [FAKER-Air](https://huggingface.co/datasets/2na-97/FAKER-Air), the 27 km predecessor dataset.

---

## Acknowledgements

Observations are from the Korean national air-quality monitoring network and regional partners; the reanalysis is CMAQ. The dataloading and grid conventions began as a fork of the [Aurora](https://github.com/microsoft/aurora) preprocessing stack — the released code carries no dependency on it.

## License

[MIT](LICENSE). The dataset is released under the terms stated on its [HuggingFace card](https://huggingface.co/datasets/2na-97/PLUME).
