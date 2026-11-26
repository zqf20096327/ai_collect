# OBDTrace

**An agentic OBD-II reader with a built-in data logger.** OBDTrace reads fault
codes, freeze frames, readiness and live sensors from ELM327-compatible
Bluetooth, serial and TCP adapters. It records every drive into a local session
history and exposes it all over MCP, so an AI agent can read the car, query
past recordings and compare behaviour before and after a repair.

- **Data logger:** continuous recording of live PIDs (including narrowband and
  wideband oxygen sensors and commanded lambda), DTC events and adapter state
  into a local SQLite history, browsable in the app and exportable.
- **Agent-ready:** an MCP server with diagnostic and history tools (compact
  JSON time series, bucketed summaries, aligned multi-sensor tables,
  similar-condition search). MCP is the
  only agent interface; `OBDTRACE_READ_ONLY=1` limits a server to reads, and
  clearing codes needs explicit opt-in and human confirmation.
- **Local first:** one Rust binary with a browser UI. It works without an AI
  client and makes no AI-service or cloud calls itself. MIT licensed.

## Install and try the demo

**Linux x86-64:** release binaries are tested against the built-in simulator;
real-adapter support is best-effort. Run OBDTrace as a single-user desktop app
and do not share diagnostic exports. See the [security policy](SECURITY.md) for
known limitations and private reporting.

Use [GitHub Releases](https://github.com/Avokid/obdtrace/releases) for published
binary downloads. If no suitable release is available, [build from source](#build-from-source).

1. The first binary release targets **Linux x86-64**. Verify the archive's
   SHA-256 against `SHA256SUMS` and see the [Linux dependencies](docs/linux-dependencies.md).
   Windows x64 and Apple silicon macOS builds are tested in CI, not released.
2. Extract it to a permanent folder. Run `./obdtrace demo` on Linux or macOS,
   or `.\obdtrace.exe demo` in PowerShell. No adapter or Rust installation is
   needed for the demo. Stop the demo before connecting a real vehicle.
3. Run `./obdtrace app` (Windows: `.\obdtrace.exe app`) to open the setup UI.
   The command `obdtrace doctor` checks the MCP handshake without an adapter.

See the [installation and migration guide](docs/install.md) for platform
requirements, updates, and how to bring history and MCP settings over from
the previous `obd2-mcp` name.

In current source builds, run `obdtrace app` to open an authenticated browser
tab. With `--no-browser`, open the private HTML file named in the terminal;
do not share it. The bare loopback URL does not grant access.
The local UI includes OS-specific Bluetooth instructions,
manual connection targets and AI-client setup. A running app and MCP clients
share one adapter owner. Set `OBDTRACE_PORT` if needed.

## Connect an MCP client

OBDTrace is an ordinary stdio MCP server: any MCP client can start it with the
absolute path to the executable and the single argument `mcp`. On the
**Connect** page, **Set up AI assistant** shows a ready configuration snippet
(VS Code, Claude Desktop) or command (Claude Code) to copy into your client.
OBDTrace never edits another application's configuration. Add
`"OBDTRACE_READ_ONLY": "1"` to the server's `env` to expose only diagnostic and
history reads. Test the setup by asking the agent to call `connection_status`.

## Adapter connection targets

| Adapter | Connection |
| --- | --- |
| Bluetooth LE (Linux, macOS, Windows) | Use **Search adapters** and select the adapter. Unnamed BLE devices are shown by ID. You can also enter `ble:<id>` or `ble:<name>`, or `ble:<MAC>` where the OS exposes a MAC. Known and generic GATT channels are tried and checked for an ELM identification reply. Try without OS pairing first; pair if your adapter requires it. |
| Classic Bluetooth SPP (Linux) | Pair in the OS. The search also lists paired devices BlueZ identifies as SPP. Alternatively, enter `rfcomm:AA:BB:CC:DD:EE:FF` (channel 1), or append `@<channel>` if the adapter uses another channel. No `/dev/rfcomm` binding is needed for a direct connection. An existing `serial:/dev/rfcomm0` still works. |
| Classic Bluetooth SPP (Windows/macOS) | Pair in the OS and choose its outgoing serial port, e.g. `serial:COM3` or `serial:/dev/cu.OBDII`, if the OS exposes one. A port can be entered manually even if it is not shown in the list. Use `@<baud>` to override the serial default of 38400 if needed. |
| Wi-Fi or USB | Enter `tcp:<host>:<port>` or choose the USB serial port. |

Use the adapter's own pairing instructions and close any other app currently
using it. The adapter must expose an ELM-compatible command interface; devices
that require a proprietary app, authentication or protocol are not guaranteed
to work.

Every connection is recorded locally. DTC observations, code-clearing events and
externally supplied AI assessments remain searchable alongside the sensor data.
The browser UI and AI prompts are available in English, Finnish, Spanish,
German, French and Brazilian Portuguese. The browser language is used by
default; the language selector remembers your choice. Translations and the
i18next browser runtime (MIT, pinned at 27.2.6) are embedded in the binary, so
no network or Node.js runtime is needed. Edit the catalogs in
[`assets/locales`](assets/locales) and the long history prompts in
[`assets/prompts`](assets/prompts).

**[MCP agent guide](docs/mcp.md)** · **[Session history and privacy](docs/history.md)** · **[History and saving playbook](docs/mcp-history.md)**

VINs are masked in public outputs. Keep the local database and `vehicle.key`
private. No automatic history deletion or telemetry. Generic OBD-II is not a
complete vehicle inspection, and adapter/OS hardware compatibility still requires
real-device verification. Interact only with the car parked.

## Build from source

Use Rust 1.89 or newer. On Debian/Ubuntu install the build dependencies
`pkg-config`, `libdbus-1-dev` and `libudev-dev` first. macOS needs the Xcode
Command Line Tools; Windows with the MSVC Rust toolchain needs the Visual C++
build tools.

```bash
git clone https://github.com/Avokid/obdtrace.git
cd obdtrace
cargo build --release --locked
./target/release/obdtrace demo
```

Stop the demo before connecting a real vehicle:

```bash
./target/release/obdtrace app
```

On Windows, use `.\target\release\obdtrace.exe` instead.

Contributors: see [AGENTS.md](AGENTS.md) for the development workflow.
Maintainers: see the [release checklist](docs/releasing.md).
