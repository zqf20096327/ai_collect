<div align="center">

<h1>TerminalWorld: Benchmarking Agents on Real-World Terminal Tasks</h1>

<p><strong>NeurIPS 2026 · Evaluations and Datasets Track</strong></p>

<a href="https://arxiv.org/abs/2605.22535"><img src="https://img.shields.io/badge/Paper-arXiv-B31B1B?style=flat-square&amp;logo=arxiv&amp;logoColor=white" alt="Paper on arXiv"></a>
<a href="https://terminalworld.ai/"><img src="https://img.shields.io/badge/Website-TerminalWorld-2563EB?style=flat-square" alt="TerminalWorld website"></a>
<a href="https://huggingface.co/datasets/terminalworld/TerminalWorld"><img src="https://img.shields.io/badge/Dataset-Hugging_Face-EAB308?style=flat-square&amp;logo=huggingface&amp;logoColor=white" alt="Dataset on Hugging Face"></a>

</div>

TerminalWorld is a scalable data engine that automatically reverse-engineers high-fidelity evaluation tasks from in-the-wild terminal recordings. Processing 80,870 terminal recordings, the engine yields a full benchmark of 1,530 validated tasks, spanning 18 real-world categories, ranging from short everyday operations to workflows exceeding 50 steps, and covering 1,280 unique commands. The automated engine makes TerminalWorld authentic and scalable by construction, enabling it to evaluate agents in real-world terminal environments as developer practices evolve.

<p align="center">
  <img src="assets/pipeline.png" alt="TerminalWorld data engine: collecting human recordings, synthesizing terminal tasks, reproducing executable environments, and generating test suites." width="100%">
</p>

---

## Overview

