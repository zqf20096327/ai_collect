---
languages:
- cpp
- csharp
- go
- python
- rust
- javascript
products:
- windows
description: "Samples demonstrating Remote Desktop Protocol (RDP) Dynamic Virtual Channel (DVC) plugins across multiple languages and activation models."
urlFragment: rdp-dvc-plugin-samples
page_type: sample
name: "RDP DVC plugin samples"
---

# RDP DVC Plugin Samples

Samples for **Remote Desktop Protocol (RDP) Dynamic Virtual Channels (DVC)** across multiple languages and activation models. Each sample is self-contained: build scripts, protocol, client plugin, and server live together.

These samples model the “two cooperating parts” for RDP virtual channels: a **client-side module** loaded by the RDP client, and a **server-side module** running in the remote session; the RDP transport multiplexes multiple virtual channels alongside display/input traffic.

## Contents

| File/folder | Description |
|---|---|
| [`Simple/`](https://github.com/microsoft/rdp-dvc-plugin-samples/tree/main/Simple) | Minimal ping/echo protocol samples. |
| [`Advanced/`](https://github.com/microsoft/rdp-dvc-plugin-samples/tree/main/Advanced) | Full-featured samples with session lifecycle and Protocol Buffers. |
| [`BUILD_MATRIX.md`](https://github.com/microsoft/rdp-dvc-plugin-samples/blob/main/BUILD_MATRIX.md) | Per-language build requirements matrix. |
| [`TROUBLESHOOTING.md`](https://github.com/microsoft/rdp-dvc-plugin-samples/blob/main/TROUBLESHOOTING.md) | Troubleshooting guide. |
| `README.md` | This README file. |

How to choose:
- New to DVCs: start with **Simple**.
- Need multiple activation models or protobuf-style framing: pick **Advanced**.
- Language-specific work: open the README under that language folder.


## Running the sample
1) Pick a language under Simple/ or Advanced/ and open its README.
2) Register the client plugin on the RDP client machine (per-user or per-machine as noted).
3) Connect with an RDP client; the channel opens automatically.
4) Start the server inside an RDP session on the remote machine.

At a high level, every sample follows the same handshake: register/enable the client plugin on the **client machine** (the machine running the RDP client), establish an RDP connection, and then run the server application inside the **remote session** so it can open a DVC endpoint and exchange data. That separation (client plugin vs server app) is the core virtual-channel model.


## Client plugin activation modes
- **LocalServer COM (out-of-proc, recommended)**
  - AddIns key points to CLSID; CLSID\LocalServer32 points to the EXE.
  - You can launch it before the RDP client or let COM activate it via CLSID/`-Embedding`.
  - Register **before** starting the RDP client; isolates crashes away from the RDP client.
- **In-process COM (DLL)**
  - AddIns key points to CLSID; CLSID\InprocServer32 points to the DLL.
  - Runs inside the RDP client process; instability can take down the client. Use only when in-proc is required.
- **LoadLibrary / VirtualChannelGetInstance**
  - AddIns key points directly to a DLL; the RDP client loads it and calls the export.
  - Minimal registration but same in-proc stability trade-offs as COM DLL.

## DVC session and channel lifecycle (high level)
- **Server side (in-session):** open the DVC for the active session only. Advanced samples show checking session state (`WTSQuerySessionInformation`) and subscribing to logon/disconnect (`WTSRegisterSessionNotificationEx`) so you reopen on reconnect.
- **Notification flow:** subscribe → on logon/unlock, find active SessionId → open channel (`WTSVirtualChannelOpenEx`) → on disconnect/logoff, close and wait for the next active session.
- **Client side (RDP client plugin):** `IWTSPlugin::Initialize` → `CreateListener` → `IWTSListenerCallback::OnNewChannelConnection` → per-connection `IWTSVirtualChannelCallback` handles data.
- **Data plane:** server uses WTS APIs (`WTSVirtualChannelRead/Write`) or file-handle mode; client handles `OnDataReceived` and responds via `IWTSVirtualChannel::Write`.

## Next steps

- [Terminal Services Virtual Channels](https://learn.microsoft.com/windows/win32/termserv/terminal-services-virtual-channels)
- [DVC plug-in registration](https://learn.microsoft.com/windows/win32/termserv/dvc-plug-in-registration)
- [IWTSPlugin interface](https://learn.microsoft.com/windows/win32/api/tsvirtualchannels/nn-tsvirtualchannels-iwtsplugin)
- Simple samples: [C++](https://github.com/microsoft/rdp-dvc-plugin-samples/blob/main/Simple/cpp/README.md), [.NET 8](https://github.com/microsoft/rdp-dvc-plugin-samples/blob/main/Simple/dotnet/README.md), [.NET Framework](https://github.com/microsoft/rdp-dvc-plugin-samples/blob/main/Simple/netfx/README.md), [Rust](https://github.com/microsoft/rdp-dvc-plugin-samples/blob/main/Simple/rust/README.md), [Go](https://github.com/microsoft/rdp-dvc-plugin-samples/blob/main/Simple/go/README.md), [Python](https://github.com/microsoft/rdp-dvc-plugin-samples/blob/main/Simple/python/README.md), [Electron](https://github.com/microsoft/rdp-dvc-plugin-samples/blob/main/Simple/electron/README.md)
- Advanced samples: [C++](https://github.com/microsoft/rdp-dvc-plugin-samples/blob/main/Advanced/cpp/README.md), [.NET 8](https://github.com/microsoft/rdp-dvc-plugin-samples/blob/main/Advanced/dotnet/README.md)
