<h1 align="center">boos</h1>

<p align="center">
  <b>The beginning of an operating system where a model makes the apps.</b><br>
  Its kernel is written from nothing in Rust, for x86-64 PCs. The firmware loads it directly, with no bootloader in between.
</p>

<p align="center">
  <a href="#the-idea">The idea</a> ·
  <a href="#what-it-does-today">What it does</a> ·
  <a href="#what-a-start-looks-like">What a start looks like</a> ·
  <a href="#run-it">Run it</a> ·
  <a href="#how-it-is-written">How it is written</a> ·
  <a href="docs/README.md">The notes</a>
</p>

---

## The idea

**You do not install apps. You ask for one, and a model writes it.**

- **A small kernel that is always on does the fast, exact work:** sharing the processor and the memory, keeping apps apart, talking to devices.
- **A model does the slow, clever work:** it writes the app you asked for. It is not part of the kernel. It is reached over the internet.
- **What the model writes is a script, plain text.** It runs locked in a box, where it can ask the kernel for a few things and touch nothing else. A clumsy app, one that never ends or eats its memory, is stopped, and the kernel carries on.

**The last step is built, in its first and simplest form: an app is written on request.** Everything you type into the chat box goes to the model, which answers in words or by using one of a few tools the kernel offers it. Ask for an app in your own words, such as `I want a dice that rolls`, and the model has it written as a script, which the kernel runs in the box; what the app shows appears on the screen. An app that ran to its end is kept on the disk and listed on the screen, and a later wish that fits it can run it again as it was kept, without writing it anew. An app can still do little: show one line and print to the terminal. Most of this page is about the ground under the idea: the kernel itself, an encrypted link to the outside, the questions to a model, the box, an interpreter that runs scripts, a screen to show things on, a chat box to type into, and a disk to keep things on.

## What is there

boos starts as a UEFI application, takes the machine over from the firmware, and from then on does everything itself: memory, tasks, the keyboard, the screen, a disk, the network. It can run small programs that are not part of it, **apps**, locked in a box where each one gets a block of memory of its own and can touch nothing else. Apps are written as text, as scripts in the language Lua: the model writes them when asked, and the kernel carries the interpreter that runs them.

It runs in QEMU, and it has also started in VirtualBox from its boot disk. It has never run on real hardware.

```text
kernel                      shares the processor and the memory, talks to devices
└─ the box                  WebAssembly: keeps everything inside locked in
   └─ the interpreter       understands Lua
      └─ an app             a script, plain text, written by the model
```

## What it does today

**The machine**

- Starts with no bootloader: the firmware loads the kernel's file, the kernel asks it for the memory map and the screen, and then tells it to step aside.
- Reports a processor failure (an exception), or its own code giving up (a panic), in one line of words, shows that line on a dark red stop screen above the lines it said before it, and then stops.
- Listens to the timer and the keyboard, Shift keys included.
- Manages memory itself: a pile of free frames, its own page tables, a heap.
- Runs several tasks that take turns under the timer. A task that waits uses no processor time.

**The network**

- Finds its network card on the PCI list and drives it: a virtio card, or one of Intel's 82540EM and 82545EM cards.
- Is given an address, looks up a name, and fetches a web page over an encrypted link (TLS). The site proves who it is with a certificate, and the kernel checks it against a list of trusted roots it carries.
- Gets random numbers from the processor and the date from the clock chip, which encryption needs.

**The model**

