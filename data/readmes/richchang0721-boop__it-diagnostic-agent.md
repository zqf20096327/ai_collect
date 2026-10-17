[English](README.en.md) | **繁體中文**

# IT Diagnostic Agent — 智慧 IT 故障排除助手

> 互動式決策樹 + 深度排查引導 + AI 診斷，專為 IT 工程師設計的免費開源工具

![License](https://img.shields.io/badge/license-MIT-green)
![Static](https://img.shields.io/badge/deploy-static%20HTML-blue)
![Multi-LLM](https://img.shields.io/badge/LLM-Claude%20%7C%20Gemini%20%7C%20OpenAI%20%7C%20Ollama-orange)

---

## 功能概覽

- **互動式決策樹** — 涵蓋網路、硬體、軟體三大診斷模組
- **深度排查引導** — 引導式 YES/NO 步驟流程，適合凌晨三點腦袋不清醒時使用
- **決策樹編輯模式** — 不需要寫程式，用表單即可新增/修改診斷內容
- **Runbook 模式** — 隱藏 AI 面板，純決策樹介面，適合企業內部 SOP 展示
- **多模型支援** — Claude、Gemini、OpenAI 相容、Ollama 本地模型
- **Ollama 確認提示** — 切換本地模型時自動提示部署檢查清單
- **深色 / 淺色主題** — 一鍵切換，偏好自動儲存
- **零依賴部署** — 純靜態 HTML，不需後端
- **繁體中文 / English 雙語介面**

---

## 深度排查引導

點擊「🔍 深度排查」按鈕進入引導式步驟模式：

- **逐步 YES/NO 引導**，一次只看一個問題，不會資訊過載
- **技術細節可展開**，包含具體指令、線序、Beep 碼等參考資訊
- **三種結果類型**：
  - ✓ **已解決** — 找到問題根因，給出修復步驟
  - → **建議處理步驟** — 中間診斷結果，可繼續下一步或詢問 AI
  - ⚠ **升級二線** — 超出一線範圍，提供升級時需準備的資訊
- **可退回上一步**，不怕走錯路
- **詢問 AI 按鈕** — 直接把當前診斷情境帶入 AI 對話

### 目前支援的深度排查場景

| 場景 | 步驟數 | 涵蓋內容 |
|------|--------|---------|
| 🖥️ 主機不開機 | 8 步 | 電源 → PSU → POST/Beep → RAM → 主板目視 → 最小系統 → CMOS 重置 |
| 🌐 網路斷線 | 8 步 | 範圍確認 → 燈號 → 測線器/線序 → IP 取得 → Ping 閘道 → Ping 8.8.8.8 → DNS |
| 🖨️ 印表機無法列印 | 8 步 | 電源 → 卡紙/耗材 → Ping IP → 列印佇列 → 其他電腦測試 → 測試頁 → 驅動 → GPO |

---

## 決策樹編輯模式

點擊右上角的「**編輯模式**」按鈕，即可在瀏覽器中直接編輯所有診斷內容，**完全不需要修改程式碼**。這讓任何 IT 人員都能維護與擴充診斷流程，不必依賴開發者。

### 編輯介面

進入編輯模式後，主畫面切換為左側編輯器 + 右側即時預覽，分為兩個分頁：

- **GUIDES 步驟編輯** — 編輯深度排查的引導步驟
- **節點卡片編輯** — 編輯決策樹卡片的文字內容

### GUIDES 步驟編輯

- **新增、刪除與重新命名 GUIDES Book**，不再限制於主機、網路及印表機
- 自訂 Book 的中英文名稱與裝置標籤
- **新增 / 刪除 / 排序**步驟（▲▼ 上下移動）
- 每個步驟可編輯中英文的問題、描述、技術細節
- **路由用下拉選單**選擇（前往下一步 / 跳至指定步驟 / 顯示結果），防止打錯
- 技術細節用文字框編輯，一行一項

### 節點卡片編輯

- **新增、刪除與排序** Network / Hardware / Software 節點
- 編輯卡片的徽章、顏色、標題、描述與步驟清單（中英文）
- 新增或刪除內容群組，適合一張卡片包含多組排查步驟
- 建立節點之間的**有向連線**，並設定中英文連線標籤
- 將任何節點連結到任意 GUIDES Book
- 點擊主決策樹的連線即可跳到目標節點
- 即時反映在預覽面板

### 將決策樹節點連結至 GUIDES Book

1. 點擊右上角的「**編輯模式**」。
2. 先到「**GUIDES 編輯**」建立或選擇一本 Book，設定中英文名稱並編輯其中的步驟。
3. 切換到「**節點卡片**」，在左側選擇要連結的決策樹節點。
4. 在右側表單找到「**深度排查 / Guide**」下拉選單，選擇目標 GUIDES Book。
5. 變更會自動儲存。離開編輯模式後，展開該節點即可看到「**🔍 深度排查 / Deep Diagnosis**」按鈕。
6. 點擊按鈕便會從所選 Book 的第一個步驟開始執行。

> 「節點連結 GUIDES Book」與「節點之間的有向連線」是兩種不同功能：前者啟動逐步診斷流程；後者是在決策樹中跳到另一個節點。

### 即時預覽

- 右側面板顯示**實際渲染畫面**（所見即所得）
- **每次輸入即時更新**，不需按儲存
- 跟隨目前的語系（中 / 英）顯示

### 安全機制

- 所有編輯**自動儲存**至瀏覽器 localStorage，重整頁面不遺失
- **刪除步驟**需要確認（破壞性操作）
- **「還原為預設」**按鈕：一鍵清除所有自訂內容，恢復原始診斷內容
- 編輯結果可**匯出為帶版本號的 JSON** 檔備份或分享（目前格式版本 2，仍可匯入版本 1）

### 匯出 / 匯入（設定 → 資料分頁）

- **匯出 JSON** — 將目前所有診斷內容下載為 `it-diagnostic-data.json`
- **匯入 JSON** — 上傳 JSON 檔覆蓋現有內容，匯入前有檔名確認與驗證（格式 / 版本 / 欄位檢查）

> 設計理念：使用者只能編輯「診斷內容」（卡片文字、步驟），介面字串與按鈕標籤保持鎖定，避免誤改破壞介面。

---

## 支援的 AI 模型

| Provider | 說明 | API Key |
|----------|------|---------|
| Claude (Anthropic) | 預設，診斷品質最佳 | ✅ 需要 |
| Gemini (Google) | 速度快，成本低 | ✅ 需要 |
| OpenAI 相容介面 | 支援 Kimi、Groq、DeepSeek 等 | ✅ 需要 |
| **Ollama（本地）** | 完全離線，零成本，資料不離開公司 | ❌ 不需要 |

### 建議的本地模型

| 模型 | 參數量 | 適用情境 |
|------|--------|---------|
| Gemma 3 12B | 12B | 個人使用，速度快 |
| Gemma 3 72B | 72B | 高品質診斷，需較高記憶體 |
| Gemma 4 E2B / E4B | 2B / 4B | 低資源環境，輕量部署 |
| Qwen3 8B | 8B | 中文優化，適合華文環境 |
| Qwen3.6 35B-A3B | 35B | 高品質，MoE 架構省資源 |

---

## 三階段企業導入建議

### 第一階段：純 Runbook 模式
點擊右上角 📋 按鈕開啟 Runbook 模式，隱藏 AI 面板。
- 零資安風險，不連任何外部服務
- 搭配深度排查引導，讓新人也能獨立排障

### 第二階段：雲端 LLM（低敏感度案例）
適合：印表機、Outlook、DNS、Wi-Fi、NAS。
**注意**：不要輸入帳號密碼、IP 位址表、AD 管理帳號等敏感資訊。

### 第三階段：本地模型（資安要求高的環境）
使用 Ollama 在本機或內網跑模型，資料完全不離開公司。

---

## 快速開始

### GitHub Pages（推薦）
1. Fork 此 repository
2. Settings → Pages → Source 選 `main` branch
3. 訪問 `https://你的帳號.github.io/it-diagnostic-agent`

### 本機使用
```bash
git clone https://github.com/richchang0721-boop/it-diagnostic-agent.git
open index.html
```

---

## Ollama 本地模型設定

### 本機部署
```bash
# 安裝 Ollama
curl -fsSL https://ollama.com/install.sh | sh

# 下載模型
ollama pull gemma3:12b
ollama pull qwen3:8b
ollama pull gemma4:e2b

# 啟動服務
ollama serve
# 端點：http://localhost:11434
```

### 區網部署（全公司共用）
```bash
# 允許外部連線
export OLLAMA_HOST=0.0.0.0
ollama serve

# 員工端點設定：http://192.168.x.x:11434
```

### 帳密控管建議

| 方案 | 說明 | 難度 |
|------|------|------|
| 網路層隔離 | Ollama 只綁定內網 IP | ⭐ 簡單 |
| VPN 控管 | 需連 VPN 才能存取，整合現有 AD | ⭐⭐ 中等 |
| Nginx + Basic Auth | 反向代理加帳密驗證 | ⭐⭐ 中等 |
| OpenID / LDAP | 整合 AD 帳號，企業級 | ⭐⭐⭐ 複雜 |

---

## 涵蓋範圍

### 網路
- CCTV / IP Camera / NVR（PoE、影像斷線、遠端存取）
- Wi-Fi / AP / 802.1X
- DNS 解析失敗
- ISP 線路故障與備援切換

### 硬體
- 伺服器 / PC（POST、開機、效能）
- NAS（RAID 降級、SMB/NFS 存取）
- 印表機（網路列印、驅動、Print Spooler）

### 軟體
| 系統 | 涵蓋範圍 |
|------|----------|
| Active Directory | 帳號鎖定、GPO、DC 複寫、FSMO 轉移 |
| SQL Server | 連線失敗、效能優化、備份還原 |
| Exchange Server | 郵件佇列、SPF/DKIM、遷移至 M365 |
| Office | 部署、KMS 授權、修復 |
| Outlook | Autodiscover、OST 修復、OAuth 2.0 |

---

## 疑難排解

### Ollama 出現 `Failed to fetch`

這是 Ollama 的 CORS（跨來源資源共用）限制造成的。Ollama 預設不允許跨來源請求，當瀏覽器（特別是 GitHub Pages 的 HTTPS 頁面）嘗試呼叫本地 Ollama API 時會被擋下。

**解決方法**：設定 `OLLAMA_ORIGINS` 環境變數允許跨來源連線。

**Windows（PowerShell）**
```powershell
# 臨時設定
$env:OLLAMA_ORIGINS="*"
ollama serve

# 永久設定
[System.Environment]::SetEnvironmentVariable('OLLAMA_ORIGINS', '*', 'User')
```

**macOS / Linux**
```bash
OLLAMA_ORIGINS="*" ollama serve
```

**macOS（永久設定）**
```bash
launchctl setenv OLLAMA_ORIGINS "*"
```

設定後重啟 Ollama 服務即可。

> 安全提醒：`OLLAMA_ORIGINS="*"` 允許所有來源連線，適合個人或內網環境。若是正式部署，建議改為指定來源，例如 `OLLAMA_ORIGINS="https://你的網域"`。

### 透過 HTTPS 存取本地 Ollama 被封鎖

GitHub Pages 是 HTTPS，瀏覽器安全限制會封鎖 HTTPS 頁面呼叫 HTTP 的本地端點（Mixed Content）。

**解決方法**：
- 將 `index.html` 下載後在本機直接開啟（`file://` 或 `http://localhost`）
- 或為 Ollama Server 設定 HTTPS 反向代理

---

## 授權

MIT License — 自由使用、修改、商業用途均可

---

## 資源

- [Anthropic API](https://console.anthropic.com)
- [Gemini API](https://aistudio.google.com)
- [Ollama 官網](https://ollama.com)
- [線上試用](https://richchang0721-boop.github.io/it-diagnostic-agent)
