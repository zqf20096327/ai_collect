# delhi-bus-reliability

[![CI](https://github.com/RutuK2005/delhi-bus-reliability/actions/workflows/ci.yml/badge.svg)](https://github.com/RutuK2005/delhi-bus-reliability/actions/workflows/ci.yml)
![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue)
![License: MIT](https://img.shields.io/badge/license-MIT-green)

If you take buses in Delhi you know the pattern: nothing for half an hour, then three buses
of the same route turn up together. That's bus bunching. A bus that falls a little behind
finds more people waiting at each stop and slows down further, while the bus behind it
finds empty stops and catches up.

I wanted to put numbers on it. This project takes three months of stop-arrival data for two
Delhi routes (425 and 534), works out headways (time between consecutive buses at a stop),
flags bunching and long gaps, and trains a model to predict arrival times. There's also a
poller for Delhi's live GTFS-Realtime feed, though I don't have an API key for it yet.

![String diagram of route 534](docs/string_diagram.png)

Each line is one bus on route 534 moving up the route over a morning. Red dots are arrivals
less than a quarter of the usual headway after the bus in front. Between 07:00 and 07:50
pairs of buses run glued together for 25+ stops, and it happens again after 10:00.
`busrel plot` picks the day with the median bunching rate for 07:00-11:00, so this is an
ordinary day, not the worst one.

## Running it

```bash
python -m venv .venv
.venv\Scripts\activate            # Windows; on Linux/macOS: source .venv/bin/activate
pip install -e ".[dev]"

busrel fetch-history              # downloads ~19 MB into data/, writes data/processed/events.parquet
busrel analyze --route 534        # bunching tables in the terminal
busrel plot                       # regenerates docs/string_diagram.png
busrel train-eta                  # trains on months 1-2, tests on month 3, saves to models/
busrel serve                      # dashboard at http://127.0.0.1:8000
```

For live data you need a free key from https://otd.delhi.gov.in and the static GTFS zip
from https://otd.delhi.gov.in/data/static/. Then `busrel poll --interval 30` collects
positions (set `OTD_API_KEY` first) and `busrel snap path/to/GTFS.zip` turns them into
stop arrivals. Without a key `busrel poll` just tells you where to get one. `pytest` and
`ruff check .` run the tests and lint; the tests use small synthetic data, no network.

## How it works

Both data sources end up in one table with a row per bus arriving at a stop
(`service_day, route, direction, vehicle_id, trip_id, stop_seq, stop_id, arrived_at`), so
the analysis doesn't care where the data came from. The historical loader reads all 184 day
sheets in the IIIT-Delhi zip, splits each bus's day into trips and drops duplicates,
out-of-order times and fragments under 5 stops. The live poller fetches VehiclePositions
every 30 s (never faster than 20 s) into date-partitioned Parquet, and `snap` matches each
position to the nearest stop on its trip within 60 m.

Headways come from a DuckDB `LAG` window over each stop's arrivals. A headway is bunched if
it's under 25% of the median for that stop and hour of day, and a long gap if it's over 2x
(`--bunch-ratio` and `--gap-ratio` change these).

The ETA model is a scikit-learn `HistGradientBoostingRegressor` that predicts the time from
a bus's current stop to a later one. Its features are route, direction, both stops, number
of stops, hour, a weekday stand-in, the historical median for that stretch, and how long the
last bus to finish the same stretch took. Only buses that reached the destination before
the prediction time count, so it never sees the future. I added a dashboard as well: one
HTML page served by FastAPI, with charts, a replay of any day and a map for live buses.

## What I found

From a full run on the dataset: 924,375 raw rows, 923,102 events after cleaning, 21,127
trips over 92 service days. The raw output is in [docs/results.txt](docs/results.txt).

| route | direction | median headway | bunched | long gaps | wait if evenly spaced | expected wait |
|---|---|---|---|---|---|---|
| 534 | up | 8.3 min | 13.5% | 22.9% | 5.9 min | 12.3 min |
| 534 | down | 8.6 min | 13.6% | 22.3% | 5.9 min | 11.9 min |
| 425 | up | 27.4 min | 10.8% | 19.0% | 18.0 min | 31.5 min |
| 425 | down | 27.3 min | 11.2% | 19.1% | 18.0 min | 32.9 min |

Expected wait is for someone who turns up at a random time. With uneven gaps that's it
E[h^2] / 2E[h] rather than half the average headway, since you're more likely to land in a
long gap. On 534 the uneven spacing about doubles the wait; on 425 it's around 1.8x.

It gets worse through the day. On 534 the bunched share goes from 9.9% at 07:00 to 13.0% at
11:00 and 18.7% at 21:00; on 425 from 7.9% at 07:00 to about 15% by late afternoon. Apart
from the last stop of 534 down, where buses wait anyway, the worst stop-hours are all on
534 down in the evening (stops 49 to 51 at 21:00, stop 15 at 20:00), with 23 to 24% of
headways bunched.

For ETA I held out month 3 (31 days, 938,947 predictions) and compared the model with the
historical median for that stretch and hour, and with "whatever the bus ahead took" (which
was available for 95.7% of predictions):

| horizon | historical median (MAE / P90) | bus ahead (MAE / P90) | model (MAE / P90) |
|---|---|---|---|
| 1-5 stops | 1.25 / 2.83 min | 1.26 / 2.77 min | 1.06 / 2.30 min |
| 6-15 stops | 3.22 / 7.83 min | 2.93 / 6.67 min | 2.48 / 5.58 min |
| 16+ stops | 7.38 / 17.78 min | 6.61 / 15.22 min | 5.07 / 11.48 min |
| all | 3.30 / 8.95 min | 3.04 / 7.82 min | 2.44 / 6.13 min |

Copying the bus ahead already beats the historical median on longer trips, so recent
conditions matter more than what usually happens at that hour. The model cuts overall MAE
by 26% against the historical median and 20% against the bus ahead, and on long trips the
P90 error drops from about 18 to 11.5 minutes.

## Limitations and next steps

The historical data has no coordinates or calendar dates, just stop numbers and Month/Day
indices. I turn Day N of Month M into service day `M*100 + N`, and the weekday stand-in
assumes the days are consecutive, which I can't check. It's also only two routes, and 425
runs every ~27 minutes, so its per-stop medians are noisy. When a tracker drops out, the
next bus's headway looks longer than it really was, so part of the long-gap share isn't real.

The live poller and stop snapping are only tested on synthetic GTFS and protobuf data so
far. Once I have a key I want to run the poller for a few weeks and compare live bunching
with these numbers, show per-bus ETAs in the dashboard, and map 534's stop numbers to real
GTFS stops so the replay can sit on the map.

## Data

Historical data is the IIIT-Delhi bus dataset (https://bus-data.github.io, arXiv:1910.08903),
which `busrel fetch-history` downloads. Live and static GTFS come from Delhi Open Transit
Data, and only vehicle positions are kept. Map tiles are from OpenStreetMap. MIT licensed.
