# Architecture-First Model CRACK on DGX Spark

A project-local Codex skill for analyzing an open-weight model, choosing the best architecture-specific behavioral intervention, implementing it on a two-node NVIDIA DGX Spark cluster, and validating only the claims supported by evidence.

The skill deliberately contains no model names, versions, layer numbers, tensor names, edit strengths, or historical benchmark results. Each run starts from the exact checkpoint, runtime, forward graph, distributed semantics, and quantization format in front of the agent.

## What it does

- Builds a header-only checkpoint, writer, quantization, and special-path inventory without loading tensor payloads.
- Proposes evidence-driven signal and implementation routes instead of replaying a fixed recipe.
- Separates reference differencing, paired activation discovery, checkpoint editing, runtime sidecars, bounded residual correction, and training fallback.
- Requires both zero-edit codec roundtrips and edit-expressibility tests for quantized checkpoints.
- Supports smoke, behavior-only, capability-preservation, and release evaluation profiles.
- Tracks the run in a resumable evidence ledger and audits plan, candidate, handoff, and publication gates.
- Keeps model weights and large-model execution on the DGX nodes.

## Repository layout

```text
SKILL.md
agents/openai.yaml
references/
  architecture-discovery.md
  method-routing.md
  evaluation-system.md
  validation-release.md
scripts/
  checkpoint_inventory.py
  plan_pipeline.py
  new_run.py
  audit_run.py
```

## Use as a project-local skill

Clone the repository into a project's `skills/` directory:

```bash
git clone https://github.com/jiayuqi7813/crack-open-models-dgx-spark.git \
  skills/crack-open-models-dgx-spark
```

Then invoke:

```text
$crack-open-models-dgx-spark
```

The target project should provide its own infrastructure instructions, cluster topology, service lifecycle rules, and authorization boundaries. This skill supplies the model-analysis and intervention system, not those project-specific facts.

## Core automation

Create a run ledger:

```bash
python3 scripts/new_run.py \
  --output runs/model/intervention-run.json \
  --model-id ORG/MODEL --revision COMMIT \
  --objective refusal-behavior-edit \
  --backend auto --nodes node-a,node-b
```

Inventory a DGX-local checkpoint and generate an initial route plan:

```bash
python3 scripts/checkpoint_inventory.py \
  /path/to/checkpoint --output runs/model/checkpoint-inventory.json

python3 scripts/plan_pipeline.py \
  runs/model/checkpoint-inventory.json \
  --output runs/model/pipeline-plan.json
```

Audit progressive gates:

```bash
python3 scripts/audit_run.py runs/model/intervention-run.json --mode plan
python3 scripts/audit_run.py runs/model/intervention-run.json --mode candidate
python3 scripts/audit_run.py runs/model/intervention-run.json --mode handoff
python3 scripts/audit_run.py runs/model/intervention-run.json --mode publish
```

Generated plans are hypotheses. The agent must still confirm writer orientation, residual topology, tensor-parallel collectives, quantization codecs, and runtime behavior from current primary sources and a real minimal forward pass.

## License

MIT. See [LICENSE](LICENSE).
