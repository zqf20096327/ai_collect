# Diskless Steam Deck LLM fleet

Bare Steam Deck motherboards running as disposable, diskless LLM nodes. Plug in
ethernet and USB-C power, and about two minutes later the board is serving an
OpenAI-compatible API on port 8080, running an 8B model on its GPU. Nothing is written
to the board. Pull the power and it leaves no trace.

Steam Deck boards (both the OLED "Sephiroth" and the LCD "Jupiter" / Van Gogh batch) are
cheap on the salvage market, sip power, and carry a capable little RDNA2 GPU with 16GB of
LPDDR5. That makes them a surprisingly good substrate for a small, distributed local-LLM
cluster, with two problems in the way: getting the boards to boot something useful with
no disk, and stopping the firmware from throttling the GPU. This repo is how I solved both.

There is a video version of this story:
[I spent all my money on broken Steam Decks](https://youtu.be/P0GXwKlg3pU),
and a written case study at
[matthewnoh.com/work/steamdeck-pxe-llm](https://www.matthewnoh.com/work/steamdeck-pxe-llm/).

## What it needs

Per node, the hardware is minimal:

- **A bare Steam Deck motherboard** (LCD / Van Gogh, or OLED). The board is the whole
  computer: CPU, GPU, and 16GB of RAM are all on it. No screen, storage, keyboard, or
  case required.
- **A USB-C dongle or dock that does ethernet and power at the same time.** This is the
  one part people get wrong. These run as always-on nodes, so power has to come in
  continuously over USB-C: a battery, if the board even has one, only buffers and will not
  run it for long, and plenty of salvage boards have no battery at all. The board also
  wants roughly **15V USB-C PD** to power on (a plain 5V source will not do it), so the
  dock/hub has to provide a wired ethernet port *and* pass PD power through to the
  board. A plain ethernet-only dongle will not power the board. A cheap USB-C hub with
  "PD passthrough" plus an ethernet jack, fed by any 15V-capable PD charger (most 30W+
  chargers qualify), is enough.

On the network side there are options, and **a managed switch is not required**:

- **Just a router / an unmanaged switch / a direct cable** all work. A managed switch is
  a nice-to-have (it can remotely bounce a wedged port and report per-port counters),
  but nothing here depends on one.
- **A PXE host**: any always-on Linux box (a mini PC, an old laptop, a Raspberry Pi, a
  spare Proxmox host) with a network interface it can dedicate to the deck segment. It
  runs dnsmasq (DHCP + TFTP) and a static HTTP server, and holds the model files. It does
  not need a GPU; the decks do the inference.

### With only a home router

PXE means running a DHCP server, and two DHCP servers cannot share one network without
fighting. So the decks want their own small segment, separate from the normal LAN. The
simplest way, and what the configs here assume: put a **second network interface** on the
PXE host (a USB ethernet adapter is fine), plug the board into it (directly, or through a
cheap unmanaged switch), give that interface an isolated subnet like `10.66.6.1/24`, and
bind dnsmasq to just that interface. The main router never sees the deck DHCP traffic, and
the boards stay isolated from the rest of the LAN and the internet. (A managed switch can
do the same thing with a VLAN instead; a router running OpenWrt can point PXE clients at a
next-server itself; but the dedicated-interface route is the most predictable.)

## How it works

```
bare board + ethernet + USB-C power
        |
        v
  UEFI PXE  ->  iPXE  ->  Fedora CoreOS booted entirely into RAM
        |
        v
  ignition applies one declarative config:
    - mount the model library from the host over NFS (read-only)
    - pin the GPU clock so inference runs at full speed
    - start llama.cpp (or whisper.cpp) on :8080, model chosen by hostname
```

There is no per-board setup. Every board boots the same image and the same ignition,
learns its identity from DHCP, and picks its model from a shared assignment file. Swapping
a board's model is one line in a config file plus a service restart, no reboot.

## The two interesting parts

- **[docs/pxe-boot.md](docs/pxe-boot.md)**: the diskless boot chain, PXE to iPXE to
  Fedora CoreOS in RAM, why FCOS, the GTT kernel arg that lets an 8B model fit, and the
  trick of letting the USB ethernet dongle carry each node's identity.

- **[docs/gpu-pin.md](docs/gpu-pin.md)**: the part that makes it worthwhile. Run a Deck
  board with no battery and the embedded controller clamps the GPU clock, so inference
  crawls at under 2 tok/s. Pinning the clock through the amdgpu overdrive interface
  restores full speed (about 12.4 tok/s per board on an 8B Q4 model). This also explains
  why the CPU clamp is a dead end and why there is no "unlock more cores" to be had.

Plus [docs/cooling.md](docs/cooling.md) for the cooler iteration, since the GPU pin only
pays off if the board can shed the heat.

## Layout

```
docs/setup.md               full copy-paste setup runbook (start here to build it)
server/                     runs on the PXE host
  setup-host.sh                  one-shot host plumbing (dnsmasq, NAT, HTTP, NFS)
  dnsmasq.d/steamdeck-pxe.conf   DHCP + TFTP, two-stage PXE chainload
  tftp/boot.ipxe                 iPXE script: boot FCOS in RAM
  ignition/deck.bu               the whole node definition (Butane source, self-contained)
  exports.example                NFS share for the model library
deck/                       runs on each board
  deck-launch.sh                 pick model+mode by hostname, run the server
  fleet-assign.conf              which board serves which model
host-scripts/               helpers on the PXE host
  fetch-fleet-models.sh          download the GGUF/whisper models
  roll-decks.sh                  reboot boards and wait until they serve again
```

## Using it

Full copy-paste walkthrough: **[docs/setup.md](docs/setup.md)**. Every step there is a
paste-able command. The short version:

```bash
# on the PXE host (an always-on Linux box), Debian/Ubuntu
git clone https://github.com/Floral-Overcast/steamdeck-pxe-llm ~/steamdeck-pxe-llm
cd ~/steamdeck-pxe-llm

# 1. host plumbing: isolated interface, NAT, dnsmasq, boot files, HTTP, NFS share
#    (set DECK_IF to the interface facing the decks, WAN_IF to the internet-facing one)
sudo DECK_IF=eth1 WAN_IF=eth0 ./server/setup-host.sh

# 2. download the models
sudo MODELS_DIR=/srv/models bash ./host-scripts/fetch-fleet-models.sh

# 3. build the ignition: fill in the ssh key + password hash placeholders in
#    server/ignition/deck.bu (mkpasswd --method=yescrypt), then compile it into place
podman run --rm -i quay.io/coreos/butane:release --pretty --strict \
  < server/ignition/deck.bu | sudo tee /srv/tftp/ignition.json >/dev/null

# 4. wire a board (dock giving ethernet + 15V PD), power on, wait ~2 min, then:
curl -s http://10.66.6.101:8080/v1/models
```

`setup-host.sh` just runs steps 2 to 7 of [docs/setup.md](docs/setup.md); do the
same steps by hand to see exactly what it touches. Registering a board's dongle
MAC as `deck-N` (so it always gets the same IP and model) is one line in the dnsmasq config,
shown in the runbook.

## Notes and scope

This runs on an isolated, firewalled subnet with no inbound route from the internet,
which is why password auth is left on for convenience. Do not expose these boards
directly. The BIOS unlock and crisis-flash side of this project (for boards that need a
firmware change before they behave) is involved enough that I have left it out of the
first cut; open an issue if that part would be useful.

Hardware specifics I found while doing this (clock ceilings, thermal numbers, the dongle
wedge, the CPU clamp) are written down in the docs so nobody has to rediscover them.

## License

MIT. See [LICENSE](LICENSE).

## Author

Built by [Matthew Noh](https://www.matthewnoh.com), a product designer in Dallas.
More projects like this under [Floral Overcast](https://github.com/Floral-Overcast).
