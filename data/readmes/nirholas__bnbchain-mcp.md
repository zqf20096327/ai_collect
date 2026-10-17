<div align="center">    
 
```   

                                                                                      
    ██████╗ ███╗   ██╗██████╗      ██████╗██╗  ██╗ █████╗ ██╗███╗   ██╗              
    ██╔══██╗████╗  ██║██╔══██╗    ██╔════╝██║  ██║██╔══██╗██║████╗  ██║              
    ██████╔╝██╔██╗ ██║██████╔╝    ██║     ███████║███████║██║██╔██╗ ██║              
    ██╔══██╗██║╚██╗██║██╔══██╗    ██║     ██╔══██║██╔══██║██║██║╚██╗██║              
    ██████╔╝██║ ╚████║██████╔╝    ╚██████╗██║  ██║██║  ██║██║██║ ╚████║              
    ╚═════╝ ╚═╝  ╚═══╝╚═════╝      ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝              
                                                                                      
              ███╗   ███╗ ██████╗██████╗     ███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗  
              ████╗ ████║██╔════╝██╔══██╗    ██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗ 
              ██╔████╔██║██║     ██████╔╝    ███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝ 
              ██║╚██╔╝██║██║     ██╔═══╝     ╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗ 
              ██║ ╚═╝ ██║╚██████╗██║         ███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║ 
              ╚═╝     ╚═╝ ╚═════╝╚═╝         ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝ 
                                                                                       

```

<h1>BNB Chain MCP Server</h1>

<p><strong>The most comprehensive Model Context Protocol server for BNB Chain & EVM blockchains</strong></p>

