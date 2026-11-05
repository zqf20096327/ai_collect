<h1 align="center">說人話 zh-TW</h1>

<p align="center">
  <strong>繁體中文（臺灣）AI 味清理 Skill —— 讓 AI 寫的稿子，讀起來像你寫的。</strong>
</p>

<p align="center">
  去 AI 腔 ・ 清中港用語 ・ 修簡轉繁錯字 ・ 教育部標點規範 ・ 七種出版語體 ・ 60 分品質評分
</p>

<p align="center">
  給 Claude Code、Codex、Cursor、ChatGPT 和自建 agent 用的開源 Skill。
</p>

<p align="center">
  <a href="README.md">繁體中文（臺灣）</a> ・ <a href="README.en.md">English</a>
</p>

<p align="center">
  <a href="#為什麼做這個專案">為什麼做這個</a> ·
  <a href="#30-秒上手">30 秒上手</a> ·
  <a href="#它會做什麼">功能</a> ·
  <a href="#它怎麼判斷怎麼改">運作原理</a> ·
  <a href="#常見問題">FAQ</a> ·
  <a href="#關於-tenten-ai">關於我們</a>
</p>

---

> **English TL;DR** — `shuorenhua-zh-tw` is an open-source AI humanizer skill for **Traditional Chinese (Taiwan)**. It removes AI-flavored writing patterns (sycophantic openers, empty conclusions, buzzword inflation), replaces Mainland Chinese terms with Taiwanese usage (軟件→軟體, 視頻→影片, 用戶→使用者), fixes Simplified-to-Traditional conversion artifacts, applies Taiwan's official punctuation standards, and offers seven publishing genre presets with a 60-point quality score. Works as a Claude Code Skill, with install guides for Codex, Cursor, and ChatGPT. Forked from [MrGeDiao/shuorenhua](https://github.com/MrGeDiao/shuorenhua), merged with [tentenco/Better-Humanizer-zh-TW](https://github.com/tentenco/Better-Humanizer-zh-TW). **[Full English README →](README.en.md)**

---

## 為什麼做這個專案

我們是每天用 AI 寫東西的人。電子報、白皮書、客戶提案、粉專貼文、技術文件——AI 幫我們省下大量初稿時間，但交出去之前，總有一關過不去：

**每個字都對，但一看就不是你寫的。**

開頭先頒獎（「這是一個很好的問題！」），中間硬拔高（「這不僅僅是一次更新，更是一場革命」），結尾上價值（「讓我們拭目以待」）。這些句子單獨看都沒錯，堆在一起就是一股洗不掉的機器味。

