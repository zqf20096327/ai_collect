<div align="center">

# ⚡ AniSubx

### صدای ویدیو را به زیرنویس فارسی تبدیل کن — با تشخیص گفتار و ترجمهٔ هوش مصنوعی، روی دستگاه خودت

`تبدیل گفتار به متن` · `ترجمه با LLM` · `زیرنویس SRT` · `حک زیرنویس روی ویدیو` · `وباپ سبک و خودمیزبان`

[![License: AGPL-3.0-only](https://img.shields.io/badge/License-AGPL--3.0--only-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-2ea44f.svg)](app/__init__.py)
[![Python](https://img.shields.io/badge/Python-3.8%2B-3776ab.svg)](requirements.txt)
[![Framework](https://img.shields.io/badge/FastAPI-0.99%2B-05998b.svg)](requirements.txt)

[🇮🇷 فارسی](#fa) · [🇬🇧 English](#en) · [📸 تصاویر برنامه](#screenshots) · [🗺️ فهرست مطالب](#table-of-contents) · [📥 نصب](#fa-install)

</div>

---

<a id="screenshots"></a>

## 📸 تصاویر برنامه

تصاویری از رابط کاربری وب در یک گوشی:

<div align="center">

<img src="image01.jpg" width="240" alt="AniSubx — رابط کاربری وب، نمونه ۱">
<img src="image02.jpg" width="250" alt="AniSubx — رابط کاربری وب، نمونه ۲">

</div>

---

<a id="table-of-contents"></a>

## 🗺️ فهرست مطالب

| 🇮🇷 فارسی | 🇬🇧 English |
| :--- | :--- |
| [آشنایی با AniSubx](#fa-about) | [Overview](#en-overview) |
| [امکانات اصلی](#fa-features) | [Core Features](#en-features) |
| [فرمت‌ها و خروجی‌ها](#fa-formats) | [Formats & Outputs](#en-formats) |
| [معماری](#fa-architecture) | [Architecture](#en-architecture) |
| [رابط کاربری وب](#fa-ui) | [Web UI](#en-ui) |
| [نصب و راه‌اندازی](#fa-install) | [Installation](#en-install) |
| [استفاده](#fa-usage) | [Usage](#en-usage) |
| [پیکربندی](#fa-config) | [Configuration](#en-config) |
| [حریم خصوصی و امنیت](#fa-privacy) | [Privacy & Security](#en-privacy) |
| [نکات مهم](#fa-notes) | [Important Notes](#en-notes) |
| [ساخت از سورس](#fa-build) | [Build from Source](#en-build) |
| [مشارکت](#fa-contributing) | [Contributing](#en-contributing) |
| [مجوز](#fa-license) | [License](#en-license) |

---

<a id="fa"></a>

# 🇮🇷 فارسی

<a id="fa-about"></a>

## آشنایی با AniSubx

**AniSubx** یک اپلیکیشن وب سبک و **خودمیزبان** (self-hosted) است که گفتار داخل یک ویدیو (یا فایل صوتی) را به **زیرنویس فارسی** تبدیل می‌کند:

1. صدای ویدیو را استخراج می‌کند.
2. آن را برای تبدیل گفتار به متن (speech-to-text) به سرویسی که خودتان معرفی می‌کنید می‌فرستد.
3. متن پیاده‌شده را با یک مدل زبانی (LLM) به فارسی ترجمه می‌کند.
4. فایل زیرنویس `.srt` می‌سازد و در صورت درخواست، زیرنویس را با FFmpeg روی ویدیو «حک» (داخلی/burn) می‌کند و یک MP4 آماده‌ی پخش تحویل می‌دهد.

همه‌چیز روی دستگاه خود شما اجرا می‌شود و از **کلیدهای API خود شما** استفاده می‌کند — هیچ فایلی به سرویس میزبانی‌شده توسط AniSubx آپلود نمی‌شود.

این پروژه در درجهٔ اول برای **Termux/اندروید** طراحی شده وابستگی‌های سبکی دارد (بدون دیتابیس، بدون Redis، بدون Celery) تا روی یک گوشی هم روان کار کند؛ اما هر جا که Python و FFmpeg در دسترس باشد قابل اجراست.

<a id="fa-features"></a>

## امکانات اصلی

| | قابلیت | توضیح |
| :---: | :--- | :--- |
| 🎬 | **پردازش ویدیو و صدا** | پشتیبانی از فرمت‌های رایج ویدیو و ورودی‌های صوتی؛ نمایش اطلاعات واقعی رسانه (قالب، کدک، رزولوشن، نرخ فریم و…) با ffprobe هنگام انتخاب فایل |
| 🗣️ | **تبدیل گفتار به متن** | ارسال صدا به هر سرویس سازگار با پروتکل OpenAI؛ تقسیم خودکار صدای بلند به قطعه‌های کوچک و جبران اختلاف زمانی هر قطعه |
| 🌐 | **ترجمه زیرنویس** | ترجمهٔ دسته‌ای با هر API سازگار با `chat/completions`؛ حفظ ترتیب، تعداد و زمان‌بندی زیرنویس‌ها |
| 📝 | **تولید زیرنویس** | ساخت فایل SRT استاندارد (UTF-8) با راست‌چین کامل برای متن فارسی |
| 🎨 | **استایل و حک زیرنویس** | یافتن خودکار فونت پشتیبان فارسی، ساخت فایل ASS و حک زیرنویس روی ویدیو با FFmpeg و libass |
| 🖥️ | **رابط وب دوزبانه** | سه برگهٔ «جدید / تاریخچه / تنظیمات»، با پشتیبانی کامل از فارسی (راست‌چین) و انگلیسی |
| 📱 | **قابل نصب به‌صورت PWA** | با مرورگر گوشی نصب می‌شود و مانند یک برنامهٔ مستقل کار می‌کند |
| 🔁 | **ادامهٔ کار ناتمام** | یک کار ناموفق/لغوشده از همان‌جا ادامه می‌یابد؛ ترجمهٔ دسته‌های انجام‌شده تکرار نمی‌شود |
| 🧪 | **بررسی واقعی سیستم** | بخش Re-check تست‌های واقعی (نه ظاهری) روی Python، بسته‌ها، FFmpeg، ffprobe، libass، فونت و APIهای گفتار/ترجمه انجام می‌دهد |

<a id="fa-formats"></a>

## فرمت‌ها و خروجی‌ها

**ورودی‌های پشتیبانی‌شده:**

| نوع | فرمت‌ها |
| :--- | :--- |
| ویدیو | `.mp4` `.mkv` `.mov` `.webm` `.avi` `.m4v` `.mpg` `.mpeg` `.ts` `.m2ts` `.flv` `.wmv` `.3gp` `.ogv` |
| صدا (فقط زیرنویس) | `.mp3` `.wav` `.m4a` `.aac` `.flac` `.ogg` `.opus` `.wma` |

**خروجی:**

- **فایل زیرنویس** `<نام-فایل>.fa.srt` — همیشه تولید می‌شود.
- **ویدیوی حک‌شده** `<نام-فایل>.fa.mp4` — فقط وقتی گزینهٔ «حک زیرنویس روی ویدیو» فعال باشد.
- اگر فایل ورودی **فقط صوتی** باشد یا ویدیو فاقد ویدیو (فقط صدا) باشد، فقط فایل `.srt` ساخته می‌شود.

<a id="fa-architecture"></a>

## معماری

```
run.py ──> app.main (FastAPI) ──────────────── پوستهٔ وب ایستا (HTML/CSS/JS/PWA)
             │  │  │
             │  ├── /api/jobs ──> صف کارها (۱ کارگر پس‌زمینه) ──> خط لولهٔ پردازش
             │  │                    │  ├── استخراج صدا          (ffmpeg)
             │  │                    │  ├── تبدیل گفتار به متن   (API گفتار)
             │  │                    │  ├── ترجمه                (API ترجمه)
             │  │                    │  └── حک زیرنویس           (ffmpeg + libass)
             │  └── /api/config, /api/health, /api/diagnostics
             └── data/settings.json (پیکربندی زمان اجرا؛ کلیدهای API از سرور خارج نمی‌شوند)
```

نکات کلیدی طراحی:

- **آپلود تکه‌به‌تکه** روی دیسک صورت می‌گیرد، پس یک گوشی با حافظهٔ کم هم می‌تواند فایل‌های بزرگ بپذیرد.
- کارهای طولانی در **یک کارگر پس‌زمینه** انجام می‌شوند؛ هیچ درخواست HTTP منتظر رمزگذاری نمی‌ماند و مرورگر وضعیت را از `GET /api/jobs/{id}` دنبال می‌کند.
- وضعیت هر کار در `data/jobs/<id>/job.json` ذخیره می‌شود تا با راه‌اندازی مجدد سرور، کارها از بین نروند.
- **بدون دیتابیس، بدون Redis، بدون Celery** — فقط یک صف درون‌فرایندی ساده.
- سرویس‌دهنده‌های سبک مبتنی بر **کتابخانهٔ استاندارد Python** هستند؛ حتی تشخیص فونت فارسی هم فقط با پارسِ دستی فایل‌های فونت انجام می‌شود.

### پیش‌نیازهای زمان اجرا

- **Python 3.8+** (تشخیص سلامت، نسخهٔ 3.9+ را توصیه می‌کند).
- **FFmpeg و ffprobe** در `PATH` (یا مشخص کردن `FFMPEG_PATH` / `FFPROBE_PATH`).
  - برای حک زیرنویس، نسخهٔ FFmpeg باید **libass** داشته باشد.
  - در Termux: `pkg install ffmpeg`
- یک **فونت پشتیبان فارسی** برای حک زیرنویس (به‌صورت خودکار پیدا می‌شود؛ قابل تعیین با `SUBTITLE_FONT`).
  - در Termux: `pkg install noto-fonts`
- دسترسی شبکه به سرویس‌های گفتار و ترجمهٔ انتخابی شما.

### پروتکل‌های سازگار

- **گفتار به متن:** هر سروری که پروتکل `POST /v1/audio/transcriptions` (سبک OpenAI) را پیاده کند — از جمله OpenAI، Groq، دروازه‌های سازگار با OpenRouter، پروکسی‌های LiteLLM، سرور faster-whisper و سرور HTTP وویسپر.cpp. چندین قالب پاسخ (verbose_json، سبک whisper.cpp، Deepgram، کلمه‌ای و…) پشتیبانی می‌شود.
- **ترجمه:** هر سروری که پروتکل `POST /v1/chat/completions` را پیاده کند — از جمله OpenAI، OpenRouter، Groq، Together، Mistral، پروکسی‌های LiteLLM و شیم OpenAI شرکت Ollama.

<a id="fa-ui"></a>

## رابط کاربری وب

رابط کاربری یک صفحهٔ واحد با سه برگه است:

1. **جدید** — فایل ویدیو/صوتی را انتخاب کنید. هنگام انتخاب، سرآیند فایل بررسی می‌شود و اطلاعات واقعی رسانه (قالب، رزولوشن، کدک، نرخ فریم، کانال‌های صدا و…) نمایش داده می‌شود. می‌توانید تصمیم بگیرید زیرنویس روی ویدیو حک شود یا فقط فایل `.srt` بگیرید. یک «خط زمانی» پیشرفت، وضعیت هر مرحله (آپلود ← صدا ← گفتار-به-متن ← ترجمه ← SRT ← حک ← آماده‌سازی) را با زمان‌بندی نشان می‌دهد.
2. **تاریخچه** — همهٔ کارها با وضعیت، زبان، حجم، مدت، زمان صرف‌شده و دکمه‌های دانلود. دکمهٔ **Re-check** بررسی سیستم را روی یک کار موجود اجرا می‌کند.
3. **تنظیمات** — تنظیم گفتار/ترجمه/زیرنویس/رمزگذاری/نگهداری. ذخیره در `data/settings.json` نوشته می‌شود. دکمهٔ **Re-check** در اینجا بررسی «زنده» (با درخواست واقعی به APIها) اجرا می‌کند.

کنترل‌های هر کار: **لغو** (در نزدیک‌ترین نقطهٔ امن)، **ادامه** (Resume — از حالت ذخیره‌شدهٔ ترجمه از سر گرفته می‌شود)، **حذف** (آزادسازی فوری فضا).

زبان رابط به‌صورت خودکار بین **فارسی (راست‌چین)** و **انگلیسی** شناسایی می‌شود و با یک دکمه قابل تعویض است. برنامه به‌صورت **PWA** قابل نصب است (`/manifest.webmanifest` و `/service-worker.js`). سرویس‌کاربر هرگز پاسخ‌های `/api/*` را کش نمی‌کند.

<a id="fa-install"></a>

## نصب و راه‌اندازی

### پیش‌نیازها

- Python 3.8+ و `pip`
- FFmpeg + ffprobe (برای حک زیرنویس: نسخهٔ دارای libass)
- فونت فارسی (برای حک زیرنویس)

### نصب

```bash
python -m venv --system-site-packages .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> `--system-site-packages` به این معناست که بسته‌هایی که از قبل در سیستم نصب هستند (مثل بسته‌های Termux) دوباره دانلود نمی‌شوند. اگر این گزینه را نمی‌خواهید، بدون آن اجرا کنید؛ فقط ممکن است وابستگی‌ها دوباره نصب شوند.

ابزارهای رسانه‌ای (در Termux):

```bash
pkg install ffmpeg noto-fonts
```

### پیکربندی اولیه

```bash
cp .env.example .env
```

فایل `.env` را ویرایش کنید و دست‌کم **آدرس API، کلید API و نام مدل** را برای سرویس گفتار و سرویس ترجمه پر کنید (جزئیات در جدول پیکربندی).

### شروع سرور

```bash
python run.py                  # 127.0.0.1:8000
python run.py --host 0.0.0.0   # قابل دسترس از دستگاه‌های دیگر شبکه
python run.py --port 8080
python run.py --reload         # راه‌اندازی مجدد خودکار (توسعه)
```

سپس مرورگر را باز کنید: **http://127.0.0.1:8000**

> **هشدار امنیتی:** اتصال به `0.0.0.0` سرور را در معرض **همهٔ دستگاه‌های شبکه** قرار می‌دهد و برنامه **رمز عبور ندارد** — فقط در شبکه‌ای که به آن اعتماد دارید این کار را انجام دهید.

<a id="fa-usage"></a>

## استفاده

به زبان ساده، کار با AniSubx به این شکل است:

1. سرور را اجرا کنید (`python run.py`) و یک مرورگر را باز کنید.
2. در برگهٔ **جدید**، ویدیو (یا فایل صوتی) را انتخاب کنید؛ مشخصات فایل نمایش داده می‌شود.
3. تصمیم بگیرید زیرنویس روی ویدیو حک شود یا فقط فایل `.srt` بگیرید (برداشتن تیک، گزینهٔ سریع‌تر است).
4. با زدن **شروع ترجمه**، فایل بارگذاری و وارد صف پردازش می‌شود.
5. خط زمانی پیشرفت، مراحل استخراج صدا ← تبدیل گفتار به متن ← ترجمه ← ساخت SRT ← حک ← آماده‌سازی را نشان می‌دهد. در صورت نیاز می‌توانید کار را **لغو** کنید.
6. پس از پایان، از دکمه‌های دانلود، ویدیوی حک‌شده (`...fa.mp4`) یا فایل زیرنویس (`...fa.srt`) را دانلود کنید.
7. در بخش **پیش‌نمایش زیرنویس** می‌توانید متن ترجمه‌شده را مرور کنید.
8. در صورت خطا، کار در **تاریخچه** باقی می‌ماند و با دکمهٔ **ادامه** بدون تکرار بخش‌های انجام‌شده (و بدون هزینهٔ دوبارهٔ ترجمه‌های پرداخت‌شده) از سر گرفته می‌شود.

<a id="fa-config"></a>

## پیکربندی

پیکربندی از سه لایه ساخته می‌شود (لایهٔ بعدی بر لایهٔ قبلی غلبه دارد):

1. پیش‌فرض‌های داخلی (در `app/config.py`).
2. متغیرهای محیطی — به‌صورت اختیاری از فایل `.env`.
3. تنظیمات ذخیره‌شده از طریق رابط وب (برگهٔ **تنظیمات**) در `data/settings.json` — **اولویت با این لایه است**.

کلیدهای API **فقط روی سرور** نگه داشته می‌شوند و هرگز به مرورگر فرستاده نمی‌شوند؛ مرورگر فقط یک پرچم «تنظیم شده است» و یک پیش‌نمایش ماسک‌شده می‌بیند.

### لیست متغیرهای محیطی

#### گفتار به متن (STT)

| متغیر | پیش‌فرض | توضیح |
| :--- | :--- | :--- |
| `STT_API_URL` | `https://api.openai.com/v1/audio/transcriptions` | آدرس سرویس گفتار (پروتکل OpenAI) |
| `STT_API_KEY` | (خالی) | کلید API گفتار |
| `STT_MODEL` | `whisper-1` | نام مدل |
| `STT_LANGUAGE` | `en` | زبان مبدأ؛ `auto` یعنی تشخیص خودکار |
| `STT_RESPONSE_FORMAT` | `verbose_json` | `verbose_json` = زمان‌بندی هر بخش |
| `STT_PROMPT` | (خالی) | راهنمای اختیاری برای مدل |
| `STT_CHUNK_SECONDS` | `600` | طول هر قطعهٔ صوتی (درخواست‌های کوتاه‌تر) |
| `STT_AUDIO_FORMAT` | `mp3` | قالب صدای استخراج‌شده (`mp3`/`m4a`/`wav`/`ogg`/`flac`) |
| `STT_AUDIO_BITRATE` | `64k` | نرخ بیت صدای استخراج‌شده |
| `STT_SAMPLE_RATE` | `16000` | نرخ نمونه‌برداری (هرتز) |
| `STT_TIMEOUT` | `600` | مهلت انتظار هر درخواست (ثانیه) |

#### ترجمه

| متغیر | پیش‌فرض | توضیح |
| :--- | :--- | :--- |
| `TRANSLATION_API_URL` | `https://api.openai.com/v1/chat/completions` | آدرس سرویس ترجمه (پروتکل OpenAI) |
| `TRANSLATION_API_KEY` | (خالی) | کلید API ترجمه |
| `TRANSLATION_MODEL` | `gpt-4o-mini` | نام مدل ترجمه |
| `TRANSLATION_TEMPERATURE` | `0.2` | دمای نمونه‌برداری |
| `TRANSLATION_MAX_TOKENS` | `0` | حداکثر توکن خروجی؛ `0` = انتخاب با سرویس‌دهنده |
| `TRANSLATION_BATCH_SIZE` | `20` | تعداد خط زیرنویس در هر درخواست |
| `TRANSLATION_TIMEOUT` | `240` | مهلت انتظار هر درخواست (ثانیه) |
| `TRANSLATION_RETRIES` | `3` | تعداد تلاش مجدد برای هر دسته |
| `TARGET_LANGUAGE` | `Persian` | زبان مقصد زیرنویس‌ها |

#### زیرنویس

| متغیر | پیش‌فرض | توضیح |
| :--- | :--- | :--- |
| `SUBTITLE_FONT` | (خالی) | مسیر فونت‌فایل؛ خالی = تشخیص خودکار |
| `SUBTITLE_FONT_NAME` | (خالی) | نام خانوادگی فونت؛ خالی = استخراج از فایل |
| `SUBTITLE_FONT_SIZE` | `0` | اندازهٔ فونت؛ `0` = مقیاس‌پذیر از ارتفاع ویدیو |
| `SUBTITLE_OUTLINE` | `2` | ضخامت دورخط |
| `SUBTITLE_SHADOW` | `0` | عمق سایه |
| `SUBTITLE_MARGIN_V` | `28` | حاشیهٔ عمودی |
| `SUBTITLE_PRIMARY_COLOUR` | `&H00FFFFFF` | رنگ متن (سفارش رنگی ASS `&HBBGGRR`) |
| `SUBTITLE_OUTLINE_COLOUR` | `&H00000000` | رنگ دورخط |
| `SUBTITLE_BACK_COLOUR` | `&HA0000000` | رنگ پس‌زمینه هنگام `BORDER_STYLE=3` |
| `SUBTITLE_BORDER_STYLE` | `1` | `1` = دورخط+سایه، `3` = کادر توپر |
| `SUBTITLE_MAX_LINE_CHARS` | `42` | حداکثر نویسه در هر خط |
| `SUBTITLE_MAX_LINES` | `2` | حداکثر خط در هر زیرنویس |

#### رمزگذاری ویدیو

| متغیر | پیش‌فرض | توضیح |
| :--- | :--- | :--- |
| `FFMPEG_PATH` / `FFPROBE_PATH` | `ffmpeg` / `ffprobe` | مسیر باینری‌ها |
| `VIDEO_ENCODER` | `libx264` | رمزگذار (لیست مجاز در `/api/config`) |
| `VIDEO_PRESET` | `veryfast` | پیش‌تنظیم رمزگذار |
| `VIDEO_CRF` | `26` | کیفیت (عدد کوچک‌تر = کیفیت بالاتر/حجم بیشتر) |
| `VIDEO_THREADS` | `0` | `0` = تصمیم با FFmpeg |
| `AUDIO_COPY` | `true` | کپی صدای اصلی وقتی سازگار باشد (به‌جای رمزگذاری دوباره) |
| `AUDIO_FALLBACK_BITRATE` | `128k` | نرخ بیت صدا وقتی رمزگذاری دوباره لازم است |
| `BURN_TIMEOUT` | `0` | `0` = بدون محدودیت زمان برای مرحلهٔ حک |

#### سرور و نگهداری

| متغیر | پیش‌فرض | توضیح |
| :--- | :--- | :--- |
| `HOST` | `127.0.0.1` | رابطی که سرور به آن متصل می‌شود |
| `PORT` | `8000` | پورت TCP |
| `MAX_UPLOAD_BYTES` | `0` | سقف حجم آپلود؛ `0` = بدون سقف (محدود به دیسک) |
| `JOB_RETENTION_HOURS` | `24` | حذف خودکار کارهای قدیمی پس از این تعداد ساعت |
| `CLEANUP_INTERVAL_HOURS` | `6` | بازهٔ اجرای پاک‌سازی |
| `MIN_FREE_DISK_MB` | `500` | آستانهٔ هشدار فضای آزاد دیسک |
| `KEEP_INTERMEDIATE` | `false` | نگه‌داشتن فایل‌های میانی (صدا/ASS) برای اشکال‌زدایی |
| `LOG_LEVEL` | `INFO` | سطح لاگ ریشه |

متغیرهای مسیر اختیاری: `DATA_DIR` (ریشهٔ دادهٔ زمان اجرا) و `ENV_FILE` (مسیر فایل `.env`؛ پیش‌فرض `<repo>/.env`).

> **امنیت تنظیمات:** `data/settings.json` کلیدهای واقعی API را نگه می‌دارد و با مجوز `0600` نوشته می‌شود. فایل `.env` هرگز به مرورگر ارسال نمی‌شود و از لاگ‌ها هم حذف (redact) می‌شود.

<a id="fa-privacy"></a>

## حریم خصوصی و امنیت

- پردازش (استخراج صدا، ساخت زیرنویس، رمزگذاری) **روی دستگاه خود شما** انجام می‌شود.
- فایل‌های آپلودشده، صدای استخراج‌شده و خروجی‌ها در `data/jobs/<id>/` روی دستگاه شما نگهداری می‌شوند.
- برای تبدیل گفتار به متن و ترجمه، **صدا و متن** به سرویس‌هایی که **شما** در تنظیمات معرفی می‌کنید ارسال می‌شود.
- کلیدهای API شما فقط روی سرور (در `data/settings.json` با مجوز `0600`) ذخیره می‌شوند؛ مرورگر فقط «تنظیم شده/نشده» و یک پیش‌نمایش ماسک‌شده می‌بیند.
- برنامه **حساب کاربری، رمز عبور یا احراز هویت ندارد**. سرور را به `127.0.0.1` محدود کنید مگر اینکه در شبکهٔ مطمئن باشید.
- هیچ سرویس میزبانِ «شخص سوم» لازم نیست؛ فقط APIهایی که خودتان پیکربندی می‌کنید.

<a id="fa-notes"></a>

## نکات مهم

- **هزینهٔ API:** ترجمهٔ گفتار و متن، هزینهٔ جداگانه دارد (بسته به سرویس انتخابی شما). دسته‌های ترجمه فقط پس از موفقیت «پرداختشده» ثبت می‌شوند؛ با Resume هزینهٔ دوباره ندارند.
- **زمان پردازش:** حک زیرنویس با رمزگذار نرم‌افزاری روی گوشی کند است؛ اگر سرعت لازم دارید می‌توانید از گزینهٔ «فقط SRT» استفاده کنید.
- **فضای دیسک:** پردازش هر ویدیو به تقریباً **دو برابر حجم فایل** فضای خالی نیاز دارد.
- **فایل‌های موقت:** فایل‌های میانی پس از پایان کار حذف می‌شوند (مگر `KEEP_INTERMEDIATE=true`)؛ کارهای قدیمی با `JOB_RETENTION_HOURS` به‌صورت خودکار پاک می‌شوند.
- **کیفیت تشخیص گفتار:** به مدل و زبان انتخابی بستگی دارد. اگر سرویس گفتار زمان‌بندی (timestamp) برنگرداند، زمان‌بندی زیرنویس **تخمینی** خواهد بود و ممکن است جابه‌جا شود.
- **libass:** برای حک زیرنویس، FFmpeg باید با libass ساخته شده باشد؛ بدون آن فقط فایل `.srt` قابل‌دسترس است.
- **فونت فارسی:** برای نمایش درست حروف فارسی هنگام حک، وجود یک فونت پشتیبان فارسی لازم است (Termux: `pkg install noto-fonts`).
- **خطوط ترجمه‌نشده:** اگر مدل ترجمه نتواند خطی را ترجمه کند، متن اصلی همان خط در خروجی نگه داشته می‌شود تا ترتیب زیرنویس‌ها به هم نخورد.

<a id="fa-build"></a>

## ساخت از سورس و توسعه

پروژه یک بستهٔ Python است و نیازی به «کامپایل» ندارد. برای محیط توسعه:

```bash
python -m venv --system-site-packages .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

اجرای سرور در حالت توسعه:

```bash
python run.py --reload
```

اجرای تست‌ها:

```bash
python -m pytest -q
```

مجموعهٔ تست (پایتست) از HTTP ساختگی و خروجی ffprobe ساختگی استفاده می‌کند — **بدون کلید API واقعی و بدون درخواست شبکه**. ساده‌سازی‌های بسته نیز «سبک و کم‌وابستگی» هستند؛ پیش از افزودن وابستگی جدید، حتماً از کتابخانهٔ استاندارد استفاده کنید (راهنمای کامل در [CONTRIBUTING.md](CONTRIBUTING.md)).

### ساختار پروژه

```
app/                 # برنامهٔ FastAPI و منطق پردازش
  ├── main.py          # همهٔ مسیرهای HTTP
  ├── jobs.py          # صف کارها، ذخیرهٔ وضعیت، خط لولهٔ پردازش
  ├── config.py        # پیکربندی لایه‌ای (پیش‌فرض → .env → settings.json)
  ├── transcription.py # تقسیم صدا و درایور تبدیل گفتار به متن
  ├── translation.py   # درایور ترجمه (دسته‌بندی‌شده، قابل ادامه)
  ├── subtitles.py     # ساخت/پارس/اعتبارسنجی SRT و ASS
  ├── video.py         # ffprobe/ffmpeg: بررسی، استخراج صدا، حک، رمزگذاری
  ├── fonts.py         # یافتن فونت فارسی (فقط کتابخانهٔ استاندارد)
  ├── diagnostics.py   # بررسی‌های واقعی سیستم
  └── providers/       # کلاینت‌های سبک برای گفتار و ترجمه (پروتکل OpenAI)
static/              # رابط کاربری وب (JS خالص، PWA، i18n فارسی/انگلیسی)
app/templates/       # پوستهٔ HTML تک‌صفحه‌ای
tests/               # تست‌های پایتست
run.py               # نقطهٔ ورود سرور
requirements.txt     # وابستگی‌های زمان اجرا (فقط ۳ بسته)
```

<a id="fa-contributing"></a>

## مشارکت

مشارکت‌ها را با روی گشوده می‌پذیریم:

1. مخزن را **Fork** کنید.
2. یک **شاخه** (`branch`) با نام مناسب بسازید.
3. تغییر خود را متمرکز و کم‌وابستگی نگه دارید (تست‌های مربوطه را بنویسید).
4. تغییرات را **Commit** و سپس در قالب **Pull Request** (با توضیح «چرا») ارسال کنید.
5. قبل از ارسال، مطمئن شوید `python -m pytest -q` بدون خطا اجرا می‌شود.

راهنما: [CONTRIBUTING.md](CONTRIBUTING.md) · گزارش امنیت: [SECURITY.md](SECURITY.md)

<a id="fa-license"></a>

## مجوز

AniSubx نرم‌افزار آزاد و متن‌باز است و تحت **مجوز عمومی همگانی آفرو گنو نسخهٔ ۳ فقط (`AGPL-3.0-only`)** منتشر می‌شود.

- متن کامل: [LICENSE](LICENSE)
- اجزای طرف‌سوم (بسته‌های Python، فونت‌ها، FFmpeg) تحت مجوزهای خودشان باقی می‌مانند — [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md)

---

<a id="en"></a>

# 🇬🇧 English

<a id="en-overview"></a>

## Overview

**AniSubx** is a small, self-hosted web app that turns the speech track of a video (or an audio file) into **Persian subtitles**:

1. It extracts the audio track with FFmpeg.
2. It sends it to the speech-to-text service of your choice.
3. It translates the transcript to Persian with an LLM of your choice.
4. It generates an `.srt` file and, optionally, burns the subtitles into a new MP4.

Everything runs on your own machine and talks to **your own API keys** — nothing is uploaded to an AniSubx-hosted service.

The project is built with **Termux/Android in mind** and is deliberately dependency-light (no database, no Redis, no Celery), but it runs anywhere Python and FFmpeg are available.

<a id="en-features"></a>

## Core Features

| | Feature | Description |
| :---: | :--- | :--- |
| 🎬 | **Video & audio processing** | Common video and audio containers; real container/stream metadata (format, codec, resolution, fps…) shown via ffprobe when you pick a file |
| 🗣️ | **Speech-to-text** | Any OpenAI-compatible transcription endpoint; long audio is split into chunks and timestamps are stitched back together |
| 🌐 | **Subtitle translation** | Batched LLM translation via any `chat/completions`-compatible API; count, order and timing of cues are preserved |
| 📝 | **Subtitle generation** | Standard UTF-8 SRT output with full RTL support for Persian text |
| 🎨 | **Subtitle styling & burn-in** | Automatic Persian-font discovery, ASS generation and burning via FFmpeg + libass |
| 🖥️ | **Bilingual web UI** | Three tabs (New / History / Settings), fully localised in Persian (RTL) and English |
| 📱 | **Installable PWA** | Install it from the browser and use it like a standalone app |
| 🔁 | **Resume** | A failed/cancelled job continues from saved progress; finished translation batches are never re-billed |
| 🧪 | **Real system checks** | Re-check runs real tests (not just presence checks) for Python, packages, FFmpeg, ffprobe, libass, fonts and both APIs |

<a id="en-formats"></a>

## Formats & Outputs

**Supported inputs:**

| Type | Formats |
| :--- | :--- |
| Video | `.mp4` `.mkv` `.mov` `.webm` `.avi` `.m4v` `.mpg` `.mpeg` `.ts` `.m2ts` `.flv` `.wmv` `.3gp` `.ogv` |
| Audio (SRT only) | `.mp3` `.wav` `.m4a` `.aac` `.flac` `.ogg` `.opus` `.wma` |

**Outputs:**

- **Subtitle file** `<name>.fa.srt` — always produced.
- **Burned video** `<name>.fa.mp4` — only when “burn subtitles” is enabled.
- If the input is an **audio-only** file, only the `.srt` is produced.

<a id="en-architecture"></a>

## Architecture

```
run.py ──> app.main (FastAPI) ──────────────── static web shell (HTML/CSS/JS/PWA)
             │  │  │
             │  ├── /api/jobs ──> job queue (1 background worker) ──> Pipeline
             │  │                    │  ├── audio extraction    (ffmpeg)
             │  │                    │  ├── transcription       (STT API)
             │  │                    │  ├── translation         (LLM API)
             │  │                    │  └── subtitle burn       (ffmpeg + libass)
             │  └── /api/config, /api/health, /api/diagnostics
             └── data/settings.json (runtime config; API keys never leave the server)
```

Key design points:

- Uploads are **streamed to disk in chunks**, so a low-memory phone can accept large files.
- Long work runs in a **single background worker**; no HTTP request ever blocks on an encode. The browser polls `GET /api/jobs/{id}`.
- Job state is mirrored to `data/jobs/<id>/job.json`, so jobs survive a server restart.
- **No database, Redis or Celery** — a simple in-process queue.
- Providers are built on the **Python standard library**; even Persian-font detection is done by parsing font files directly.

### Runtime requirements

- **Python 3.8+** (the health check recommends 3.9+).
- **FFmpeg + ffprobe** on `PATH` (or `FFMPEG_PATH` / `FFPROBE_PATH`); burning needs an FFmpeg built with **libass** (Termux: `pkg install ffmpeg`).
- A **Persian-capable font** for burning (auto-detected; override with `SUBTITLE_FONT`). Termux: `pkg install noto-fonts`.
- Network access to your chosen speech-to-text and translation endpoints.

### Compatible protocols

- **Speech-to-text:** any server implementing the OpenAI-style `POST /v1/audio/transcriptions` protocol — OpenAI, Groq, OpenRouter-compatible gateways, LiteLLM proxies, faster-whisper-server, whisper.cpp's HTTP server, and similar. Multiple response schemas (verbose_json, whisper.cpp-style, Deepgram, word-level, SRT/VTT/plain text) are handled.
- **Translation:** any server implementing `POST /v1/chat/completions` — OpenAI, OpenRouter, Groq, Together, Mistral, LiteLLM proxies and Ollama's OpenAI shim.

<a id="en-ui"></a>

## Web UI

The UI is a single page with three tabs:

1. **New** — pick a video/audio file. While picking, the file header is probed and real media metadata is shown (format, resolution, codec, fps, audio channels…). Choose whether to burn subtitles or get only the `.srt`. A progress timeline shows each stage (upload → audio → transcribe → translate → SRT → burn → package) with per-stage timing.
2. **History** — every job with status, language, size, duration, elapsed time and download buttons. A **Re-check** button runs Diagnostics on an existing job.
3. **Settings** — configure STT/translation/subtitle/encoding/housekeeping options. Saving writes to `data/settings.json`. **Re-check** here runs live diagnostics (`live=true`).

Per-job controls: **Cancel** (stops at the next safe checkpoint), **Resume** (continues from the saved transcript and per-batch translation progress), **Delete** (frees storage immediately).

The interface auto-detects **Persian (RTL)** and **English**, with a manual switch. The app is installable as a **PWA** (`/manifest.webmanifest`, `/service-worker.js`), and the service worker never caches `/api/*` responses.

<a id="en-install"></a>

## Installation

### Prerequisites

- Python 3.8+ with `pip`
- FFmpeg + ffprobe (libass-enabled for burning)
- A Persian font (for burning)

### Install

```bash
python -m venv --system-site-packages .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> `--system-site-packages` lets the venv reuse packages already installed system-wide (useful on Termux). Omit it if you prefer an isolated venv; dependencies will simply be reinstalled.

Media tooling (Termux):

```bash
pkg install ffmpeg noto-fonts
```

### Initial configuration

```bash
cp .env.example .env
```

Edit `.env` and set at least the **API URL, API key and model** for both the speech-to-text and translation services (see the configuration tables below).

### Start the server

```bash
python run.py                  # 127.0.0.1:8000
python run.py --host 0.0.0.0   # reachable from other devices on your LAN
python run.py --port 8080
python run.py --reload         # development auto-reload
```

Then open **http://127.0.0.1:8000** in a browser.

> **Security warning:** binding to `0.0.0.0` exposes the server to **every device on the network**, and the app has **no authentication**. Only do that on a network you trust.

<a id="en-usage"></a>

## Usage

A typical workflow:

1. Start the server (`python run.py`) and open a browser.
2. On the **New** tab, select a video (or audio) file; its metadata is shown.
3. Decide whether to burn subtitles into the video or get only the `.srt` (unchecking is faster).
4. Press **Start translation** to upload and queue the job.
5. The progress timeline shows audio extraction → transcription → translation → SRT → burn → packaging. You can **Cancel** at any time.
6. When done, download the burned video (`...fa.mp4`) or the subtitle file (`...fa.srt`).
7. Browse the translated text in the **preview** panel.
8. On failure, the job stays in **History** and can be **resumed** without repeating finished (already billed) work.

<a id="en-config"></a>

## Configuration

Configuration is merged from three layers (later layers win):

1. Built-in defaults (`app/config.py`).
2. Environment variables, optionally seeded from a `.env` file.
3. Runtime settings saved through the web UI (Settings tab) into `data/settings.json` — **this layer takes precedence**.

API keys live **only on the server**. The browser only ever receives a boolean "is configured" flag plus a masked hint.

### Environment variables

#### Speech to text

| Variable | Default | Meaning |
| :--- | :--- | :--- |
| `STT_API_URL` | `https://api.openai.com/v1/audio/transcriptions` | STT endpoint (OpenAI protocol) |
| `STT_API_KEY` | (empty) | STT API key |
| `STT_MODEL` | `whisper-1` | model name |
| `STT_LANGUAGE` | `en` | source language hint; `auto` = detect |
| `STT_RESPONSE_FORMAT` | `verbose_json` | `verbose_json` = per-segment timings |
| `STT_PROMPT` | (empty) | optional prompt/context for the model |
| `STT_CHUNK_SECONDS` | `600` | split audio into chunks of this many seconds |
| `STT_AUDIO_FORMAT` | `mp3` | extracted-audio format (`mp3`/`m4a`/`wav`/`ogg`/`flac`) |
| `STT_AUDIO_BITRATE` | `64k` | extracted-audio bitrate |
| `STT_SAMPLE_RATE` | `16000` | extracted-audio sample rate (Hz) |
| `STT_TIMEOUT` | `600` | per-request timeout (seconds) |

#### Translation

| Variable | Default | Meaning |
| :--- | :--- | :--- |
| `TRANSLATION_API_URL` | `https://api.openai.com/v1/chat/completions` | translation endpoint (OpenAI protocol) |
| `TRANSLATION_API_KEY` | (empty) | translation API key |
| `TRANSLATION_MODEL` | `gpt-4o-mini` | model name |
| `TRANSLATION_TEMPERATURE` | `0.2` | sampling temperature |
| `TRANSLATION_MAX_TOKENS` | `0` | output token cap; `0` = provider decides |
| `TRANSLATION_BATCH_SIZE` | `20` | subtitle lines per request |
| `TRANSLATION_TIMEOUT` | `240` | per-request timeout (seconds) |
| `TRANSLATION_RETRIES` | `3` | retries per failed batch |
| `TARGET_LANGUAGE` | `Persian` | language subtitles are translated into |

#### Subtitles

| Variable | Default | Meaning |
| :--- | :--- | :--- |
| `SUBTITLE_FONT` | (empty) | font file path; empty = auto-detect |
| `SUBTITLE_FONT_NAME` | (empty) | family name to embed; empty = derived from the file |
| `SUBTITLE_FONT_SIZE` | `0` | font size; `0` = scaled from the video height |
| `SUBTITLE_OUTLINE` | `2` | outline width (ASS units) |
| `SUBTITLE_SHADOW` | `0` | shadow depth |
| `SUBTITLE_MARGIN_V` | `28` | vertical margin |
| `SUBTITLE_PRIMARY_COLOUR` | `&H00FFFFFF` | text colour (ASS `&HBBGGRR` order) |
| `SUBTITLE_OUTLINE_COLOUR` | `&H00000000` | outline colour |
| `SUBTITLE_BACK_COLOUR` | `&HA0000000` | box colour when `BORDER_STYLE=3` |
| `SUBTITLE_BORDER_STYLE` | `1` | `1` = outline+shadow, `3` = opaque box |
| `SUBTITLE_MAX_LINE_CHARS` | `42` | max characters per line |
| `SUBTITLE_MAX_LINES` | `2` | max lines per cue |

#### Video encoding

| Variable | Default | Meaning |
| :--- | :--- | :--- |
| `FFMPEG_PATH` / `FFPROBE_PATH` | `ffmpeg` / `ffprobe` | binary paths |
| `VIDEO_ENCODER` | `libx264` | encoder (allowed list via `/api/config`) |
| `VIDEO_PRESET` | `veryfast` | encoder preset |
| `VIDEO_CRF` | `26` | quality (lower = better/larger) |
| `VIDEO_THREADS` | `0` | `0` = let FFmpeg decide |
| `AUDIO_COPY` | `true` | copy original audio when MP4-safe instead of re-encoding |
| `AUDIO_FALLBACK_BITRATE` | `128k` | bitrate when audio must be re-encoded |
| `BURN_TIMEOUT` | `0` | `0` = no timeout on the burn step |

#### Server & housekeeping

| Variable | Default | Meaning |
| :--- | :--- | :--- |
| `HOST` | `127.0.0.1` | interface to bind |
| `PORT` | `8000` | TCP port |
| `MAX_UPLOAD_BYTES` | `0` | upload limit; `0` = unlimited (disk bound) |
| `JOB_RETENTION_HOURS` | `24` | auto-delete finished job workspaces after N hours |
| `CLEANUP_INTERVAL_HOURS` | `6` | how often cleanup runs |
| `MIN_FREE_DISK_MB` | `500` | free-storage warning threshold |
| `KEEP_INTERMEDIATE` | `false` | keep intermediate audio/ASS files (debugging) |
| `LOG_LEVEL` | `INFO` | root log level |

Optional path overrides: `DATA_DIR` (runtime data root) and `ENV_FILE` (location of `.env`; default `<repo>/.env`).

> **Settings security:** `data/settings.json` stores real API keys and is written with mode `0600`. `.env` is never sent to the browser and secrets are redacted from logs.

<a id="en-privacy"></a>

## Privacy & Security

- Processing (audio extraction, subtitle generation, encoding) happens **on your own machine**.
- Uploaded files, extracted audio and outputs live in `data/jobs/<id>/` on your device.
- For speech-to-text and translation, **audio and text** are sent to the services **you** configure — nothing is sent to an AniSubx-operated server.
- Your API keys are stored **only on the server** (`data/settings.json`, mode `0600`); the browser sees only an "is configured" flag and a masked hint.
- The app has **no accounts, passwords or authentication**. Keep it bound to `127.0.0.1` unless you are on a trusted network.
- No third-party hosted service is required; only the APIs you configure yourself.

<a id="en-notes"></a>

## Important Notes

- **API costs:** speech recognition and translation each incur their own cost (per your chosen providers). Translation batches are recorded as billed only after success, so resume never re-bills finished work.
- **Processing time:** burning with a software encoder is slow on phones; use the SRT-only option when speed matters.
- **Disk space:** processing roughly **doubles** the input file's space requirement.
- **Temporary files:** intermediates are removed when a job finishes (unless `KEEP_INTERMEDIATE=true`); old jobs are auto-cleaned per `JOB_RETENTION_HOURS`.
- **Recognition quality:** depends on the model and source language. If the STT provider returns no timestamps, subtitle timings are **estimated** and may drift.
- **libass:** burning requires an FFmpeg built with libass; otherwise only the `.srt` is available.
- **Persian font:** a Persian-capable font is required for correct rendering during burn-in (Termux: `pkg install noto-fonts`).
- **Untranslated lines:** if the model cannot translate a line, the original text is kept so the subtitle timing never desynchronises.

<a id="en-build"></a>

## Build from Source

There is nothing to compile — this is a plain Python package. For a development environment:

```bash
python -m venv --system-site-packages .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

Run the server in development mode:

```bash
python run.py --reload
```

Run the tests:

```bash
python -m pytest -q
```

The pytest suite uses a fake HTTP transport and fake ffprobe output — **no real API keys or network calls**. Keep changes dependency-light and prefer the standard library; full guidance is in [CONTRIBUTING.md](CONTRIBUTING.md).

### Project layout

```
app/                 # FastAPI application and processing logic
  ├── main.py          # all HTTP routes
  ├── jobs.py          # job queue, state store, processing pipeline
  ├── config.py        # layered configuration (defaults → .env → settings.json)
  ├── transcription.py # audio chunking and speech-to-text driver
  ├── translation.py   # LLM translation driver (batched, resumable)
  ├── subtitles.py     # SRT/ASS generation, parsing, validation
  ├── video.py         # ffprobe/ffmpeg: probing, extraction, burn, encoding
  ├── fonts.py         # Persian font discovery (pure stdlib)
  ├── diagnostics.py   # real system checks
  └── providers/       # lightweight STT & translation clients (OpenAI protocol)
static/              # web UI (vanilla JS, PWA, fa/en i18n)
app/templates/       # single-page HTML shell
tests/               # pytest suite
run.py               # server entry point
requirements.txt     # runtime dependencies (just 3 packages)
```

<a id="en-contributing"></a>

## Contributing

Contributions are welcome:

1. **Fork** the repository.
2. Create a **branch** with a descriptive name.
3. Keep the change focused and dependency-light (write/update tests).
4. **Commit** and open a **Pull Request** with a clear “why”.
5. Make sure `python -m pytest -q` passes before submitting.

Guidelines: [CONTRIBUTING.md](CONTRIBUTING.md) · Security: [SECURITY.md](SECURITY.md)

<a id="en-license"></a>

## License

AniSubx is free and open-source software licensed under the **GNU Affero General Public License v3.0 only (`AGPL-3.0-only`)**.

- Full text: [LICENSE](LICENSE)
- Third-party components (Python packages, fonts, FFmpeg) remain under their own licenses — see [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md)

---

<div align="center">

### ⚡ AniSubx

صدای ویدیو را به زیرنویس فارسی تبدیل کن — سریع، سبک و روی دستگاه خودت

Turn video speech into Persian subtitles — fast, lightweight, on your own device

<br>

Made with ❤️ for anime and subtitle lovers

</div>