- Sends every line typed in the chat box to a model, together with a short fixed text, a record of what was said before it, and a list of tools: make an app, run a kept app, pick a look, turn the page of the panel of apps, and forget what was said. The model answers in words, which appear in the chat box as a row that begins with `Model:`, or asks for a tool, which the kernel checks and does, saying in its own sentence how that went. The record holds the last 10 lines that went to the model, each with what came of it, and lasts until the machine is switched off; asked to forget, the model uses the tool, and the next line starts afresh. The model is `deepseek/deepseek-v4.1-flash-1017`, reached through the provider OrcaRouter, a service on the internet that passes questions on to models. The fixed text, the record and the tools are in [docs/tools.md](docs/tools.md).
- When the model asks for a new app, asks it for the app itself: the request the model wrote, cut at 45 signs, together with a fixed text that tells the model how an app for this kernel is written (the language, the two things an app can ask for, and their limits). The text is in [docs/apps.md](docs/apps.md).
- Sends the key that the provider asks for, which you type yourself, to that one site only, over a link whose certificate was checked. If the provider repeats the key in its answer, stars are shown in its place.
- The real provider has answered it: in runs with a real key, the model's answer appeared in the chat box, and an app the real model wrote ran and its text appeared on the screen. The tests use a stand-in for the provider and a made-up key.
- Says in the terminal how many tokens each answer took, which is what the provider is paid for.

**Apps**

- Runs an app as a WebAssembly program in a locked box, checked against WebAssembly's rules before it runs, with a limit on its memory and a budget of steps (fuel), so that an app that never ends is stopped and the kernel carries on.
- Offers an app two things so far: `print`, a line in the terminal, and `show`, a text on the screen.
- Carries an interpreter for Lua that itself runs inside the box. At every start it hands it a script written by hand:

  ```lua
  local greeting = "Hello from a Lua script"
  for count = 1, 3 do
    greeting = greeting .. "!"
  end
  print(greeting)
  show(greeting)
  ```

- Runs the app the model wrote: the kernel takes the script out of the model's answer, checks that the answer came whole and that the script fits the box, lists the script in the terminal line by line, and runs it once. What the app shows appears in the box in the middle of the screen, what it prints comes out in the terminal, and the chat box says in one plain sentence how the run went, or why the app was stopped.
- Keeps an app that ran to its end on the disk, with the words it was asked for, and reads the script back to check that it was written whole. A panel near the top left of the screen lists the apps kept, five a page, the newest first, and it is there again after a restart. The model can run a kept app again, as it was kept, without having it written anew, and turn the panel's page; an app made again for the same request takes the old one's place.

**The screen and the chat box**

- Paints rectangles and writes text into the screen's memory, with letters whose shapes were drawn by hand for it, each one a small grid of dots in the source:

  ```text
  .....
  .....
  .####
  #...#
  #...#
  #...#
  .####
  ....#
  .###.
  ```

- Shows an app's text in a box. The app only says which text; the kernel decides how the box looks.
- Has a chat box along the bottom of the screen: type a line, press Enter, and it goes to the model; the kernel says at once that it is asking, and the answer follows some seconds later. A few words stay with the kernel instead, such as `key`, which makes it take a secret that shows as stars, is kept in memory only, and goes along as the key. Four looks for the screen are built in, Blue, Night, Paper and Contrast: a wish for another look has the model pick one, the whole screen is painted in it at once, and the look picked is kept on the disk.
- Shows its own lines on the screen as well as in the terminal, since many PCs have no serial port: while the machine starts they cover the screen, white on dark blue, one below the other, and when the start is over the usual picture takes their place. F1 shows them again, and any key brings the usual picture back.

**The disk**

- Finds the disk controller (AHCI), sets it up, and reads the list that says how the disk is divided into parts (the GUID partition table).
- Writes only inside the part that is its own. The code that writes a block cannot be called from anywhere else.
- Keeps a notebook there: named things, each written as a new entry behind the last, so that nothing already written is ever changed. The last line you sent in the chat box is in it, and the kernel says it again at its next start.

## What a start looks like

The kernel's lines appear in the terminal, through the serial port, and on the screen while the machine starts. Some of them:

```text
Hello from my kernel!
The firmware has stepped aside. This machine is mine.
Free memory: 197 MB
Page tables: the kernel's own, covering 4 GB
Screen: found, 1280 dots wide and 800 dots high, its memory starts at 0x80000000
Encryption: 8 of 8 checks of the arithmetic are right, and 112 trusted roots are on board
Box: a program of 41 bytes ran inside it and answered 2 + 3 = 5
App: Hello from inside the box
Interpreter: a program of 765037 bytes that understands Lua is on board, and the box accepts it
App: Hello from a Lua script!!!
Disk: ready, "QEMU HARDDISK", 16 MB, in socket 0 of its controller
Disk: my own part is 14 MB, from block 2048 to block 32734
Disk: this is start number 7
Network: this machine was given the address 10.0.2.15 by 10.0.2.2
Network: example.com proved who it is: its certificate leads back to one of the 112 trusted roots. The link is encrypted with ChaCha20-Poly1305.
Network: example.com answered "HTTP/1.1 200 OK". Its page begins:
    ...
```

