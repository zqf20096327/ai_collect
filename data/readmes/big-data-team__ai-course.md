# About

The repository is used during the following courses:
1. Practical AI Course: Agentic Coding & AI Agents (AI Agents Engineer Specialization)

- AI agents: tools and MCP
- agentic coding and agentic environment
- LLMs, Ralph-loop and evals
- context & memory, agent harness
- capstone project
- https://bigdatateam.org/ru/artificial-intelligence-course

# Environment Configuration

Solutions are graded on Python 3.10 with the packages from [requirements.txt](requirements.txt).

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/)
2. Download [requirements.txt](requirements.txt)
3. Create the environment:
```bash
# uv downloads Python 3.10 itself if there is none on the machine
uv venv --python 3.10
source .venv/bin/activate
uv pip install -r requirements.txt
```

For more information about Python virtual environments see:
* https://docs.astral.sh/uv/pip/environments/
* https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
* https://docs.python.org/3/library/venv.html

See the Python version and the packages of the environment with the help of:
```bash
uv run python --version
uv pip list
```

If you need to remove the environment, delete its folder:
```bash
rm -rf .venv
```

# Programming Assignments

## HW01: AI Tool for Datetime Parsing (`ai.tool_datetime_parser`)

Starter files: [hw01_tool_datetime_parser](hw01_tool_datetime_parser)

| File | What it is |
|---|---|
| `task_Surname_Name_tool_datetime_parser.py` | the function template: rename it to `task_<Surname>_<Name>_tool_datetime_parser.py` |
| `tool.json` | the MCP Tool description: write your texts instead of `<...>`, keep `outputSchema` as is |
| `tests.json` | your test cases, required: replace the example with your own (up to 5 public and 10 private) |
| `open_cases.json` | the open test cases of the Grader |
| `check_open_cases.py` | a self-check on the open cases |

How to run the self-check:
```bash
cd hw01_tool_datetime_parser
uv run python check_open_cases.py task_Dral_Alexey_tool_datetime_parser.py
```

### Grading

| Grader check | Weight | What it checks |
|---|---|---|
| `test_open_cases` | 0.3 | 66 open phrases from `open_cases.json` |
| `test_hidden_cases` | 0.5 | 192 hidden phrases: 16 categories, 12 each |
| `test_contract` | 0.2 | `tool.json`, responses against `outputSchema` and 6 robustness probes; counts along the hidden score, from 0 at 20% to the full weight at 50% |
| `test_open_cases_failures`, `test_hidden_cases_summary`, `test_contract_details` | 0 | details for you: failed open phrases, results per category, failed contract checks |
| `test_tests_json` | 0 | your `tests.json`: format, limits and which of your tests your tool fails |

A submission without `tests.json`, with invalid JSON in it or with an empty list is not admitted: the score is 0.

How simple approaches score with a perfect `tool.json`:

| Solution | Score |
|---|---|
| the reference solution | 1.0 |
| a wrapper over `dateparser` (not available in the Grader, run outside the sandbox) | ≈0.45 |
| ISO 8601 / RFC 3339 / Unix time only | ≈0.26 |
| `dateutil.parser` with `fuzzy=True` | ≈0.22 |
| always `not_found` | ≈0.10 |

The categories weigh the same, so simple formats do not outweigh hard ones:

| Category | Examples from the open cases | Open phrases |
|---|---|---|
| `iso_rfc3339` | `2026-11-04T17:00:00+05:00`, `2026-11-04T12:00:00Z`, `2026-11-10 15:30` | 4 |
| `unix_time` | `1793872800`, `1793872800000` | 2 |
| `numeric_dates` | "03.04.2026", "03/04/2026", "в 10.11" | 6 |
| `words_ru` | "4 ноября", "25 декабря в 19:00" | 5 |
| `words_en` | "November 20 at 3pm", "on 5 December 2026" | 2 |
| `relative_ru` | "завтра в 10:30", "сегодня в 16:55" | 12 |
| `relative_en` | "tomorrow at 5pm", "in 2 hours" | 2 |
| `weekdays` | "в пятницу в 15:00", "в ближайшую субботу" | 8 |
| `time_of_day` | "в 5", "в 9 утра", "в 19:15" | 5 |
| `explicit_zone` | "в 15:00 по Москве", "в 9:00 по Алматы" | 2 |
| `dst` | "завтра в 2:30" the day before a clock change | 2 |
| `history` | "встреча 2024-02-15 10:00": a past offset of the zone | 3 |
| `invalid_date` | "30 февраля", "31.04.2026", "в 25:00" | 3 |
| `no_date` | "привет, как дела?", "купи 2 литра молока" | 3 |
| `multiple` | "напомни завтра утром про встречу в пятницу в 15:00" | 2 |
| `reference_rules` | "через час", "завтра в 10:00" with different `reference_time` and `timezone` | 5 |

