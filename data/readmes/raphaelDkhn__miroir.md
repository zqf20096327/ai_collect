# Miroir 🪞

**Turn a product into an agentic RL environment**

Miroir turns a product's Docker image into [Harbor](https://docs.harborframework.com)
environments that grade what an agent did to the real product: the database rows it changed, the
emails and HTTP calls the product sent, and the answer it gave. Any change outside the task's scope
counts as `harm`, reported next to `reward`.

Harbor already runs agents, sandboxes and jobs. Miroir adds the two pieces it lacks: a product
image with seeded data, and a grader that reads what changed below the product's API.

## Quick start

You need Docker with buildx and [uv](https://docs.astral.sh/uv/). From a clone:

```bash
uv tool install harbor==0.26.0
docker buildx bake
harbor run -c fixtures/acme-crm/check.yaml --job-name quick-start
alias miroir='docker run --rm -v "$PWD:$PWD" -w "$PWD" miroir:dev miroir'
miroir check --tasks fixtures/acme-crm/tasks jobs/quick-start
```

This builds a small CRM with 7 tasks, then has Harbor run each task's reference solution, an agent
that does nothing, and probes: wrong solutions the grader has to catch. `miroir check` should end
with:

```text
7 tasks, 21 trials, 7 skipped probe slots, 0 violations, 0 voids
```

The first build compiles Miroir (6 min 44 s on a 12-CPU Docker Desktop). The trials take under a
minute.

## How it works

1. `miroir bake` seeds the product's data into its image during `docker build`.
2. Each Harbor trial starts that image next to the agent's container. `miroir run` boots the
   product and moves its dates to the trial's day. The agent uses the product's own API.
3. When the agent stops, `miroir collect` records the rows that changed and the emails and HTTP
   calls the product sent.
4. `miroir grade` scores that record in Harbor's separate verifier, using the SQL checks and
   allowed changes in the task's `task.toml`.

Tasks are plain Harbor task directories. `miroir check` fails when a grader rejects the reference
solution or lets a probe through, and `miroir draft` writes a first grading spec from reference
runs.

## More

- [Docs](https://miroir.mintlify.site): wrap a product, write tasks, validate, train
- [Gitea example](examples/gitea): stock Gitea, three seeded companies, 120 tasks
- [Skill](skills/miroir/SKILL.md) for coding agents. In Claude Code:
  `claude plugin marketplace add raphaelDkhn/miroir`, then `claude plugin install miroir@miroir`
- [Contributing](CONTRIBUTING.md), [security](SECURITY.md), [Apache-2.0](LICENSE)
