# Orchard-TUI (BETA)

This is a **very basic** example of a terminal interface for [Orchard AI Agent](https://github.com/aerth/orchard).

Markdown is nicely "rendered" to the terminal window, this can be toggled with "shift+tab".

## Installation

Install easily with Go.

Since we use sqlite for persistence, you must have a C compiler. Compiling the sqlite part takes a while, be patient!

Otherwise, orchard-tui is a single executable. You can install it where you prefer.
Below are a few ways one might install to `~/bin/orchard-tui`

*Don't forget to clone a [toolbox](https://github.com/aerth/orchard-tools) so you have some basic tools to get started.*

### Compile

Install to ~/bin/ directory
```bash
GOBIN=~/bin go install -v github.com/aerth/orchard-tui@latest
~/bin/orchard-tui
```

Or, the right way. Clone and use `make`:

```bash
git clone https://github.com/aerth/orchard-tui
cd orchard-tui
make && make install
~/bin/orchard-tui
```

### Docker

Now available in container form, built by robots (CI).
Latest tools are included (`ORCHARD_TOOLS=/home/username/src/otools`)

To get self-signed LAN LLM to work properly, you may need some volume mounts. Set up an env-file with LLM_HOST, LLM_MODEL, and give it a try in a container to get familiar before installing everywhere!

```bash
docker run -it -v /etc/ssl/certs:/etc/ssl/certs:ro -v /etc/ca-certificates:/etc/ca-certificates:ro --network host --rm --env-file ~/.config/orchard/env ghcr.io/aerth/orchard-tui:latest
```

Example dockerized wrapper script might include `-v ./:/src` volume mount to make the current (host) directory as writable in the container. The `WORKDIR` is `/src`. 


## Usage

Minimally, `LLM_MODEL` and `LLM_HOST` is required. Without `ORCHARD_TOOLS`, a basic shell tool is the only tool available to the model. If `LLM_API_KEY` is present, it is added to Authentication header for each llm request.

When first opened, we do a startup test to make sure we can generate a short greeting. Press ENTER to begin the chat interface, where you can type your demands into the text area.

Use `-h` to show command-line flag usage, and from the chat you can use `/help` to show slash commands and key bindings.

Attach images to the conversation with `[./path/to/image.png]` with path in brackets.

To limit the tools available easily, run with `-tool [name]` flag.

To require confirmation on a certain tool, run with `--require-confirm [name]`. Both of these flags can be repeated or given a comma-separated-list of tool names.

### Configuration 

Consider creating a `~/.config/orchard/env` file, which is loaded if it exists (unless `-e none` command line).

Currently, the host and model are not easily changed at runtime. In the future, we can consider secret storage for API keys and a list of provider/model combos to easily switch between messages. Until then, with sqlite database, restarting the program resumes the conversation fully.

The orchard env file does not override variables that are already set..

Can use `-e none` or `-e /path/to/other/env-file` to **not** use the default location.

```bash
# env config for orchard (https://github.com/aerth/orchard)
LLM_HOST='https://ollama.home.arpa'
LLM_MODEL=gemma4:12b
LLM_API_KEY=abcdef123456
LLM_THINK=low
# if ORCHARD_TOOLS is used and this directory does not exist, the program will not start.
#ORCHARD_TOOLS=~/src/otools
# if ORCHARD_DB is used, persistence is activated.
#ORCHARD_DB=~/.local/state/orchard/orchard.db
```

You can drop this snippet into ~/.config/orchard/env for reference:

```bash
## orchard paths (disabled if omitted)
#ORCHARD_DB=~/.local/state/orchard/orchard.db
#ORCHARD_TOOLS=~/src/otools
## llama.cpp
#LLM_HOST=http://127.0.0.1:9931 
#LLM_API_KEY=foo
## ollama
#LLM_HOST=http://127.0.0.1:11434
## nvidia example
#LLM_HOST=https://integrate.api.nvidia.com 
#LLM_API_KEY=foo
#LLM_MODEL=nvidia/nemotron-3.5-lightning-30b-a3b
#LLM_MODEL=nvidia/nemotron-3.5-super-vl-120b-a12b
#LLM_MODEL=nvidia/nemotron-3.5-bolt-e4b 
## openai example
#LLM_HOST=https://api.openai.com/v1/chat/completions
#LLM_API_KEY=foo
#LLM_MODEL=gpt-6-luna
#LLM_MODEL=gpt-6-sol
```

### llama.cpp example

```bash
export LLM_MODEL=gemma-4-E2B-it-Q4_K_M LLM_HOST=http://127.0.0.1:9931/v1/chat/completions LLM_API_KEY=keyhere
export ORCHARD_DB=/tmp/orchard.sqlite
cd path/to/some/project
orchard-tui
```

### ollama example

```bash
export LLM_MODEL=gemma4:12b LLM_HOST=http://127.0.0.1:11434/v1/chat/completions
export ORCHARD_DB=/tmp/orchard.sqlite
cd path/to/some/project
# specifying thread allows grouping multi-directory conversations in one thread.
orchard-tui
```

## Persistence (conversation history)

When using a database for persistent conversations, we use `$PWD` as thread ID (as if thread flag was `orchard-tui -thread $PWD`) to automatically create a "thread ID" for each project directory. To specify the conversation thread ID, use the `-thread` flag. If thread argument is not a UUID, then it is hashed. This allows for words such as `-thread foo` to make it easy to generate new deterministic thread ID.

From the command-line you can `--delete-thread confirm` to delete the thread from the database. 
In the chat, you can `/clear` for the same.

Images are not persisted to database.

## Logs

See `/tmp/orchard.json.log` and run with `-v` for more logs.

## Dynamic Tools

This program reads ORCHARD_TOOLS env to create a dynamic toolbox.

When used, this *adds* to the default tools (`run_bash`). To use **only** the toolboxes _without_ the builtin bash tool, add `--no-bash` flag when opening orchard-tui, or whitelist tools using `-tool` flag.

For a nice starter pack of tools to use, try [orchard-tools](https://github.com/aerth/orchard-tools) toolbox.

```
git clone https://github.com/aerth/orchard-tools ~/src/otools
ORCHARD_TOOLS=~/src/otools orchard-tui -db /tmp/orchard.db
```

Refer to the *orchard* and *orchard-tools* documentation for more information on dynamic tools.

## Copyright

Copyright (c) 2026 aerth

See [LICENSE](./LICENSE) file.