<p>Enable AI agents to interact with BNB Chain, opBNB, and other EVM networks through natural language</p>
[![MCP](https://img.shields.io/badge/MCP-Compatible-purple?style=flat-square)](https://modelcontextprotocol.io)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue?style=flat-square&logo=typescript)](https://www.typescriptlang.org/)
[![BNB Chain](https://img.shields.io/badge/BNB_Chain-Native-F0B90B?style=flat-square&logo=binance)](https://www.bnbchain.org)

<br/>

[![BNB Chain](https://img.shields.io/badge/BNB_Chain-F0B90B?style=for-the-badge&logo=binance&logoColor=white)](https://www.bnbchain.org)
[![opBNB](https://img.shields.io/badge/opBNB-F0B90B?style=for-the-badge&logo=binance&logoColor=white)](https://opbnb.bnbchain.org)

<br/>

<!-- Animated Demo -->
<img src="assets/demo.svg" alt="BNB Chain MCP Demo" width="800">

<br/><br/>

> ⭐ **If you find this useful, please star the repo!** It helps others discover this project.

<br/>

[📖 Documentation](https://bnbchain-mcp-docs-lp642k3kpa-uc.a.run.app) • [🚀 Quick Start](#-quick-start) • [🛠️ Features](#-features-overview) • [📊 Roadmap](#️-roadmap) • [🤝 Contributing](#-contributing)

</div>

---

## 📋 Table of Contents

- [What is BNB Chain MCP?](#-what-is-bnb-chain-mcp)
- [Quick Start](#-quick-start)
- [Features Overview](#-features-overview)
- [Supported Networks](#-supported-networks)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Data Sources](#-data-sources)
- [Example Conversations](#-example-conversations)
- [Architecture](#-architecture)
- [Roadmap](#️-roadmap)
- [Related MCP Servers](#-related-mcp-servers)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 What is BNB Chain MCP?

**BNB Chain MCP** is a Model Context Protocol (MCP) server optimized for BNB Chain and opBNB, while also supporting other EVM-compatible blockchains. It enables AI assistants like Claude, ChatGPT, and Cursor to interact with blockchain networks through natural language.

### Why BNB Chain MCP?

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│   User: "What's the current price of ETH and show me the best DEX pools"     │
│                                    │                                         │
│                                    ▼                                         │
│   ┌────────────────────────────────────────────────────────┐                 │
│   │              AI Assistant (Claude/ChatGPT)             │                 │
│   │                                                        │                 │
│   │         "Let me check that for you..."                 │                 │
│   └────────────────────────────────────────────────────────┘                 │
│                                    │                                         │
│                                    ▼                                         │
│   ┌───────────────────────────────────────────────────────┐                  │
│   │                  BNB Chain MCP Server                 │                  │
│   │                                                       │                  │
│   │   ┌──────────┐  ┌──────────┐  ┌──────────┐            │                  │
│   │   │CoinGecko │  │GeckoTerm │  │DefiLlama │   ...      │                  │
│   │   └────┬─────┘  └────┬─────┘  └────┬─────┘            │                  │
│   └────────┼─────────────┼─────────────┼──────────────────┘                  │
│            │             │             │                                     │
│            ▼             ▼             ▼                                     │
│   ┌────────────────────────────────────────────────────────┐                 │
│   │                  Blockchain Networks                   │                 │
│   │   BNB Chain  │  Ethereum  │  Arbitrum  │  Polygon      │                 │
│   └────────────────────────────────────────────────────────┘                 │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Key Benefits

| Benefit | Description |
|---------|-------------|
| **Natural Language** | Ask questions in plain English, get blockchain data instantly |
| **Multi-Chain** | One server supports 10+ EVM networks simultaneously |
| **Read + Write** | Query data or execute transactions (with wallet) |
| **Security Built-In** | GoPlus integration for token/contract safety checks |
| **Rich Data** | Prices, DEX pools, TVL, social sentiment, news & more |
| **AI-Native** | Built specifically for LLMs with structured responses |

### Use Cases

<details>
<summary><strong>🔍 Research & Analysis</strong></summary>

- Check token prices and historical data
- Analyze DEX liquidity pools
- Monitor protocol TVL and metrics
- Research new tokens before investing
- Track whale wallets and movements

</details>

<details>
<summary><strong>💹 Trading & DeFi</strong></summary>

- Get swap quotes across DEX aggregators
- Find best yield farming opportunities
- Monitor lending rates on Aave/Compound
- Execute token swaps and transfers
- Bridge tokens across chains

</details>

<details>
<summary><strong>🛡️ Security & Compliance</strong></summary>

- Detect honeypot tokens
- Check for rug pull risks
- Verify smart contract safety
- Screen wallet addresses
- Check token holder distribution

</details>

<details>
<summary><strong>👨‍💻 Development</strong></summary>

- Deploy and verify smart contracts
- Query contract state and events
- Test transactions before execution
- Manage multi-sig operations
- Debug failed transactions

</details>

<br/>

<div align="center">
  <img src="assets/demo-defi.svg" alt="BNB Chain MCP DeFi Demo" width="800">
  <p><em>DeFi tools in action: swap quotes, TVL tracking, and more</em></p>
</div>

---

## 🚀 Quick Start

Get up and running in under 60 seconds!

### Option 1: Claude Desktop (Recommended)

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "bnb-chain-mcp": {
      "command": "npx",
      "args": ["-y", "@nirholas/bnbchain-mcp@latest"]
    }
  }
}
```

<details>
<summary>📁 Config file locations</summary>

| OS | Path |
|----|------|
| **macOS** | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| **Windows** | `%APPDATA%\Claude\claude_desktop_config.json` |
| **Linux** | `~/.config/claude/claude_desktop_config.json` |

</details>

### Option 2: Cursor / VS Code

Add to your MCP settings:

```json
{
  "mcpServers": {
    "bnb-chain-mcp": {
      "command": "npx",
      "args": ["-y", "@nirholas/bnbchain-mcp@latest"]
    }
  }
}
```

### Option 3: ChatGPT Developer Mode

1. Enable [Developer Mode](https://chatgpt.com/#settings/Connectors/Advanced) in ChatGPT settings
2. Start the HTTP server:
   ```bash
   npx @nirholas/bnbchain-mcp@latest --http
   ```
3. In ChatGPT Settings → Apps, click **Create app**
4. Enter your server URL: `http://localhost:3001/mcp`
5. Select the app in conversations via **Developer mode** menu

📖 [Full ChatGPT Setup Guide](https://bnbchain-mcp-docs-lp642k3kpa-uc.a.run.app/mcp-server/chatgpt-setup/)

### Option 4: npx Instant Start

```bash
# stdio mode (Claude, Cursor)
npx @nirholas/bnbchain-mcp@latest

# HTTP mode (ChatGPT Developer Mode)
npx @nirholas/bnbchain-mcp@latest --http

# SSE mode (legacy clients)
npx @nirholas/bnbchain-mcp@latest --sse
```

---

## 🛠️ Features Overview

### Feature Matrix

| Category | Features | Status |
|----------|----------|--------|
| **Swap/DEX** | Token swaps via 1inch, 0x, ParaSwap | ✅ |
| **Bridge** | Cross-chain transfers via LayerZero, Stargate | ✅ |
| **Gas** | Gas prices across chains, EIP-1559 suggestions | ✅ |
| **Multicall** | Batch read/write operations | ✅ |
| **Events/Logs** | Query historical events, decode logs | ✅ |
| **Security** | Rug pull detection, honeypot check, GoPlus integration | ✅ |
| **Staking** | Liquid staking (Lido), LP farming | ✅ |
| **Signatures** | Sign messages, verify signatures, EIP-712 | ✅ |
| **Lending** | Aave/Compound positions, borrow rates | ✅ |
| **Price Feeds** | Historical prices, TWAP, oracle aggregation | ✅ |
| **Portfolio** | Track holdings across chains | ✅ |
| **Governance** | Snapshot votes, on-chain proposals | ✅ |
| **Deployment** | Deploy contracts, CREATE2, upgradeable proxies | ✅ |
| **MEV Protection** | Flashbots Protect, private transactions | ✅ |
| **ENS/Domains** | Register, transfer, renew, set records | ✅ |
| **Market Data** | CoinGecko prices, OHLCV, trending | ✅ |
| **DeFi Analytics** | DefiLlama TVL, yields, fees, protocols | ✅ |
| **Social Sentiment** | LunarCrush metrics, influencers, trending | ✅ |
| **DEX Analytics** | GeckoTerminal pools, trades, OHLCV | ✅ |

### Tool Categories

<details>
<summary><strong>🔗 Core Blockchain (45+ tools)</strong></summary>

| Tool | Description |
|------|-------------|
| `get_chain_info` | Get chain ID, block number, gas price |
| `get_block` | Get block by number or hash |
| `get_transaction` | Get transaction details and receipt |
| `send_transaction` | Send native token transfer |
| `estimate_gas` | Estimate gas for transaction |
| `get_balance` | Get native/token balance |
| `call_contract` | Call view/pure contract functions |
| ... | [See full list →](https://bnbchain-mcp-docs-lp642k3kpa-uc.a.run.app/tools/blockchain) |

</details>

<details>
<summary><strong>💰 Token Operations (30+ tools)</strong></summary>

| Tool | Description |
|------|-------------|
| `get_token_info` | Get name, symbol, decimals, supply |
| `get_token_balance` | Get token balance for address |
| `transfer_token` | Transfer ERC-20 tokens |
| `approve_token` | Approve spending allowance |
| `get_nft_metadata` | Get NFT metadata and traits |
| `transfer_nft` | Transfer ERC-721 NFT |
| ... | [See full list →](https://bnbchain-mcp-docs-lp642k3kpa-uc.a.run.app/tools/tokens) |

</details>

<details>
<summary><strong>🏦 DeFi (50+ tools)</strong></summary>

| Tool | Description |
|------|-------------|
| `get_swap_quote` | Get swap quote from DEX aggregators |
| `execute_swap` | Execute token swap |
| `add_liquidity` | Add liquidity to DEX pools |
| `get_lending_rates` | Get Aave/Compound rates |
| `supply_to_lending` | Supply assets to lending protocol |
| `get_farming_apy` | Get yield farming APY |
| ... | [See full list →](https://bnbchain-mcp-docs-lp642k3kpa-uc.a.run.app/tools/defi) |

</details>

<details>
<summary><strong>🔒 Security (15+ tools)</strong></summary>

| Tool | Description |
|------|-------------|
| `check_token_security` | GoPlus token security analysis |
| `detect_honeypot` | Check if token is honeypot |
| `check_rug_pull` | Assess rug pull risk |
| `get_holder_distribution` | Get top holder breakdown |
| `check_contract_verified` | Verify contract source |
| `screen_address` | Check address risk score |
| ... | [See full list →](https://bnbchain-mcp-docs-lp642k3kpa-uc.a.run.app/tools/security) |

</details>

<details>
<summary><strong>📊 Market Data (25+ tools)</strong></summary>

| Tool | Description |
|------|-------------|
| `get_price` | Get current token price |
| `get_price_history` | Get historical OHLCV data |
| `get_trending_coins` | Get trending tokens |
| `get_tvl` | Get protocol TVL from DefiLlama |
| `get_dex_pools` | Get DEX pool data |
| `get_social_metrics` | Get LunarCrush sentiment |
| ... | [See full list →](https://bnbchain-mcp-docs-lp642k3kpa-uc.a.run.app/tools/market-data) |

</details>

---

## 🌐 Supported Networks

| Network | Chain ID | Native Token | Status |
|---------|----------|--------------|--------|
| **BNB Smart Chain** | 56 | BNB | ✅ Full Support |
| **opBNB** | 204 | BNB | ✅ Full Support |
| **Arbitrum One** | 42161 | ETH | ✅ Full Support |
| **Ethereum** | 1 | ETH | ✅ Full Support |
| **Polygon** | 137 | MATIC | ✅ Full Support |
| **Base** | 8453 | ETH | ✅ Full Support |
| **Optimism** | 10 | ETH | ✅ Full Support |
| **Avalanche C-Chain** | 43114 | AVAX | ✅ Full Support |
| **Fantom** | 250 | FTM | ✅ Full Support |
| **Gnosis** | 100 | xDAI | ✅ Full Support |
| **BSC Testnet** | 97 | tBNB | ✅ Testnet |
| **Sepolia** | 11155111 | SepoliaETH | ✅ Testnet |
| **Goerli** | 5 | GoerliETH | ✅ Testnet |

### Adding Custom Networks

```json
{
  "mcpServers": {
    "bnb-chain-mcp": {
      "command": "npx",
      "args": ["-y", "@nirholas/bnbchain-mcp@latest"],
      "env": {
        "CUSTOM_RPC_56": "https://your-bnb-rpc.com",
        "CUSTOM_RPC_1": "https://your-eth-rpc.com"
      }
    }
  }
}
```

---

## 📦 Installation

### Server Modes

| Mode | Command | Use Case |
|------|---------|----------|
| **stdio** | `npx @nirholas/bnbchain-mcp` | Claude Desktop, Cursor |
| **HTTP** | `npx @nirholas/bnbchain-mcp --http` | ChatGPT Developer Mode |
| **SSE** | `npx @nirholas/bnbchain-mcp --sse` | Legacy HTTP clients |

### From npm (Recommended)

```bash
# Run directly with npx (no install required)
npx @nirholas/bnbchain-mcp@latest

# Or install globally
npm install -g @nirholas/bnbchain-mcp

# Then run
bnbchain-mcp
```

### From Source

```bash
# Clone
git clone https://github.com/nirholas/bnbchain-mcp
cd bnbchain-mcp

# Install dependencies
bun install

# Build
bun run build

# Run dev server (stdio - Claude)
bun dev

# Run dev server (HTTP - ChatGPT)
bun dev:http

# Run dev server (SSE - legacy)
bun dev:sse
```

### Docker

```bash
# Build
docker build -t bnb-chain-mcp .

# Run stdio mode
docker run -it bnb-chain-mcp

# Run HTTP mode
docker run -p 3001:3001 bnb-chain-mcp --http
```

---

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `PRIVATE_KEY` | Wallet private key for transactions | - | No (read-only without) |
| `COINGECKO_API_KEY` | CoinGecko Pro API key | - | No |
| `COINSTATS_API_KEY` | CoinStats API key | - | No |
| `LUNARCRUSH_API_KEY` | LunarCrush API key | - | No |
| `CRYPTOPANIC_API_KEY` | CryptoPanic news API key | - | No |
| `CUSTOM_RPC_<CHAIN_ID>` | Custom RPC for specific chain | - | No |
| `PORT` | HTTP server port | 3001 | No |
| `LOG_LEVEL` | Logging level | info | No |

### Full Configuration Example

```json
{
  "mcpServers": {
    "bnb-chain-mcp": {
      "command": "npx",
      "args": ["-y", "@nirholas/bnbchain-mcp@latest"],
      "env": {
        "PRIVATE_KEY": "0x...",
        "COINGECKO_API_KEY": "CG-xxx",
        "LUNARCRUSH_API_KEY": "xxx",
        "CUSTOM_RPC_56": "https://bsc-rpc.publicnode.com",
        "CUSTOM_RPC_1": "https://eth-rpc.publicnode.com",
        "LOG_LEVEL": "debug"
      }
    }
  }
}
```

### Claude Desktop Configuration

<details>
<summary><strong>macOS</strong></summary>

```bash
# Open config file
open ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

</details>

<details>
<summary><strong>Windows</strong></summary>

```powershell
# Open config file
notepad %APPDATA%\Claude\claude_desktop_config.json
```

</details>

<details>
<summary><strong>Linux</strong></summary>

```bash
# Open config file
nano ~/.config/claude/claude_desktop_config.json
```

</details>

---

## 📊 Data Sources

This MCP server integrates with the following APIs:

| Provider | Data Type | API Key | Rate Limits |
|----------|-----------|---------|-------------|
| [CoinGecko](https://coingecko.com) | Market data, prices, OHLCV | Optional | 10-50 req/min |
| [CoinStats](https://coinstats.app) | Portfolio, prices, wallets | Required | Varies |
| [DefiLlama](https://defillama.com) | TVL, yields, fees, protocols | No | Generous |
| [LunarCrush](https://lunarcrush.com) | Social sentiment, influencers | Required | Varies |
| [GoPlus](https://gopluslabs.io) | Security analysis, honeypot | No | Generous |
| [GeckoTerminal](https://geckoterminal.com) | DEX pools, trades, OHLCV | No | Generous |
| [DexPaprika](https://dexpaprika.com) | DEX analytics, pools | No | Generous |
| [CryptoPanic](https://cryptopanic.com) | Crypto news | Required | Varies |
| [Alternative.me](https://alternative.me) | Fear & Greed Index | No | Generous |

---

## 💬 Example Conversations

### Price Queries

> **User:** "What's the current price of BNB?"
>
> **AI:** *Uses `get_price` tool* → "BNB is currently trading at $XXX.XX, up 2.5% in the last 24 hours."

### Security Checks

> **User:** "Is this token safe? 0x..."
>
> **AI:** *Uses `check_token_security` and `detect_honeypot`* → "⚠️ Warning: This token has several red flags..."

### DEX Analysis

> **User:** "Show me the best BNB liquidity pools"
>
> **AI:** *Uses `get_dex_pools`* → "Here are the top pools on BNB Chain by TVL..."

### Multi-Chain Portfolio

> **User:** "Check my wallet across all chains: 0x..."
>
> **AI:** *Uses `get_portfolio`* → "Your total portfolio value is $X across 5 chains..."

### DeFi Research

> **User:** "What are the best yield farming opportunities on BNB Chain?"
>
> **AI:** *Uses `get_yield_farms` and `get_tvl`* → "Here are the top yield opportunities..."

---

## 🏗️ Architecture

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                          BNB Chain MCP Server                                │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                        │
│  │    stdio     │  │     HTTP     │  │      SSE     │   Transport Layer      │
│  │   (Claude)   │  │   (ChatGPT)  │  │   (Legacy)   │                        │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘                        │
│         │                 │                 │                                │
│         └─────────────────┼─────────────────┘                                │
│                           │                                                  │
│                           ▼                                                  │
│  ┌───────────────────────────────────────────────────────────────────────┐   │
│  │                        MCP Protocol Handler                           │   │
│  │     Tools Registration  |  Resource Management  |  Prompt Templates   │   │
│  └───────────────────────────────────────────────────────────────────────┘   │
│                           │                                                  │
│         ┌─────────────────┼─────────────────┐                                │
│         ▼                 ▼                 ▼                                │
│  ┌────────────┐    ┌────────────┐    ┌────────────┐                          │
│  │ Blockchain │    │   Market   │    │  Security  │    Tool Categories       │
│  │   Tools    │    │    Data    │    │   Tools    │                          │
│  └─────┬──────┘    └─────┬──────┘    └─────┬──────┘                          │
│        │                 │                 │                                 │
│        ▼                 ▼                 ▼                                 │
│  ┌───────────────────────────────────────────────────────────────────────┐   │
│  │                         Provider Integrations                         │   │
│  │   viem | CoinGecko | DefiLlama | GoPlus | LunarCrush | GeckoTerminal  │   │
│  └───────────────────────────────────────────────────────────────────────┘   │
│                           │                                                  │
│                           ▼                                                  │
│  ┌───────────────────────────────────────────────────────────────────────┐   │
│  │                           EVM Networks                                │   │
│  │   BNB Chain | Ethereum | Arbitrum | Polygon | Base | Optimism | ...   │   │
│  └───────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Module Organization

```
src/
├── index.ts              # Entry point
├── server/
│   ├── stdio.ts          # stdio transport
│   ├── http.ts           # HTTP transport
│   └── sse.ts            # SSE transport
├── tools/
│   ├── blockchain/       # Core chain operations
│   ├── tokens/           # Token operations
│   ├── defi/             # DeFi protocols
│   ├── security/         # Security checks
│   ├── market/           # Market data
│   └── social/           # Social sentiment
├── providers/
│   ├── coingecko.ts      # CoinGecko API
│   ├── defillama.ts      # DefiLlama API
│   ├── goplus.ts         # GoPlus Security
│   └── ...
└── utils/
    ├── chains.ts         # Chain configurations
    ├── abi.ts            # Common ABIs
    └── format.ts         # Formatters
```

---

## 🔐 Security

### Security Model

| Feature | Description |
|---------|-------------|
| **Read-Only Mode** | Without `PRIVATE_KEY`, server only reads blockchain state |
| **No Key Storage** | Private keys are never stored, only used in memory |
| **Input Validation** | All inputs validated with Zod schemas |
| **Rate Limiting** | Built-in rate limiting prevents API abuse |
| **Verified Sources** | Only uses reputable data providers |

### Best Practices

- ⚠️ **Never share** your `PRIVATE_KEY` in public configs
- ✅ Use environment variables or secrets management
- ✅ Use read-only mode when possible
- ✅ Always verify token safety before interacting
- ✅ Review transaction simulations before executing

---

## ❓ Troubleshooting

<details>
<summary><strong>Server won't start</strong></summary>

1. Check Node.js version (requires 18+):
   ```bash
   node --version
   ```
2. Clear npx cache:
   ```bash
   npx clear-npx-cache
   ```
3. Try installing globally:
   ```bash
   npm install -g @nirholas/bnbchain-mcp
   ```

</details>

<details>
<summary><strong>Claude Desktop doesn't see the server</strong></summary>

1. Verify config file location and JSON syntax
2. Restart Claude Desktop completely
3. Check logs:
   - macOS: `~/Library/Logs/Claude/mcp*.log`
   - Windows: `%APPDATA%\Claude\logs\mcp*.log`

</details>

<details>
<summary><strong>RPC errors / Rate limiting</strong></summary>

1. Use a dedicated RPC provider (Alchemy, QuickNode, etc.)
2. Configure custom RPC:
   ```json
   "env": {
     "CUSTOM_RPC_56": "https://your-dedicated-rpc.com"
   }
   ```

</details>

<details>
<summary><strong>API key errors</strong></summary>

1. Verify API key is correct (no extra spaces)
2. Check API key has required permissions
3. Verify rate limits haven't been exceeded

</details>

---

## 🗺️ Roadmap

A comprehensive roadmap of all crypto/blockchain/DeFi/Web3 features to be implemented.

### Legend
- ✅ Implemented
- 🚧 In Progress
- 📋 Planned

---

### 🔗 Core Blockchain Operations

#### Network & Chain
| Feature | Status |
|---------|--------|
| Get chain ID, block number, gas price | ✅ |
| Get network status/health | ✅ |
| Switch networks/chains | ✅ |
| Get supported networks list | ✅ |
| Get RPC endpoints | ✅ |
| Estimate block time | ✅ |
| Get chain metadata (name, symbol, explorers) | ✅ |
| Get finality status | ✅ |
| Get mempool/pending transactions | ✅ |
| Get network peers/nodes | ✅ |
| Get gas oracle | ✅ |

#### Blocks
| Feature | Status |
|---------|--------|
| Get block by number/hash | ✅ |
| Get latest block | ✅ |
| Get block transactions | ✅ |
| Get block receipts | ✅ |
| Get uncle blocks | ✅ |
| Subscribe to new blocks | 📋 |
| Get block rewards | ✅ |
| Get block gas used/limit | ✅ |
| Get block range | ✅ |
| Get blocks by miner | ✅ |

#### Transactions
| Feature | Status |
|---------|--------|
| Send transaction | ✅ |
| Get transaction by hash | ✅ |
| Get transaction receipt | ✅ |
| Get transaction status | ✅ |
| Estimate gas | ✅ |
| Speed up transaction (replace with higher gas) | ✅ |
| Cancel transaction | ✅ |
| Decode transaction input | ✅ |
| Simulate transaction | ✅ |
| Get transaction trace | 📋 |
| Get internal transactions | 📋 |
| Batch transactions | ✅ |
| Get pending transactions | ✅ |
| Get transaction history by address | ✅ |

#### Accounts/Wallets
| Feature | Status |
|---------|--------|
| Get balance (native/token) | ✅ |
| Get nonce | ✅ |
| Get transaction count | ✅ |
| Create wallet | ✅ |
| Import wallet (private key/mnemonic) | ✅ |
| Export private key | 📋 |
| Sign message | ✅ |
| Verify signature | ✅ |
| Get address from private key | ✅ |
| Generate mnemonic | ✅ |
| Derive addresses (HD wallet) | ✅ |
| Multi-sig wallet operations | 📋 |
| Get wallet permissions | 📋 |
| Revoke approvals | ✅ |
| Account abstraction (ERC-4337) | 📋 |
| Social recovery | 📋 |
| Hardware wallet integration | 📋 |
| Get wallet portfolio | ✅ |
| Get token approvals | ✅ |

---

### 💰 Token Operations

#### Native Tokens
| Feature | Status |
|---------|--------|
| Get native balance | ✅ |
| Transfer native tokens | ✅ |
| Wrap/unwrap native tokens (WETH, WBNB) | ✅ |

#### ERC-20 (Fungible Tokens)
| Feature | Status |
|---------|--------|
| Get token info (name, symbol, decimals, total supply) | ✅ |
| Get token balance | ✅ |
| Transfer tokens | ✅ |
| Approve spending | ✅ |
| Get allowance | ✅ |
| Transfer from (delegated) | ✅ |
| Burn tokens | ✅ |
| Mint tokens | ✅ |
| Get token holders | ✅ |
| Get token transfers | ✅ |
| Permit (gasless approvals - EIP-2612) | ✅ |
| Batch transfers | ✅ |
| Token snapshots | 📋 |
| Get token supply info | ✅ |
| Check/revoke token approval | ✅ |

#### ERC-721 (NFTs)
| Feature | Status |
|---------|--------|
| Get NFT metadata | ✅ |
| Get NFT owner | ✅ |
| Transfer NFT | ✅ |
| Approve NFT | ✅ |
| Set approval for all | ✅ |
| Get NFTs by owner | ✅ |
| Get NFT collection info | ✅ |
| Mint NFT | 📋 |
| Burn NFT | 📋 |
| Get NFT transfer history | 📋 |
| Get NFT traits/attributes | ✅ |
| Get NFT rarity | 📋 |
| Verify NFT authenticity | 📋 |
| Batch transfer NFTs | ✅ |
| Check NFT approval | ✅ |
| Revoke NFT approval | ✅ |
| Approve for marketplace | ✅ |
| Fetch NFT metadata from URI | ✅ |

#### ERC-1155 (Multi-Token)
| Feature | Status |
|---------|--------|
| Get token balance (fungible + NFT) | ✅ |
| Batch transfers | 📋 |
| Batch balance queries | 📋 |
| Safe transfer | ✅ |
| Get URI | ✅ |

#### Other Token Standards
| Feature | Status |
|---------|--------|
| ERC-777 (advanced fungible) | 📋 |
| ERC-3525 (semi-fungible) | 📋 |
| ERC-4626 (tokenized vaults) | 📋 |
| ERC-6551 (token-bound accounts) | 📋 |
| ERC-404 (hybrid tokens) | 📋 |
| Soulbound tokens (SBTs) | 📋 |

---

### 🏦 DeFi - Decentralized Exchanges (DEX)

#### Swaps
| Feature | Status |
|---------|--------|
| Get quote/price | ✅ |
| Swap exact tokens for tokens | ✅ |
| Swap tokens for exact tokens | ✅ |
| Multi-hop swaps | ✅ |
| Split route swaps | 📋 |
| Cross-DEX aggregation | ✅ |
| Limit orders | 📋 |
| TWAP orders (time-weighted) | 📋 |
| Stop-loss orders | 📋 |
| Get slippage estimate | ✅ |
| Get price impact | ✅ |
| MEV protection (private transactions) | 📋 |

#### DEX Analytics
| Feature | Status |
|---------|--------|
| Get trending pools | ✅ |
| Get new pools | ✅ |
| Get top pools by volume | ✅ |
| Get pool OHLCV data | ✅ |
| Get pool trades | ✅ |
| Get token pools | ✅ |
| Get DEX list | ✅ |
| Search pools cross-chain | ✅ |
| Get token price by contract | ✅ |
| Get pool transactions | ✅ |
| Multi-token price lookup | ✅ |

#### Liquidity Provision
| Feature | Status |
|---------|--------|
| Add liquidity | ✅ |
| Remove liquidity | ✅ |
| Get LP token balance | ✅ |
| Get pool reserves | ✅ |
| Get pool APY/APR | 📋 |
| Get impermanent loss estimate | 📋 |
| Concentrated liquidity (Uniswap V3) | 📋 |
| Set price range | 📋 |
| Collect fees | 📋 |
| Rebalance position | 📋 |
| Add liquidity with native token | ✅ |
| Calculate arbitrage opportunities | ✅ |

#### AMM Types Support
| Feature | Status |
|---------|--------|
| Constant product (x*y=k) | ✅ |
| Stable swap (Curve) | 📋 |
| Concentrated liquidity | 📋 |
| Order book hybrid | 📋 |
| Virtual AMM (perpetuals) | 📋 |

---

### 🏦 DeFi - Lending & Borrowing

#### Lending
| Feature | Status |
|---------|--------|
| Supply/deposit assets | ✅ |
| Withdraw assets | ✅ |
| Get supply APY | ✅ |
| Get supplied balance | ✅ |
| Get utilization rate | 📋 |
| Enable/disable as collateral | 📋 |

#### Borrowing
| Feature | Status |
|---------|--------|
| Borrow assets | ✅ |
| Repay debt | ✅ |
| Get borrow APY | ✅ |
| Get borrowed balance | ✅ |
| Get health factor | ✅ |
| Get liquidation threshold | ✅ |
| Get max borrowable amount | 📋 |
| Flash loans | ✅ |
| Get borrow limit | 📋 |
| Get flash loan info | ✅ |

#### Liquidations
| Feature | Status |
|---------|--------|
| Liquidate unhealthy positions | 📋 |
| Get liquidatable positions | ✅ |
| Get liquidation bonus | 📋 |
| Partial liquidations | 📋 |

#### Isolated Markets
| Feature | Status |
|---------|--------|
| Supply to isolated pool | 📋 |
| Borrow from isolated pool | 📋 |
| Get isolation mode debt ceiling | 📋 |

---

### 🥩 DeFi - Staking

#### Native Staking
| Feature | Status |
|---------|--------|
| Stake native tokens | ✅ |
| Unstake/withdraw | ✅ |
| Claim rewards | ✅ |
| Get staking APY | ✅ |
| Get validator list | 📋 |
| Delegate to validator | 📋 |
| Redelegate | 📋 |
| Get unbonding period | 📋 |

#### Liquid Staking
| Feature | Status |
|---------|--------|
| Stake for liquid staking tokens (stETH, rETH) | ✅ |
| Unwrap liquid staking tokens | ✅ |
| Get exchange rate | ✅ |
| Get staking rewards rate | ✅ |

#### LP Staking/Farming
| Feature | Status |
|---------|--------|
| Stake LP tokens | ✅ |
| Unstake LP tokens | ✅ |
| Claim farming rewards | ✅ |
| Get farming APY | ✅ |
| Compound rewards | 📋 |
| Get pending rewards | ✅ |
| Boost rewards (veTokens) | 📋 |

#### Restaking
| Feature | Status |
|---------|--------|
| Restake assets (EigenLayer) | 📋 |
| Get restaking points | 📋 |
| Choose operators | 📋 |
| Withdraw from restaking | 📋 |

---

### 📊 DeFi - Derivatives

#### Perpetual Futures
| Feature | Status |
|---------|--------|
| Open long/short position | 📋 |
| Close position | 📋 |
| Add/remove margin | 📋 |
| Set leverage | 📋 |
| Get funding rate | 📋 |
| Get open interest | 📋 |
| Get liquidation price | 📋 |
| Set stop-loss/take-profit | 📋 |
| Get PnL | 📋 |
| Partial close | 📋 |

#### Options
| Feature | Status |
|---------|--------|
| Buy call/put options | 📋 |
| Sell/write options | 📋 |
| Exercise options | 📋 |
| Get option greeks | 📋 |
| Get implied volatility | 📋 |
| Get option chain | 📋 |
| Spread strategies | 📋 |

#### Synthetics
| Feature | Status |
|---------|--------|
| Mint synthetic assets | 📋 |
| Burn synthetic assets | 📋 |
| Get collateral ratio | 📋 |
| Get synthetic price feed | 📋 |
| Liquidate synthetic positions | 📋 |

---

### 🌉 Cross-Chain & Bridges

#### Bridging
| Feature | Status |
|---------|--------|
| Bridge tokens cross-chain | ✅ |
| Get bridge quote | ✅ |
| Get bridge status | ✅ |
| Get supported chains | ✅ |
| Get supported tokens | ✅ |
| Claim bridged tokens | 📋 |
| Get bridge fees | ✅ |
| Get estimated time | ✅ |

#### Cross-Chain Messaging
| Feature | Status |
|---------|--------|
| Send cross-chain message | 📋 |
| Receive cross-chain message | 📋 |
| LayerZero operations | 📋 |
| Axelar operations | 📋 |
| Wormhole operations | 📋 |
| CCIP (Chainlink) | 📋 |
| Hyperlane operations | 📋 |

#### Atomic Swaps
| Feature | Status |
|---------|--------|
| Initiate atomic swap | 📋 |
| Complete atomic swap | 📋 |
| Refund atomic swap | 📋 |

---

### 🗳️ Governance

#### Voting
| Feature | Status |
|---------|--------|
| Create proposal | ✅ |
| Vote on proposal | ✅ |
| Delegate votes | ✅ |
| Get voting power | ✅ |
| Get proposal state | ✅ |
| Queue proposal | ✅ |
| Execute proposal | ✅ |
| Cancel proposal | ✅ |
| Get vote receipt | ✅ |

#### Token Locking
| Feature | Status |
|---------|--------|
| Lock tokens for voting (veTokens) | 📋 |
| Extend lock period | 📋 |
| Increase locked amount | 📋 |
| Withdraw unlocked tokens | 📋 |
| Get lock info | 📋 |

#### Snapshot (Off-chain)
| Feature | Status |
|---------|--------|
| Create space | 📋 |
| Create off-chain proposal | 📋 |
| Vote off-chain | 📋 |
| Get snapshot results | 📋 |

---

### 🔐 Security & Analysis

#### Contract Analysis
| Feature | Status |
|---------|--------|
| Verify contract source | ✅ |
| Get contract ABI | ✅ |
| Check if contract is proxy | ✅ |
| Get implementation address | ✅ |
| Detect honeypots | ✅ |
| Check for rug pull risks | ✅ |
| GoPlus token security check | ✅ |
| GoPlus rug pull detection | ✅ |
| Audit score | 📋 |
| Get contract creator | ✅ |
| Get contract age | ✅ |
| Detect malicious functions | ✅ |

#### Token Security
| Feature | Status |
|---------|--------|
| Check token safety | ✅ |
| Get holder distribution | ✅ |
| Check if mintable | ✅ |
| Check if pausable | ✅ |
| Check for hidden fees | ✅ |
| Check liquidity locked | ✅ |
| Get top holders | ✅ |
| Check ownership renounced | ✅ |
| GoPlus NFT security | ✅ |
| GoPlus approval security | ✅ |

#### Wallet Security
| Feature | Status |
|---------|--------|
| Get approval list | ✅ |
| Revoke approvals | ✅ |
| Check for drainers | ✅ |
| Simulate transaction safety | ✅ |
| Get wallet risk score | 📋 |
| GoPlus address security | ✅ |
| GoPlus dApp phishing check | ✅ |
| GoPlus signature decode | ✅ |

---

### 📈 Price & Market Data

#### Price Feeds
| Feature | Status |
|---------|--------|
| Get current price | ✅ |
| Get historical prices | ✅ |
| Get OHLCV data | ✅ |
| Get price from DEX | ✅ |
| Get price from oracle (Chainlink, Pyth) | ✅ |
| Get TWAP price | ✅ |
| Get price across exchanges | ✅ |
| Get volume | ✅ |
| Get market cap | ✅ |
| Get trending coins | ✅ |
| Get token by contract address | ✅ |
| Get exchange rates | ✅ |
| Get coin categories | ✅ |
| Get derivatives data | ✅ |
| Get company BTC/ETH holdings | ✅ |

#### Analytics
| Feature | Status |
|---------|--------|
| Get TVL (Total Value Locked) | ✅ |
| Get protocol metrics | ✅ |
| Get yield farming APYs | ✅ |
| Get gas tracker | ✅ |
| Get whale transactions | 📋 |
| Get token flow analysis | 📋 |
| Get DEX volume | ✅ |
| Get lending metrics | 📋 |
| Get DeFi fees & revenue | ✅ |
| Get stablecoin data | ✅ |
| Get bridge volumes | ✅ |
| Get liquidation data | ✅ |
| Get DeFi hacks history | ✅ |
| Get perpetuals data | ✅ |

---

### 🆔 Identity & Domains

#### ENS (Ethereum Name Service)
| Feature | Status |
|---------|--------|
| Register domain | ✅ |
| Resolve name to address | ✅ |
| Reverse resolve address to name | ✅ |
| Set primary name | 📋 |
| Set records (text, address, content hash) | ✅ |
| Transfer domain | ✅ |
| Renew domain | ✅ |
| Get expiry date | 📋 |
| Set subdomains | ✅ |

#### Other Name Services
| Feature | Status |
|---------|--------|
| Unstoppable Domains | 📋 |
| Space ID (.bnb) | 📋 |
| Bonfida (.sol) | 📋 |
| ANS (.avax) | 📋 |

#### DIDs & Verifiable Credentials
| Feature | Status |
|---------|--------|
| Create DID | 📋 |
| Resolve DID | 📋 |
| Issue verifiable credential | 📋 |
| Verify credential | 📋 |
| Revoke credential | 📋 |

---

### 🖼️ NFT & Metaverse

#### NFT Marketplace
| Feature | Status |
|---------|--------|
| List NFT for sale | 📋 |
| Buy NFT | 📋 |
| Make offer | 📋 |
| Accept offer | 📋 |
| Cancel listing | 📋 |
| Auction NFT | 📋 |
| Bid on auction | 📋 |
| Get floor price | 📋 |
| Get collection stats | 📋 |

#### NFT Creation
| Feature | Status |
|---------|--------|
| Deploy NFT collection | 📋 |
| Mint NFTs | 📋 |
| Set royalties | 📋 |
| Set metadata | 📋 |
| Reveal NFTs | 📋 |
| Whitelist management | 📋 |
| Airdrop NFTs | 📋 |

#### NFT Finance
| Feature | Status |
|---------|--------|
| NFT collateralized loans | 📋 |
| NFT fractionalization | 📋 |
| NFT renting | 📋 |
| NFT staking | 📋 |

#### Metaverse
| Feature | Status |
|---------|--------|
| Buy virtual land | 📋 |
| Sell virtual land | 📋 |
| Build on land | 📋 |
| Transfer assets between metaverses | 📋 |

---

### 🔔 Events & Subscriptions

#### Event Listening
| Feature | Status |
|---------|--------|
| Subscribe to contract events | 📋 |
| Subscribe to pending transactions | 📋 |
| Subscribe to new blocks | 📋 |
| Subscribe to logs | 📋 |
| Filter events by topic | ✅ |
| Get historical events | ✅ |
| Decode event logs | ✅ |

#### Webhooks & Notifications
| Feature | Status |
|---------|--------|
| Set up webhook for events | 📋 |
| Get transaction notifications | 📋 |
| Get price alerts | 📋 |
| Get whale alerts | 📋 |
| Get governance notifications | 📋 |

---

### 📜 Smart Contract Interaction

#### Read Operations
| Feature | Status |
|---------|--------|
| Call view/pure functions | ✅ |
| Get storage at slot | ✅ |
| Get contract bytecode | ✅ |
| Multicall (batch reads) | ✅ |
| Static call simulation | ✅ |

#### Write Operations
| Feature | Status |
|---------|--------|
| Send transaction to contract | ✅ |
| Encode function call | ✅ |
| Decode function result | ✅ |
| Estimate gas for call | ✅ |
| Batch transactions | ✅ |

#### Contract Deployment
| Feature | Status |
|---------|--------|
| Deploy contract | ✅ |
| Deploy with CREATE2 | ✅ |
| Deploy proxy contract | ✅ |
| Upgrade proxy | ✅ |
| Verify on explorer | ✅ |

---

### 🤖 Advanced Features

#### MEV & Flashbots
| Feature | Status |
|---------|--------|
| Submit private transaction | ✅ |
| Submit bundle | ✅ |
| Get MEV opportunities | ✅ |
| Backrun protection | ✅ |
| Frontrun protection | ✅ |
| Sandwich protection | ✅ |

#### Account Abstraction (ERC-4337)
| Feature | Status |
|---------|--------|
| Create smart account | 📋 |
| Execute user operation | 📋 |
| Batch operations | 📋 |
| Sponsor gas (Paymaster) | 📋 |
| Session keys | 📋 |
| Social recovery | 📋 |

#### Intents & Solvers
| Feature | Status |
|---------|--------|
| Submit intent | 📋 |
| Get solver quotes | 📋 |
| Execute via solver | 📋 |

#### Oracles
| Feature | Status |
|---------|--------|
| Get Chainlink price | ✅ |
| Get Pyth price | 📋 |
| Get Band Protocol price | 📋 |
| Get API3 price | 📋 |
| Request randomness (VRF) | 📋 |
| Request external data | 📋 |

---

### 🛠️ Utility Functions

#### Gas
| Feature | Status |
|---------|--------|
| Get gas price | ✅ |
| Get priority fee | ✅ |
| Get base fee | ✅ |
| Get gas history | ✅ |
| Estimate gas for transaction | ✅ |
| Get EIP-1559 fees | ✅ |

#### Encoding/Decoding
| Feature | Status |
|---------|--------|
| ABI encode | ✅ |
| ABI decode | ✅ |
| Keccak256 hash | ✅ |
| Pack/unpack data | ✅ |
| Sign typed data (EIP-712) | ✅ |

#### Address Utils
| Feature | Status |
|---------|--------|
| Validate address | ✅ |
| Checksum address | ✅ |
| Get address from ENS | ✅ |
| Check if contract | ✅ |
| Get contract type | 📋 |

---

### 📰 Data & Information

#### News & Social
| Feature | Status |
|---------|--------|
| Get crypto news | ✅ |
| Search crypto news | ✅ |
| Get DeFi news | ✅ |
| Get Bitcoin news | ✅ |
| Get breaking news | ✅ |
| Get social sentiment | ✅ |
| Get influencer rankings | ✅ |
| Get trending topics | ✅ |
| Get coin social metrics | ✅ |
| Get social feed | ✅ |
| Get market sentiment index | ✅ |
| Get Galaxy Score | ✅ |
| Get AltRank | ✅ |
| Get Twitter mentions | 📋 |
| Get Discord activity | 📋 |
| Get GitHub activity | 📋 |

#### On-Chain Data
| Feature | Status |
|---------|--------|
| Get token holders | 📋 |
| Get whale wallets | 📋 |
| Get smart money movements | 📋 |
| Get protocol users | 📋 |
| Get daily active addresses | 📋 |
| Get network hash rate | 📋 |

---

### 🏛️ Institutional & Compliance

#### KYC/AML
| Feature | Status |
|---------|--------|
| Wallet screening | 📋 |
| Transaction monitoring | 📋 |
| Risk scoring | 📋 |
| Sanctions checking | 📋 |

#### Custody
| Feature | Status |
|---------|--------|
| Multi-sig operations | 📋 |
| Cold storage | 📋 |
| Hot wallet management | 📋 |
| Policy enforcement | 📋 |

#### Reporting
| Feature | Status |
|---------|--------|
| Tax reporting | 📋 |
| Portfolio tracking | ✅ |
| P&L reporting | 📋 |
| Transaction history export | 📋 |

---

## Data Sources

This MCP server integrates with the following APIs:

| Provider | Data Type | API Key Required |
|----------|-----------|------------------|
| [CoinGecko](https://coingecko.com) | Market data, prices, OHLCV | Optional (free tier) |
| [CoinStats](https://coinstats.app) | Portfolio, prices, wallets | Yes |
| [DefiLlama](https://defillama.com) | TVL, yields, fees, protocols | No |
| [LunarCrush](https://lunarcrush.com) | Social sentiment, influencers | Yes |
| [GoPlus](https://gopluslabs.io) | Security analysis, honeypot detection | No |
| [GeckoTerminal](https://geckoterminal.com) | DEX pools, trades, OHLCV | No |
| [DexPaprika](https://dexpaprika.com) | DEX analytics, pools | No |
| [CryptoPanic](https://cryptopanic.com) | Crypto news | Yes |
| [Alternative.me](https://alternative.me) | Fear & Greed Index | No |

---

## 🔗 Related MCP Servers

Related MCP servers, each maintained in its own repository:

| Server | Description | Tools |
|--------|-------------|-------|
| [Binance-MCP](https://github.com/nirholas/Binance-MCP) | Binance.com global exchange API | 156+ tools |
| [Binance-US-MCP](https://github.com/nirholas/Binance-US-MCP) | Binance.US exchange API | 71+ tools |

### Binance.com Server
Full Binance global API coverage including:
- Spot trading, wallet, staking, mining
- Convert, Simple Earn, Algo Trading (TWAP/VP)
- NFT, Pay, Copy Trading, Dual Investment
- VIP Loans, C2C/P2P, Fiat

```json
{
  "mcpServers": {
    "binance": {
      "command": "npx",
      "args": ["ts-node", "binance-mcp-server/src/index.ts"],
      "env": {
        "BINANCE_API_KEY": "your_key",
        "BINANCE_API_SECRET": "your_secret"
      }
    }
  }
}
```

### Binance.US Server
US-regulated exchange with:
- Market data, spot trading, wallet
- Staking, OTC, sub-accounts
- Custodial solutions (institutional)

```json
{
  "mcpServers": {
    "binance-us": {
      "command": "node",
      "args": ["binance-us-mcp-server/build/index.js"],
      "env": {
        "BINANCE_US_API_KEY": "your_key",
        "BINANCE_US_API_SECRET": "your_secret"
      }
    }
  }
}
```

---

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### Development Setup

```bash
# Fork and clone
git clone https://github.com/nirholas/bnbchain-mcp
cd bnbchain-mcp

# Install dependencies
bun install

# Create feature branch
git checkout -b feature/amazing-feature

# Make changes and test
bun dev
bun test

# Commit and push
git commit -m "feat: add amazing feature"
git push origin feature/amazing-feature

# Open Pull Request
```

### Contribution Guidelines

- 📝 Follow existing code style
- ✅ Add tests for new features
- 📖 Update documentation
- 🔍 Run linting before committing

### Adding New Tools

1. Create tool file in `src/tools/<category>/`
2. Export tool definition with Zod schema
3. Add to tool index
4. Document in README

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Credits

Built by **[nich](https://x.com/nichxbt)** ([github.com/nirholas](https://github.com/nirholas)) **[and the Sperax Team](https://x.com/SperaxUSD)** ([github.com/speraxos](https://github.com/speraxos)) ([github.com/sperax](https://github.com/sperax))

### Special Thanks

- [Model Context Protocol](https://modelcontextprotocol.io) team
- [viem](https://viem.sh) for excellent EVM tooling
- All the amazing Web3 API providers

---

<div align="center">

### 🌟 Star us on GitHub!

If you find this project useful, please consider giving it a ⭐️

[![GitHub stars](https://img.shields.io/github/stars/nirholas/bnbchain-mcp?style=social)](https://github.com/nirholas/bnbchain-mcp)

<br/>

<sub>Empowering AI agents to interact with blockchains</sub>

</div>

<details>
<summary>.</summary>
# ERC-8004 Keywords & SEO Terms

> Comprehensive keyword list for ERC-8004 Trustless Agents ecosystem

---

## Core Protocol Keywords

ERC-8004, ERC8004, EIP-8004, EIP8004, Trustless Agents, trustless agent, trustless AI, trustless AI agents, agent protocol, agent standard, Ethereum agent standard, blockchain agent protocol, on-chain agents, onchain agents, on-chain AI, onchain AI, decentralized agents, decentralized AI agents, autonomous agents, autonomous AI agents, AI agent protocol, AI agent standard, agent discovery, agent trust, agent reputation, agent validation, agent identity, agent registry, identity registry, reputation registry, validation registry, agent NFT, ERC-721 agent, agent tokenId, agentId, agentURI, agentWallet, agent registration, agent registration file, agent-registration.json, agent card, agent metadata, agent endpoints, agent discovery protocol, agent trust protocol, open agent protocol, open agent standard, permissionless agents, permissionless AI, censorship-resistant agents, portable agent identity, portable AI identity, verifiable agents, verifiable AI agents, accountable agents, accountable AI, agent accountability

## Blockchain & Web3 Keywords

Ethereum, Ethereum mainnet, ETH, EVM, Ethereum Virtual Machine, smart contracts, Solidity, blockchain, decentralized, permissionless, trustless, on-chain, onchain, L2, Layer 2, Base, Optimism, Polygon, Linea, Arbitrum, Scroll, Monad, Gnosis, Celo, Sepolia, testnet, mainnet, singleton contracts, singleton deployment, ERC-721, NFT, non-fungible token, tokenURI, URIStorage, EIP-712, ERC-1271, wallet signature, EOA, smart contract wallet, gas fees, gas sponsorship, EIP-7702, subgraph, The Graph, indexer, blockchain indexing, IPFS, decentralized storage, content-addressed, immutable data, public registry, public good, credibly neutral, credibly neutral infrastructure, open protocol, open standard, Web3, crypto, cryptocurrency, DeFi, decentralized finance

## AI & Agent Technology Keywords

AI agents, artificial intelligence agents, autonomous AI, AI autonomy, LLM agents, large language model agents, machine learning agents, ML agents, AI assistant, AI chatbot, intelligent agents, software agents, digital agents, virtual agents, AI automation, automated agents, agent-to-agent, A2A, A2A protocol, Google A2A, Agent2Agent, MCP, Model Context Protocol, agent communication, agent interoperability, agent orchestration, agent collaboration, multi-agent, multi-agent systems, agent capabilities, agent skills, agent tools, agent prompts, agent resources, agent completions, AgentCard, agent card, agent endpoint, agent service, AI service, AI API, agent API, AI infrastructure, agent infrastructure, agentic, agentic web, agentic economy, agentic commerce, agent economy, agent marketplace, AI marketplace, agent platform, AI platform

## Trust & Reputation Keywords

trust, trustless, reputation, reputation system, reputation protocol, reputation registry, feedback, client feedback, user feedback, on-chain feedback, on-chain reputation, verifiable reputation, portable reputation, reputation aggregation, reputation scoring, reputation algorithm, trust signals, trust model, trust verification, trust layer, recursive reputation, reviewer reputation, spam prevention, Sybil attack, Sybil resistance, anti-spam, feedback filtering, trusted reviewers, rating, rating system, quality rating, starred rating, uptime rating, success rate, response time, performance history, track record, audit trail, immutable feedback, permanent feedback, feedback response, appendResponse, giveFeedback, revokeFeedback, feedback tags, feedback value, valueDecimals, feedbackURI, feedbackHash, clientAddress, reviewer address

## Validation & Verification Keywords

validation, validation registry, validator, validator contract, cryptographic validation, cryptographic proof, cryptographic attestation, zero-knowledge, ZK, zkML, zero-knowledge machine learning, ZK proofs, trusted execution environment, TEE, TEE attestation, TEE oracle, stake-secured, staking validators, crypto-economic security, inference re-execution, output validation, work verification, third-party validation, independent validation, validation request, validation response, validationRequest, validationResponse, requestHash, responseHash, verifiable computation, verified agents, verified behavior, behavioral validation, agent verification

## Payment & Commerce Keywords

x402, x402 protocol, x402 payments, programmable payments, micropayments, HTTP payments, pay-per-request, pay-per-task, agent payments, AI payments, agent monetization, AI monetization, agent commerce, AI commerce, agentic commerce, agent economy, AI economy, agent marketplace, service marketplace, agent-to-agent payments, A2A payments, stablecoin payments, USDC, crypto payments, on-chain payments, payment settlement, programmable settlement, proof of payment, proofOfPayment, payment receipt, payment verification, Coinbase, Coinbase x402, agent pricing, API pricing, service pricing, subscription, API keys, revenue, trading yield, cumulative revenues, agent wallet, payment address, toAddress, fromAddress, txHash

## Discovery & Registry Keywords

agent discovery, service discovery, agent registry, identity registry, agent registration, register agent, mint agent, agent NFT, agent tokenId, agent browsing, agent explorer, agent scanner, 8004scan, 8004scan.io, agentscan, agentscan.info, 8004agents, 8004agents.ai, agent leaderboard, agent ranking, top agents, agent listing, agent directory, agent catalog, agent index, browse agents, search agents, find agents, discover agents, agent visibility, agent discoverability, no-code registration, agent creation, create agent, my agents, agent owner, agent operator, agent transfer, transferable agent, portable agent

## Endpoints & Integration Keywords

endpoint, agent endpoint, service endpoint, API endpoint, MCP endpoint, A2A endpoint, web endpoint, HTTPS endpoint, HTTP endpoint, DID, decentralized identifier, ENS, Ethereum Name Service, ENS name, agent.eth, vitalik.eth, email endpoint, OASF, Open Agent Specification Format, endpoint verification, domain verification, endpoint ownership, .well-known, well-known, agent-registration.json, endpoint domain, endpoint URL, endpoint URI, base64 data URI, on-chain metadata, off-chain metadata, metadata storage, JSON metadata, agent JSON, registration JSON

## SDK & Developer Tools Keywords

SDK, Agent0 SDK, Agent0, ChaosChain SDK, ChaosChain, Lucid Agents, Daydreams AI, create-8004-agent, npm, TypeScript SDK, Python SDK, JavaScript, Solidity, smart contract, ABI, contract ABI, deployed contracts, contract addresses, Hardhat, development tools, developer tools, dev tools, API, REST API, GraphQL, subgraph, The Graph, indexer, blockchain explorer, Etherscan, contract verification, open source, MIT license, CC0, public domain, GitHub, repository, code repository, documentation, docs, best practices, reference implementation

## Ecosystem & Community Keywords

ecosystem, community, builder, builders, developer, developers, contributor, contributors, partner, partners, collaborator, collaborators, co-author, co-authors, MetaMask, Ethereum Foundation, Google, Coinbase, Consensys, AltLayer, Virtuals Protocol, Olas, EigenLayer, Phala, ElizaOS, Flashbots, Polygon, Base, Optimism, Arbitrum, Scroll, Linea, Monad, Gnosis, Celo, Near Protocol, Filecoin, Worldcoin, ThirdWeb, ENS, Collab.land, DappRadar, Giza Tech, Theoriq, OpenServ, Questflow, Semantic, Semiotic, Cambrian, Nevermined, Oasis, Towns Protocol, Warden Protocol, Terminal3, Pinata Cloud, Silence Labs, Rena Labs, Index Network, Trusta Network, Turf Network

## Key People & Organizations Keywords

Marco De Rossi, MetaMask AI Lead, Davide Crapis, Ethereum Foundation AI, Head of AI, Jordan Ellis, Google engineer, Erik Reppel, Coinbase engineering, Head of Engineering, Sumeet Chougule, ChaosChain founder, YQ, AltLayer co-founder, Wee Kee, Virtuals contributor, Cyfrin audit, Nethermind audit, Ethereum Foundation Security Team, security audit, audited contracts

## Use Cases & Applications Keywords

trading bot, DeFi agent, yield optimizer, data oracle, price feed, analytics agent, research agent, coding agent, development agent, automation agent, task agent, workflow agent, portfolio management, asset management, supply chain, service agent, API service, chatbot, AI assistant, virtual assistant, personal agent, enterprise agent, B2B agent, agent-as-a-service, AaaS, SaaS agent, AI SaaS, delegated agent, proxy agent, helper agent, worker agent, coordinator agent, orchestrator agent, validator agent, auditor agent, insurance agent, scoring agent, ranking agent

## Technical Specifications Keywords

ERC-8004 specification, EIP specification, Ethereum Improvement Proposal, Ethereum Request for Comment, RFC 2119, RFC 8174, MUST, SHOULD, MAY, OPTIONAL, REQUIRED, interface, contract interface, function signature, event, emit event, indexed event, storage, contract storage, view function, external function, public function, uint256, int128, uint8, uint64, bytes32, string, address, array, struct, MetadataEntry, mapping, modifier, require, revert, transfer, approve, operator, owner, tokenId, URI, hash, keccak256, KECCAK-256, signature, deadline

## Events & Conferences Keywords

8004 Launch Day, Agentic Brunch, Builder Nights Denver, Trustless Agent Day, Devconnect, ETHDenver, community call, meetup, hackathon, workshop, conference, summit, builder program, grants, bounties, ecosystem fund

## News & Media Keywords

announcement, launch, mainnet launch, testnet launch, protocol update, upgrade, security review, audit, milestone, breaking news, ecosystem news, agent news, AI news, blockchain news, Web3 news, crypto news, DeFi news, newsletter, blog, article, press release, media coverage

## Competitor & Alternative Keywords

agent framework, agent platform, AI platform, centralized agents, closed agents, proprietary agents, gatekeeper, intermediary, platform lock-in, vendor lock-in, data silos, walled garden, open alternative, decentralized alternative, permissionless alternative, trustless alternative

## Future & Roadmap Keywords

cross-chain, multi-chain, chain agnostic, bridge, interoperability, governance, community governance, decentralized governance, DAO, protocol upgrade, upgradeable contracts, UUPS, proxy contract, ERC1967Proxy, protocol evolution, standard finalization, EIP finalization, mainnet feedback, testnet feedback, security improvements, gas optimization, feature request, enhancement, proposal

---

## Long-tail Keywords & Phrases

how to register AI agent on blockchain, how to create ERC-8004 agent, how to build trustless AI agent, how to verify agent reputation, how to give feedback to AI agent, how to monetize AI agent, how to accept crypto payments AI agent, how to discover AI agents, how to trust AI agents, how to validate AI agent output, decentralized AI agent marketplace, on-chain AI agent registry, blockchain-based AI reputation, verifiable AI agent identity, portable AI agent reputation, permissionless AI agent registration, trustless AI agent discovery, autonomous AI agent payments, agent-to-agent micropayments, AI agent service discovery, AI agent trust protocol, open source AI agent standard, Ethereum AI agent protocol, EVM AI agent standard, blockchain AI agent framework, decentralized AI agent infrastructure, Web3 AI agent ecosystem, crypto AI agent platform, DeFi AI agent integration, NFT-based agent identity, ERC-721 agent registration, on-chain agent metadata, off-chain agent data, IPFS agent storage, subgraph agent indexing, agent explorer blockchain, agent scanner Ethereum, agent leaderboard ranking, agent reputation scoring, agent feedback system, agent validation proof, zkML agent verification, TEE agent attestation, stake-secured agent validation, x402 agent payments, MCP agent endpoint, A2A agent protocol, ENS agent name, DID agent identity, agent wallet address, agent owner operator, transferable agent NFT, portable agent identity, censorship-resistant agent registry, credibly neutral agent infrastructure, public good agent data, open agent economy, agentic web infrastructure, trustless agentic commerce, autonomous agent economy, AI agent economic actors, accountable AI agents, verifiable AI behavior, auditable AI agents, transparent AI agents, decentralized AI governance, community-driven AI standards, open protocol AI agents, permissionless AI innovation

---

## Brand & Product Keywords

8004, 8004.org, Trustless Agents, trustlessagents, trustless-agents, 8004scan, 8004scan.io, agentscan, agentscan.info, 8004agents, 8004agents.ai, Agent0, agent0, sdk.ag0.xyz, ChaosChain, chaoschain, docs.chaoscha.in, Lucid Agents, lucid-agents, daydreams.systems, create-8004-agent, erc-8004-contracts, best-practices, agent0lab, subgraph

---

## Hashtags & Social Keywords

#ERC8004, #TrustlessAgents, #AIAgents, #DecentralizedAI, #OnChainAI, #AgenticWeb, #AgentEconomy, #Web3AI, #BlockchainAI, #EthereumAI, #CryptoAI, #AutonomousAgents, #AIAutonomy, #AgentDiscovery, #AgentTrust, #AgentReputation, #x402, #MCP, #A2A, #AgentProtocol, #OpenAgents, #PermissionlessAI, #VerifiableAI, #AccountableAI, #AIInfrastructure, #AgentInfrastructure, #BuildWithAgents, #AgentBuilders, #AgentDevelopers, #AgentEcosystem

---

## Statistical Keywords

10000+ agents, 10300+ agents, 10000+ testnet registrations, 20000+ feedback, 5 months development, 80+ teams, 100+ partners, January 28 2026, January 29 2026, mainnet live, production ready, audited contracts, singleton deployment, per-chain singleton, ERC-721 token, NFT minting, gas fees, $5-20 mainnet gas

---

## Additional Core Protocol Terms

ERC 8004, EIP 8004, trustless agent protocol, trustless agent standard, trustless agent framework, trustless agent system, trustless agent network, trustless agent infrastructure, trustless agent architecture, trustless agent specification, trustless agent implementation, trustless agent deployment, trustless agent integration, trustless agent ecosystem, trustless agent platform, trustless agent marketplace, trustless agent registry, trustless agent identity, trustless agent reputation, trustless agent validation, trustless agent discovery, trustless agent verification, trustless agent authentication, trustless agent authorization, trustless agent registration, trustless agent management, trustless agent operations, trustless agent services, trustless agent solutions, trustless agent technology, trustless agent innovation, trustless agent development, trustless agent research, trustless agent security, trustless agent privacy, trustless agent transparency, trustless agent accountability, trustless agent governance, trustless agent compliance, trustless agent standards, trustless agent protocols, trustless agent interfaces, trustless agent APIs, trustless agent SDKs, trustless agent tools, trustless agent utilities, trustless agent libraries, trustless agent modules, trustless agent components, trustless agent extensions

## Extended Blockchain Terms

Ethereum blockchain, Ethereum network, Ethereum protocol, Ethereum ecosystem, Ethereum infrastructure, Ethereum development, Ethereum smart contract, Ethereum dApp, Ethereum application, Ethereum transaction, Ethereum gas, Ethereum wallet, Ethereum address, Ethereum account, Ethereum signature, Ethereum verification, Ethereum consensus, Ethereum finality, Ethereum block, Ethereum chain, Ethereum node, Ethereum client, Ethereum RPC, Ethereum JSON-RPC, Ethereum Web3, Ethereum ethers.js, Ethereum viem, Ethereum wagmi, Ethereum hardhat, Ethereum foundry, Ethereum truffle, Ethereum remix, Ethereum deployment, Ethereum verification, Ethereum explorer, Ethereum scanner, Base blockchain, Base network, Base L2, Base layer 2, Base mainnet, Base testnet, Base Sepolia, Optimism blockchain, Optimism network, Optimism L2, Optimism mainnet, Optimism Sepolia, Polygon blockchain, Polygon network, Polygon PoS, Polygon zkEVM, Polygon mainnet, Polygon Mumbai, Arbitrum blockchain, Arbitrum One, Arbitrum Nova, Arbitrum Sepolia, Arbitrum Stylus, Linea blockchain, Linea network, Linea mainnet, Linea testnet, Scroll blockchain, Scroll network, Scroll mainnet, Scroll Sepolia, Monad blockchain, Monad network, Monad testnet, Gnosis Chain, Gnosis Safe, Celo blockchain, Celo network, Avalanche, Fantom, BNB Chain, BSC, Binance Smart Chain, zkSync, StarkNet, Mantle, Blast, Mode, Zora, opBNB, Manta, Taiko

## Extended AI Agent Terms

artificial intelligence agent, machine learning agent, deep learning agent, neural network agent, transformer agent, GPT agent, Claude agent, Gemini agent, Llama agent, Mistral agent, AI model agent, foundation model agent, language model agent, multimodal agent, vision agent, audio agent, speech agent, text agent, code agent, coding assistant, programming agent, developer agent, software agent, application agent, web agent, mobile agent, desktop agent, cloud agent, edge agent, IoT agent, robotic agent, automation agent, workflow agent, process agent, task agent, job agent, worker agent, assistant agent, helper agent, support agent, service agent, utility agent, tool agent, function agent, capability agent, skill agent, knowledge agent, reasoning agent, planning agent, decision agent, execution agent, monitoring agent, logging agent, analytics agent, reporting agent, notification agent, alert agent, scheduling agent, calendar agent, email agent, messaging agent, chat agent, conversation agent, dialogue agent, interactive agent, responsive agent, reactive agent, proactive agent, predictive agent, adaptive agent, learning agent, evolving agent, self-improving agent, autonomous agent system, multi-agent architecture, agent swarm, agent collective, agent network, agent cluster, agent pool, agent fleet, agent army, agent workforce, agent team, agent group, agent ensemble, agent coalition, agent federation, agent consortium, agent alliance, agent partnership, agent collaboration, agent cooperation, agent coordination, agent orchestration, agent choreography, agent composition, agent aggregation, agent integration, agent interoperability, agent compatibility, agent standardization, agent normalization, agent harmonization

## Extended Trust & Reputation Terms

trust protocol, trust system, trust network, trust infrastructure, trust layer, trust framework, trust model, trust algorithm, trust computation, trust calculation, trust score, trust rating, trust level, trust tier, trust grade, trust rank, trust index, trust metric, trust indicator, trust signal, trust factor, trust weight, trust coefficient, trust threshold, trust minimum, trust maximum, trust average, trust median, trust distribution, trust aggregation, trust normalization, trust scaling, trust decay, trust growth, trust accumulation, trust history, trust timeline, trust evolution, trust trajectory, trust prediction, trust forecast, trust estimation, trust inference, trust derivation, trust propagation, trust transfer, trust delegation, trust inheritance, trust chain, trust path, trust graph, trust network analysis, trust community detection, trust clustering, trust similarity, trust distance, trust proximity, trust relationship, trust connection, trust link, trust edge, trust node, trust vertex, reputation protocol, reputation system, reputation network, reputation infrastructure, reputation layer, reputation framework, reputation model, reputation algorithm, reputation computation, reputation calculation, reputation score, reputation rating, reputation level, reputation tier, reputation grade, reputation rank, reputation index, reputation metric, reputation indicator, reputation signal, reputation factor, reputation weight, reputation coefficient, reputation threshold, reputation minimum, reputation maximum, reputation average, reputation median, reputation distribution, reputation aggregation, reputation normalization, reputation scaling, reputation decay, reputation growth, reputation accumulation, reputation history, reputation timeline, reputation evolution, reputation trajectory, reputation prediction, reputation forecast, reputation estimation, reputation inference, reputation derivation, reputation propagation, reputation transfer, reputation delegation, reputation inheritance, reputation chain, reputation path, reputation graph, reputation network analysis, reputation community detection, reputation clustering, reputation similarity, reputation distance, reputation proximity, reputation relationship, reputation connection, reputation link, feedback protocol, feedback system, feedback network, feedback infrastructure, feedback layer, feedback framework, feedback model, feedback algorithm, feedback computation, feedback calculation, feedback score, feedback rating, feedback level, feedback tier, feedback grade, feedback rank, feedback index, feedback metric, feedback indicator, feedback signal, feedback factor, feedback weight, feedback coefficient, feedback threshold, feedback minimum, feedback maximum, feedback average, feedback median, feedback distribution, feedback aggregation, feedback normalization, feedback scaling, review system, rating system, scoring system, ranking system, evaluation system, assessment system, appraisal system, judgment system, quality assurance, quality control, quality metrics, quality standards, quality benchmarks, performance metrics, performance indicators, performance benchmarks, performance standards, performance evaluation, performance assessment, performance monitoring, performance tracking, performance analytics, performance reporting, performance dashboard

## Extended Validation & Verification Terms

validation protocol, validation system, validation network, validation infrastructure, validation layer, validation framework, validation model, validation algorithm, validation computation, validation process, validation procedure, validation workflow, validation pipeline, validation chain, validation sequence, validation step, validation stage, validation phase, validation checkpoint, validation gate, validation barrier, validation filter, validation criteria, validation rules, validation logic, validation conditions, validation requirements, validation specifications, validation standards, validation benchmarks, validation metrics, validation indicators, validation signals, validation evidence, validation proof, validation attestation, validation certification, validation confirmation, validation approval, validation acceptance, validation rejection, validation failure, validation success, validation result, validation outcome, validation report, validation log, validation audit, validation trace, validation record, validation history, verification protocol, verification system, verification network, verification infrastructure, verification layer, verification framework, verification model, verification algorithm, verification computation, verification process, verification procedure, verification workflow, verification pipeline, verification chain, verification sequence, verification step, verification stage, verification phase, verification checkpoint, verification gate, verification barrier, verification filter, verification criteria, verification rules, verification logic, verification conditions, verification requirements, verification specifications, verification standards, verification benchmarks, verification metrics, verification indicators, verification signals, verification evidence, verification proof, verification attestation, verification certification, verification confirmation, verification approval, verification acceptance, verification rejection, verification failure, verification success, verification result, verification outcome, verification report, verification log, verification audit, verification trace, verification record, verification history, cryptographic verification, mathematical verification, formal verification, automated verification, manual verification, human verification, machine verification, AI verification, hybrid verification, multi-party verification, distributed verification, decentralized verification, consensus verification, probabilistic verification, deterministic verification, real-time verification, batch verification, streaming verification, incremental verification, partial verification, complete verification, exhaustive verification, sampling verification, statistical verification, heuristic verification, rule-based verification, model-based verification, data-driven verification, evidence-based verification, proof-based verification, attestation-based verification, signature-based verification, hash-based verification, merkle verification, zero-knowledge verification, ZK verification, zkSNARK, zkSTARK, PLONK, Groth16, recursive proof, proof composition, proof aggregation, proof batching, proof compression, proof generation, proof verification, prover, verifier, trusted setup, universal setup, transparent setup, TEE verification, SGX verification, TDX verification, SEV verification, enclave verification, secure enclave, hardware security, hardware attestation, remote attestation, local attestation, platform attestation, application attestation, code attestation, data attestation, execution attestation, result attestation

## Extended Payment & Commerce Terms

payment protocol, payment system, payment network, payment infrastructure, payment layer, payment framework, payment model, payment algorithm, payment computation, payment process, payment procedure, payment workflow, payment pipeline, payment chain, payment sequence, payment step, payment stage, payment phase, payment gateway, payment processor, payment provider, payment service, payment solution, payment platform, payment application, payment interface, payment API, payment SDK, payment integration, payment compatibility, payment interoperability, payment standardization, payment normalization, payment harmonization, payment settlement, payment clearing, payment reconciliation, payment confirmation, payment verification, payment validation, payment authorization, payment authentication, payment security, payment privacy, payment transparency, payment accountability, payment compliance, payment regulation, payment governance, payment audit, payment reporting, payment analytics, payment monitoring, payment tracking, payment logging, payment history, payment record, payment receipt, payment invoice, payment statement, payment notification, payment alert, payment reminder, payment schedule, payment recurring, payment subscription, payment one-time, payment instant, payment delayed, payment batch, payment streaming, payment conditional, payment escrow, payment refund, payment chargeback, payment dispute, payment resolution, micropayment protocol, micropayment system, micropayment network, micropayment infrastructure, nanopayment, minipayment, small payment, fractional payment, partial payment, incremental payment, progressive payment, milestone payment, completion payment, success payment, performance payment, outcome payment, result payment, delivery payment, service payment, product payment, subscription payment, usage payment, consumption payment, metered payment, measured payment, tracked payment, verified payment, validated payment, confirmed payment, settled payment, cleared payment, finalized payment, irreversible payment, reversible payment, conditional payment, unconditional payment, guaranteed payment, insured payment, secured payment, unsecured payment, collateralized payment, uncollateralized payment, stablecoin payment, USDC payment, USDT payment, DAI payment, FRAX payment, LUSD payment, ETH payment, Ether payment, native token payment, ERC-20 payment, token payment, crypto payment, cryptocurrency payment, digital payment, electronic payment, online payment, internet payment, web payment, mobile payment, in-app payment, embedded payment, invisible payment, seamless payment, frictionless payment, instant payment, real-time payment, near-instant payment, fast payment, quick payment, rapid payment, speedy payment, efficient payment, low-cost payment, cheap payment, affordable payment, economical payment, cost-effective payment, value payment, premium payment, standard payment, basic payment, free payment, zero-fee payment, low-fee payment, minimal-fee payment, reduced-fee payment, discounted payment, promotional payment, incentivized payment, rewarded payment, cashback payment, rebate payment, bonus payment, tip payment, donation payment, contribution payment, support payment, funding payment, investment payment, capital payment, equity payment, debt payment, loan payment, credit payment, debit payment, prepaid payment, postpaid payment, pay-as-you-go payment, pay-per-use payment, pay-per-request payment, pay-per-call payment, pay-per-query payment, pay-per-task payment, pay-per-job payment, pay-per-result payment, pay-per-outcome payment, pay-per-success payment, pay-per-completion payment, pay-per-delivery payment, pay-per-service payment, pay-per-product payment, pay-per-access payment, pay-per-view payment, pay-per-download payment, pay-per-stream payment, pay-per-minute payment, pay-per-second payment, pay-per-byte payment, pay-per-token payment, pay-per-inference payment, pay-per-generation payment, pay-per-response payment, pay-per-answer payment, pay-per-solution payment, pay-per-recommendation payment, pay-per-prediction payment, pay-per-analysis payment, pay-per-insight payment, pay-per-report payment

## Extended Discovery & Registry Terms

discovery protocol, discovery system, discovery network, discovery infrastructure, discovery layer, discovery framework, discovery model, discovery algorithm, discovery computation, discovery process, discovery procedure, discovery workflow, discovery pipeline, discovery chain, discovery sequence, discovery step, discovery stage, discovery phase, discovery mechanism, discovery method, discovery technique, discovery approach, discovery strategy, discovery tactic, discovery pattern, discovery template, discovery schema, discovery format, discovery standard, discovery specification, discovery interface, discovery API, discovery SDK, discovery tool, discovery utility, discovery library, discovery module, discovery component, discovery extension, discovery plugin, discovery addon, discovery integration, discovery compatibility, discovery interoperability, discovery standardization, discovery normalization, discovery harmonization, registry protocol, registry system, registry network, registry infrastructure, registry layer, registry framework, registry model, registry algorithm, registry computation, registry process, registry procedure, registry workflow, registry pipeline, registry chain, registry sequence, registry step, registry stage, registry phase, registry mechanism, registry method, registry technique, registry approach, registry strategy, registry tactic, registry pattern, registry template, registry schema, registry format, registry standard, registry specification, registry interface, registry API, registry SDK, registry tool, registry utility, registry library, registry module, registry component, registry extension, registry plugin, registry addon, registry integration, registry compatibility, registry interoperability, registry standardization, registry normalization, registry harmonization, agent catalog, agent directory, agent index, agent database, agent repository, agent store, agent hub, agent center, agent portal, agent gateway, agent aggregator, agent collector, agent curator, agent organizer, agent manager, agent administrator, agent operator, agent controller, agent supervisor, agent monitor, agent tracker, agent watcher, agent observer, agent listener, agent subscriber, agent publisher, agent broadcaster, agent announcer, agent advertiser, agent promoter, agent marketer, agent distributor, agent connector, agent linker, agent bridge, agent router, agent dispatcher, agent scheduler, agent allocator, agent balancer, agent optimizer, agent enhancer, agent improver, agent upgrader, agent updater, agent maintainer, agent supporter, agent helper, agent assistant, agent advisor, agent consultant, agent expert, agent specialist, agent professional, agent practitioner, agent implementer, agent developer, agent builder, agent creator, agent designer, agent architect, agent engineer, agent programmer, agent coder, agent hacker, agent maker, agent producer, agent manufacturer, agent provider, agent supplier, agent vendor, agent seller, agent buyer, agent consumer, agent user, agent customer, agent client, agent subscriber, agent member, agent participant, agent contributor, agent collaborator, agent partner, agent ally, agent friend, agent colleague, agent peer, agent neighbor, agent community, agent ecosystem, agent network, agent cluster, agent group, agent team, agent squad, agent unit, agent division, agent department, agent organization, agent company, agent enterprise, agent business, agent startup, agent project, agent initiative, agent program, agent campaign, agent movement, agent revolution, agent evolution, agent transformation, agent innovation, agent disruption, agent advancement, agent progress, agent growth, agent expansion, agent scaling, agent multiplication, agent proliferation, agent adoption, agent acceptance, agent integration, agent incorporation, agent assimilation, agent absorption, agent merger, agent acquisition, agent partnership, agent collaboration, agent cooperation, agent coordination, agent synchronization, agent harmonization, agent alignment, agent optimization, agent maximization, agent minimization, agent efficiency, agent effectiveness, agent productivity, agent performance, agent quality, agent reliability, agent availability, agent accessibility, agent usability, agent scalability, agent flexibility, agent adaptability, agent extensibility, agent maintainability, agent sustainability, agent durability, agent longevity, agent persistence, agent continuity, agent stability, agent security, agent safety, agent privacy, agent confidentiality, agent integrity, agent authenticity, agent validity, agent accuracy, agent precision, agent correctness, agent completeness, agent consistency, agent coherence, agent clarity, agent simplicity, agent elegance, agent beauty, agent aesthetics

## Extended Technical Implementation Terms

smart contract development, smart contract programming, smart contract coding, smart contract writing, smart contract design, smart contract architecture, smart contract pattern, smart contract template, smart contract library, smart contract framework, smart contract toolkit, smart contract suite, smart contract collection, smart contract set, smart contract bundle, smart contract package, smart contract module, smart contract component, smart contract function, smart contract method, smart contract procedure, smart contract routine, smart contract subroutine, smart contract logic, smart contract algorithm, smart contract computation, smart contract calculation, smart contract operation, smart contract action, smart contract transaction, smart contract call, smart contract invocation, smart contract execution, smart contract deployment, smart contract migration, smart contract upgrade, smart contract update, smart contract patch, smart contract fix, smart contract bug, smart contract vulnerability, smart contract exploit, smart contract attack, smart contract defense, smart contract protection, smart contract security, smart contract audit, smart contract review, smart contract analysis, smart contract testing, smart contract verification, smart contract validation, smart contract certification, smart contract documentation, smart contract specification, smart contract interface, smart contract ABI, smart contract bytecode, smart contract opcode, smart contract gas, smart contract optimization, smart contract efficiency, smart contract performance, smart contract scalability, smart contract reliability, smart contract availability, smart contract maintainability, smart contract upgradeability, smart contract proxy, smart contract implementation, smart contract storage, smart contract memory, smart contract stack, smart contract heap, smart contract variable, smart contract constant, smart contract immutable, smart contract state, smart contract event, smart contract log, smart contract emit, smart contract modifier, smart contract require, smart contract assert, smart contract revert, smart contract error, smart contract exception, smart contract fallback, smart contract receive, smart contract payable, smart contract view, smart contract pure, smart contract external, smart contract internal, smart contract public, smart contract private, smart contract virtual, smart contract override, smart contract abstract, smart contract interface, smart contract library, smart contract import, smart contract inheritance, smart contract composition, smart contract delegation, smart contract proxy pattern, UUPS proxy, transparent proxy, beacon proxy, minimal proxy, clone factory, diamond pattern, EIP-2535, upgradeable contract, upgradeable proxy, upgrade mechanism, upgrade process, upgrade procedure, upgrade workflow, upgrade pipeline, upgrade chain, upgrade sequence, upgrade step, upgrade stage, upgrade phase, upgrade checkpoint, upgrade gate, upgrade barrier, upgrade filter, upgrade criteria, upgrade rules, upgrade logic, upgrade conditions, upgrade requirements, upgrade specifications, upgrade standards, upgrade benchmarks, upgrade metrics, upgrade indicators, upgrade signals, upgrade evidence, upgrade proof, upgrade attestation, upgrade certification, upgrade confirmation, upgrade approval, upgrade acceptance, upgrade rejection, upgrade failure, upgrade success, upgrade result, upgrade outcome, upgrade report, upgrade log, upgrade audit, upgrade trace, upgrade record, upgrade history

## Extended Use Case Terms

DeFi agent, DeFi bot, DeFi automation, DeFi yield, DeFi farming, DeFi staking, DeFi lending, DeFi borrowing, DeFi trading, DeFi arbitrage, DeFi liquidation, DeFi governance, DeFi voting, DeFi proposal, DeFi treasury, DeFi vault, DeFi pool, DeFi liquidity, DeFi swap, DeFi exchange, DeFi DEX, DeFi AMM, DeFi orderbook, DeFi perpetual, DeFi options, DeFi futures, DeFi derivatives, DeFi insurance, DeFi prediction, DeFi oracle, DeFi bridge, DeFi cross-chain, DeFi multichain, DeFi aggregator, DeFi router, DeFi optimizer, DeFi maximizer, DeFi compounder, DeFi harvester, DeFi rebalancer, DeFi hedger, DeFi protector, DeFi guardian, DeFi sentinel, DeFi watchdog, DeFi monitor, DeFi tracker, DeFi analyzer, DeFi reporter, DeFi alerter, DeFi notifier, trading agent, trading bot, trading automation, trading algorithm, trading strategy, trading signal, trading indicator, trading pattern, trading trend, trading momentum, trading volume, trading liquidity, trading spread, trading slippage, trading execution, trading order, trading limit, trading market, trading stop, trading take-profit, trading stop-loss, trading position, trading portfolio, trading balance, trading equity, trading margin, trading leverage, trading risk, trading reward, trading return, trading profit, trading loss, trading performance, trading history, trading record, trading log, trading report, trading analytics, trading dashboard, trading interface, trading API, trading SDK, trading integration, trading compatibility, trading interoperability, data agent, data bot, data automation, data collection, data aggregation, data processing, data transformation, data cleaning, data validation, data verification, data enrichment, data augmentation, data annotation, data labeling, data classification, data categorization, data clustering, data segmentation, data filtering, data sorting, data ranking, data scoring, data rating, data evaluation, data assessment, data analysis, data analytics, data visualization, data reporting, data dashboard, data interface, data API, data SDK, data integration, data compatibility, data interoperability, research agent, research bot, research automation, research collection, research aggregation, research processing, research analysis, research synthesis, research summarization, research extraction, research identification, research discovery, research exploration, research investigation, research examination, research evaluation, research assessment, research review, research critique, research comparison, research benchmarking, research testing, research experimentation, research validation, research verification, research confirmation, research publication, research dissemination, research communication, research collaboration, research cooperation, research coordination, customer service agent, customer support agent, customer success agent, customer experience agent, customer engagement agent, customer retention agent, customer acquisition agent, customer onboarding agent, customer training agent, customer education agent, sales agent, marketing agent, advertising agent, promotion agent, outreach agent, engagement agent, conversion agent, retention agent, loyalty agent, advocacy agent, referral agent, partnership agent, collaboration agent, cooperation agent, coordination agent, communication agent, messaging agent, notification agent, alert agent, reminder agent, scheduling agent, calendar agent, booking agent, reservation agent, appointment agent, meeting agent, conference agent, event agent, webinar agent, presentation agent, demonstration agent, tutorial agent, training agent, education agent, learning agent, teaching agent, coaching agent, mentoring agent, advising agent, consulting agent, expert agent, specialist agent, professional agent, practitioner agent, implementer agent, developer agent, builder agent, creator agent, designer agent, architect agent, engineer agent, programmer agent, coder agent, hacker agent, maker agent, producer agent, manufacturer agent, provider agent, supplier agent, vendor agent, content agent, writing agent, copywriting agent, editing agent, proofreading agent, translation agent, localization agent, transcription agent, summarization agent, extraction agent, generation agent, creation agent, production agent, publication agent, distribution agent, syndication agent, aggregation agent, curation agent, recommendation agent, personalization agent, customization agent, optimization agent, enhancement agent, improvement agent, refinement agent, polishing agent, finishing agent, completion agent, delivery agent, fulfillment agent, execution agent, implementation agent, deployment agent, integration agent, configuration agent, setup agent, installation agent, maintenance agent, support agent, troubleshooting agent, debugging agent, fixing agent, patching agent, updating agent, upgrading agent, migrating agent, transitioning agent, transforming agent, converting agent, adapting agent, adjusting agent, modifying agent, changing agent, evolving agent, growing agent, expanding agent, scaling agent, multiplying agent, proliferating agent

---

## Industry & Vertical Keywords

healthcare agent, medical agent, clinical agent, diagnostic agent, treatment agent, pharmaceutical agent, drug discovery agent, patient agent, doctor agent, nurse agent, hospital agent, clinic agent, telemedicine agent, telehealth agent, health monitoring agent, wellness agent, fitness agent, nutrition agent, mental health agent, therapy agent, counseling agent, psychology agent, psychiatry agent, insurance agent, claims agent, underwriting agent, risk assessment agent, actuarial agent, policy agent, coverage agent, benefits agent, reimbursement agent, billing agent, invoicing agent, accounting agent, bookkeeping agent, tax agent, audit agent, compliance agent, regulatory agent, legal agent, contract agent, agreement agent, negotiation agent, dispute agent, arbitration agent, mediation agent, litigation agent, court agent, judge agent, lawyer agent, attorney agent, paralegal agent, notary agent, real estate agent, property agent, housing agent, rental agent, lease agent, mortgage agent, appraisal agent, valuation agent, inspection agent, construction agent, architecture agent, engineering agent, design agent, planning agent, zoning agent, permit agent, licensing agent, certification agent, accreditation agent, quality agent, testing agent, inspection agent, manufacturing agent, production agent, assembly agent, logistics agent, supply chain agent, inventory agent, warehouse agent, shipping agent, delivery agent, transportation agent, fleet agent, routing agent, dispatch agent, tracking agent, monitoring agent, surveillance agent, security agent, protection agent, safety agent, emergency agent, disaster agent, crisis agent, response agent, recovery agent, restoration agent, maintenance agent, repair agent, service agent, support agent, helpdesk agent, ticketing agent, incident agent, problem agent, change agent, release agent, deployment agent, configuration agent, asset agent, resource agent, capacity agent, performance agent, optimization agent, efficiency agent, productivity agent, automation agent, integration agent, migration agent, transformation agent, modernization agent, innovation agent, research agent, development agent, experimentation agent, prototyping agent, testing agent, validation agent, verification agent, certification agent, documentation agent, training agent, education agent, learning agent, teaching agent, tutoring agent, mentoring agent, coaching agent, consulting agent, advisory agent, strategy agent, planning agent, forecasting agent, prediction agent, analysis agent, reporting agent, visualization agent, dashboard agent, monitoring agent, alerting agent, notification agent, communication agent, collaboration agent, coordination agent, scheduling agent, calendar agent, meeting agent, conference agent, presentation agent, demonstration agent, proposal agent, quotation agent, estimation agent, budgeting agent, costing agent, pricing agent, discount agent, promotion agent, marketing agent, advertising agent, branding agent, campaign agent, outreach agent, engagement agent, conversion agent, retention agent, loyalty agent, advocacy agent, referral agent, partnership agent, alliance agent, consortium agent, federation agent, network agent, community agent, ecosystem agent, platform agent, marketplace agent, exchange agent, trading agent, brokerage agent, clearing agent, settlement agent, custody agent, escrow agent, trust agent, fiduciary agent, investment agent, portfolio agent, wealth agent, asset management agent, fund agent, hedge fund agent, mutual fund agent, ETF agent, index agent, bond agent, equity agent, derivative agent, option agent, future agent, swap agent, commodity agent, currency agent, forex agent, crypto agent, bitcoin agent, ethereum agent, altcoin agent, token agent, NFT agent, DeFi agent, yield agent, staking agent, lending agent, borrowing agent, liquidity agent, AMM agent, DEX agent, CEX agent, bridge agent, oracle agent, governance agent, DAO agent, treasury agent, proposal agent, voting agent, delegation agent, staking agent, validator agent, node agent, miner agent, block agent, transaction agent, gas agent, fee agent, reward agent, penalty agent, slashing agent, epoch agent, finality agent, consensus agent, proof agent, attestation agent, signature agent, encryption agent, decryption agent, hashing agent, merkle agent, trie agent, state agent, storage agent, memory agent, cache agent, database agent, query agent, index agent, search agent, retrieval agent, ranking agent, recommendation agent, personalization agent, segmentation agent, targeting agent, attribution agent, analytics agent, metrics agent, KPI agent, OKR agent, goal agent, objective agent, milestone agent, deadline agent, timeline agent, roadmap agent, backlog agent, sprint agent, iteration agent, release agent, version agent, changelog agent, documentation agent, specification agent, requirement agent, user story agent, acceptance criteria agent, test case agent, bug agent, issue agent, ticket agent, task agent, subtask agent, epic agent, feature agent, enhancement agent, improvement agent, optimization agent, refactoring agent, debugging agent, profiling agent, benchmarking agent, load testing agent, stress testing agent, penetration testing agent, security testing agent, vulnerability agent, exploit agent, patch agent, hotfix agent, update agent, upgrade agent, migration agent, rollback agent, backup agent, restore agent, disaster recovery agent, business continuity agent, high availability agent, fault tolerance agent, redundancy agent, replication agent, synchronization agent, consistency agent, durability agent, availability agent, partition tolerance agent, CAP agent, ACID agent, BASE agent, eventual consistency agent, strong consistency agent, linearizability agent, serializability agent, isolation agent, atomicity agent, transaction agent, commit agent, rollback agent, savepoint agent, checkpoint agent, snapshot agent, backup agent, archive agent, retention agent, lifecycle agent, expiration agent, deletion agent, purging agent, cleanup agent, garbage collection agent, memory management agent, resource management agent, capacity planning agent, scaling agent, autoscaling agent, load balancing agent, traffic management agent, rate limiting agent, throttling agent, circuit breaker agent, retry agent, timeout agent, fallback agent, graceful degradation agent, feature flag agent, A/B testing agent, canary deployment agent, blue-green deployment agent, rolling deployment agent, immutable deployment agent, infrastructure agent, platform agent, container agent, kubernetes agent, docker agent, serverless agent, function agent, lambda agent, edge agent, CDN agent, caching agent, proxy agent, gateway agent, API gateway agent, service mesh agent, sidecar agent, envoy agent, istio agent, linkerd agent, consul agent, vault agent, terraform agent, ansible agent, puppet agent, chef agent, saltstack agent, cloudformation agent, pulumi agent, crossplane agent, argocd agent, fluxcd agent, jenkins agent, github actions agent, gitlab CI agent, circleci agent, travisci agent, drone agent, tekton agent, spinnaker agent, harness agent, octopus agent, buildkite agent, teamcity agent, bamboo agent, azure devops agent, AWS codepipeline agent, GCP cloud build agent, monitoring agent, observability agent, logging agent, tracing agent, metrics agent, alerting agent, incident management agent, on-call agent, pagerduty agent, opsgenie agent, victorops agent, datadog agent, newrelic agent, dynatrace agent, splunk agent, elastic agent, prometheus agent, grafana agent, loki agent, tempo agent, jaeger agent, zipkin agent, opentelemetry agent, sentry agent, rollbar agent, bugsnag agent, honeybadger agent, raygun agent, airbrake agent

## Technology Stack Keywords

JavaScript agent, TypeScript agent, Python agent, Go agent, Rust agent, Java agent, Kotlin agent, Swift agent, Objective-C agent, C++ agent, C# agent, Ruby agent, PHP agent, Scala agent, Clojure agent, Elixir agent, Erlang agent, Haskell agent, OCaml agent, F# agent, Dart agent, Flutter agent, React agent, Vue agent, Angular agent, Svelte agent, Solid agent, Next.js agent, Nuxt agent, Remix agent, Gatsby agent, Astro agent, Qwik agent, Fresh agent, SvelteKit agent, Express agent, Fastify agent, Koa agent, Hapi agent, NestJS agent, Adonis agent, Sails agent, Meteor agent, Django agent, Flask agent, FastAPI agent, Starlette agent, Tornado agent, Pyramid agent, Bottle agent, Falcon agent, Sanic agent, Quart agent, Rails agent, Sinatra agent, Hanami agent, Roda agent, Grape agent, Spring agent, Quarkus agent, Micronaut agent, Vert.x agent, Play agent, Akka agent, Lagom agent, ASP.NET agent, Blazor agent, MAUI agent, Xamarin agent, Unity agent, Godot agent, Unreal agent, Bevy agent, Amethyst agent, ggez agent, macroquad agent, Raylib agent, SDL agent, SFML agent, OpenGL agent, Vulkan agent, DirectX agent, Metal agent, WebGL agent, WebGPU agent, Three.js agent, Babylon.js agent, PlayCanvas agent, A-Frame agent, React Three Fiber agent, Pixi.js agent, Phaser agent, Cocos agent, Defold agent, Construct agent, GameMaker agent, RPG Maker agent, Twine agent, Ink agent, Yarn Spinner agent, Dialogflow agent, Rasa agent, Botpress agent, Microsoft Bot Framework agent, Amazon Lex agent, IBM Watson agent, Google Dialogflow agent, Wit.ai agent, Snips agent, Mycroft agent, Jasper agent, Leon agent, Hugging Face agent, OpenAI agent, Anthropic agent, Cohere agent, AI21 agent, Stability AI agent, Midjourney agent, DALL-E agent, Stable Diffusion agent, Imagen agent, Gemini agent, Claude agent, GPT agent, LLaMA agent, Mistral agent, Mixtral agent, Phi agent, Qwen agent, Yi agent, DeepSeek agent, Falcon agent, MPT agent, BLOOM agent, OPT agent, Pythia agent, Cerebras agent, Inflection agent, Adept agent, Character.AI agent, Poe agent, Perplexity agent, You.com agent, Neeva agent, Kagi agent, Brave Search agent, DuckDuckGo agent, Startpage agent, Ecosia agent, Qwant agent, Mojeek agent, Yandex agent, Baidu agent, Naver agent, Seznam agent, Sogou agent

## Emerging Technology Keywords

quantum computing agent, quantum machine learning agent, quantum optimization agent, quantum simulation agent, quantum cryptography agent, post-quantum agent, lattice-based agent, hash-based agent, code-based agent, isogeny-based agent, multivariate agent, neuromorphic agent, spiking neural network agent, memristor agent, photonic agent, optical computing agent, DNA computing agent, molecular computing agent, biological computing agent, wetware agent, biocomputing agent, synthetic biology agent, gene editing agent, CRISPR agent, mRNA agent, protein folding agent, AlphaFold agent, drug discovery agent, virtual screening agent, molecular dynamics agent, computational chemistry agent, materials science agent, nanotechnology agent, metamaterials agent, 2D materials agent, graphene agent, quantum dots agent, nanoparticles agent, nanorobots agent, nanomedicine agent, targeted delivery agent, biosensors agent, wearables agent, implantables agent, brain-computer interface agent, neural interface agent, Neuralink agent, EEG agent, fMRI agent, PET agent, MEG agent, TMS agent, tDCS agent, optogenetics agent, chemogenetics agent, connectomics agent, brain mapping agent, cognitive computing agent, affective computing agent, emotion AI agent, sentiment analysis agent, opinion mining agent, social listening agent, brand monitoring agent, reputation management agent, crisis communication agent, public relations agent, media monitoring agent, press agent, journalist agent, editor agent, writer agent, author agent, content creator agent, influencer agent, streamer agent, YouTuber agent, TikToker agent, podcaster agent, blogger agent, vlogger agent, photographer agent, videographer agent, animator agent, illustrator agent, graphic designer agent, UI designer agent, UX designer agent, product designer agent, industrial designer agent, fashion designer agent, interior designer agent, architect agent, landscape architect agent, urban planner agent, city planner agent, transportation planner agent, traffic agent, autonomous vehicle agent, self-driving agent, ADAS agent, V2X agent, connected vehicle agent, smart transportation agent, smart city agent, smart grid agent, smart meter agent, smart home agent, smart building agent, smart factory agent, Industry 4.0 agent, IoT agent, IIoT agent, edge computing agent, fog computing agent, mist computing agent, cloudlet agent, mobile edge agent, MEC agent, NOMA agent, massive MIMO agent, beamforming agent, millimeter wave agent, terahertz agent, 6G agent, 5G agent, LTE agent, NB-IoT agent, LoRa agent, Sigfox agent, Zigbee agent, Z-Wave agent, Thread agent, Matter agent, HomeKit agent, Alexa agent, Google Home agent, SmartThings agent, Home Assistant agent, OpenHAB agent, Domoticz agent, Hubitat agent, Homey agent, Tuya agent, eWeLink agent, Sonoff agent, Shelly agent, Tasmota agent, ESPHome agent, WLED agent, Zigbee2MQTT agent, deCONZ agent, ZHA agent, Philips Hue agent, IKEA Tradfri agent, Aqara agent, Xiaomi agent, Yeelight agent, Nanoleaf agent, LIFX agent, TP-Link Kasa agent, Wyze agent, Ring agent, Nest agent, Ecobee agent, Honeywell agent, Emerson agent, Carrier agent, Trane agent, Lennox agent, Daikin agent, Mitsubishi Electric agent, LG agent, Samsung agent, Bosch agent, Siemens agent, ABB agent, Schneider Electric agent, Rockwell agent, Emerson agent, Honeywell agent, Yokogawa agent, Endress+Hauser agent, SICK agent, Pepperl+Fuchs agent, Balluff agent, ifm agent, Banner agent, Turck agent, Omron agent, Keyence agent, Cognex agent, Basler agent, FLIR agent, Teledyne agent, Allied Vision agent, JAI agent, IDS agent, Baumer agent, Stemmer agent, MVTec agent, Matrox agent, National Instruments agent, Beckhoff agent, Phoenix Contact agent, Wago agent, Weidmuller agent, Murrelektronik agent, Pilz agent, 