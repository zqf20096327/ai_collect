<div align="center">

<h1>Claude Code "Code Mode" Benchmark</h1>

<p>
  <strong>A repeatable experiment that measures what Code Mode changes in Claude Code:<br>
  tokens processed, requests, time and correctness, with Code Mode off and on.</strong>
</p>

<p>
  <img alt="Tested on Claude Code v2.1.326; Code Mode needs v2.1.323 or later" src="https://img.shields.io/badge/Claude_Code-tested_on_v2.1.326-d97757">
  <img alt="Code Mode is an experimental feature" src="https://img.shields.io/badge/Code_Mode-experimental-orange">
  <img alt="Models tested: Opus 5.5, Sonnet 5.5, Haiku 5.5 and Fable 5.2" src="https://img.shields.io/badge/models-Opus_%C2%B7_Sonnet_%C2%B7_Haiku_%C2%B7_Fable-blue">
  <img alt="Scripts tried on macOS only" src="https://img.shields.io/badge/platform-tried_on_macOS-lightgrey">
  <img alt="Licence: all rights reserved" src="https://img.shields.io/badge/licence-all_rights_reserved-lightgrey">
</p>

<p>
  <a href="#findings"><strong>Findings</strong></a> ·
  <a href="results/README.md"><strong>Results</strong></a> ·
  <a href="archive/README.md"><strong>Archived Benchmarks</strong></a> ·
  <a href="#methodology"><strong>Method</strong></a> ·
  <a href="PREDICTIONS.md"><strong>Predictions</strong></a> ·
  <a href="BENCHMARK_GUIDE.md"><strong>Run It Yourself</strong></a> ·
  <a href="CODE_MODE_OVERVIEW.md"><strong>Code Mode Overview</strong></a>
</p>

</div>

<details>
<summary><strong>Contents</strong></summary>

