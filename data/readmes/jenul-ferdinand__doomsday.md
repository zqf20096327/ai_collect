<div align="center">
  <img src=".github/ttys.png" alt="Wide-eyed bald man in front of a smoking battlefield">
  <h1>doomsday</h1>
  <p>Guides for surviving a nuclear attack and its aftermath, and an offline stack (all of Wikipedia, a local AI, mesh networking) that runs without the internet.</p>
</div>

Print the guides and keep them with your kit. Paper works when phones and power don't.

## If it's happening now

1. **Flash or warning:** don't look toward the flash. Get behind anything solid, lie face down and cover your head. In a car, stop and duck below the windows. The blast wave can take 30 seconds or more to arrive, so stay down until it passes.
2. **Get inside within 10 minutes,** before fallout starts landing. Go underground or to the middle of a large brick or concrete building. Cars and timber houses give little protection. If a basement or multi-storey building is a few minutes away, go there now.
3. **Stay inside for at least 24 hours,** longer if officials say so. Your family should shelter wherever they are. Don't go out to find them.
4. **Stay tuned** to a battery or crank radio and phone alerts. Officials can measure where the fallout went, so their instructions override this repo.
5. **If fallout (grit, ash, dust) landed on you,** take off your outer clothes, bag them and leave the bag away from people. Shower with soap and shampoo, no conditioner. With no shower, wipe your skin and hair with a wet cloth, then your eyelids, ears and nose.

Then read [3. Shelter](guides/03-shelter.md).

## Guides

| Guide | Covers |
|-------|--------|
| [1. Prepare](guides/01-prepare.md) | Risk, plan, kit, radiation meters, skills. Read it now |
| [2. Detonation](guides/02-detonation.md) | Warning, flash, blast and the first 10 minutes |
| [3. Shelter](guides/03-shelter.md) | Where to shelter from fallout, how to improve it, how long to stay |
| [4. Decontamination](guides/04-decontamination.md) | People, pets, food, water, home |
| [5. Medical](guides/05-medical.md) | Bleeding, burns, radiation sickness, potassium iodide |
| [6. Comms and power](guides/06-comms-power.md) | Radio, mesh networks, EMP, solar |
| [7. Aftermath](guides/07-aftermath.md) | Water, sanitation, nuclear winter, growing food, community |
| [8. Regions](guides/08-regions.md) | Alerts, shelters and official guidance by country |

## Offline stack

The submodules in `modules/` hold the source code. `setup.sh` puts the data (Wikipedia, the AI model, manuals) and the built programs in `data/`, which git ignores. Run it while the internet still works. It skips finished files and resumes interrupted ones, so re-run it after a failure.

```sh
git clone --recurse-submodules <url>   # in an existing clone: git submodule update --init --depth 1
DRY=1 ./setup.sh                       # list the downloads (about 130 GB)
./setup.sh
```

It needs `git`, `curl`, `cmake` and a C++ compiler (`sudo apt install git curl cmake build-essential`).

| For | Module | Data |
|-----|--------|------|
| Wikipedia | [kiwix-tools](https://github.com/kiwix/kiwix-tools): `kiwix-serve` hosts ZIM archives as a website | English Wikipedia with images (119 GB), WikiMed, iFixit repair guides, and post-disaster, medicine, food, water and knots libraries |
| Local AI | [llama.cpp](https://github.com/ggml-org/llama.cpp): runs open models on a plain CPU and serves a chat page | Gemma 4 E4B (4.6 GB, needs 8 GB RAM) |
| Local internet | [iiab](https://github.com/iiab/iiab): Internet-in-a-Box turns a Raspberry Pi into an offline Wi-Fi hotspot with Wikipedia, maps and courses | |
| Messaging | [meshtastic-firmware](https://github.com/meshtastic/firmware): text messages over LoRa radio, relayed node to node for kilometres | |
| Networking | [reticulum](https://github.com/markqvist/Reticulum): encrypted networking over LoRa, packet radio, Wi-Fi or serial links | |
| Manual | | Cresson Kearny, *Nuclear War Survival Skills* (PDF) |

### Run it

```sh
data/kiwix/kiwix-serve --port 8080 data/*.zim
data/llama.cpp/bin/llama-server -m data/gemma-4-E4B-it-Q4_0.gguf --host 0.0.0.0 --port 8081
```

Open http://localhost:8080 for the libraries and http://localhost:8081 for the chat. Other devices on the same Wi-Fi use your machine's IP address in place of `localhost`. A Wi-Fi router makes a local network with no internet connection, and on Linux `nmcli device wifi hotspot ssid doomsday password <8+ characters>` turns a laptop into one.

The AI makes mistakes, worst on doses, drugs and numbers. Check anything that matters against the guides and Wikipedia.

### While the internet works

- **Phones:** install [Kiwix](https://kiwix.org) and load `wikipedia_en_medicine_maxi` or the 13 GB `wikipedia_en_all_mini`. Install [Organic Maps](https://organicmaps.app) and download your region. Install the [Meshtastic](https://meshtastic.org) app.
- **Raspberry Pi:** install Internet-in-a-Box from [internet-in-a-box.org](https://internet-in-a-box.org) (the installer needs internet).
- **Meshtastic radios:** flash them at [flasher.meshtastic.org](https://flasher.meshtastic.org) and set the region (`ANZ` in Australia and New Zealand).
- **Spare copy:** copy this repo and `data/` to an external drive and keep it in a metal box ([EMP](guides/06-comms-power.md#emp)).

## Sources

- FEMA, *Planning Guidance for Response to a Nuclear Detonation*, 3rd ed. (2022)
- [Ready.gov: Nuclear Explosion](https://www.ready.gov/nuclear-explosion)
- [CDC: Radiation Emergencies](https://www.cdc.gov/radiation-emergencies/)
- [REMM](https://remm.hhs.gov): Radiation Emergency Medical Management, US Department of Health and Human Services
- Cresson Kearny, *Nuclear War Survival Skills* (1987), [oism.org/nwss](https://www.oism.org/nwss/)
- Samuel Glasstone and Philip Dolan, *The Effects of Nuclear Weapons*, 3rd ed. (1977)
- WHO, *Iodine Thyroid Blocking* (2017); US FDA potassium iodide guidance (2001)
