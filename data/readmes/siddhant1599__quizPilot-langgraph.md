# QuizPilot

AI quiz coach built with Python and LangGraph featuring an orchestrator agent, specialist agents as tools, personalized questions, and resumable sessions.

QuizPilot guides you through a topic using three agent roles powered by one shared language model. When you start a live quiz, you choose a subject, such as Java collections.The coach agent acts as the orchestrator, choosing a suitable focus based on your topic, current difficulty, previous questions, and concepts you have struggled with.

The coach delegates question creation by calling the generate_question tool, which starts the question specialist agent’s workflow. This specialist prepares a question, a reference answer, grading criteria and a hint.

Once you answer, the coach calls the grade_answer tool, which runs the grading specialist. The grader checks your response against the reference answer, grading criteria, and available notes, considering meaning rather than requiring an exact wording match.

At the end, QuizPilot shows your total score, hint usage, and concepts worth reviewing. Sessions are stored in SQLite so you can resume later without regenerating an unanswered question.

This design demonstrates agents as tools i.e specialist agents perform focused tasks, while LangGraph and Python enforce the workflow and maintain consistent quiz state.

## Run demo

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev,openrouter]"
quizpilot --demo
```
```bash
quizpilot --demo --questions 2 --difficulty easy --trace
```

## Quiz commands

| Input | Effect |
| --- | --- |
| Your answer | Ask the grading agent to evaluate it, then move to the next question. |
| `/hint` | Reveal a prepared clue and stay on the same question. |
| `/pause` | Save the session and exit. |
| `/stop` | End the quiz and show a summary of completed answers. |
| `/help` | Show the commands. |

```bash
quizpilot --resume YOUR_SESSION_ID
```

## Agent architecture

```mermaid
flowchart TD
    START([Start]) --> COACH[Coach agent]
    COACH -->|Tool call| TOOLS[Execute phase-appropriate tool]
    TOOLS -->|generate_question| QUESTION[Question specialist]
    TOOLS -->|grade_answer| GRADER[Grading specialist]
    TOOLS -->|give_hint| HINT[Prepared hint]
    QUESTION <-->|read_notes| NOTES[(Optional lesson notes)]
    GRADER <-->|read_notes| NOTES
    QUESTION -->|Question and private rubric| WAIT[Present question and pause]
    HINT --> WAIT
    WAIT -->|Learner reply via interrupt/resume| COACH
    GRADER -->|Record grade and update difficulty| COACH
    COACH -->|Limit reached or stop| SUMMARY[Score and review summary]
    SUMMARY --> END([End])
```

- **Coach:** a tool-calling model that selects the focus for each question and
  delegates the current task. It sees the quiz history and weak concepts.
- **Question specialist:** an isolated LangGraph agent built with LangChain's
  `create_agent`. It checks for notes and returns a validated `Question`.
- **Grading specialist:** another isolated agent with its own prompt. It reads
  any supplied notes and evaluates the actual submitted answer, returning a `Grade`.
- **Ordinary Python:** exposes only tools valid for the current phase, prevents
  grading before an answer, updates totals and difficulty, and enforces the
  question limit. Hint retrieval and the final summary do not need another LLM.

The specialists are wrapped in `@tool` functions. Those wrappers inject the
current lesson, rubric, and learner answer, so the coach cannot replace them
through tool arguments. Each specialist invocation has a fresh conversation.
The outer `StateGraph` owns persistent session state and the tool-call history.

## API Key through OpenRouter

Set **`QUIZPILOT_MODEL` in `.env` once**. The coach, question specialist, and
grading specialist all share that model and its API key. Each agent uses its own prompt and tools. a quiz makes multiple model calls.

```bash
python -m pip install -e ".[openrouter]"
```

```dotenv
QUIZPILOT_MODEL=openrouter:<your-model-id>
OPENROUTER_API_KEY=your-openrouter-api-key
```

Run from the QuizPilot folder so the CLI loads this `.env` file:

```bash
quizpilot --live
```

Enter any subject, or press Enter to accept the suggested topic. You can also
skip the prompt by passing the topic directly; no notes file is required:

```bash
quizpilot --live --topic "Java collections"
```

For topics without lesson notes, the agents use the model's knowledge. Python
basics uses the bundled lesson. To quiz from your own material, add an optional

```bash
quizpilot --live --topic "HTTP fundamentals" --notes ./http_notes.md
```

## References

- [LangGraph interrupts and resume](https://docs.langchain.com/oss/python/langgraph/interrupts)
- [Agents as tools](https://docs.langchain.com/oss/python/langchain/multi-agent/subagents)
- [OpenRouter LangChain integration](https://openrouter.ai/docs/guides/community/langchain)
