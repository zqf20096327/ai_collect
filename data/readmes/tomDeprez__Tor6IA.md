<p align="center"><img src="docs/banner.svg" alt="Tor6IA: share your computer, use bigger AI models" width="100%"></p>

# Tor6IA: share your computer, use bigger AI models

<p align="center">
  <a href="https://github.com/tomDeprez/Tor6IA/actions/workflows/ci.yml"><img src="https://github.com/tomDeprez/Tor6IA/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://github.com/tomDeprez/Tor6IA/releases/latest"><img src="https://img.shields.io/github/v/release/tomDeprez/Tor6IA" alt="Latest release"></a>
  <a href="https://github.com/tomDeprez/Tor6IA/releases"><img src="https://img.shields.io/github/downloads/tomDeprez/Tor6IA/total" alt="Downloads"></a>
  <a href="https://github.com/tomDeprez/Tor6IA/stargazers"><img src="https://img.shields.io/github/stars/tomDeprez/Tor6IA" alt="Stars"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="License: MIT"></a>
</p>

**Tor6IA is a peer-to-peer network for running open LLMs.** Your machine runs a model for other people and earns credits. You spend those credits on the models other machines run, including models too large for your own computer.

It is simple: one file, no account, nothing to configure. [Français](README.fr.md)

<p align="center">
  <a href="https://github.com/tomDeprez/Tor6IA/releases/latest/download/tor6ia-windows-amd64.exe"><img src="https://img.shields.io/badge/Download_for_Windows-tor6ia.exe-1c7a4c?style=for-the-badge" alt="Download for Windows"></a>
  &nbsp;
  <a href="#linux-and-macos"><img src="https://img.shields.io/badge/Linux_and_macOS-one_command-1f5fd1?style=for-the-badge" alt="Linux and macOS: one command"></a>
</p>

<p align="center"><img src="docs/screenshot.png" alt="The Tor6IA interface: connection state, credits, models and chat" width="900"></p>

## Three steps

| | |
|---|---|
| **1. Install** | Double-click one file on Windows, or paste one command on Linux and macOS. Ollama and the model are installed for you. |
| **2. Your machine shares** | The big button turns green: you are connected. When someone uses your machine it turns blue, and you earn credits. |
| **3. Use any model** | Chat in the interface, or point any OpenAI client at `http://localhost:7606/v1`. Your credits pay for models bigger than your machine. |

## Install

### Windows

