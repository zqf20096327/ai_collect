# Companion Bot — 有長期記憶的 Telegram 陪伴型對話 Bot

![tests](https://github.com/amuro93/companion-bot/actions/workflows/ci.yml/badge.svg)

[English →](README.en.md)

一個以 SQLite 為核心、可完全在地端模型上運行的陪伴型對話 Bot。目標不是「問答」，而是讓角色記得你說過的事、說得像人、並且在模型出狀況時**明確失敗而不是胡言亂語**。

- 對話後端：任何 OpenAI 相容的 `/v1/chat/completions`（llama.cpp、vLLM、Ollama、雲端 API 皆可）
- 記憶：SQLite（結構化事實 + 向量索引 + 非同步抽取佇列）
- 介面：Telegram（私人對話，單一擁有者）

## 特色

**1. 分層記憶，不是只把歷史塞進 context**
短期歷史、L0 固定設定、具名事實（key-value）、語意檢索、延遲抽取佇列分開存放。寫入走單一 SQLite 交易，避免「檢查後才寫」的競態；來源被撤回時，衍生記憶一併排除。

**2. Fail-closed 的啟動檢查**
設定檔嚴格驗證（未知欄位直接拒絕）、人設檔缺失即啟動失敗、模型端點必須在允許清單內、憑證只從環境變數讀取（設定檔只記變數名）。錯的設定不會變成「跑起來但行為詭異」。

**3. 混合推理模型的 bounded thinking**
支援的端點會帶 `reasoning_budget_tokens`（預設 128）。低比特量化的地端模型在「完全關閉思考」時常退化成一兩個字或空回；給一個小額思考預算能顯著穩定輸出，但過大反而變差——這是實測後的預設值，不是憑感覺。

**4. 執行期切換模型**
Telegram 打 `/model` 會列出所有設定的後端，按鈕切換後立即生效並記住選擇（重啟仍保留）。適合「日常用雲端、敏感場景用地端」這種雙軌用法。

**5. 555 項自動化測試**
從設定驗證、記憶原子性、佇列復原、向量索引，到 Telegram handler 的派送行為都有測試。其中一條測試會用真實的 `Application.process_update` 斷言 `/model` 不會被其他攔截器吃掉——這個 bug 真的發生過，所以留了回歸測試。

## 設計理念：記憶只存原句，不讓模型摘要

多數記憶系統（mem0、Letta 這類）走「讓 LLM 把對話整理成事實」的路線：使用者說「最近晚上都睡不好，因為小的半夜會醒」，系統存成「使用者有睡眠問題」。

這很省 context，但代價有三個：模型的理解錯誤會被固化而且無法回溯（只看得到摘要，看不到原句）；來源被撤回時，衍生出來的摘要追不回來；兩次摘要還可能互相矛盾。

這個專案刻意反過來做：

- **只存使用者原句**——模型可以判斷「這句值不值得記」，但不能改寫成摘要
- **寫入前先用確定性規則過濾**（家庭、住處、健康、行程等類別），規則判不出來才問本地模型；模型判斷失敗就**不記**，不猜
- **手動記憶優先於自動記憶**，衝突時手動版不會被自動流程覆蓋
- 修正與撤回都留紀錄；**來源訊息撤回時，由它衍生的記憶一併排除**

代價是 context 比較長、檢索要多一層。換來的是任何一條記憶都能回溯到「使用者當時到底說了什麼」。

下面的端點白名單與 fail-closed 啟動檢查，其實是同一個原則的另一面：寧可明確失敗，也不要安靜地做錯。

## 架構

```
Telegram  ──►  telegram_test_adapter   (handler 分層、權限、/model 按鈕)
                    │
                    ▼
               companion_chat          (對話組裝、persona 注入、記憶檢索)
                 │        │
                 │        └──► model_router ──► OpenAI 相容端點
                 │
                 ▼
            memory_* 記憶層
              ├─ memory_core          結構化事實、單一交易寫入
              ├─ memory_index / search 索引與檢索
              ├─ memory_sqlite_vector  本地向量索引
              ├─ memory_deferred_*     延遲抽取（佇列 / worker / processor）
              ├─ memory_gate / trigger 寫入前安全閘門與觸發判斷
              └─ memory_http           內部記憶服務（僅 loopback）
```

主要模組：

| 模組 | 職責 |
|---|---|
| `bootstrap_test_bot.py` | 啟動入口、前置檢查、依賴接線 |
| `bot_config.py` | 設定 schema、嚴格驗證、端點允許清單 |
| `companion_chat.py` | 單輪對話流程與 context 組裝 |
| `persona_l0.py` | 人設與 L0 分層記憶載入 |
| `memory_core.py` | 事實儲存與交易邊界 |
| `model_router.py` | 多後端切換與選擇持久化 |
| `telegram_test_adapter.py` | Telegram handler 與互動 |

## 快速開始

需求：Python 3.11+、一個 OpenAI 相容的模型端點。

```bash
git clone <this-repo> && cd companion-bot
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp model-auth.synthetic.example.json bot.json
# 編輯 bot.json：填入你的 model_url / model_id，並把人設檔指向你的角色

export BOT_TELEGRAM_TOKEN="你的 bot token"      # 從 @BotFather 取得
export BOT_TELEGRAM_USER_ID="你的 Telegram 數字 ID"
export MODEL_API_KEY="端點需要的 key（若不需要可留空字串）"

python bootstrap_test_bot.py --check --config bot.json   # 只做設定檢查，不連網
python bootstrap_test_bot.py --config bot.json           # 正式啟動
```

`--check` 會驗證設定欄位、路徑、人設檔與端點允許清單，不會啟動服務或連 Telegram——建議每次改設定都先跑一次。

## 設定檔

最小可用欄位：

```json
{
  "root": ".",
  "db": "companion.sqlite3",
  "owner_id": "local-owner",
  "character_id": "example-companion",
  "persona_file": "personas/example_companion.txt",
  "l0_dir": "personas",
  "model_url": "http://localhost:8080/v1/chat/completions",
  "model_id": "your-model-name",
  "telegram_token_env": "BOT_TELEGRAM_TOKEN",
  "telegram_user_id_env": "BOT_TELEGRAM_USER_ID",
  "model_api_key_env": "MODEL_API_KEY"
}
```

- `*_env` 欄位填的是**環境變數名稱**，不是值。設定檔可以進版控，憑證不會。
- `model_url` 必須是 loopback 或明列在 `bot_config.py` 白名單中的端點（避免把 key 送去任意網域）。
- 選填 `model_choices`：多個後端時填這個陣列，即可用 `/model` 切換。

## 模型切換

```json
"model_choices": [
  {"label": "Cloud", "model_url": "https://api.example.com/chat/completions",
   "model_id": "your-cloud-model", "model_api_key_env": "CLOUD_API_KEY"},
  {"label": "Local GPU", "model_url": "http://localhost:8080/v1/chat/completions",
   "model_id": "your-local-model", "model_api_key_env": "MODEL_API_KEY"}
]
```

第一個是預設值。在 Telegram 打 `/model` 會出現每顆一列的 inline 按鈕，按下即切換，選擇寫入 `model-choice.json`（放在資料庫同目錄）。

## 思考預算

| 端點 | 行為 |
|---|---|
| 一般端點 | 預設 `chat_template_kwargs: {"enable_thinking": false}` |
| 支援 budget 的端點 | 帶 `reasoning_budget_tokens`（預設 128） |
| 環境變數 `THINK_MODE=off` | 明確關閉思考 |

實測（Qwen 系 3-bit / 4-bit 量化）：關閉思考時約 1/3 的回覆會短於 5 字或空白；給 64 token 仍不穩，128 較穩，150 反而變差。若你的模型不同，請自行量測再調整。

## 測試

```bash
python -m unittest discover -s . -p "test_*.py" -t .
```

555 項測試，不需要網路、不需要真的模型或 Telegram token（外部呼叫都以假 opener 取代）。

## 設計取捨

- **SQLite 而非 Postgres**：單人使用、要能離線、備份就是一個檔案。代價是不做水平擴展——這個專案也不需要。
- **單一擁有者**：`owner_id` 貫穿所有資料表，非擁有者的訊息在 handler 層就擋掉。這不是多租戶設計。
- **不用框架重寫**：FastAPI/ORM 會讓記憶交易邊界變模糊；這裡直接寫 SQL，換來的是可以精確控制 `BEGIN IMMEDIATE` 與回滾範圍。
- **不假裝是真人**：人設檔明寫角色是角色，被直接問時要坦白。

## 狀態

個人使用中的專案，尚未做多實例或大規模部署驗證。歡迎開 issue 討論設計。

## 授權

MIT，見 `LICENSE`。
