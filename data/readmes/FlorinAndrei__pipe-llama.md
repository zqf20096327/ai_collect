# Pipe Llama

Put an LLM in your shell scripts and command-line pipelines.

Works just like any basic shell tool with `stdin` and `stdout`. Your prompt is the main argument; it is prefixed to `stdin` and together are sent to the model. The reply from the model becomes `stdout`. Dead simple.

Like `sed` or `awk`, but with LLMs.

If [Ollama](https://ollama.com/) is running locally, it will use it. Or tell the app to use another Ollama endpoint URL.

It will use the first model listed by Ollama. Or tell the app to use another model.

You can force the output to be just a single line per inference (one-line mode).

Thinking is disabled by default (where applicable), but can be enabled.

![logo](logo.png)

## Installation

Download the right binary for your platform, rename it as `pllama`, and put it anywhere in your $PATH. E.g. `~/bin/pllama`.

On macOS, read this if you get a pop-up saying the app won't run: https://support.apple.com/en-us/102445#openanyway

## Usage

```bash
# Warm-up mode, no prompt (just preload the default model then exit)
pllama

# Basic usage, your prompt is the main argument
echo "Hello world" | pllama "Translate to French:"

# No real input, only the prompt is used
echo | pllama "Hi!"

# Read the input from a file instead of stdin
pllama -i input.txt "What is this file?"

# Same, but force a terse, one-line output (one-line mode)
pllama -i input.txt -1 "What is this file?"

# Save output to file instead of stdout
pllama -i input.txt -o output.txt "Summarize this text:"

# Follow mode for continuous input (like tail -f), one-line mode
pllama -i /var/log/syslog -f -1 "Any serious issues in syslog? If not, say - no issues."

# Use a specific model
echo | pllama -m "llama3:8b" "Tell me a joke."

# Model pattern matching from a list (use first match)
echo | pllama -m "llama3*,mistral*,*" "Hi!"
```

## Configuration

### Command-Line Flags

| Flag | Description | Default |
|------|-------------|---------|
| `-h, --help` | Print help | |
| `-v, --version` | Print version | |
| `-e, --endpoint` | Ollama endpoint URL | `http://127.0.0.1:11434` |
| `-m, --model` | Model name/pattern (comma-separated) | First available |
| `-i, --input` | Input file | stdin |
| `-o, --output` | Output file | stdout |
| `-f, --follow` | Follow mode (continuous input) | false |
| `-bt, --batch-time` | Batch time interval in follow mode | 10s |
| `--max-retries` | Max retries per batch | 3 |
| `--retry-delay` | Initial retry delay | 2s |
| `--retry-backoff` | Retry backoff multiplier | 2.0 |
| `--max-consecutive-failures` | Circuit breaker threshold (0=unlimited) | 3 |
| `-d, --debug` | Enable debug output | false |
| `-1, --one-line` | Single-line response mode | false |
| `-t, --think` | Enable thinking mode (if model supports it) | false |

### Environment Variables

| Variable | Corresponds to |
|----------|---------------|
| `PLLAMA_ENDPOINT` | `--endpoint` |
| `PLLAMA_MODEL` | `--model` |
| `PLLAMA_BATCH_TIME` | `--batch-time` |
| `PLLAMA_MAX_RETRIES` | `--max-retries` |
| `PLLAMA_RETRY_DELAY` | `--retry-delay` |
| `PLLAMA_RETRY_BACKOFF` | `--retry-backoff` |
| `PLLAMA_MAX_CONSECUTIVE_FAILURES` | `--max-consecutive-failures` |

To make these settings permanent, export the variables from your shell configuration files, such as `~/.zshrc` or `~/.bashrc`, and reload your shell. Example:

```
export PLLAMA_ENDPOINT="http://some.other.system:11434"
export PLLAMA_MODEL="gemma3:4b"
```

Command-line flags take precedence over environment variables.

## Features

### Automatic Batching

Large inputs are automatically split into batches that fit the model's context window. Batch size is auto-detected from the model's context length. Each batch is processed with the same prompt, each as a separate inference event, until all input is consumed.

The app assumes a certain ratio of input bytes / token when making a batch. If that's too big, it will be adjusted down, a warning is printed out, and the batch is retried.

The adjusted values are saved in `~/.config/pllama/model_ratios.json`. You can purge that file if you wish, but it's generally useful.

### Follow Mode

With `-f`, the app continuously reads the input and processes it in batches, similar to `tail -f`. Useful for monitoring logs or streaming data.

### One-line Mode

With `-1`, the app forces the LLM to limit its output to a single line of text. This is done by prefixing your prompt with a system prompt that does just that.

### Retry Logic

Failed API calls are retried with exponential backoff. A circuit breaker exits the app after too many consecutive failures to prevent infinite loops.

### Model Selection

The `-m` flag accepts:
- Exact model names: `llama3:8b`
- Shell wildcards: `llama3*`, `mistral*`
- Comma-separated list (tries in order): `llama3:8b,mistral:7b,*`

The first match wins.

For most typical use cases of this app, you should prefer small and fast models. It is definitely possible to invoke large models with it (I've tested it with devstral-2:123b), but it may turn out other Ollama clients might be a better fit for that. You be the judge, I'm not telling you what to do.

### Warm-Up Mode

Running `pllama` without a prompt preloads the selected model into Ollama's memory, reducing latency for subsequent requests.

### Thinking

Thinking is disabled by default, but it can be enabled via `-t`.

Some models (e.g. gpt-oss) do not allow thinking to be disabled, but have different levels of thinking. In this case, the lowest level is used by default, and the highest is enabled with `-t`.

Some models do not support thinking at all (e.g. gemma3). Using `-t` will error out in this case.

## Requirements

- [Ollama](https://ollama.com/) running locally or accessible via network
- At least one model installed in Ollama

## Build From Source

```bash
git clone https://github.com/FlorinAndrei/pipe-llama.git
cd pipe-llama
make dev        # Build for current platform
# or
make build      # Build for all platforms
```

Binaries are placed in the `dist/` directory.

### Supported Platforms

- Linux (amd64, arm64)
- macOS (amd64, arm64)
- Windows (amd64, arm64)