**[Download tor6ia-windows-amd64.exe](https://github.com/tomDeprez/Tor6IA/releases/latest/download/tor6ia-windows-amd64.exe)** and double-click it.

It installs itself, installs Ollama, picks the model that fits your machine, downloads it and opens the interface. No admin rights needed.

Windows shows "Windows protected your PC" because the file is not signed yet: click **More info**, then **Run anyway**. Or use PowerShell, which shows no warning:

```powershell
irm https://raw.githubusercontent.com/tomDeprez/Tor6IA/main/install.ps1 | iex
```

### Linux and macOS

```sh
curl -fsSL https://raw.githubusercontent.com/tomDeprez/Tor6IA/main/install.sh | sh
```

The interface opens on `http://localhost:7606`. Every release runs this command on clean Linux and macOS machines and asks the model a question.

## Why

Running a large language model at home needs a graphics card most people do not have. Tor6IA pools machines:

- **Fair.** No credit is ever created. You earn exactly what another person pays for the work done on your machine.
- **Verifiable.** The credit ledger is public, hash-chained and signed, like a blockchain. Every node audits it.
- **Private.** Prompts and answers are encrypted end to end. The coordinator knows who asks but cannot read. The machine that answers reads the prompt but does not know who sent it.
- **No account.** Your identity is a key created on your machine. No e-mail, no password.
- **Works with your tools.** OpenAI-compatible API on `http://localhost:7606/v1`.

## The interface

The large button at the top says what your machine is doing. Click it to pause or resume sharing.

| Colour | State |
|---|---|
| Green | Connected, waiting for a job |
| Blue | Computing for someone: you earn credits |
| Orange | Installing or connecting |
| Grey | Paused, or coordinator unreachable |
| Red | Problem, or alert: the ledger failed its audit |

The model list shows how many machines offer each model, its price, and how many tokens your balance buys. A machine shares one model at a time. **Choose** switches to another one. It always asks first and says what it implies: download size, speed on your hardware, what you earn, and whether to delete the old model.

**Shared ✓** stops sharing a model, and can delete its files to free the disk. A download in progress can be cancelled. **Uninstall Tor6IA…** at the bottom removes everything: the machine leaves the network, the shared models and the program are deleted. When a machine pauses or leaves, the others see at once that its models lost a machine.

**Updates.** When a new release is published, the program shows what changed and updates itself in one click. A build from source never asks.

## Models

| Model | Price | Runs fast on | Runs slowly on |
|---|---|---|---|
| Llama 3.2 3B | ×1 | any PC with 6 GB of memory | |
| Gemma 4 E2B | ×2 | any PC with 10 GB of memory | |
| Gemma 4 12B | ×4 | 10 GB graphics card | processor with 14 GB of memory |
| Gemma 4 26B | ×6 | 22 GB graphics card | processor with 31 GB of memory |
| Gemma 4 31B | ×10 | 24 GB graphics card | processor with 33 GB of memory |

Gemma 4 26B holds 26 billion parameters and uses 4 billion per token: it answers much faster than its size suggests.

A node starts with the heaviest model it runs fast. A machine never loads a model it has no memory for, and computing uses half of its processors, so it stays usable. Only NVIDIA cards and Apple Silicon are detected automatically.

A model with no machine shows "waiting for a machine". It becomes available the moment someone with enough hardware shares it.

## One model across several machines

A model too big for one machine can be shared by a group. The model is cut into blocks of layers; each machine of the group holds the blocks its memory allows, and yours offers the model to the network and is paid for it.

A model is cut into blocks of about 1 GB, the same way on every machine. Gemma 4 12B has 6 blocks, for example.

1. On each machine of the group, open Tor6IA and click **Hold blocks of a model…**. Choose the model: the interface reads its plan without downloading it, says how many blocks it has and how many your machine can hold. Choose the blocks, for example 2 to 3. The machine downloads those blocks only, loads them, and shows a line to give to the group, like `192.168.1.20:50052=2-3#5f1c…`. The end of the line is a secret: whoever has the line can make this machine compute, nobody else can.
2. On the machine that holds the conversation, click **Spread a model over several machines…**, choose the model and paste one line per machine. The blocks must make the whole model, each block once: a group with a hole is refused, and the interface says which blocks nobody holds. This machine needs the whole model file.

The block server runs locked in: it cannot read your files, connect anywhere or start a program.

<p align="center"><img src="docs/hold.png" alt="The Tor6IA window to hold blocks of a model: 16 blocks in Gemma 4 31B, 8 advised for this machine, the size to download and the memory used" width="900"></p>

<p align="center"><img src="docs/split.png" alt="The Tor6IA interface showing Gemma 4 26B split in three blocks, with the machine and the layers of each block" width="900"></p>

The interface then shows the split: one bar for the model, one segment per block, and which machine holds which layers. If a machine of the group leaves, the model stops being split and the interface says so; your machine keeps offering it alone when it has the memory.

**Between people you chose.** What passes between the machines of a group is encrypted, and a machine obeys only who has its line. With a group set up by hand the machines must be able to reach each other: same network, a VPN, or an open port.

### The network forms the groups

Nobody has to exchange lines. Each machine says what it does, and the coordinator puts the machines together:

1. **Hold blocks of a model…** on several machines. Each one reports its blocks to the network, and the window proposes the blocks the fewest machines hold. A machine behind a home router is reached through the network's relay: it opens no port.
2. **Hold the conversations of a model in blocks…** on a machine that has room on its disk for the whole file of the model. It needs little memory.
3. When every block has its holders (two for each block on the public network, so that one can leave) and one machine holds the conversations, the coordinator gives that machine a chain, one holder for each block. It loads the model across them and offers it to everyone, like any other model.

The list of models shows it as it happens: "In blocks: 4 blocks of 6 held", then "chain formed". When a machine of the chain leaves, the coordinator makes another chain with the holders that remain, and an answer that was being written goes on from where it stopped.

The relay carries what the machines exchange when they cannot reach each other directly. It sees who talks to whom and how much, never what: the link between two machines is encrypted from end to end. Two machines of the same network talk directly, without the relay.

**Everyone in a chain is paid.** The credits of an answer are shared: two parts in ten to the machine that holds the conversation, eight to the holders, each according to the blocks it has in the chain. The account that asks signs that list before the job starts, so the coordinator cannot send a part to anyone else, and the shares are written in the public ledger. `tor6ia audit` checks them like the rest.

**A machine that computes wrong is found and left out.** The coordinator sends test jobs with a known answer. When one fails through a chain, it replaces one holder at a time and tests again. A holder is excluded for a day when the chain fails with it, passes without it, and fails again when it is put back: two tests must agree, because a test can fail by bad luck. Measured: a holder that answers noise is out after 4 tests, about a minute.

To try it with several people, follow the [trial guide](docs/ESSAI.md) (in French).

What to know before using or holding a model in blocks:

- The machines of a chain see the numbers of the computation pass, not the text. An expert could draw part of the meaning from them. The machine that holds the conversation sees the text, as any machine that answers does. The interface says so before you ask.
- The coordinator gives a holder's line to the machine it chose to hold the conversations. A line lets that machine use the blocks.
- A holder that computes wrong can only be told from the others when another machine holds the same blocks. Measured on one laptop, Gemma 4 12B split in two answers at 3.3 tokens per second, and still 1.9 with 50 ms of network delay each way.

## Credits

**No credit is created.** A payment moves credits from the account that asks to the account that computes. All balances always add up to zero.

- **Everyone starts at 0.**
- **Earning.** When another person computes on your machine, you receive exactly what they pay.
- **Price.** One credit is about one token of a ×1 model: 4 bytes of answer, or 40 bytes of prompt, times the model price. The coordinator counts the bytes; your node counts them again and raises an alert on any difference.
- **Starting overdraft.** If everyone is at 0, nobody can pay for the first request. So a machine that passes a test job, whose answer the coordinator knows, may go down to −200. The test is limited to one machine per IP address every 10 minutes.
- **Free at home.** A model your own machine hosts answers locally, with no credit and no network.
- **Failover.** If the machine that computes goes away before answering, your node asks another one. The failed attempt costs nothing.

## Nobody can cheat on credits

The ledger is public: `https://<coordinator>/v1/ledger`. Each line contains the hash of the previous one.

| Rule | What enforces it |
|---|---|
| Nobody takes your credits, not even the coordinator | A payment is valid only with your key's signature, for that job, that payee and that ceiling |
| No credit comes out of nowhere | The ledger only knows payments: the sum stays zero |
| Nobody spends more than balance plus overdraft | Checked on every line |
| The past cannot be rewritten | Every line is chained and signed; every node keeps the last position it verified |

Every node replays the whole ledger at startup, then every 30 minutes. A broken rule shows a red alert. To check by hand:

```sh
tor6ia audit
```

## Use the API

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:7606/v1", api_key="unused")
reply = client.chat.completions.create(
    model="gemma4:e2b",
    messages=[{"role": "user", "content": "Hello!"}],
)
print(reply.choices[0].message.content)
```

Text only: no images, no tool calls.

## How it works

<p align="center"><img src="docs/how-it-works.svg" alt="Your prompt goes encrypted through the coordinator to a machine that computes; credits move from you to that machine on a public ledger" width="100%"></p>

1. Your node asks for a model. The coordinator reserves the fastest free machine and returns its public key.
2. Your node encrypts the conversation for that machine (X25519, AES-256-GCM) and signs the highest price it accepts.
3. The machine decrypts, computes, and sends the answer back encrypted, piece by piece.
4. The coordinator counts the bytes and writes the signed payment to the ledger.

Nodes accept no incoming connection: they poll the coordinator. No port to open, it works behind a home router.

## Run your own network

Without a coordinator, a node runs in **solo mode**: a private coordinator limited to the machine. A shared network needs one machine everybody can reach. It computes nothing: a small server is enough.

With a Debian or Ubuntu server, Apache, certbot and SSH key access:

```powershell
./deploy.ps1 -Server root@203.0.113.10 -Domain tor6ia.example.org
```

The script installs a `tor6ia-coordinator` service that serves HTTPS itself on port 8443, with its own user, memory and processor limits, and a Let's Encrypt certificate renewed automatically. It changes no existing site. Run it again to update.

Without a domain name, `tor6ia.203-0-113-10.sslip.io` points to `203.0.113.10`.

Then build the clients for your network:

```powershell
./build.ps1 -Coordinator https://tor6ia.example.org:8443
```

## Pipeline

`.github/workflows/ci.yml`:

- **Every push**: format, `go vet`, tests.
- **Every tag `vX.Y.Z`**: deploys the coordinator, publishes the binaries as a GitHub release, then runs the one-line install on clean Linux and macOS machines and asks the model a question.

```sh
git tag v0.2.0 && git push origin v0.2.0
```

The release notes are the `## v0.2.0` section of `CHANGELOG.md`, written before tagging. Installed programs show them in their update window.

Repository settings (Settings, Secrets and variables, Actions):

| Name | Kind | Role |
|---|---|---|
| `COORDINATOR_URL` | variable | network the published clients join |
| `DEPLOY_SERVER` | variable | `root@address`. Empty: no automatic deploy |
| `DEPLOY_DOMAIN` | variable | name of the coordinator |
| `DEPLOY_KNOWN_HOSTS` | variable | output of `ssh-keyscan address` |
| `DEPLOY_SSH_KEY` | secret | private key used only for deploys |

Automatic deploy gives GitHub Actions root access to the server. Use a dedicated key, never your personal one. Without these settings, deploy by hand with `deploy.ps1`.

## Known limits

- **Models in blocks are young.** They were tested on a few machines of the same owner, not yet by strangers. A machine that holds conversations may use the blocks it was given outside the network, unpaid.
- **The machine that computes reads your prompt.** It does not know who you are, but do not send secrets.
- **The coordinator is still trusted for three things.** It assigns machines: the encryption key is signed by the account that is paid, so it cannot read a job sent to someone else's machine, but it could send your job to a machine it runs itself. It counts answer bytes: your node recounts what it pays, not yet what it earns. It grants overdrafts: it could grant them to fake accounts, but each is capped at 200 and visible in the ledger.
- **An account can leave with its debt.** The 200 overdraft is the entry cost of the network. The per-IP test limits it; several addresses get around it.
- **The announced model is not proven.** Tests check that a machine really computes, not which model it runs. Three failed tests exclude it for an hour.
- **The ledger is public.** Accounts are anonymous keys, but who pays whom, and how much, is readable.
- **One job at a time per machine.** Requests wait at most 30 seconds for a free machine.

## License

[MIT](LICENSE)

## Develop

```sh
go test ./...
go build -o dist/tor6ia.exe .
```

No dependency outside the Go standard library.

| File | Role |
|---|---|
| `proto.go` | messages, signatures, encryption, prices |
| `ledger.go` | public ledger: rules, chain, audit |
| `coordinator.go` | job queue, test jobs, settlement |
| `node.go` | computing for the network, local API, audit |
| `ollama.go` | Ollama install, models, hardware detection |
| `split.go` | a model across a group of machines, with the Tor6IA engine |
| `hold.go` | the blocks this machine holds for a group |
| `head.go` | this machine as the head of a chain the network formed |
| `chain.go` | the coordinator's register of blocks, how it forms chains and shares a payment |
| `chaintest.go` | how the coordinator finds a machine of a chain that computes wrong |
| `ui/index.html` | interface |
| `deploy.ps1`, `deploy/remote.sh` | coordinator deployment |

## Star history

[![Star history of Tor6IA](https://api.star-history.com/svg?repos=tomDeprez/Tor6IA&type=Date)](https://star-history.com/#tomDeprez/Tor6IA&Date)
