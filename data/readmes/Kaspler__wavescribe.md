<h1>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/lockup-on-dark.svg">
    <img alt="Wavescribe" src="assets/lockup-on-light.svg" height="56">
  </picture>
</h1>

**Wavescribe listens to the radio for you.** It follows several stations at once, writes down
what is said, translates it into your language, and **can alert you when something you care
about comes up**: a road closure, a strike, a water cut, a wildfire. It works with internet radio,
and with FM and other radio through an inexpensive RTL-SDR receiver. Everything runs on your Mac,
with no cloud and no account.

![The Wavescribe page following three synthetic test broadcasts (text-to-speech, not real stations) in French, German and Spanish, each sentence shown with its machine translation into English, and a "Road closed" alert raised by the German traffic report](assets/demo.gif)

*Test broadcasts made with text-to-speech, not real stations. The recognition, the translation
and the alert are the app's own output.*

Early alpha, for macOS on Apple Silicon.
**[Getting started](docs/GETTING_STARTED.md)** · [Documentation](#documentation)

**Not a safety system.** Wavescribe can miss an announcement, or raise an alert for something
that wasn't said: reception drops, speech recognition and machine translation make mistakes, and
this is early software. Use it to stay informed, never as your only source where life, health or
property is at stake: follow official warnings and the emergency services.

## What it's for

Radio is live, in one language, one station at a time, and gone once it's said. Wavescribe
writes it down, translates it and keeps it, so it can be read, searched and acted on.

**To understand it**

- **Where you don't speak the language.** Read local news and official announcements in your own
  language, and get an alert for what matters to you: a wildfire, a flood warning, a strike, a
  road closure, a power or water cut.
- **Learning a language, or keeping up with home.** Real radio, each sentence next to its
  translation, and any sentence can be played again.
- **Radio you can read.** For deaf and hard-of-hearing people, radio as text, sentence by
  sentence, a few seconds behind the broadcast, on the Mac or on a phone. Speech recognition
  makes mistakes; this is not a certified captioning service.
- **Out of curiosity.** Plug in a receiver and see what is on the air around you: one scan lists
  the stations it hears, with their names where they send one.

**To keep track and act**

- **Many stations, one reader.** Journalists, researchers, OSINT analysts and media monitors
  follow several stations in several languages, search everything that was said, and ask
  questions that are answered with the quoted moments.
- **Automations.** An alert can call a webhook, so a home-automation system or a chat bot can act
  on it: flash a lamp, post a message.
- **Give your AI agent a radio.** An AI agent can search what was said, ask about it, and wait for
  alerts to act on, through an MCP server or JSON on the command line; experimental, see
  [Agent tools](docs/AGENT_TOOLS.md).
- **One listener, many readers.** One Mac follows the radio and everyone on the same Wi-Fi reads
  along on a phone: a household, a club, a community centre.

**Where there's no internet**

- **Off the grid.** On a boat, in a campervan or a cabin: with a receiver it needs no internet.
- **When the power and the networks go down.** Broadcast radio keeps working. During the power
  cut of 28 April 2025 in Spain and Portugal, radio was how people learned what was going on, in
  Spanish and Portuguese only.

## Quick start

You need a Mac with Apple Silicon, 16 GB of memory or more, about 11 GB of free disk (8 GB of it
models), and [Homebrew](https://brew.sh). No receiver is needed to try it: start with internet
radio.

```sh
git clone https://github.com/Kaspler/wavescribe.git
cd wavescribe
brew install ffmpeg uv librtlsdr        # librtlsdr only for an RTL-SDR receiver
uv sync
uv run wavescribe models fetch          # about 8 GB: half an hour at 35 Mbit/s
uv run wavescribe serve --open          # opens the page: pick stations and read along
```

Already have ffmpeg and uv? Any recent version works. Those models transcribe 25 European
languages; for others, also run `uv run wavescribe models fetch whisper-large-v3-turbo` (1.5 GB).

For news stations in eight languages, ready to try:

```sh
uv run wavescribe serve --config config/stations.world.example.toml --open
```

A few more commands:

```sh
uv run wavescribe serve --lan           # phones on the same Wi-Fi read along (read-only, no
                                        # login: only on a network you trust)
uv run wavescribe search "água"         # search everything heard
uv run wavescribe alerts test           # check notifications and the spoken-alert voices
uv run wavescribe radio scan a fm       # find FM stations with receiver `a`
```

[Getting started](docs/GETTING_STARTED.md) goes through stations, alerts, phones and a radio
receiver step by step.

## Hardware

- **None:** internet radio needs only the Mac.
- **Starter:** one RTL-SDR Blog V4 receiver and its antenna (about €40–60): a few FM stations
  that sit close together, station finding, and listening to any frequency.
- **More stations:** three receivers behind one antenna and a splitter (about €150–250).

[docs/HARDWARE.md](docs/HARDWARE.md) says which Mac, what to buy, which antenna and how to
connect it.

## What it does

What is implemented, one line each, with a link to how to use it. *(experimental)* marks what
is less tried.

**Stations and sources**

- [Several stations at once](docs/GETTING_STARTED.md#4-choose-your-stations), each in its own
  language.
- [Internet radio from a station directory](docs/GETTING_STARTED.md#4-choose-your-stations),
  searched by name, country or language, offline too once downloaded.
- [An internet station by its stream address](docs/GETTING_STARTED.md#4-choose-your-stations) (URL),
  or from an `.m3u` or `.pls` playlist.
- [A ready-made list of news stations](docs/GETTING_STARTED.md#4-choose-your-stations) in eight
  languages.
- [FM broadcast radio](docs/GETTING_STARTED.md#9-use-a-radio-receiver-sdr) through an RTL-SDR
  receiver (a USB dongle), with no internet.
- [Several FM stations on one receiver](docs/HARDWARE.md#planning-frequencies) when they sit close
  together.
- [Several receivers at once](docs/HARDWARE.md#sharing-one-antenna), also sharing one antenna
  through a splitter (experimental).
- [Walkie-talkie (PMR446), amateur, marine and aviation
  channels](docs/RADIO.md#keeping-a-frequency-as-a-station) as stations, in NFM and AM
  (experimental).
- [Listen only, transcribe, or transcribe and
  translate](docs/RADIO.md#listen-only-transcribe-or-translate), chosen per station; listen only
  needs no model.
- [Language `auto`](docs/GETTING_STARTED.md#4-choose-your-stations), for a station whose language
  you don't know or that switches between several.
- [Stations in a file](docs/GETTING_STARTED.md#4-choose-your-stations), `config/stations.toml`; what
  you change on the page is kept apart from it.
- [Remote stations](docs/FEED.md#many-places-one-central-server): what another Wavescribe
  transcribes, followed as text.

**Reading and listening**

- [A page in the browser](docs/GETTING_STARTED.md#5-read-along-listen-translate),
  `wavescribe serve`: the live transcript of one station, or of all side by side.
- [Transcribes speech](docs/MODELS.md#speech-recognition-chain-default-order) in 25 European
  languages with the default model; about 100 with Whisper, a second download.
- [Skips most music](docs/MODELS.md#speech-vs-music), so most songs aren't written down.
- [Plays any station live](docs/GETTING_STARTED.md#5-read-along-listen-translate), and any line
  again from its time.
- [Text size, light or dark theme](docs/GETTING_STARTED.md#5-read-along-listen-translate) and which
  stations are shown, per device.
- [Keyboard shortcuts](docs/GETTING_STARTED.md#5-read-along-listen-translate) on the page; `?` lists
  them.
- [The same transcript in the Terminal](docs/GETTING_STARTED.md#5-read-along-listen-translate),
  without the page: `wavescribe listen`.

**Translation**

- [Translates each station](docs/GETTING_STARTED.md#4-choose-your-stations) into one or more
  languages as it is said, with a model on your Mac.
- [The language to read in](docs/GETTING_STARTED.md#5-read-along-listen-translate) is each reader's
  choice, with or without the original beside it.
- [Alerts in further languages](docs/GETTING_STARTED.md#7-get-alerts), for readers and webhooks
  (`alert_languages`).
- [A speech model and a translation model of its
  own](docs/RADIO.md#listen-only-transcribe-or-translate) for a station that needs them.

**Alerts**

- [Keyword alerts](docs/GETTING_STARTED.md#7-get-alerts): words and phrases per language, matched on
  the station's own words, not on the translation.
- [Words suggested by the local model](docs/GETTING_STARTED.md#7-get-alerts) in each station's
  language; it can also confirm each match in context.
- [Regular expressions](docs/GETTING_STARTED.md#7-get-alerts) (regex) in a keyword rule, such as a
  road and its number.
- [Rules in plain language](docs/GETTING_STARTED.md#7-get-alerts): describe what you want to hear
  about, and the local model checks for it (LLM rules).
- [A rule's severity](docs/GETTING_STARTED.md#7-get-alerts) decides what happens: a highlight in the
  transcript, a Mac notification, a spoken alert.
- [Spoken alerts](docs/GETTING_STARTED.md#7-get-alerts) in the languages you choose, each with its
  own macOS voice.
- [One alert for a story repeated on air](docs/GETTING_STARTED.md#7-get-alerts): further mentions
  are counted, with a reminder while it goes on.
- [Silence alert](docs/GETTING_STARTED.md#7-get-alerts): a station that sends no audio for some
  minutes, and a notification when it is back.
- [Traffic alert](docs/GETTING_STARTED.md#7-get-alerts): an FM station flags a traffic announcement
  in its RDS.
- [Recent alerts on the page](docs/GETTING_STARTED.md#7-get-alerts), to play or to find in the
  transcript; `wavescribe alerts` lists them.
- [Webhooks and live pushes](docs/FEED.md#push-outputs): alerts, or every line, sent to your own
  program, a chat bot or home automation as JSON, CAP 1.2 XML or text, with filters, retries (an
  alert that hasn't got there waits through a restart), signatures and a delivery log.
- [A test of the notification and of each voice](docs/GETTING_STARTED.md#7-get-alerts):
  `wavescribe alerts test`.
- [Rules tried on a sentence](docs/GETTING_STARTED.md#7-get-alerts) (`alerts check`) or on
  everything heard so far (`alerts replay`); nothing is raised.

**Finding radio and watching bands**

- [Scans a band](docs/RADIO.md#finding-stations) and lists the signals it finds, strongest first:
  `wavescribe radio scan`.
- [FM stations named from their RDS](docs/RADIO.md#finding-stations); `radio rds` shows one
  station's name, programme type and radiotext live.
- [The dial](docs/RADIO.md#finding-stations) on the page: the bands a receiver can tune, what each
  one is, what was heard on it, and how much of a band each receiver hears at once.
- [Band plans by region](docs/RADIO.md#band-plans-and-regions) (Europe, Africa and the Middle East,
  the Americas, Asia-Pacific, Japan): `radio bands`.
- [A list of everything your scans heard](docs/RADIO.md#finding-stations), kept on the Mac:
  `radio heard`.
- [A receiver's own signals (spurs)](docs/RADIO.md#finding-stations), learnt with no antenna so that
  scans leave them out: `radio spurs`.
- [Receivers set up on the page](docs/RADIO.md#your-first-receiver): gain, centre frequency, and a
  live spectrum to test the antenna.
- [Listening by hand](docs/RADIO.md#listening-by-hand): spectrum and waterfall, click to tune, seek,
  squelch, gain; nothing is stored.
- [Stepping as on a radio](docs/RADIO.md#listening-by-hand): the arrow keys and up and down buttons
  step by the band's raster or channel by channel, ten at a time with Shift.
- [A scanner](docs/RADIO.md#listening-by-hand) over a band's channels that stops where someone
  talks, and can skip a busy channel.
- [Any frequency kept as a station](docs/RADIO.md#keeping-a-frequency-as-a-station), or transcribed
  from the Terminal with `radio tune`.
- [Band watch](docs/RADIO.md#catching-radio-that-only-talks-now-and-then) (experimental):
  transcribes every channel of a band at once, such as walkie-talkies: `radio watch`.
- [Caught here](docs/RADIO.md#catching-radio-that-only-talks-now-and-then) (experimental): what a
  watch caught, by frequency and time, with its words: `radio catches`.
- [A name, a note and tags](docs/RADIO.md#catching-radio-that-only-talks-now-and-then) for a
  frequency: `radio note`.
- [Asks before listening](docs/RADIO.md#what-wavescribe-does-with-each-kind-of-radio) to radio that
  isn't broadcast or amateur: aircraft, ships, walkie-talkies.
- [What is kept of each kind of radio](docs/RADIO.md#you-decide-what-is-kept) is yours to set; by
  default, radio that isn't broadcast is kept for a few days or not at all.
- [Receive only](docs/RADIO.md#what-wavescribe-does-with-each-kind-of-radio): no transmitting, no
  digital decoder, no decryption.

**Search, Ask and summaries**

- [Search](docs/GETTING_STARTED.md#6-search-and-ask) everything heard, originals and translations,
  in any language: on the page or with `wavescribe search`.
- [Ask](docs/GETTING_STARTED.md#6-search-and-ask) a question in plain language: the answer cites the
  stations and moments it rests on, which can be played.
- [Summary](docs/GETTING_STARTED.md#6-search-and-ask) (experimental): a few points from what was
  said while you were away: `wavescribe digest`.
- ["What are they talking about now?"](docs/GETTING_STARTED.md#6-search-and-ask) for one station
  (experimental): `wavescribe digest --now`.
- [Summaries on a schedule](docs/GETTING_STARTED.md#7-get-alerts) (experimental), as a quiet
  notification, read aloud if you like.
- [How long text and speech audio are
  kept](docs/GETTING_STARTED.md#10-what-wavescribe-keeps-and-why) is yours to set; the page
  downloads the last 24 hours as CSV.

**Phones and other readers**

- [Phones and tablets on the same Wi-Fi](docs/GETTING_STARTED.md#8-read-along-on-your-phone) read
  along and listen, read-only: `wavescribe serve --lan`.
- [Ask from other devices](docs/GETTING_STARTED.md#8-read-along-on-your-phone) only when you allow
  it: `--allow-remote-ask`.
- [Reading over the internet](docs/FEED.md#who-can-read-what) through your own reverse proxy:
  `serve --behind-proxy`, with read tokens.
- [Radio that isn't broadcast stays on the
  Mac](docs/GETTING_STARTED.md#10-what-wavescribe-keeps-and-why) by default: other devices don't see
  it.

**For other programs and agents**

- [A text feed over HTTP](docs/FEED.md#pull-feedv1), `/feed/v1`: live events, and what was said as
  JSON, NDJSON or CSV.
- [Feed tokens](docs/FEED.md#who-can-read-what), to read or to push, made on the page or with
  `wavescribe token`.
- [One central Wavescribe](docs/FEED.md#many-places-one-central-server) that collects the text of
  many places, by pulling or by taking pushes.
- [Every alert as a CAP 1.2 document](docs/FEED.md#event-format-version-1) (Common Alerting
  Protocol): `wavescribe alerts cap`.
- [Monitoring](docs/FEED.md#pull-feedv1): `/healthz` and Prometheus `/metrics`.
- [Agent tools](docs/AGENT_TOOLS.md#1-mcp-tools-your-agent-can-call) (experimental): an MCP server,
  `wavescribe mcp`, to search, ask, summarise and wait for an alert; it adds, starts and stops
  stations only with `--allow-control`.
- [JSON on the command line](docs/AGENT_TOOLS.md#2-the-command-line---json-and-follow)
  (experimental): `--json` on commands, and `wavescribe follow` for the live feed.

**Running it**

- [Models downloaded once](docs/GETTING_STARTED.md#3-download-the-models) from their publishers,
  with `wavescribe models fetch` or on the page.
- [Models removed again](docs/GETTING_STARTED.md#uninstalling) to free the disk:
  `wavescribe models remove` deletes what a model downloaded and says how much that freed.
- [Each model's licence, size and fit](docs/MODELS.md#will-it-fit-settings--languages-and-models)
  for this Mac, listed on the page, which can search for more online.
- [Models and their attribution](docs/LICENSING.md#disclosure-to-users) in the Terminal:
  `wavescribe models list` shows licences and what is installed, `models credits` the attribution.
- [A model with terms to accept](docs/MODELS.md#opt-in-and-restricted-models) is used only once you
  accept them: `wavescribe models accept`.
- [A model of your own](docs/MODELS.md#bring-your-own-model), through `config/models.local.toml`.
- [A background service](docs/GETTING_STARTED.md#11-keep-it-running) on macOS (launchd) that starts
  at login and restarts after a crash: `wavescribe service`.
- [A self-check](docs/GETTING_STARTED.md#troubleshooting) of tools, models, receivers, disk,
  settings and voices: `wavescribe doctor`.
- [A Health page](docs/GETTING_STARTED.md#11-keep-it-running): memory, processor, battery and disk,
  and how far behind each station is.
- [Reconnects by itself](docs/GETTING_STARTED.md#troubleshooting) when an internet stream comes
  back, and [starts a receiver's stations again](docs/HARDWARE.md#limits-today) when it is plugged
  back in.
- [Speech models compared](docs/MODELS.md#speech-recognition-chain-default-order) on a recording of
  your own station: `wavescribe record`, then `wavescribe bakeoff`.
- **[Local by design](docs/GETTING_STARTED.md#questions)**: every model runs on your Mac; no
  account, no telemetry, nothing sent unless you set it up.

Limits: it runs on macOS on Apple Silicon only. With an RTL-SDR receiver it tunes 24 to
1766 MHz, which holds FM broadcast and the VHF and UHF bands, not medium wave or shortwave.
Ideas and requests are welcome as [issues](https://github.com/Kaspler/wavescribe/issues).

## How it works

```
antennas ─► SDR(s) ─► channelizer ─► audio per station
   ─► speech/music gate ─► speech recognition ─► alert rules ─► notify / speak / log / webhooks
                                              └► translation ─► transcript, web page, text feed
```

Internet streams enter at "audio per station". Details are in
[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Documentation

| | |
|---|---|
| [Getting started](docs/GETTING_STARTED.md) | Install, stations, reading, search and Ask, alerts, phones, radio receivers, troubleshooting |
| [Commands](docs/COMMANDS.md) | Every `wavescribe` command and its options |
| [Hardware](docs/HARDWARE.md) | Which Mac, what to buy, antennas, connectors, setup |
| [Radio](docs/RADIO.md) | Finding stations, listening by hand, what's kept of each kind of radio, the law |
| [Feed and outputs](docs/FEED.md) | The text feed, webhooks, remote stations, using Wavescribe from another program |
| [Agent tools](docs/AGENT_TOOLS.md) | Give your AI agent a radio: the MCP server, JSON output and `follow` (experimental) |
| [Models](docs/MODELS.md) | The speech and translation models per language |
| [Licensing](docs/LICENSING.md) | The licence of every library, tool and model |
| [Architecture](docs/ARCHITECTURE.md) | How it works inside, and the decisions behind it |
| [Measurements](docs/MEASUREMENTS.md) | Speed, memory and long-run figures |

## Using it responsibly

**Don't rely on it for safety.** Wavescribe is not an emergency alert system and no substitute
for official warnings: sirens, cell broadcast, civil protection, the emergency services. An alert
may come late, be wrong, or not come at all, and a quiet page doesn't mean nothing is happening.
Transcripts and translations are made by machine: check the original before you act on one.

**You are responsible for using Wavescribe lawfully where you are.** Laws on receiving radio
differ by country and by kind of radio. Broadcast radio is meant for the public; transcripts and
recordings are for your personal use, and broadcasts are copyrighted. Internet streams also come
with their broadcaster's terms of use, which can limit where and how they may be played. Other
radio (aircraft, ships, walkie-talkies) is often protected: in many countries it may be received
but not recorded or passed on. Wavescribe asks before it listens to such radio and keeps little
of it by default; you set what is kept. It only receives: it cannot transmit, and it has no
digital decoder and no decryption.

[The law where you are](docs/RADIO.md#the-law-where-you-are) has the details. This is not legal
advice. Wavescribe is provided "as is", without warranty of any kind (Apache License 2.0,
sections 7 and 8).

## Contributing

Issues and pull requests are welcome: see [CONTRIBUTING.md](CONTRIBUTING.md). Wavescribe is
written with AI coding tools; if you know radio and something in the signal processing, the band
plan or the hardware guide looks wrong, an issue is the best way to say so. To report a security
problem, see [SECURITY.md](SECURITY.md).

## License

Copyright 2026 Vitali Kaspler. Licensed under the [Apache License 2.0](LICENSE).

The licence covers the code and documentation, not the Wavescribe name or logo (`assets/` and
the page's icons). A modified version you distribute needs its own name and logo; saying it is
based on Wavescribe is fine.

Models aren't part of Wavescribe and are never shipped with it: you download each one from its
publisher, under its own licence ([docs/LICENSING.md](docs/LICENSING.md)). The built web page
bundles React and Lucide icons; their notices are in
[`src/wavescribe/web/dist/licenses.txt`](src/wavescribe/web/dist/licenses.txt).