繁體中文使用者還多一層問題。模型的中文語料以簡體為主，寫出來的「繁體」常常只是簡轉繁：**軟件、視頻、用戶、信息**滿天飛，「賦能」「抓手」「閉環」這些對岸職場用語混在臺灣的稿子裡，編輯一眼看穿。英文世界有 [stop-slop](https://github.com/hardikpandya/stop-slop) 和 [humanizer](https://github.com/blader/humanizer)，簡中世界有很成熟的「說人話」，但臺灣的寫作者一直夾在中間——工具是別人的語境，問題卻是我們天天遇到的。

所以我們動手做了兩件事：

1. **2025 年，我們做了 [Better-Humanizer-zh-TW](https://github.com/tentenco/Better-Humanizer-zh-TW)**：研究了 GitHub 上五個熱門中文 humanizer，整合成一個為臺灣出版場景設計的技能——臺灣用語對照、教育部標點規範、七種出版語體、品質評分。
2. **然後我們遇到了 [MrGeDiao/shuorenhua](https://github.com/MrGeDiao/shuorenhua)**：一個工程紀律好得令人佩服的簡中專案。它不是詞表替換器，而是一套完整的判斷流程——先劃保護片段再動筆、按場景控制力度、長文走刪除清單不縮水、75 條評測用例守住誤殺邊界。這些是我們前作沒有做到的深度。

這個專案就是兩者的合併：**用簡中版的工程紀律，做繁中版的在地品質。** 流程骨幹來自 shuorenhua，臺灣化能力來自 Better-Humanizer-zh-TW，再加上我們把兩邊接起來時補的新東西（臺灣化檢查獨立成軸、出版場景整合進主流程、繁中評測集）。

## 它幫助了我們什麼

說幾個我們自己的真實用法：

- **電子報和粉專貼文**：AI 打草稿，skill 過一遍，把「在這個快速變化的時代」這類開場和硬凹的金句清掉，發文前不用再逐句手改。
- **客戶提案和白皮書**：`whitepaper` 語體會把「賦能、閉環、打造」全清（這批詞在臺灣稿件裡同時是 AI 味和對岸用語，雙重扣分），缺具體數據的地方它會標出來要我們補，而不是替我們編。
- **技術文件**：簡轉繁殘留的「服務器、緩存、內存」一次抓乾淨，而且不會誤改程式碼、命令和引用原文——這是我們以前用純詞表替換工具最常踩的雷。
- **審稿**：annotation mode 只標問題不動稿，適合改別人的稿子時先給意見。

最實際的收穫是心理上的：**交稿前不用再焦慮「這段會不會被看出來是 AI 寫的」。** 因為過完這一遍，它就是你的稿子——事實是你的、判斷是你的、用語是臺灣的，只是初稿的體力活讓模型代勞了。

## 它會做什麼

| 場景 | 它會做什麼 |
|------|------------|
| 日常聊天 | 刪掉過度承接、推銷式結尾和工程報告腔，保留口語感 |
| 技術狀態同步 | 保住事實、版本、命令、錯誤訊息和責任歸屬，壓低套話 |
| README / release note | 先講清楚專案、變更、驗證和限制，不寫發布宣言 |
| 論壇文 / issue 回覆 | 像維護者在認真溝通，不像客服公告或行銷稿 |
| 中文長文 | 句內清理保住節奏，整句空話列「建議刪除」清單交你確認，不讓長文越改越短 |
| 出版稿件 | 七種語體預設（學術／白皮書／雜誌／新聞／內刊／教科書／文學），60 分品質評分，術語全篇鎖定 |
| 臺灣化檢查 | 150+ 條中港用語對照、簡轉繁錯字、教育部標點規範，讀起來像臺灣人寫的 |

### 改成什麼樣

**聊天答疑，先頒獎再推銷：**

> ❌ 你說的很對，這個問題一針見血。一句話總結：核心邏輯是先把流程跑通，再談優化。要不要我順手把文檔也整理了？你一句話的事。
>
> ✅ 對，問題就在這：先把流程跑通，再談最佳化。文件要不要一起弄？

**簡轉繁殘留＋AI 套話的雙重問題：**

> ❌ 值得注意的是，該軟件通過對用戶數據的深度挖掘，不僅顯著提升了視頻加載速度，更是重新定義了信息獲取的方式。
>
> ✅ 這套軟體改了資料查詢方式之後，影片載入從 3 秒降到 0.8 秒。

**出版稿的宏大開場：**

> ❌ 在這個瞬息萬變的時代，我們必須擁抱變化、擁抱挑戰、擁抱未知。這不僅是一種選擇，更是一種必然。讓我們拭目以待。
>
> ✅ 我也說不準變化的速度——只是這幾年寫稿的時候，我發現自己比以前更常停下來查資料。可能是時代變快，也可能是我變慢。

更多對照見 [references/examples.md](references/examples.md)。

## 30 秒上手

**Claude Code** — 放進 skills 目錄，之後自動觸發：

```bash
git clone https://github.com/tentenco/shuorenhua-zh-tw.git ~/.claude/skills/shuorenhua
```

裝好後在對話裡說「把這段去 AI 味」「檢查臺灣用語」「幫我改成能發的稿子」就會命中。想跟隨倉庫更新，用軟連結代替複製，見 [install/claude-code.md](install/claude-code.md)。

**Codex** — clone 後單次使用：

```bash
codex exec -C . "讀取 ./SKILL.md，按其中規則改寫以下文本：……"
```

**只想先看問題、不要改稿**：指令裡加一句「按 annotation mode 只標註不改寫」。

Cursor、OpenClaw、ChatGPT Custom GPT 的安裝方式見 [install/](install/) 目錄。

## 它怎麼判斷怎麼改

`說人話` 不是見詞就替換。一句話原則：

> **先保資訊，再談風格。**

完整流程固定九步：

1. 判場景：`chat / status / docs / public-writing / publishing`；命中 README、release note、論壇文、issue 回覆時，再進對應的 Scene Pack；出版稿再判七種語體之一
2. 劃保護片段：數字、版本、命令、路徑、錯誤訊息、引用原文、人名和責任歸屬先鎖住（[references/protected-spans.md](references/protected-spans.md)）
3. 臺灣化檢查：中港用語、簡轉繁錯字、標點慣例（[references/taiwan-localization.md](references/taiwan-localization.md)、[references/typography.md](references/typography.md)）
4. 按命中強度定 Tier，按力度定檔位（`minimal / standard / aggressive`），按能刪到什麼程度定 scope（`structural / bounded / in-place`）
5. 先按模式改，詞表只補漏
6. 保真回讀：事實、術語、語域、保護片段、臺灣化逐項過
7. 仍有殘味才做第二遍 Residual Audit，只允許輕量修正
8. 輸出單一推薦版本；`publishing` 場景附變更摘要、60 分評分和未解決疑問
9. 使用者要求時切 annotation mode：只標問題，不動稿

### 長文不縮水：三檔 scope

長文按預設動作改寫，刪句、併句會疊加，1800 字可能被壓到 1000 字；反過來一句不刪，整句空話又留在文裡。所以「刪到什麼程度」單獨分三檔，和力度正交：

| scope | 刪整句嗎 | 適用 |
|-------|----------|------|
| `structural` | 自由刪併重排 | 短文、明確要重寫 |
| `bounded`（長文預設） | 整句空話列成「建議刪除（待確認）」清單，刪多少你決定 | `public-writing` / `publishing` 長文 |
| `in-place` | 一句都不刪，只句內降調 | 明確要求「完全原樣」 |

### 誤殺防護是一等公民

會咬人的替換工具沒人敢用在正式稿上。這個 skill 花在「什麼不能改」上的規則，和「什麼該改」一樣多：

- 引用簡體原文？引號內連字形都不轉。
- 「微信」「支付寶」「個人信息保護法」？專有名詞，不改成 LINE 或個資法。
- 學術論文的被動句和重複術語？語體要求，放行。
- 公文裡的「業已、予以、以資」？正式公文的固定寫法，不是 AI 腔。
- 工程師說「接住了 2.4 萬 QPS」？有指標有系統主語，是技術描述不是姿態。

完整邊界見 [references/severity.md](references/severity.md) 和 [references/boundary-cases.md](references/boundary-cases.md)。

## 評測

規則層覆蓋 210+ 中文短語、96 條英文短語、24 類結構反模式、150+ 條臺灣用語對照。

- 繁中臺灣情境評測集：[evals/zh-tw-cases.md](evals/zh-tw-cases.md)（中港用語、標點、出版語體、誤殺邊界）
- 上游簡中版的 75 條 benchmark（[evals/benchmark.md](evals/benchmark.md)）保留為模式層回歸資產
- 對照上游 v1.9.1 的實跑結果：臺灣化與出版合約用例，新版全數通過，舊版在「任務沒有明說要臺灣化」時會殘留中港用語

## 常見問題

### 這是不是拿來騙 AI 偵測器的？

不是。目標是減少模板感、表演感和語域漂移，讓文本更自然、更可發布，不是繞過偵測。事實查核和來源補齊仍然是作者的責任——它遇到「研究表明」這種無來源引用，只會標出來，不會替你編一個出處。

### 和簡中版「說人話」差在哪？

流程一樣，語言層完全不同：全繁體（臺灣用語）、獨立的臺灣化檢查步驟、教育部標點規範、七種出版語體與品質評分、術語一致性鎖定。目標讀者在中國大陸的話，用[上游版](https://github.com/MrGeDiao/shuorenhua)更合適。

### 和 Better-Humanizer-zh-TW 差在哪？

那是我們的前作，定位是出版稿的單頁規則集。這個專案繼承了它全部的臺灣化能力，另外補上它沒有的：分場景力度控制、保護片段預檢、長文不縮水機制、annotation mode、評測體系。日常聊天、技術文件、社群貼文這些非出版場景，前作會綁手綁腳，這版各有各的檔位。

### 丟簡體稿進來會怎樣？

預設輸出繁體（臺灣用語）。引用原文、程式碼、命令維持原字形；明確要求保留簡體時，它只做去 AI 味。

### 會不會把技術文件改壞？

正常不會。`docs`、`status`、`code-context` 都有更保守的保護策略，命令、路徑、版本、錯誤訊息和指標優先保真。

### 只裝 SKILL.md 一個檔案能用嗎？

能。`SKILL.md` 內建單檔後備規則（基礎清理＋臺灣化替換＋標點基礎）；完整能力需要 `references/` 目錄，長期使用建議整包裝。

## 關於 Tenten AI

我們是 [Tenten](https://tenten.co)，一支把前沿 AI 當日常工具用的團隊。

我們的日常大概是這樣：新模型、新協定出來的第一週就上手用；把用出心得的工作流寫成 Skills、發成開源專案；再把過程中學到的東西整理出來公開分享。我們特別著迷 **Agent Skills** 這個方向——把一個領域的專業判斷（例如「臺灣編輯怎麼看稿」）寫成模型讀得懂、執行得穩的規則，一次寫好，處處能用。這個專案和 [Better-Humanizer-zh-TW](https://github.com/tentenco/Better-Humanizer-zh-TW) 都是這條路上的產物。

我們相信好的 Skill 和好的文章一樣：具體、誠實、經得起用。如果這個專案幫你省下了改稿時間，歡迎回來提一個 bad case——那比 star 更能讓它變好（當然，star 我們也很開心）。

同一套日常，也長成了我們的商業服務：

- **[Tenten GEO](https://geo.tenten.co/en)** —— 讓 AI 搜尋引擎推薦你的品牌。GEO（生成式引擎最佳化）不是一次性顧問案，而是持續運轉的系統：AI 可見度健檢、每週追蹤 ChatGPT／Perplexity／Google AI Overviews 的引用狀況、按週期改寫內容，成效看 pipeline 貢獻，不看虛榮流量。
- **[Tenten AI](https://www.tentenai.com/en)** —— 企業 AI 導入。Copilot 部署、agentic workflows、RAG 知識系統、預測模型；同一組團隊從策略、工程做到上線維運，第一個真正進 production 的 AI 應用以週計，不以季計。

這個 skill 讓 AI 寫的字像人；GEO 讓 AI 引擎引用你的品牌。產品不同，功夫是同一套：天天泡在 AI 怎麼讀、怎麼寫、怎麼推薦的第一線。

- 每天一手 AI 觀察：[tenten.co/learning](https://tenten.co/learning/)
- 更多開源專案：[github.com/tentenco](https://github.com/tentenco)

## 貢獻：bad case 比 star 有用

歡迎提交評測樣本、邊界案例、臺灣用語對照詞條、改寫前後樣本和誤殺回報。提交前先想一件事：

> 這是一個「新模式」，還是只是「現有模式的變體」？

詳細規則見 [CONTRIBUTING.md](CONTRIBUTING.md)。請先去識別化，不要貼未授權私訊全文、金鑰、內部連結或真實個資。

## 相關專案

- [MrGeDiao/shuorenhua](https://github.com/MrGeDiao/shuorenhua)：簡中版「說人話」，本專案的流程骨幹來源
- [tentenco/Better-Humanizer-zh-TW](https://github.com/tentenco/Better-Humanizer-zh-TW)：出版級繁中 humanizer，本專案的臺灣化來源
- [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh)：中文 humanizer 圈的奠基專案
- [stop-slop](https://github.com/hardikpandya/stop-slop)：英文 AI slop 規則和評分框架
- [humanizer](https://github.com/blader/humanizer)：英文 AI 模式分類

## 授權

[MIT](LICENSE) — fork、改版、商用都歡迎，記得帶上授權聲明。

---

<p align="center">
  <sub>關鍵字：AI 味 / 去 AI 味 / AI 腔 / 說人話 / AI humanizer / AI text cleaner / 繁體中文 / 臺灣用語 / Traditional Chinese / zh-TW / 簡轉繁 / 中港用語 / 潤稿 / 校稿 / AI 寫作 / Claude Code Skill / Agent Skills / ChatGPT / 人性化改寫</sub>
</p>

<p align="center">
  <strong>由 <a href="https://tenten.co">Tenten AI</a> 建立並維護</strong>
</p>
