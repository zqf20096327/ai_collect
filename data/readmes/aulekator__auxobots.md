# Auxobots

**Grid Trading Bot with Django Dashboard – Powered by Nautilus Trader**

Auxobots is an open-source, self-hosted grid trading bot with a modern dashboard interface.  
It supports **live** and **demo** (testnet) trading on Binance USDT-M futures using the Nautilus Trader framework.

Main features include:

- Geometric / dynamic grid strategy with volatility adaptation
- Built-in risk controls (max drawdown, exposure limits, trailing stop, breakout protection, margin monitoring)
- Trend-aware asymmetric take-profits
- Isolated per-user bot processes (live & demo)
- Real-time dashboard showing PnL, positions, open orders, logs
- Easy configuration via web interface (API keys, pair, quantity, etc.)

**⚠️ Important Warning**  
This software interacts with real financial markets.  
Trading involves substantial risk of loss.  
Use at your own risk. See [DISCLAIMER.md](DISCLAIMER.md).

## Features

- Live & Binance Testnet support
- Dynamic grid adjustment based on ATR/volatility & trend detection (SMA crossover + price slope)
- Safety triggers: max drawdown %, exposure limits, margin ratio, breakout detection, trailing stop
- Auto-recenter grid on drift
- Per-user isolation (separate processes / threads)
- Dashboard: metrics, positions, orders, recent trades, terminal-style logs
- Logging to database (searchable, auto-cleanup)
- Extensible strategy class (`GridStrategy`)

## System Architecture

```mermaid
graph TB
    subgraph "Frontend Layer"
        F1[Django Templates]
        F2[Dashboard UI]
        F3[Web Interface]
    end

    subgraph "Application Layer"
        A1[Live Trading Bot]
        A2[Demo Trading Bot]
        A3[Grid Strategy Engine]
        A4[Django Views/Controllers]
    end

    subgraph "Data Layer"
        D1[MySQL Database]
        D2[Bot Configurations]
        D3[Trade History]
        D4[User Data]
    end

    subgraph "Trading Engine Layer"
        T1[Nautilus Trader Core]
        T2[Binance Adapter]
        T3[Exchange APIs]
        T4[Market Data]
    end

    subgraph "Infrastructure Layer"
        I1[Multi-process Manager]
        I2[Session Isolation]
        I3[Signal Handlers]
        I4[Error Recovery]
    end

    F1 --> A4
    A4 --> D1
    A1 --> T1
    A2 --> T1
    A3 --> A1
    A3 --> A2
    T1 --> T2
    T2 --> T3
    I1 --> A1
    I1 --> A2
```

## Prerequisites

Make sure you have these installed and set up before proceeding:

### Required Software
- **Python 3.12+** - Download from [python.org](https://www.python.org/downloads/)
- **Django 4.x+** - Web framework for the project
- **Nautilus Trader** - Trading framework (will be installed via requirements.txt)

### Required Accounts
- **Binance Account** - For obtaining API keys (live or demo)

### Development Environment
- **Virtual Environment** (`venv`) - For managing Python dependencies
 
## Installation

Follow these steps to set up and run the project locally:

### 1. Clone the Repository
- git clone https://github.com/aulekator/auxobots.git
- cd auxobots

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

pip install -r requirements.txt

# Django Configuration
- SECRET_KEY=your_django_secret_key_here
- DEBUG=True  # Set to False in production
- ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration (choose one)
- DATABASE_URL=sqlite:///db.sqlite3  # For development
- DATABASE_URL=postgresql://user:password@localhost:5432/auxobots  # For production

# Binance API (optional - can be configured per user in UI)
- BINANCE_API_KEY=your_binance_api_key_here
- BINANCE_API_SECRET=your_binance_api_secret_here

# Optional: Trading Configuration
- DEFAULT_EXCHANGE=BINANCE
- DEFAULT_MARKET=BTCUSDT

# Run migrations
- python manage.py makemigrations
- python manage.py migrate

# Create superuser (admin account)
python manage.py createsuperuser

python manage.py runserver

# Start bot runner (in a separate terminal)
python manage.py run_live_bot_runner

## Usage

Once installed, here's how to use the trading bot system:

### Dashboard
- **Access**: Navigate to `/dashboard/` (login required)
- **Features**:
  - Configure API keys (Binance)
  - Set trading instrument (e.g., `SOL`, )
  - Define position quantity
  - Start/stop trading bots in real-time
  - Monitor bot performance and status

### Trading Modes

#### Live Trading
- **Purpose**: Execute trades with real funds on Binance
- **Setup**: 
  1. Enable in configuration settings
  2. Add valid Binance API keys (with trading permissions)
  3. Start via dashboard interface
- **Warning**: Uses real money - test thoroughly first!

#### Demo Trading
- **Purpose**: Test strategies risk-free using Binance Testnet
- **Setup**:
  1. Get test API keys from [Binance Testnet](https://testnet.binance.vision/)
  2. Configure in dashboard
  3. Start demo bot
- **Recommended**: Use for strategy testing and development

### Customization

#### Strategy Parameters
Edit `grid_strategy.py` to modify trading logic:

# Example configuration
- GRID_LEVELS = 15            # Number of grid levels
- GRID_OFFSET = 0.08          # Price offset between grids (8%)
- MAX_POSITION_SIZE = 0.01    # Maximum position size in BTC
- STOP_LOSS_PERCENT = 0.05    # Stop loss percentage (5%)
- TAKE_PROFIT_PERCENT = 0.10  # Take profit percentage (10%)

## Contributing

We welcome contributions! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute to this project.

### Quick Contribution Steps:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Need Help?
- Check open [issues](https://github.com/aulekator/auxobot/issues)
# Join our Discord
- (https://discord.gg/tafKjBnPEQ)