# MSXCODE

`msxcode` is an AI assistant client for MSX computers. It runs as an
MSX-DOS 2 executable, connects to OpenAI-compatible chat completion APIs over
TCP/IP UNAPI, and presents the conversation through an 85-column graphical
text interface (screen 7).

The application is written in C and Z80 assembly and targets MSX2, MSX2+, MSX turbo R machines, and MSX FPGA Cores.

![](.images/msxcode_001.png) ![](.images/msxcode_002.png)
> Usage example with the `Minimax-M3` model.

## Features

- OpenAI-compatible `/v1/chat/completions` client
- HTTP (HTTPS not fully not implemented yet) through compatible TCP/IP UNAPI implementations
- Optional bearer-token authentication
- Multi-turn conversation history stored in memory mapper segments
- Function calling with read-only MSX tools:
  - List files and directories
  - Read text and binary files
  - Get the MSX date and time
  - Get basic system information
- Session export to disk
- Screen 7 interface rendered by `msx2ansi`
- UTF-8 response conversion for the MSX character set

## Requirements

### MSX

- MSX2, MSX2+ or MSX turbo R
- MSX-DOS 2.x or newer
- V9938 or V9958 VDP
- Memory mapper
- TCP/IP UNAPI implementation with active TCP and DNS support

In the future when supported, HTTPS, additionally will require a TCP/IP UNAPI 1.1 implementation that advertises
TLS support. TLS is handled by the network implementation, not by the Z80.
Adapters without this capability will only use `http://` endpoints.

## Configuration

Place `MSXCODE.INI` in the same folder than `MSXCODE.COM`.

The filename is derived from the executable name, so renaming the executable also changes the expected INI filename.

```ini
API_URL=http://api.example.com/v1
API_KEY=your-api-key
LLM_MODEL=your-model-name
```

`API_URL` is the API base URL. `msxcode` appends `/chat/completions`
automatically. A trailing slash is optional.

`API_KEY` is optional. Leave it empty when the endpoint does not require
bearer authentication:

```ini
API_KEY=
```

### Example configuration for Ollama local server

```ini
API_URL=http://192.168.1.10:11434/v1
API_KEY=
LLM_MODEL=qwen3.5:4b
```

> Change the IP address to match your local server.

> Change the model name to match the available models on your server (`ollama ls`).

### Configuration notes

Different OpenAI-compatible providers support different model names and
optional request parameters. Consult the documentation for the selected
provider and model.

> Do not distribute the `.INI` file containing a real API key.

## Running

From MSX-DOS 2:

```text
A:\> MSXCODE
```

The main controls are:

| Key | Action |
| --- | --- |
| Enter | Send the message |
| Shift+Enter | Insert a new line |
| Arrow keys | Move the cursor |
| Ctrl+Left / Ctrl+Right | Move by word |
| Backspace / Delete | Delete a character |
| Ctrl+Backspace / Ctrl+Delete | Delete a word |
| Esc | Exit |

Available slash commands:

| Command | Action |
| --- | --- |
| `/help` | Show the help screen |
| `/new` | Start a new conversation |
| `/export` | Export the current conversation to disk |
| `/exit` | Exit the application |

## Tool Access

Models with function-calling support can ask `msxcode` to list directories,
read files and inspect basic system information. These tools are read-only,
but file contents are sent to the configured API endpoint as part of the
conversation. Use trusted endpoints and avoid exposing sensitive files.

| Tool | Description | Arguments |
| --- | --- | --- |
| `listDir` | List an MSX-DOS directory. Defaults to the root of drive A. | Optional `path` |
| `readFile` | Read a byte range as text or as a hexadecimal dump. | Required `path`, `offset` and `length`; optional `format` (`auto`, `text` or `hex`) |
| `getDateTime` | Get the current MSX system date and time. | None |
| `getSysInfo` | Get basic machine, keyboard, MSX-DOS and drive information. | None |

## Build host (just for compiling your own executable)

- GNU Make
- Docker
- Git with submodule support

The build uses SDCC 4.5.0 and `hex2bin` through the `nataliapc/sdcc:4.5.0` Docker image.

### Project Layout

```text
src/                   Application and project library sources
includes/              Public and internal C headers
contrib/               Bundled networking and display libraries
externals/             Git submodules for MSX-DOS and console support
res/                   Help and graphical resources
emulation/             openMSX boot scripts
dsk/                   Local runtime disk directory and build output
```

### Building

Clone the repository and its submodules:

```sh
git clone --recurse-submodules https://github.com/nataliapc/msxcode.git
cd msxcode
```

Build the application:

```sh
mkdir -p dsk
make
```

The resulting executable is copied to:

```text
dsk/msxcode.com
```

If the repository was cloned without submodules, initialize them before
building:

```sh
git submodule update --init --recursive
```

After modifying a source under `contrib/`, rebuild it explicitly:

```sh
make cleancontrib
make
```

### openMSX

The Makefile includes a `make test` target that mounts `dsk/` as drive A and
starts a turbo R with the `debugdevice` and `unapinet` extensions.

`unapinet` is not part of a standard openMSX v0.21 installation. HTTP testing also
requires a network implementation that advertises [TCP/IP UNAPI support](https://github.com/antxiko/openMSXnet).

## Acknowledgements

This project builds on software and specifications created by members of the
MSX community. Special thanks to:

- [Oduvaldo Pavan Junior](https://github.com/ducasp) for the SDCC version of
  `msx2ansi`, the HGET library and its TCP/IP UNAPI work.
- Tobias Keizer for the original `ANSI-DRV.BIN` rendering engine on which
  `msx2ansi` is based.
- Piter Punk for fixes and extensions contributed to `msx2ansi`.
- [Nestor Soriano (Konamiman)](https://github.com/Konamiman) for the original
  HGET utility, MSX-UNAPI specifications and related networking code.
- [Antxiko Gorjon](https://github.com/antxiko) for
  [openMSXnet](https://github.com/antxiko/openMSXnet), the openMSX fork and
  UNAPI bridge used during development and testing.
- The [openMSX](https://openmsx.org/) developers for the emulator on which
  openMSXnet is built.

## License

This project is distributed under the GNU General Public License version 2.
See [LICENSE](LICENSE).

Copyright (c) 2025 NataliaPC.

## More stars!

Please give us a star on [GitHub](https://github.com/nataliapc/mcp-openmsx) if you like this project.

## Star History

[![Star History Chart](https://api.star-history.com/chart?repos=nataliapc/msxcode&type=date&legend=top-left&theme=dark&sealed_token=oEDq0R9aoma8xNR3jECh7FtQpRrY9eT1sYOmTg9pGx5DvUrsRcfDYXIPG4LkY6VtmduBqAFAm7qKTVqPUyAi8lMw1F2V9pbxyHY3nm9z5drPcCZ-B77tJ8I-5RadKYNAeY_AlqQKIMo4RQar6-h20TqHqGD1-N6vObcMRH-iG-W4nF9PdqmU_iN_k2YN)](https://www.star-history.com/?repos=nataliapc%2Fmsxcode&type=date&legend=top-left)

---