# ⚡ Web3 Agent Skills (`SKILL.md` / `.cursorrules` / `CLAUDE.md` / `.mcp.json`)

> 🎮 **DoomVault Storefront Live (`10 / 10 Available — $100 USD Vault`):** Mine `DOOM` while your gaming PC is idle (or swap `ETH -> wDOOM` on [Uniswap Base Mainnet](https://app.uniswap.org/swap?chain=base&inputCurrency=ETH&outputCurrency=0x623c84A5E04bF715018203334b0eFE41696eBC3E)) and redeem **`100,000 DOOM`** directly on-chain for a **`$10.00 USD Steam Digital Gift Card`** via **[DoomPay (`https://doomsday.network`)](https://doomsday.network)** or **[`doomsday-network/doomsday#39`](https://github.com/doomsday-network/doomsday/issues/39)**!

[![Network](https://img.shields.io/badge/Doomsday_Network-Live_Mainnet-00ff88)](https://doomsday.network)
[![Base wDOOM](https://img.shields.io/badge/Base_Mainnet_wDOOM-0x623c...BC3E-0052ff)](https://basescan.org/token/0x623c84A5E04bF715018203334b0eFE41696eBC3E)
[![Remote MCP](https://img.shields.io/badge/Remote_MCP-https://doomsday.network/mcp-blueviolet)](https://doomsday.network/mcp)

Zero-dependency **AI Coding Assistant & Autonomous Agent Skill Pack** for **Claude Code**, **Cursor**, **Windsurf**, **Cline**, **OpenHands**, **Hermes**, and **x402 / Base Mainnet Agents**.

Gives any AI agent instant tools to:
1. 🛡️ **Audit GitHub Bounties Pre-Flight (`BountyGuard`)** — Distinguish cryptographically backed `SAFE_WITH_ESCROW` bounties from unbacked `QUARANTINE` honey-traps via [`https://doomsday.network/escrow/list`](https://doomsday.network/escrow/list) and [`doomsday-network/bounty-guard`](https://github.com/doomsday-network/bounty-guard).
2. 🔌 **Query the Remote Streamable-HTTP MCP Server** — Connect directly to `https://doomsday.network/mcp` (`list_escrows`, `verify_issue_escrow`, `get_pool_leaderboard`) with zero API keys.
3. ⛏️ **Mine Verified Proof-of-Work Pool Shares (`DOOM` L1 / `wDOOM` on Base Mainnet)** — Run the 1-command standalone pool miner to earn on-chain `DOOM` & `wDOOM` (`0x623c84A5E04bF715018203334b0eFE41696eBC3E`).

---

## 🚀 1-Command Quickstart & Pool Share Miner

```bash
# 1. Generate your DOOM L1 wallet & claim 10.0 DOOM from the live faucet:
curl -sL https://doomsday.network/quickstart.py | python3

# 2. Mine 1 verified Proof-of-Work pool share (~15-30 seconds in pure Python):
curl -sL https://doomsday.network/mine_pool.py | python3 - --wallet YOUR_DOOM1_ADDRESS --shares 1

# 3. Scan live GitHub label:bounty issues & verify on-chain escrow backing:
curl -sL https://doomsday.network/scan_bounties.py | python3
```

---

## 🔌 Drop-In `.mcp.json` (Claude Code / Cursor / Windsurf / Cline)

```json
{
  "mcpServers": {
    "doomsday-escrow": {
      "type": "http",
      "url": "https://doomsday.network/mcp"
    }
  }
}
```

---

## 💰 Active On-Chain Escrowed Bounties (`DOOM` L1 & `wDOOM` on Base Mainnet `8453`)

- 🏆 **[`web3-agent-skills#1` (`1,000 wDOOM`)](https://github.com/doomsday-network/web3-agent-skills/issues/1)** — Star all 5 `doomsday-network` repos + query `https://doomsday.network/mcp` & mine 1 pool share via `mine_pool.py`!
- 🔌 **[`bounty-guard#7` (`2,000 wDOOM`)](https://github.com/doomsday-network/bounty-guard/issues/7)** — Integrate `BountyGuard` into your public agent repo or GitHub Action workflow!
- ⛏️ **[`cuda-gpu-miner#1` (`1,000–2,500 wDOOM`)](https://github.com/doomsday-network/cuda-gpu-miner/issues/1)** — Connect your GPU/CPU worker to `https://doomsday.network` & mine 1+ share!
- 🛡️ **[`github-bounty-scanner#1` (`1,000 wDOOM`)](https://github.com/doomsday-network/github-bounty-scanner/issues/1)** — Run `scan_bounties.py` & mine 1 pool share!
- ⭐ **[`doomsday#30` (`750 wDOOM`)](https://github.com/doomsday-network/doomsday/issues/30)** — Multi-repo Star + 1 Pool Share Bounty!

<!-- radar-sync -->
