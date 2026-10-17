---
title: AutoQuizzer
emoji: 🧑‍🏫
colorFrom: purple
colorTo: blue
sdk: gradio
sdk_version: 5.35.0
app_file: app.py
header: mini
pinned: true
short_description: Generate a quiz, play or let 🦙 LLM play
models: [openai/gpt-oss-20b]
---

# 🧑‍🏫 AutoQuizzer &nbsp; [![HF Space](https://img.shields.io/badge/%F0%9F%A4%97-Live%20demo-blue.svg)](https://huggingface.co/spaces/deepset/autoquizzer)

Generates a quiz from a URL. You can play the quiz, or let the LLM play it.

Built using: [🏗️ Haystack](https://haystack.deepset.ai/) • 🦙 GPT-OSS 20B • ⚡ Groq

> ℹ️ This project originally used 🦙 Llama 3 8B Instruct (later `llama-3.1-8b-instant`).
> It moved to `openai/gpt-oss-20b` when Groq decommissioned the Llama model.

<!--- Include in Info tab -->

## How does it work?

🎬 [**Project walkthrough video**](https://www.youtube.com/watch?v=C1oJ1ArYYZA)

![AutoQuizzer](autoquizzer.png)

- **Quiz generation Pipeline**: downloads HTML content from the URL, extracts the text and passes it to the LLM to generate a quiz in JSON format.
- You can play the quiz and get a score.
- You can let the LLM play the quiz:
  - **closed book answer Pipeline**: the LLM is given only the general quiz topic and questions. It can answer the questions based on its parametric knowledge and reasoning abilities.
  - **Web RAG answer Pipeline**: for each question, a Google search is performed and the top 3 snippets are included in the prompt for the LLM.

## How to run it locally?

- Clone the repo: `git clone https://github.com/anakin87/autoquizzer`
- Install: `cd autoquizzer && pip install -r requirements.txt`
- Export two environment variables:
  - `GROQ_API_KEY`: API key for the [Groq API](https://groq.com/), used to serve `openai/gpt-oss-20b`.
  - `SERPERDEV_API_KEY`: API key for the [SerperDev API](https://serper.dev/), used to fetch search results.
- Run the webapp: `gradio app.py`

## Customization and potential improvements
- To not exceed the rate limits of Groq's free API, we truncate the text extracted from the URL to 4000 characters. This means that the generated quiz focuses on the beginning of the text. You can increase/remove this limit, taking into account the maximum context length of the model.
- We are using the `OpenAIChatGenerator` to query `openai/gpt-oss-20b` on Groq. You can use an OpenAI model with the same generator. You can also use a different generator ([Haystack generators](https://docs.haystack.deepset.ai/docs/generators)).
- In the quiz generation pipeline, we ask the model to generate a JSON. GPT-OSS 20B usually works. You can also create a more robust JSON generation pipeline, as shown in this tutorial: [Generating Structured Output with Loop-Based Auto-Correction](https://haystack.deepset.ai/tutorials/28_structured_output_with_loop).
- GPT-OSS is a reasoning model. We set `reasoning_effort="low"` to keep it brief (Groq does not accept `"none"` for this model). Since reasoning tokens count against `max_tokens`, the answer pipelines need headroom well above the single letter they return.