Some numbers differ from one computer and one start to the next. The whole listing, with what each line means and what it reads when something is missing, is in [docs/startup.md](docs/startup.md).

The QEMU window shows what the kernel paints. Drawn here with signs; in the first look it is white letters on dark blue, and light boxes with orange frames:

```text
┌────────────────────────────────────────────────────────────────────┐
│  Hello from my kernel! I draw my own letters now.                  │
│                                                                    │
│                                                                    │
│                 ┌────────────────────────────────┐                 │
│                 │ Hello from a Lua script!!!     │                 │
│                 └────────────────────────────────┘                 │
│                                                                    │
│                                                                    │
│ ┌────────────────────────────────────────────────────────────────┐ │
│ │ Kernel: type a line and press Enter.                           │ │
│ │ You: Hello, World!?                                            │ │
│ │ Kernel: I am asking the model.                                 │ │
│ │ _                                                              │ │
│ └────────────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────────┘
```

## Run it

**To try it without building anything,** download `boos-0.1.0.zip`, an early test version, from [the releases page](../../releases). It holds the same disk twice, `boot.vdi` for VirtualBox and `boot.img` for QEMU, with the licences and the notices; the release page says how to start it and gives the file's checksum. Anything the model does needs a key of your own from the provider, OrcaRouter, since every line you type goes to the model and is paid for with that key. You can sign up through [the author's referral link](https://www.orcarouter.ai/ref/ref_3f5501c7dd1f98cb4f25), which earns the author a share of what you spend there, or directly at [orcarouter.ai](https://www.orcarouter.ai). A used disk keeps what boos stored on it, so pass on the download, not your disk.

To build it yourself from the source: the run script is written for Windows. You need:

- **Rust**, the stable release, with two targets added:

  ```powershell
  rustup target add x86_64-unknown-uefi
  ```

  ```powershell
  rustup target add wasm32-unknown-unknown
  ```

- **QEMU**, installed in `C:\Program Files\qemu`, which is where `run.bat` looks for it.
- **QEMU's UEFI firmware file**, `edk2-x86_64-code.fd`, copied from QEMU's `share` folder into the project's root.

Then, from the project's root:

```powershell
.\run.bat
```

It builds the interpreter, then the kernel, and starts QEMU. Read the kernel's lines in the terminal, then click the QEMU window and type in its chat box.

To start from one disk file instead, the way a PC starts, run `.\run-boot-disk.bat`: it makes the file `boot.img`, with a start part that holds the kernel and the kernel's own part after it, and starts QEMU from that file. A copy of it in VirtualBox's own format starts in VirtualBox too; [docs/startup.md](docs/startup.md) has the steps.

Three things to know before the first run:

- **The first build needs the internet** to fetch the outside crates. After that, building works without it.
- **Every start reaches the internet, and so does every line you send.** At every start the kernel looks up one name and fetches the page of example.com over an encrypted link. Every line you send, except the few words the kernel keeps for itself, goes with the secret you typed as the key to the provider's site, `api.orcarouter.ai`, and to nobody else, together with the model's name, a fixed text, a record of the last lines said before it and the list of tools, which names the apps kept on the disk by the words they were made for; the provider passes it on to the model. A new app adds a second request to the same site, with the fixed text about apps and the request the model wrote. Each request is paid for.
- **The first run makes a file, `disk.img`**, 16 MB, in the project's root. It is the machine's disk. The kernel writes to it at every start and at every line you send, and to nothing else: inside QEMU it can reach only the files QEMU is given. A PowerShell script divides the new file into parts; on a computer whose settings refuse to run script files, `run.bat` stops there and says that the disk file could not be divided.

[docs/testing.md](docs/testing.md) says how to build by hand and how to boot without a window.

## How it is written

- **To be read.** Plain words, small files, one topic per file, and a comment above every unusual step saying why. A device "signal" is an interrupt, a processor "failure" is an exception, a "frame" is 4096 bytes of real memory. The hardware's own name appears once, in brackets, where the thing is introduced.
- **Owned.** Everything is written for this kernel except four pieces of outside code, listed below. Stable Rust, `#![no_std]`. Building it runs no build script and uses no macro crate.
- **With notes that are kept true.** [docs/](docs/README.md) holds what the code cannot say for itself: the order things must happen in, facts about the hardware, what was tested and what was not, and the known limits. When the code changes, the matching note changes with it.

### Outside code

| What | For | Where its record is |
| --- | --- | --- |
| [smoltcp](https://crates.io/crates/smoltcp) | the network stack | [docs/network.md](docs/network.md) |
| [rustls](https://crates.io/crates/rustls) and the crates that do the arithmetic | the encrypted link | [docs/encryption.md](docs/encryption.md) |
| [wasmi](https://crates.io/crates/wasmi) | the box that apps run in | [docs/box.md](docs/box.md) |
| [omnilua](https://crates.io/crates/omnilua) | the interpreter for Lua | [docs/interpreter.md](docs/interpreter.md) |

Seven crates are kept as copies in `vendor/`. Six of them came with a build script, which is taken out, so that building the kernel runs no program that was compiled along the way. [vendor/README.md](vendor/README.md) says where each came from, what was changed, and under which licence it stands.

### Where things are

| Folder or file | What it holds |
| --- | --- |
| `src/` | The kernel, one topic per file. The map is in [docs/README.md](docs/README.md) |
| `interpreter/` | The interpreter for Lua, a program of its own, built for WebAssembly before the kernel |
| `password-key/` | A small crate of the project's own that turns a password into a key, kept apart so that it is built to run fast |
| `docs/` | The notes, from the takeover to the apps the model writes |
| `vendor/` | The copies of outside code |
| `run.bat` | Builds both, makes the disk file the first time, starts QEMU |
| `make-disk.ps1` | Divides a new disk file into parts, with one part for the kernel |
| `run-boot-disk.bat` | Builds both, makes the boot disk file the first time, starts QEMU from it |
| `make-boot-disk.ps1` | Makes the boot disk: one disk file with a start part that holds the kernel, and the kernel's own part |
| `LICENSE-MIT`, `LICENSE-APACHE` | The licence of the project's own code: either one, whichever you choose |

## What it cannot do

Said plainly, because a list of what works is only half the picture:

- Whether the model runs a kept app or has a new one written is its own choice, and nothing checks it.
- An app can show one line of 40 signs and print to the terminal, and nothing else. It cannot wait or read a key. A request for one has at most 45 signs.
- The model is told the same fixed text with every request for an app, and whether it keeps to it is not checked: an answer in words instead of a script is taken as the script.
- Every line is a paid question that needs the internet and takes seconds. The model sees that line and a record of up to 10 lines before it, with what came of each, and nothing older; the record is gone when the machine is switched off. Only the first tool it asks for is done, and what the tool did reaches the model only with the next line, in the record.
- It has run in QEMU and, from its boot disk, in VirtualBox, and nowhere else. What a real PC may do differently is collected in [docs/open-points.md](docs/open-points.md).
- Its network card is a virtio card, a kind that exists only in virtual machines, or one of Intel's 82540EM and 82545EM, which QEMU and VMware play and some older PCs have. The Intel driver has run only in QEMU.
- The mouse is switched off, and the look of the screen is one of four built into the kernel.

Start with [docs/README.md](docs/README.md) if you want to read the code or change it.

## Licence

The project's own code may be used under the MIT licence ([LICENSE-MIT](LICENSE-MIT)) or the Apache License, Version 2.0 ([LICENSE-APACHE](LICENSE-APACHE)), whichever you choose. The outside code keeps its own licences; [vendor/README.md](vendor/README.md) lists those of the copies.