- [How Code Mode Works](#how-code-mode-works)
  - [Why It Is Needed](#why-it-is-needed)
- [Code Mode Across the AI Industry](#code-mode-across-the-ai-industry)
- [Benchmark](#benchmark)
  - [Findings](#findings)
    - [Overall Summary of the Benchmark](#overall-summary-of-the-benchmark)
    - [Compared With Claude Code 2.1.325](#compared-with-claude-code-21325)
    - [Detail by Test](#detail-by-test)
    - [Assessment and Recommendations](#assessment-and-recommendations)
  - [Methodology](#methodology)
  - [How a Comparison Runs](#how-a-comparison-runs)
  - [The Tasks](#the-tasks)
  - [What Is Measured](#what-is-measured)
  - [How a Difference Is Judged](#how-a-difference-is-judged)
  - [Results](#results)
  - [Try It Yourself](#try-it-yourself)
  - [Share Your Results](#share-your-results)
  - [Limits](#limits)
- [Repository Layout](#repository-layout)
- [FAQ](#faq)
- [Changelog](#changelog)
- [License](#license)
- [Acknowledgements](#acknowledgements)

</details>

Code Mode is an experimental Claude Code feature (v2.1.323 and later) that lets Claude batch tool calls in code instead of making them one step at a time. Claims about what it saves are easy to find and hard to check. This repository is a small benchmark that anyone can repeat on their own machine: the same six tasks, the same files and the same prompts, with Code Mode off and then on.

## How Code Mode Works

Without Code Mode, Claude works in steps: it can ask for several independent tool calls at once, but each result enters the conversation in full before it decides what to do next. With Code Mode, Claude writes a piece of JavaScript that makes the calls, and only what that code returns goes back to Claude. The official description is in the [Claude Code docs](https://code.claude.com/docs/en/code-mode).

<p align="center">
  <img src="assets/how-code-mode-works.svg" width="720" alt="Two columns. Code Mode off: Claude asks for a tool call, the tool runs, the whole result is added to Claude's context, then the next call. Code Mode on: Claude writes one piece of JavaScript, the code runs many tool calls in one go, and only what the code returns is added to Claude's context.">
</p>

### Why It Is Needed

Code Mode is aimed at two costs: intermediate results that fill the conversation, and the number of requests to the model. With it, the loops, filters and parallel calls happen in code that Claude Code runs in your session, and the model reads only what the code returns.

This benchmark measures both costs. A third cost, tool definitions sent on every request, is mostly addressed by loading tools on demand. Code Mode changes it too: every Code Mode session here started about 13,000 tokens smaller. How that changes with many tools connected is not tested: the benchmark's MCP server has two tools.

## Code Mode Across the AI Industry

Cloudflare named the idea Code Mode in September 2025 and Anthropic followed that November. Through 2026 Codex CLI, OpenCode, goose and Claude Code built it in, along with many MCP gateways, but it is unevenly finished: stable on the Claude API, experimental in Claude Code, and missing from Gemini CLI, Cursor and GitHub Copilot CLI as far as we could find. We found no independent benchmark of Code Mode in coding agents, and the savings figures in circulation are vendors' own examples, which is why this repository exists. The timeline, the tools that have it and a side-by-side comparison are in the **[Code Mode Overview](CODE_MODE_OVERVIEW.md)**.

## Benchmark

**What the benchmark is.** Six small tests, each run in a new Claude Code session with Code Mode off and again with it on, on four models. Everything else is held the same between the two runs: the prompt, the starting files, the model, the effort level and a clean configuration. A checker scores each run against a known answer, and every number is read from the transcript Claude Code saves, not from the screen.

**What it is for:**

- **To measure, not assert.** How many tokens does Claude process to do the same work with Code Mode off and with it on?
- **To find where Code Mode helps and where it does not.** The tests were chosen to disagree: calls to a tool the shell cannot reach, file work the shell can already script, and reading that needs judgement.
- **To check that a saving costs no accuracy.** A run only counts if it passes its check, and the runs that failed are reported.
- **To say what we expected first.** Our predictions were written before the runs, and the wrong ones are left in.
- **To be repeatable by anyone.** The scripts, prompts and test data are all here, and one model takes well under an hour.

**Where to read more:**

| To find                                                                 | Go to                                                                                             |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| What each test asks and how it is scored                                | [The Tasks](#the-tasks)                                                                           |
| How the two runs are kept alike                                         | [Methodology](#methodology)                                                                       |
| What is measured, and when a difference counts                          | [What Is Measured](#what-is-measured) · [How a Difference Is Judged](#how-a-difference-is-judged) |
| What we expected before running anything                                | [Predictions](PREDICTIONS.md)                                                                     |
| Every run, the four models side by side, and the three runs that failed | [Results](results/README.md)                                                                      |
| Earlier benchmarks, each kept whole as it was published                 | [Archived Benchmarks](archive/README.md) · [how archiving works](ARCHIVING.md)                    |
| How to run it yourself                                                  | [Benchmark Guide](BENCHMARK_GUIDE.md)                                                             |
| How to suggest a test or an extension                                   | [Suggesting a Test or an Extension](BENCHMARK_GUIDE.md#suggesting-a-test-or-an-extension)         |
| What code mode is and who else has it                                   | [Code Mode Overview](CODE_MODE_OVERVIEW.md)                                                       |

### Findings

#### Overall Summary of the Benchmark

We ran six tests, each twice with Code Mode off (the default) and twice with it on, on each of four models: 96 runs in all, on Claude Code 2.1.326.

**Tokens processed** is every token the model read or wrote across a run: the input sent with each request, whether or not it came from the prompt cache, plus the output. It already includes the smaller start of a Code Mode session, because the start is sent again with every request. The chart adds up all runs of a model in one mode, first by kind of work and then for all six tests. The saving is largest where records are fetched through a tool, because that is where Code Mode keeps the intermediate results out of the conversation.

<p align="center">
  <img src="assets/tokens-processed-summary.svg" width="880" alt="Bar chart of tokens processed with Code Mode off and on, for four models and four kinds of work. Totalling 120 records fetched through a tool: 62% to 77% saved. Reading and judging the same records: 40% to 68% saved. Finding and changing things in files: 15% to 54% saved on three models, and 9% more used on Haiku 5.5. One question about one file, the control: 29% to 30% saved. Totals for all six tests are given without a percentage. Every figure is in the table below.">
</p>

<details>
<summary><strong>The same figures as a table</strong></summary>

<table border="1">
  <thead>
    <tr><th align="left">Kind of work</th><th align="left">Model</th><th align="right">Tokens processed,<br>Code Mode off</th><th align="right">Tokens processed,<br>Code Mode on</th><th align="right">Saved with<br>Code Mode on</th></tr>
  </thead>
  <tbody>
    <tr><td rowspan="4" valign="top"><strong>Totalling 120 records fetched through a tool</strong></td><td>Opus 5.5</td><td align="right">1.51M</td><td align="right">0.35M</td><td align="right"><strong>77%</strong></td></tr>
    <tr><td>Sonnet 5.5</td><td align="right">1.16M</td><td align="right">0.38M</td><td align="right"><strong>67%</strong></td></tr>
    <tr><td>Haiku 5.5</td><td align="right">1.05M</td><td align="right">0.40M</td><td align="right"><strong>62%</strong></td></tr>
    <tr><td>Fable 5.2</td><td align="right">1.01M</td><td align="right">0.30M</td><td align="right"><strong>71%</strong></td></tr>
    <tr><td rowspan="4" valign="top"><strong>Reading and judging 120 records fetched through a tool</strong></td><td>Opus 5.5</td><td align="right">2.98M</td><td align="right">0.97M</td><td align="right"><strong>68%</strong></td></tr>
    <tr><td>Sonnet 5.5</td><td align="right">2.24M</td><td align="right">1.14M</td><td align="right"><strong>49%</strong></td></tr>
    <tr><td>Haiku 5.5</td><td align="right">2.22M</td><td align="right">1.34M</td><td align="right"><strong>40%</strong></td></tr>
    <tr><td>Fable 5.2</td><td align="right">2.15M</td><td align="right">0.83M</td><td align="right"><strong>61%</strong></td></tr>
    <tr><td rowspan="4" valign="top"><strong>Finding and changing things in files</strong></td><td>Opus 5.5</td><td align="right">1.33M</td><td align="right">0.84M</td><td align="right"><strong>37%</strong></td></tr>
    <tr><td>Sonnet 5.5</td><td align="right">1.01M</td><td align="right">0.46M</td><td align="right"><strong>54%</strong></td></tr>
    <tr><td>Haiku 5.5</td><td align="right">1.19M</td><td align="right">1.30M</td><td align="right"><strong>-9%</strong></td></tr>
    <tr><td>Fable 5.2</td><td align="right">1.02M</td><td align="right">0.87M</td><td align="right"><strong>15%</strong></td></tr>
    <tr><td rowspan="4" valign="top"><strong>One question about one file (the control)</strong></td><td>Opus 5.5</td><td align="right">0.18M</td><td align="right">0.12M</td><td align="right"><strong>29%</strong></td></tr>
    <tr><td>Sonnet 5.5</td><td align="right">0.18M</td><td align="right">0.12M</td><td align="right"><strong>30%</strong></td></tr>
    <tr><td>Haiku 5.5</td><td align="right">0.18M</td><td align="right">0.13M</td><td align="right"><strong>29%</strong></td></tr>
    <tr><td>Fable 5.2</td><td align="right">0.18M</td><td align="right">0.13M</td><td align="right"><strong>29%</strong></td></tr>
    <tr><td rowspan="4" valign="top"><strong>All six tests</strong></td><td>Opus 5.5</td><td align="right">6.00M</td><td align="right">2.29M</td><td align="right">not quoted</td></tr>
    <tr><td>Sonnet 5.5</td><td align="right">4.58M</td><td align="right">2.11M</td><td align="right">not quoted</td></tr>
    <tr><td>Haiku 5.5</td><td align="right">4.65M</td><td align="right">3.17M</td><td align="right">not quoted</td></tr>
    <tr><td>Fable 5.2</td><td align="right">4.37M</td><td align="right">2.13M</td><td align="right">not quoted</td></tr>
  </tbody>
</table>

</details>

**Before you quote these figures:**

- **No percentage is given for all six tests.** That total depends on this mix: three of the six tests make 120 tool calls each, which is where Code Mode does best. If your work is mostly files, read the file-work rows.
- **Tokens processed is not cost.** Most of these tokens are read from the prompt cache, which is billed at a lower rate.
- **File work saved mainly the smaller start.** With Code Mode off, Claude already writes one script to do the whole job. What fell is the 13,000 tokens that every Code Mode session starts smaller by, which the control rows show by themselves, sent again with every request, and in some runs the number of requests.
- **Haiku 5.5's file work cost more with Code Mode on because of one run.** In that run its script looked for files from the wrong folder, and 344 of its 349 shell commands failed. The run still passed, with three times the task context of its twin. Of Haiku's other three file-work pairs, two used fewer tokens with Code Mode on and one used 16% more.
- **Reading and judging is flattered by our test data, and three runs missed records.** The models found patterns in our generated tickets that real records would not have. All three failed runs were Haiku 5.5: two of 16 runs with Code Mode on and one of 16 with it off. Two of the three turn on two tickets whose reading is open to argument.
- **Two runs are behind each figure,** at medium effort on Claude Code 2.1.326.

Only totalling meets our [rule](#how-a-difference-is-judged) for a real difference without a caveat. The [detail by test](#detail-by-test) below uses a second measure, task context, whose percentages are larger because it leaves out the start that every request repeats.

#### Compared With Claude Code 2.1.325

The same benchmark, unchanged, was run on Claude Code 2.1.325 before this round. By the rule we wrote before the 2.1.326 round, a difference between versions counts only if it is larger than the gap between the two runs on either version and points the same way on at least three of the four models. No task met it, in either mode: the two versions gave the same results within the run-to-run noise. Every Code Mode session still started about 13,000 tokens smaller. The comparison, task by task, is on the [results page](results/README.md#compared-with-claude-code-21325).

<details>
<summary><strong>Claude Code 2.1.325 (benchmark 0.3.0), archived 2026-11-17</strong></summary>

<p align="center">
  <img src="archive/claude-code-2.1.325/assets/tokens-processed-summary.svg" width="880" alt="Bar chart of tokens processed with Code Mode off and on, for four models and four kinds of work, on Claude Code 2.1.325. Totalling 120 records fetched through a tool: 60% to 79% saved. Reading and judging the same records: 36% to 65% saved. Finding and changing things in files: 11% to 43% saved. One question about one file, the control: 28% to 29% saved. Totals for all six tests are given without a percentage.">
</p>

[The full benchmark as published for Claude Code 2.1.325](archive/claude-code-2.1.325/README.md)

</details>

#### Detail by Test

The summary groups six tests by kind of work. This section names them and gives the two measures our [rule](#how-a-difference-is-judged) is written in: task context and requests. They explain why tokens processed moved; they are not a second headline. Each test is one prompt, run in a new session with Code Mode off and again with it on, from the same starting files.

- **C0 Control** (one question about one file). Claude answers one question about one Fastify documentation file. It measures the smaller start and nothing else, so it is left out of the table below.
- **T1 Broken links** (file work). 47 Markdown files from the [Fastify](https://github.com/fastify/fastify) project, with five files removed. Claude has to find the 11 links that now point at nothing. This is file work the shell can already script.
- **E1 API change** (file work). A small Python project with 36 calls to one function, written eight different ways, and 39 tests. Claude has to rename the function, change its signature and keep every test passing. This is one change repeated across many files.
- **M1 Aggregate** (totalling). 120 made-up support tickets held by an MCP server, which hands them over one call at a time. Claude has to find the open tickets for one product and add up their refunds: 7 tickets. This is many tool calls where only a total is needed, the case Code Mode is built for.
- **M2 Triage** (reading and judging). The same 120 tickets. Claude has to find the customers who were really charged twice: 9 tickets, among 15 others that only sound like it. Here each ticket has to be read and judged, not just counted.
- **M3 Triage, varied** (reading and judging). The M2 question on the same tickets, reworded so that no sentence repeats. It checks whether M2's saving survives when a script cannot shorten the reading by removing repeats.

[The Tasks](#the-tasks) has each one in full, with how it is scored.

**How to read the table.** Each cell gives the task context, in tokens, with Code Mode off, then with it on, then the change. Task context is how much the conversation grew while Claude did the task. The figures are averaged over the two runs and rounded to the nearest hundred. "Start smaller by" is how many fewer tokens each Code Mode session began with.

| Model      | Checks passed | Start smaller by | T1 Broken links         | E1 API change           | M1 Aggregate           | M2 Triage               | M3 Triage, varied       |
| ---------- | ------------- | ---------------- | ----------------------- | ----------------------- | ---------------------- | ----------------------- | ----------------------- |
| Opus 5.5   | 24 of 24      | 13,106           | 6,400 to 14,300 (+124%) | 9,000 to 13,700 (+52%)  | 54,000 to 4,000 (-93%) | 54,200 to 13,000 (-76%) | 61,000 to 12,400 (-80%) |
| Sonnet 5.5 | 24 of 24      | 13,059           | 4,000 to 3,600 (-11%)   | 6,000 to 7,600 (+26%)   | 53,900 to 3,600 (-93%) | 53,800 to 15,900 (-70%) | 60,800 to 17,800 (-71%) |
| Haiku 5.5  | 21 of 24      | 13,055           | 6,700 to 29,500 (+340%) | 14,200 to 17,500 (+23%) | 54,400 to 8,700 (-84%) | 55,500 to 17,600 (-68%) | 62,200 to 20,600 (-67%) |
| Fable 5.2  | 24 of 24      | 13,057           | 9,500 to 24,300 (+156%) | 12,200 to 18,000 (+48%) | 53,800 to 8,400 (-84%) | 53,900 to 13,300 (-75%) | 60,600 to 16,200 (-73%) |

The averages hide how far two runs can differ, which on T1 and E1 is a long way. The [results page](results/README.md#across-the-four-models) gives every run, in tokens processed and in task context.

What the detail shows:

- **M1: far less context, on every model.** Adding up the 120 tickets took about 54,000 tokens of task context with Code Mode off on all four models, and 3,500 to 8,800 with it on: 84% to 94% less in all eight pairs of runs, with the same correct answer in all 16. Requests fell in every pair. The server received the same calls in both modes, apart from one extra call in each of two Code Mode runs; with Code Mode on, the tickets stayed inside the script. [Details](results/README.md#task-context-and-requests)
- **C0: every Code Mode session started about 13,000 tokens smaller, on every model.** That is 29% to 30% of the first request, because Claude Code sends far fewer built-in tool definitions. Over a whole run of the control it comes to 29% to 30% of tokens processed. Tokens processed was lower with Code Mode on in 46 of the 48 pairs of runs; both exceptions are Haiku 5.5's second pairs on the two file tests. The benchmark's configuration has few tools; how this changes with many is not tested. [Fixed context](results/README.md#fixed-context) · [Tokens processed by test](results/README.md#tokens-processed-by-test)
- **T1 and E1: no saving in the conversation, and often more of it.** Task context was higher with Code Mode on in 14 of the 16 pairs. None of these differences can be told from the noise: on T1 two identical Code Mode runs differed by more than half on every model, and on E1 the two models steady enough to judge rose by less than 35% in one pair each. [What meets our rule](results/README.md#what-meets-our-rule)
- **M2 and M3: far less context, on data that flatters Code Mode.** Task context fell by 65% to 83%. All four models found repeated sentences or sentence patterns in our generated tickets and read only the rare ones. The three runs that left out tickets were all here, all on Haiku 5.5, and one of them had Code Mode off. [The three failed checks](results/README.md#the-three-failed-checks) · [What M2 and M3 show](results/README.md#what-the-m2-result-does-and-does-not-show)
- **What a script prints back decides the context.** The large swings between identical Code Mode runs came from scripts that returned raw data, such as every link a check had set aside or a report on every file changed, and from tool searches with no limit on their results. [Why runs differ](results/README.md#how-much-two-identical-runs-differ)

#### Assessment and Recommendations

**Our assessment:** Code Mode does what it is built for when the work is many calls to tools the shell cannot reach and the answer is much smaller than the data: the intermediate results stay out of the conversation. Where Claude can already write a shell script, the conversation did not shrink and sometimes grew; what fell was the start that every request repeats. And where a script decides what the model reads, accuracy is at risk: in one run a keyword filter left four of nine tickets out of the answer, and on Claude Code 2.1.325 another hid two of nine while the answer said every ticket had been read.

**Recommendations:**

- **Turn it on** for work that makes many MCP tool calls and needs back a count, a total or a short list rather than the records themselves. That is where the saving was large and repeated on every model. It needs an interactive terminal session; see [What You Need](BENCHMARK_GUIDE.md#what-you-need).
- **Expect no saving in the conversation** on file work Claude can do with a shell script. The gain there is the smaller start: 15% to 54% fewer tokens processed on three models in our runs, and 9% more on Haiku 5.5, where one script repeated a failing command hundreds of times.
- **Do not rely on it yet** to read and judge free text cheaply. Our triage savings rest on patterned test data. Check answers that came from a script's filter, and do not take "I read all of them" on trust.
- **Do not quote a single saving.** We report no "X% saved" figure across tasks and no percentage beside the totals, and a Code Mode run's context depends on what its scripts print. See [Limits of This Result](results/README.md#limits-of-this-result).

Every number is on the [results page](results/README.md), with what we [predicted](results/README.md#against-the-predictions) and [what Claude did](results/README.md#what-claude-did). To check them on your own machine, see the [Benchmark Guide](BENCHMARK_GUIDE.md); for where else code mode exists, see the [Code Mode Overview](CODE_MODE_OVERVIEW.md).

### Methodology

The benchmark asks one question of each task: with the same prompt, the same starting files and the same model, what changes when Code Mode is turned on?

1. **Tasks chosen to disagree.** One where Code Mode should make no difference, one the shell can already script, one repeated edit across many files, one with many calls to an MCP tool, and one where those calls need reading and judgement. A benchmark built only from the cases that flatter Code Mode would prove nothing.
2. **Identical starts.** Every run rebuilds the task's files from a frozen copy and begins a new session. Sessions use a clean Claude Code configuration, medium effort, fast mode off, auto permission mode and no memory carried between runs.
3. **Prompts that say what, never how.** Whether Claude writes a script, makes calls one at a time or starts a subagent is its own choice in both modes, and the measurements record what it chose.
4. **Exact answers, checked by script.** Each task has one known right answer and a single pass or fail. A saving only counts if both runs passed.
5. **Measurements from records, not the screen.** The task's own share of the context is reported apart from what the session costs before the task starts, so that one person's setup does not pass for a result.
6. **Predictions first.** What we expect for each task is written in [PREDICTIONS.md](PREDICTIONS.md) before the runs, and the results are reported against it.

### How a Comparison Runs

<p align="center">
  <img src="assets/how-a-comparison-runs.svg" width="620" alt="The task's starting files are rebuilt and given to a new session with Code Mode off, then rebuilt again and given to a new session with Code Mode on, with the same prompt. Both runs are scored and measured, and off is compared with on for the same model and task.">
</p>

Every run starts from identical files, in a new session, with the same prompt. `bin/run.py` rebuilds the task's work folder each time, so nothing carries over from one run to the next.

### The Tasks

Six tasks, chosen to show where Code Mode should help, where it should not, and where it might cost accuracy. Each runs once with Code Mode off and once with it on: twelve sessions per model.

| Task   | What Claude is asked to do                                                                | What it tests                                                                                                       | How it is scored                                                                                        |
| ------ | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **C0** | Answer one question about one file                                                        | The control: Code Mode's fixed cost when there is nothing to save                                                   | The answer states the right fact and no file changes                                                    |
| **T1** | Find the broken local links across 47 Markdown files in the Fastify repository            | Work the shell can already script. This is close to the example in Claude Code's own docs                           | Against the 11 known broken links                                                                       |
| **E1** | Rename a function and change its signature across 36 call sites in a small Python project | A change repeated across many files, with Claude Code's built-in tools                                              | The project's 39 original tests pass, and no trace of the old name is left                              |
| **M1** | Find the open Atlas tickets among 120 support tickets held by an MCP server               | Many calls to a tool the shell cannot reach, where only a total is needed. Built to favour Code Mode                | Against the 7 known tickets and their total, and only if all 120 tickets were fetched through the tools |
| **M2** | Find the tickets where the customer was really charged more than once                     | The same many calls, but each ticket has to be read and judged. Designed so that filtering in code should miss some | Against the 9 known tickets, with the same rule about fetching                                          |
| **M3** | The same question as M2, on the same tickets reworded so that no sentence repeats         | Whether M2's saving survives when the data cannot be shortened by removing repeats. Added after the first results   | Against the same 9 tickets, with the same rule about fetching                                           |

C0 and T1 run on [Fastify](https://github.com/fastify/fastify)'s documentation: a real, well-known project, small enough to download in seconds, whose Markdown files link to each other with relative paths. Its docs have no broken links, so five files are removed to leave eleven links that point at nothing, and the right answer is known exactly.

The MCP server ships with this repository and starts automatically. It uses only the Python standard library and needs no account.

### What Is Measured

Everything comes from machine records, not from reading the screen.

| Measure                                                                                                                             | Source                                                |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| Pass or fail, with the detail behind it                                                                                             | `bin/check.py`, run automatically when a session ends |
| **Tokens processed, the headline measure:** every request's input added up over the session, cached or not, plus every output token | The saved transcripts                                 |
| Fixed context: tokens sent in the session's first request (system prompt, tool definitions and your prompt)                         | The first request in the saved transcript             |
| Task context: tokens in the last request plus its reply, minus the fixed context                                                    | The saved transcript                                  |
| Requests to the model, including any subagents                                                                                      | The saved transcripts                                 |
| Tools actually run, including those run from Code Mode scripts                                                                      | A logger that Claude Code calls before every tool     |
| MCP calls made                                                                                                                      | The MCP server's own count                            |
| Time and cost                                                                                                                       | The saved transcript                                  |

Tokens processed is what the [summary](#overall-summary-of-the-benchmark) reports. Fixed context, task context and requests explain it: the fixed context is sent again with every request, so a smaller start and fewer requests both lower it, while task context shows whether the conversation itself grew. `bin/measure.py` also prints `total_in`, the same sum without the output; the published results use tokens processed only.

Fixed context and task context count the main conversation only. If Claude starts a subagent, its work shows in the request count and tokens processed, not in these two.

### How a Difference Is Judged

One run of each is one sample, and runs vary. A difference counts only if all of these hold: both runs passed; both models differ in the same direction; and task context or requests differ by more than 35%.

Repeating two of the Code Mode off runs shows how much runs vary by themselves. If those repeats differ from each other by more than 35% on a measure, that measure is reported as too noisy to judge. If you run one model, report your difference as one model, one sample.

The noise rule is applied task by task. We settled that reading on 2026-11-16, after our second round: there, T1 with Code Mode off differed from its repeat by 36% on task context, while M1 and M2 with Code Mode off repeated to within 1%. Read across all tasks at once, the rule would have discarded the steadiest results with the noisiest. Our second round also repeated every run, not two of them.

The rule was written before the runs, in task context and requests, and it is still the test of whether a difference is real. The headline measure, tokens processed, is reported beside it and not judged by it: it carries the smaller start into every request, so it can fall even where task context rose, as it did on the file tasks.

No single "X% saved" figure is reported across tasks, and no percentage is given beside the totals: the tasks were chosen to differ, and an average would hide that.

### Results

Four models have been run on Claude Code 2.1.326: Opus 5.5, Sonnet 5.5, Haiku 5.5 and Fable 5.2, each twice on every task in each mode. Of 96 runs, 93 passed their checks. The same benchmark on Claude Code 2.1.325 is [archived](archive/claude-code-2.1.325/README.md). What they show is under [Findings](#findings), at the start of this section: tokens processed by model and by kind of work, then task context for every model and test.

The [results page](results/README.md) has every run, the four models side by side, what Claude did, the three runs that failed, how the results compare with Claude Code 2.1.325 and with the [predictions](PREDICTIONS.md), and a log of what changed between rounds.

You do not have to take our word for it. The same benchmark runs on your own machine in well under an hour: see [Try It Yourself](#try-it-yourself) below, or go straight to the **[Benchmark Guide](BENCHMARK_GUIDE.md)**.

### Try It Yourself

You can run the same benchmark on your own machine and compare the two modes with each other. Our numbers for four models are above. You need Claude Code v2.1.323 or later in a terminal, a Claude subscription or Console account, `git` and `python3` ([full list](BENCHMARK_GUIDE.md#what-you-need)). The sessions use your plan or API credit like any other session.

```bash
git clone https://github.com/Bicameral-AI/claude-code-mode-benchmark.git
cd claude-code-mode-benchmark
bin/setup.py
bin/run.py C0 off opus   # then the same with "on"; the guide covers the one-time sign-in first
bin/measure.py
```

The **[Benchmark Guide](BENCHMARK_GUIDE.md)** has the full walkthrough: the one-time sign-in, what each command prints, all twelve runs, how to let a script do the typing, and what to do when Code Mode does not start. To test another model, see [Models and Effort](BENCHMARK_GUIDE.md#models-and-effort).

A script can do all twelve runs for you: see [Option B: By Script](BENCHMARK_GUIDE.md#option-b-by-script).

### Share Your Results

Ran it yourself? Open an issue with your `results/measure.txt` and `results/checks.txt`, the Claude Code version and the models you used. Results that differ from ours are as interesting as ones that agree.

### Limits

- Code Mode is experimental and may change or be removed.
- Runs of a language model vary. One run of each is one sample, and the results page says how many runs each number rests on.
- Six small tasks say little about other kinds of work, and the totals in tokens processed reflect this mix: three of the six make 120 tool calls each, where Code Mode does best. In particular, none of them runs long enough to fill a large context window; a long-run task for that is not built.
- The results depend on what Claude chooses to do. A task where Claude writes a shell script with Code Mode off will show little difference, and that is a finding, not a fault.
- The results are two runs per task and mode on four models, at one effort level and on one version of Claude Code, 2.1.326. Two runs show that a figure can move, not how far it usually moves.
- The scripts have been tried on macOS only.

## Repository Layout

<details>
<summary><strong>Show the file tree</strong></summary>

```text
.
├── README.md
├── BENCHMARK_GUIDE.md      how to run the benchmark
├── CODE_MODE_OVERVIEW.md   why code mode, who has it, tools that add it
├── PREDICTIONS.md          what we expected, written before the runs
├── ARCHIVING.md            how a new benchmark replaces the current one, step by step
├── CHANGELOG.md            what changed, and when results stop being comparable
├── LICENSE
├── tasks/                  the six prompts: C0, T1, E1, M1, M2, M3
├── bin/
│   ├── setup.py            build the test files and work folders
│   ├── run.py              do one run: prepare, start the session, score it
│   ├── run-all.py          every run for a model, back to back, typed by the script
│   ├── autopilot.py        the part of run-all.py that types into the session
│   ├── measure.py          print the numbers for every run
│   ├── validate.py         check a set of runs before its results are published
│   ├── archive.py          keep a full copy of a published benchmark, verify it, promote a new run
│   ├── publish.py          build the published copy of the benchmark, check it, commit it
│   ├── privatelist.py      read private-files.txt, the files never archived or published
│   ├── check.py            score a run (run.py calls it for you)
│   ├── new-round.py        start a clean set of runs
│   ├── clean.py            remove everything the benchmark built, back to a fresh download
│   └── benchlib.py         shared paths and helpers
├── mcp/
│   ├── records_server.py   the benchmark's MCP server
│   └── records.py          the tickets it serves
├── fixtures/
│   └── invoice_gen.py      generates the Python project for task E1
├── assets/                 the diagrams on this page, and their sources
├── archive/                earlier benchmarks, each a complete copy as published
└── results/
    ├── README.md           results page
    ├── measure.txt         the numbers for every run, as bin/measure.py printed them
    ├── compare.txt         first run beside latest, for everything run more than once
    ├── checks.txt          the checker's verdict for every run
    ├── context/            Claude Code's own context report for each scripted run
    └── screenshots/
```

</details>

Nothing a test session works on is stored here. `bin/setup.py` builds the starting files and the benchmark's own Claude Code configuration under `~/.cache/claude-code-mode-benchmark`, and the folders sessions run in under `/var/tmp`. Those are outside your home folder on purpose: Claude Code loads any `CLAUDE.md` it finds in the folders above a session, and yours would otherwise be read into every run.

## FAQ

<details>
<summary><strong>Why does it use a clean configuration?</strong></summary>

In an early trial, which is not part of the results, most of the session's starting context came from the author's own plugins, skills and agents, and the task itself added comparatively little. Numbers like that say more about a person's setup than about Code Mode. A clean configuration gives everyone the same starting point. It costs one extra sign-in. The clean configuration removes your local plugins, hooks, settings and memory files, and the work folders sit where your own `CLAUDE.md` is not loaded. Skills and plugins synced to your Claude account still load, which is one reason the starting context is reported separately from the task. In our runs, skills and custom agents took about 10,400 tokens of every session's start, in both modes alike, and part of that came from the author's account. Your starting context may differ from ours by up to that much.

</details>

<details>
<summary><strong>What is the MCP server for?</strong></summary>

Tasks M1, M2 and M3. A coding agent with a shell can already batch file work by writing a script, so tasks on files alone leave Code Mode little to improve. MCP tools cannot be reached from the shell, so without Code Mode each call is a separate step. The server in `mcp/` holds 120 made-up support tickets and logs every call it receives, which is how a run is checked to have really fetched them all.

</details>

<details>
<summary><strong>Why is there no task built on subagents?</strong></summary>

Subagents already keep their work out of the main conversation without Code Mode, and a prompt that asks for them would be telling Claude how to do the job. So the benchmark does not ask for subagents, but it counts them: if Claude chooses to use one, its requests and tokens are counted and the number of subagents is reported.

</details>

<details>
<summary><strong>Why will my numbers differ from yours?</strong></summary>

Runs of a language model vary, and Claude may choose a different way to do the same task. Your session's start can also differ from ours by up to about 10,400 tokens (see the first question), and tokens processed carries that difference into every request. Compare your own two modes with each other, task by task. To set your figures beside ours, use task context, which leaves the start out.

</details>

## Changelog

Changes to the tasks, prompts, scoring or measurements are recorded in [CHANGELOG.md](CHANGELOG.md), because any of them makes earlier results not comparable with later ones.

## License

Copyright © 2026 Bicameral, LLC. All rights reserved.

This repository is published so that its method and results can be examined and checked. It is not open source. You may download it and run it to evaluate Code Mode for yourself, and publish the results you get with credit and a link back. You may not redistribute it, publish a modified version, present it as your own benchmark, or include any part of it in a product, service, dataset or other benchmark without written permission. The full terms are in [LICENSE](LICENSE).

## Acknowledgements

- [Fastify](https://github.com/fastify/fastify), MIT licensed, is the test repository. It belongs to its authors and is downloaded, not redistributed.
- The [Code Mode documentation](https://code.claude.com/docs/en/code-mode) is the reference for how the feature works.

This is an independent test. It is not affiliated with or endorsed by Anthropic or the Fastify project.

---

© 2026 Bicameral, LLC. All rights reserved. See [LICENSE](LICENSE).
