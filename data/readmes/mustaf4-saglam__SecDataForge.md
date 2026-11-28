# SecDataForge

Açık ve yeniden kullanılabilir siber güvenlik veri seti üretim aracı.

SecDataForge, açık siber güvenlik kaynaklarından veri toplar, standartlaştırır,
tekrarları ayıklar, Türkçe açıklama ve soru-cevap örnekleri üretir, kalite
kontrollerinden geçirir ve LLM eğitimi/değerlendirmesi için JSONL ve CSV
formatında dışa aktarır. Bu proje bir chatbot değildir; amacı izlenebilir ve
kalitesi ölçülebilir veri setleri üretmektir.

## Teknoloji yığını

- Python 3.12+
- [httpx](https://www.python-httpx.org/): HTTP istemcisi
- [pydantic](https://docs.pydantic.dev/): veri modelleri ve doğrulama
- SQLite: kayıtlar, işlem durumu ve izlenebilirlik
- [typer](https://typer.tiangolo.com/): komut satırı arayüzü
- [Streamlit](https://streamlit.io/): yönetim paneli
- [pytest](https://docs.pytest.org/): testler
- [Ruff](https://docs.astral.sh/ruff/): biçimlendirme ve statik kontroller
- Ollama / OpenAI uyumlu API: isteğe bağlı LLM bağlantısı (kapalı varsayılan)

## Klasör yapısı

```text
secdataforge/
├── pyproject.toml
├── README.md
├── .env.example
├── .gitignore
├── src/secdataforge/      # paket kodu (cli, config, schemas, database, pipeline, ...)
├── app/dashboard.py       # Streamlit yönetim paneli
├── tests/                 # pytest birim testleri
├── examples/              # örnek JSON kayıtları
└── data/                  # raw / processed / exports (Git'e dahil değil)
```

## Kurulum

```bash
# 1. Depoyu klonlayın / klasöre geçin
cd SecDataForge

# 2. Sanal ortam oluşturun (önerilir)
python3 -m venv .venv
source .venv/bin/activate          # fish kabuğunda: source .venv/bin/activate.fish

# 3. Bağımlılıkları yükleyin (streamlit paneli dahil)
pip install -e .

# 4. Ortam dosyasını oluşturun
cp .env.example .env
# .env dosyasını düzenleyin (GITHUB_TOKEN gibi değerleri ekleyebilirsiniz).
```

`pip install -e .` komutu `secdataforge` konsol komutunu ve panel için
`streamlit` aracını kurar. Sanal ortam aktifken `secdataforge` ve `streamlit`
komutları doğrudan çalışır.

## İlk çalıştırma

Aşağıdaki toplama komutları gerçek API'lere bağlanır. Ağsız doğrulama için testleri kullanın.

```bash
# Veritabanını başlat ve kaynakları listele
secdataforge sources

# Örnek veriyle bir toplamayla başlatmak için pipeline'ı kullanabilirsiniz;
# aşağıdaki komut gerçek GitHub API'sine çağrı yapar (hız sınırı uygulanabilir).
secdataforge collect github --limit 50

# OSV: kimlik veya paket/ekosistem filtresi zorunludur
secdataforge collect osv --package django --ecosystem PyPI --limit 100

# Kalite raporu
secdataforge report

# Sadece 'valid' kayıtları dışa aktar
secdataforge export --format both --output data/exports --quality valid

# Tüm durumdaki kayıtları dışa aktar
secdataforge export --format jsonl --output data/exports --prefix all --quality all
```

Komutların `--help` çıktıları mevcuttur:

```bash
secdataforge --help
secdataforge collect --help
```

## Komut satırı komutları

### Terminalden başlatma ve grafik arayüzüne geçiş

`secdataforge` tek başına yazıldığında etkileşimli **terminal menüsü** açılır;
grafik arayüzü veya tarayıcı kendiliğinden başlatılmaz. Menüden kaynakları ve
raporu görebilir, komut çalıştırabilir veya **5 — Grafik arayüzüne geç** seçeneğiyle
paneli açabilirsiniz. Panel açıkken `Ctrl+C` ile durdurup terminal menüsüne dönün.

```bash
secdataforge                  # terminal menüsü
secdataforge gui              # yalnız istendiğinde grafik arayüzü
secdataforge gui --port 8502   # farklı yerel port
secdataforge collect github --limit 50  # doğrudan komutlar da çalışır
```

Etkileşimsiz çalıştırmada komutsuz çağrı menü yerine yardımı gösterir.
Menüye açıkça girmek için `secdataforge menu` kullanılabilir. Panel yalnız
`127.0.0.1` üzerinde dinler.

Bu bilgisayarda `~/.local/bin/secdataforge` başlatıcısı `.venv-current` ortamını
kullanır; dizin değiştirmeye veya ortamı elle etkinleştirmeye gerek yoktur.
Fish için kullanıcı komut dizini `~/.config/fish/conf.d/secdataforge.fish` ile
PATH'e eklenmiştir. Yeni terminal açın; mevcut Fish oturumunda bir kez
`source ~/.config/fish/conf.d/secdataforge.fish` çalıştırın. Başka bilgisayarlarda
paket kurulumunun ardından sanal ortamı etkinleştirin veya benzer bir başlatıcı ekleyin.

| Komut | Açıklama |
|-------|----------|
| `secdataforge sources` | Yapılandırılan kaynakları ve son işlem durumlarını listeler |
| `secdataforge collect [kaynak] [--limit N] [--resume] [--full-history] [--since YYYY-MM-DD]` | Varsayılan olarak en son güncellenen kayıtlardan başlar; `--resume` önceki toplamanın imlecinden geçmiş taramasını sürdürür; `--full-history` imleci yok sayar. Tüm modlar `--limit` ile sınırlıdır. |
| `secdataforge validate` | Mevcut kayıtların kalitesini yeniden değerlendirir |
| `secdataforge enrich [--llm] [--force]` | Reddedilmemiş ve henüz tamamlanmamış kayıtları zenginleştirir; `--force` tamamlananları da yeniden üretir (ek API maliyeti). |
| `secdataforge review RECORD_ID --approve/--reject` | Kaynak içeriği için açık insan incelemesi kararı verir; lisans/kalite sorunu olan kaynak onaylanamaz. |
| `secdataforge review-qa QA_ID --approve/--reject` | QA için açık insan incelemesi kararı verir; onay için tüm kaynakların uygun olması gerekir. |
| `secdataforge export [--format jsonl\|csv\|both] [--quality valid\|all] [--output DIR] [--source X]` | Kayıtları dışa aktarır |
| `secdataforge report` | Veri kalitesi raporunu gösterir |

## Kaynak yapılandırması

Bağlayıcılar `src/secdataforge/config.py` ve `.env` üzerinden yapılandırılır:

- `GITHUB_BASE_URL` — GitHub Global Security Advisories API (varsayılan: `https://api.github.com`)
- `GITHUB_TOKEN` — GitHub personal access token (opsiyonel, oran sınırını artırır)
- `OSV_BASE_URL` — OSV Vulnerability API (varsayılan: `https://api.osv.dev/v1`)
- `DEFAULT_RECORD_LIMIT`, `REQUEST_TIMEOUT`, `MAX_RETRIES`, `BACKOFF_FACTOR`

Bağlayıcılar sayfalama, zaman aşımı, sınırlı yeniden deneme (artan bekleme), HTTP 429
yönetimi ve idempotent (tekrar çalıştırılabilir) işlemleri destekler. Tüm veritabanı
kontrolsüz indirilmez; kayıt sınırı ve sayfalama ile sınırlandırılır.

### `collect` ek seçenekleri (GitHub için)

| Seçenek | Açıklama |
|---------|----------|
| `--resume` | Son işlemin kaydettiği sayfa imlecinden (`next_cursor`) devam eder. **Yeni kayıt kontrolü değildir**; geçmiş taramasını sürdürür. |
| `--full-history` | İmleci yok sayarak en son güncellenenden başlar. `--limit` kadar kayıt işler; kalan geçmiş için sonraki çalıştırmalarda `--resume` kullanın. `--resume` ile birlikte verilirse bu seçenek önceliklidir. |
| `--since YYYY-MM-DD` | Belirtilen tarihten eski kayıtları atlar (client-side filtre); `published_at` alanına bakar. Limit çekilen kayıt sayısıdır; filtreye uyan sonuç sayısı daha az olabilir. |

**Örnekler:**

```bash
# Periyodik kontrol: en son güncellenen 500 kaydı yeniden değerlendir
secdataforge collect github --limit 500

# Önceki toplamanın geriye doğru sayfalamasını sürdür
secdataforge collect github --limit 500 --resume

# Geçmiş taramasını başlat (ilk 5000; kalanı --resume ile)
secdataforge collect github --limit 5000 --full-history

# İlk 5000 kayıt içinde yayın tarihi 2024 ve sonrası olanlar
secdataforge collect github --limit 5000 --full-history --since 2024-01-01

# Sadece 2025'ten bugüne (imleç yok, sadece filtre)
secdataforge collect github --limit 2000 --since 2025-01-01
```

GitHub kayıtları `updated DESC` sırasıyla alınır. Aynı kaynak kimliğinin ham içeriği
değiştiğinde kayıt güncellenir; eski ham sürümler `raw_record_versions` tablosunda
korunur. Eski çeviri/önlem ve tamamlanma işaretleri temizlenir; ilgili QA onayları
yeniden incelemeye alınır. Değişmeyen kayıtlar tekrar eklenmez. Toplama sonuçları
eklenen ve güncellenen kayıt sayılarını ayrı gösterir.

OSV örnekleri:

```bash
secdataforge collect osv --cve CVE-2024-0001 --ghsa GHSA-xxxx-yyyy-zzzz
secdataforge collect osv --package django --ecosystem PyPI --version 4.2 --limit 100
# İki kaynak birlikte çalıştırılacaksa OSV filtresi de verin
secdataforge collect all --package django --ecosystem PyPI --limit 100
```

Kimlik sorguları `GET /v1/vulns/{id}`, paket sorguları `POST /v1/query` kullanır.
OSV sayfa belirteçleri ve kayıt limiti nedeniyle yarım kalan sayfalar imleçte
saklanır. OSV filtresi değişirse `--resume` kullanmadan yeni tarama başlatın.
Boş filtre veya HTTP hatası sessiz başarı olarak gösterilmez.

Varsayılan toplama yalnız verilen limit kapsamındaki güncellemeleri kontrol eder;
tüm geçmişin güncel olduğunu garanti etmez. Yenileme ve geçmiş devamı aynı son
işlem imlecini kullanır; uzun geçmiş taraması sırasında araya yenileme sokmayın.

OWASP bağlayıcısı sonraki bir aşamada planlanmıştır; yalnızca erişim ve içerik
kullanım koşulları doğrulanmış içerikler içe aktarılacaktır.

## LLM ayarları (isteğe bağlı, kapalı varsayılan)

LLM entegrasyonu varsayılan olarak kapalıdır ve uygulamanın diğer işlevleri
LLM olmadan da çalışmaya devam eder. `.env` üzerinden yapılandırın:

```ini
LLM_ENABLED=true
LLM_PROVIDER=gemini          # ollama | openai_compatible | gemini | claude | huggingface | evren
LLM_MODEL=gemini-1.5-flash
LLM_TEMPERATURE=0.0
LLM_TIMEOUT=120.0            # saniye; yavaş yerel modeller için artırın

# Sağlayıcıbazlı API anahtarlardan biri yeterli
GEMINI_API_KEY=              # https://aistudio.google.com/
CLAUDE_API_KEY=              # https://console.anthropic.com/
HUGGINGFACE_API_KEY=         # https://huggingface.co/settings/tokens
LLM_API_KEY=                 # openai_compatible (OpenAI, Mistral, vb.) için

# EVREN LLM API (Türkiye, SAYZEK ekosistemi; OpenAI uyumlu)
EVREN_API_KEY=               # EVREN hesabınızdan alın; ASLA koda/depoya yazmayın
EVREN_BASE_URL=https://evren-llmapi.ssyz.org.tr/v1
EVREN_MODEL=                 # boş bırakılırsa /models listesinden ilk model seçilir
EVREN_TERMS_URL=https://evren-llmapi.ssyz.org.tr
```

### Desteklenen LLM sağlayıcıları

| Sağlayıcı | `LLM_PROVIDER` | API anahtarı | Önerilen modeller |
|-----------|----------------|--------------|-------------------|
| **Ollama** (yerel) | `ollama` | Yok (localhost) | `llama3.2`, `mistral`, `qwen2.5` |
| **OpenAI uyumlu** | `openai_compatible` | `LLM_API_KEY` | `gpt-4o-mini`, `gpt-4o`, `mistral-large` |
| **Google Gemini** | `gemini` | `GEMINI_API_KEY` | `gemini-1.5-flash`, `gemini-1.5-pro` |
| **Anthropic Claude** | `claude` | `CLAUDE_API_KEY` | `claude-3-5-sonnet`, `claude-3-haiku` |
| **Hugging Face** (açık kaynak) | `huggingface` | `HUGGINGFACE_API_KEY` | `meta-llama/Llama-3.1-8B-Instruct`, `mistralai/Mistral-7B-Instruct-v0.3` |
| **EVREN** (Türkiye) | `evren` | `EVREN_API_KEY` | `/models` listesinden seçilir (tahmini ad YOK) |

**Hugging Face** ile erişebileceğiniz açık kaynak dağıtık modellerden bazıları:

- `meta-llama/Llama-3.1-8B-Instruct` — Meta'nın Llama 3.1 modeli
- `mistralai/Mistral-7B-Instruct-v0.3` — Mistral AI
- `Qwen/Qwen2.5-7B-Instruct` — Alibaba Qwen
- `deepseek-ai/DeepSeek-V3` — DeepSeek
- `google/gemma-2-9b-it` — Google Gemma

Binlerce model: https://huggingface.co/models?pipeline_tag=text-generation

**Kullanım örnekleri:**

```bash
# Yerel Ollama (varsayılan)
secdataforge enrich --llm --model llama3.2 --limit 10

# Google Gemini
secdataforge enrich --llm --provider gemini --model gemini-1.5-flash --limit 10

# Anthropic Claude
secdataforge enrich --llm --provider claude --model claude-3-5-sonnet-20241022 --limit 10

# Hugging Face açık kaynak model
secdataforge enrich --llm --provider huggingface --model meta-llama/Llama-3.1-8B-Instruct --limit 10

# OpenAI veya uyumlu API (Mistral, Groq, vb.)
secdataforge enrich --llm --provider openai_compatible --model gpt-4o-mini --limit 10
```

### EVREN entegrasyonu (Türkiye, SAYZEK)

EVREN, OpenAI uyumlu bir REST API'dir
(`https://evren-llmapi.ssyz.org.tr/v1`). Entegrasyon üç adımdır:

```bash
# 1) .env'e anahtarınızı ekleyin (koda asla yazmayın)
cp .env.example .env
# EVREN_API_KEY=... değerini .env içine girin

# 2) Kullanım şartlarını okuyup AÇIK onay verin (otomatik kabul YOK)
secdataforge evren-setup

# 3) Bağlantı + model listesi + kısa sohbet testini çalıştırın
secdataforge evren-test
# opsiyonel: --model <id>  veya  --no-chat

# 4) Kullanım
secdataforge enrich --llm --provider evren --limit 10
```

EVREN davranışları:

- **Model adı tahmin edilmez:** `EVREN_MODEL` boşsa model kimliği her zaman
  `GET /models` yanıtından seçilir. Listeyi `secdataforge evren-test` ile
  görebilirsiniz.
- **Kullanım şartları:** `enrich --provider evren` yalnızca `evren-setup`
  ile açık onay verildikten sonra çalışır. Onay kaydı yerel dosyada tutulur
  (`data/evren_terms_accepted.json`, `.gitignore`'da) ve **API anahtarı
  içermez** (yalnızca 12 karakterlik parmak izi).
- **Hata eşlemesi:** 401 (anahtar), 403 (şart/izin), 404 (endpoint/model),
  429 (kota) ve 5xx (servis) için açıklayıcı Türkçe mesaj üretilir.
- **Panel:** `streamlit run app/dashboard.py` → *LLM / EVREN* sekmesinde
  model listesi çekme, bağlantı testi, şart onayı ve zenginleştirme var.
  API anahtarı panele/tarayıcıya ASLA gönderilmez; yalnızca
  "tanımlı/tanımsız" gösterilir.
- **Kimlik doğrulama:** `Authorization: Bearer` ve `X-API-Key` başlıkları
  birlikte gönderilir.
- `response_format` desteklemeyen dağıtımlar için otomatik geri düşme vardır.

**Önemli notlar:**

- API anahtarları kod içine yazılmaz, sadece `.env` dosyasında tutulur
- Her sağlayıcı için `is_available()` kontrolü yapılır — anahtar yoksa açıklayıcı hata alırsınız
- Yavaş modeller için `LLM_TIMEOUT=300` gibi değerler kullanın
- Tüm çıktılar `review` kuyruğuna düşer; otomatik onay yok

Görevler: Türkçeleştirme, açıklama üretimi, kaynakla desteklenen soru-cevap
hazırlama, önlem önerisi ve sınıflandırma. Çıktılar yapılandırılmış JSON olarak
üretilir ve Pydantic ile doğrulanır. CVE kimlikleri, sürümler, tarihler, paket
isimleri ve önem derecesini değiştirmeye izin verilmez. Yalnızca JSON şemasına
uymak yetmez; kaynakla dayanak kontrolü, kalite filtreleri ve inceleme süreci
ayrı tutulur. LLM çıktıları varsayılan olarak inceleme kuyruğuna alır.

## Veri şeması

### Zenginleştirme ve insan incelemesi

`enrich`, yalnız `review` kayıtlarını değil, `valid` ve `pending` dahil tüm
reddedilmemiş ve tamamlanmamış kayıtları seçer. Başarılı görevler ayrı ayrı
kaydedilir; kısmi hatalarda sonraki çalıştırma yalnız başarısız görevleri tekrarlar.
Kaynakla desteklenmeyen QA yanıtı da tamamlanmış bir denemedir. HTTP/JSON/şema
hataları hata olarak raporlanır ve `processing_errors` tablosuna yazılır.

LLM çıktısı bulunan kayıtlar `llm_review_required` ile korunur. `validate` bu
işareti kaldırmaz; yalnız CLI'deki `review` komutu veya paneldeki açık karar
butonları kaldırabilir. Reddedilmiş kayıtlar doğrulamayla otomatik onaylanmaz.

```bash
secdataforge enrich --llm --limit 10 --verbose
# Kaynak metni, çeviri ve önlemi inceledikten sonra:
secdataforge review gh:GHSA-xxxx-yyyy-zzzz --approve
# Soru, cevap ve kaynaklarını inceledikten sonra:
secdataforge review-qa 'qa:...' --approve
secdataforge export --qa --output data/exports
```

Normal dışa aktarım yalnız `valid`, lisansı `allowed`, LLM incelemesi tamamlanmış
kayıtları içerir. QA varsayılanı `approved` durumudur; insan inceleme bayrağı kapalı
ve **tüm** kaynakları uygun olmalıdır. `--qa-status all` tek başına bu korumaları
kaldırmaz. Yalnız yerel inceleme için `--unsafe-qa --qa-status all` kullanılabilir;
bu çıktı eğitim/yeniden dağıtım için uygun kabul edilmemelidir. Benzer şekilde
`--quality all` tanısal kullanım içindir.

`--prefix` yalnız tek bir dosya adı öneki kabul eder; yol, `../` veya çıktı dizini
dışına yönelen sembolik bağlantılar reddedilir. Panel aynı kontrolü kullanır.

İlk açılışta eski veritabanına alanlar otomatik eklenir. Eski çeviri/önlem
kayıtlarının insan onayı kanıtlanamadığından bunlar yeniden incelemeye alınır;
metinler silinmez. Güncellemeden önce veritabanının yedeğini almanız önerilir.

Ortak güvenlik duyurusu şeması (`src/secdataforge/schemas.py`):

| Alan | Tür | Açıklama |
|------|-----|----------|
| `record_id` | string | Uygulama içi benzersiz kimlik |
| `source` | string | Kaynak adı (`github`, `osv`, ...) |
| `source_id` | string | Kaynaktaki orijinal kimlik (GHSA / CVE / OSV) |
| `source_url` | string? | Kaynak bağlantısı |
| `license` | string? | İçerik lisansı |
| `license_status` | enum | `allowed` / `restricted` / `unknown` |
| `collected_at` | datetime | Toplanma tarihi |
| `published_at` | datetime? | Yayın tarihi |
| `modified_at` | datetime? | Son değişiklik tarihi |
| `title` | string? | Başlık |
| `description_original` | string? | Orijinal açıklama |
| `description_tr` | string? | Türkçe açıklama |
| `cve_ids` | [string]? | CVE kimlikleri |
| `cwe_ids` | [string]? | CWE kimlikleri |
| `affected_packages` | [string]? | Etkilenen paketler |
| `severity` | string? | Önem derecesi |
| `references` | [string]? | Referans bağlantılar |
| `remediation_tr` | string? | Türkçe önlem önerisi |
| `raw_hash` | string? | Ham veri SHA-256 özeti |
| `quality_status` | enum | `pending` / `valid` / `review` / `rejected` |
| `quality_issues` | [string]? | Tespit edilen kalite sorunları |
| `llm_review_required` | bool | LLM içeriği için açık insan onayı bekleniyor mu? |
| `enrichment_tasks` | [string] | Tamamlanan çeviri, önlem ve QA görevleri |
| `enriched_at` | datetime? | Üç görev hatasız tamamlandığında işaretlenir |

Ham yanıt `raw_records` tablosunda, normalize edilmiş veri
`security_advisories` tablosunda ayrı ayrı tutulur. AI üretilen soru-cevap
örnekleri `qa_pairs` tablosunda (soru, cevap, kaynak kimlikleri, dayanak alanları,
model, üretim zamanı, doğrulama durumu, insan inceleme bayrağı) saklanır.

Örnek kayıtlar `examples/` dizinindedir:
- `examples/sample_advisory.json`
- `examples/sample_qa.json`

## Lisans yaklaşımı

Kaynakları yalnızca HTTP ile alınabiliyor olmaları temel alınarak yeniden
dağıtılabilir kabul edilmez. Her kaynak için kullanım koşulları ve lisansı ayrı
değerlendirilir. Bilinmeyen veya uygun olmayan lisanslı içerikler varsayılan
olarak dışa aktarılabilir veri setine girmez; `license_status` `unknown` veya
`restricted` olan kayıtlar `review` (inceleme) durumunda tutulur ve
`--quality valid` dışa aktarımlarından çıkarıldıkları gibi kalır.

GitHub Global Security Advisories verisi, GitHub Advisory Database'ten gelir ve
CC-BY-4.0 lisansı ile yayımlanır (kaynak:
<https://github.com/github/advisory-database> — LICENSE.md). Atıf koşulu, her
kayıtta korunan `source_url` (GHSA sayfası) ve `license` alanıyla sağlanır.
Bu nedenle GitHub konektörü lisansı `CC-BY-4.0` / `allowed` olarak tanımlıdır.

OSV verisi farklı veritabanlarından harmanlandığı için tek ve doğrulanmış bir
lisans sunmaz; kayıtlar varsayılan olarak `unknown` işaretlenir ve inceleme
kuyruğunda tutulur. Veri setinizde OSV kullanacaksanız her kaynağın kullanım
koşullarını ayrıca değerlendirmeniz gerekir.

Lisans kararları konektör yapılandırmasında (`license`, `license_status`)
tutulur; `secdataforge validate` güncel politikayı mevcut kayıtlara da uygular
(ör. sonradan verilen bir lisans kararı lisans kaynaklı incelemeyi kaldırabilir;
LLM insan incelemesi gereksinimini kaldırmaz).

## Testler

```bash
pip install -e '.[dev]'        # dev bağımlılıkları
python -m pytest              # tüm birim testleri
ruff check src/ tests/ app/    # statik kontroller
ruff format --check src/ tests/ app/  # dosyaları değiştirmeden biçim denetimi
```

Sistem Python sürümü yükseltilince eski `.venv` bağımlılıkları bulunamıyorsa,
eski ortamı silmeden yeni ortam oluşturabilirsiniz:

```bash
python3 -m venv .venv-current
source .venv-current/bin/activate
python -m pip install -e '.[dev]'
```

Testler gerçek HTTP/API çağrısı yapmaz; sentetik veri ve mock bağlayıcılar
kullanılır. Canlı verilerden gelen sonuçlar testlerin tek doğru çıktısı olarak
sabitlenmez.

## Bilinen sınırlamalar

- Kimlik doğrulamasız GitHub isteklerinde saatlik 60 isteklik oran sınırı
  vardır (`GITHUB_TOKEN` ile daha yüksek sınır).
- OSV'in genel "liste tüm" endpoint'i yoktur; `cves`/`ghsas`/`package` filtreleri
  üzerinden sorgu yapılır.
- LLM entegrasyonu opsiyonel; yapılandırılmadığında çeviri/QA/önlem özellikleri
  devre dışı kalır.
- OWASP bağlayıcısı ilk sürümde dahil değildir.
- Türkçeleştirme ve LLM çıktıları otomatik olarak onaylanmaz; insansözlü
  inceleme kuyruğuna alınır.

## Geliştirici notları

- Tüm işlem hatı aşamaları ayrı modüldedir (`pipeline.py`, `exporters.py`,
  `quality.py`, `sources/`, `llm/`). Bir kaynak hata verdiğinde tüm hatayı
  çökmemesini sağlar; işlem devam ettirilebilir ve idempotent-dir.
- Yeni bir kaynak eklemek için `sources/base.py`'daki `BaseConnector` sınıfını
  miras alıp `fetch`, `normalize`, `enrich` metodlarını uygulamak yeterlidir.
- Gizli bilgiler `.env` dosyasında tutulur; `.env` Git'e eklenmez
  (`.gitignore`).