## HW02: AI Skill for Job Market Analysis (`ai.skill_hr_assistant`)

Here is what you build. The skill of our HR assistant made the "Typical Python developer" card below: a script counted the numbers over the vacancies of 2018 and 2024, and the layout is a part of the skill too. Your skill answers the same questions for a fresh 12-month window.

![Typical Python developer: top skills in Python vacancies, 2018 and 2024](images/hw02_example_skills.png)

![Typical Python developer: Python vacancies of 2024 and those available remotely from Kazakhstan](images/hw02_example_vacancies.png)

The card shows the answer of our skill, not the reference answer of the calibration: in `calibration_2024.json` the same year has 855 Python vacancies.

Starter files: [hw02_skill_hr_assistant](hw02_skill_hr_assistant)

| File | What it is |
|---|---|
| `prompt.txt` | the fixed prompt of every run: do not change it |
| `run.sh` | one isolated non-interactive run of the prompt in Claude Code, Codex or OpenCode |
| `check_answer.py` | checks the form of the final answer in a run log: the contract of the prompt, the window and the invariants; there is no etalon in it |
| `make_calib_data.py` | a copy of the dataset cut at 2024-12, for the calibration run |
| `calibration_2024.json` | the calibration package: the etalon answer for the window 2024-01..2024-12, the base of your own eval |
| `pack.py` | optional: builds `HW02_<Surname>_<Name>.zip` and checks an archive the way the Grader does |

`check_answer.py`, `make_calib_data.py` and `pack.py` need Python 3 with its standard library only and work on any OS (on Windows the command is often `py` or `python` instead of `python3`).

The skill follows the open Agent Skills standard and does not depend on the agent: you may work in Claude Code, Codex or OpenCode, further agents are added on request. `run.sh` starts all three, and the Grader reads the logs of all three; submission in learn opens together with the automatic check.

The Grader does not run models or your code. It reads:
- the skill in `skill/hr-assistant/`;
- the files of each run in `runs/<stage>_<model>_r<number>/`: `log.jsonl`, `stderr.txt`, `wall_seconds.txt` and, for Codex and OpenCode, `agent.json`.

So the OS and the way you start the agent are yours to choose, as long as the Grader can read the run. Do steps 1 and 3 in one agent with one model: different agents count as different models. If step 1 has no valid run of the step 3 model with a JSON object in the final answer and a run time, the Grader takes the step 1 runs of another model as the base of the speedup, the model with the most such runs (a stronger model is expected), and marks this base for the mentors.

