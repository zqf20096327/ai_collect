# FTMO Trading Bot

[![tests](https://github.com/Dahshan228/FTMO-TradingBot/actions/workflows/tests.yml/badge.svg)](https://github.com/Dahshan228/FTMO-TradingBot/actions/workflows/tests.yml)
[![license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![python](https://img.shields.io/badge/python-3.11%2B-blue.svg)

Multi-strategy algorithmic trading bot for FTMO MT5 prop accounts. Three independent bots run side-by-side on a shared account with full FTMO compliance baked in: 5%/10% loss limits, 8-10% stagnation rule, 30-day inactivity rule, post-target evaluation flow.

| Bot | Strategy | Symbol | Sizing |
|---|---|---|---|
| Equity | LightGBM 3-class on `^GSPC` daily bars | US500 (CFD) | Full Kelly capped at 30% |
| BTC | Golden cross 3/50 MA, 1.5× ATR stop | BTCUSD | 15% per trade |
| Forex | Golden cross, multi-pair | GBPJPY / USDJPY / CHFJPY | 10% per pair |

Backtest 2015-2025: **+12.97% gross CAGR / +7.81% live** (60% live haircut for slippage + spread + swap). 11/12 profitable years. Max DD 13.50% peak-to-trough, -7.69% from a fresh start. See `HISTORY.md` for the year-by-year table and the research that drove every parameter.

---

## Quick start

### Windows (recommended)

```powershell
git clone https://github.com/Dahshan228/FTMO-TradingBot.git
cd FTMO-TradingBot
.\setup.ps1
```

`setup.ps1` creates `.venv`, installs all dependencies (including the Windows-only `MetaTrader5` SDK), scaffolds `.env` from `.env.example`, and runs the preflight check. Idempotent — re-runnable. Flags:

- `-Force` — wipe and rebuild `.venv` from scratch
- `-SkipPreflight` — skip the final preflight check (e.g. unattended installs)

If PowerShell blocks the script: `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`, or run as `powershell -ExecutionPolicy Bypass -File .\setup.ps1`.

After the first run: edit `.env` with your FTMO credentials, install + log into the MT5 terminal under that account (Algo Trading enabled), then re-run `.\setup.ps1` to confirm preflight reports GO.

### Manual setup (any platform)

```bash
pip install -r requirements.txt -c constraints.txt
cp .env.example .env
```

`constraints.txt` pins the full dependency set from the last verified-green test run — LightGBM/numpy/pandas drift can subtly change model behavior, so live deployments should always install with `-c`.

Then edit `.env`:

```bash
ALPACA_API_KEY=...
ALPACA_SECRET_KEY=...
FTMO_MT5_ACCOUNT=...
FTMO_MT5_PASSWORD=...
FTMO_MT5_SERVER=OANDA-Demo-1
DISCORD_WEBHOOK_URL=...     # optional
```

> macOS / Linux: the MetaTrader5 SDK is Windows-only (pip skips it via `sys_platform` marker). Backtests, training, dashboard, and tests run cross-platform; live trading requires Windows.

### One-time model training

Model artifacts are `.gitignore`'d (`models_*/`). On a fresh clone:

```bash
python -m src.data.backfill --primary GSPC
python -m src.model.run_training --primary GSPC --tune --save-dir models_gspc_full_kelly
python -m src.model.compute_baseline --primary GSPC \
    --model models_gspc_full_kelly/production.lgb \
    --out config/signal_baseline.json
```

~3 min tuned. Alternatively, copy `models_gspc_full_kelly/` + `config/signal_baseline.json` from another machine.

### Launch (4 terminals — supervisors auto-restart on crash)

```bash
python -m scripts.run_forever         # Terminal 1: equity bot
python -m scripts.run_forever_btc     # Terminal 2: BTC bot
python -m scripts.run_forever_forex   # Terminal 3: forex bot
streamlit run src/broker/dashboard.py # Terminal 4: dashboard
```

Or use the dashboard's "Start All" button to spawn all three supervisors from one terminal.

---

## Architecture

```
                        FTMO MT5 Account
                             |
              +--------------+--------------+
              |              |              |
        +-----+-----+  +-----+-----+  +-----+-----+
        |  EQUITY   |  |    BTC    |  |   FOREX   |
        |  LightGBM |  |  3/50 MA  |  | 3-pair MA |
        |  30% cap  |  | 15% size  |  | 10%/pair  |
        |  NYSE hrs |  | 24/7 daily|  | 24/5 daily|
        | News-gate |  | 1.5x ATR  |  | per-pair  |
        |   "mt5"   |  | "mt5_btc" |  |"mt5_forex"|
        +-----+-----+  +-----+-----+  +-----+-----+
              |              |              |
              +--------------+--------------+
                             |
                  +----------+-----------+
                  | SHARED INFRASTRUCTURE|
                  |  MT5Adapter          |
                  |  FTMO Compliance     |
                  |  SQLite (per-bot)    |
                  |  Combined cap (75%)  |
                  |  Consensus sizing    |
                  |  Discord             |
                  |  Streamlit dashboard |
                  +----------------------+
```

All three bots connect to the same MT5 terminal, see the same account equity, maintain independent state (`provider="mt5"` / `"mt5_btc"` / `"mt5_forex"` in SQLite), and independently enforce FTMO 5%/10% loss limits.

**Combined max exposure: 75%** (30% equity + 15% BTC + 30% forex from 3 pairs × 10%). At FTMO Swing 1:30 forex leverage that's ~2.5% margin used on $100K equity — well below FTMO's leverage ceiling.

---

## Strategies

### Equity bot (LightGBM)

LightGBM 3-class classifier on `^GSPC` (S&P 500 cash index, not SPY). Trained on 20 years of daily bars, walk-forward validated across 13 folds. Trades the US500 CFD on FTMO.

| Metric | Value |
|---|---|
| Profitable folds | 11/13 |
| Median Sharpe | 0.66 |
| Worst single-fold DD | 3.83% (2025) |
| EV per trade (gross) | 40 bps |
| Win rate / payoff | 63.3% / 1.02 |
| Profit factor | 1.81 |
| SHAP-stable features | 16/22 (73%) |
| Total trades (13 yrs) | 381 |

Execution params (Optuna-tuned): SL 2.63× ATR, TP 2.30× ATR, trail 3.0%, partial 23.4% at 8.2% MFE, time-stop 208 daily-bar-equivalents (~8 trading days). Signal threshold 0.079.

Each NYSE cash-hours 15-min bar:
1. Mark-to-market any open position
2. Check inner-ring + FTMO gates; halt if tripped
3. Check news gate; skip entries within 30 min of FOMC/CPI/NFP
4. If in a position: run all stops (SL → TP → trailing → partial → time)
5. If flat: compute signal `P(UP) - P(DOWN) in [-1, +1]`; enter if `|signal| > 0.079` AND outside ATR-adaptive flat zone AND regime not blocked
6. Submit order with idempotent magic-number tracking + SL/TP attached
7. Verify SL attached post-fill; defensive `modify_stops` if missing
8. Persist state atomically

Model artifacts: `models_gspc_full_kelly/production.lgb` + sidecar JSONs.

### BTC bot

Rule-based golden cross on daily BTCUSD bars. Long-only — short-side blowups during bull squeezes are documented and costly.

| Rule | Setting |
|---|---|
| Entry | Long when 3d MA > 50d MA |
| Exit | Death cross (3 < 50) OR 1.5× ATR stop OR 4% inner kill |
| Size | 15% of equity, plus B6 add-on (50% of base size) at +1 ATR profit |
| Main BE lock | Enabled — when B6 fires, main SL moves to entry too |
| Bar source | MT5 D1 with yfinance fallback if <200 bars |
| Cadence | Daily 00:15 UTC + hourly signal check, 5-min stop monitor |

### Forex bot

Same trend logic as BTC, parametric over 3 pairs running in parallel under one scheduler. Daily 00:20 UTC + hourly check, 5-min stop monitor.

| Pair | Fast / Slow MA | Size | ATR stop |
|---|---|---|---|
| GBPJPY.sim | 5 / 20 | 10% | 2× |
| USDJPY.sim | 5 / 20 | 10% | 2× |
| CHFJPY.sim | 10 / 30 | 10% | 3× |

Forex differs from BTC in two ways: B6 add-on fraction is **75%** instead of 50% (forex's positive JPY carry rewards bigger in-trend positions; BTC's negative swap punishes them), and a pre-close gate blocks fresh entries within 120 min of Friday 17:00 ET close (FTMO weekend-gap rule).

### Trend-bot per-tick logic (BTC + forex)

In a position?
- Death cross → close at market (cascades to close any B6 add-on)
- ATR stop hit → close
- Inner kill hit (≥4% loss on position) → close
- B6 enabled, profit ≥ 1.0 × ATR_at_entry, no add-on yet, combined cap allows → submit add-on with SL at original entry; if `lock_main_at_be: true` (BTC), also move main SL to entry

Flat?
- Golden cross active → enter long at `base_size × consensus_multiplier` with SL at entry - `atr_mult × ATR`
- Otherwise stay flat

### Scale-on-Profit add-on (B6)

For each open position, once unrealized profit reaches `1.0 × ATR_at_entry`:

1. Compute the proposed add-on size (`addon_fraction × base_position_pct`)
2. Run combined-exposure check including the proposed add; skip if it would breach the 75% cap
3. Submit market buy with SL placed at the **original entry price** (break-even on the add)
4. Track add-on as a separate broker ticket nested in the position dict; persist across restart
5. On main close (death cross / ATR / FTMO halt / control bus), cascade-close the add-on too

The break-even stop on the add caps its worst-case at zero gross PnL — distinct from earlier pyramiding experiments that stacked ATR stops and accumulated drawdown across the stack. Walk-forward validated 4/4 sub-windows positive on every BTC and forex pair.

Per-bot add-on fraction: BTC 50%, forex 75%. Both bots opt in via `broker.<bot>.scale_on_profit.enabled: true`.

### Cross-bot consensus sizing

Each bot publishes its current direction (`-1` / `0` / `+1`) to SQLite on every tick. When a bot considers a new entry, it reads the other bots' last-published directions and applies a multiplier based on cross-bot agreement:

| Agreement count `|c|` | Multiplier |
|---|---|
| 3 (all aligned) | 1.00× |
| 2 | 0.85× |
| 1 | 0.65× |
| 0 (split) | 0.50× |

Applies to **new entries only** — open positions are unaffected. Backtest: -1.6% income for **-16.4% MaxDD reduction**, +0.06 Sharpe, 2018 worst-year DD -12.21% → -10.13%. Toggle via `risk.consensus_sizing_enabled`.

---

## Risk management

**Four layers of defense per bot:**

1. **ATR stop loss** — server-side, attached to position; broker fires automatically
2. **Inner kill switch** — bot-side, 4% per BTC/forex position OR 6% peak-relative for equity
3. **FTMO daily loss** — 5% from prev-day close → bot halts
4. **FTMO overall loss** — 10% from initial balance → bot kills + flattens

**Plus combined-exposure cap (75%):** every bot checks the others' open positions (including active B6 add-ons) before entering or firing an add. Worst-case stack post-CHFJPY: 30% equity + 15% BTC + 30% forex = 75% (exactly at cap). With B6 active, theoretical max stack rises to 30% + 22.5% + 45% = 97.5%, so the cap actively throttles add-ons during multi-bot busy periods — by design, keeps multi-bot drawdown survivable against -10% correlated tail events at FTMO's 10% floor.

**Two-ring detail:**

| Ring | Trigger | Action |
|---|---|---|
| Inner — equity bot kill | 6% peak-relative DD | Permanent halt until reset |
| Inner — equity bot daily | 3% from start-of-day | Pause until next reset |
| Inner — equity bot circuit | 3 stop-loss exits in 60 min | 2-hour cooldown |
| Inner — BTC/forex per-position | 4% loss on position | Close position |
| Outer — FTMO daily | 5% from `max(prev-close, initial)` | Pause |
| Outer — FTMO overall | 10% from initial balance | Kill + flatten |
| Outer — consistency | Single day > 50% of total profit | Warn |

Inner ring fires first in normal conditions (3% < 5%, 6% < 10%). Outer ring catches the asymmetric winning-streak edge case where a built-up account makes the inner ring more permissive than FTMO's prev-day baseline.

Both rings fire on every CFD bar (23/5), not just NYSE cash hours.

---

## FTMO compliance

### Drawdown band tracker (Clause 12.2.3(b) — 8-10% stagnation)

> *"You maintain a loss in the FTMO Challenge Account in the amount between 8% and 10% (included) of the Initial Simulated Capital for a period longer than thirty (30) calendar days"* → account terminated.

Sitting at -9% for 30 days terminates the account regardless of whether you breach -10%. Separate failure mode from the daily/overall loss limits.

Dashboard pill:

| Band | DD | Status |
|---|---|---|
| Green | <5% | Safe |
| Yellow | 5-8% | Watching |
| Orange | ≥8%, days_in_danger <20 | Recovery window |
| Red | ≥8%, days_in_danger ≥20 | Termination imminent |

Auto-flatten at -8% would lock realized losses and stop trading — exactly how the stagnation rule terminates accounts. Right behavior is to alert and let the bots grind toward recovery. Daily snapshot job sends a Discord one-shot when DD crosses into orange, with an escalating message at red.

### Inactivity tracker (Clause 12.2.3(a) — 30-day no-trade rule)

Slow trend-followers can hold a single position for 60+ days without opening anything new. Holding doesn't reset the timer — only NEW entries do.

| Band | Days since last entry | Status |
|---|---|---|
| Green | <15 | Safe |
| Yellow | 15-25 | Watching |
| Red | 25+ | Open a trade or account terminates |

Reads from `closed_trades.open_time` + currently-open position records. Equity bot adds ~25-40 trades/year and usually backfills BTC/forex gaps. You **cannot** open a fake trade to reset the timer — FTMO explicitly detects this.

### Daily snapshot job

`scripts/daily_snapshot.py` runs once a day at 17:00 ET (1h after NYSE close, after MT5 settles) inside the equity bot's APScheduler. Writes two append-only tables:

- **`daily_snapshots`** — one row per date per provider with balance, equity, margin used/free/level, open P/L, # positions
- **`closed_trades`** — one row per closed MT5 position (idempotent on `position_id`), pulled from `mt5.history_deals_get()`

Feeds the dashboard performance view, the FTMO drawdown tracker, and the Discord stagnation alert.

### Request FTMO Evaluation control

Clause 5.8.6 requires every position flat before phase evaluation. Dashboard → Danger Zone → **Request FTMO Evaluation** → type YES → broadcasts `close_position` + `pause` to all 3 bots. Once flat, submit the phase evaluation in your FTMO client area.

---

## Trading modes

| `provider` | `mode` | What it is | Real money |
|---|---|---|---|
| `alpaca` | `paper` | Alpaca paper trading | No |
| `alpaca` | `live` | Alpaca live API | **Yes** |
| `mt5` | `demo` | FTMO Free Trial demo | No |
| `mt5` | `challenge` | FTMO paid Challenge / Verification | No |
| `mt5` | `funded` | FTMO Funded (post-Challenge) | **Yes** |

Real-money modes require explicit confirmation at startup — interactive `Type 'YES'` prompt OR `SPY_BOT_LIVE_CONFIRMED=YES` env var (parallel: `BTC_BOT_LIVE_CONFIRMED`, `FOREX_BOT_LIVE_CONFIRMED`).

### Demo → Funded symbol migration

FTMO Demo uses a `.sim` suffix on every symbol; funded accounts drop it. Same MT5 server sources both books — the suffix scopes which one your trade lands on.

| Bot | Demo | Funded |
|---|---|---|
| Equity | `US500.sim` | `US500` |
| BTC | `BTCUSD.sim` | `BTCUSD` |
| Forex | `GBPJPY.sim`, `USDJPY.sim`, `CHFJPY.sim` | `GBPJPY`, `USDJPY`, `CHFJPY` |

**Steps when funding:**

1. Edit `config/settings.yaml` — strip `.sim` from `broker.mt5.symbol`, `broker.btc.symbol`, every `broker.forex.pairs[].symbol`
2. Set `broker.mt5.mode: funded`
3. Update `.env` with funded credentials if they differ; update `broker.mt5.server` if FTMO assigned a different server name
4. Run `python -m scripts.preflight` — the funded-symbol guard fails with a list if any `.sim` is left
5. Smoke test with equity bot first (one trade, verify it lands on `US500` not `US500.sim`) before re-enabling BTC + forex

The `MT5Adapter._resolve_symbol` refuses to launch with `.sim` symbols against a funded server (raises `BrokerAPIError`) — fail-fast, not silent mistrade.

### Demo as a live proxy

Demo P&L is an accurate proxy for funded performance. Demo runs on OANDA's real demo server, sourcing prices, swap rates, commissions, and margin behavior from the same liquidity provider FTMO uses on funded.

The **60% live-degradation multiplier** in the backtest (13.0% gross → 7.8% live) is the buffer for symbol naming differences, stress-condition slippage, and order-routing scrutiny on funded. See `HISTORY.md` for the 9-day reconciliation that validated the proxy.

---

## Operations

### Pre-flight

```bash
python -m scripts.preflight
# Expected: PASSED 56  WARNINGS 0  FAILED 0  -> "GO"
```

Runs ~30 environment, config, credential, model-artifact, and MT5-connectivity checks. Optional sanity: `pytest tests/ -q` (1494+ passing) and `grep -oE '^[A-Z_]+' .env | sort` to verify credentials.

### Sunday-night launch (dashboard one-click)

1. Confirm MT5 terminal is running and Algo Trading is enabled:
   - Logged into your FTMO Demo / Challenge / Funded account
   - Toolbar `Algo Trading` button is GREEN
   - `Tools → Options → Expert Advisors`: "Allow algo trading" checked
   - Right-click each symbol in Market Watch → Show: `US500.sim`, `BTCUSD.sim`, `GBPJPY.sim`, `USDJPY.sim`, `CHFJPY.sim`

2. Launch dashboard: `streamlit run src/broker/dashboard.py` — browser opens at http://localhost:8501. Header should show `[MT5] OANDA-Demo-1`.

3. Click `▶ Start All` in the Bots panel. The dashboard spawns all three supervisors as detached subprocesses; they survive a dashboard restart. To stop everything: `■ Stop All`.

4. Discord should fire one `Bot Started` notification per bot.

### Sunday-night launch (manual 4-terminal fallback)

If the dashboard is unavailable or you want to stream each bot's stdout to a separate window:

```bash
# Terminal 1
python -m scripts.run_forever
# Watch for: MT5Adapter connected, FTMO compliance loaded, Scheduler started, Discord "[Equity] Bot Started"

# Terminal 2 (after equity bot stable ~30s)
python -m scripts.run_forever_btc
# Watch for: BTCTrendRunner starting, Discord "[BTC] Bot Started"

# Terminal 3
python -m scripts.run_forever_forex
# Watch for: ForexTrendRunner starting, per-pair config lines, Discord "[FOREX] Bot Started"

# Terminal 4
streamlit run src/broker/dashboard.py
```

### Monitor first 24 hours

| What | Where | Healthy |
|---|---|---|
| Bar arrival timing | Dashboard heartbeat | ≤16 min stale during NYSE cash session |
| MT5 disconnects | `trading.log` / `btc_trading.log` / `forex_trading.log` | Zero `Bar stream stalled` warnings |
| FTMO gate trips | Log lines `FTMO ... LIMIT HIT` | None expected |
| Position sizing | First entry log per bot | Matches `quantize_size`; forex lots ≤1.0 |
| SL attached | `_verify_sl_attached` log | `OK`, not `defensive modify_stops` |
| Discord notifications | Webhook channel | One `Bot Started` per bot, then per-trade only |
| Forex symbol routing | First forex order | `symbol=GBPJPY.sim` (NOT `US500.sim`) |
| Combined exposure | Dashboard FTMO panel | Usually 0%; spikes to ≤75% under max-positions stack |

### Critical: do NOT

- Run multiple instances of the same bot against the same FTMO account — provider-scoped state writes will collide
- Manually close bot-opened positions via MT5 GUI without first pausing the bot — startup reconcile will halt or clear
- Change `.env` while bots are running — credentials cached at startup
- Change `kelly_fraction` or `max_position_pct` mid-position — sizing math goes weird until next entry
- Switch `mt5.mode: funded` without stripping `.sim` from every symbol — preflight will fail with the offending list

### Recurring operator tasks

| Cadence | Task | How |
|---|---|---|
| Every session | Launch MT5, verify Algo Trading green, verify symbols subscribed, launch supervisors | See Sunday launch above |
| Daily (~30s) | Glance at dashboard heartbeat, DD pill, inactivity pill, Discord channel | Dashboard |
| Every 14 days | FTMO Demo renewal | Re-register in FTMO client area; update `.env`; delete `data/trading.db` + WAL/SHM sidecars; restart bots |
| Event-driven | Clear halt flag after kill-switch / MT5-disconnect trip | Dashboard "Resume" (equity) or `sqlite3 data/trading.db "DELETE FROM state WHERE key='mt5_btc:halted'"` (BTC/forex) |
| Event-driven | Request FTMO Evaluation when profit target hits | Dashboard → Danger Zone → "Request FTMO Evaluation" → YES |
| Quarterly | Model retraining | `python -m scripts.retrain_scheduler` (auto-promotes + refreshes baseline + sends `reload_model`) |
| Quarterly | Economic calendar refresh | Edit `config/economic_calendar.json` from Fed/BLS/BEA/ECB/BoJ/BoE sources (URLs in `StaticFileProvider` docstring) |
| Before 2031 | Extend NYSE + CFD calendars | Edit `src/broker/market_calendar.py` and `src/broker/cfd_calendar.py` — both fail closed past coverage |
| As needed | Log rotation | Manually rotate `trading.log` / `btc_trading.log` / `forex_trading.log` / `dashboard.log` |

### Dead-man's switch (recommended for live)

Bot-side alerting cannot cover machine death — if the PC dies, the FTMO gates and Discord alerts die with it while positions stay open at the broker with only server-side stops standing. Set `DEADMAN_PING_URL` in `.env` to a [healthchecks.io](https://healthchecks.io)-style ping URL; every supervisor pings it every 5 minutes, and the external service alerts you when pings stop.

### Dashboard security

The Streamlit dashboard has **no authentication** — its Danger Zone can flatten every position. It binds to localhost by default; never launch it with `--server.address 0.0.0.0` or expose the port beyond the local machine.

### Automated (don't touch)

- Daily MT5 account snapshot (17:00 ET)
- Daily SQLite backup to `data/backups/` (17:30 ET, 14-day retention)
- Weekly economic calendar runway check (Sunday 18:00 ET)
- FTMO daily baseline reset (17:00 Europe/Prague — broker EOD)
- Heartbeat (every 10s)
- Drift detection (every 60 min)
- Engine ↔ broker reconcile (every 30 min)
- Stream-stall watchdog (every 60s)
- BTC + per-pair forex stop monitors (every 5 min)
- Weekly Discord summary (Friday 16:15 ET)

---

## Configuration

All parameters live in `config/settings.yaml`. A gitignored `config/settings.local.yaml` (same name + `.local` for any settings file) deep-merges over the base file at load time — put account-specific values and any private parameter retunes there, restating only the keys that differ. **If you run this against a real FTMO account, retune at least the trend-bot parameters in your local override**: everyone running the public defaults produces near-identical trades, and FTMO's prohibited-practices rules cover duplicated trading patterns across accounts.

The knobs operators actually touch:

| Key | Default | When to change |
|---|---|---|
| `broker.mt5.mode` | `demo` | Switch to `challenge` / `funded` when funding |
| `broker.mt5.symbol`, `broker.btc.symbol`, `broker.forex.pairs[].symbol` | `*.sim` | Strip `.sim` when funding |
| `broker.mt5.server` | `OANDA-Demo-1` | FTMO assigns `FTMO-Server2` / `Server3` for paid accounts |
| `broker.mt5.challenge_initial_balance` | account-dependent | Match your funded account size |
| `broker.btc.scale_on_profit.*`, `broker.forex.scale_on_profit.*` | enabled | Disable to revert to base-size-only |
| `risk.consensus_sizing_enabled` | `true` | Disable to revert to independent bot sizing |
| `risk.combined_exposure_cap_pct` | 0.75 | Lower it to throttle multi-bot stress |
| `risk.daily_loss_limit_pct`, `risk.kill_switch_pct` | 0.03 / 0.06 | Tighten if you want inner ring more aggressive than FTMO 0.05/0.10 |
| `model.path` | `models_gspc_full_kelly/production.lgb` | Update after a retrain that promotes |

Everything else (kelly_fraction, max_position_pct, news gate, live loop tuning) is set and shouldn't move without backtest justification. See `HISTORY.md` for which values were tuned and why.

---

## Project layout

```
src/
  config.py                      # YAML + env var loader
  data/                          # backfill + yfinance/MT5 fetchers
  features/                      # 22 daily features, labels, regime classifier,
                                 # news_sentiment (R&D, not promoted)
  model/                         # LightGBM training, predict, validate, SHAP, backtest
  execution/                     # sizing, stops, engine, scale_on_profit, backtest
  strategies/                    # btc_trend (primitives), btc_runner, forex_runner,
                                 # shadow + shadow_runner (paper-only validation)
  broker/                        # MT5 + Alpaca adapters, streams, dashboard,
                                 # news_gate, calendars, control_bus, job_manager,
                                 # health, intent, main.py, btc_main.py, forex_main.py,
                                 # shadow_main.py
  risk/                          # risk_manager, ftmo_compliance, combined_exposure,
                                 # consensus_sizing, divergence_monitor, swap_rates
scripts/                         # supervisors (incl. run_forever_shadow), preflight,
                                 # snapshot, backup, combined_backtest, retrain_scheduler,
                                 # divergence_alert, fetch_gdelt_*, generate_synthetic_gdelt
config/                          # settings.yaml, settings.production.yaml,
                                 # settings.dress_rehearsal.yaml, shadow_strategies.yaml,
                                 # economic_calendar.json, signal_baseline.json
tests/                           # 1494 tests
```

---

## Notifications

Discord webhooks (optional — set `DISCORD_WEBHOOK_URL` to enable). All three bots send to the same webhook with bot prefixes:

- `[Equity]` — LightGBM trades on US500
- `[BTC]` — golden-cross BTC trades
- `[FOREX]` — multi-pair forex; body includes `Symbol:` line for pair disambiguation

Price formatting:
- Equity / BTC: `$1234.56` (2 decimals, dollar prefix)
- Forex: `1.10523` (5 decimals, no dollar)

Webhook URL is type-only-logged on errors (the secret never appears in stack traces).

---

## Tests

```bash
pytest tests/                       # all 1494 tests
pytest tests/ -k mt5                # filter
pytest tests/strategies/            # BTC + forex runner tests
pytest tests/risk/                  # FTMO compliance + combined exposure tests
pytest tests/test_job_manager*.py   # multi-bot supervisor dispatch tests
pytest tests/test_daily_snapshot.py # daily snapshot + closed-trade tests
```

Tests use the `mock_mt5` fixture (`tests/conftest.py`) to stub the MetaTrader5 module via `sys.modules` — they run on any platform without an MT5 terminal.

---

## Troubleshooting

| Symptom | Cause / fix |
|---|---|
| "Model file not found" | Run `python -m src.model.run_training --primary GSPC --tune`; update `model.path` in `settings.yaml` |
| "FTMO server reports HEDGING mode" warning | Expected on FTMO Free Trial demos — adapter auto-routes closes to close-by-ticket. Paid accounts may be netting (no warning then) |
| "0 bars in last 24h" from `get_bars` | Symbol not subscribed in MT5 Market Watch — right-click → Show |
| Server `OANDA-Demo-1` at startup | Expected on FTMO Free Trial (FTMO whitelabels OANDA). Paid accounts run on `FTMO-Server2` / `FTMO-Server3` |
| BTC bot can't fetch 200 daily bars from MT5 | Expected on new FTMO Demo (limited crypto history). Yfinance fallback kicks in — check `btc_trading.log` for "Falling back to yfinance" |
| "FTMO DAILY LIMIT HIT" | Bots should auto-pause. If not, pause manually via dashboard Control Plane and investigate logs for missed gate checks |
| `--live` aborts non-interactively | Run from interactive terminal and type YES, or set `SPY_BOT_LIVE_CONFIRMED=YES` (parallel: `BTC_BOT_LIVE_CONFIRMED`, `FOREX_BOT_LIVE_CONFIRMED`) |
| "DB has position but broker does not" | Position was closed externally (e.g., manually in MT5 GUI). Bot auto-reconciles on startup |
| "Combined exposure cap reached" | New entry / add-on would exceed 75%. Skipped by design — wait until an existing position closes |
| Halt flag set, can't trade | BTC/forex halts persist across restarts (intentional). Clear: `sqlite3 data/trading.db "DELETE FROM state WHERE key='mt5_btc:halted'"` (or `mt5_forex:halted`). Equity uses dashboard "Resume" |
| Forex `signal_check` runs but no entries | (a) no golden cross on any pair, (b) blocked by combined-exposure cap (`combined exposure ...% would exceed cap` log), or (c) yfinance fallback (entries blocked until MT5 catches up) |
| "No symbol matching pattern *.sim*" on funded | Run preflight — funded-symbol guard lists offenders. See migration checklist |
| "MissingTickerError: ... ['SPY']" | Bot is running pre-fix code — stop and restart |
| Dashboard shows ORPHAN / "RUNNING (no supervisor)" | Bot alive but no supervisor PID. Operationally fine; only auto-restart is missing. Dashboard → Stop All → Start All to restore (don't double-launch — would spawn duplicates) |
| Daily snapshot table empty | Equity bot hasn't run a full 17:00 ET cycle yet, or MT5 was unreachable. Run manually: `python -m scripts.daily_snapshot` (idempotent) |
| Inactivity pill red | No new trade in 25+ days. Clause 12.2.3(a) terminates at 30. Cannot fake-trade to reset (FTMO detects). Wait for a genuine signal |
| Bot crashed | With supervisor, auto-restarts (30s → 60s → 120s backoff, capped 5 min, 10 restarts/hour brake). Halt state, position state, and FTMO baseline persist via SQLite |
| Calendar coverage past 2030 | NYSE + CFD calendars fail closed. Extend `market_calendar.py` and `cfd_calendar.py` before 2031 |

---

## Known limitations

Documented deliberately — knowing where the edges are is part of the risk management.

- **The equity model's edge is statistically fragile.** CPCV puts the probability of backtest overfitting at 0.588, and the headline "11/12 profitable years" is a post-selection statistic from many sequential research waves over the same 2015–2025 data. The risk containment is the proven part of this system; the alpha is a monitored hypothesis (see the divergence alerter).
- **Gap risk is structurally understated by daily-close backtests.** All three bots are long-risk-assets; in a correlated shock (e.g., a JPY carry unwind) they draw down together, and stops do not protect against gaps — a weekend or overnight gap fills at the open, past the stop. FTMO's 5% daily limit is breached intraday; the backtest can't see that.
- **The 60% live-degradation multiplier rests on a 9-day demo reconciliation** in calm conditions. Live BTC swap already measured ~20% worse than modeled; the divergence monitor exists to catch further drift, not prevent it.
- **Live features depend on yfinance** (VIX/HYG/TLT complex plus the BTC fallback) — an unofficial data path that rate-limits and occasionally breaks. Staleness alerts and degraded modes mitigate; a paid feed would fix.
- **Public parameters are copyable.** Anyone running the unmodified trend-bot defaults on FTMO produces near-identical trades to every other clone, which FTMO's duplicate-pattern detection may flag. Retune privately via `config/settings.local.yaml`.
- **Scheduled-event news gate only.** Unscheduled events (BoJ interventions, flash crashes) are not gated — inherent to daily-cadence trend following.

## Disclaimer

This project is provided for educational and research purposes only. It is not financial advice, and nothing here is a recommendation to trade any instrument. Trading CFDs, forex, and crypto involves substantial risk of loss. Backtest results do not guarantee future performance. If you run this software against a live or funded account, you do so entirely at your own risk.

## License

[MIT](LICENSE)
