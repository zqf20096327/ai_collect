# hermes-market-skills

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Status: active](https://img.shields.io/badge/status-active-success.svg)](#status)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Issues](https://img.shields.io/github/issues/jagres0039/hermes-market-skills.svg)](https://github.com/jagres0039/hermes-market-skills/issues)
[![Last commit](https://img.shields.io/github/last-commit/jagres0039/hermes-market-skills.svg)](https://github.com/jagres0039/hermes-market-skills/commits/main)

Market-analysis skills for the [Hermes](https://github.com/aiandi/hermes) AI agent. Three independent skills covering the asset classes the agent (Gresman) is asked about most often:

| Skill | Scope | Trigger keywords (Bahasa / English) |
| --- | --- | --- |
| `skills/crypto` | Cryptocurrencies (BTC, ETH, altcoins, on-chain metrics) | `crypto`, `btc`, `eth`, `coin`, `token`, `defi`, ticker like `SOL`, `DOGE` |
| `skills/saham_idn` | Indonesian stock market (IDX / BEI) | `saham`, `ihsg`, `bbri`, `bbca`, `tlkm`, `asii`, ticker with `.JK` |
| `skills/forex_comm` | Forex pairs + commodities (gold, oil, silver, copper) | `forex`, `eurusd`, `usdjpy`, `gold`, `xau`, `oil`, `silver`, `komoditas` |

Each skill is **self-contained**: own data feed, own analysis logic, own CLI. The skills share TA / charting / LLM-summary helpers from `skills/_shared/`.

## Status

| Skill | v1 (price/ta/analyze) | v2 (`recommend`) | v3 (SMC + backtest) |
| --- | --- | --- | --- |
| `_shared` (TA, chart, llm, signals, patterns, sentiment, news, telegram, macro, **smc**, **backtest**) | done | done | done |
| `crypto` | done | done — TA + funding + F&G + dominance + leverage hint | **done — SMC overlay default ON; `backtest` subcommand** |
| `saham_idn` | done | done — TA + fundamental overlay (PER/yield/EPS) + IHSG context | n/a (cash market, no perp/futures — SMC not applicable) |
| `forex_comm` | done | done — TA + DXY overlay + economic calendar window | **done — SMC overlay default ON; `backtest` subcommand** |

## Quick start

```bash
# 1. clone
git clone https://github.com/jagres0039/hermes-market-skills.git
cd hermes-market-skills

# 2. install python deps (uses uv if available, falls back to pip)
python3 -m pip install --user -r requirements.txt

# 3. set free-tier API keys in env (all skills work without them, with reduced coverage)
export COINGECKO_API_KEY=""          # optional — boost rate limit
export TWELVEDATA_API_KEY=""         # optional — forex OHLCV (free 800/day)
export CRYPTOPANIC_API_KEY=""        # optional — crypto news feed

# 4. try each skill
python3 -m skills.crypto.analyze        price BTC
python3 -m skills.saham_idn.analyze     price BBRI
python3 -m skills.forex_comm.analyze    price XAUUSD
```

## CLI pattern (shared by all three skills)

```
python3 -m skills.<asset>.analyze <command> <symbol> [flags]

  price <symbol>             current price, 24h change, volume
  ta    <symbol> [--tf TF]   indicators (RSI, MACD, BB, EMA, Ichimoku, Fib)
  analyze <symbol> [--tf TF] full report (price + TA + news + opinion + chart PNG)
  recommend <symbol> [--tf]  v2 — BUY/SELL/LONG/SHORT/HOLD/WAIT verdict
                             with entry zone, stop loss, 3-tier take profit
  backtest  <symbol> [--tf]  v3 — walk-forward simulation of the rule engine
                             on historical OHLCV; aggregated metrics
                             (crypto + forex_comm only)
  news  <symbol|topic>       latest news + sentiment scoring
  compare <a> <b>            head-to-head comparison
  watchlist [add|rm|list] s  manage per-skill watchlist (JSON file)
```

`<TF>` is `1h`, `4h`, `1d` (default), `1w`.

### `recommend` flags

```
--tf TF             timeframe (1h | 4h | 1d | 1w), default 1d
--mtf               multi-timeframe confluence (cross-check 1w/1d/4h alignment)
--risk PROFILE      conservative (default) | balanced | aggressive
--no-smc            disable Smart Money Concepts overlay (crypto + forex_comm only;
                    default ON in v3 — empirically improves expectancy across
                    BTC/ETH/SOL and EURUSD/GBPUSD/XAUUSD on the daily TF)
--no-news           skip RSS news fetch (faster, no sentiment overlay)
--no-telegram       skip Telegram channel ingestion (use RSS only)
--no-narrative      skip LLM narrative (rule-based summary only)
```

Conservative profile gates a tradeable verdict on `|score| >= 4.0 AND first RR >= 2.0`. Below the gate the verdict is automatically demoted to `WAIT` (crypto/forex) or `HOLD` (saham, long-only).

### Smart Money Concepts (SMC) overlay (v3)

The SMC layer in `skills/_shared/smc.py` adds **structure-aware votes** on top of classical TA. Pure pandas/numpy — no extra dependencies. Default **ON** for `crypto` and `forex_comm` (disable per-call with `--no-smc`). Saham IDN does not use SMC (cash market, no perp/futures liquidity to exploit).

Detectors:

- **Swings** — fractal pivot (bar is swing-high/low when its high/low is extremum within ±N bars).
- **Market structure** — walks alternating swings to classify `HH/HL/LH/LL`, then emits `BOS` (break of structure, continuation) or `CHoCH` (change of character, reversal) when a close pierces the prior swing extreme.
- **Order Blocks (OB)** — last opposing candle before an impulsive ATR-scaled move; tagged as `bullish` (demand) or `bearish` (supply) with mitigation status.
- **Fair Value Gap (FVG)** — 3-candle imbalance where bar 1's wick and bar 3's wick do not overlap; tracked until filled.
- **Liquidity sweeps** — recent swing high/low pierced intrabar but the close rejects back inside the prior range (a.k.a. stop hunt).
- **Premium / Discount zone** — Fib 0.5 split of the last range; signals when current close is in the upper half (premium, short bias) vs lower half (discount, long bias).

The rule engine votes off this structure: e.g. `BOS bullish` → +1 long vote (weight 0.6); `liquidity sweep bullish` (recent low pierced + close rejects) → +1 long vote (weight 2.0); `premium zone` → +1 short vote (weight 0.5). Votes feed the same gated scorer as the classical TA — SMC adds signal, not a separate decision path.

### `backtest` subcommand (crypto + forex_comm)

Walk-forward simulation of the rule engine on historical OHLCV. No lookahead bias. Entry at the bar **after** the signal (`next_open` by default), intrabar SL / TP1 / TP2 / TP3 checking each subsequent bar, max-hold timeout, then aggregated metrics per backtest.

```
python3 -m skills.crypto.analyze backtest BTC --tf 1d
python3 -m skills.crypto.analyze backtest BTC --tf 1d --no-smc           # classic-only baseline
python3 -m skills.forex_comm.analyze backtest GBPUSD --tf 1d --risk balanced
```

Output JSON includes per-trade list (`open_ts`, `side`, `entry`, `stop`, `targets`, `exit_price`, `exit_reason`, `bars_held`, `pnl_pct`, `r_multiple`, `verdict_at_open`, `confidence`, `score`) plus aggregated metrics: `trades`, `win_rate_pct`, `avg_r`, `total_r`, `expectancy_r`, `profit_factor`, `max_drawdown_r`, `long_trades` / `short_trades`, `avg_bars_held`. Backtest is deterministic (offline; macro / news / Telegram are intentionally excluded so results are reproducible — the live `recommend` engine still uses them).

Flags: `--risk PROFILE`, `--no-smc`, `--warmup N` (skip first N bars to let TA stabilize, default 250), `--max-hold N` (close position after N bars, default 20), `--cooldown N` (bars between trades, default 1), `--entry-mode {next_open,close}`, `--no-trades` (omit per-trade list).

Output is always JSON to stdout. Charts are saved to `OUT_DIR` (default `/tmp/hermes-charts/`) and the path is included in the JSON. Hermes uses the JSON to compose the natural-language reply (Bahasa Indonesia, default tone: educational + opinionated).

## Data sources (all free tier by default)

**Crypto** — CoinGecko (price + market cap), Binance public REST via CCXT (OHLCV), DeFiLlama (TVL), CryptoPanic (news).

**Saham IDN** — Yahoo Finance via `yfinance` with `.JK` suffix (OHLCV + fundamentals), IDX official scrape (composite stats), RSS from Bisnis Indonesia / Kontan (news).

**Forex + Commodities** — TwelveData (forex OHLCV), Yahoo futures tickers (`GC=F` gold, `SI=F` silver, `CL=F` oil WTI, `BZ=F` brent, `NG=F` natgas, `HG=F` copper), ForexFactory scrape (economic calendar).

**News + Sentiment (v2)** — RSS feeds (CoinDesk, Cointelegraph, Decrypt for crypto; Bisnis Indonesia, Kontan, IDN Financials for saham; Investing.com Forex News, Reuters Markets for forex) merged with optional Telegram channels (Telethon user session, read-only). VADER polarity + finance keyword overlay + optional 9router LLM scoring; weighted aggregation feeds the recommendation engine.

**Macro overlays (v2)** — BTC dominance (CoinGecko `/global`), Binance perp funding rate, Fear & Greed Index (`alternative.me/fng`), DXY (`DX-Y.NYB`), IHSG (`^JKSE`).

See each skill's `README.md` for the full source list and rate-limit notes.

## Telegram channel ingestion (v2, optional)

The recommendation engine can read messages from Telegram channels you have already joined (read-only, via a Telethon user session — not a bot).

One-time setup:

```bash
# 1. Get free API id/hash from https://my.telegram.org → API development tools
export TELEGRAM_API_ID=1234567
export TELEGRAM_API_HASH=abcdef0123456789abcdef0123456789
export HERMES_TG_SESSION=~/.agent/credentials/telegram-user.session

# 2. Run interactive login (prompts for phone + OTP from Telegram)
python3 scripts/telegram_login.py
chmod 600 ~/.agent/credentials/telegram-user.session

# 3. List the channels you want Hermes to read in tg-channels.yaml
cat > ~/.agent/credentials/tg-channels.yaml <<'EOF'
channels:
  - id: "@example_crypto_signals"
    category: crypto       # crypto | saham | forex | macro
    tags: [BTC, ETH]
    weight: 0.8            # 0..1 — how much to trust this channel
  - id: "@example_idx_news"
    category: saham
    tags: [IHSG, BBRI]
    weight: 0.9
EOF
export HERMES_TG_CHANNELS_FILE=~/.agent/credentials/tg-channels.yaml
```

Once configured, `recommend` automatically merges Telegram messages (filtered by `category` + `tags`) with RSS news for sentiment scoring. Pass `--no-telegram` to skip.

## Repository layout

```
hermes-market-skills/
├── README.md
├── LICENSE                       # MIT
├── SECURITY.md                   # no-secret-in-repo policy
├── .gitignore
├── requirements.txt
├── pyproject.toml
├── skills/
│   ├── _shared/                  # shared library (NOT a skill, internal use only)
│   │   ├── __init__.py
│   │   ├── ta.py                 # technical analysis indicators
│   │   ├── chart.py              # matplotlib chart helper
│   │   ├── llm_summary.py        # wrapper around 9router LLM for narrative analysis
│   │   ├── http_cache.py         # tiny on-disk HTTP cache to be polite to free APIs
│   │   └── output.py             # JSON output formatting + watchlist storage
│   ├── crypto/
│   │   ├── __init__.py
│   │   ├── analyze.py            # CLI entrypoint
│   │   ├── feeds.py              # CoinGecko + CCXT + DeFiLlama + CryptoPanic adapters
│   │   ├── SKILL.md              # Hermes-facing skill manifest
│   │   └── README.md
│   ├── saham_idn/
│   │   ├── __init__.py
│   │   ├── analyze.py
│   │   ├── feeds.py              # yfinance + IDX scrape + RSS
│   │   ├── SKILL.md
│   │   └── README.md
│   └── forex_comm/
│       ├── __init__.py
│       ├── analyze.py
│       ├── feeds.py              # TwelveData + Yahoo commodities + ForexFactory
│       ├── SKILL.md
│       └── README.md
├── scripts/
│   ├── install-to-hermes.sh      # symlinks skills/ into ~/.hermes/skills/research/market/
│   └── smoketest.sh              # runs `price` on a known-good symbol for each skill
└── tests/
    └── ...
```

## Hermes integration

Each skill ships a `SKILL.md` that Hermes parses to discover its commands, trigger keywords, and required env vars. To wire all three skills into a running Hermes installation:

```bash
bash scripts/install-to-hermes.sh
```

The installer creates a symlink at `~/.hermes/skills/research/market/` pointing to this repo's `skills/` directory, so updates from `git pull` are picked up immediately.

## License

MIT — see [LICENSE](LICENSE). No warranty. Nothing in this repository constitutes financial advice. Trade at your own risk.
