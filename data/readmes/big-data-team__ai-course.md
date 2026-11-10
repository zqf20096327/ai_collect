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

# Contributors

<a href = "https://github.com/big-data-team/ai-course/graphs/contributors">
  <img src = "https://contrib.rocks/image?repo=big-data-team/ai-course"/>
</a>

<!-- made with [contributors-img](https://contrib.rocks) -->
