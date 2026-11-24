<p align="center"><img src="docs/logo.png" alt="Drive Energy Doc Logo" width="160"></p>


# Drive Energy Doc for Home Assistant

<p align="center">
<a href="https://github.com/AlphaLima/ha-drive-energy-doc/releases"><img src="https://img.shields.io/github/v/release/AlphaLima/ha-drive-energy-doc" alt="Release"></a>
<a href="LICENSE"><img src="https://img.shields.io/github/license/AlphaLima/ha-drive-energy-doc" alt="License MIT"></a>
<a href="https://github.com/AlphaLima/ha-drive-energy-doc/actions"><img src="https://img.shields.io/github/actions/workflow/status/AlphaLima/ha-drive-energy-doc/validate.yaml?label=HACS%20%2F%20Marketplace" alt="Validation"></a>
</p>

🇬🇧 English · [🇩🇪 Deutsch](README.de.md)


### The smart, fully automatic fuel and charging log

A **fuel and charging log for any number of vehicles** (combustion and electric) that keeps itself fully automatically. There are two ways to use it, and you can mix them:

- **Connected to the car (fully automatic):** Home Assistant detects refuelling or charging on its own from the car's sensors (level, odometer, GPS), creates the entry, looks up the price and calculates the consumption. The driver does not have to do anything. The receipt is only a bonus: if it is sent via Telegram, the AI reads it, the accounting becomes even more precise (real quantity, price and total) and the event is documented as well.
- **Without any connection to the car (photo mode):** Just send a **photo of the odometer** and a **photo of the pump or the receipt** via Telegram. The AI reads mileage, quantity, price and total, the log is kept and the receipts are archived. No sensors are needed for the vehicle. This is **ideal for fleet management**: every vehicle gets its own Telegram chat (e.g. with the driver), and all vehicles end up in one list with CSV and PDF export.

**Other consumables** (AdBlue, oil, washer fluid, …) can be documented as well, by message or photo; they count towards costs but not towards consumption.

Everything ends up in one list in the sidebar (with CSV and PDF printing).

