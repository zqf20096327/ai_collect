# ⚖️ OpenEvals

Much like tests in traditional software, evals are an important part of bringing LLM applications to production.
The goal of this package is to help provide a starting point for you to write evals for your LLM applications, from which
you can write more custom evals specific to your application.

If you are looking for evals specific to evaluating LLM agents, please check out [`agentevals`](https://github.com/langchain-ai/agentevals).

# Quickstart

> [!TIP]
> If you'd like to follow along with a video walkthrough, click the image below:
> [![Video quickstart](https://img.youtube.com/vi/J-F30jRyhoA/0.jpg)](https://www.youtube.com/watch?v=J-F30jRyhoA)

To get started, install `openevals`:

<details>
<summary>Python</summary>

```bash
pip install openevals
```
</details>

<details>
<summary>TypeScript</summary>

```bash
npm install openevals @langchain/core
```
</details>

This quickstart will use an evaluator powered by OpenAI's `gpt-5.6-sol` model to judge your results, so you'll need to set your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY="your_openai_api_key"
```

Once you've done this, you can run your first eval:

<details>
<summary>Python</summary>

```python
from openevals.llm import create_llm_as_judge
from openevals.prompts import CONCISENESS_PROMPT

conciseness_evaluator = create_llm_as_judge(
    # CONCISENESS_PROMPT is just an f-string
    prompt=CONCISENESS_PROMPT,
    model="openai:gpt-5.6-sol",
)

inputs = "How is the weather in San Francisco?"
# These are fake outputs, in reality you would run your LLM-based system to get real outputs
outputs = "Thanks for asking! The current weather in San Francisco is sunny and 90 degrees."
# When calling an LLM-as-judge evaluator, parameters are formatted directly into the prompt
eval_result = conciseness_evaluator(
    inputs=inputs,
    outputs=outputs,
)

print(eval_result)
```

```
{
    'key': 'score',
    'score': False,
    'comment': 'The output includes an unnecessary greeting ("Thanks for asking!") and extra..'
}
```
</details>

<details>
<summary>TypeScript</summary>

```ts
import { createLLMAsJudge, CONCISENESS_PROMPT } from "openevals";

const concisenessEvaluator = createLLMAsJudge({
  // CONCISENESS_PROMPT is just an f-string
  prompt: CONCISENESS_PROMPT,
  model: "openai:gpt-5.6-sol",
});

const inputs = "How is the weather in San Francisco?"
// These are fake outputs, in reality you would run your LLM-based system to get real outputs
const outputs = "Thanks for asking! The current weather in San Francisco is sunny and 90 degrees."

// When calling an LLM-as-judge evaluator, parameters are formatted directly into the prompt
const evalResult = await concisenessEvaluator({
  inputs,
  outputs,
});

console.log(evalResult);
```

```
{
    key: 'score',
    score: false,
    comment: 'The output includes an unnecessary greeting ("Thanks for asking!") and extra..'
}
```
</details>

This is an example of a reference-free evaluator - some other evaluators may accept slightly different parameters such as a required reference output. LLM-as-judge evaluators will attempt to format any passed parameters into their passed `prompt`, allowing you to flexibly customize criteria or add other fields.

See the [LLM-as-judge](#llm-as-judge) section for more information on how to customize the [scoring](#customizing-output-score-values) to output float values rather than just `True/False`, the [model](#customizing-the-model), or the [prompt](#customizing-prompts)!

# Table of Contents

- [⚖️ OpenEvals](#️-openevals)
- [Quickstart](#quickstart)
- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Evaluators](#evaluators)
  - <details>
      <summary><a href="#llm-as-judge">LLM-as-Judge</a></summary>

    - [Customizing prompts](#customizing-prompts)
      - [Customizing with LangChain prompt templates](#customizing-with-langchain-prompt-templates)
    - [Customizing the model](#customizing-the-model)
    - [Customizing output score values](#customizing-output-score-values)
    - [Customizing output schema](#customizing-output-schema)
      - [Logging feedback with custom output schemas](#logging-feedback-with-custom-output-schemas)
      - [Structured prompts](#structured-prompts)
    - [Multimodal](#multimodal)
      - [Option 1: `attachments` parameter](#option-1-attachments-parameter)
      - [Option 2: LangChain prompt template](#option-2-langchain-prompt-template)
  </details>

  - <details>
      <summary><a href="#prebuilt-prompts">Prebuilt prompts</a></summary>

    - [Quality](#quality)
    - [Safety](#safety)
    - [Security](#security)
    - [Image](#image)
    - [Voice](#voice)
    - <details>
        <summary><a href="#rag">RAG</a></summary>

      - [Correctness](#correctness-rag)
      - [Helpfulness](#helpfulness)
      - [Groundedness](#groundedness)
      - [Retrieval relevance](#retrieval-relevance)
        - [Retrieval relevance with LLM-as-judge](#retrieval-relevance-with-llm-as-judge)
        - [Retrieval relevance with string evaluators](#retrieval-relevance-with-string-evaluators)

    </details>

  </details>

  - <details>
      <summary><a href="#extraction-and-tool-calls">Extraction and tool calls</a></summary>

    - [Evaluating structured output with exact match](#evaluating-structured-output-with-exact-match)
    - [Evaluating structured output with LLM-as-a-Judge](#evaluating-structured-output-with-llm-as-a-judge)
    - [Nested objects](#nested-objects)

  </details>

  - <details>
      <summary><a href="#code">Code</a></summary>

    - [Extracting code outputs](#extracting-code-outputs)
    - [Pyright (Python-only)](#pyright-python-only)
    - [Mypy (Python-only)](#mypy-python-only)
    - [TypeScript type-checking (TypeScript-only)](#typescript-type-checking-typescript-only)
    - [LLM-as-judge for code](#llm-as-judge-for-code)

  </details>

  - <details>
      <summary><a href="#sandboxed-code">Sandboxed code</a></summary>

    - [Sandbox Pyright (Python-only)](#sandbox-pyright-python-only)
    - [Sandbox TypeScript type-checking (TypeScript-only)](#sandbox-typescript-type-checking-typescript-only)
    - [Sandbox Execution](#sandbox-execution)

  </details>

  - <details>
      <summary><a href="#agent-trajectory">Agent trajectory</a></summary>

    - [Trajectory match](#trajectory-match)
      - [Strict match](#strict-match)
      - [Unordered match](#unordered-match)
      - [Subset and superset match](#subset-and-superset-match)
      - [Tool args match modes](#tool-args-match-modes)
    - [Trajectory LLM-as-judge](#trajectory-llm-as-judge)
    - [Prebuilt trajectory prompts](#prebuilt-trajectory-prompts)

  </details>

  - <details>
      <summary><a href="#other">Other</a></summary>

    - [Exact match](#exact-match)
    - [Levenshtein distance](#levenshtein-distance)
    - [Embedding similarity](#embedding-similarity)

  </details>

  - [Creating your own](#creating-your-own)
    - [Evaluator interface](#evaluator-interface)
    - [Logging to LangSmith](#logging-to-langsmith)
    - [Example](#example)
  - [Python async support](#python-async-support)

- [Multiturn Simulation](#multiturn-simulation)
  - [Simulating users](#simulating-users)
    - [Prebuilt simulated user](#prebuilt-simulated-user)
    - [Custom simulated users](#custom-simulated-users)
  - [Multiturn simulation with LangGraph](#multiturn-simulation-with-langgraph)

- [LangSmith Integration](#langsmith-integration)
  - [Pytest or Vitest/Jest](#pytest-or-vitestjest)
  - [Evaluate](#evaluate)

- [Acknowledgements](#acknowledgements)
- [Thank you!](#thank-you)

# Installation

You can install `openevals` like this:

<details>
<summary>Python</summary>

```bash
pip install openevals
```
</details>

<details>
<summary>TypeScript</summary>

```bash
npm install openevals @langchain/core
```
</details>

For LLM-as-judge evaluators, you will also need an LLM client. By default, `openevals` will use [LangChain chat model integrations](https://python.langchain.com/docs/integrations/chat/) and comes with `langchain_openai` installed by default. However, if you prefer, you may use the OpenAI client directly:

<details>
<summary>Python</summary>

```bash
pip install openai
```
</details>

<details>
<summary>TypeScript</summary>

```bash
npm install openai
```
</details>

It is also helpful to be familiar with some [evaluation concepts](https://docs.langchain.com/langsmith/evaluation-concepts).

# Evaluators

## LLM-as-judge

One common way to evaluate an LLM app's outputs is to use another LLM as a judge. This is generally a good starting point for evals.

This package contains the `create_llm_as_judge` function, which takes a prompt and a model as input, and returns an evaluator function
that handles converting parameters into strings and parsing the judge LLM's outputs as a score.

To use the `create_llm_as_judge` function, you need to provide a prompt and a model. To get started, OpenEvals has some prebuilt prompts in the `openevals.prompts` module that you can use out of the box. Here's an example:

<details>
<summary>Python</summary>

```python
from openevals.llm import create_llm_as_judge
from openevals.prompts import CORRECTNESS_PROMPT

correctness_evaluator = create_llm_as_judge(
    prompt=CORRECTNESS_PROMPT,
    model="openai:gpt-5.6-sol",
)
```
</details>

<details>
<summary>TypeScript</summary>

```ts
import { createLLMAsJudge, CORRECTNESS_PROMPT } from "openevals";

const correctnessEvaluator = createLLMAsJudge({
  prompt: CORRECTNESS_PROMPT,
  model: "openai:gpt-5.6-sol",
});
```

</details>

Note that `CORRECTNESS_PROMPT` is a simple f-string that you can log and edit as needed for your specific use case:

<details>
<summary>Python</summary>

```python
print(CORRECTNESS_PROMPT)
```

```
You are an expert data labeler evaluating model outputs for correctness. Your task is to assign a score based on the following rubric:

<Rubric>
  A correct answer:
  - Provides accurate and complete information
  ...
<input>
{inputs}
</input>

<output>
{outputs}
</output>
...
```
</details>

<details>
<summary>TypeScript</summary>

```ts
console.log(CORRECTNESS_PROMPT);
```

```
You are an expert data labeler evaluating model outputs for correctness. Your task is to assign a score based on the following rubric:

<Rubric>
  A correct answer:
  - Provides accurate and complete information
  ...
<input>
{inputs}
</input>

<output>
{outputs}
</output>
...
```

</details>

By convention, we generally suggest sticking to `inputs`, `outputs`, and `reference_outputs` as the names of the parameters for LLM-as-judge evaluators, but these will be directly formatted into the prompt so you can use any variable names you want.

OpenEvals includes many prebuilt prompts for common evaluation scenarios. See the [Prebuilt prompts](#prebuilt-prompts) section for a full list organized by category.

### Customizing prompts

The `prompt` parameter for `create_llm_as_judge` may be an f-string, [LangChain prompt template](#customizing-with-langchain-prompt-templates), or a function that takes kwargs and returns a list of formatted messages.

Though we suggest sticking to conventional names (`inputs`, `outputs`, and `reference_outputs`) as prompt variables, your prompts can also require additional variables. You would then pass these extra variables when calling your evaluator function. Here's an example of a prompt that requires an extra variable named `context`:

<details>
<summary>Python</summary>

```python
from openevals.llm import create_llm_as_judge

MY_CUSTOM_PROMPT = """
Use the following context to help you evaluate for hallucinations in the output:

<context>
{context}
</context>

<input>
{inputs}
</input>

<output>
{outputs}
</output>
"""

custom_prompt_evaluator = create_llm_as_judge(
    prompt=MY_CUSTOM_PROMPT,
    model="openai:gpt-5.6-sol",
)

custom_prompt_evaluator(
    inputs="What color is the sky?",
    outputs="The sky is red.",
    context="It is early evening.",
)
```

</details>

<details>
<summary>TypeScript</summary>

```ts
import { createLLMAsJudge } from "openevals";

const MY_CUSTOM_PROMPT = `
Use the following context to help you evaluate for hallucinations in the output:

<context>
{context}
</context>

<input>
{inputs}
</input>

<output>
{outputs}
</output>
`;

const customPromptEvaluator = createLLMAsJudge({
  prompt: MY_CUSTOM_PROMPT,
  model: "openai:gpt-5.6-sol",
});

const inputs = "What color is the sky?"
const outputs = "The sky is red."

const evalResult = await customPromptEvaluator({
  inputs,
  outputs,
});
```
</details>

The following options are also available for string prompts:

- `system`: a string that sets a system prompt for the judge model by adding a `system` message before other parts of the prompt.
- `few_shot_examples`: a list of example dicts that are appended to the end of the prompt. This is useful for providing the judge model with examples of good and bad outputs. The required structure looks like this:

<details>
<summary>Python</summary>

```python
few_shot_examples = [
    {
        "inputs": "What color is the sky?",
        "outputs": "The sky is red.",
        "reasoning": "The sky is red because it is early evening.",
        "score": 1,
    }
]
```

</details>

<details>
<summary>TypeScript</summary>

```ts
const fewShotExamples = [
    {
        inputs: "What color is the sky?",
        outputs: "The sky is red.",
        reasoning: "The sky is red because it is early evening.",
        score: 1,
    }
]
```
</details>

These will be appended to the end of the final user message in the prompt.

#### Customizing with LangChain prompt templates

You can also pass a [LangChain prompt template](https://python.langchain.com/docs/concepts/prompt_templates/) if you want more control over formatting. Here's an example that uses mustache formatting instead of f-strings:

<details>
<summary>Python</summary>

```python
from openevals.llm import create_llm_as_judge
from langchain_core.prompts.chat import ChatPromptTemplate

inputs = {"a": 1, "b": 2}
outputs = {"a": 1, "b": 2}

prompt = ChatPromptTemplate([
    ("system", "You are an expert at determining if two objects are equal."),
    ("human", "Are these two equal? {{inputs}} {{outputs}}"),
], template_format="mustache")

llm_as_judge = create_llm_as_judge(
    prompt=prompt,
    model="openai:gpt-5.6-sol",
    feedback_key="equality",
)

eval_result = llm_as_judge(inputs=inputs, outputs=outputs)

print(eval_result)
```

```
{
    key: 'equality',
    score: True,
    comment: '...'
}
```

</details>

<details>
<summary>TypeScript</summary>

```ts
import { createLLMAsJudge } from "openevals";
import { ChatPromptTemplate } from "@langchain/core/prompts";

const inputs = { a: 1, b: 2 };
const outputs = { a: 1, b: 2 };

const prompt = ChatPromptTemplate.fromMessages([
  ["system", "You are an expert at determining if two objects are equal."],
  ["user", "Are these two equal? {{inputs}} {{outputs}}"],
], { templateFormat: "mustache" });

const evaluator = createLLMAsJudge({
  prompt,
  model: "openai:gpt-5.6-sol",
  feedbackKey: "equality",
});

const result = await evaluator({ inputs, outputs });
```

```
{
    key: 'equality',
    score: true,
    comment: '...'
}
```

</details>

You can also pass in a function that takes your LLM-as-judge inputs as kwargs and returns formatted chat messages.

### Customizing the model

There are a few ways you can customize the model used for evaluation. You can pass a string formatted as `PROVIDER:MODEL` (e.g. `model=anthropic:claude-3-5-sonnet-latest`) as the `model`, in which case the package will [attempt to import and initialize a LangChain chat model instance](https://python.langchain.com/docs/how_to/chat_models_universal_init/). This requires you to install the appropriate LangChain integration package installed. Here's an example:

<details>
<summary>Python</summary>

```bash
pip install langchain-anthropic
```

```python
from openevals.llm import create_llm_as_judge
from openevals.prompts import CORRECTNESS_PROMPT

anthropic_evaluator = create_llm_as_judge(
    prompt=CORRECTNESS_PROMPT,
    model="anthropic:claude-3-5-sonnet-latest",
)
```

</details>

<details>
<summary>TypeScript</summary>

```bash
npm install @langchain/anthropic
```

```ts
import { createLLMAsJudge, CORRECTNESS_PROMPT } from "openevals";

const anthropicEvaluator = createLLMAsJudge({
  prompt: CORRECTNESS_PROMPT,
  model: "anthropic:claude-3-5-sonnet-latest",
});
```
</details>

You can also directly pass a LangChain chat model instance as `judge`. Note that your chosen model must support [structured output](https://python.langchain.com/docs/integrations/chat/):

<details>
<summary>Python</summary>

```python
from openevals.llm import create_llm_as_judge
from openevals.prompts import CORRECTNESS_PROMPT
from langchain_anthropic import ChatAnthropic

anthropic_evaluator = create_llm_as_judge(
    prompt=CORRECTNESS_PROMPT,
    judge=ChatAnthropic(model="claude-3-5-sonnet-latest", temperature=0.5),
)
```

</details>

<details>
<summary>TypeScript</summary>

```ts
import { createLLMAsJudge, CORRECTNESS_PROMPT } from "openevals";
import { ChatAnthropic } from "@langchain/anthropic";

const anthropicEvaluator = createLLMAsJudge({
  prompt: CORRECTNESS_PROMPT,
  judge: new ChatAnthropic({ model: "claude-3-5-sonnet-latest", temperature: 0.5 }),
});
```
</details>

This is useful in scenarios where you need to initialize your model with specific parameters, such as `temperature` or alternate URLs if using models through a service like Azure.

Finally, you can pass a model name as `model` and a `judge` parameter set to an OpenAI client instance:

<details>
<summary>Python</summary>

```bash
pip install openai
```

```python
from openai import OpenAI

from openevals.llm import create_llm_as_judge
from openevals.prompts import CORRECTNESS_PROMPT

openai_evaluator = create_llm_as_judge(
    prompt=CORRECTNESS_PROMPT,
    model="gpt-5.6-sol",
    judge=OpenAI(),
)
```

</details>

<details>
<summary>TypeScript</summary>

```bash
npm install openai
```

```ts
import { OpenAI } from "openai";
import { createLLMAsJudge, CORRECTNESS_PROMPT } from "openevals";

const openaiEvaluator = createLLMAsJudge({
  prompt: CORRECTNESS_PROMPT,
  model: "gpt-5.6-sol",
  judge: new OpenAI(),
});
```
</details>

### Customizing output score values

There are two fields you can set to customize the outputted scores of your evaluator:

- `continuous`: a boolean that sets whether the evaluator should return a float score somewhere between 0 and 1 instead of a binary score. Defaults to `False`.
- `choices`: a list of floats that sets the possible scores for the evaluator.

These parameters are mutually exclusive. When using either of them, you should make sure that your prompt is grounded in information on what specific scores mean - the prebuilt ones in this repo do not have this information!

For example, here's an example of how to define a less harsh definition of correctness that only penalizes incorrect answers by 50% if they are on-topic:

<details>
<summary>Python</summary>

```python
from openevals.llm import create_llm_as_judge

MY_CUSTOM_PROMPT = """
You are an expert data labeler evaluating model outputs for correctness. Your task is to assign a score based on the following rubric:

<Rubric>
  Assign a score of 0, .5, or 1 based on the following criteria:
  - 0: The answer is incorrect and does not mention doodads
  - 0.5: The answer mentions doodads but is otherwise incorrect
  - 1: The answer is correct and mentions doodads
</Rubric>

<input>
{inputs}
</input>

<output>
{outputs}
</output>

<reference_outputs>
{reference_outputs}
</reference_outputs>
"""

evaluator = create_llm_as_judge(
    prompt=MY_CUSTOM_PROMPT,
    choices=[0.0, 0.5, 1.0],
    model="openai:gpt-5.6-sol",
)

result = evaluator(
    inputs="What is the current price of doodads?",
    outputs="The price of doodads is $10.",
    reference_outputs="The price of doodads is $15.",
)

print(result)
```

```
{
    'key': 'score',
    'score': 0.5,
    'comment': 'The provided answer mentioned doodads but was incorrect.'
}
```

</details>

<details>
<summary>TypeScript</summary>

```ts
import { createLLMAsJudge } from "openevals";

const MY_CUSTOM_PROMPT = `
You are an expert data labeler evaluating model outputs for correctness. Your task is to assign a score based on the following rubric:

<Rubric>
  Assign a score of 0, .5, or 1 based on the following criteria:
  - 0: The answer is incorrect and does not mention doodads
  - 0.5: The answer mentions doodads but is otherwise incorrect
  - 1: The answer is correct and mentions doodads
</Rubric>

<input>
{inputs}
</input>

<output>
{outputs}
</output>

<reference_outputs>
{reference_outputs}
</reference_outputs>
`;

const customEvaluator = createLLMAsJudge({
  prompt: MY_CUSTOM_PROMPT,
  choices: [0.0, 0.5, 1.0],
  model: "openai:gpt-5.6-sol",
});

const result = await customEvaluator({
  inputs: "What is the current price of doodads?",
  outputs: "The price of doodads is $10.",
  reference_outputs: "The price of doodads is $15.",
});

console.log(result);
```

```
{
    'key': 'score',
    'score': 0.5,
    'comment': 'The provided answer mentioned doodads but was incorrect.'
}
```
</details>

Finally, if you would like to disable justifications for a given score, you can set `use_reasoning=False` when creating your evaluator.

### Customizing output schema

If you need to change the structure of the raw output generated by the LLM, you can also pass a custom output schema into your LLM-as-judge evaluator as `output_schema` (Python) / `outputSchema` (TypeScript). This may be helpful for specific prompting strategies or if you would like to extract multiple metrics at the same time rather than over multiple calls.

> [!CAUTION]
> Passing `output_schema` changes the return value of the evaluator to match the passed `output_schema` value instead of the typical OpenEvals format.
> We recommend sticking with the default schema if you do not specifically need additional properties.

For Python, `output_schema` may be:

- A `TypedDict` instance
- A [Pydantic](https://docs.pydantic.dev) model
- [JSON schema](https://json-schema.org/)
- [OpenAI's structured output format](https://platform.openai.com/docs/guides/structured-outputs?api-mode=chat#supported-schemas)

For TypeScript, `outputSchema` may be:

- A [Zod](https://zod.dev) object
- [JSON schema](https://json-schema.org/)
- [OpenAI's structured output format](https://platform.openai.com/docs/guides/structured-outputs?api-mode=chat#supported-schemas)

Note that if you are using an OpenAI client directly, only JSON schema and OpenAI's structured output format.

Here's an example:

<details>
<summary>Python</summary>

```python
from typing_extensions import TypedDict

from openevals.llm import create_llm_as_judge

class EqualityResult(TypedDict):
    equality_justification: str
    are_equal: bool

inputs = "The rain in Spain falls mainly on the plain."

outputs = "The rain in Spain falls mainly on the plain."

llm_as_judge = create_llm_as_judge(
    prompt="Are the following two values equal? {inputs} {outputs}",
    model="openai:gpt-5.6-sol",
    output_schema=EqualityResult,
)
eval_result = llm_as_judge(inputs=inputs, outputs=outputs)

print(eval_result)
```

```
{
    'equality_justification': 'The values are equal because they have the same properties with identical values.',
    'are_equal': True,
}
```

</details>

<details>
<summary>TypeScript</summary>

```ts
import { z } from "zod";

import { createLLMAsJudge } from "openevals";

const equalitySchema = z.object({
  equality_justification: z.string(),
  are_equal: z.boolean(),
})

const inputs = "The rain in Spain falls mainly on the plain.";
const outputs = "The rain in Spain falls mainly on the plain.";

const llmAsJudge = createLLMAsJudge({
  prompt: "Are the following two values equal? {inputs} {outputs}",
  model: "openai:gpt-5.6-sol",
  outputSchema: equalitySchema,
});

const evalResult = await llmAsJudge({ inputs, outputs });

console.log(evalResult);
```

```
{
    'equality_justification': 'The values are equal because they have the same properties with identical values.',
    'are_equal': True,
}
```

</details>

#### Logging feedback with custom output schemas

If you are using an OpenEvals evaluator with [LangSmith's `pytest` or `Vitest`/`Jest` runners](#pytest-or-vitestjest), you will need to manually [log feedback keys](https://docs.langchain.com/langsmith/pytest#log-feedback).

If you are using `evaluate`, you will need to wrap your evaluator in another function that maps your evaluator return value to [feedback in the right format](https://docs.langchain.com/langsmith/code-evaluator).

#### Structured prompts

Passing in a pulled prompt from the [LangChain prompt hub](https://smith.langchain.com/hub) that has an output schema set will also change the output schema for the LLM-as-judge evaluator.

### Multimodal

LLM-as-judge evaluators support multimodal inputs including images, audio, and PDFs. There are two ways to pass multimodal content:

- **`attachments` parameter** — include an `{attachments}` placeholder in your prompt and pass the content via the `attachments` kwarg.
- **LangChain prompt template** — introduce multimodal content directly into the prompt message. See the [LangChain multimodal messages docs](https://docs.langchain.com/oss/python/langchain/messages#multimodal) for details.

#### Option 1: `attachments` parameter

The `attachments` parameter supports a single dict or a list of dicts with a `mime_type` and base64-encoded `data` field. The prebuilt [Image](#image) and [Voice](#voice) prompts already include the `{attachments}` placeholder, or you can add it to any custom prompt.

Supported attachment types:

| Type | `mime_type` |
|------|-------------|
| Images | `image/png`, `image/jpeg`, `image/gif`, `image/webp` |
| Audio | `audio/wav`, `audio/mp3`, `audio/mpeg` |
| PDF | `application/pdf` |

> [!NOTE]
> Multimodal support depends on your model provider. Audio input and structured output (e.g. returning a score with a comment) are not supported simultaneously by all providers — currently only Gemini supports both at once. The prebuilt [Voice](#voice) prompts use `google_genai:gemini-2.0-flash` (Python) / `google-genai:gemini-2.0-flash` (TypeScript) for this reason.

Passing a URL string directly as `attachments` is supported for images only. Audio and PDF attachments must be passed as a base64-encoded data URI with `mime_type` and `data` fields.

Here's an example using the prebuilt `SENSITIVE_IMAGERY_PROMPT`. You can pass an image as a URL or as a base64-encoded data URI — both work the same way:

<details>
<summary>Python</summary>

```python
import base64
from openevals.llm import create_llm_as_judge
from openevals.prompts import SENSITIVE_IMAGERY_PROMPT

evaluator = create_llm_as_judge(
    prompt=SENSITIVE_IMAGERY_PROMPT,
    feedback_key="sensitive_imagery",
    model="openai:gpt-5.6-sol",
)

# Option A: pass a URL string directly
eval_result = evaluator(
    inputs="Review this image for sensitive content",
    outputs="The image appears to contain appropriate content",
    attachments="https://example.com/image.jpg",
)

# Option B: pass a base64-encoded data URI
with open("image.jpg", "rb") as f:
    image_data = "data:image/jpeg;base64," + base64.b64encode(f.read()).decode("utf-8")

eval_result = evaluator(
    inputs="Review this image for sensitive content",
    outputs="The image appears to contain appropriate content",
    attachments={"mime_type": "image/jpeg", "data": image_data},
)

print(eval_result)
```

```
{
    'key': 'sensitive_imagery',
    'score': False,
    'comment': '...'
}
```
</details>

<details>
<summary>TypeScript</summary>

```ts
import * as fs from "fs";
import { createLLMAsJudge, SENSITIVE_IMAGERY_PROMPT } from "openevals";

const evaluator = createLLMAsJudge({
  prompt: SENSITIVE_IMAGERY_PROMPT,
  feedbackKey: "sensitive_imagery",
  model: "openai:gpt-5.6-sol",
});

// Option A: pass a URL string directly
const evalResult = await evaluator({
  inputs: "Review this image for sensitive content",
  outputs: "The image appears to contain appropriate content",
  attachments: "https://example.com/image.jpg",
});

// Option B: pass a base64-encoded data URI
const imageData = "data:image/jpeg;base64," + fs.readFileSync("image.jpg").toString("base64");

const evalResultB64 = await evaluator({
  inputs: "Review this image for sensitive content",
  outputs: "The image appears to contain appropriate content",
  attachments: { mime_type: "image/jpeg", data: imageData },
});

console.log(evalResult);
```

```
{
    key: 'sensitive_imagery',
    score: false,
    comment: '...'
}
```
</details>

#### Option 2: LangChain prompt template

You can also introduce multimodal content into the prompt using a LangChain prompt template. See the [LangChain multimodal messages docs](https://docs.langchain.com/oss/python/langchain/messages#multimodal) for details.

## Prebuilt prompts

OpenEvals includes prebuilt prompts for common evaluation scenarios that work out of the box with [`create_llm_as_judge`](#llm-as-judge). All prebuilt prompts are importable from `openevals.prompts` (Python) or `openevals` (TypeScript).

### Quality

These prompts evaluate general output quality.

| Prompt | Parameters | What it evaluates |
|--------|-----------|-------------------|
| `CONCISENESS_PROMPT` | `inputs`, `outputs` | Whether the output is appropriately brief and avoids unnecessary padding |
| `CORRECTNESS_PROMPT` | `inputs`, `outputs`, `reference_outputs` (optional) | Factual accuracy and completeness of the output |
| `HALLUCINATION_PROMPT` | `inputs`, `outputs`, `context` (optional) | Whether the output contains information not supported by the provided context |
| `ANSWER_RELEVANCE_PROMPT` | `inputs`, `outputs` | Whether the output directly addresses the question asked |
| `PLAN_ADHERENCE_PROMPT` | `inputs`, `outputs`, `plan` | Whether the output follows a provided plan |
| `CODE_CORRECTNESS_PROMPT` | `inputs`, `outputs` | Code correctness against the problem specification |
| `CODE_CORRECTNESS_PROMPT_WITH_REFERENCE_OUTPUTS` | `inputs`, `outputs`, `reference_outputs` | Code correctness compared to a reference solution |
| `LAZINESS_PROMPT` | `inputs`, `outputs` | Whether the agent returned a blank, empty, or low-effort response |

Here's an example using `CORRECTNESS_PROMPT`:

<details>
<summary>Python</summary>

```python
from openevals.llm import create_llm_as_judge
from openevals.prompts import CORRECTNESS_PROMPT

correctness_evaluator = create_llm_as_judge(
    prompt=CORRECTNESS_PROMPT,
    feedback_key="correctness",
    model="openai:gpt-5.6-sol",
)

inputs = "How much has the price of doodads changed in the past year?"
outputs = "Doodads have increased in price by 10% in the past year."
reference_outputs = "The price of doodads has decreased by 50% in the past year."

eval_result = correctness_evaluator(
  inputs=inputs,
  outputs=outputs,
  reference_outputs=reference_outputs
)

print(eval_result)
```

```
{
    'key': 'correctness',
    'score': False,
    'comment': '...'
}
```
</details>

<details>
<summary>TypeScript</summary>

```ts
import { createLLMAsJudge, CORRECTNESS_PROMPT } from "openevals";

const correctnessEvaluator = createLLMAsJudge({
  prompt: CORRECTNESS_PROMPT,
  feedbackKey: "correctness",
  model: "openai:gpt-5.6-sol",
});

const inputs = "How much has the price of doodads changed in the past year?";
const outputs = "Doodads have increased in price by 10% in the past year.";
const referenceOutputs = "The price of doodads has decreased by 50% in the past year.";

const evalResult = await correctnessEvaluator({
  inputs,
  outputs,
  referenceOutputs,
});

console.log(evalResult);
```

```
{
    key: 'correctness',
    score: false,
    comment: '...'
}
```
</details>

### Safety

These prompts detect harmful or biased content in LLM outputs.

| Prompt | Parameters | What it evaluates |
|--------|-----------|-------------------|
| `TOXICITY_PROMPT` | `inputs`, `outputs` | Harmful, offensive, or abusive language |
| `FAIRNESS_PROMPT` | `inputs`, `outputs` | Bias or discrimination toward individuals or groups based on protected characteristics |

Here's an example using `FAIRNESS_PROMPT`:

<details>
<summary>Python</summary>

```python
from openevals.llm import create_llm_as_judge
from openevals.prompts import FAIRNESS_PROMPT

llm_as_judge = create_llm_as_judge(
    prompt=FAIRNESS_PROMPT,
    feedback_key="fairness",
    model="openai:gpt-5.6-sol",
)

eval_result = llm_as_judge(
    inputs="Should we hire this candidate?",
    outputs="Their name is hard to pronounce — that could make clients uncomfortable.",
)

print(eval_result)
```

```
{
    'key': 'fairness',
    'score': True,
    'comment': '...'
}
```
</details>

<details>
<summary>TypeScript</summary>

```ts
import { createLLMAsJudge, FAIRNESS_PROMPT } from "openevals";

const fairnessEvaluator = createLLMAsJudge({
  prompt: FAIRNESS_PROMPT,
  feedbackKey: "fairness",
  model: "openai:gpt-5.6-sol",
});

const evalResult = await fairnessEvaluator({
  inputs: "Should we hire this candidate?",
  outputs: "Their name is hard to pronounce — that could make clients uncomfortable.",
});

console.log(evalResult);
```

```
{
    key: 'fairness',
    score: true,
    comment: '...'
}
```
</details>

### Security

These prompts detect security threats in LLM inputs and outputs.

| Prompt | Parameters | What it evaluates |
|--------|-----------|-------------------|
| `PII_LEAKAGE_PROMPT` | `inputs`, `outputs` | Personally identifiable information exposed in the output |
| `PROMPT_INJECTION_PROMPT` | `inputs` | Attempts to manipulate or override AI system instructions, including social engineering and roleplay-based circumvention |
| `CODE_INJECTION_PROMPT` | `inputs` | Malicious code or exploits embedded in inputs |

Here's an example using `PII_LEAKAGE_PROMPT`:

<details>
<summary>Python</summary>

```python
from openevals.llm import create_llm_as_judge
from openevals.prompts import PII_LEAKAGE_PROMPT

llm_as_judge = create_llm_as_judge(
    prompt=PII_LEAKAGE_PROMPT,
    feedback_key="pii_leakage",
    model="openai:gpt-5.6-sol",
)

eval_result = llm_as_judge(
    inputs="What is my account info?",
    outputs="Your name is John Smith, your email is john.smith@example.com, and your SSN is 123-45-6789.",
)

print(eval_result)
```

```
{
    'key': 'pii_leakage',
    'score': True,
    'comment': '...'
}
```
</details>

<details>
<summary>TypeScript</summary>

```ts
import { createLLMAsJudge, PII_LEAKAGE_PROMPT } from "openevals";

const piiEvaluator = createLLMAsJudge({
  prompt: PII_LEAKAGE_PROMPT,
  feedbackKey: "pii_leakage",
  model: "openai:gpt-5.6-sol",
});

const evalResult = await piiEvaluator({
  inputs: "What is my account info?",
  outputs: "Your name is John Smith, your email is john.smith@example.com, and your SSN is 123-45-6789.",
});

console.log(evalResult);
```

```
{
    key: 'pii_leakage',
    score: true,
    comment: '...'
}
```
</details>

### Image

These prompts evaluate image content and its relation to the associated context. All image prompts require an `attachments` parameter — see the [Multimodal](#multimodal) section for details on passing image data. Note that your chosen model must support vision inputs (e.g. `openai:gpt-5.6-sol`).

| Prompt | Parameters | What it evaluates |
|--------|-----------|-------------------|
| `EXPLICIT_CONTENT_PROMPT` | `inputs`, `outputs`, `attachments` | Sexually explicit or graphic material inappropriate for general audiences |
| `SENSITIVE_IMAGERY_PROMPT` | `inputs`, `outputs`, `attachments` | Hate symbols, inflammatory political imagery, or depictions of suffering |

### Voice

These prompts evaluate voice and audio content. All voice prompts require an `attachments` parameter — see the [Multimodal](#multimodal) section for details on passing audio data. Note that your chosen model must support audio inputs — as mentioned in the [Multimodal](#multimodal) section, only Gemini currently supports audio and structured output simultaneously.

| Prompt | Parameters | What it evaluates |
|--------|-----------|-------------------|
| `AUDIO_QUALITY_PROMPT` | `inputs`, `outputs`, `attachments` | Clipping, distortion, or glitches that degrade listening experience |
| `TRANSCRIPTION_ACCURACY_PROMPT` | `inputs`, `outputs`, `attachments` | Accuracy of speech-to-text transcription |
| `USER_INTERRUPTS_PROMPT` | `inputs`, `outputs`, `attachments` | Whether the agent handled user interruptions gracefully |
| `VOCAL_AFFECT_PROMPT` | `inputs`, `outputs`, `attachments` | Appropriateness and consistency of the agent's vocal tone |

Here's an example using `AUDIO_QUALITY_PROMPT`:

<details>
<summary>Python</summary>

```python
import base64
from openevals.llm import create_llm_as_judge
from openevals.prompts import AUDIO_QUALITY_PROMPT

with open("audio.wav", "rb") as f:
    audio_data = base64.b64encode(f.read()).decode("utf-8")

llm_as_judge = create_llm_as_judge(
    prompt=AUDIO_QUALITY_PROMPT,
    feedback_key="audio_quality",
    model="google_genai:gemini-2.0-flash",
)

eval_result = llm_as_judge(
    inputs="Customer service call recording",
    outputs="Audio response from agent",
    attachments={"mime_type": "audio/wav", "data": audio_data},
)

print(eval_result)
```

```
{
    'key': 'audio_quality',
    'score': True,
    'comment': '...'
}
```
</details>

<details>
<summary>TypeScript</summary>

```ts
import * as fs from "fs";
import { createLLMAsJudge } from "openevals";
import { AUDIO_QUALITY_PROMPT } from "openevals/prompts";

const audioData = fs.readFileSync("audio.wav").toString("base64");

const llmAsJudge = createLLMAsJudge({
  prompt: AUDIO_QUALITY_PROMPT,
  feedbackKey: "audio_quality",
  model: "google-genai:gemini-2.0-flash",
});

const evalResult = await llmAsJudge({
  inputs: "Customer service call recording",
  outputs: "Audio response from agent",
  attachments: { mime_type: "audio/wav", data: audioData },
});

console.log(evalResult);
```

```
{
    key: 'audio_quality',
    score: true,
    comment: '...'
}
```
</details>

### RAG

RAG applications in their most basic form consist of 2 steps. In the retrieval step, context is retrieved (often from something like a vector database that a user has prepared ahead of time, though [web retrieval](https://github.com/assafelovic/gpt-researcher) use-cases are gaining in popularity as well) to provide the LLM with the information it needs to respond to the user. In the generation step, the LLM uses the retrieved context to formulate an answer.

OpenEvals provides prebuilt prompts and other methods for the following:

1. [Correctness](#correctness-rag)
- Evaluates: Final output vs. input + reference answer
- Goal: Measure "how similar/correct is the generated answer relative to a ground-truth answer"
- Requires reference: Yes

2. [Helpfulness](#helpfulness)
- Evaluates: Final output vs. input
- Goal: Measure "how well does the generated response address the initial user input"
- Requires reference: No, because it will compare the answer to the input question

3. [Groundedness](#groundedness)
- Evaluates: Final output vs. retrieved context
- Goal: Measure "to what extent does the generated response agree with the retrieved context"
- Requires reference: No, because it will compare the answer to the retrieved context

4. [Retrieval relevance](#retrieval-relevance)
- Evaluates: Retrieved context vs. input
- Goal: Measure "how relevant are my retrieved results for this query"
- Requires reference: No, because it will compare the question to the retrieved context

#### Correctness {#correctness-rag}

`correctness` measures how similar/correct a generated answer is to a ground-truth answer. By definition, this requires you to have a reference output to compare against the generated one. It is useful to test your RAG app end-to-end, and does directly take into account context retrieved as an intermediate step.

You can evaluate the correctness of a RAG app's outputs using the LLM-as-judge evaluator alongside the general [`CORRECTNESS_PROMPT`](#quality) covered in the [Quality](#quality) section above. Here's an example:

<details>
<summary>Python</summary>

```python
from openevals.llm import create_llm_as_judge
from openevals.prompts import CORRECTNESS_PROMPT

correctness_evaluator = create_llm_as_judge(
    prompt=CORRECTNESS_PROMPT,
    feedback_key="correctness",
    model="openai:gpt-5.6-sol",
)

inputs = "How much has the price of doodads changed in the past year?"
outputs = "Doodads have increased in price by 10% in the past year."
reference_outputs = "The price of doodads has decreased by 50% in the past year."

eval_result = correctness_evaluator(
  inputs=inputs,
  outputs=outputs,
  reference_outputs=reference_outputs
)

print(eval_result)
```

```
{
    'key': 'correctness',
    'score': False,
    'comment': '...'
}
```
</details>

<details>
<summary>TypeScript</summary>

```ts
import { createLLMAsJudge, CORRECTNESS_PROMPT } from "openevals";

const correctnessEvaluator = createLLMAsJudge({
  prompt: CORRECTNESS_PROMPT,
  feedbackKey: "correctness",
  model: "openai:gpt-5.6-sol",
});

const inputs = "How much has the price of doodads changed in the past year?";
const outputs = "Doodads have increased in price by 10% in the past year.";
const referenceOutputs = "The price of doodads has decreased by 50% in the past year.";

const evalResult = await correctnessEvaluator({
  inputs,
  outputs,
  referenceOutputs,
});

console.log(evalResult);
```

```
{
    key: 'correctness',
    score: false,
    comment: '...'
}
```
</details>

For more information on customizing LLM-as-judge evaluators, see [these sections](#customizing-prompts).

#### Helpfulness

`helpfulness` measures how well the generated response addresses the initial user input. It compares the final generated output against the input, and does not require a reference. It's useful to validate that the generation step of your RAG app actually answers the original question as stated, but does *not* measure that the answer is supported by any retrieved context!

You can evaluate the helpfulness of a RAG app's outputs using the LLM-as-judge evaluator with a prompt like the built-in `RAG_HELPFULNESS_PROMPT`. Here's an example:

<details>
<summary>Python</summary>

```python
from openevals.llm import create_llm_as_judge
from openevals.prompts import RAG_HELPFULNESS_PROMPT

helpfulness_evaluator = create_llm_as_judge(
    prompt=RAG_HELPFULNESS_PROMPT,
    feedback_key="helpfulness",
    model="openai:gpt-5.6-sol",
)

inputs = {
    "question": "Where was the first president of FoobarLand born?",
}

outputs = {
    "answer": "The first president of FoobarLand was Bagatur Askaryan.",
}

eval_result = helpfulness_evaluator(
  inputs=inputs,
  outputs=outputs,
)

print(eval_result)
```

```
{
  'key': 'helpfulness',
  'score': False,
  'comment': "The question asks for the birthplace of the first president of FoobarLand, but the retrieved outputs only identify the first president as Bagatur and provide an unrelated biographical detail (being a fan of PR reviews). Although the first output is somewhat relevant by identifying the president's name, neither document provides any information about his birthplace. Thus, the outputs do not contain useful information to answer the input question. Thus, the score should be: false."
}
```

</details>

<details>
<summary>TypeScript</summary>

```ts
import { createLLMAsJudge, RAG_HELPFULNESS_PROMPT } from "openevals";

const inputs = {
  "question": "Where was the first president of FoobarLand born?",
};

const outputs = {
  "answer": "The first president of FoobarLand was Bagatur Askaryan.",
};

const helpfulnessEvaluator = createLLMAsJudge({
  prompt: RAG_HELPFULNESS_PROMPT,
  feedbackKey: "helpfulness",
  model: "openai:gpt-5.6-sol",
});

const evalResult = await helpfulnessEvaluator({
  inputs,
  outputs,
});

console.log(evalResult);
```

```
{
  'key': 'helpfulness',
  'score': False,
  'comment': "The question asks for the birthplace of the first president of FoobarLand, but the retrieved outputs only identify the first president as Bagatur and provide an unrelated biographical detail (being a fan of PR reviews). Although the first output is somewhat relevant by identifying the president's name, neither document provides any information about his birthplace. Thus, the outputs do not contain useful information to answer the input question. Thus, the score should be: false."
}
```

</details>

#### Groundedness

`groundedness` measures the extent that the generated response agrees with the retrieved context. It compares the final generated output against context fetched during the retrieval step, and verifies that the generation step is properly using retrieved context vs. hallucinating a response or overusing facts from the LLM's base knowledge.

You can evaluate the groundedness of a RAG app's outputs using the LLM-as-judge evaluator with a prompt like the built-in `RAG_GROUNDEDNESS_PROMPT`. Note that this prompt does not take the example's original `inputs` into account, only the outputs and their relation to the retrieved context. Thus, unlike some of the other prebuilt prompts, it takes `context` and `outputs` as prompt variables:

<details>
<summary>Python</summary>

```python
from openevals.llm import create_llm_as_judge
from openevals.prompts import RAG_GROUNDEDNESS_PROMPT

groundedness_evaluator = create_llm_as_judge(
    prompt=RAG_GROUNDEDNESS_PROMPT,
    feedback_key="groundedness",
    model="openai:gpt-5.6-sol",
)

context = {
    "documents": [
        "FoobarLand is a new country located on the dark side of the moon",
        "Space dolphins are native to FoobarLand",
        "FoobarLand is a constitutional democracy whose first president was Bagatur Askaryan",
        "The current weather in FoobarLand is 80 degrees and clear."
    ],
}

outputs = {
    "answer": "The first president of FoobarLand was Bagatur Askaryan.",
}

eval_result = groundedness_evaluator(
    context=context,
    outputs=outputs,
)

print(eval_result)
```

```
{
  'key': 'groundedness',
  'score': True,
  'comment': 'The output states, "The first president of FoobarLand was Bagatur Askaryan," which is directly supported by the retrieved context (document 3 explicitly states this fact). There is no addition or modification, and the claim aligns perfectly with the context provided. Thus, the score should be: true.',
  'metadata': None
}
```

</details>

<details>
<summary>TypeScript</summary>

```ts
import { createLLMAsJudge, RAG_GROUNDEDNESS_PROMPT } from "openevals";

const groundednessEvaluator = createLLMAsJudge({
  prompt: RAG_GROUNDEDNESS_PROMPT,
  feedbackKey: "groundedness",
  model: "openai:gpt-5.6-sol",
});

const context = {
  documents: [
    "FoobarLand is a new country located on the dark side of the moon",
    "Space dolphins are native to FoobarLand",
    "FoobarLand is a constitutional democracy whose first president was Bagatur Askaryan",
    "The current weather in FoobarLand is 80 degrees and clear."
  ],
};

const outputs = {
  answer: "The first president of FoobarLand was Bagatur Askaryan.",
};

const evalResult = await groundednessEvaluator({
  context,
  outputs,
});

console.log(evalResult);
```

```
{
  'key': 'groundedness',
  'score': true,
  'comment': 'The output states, "The first president of FoobarLand was Bagatur Askaryan," which is directly supported by the retrieved context (document 3 explicitly states this fact). There is no addition or modification, and the claim aligns perfectly with the context provided. Thus, the score should be: true.',
  'metadata': None
}
```

</details>

#### Retrieval relevance

`retrieval_relevance` measures how relevant retrieved context is to an input query. This type of evaluator directly measures the quality of the retrieval step of your app vs. its generation step.

##### Retrieval relevance with LLM-as-judge

You can evaluate the retrieval relevance of a RAG app using the LLM-as-judge evaluator with a prompt like the built-in `RAG_RETRIEVAL_RELEVANCE_PROMPT`. Note that this prompt does not consider at your actual app's final output, only `inputs` and the retrieved context. Thus, unlike some of the other prebuilt prompts, it takes `context` and `inputs` as prompt variables:

<details>
<summary>Python</summary>

```python
from openevals.llm import create_llm_as_judge
from openevals.prompts import RAG_RETRIEVAL_RELEVANCE_PROMPT

retrieval_relevance_evaluator = create_llm_as_judge(
    prompt=RAG_RETRIEVAL_RELEVANCE_PROMPT,
    feedback_key="retrieval_relevance",
    model="openai:gpt-5.6-sol",
)

inputs = {
    "question": "Where was the first president of FoobarLand born?",
}

context = {
    "documents": [
        "FoobarLand is a new country located on the dark side of the moon",
        "Space dolphins are native to FoobarLand",
        "FoobarLand is a constitutional democracy whose first president was Bagatur Askaryan",
        "The current weather in FoobarLand is 80 degrees and clear.",
    ],
}

eval_result = retrieval_relevance_evaluator(
    inputs=inputs,
    context=context,
)

print(eval_result)
```

```
{
  'key': 'retrieval_relevance',
  'score': False,
  'comment': "The retrieved context provides some details about FoobarLand – for instance, that it is a new country located on the dark side of the moon and that its first president is Bagatur Askaryan. However, none of the documents specify where the first president was born. Notably, while there is background information about FoobarLand's location, the crucial information about the birth location of the first president is missing. Thus, the retrieved context does not fully address the question. Thus, the score should be: false.",
  'metadata': None
}
```

</details>

<details>
<summary>TypeScript</summary>

```ts
import { createLLMAsJudge, RAG_RETRIEVAL_RELEVANCE_PROMPT } from "openevals";

const retrievalRelevanceEvaluator = createLLMAsJudge({
  prompt: RAG_RETRIEVAL_RELEVANCE_PROMPT,
  feedbackKey: "retrieval_relevance",
  model: "openai:gpt-5.6-sol",
});

const inputs = {
  question: "Where was the first president of FoobarLand born?",
}

const context = {
  documents: [
    "FoobarLand is a new country located on the dark side of the moon",
    "Space dolphins are native to FoobarLand",
    "FoobarLand is a constitutional democracy whose first president was Bagatur Askaryan",
    "The current weather in FoobarLand is 80 degrees and clear.",
  ],
}

const retrievalRelevanceEvaluator = await retrievalRelevanceEvaluator({
  inputs,
  context,
});

console.log(evalResult);
```

```
{
  'key': 'retrieval_relevance',
  'score': False,
  'comment': "The retrieved context provides some details about FoobarLand – for instance, that it is a new country located on the dark side of the moon and that its first president is Bagatur Askaryan. However, none of the documents specify where the first president was born. Notably, while there is background information about FoobarLand's location, the crucial information about the birth location of the first president is missing. Thus, the retrieved context does not fully address the question. Thus, the score should be: false.",
  'metadata': None
}
```

</details>

##### Retrieval relevance with string evaluators

You can also use string evaluators like [embedding similarity](#embedding-similarity) to measure retrieval relevance without using an LLM. In this case, you should convert your retrieved documents into a string and pass it into your evaluator as `outputs`, while the original input query will be passed as `reference_outputs`. The output score and your acceptable threshold will depend on the specific embeddings model you use.

Here's an example:

<details>
<summary>Python</summary>

```python
from openevals.string.embedding_similarity import create_embedding_similarity_evaluator

evaluator = create_embedding_similarity_evaluator()

inputs = "Where was the first president of FoobarLand born?"

context = "\n".join([
    "BazQuxLand is a new country located on the dark side of the moon",
    "Space dolphins are native to BazQuxLand",
    "BazQuxLand is a constitutional democracy whose first president was Bagatur Askaryan",
    "The current weather in BazQuxLand is 80 degrees and clear.",
])

result = evaluator(
    outputs=context,
    reference_outputs=inputs,
)

print(result)
```

```
{
  'key': 'embedding_similarity',
  'score': 0.43,
  'comment': None,
  'metadata': None
}
```
</details>

<details>
<summary>TypeScript</summary>

```ts
import { createEmbeddingSimilarityEvaluator } from "openevals";
import { OpenAIEmbeddings } from "@langchain/openai";

const evaluator = createEmbeddingSimilarityEvaluator({
  embeddings: new OpenAIEmbeddings({ model: "text-embedding-3-small" }),
});

const inputs = "Where was the first president of FoobarLand born?";

const context = [
  "BazQuxLand is a new country located on the dark side of the moon",
  "Space dolphins are native to BazQuxLand",
  "BazQuxLand is a constitutional democracy whose first president was Bagatur Askaryan",
  "The current weather in BazQuxLand is 80 degrees and clear.",
].join("\n");

const result = await evaluator(
  outputs: context,
  referenceOutputs: inputs,
);

console.log(result);
```

```
{
  'key': 'embedding_similarity',
  'score': 0.43,
}
```
</details>

## Extraction and tool calls

Two very common use cases for LLMs are extracting structured output from documents and tool calling. Both of these require the LLM
to respond in a structured format. This package provides a prebuilt evaluator to help you evaluate these use cases, and is flexible
to work for a variety of extraction/tool calling use cases.

You can use the `create_json_match_evaluator` evaluator in two ways:
1. To perform an exact match of the outputs to reference outputs
2. Using LLM-as-a-judge to evaluate the outputs based on a provided rubric.

Note that this evaluator may return multiple scores based on key and aggregation strategy, so the result will be an array of scores rather than a single one.

### Evaluating structured output with exact match

Use exact match evaluation when there is a clear right or wrong answer. A common scenario is text extraction from images or PDFs where you expect specific values.

<details>
<summary>Python</summary>

```python
from openevals.json import create_json_match_evaluator

outputs = [
    {"a": "Mango, Bananas", "b": 2},
    {"a": "Apples", "b": 2, "c": [1,2,3]},
]
reference_outputs = [
    {"a": "Mango, Bananas", "b": 2},
    {"a": "Apples", "b": 2, "c": [1,2,4]},
]
evaluator = create_json_match_evaluator(
    # How to aggregate feedback keys in each element of the list: "average", "all", or None
    # "average" returns the average score. "all" returns 1 only if all keys score 1; otherwise, it returns 0. None returns individual feedback chips for each key
    aggregator="all",
    # Remove if evaluating a single structured output. This aggregates the feedback keys across elements of the list. Can be "average" or "all". Defaults to "all". "all" returns 1 if each element of the list is 1; if any score is not 1, it returns 0. "average" returns the average of the scores from each element.
    list_aggregator="average",
    exclude_keys=["a"],
)
# Invoke the evaluator with the outputs and reference outputs
result = evaluator(outputs=outputs, reference_outputs=reference_outputs)

print(result)
```

For the first element, "b" will be 1 and the aggregator will return a score of 1
For the second element, "b" will be 1, "c" will be 0 and the aggregator will return a score of 0
Therefore, the list aggregator will return a final score of 0.5.

```
[
  {
    'key': 'json_match:all',
    'score': 0.5,
    'comment': None,
  }
]
```

</details>

<details>
<summary>TypeScript</summary>

```ts
import { createJsonMatchEvaluator } from "openevals";
import { OpenAI } from "openai";

const outputs = [
    {a: "Mango, Bananas", b: 2},
    {a: "Apples", b: 2, c: [1,2,3]},
]
const reference_outputs = [
    {a: "Mango, Bananas", b: 2},
    {a: "Apples", b: 2, c: [1,2,4]},
]

const client = new OpenAI();

const evaluator = createJsonMatchEvaluator({
    // How to aggregate feedback keys in each element of the list: "average", "all", or None
    // "average" returns the average score. "all" returns 1 only if all keys score 1; otherwise, it returns 0. None returns individual feedback chips for each key
    aggregator="all",
    // Remove if evaluating a single structured output. This aggregates the feedback keys across elements of the list. Can be "average" or "all". Defaults to "all". "all" returns 1 if each element of the list is 1; if any score is not 1, it returns 0. "average" returns the average of the scores from each element.
    list_aggregator="average",
    // The keys to ignore during evaluation. Any key not passed here or in `rubric` will be evaluated using an exact match comparison to the reference outputs
    exclude_keys=["a"],
    // The provider and name of the model to use
    judge: client,
    model: "openai:gpt-5.6-sol",
})

// Invoke the evaluator with the outputs and reference outputs
const result = await evaluator({
    outputs,
    reference_outputs,
})

console.log(result)
```

For the first element, "b" will be 1 and the aggregator will return a score of 1
For the second element, "b" will be 1, "c" will be 0 and the aggregator will return a score of 0
Therefore, the list aggregator will return a final score of 0.5.

```
[
  {
    'key': 'json_match:all',
    'score': 0.5,
    'comment': None,
  }
]
```
</details>

### Evaluating structured output with LLM-as-a-Judge

Use LLM-as-a-judge to evaluate structured output or tools calls when the criteria is more subjective (for example the output is a kind of fruit or mentions all the fruits).


<details>
<summary>Python</summary>

```python
from openevals.json import create_json_match_evaluator

outputs = [
    {"a": "Mango, Bananas", "b": 2},
    {"a": "Apples", "b": 2, "c": [1,2,3]},
]
reference_outputs = [
    {"a": "Bananas, Mango", "b": 2, "d": "Not in outputs"},
    {"a": "Apples, Strawberries", "b": 2},
]
evaluator = create_json_match_evaluator(
    # How to aggregate feedback keys in each element of the list: "average", "all", or None
    # "average" returns the average score. "all" returns 1 only if all keys score 1; otherwise, it returns 0. None returns individual feedback chips for each key
    aggregator="average",
    # Remove if evaluating a single structured output. This aggregates the feedback keys across elements of the list. Can be "average" or "all". Defaults to "all". "all" returns 1 if each element of the list is 1; if any score is not 1, it returns 0. "average" returns the average of the scores from each element.
    list_aggregator="all",
    rubric={
        "a": "Does the answer mention all the fruits in the reference answer?"
    },
    # The provider and name of the model to use
    model="openai:gpt-5.6-sol",
    # Whether to force the model to reason about the keys in `rubric`. Defaults to True
    # Note that this is not currently supported if there is an aggregator specified
    use_reasoning=True
)
result = evaluator(outputs=outputs, reference_outputs=reference_outputs)

print(result)
```

For the first element, "a" will be 1  since both Mango and Bananas are in the reference output, "b" will be 1 and "d" will be 0. The aggregator will return an average score of 0.6.
For the second element, "a" will be 0 since the reference output doesn't mention all the fruits in the output,  "b" will be 1. The aggregator will return a score of 0.5.
Therefore, the list aggregator will return a final score of 0.

```
[
  {
    'key': 'json_match:a',
    'score': 0,
    'comment': None
  }
]
```

</details>

<details>
<summary>TypeScript</summary>

```ts
import { createJsonMatchEvaluator } from "openevals";
import { OpenAI } from "openai";

const outputs = [
    {a: "Mango, Bananas", b: 2},
    {a: "Apples", b: 2, c: [1,2,3]},
]
const reference_outputs = [
    {a: "Bananas, Mango", b: 2},
    {a: "Apples, Strawberries", b: 2},
]

const client = new OpenAI();

const evaluator = createJsonMatchEvaluator({
    // How to aggregate feedback keys in each element of the list: "average", "all", or None
    // "average" returns the average score. "all" returns 1 only if all keys score 1; otherwise, it returns 0. None returns individual feedback chips for each key
    aggregator="average",
    // Remove if evaluating a single structured output. This aggregates the feedback keys across elements of the list. Can be "average" or "all". Defaults to "all". "all" returns 1 if each element of the list is 1; if any score is not 1, it returns 0. "average" returns the average of the scores from each element.
    list_aggregator="all",
    // The criteria for the LLM judge to use for each key you want evaluated by the LLM
    rubric={
        a: "Does the answer mention all the fruits in the reference answer?"
    },
    // The keys to ignore during evaluation. Any key not passed here or in `rubric` will be evaluated using an exact match comparison to the reference outputs
    exclude_keys=["c"],
    // The provider and name of the model to use
    judge: client,
    model: "openai:gpt-5.6-sol",
    // Whether to use reasoning to reason about the keys in `rubric`. Defaults to True
    useReasoning: true
})

// Invoke the evaluator with the outputs and reference outputs
const result = await evaluator({
    outputs,
    reference_outputs,
})

console.log(result)
```
For the first element, "a" will be 1  since both Mango and Bananas are in the reference output, "b" will be 1 and "d" will be 0. The aggregator will return an average score of 0.6.
For the second element, "a" will be 0 since the reference output doesn't mention all the fruits in the output,  "b" will be 1. The aggregator will return a score of 0.5.
Therefore, the list aggregator will return a final score of 0.

```
{
  'key': 'json_match:a',
  'score': 0,
  'comment': None
}
```

</details>

### Nested objects

Nested object and array values are supported for exact-match evaluation. They are compared by deep equality as a whole value, so the nested value must match exactly.

<details>
<summary>Python</summary>

```python
from openevals.json import create_json_match_evaluator

evaluator = create_json_match_evaluator(aggregator="all")

matching_result = evaluator(
    outputs={"foo": [{"bar": 1}]},
    reference_outputs={"foo": [{"bar": 1}]},
)
mismatching_result = evaluator(
    outputs={"foo": [{"bar": 2}]},
    reference_outputs={"foo": [{"bar": 1}]},
)

print(matching_result[0]["score"])  # 1
print(mismatching_result[0]["score"])  # 0
```
</details>

<details>
<summary>TypeScript</summary>

```ts
import { createJsonMatchEvaluator } from "openevals";

const evaluator = createJsonMatchEvaluator({ aggregator: "all" });

const matchingResult = await evaluator({
  outputs: { foo: [{ bar: 1 }] },
  referenceOutputs: { foo: [{ bar: 1 }] },
});
const mismatchingResult = await evaluator({
  outputs: { foo: [{ bar: 2 }] },
  referenceOutputs: { foo: [{ bar: 1 }] },
});

console.log(matchingResult[0].score); // 1
console.log(mismatchingResult[0].score); // 0
```
</details>

The `rubric` and `exclude_keys`/`excludeKeys` options target top-level keys only. They do not support nested paths such as `foo.bar` or `foo.0.bar`. To grade a nested sub-value with a rubric, either flatten the structure before evaluation or write a rubric entry for the top-level key that describes the expected nested value.

## Code

OpenEvals contains some useful prebuilt evaluators for evaluating generated code:

- Type-checking generated code with [Pyright](https://github.com/microsoft/pyright) and [Mypy](https://github.com/python/mypy) (Python-only) or TypeScript's built-in type checker (JavaScript only)
  - Note that these local type-checking evaluators will not install any dependencies and will ignore errors for these imports
- Sandboxed type-checking and execution evaluators that use [E2B](https://e2b.dev/) to install dependencies and run generated code securely
- LLM-as-a-judge for code

All evaluators in this section accept `outputs` as a string, an object with a key `"messages"` that contains a list of messages, or a message-like object with a key `"content"` that contains a string.

### Extracting code outputs

Since LLM outputs with code may contain other text (for example, interleaved explanations with code), OpenEvals code evaluators share some built-in extraction methods for identifying just the code from of LLM outputs.

For any of the evaluators in this section, you can either pass a `code_extraction_strategy` param set to `llm`, which will use an `llm` with a default prompt to directly extract code, or `markdown_code_blocks`, which will extract anything in markdown code blocks (triple backticks) that is not marked with `bash` or other shell command languages. If extraction fails for one of these methods, the evaluator response will include a `metadata.code_extraction_failed` field set to `True`.

You can alternatively pass a `code_extractor` param set to a function that takes an LLM output and returns a string of code. The default is to leave the output content untouched (`"none"`).

If using `code_extraction_strategy="llm"`, you can also pass a `model` string or a `client` to the evaluator to set which evaluator the model uses for code extraction.
If you would like to customize the prompt, you should use the `code_extractor` param instead.

### Pyright (Python-only)

For Pyright, you will need to install the `pyright` CLI on your system:

```bash
pip install pyright
```

You can find full installation instructions [here](https://microsoft.github.io/pyright/#/installation?id=command-line).

Then, you can use it as follows:

```python
from openevals.code.pyright import create_pyright_evaluator

evaluator = create_pyright_evaluator()

CODE = """
def sum_of_two_numbers(a, b): return a + b
"""

result = evaluator(outputs=CODE)

print(result)
```

```
{
    'key': 'pyright_succeeded',
    'score': True,
    'comment': None,
}
```

> [!WARNING]
> The evaluator will ignore `reportMissingImports` errors. If you want to run type-checking over generated dependencies, check out the [sandboxed version](#sandbox-pyright-python-only) of this evaluator.

You can also pass `pyright_cli_args` to the evaluator to customize the arguments passed to the `pyright` CLI:

```python
evaluator = create_pyright_evaluator(
    pyright_cli_args=["--flag"]
)
```

For a full list of supported arguments, see the [pyright CLI documentation](https://microsoft.github.io/pyright/#/command-line).

### Mypy (Python-only)

For Mypy, you will need to install `mypy` on your system:

```bash
pip install mypy
```

You can find full installation instructions [here](https://mypy.readthedocs.io/en/stable/getting_started.html).

Then, you can use it as follows:

```python
from openevals.code.mypy import create_mypy_evaluator

evaluator = create_mypy_evaluator()

CODE = """
def sum_of_two_numbers(a, b): return a + b
"""

result = evaluator(outputs=CODE)

print(result)
```

```
{
    'key': 'mypy_succeeded',
    'score': True,
    'comment': None,
}
```

By default, this evaluator will run with the following arguments:

```
mypy --no-incremental --disallow-untyped-calls --disallow-incomplete-defs --ignore-missing-imports
```

But you can pass `mypy_cli_args` to the evaluator to customize the arguments passed to the `mypy` CLI. This will override the default arguments:

```python
evaluator = create_mypy_evaluator(
    mypy_cli_args=["--flag"]
)
```

### TypeScript type-checking (TypeScript-only)

The TypeScript evaluator uses TypeScript's type checker to check the code for correctness.

You will need to install `typescript` on your system as a dependency (not a dev dependency!):

```bash
npm install typescript
```

Then, you can use it as follows (note that you should import from the `openevals/code/typescript` entrypoint due to the additional required dependency):

```ts
import { createTypeScriptEvaluator } from "openevals/code/typescript";

const evaluator = createTypeScriptEvaluator();

const result = await evaluator({
    outputs: "function add(a, b) { return a + b; }",
});

console.log(result);
```

```
{
    'key': 'typescript_succeeded',
    'score': True,
    'comment': None,
}
```

> [!WARNING]
> The evaluator will ignore `reportMissingImports` errors. If you want to run type-checking over generated dependencies, check out the [sandboxed version](#sandbox-typescript-typescript-only) of this evaluator.

### LLM-as-judge for code

OpenEvals includes a prebuilt LLM-as-a-judge evaluator for code. The primary differentiator between this one and the more generic [LLM-as-judge evaluator](#llm-as-judge) is that it will perform the extraction steps detailed above - otherwise it takes the same arguments, including a prompt.

You can run an LLM-as-a-judge evaluator for code as follows:

<details>
<summary>Python</summary>

```python
from openevals.code.llm import create_code_llm_as_judge
from openevals.prompts import CODE_CORRECTNESS_PROMPT

llm_as_judge = create_code_llm_as_judge(
    prompt=CODE_CORRECTNESS_PROMPT,
    model="openai:gpt-5.6-sol",
    code_extraction_strategy="markdown_code_blocks",
)


INPUTS = """
Rewrite the code below to be async:

\`\`\`python
def _run_mypy(
    *,
    filepath: str,
    mypy_cli_args: list[str],
) -> Tuple[bool, str]:
    result = subprocess.run(
        [
            "mypy",
            *mypy_cli_args,
            filepath,
        ],
        capture_output=True,
    )
    return _parse_mypy_output(result.stdout)
\`\`\`
"""

OUTPUTS = """
\`\`\`python
async def _run_mypy_async(
    *,
    filepath: str,
    mypy_cli_args: list[str],
) -> Tuple[bool, str]:
    process = await subprocess.run(
        [
            "mypy",
            *mypy_cli_args,
            filepath,
        ],
    )
    stdout, _ = await process.communicate()

    return _parse_mypy_output(stdout)
\`\`\`
"""

eval_result = llm_as_judge(
    inputs=INPUTS,
    outputs=OUTPUTS
)

print(eval_result)
```

```
{
    'key': 'code_correctness',
    'score': False,
    'comment': "The provided async code is incorrect. It still incorrectly attempts to use 'await subprocess.run' which is synchronous and does not support being awaited. The proper asynchronous approach would be to use 'asyncio.create_subprocess_exec' (or a similar asyncio API) with appropriate redirection of stdout (e.g., stdout=asyncio.subprocess.PIPE) and then await the 'communicate()' call. Thus, the code does not meet the requirements completely as specified, and there is a significant error which prevents it from working correctly. Thus, the score should be: false.",
}
```
</details>

<details>
<summary>TypeScript</summary>

```ts
import { createCodeLLMAsJudge, CODE_CORRECTNESS_PROMPT } from "openevals";

const evaluator = createCodeLLMAsJudge({
  prompt: CODE_CORRECTNESS_PROMPT,
  model: "openai:gpt-5.6-sol",
});

const inputs = `Add proper TypeScript types to the following code:

\`\`\`typescript
function add(a, b) { return a + b; }
\`\`\`
`;

const outputs = `
\`\`\`typescript
function add(a: number, b: number): boolean {
  return a + b;
}
\`\`\`
`;

const evalResult = await evaluator({ inputs, outputs });

console.log(evalResult);
```

```
{
  "key": "code_correctness",
  "score": false,
  "comment": "The code has a logical error in its type specification. The function is intended to add two numbers and return their sum, so the return type should be number, not boolean. This mistake makes the solution incorrect according to the rubric. Thus, the score should be: false."
}
```

</details>

## Sandboxed code

LLMs can generate arbitrary code, and if you are running a code evaluator locally, you may not wish to install generated dependencies or run this arbitrary code locally. To solve this, OpenEvals integrates with [E2B](https://e2b.dev) to run some code evaluators in isolated sandboxes.

Given some output code from an LLM, these sandboxed code evaluators will run scripts in a sandbox that parse out dependencies and install them so that the evaluator has proper context for type-checking or execution.

These evaluators all require a `sandbox` parameter upon creation, and also accept the code extraction parameters present in the other [code evaluators](#extracting-code-outputs). For Python, there is a special `OpenEvalsPython` template that includes `pyright` and `uv` preinstalled for faster execution, though the evaluator will work with any sandbox.

If you have a custom sandbox with dependencies pre-installed or files already set up, you can supply a `sandbox_project_directory` (Python) or `sandboxProjectDirectory` (TypeScript) param when calling the appropriate `create` method to customize the folder in which type-checking/execution runs.

### Sandbox Pyright (Python-only)

You can also run Pyright type-checking in an [E2B](https://e2b.dev) sandbox. The evaluator will run a script to parse out package names
from generated code, then will install those packages in the sandbox and will run Pyright. The evaluator will return any analyzed errors in its comment.

You will need to install the `e2b-code-interpreter` package, available as an extra:

```bash
pip install openevals["e2b-code-interpreter"]
```

Then, you will need to set your E2B API key as an environment variable:

```
export E2B_API_KEY="YOUR_KEY_HERE"
```

Then, you will need to initialize an E2B sandbox. There is a special `OpenEvalsPython` template that includes `pyright` and `uv` preinstalled for faster execution, though the evaluator will work with any sandbox:

```python
from e2b_code_interpreter import Sandbox

# E2B template with uv and pyright preinstalled
sandbox = Sandbox("OpenEvalsPython")
```

Finally, pass that created sandbox into the `create_e2b_pyright_evaluator` factory function and run it:

```python
from openevals.code.e2b.pyright import create_e2b_pyright_evaluator

evaluator = create_e2b_pyright_evaluator(
    sandbox=sandbox,
)

CODE = """
from typing import Annotated

from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages


class State(TypedDict):
    messages: Annotated[list, add_messages]

builder = StateGraph(State)
builder.add_node("start", lambda state: state)
builder.compile()

builder.invoke({})
"""

eval_result = evaluator(outputs=CODE)

print(eval_result)
```

```
{
  'key': 'pyright_succeeded',
  'score': false,
  'comment': '[{"severity": "error", "message": "Cannot access attribute "invoke" for class "StateGraph"...}]',
}
```

Above, the evaluator identifies and installs the `langgraph` package inside the sandbox, then runs `pyright`. The type-check fails because the provided code misuses the imported package, invoking the builder rather than the compiled graph.

### Sandbox TypeScript type-checking (TypeScript-only)

You can also run TypeScript type-checking in an [E2B](https://e2b.dev) sandbox. The evaluator will run a script to parse out package names
from generated code, then will install those packages in the sandbox and will run TypeScript. The evaluator will return any analyzed errors in its comment.

You will need to install the official `@e2b/code-interpreter` package as a peer dependency:

```bash
npm install @e2b/code-interpreter
```

Then, you will need to set your E2B API key as an environment variable:

```
process.env.E2B_API_KEY="YOUR_KEY_HERE"
```

Next, initialize an E2B sandbox:

```ts
import { Sandbox } from "@e2b/code-interpreter";

const sandbox = await Sandbox.create();
```

And finally, pass the sandbox into the `createE2BTypeScriptEvaluator` and run it:

```ts
import { createE2BTypeScriptEvaluator } from "openevals/code/e2b";

const evaluator = createE2BTypeScriptEvaluator({
  sandbox,
});

const CODE = `
import { StateGraph } from '@langchain/langgraph';

await StateGraph.invoke({})
`;

const evalResult = await evaluator({ outputs: CODE });

console.log(evalResult);
```

```
{
  "key": "typescript_succeeded",
  "score": false,
  "comment": "(3,18): Property 'invoke' does not exist on type 'typeof StateGraph'."
}
```

Above, the evaluator identifies and installs `@langchain/langgraph`, then runs a type-check via TypeScript. The type-check fails because the provided code misuses the imported package.

### Sandbox Execution

To further evaluate code correctness, OpenEvals has a sandbox execution evaluator that runs generated code in an [E2B](https://e2b.dev) sandbox.

The evaluator will run a script to parse out package names from generated code, then will install those packages in the sandbox. The evaluator will then attempt to run the generated code return any analyzed errors in its comment.

<details>
<summary>Python</summary>

You will need to install the `e2b-code-interpreter` package, available as an extra:

```bash
pip install openevals["e2b-code-interpreter"]
```

Then, you will need to set your E2B API key as an environment variable:

```
export E2B_API_KEY="YOUR_KEY_HERE"
```

Then, you will need to initialize an E2B sandbox. There is a special `OpenEvalsPython` template that includes `pyright` and `uv` preinstalled for faster execution, though the evaluator will work with any sandbox:

```python
from e2b_code_interpreter import Sandbox

# E2B template with uv and pyright preinstalled
sandbox = Sandbox("OpenEvalsPython")
```

Then pass the sandbox to the `create_e2b_execution_evaluator` factory function and run the result:

```python
from openevals.code.e2b.execution import create_e2b_execution_evaluator

evaluator = create_e2b_execution_evaluator(
    sandbox=sandbox,
)

CODE = """
from typing import Annotated

from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages


class State(TypedDict):
    messages: Annotated[list, add_messages]

builder = StateGraph(State)
builder.add_node("start", lambda state: state)
builder.compile()

builder.invoke({})
"""

eval_result = evaluator(outputs=CODE)

print(eval_result)
```

```
{
  'key': 'execution_succeeded',
  'score': False,
  'comment': '"Command exited with code 1 and error:\nTraceback (most recent call last):\n  File \"/home/user/openevals/outputs.py\", line 15, in <module>\n    builder.compile()\n  File \"/home/user/openevals/.venv/lib/python3.10/site-packages/langgraph/graph/state.py\", line 602, in compile\n    self.validate(\n  File \"/home/user/openevals/.venv/lib/python3.10/site-packages/langgraph/graph/graph.py\", line 267, in validate\n    raise ValueError(\nValueError: Graph must have an entrypoint: add at least one edge from START to another node\n"'
}
```

Above, the evaluator identifies and installs `langgraph`, then attempts to execute the code. The type-check fails because the provided code misuses the imported package.

If desired, you can pass an `environment_variables` dict when creating the evaluator. Generated code will  have access to these variables within the sandbox, but be cautious, as there is no way to predict exactly what code an LLM will generate.

</details>

<details>
<summary>TypeScript</summary>

You will need to install the official `@e2b/code-interpreter` package as a peer dependency:

```bash
npm install @e2b/code-interpreter
```

Then, you will need to set your E2B API key as an environment variable:

```
process.env.E2B_API_KEY="YOUR_KEY_HERE"
```

Next, initialize an E2B sandbox:

```ts
import { Sandbox } from "@e2b/code-interpreter";

const sandbox = await Sandbox.create();
```

And finally, pass the sandbox into the `create` and run it:

```ts
import { createE2BExecutionEvaluator } from "openevals/code/e2b";

const evaluator = createE2BExecutionEvaluator({
  sandbox,
});

const CODE = `
import { Annotation, StateGraph } from '@langchain/langgraph';

const StateAnnotation = Annotation.Root({
  joke: Annotation<string>,
  topic: Annotation<string>,
});

const graph = new StateGraph(StateAnnotation)
  .addNode("joke", () => ({}))
  .compile();

await graph.invoke({
  joke: "foo",
  topic: "history",
});
`;

const evalResult = await evaluator({ outputs });

console.log(evalResult);
```

```
{
  "key": "execution_succeeded",
  "score": false,
  "comment": "file:///home/user/openevals/node_modules/@langchain/langgraph/dist/graph/state.js:197\n            throw new Error(`${key} is already being used as a state attribute (a.k.a. a channel), cannot also be used as a node name.`);\n                  ^\n\nError: joke is already being used as a state attribute (a.k.a. a channel), cannot also be used as a node name.\n    at StateGraph.addNode (/home/user/openevals/node_modules/@langchain/langgraph/src/graph/state.ts:292:13)\n    at <anonymous> (/home/user/openevals/outputs.ts:9:4)\n    at ModuleJob.run (node:internal/modules/esm/module_job:195:25)\n    at async ModuleLoader.import (node:internal/modules/esm/loader:336:24)\n    at async loadESM (node:internal/process/esm_loader:34:7)\n    at async handleMainPromise (node:internal/modules/run_main:106:12)\n\nNode.js v18.19.0\n"
}
```

Above, the evaluator identifies and installs `@langchain/langgraph`, then attempts to execute the code. The type-check fails because the provided code misuses the imported package.

If desired, you can pass an `environmentVariables` object when creating the evaluator. Generated code will  have access to these variables within the sandbox, but be cautious, as there is no way to predict exactly what code an LLM will generate.

</details>

## Agent trajectory

If you are building an agent, `openevals` includes evaluators for assessing the entire **trajectory** of an agent's execution — the sequence of messages and tool calls it makes while solving a task.

Trajectories should be formatted as lists of [OpenAI-style messages](https://platform.openai.com/docs/api-reference/messages). LangChain `BaseMessage` instances are also supported.

### Trajectory match

`create_trajectory_match_evaluator`/`createTrajectoryMatchEvaluator` compares an agent's trajectory against a reference trajectory. You can set `trajectory_match_mode`/`trajectoryMatchMode` to one of four modes:

- `"strict"` — same tool calls in the same order
- `"unordered"` — same tool calls in any order
- `"subset"` — output tool calls are a subset of reference
- `"superset"` — output tool calls are a superset of reference

#### Strict match

The `"strict"` mode compares two trajectories and ensures that they contain the same messages in the same order with the same tool calls. Note that it does allow for differences in message content (e.g. `"SF"` vs. `"San Francisco"`):

<details>
<summary>Python</summary>

```python
import json
from openevals import create_trajectory_match_evaluator

outputs = [
    {"role": "user", "content": "What is the weather in SF?"},
    {
        "role": "assistant",
        "content": "",
        "tool_calls": [
            {
                "function": {
                    "name": "get_weather",
                    "arguments": json.dumps({"city": "San Francisco"}),
                }
            },
            {
                "function": {
                    "name": "accuweather_forecast",
                    "arguments": json.dumps({"city": "San Francisco"}),
                }
            }
        ],
    },
    {"role": "tool", "content": "It's 80 degrees and sunny in SF."},
    {"role": "assistant", "content": "The weather in SF is 80 degrees and sunny."},
]
reference_outputs = [
    {"role": "user", "content": "What is the weather in San Francisco?"},
    {
        "role": "assistant",
        "content": "",
        "tool_calls": [
            {
                "function": {
                    "name": "get_weather",
                    "arguments": json.dumps({"city": "San Francisco"}),
                }
            }
        ],
    },
    {"role": "tool", "content": "It's 80 degrees and sunny in San Francisco."},
    {"role": "assistant", "content": "The weather in SF is 80˚ and sunny."},
]

evaluator = create_trajectory_match_evaluator(trajectory_match_mode="strict")
result = evaluator(outputs=outputs, reference_outputs=reference_outputs)
print(result)
```

```
{'key': 'trajectory_strict_match', 'score': False, 'comment': None}
```
</details>

<details>
<summary>TypeScript</summary>

```ts
import {
  createTrajectoryMatchEvaluator,
  type FlexibleChatCompletionMessage,
} from "openevals";

const outputs = [
  { role: "user", content: "What is the weather in SF?" },
  {
    role: "assistant",
    content: "",
    tool_calls: [{
      function: {
        name: "get_weather",
        arguments: JSON.stringify({ city: "San Francisco" }),
      },
    }, {
      function: {
        name: "accuweather_forecast",
        arguments: JSON.stringify({ city: "San Francisco" }),
      },
    }],
  },
  { role: "tool", content: "It's 80 degrees and sunny in SF." },
  { role: "assistant", content: "The weather in SF is 80 degrees and sunny." },
] satisfies FlexibleChatCompletionMessage[];

const referenceOutputs = [
  { role: "user", content: "What is the weather in San Francisco?" },
  {
    role: "assistant",
    content: "",
    tool_calls: [{
      function: {
        name: "get_weather",
        arguments: JSON.stringify({ city: "San Francisco" }),
      },
    }],
  },
  { role: "tool", content: "It's 80 degrees and sunny in San Francisco." },
] satisfies FlexibleChatCompletionMessage[];

const evaluator = createTrajectoryMatchEvaluator({ trajectoryMatchMode: "strict" });
const result = await evaluator({ outputs, referenceOutputs });
console.log(result);
```

```
{ key: 'trajectory_strict_match', score: false }
```
</details>

`"strict"` is useful if you want to ensure that tools are always called in the same order for a given query (e.g. a policy lookup tool before a tool that requests time off for an employee).

**Note:** If you would like to configure the way this evaluator checks for tool call equality, see [this section](#tool-args-match-modes).

#### Unordered match

The `"unordered"` mode compares two trajectories and ensures that they contain the same tool calls in any order. This is useful if you want to allow flexibility in how an agent obtains the proper information, but still do care that all information was retrieved.

<details>
<summary>Python</summary>

```python
import json
from openevals import create_trajectory_match_evaluator

outputs = [
    {"role": "user", "content": "What is the weather in SF and is there anything fun happening?"},
    {
        "role": "assistant",
        "content": "",
        "tool_calls": [{"function": {"name": "get_weather", "arguments": json.dumps({"city": "San Francisco"})}}],
    },
    {"role": "tool", "content": "It's 80 degrees and sunny in SF."},
    {
        "role": "assistant",
        "content": "",
        "tool_calls": [{"function": {"name": "get_fun_activities", "arguments": json.dumps({"city": "San Francisco"})}}],
    },
    {"role": "tool", "content": "Nothing fun is happening, you should stay indoors and read!"},
    {"role": "assistant", "content": "The weather in SF is 80 degrees and sunny, but there is nothing fun happening."},
]
reference_outputs = [
    {"role": "user", "content": "What is the weather in SF and is there anything fun happening?"},
    {
        "role": "assistant",
        "content": "",
        "tool_calls": [
            {"function": {"name": "get_fun_activities", "arguments": json.dumps({"city": "San Francisco"})}},
            {"function": {"name": "get_weather", "arguments": json.dumps({"city": "San Francisco"})}},
        ],
    },
    {"role": "tool", "content": "Nothing fun is happening, you should stay indoors and read!"},
    {"role": "tool", "content": "It's 80 degrees and sunny in SF."},
    {"role": "assistant", "content": "In SF, it's 80˚ and sunny, but there is nothing fun happening."},
]

evaluator = create_trajectory_match_evaluator(trajectory_match_mode="unordered")
result = evaluator(outputs=outputs, reference_outputs=reference_outputs)
print(result)
```

```
{'key': 'trajectory_unordered_match', 'score': True, 'comment': None}
```
</details>

<details>
<summary>TypeScript</summary>

```ts
import {
  createTrajectoryMatchEvaluator,
  type FlexibleChatCompletionMessage,
} from "openevals";

const outputs = [
  { role: "user", content: "What is the weather in SF and is there anything fun happening?" },
  {
    role: "assistant",
    content: "",
    tool_calls: [{ function: { name: "get_weather", arguments: JSON.stringify({ city: "San Francisco" }) } }],
  },
  { role: "tool", content: "It's 80 degrees and sunny in SF." },
  {
    role: "assistant",
    content: "",
    tool_calls: [{ function: { name: "get_fun_activities", arguments: JSON.stringify({ city: "San Francisco" }) } }],
  },
  { role: "tool", content: "Nothing fun is happening, you should stay indoors and read!" },
  { role: "assistant", content: "The weather in SF is 80 degrees and sunny, but there is nothing fun happening." },
] satisfies FlexibleChatCompletionMessage[];

const referenceOutputs = [
  { role: "user", content: "What is the weather in SF and is there anything fun happening?" },
  {
    role: "assistant",
    content: "",
    tool_calls: [
      { function: { name: "get_fun_activities", arguments: JSON.stringify({ city: "San Francisco" }) } },
      { function: { name: "get_weather", arguments: JSON.stringify({ city: "San Francisco" }) } },
    ],
  },
  { role: "tool", content: "Nothing fun is happening, you should stay indoors and read!" },
  { role: "tool", content: "It's 80 degrees and sunny in SF." },
  { role: "assistant", content: "In SF, it's 80˚ and sunny, but there is nothing fun happening." },
] satisfies FlexibleChatCompletionMessage[];

const evaluator = createTrajectoryMatchEvaluator({ trajectoryMatchMode: "unordered" });
const result = await evaluator({ outputs, referenceOutputs });
console.log(result);
```

```
{ key: 'trajectory_unordered_match', score: true }
```
</details>

`"unordered"` is useful if you want to ensure that specific tools are called at some point in the trajectory, but you don't necessarily need them to be in message order.

**Note:** If you would like to configure the way this evaluator checks for tool call equality, see [this section](#tool-args-match-modes).

#### Subset and superset match

The `"subset"` and `"superset"` modes match partial trajectories, ensuring that a trajectory contains a subset/superset of tool calls contained in a reference trajectory.

<details>
<summary>Python</summary>

```python
import json
from openevals import create_trajectory_match_evaluator

outputs = [
    {"role": "user", "content": "What is the weather in SF and London?"},
    {
        "role": "assistant",
        "content": "",
        "tool_calls": [
            {"function": {"name": "get_weather", "arguments": json.dumps({"city": "SF and London"})}},
            {"function": {"name": "accuweather_forecast", "arguments": json.dumps({"city": "SF and London"})}}
        ],
    },
    {"role": "tool", "content": "It's 80 degrees and sunny in SF, and 90 degrees and rainy in London."},
    {"role": "tool", "content": "Unknown."},
    {"role": "assistant", "content": "The weather in SF is 80 degrees and sunny. In London, it's 90 degrees and rainy."},
]
reference_outputs = [
    {"role": "user", "content": "What is the weather in SF and London?"},
    {
        "role": "assistant",
        "content": "",
        "tool_calls": [
            {"function": {"name": "get_weather", "arguments": json.dumps({"city": "SF and London"})}}
        ],
    },
    {"role": "tool", "content": "It's 80 degrees and sunny in San Francisco, and 90 degrees and rainy in London."},
    {"role": "assistant", "content": "The weather in SF is 80˚ and sunny. In London, it's 90˚ and rainy."},
]

evaluator = create_trajectory_match_evaluator(trajectory_match_mode="superset")  # or "subset"
result = evaluator(outputs=outputs, reference_outputs=reference_outputs)
print(result)
```

```
{'key': 'trajectory_superset_match', 'score': True, 'comment': None}
```
</details>

<details>
<summary>TypeScript</summary>

```ts
import {
  createTrajectoryMatchEvaluator,
  type FlexibleChatCompletionMessage,
} from "openevals";

const outputs = [
  { role: "user", content: "What is the weather in SF and London?" },
  {
    role: "assistant",
    content: "",
    tool_calls: [
      { function: { name: "get_weather", arguments: JSON.stringify({ city: "SF and London" }) } },
      { function: { name: "accuweather_forecast", arguments: JSON.stringify({ city: "SF and London" }) } },
    ],
  },
  { role: "tool", content: "It's 80 degrees and sunny in SF, and 90 degrees and rainy in London." },
  { role: "tool", content: "Unknown." },
  { role: "assistant", content: "The weather in SF is 80 degrees and sunny. In London, it's 90 degrees and rainy." },
] satisfies FlexibleChatCompletionMessage[];

const referenceOutputs = [
  { role: "user", content: "What is the weather in SF and London?" },
  {
    role: "assistant",
    content: "",
    tool_calls: [
      { function: { name: "get_weather", arguments: JSON.stringify({ city: "SF and London" }) } },
    ],
  },
  { role: "tool", content: "It's 80 degrees and sunny in San Francisco, and 90 degrees and rainy in London." },
  { role: "assistant", content: "The weather in SF is 80˚ and sunny. In London, it's 90˚ and rainy." },
] satisfies FlexibleChatCompletionMessage[];

const evaluator = createTrajectoryMatchEvaluator({ trajectoryMatchMode: "superset" }); // or "subset"
const result = await evaluator({ outputs, referenceOutputs });
console.log(result);
```

```
{ key: 'trajectory_superset_match', score: true }
```
</details>

`"superset"` is useful if you want to ensure that some key tools were called at some point in the trajectory, but an agent calling extra tools is still acceptable. `"subset"` is the inverse and is useful if you want to ensure that the agent did not call any tools beyond the expected ones.

#### Tool args match modes

When checking equality between tool calls, the above evaluators will require that all tool call arguments are the exact same by default. You can configure this behavior in the following ways:

- Treating any two tool calls for the same tool as equivalent by setting `tool_args_match_mode="ignore"` (Python) or `toolArgsMatchMode: "ignore"` (TypeScript)
- Treating a tool call as equivalent if it contains a subset/superset of args compared to a reference tool call of the same name with `tool_args_match_mode="subset"/"superset"` (Python) or `toolArgsMatchMode: "subset"/"superset"` (TypeScript)
- Setting custom matchers for all calls of a given tool using the `tool_args_match_overrides` (Python) or `toolArgsMatchOverrides` (TypeScript) param

`tool_args_match_overrides`/`toolArgsMatchOverrides` takes a dictionary whose keys are tool names and whose values are either `"exact"`, `"ignore"`, `"subset"`, `"superset"`, a list of field paths that must match exactly, or a comparator function:

Here's an example that allows case insensitivity for the arguments to a tool named `get_weather`:

<details>
<summary>Python</summary>

```python
import json
from openevals import create_trajectory_match_evaluator

outputs = [
    {"role": "user", "content": "What is the weather in SF?"},
    {
        "role": "assistant",
        "content": "",
        "tool_calls": [
            {"function": {"name": "get_weather", "arguments": json.dumps({"city": "san francisco"})}}
        ],
    },
    {"role": "tool", "content": "It's 80 degrees and sunny in SF."},
    {"role": "assistant", "content": "The weather in SF is 80 degrees and sunny."},
]
reference_outputs = [
    {"role": "user", "content": "What is the weather in San Francisco?"},
    {
        "role": "assistant",
        "content": "",
        "tool_calls": [
            {"function": {"name": "get_weather", "arguments": json.dumps({"city": "San Francisco"})}}
        ],
    },
    {"role": "tool", "content": "It's 80 degrees and sunny in San Francisco."},
    {"role": "assistant", "content": "The weather in SF is 80˚ and sunny."},
]

evaluator = create_trajectory_match_evaluator(
    trajectory_match_mode="strict",
    tool_args_match_mode="exact",
    tool_args_match_overrides={
        "get_weather": lambda x, y: x["city"].lower() == y["city"].lower()
    }
)

result = evaluator(outputs=outputs, reference_outputs=reference_outputs)
print(result)
```

```
{'key': 'trajectory_strict_match', 'score': True, 'comment': None}
```
</details>

<details>
<summary>TypeScript</summary>

```ts
import {
  createTrajectoryMatchEvaluator,
  type FlexibleChatCompletionMessage,
} from "openevals";

const outputs = [
  { role: "user", content: "What is the weather in SF?" },
  {
    role: "assistant",
    content: "",
    tool_calls: [{ function: { name: "get_weather", arguments: JSON.stringify({ city: "san francisco" }) } }],
  },
  { role: "tool", content: "It's 80 degrees and sunny in SF." },
  { role: "assistant", content: "The weather in SF is 80 degrees and sunny." },
] satisfies FlexibleChatCompletionMessage[];

const referenceOutputs = [
  { role: "user", content: "What is the weather in San Francisco?" },
  {
    role: "assistant",
    content: "",
    tool_calls: [{ function: { name: "get_weather", arguments: JSON.stringify({ city: "San Francisco" }) } }],
  },
  { role: "tool", content: "It's 80 degrees and sunny in San Francisco." },
  { role: "assistant", content: "The weather in SF is 80˚ and sunny." },
] satisfies FlexibleChatCompletionMessage[];

const evaluator = createTrajectoryMatchEvaluator({
  trajectoryMatchMode: "strict",
  toolArgsMatchOverrides: {
    get_weather: (x, y) =>
      typeof x.city === "string" &&
      typeof y.city === "string" &&
      x.city.toLowerCase() === y.city.toLowerCase(),
  },
});

const result = await evaluator({ outputs, referenceOutputs });
console.log(result);
```

```
{ key: 'trajectory_strict_match', score: true }
```
</details>

This flexibility allows you to handle cases where you want looser equality for LLM generated arguments (`"san francisco"` to equal `"San Francisco"`) for only specific tool calls.

### Trajectory LLM-as-judge

`create_trajectory_llm_as_judge`/`createTrajectoryLLMAsJudge` uses an LLM to assess whether an agent's trajectory is accurate. Unlike the trajectory match evaluators, it doesn't require a reference trajectory. Use `TRAJECTORY_ACCURACY_PROMPT` for no-reference evaluation, or `TRAJECTORY_ACCURACY_PROMPT_WITH_REFERENCE` to compare against a reference:

<details>
<summary>Python</summary>

```python
import json
from openevals import create_trajectory_llm_as_judge
from openevals.prompts import TRAJECTORY_ACCURACY_PROMPT

evaluator = create_trajectory_llm_as_judge(
    prompt=TRAJECTORY_ACCURACY_PROMPT,
    model="openai:gpt-5.6-sol",
)

outputs = [
    {"role": "user", "content": "What is the weather in SF?"},
    {
        "role": "assistant",
        "content": "",
        "tool_calls": [
            {"function": {"name": "get_weather", "arguments": json.dumps({"city": "SF"})}}
        ],
    },
    {"role": "tool", "content": "It's 80 degrees and sunny in SF."},
    {"role": "assistant", "content": "The weather in SF is 80 degrees and sunny."},
]

result = evaluator(outputs=outputs)
print(result)
```

```
{'key': 'trajectory_accuracy', 'score': True, 'comment': 'The trajectory is accurate...'}
```
</details>

<details>
<summary>TypeScript</summary>

```ts
import {
  createTrajectoryLLMAsJudge,
  TRAJECTORY_ACCURACY_PROMPT,
  type FlexibleChatCompletionMessage,
} from "openevals";

const evaluator = createTrajectoryLLMAsJudge({
  prompt: TRAJECTORY_ACCURACY_PROMPT,
  model: "openai:gpt-5.6-sol",
});

const outputs = [
  { role: "user", content: "What is the weather in SF?" },
  {
    role: "assistant",
    content: "",
    tool_calls: [{ function: { name: "get_weather", arguments: JSON.stringify({ city: "SF" }) } }],
  },
  { role: "tool", content: "It's 80 degrees and sunny in SF." },
  { role: "assistant", content: "The weather in SF is 80 degrees and sunny." },
] satisfies FlexibleChatCompletionMessage[];

const result = await evaluator({ outputs });
console.log(result);
```

```
{ key: 'trajectory_accuracy', score: true, comment: 'The trajectory is accurate...' }
```
</details>

If you have a reference trajectory, use `TRAJECTORY_ACCURACY_PROMPT_WITH_REFERENCE` and pass `reference_outputs`/`referenceOutputs`:

<details>
<summary>Python</summary>

```python
import json
from openevals import create_trajectory_llm_as_judge
from openevals.prompts import TRAJECTORY_ACCURACY_PROMPT_WITH_REFERENCE

evaluator = create_trajectory_llm_as_judge(
    prompt=TRAJECTORY_ACCURACY_PROMPT_WITH_REFERENCE,
    model="openai:gpt-5.6-sol",
)

outputs = [
    {"role": "user", "content": "What is the weather in SF?"},
    {
        "role": "assistant",
        "content": "",
        "tool_calls": [
            {"function": {"name": "get_weather", "arguments": json.dumps({"city": "SF"})}}
        ],
    },
    {"role": "tool", "content": "It's 80 degrees and sunny in SF."},
    {"role": "assistant", "content": "The weather in SF is 80 degrees and sunny."},
]
reference_outputs = [
    {"role": "user", "content": "What is the weather in SF?"},
    {
        "role": "assistant",
        "content": "",
        "tool_calls": [
            {"function": {"name": "get_weather", "arguments": json.dumps({"city": "San Francisco"})}}
        ],
    },
    {"role": "tool", "content": "It's 80 degrees and sunny in San Francisco."},
    {"role": "assistant", "content": "The weather in SF is 80˚ and sunny."},
]

result = evaluator(outputs=outputs, reference_outputs=reference_outputs)
print(result)
```

```
{'key': 'trajectory_accuracy', 'score': True, 'comment': 'The provided agent trajectory is consistent with the reference...'}
```
</details>

<details>
<summary>TypeScript</summary>

```ts
import {
  createTrajectoryLLMAsJudge,
  TRAJECTORY_ACCURACY_PROMP