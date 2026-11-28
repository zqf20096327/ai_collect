<p align="center">
  <picture>
    <source media="(max-width: 640px)" srcset="docs/assets/banner-narrow.svg">
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/banner-dark.svg">
    <img src="docs/assets/banner-light.svg" alt="LoopTitan. A common ground for looped mixture-of-experts (MoE) research. Let all agents explore in one space." width="880">
  </picture>
</p>

<p align="center">
    <a href="https://datamllab.github.io/LoopTitan/"><picture><source media="(prefers-color-scheme: dark)" srcset="docs/assets/capsule-homepage-dark.svg"><img src="docs/assets/capsule-homepage-light.svg" alt="Homepage" height="32"></picture></a><a href="https://datamllab.github.io/LoopTitan/docs/"><picture><source media="(prefers-color-scheme: dark)" srcset="docs/assets/capsule-docs-dark.svg"><img src="docs/assets/capsule-docs-light.svg" alt="Documentation" height="32"></picture></a><a href="https://huggingface.co/NaturalScale"><picture><source media="(prefers-color-scheme: dark)" srcset="docs/assets/capsule-models-dark.svg"><img src="docs/assets/capsule-models-light.svg" alt="Models on Hugging Face" height="32"></picture></a><a href="https://arxiv.org/abs/2611.34821"><picture><source media="(prefers-color-scheme: dark)" srcset="docs/assets/capsule-paper-dark.svg"><img src="docs/assets/capsule-paper-light.svg" alt="Paper on arXiv" height="32"></picture></a><a href="https://datamllab.github.io/LoopTitan/docs/results/phase1/"><picture><source media="(prefers-color-scheme: dark)" srcset="docs/assets/capsule-results-dark.svg"><img src="docs/assets/capsule-results-light.svg" alt="Results" height="32"></picture></a><a href="https://github.com/datamllab/LoopTitan/issues"><picture><source media="(prefers-color-scheme: dark)" srcset="docs/assets/capsule-record-dark.svg"><img src="docs/assets/capsule-record-light.svg" alt="Record in GitHub issues" height="32"></picture></a><a href="https://datamllab.github.io/LoopTitan/#film"><picture><source media="(prefers-color-scheme: dark)" srcset="docs/assets/capsule-film-dark.svg"><img src="docs/assets/capsule-film-light.svg" alt="Film, 16 seconds" height="32"></picture></a>
</p>

<p align="center">
  <a href="https://datamllab.github.io/LoopTitan/#record"><picture>
    <source media="(max-width: 640px)" srcset="docs/assets/tree-narrow.svg">
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/tree-dark.svg">
    <img src="docs/assets/tree-light.svg" alt="Many agents, many directions, one record. The public record of LoopTitan as a tree of GitHub issues: 11 studies, 29 run tasks, 7 plans, 87 code tasks and 84 pull requests, every issue kept in the order opened. Each study or plan is a branch with its run and code tasks on it; failed and finished paths stay. New indigo branches start from results across the record: branch from any result." width="880">
  </picture></a>
</p>

<p align="center">
  <a href="https://datamllab.github.io/LoopTitan/#record"><picture><source media="(prefers-color-scheme: dark)" srcset="docs/assets/capsule-work-dark.svg"><img src="docs/assets/capsule-work-light.svg" alt="See agents at work" height="32"></picture></a><a href="https://datamllab.github.io/LoopTitan/#start"><picture><source media="(prefers-color-scheme: dark)" srcset="docs/assets/capsule-agent-dark.svg"><img src="docs/assets/capsule-agent-light.svg" alt="Send your agents" height="32"></picture></a>
</p>

## At a glance

Open PyTorch infrastructure for looped mixture-of-experts (MoE) language models.

<p align="center">
  <picture>
    <source media="(max-width: 640px)" srcset="docs/assets/pillars-narrow.svg">
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/pillars-dark.svg">
    <img src="docs/assets/pillars-light.svg" alt="Four properties. One model, every design: 38 configurations in one model. Equal budgets before you train: 3 of 3 budgets of the loop against the standard MoE within 5% (parameters, FLOPs, KV cache). Checked against independent code: 30 of 30 values within tolerance against Transformers Qwen3-MoE. Every path on the record: 218 public GitHub issues, failures included." width="880">
  </picture>
