# Hermes3 (H3)

Advanced Web3 AI Agent featuring dynamic parsing and multi-chain support for sophisticated blockchain interactions and real-time analytics.

## Features

### Transaction Management
- Smart contract interactions
- Token swaps and transfers
- Gas optimization
- Multi-chain support (Base, Ethereum, Polygon)

### Real-time Analytics
- Contract analysis and security auditing
- Price monitoring and alerts
- Volume and liquidity tracking
- Historical data analysis
- Technical analysis with multiple timeframes

### Market Intelligence
- Social sentiment analysis (requires Twitter API)
- Price-sentiment correlation
- Market trend monitoring
- Token metrics tracking
- Technical indicators and chart analysis

### Configuration Management
- Dynamic chain and token management
- Custom token and chain addition
- Flexible parameter configuration

## Requirements

![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![PostgreSQL](https://img.shields.io/badge/postgresql-16.4-blue.svg)
![Web3](https://img.shields.io/badge/web3-6.11.1-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey.svg)
![Twitter API](https://img.shields.io/badge/Twitter%20API-v2-00acee.svg)
![Google AI](https://img.shields.io/badge/Google%20AI-Gemini%201.5-red.svg)
![Status](https://img.shields.io/badge/status-beta-yellow.svg)

Developed with Python 3.13. Requires minimum Python 3.10.
Database: PostgreSQL 16.4 or higher.

### Dependencies
```
web3==6.11.1          # Ethereum interface
python-dotenv==1.0.0  # Environment management
tweepy==4.14.0        # Twitter API interface
pandas==2.1.1         # Data manipulation
numpy==1.24.3         # Numerical operations
textblob==0.17.1      # Text analysis
tabulate==0.9.0       # Table formatting
plotext==5.2.8        # Terminal plotting
colorama==0.4.6       # Terminal colors
requests==2.31.0      # HTTP requests
google-generativeai==0.3.1  # Google AI integration
psycopg2-binary==2.9.9     # PostgreSQL interface
goplus-sdk-py==1.0.4       # Security API
```

Note: Some system-specific modules (like `msvcrt` for Windows) are built-in and not listed in requirements.

## Installation

```bash
git clone https://github.com/arpahls/hermes3.git
cd hermes3
pip install -r requirements.txt
```

## Configuration

1. Copy `.env.example` to `.env` and fill in your API keys
2. Copy `kun.example.py` to `kun.py` and configure your users
3. Made with Python3.13, min: 3.10

## Commands

### Chat
```
/0x chat
    - Chat with AI agent for natural language interactions
```

### Transaction Commands
```
/0x buy <amount> <token> using <token> on <chain>
/0x sell <amount> <token> for <token> on <chain>
/0x send <chain> <token> <amount> to <recipient>
/0x gas <low|medium|high>
/0x receive
```

### Analysis Commands
```
/0x analyze <contract_address> <chain>
    - Analyzes contract metrics, security, and market data
    - Currently supported chains: Base
    - Example: /0x analyze 0x4ed4e862860bed51a9570b96d89af5e1b0efefed base

/0x ta <token> <chain> [timeframe]
    - Performs technical analysis on tokens
    - Supported timeframes: 1h, 4h, 12h, 24h, 7d, 30d
    - Default timeframe: 24h
    - Example: /0x ta DEGEN Base
    - Example: /0x ta 0x4ed4e862860bed51a9570b96d89af5e1b0efefed Base 7d
```

### Monitoring Commands
```
/0x monitor <contract_address> <chain> [metrics]
    - Monitors token metrics in real-time
    - Optional metrics: reserves, volume, fees (default: all)
    - Example: /0x monitor 0x4ed4e862860bed51a9570b96d89af5e1b0efefed base
    - Example: /0x monitor 0x4ed4e862860bed51a9570b96d89af5e1b0efefed base reserves,volume

/0x monitor live <contract_address> <chain> <threshold>
    - Monitors live transactions above threshold value
    - Threshold in USD (e.g., 50000 for $50k)
    - Example: /0x monitor live 0x4ed4e862860bed51a9570b96d89af5e1b0efefed base 50000

/0x history <contract_address> <chain> [metric_type] [days]
    - Shows historical monitoring data
    - Optional metric_type: reserves, volume, fees (default: all)
    - Optional days: number of days to look back (default: 7)
    - Example: /0x history 0x4ed4e862860bed51a9570b96d89af5e1b0efefed base
    - Example: /0x history 0x4ed4e862860bed51a9570b96d89af5e1b0efefed base volume 30
```

### Configuration Commands
```
/0x new chain
/0x new token
/0x forget chain <name>
/0x forget token <name>
```

### Social Commands
```
/0x twitter <token_symbol>
    - Analyzes social media sentiment and price correlation
    - Example: /0x twitter $DEGEN
    - Example: /0x twitter USDC
```

### Example Interactions
```bash
# Buy tokens
/0x buy 100 DEGEN using ETH on Base

# Monitor contract
/0x monitor 0x4ed4e862860bed51a9570b96d89af5e1b0efefed base volume

# View history
/0x history 0x4ed4e862860bed51a9570b96d89af5e1b0efefed base volume 30

# Technical Analysis
/0x ta DEGEN Base 7d
/0x ta 0x4ed4e862860bed51a9570b96d89af5e1b0efefed Base 24h

# Chat mode
- hey can you please send 10 DEGEN to Ross? Thanks
- I'd like you to analyze the degen contract on base
- can you monitor the degen contract live for TXs over 5k?
- show me technical for DEGEN for 7d
- do a TA on 0x644192291cc835a93d6330b24ea5f5fedd0eef9e on Ethereum
```

## Architecture

- `web3_handler.py`: Core Web3 functionality and command processing
- `web3_handler_x.py`: Social media analysis and market intelligence
- `web3_handler_agent.py`: AI agent interface and natural language processing
- `web3_handler_ta.py`: Technical analysis functionality
- `kun.py`: User management and configuration
- `.env`: Environment variables and API keys

## Dependencies

See `requirements.txt` for complete list of dependencies.

## License

MIT License

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

