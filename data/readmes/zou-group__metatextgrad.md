<!--- BADGES: END --->

# metaTextGrad: Automatically optimizing language model optimizers

[![GitHub license](https://img.shields.io/badge/License-MIT-blue.svg)][#license-gh-package]
[![NeurIPS 2025](https://img.shields.io/badge/NeurIPS%202025-Poster-green.svg)](https://openreview.net/pdf?id=10s01YrlKp)
[![Arxiv](https://img.shields.io/badge/arXiv-2505.18524-B31B1B.svg)][#arxiv-paper-package]

[#license-gh-package]: https://lbesson.mit-license.org/
[#arxiv-paper-package]: https://arxiv.org/abs/2505.18524

A meta-optimizer — for optimizing LLM optimizers!

metaTextGrad automatically optimizes LLM-based optimizers like TextGrad and ADAS through meta prompt and structure optimization, achieving stronger performance and better task alignment.

![Teaser](assets/teaser.png)

## 📣 Updates

- **[November 2025]** The code for metaTextGrad is now released.

- **[September 2025]** metaTextGrad is published at NeurIPS 2025. Check out our [paper](https://openreview.net/pdf?id=10s01YrlKp) for more details.

- **[May 2025]** metaTextGrad is now released. Check out our [preprint](https://arxiv.org/abs/2505.18524) on arXiv.

## 🛠️ Installation

To set up the environment for metaTextGrad, please follow the steps below:

```bash
conda create -n metatextgrad python=3.10
conda activate metatextgrad
cd textgrad
pip install -e .
```

Since we’ve modified the original TextGrad codebase, make sure to install TextGrad from our repository rather than the official one.

## 🚀 Motivating Example

Existing LLM-based optimizers like **TextGrad** and **DSPy** are manually designed to perform well across many different tasks. Their prompts are highly general. For example:

> You are part of an optimization system that improves text (i.e., variable). You will be asked to creatively and critically improve prompts, solutions to problems, code, or any other text-based variable.

However, this generality can sometimes limit their effectiveness on specific tasks.  
When the optimizer only receives noisy feedback, such as overly detailed textual suggestions:

> To improve the prompt for the executer and enhance the objective function, consider the following feedback: 1. **Explicit Criteria Definition**: The prompt should explicitly instruct the executer to define the criteria for optical activity at the beginning of the response. This can prevent ambiguity and ensure that the executer uses the correct scientific principles. For example, the prompt could include a directive to "List the criteria for optical activity before analyzing each compound." 2. **Data Verification Directive**: Incorporate a step in the prompt that requires the executer to verify the input data against reliable sources. This could be phrased as "Cross-check the properties of each compound with a trusted chemical database before proceeding with the analysis." 3. **Structured Logical Reasoning**: Encourage a structured approach to reasoning by breaking down the analysis into distinct steps. The prompt could suggest a format like "For each compound, first identify chiral centers, then assess symmetry, and finally determine optical activity". 4. **Cross-Referencing Encouragement**: ... By incorporating these elements into the prompt, the executer can be guided to produce more accurate and reliable responses, thereby improving alignment with the ground truth answer and enhancing the objective function.

It may incorporate irrelevant information and fail to improve the model effectively.

In contrast, a **task-specific optimizer** can be explicitly aligned with the target task distribution.  
For instance, an optimizer optimizaed for _Dyck Languages (bracket matching)_ might include guidance such as focusing on _proper nesting_ and _LIFO order_:

> You are part of an optimization system specialized in improving prompts for bracket matching and sequence completion tasks. Your role is to enhance prompts that help solve Dyck language problems, which involve proper nesting and closure of different types of brackets ({}, <>, ()). When improving prompts, focus on these critical aspects: (1) maintaining accurate bracket pair matching, (2) preserving the LIFO (Last In First Out) order of nested structures, (3) handling multiple bracket types simultaneously, and (4) ensuring complete closure of all open brackets. You should critically analyze how the prompts can better guide the model to track open brackets, maintain proper nesting order, and systematically complete sequences. Consider incorporating pattern recognition strategies and explicit validation rules in the improved prompts. Your improvements should lead to more reliable and accurate bracket sequence completions.

Such alignment helps the optimizer produce better programs even when the feedback remains noisy. Therefore, rather than designing new optimizers manually for every task, **metaTextGrad** aims to _meta-learn how to adapt optimizers automatically_ and create optimizers that are both stronger and task-aligned.

## 💻 Code Usage

Below are examples of how to run **metaTextGrad** and its baselines.  
The baselines include standard prompting methods (e.g., Zero-shot, Few-shot, CoT), as well as optimization-based methods like **TextGrad**, **ADAS-TG**, and **MIPROv2**.  
At the end, we show how to run **metaTextGrad**.

---

### 🔹 Vanilla Prompting Methods

Zero-shot CoT:

```bash
python zero_shot_cot.py --task BBH_word_sorting
```

Few-shot CoT with 8 demonstrations:

```bash
python few_shot_cot.py --task BBH_word_sorting
```

Self-consistency (samples multiple reasoning paths and aggregates):

```bash
python self_consistency.py --task BBH_word_sorting
```

Best-of-N (selects best answer from multiple generations):

```bash
python best_of_n.py --task BBH_word_sorting
```

---

### 🔹 TextGrad & ADAS-TG Baselines

**TextGrad TGD** — the gradient-descent-like optimization baseline using textual feedback:

```bash
python textgrad_baselines.py --optimizer TGD --task BBH_word_sorting
```

**ADAS-TG** — our implementation of ADAS (Meta Agent Search) within the TextGrad framework:

```bash
python textgrad_baselines.py --optimizer PipelineOptimizer --task BBH_word_sorting
```

---

### 🔹 DSPy Baselines

**Zero-shot MIPROv2** — no demonstrations:

```bash
python dspy_baselines.py --demo 0 --task BBH_word_sorting
```

**Few-shot MIPROv2** — with 8 demonstrations:

```bash
python dspy_baselines.py --demo 8 --task BBH_word_sorting
```

---

### 🔹 metaTextGrad

```bash
python meta_optimization.py --task BBH_word_sorting
```

You can use the `--run_structure_optimization` flag to enable meta structure optimization. However, please control the number of optimization epochs and monitor your API usage carefully, as this process may cost tens of dollars or more. Therefore, this option is disabled by default.

---

### 🧩 Running Other Tasks

You can run other tasks by changing the `--task` argument.
Available tasks include:

- `MMLUs` (MMLU Abstract Algebra)
- `BBH_word_sorting`
- `BBH_dyck_languages`
- `GPQA_diamond`

## 📝 Resources

### Inspiration

Many existing works greatly inspired this project! Here is a non-exhaustive list:

- 📚 [**TextGrad**](https://github.com/zou-group/textgrad) — the core codebase our work is built upon.
- 📚 [**DSPy**](https://github.com/stanfordnlp/dspy) — a pioneering framework for building LM-based programs in diverse ways.
- 📚 [**ADAS**](https://github.com/ShengranHu/ADAS) — uses Meta Agent Search to show that agents can invent novel and powerful designs; we use this idea within the TextGrad framework to implement ADAS-TG.

### Citation

```bibtex
@inproceedings{
xu2025metatextgrad,
title={metaTextGrad: Automatically optimizing language model optimizers},
author={Guowei Xu and Mert Yuksekgonul and Carlos Guestrin and James Zou},
booktitle={The Thirty-ninth Annual Conference on Neural Information Processing Systems},
year={2025},
url={https://openreview.net/forum?id=10s01YrlKp}
}
```

### 🙏 Contributors

We are grateful for all the help we got from our contributors!

<!-- readme: contributors -start -->
<table>
    <tbody>
        <tr>
            <td align="center">
                <a href="https://github.com/XuGW-Kevin">
                    <img src="https://avatars.githubusercontent.com/u/113534787?v=4" width="100;" alt="guowei"/>
                    <br />
                    <sub><b>Guowei Xu</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/mertyg">
                    <img src="https://avatars.githubusercontent.com/u/29640736?v=4" width="100;" alt="mertyg"/>
                    <br />
                    <sub><b>Mert Yuksekgonul</b></sub>
                </a>
            </td>
        </tr>
    <tbody>
</table>
<!-- readme: contributors -end -->
