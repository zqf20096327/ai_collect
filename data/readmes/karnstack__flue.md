<h1 align="center">flue</h1>

<p align="center"><strong>Your Claude Code sessions and terminals, in one place.</strong></p>

<p align="center">
  <a href="https://github.com/karnstack/flue/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/karnstack/flue/ci.yml?branch=main&label=ci" alt="CI status"></a>
  <a href="https://codecov.io/gh/karnstack/flue"><img src="https://codecov.io/gh/karnstack/flue/graph/badge.svg" alt="Coverage"></a>
  <a href="https://github.com/karnstack/flue/releases/latest"><img src="https://img.shields.io/github/v/release/karnstack/flue?label=release" alt="Latest release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT license"></a>
  <a href="https://pkg.go.dev/github.com/karnstack/flue"><img src="https://pkg.go.dev/badge/github.com/karnstack/flue.svg" alt="Go reference"></a>
</p>

<p align="center">
  <a href="https://flue.sh">flue.sh</a> ·
  <a href="https://flue.sh/docs/setup">setup</a> ·
  <a href="https://flue.sh/docs/how-it-works">how it works</a> ·
  <a href="https://flue.sh/docs/relay">remote access</a> ·
  <a href="https://flue.sh/docs/faq">faq</a>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/hero-dark.png">
    <img src="docs/hero-light.png" width="900"
      alt="flue's sessions screen in a browser tab on 127.0.0.1:7717, listing six sessions grouped across four machines: macbook, studio, pi-4 and vps. Beside it a phone, on the relay's own address, has the same highlighted session open, showing an agent transcript and a row of terminal keys.">
  </picture>
</p>

flue is a daemon that keeps terminal sessions alive, and a web app that lists
every one of them across your machines. Claude Code, Codex, Pi, builds, SSH.
Name them, tag them, pin them, find them, open them from any screen you own.

- **Sessions outlive the tab.** Close it, the agent keeps working. Reopen it,
  the scrollback replays.
- **Sessions outlive flue.** Each one runs in its own holder process. Update
  or crash the daemon, nothing stops. After a reboot, each comes back with its
  history and the command that resumes the conversation.
- **One list, every machine.** Group by machine or by tag. Name, tag, pin,
  search. Drag a row onto a group to retag it. Save a view.
- **One keystroke to any of them.** `⌘K` or `Ctrl+Shift+K` lists every session
  on every machine, and the highlighted row shows its last 14 lines.
  `Ctrl+Shift+1` to `9` jumps to a pinned one.
- **Splits and tabs.** `⌘D` splits right, `⇧⌘D` splits down, `⌥⌘T` opens a
  tab. `⌘/` lists every chord, spelled for the keyboard you are on. Linux and
  Windows use Ctrl.
- **Agent history.** Every Claude Code, Codex and Pi conversation from every
  machine. Search it, see tokens and cost per day, read the transcript, resume
  it in a terminal.
- **Files.** Select a path in a terminal, peek at the file, open it in a tab.
- **Phone and tablet.** Pair once with a QR code. A key bar with Esc, Tab,
  arrows and Ctrl. Two devices can mirror one session.

One static Go binary. macOS, Linux, WSL. No Node, no Python, no toolchain.

## Install

```sh
brew install karnstack/tap/flue    # or: curl -fsSL https://flue.sh/install.sh | sh
flue enable
```

`flue enable` installs a login service, starts the daemon, and opens the UI.
On Linux it also runs `loginctl enable-linger`, so the daemon and your sessions
survive your last logout. If lingering cannot be turned on, which happens in
some containers, `flue enable` warns you and names the command to run.
Everything after that happens in the browser.

## More than one machine

One relay, every machine joined to it, every device paired once.

1. Install flue and run `flue enable` on every machine that runs work.
2. Run `flue relay setup` **once**, on one machine. Running it again does not
   add a relay, it replaces the one you have, and every machine and device
   has to join and pair again.
3. Run the `flue relay join` line it prints on every other machine.
4. Pair each phone or tablet once, from a QR code. That pairing covers the
   whole fleet. It is per browser, so Safari and Chrome on one iPad pair
   separately.

The full version, with a recording of the whole thing, is at
[flue.sh/docs/setup](https://flue.sh/docs/setup).

## The CLI

```
flue enable        # install the login service, start the daemon, open the UI
flue disable       # remove it
flue status        # daemon, login service, and session diagnostics
flue open [path]   # spawn a session here, handy from a shell prompt
flue relay setup   # deploy a relay to your own Cloudflare account
flue relay join    # point this machine at a relay another machine deployed
flue relay status  # show the configured relay
flue relay update  # redeploy this release's relay; secret and pairings kept
flue relay address # repoint this machine at a custom domain on the same relay
flue relay leave   # take this machine off its relay; the Worker stays deployed
flue serve         # run the daemon in the foreground, no login service
flue update        # download the newest release, swap this binary, restart the daemon
flue version       # print the version (also --version, -v)
```

## Remote access

The daemon listens on loopback and nothing else. Reaching it from somewhere
else is opt-in and takes one command:

```sh
flue relay setup                                                 # machine 1: paste a Cloudflare token
flue relay join wss://<your-relay> --secret <...> --fleet <...>  # every other machine
```

That deploys a Worker and this web app into your own Cloudflare account, on the
free plan. Everything crossing it is end-to-end encrypted with Noise IK, with
the daemon's key pinned when a browser pairs, so the Worker forwards ciphertext
it holds no key for. There is no flue account, no flue server and no billing.
flue.sh serves docs and downloads and is never part of the data path.

What it deploys and what it costs is at
[flue.sh/docs/relay](https://flue.sh/docs/relay), with the operator-grade
version in [docs/RELAY.md](docs/RELAY.md). What a hostile relay origin could do
despite the encryption, because the browser loads its JavaScript from that
origin, is in the [FAQ](https://flue.sh/docs/faq) and at length in
[docs/faq.md](docs/faq.md).

<p align="center">
  <img src="docs/architecture.png" width="830"
    alt="Architecture of flue: on your machine, a browser tab talks to the flue daemon over a loopback websocket. The daemon and your other devices each dial outbound into a flue-relay Worker in your own Cloudflare account, which forwards ciphertext it holds no key for. A Noise IK channel runs end to end from the daemon to the remote browser, the daemon's key pinned at pairing. No hosted service; flue.sh is never part of the data path.">
</p>

## Status

Released and in daily use. The current release is on the
[releases page](https://github.com/karnstack/flue/releases/latest), and
`brew install karnstack/tap/flue` gets it. It is 0.x, so commands, flags and
the config file can still change between releases. Known rough edges live in
[docs/FOLLOW-UPS.md](docs/FOLLOW-UPS.md).

flue is open source and always free.

## Building and developing

```sh
mise install   # go, node, pnpm, pinned in mise.toml
make build     # web UI + relay Worker, embedded, into bin/flue
make test
```

The dev loop, the dev/prod split, and working on the relay are in
[docs/DEVELOPMENT.md](docs/DEVELOPMENT.md). The landing site is its own package
under [site/](site/), and `make site-dev` runs it.

## License

[MIT](LICENSE)