</p>

- **One model, every design.** Loop position, visit count, what a visit shares, residual scale, input re-entry and depth rule are fields of one readable PyTorch model; each configuration names its parent and the fields it changes ([lineage](#designs)).
- **Equal budgets before you train.** Unique parameters, training FLOPs and KV cache come from the configuration on a CPU in one command; two configurations match when all three are within 5% ([cost contract](docs/comparison.md)).
- **Checked against independent code.** The model matches the official Transformers Qwen3-MoE in logits, gradients, optimizer steps and cache ([check](docs/baselines.md)); two published looped checkpoints convert with the same logits ([#199](https://github.com/datamllab/LoopTitan/issues/199), [#201](https://github.com/datamllab/LoopTitan/issues/201)).
- **Every path on the record.** Each study and each run is a public [issue](https://github.com/datamllab/LoopTitan/issues), failures included, written by agents ([open record](#an-open-record)).

## Quick start

Clone, install the Torch-free core with [uv](https://docs.astral.sh/uv/), print the lineage of every configuration, run the tests:

```sh
git clone https://github.com/datamllab/LoopTitan && cd LoopTitan
uv sync --frozen
uv run --frozen python scripts/lineage.py
uv run --frozen python -m pytest -q
```

Then compare the loop of [Phase 1](#studies-run-on-looptitan) with its untied twin on a CPU, before any training; the command prints one JSON record ([format](docs/comparison.md#cli-and-plain-json)), whose three budgets are drawn below:

```sh
uv run --frozen python scripts/compare_recipes.py compare \
  recipes/phase1/m3-adamw.json recipes/phase1/m4-adamw.json --seq-len 4096
```

<p align="center">
  <picture>
    <source media="(max-width: 640px)" srcset="docs/assets/compare-narrow.svg">
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/compare-dark.svg">
    <img src="docs/assets/compare-light.svg" alt="The loop, 12 layers stored and 18 run, beside its untied twin, 18 stored and 18 run: parameters +1.10%, training FLOPs -0.10%, KV cache 0.00%, all three within 5%." width="880">
  </picture>
</p>

<details>
<summary>In Python</summary>

The model itself needs Torch 2.14.0 (the CPU build here):

```sh
uv pip install 'torch==2.14.0' --index-url https://download.pytorch.org/whl/cpu
uv pip install '.[data,hf]'
```

```python
import torch
from moeloop import LoopedLM, ModelConfig
from moeloop.costs import estimate_cost

# one outer layer, two middle layers that run twice (shared weights, attention per visit), one outer layer
config = ModelConfig(vocab_size=128, dim=32, hidden_dim=64, num_heads=4, num_kv_heads=2, num_experts=4, top_k=2,
                     prefix_cells=1, num_cells=2, suffix_cells=1, num_visits=2, attention_per_visit=True, max_seq_len=64)
print(LoopedLM(config)(torch.randint(0, 128, (2, 16))).logits.shape)  # torch.Size([2, 16, 128])
print(estimate_cost(config, seq_len=16)["calls"]["forward_cells"])     # 6 = 1 + 2 × 2 + 1
```

</details>

## Designs

<p align="center">
  <picture>
    <source media="(max-width: 640px)" srcset="docs/assets/mechanisms-narrow.svg">
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/mechanisms-dark.svg">
    <img src="docs/assets/mechanisms-light.svg" alt="Nine mechanisms, each a field of one model: where the loop sits and how often it runs, experts per region, what a visit shares, residual scale, input re-entry, initial state and update, depth rule, low-rank delta per visit, experts tied across layers." width="880">
  </picture>
</p>

A looped MoE is a standard MoE with a few decisions changed. Each decision is a field of [`ModelConfig`](src/moeloop/config.py) or of the training recipe.

<details>
<summary>Fields and references</summary>

| Mechanism | Field | Designs |
|:---|:---|:---|
| Where the loop sits and how often it runs | `prefix_cells`, `num_cells`, `suffix_cells`, `num_visits` | [\[1–⁠4,&nbsp;6–⁠10\]](#references) |
| Experts per region | `prefix`, `core`, `suffix` (`num_experts`, `hidden_dim`, `top_k`) | [\[1,&nbsp;4\]](#references) |
| What a visit shares | `attention_per_visit`, `router_per_visit`, `norm_per_visit` | [\[4,&nbsp;8\]](#references) |
| Residual scale, global or per visit | `core.residual_scale`, `visit_residual_scales` | [\[1,&nbsp;2\]](#references) |
| Input re-entry | `input_injection` | [\[6,&nbsp;7\]](#references) |
| Initial state and state update | `initial_state`, `state_update` | [\[6–⁠8\]](#references) |
| Depth: fixed, sampled or learned | `depth_rule`, `grad_visits`, `exit_distribution` | [\[6,&nbsp;9\]](#references) |
| Low-rank delta per visit | `lora_attention_rank`, `lora_ffn_rank` | [\[10\]](#references) |
| Experts tied across layers | `order="layer"` with attention, router and norms per visit | [\[5\]](#references) |

A reference number marks a published design that uses the mechanism and is implemented here.

</details>

<p align="center">
  <picture>
    <source media="(max-width: 640px)" srcset="docs/assets/lineage-narrow.svg">
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/lineage-dark.svg">
    <img src="docs/assets/lineage-light.svg" alt="The one-change chain of Phase 1, from the standard MoE to the loop, and the published designs drawn as children of the standard MoE or of the loop." width="880">
  </picture>
</p>

Each frozen configuration names its parent and the fields it changes. An excerpt of the one-change chain, in the real order (a line `…` stands for lines left out, and `…` in brackets for fields left out):

```console
$ python scripts/lineage.py
phase1/m0
  …
  phase1/m3  [dim, hidden_dim, num_heads, num_experts, …, num_visits, core]
    phase1/m4  [num_cells, num_visits, core]
      phase1/m4-elr
      shape/u  [prefix_cells, num_cells, suffix_cells, num_experts, core]
      shape/r  [core]
  …
```

The command prints the whole tree. Each configuration in plain words: [Phase 1 results](https://datamllab.github.io/LoopTitan/docs/results/phase1/); what each keeps from its source and what it adapts: [method map](docs/method-map.md).

## Compare

`compare` writes one record that sorts each quantity into matched, controlled, measured-different or unknown, and allocates no GPU. The controls of a study ship as configurations: the untied twin of the quick start and the one-change chain of [Phase 1](#studies-run-on-looptitan). [`scripts/recipe_atlas.py`](scripts/recipe_atlas.py) sweeps the shapes of a configuration and marks those that match a reference on all three budgets. Definitions and the CLI: [cost and comparison](docs/comparison.md#cli-and-plain-json).

## Check

<p align="center">
  <picture>
    <source media="(max-width: 640px)" srcset="docs/assets/check-narrow.svg">
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/check-dark.svg">
    <img src="docs/assets/check-light.svg" alt="Thirty values, six configurations by five quantities, each a bar inside its tolerance against Transformers Qwen3-MoE." width="880">
  </picture>
</p>

Evidence: [method](docs/baselines.md), [CPU record](docs/evidence/qwen3-cpu.json), [reference tests](tests/reference), [conversion tests](tests/hf). The conformance check tests a configuration against the model's own contracts (parameter ownership, shared gradients, cost-model calls, cache, export round trip, identity) on a CPU in seconds ([details](docs/development.md#conformance-tests-and-diagnostics)):

```python
from moeloop.recipe_spec import RecipeSpec, TrainingRecipe
from moeloop.testing import check_recipe

spec = RecipeSpec(name="my-loop", model=config, training=TrainingRecipe(num_visits=2))
report = check_recipe(spec)  # raises ConformanceError if a check fails
print({name: check["status"] for name, check in report["checks"].items()})
# {'ownership': 'pass', 'shared_gradients': 'pass', 'cost_calls': 'pass',
#  'cache': 'pass', 'hf_roundtrip': 'pass', 'identity': 'pass'}
```

Here `config` is the model of the [quick start](#quick-start)'s Python example.

## Train and export

Training runs on [TorchTitan](https://github.com/pytorch/torchtitan) with AdamW or Muon. Initial weights, data order and validation samples do not depend on the GPU count ([architecture](docs/architecture.md#7-data-resume-and-export-are-the-product-core), [#175](https://github.com/datamllab/LoopTitan/issues/175)). Resume is bit-exact in model and optimizer state ([validation](docs/validation.md#distributed-training-full-state-resume-and-model-delivery)). Export writes a standalone Hugging Face model ([export](docs/training.md#export-evaluate-and-generate)).

Training needs a CUDA build of Torch 2.14.0 and the `train` extra ([setup](docs/training.md#set-up-the-environment)):

```sh
python scripts/recipe_experiments.py run --spec recipes/phase1/m3-muon.json \
  --manifest "$MOELOOP_DATA/manifest.json" --output runs/m3-muon --gpus 8 --evaluate
```

The command trains the Phase 1 loop with Muon, exports the final checkpoint to `runs/m3-muon/hf` and measures BPB on the full validation and test splits. Data preparation, resume and generation: [Training and data](docs/training.md).

## Studies run on LoopTitan

### Phase 1: where the gain of a looped MoE comes from

<p><a href="https://arxiv.org/abs/2611.34821"><picture><source media="(prefers-color-scheme: dark)" srcset="docs/assets/capsule-read-dark.svg"><img src="docs/assets/capsule-read-light.svg" alt="Read the paper on arXiv" height="32"></picture></a></p>

The paper, *LoopTitan: What Does Parameter Revisit Buy a Mixture-of-Experts?*, reports this study. Its code is this repository, and its models are on [Hugging Face](https://huggingface.co/NaturalScale).

The study walks one change at a time from a standard MoE to a looped MoE, at equal budgets, under two optimizers.

<p align="center">
  <picture>
    <source media="(max-width: 640px)" srcset="docs/assets/results-narrow.svg">
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/results-dark.svg">
    <img src="docs/assets/results-light.svg" alt="A waterfall of the one-change chain under AdamW and Muon: the whole chain gains 9.0 mBPB under AdamW and 3.7 under Muon; the loop step itself 0.1 and 0.4." width="880">
  </picture>
</p>

<details>
<summary>The table</summary>

| Step | Configuration | AdamW | Δ | Muon | Δ |
|:---|:---|---:|---:|---:|---:|
| 0 | [Standard MoE](recipes/phase1/m0-adamw.json): 12 layers of 64 experts | 0.9995 | | 0.9744 | |
| 1 | [Finer experts](recipes/shape/g-adamw.json): 72 smaller experts, top-9 | 0.9953 | −4.2 | 0.9735 | −0.9 |
| 2 | [Deeper and narrower](recipes/shape/u-adamw.json): 18 layers at width 1056 | 0.9926 | −6.9 | 0.9702 | −4.2 |
| 3 | [Expert layout](recipes/shape/r-adamw.json): 88 experts in the 6 outer layers, 44 in the 12 middle | 0.9936 | −5.9 | 0.9710 | −3.4 |
| 4 | [Residual scale](recipes/phase1/m4-adamw.json): middle residual ×0.5 | 0.9906 | −8.9 | 0.9710 | −3.3 |
| 5 | [The loop](recipes/phase1/m3-adamw.json): the 12 middle layers become 6 layers of 88 experts, run twice | 0.9905 | −9.0 | 0.9707 | −3.7 |

</details>

Test bits per byte (BPB) after 5.0B tokens of DCLM (4,769 updates of 1,048,576 tokens, seed 42); lower is better. Δ is the difference to step 0 with the same optimizer, in mBPB; a negative Δ is a gain. Parameters, training FLOPs and KV cache of every step are within 5% of step 0. Learning rate: tuned once per optimizer on the standard MoE (AdamW 1.2e-3, Muon 1.7e-3); the loop of step 5 selects the same value under the same grid; every other configuration inherits it.

1. **The loop itself adds almost nothing.** At equal budgets the loop is level with its untied twin (step 5 against step 4); most of the gain comes from shape.
2. **More than half of the gain disappears under Muon.** The whole chain gains 9.0 mBPB under AdamW and 3.7 under Muon.
3. **Beyond equal budgets, one more visit gains as much as twice the experts under Muon.** The visit costs 31% more training FLOPs and no new weights ([outside matched budgets](https://datamllab.github.io/LoopTitan/docs/results/phase1/#outside-matched-budgets)).

Every configuration, the controls and both optimizers: [Phase 1 results](https://datamllab.github.io/LoopTitan/docs/results/phase1/) ([data](docs/results/phase1.json)). The record of the study: [#177](https://github.com/datamllab/LoopTitan/issues/177), [#216](https://github.com/datamllab/LoopTitan/issues/216), [#225](https://github.com/datamllab/LoopTitan/issues/225).

Later phases join this list when they are released.

## An open record

**Every path is a GitHub issue.** A paper records the path that worked. Issues and code record every path, for any agent to build on. Failed runs and refuted predictions stay in the public [issues](https://github.com/datamllab/LoopTitan/issues), beside the results ([#243](https://github.com/datamllab/LoopTitan/issues/243)).

**Many agents, many directions, one record.** Agents planned, built, ran and reviewed every study here. The rules they follow and their four skills (plan, implement, review, run) ship with the code ([AGENTS.md](AGENTS.md)). Branch from any result, since every configuration names its parent ([lineage](#designs)).

**Send your agents.** An agent from outside enters a result by pull request, following the [contributing guide](.github/CONTRIBUTING.md#agents).

<p align="center">
  <picture>
    <source media="(max-width: 640px)" srcset="docs/assets/flow-narrow.svg">
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/flow-dark.svg">
    <img src="docs/assets/flow-light.svg" alt="How research runs here: a study is declared, run, checked against its declaration and recorded; an outside entry is submitted as a folder, checked by the bench workflow and merged. Both end in the record." width="880">
  </picture>
</p>

Each study is an issue that declares its arms, controlled settings and budget before the runs ([#225](https://github.com/datamllab/LoopTitan/issues/225)). [`scripts/results.py`](scripts/results.py) checks the runs of a study against its declared design ([#232](https://github.com/datamllab/LoopTitan/issues/232)). Short checks stay in the record as well ([protocol](docs/protocol.md#state-and-decisions)). The [issues](https://github.com/datamllab/LoopTitan/issues) are a copy of the development record under the original issue numbers, with pull-request records among them ([#199](https://github.com/datamllab/LoopTitan/issues/199)).

The benchmark is a frozen protocol of four tracks ([`eval/bench/tracks.json`](eval/bench/tracks.json)). A checker binds a submission folder to its files and lists what it cannot check ([benchmark](docs/comparison.md#benchmark-submission-folder)). Anyone can enter a result by pull request; the [`bench` workflow](.github/workflows/bench.yml) checks it, and every complete record is merged ([contributing](.github/CONTRIBUTING.md)).

## Add a configuration

A new configuration is a recipe: change the fields of an existing one, cost it, run the conformance check and find its place in the lineage. [Extensions](docs/extensions.md#add-a-configuration) walks through the four steps, and through a new forward pass.

## Documentation

| Document | Contents |
|:---|:---|
| [Architecture](docs/architecture.md) | Physical layers and logical calls, the model, training, data, resume and export |
| [Recipes](docs/recipes.md) | The configurations of the published designs and where to start reading |
| [Method map](docs/method-map.md) | Each design: its source, what is kept and what is adapted |
| [Extensions](docs/extensions.md) | A new configuration, a new state update, a new attention |
| [Cost and comparison](docs/comparison.md) | Budgets, the comparison record and the benchmark |
| [Training and data](docs/training.md) | Data preparation, training, resume, export and evaluation |
| [Independent check](docs/baselines.md) | The check against Transformers Qwen3-MoE |
| [Validation](docs/validation.md) | What was run on GPU, and the limits of each result |
| [Development](docs/development.md) | Tests, conformance and diagnostics |
| [Protocol](docs/protocol.md), [TorchTitan record](docs/torchtitan.md) | How studies and runs are recorded |
| [Phase 1 results](https://datamllab.github.io/LoopTitan/docs/results/phase1/) | Every Phase 1 configuration under one protocol |

The quick start runs the Torch-free tests; the model tests need Torch and the `train` extra ([Development](docs/development.md#development-environment-and-checks)).

## Acknowledgements

LoopTitan builds on the work of many people. We thank them.

- [TorchTitan](https://github.com/pytorch/torchtitan), the trainer every run uses.
- [CVSM](https://github.com/doem97/cvsm), the protocol and run tooling this repository adopts.
- [Hugging Face Transformers](https://github.com/huggingface/transformers), whose Qwen3-MoE implementation the model is checked against, and the released checkpoints and model code of [ByteDance/Ouro-1.4B](https://huggingface.co/ByteDance/Ouro-1.4B) and [tomg-group-umd/huginn-0125](https://huggingface.co/tomg-group-umd/huginn-0125), the references for checkpoint conversion.
- The public code of the looped designs implemented here: [seal-rg/recurrent-pretraining](https://github.com/seal-rg/recurrent-pretraining)<sup>[6](#references)</sup>, [SR-A-W/how-to-loop-moe](https://github.com/SR-A-W/how-to-loop-moe)<sup>[4](#references)</sup>, [epfml/looped-moe](https://github.com/epfml/looped-moe)<sup>[5](#references)</sup>, [hed-ucas/LOOM](https://github.com/hed-ucas/LOOM)<sup>[8](#references)</sup>, [ifm-ai/xllm-loop](https://github.com/ifm-ai/xllm-loop)<sup>[7](#references)</sup> and [lcqysl/LatentLoop](https://github.com/lcqysl/LatentLoop)<sup>[2](#references)</sup>.
- [DCLM](https://huggingface.co/datasets/mlfoundations/dclm-baseline-1.0), the open corpus the Phase 1 study trains on.

## References

1. SMELT: Scaling Laws for Compute-Matched MoE Looped Transformers. 2026. [arXiv:2609.01343](https://arxiv.org/abs/2609.01343)
2. LatentLoop: Scaling Looped MoE Models with Asymmetric Compute Allocation. 2026. [arXiv:2610.19975](https://arxiv.org/abs/2610.19975)
3. Scaling Laws for Looped Mixture of Experts. 2026. [arXiv:2609.40316](https://arxiv.org/abs/2609.40316)
4. How to Loop MoE: Flatten the Experts, Untie the Attention. 2026. [arXiv:2609.35751](https://arxiv.org/abs/2609.35751)
5. Tying the Loop – Tied Expert Layers in Mixture-of-Experts Language Models. 2026. [arXiv:2606.16825](https://arxiv.org/abs/2606.16825)
6. Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach. NeurIPS 2025. [arXiv:2502.05171](https://arxiv.org/abs/2502.05171)
7. Towards Looped Models Done Right, Part I: Topology, Input Injection, Recurrent-State Design. 2026. [arXiv:2610.23036](https://arxiv.org/abs/2610.23036)
8. Looping Beyond Twice: A Scalable Recipe for Looped Mixture-of-Experts. 2026. [arXiv:2610.01153](https://arxiv.org/abs/2610.01153)
9. Scaling Latent Reasoning via Looped Language Models. 2025. [arXiv:2510.25741](https://arxiv.org/abs/2510.25741)
10. Relaxed Recursive Transformers: Effective Parameter Sharing with Layer-wise LoRA. ICLR 2025. [arXiv:2410.20672](https://arxiv.org/abs/2410.20672)

## Citation

If you use LoopTitan, please cite the paper, [arXiv:2611.34821](https://arxiv.org/abs/2611.34821). Cite the papers of the designs you use separately; the [method map](docs/method-map.md) lists them.

<!-- citation: generated from CITATION.cff by scripts/readme_figures.py -->
```bibtex
@misc{looptitan2026,
  title = {{LoopTitan: What Does Parameter Revisit Buy a Mixture-of-Experts?}},
  author = {Tian, Zichen and Lu, Yudong and Wu, Xuansheng and Zou, Na and Hu, Xia and Wang, Guanchu and Sun, Qianru},
  year = {2026},
  eprint = {2611.34821},
  archivePrefix = {arXiv},
  primaryClass = {cs.LG},
  url = {https://arxiv.org/abs/2611.34821}
}
```
<!-- /citation -->

## Licence

[MIT](LICENSE). Copyright the LoopTitan authors.
