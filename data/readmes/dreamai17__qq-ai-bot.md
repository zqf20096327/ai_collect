# 如月栞 · QQ 群聊机器人（V0.3）

<div align="center">

**会聊天 · 会搜图 · 会汉化 · 会播报天气的 QQ 群聊 AI 机器人**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org)
[![OneBot 11](https://img.shields.io/badge/OneBot%2011-NapCatQQ-25A162)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-httpx-009688?logo=fastapi&logoColor=white)]()
[![LLM](https://img.shields.io/badge/LLM-DeepSeek-4D6BFE)](https://platform.deepseek.com)

[**简体中文**](#zh) · [**English**](#english) · [**繁體中文**](#hant) · [**日本語**](#ja)

</div>

---

<a id="zh"></a>
## 简体中文

一个基于 **NapCatQQ（OneBot 11）+ FastAPI + DeepSeek** 的 QQ 群聊机器人，内置完整人设「如月栞」——@ 它或喊它的名字（小栞 / 栞ちゃん / Shiorin / 栞栞 / 栞酱）就会回复。开箱即聊，不写代码也能跑：双击 `start.bat` 即可。

### 🔧 V0.3 修复版亮点

- 修复图片主动反应的并发冷却竞态，并持久化冷却状态，避免短时间重复反应。
- 优化识图找来源：修复未命中缓存异常、负缓存过期和配置冷却未生效问题。
- 配置台保存改为增量合并，不会因表单缺字段覆盖整份配置；保存成功会显示确认弹窗。
- 结构化人设编辑器改为只读合成提示词，统一通过 `persona.json` 编辑，避免内容保存丢失。
- 配额检查在放行后才增加好感度，超额消息无法借此升级限流档位。
- 人设 API 拒绝路径穿越；管理后台默认仅监听 `127.0.0.1`，API 密钥展示自动脱敏。

> 安全提示：后台默认只允许本机访问。若手动设置 `BOT_HOST=0.0.0.0`，请自行在反向代理或防火墙层增加访问控制。

### 🧩 功能特性

**💬 角色扮演**
- **完整人设「如月栞」**：17 岁软萌学妹 × 腹黑吐槽 × 病娇占有欲的调色盘人格，含世界观 / 外貌 / 亲密场景机制（Tavern 角色卡体系，可换卡）
- **称呼护栏（全路径·中央化）**：只有管理员会被叫「前辈」，群友一律用名字 /「你」——铁律收在 `chat_guard.py` 一处维护，发送层另有兜底重写
- **好感度限流**：新朋友 10 / 活跃群友 20 / 元老 40 次每日互动，管理员不限
- **关系卡**：与管理员相处自动沉淀「相处记忆」，场景触发注入（触发词快车道 + LLM 兜底 + 冷却）
- **长期记忆**：自动记住群友说过的事实（SQLite，24h 节流）
- **主动插嘴 / 图片反应**：群聊火热时偶尔冒泡，有人发图偶尔点评；冷场开话题后能**语义接住**追问
- **统一人设出口**：命令 / 识图 / 推送等模板文本发送前用角色口吻转述，CQ 码与链接先保护后还原，不 OOC

**🌐 联网搜索**
- 实时 / 事实类问题自动联网，**智能判域**优先垂直信源：番剧评分 Bangumi、galgame / 视觉小说走 **Bangumi 游戏库**、游戏价格 Steam、ACG 设定萌娘百科（必要时补 B站视频）、**GitHub 开源检索**（开源项目 / 找仓库 / 源码），无垂直信源用 Tavily / DuckDuckGo 兜底
- 通用搜索结果带**来源前缀**（【知乎网友帖】= 社区网友发言、【萌娘百科】= 客观资料页），模型不会把网友帖里「我求推荐 / 我不接受 XX」等第一人称偏好当成当前群友的观点
- 求推荐类**泛检索**自动去重 + 随机打散 + 质量排序，不会每次都推同一批 top 作品
- 用量统计（`data/search_usage.json`），可配每日限额

**🎨 图片能力**
- **识图找来源（搜出处）**：发图 + 「出处 / 搜图 / 谁画的 / 哪部番」→ SauceNAO 插画本子 + Trace.moe 动画截图兜底，MD5 缓存 7 天，H 源只发作品名不发外链；支持**跨消息两段式**（先字后图 90 秒内补图 / 先图后字 5 分钟内补意图）
- **漫画翻译汉化**：发图说「翻译一下」→ 可插拔检测（RapidOCR / **DBNet**）→ 气泡识别 → 批量翻译（DeepSeek 专用无思维链模型，或自接 OpenAI 兼容端点如本地 SakuraLLM）→ LaMa 擦字 → 绘制中文回发；OCR 乱码自动清洗 / 打标，可选整页顺稿；增强权重缺省自动降级
- **图片「图注」**：群里发图自动补一句视觉描述进上下文，AI 真正「看懂」群里的图

**📅 天气播报（和风天气 QWeather）**
- 配置台维护城市清单，每天到点（任意 HH:MM）向指定群推送**一张天气长图**：今日实况 + 24 小时 + 未来 7 天，左上角带城市名 + 地区行（Pillow 渲染，失败自动降级纯文本）
- 适配 2026 迁移：账号专属 **API Host** + `X-QW-Api-Key` 鉴权、AQI 与极端天气预警新版坐标接口、旧缓存自动重查

**📣 主动推送 & 情报监控**
- **pixiv 定时推送**：可配关键词 / R18 开关 / 每群负面标签过滤
- **B站视频推送**：官方接口自动选 1 周内最新，热门榜优先、官方搜索兜底，绝不推旧视频；内容级去重 + 每群负面词过滤（如排除「直播回放」「预告」），重启不丢
- **B站官方号动态监控**：定时检查预设官方号（原神官号等）新动态，角色口吻播报（WBI 签名，48h 新鲜窗口，停机回来不补旧闻）

**🔒 链接安全**
- **外链防风控（链接加密）**：群消息出口在链接**域名内部随机插一个汉字**（如 `https://www.pi中xiv.net/…`，www 开头优先打断 www 段）——QQ 拼不出合法网址，防外链风控吞链；幂等可重入，群友删掉那个字即可打开

**🛠️ 工程 & 后台**
- **可视化管理后台**：`http://127.0.0.1:8010/admin`——深 / 浅双主题、左侧导航、分区折叠，配置**保存即热重载**（API Key 打码显示）
- **命令系统**：`/affinity` `/relationship` `/status` `/sleep` `/wake` `/push` `/toggle` `/log` `/ping` `/help`
- **技能插件体系**：`src/skills/` 下新增一个文件 + 一行注册即可扩展
- **测试友好**：`tests/mock_napcat.py` 模拟 NapCat，不接真实 QQ 就能测触发逻辑

### 🚀 快速开始

1. 安装 **Python 3.10+**（勾选 *Add Python to PATH*）
2. 安装并登录 **NapCatQQ**（机器人专用 QQ 小号；OneBot 11 网络配置：HTTP 服务端口 `3000`，事件上报填 `http://127.0.0.1:8010/event`）
3. 复制 `src/config.example.json` 为 `src/config.json`，填入你的 **DeepSeek API Key** 与**管理员 QQ 号**（后台也能改）
4. Windows 双击 **`start.bat`**（自动装依赖 → 启动 → 打开管理后台）

> 🧑‍💻 **不写代码也能用**：图文教程见 [使用说明.md](使用说明.md)；更新历史见 [CHANGELOG.md](CHANGELOG.md)。

### 📁 目录结构（节选）

```
├── start.bat              # Windows 一键启动（自动装依赖 + 启动 + 打开后台）
├── requirements.txt       # Python 依赖
├── 使用说明.md            # 非开发人员使用教程（图文）
├── CHANGELOG.md           # 更新日志
├── src/                   # ★ 运行时代码 + 资源
│   ├── bot.py             #   主程序：消息处理 / 路由 / 管理后台 / 统一人设出口
│   ├── config.py          #   配置管理（读写 config.json，热重载，key 打码）
│   ├── config.example.json#   配置模板（复制为 config.json 后填写）
│   ├── admin.html         #   可视化管理后台页面
│   ├── chat_guard.py      #   称呼护栏文案（一处维护，全路径生效）
│   ├── weather_push.py    #   天气播报（QWeather 长图）
│   ├── search_connectors.py # 联网搜索（垂直信源 + Tavily/DDG）
│   ├── proactive.py       #   主动推送调度（pixiv / B站）
│   ├── monitor.py         #   B站官方号动态监控
│   ├── skills/            #   技能插件（命令 / 识图 / 搜出处 / 漫画汉化 / pixiv 推送 / 记忆）
│   ├── personas/          #   人设卡（如月栞/persona.json，改后即时生效）
│   └── stickers/          #   表情包图片（文件名 = 触发标签）
├── tests/                 # 模拟 NapCat 的端到端测试工具
└── docs/                  # 功能设计文档
```

### ⚙️ 主要配置（`src/config.json`）

| 配置项 | 说明 |
|--------|------|
| `deepseek.api_key` | **必填**。DeepSeek API Key |
| `bot.admin_qqs` | 管理员 QQ 号列表（机器人只对 TA 叫「前辈」、不限次数、可执行管理命令） |
| `search_api.tavily_key` | 选填。通用联网搜索 Key（不填则用 DuckDuckGo） |
| `weather.api_key` / `weather.api_host` | 选填。和风天气 API Key + **账号专属 API Host**（2026 起公共域名停服，控制台-设置查看，形如 `h2a9cf3mhs.xy.qweatherapi.com`） |
| `pixiv.phpsessid` | 选填。pixiv Cookie（不填也能推普通图） |
| `bilibili.sessdata` | 选填。B站 Cookie（动态监控与部分接口需要） |
| `sauce.api_key` | 选填。SauceNAO Key（不填则搜出处仅能查动画截图） |
| `monitor.sources` / `proactive.groups` | B站监控源 / 主动推送群白名单（后台卡片可配） |
| `nsfw.enabled` | 私密场景开关（**默认关闭**） |

完整默认值见 `src/config.py` 的 `DEFAULTS`，绝大多数项可在后台可视化修改。

### 🛠 技术栈

- **Python 3.10+ / FastAPI / httpx / Pillow / SQLite**
- **NapCatQQ**（OneBot 11 协议桥接）
- **DeepSeek API**（对话 / 视觉 / 智能判域 / 汉化翻译）
- **和风天气 QWeather**（天气长图，专属 API Host + X-QW-Api-Key）
- 本地 OCR / 文本检测（rapidocr + 可选 manga-ocr / DBNet / 48px OCR，权重可选下载）、LaMa 图像修复（均可选装）

> 💡 **可选增强（汉化检测精度）**：仓库不包含大权重（GitHub 单文件 100MB 上限）。
> 从 zyddnys/manga-image-translator 的发行资源获取 detect.ckpt（DBNet 检测，~294MB）与
> ocr_ar_48px.ckpt（48px OCR，~195MB），分别放入 src/vendor/manga_detect/models/detection/
> 与 src/vendor/manga_detect/models/ocr/，即可启用 db 检测与 48px 精修；缺省自动回退
> RapidOCR + manga-ocr。

### 🧪 开发 / 测试

不接真实 NapCat，零成本测触发逻辑——三个终端：

```bash
# 终端 1：模拟 NapCat 的 3000 端口
python tests/mock_napcat.py

# 终端 2：机器人（可用假 key）
python src/bot.py

# 终端 3：发模拟群消息
python tests/test_event.py
```

新增技能：在 `src/skills/` 新建 `xxx.py`，实现 `async def handle(event, text, is_at_me, ctx)`，
底部 `register(handle, "xxx", priority=10)`，并把文件名加进 `skills/__init__.py` 的 `_SKILL_MODULES`。

<!-- 📸 预览截图：把效果图放进 assets/screenshots/ 后取消注释即可展示
<p align="center">
  <img src="assets/screenshots/chat.png" width="45%">
  <img src="assets/screenshots/weather.png" width="45%">
</p>
<p align="center"><img src="assets/screenshots/manga.png" width="45%"></p>
-->

### ⚠️ 免责声明

- 本项目仅供学习交流，请遵守 DeepSeek / pixiv / Bilibili / SauceNAO / QWeather 等服务商的使用条款
- 机器人发言由 AI 生成，不代表项目作者观点
- 使用机器人 QQ 小号存在封号风险，请自行评估
- 角色卡含成人向设定（**默认关闭**），请勿用于非法用途；公开发布前请自行确认合规

---

<a id="en"></a>
## English

**Shiorin（如月栞）· QQ Group Chat Bot** — an out-of-the-box AI chatbot for QQ groups, built with **NapCatQQ (OneBot 11) + FastAPI + DeepSeek**. It role-plays a built-in character, chats when @-mentioned or called by name, and runs without writing any code (double-click `start.bat`).

### Highlights

- **Roleplay personality** — full built-in character with world view & intimacy mechanics (Tavern card format, swappable); affinity limits per user tier; relationship cards that grow from interactions; long-term memory (SQLite); proactive chatter & image reactions
- **Web search** — auto goes online for real-time/factual questions; smart routing to vertical sources (Bangumi anime scores, **Bangumi game DB for galgame/visual novels**, Steam prices, Moegirlpedia ACG lore, bilibili, **GitHub repo search**) with Tavily / DuckDuckGo fallback; result lines tagged by source (community post vs. encyclopedia page) so the model never mistakes a forum poster's first-person preference for the group member's; broad "recommend me" queries are de-duplicated & randomized
- **Image tools** — reverse image search for sources (SauceNAO + Trace.moe, two-phase cross-message flow); **manga translation/汉化** (pluggable detection/OCR, OCR-noise cleaning, batch translate via DeepSeek or an OpenAI-compatible endpoint, optional whole-page polish → LaMa erase → draw Chinese); automatic image captioning into context
- **Weather broadcast** — QWeather-powered daily weather card images (today + 24h + 7-day) to configured groups, adapted to the 2026 API-host migration (account-specific API Host + X-QW-Api-Key)
- **Proactive feeds** — pixiv keyword push; bilibili videos auto-picked from the latest week with per-group negative filters & dedupe; official-account feed monitoring with persona-style announcements
- **Link protection** — outbound links get a random Chinese char inserted *inside the domain* so QQ can't treat them as clickable URLs (anti-link-risk-control); idempotent; readers just delete the extra char
- **Web admin panel** at `http://127.0.0.1:8010/admin` — dark/light themes, save = hot reload
- **Test-friendly** — `tests/mock_napcat.py` simulates NapCat so you can test triggers without a real QQ account

### Quick start

1. Install **Python 3.10+** (check *Add to PATH*)
2. Install & login **NapCatQQ** with a dedicated QQ account (OneBot 11: HTTP service on port `3000`, event report URL `http://127.0.0.1:8010/event`)
3. Copy `src/config.example.json` → `src/config.json`, fill in your **DeepSeek API Key** and **admin QQ**
4. Double-click **`start.bat`** on Windows (installs deps → starts → opens the admin panel)

> Full changelog: [CHANGELOG.md](CHANGELOG.md)（mainly Chinese）. The detailed illustrated setup guide (Chinese) lives in [使用说明.md](使用说明.md).

**Stack**: Python 3.10+ · FastAPI · httpx · Pillow · SQLite · NapCatQQ (OneBot 11) · DeepSeek API · QWeather · rapidocr / manga-ocr / LaMa (optional) · DBNet / 48px OCR (optional weights).

> ⚠️ For study/communication only. Respect the ToS of DeepSeek / pixiv / Bilibili / SauceNAO / QWeather. Bot messages are AI-generated and do not represent the author. Using a bot QQ account carries a ban risk. Some character-card content is adult-oriented but **disabled by default**.

---

<a id="hant"></a>
## 繁體中文

**如月栞 · QQ 群聊機器人** —— 基於 **NapCatQQ（OneBot 11）+ FastAPI + DeepSeek** 的 QQ 群聊 AI 機器人，內建完整人設「如月栞」，@ 它或喊名字就會回覆；開箱即聊，雙擊 `start.bat` 就能跑。

### 功能特色

- **角色扮演**：內建人設（含世界觀 / 親密場景機制，Tavern 卡片可換）；稱呼護欄（只有管理員會被叫「前輩」）；好感度分級限流；關係卡隨互動成長；長期記憶（SQLite）；主動插嘴與圖片反應
- **聯網搜尋**：即時 / 事實類問題自動上網，智慧判域優先垂直來源（番劇 Bangumi、galgame / 視覺小說走 **Bangumi 遊戲庫**、Steam 價格、萌娘百科、B站、**GitHub 開源檢索**），Tavily / DuckDuckGo 兜底；結果帶**來源前綴**（【知乎網友帖】vs【萌娘百科】），不會把網友的第一人稱偏好當成群友觀點；泛推薦自動去重隨機
- **圖片能力**：**找圖出處**（SauceNAO + Trace.moe，支援跨訊息兩段式）；**漫畫漢化**（可插拔檢測 / OCR、亂碼清洗、DeepSeek 或 OpenAI 相容端點翻譯、可選整頁順稿 → LaMa 擦字 → 繪製中文回傳）；圖片自動「圖註」進上下文
- **天氣播報**：和風天氣每日天氣長圖（今日實況 + 24 小時 + 7 天，左上角城市名 + 地區行），已適配 2026 專屬 API Host + X-QW-Api-Key 遷移
- **主動推播 / 監控**：pixiv 關鍵字推播、B站一週內最新影片（每群負面詞過濾 + 去重、重啟不丟）、官方號動態監控（48h 新鮮窗口）
- **外鏈防風控**：在連結**網域內部隨機插入一個漢字**（如 `https://www.pi中xiv.net/…`），QQ 拼不出合法網址；冪等，群友刪掉那個字即可開啟
- **可視化管理後台**：`http://127.0.0.1:8010/admin`——深 / 淺雙主題，儲存即熱重載
- **測試友善**：`tests/mock_napcat.py` 模擬 NapCat，不接真實 QQ 即可測觸發邏輯

### 快速開始

1. 安裝 **Python 3.10+**（勾選 *Add Python to PATH*）
2. 安裝並登入 **NapCatQQ**（機器人專用小號；OneBot 11：HTTP 連接埠 `3000`，事件上報 `http://127.0.0.1:8010/event`）
3. 複製 `src/config.example.json` 為 `src/config.json`，填入 **DeepSeek API Key** 與**管理員 QQ**
4. Windows 雙擊 **`start.bat`**（自動裝依賴 → 啟動 → 開啟後台）

> 完整更新紀錄見 [CHANGELOG.md](CHANGELOG.md)；圖文教學（簡體中文）見 [使用說明.md](使用說明.md)。

> ⚠️ 僅供學習交流，請遵守各服務商使用條款；機器人發言由 AI 生成，不代表作者立場；使用小號有封號風險；角色卡含成人向設定（**預設關閉**），請勿用於非法用途。

---

<a id="ja"></a>
## 日本語

**如月栞（しおり）· QQ 群聊 Bot** — **NapCatQQ（OneBot 11）+ FastAPI + DeepSeek** 製の、QQ グループ向け AI チャットボットです。内蔵キャラ「如月栞」が @ メンションや呼びかけに返事します。コード不要で、`start.bat` をダブルクリックするだけで起動できます。

### 主な機能

- **キャラクターロールプレイ**：内蔵キャラ（世界観・親密シーン機構付き、Tavern カード形式で差し替え可）。管理者だけが「先輩」と呼ばれる呼称ガード、好感度による日次制限、関係カード、長期記憶（SQLite）、能動的な相槌・画像リアクション
- **Web 検索**：リアルタイム / 事実系の質問に自動でオンライン検索。垂直ソースを優先（アニメ評価 = Bangumi、**galgame / ビジュアルノベル = Bangumi ゲーム DB**、Steam 価格、萌娘百科、bilibili、GitHub リポジトリ検索）、Tavily / DuckDuckGo でフォールバック。結果には**出典プレフィックス**（【知乎网友帖】= 掲示板ユーザーの発言、【萌娘百科】= 百科事典）付きで、他人の一人称の好みを質問者本人の意見と誤認しません。「おすすめ募集」系は重複排除 + ランダム化
- **画像機能**：**出典検索**（SauceNAO + Trace.moe、2 段階メッセージ対応）、**漫画翻訳・漢化**（検出 / OCR をプラグイン化、OCR ノイズ除去、DeepSeek または OpenAI 互換エンドポイントで翻訳、ページ全体推敲オプション → LaMa で消去 → 中国語を描画）、画像の自動キャプション
- **天気予報**：和風天氣（QWeather）の毎日天気カード画像（今日 + 24 時間 + 7 日間）。2026 年の API Host 移行（アカウント専用 Host + X-QW-Api-Key）に対応済み
- **プッシュ通知 / 監視**：pixiv キーワード配信、bilibili の直近 1 週間の動画配信（グループごとの NG ワード + 重複排除）、公式アカウントの新着監視
- **リンク保護**：送信リンクの**ドメイン内に漢字を 1 文字ランダム挿入**（例 `https://www.pi中xiv.net/…`）し、QQ が URL として認識できないようにします。冪等で、読者はその 1 文字を消すだけで開けます
- **管理パネル**：`http://127.0.0.1:8010/admin`（ダーク / ライトテーマ、保存で即ホットリロード）
- **テスト容易**：`tests/mock_napcat.py` が NapCat を模擬し、本物の QQ なしでトリガーをテスト可能

### クイックスタート

1. **Python 3.10+** をインストール（*Add to PATH* にチェック）
2. **NapCatQQ** を専用サブアカウントでインストール＆ログイン（OneBot 11：HTTP ポート `3000`、イベント送信先 `http://127.0.0.1:8010/event`）
3. `src/config.example.json` を `src/config.json` にコピーし、**DeepSeek API Key** と**管理者 QQ** を入力
4. **`start.bat`** をダブルクリック（依存関係の導入 → 起動 → 管理パネルを開く）

> 更新履歴は [CHANGELOG.md](CHANGELOG.md)（中国語）を参照。

> ⚠️ 学習・交流目的のみ。各サービスの利用規約を守ってください。AI 生成の発言は作者の見解ではありません。Bot 用アカウントの利用は凍結リスクがあります。一部キャラクターカードは成人向け設定を含みますが、**デフォルトでは無効**です。
