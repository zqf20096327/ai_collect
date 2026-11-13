# ha-first-home-planner：第一個 Home Assistant 智慧家庭規劃 Skill（繁體中文）

> 📖 為什麼做、怎麼用：[智慧家庭怎麼開始：四年後，今天仍會買和絕不重買的東西](https://drpwchen.com/posts/smart-home-2026-rebuild/)　｜　[English summary](#english-summary)

一個 [Agent Skill](https://agentskills.io/specification)，讓 Claude Code、Codex 這類 AI agent
帶**完全沒經驗的人**規劃第一個 Home Assistant（HA）智慧家庭：先問你想解決什麼生活小事、住哪、跟誰住、
能不能動線路、斷網要剩什麼，再給你一張**第一期購物清單三格表（必買／可等／別買）**和**買之前要查的事**。

> ⚠️ AI 給的規劃要人驗證。這個 skill 刻意**不放設備型號與價格**（半年就過期），而是教 AI 當下去查、
> 附連結和查證日期。HA 官方論壇因為 AI 答案「wrong in subtle ways」禁止貼 AI 生成的回答
> （[2023 公告](https://www.home-assistant.io/blog/2023/01/23/help-others-leave-ai-at-the-dor/)）——請把輸出當草稿。

## 它做什麼、不做什麼

| 做 | 不做 |
|---|---|
| 訪談：生活問題、住家、租／自有、家人、預算、隱私底線、出國需求、技術意願 | 推薦特定品牌型號、比價 |
| 把每件事翻成「盯什麼物理狀態」，每項買的東西答三格：盯什麼、斷網還剩什麼、誰發現它壞了 | 寫自動化 YAML、改 HA 設定（交給下面的工具） |
| 主機（成品盒 vs N100 小主機）、Zigbee／Matter／Wi-Fi、語音、攝影機的**決策原則** | 門鎖、保全、市電接線的細節（找專業人員） |
| 台灣在地查核：110V、NCC、商品安全標章、陸版米家、涂鴉白牌、租屋、繁中語音 | 替你下法律結論 |

判斷原則出自作者家裡一套 HA 四年多的長期運作紀錄（243 條自動化），重點是新手「不知道要問的問題」：
失聯的感應器會留著舊值、回報成功不等於事情發生、雲端整合的爆炸半徑、監控要在第十台裝置之前裝好。
另外整理了中英文社群（PTT、Mobile01、瀚思彼岸、r/homeassistant、HA 論壇等）新手最常問、最常後悔的事，
見 [`research/community.md`](research/community.md)。

## 跟其他工具的分工：裝好之前 vs 之後

| 階段 | 用什麼 |
|---|---|
| **還沒買／剛買第一批**：要買什麼、主機選哪個、會踩什麼坑 | **這個 skill** |
| HA 已經在跑：寫自動化、儀表板、備份的最佳實務 | 官方 [homeassistant-ai/skills](https://github.com/homeassistant-ai/skills) |
| HA 已經在跑：讓 AI 直接讀狀態、操作、管理設定 | [ha-mcp](https://github.com/homeassistant-ai/ha-mcp)、HA 內建 MCP Server 整合 |

## 需求與費用

- 一個能載入 Agent Skill 的 AI agent：Claude Code 或 Codex CLI 等（工具本身的訂閱費另計）。
- 不需要 Home Assistant、不需要任何設備，也不需要 API key；這個 skill 是純文字，本身免費。
- 作業系統不限（只是複製資料夾）。

## 安裝

把 `skills/ha-first-home-planner/` 整個資料夾複製到 agent 的 skills 目錄。以 Claude Code 個人目錄為例
（macOS／Linux／Windows 的 Git Bash 都適用）：

```bash
git clone https://github.com/drpwchen/ha-first-home-skill.git
mkdir -p ~/.claude/skills
cp -r ha-first-home-skill/skills/ha-first-home-planner ~/.claude/skills/
```

各工具的 skills 目錄：

- **Claude Code**：個人 `~/.claude/skills/ha-first-home-planner/`，或專案內 `.claude/skills/ha-first-home-planner/`
- **Codex CLI**：`~/.codex/skills/ha-first-home-planner/`（Codex 的 skills 目錄依版本可能不同，以 Codex 官方文件為準）
- **其他支援 Agent Skills 標準的工具**：放進該工具的 skills 目錄

然後開一個新的 session（skill 在開場時載入），直接說：「我想開始做智慧家庭，可以幫我規劃嗎？」

預期結果：AI 會先問你生活小事、住家、家人、預算等問題，問完後給你「必買／可等／別買」三格購物清單與買之前要查的事。

> 🧋 省了你時間的話，[請我喝杯飲料](https://drpwchen.com/support/)。

## 限制

- 只管「還沒買／剛買第一批」：不寫自動化 YAML、不改 HA 設定，那是裝好之後的事（見上面的分工表）。
- 不放設備型號與價格；AI 要在當下自己查，查到的連結與日期請你再看一次。
- 台灣在地化查核（110V、NCC、商品安全標章等）以截至文件標註日期為準，之後可能變動。
- AI 的輸出是草稿，不是專業建議；門鎖、保全、市電接線請找專業人員。

## 檔案

```
skills/ha-first-home-planner/
├── SKILL.md                         訪談流程、三格表、輸出格式
└── references/
    ├── interview.md                 題庫：每題答案會改變什麼、預設值
    ├── principles.md                判斷原則：失敗型態、主機與協定決策、別買清單
    ├── verify-before-buy.md         買前查核、台灣在地化、能不能斷網矩陣
    └── community-pitfalls.md        中英文社群新手常問與常後悔
research/community.md                社群現況調查原文（附來源連結）
tests/scenarios/                     四個新手情境的自測輸出與評語（三輪）
scripts/check_skill.py               格式與個資檢查
```

## 授權

- 文字內容（skill 本體、`research/`、`tests/`、本 README）：[CC BY 4.0](LICENSE)——可以自由分享、改作、商用，
  請標示出處（作者陳柏威＋本 repo 連結）並註明是否修改。
- `scripts/check_skill.py`：[MIT](LICENSE-MIT)。

## Support 支持

如果這個 skill 幫你少踩了坑，歡迎[請我喝杯飲料](https://drpwchen.com/support/) 🧋

---

## English summary

**ha-first-home-planner** is a Traditional-Chinese (Taiwan) Agent Skill that helps an AI agent plan a
complete beginner's *first* Home Assistant home — before anything is bought. It interviews the user
(life problems to solve, housing, renting vs owning, family members' tech comfort, budget, privacy limits,
travel/away needs), then outputs a phase-1 shopping list in three columns (**must buy / can wait / don't buy**),
where every item must answer: *what physical state it watches, what still works offline, and who notices
when it breaks*. It deliberately ships **no device models or prices**; instead it teaches the agent what to
verify at purchase time (integration `iot_class`, Zigbee2MQTT device list, Matter certification, Taiwan
110 V / NCC / safety marks, regional Xiaomi servers). Principles come from four years of running a real HA
home. Use it *before* HA is installed; afterwards, use the official
[homeassistant-ai/skills](https://github.com/homeassistant-ai/skills) or [ha-mcp](https://github.com/homeassistant-ai/ha-mcp).
Install by copying `skills/ha-first-home-planner/` into your agent's skills directory. License: CC BY 4.0 for all content; MIT for `scripts/check_skill.py`.
