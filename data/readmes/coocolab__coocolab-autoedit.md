# Coocolab AutoEdit｜錄完丟進來，AI 幫你剪

[![License: MIT](https://img.shields.io/github/license/coocolab/coocolab-autoedit)](LICENSE)
[![Latest release](https://img.shields.io/github/v/release/coocolab/coocolab-autoedit)](https://github.com/coocolab/coocolab-autoedit/releases/latest)
[![CI](https://github.com/coocolab/coocolab-autoedit/actions/workflows/ci.yml/badge.svg)](https://github.com/coocolab/coocolab-autoedit/actions/workflows/ci.yml)

口播影片的 AI 自動剪輯工具。你照常錄，卡住、重講、停頓都沒關係，把影片丟進資料夾，跟 Claude Code 或 Codex 說一句「幫我剪這支」就好。剪片、上字幕、字卡、音量都會處理，全部在你自己的電腦上跑，免費開源。

[![剪片 5 小時變 0？AI 自動剪輯＋上字幕，整套免費開源 autoedit v1｜酷可實驗室](https://i.ytimg.com/vi/A5-Xyjmkzxk/maxresdefault.jpg)](https://youtu.be/A5-Xyjmkzxk)

**▶ [看影片了解怎麼用](https://youtu.be/A5-Xyjmkzxk)**（點上面的圖也可以）

### 👉 [一鍵安裝 prompt：複製、貼進 Claude Code 或 Codex 就開始裝](https://coocolab.com/member/resources/?slug=one-click-edit)

三步開始：**複製安裝 prompt** → **貼進 Claude Code／Codex，照它的問題回答** → **把影片放進 `AI剪片/原片/`，說「幫我剪這支」**。想自己動手裝，看下面的[手動安裝](#手動安裝)。

> 酷可實驗室，酷的實驗你也可以。

## 它會做什麼

| 步驟 | 內容 |
|---|---|
| 聽打 | 把人聲切成一段一段分開聽打，講到一半重講也抓得到 |
| 剪掉清單 | AI 標出重講、卡住、語助詞、喊卡，**先列清單給你確認**，你說 OK 才剪 |
| 剪片 | 剪點逐格對齊，嘴型不會跑掉。太長的停頓會縮短，跳剪時交替放大一點點，看起來像換鏡頭 |
| 字幕 | 字跟著聲音一個一個跳，重點詞變橘色，中英文之間自動空格，另外輸出 .srt |
| 字卡 | AI 挑重點，講到那句話的時候字卡就彈出來 |
| 動態特效 | 跟人疊在一起的特效：字從頭後滑出、光沿著輪廓跑一圈、便條紙、數字卡、清單卡、會自己打字的指令列、照片牆、影片卡、3D 軌道 |
| 語速 | 量你每秒講幾個字，建議要不要整支加速。音調不變 |
| 音量 | 調到 -14 LUFS（YouTube／IG 的標準音量），人聲放在左右聲道正中間 |
| 封面 | 挑一格畫面，加上大標題 |

全部在你自己的電腦上跑，不用月費，影片不會上傳到任何地方。

## 安裝（最簡單的方法）

到 **[免費資源區的「一鍵剪片」頁面](https://coocolab.com/member/resources/?slug=one-click-edit)** 複製安裝 prompt，整段貼進 Claude Code 或 Codex。它會：
1. 檢查你的電腦：Mac 還是 Windows、夠不夠力、缺哪些工具。
2. 只下載你缺的東西，每裝一樣都會先問你。
3. 建好 `AI剪片` 資料夾，裡面有「原片」和「成片」兩個資料夾。

## 手動安裝

需要：Python 3.10～3.13（建議 3.12）、ffmpeg 5.1 以上、Git。

```bash
git clone https://github.com/coocolab/coocolab-autoedit.git
cd coocolab-autoedit
python3 install/setup.py check      # 看缺什麼（什麼都不裝）
python3 install/setup.py install    # 建環境、裝套件、下載字型、建 AI剪片 資料夾（預設在桌面）
```

- Windows 把 `python3` 換成 `py`。
- `install` 會一次裝完 Python 套件和字型（下載幾百 MB，裝好後 `.venv` 約 1.5 GB；語音模型另外約 1.5 GB，第一次聽打時才下載），約 1～5 分鐘。指令不要被中斷；被中斷的話重跑一次就好，已經裝好的會跳過，下載到一半的檔案會重新下載。
- 「AI剪片」資料夾預設放桌面。但如果桌面會同步到雲端（Mac 開了「iCloud 桌面與文件」、Windows 桌面被 OneDrive 接管），會改放在家目錄底下的 `AI剪片`，因為幾 GB 的影片會一直上傳。真的要放雲端資料夾，加 `--allow-cloud`。指定位置用 `--folder 路徑`。
- 動態特效用的 MediaPipe 是選用的（`requirements-fx.txt`）。裝不起來時只有特效不能用，其他功能照常。
- Linux：Ubuntu 22.04 的 apt ffmpeg 是 4.4，太舊，請用 `sudo snap install ffmpeg` 或靜態版；動態特效需要 `sudo apt install libgl1 libegl1 libgles2`。
- 重跑 `install` 時，如果 `AI剪片` 裡的 `CLAUDE.md`／`AGENTS.md` 被你改過，舊的會先備份成 `.bak-日期`。

## 怎麼用

1. 把影片放進 `AI剪片/原片/`。
2. 在 `AI剪片` 資料夾打開 Claude Code（或 Codex）。
3. 說「幫我剪這支」。

這個資料夾裡的 `CLAUDE.md`／`AGENTS.md` 會告訴 AI 整個流程和規矩，所以不用再貼任何 prompt。

聽打、剪片、特效、輸出都可能跑超過 2 分鐘（長片要十幾分鐘）。`CLAUDE.md` 已經提醒 AI 用最長的指令逾時或背景執行；如果還是被中斷，重跑同一步就好，每一步都可以安全重跑。

手機直拍（帶旋轉資訊）、螢幕錄影這類「可變幀率」影片、iPhone 的 HDR 影片，聽打前會先在 `工作區/` 轉一份工作檔（原片不動），剪出來才不會變形、不同步或偏灰。

也可以自己下指令：

```bash
AE="<.venv 裡的 python> <這個 repo>/ae.py"
$AE init "原片/我的影片.mp4"
$AE transcribe 工作區/我的影片
$AE suggest 工作區/我的影片        # → 剪掉清單.md，看過、改好 cuts.json
$AE cut 工作區/我的影片
$AE subs 工作區/我的影片           # → subtitles.txt，錯字寫進 fixes.json
$AE fx 工作區/我的影片             # 照 fx.json 做動態特效（可省略）
$AE finish 工作區/我的影片         # → 成片/我的影片.mp4 + .srt
$AE cover 工作區/我的影片 12.5 "主標" "副標"
$AE --version
```

Windows 的 PowerShell 要在最前面加 `& `（`& "<python>" "<ae.py>" init ...`）。安裝時產生的 `CLAUDE.md` 會寫好兩種寫法。

## 聽打引擎

| 電腦 | 用什麼 | 速度（15 分鐘的影片） |
|---|---|---|
| Mac（M 系列晶片） | mlx-whisper，large-v3-turbo | 幾分鐘 |
| 有 NVIDIA 顯示卡 | faster-whisper，large-v3-turbo | 幾分鐘 |
| 其他（只有 CPU） | faster-whisper，medium | 比較久，可以先去泡咖啡 |

第一次會自動下載模型，約 1.5 GB。

## 錄影小技巧

- 講錯就停一秒，從那句的**開頭**重講。AI 會留最後一次講完整的。
- 不要在一句話中間接著重講，停一下再講，比較好剪。
- 收音盡量安靜。只有一邊聲道有聲音也沒關係，工具會自動處理。

## 想改成你自己的

這套是一個架構，不是一個黑盒子。有剪輯經驗、或有自己想要的功能，都可以拿去改：

- `autoedit/suggest.py`：判斷要剪什麼的規則。
- `autoedit/cut.py`：停頓長度（`LONG_PAUSE`、`PAUSE_KEEP`）、放大倍率（`PUSH_IN`）。
- `autoedit/finish.py`：字幕和字卡的樣式、顏色、位置。
- `autoedit/fx.py`：動態特效，每一種都是一個 class，可以照著加新的。
- `agent/AGENTS.template.md`：AI 的工作流程和規矩。

改完歡迎發 PR。測試：

```bash
.venv/bin/python -m unittest discover -s tests -v   # 單元測試（不需要影片）
.venv/bin/python tests/e2e_synthetic.py             # 用 ffmpeg 做假影片，跑完整流程（不需要語音模型）
```

GitHub Actions 會在 Windows、macOS、Linux 上跑這兩個。

## 支援平台與已知限制

| 平台 | 狀態 |
|---|---|
| Mac（M 系列） | 作者實測，包含聽打 |
| Windows 10／11（x64）、Linux（Ubuntu 24.04）、Intel Mac | 安裝、剪片、字幕、特效有自動測試（CI）；聽打模型沒有在這些平台實測，歡迎回報 |

- **Windows 用 winget 裝完 ffmpeg／Python 後**，新的 PATH 只對新開的程式有效：要把 Claude Code／Codex 整個關掉重開，再貼一次安裝 prompt，它會從檢查環境開始、跳過已經裝好的。
- **Windows ARM（Snapdragon 筆電）**：聽打套件沒有 ARM 版，請裝 x64 版的 Python 3.12（會用模擬執行，比較慢）。
- **Windows 使用者名稱是中文**時，動態特效載入模型可能失敗（沒實測）。遇到的話把這個 repo 放到純英文路徑，例如 `C:\coocolab-autoedit`，再重跑 install。
- **Intel Mac**：MediaPipe 最後一版 Intel 版只支援到 Python 3.12，所以安裝會優先用 3.12；用 3.13 的話動態特效不能用。
- **Linux**：MediaPipe 新版會用到 `sounddevice`，少了 libportaudio 時可能無法 import，只影響動態特效。
- **很長的影片**（1 小時以上）：聲音會整段讀進記憶體，8 GB 記憶體的電腦可能不夠，建議先切成幾段。
- **有 NVIDIA 顯示卡但沒裝 CUDA／cuDNN**：聽打會自動改用 CPU（比較慢）。
- **搬動了這個 repo 的資料夾**：`.venv` 和 `CLAUDE.md` 裡記的是絕對路徑，搬完要重跑一次 `install`。
- 套件版本有設上限（見 `requirements*.txt`），是實際裝起來、跑過的版本範圍。

## 用到的開源專案

完整的授權說明（含模型權重、字型）見 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

- [Whisper](https://github.com/openai/whisper) 語音模型（MIT）
- [faster-whisper](https://github.com/SYSTRAN/faster-whisper)（MIT）
- [mlx-whisper](https://github.com/ml-explore/mlx-examples)（MIT）
- [OpenCC](https://github.com/BYVoid/OpenCC)：簡轉繁（Apache 2.0）
- [MediaPipe](https://github.com/google-ai-edge/mediapipe)：人像去背，用在動態特效（Apache 2.0），模型第一次使用時下載
- [OpenCV](https://opencv.org)（Apache 2.0）
- [Noto Sans TC](https://github.com/notofonts/noto-cjk)：字型（SIL OFL 1.1），安裝時下載
- [FFmpeg](https://ffmpeg.org)：影音處理，需要自己另外安裝

## 授權

MIT。可以自由使用、修改、商用，保留原作者聲明就好。

## 支持這個專案

覺得好用的話：

- 幫這個 repo 按個 ⭐ Star，讓更多人找得到。
- 到 YouTube 訂閱 [酷可實驗室](https://www.youtube.com/@coocolab)，之後的更新和新教學都會發在那裡。
- 到 [Discussions](https://github.com/coocolab/coocolab-autoedit/discussions) 分享你剪出來的片，或是提問、回報問題。