## Contents
1. [What is it for?](#what-is-it-for)
2. [Ways to get data into the log](#ways-to-get-data-into-the-log)
3. [Photo mode without a car connection (fleet management)](#photo-mode-without-a-car-connection-fleet-management)
4. [How it works (overview)](#how-it-works-overview)
5. [How a refuelling is detected (in detail)](#how-a-refuelling-is-detected-in-detail)
6. [Which position and which price is used](#which-position-and-which-price-is-used) · [Countries with price portals: supported and not supported](#countries-with-price-portals-supported-and-not-supported)
7. [Receipt, accessories and odometer by message](#receipt-accessories-and-odometer-by-message) · [Receipt for refuelling](#receipt-for-refuelling) · [Accessories (AdBlue, oil, wipers …)](#accessories-adblue-oil-wipers-) · [Odometer reading](#odometer-reading)
8. [How consumption is calculated](#how-consumption-is-calculated)
9. [Electric vehicles](#electric-vehicles)
10. [The panel](#the-panel) · [Example printout](#example-printout)
11. [Sensors, event and services](#sensors-event-and-services)
12. [Installation and setup](#installation-and-setup)
13. [Setting up the AI for receipt reading](#setting-up-the-ai-for-receipt-reading)
14. [Setting up Telegram](#setting-up-telegram)
15. [Setting up WhatsApp (Meta's official Cloud API)](#setting-up-whatsapp-metas-official-cloud-api)
16. [Languages](#languages)
17. [Data and privacy](#data-and-privacy)
18. [Limits](#limits)
19. [Tests](#tests)
20. [License](#license)

---

![The panel with vehicle header, key figures and list](docs/panel-liste.png)

*The panel (sample data): vehicle header, key figures, big photo button and the list with receipt photos.*

> **Note: All screenshots, examples and test images in this project show entirely fictional dummy data.** Licence plates, filling stations, addresses, receipts, prices and odometer readings are made up and belong to no real vehicle, no real person and no real filling station. Any resemblance to real plates or places is coincidental.

<table>
<tr>
<td align="center"><img src="docs/panel-lesen.png" alt="Reading the receipt" width="300"><br><sub>The AI reads the receipt (with magnifier)</sub></td>
<td align="center"><img src="docs/panel-ergebnis.png" alt="Result after the upload" width="300"><br><sub>Result: station, quantity, price, total</sub></td>
<td align="center"><img src="docs/panel-fahrzeugauswahl.png" alt="Vehicle selection" width="300"><br><sub>Choose a vehicle by clicking the header area</sub></td>
</tr>
</table>

**Several photos at once:** The photo button lets you pick several images in one go (receipts and odometer photos mixed, in any order). They are processed one after the other; the progress dialog shows all photos with a tick for the finished ones, a counter and a bar; **Cancel** stops the whole batch. There are no follow-up questions about mileage or consumption in the middle: odometer photo and receipt are matched by capture time (EXIF) and mileage, and a summary at the end shows all results including warnings.

<p align="center"><img src="docs/panel-stapel.png" alt="Batch processing: 8 of 40 photos" width="320"><br><sub>Batch processing: 8 of 40 photos, finished ones ticked, progress bar and cancel button</sub></p>

## What is it for?

A fuel log answers questions you would otherwise only guess:
- **What does my car really cost?** Fuel or electricity plus accessories (AdBlue, oil, wipers), per month and over 12 months.
- **What does it really consume?** Calculated full-to-full, independent of the (often too optimistic) trip computer; changes (winter tyres, a defect, a different driving style) become visible.
- **Receipts and proof:** Each row can hold the photo of the receipt and of the odometer, for tax, company cars, warranty or resale. The list can be exported as CSV (Excel) or printed as PDF.
- **Several vehicles in one log**, combustion and electric treated the same, without paperwork or hand-made spreadsheets.

The effort is kept as small as possible: the car reports the refuelling by itself, and at most you send a photo of the receipt.

## Ways to get data into the log

| Way | What you do | What happens automatically |
|---|---|---|
| **1. Automatic (sensors)** | nothing | Level rises, refuelling is detected; quantity, place, odometer and (if available) price are recorded |
| **2. Receipt photo via Telegram / WhatsApp / Companion** | photograph the receipt or pump and send it to the bot | AI reads quantity/price/total/date, the photo is cropped and stored with the entry, receipt values replace the estimated ones |
| **3. Receipt as text** | write `45,93 105,13` or `27.10. 45,93 105,13` | values are assigned to the matching refuelling (no AI) |
| **4. Accessories** | `+ 24,90`, `extra Öl 1 9,50`, short word `adblue`, or a photo with a caption | own entry, counts towards costs, not towards consumption |
| **5. Odometer photo / `km 54210`** | photograph the odometer or send text | mileage is assigned to the refuelling that fits in time; the bot asks if in doubt |
| **6. Panel** | manual entry ("+"), edit an entry, upload or delete photos | – |
| **7. Service** `drive_energy_doc.submit_text` | feed text in, e.g. from an automation or script | like ways 3–5 |
| **8. Import (one-off)** | put old data at `config/drive_energy_doc/import/<vehicle name>/entries.json` (optionally with `photos/`, `originals/`) | entries including photos are taken over at the next start |

The **receipt always wins** over the automatic values: the car estimates, the receipt is right. All ways lead into the same log; mix them as you like.

## Photo mode without a car connection (fleet management)

When adding the vehicle, only name, energy type and tank size are required. If you leave the level, odometer and GPS sensors empty, the vehicle works purely through messages:

1. The driver sends the bot a **photo of the odometer** (or `km 54210` as text). A new entry with this mileage is created.
2. Then they send the **photo of the receipt or the pump** (up to 48 hours later). The AI reads quantity, price, total and date; the photo is cropped and archived with the entry. The order does not matter: if the receipt comes first it creates the entry and the odometer completes it.
3. Accessories (AdBlue, oil …) work the same way with `+ 24,90` or a photo with a caption.

Consumption (full-to-full) is calculated from the mileages and quantities. Because without sensors it is not known whether the tank was filled up, every refuelling counts as full. For a **fleet**, create one entry per vehicle with its own Telegram chat; the assignment is done via the chat ID.

## How it works (overview)

```
Car sensors (level %, odometer, GPS)
        │
        ▼
 Detection: level rises → refuelling → quiet + distance → "done"
        │
        ├─► look up the price (fuel price service, optional)
        ├─► create the log entry (time, quantity, price, cost, odometer, place)
        └─► message via Telegram/WhatsApp/Companion app: "Refuelling detected – send the receipt if you like"
                   │
                   ▼
        Photo of receipt / pump / text  ─►  AI reads quantity, price, total, date
                   │                         (photo is cropped and stored with the entry)
                   ▼
        The receipt always wins: its values replace the estimated ones
```

Each vehicle is its own entry in the integration. In addition there is one **"Global settings"** entry for everything that is the same for all vehicles (price sources, electricity price, AI choice, Telegram/WhatsApp credentials). Each vehicle has its own configuration (sensors, fuel type, thresholds, chat), its own log and its own sensors.

## How a refuelling is detected (in detail)

The detection is a small state machine. It runs on every change of the **level sensor** (in %) and additionally checks the time every 15 seconds. There are four states:

1. **Idle.** Nothing happens while the level stays the same or falls (driving uses fuel).
2. **Candidate.** As soon as the level **rises**, the integration remembers the value before it (`level from`), the time and the **position**. Further rises are added up into *one* event (many cars report the fill in several small steps).
3. **Valid.** Once the total increase reaches **at least 5 %** (adjustable), the event counts as a real refuelling. Smaller fluctuations (tilt sensor, hills, noise) are ignored this way. From here on the price is fetched (see below).
4. **Done.** The refuelling is completed when **both** are true:
   - the level has **not risen further for 60 seconds** (adjustable), and
   - the car is **more than 250 m away from the filling place** (adjustable, straight-line distance to the start position).

   Why the distance? The level often rises with a delay; someone still standing at the pump should not trigger an entry yet. Only when the car has driven away is it certain that the refuelling is over. Only then does the message arrive in which you can submit the receipt if you like (optional; the entry is complete even without a receipt).

   **Exception, electric cars:** the distance condition does not apply (the car stays put while charging). The default is **10 minutes of quiet** without a further rise; this is adjustable too. The distance rule can also be switched off for combustion cars.

**Cancel.** If the increase does not grow after 10 minutes and never becomes valid (below the threshold), the candidate is discarded. If Home Assistant restarts meanwhile, an event in progress is kept (it is stored) and continued afterwards.

**What ends up in the entry:** time, level from/to, from that the quantity (increase × tank volume or battery capacity), mileage (from the odometer sensor, if present), place and the price (if available). The tank volume is entered once per vehicle.

## Which position and which price is used

**Position:** The **last known GPS position of the vehicle (`device_tracker`) at the moment the first level rise arrives** is used. The car is then standing at the pump. Important: if the car reports the new level late, the last reported position may still be from the way there. The entry then shows the wrong place and the price comes from the wrong station; the receipt corrects the price in any case.

**Price:** Optional. At the transition to "valid" the integration uses the start position to find the **nearest open station within 400 m** and takes the price of the chosen fuel type (diesel, E5, E10). Sources:

| Country | Service | Key |
|---|---|---|
| Germany | Tankerkönig | personal, free API key |
| Austria | E-Control | none needed |
| France | prix-carburants (data.gouv.fr) | none needed |
| Spain | MINETUR / MITECO (ministry) | none needed |
| Italy | MIMIT Osservaprezzi (open data) | none needed |

The source depends on the country of the position (or is fixed by choice). Without any source everything still works; the price then comes from the receipt. **Electric:** a fixed price per kWh or a sensor/helper that supplies the electricity price (e.g. a dynamic tariff).

### Countries with price portals: supported and not supported

State of the research: November 2026. There is no official Europe-wide portal with prices **per station**; the EU only publishes averages.
Each country provides its data separately, in its own format and under its own terms.

**Supported**

| Country | Source | Advantages | Disadvantages |
|---|---|---|---|
| Germany | Tankerkönig | price per station, near real time, brand and address | personal free key required; passing real-time data on to third parties needs approval (not an issue for private use in your own Home Assistant) |
| Austria | E-Control fuel price calculator | official, no key, price per station, closed stations are skipped | Austria only; update interval not checked |
| France | prix-carburants (data.gouv.fr), "flux instantané" | official, no key, all stations | no station name, only the address; opening hours are not checked |
| Spain | MINETUR / MITECO (ministry) | official, no key, updated hourly according to the source, with brand and address | large national file (about 12 MB), the first call takes about 25 seconds (then cached for 30 minutes); the server needs an older TLS setting (applied for this request only); opening hours are not checked |
| Italy | MIMIT Osservaprezzi (open data, licence IODL 2.0) | official, no key, all stations with coordinates, self-service price preferred | prices are as of 8 a.m., not live; marked "experimental", the format may change (the separator changed in February 2026); two files (about 7 MB); opening hours are not checked |

**Not supported**

| Country | Finding | Option |
|---|---|---|
| Netherlands | Officially only average prices from the statistics office CBS, no prices per station. Third-party services not checked. | receipt photo only |
| Belgium | No open per-station interface found. Official maximum prices exist (not checked). | receipt photo only |
| Luxembourg | The Ministry of the Economy sets a **single nationwide maximum price** per fuel. | one national price would be possible, not built yet |
| Portugal | DGEG portal (mainland only). No documented official interface; one endpoint is only known from third-party projects and may change. | uncertain, not built |
| Denmark, Cyprus, Slovenia, Romania | Open or newly mandatory according to third parties, not confirmed. | still to be checked |
| Czech Republic, Finland, Greece, Poland, Hungary, Switzerland | Nothing usable found. | still to be checked |

**Without a price source** everything keeps working: the receipt photo supplies station, address, quantity, price and total in every country. The
price source only matters for vehicles that detect refuelling themselves (level and GPS). More countries are welcome as contributions: a provider is a
function in `price.py` plus an entry in `PROVIDERS` and `BY_COUNTRY`.

**The receipt always wins.** Quantity, price and total from the receipt overwrite the estimated values. An entry is only marked as "receipt checked" when at least quantity, price or total came from the receipt.

## Receipt, accessories and odometer by message

Messages run via **Telegram** (own bot, recommended), **WhatsApp** (Meta Cloud API) or the **Companion app** (push message; photo upload then in the panel). Per vehicle you choose which channels are used. With `?`, `h`, `help` or `hilfe` (also `/help`, `/start`) the bot lists all commands. Replies and keywords work in many languages (see *Languages*).

### Receipt for refuelling
- Send a **photo** of the receipt or the pump. The AI reads quantity, price, total, date and, if visible, the mileage. The photo is **cropped to the receipt** (the AI gives the frame; without an AI answer a simple detection of tall, bright paper receipts takes over). The original is kept and can be viewed in the panel.
- **Text:** `45,93 105,13` (quantity amount), `45,93 2,289 105,13` (quantity price amount) or with a date in front `27.10. 45,93 105,13`.
- **Another photo** for the last refuelling: a photo with the word `zusatz` in the caption.
- If a value is implausible or unreadable, the bot replies with a note instead of saving something wrong.

### Accessories (AdBlue, oil, wipers …)
Anything that costs money but is not fuel. Keyword **`+`, `e`, `x`, `extra`, `z`, `zub`** or `zubehör`, then optionally the name and the numbers: `+ 24,90`, `extra Öl 1 9,50`, `z Scheibenwischer 24,90`. Allowed are only amount, quantity amount or quantity price amount, optionally with a date. Short words without a keyword: `adblue`, `öl`, `scheibenwischer`, `scheibenwasser`, `frostschutz`. The same as the caption of a photo attaches the receipt to the entry. Accessories appear as their own row and count towards costs, but **not** towards consumption.

### Odometer reading
**Order of the sources:** The mileage of an entry comes from the best available source: **1. the vehicle's entity** (odometer sensor), **2. the odometer photo**, **3. only then the reading on the receipt**. On the receipt it is often written in by hand and can be wrong, so it never overwrites a better reading. A reading you type or change in the panel yourself counts as a deliberate decision and always wins. The sensor value only counts for an entry that fits in time: if a receipt is uploaded later (date more than 3 hours away), the current sensor value is not taken over.

**When in doubt the odometer reading is left out.** A reading the AI takes from a **photo** is never guessed and never asked about: if it does not fit the entry, is
lower than the previous reading or gives an implausible consumption, it stays empty and the odometer photo is attached to the entry as an extra photo. On receipts a
mileage only counts if a line is explicitly labelled as such (a receipt number, pump number or card number is not), and it must fit the order of the entries (not lower
than the previous one, not higher than the next one, at most a 5000 km jump, at most six digits). The bot only asks about a reading you **typed by hand**
(`km 54210`), because you entered that yourself; the following paragraphs describe that case.

Send a photo of the odometer or text such as `km 54210`. The value is assigned to the refuelling whose time is closest to the sending time (24-hour window). If the value deviates a lot from the stored one (> 300 km), is lower than at the previous refuelling, or the refuelling is too old, the bot asks and waits for your confirmation (`ja`).
It also checks the **consumption**: if the new reading, the filled quantity (plus partial refuellings in between) and the kilometres since the last full refuelling give a consumption that deviates by more than 40 % from the average of the last five full-to-full values, it warns (e.g. "would give 24.5 l/100 km over 200 km since the last refuelling, average 7.0 l/100 km") and asks whether to apply the reading anyway (`yes` or `no`). The same warning appears under a receipt whose odometer reading looks implausible. The check needs at least two earlier consumption values and only applies to full refuellings.

## How consumption is calculated

Method **full-to-full**: a refuelling counts as "full" if the increase is **at least 30 %**. Between two full refuellings all filled quantities are added up and divided by the kilometres driven (result per 100 km or kWh/100 km). Partial refuellings therefore show no consumption of their own, but flow into the next full calculation. Accessories do not count.

**Numbering:** Every refuelling gets a running number in the list (the oldest is no. 1, accessories have none). The number is also in the CSV export and the printout.

**Duplicate receipts:** If an entry with a receipt already exists for that day, the bot says so and asks whether to overwrite it with the new receipt (`yes` or `no`). If it is the same receipt (same quantity and total) it says that explicitly. With `no` the new photo is deleted again. If nothing is known about the increase (e.g. created by hand), the refuelling counts as full. Without a mileage there is no calculation.

## Electric vehicles

Electric cars work just like combustion cars; the differences at a glance:

**Setup:** Choose the energy type **Electric** at the vehicle and enter the **usable battery capacity in kWh** as the capacity (e.g. 58). The level sensor is the **state of charge (SoC) in %**; odometer and GPS are optional as for combustion cars. Without sensors the [photo mode](#photo-mode-without-a-car-connection-fleet-management) works here too (e.g. a photo of the charger or of the app invoice).

**Detection:** If the state of charge rises by at least **5 %**, a charging session is detected. It ends when the state of charge has **not risen further for 10 minutes** (default, adjustable under *Configure → Refuel detection (fine tuning)*). The **distance condition does not apply** (the car stays put while charging) but can be switched on. Many small charges per day are recorded as separate sessions as soon as they reach 5 %.

**Quantity:** kWh = increase in % × battery capacity. This is the energy **in the battery**; at the socket or wallbox somewhat more is usually consumed because of charging losses. If you want it exact, send the value from the receipt or the charger (e.g. `38,2 0,39 14,90`); the receipt always wins.

**Price:** There is no station lookup. Instead the integration uses the **electricity price per kWh** from the *global settings*: a fixed number (e.g. `0,32`) or an entity that supplies the current price (e.g. a dynamic tariff, helper or sensor). So every charge **at home** automatically gets price and cost. For **public charging** send the app invoice or a photo of the charger via Telegram; the AI reads kWh, price and total, and the receipt replaces the set price.

**Consumption:** Calculated full-to-full like for combustion cars, result in **kWh/100 km**. A charging session counts as "full" from **30 %** increase; smaller charges are added up until the next larger one. This needs mileages (sensor, odometer photo or `km 54210`).

**Known limits:** The wallbox meter is not read (yet); the quantity is battery-side. If the car reports the state of charge only every few minutes, a session starts and ends with the same delay. If the state of charge shows whole percent only, very small charges are imprecise.

### Plug-in hybrids

Tick **Plug-in hybrid** in the vehicle settings (next to the fuel type, e.g. petrol E10). The log then holds **both energy types in one list**: every entry is either **fuel (l)** or **electricity (kWh)**.
- **By receipt or photo:** the AI recognises a charging receipt and creates an electricity entry, a fuel receipt creates a fuel entry. On the same day both can exist side by side without overwriting each other.
- **By hand:** in the edit dialog the **Type** box offers *Fuel* and *Electricity* (plus the accessories).
- **Consumption** is calculated **separately** per energy type (l/100 km and kWh/100 km, each against the previous entry of the same type). The panel shows both averages, a second sensor `Electricity consumption` is added, and the costs of both are summed up. The kilometres are shared.
- **Automatic detection of both:** besides the fuel level sensor you can enter the **battery charge level (%)** and the **battery capacity (kWh)**. Refuelling and charging are then detected independently (two sensors, two detections); charging uses the electricity price from the global settings. **Regenerative braking is ignored:** while driving, the battery level rises without charging. If the vehicle moves more than 200 m from where the rise began (GPS) or more than 1 km (odometer), the rise is not counted as charging; a candidate is discarded, and after a real charge the rises while driving away are ignored. Without a battery sensor, charging is captured by receipt, photo, message or by hand.
- Mixed driving makes the two single values less exact than for a pure combustion or electric car: the fuel consumption of a plug-in hybrid depends on how much was driven electrically. The values are meant as a trend, the cost total is exact.

## The panel

After setup the panel appears in the sidebar, named after the Home Assistant system language (German **"Tankbuch"**, English "Fuel log", French "Carnet de carburant", …):
- List of all refuellings/charges and accessories per vehicle; columns can be reordered and resized. The columns button (above the list) hides columns you do not need; the choice is remembered per browser, a double-click on a column divider resets everything.
- Licence plate display (all European countries, EU ring or yellow for NL/GB), vehicle picture and type in the header. With several vehicles a click on the header area (logo, vehicle type, plate) opens a dialog to choose among all vehicles. You set the plate and its country in the vehicle's configuration.
- Receipt and odometer photos with a preview on hover (several photos: a picker), delete with confirmation, photo upload, also **several photos at once** (progress dialog with cancel, processing by capture time, summary with warnings at the end). Follow-up questions in the dialog have ready-made answer buttons (e.g. "Accept", "New entry", "Cancel").
- Edit and manual entry ("+") in **one dialog with all fields** (type: fuel/electricity or accessory / consumable, changeable afterwards; date and time, quantity, price, amount, odometer, note), place with a small Google Maps link, notes as an icon.
- Compact card view on phones.
- **Foreign currency:** receipts in CHF, PLN, CZK, GBP, SEK, DKK and others are converted to euro at the ECB daily rate of the receipt date. The note holds the original amount, the euro amount and the rate used. If no rate is available the values stay unchanged and the note warns you.
- **Category from the receipt:** the AI recognises AdBlue, oil, washer fluid, car wash and other accessories and creates its own accessory entry (a refuelling entry is never overwritten). If a photo cannot be read, the "manual entry" dialog opens with the photo. If the AI is overloaded (Google 503) you get a warning instead of a wrong message.
- **Photos:** readable file names (`2026-10-15_1240_Oil_Merchant.jpg`), stored compressed; accessory rows are tinted, the list has a row cursor and is sorted by number descending by default. Test receipts (also crumpled, faded, badly lit) are in `tests/test_images_zubehoer/`.
- **CSV export** (Excel-friendly) and **print/PDF** (portrait or landscape, with or without receipts).

### Example printout

The print (button "Print" in the panel) produces a list of all entries and, if wanted, the receipts with the photo pairs after it. The example comes from the [test images](tests/test_images/README.md) (all dummy data): 18 entries, numbered and sorted by date (the oldest is no. 1), with a total line (entries, litres, cost, date created). A few consumption values deviate, for example for the oil receipt (no. 7) or where an intermediate stop is missing; those are quirks of the test data.

<table>
<tr>
<td align="center"><img src="docs/beispiel-ausdruck-liste.png" alt="Example printout: list" width="360"><br><sub>Page 1: the list</sub></td>
<td align="center"><img src="docs/beispiel-ausdruck-belege.png" alt="Example printout: receipts" width="360"><br><sub>Page 2: receipt and odometer photos per entry</sub></td>
</tr>
</table>

The complete example (7 pages) as PDF: [docs/beispiel-ausdruck.pdf](docs/beispiel-ausdruck.pdf).

## Sensors, event and services

Per vehicle: **status**, **last refuelling**, **last price**, **consumption** (average of the last 5, full-to-full), **cost 12 months**. On every detected refuelling the event `drive_energy_doc_refuel` is fired (for your own automations). Services: `drive_energy_doc.export_csv` (writes `config/drive_energy_doc/<name>.csv`), `drive_energy_doc.submit_text` (feed text in like a message) and `drive_energy_doc.test_message`.

## Installation and setup

**Marketplace / HACS:** In the Home Assistant Marketplace (from 2026.11; before that in HACS) add the repository `AlphaLima/ha-drive-energy-doc` as a custom repository (type *Integration*; this connects a GitHub account), install, restart HA. Updates appear there as soon as a new release is published; beta versions are only shown to those who enable pre-releases. **Manually:** copy the folder `custom_components/drive_energy_doc` to `config/custom_components/` and restart HA.

Then *Settings → Devices & services → Add integration → Drive Energy Doc*:

1. Create the **global settings**: price source (automatic by country or fixed), Tankerkönig key (Germany only), electricity price, AI (empty = Gemini automatically, otherwise an `ai_task` entity; how to set up the AI: [Setting up the AI for receipt reading](#setting-up-the-ai-for-receipt-reading)), message channels (Companion, Telegram, WhatsApp; the WhatsApp credentials are entered here too, the Telegram token is entered at the vehicle).
2. **Add a vehicle:** only name, energy type (diesel/E5/E10/electric) and tank volume or battery capacity are required. **Optional:** level sensor (in %), odometer sensor, `device_tracker`. Without these sensors there is no automatic detection; entries are then created only by photo/text or in the panel, and every receipt without a matching entry automatically creates a new one (pure photo mode). Also optional: licence plate and country (before saving you see the drawn plate and the vehicle picture as a preview), vehicle type, language of the bot's replies, vehicle picture, Telegram chat.
3. Thresholds (5 %, 60 s, 250 m) and message channels can be changed per vehicle under *Configure*.

Requirements: Home Assistant 2025.8 or newer; to read receipts an `ai_task` integration (Gemini, OpenAI, Anthropic …).

## Setting up the AI for receipt reading

Receipts and odometer photos are read by an AI. Drive Energy Doc uses **Home Assistant's AI Task feature** for this, so it uses an AI integration you have already set up there. This project has no AI connection of its own. Without AI everything else keeps working: you then type quantity and amount (`45.93 105.13`) or a mileage (`km 54210`).

**Step by step (example Google Gemini):**

1. **Add the AI integration:** *Settings → Devices & services → Add integration → Google Gemini* (called "Google Generative AI" in older guides). Home Assistant's official guide: [Google Gemini](https://www.home-assistant.io/integrations/google_generative_ai_conversation).
2. **Create an API key:** at [Google AI Studio](https://aistudio.google.com/app/apikey) (free according to the Home Assistant guide as long as the Google Cloud project has no billing) and enter it during setup.
3. **Check the AI Task entity:** The AI integration provides an *AI Task* entity for jobs such as reading receipts (background: [AI Task](https://www.home-assistant.io/integrations/ai_task/)). You can see it under *Settings → Devices & services → Entities* (search for `ai_task`) and pick a preferred one under *Settings → System → AI*.
4. **In Drive Energy Doc:** in the **global settings** leave the "AI" field **empty**: the integration then uses the Gemini entity automatically, otherwise the first `ai_task` entity it finds. Or you choose a specific one there.
5. **Test:** upload a receipt photo in the panel. After a few seconds the entry appears in the list.

**Other providers:** Any AI integration that provides AI Task entities and understands **images** works, for example [OpenAI](https://www.home-assistant.io/integrations/openai_conversation/) ([key](https://platform.openai.com/account/api-keys), a paid service according to Home Assistant) or [Anthropic](https://www.home-assistant.io/integrations/anthropic/) ([key](https://console.anthropic.com/settings/keys), also paid). How accurately poorly photographed odometers are read depends on the model.

**Good to know:**
- **Privacy:** The photo goes to **the AI provider** for evaluation, so it leaves your home. According to Home Assistant, Google uses requests and responses of the free plan to improve its products; with billing on the project that does not apply. Check your provider's terms before sending receipts with personal data.
- **Overload:** Free services sometimes report "high demand" (error 503). The integration then retries once after 3 seconds. If nothing comes back, the photo stays saved and you type quantity and amount or the mileage.
- **Requests:** One request per photo goes to the AI, with at most one retry after a quick failure.

## Setting up Telegram
Telegram is the easiest channel: free, no business account, and Home Assistant does not need to be reachable from the internet (the integration polls Telegram itself).

**You need:** a Telegram account and about five minutes.

1. **Create a bot.** In Telegram open the contact **@BotFather**, send `/newbot`, choose a display name and a username (must end in `bot`). BotFather replies with the **token** (looks like `123456789:ABC…`). The token is like a password: do not share it or show it in screenshots.
2. **Enable the channel (once).** *Settings → Devices & services → Drive Energy Doc → "Drive Energy Doc settings" → Configure → Channels, price source, AI* and tick **Telegram** under channels.
3. **Find the chat ID.** Write a message to the new bot in Telegram (e.g. `/start`). Then open `https://api.telegram.org/bot<TOKEN>/getUpdates` in a browser (put your token in place of `<TOKEN>`) and look for the number after `"chat":{"id":`. That is the chat ID (negative for groups). If the bot is already entered at another vehicle, it answers `/start` from a new chat by itself with the chat ID.
4. **Enter it at the vehicle.** *Drive Energy Doc → vehicle → Configure → Messaging → Telegram*: enter the **bot token** and the **chat ID**. The switch **"Send test message"** checks immediately whether everything works: the message arrives in the chat and as a notification in Home Assistant.
5. **Use it.** Send the bot receipt photos, odometer photos or text (see [Receipt, accessories and odometer by message](#receipt-accessories-and-odometer-by-message)). `?` lists all commands.

**Several vehicles or drivers (fleet):** You can use **one** bot for all vehicles. Each vehicle then gets its **own chat ID**: every driver writes to the bot in their own chat, or you create one group per vehicle, add the bot and **make it an administrator of the group** (see below). The assignment to the vehicle is done by the chat ID alone. Alternatively create one bot per vehicle.

**If nothing arrives:**
- The bot does not answer at all: check the token, and whether a **second program** polls the same token (Node-RED, `telegram_bot` with polling, a second Home Assistant). A token may be polled by **one** program only.
- The bot says the chat ID is "not assigned to a vehicle": enter the number at the right vehicle.
- **In a group nothing happens when you send a photo? Make the bot an administrator of the group.** By default Telegram only passes commands (like `/help`) to a bot in a group, but no normal messages or photos. Admins see everything. In Telegram: open the group → **⋮ (three dots) → Manage group → Administrators → Add administrator** → choose your bot → Save (no special rights needed). Test with a photo or `/help`. If a message from the group shows up in the Home Assistant log as "not assigned to a vehicle", the bot already receives it and only the chat ID is missing at the vehicle.
- Alternative to the admin status: at @BotFather `/setprivacy` → choose the bot → **Disable**, then remove the bot from the group and add it again.
- Foreign chats are never processed; only messages from the entered chat ID are accepted.

## Setting up WhatsApp (Meta's official Cloud API)
WhatsApp takes more effort than Telegram, but is handy if your drivers use WhatsApp anyway. It uses **Meta's official WhatsApp Cloud API**.

**You need:**
- a Meta developer account (developers.facebook.com) and an app of type "Business" with the product "WhatsApp",
- a **phone number** for the bot: to try it out Meta provides a test number (recipients have to be added there first), for real use your own number registered with WhatsApp,
- Home Assistant must be reachable **from the internet via HTTPS**, without login, at `/api/drive_energy_doc/whatsapp` (e.g. Nabu Casa, Tailscale Funnel, Cloudflare Tunnel or a reverse proxy). Meta calls this address when a message arrives.

**Steps:**
1. In the Meta app under *WhatsApp → API setup* note the **phone number ID** and create a **permanent access token** (via a system user in the Business Manager; the temporary token expires after 24 hours). The **app secret** is under *App settings → Basic*.
2. In Home Assistant *Drive Energy Doc → "Drive Energy Doc settings" → Configure → WhatsApp access*: enter the token, phone number ID, a **verify token of your choice** and the app secret. Without the app secret the integration does not process incoming messages (the origin cannot be verified). Tick **WhatsApp** under channels (*Channels, price source, AI*).
3. In the Meta app under *WhatsApp → Configuration → Webhook* enter: callback URL `https://<your-public-HA-address>/api/drive_energy_doc/whatsapp`, the same **verify token**, and subscribe to the field **`messages`**.
4. At the vehicle (*Configure → Messaging → WhatsApp*) enter the **driver's number**, with country code, without `+` and spaces (e.g. `4917012345678`). Only messages from this number are accepted. The switch "Send test message" checks the path.
5. **Important, the 24-hour rule:** WhatsApp only allows unsolicited messages (e.g. "Refuelling detected") within 24 hours of the driver's last message. After that only an **approved template** (category *Utility*) with a text such as `Drive Energy Doc: {{1}}` works. Enter the template name and language code in the WhatsApp settings. Without a template the message only arrives while the window is open. Replies to the driver's messages are always possible.

Note: Meta's prices and rules change; check with Meta for the cost of template messages and the requirements for the business account.

## Languages
The panel and the bot speak **36 languages**: German, English, French, Spanish, Italian, Dutch, Portuguese, Polish, Czech, Slovak, Slovenian, Croatian, Serbian, Bosnian, Macedonian, Bulgarian, Ukrainian, Belarusian, **Russian**, Romanian, Hungarian, Greek, Turkish, Albanian, Lithuanian, Latvian, Estonian, Finnish, Swedish, Danish, Norwegian, Icelandic, Irish, Maltese, Luxembourgish and Catalan.
- **Panel:** follows the language of the signed-in HA user automatically; if it is not available, English is shown.
- **Bot replies:** configurable per vehicle (*Configure → Vehicle*, field "Language of the bot's replies"), default is the Home Assistant language. So every vehicle of a fleet can answer in its driver's language.
- **Commands:** `?`, `help`, `extra`, `+`, `yes`/`no`/`new` and the short words for consumables are understood in **all** languages, independent of the reply language.
- The setup dialogs in Home Assistant are available in German and English (other languages fall back to English).
- The translations were produced with AI assistance; corrections are welcome as an issue or pull request (files in `custom_components/drive_energy_doc/frontend/i18n/`).

## Data and privacy
- All entries and photos are stored **locally** in your HA installation (`.storage` and `config/drive_energy_doc/`). There is no server run by the author.
- Only the following leave your system: the price query (position ≈ surroundings of a station, sent to the price service), messages to Telegram/WhatsApp, and receipt photos to the AI you chose (`ai_task`).
- Tokens and keys are stored in the integration's configuration; do not share diagnostics or backups without checking them.

## Limits
- The level must be available in **percent**.
- The accuracy of the place depends on how quickly the car reports level and position (see above).
- The AI can misread numbers on photos (especially poor odometer photos or confused numbers on receipts). Therefore: receipt values win over estimates, and a doubtful odometer reading is left out instead of guessed. Check the list from time to time.
- Photos sent via Telegram and WhatsApp have no EXIF; there the time of the message counts, so send odometer and receipt pairs promptly.
- The integration is still young (0.1.x); please report bugs as an issue.

## Tests
`python tests/test_detector.py`, `test_receipt.py`, `test_stats.py`, `test_plate.py` (without Home Assistant).

To try it out, `tests/test_images/` holds **20 entirely fictional photo pairs** (receipt and odometer, from easy to hard to read) with the correct values in CSV files and a small script (`vergleich.py`) that checks your CSV export against the expected values, so you can test the recognition yourself, see [tests/test_images](tests/test_images/README.md).

## License
MIT
