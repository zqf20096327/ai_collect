# `blunderbuss`

## The non-toxic LLM coding harness

> LLMs aren't partners or colleagues or advisors or underlings or any other kind of embodied mind. They're tools, but stochastic and unreliable ones. They're like a [blunderbuss](https://en.wikipedia.org/wiki/Blunderbuss) you pack with nails and glass and hope the scatter hits your target.

![king k rool with blunderbuss](https://blainehansen.me/assets/img/krool-blunderbuss.1ae5aedf.jpg)

`blunderbuss` is a coding harness that acknowledges LLMs are dangerous, not just because they often [take unexpected destructive action](https://airisk.mit.edu/ai-incident-tracker/incident-timeline), but because they're cognitively toxic. They [encourage cognitive debt](https://www.mdpi.com/2075-4698/15/1/6), [push you towards mediocrity](https://archive.is/OPObK), [encourage your delusions](https://www.science.org/doi/10.1126/science.aec8352), and [gaslight you when you push back](https://www.hbs.edu/ris/Publication%20Files/26-021_8db29bd1-04ed-4e98-86de-d286721afc7a.pdf).

If you want a full discussion of the philosophy and design of `blunderbuss`, read this blog post:

[Blunderbuss: the non-toxic LLM coding harness](https://unbreakinglab.org/project/blunderbuss)

## Main design decisions

- **Editor-oriented:** When using `blunderbuss` you write all instructions and config in `blunderbuss.local.md`, rather than typing them in a (buggy and temperamental) terminal app. This keeps you working in your strongest environment, the editor, engaged with the code, rather than falling asleep at the wheel as so many are now doing.
- **Allowlist permissioning:** `blunderbuss` only has access to the shell tools you have explicitly allowed, and can't access any files in any way other than those in the current working directory that aren't ignored by git. This means you won't be nagged every 30 seconds to approve some inscrutable glob of bash or python, and you don't have to stay glued to your terminal to keep the harness making progress. ["YOLO mode" has always been a way to gaslight us.](https://blog.glyph.im/2026/09/serious-ai-product.html#a-sandbox-that-actually-works) We don't have to choose between safety and convenience!
- **`git`-based checkpointing:** When `blunderbuss` begins a task it creates a cheap temporary work-in-progress `git` commit to ensure you can easily separate the changes it makes from those you already had in your working tree. Using `git` keeps the harness much simpler and ensures *every* change is reversible, even those made by shell commands. When `blunderbuss` finishes with your task you'll be asked whether to keep the changes, revert them, or try again, and in all cases the work-in-progress commit will be removed.
- **No walls of slop:** `blunderbuss` will just silently work on your task, and when the task is done you'll be met with a clean simple selector for what to do with the changes it's made, rather than an LLM generated summary. This protects you from the twin dangers of [sycophancy](https://www.science.org/doi/10.1126/science.aec8352) and [persuasion bombing](https://www.hbs.edu/ris/Publication%20Files/26-021_8db29bd1-04ed-4e98-86de-d286721afc7a.pdf), and from the fatigue that inevitably comes when reading the dreary pablum that LLMs are mathematically guaranteed to produce.
- **No extended conversation:** `blunderbuss` is intentionally designed in an "all or nothing" manner with no back-and-forth conversation with the LLM. You describe a task, it attempts that task, and you either keep what it did, throw it away and do it yourself, or have it try again with updated instructions. This helps you avoid such productivity and mind-killing traps as [futzing](https://blog.glyph.im/2025/08/futzing-fraction.html), [anthropomorphization](https://en.wikipedia.org/wiki/ELIZA_effect), and [automation bias](https://en.wikipedia.org/wiki/Automation_bias).
- **Vendor agnostic:** `blunderbuss` is built on the [`genai` crate](https://crates.io/crates/genai), and so allows you to use any provider/model you have access to. I'm quite convinced the big proprietary LLM vendors will eventually fail or crank up prices, and it's important to stay independent and able to switch at any time.

## Usage

Install using `cargo`:

```sh
cargo install blunderbuss
```

`blunderbuss` always reads `blunderbuss.local.md` to get its instructions (putting `*.local.*` in your `.gitignore` is probably a good idea), and is invoked as `blb`.

```sh
echo "Fix the tests" > blunderbuss.local.md
blb
# blunderbuss works for a while
# then a simple selection menu appears asking
> looks good
> nope revert
> try again
```

The raw transcript of the LLM chat will be output to `blunderbuss.output.local.yml`, in case you want to see what's happening under the hood.

### `blunderbuss.local.md` (task instructions)

`blunderbuss.local.md` is a markdown file with [yaml frontmatter](https://openmarkapp.com/blog/markdown-frontmatter-yaml) where you specify config for the task.

Here's a quick example, and below we'll go through each option.

```
---
model: gemini::gemini-3.5-flash-lite
tools:
- git diff
- git log
check: cargo check
ready: git diff > ~/Desktop/diff.txt && ${EDITOR} ~/Desktop/diff.txt
maxturns: 100
max_retry_times: 10
min_retry_delay: 5
max_retry_delay: 60
---

Here are the instructions that will be given to `blunderbuss`!

It's a full markdown file, so write whatever you please.
```
<!-- #
allow:
disallow:
-->

- **`model`:** Specifies the model to use for this task, with a provider specified before the `::`. Full reference for available providers [given at the end of this page](#model-resolution-and-auth). *must be specified either here in user level config*
- **`tools`:** List of commands to allow `blunderbuss` to use as tools. Both the prefix you give and the suffix given by `blunderbuss` will be *separately* passed through [shlex](https://docs.rs/shlex/latest/shlex/), meaning arbitrary bash constructs can't be used and your prefix can't be modified into any other command (such as could happen if `tree` could be modified to `tree_spy.sh`). Be careful with these tools! Remember that any subcommand of the prefix you pass is now something `blunderbuss` can call!
- **`check`:** A command that must pass in the exact form specified before the task will be considered successful. `blunderbuss` cannot append any arguments to it, and a new turn will kick off with the failing output if it doesn't pass. It is also made available as a tool `blunderbuss` can call at any time.
- **`ready`:** A command that will be called once the task has completed successfully. This is not made available as a tool.
- **`maxturns`:** The maximum number of ["conversation turns"](https://www.developersdigest.tech/glossary/max-turns) `blunderbuss` can go through before it is forced to stop. This is an error condition, and so will cause `blunderbuss`'s changes to be reverted. *default 100*
- **`max_retry_times`:** The maximum number of times to retry on recoverable errors to the LLM provider. (passed to [`backon::ExponentialBuilder::with_max_times`](https://docs.rs/backon/latest/backon/struct.ExponentialBuilder.html#method.with_max_times)) *default 10*
- **`min_retry_delay`:** The minimum delay when retrying on recoverable errors to the LLM provider. (passed to [`backon::ExponentialBuilder::with_min_delay`](https://docs.rs/backon/latest/backon/struct.ExponentialBuilder.html#method.with_min_delay)) *default 5*
- **`max_retry_delay`:** The minimum delay when retrying on recoverable errors to the LLM provider. (passed to [`backon::ExponentialBuilder::with_max_delay`](https://docs.rs/backon/latest/backon/struct.ExponentialBuilder.html#method.with_max_delay)) *default 60*

### `~/.blunderbuss.config.yml` (user level config)

```yaml
# user level default for `model`
default_model: gemini::gemini-3.5-flash-lite
# user level default for `maxturns`
default_maxturns: 100
# user level default for `max_retry_times`
default_max_retry_times: 10
# user level default for `min_retry_delay`
default_min_retry_delay: 5
# user level default for `max_retry_delay`
default_max_retry_delay: 30
# whatever tools you put here will be available in every task
tools:
- git status
- git diff
- tree
# all of these can also be supplied as env vars instead
api_keys:
  FIREWORKS_API_KEY: ...
  TOGETHER_API_KEY: ...
  GROQ_API_KEY: ...
  AIHUBMIX_API_KEY: ...
  KIMI_API_KEY: ...
  MIMO_API_KEY: ...
  MOONSHOT_API_KEY: ...
  NEBIUS_API_KEY: ...
  XAI_API_KEY: ...
  DEEPSEEK_API_KEY: ...
  MISTRAL_API_KEY: ...
  ZAI_API_KEY: ...
  BIGMODEL_API_KEY: ...
  ALIYUN_API_KEY: ...
  QWEN_CLOUD_API_KEY: ...
  BAIDU_API_KEY: ...
  COHERE_API_KEY: ...
  OMLX_API_KEY: ...
  VERTEX_API_KEY: ...
  GITHUB_TOKEN: ...
  OPENCODE_GO_API_KEY: ...
  BEDROCK_API_KEY: ...
  OPEN_ROUTER_API_KEY: ...
  ATLASCLOUD_API_KEY: ...
  REQUESTY_API_KEY: ...
  API_ROUTE_API_KEY: ...
  HEABSY_API_KEY: ...
  RUNCRATE_API_KEY: ...
  CLOUDGPU_API_KEY: ...
  CHEAPAIMODEL_API_KEY: ...
  STANDARDCOMPUTE_API_KEY: ...
  UBERLLM_API_KEY: ...
  MINIMAX_API_KEY: ...
  OPENAI_API_KEY: ...
  GEMINI_API_KEY: ...
  ANTHROPIC_API_KEY: ...
  OLLAMA_API_KEY: ...
```

### Model resolution and auth

The `genai` crate underlying `blunderbuss` allows lots of providers out of the box. You can read their full docs here:

https://github.com/jeremychone/rust-genai#model-to-adapter-resolution

Or look at the source code for the adapter definitions here:

https://github.com/jeremychone/rust-genai/blob/v0.7.5/src/adapter/adapter_kind.rs#L184

Here's a reference table for all the provider prefixes and their associated api key names, which you can provide either in `~/.blunderbuss.config.yml` or as an env var.

| provider prefix | api key name |
|---|---|
| `fireworks::` | `FIREWORKS_API_KEY` |
| `together::` | `TOGETHER_API_KEY` |
| `groq::` | `GROQ_API_KEY` |
| `aihubmix::` | `AIHUBMIX_API_KEY` |
| `kimi::` | `KIMI_API_KEY` |
| `mimo::` | `MIMO_API_KEY` |
| `moonshot::` | `MOONSHOT_API_KEY` |
| `nebius::` | `NEBIUS_API_KEY` |
| `xai::` | `XAI_API_KEY` |
| `deepseek::` | `DEEPSEEK_API_KEY` |
| `mistral::` | `MISTRAL_API_KEY` |
| `zai::` | `ZAI_API_KEY` |
| `bigmodel::` | `BIGMODEL_API_KEY` |
| `aliyun::` | `ALIYUN_API_KEY` |
| `qwen_cloud::` | `QWEN_CLOUD_API_KEY` |
| `baidu::` | `BAIDU_API_KEY` |
| `cohere::` | `COHERE_API_KEY` |
| `omlx::` | `OMLX_API_KEY` |
| `vertex::` | `VERTEX_API_KEY` |
| `github_copilot::` | `GITHUB_TOKEN` |
| `opencode_go::` | `OPENCODE_GO_API_KEY` |
| `bedrock_api::` | `BEDROCK_API_KEY` |
| `open_router::` | `OPEN_ROUTER_API_KEY` |
| `atlascloud::` | `ATLASCLOUD_API_KEY` |
| `requesty::` | `REQUESTY_API_KEY` |
| `api_route::` | `API_ROUTE_API_KEY` |
| `heabsy::` | `HEABSY_API_KEY` |
| `runcrate::` | `RUNCRATE_API_KEY` |
| `cloudgpu::` | `CLOUDGPU_API_KEY` |
| `cheapaimodel::` | `CHEAPAIMODEL_API_KEY` |
| `standardcompute::` | `STANDARDCOMPUTE_API_KEY` |
| `uberllm::` | `UBERLLM_API_KEY` |
| `minimax::` | `MINIMAX_API_KEY` |
| `openai::` | `OPENAI_API_KEY` |
| `openai_resp::` | `OPENAI_API_KEY` |
| `gemini::` | `GEMINI_API_KEY` |
| `gemini_ix::` | `GEMINI_API_KEY` |
| `anthropic::` | `ANTHROPIC_API_KEY` |
| `ollama_cloud::` | `OLLAMA_API_KEY` |
| `ollama::` | none |

The above table was generated with this short program.

```rust
fn main() {
  println!("| provider prefix | api key name |");
  println!("|---|---|");
  for kind in genai::adapter::AdapterKind::all() {
    if *kind == genai::adapter::AdapterKind::Ollama { continue; }
    println!("| `{}::` | `{}` |", kind.as_lower_str(), kind.default_key_env_name().unwrap());
  }
  println!("| `ollama::` | none |");
}
```

## Roadmap

- [ ] Add "init" behaviors to create configs if they don't exist.
- [ ] Add `allow` and `deny` to task config, to change file-level permissions rather than only using `.gitignore`.
- [ ] Create [eval suite](https://hamel.dev/blog/posts/evals-faq/) for security of built-in tools.
- [ ] Create "short range task" benchmark to determine how small of models can complete manageably sized tasks.
- [ ] Add ability to read web pages at explicitly allowed URLs.
- [ ] Windows and Mac compatibility.
- [ ] Other installation paths than `cargo`.
- [ ] Change `model` to allow a list of models that will be rotated through when rate limits are hit.
- [ ] Create "watch subcommand" that is built to babysit long-running processes such as CI jobs.
- [ ] MCP tool support

## `blunderbuss` is human-made

[![brainmade.org](https://img.shields.io/badge/brainmade.org-FFFFFF?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxZW0iIGhlaWdodD0iNzkiIHZpZXdCb3g9IjAgMCA2NyA3OSIgZmlsbD0ibm9uZSI%2BPHBhdGggZmlsbD0iIzAwMCIgZD0iTTUyLjYxMiA3OC43ODJIMjMuMzNhMi41NTkgMi41NTkgMCAwIDEtMi41Ni0yLjU1OHYtNy42NzdoLTcuOTczYTIuNTYgMi41NiAwIDAgMS0yLjU2LTIuNTZWNTUuMzE1bC04LjgyLTQuMzk3YTIuNTU5IDIuNTU5IDAgMCAxLS45ODYtMy43MWw5LjgwNy0xNC43MTR2LTQuMzVDMTAuMjQgMTIuNTk5IDIyLjg0MyAwIDM4LjM4OCAwIDUzLjkzMiAwIDY2LjUzNCAxMi42IDY2LjUzOCAyOC4xNDNjLS42MzIgMjcuODI0LTEwLjc2IDIzLjUxNi0xMS4xOCAzNC4wNDVsLS4xODcgMTQuMDM1YTIuNTkgMi41OSAwIDAgMS0uNzUgMS44MSAyLjU1IDIuNTUgMCAwIDEtMS44MDkuNzVabS0yNi43MjMtNS4xMTdoMjQuMTY0bC4yODYtMTQuNTQyYy0uMjYzLTYuNjU2IDExLjcxNi04LjI0MyAxMS4wOC0zMC43MzQtLjM1OC0xMi43MTMtMTAuMzEzLTIzLjI3MS0yMy4wMzEtMjMuMjcxLTEyLjcxOCAwLTIzLjAyOSAxMC4zMDctMjMuMDMyIDIzLjAyNXY1LjExN2MwIC41MDYtLjE1IDEtLjQzIDEuNDJsLTguNjMgMTIuOTQxIDcuNjQ1IDMuODJhMi41NTkgMi41NTkgMCAwIDEgMS40MTUgMi4yOTF2OS42OTdoNy45NzRhMi41NTkgMi41NTkgMCAwIDEgMi41NiAyLjU1OXY3LjY3N1oiLz48cGF0aCBmaWxsPSIjMDAwIiBkPSJNNDAuMzcyIDU4LjIyMlYzOC45MzRjLjExOCAwIC4yMzcuMDE4LjM1NS4wMTggOS43NjktLjAxMiAxNy4wNS05LjAxMiAxNS4wMjItMTguNTY3YTIuMzY2IDIuMzY2IDAgMCAwLTEuODIxLTEuODIyYy04LjEwNi0xLjczLTE2LjEyMSAzLjI5Mi0xOC4wOTggMTEuMzQxLS4wMjQtLjAyNC0uMDQzLS4wNS0uMDY2LS4wNzNhMTUuMzIzIDE1LjMyMyAwIDAgMC0xNC4wNi00LjE3IDIuMzY1IDIuMzY1IDAgMCAwLTEuODIxIDEuODJjLTIuMDI4IDkuNTU1IDUuMjUyIDE4LjU1NCAxNS4wMiAxOC41NjguMjM2IDAgLjQ5Mi0uMDI4LjczOC0uMDR2MTIuMjEzaDQuNzMxWm0yLjgzOS0zMi4xNDNhMTAuNjQ2IDEwLjY0NiAwIDAgMSA4LjEyNC0zLjEwNmMuMzUgNi4zNC00Ljg4OCAxMS41NzctMTEuMjI4IDExLjIzYTEwLjU4IDEwLjU4IDAgMCAxIDMuMTA0LTguMTI0Wk0yNy40MDMgMzguMTkzYTEwLjYwNyAxMC42MDcgMCAwIDEtMy4xMTgtOC4xMjNjNi4zNDQtLjM1OCAxMS41ODcgNC44ODYgMTEuMjI4IDExLjIzLTMuMDIzLjE2OS01Ljk3My0uOTYxLTguMTEtMy4xMDdaIi8%2BPC9zdmc%2B)](https://brainmade.org/)

I appreciate the irony of directly coding a new LLM coding harness rather than using a harness, but since the whole point of this project is that existing harnesses are unhealthy and unsafe, it felt like the right choice. Aside from using search tools like perplexity, I created `blunderbuss` without any LLM assistance.

Besides, I wanted to explore the actual mechanics of building an LLM harness in Rust, and I don't believe for a second anyone can actually learn much of anything if they they're just reading summaries. I learned a lot doing it this way!
<!-- TODO citation for people learning -->

In this spirit and since I want this project to remain legible and concise, I'm heavily biased against LLM-generated contributions. PRs that are clearly fully LLM generated won't be accepted, and especially if your [descriptive text](https://rfd.shared.oxide.computer/rfd/0576#_llms_as_writers) such as PR description or comments are LLM-generated you will be banned. Even if you use LLMs to help create a PR, it must be elegant, clear, and succinctly explained.