Existing benchmarks rely on manual curation, where experts often prioritize adversarial puzzles to artificially maximize difficulty, thereby diverging from authentic, real-world terminal workflows. This labor-intensive process struggles to scale with evolving terminal practices and diverse emerging tools. TerminalWorld automatically turns in-the-wild terminal recordings shared on [asciinema.org](https://asciinema.org) into executable, rigorously validated evaluation tasks.

The pipeline operates in four stages:

```
asciinema recordings (80,870)
        │
        ▼  1. Collecting Human Recordings
   9,492 high-quality recordings
        │
        ▼  2. Synthesizing Terminal Tasks
   instruction.md + solve.sh (reference solution)
        │
        ▼  3. Reproducing Executable Environments
   Dockerfile + docker-compose.yaml (5,035 reproduced)
        │
        ▼  4. Generating Test Suites
   1,530 validated tasks (AllPassing / Nop / Partial trials)
```

---

## Repository Structure

```
TerminalWorld/
├── data_retrieval/          # Stage 1a: crawl and download asciinema recordings
│   ├── scrape_pages.py      #   Index explore feeds (public / recent / featured / popular)
│   ├── download_recordings.py #  Download .txt transcripts + info.json metadata
│   ├── parsers.py           #   HTML parsers for listing and detail pages
│   ├── config.py            #   Shared crawler configuration
│   └── stats.py             #   Dataset statistics
│
├── data_filtering/          # Stage 1b: filter recordings by quality criteria
│   ├── detect_pii.py        #   Flag PII, credentials, and malicious commands
│   ├── classify_tui.py      #   Detect TUI tool invocations (vim, htop, tmux, …)
│   ├── detect_external_urls.py # Identify and verify external repository links
│   ├── analyze_duration.py  #   Extract and analyze recording durations
│   ├── score_value.py       #   Two-stage LLM quality scoring (feasibility + value)
│   └── filter_recordings.py #   Combine all filters into a single filtering pass
│
├── task_synthesis/          # Stage 2: synthesize task instruction and reference solution
│   ├── generate_instruction.py  # LLM-based outcome-oriented instruction generation
│   ├── extract_solution.py      # LLM-based reference solution extraction from transcript
│   └── generate_task_metadata.py
│
├── environment_building/    # Stage 3: reproduce executable Docker environments
│   ├── build_environment.py  # LLM agent: synthesize and refine Dockerfile
│   ├── analyze_recording.py  # Parse transcript to extract environment signals
│   ├── batch_build.py        # Parallel batch environment reproduction
│   └── monitor.py
│
└── test_generation/         # Stage 4: generate and validate test suites
    ├── generate_tests.py     # LLM agent: snapshot-guided test suite generation
    ├── refine_task.py        # Trial-based refinement loop (AllPassing/Nop/Partial)
    ├── batch_refine.py       # Parallel batch refinement
    └── skill/                # Agent skill definitions and task format references
```

---

## Pipeline Details

### Stage 1: Collecting Human Recordings

We systematically index publicly shared asciinema recordings. For each recording, we acquire its transcript text via the standard public download links, along with metadata such as its title and description. The transcript captures the ordered sequence of executed commands and standard outputs.

Recordings are then filtered by five criteria:
1. Privacy and safety: exclude recordings exposing Personally Identifiable Information (PII), sensitive credentials, or malicious/destructive commands.
2. Pure CLI workflows: discard recordings involving Text User Interfaces (TUIs, e.g., `vim`, `nano`, and `emacs`) or GUI applications.
3. Docker reproducibility: remove recordings incapable of deterministic reproduction in Docker containers, such as those dependent on inaccessible URLs, Windows environments, or proprietary software.
4. Recording length: eliminate excessively short recordings, typically aborted or trivial sessions.
5. Recording quality: employ an LLM to score recording quality, filtering out opaque or purely exploratory sessions.

**Result:** 80,870 → **9,492** high-quality recordings.

### Stage 2: Synthesizing Terminal Tasks

We purify the transcript by removing typos, failed attempts, and redundant commands, distilling it into an instruction inferred from the underlying human intent and a clean command sequence as the reference solution.

- Task Instruction Formalization: an LLM distills the developer's core intent from the transcript alongside the title and description. The instruction specifies the task goal in concise, outcome-oriented language: it describes the expected final state, not the path to reach it. It explicitly specifies required output paths and structural formats, without procedural phrasing, specific commands, or step-by-step enumerations.
- Reference Solution Extraction: an LLM extracts a clean, executable bash script from the transcript. For long transcripts, we first split the transcript into chunks to filter execution noise and isolate valid commands. We then merge the extracted commands, remove duplicates, and assemble a coherent solution workflow. The script redirects its final results from transient terminal outputs to explicit file paths, such as `/app/result.txt`.

### Stage 3: Reproducing Executable Environments

An LLM agent synthesizes a `Dockerfile` (and `docker-compose.yaml` for multi-service tasks) by inferring dependencies from the reference solution. If the recording includes an external repository link, the agent clones and scans it to infer precise requirements. Fake binaries, stubbed dependencies, and bypasses of real software installation are explicitly prohibited.

In the execution-based refinement loop, the agent builds the Docker image, parses build logs, launches the container and any required auxiliary services, and executes the reference solution in a persistent shell session. The environment is considered reproduced only when the script executes successfully with an exit code of 0. Runtime errors are fed back to the agent for targeted repairs to the `Dockerfile` or `docker-compose.yaml`. Recordings that remain irreproducible within the computational budget or rely on inaccessible resources are discarded.

**Result:** 9,492 → **5,035** reproduced environments.

### Stage 4: Generating Test Suites

The agent captures pre- and post-execution filesystem snapshots in the Docker environment and generates state-based test assertions calibrated to the actual final state. Tests target persistent artifacts (file existence, content hashes, structured outputs) and avoid brittle non-deterministic checks (timestamps, process IDs).

In the trial-based refinement loop, the agent iteratively refines the test suite through three execution trials in fresh, isolated containers to eliminate false negatives and false positives:

| Trial | Execution | Requirement | Purpose |
|-------|-----------|-------------|------------|
| **AllPassing** | Full reference solution | All tests pass | Task *solvability* |
| **Nop** | Nothing (empty state) | All tests fail | Task *non-triviality* |
| **Partial** | Truncated / ablated solution | At least one test fails | Test *discriminability* |

A task is admitted only if its test suite satisfies all three trials. If any trial fails, the agent diagnoses the trial outputs, applies targeted fixes to the test suite, and reruns the loop. When necessary, adjustments to the test suite are synchronized back to the instruction, ensuring that the instruction explicitly specifies the state being evaluated. A task is discarded if its test suite cannot be repaired to pass all three trials within the computational budget.

**Result:** 5,035 → **1,530** validated tasks.

---

## The TerminalWorld Benchmark

| | Full Set | Verified Subset |
|--|--|--|
| **Tasks** | 1,530 | 200 |
| **Categories** | 18 | 18 |
| **Unique commands** | 1,280 | Not reported |
| **Commands absent from Terminal-Bench** | 91% | Not reported |
| **Human review** | Automated validation | ✓ (4 expert annotators) |

From the full benchmark, we curate a Verified subset of 200 tasks by carefully balancing diversity and complexity. It spans diverse real-world task categories while prioritizing tasks with longer command sequences and non-trivial domain-specific tools.

This subset undergoes manual review by four authors, each with over three years of terminal-based software development experience. Annotators build the Docker image, enter the containerized environment, and execute the reference solution step by step, repairing the `Dockerfile` or `docker-compose.yaml` if necessary. They also cross-review artifact alignment to ensure that every test constraint is stated in the instruction and that the tests accurately check the persistent artifacts produced by the reference solution.

While the full set of 1,530 tasks provides a scalable resource of in-the-wild terminal workflows, Verified offers a rigorous and challenging testbed for benchmarking frontier models and agents on complex, real-world terminal tasks.

Comprehensive benchmarking on TerminalWorld-Verified across eight frontier models and six terminal agents reveals that current systems still struggle with authentic terminal workflows, achieving a maximum pass rate of only 62.5%. Terminal-Bench scores are only weakly predictive of agent performance on TerminalWorld-Verified (Pearson *r* = 0.20), suggesting that existing expert-curated challenges do not fully capture the capabilities needed for real-world terminal workflows.

---

## Ethics & Data Policy

- We collect only publicly listed `.txt` transcripts and their coupled metadata via asciinema's standard download links, in full compliance with `robots.txt`.
- Raw `.cast` files and generated media are **never downloaded or redistributed**.
- The released benchmark contains only synthesized artifacts (instructions, environments, tests) with hyperlinks back to the original recordings. No original transcripts are redistributed.
- Recordings are filtered for PII, credentials, and malicious content before any synthesis occurs.

See the paper's ethics section for a full discussion of copyright compliance and the right-to-be-forgotten architecture.

## Citation

If you use TerminalWorld in your research, please cite:

```bibtex
@inproceedings{chu2026terminalworld,
  title     = {TerminalWorld: Benchmarking Agents on Real-World Terminal Tasks},
  author    = {Zhaoyang Chu and Jiarui Hu and Xingyu Jiang and Pengyu Zou and Han Li and Chao Peng and Peter O'Hearn and Earl T. Barr and Mark Harman and Federica Sarro and He Ye},
  booktitle = {NeurIPS 2026 Evaluations and Datasets Track},
  year      = {2026}
}
```
