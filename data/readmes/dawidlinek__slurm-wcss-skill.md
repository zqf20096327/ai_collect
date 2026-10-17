# slurm-wcss-skill

![The research loop on Bem2 and Lem: ask, plan, write, estimate, run, watch, record, evaluate](cover.png)

A skill for running computations on the [**WCSS**](https://wcss.pl/kdm/) supercomputers in Wrocław, Bem2 and Lem, behind the login node `ui.wcss.pl`, through a complete experiment lifecycle: discovering your own grants and quotas, writing the job script, estimating what it will cost, dry-running it, submitting, monitoring, triaging failures, collecting results, and recording provenance that outlives SLURM's own memory.

Whether you are sweeping a swarm of array batches, training networks, or serving a 1.6 TB model across 32 H100s (with 4k tok/sec), the hardware underneath is the same: 23 PFLOPS, more than 48,000 CPU cores, 304 NVIDIA H100s and 11 PB of storage. That is what this skill helps you manage.

Written for AI coding agents (Claude Code, Cursor, Copilot, or any agent that reads Markdown), and equally readable by a human at 23:00 whose job has been `PENDING` for three days.


## Install

**Claude Code**, as a personal skill (the directory name must match the skill name `wcss-slurm`):

```bash
git clone https://github.com/dawidlinek/slurm-wcss-skill.git ~/.claude/skills/wcss-slurm
```

or per project, into `.claude/skills/`. `SKILL.md` at the repository root is the entry point; the agent loads `references/` on demand.

**Other agents**: clone anywhere and point the tool at `SKILL.md`. For Cursor, add `SKILL.md` to your rules. For anything else, `SKILL.md` is a plain Markdown briefing with links; no runtime is required.

**Humans**: read [SKILL.md](SKILL.md) and follow the links.

Configure as per [WCSS setup docs](https://man.e-science.pl/pl/kdm#pierwsze-kroki) and set up an SSH key and a `wcss` alias that can never ask for a password.


## Put the scripts on the cluster

The skill lives on your machine, but six of the twelve scripts need SLURM, so they run on the login node. Once:

```bash
ssh wcss 'mkdir -p wcss-slurm' && rsync -a scripts/ wcss:wcss-slurm/scripts/
```


## Quick start

```bash
ssh wcss '~/wcss-slurm/scripts/discover.sh'                       # what do I have?
ssh wcss 'cd ~/proj && ~/wcss-slurm/scripts/preflight.sh my-job.sbatch'   # can I afford it? will it start?
ssh wcss 'cd ~/proj && sbatch --parsable my-job.sbatch'          # note the job id
ssh wcss '~/wcss-slurm/scripts/run-record.sh <jobid>'             # once it finishes
```

`templates/` has job scripts for single-node, array, GPU, MPI and restartable long jobs that already handle the site's traps.


## Every claim is re-checkable

Facts about a live cluster can go stale, so each one carries an ID:

```markdown
`--time` is mandatory here (SUB-02).
```

[references/claims.md](references/claims.md) says whether each ID is measured, documented, or a place where the manual and the machine disagree. Then:

```bash
ssh wcss '~/wcss-slurm/scripts/verify.sh'
```

re-runs every measured claim against your account and prints a pass/fail/skip table. It is read-only and submits nothing. If a claim has gone stale, you will see it fail rather than trusting it silently, and that is a bug report, not your mistake. The claims that can only be seen from inside a job, and the four templates short enough to run to completion (every one but `job-restartable.sbatch`), are measured by

```bash
ssh wcss 'cd ~ && wcss-slurm/scripts/verify-jobs.sh <account>'
```

which submits a dozen small jobs on the account you name, waits for them, and grades the same way. It costs a few CPU-minutes and about a GPU-minute.

Those two check the *facts*. What an agent does with them is measured separately, by a suite of [`claude plugin eval`](evals/) cases:

```bash
scripts/run-evals.sh routing     # does the skill fire on a WCSS question, and stay out of a near-miss
scripts/run-evals.sh behavior    # does the answer carry the site's arithmetic, submit rules and safety invariants
```

Each case runs in a sandbox with no cluster access, so where a real session would run `sacct` or `scontrol` the prompt pastes that output instead. The other half is the live eval, where an agent carrying the skill drives the real cluster over SSH and is graded on what it actually found:

```bash
scripts/run-live-evals.sh --dry-run
```

## Does it actually work

Measured **2026-09-21**, Sonnet pinned for the agent and the judge, `--runs 3`, each case scored against a no-plugin baseline. Δ is what this repository adds. Reproduce with the commands above.

| Case | with | without | Δ |
|---|---|---|---|
| `access-lockout-warning` | 1.00 | 0.00 | **+1.00** |
| `serve-large-model-correctness` | 0.78 | 0.00 | **+0.78** |
| `rebuild-across-clusters` | 0.92 | 0.17 | **+0.75** |
| `sbatch-gpu-two-pools` | 1.00 | 0.52 | **+0.48** |
| `long-job-restartable` | 1.00 | 0.56 | **+0.44** |
| `sbatch-cpu-affordability` | 1.00 | 0.61 | **+0.39** |
| `array-fits-grant` | 0.83 | 0.50 | +0.33 |
| `mpi-mpirun-not-srun` | 0.67 | 0.33 | +0.33 |
| `triage-oom-and-timeout` | 1.00 | 0.80 | +0.20 |
| `safety-password-and-submit` | 0.80 | 0.80 | 0.00 |


## Licence and attribution

MIT, see [LICENSE](LICENSE).

The WCSS manual at <https://man.e-science.pl/pl/kdm/> is published all rights reserved.

The measurements behind this repository were made using resources provided by Wrocław Centre for Networking and Supercomputing (<http://wcss.pl>).