| Agent | Skill directory in the run | What the log gives | How the Grader sees the skill call |
|---|---|---|---|
| [Claude Code](https://code.claude.com/docs/en/headless) | `.claude/skills/hr-assistant/` | answer, model, time, cost, tokens | the Skill tool |
| Codex | `.agents/skills/hr-assistant/` | answer, tokens; no model, time or cost: the time comes from `wall_seconds.txt`, the model from `agent.json` | Codex has no skill tool: a command that touches the skill directory (`skills/hr-assistant`) counts as using the skill |
| OpenCode | `.opencode/skills/hr-assistant/` | answer, time (from the log timestamps), cost, tokens; the model comes from `agent.json` | its skill tool |

A Codex log has no cost. The score does not use the cost: the speedup is counted by time and works as usual.

`run.sh` is a bash script that starts the agent named with `--agent`: `claude` (the default), `codex` or `opencode`. Where it works:
- Claude Code: macOS, Linux and Windows inside WSL2. On Linux and in WSL2 install the packages `bubblewrap` and `socat` for the Claude Code sandbox; in WSL keep the solution folder in the WSL file system, not under `/mnt/c`, where file access is much slower;
- Codex and OpenCode: tested on macOS only, with codex-cli 0.153.0-alpha.5 (ChatGPT login, `gpt-5.6-luna` and `gpt-5.6-terra`) and OpenCode 1.18.30 (an Anthropic key, `anthropic/claude-haiku-4-5`). On Linux and in WSL `run.sh` starts them with a "not tested on this OS" note;
- native Windows without WSL is not covered: use WSL.

### Setup

Copy the folder `hw02_skill_hr_assistant` out of your clone of this repository: it becomes your solution folder. Unpack the dataset (see [Datasets](#datasets)) into `data/` of it and run every command from it:

```
my_solution_folder/
    prompt.txt, run.sh, ...   the starter files
    data/                     the dataset: hn_whoishiring_2018-01.json .. hn_whoishiring_2026-11.json
    data_2024/                python3 make_calib_data.py data/ data_2024/
    my_draft/hr-assistant/    step 2: SKILL.md only, not submitted
    skill/hr-assistant/       step 3: SKILL.md, scripts/, references/
    runs/                     created by run.sh: the files of each run
```

### Runs

`./run.sh <stage> <model> <number> <skill_dir | none> <data_dir> [--agent claude|codex|opencode]`: the stage is `noskill` (step 1), `draft` (step 2), `skill` (step 3) or `calib` (the calibration). The model depends on the agent:
- Claude Code: a short name (`haiku`, `sonnet`, `opus`) or a full model id;
- Codex: a full model id, such as `gpt-5.6-luna`; short names and ids with "/" are refused;
- OpenCode: `provider/model`, such as `anthropic/claude-haiku-4-5`.

Steps 1 and 3 run in one agent on one base model.

```bash
./run.sh noskill haiku 1 none data/                     # step 1: runs 1, 2 and 3 of the base model
./run.sh noskill opus 1 none data/                      # step 1 on a strong model: optional
./run.sh draft haiku 1 my_draft/hr-assistant data/      # step 2: as many runs as you need
./run.sh skill haiku 1 skill/hr-assistant data/         # step 3: runs 1, 2 and 3
python3 make_calib_data.py data/ data_2024/
./run.sh calib haiku 1 skill/hr-assistant data_2024/    # the calibration: optional
python3 check_answer.py runs/skill_haiku_r1/log.jsonl   # the form of the answer

# the same steps in Codex and in OpenCode: only the model and --agent change
./run.sh noskill gpt-5.6-luna 1 none data/ --agent codex
./run.sh skill gpt-5.6-luna 1 skill/hr-assistant data/ --agent codex
./run.sh noskill anthropic/claude-haiku-4-5 1 none data/ --agent opencode
./run.sh skill anthropic/claude-haiku-4-5 1 skill/hr-assistant data/ --agent opencode
```

What `run.sh` does:
- the run works in `${HW02_RUNS_DIR:-~/hw02_runs}/<stage>_<model>_r<number>/`, which must lie outside any git repository: its own copy of the data in `data/`, the skill where the agent looks for it (`.claude/skills/hr-assistant/`, `.agents/skills/hr-assistant/` or `.opencode/skills/hr-assistant/`);
- Claude Code: the `.claude/settings.json` of the run turns the sandbox on and denies reading the other runs, your solution folder, the source skill and data and `~/.claude`; `claude -p` loads the project settings only (none of your personal skills and `CLAUDE.md`), no MCP servers and no web search, with a budget of $2 per run;
- Codex: `codex exec` ignores its own config; rules, plugins, apps, hooks, memories, bundled skills, `AGENTS.md` and web search are off; the seatbelt sandbox lets it write only into the run directory, with no network, and denies reading `~/.codex`, `~/.claude`, `~/.ssh`, `~/.config`, your solution folder and the other runs; it inherits the environment without the variables whose names contain `KEY`, `SECRET` or `TOKEN`;
- OpenCode: `opencode run` gets its own config directory, temp directory and database per run; your personal config, the Claude Code skills and external skills are off, only the skill `hr-assistant` is allowed, external directories, web fetch, web search and sub-agents are denied;
- Codex and OpenCode have no budget cap: `run.sh` stops a run after `HW02_TIMEOUT_SECONDS` seconds (900 by default);
- after the run it copies `log.jsonl`, `stderr.txt`, `wall_seconds.txt` and, for Codex and OpenCode, `agent.json` to `runs/<stage>_<model>_r<number>/` of the current folder (`--out DIR` changes it), only if they are plain files, and prints the model, whether the agent used the skill and whether it ran a script from `scripts/`.

Good to know:
- the run name is cleaned: the model is lowercased and every character other than `a-z 0-9 . -` becomes `-`, so `Model_X` gives `noskill_model-x_r1` and `anthropic/claude-haiku-4-5` gives `skill_anthropic-claude-haiku-4-5_r1`;
- a run directory is never reused: if it exists, `run.sh` stops and asks for the next number;
- a Claude Code run has three files: `log.jsonl`, `stderr.txt`, `wall_seconds.txt`. A Codex or OpenCode run has a fourth one, `agent.json`: `{"agent": "codex", "model": "gpt-5.6-luna", "agent_version": "codex-cli 0.153.0-alpha.5"}`. Their logs name no model, so the Grader takes it from this file: at most 4 KB, all three keys are required strings, `agent` is `codex` or `opencode`. A Claude Code run needs no `agent.json`; if one is there, it must be complete too;
- if you start Codex or OpenCode by hand, write `agent.json` yourself: the model is what you passed to `-m` (Codex) or `providerID/id` from `opencode export <sessionID>` (OpenCode), the version is the output of `codex --version` or `opencode --version`. Write `wall_seconds.txt` too: one number, the seconds measured around the agent command. Codex needs it, because its log has no time; for OpenCode it is a fallback;
- Codex and OpenCode have no budget cap: a run is stopped after `HW02_TIMEOUT_SECONDS` seconds, 900 by default (`HW02_TIMEOUT_SECONDS=1800 ./run.sh ...` changes it);
- OpenCode is isolated less than the other two: its bash tool has no OS sandbox, so it can read files outside the run and reach the network. It also sees your environment variables, an API key included, and a model may print them into the log, which goes into the archive. Do not keep secrets in the environment of a run;
- if a newer Codex refuses a flag of `run.sh`, the run ends at once with an empty log, and `run.sh` prints the version it was tested with next to yours;
- without the skill Codex and OpenCode sometimes do not put the JSON into the final message (Codex once wrote it to a file). The Grader reads only the final message, so such a step 1 run cannot be the base of the speedup, though it still counts for the process part: `run.sh` and `check_answer.py` warn about it. One valid step 1 run with a JSON object is enough for the base, three are safer. If the base model gives no JSON without the skill at all, add step 1 runs of a stronger model to the archive, so that the speedup has a base;
- a failed run: delete its directory in `runs/` (its working copy in `HW02_RUNS_DIR` may go too) and start the next number; the submission holds exactly three `skill_*` runs;
- do not start runs in parallel in one `HW02_RUNS_DIR`: a run closes only the run directories that exist when it starts;
- the working copies in `HW02_RUNS_DIR` (`~/hw02_runs` by default) may be deleted once a run is over: each run copies the data, about 100 MB where the file system cannot clone files. After that pass the data to the check yourself: `python3 check_answer.py runs/skill_haiku_r1/log.jsonl --data data/`;
- the logs hold absolute paths and the user name of your machine: that is fine, only the Grader and the mentors see the archive;
- `check_answer.py` says that the answer is well formed, not that the numbers are right: compare your calibration run with `calibration_2024.json` in your own eval (3.2.8 of the assignment);

### Archive

The standard way, from the solution folder (put your surname and name instead of `Dral_Alexey`):

```bash
zip -r HW02_Dral_Alexey.zip skill runs -x "*.DS_Store" "*__pycache__*" "runs/draft_*"
python3 pack.py --check HW02_Dral_Alexey.zip
```

On Windows first delete the `__pycache__` folders and move the `draft_*` runs out of `runs/` into another folder, then select only `skill` and `runs` and choose Send to > Compressed (zipped) folder.

Or build and check in one go:

```bash
python3 pack.py Dral Alexey
```

It packs `skill/hr-assistant/` and the runs `noskill_*`, `skill_*`, `calib_*` from `runs/` with their run files (`log.jsonl`, `stderr.txt`, `wall_seconds.txt` and, for Codex and OpenCode, `agent.json`), and leaves out `draft_*`, the data and service files. Do not put `draft_*` runs into a hand-made archive either.

`pack.py --check` repeats the checks of the Grader and reports on three levels:
- errors: the Grader rejects the whole archive, the score is 0 (over 3 MB, a path outside the archive, a symbolic link, a forbidden extension, no `runs/`, ...);
- zeroed: the archive is accepted, but Skills, Remote and the speedup get 0 (the skill does not pass `skills-ref validate` or the requirements of the assignment: the directory, `name: hr-assistant`, a non-empty `scripts/`; not three `skill_*` runs; the skill or its script was not called, ...);
- warnings: a part of the score may suffer (fewer than three valid `noskill_*` runs of the base model, service files, ...).

#### Check the skill with `skills-ref`

`skills-ref` is the reference validator of agentskills.io. Install it from git only, at the commit the Grader follows: the package of the same name on PyPI is not maintained by the authors of the standard.

```bash
uv tool install "git+https://github.com/agentskills/agentskills@83021e2be457a9b6679148719c1f6074f0ad975e#subdirectory=skills-ref"
```

It needs Python 3.11+, uv brings it. If `skills-ref` is not found afterwards, run `uv tool update-shell`.

On Windows set `PYTHONUTF8=1` first, otherwise `skills-ref` reads `SKILL.md` in the code page of the system and fails on non-English text:
- PowerShell: `$env:PYTHONUTF8=1`;
- cmd: `set PYTHONUTF8=1`.

Check the skill:

```bash
skills-ref validate skill/hr-assistant
```

The Grader zeroes Skills, Remote and the speedup on:
- everything `skills-ref` reports:
  - frontmatter that is not valid YAML;
  - the `name` and `description` rules;
  - a `description` over 1024 characters, a `compatibility` over 500;
  - a field other than `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`;
- the requirements of the assignment: the directory `skill/hr-assistant/` with `SKILL.md`, `name: hr-assistant`, a non-empty `scripts/`.

Some agents still load a skill with these mistakes, but `skills-ref` and the Grader do not accept it:
- a `description` with ": " inside and without quotes: the frontmatter is then not valid YAML;
- lists in brackets, such as `allowed-tools: [Bash, Read]`;
- a byte order mark at the start of `SKILL.md`: PowerShell 5.1 writes one with `-Encoding UTF8`.

```yaml
description: "Job market analysis: skills and remote vacancies"   # quoted, valid
```

Only remarks in `test_skill_diagnostics`, the score does not change:
- a `SKILL.md` longer than 500 lines: the standard recommends moving details to `references/`;
- a file `scripts/...`, `references/...` or `assets/...` named in `SKILL.md` but missing in the skill.

### Grading

| Grader check | Weight | What it checks |
|---|---|---|
| `test_process` | 0.1 | step 1: the share of valid runs of the base model, up to three; a valid run has a readable log with one session and a model id, finished with success, had no skill and is not a copy of another run |
| `test_skills` | 0.4 | question 1, skills: the mean Skills of the three runs of step 3 |
| `test_remote` | 0.3 | question 2, available to me: the mean Remote of the three runs of step 3 |
| `test_speedup` | 0.2 | the full weight if the median time of the base divided by the median time of step 3 is 3 or more, and the mean Q = (Skills + Remote) / 2 of step 3 is at least 0.6; otherwise 0. The base is the valid step 1 runs with a JSON object in the final answer and a run time: those of the step 3 model, or, if it has none, of the model with the most such runs. One run is enough |
| `test_skill_diagnostics` | 0 | remarks for you, shown only when there are any: the layout of the archive and `draft_*` runs, remarks on `SKILL.md`, numbers in the skill that look like HN post ids, invalid step 1 runs with the reasons, step 3 runs off the answer contract or with skill names outside the reference, step 1 runs over the reading limit (6 runs of the step 3 model and 6 of the other models). The reasons of a partial score are here too |

The report lists every check with its score, and only a failed check carries a text with the reasons. A weighted check fails only at 0; at a partial score it passes, its share shows as `raw_score`, and the reasons are in `test_skill_diagnostics`. While the checks pass, the report shows no time, cost or speedup of your runs: the numbers of the speedup (the speedup, the median times of steps 1 and 3, the model and the size of the base) appear only in a failed `test_speedup`. The Grader does not grade or report the calibration runs (`calib_*`): compare your calibration run with `calibration_2024.json` in your own eval.

How Skills and Remote are computed, and what zeroes each part, is in section 3.4 of the assignment.

Our reference runs in Claude Code on the dataset: Haiku is the simple model, Opus the strong one, the skill of steps 2 and 3 is the same; three runs per line, ranges over the runs (section 3.2.5 of the assignment):

| Step | Model | Skills | F1 → Remote | Q | Time of a run, s | Cost of a run, $ |
|---|---|---|---|---|---|---|
| 1. The prompt only | Haiku | 0–0.45 | 0–0.62 → 0–0.30 | 0–0.38 | 176–440 | 0.023–0.053 |
| 1. The prompt only | Opus | 0–0.37 | 0–0.48 → 0 | 0–0.18 | 166–440 | 0.51–0.83 |
| 2. The skill as text | Haiku | 0.80–0.84 | 0.83–0.93 → 0.83–1.00 | 0.83–0.90 | 62–249 | 0.017–0.055 |
| 2. The skill as text | Opus | 0.83 | 0.95–0.96 → 1.00 | 0.92 | 276–304 | 1.19–1.32 |
| 3. The skill + tool | Haiku | 0.84 | 0.95 → 1.00 | 0.92 | 19–20 | 0.006 |
| 3. The skill + tool | Opus | 0.84 | 0.95 → 1.00 | 0.92 | 32–35 | 0.21 |

Our runs in the other two agents, with the skill: Codex on `gpt-5.6-luna` took 52–57 s with Q 0.92; OpenCode on Haiku 4.5 took 24–25 s and $0.028 per run with Q 0.92.

While the model counts, a stronger model buys little quality for a lot of money. Once the tool counts, the strong model is not needed at all: it runs the same script and returns the same answer.

How our reference submissions score in the same Grader, steps 1 and 3 on the simple model (section 3.4 of the assignment):

| Submission | Score |
|---|---|
| steps 1 and 3; our reference skill | 0.94 = 0.1 + 0.4 × 0.84 + 0.3 × 1.00 + 0.2 |
| steps 1 and 3; a skill with weak "available to me" rules | 0.78 = 0.1 + 0.4 × 0.86 + 0.3 × 0.46 + 0.2 |
| the skill of step 2 submitted as the final one, without `scripts/` | at most 0.1: only the process of step 1 counts, Skills, Remote and the speedup are zeroed |
| step 1 only | 0.1 |

## Datasets

| Dataset | Used in | What is inside | Link |
|---|---|---|---|
| Hacker News "Ask HN: Who is hiring?" threads, 2018-01..2026-11, snapshot of 2026-11-19 | HW02 | a zip of 27.8 MB: 107 JSON files and `README.txt` | [Google Drive](https://drive.google.com/file/d/18x0Wqn6u7KIUe24j7Eur3btO2SOA7Gfg/view) |

Unpack the archive after download with any tool of your OS. It holds one folder, `hn_whoishiring_2018-01_2026-11`: move it into your solution folder and rename it to `data`. The JSON files must lie directly in `data/`, not one folder deeper: some unpackers, Windows Explorer among them, wrap the content into one more folder with the name of the archive.

The same from a terminal, on any OS (on Windows `py` or `python` instead of `python3`):

```
python3 -m zipfile -e hn_whoishiring_2018-01_2026-11.zip .
```

Then rename the folder: in the file manager, with `mv` on macOS, Linux and WSL, or with `ren` in the Windows command line:

```bash
mv hn_whoishiring_2018-01_2026-11 data
```

`hn_whoishiring_YYYY-MM.json` is the answer of the Algolia HN API `https://hn.algolia.com/api/v1/items/<thread id>` as is; the thread of 2026-11 was taken in the middle of the month. The Grader checks the runs on this snapshot. Downloading fresh threads is the optional part (1) of the assignment (section 3.2.2) and is yours to write: the address above is all you need, pause between requests. The texts of the posts hold the contacts of their authors: use the data for the course only.

# Contributors

<a href = "https://github.com/big-data-team/ai-course/graphs/contributors">
  <img src = "https://contrib.rocks/image?repo=big-data-team/ai-course"/>
</a>

<!-- made with [contributors-img](https://contrib.rocks) -->
