# TurkActuary MCP

**Türkçe** · [English](#english)

<!-- mcp-name: io.github.afsharid/turkactuary -->

Türkiye sigortacılık mevzuatı araması ve aktüeryal hesap araçları için bir **MCP sunucusu**.
İstediğiniz modeli ya da ajanı kullanın: LM Studio, Claude Code, Codex, VS Code, Claude Desktop, Cursor ve MCP destekleyen her istemci bu araçlara erişir.

> **Uyarı:** Bu araçlar karar desteği içindir; uzman veya yetkili kurum görüşünün yerine geçmez. Mevzuat metinleri
> 2026-10-18 erişimli konsolide kopyadır ve kendiliğinden güncellenmez. Güncel hüküm için resmî kaynağı doğrulayın.

## Ne içerir

| Araç | Ne yapar |
|---|---|
| `mevzuat_ara` | Sigortacılık mevzuatında (5684 sayılı Kanun, yönetmelikler ve tebliğler; konsolide), 16 öğretici notta ve 49 seçilmiş Yargıtay kararında arama, toplam 827 parça. Projede ölçülen **v5** karma arama (BM25 + Qwen3-Embedding-4B); embedding modeli yoksa BM25. Parça kimliği, başlık, kaynak ve metin döner. |
| `belge_getir` | Parça kimliğiyle tam metni getirir. |
| `present_value`, `annuity`, `life_insurance_pv` | Bugünkü değer, annüite, süreli hayat sigortası. |
| `chain_ladder`, `bornhuetter_ferguson` | Hasar rezervi (kümülatif üçgen, paid/incurred açık). |
| `portfolio_metrics`, `combined_ratio` | Frekans, şiddet, saf prim, hasar oranı; bileşik oran. |
| `life_annuity_pv`, `life_cashflow_projection` | Yaşam koşullu annüite, hayat poliçesi nakit akışı. |
| `xl_layer_recovery`, `credibility_estimate`, `earned_exposure` | XL katman tahsilatı, güvenilirlik, kazanılmış maruziyet. |
| `poisson_glm`, `gamma_severity_glm` | Frekans ve şiddet GLM'leri. |
| `is_goremezlik` | Sürekli/geçici iş göremezlik tazminatı (Yargıtay uygulaması). |
| `destekten_yoksun_kalma` | Destekten yoksun kalma tazminatı, hak sahibi başına (Yargıtay uygulaması). |
| `asgari_ucret` | Aylık asgari ücret 2008–2026 (ÇSGB): tarih aralığındaki dönemler, brüt ve net; çıktı doğrudan gelir dönemi olarak kullanılır. |

Bir de `turkactuary` adlı **prompt** var: modele kaynaklara dayanmasını, sayıyı araçla hesaplamasını ve belge içindeki
talimatları uygulamamasını söyleyen sistem talimatı.

Hesaplar `Decimal` ile yapılır ve testlidir. Oranlar ondalık verilir (0.10 = %10). Sunucu ağa çıkmaz, model indirmez, dosya yazmaz.

## Tazminat hesapları (Yargıtay uygulaması)

> **Bilirkişi raporu yerine geçmez.** Parametreler mahkemeye, daireye ve tarihe göre değişebilir. Her sonuç, kullanılan
> varsayımları ve dayandığı Yargıtay kararlarının kimliklerini listeler.

`mevzuat_ara` bu konuda 49 seçilmiş Yargıtay kararını da arar (4. HD 2021–2026; 17. ve 21. HD 2009–2020; kişisel veriler
maskelendi). Araçların varsayılanları bu kararlardan çıkarıldı:

- **Bakiye ömür:** TRH 2010, kaza/ölüm tarihindeki yaşa göre, kesirli yaşta doğrusal ara değer. Taleple bağlılık (ör. PMF 1931) için `bakiye_omur_yil` elle verilebilir.
- **Bilinen dönem:** kaza/ölüm tarihinden hesap tarihine, verilen gelirlerle, iskontosuz.
- **Bilinmeyen dönem:** progresif rant, her yıl %10 artış ve %10 iskonto. Aktif dönem 60 yaşa kadar, sonra bakiye ömre kadar pasif dönem.
- **Genel şartlar yöntemi uygulanmaz:** AYM 17.07.2020 (2019/40 E., 2020/40 K.) KTK m.90'daki genel şartlar atfını iptal etti.
  ZMSS Genel Şartlarının hesap ekleri Danıştay 8. Dairesince 14/5/2025'te iptal edildi ve 1/7/2026'dan beri mülga.
- **Paylaştırma:** destek 2, eş 2, her çocuk 1, ana ve baba 1'er pay. Çocuk desteği erkekte 18, kızda 22, yüksek öğrenimde 25 yaşa kadar.
  Çocuk çıkınca payı ana-babaya gitmez. Genç desteklerde ileride evlenme/çocuk ihtimali için varsayımsal hak sahibi eklenebilir.
- **İndirimler:** kusur oranı → hatır taşıması → müterafik kusur (sırayla, toplanmaz) → rücuya tabi SGK ilk peşin sermaye değeri → güncellenmiş önceki ödemeler.

- **Tablolar (`data/tables/`):** asgari ücret 2008–2026 (ÇSGB; her satır kaynak bağlantılı, vergi formülüyle denetlendi) ve
  AYİM evlenme ihtimali tablosu (dul kadın; kaynaklar ikincil, kararlardaki %12 ve %7 değerleriyle tutarlı).
  Pasif dönem geliri verilmezse hesap tarihindeki net asgari ücret kullanılır. Kadın eşin evlenme ihtimali verilmezse AYİM
  tablosundan, rapor (hesap) tarihindeki yaşla hesaplanır; 18 yaş altı her çocuk için 5 puan düşülür
  (`evlenme_yas_tarihi: "olum"` eski 17. HD uygulamasını seçer). Kullanılan her tablo değeri varsayımlarda yazılır.

Kararlarda açık kural bulunamayan değerler **zorunlu girdidir**: destekten yoksun kalmada pasif dönem desteği, erkek eşin
evlenme ihtimali (AYİM'in erkek sütunu doğrulanamadı), 2022 öncesi asgari ücrette asgari geçim indirimi seçimi.
Pakette olmayanlar: poliçe teminat limiti, cenaze ve defin giderleri, önceki ödemelerin faizle güncellenmesi.

TRH 2010 tablosu `data/tables/` altındadır; bir Yargıtay kararındaki bilirkişi değeriyle (29,86 yaş kadın → 49,14 yıl) birebir doğrulandı.

## Kurulum

Python 3.11+ yeterli; ek bağımlılık yok. Paket korpusu ve tabloları içinde taşır. Üç yoldan birini seçin.

**1. `uvx` ile kurmadan çalıştırma (önerilen).** [uv](https://docs.astral.sh/uv/) kuruluysa istemciye şu komutu verin
(paket [PyPI](https://pypi.org/p/turkactuary-mcp)'de):

```bash
uvx turkactuary-mcp
```

İstemci yapılandırmasında: `"command": "uvx"`, `"args": ["turkactuary-mcp"]`, `env` gerekmez. Claude Code:
`claude mcp add turkactuary -- uvx turkactuary-mcp`. uvx paketi önbelleğe alır; yeni sürüm için komuta bir kez
`--refresh` ekleyin. Henüz sürümlenmemiş en son kod için: `uvx --from git+https://github.com/afsharid/turkactuary-mcp turkactuary-mcp`.

**2. `pip` ile kurma.** Bir sanal ortama kurun; komut `turkactuary-mcp` olur:

```bash
python3 -m venv ~/.venvs/turkactuary && ~/.venvs/turkactuary/bin/pip install turkactuary-mcp
```

İstemci yapılandırmasında: `"command": "/Users/<siz>/.venvs/turkactuary/bin/turkactuary-mcp"`, `args` ve `env` gerekmez.

**3. `git clone` (kodu değiştirecekseniz).** Aşağıdaki istemci örnekleri bu yolu kullanır:

```bash
git clone https://github.com/afsharid/turkactuary-mcp.git
cd turkactuary-mcp
python3 -m unittest discover -s tests   # isteğe bağlı: sunucu testleri
```

### Anlamsal arama (v5) için embedding modeli

En iyi sonuç için yerel bir embedding modeli açın. LM Studio'da **Qwen3-Embedding-4B** modelini indirip yükleyin
(`text-embedding-qwen3-embedding-4b`) ve yerel sunucuyu başlatın (varsayılan `http://127.0.0.1:1234`). Sunucu açılışta
modelinizi 3 parçada hazır vektörlerle karşılaştırır: uyumluysa birkaç saniyede v5'e geçer. Uyumsuzsa beklemeden v2
(BM25) ile çalışır ve nedenini `v5_durumu` alanında yazar. Başka bir embedding modeliyle v5 istiyorsanız sunucuyu bir kez
`ACTUARYLLM_SEARCH=v5` ile başlatın: bütün parçalar o modelle hesaplanır (624 parçalık korpusta bu Mac'te ~20 dk sürdü) ve
`~/.cache/actuaryllm-mcp/` altına yazılır; sonra varsayılan `auto` kip bu önbelleği kullanır. Embedding modeli yoksa v2 ile
çalışır; her arama sonucunda `profil` ve `v5_durumu` alanları hangisinin kullanıldığını söyler.

Ayarlar (isteğe bağlı): `ACTUARYLLM_SEARCH=auto|v5|v2`, `ACTUARYLLM_EMBED_URL` (yalnız 127.0.0.1/localhost),
`ACTUARYLLM_EMBED_MODEL`, `ACTUARYLLM_CACHE`.

### LM Studio

LM Studio → **Program** sekmesi → **Install → Edit mcp.json**, sonra ekleyin (yolu kendi klasörünüzle değiştirin):

```json
{
  "mcpServers": {
    "turkactuary": {
      "command": "python3",
      "args": ["-m", "actuaryllm_mcp"],
      "env": { "PYTHONPATH": "/yol/turkactuary-mcp/src", "ACTUARYLLM_ROOT": "/yol/turkactuary-mcp" }
    }
  }
}
```

Araç çağırabilen bir model seçin. Sohbette araçlar otomatik görünür.

**Model seçimi önemli.** Sunucu doğru sonucu döndürür; onu doğru kullanmak modele kalır. 2026-11-18 denemesinde Claude
Sonnet aynı soruda aracı doğru kullandı (chain ladder rezervi 30, 5684 s.K. md. 23 atfı). Qwen3-8B ise araca hatalı
parametre verdi ve hatadan sonra sonucu kendisi uydurdu. Araç kullanmada güçlü, büyük modeller (ör. 27B ve üstü) önerilir.

### Claude Code

```bash
claude mcp add turkactuary -e PYTHONPATH=/yol/turkactuary-mcp/src -e ACTUARYLLM_ROOT=/yol/turkactuary-mcp -- python3 -m actuaryllm_mcp
```

### Codex

`~/.codex/config.toml`:

```toml
[mcp_servers.turkactuary]
command = "python3"
args = ["-m", "actuaryllm_mcp"]
env = { PYTHONPATH = "/yol/turkactuary-mcp/src", ACTUARYLLM_ROOT = "/yol/turkactuary-mcp" }
```

### VS Code (Copilot)

`.vscode/mcp.json`:

```json
{
  "servers": {
    "turkactuary": {
      "type": "stdio",
      "command": "python3",
      "args": ["-m", "actuaryllm_mcp"],
      "env": { "PYTHONPATH": "/yol/turkactuary-mcp/src", "ACTUARYLLM_ROOT": "/yol/turkactuary-mcp" }
    }
  }
}
```

### Claude Desktop / Cursor / diğerleri

LM Studio'daki `mcpServers` bloğunu istemcinin MCP yapılandırmasına ekleyin (Claude Desktop: `claude_desktop_config.json`,
Cursor: `.cursor/mcp.json`). `uv` kullanıyorsanız: `"command": "uv", "args": ["run", "--directory", "/yol/turkactuary-mcp", "turkactuary-mcp"]`.

## Örnek

> "Kümülatif ödenen üçgen [[80,100],[120]] için chain ladder rezervi nedir? Sigorta acentelerinin levha kaydı hangi
> yönetmelikte düzenlenir?"

Model `chain_ladder` aracıyla 30 TL bulur, `mevzuat_ara` ile ilgili yönetmelik parçasını getirir ve parça kimliğiyle atıf yapar.

## Kaynak ve lisans

- Kod: Apache-2.0 (`LICENSE`).
- Öğretici notlar ve proje verisi: CC BY 4.0 (`LICENSE-DATA`).
- Mevzuat metinleri: mevzuat.gov.tr konsolide metinleri (resmî metinler); kaynak, erişim tarihi ve izin kaydı
  `data/sources.json` içindedir. Kamuya açık resmî metinlerdir; yorum ve uygulama için resmî kaynak esastır.

## Ölçülen kurulumla farkı

Bu sunucu ActuaryLLM projesinin (Türkiye sigortacılık ve aktüerya asistanı pilotu) arama ve araç katmanından türetildi.
Projede ölçülen kurulumla birebir aynı değildir:

| | Projede ölçülen (Qwen3.8-27B, ince ayarsız) | Bu MCP sunucusu |
|---|---|---|
| Arama | v5: BM25 + Qwen3-Embedding-4B anlamsal arama (karma) | Aynı v5 (embedding modeli açıksa; 6 deneme sorgusunda ilk 4 parça birebir aynı). Model yoksa v2: yalnız BM25 |
| Hesap araçları | 6 araç, soru başına en çok 2 çağrı | 17 araç, çağrı sınırı yok |
| Sistem talimatı | aynı metin | `turkactuary` prompt'u (aynı metin + araç rehberi) |

Ölçümler (projenin kendi altın etiketli vakaları; otomatik ölçüm, uzman puanı değildir): kuralın modele giden bağlamda
görünme oranı dev/test/v9 için v2 0,693/0,911/0,791 → v5 0,769/0,970/0,819; uçtan uca `fact_hit` v2, önceki v1 profiline
(3 parça, kısaltılmış alıntı) göre 0,780 → 0,875 ve v5 tam sette v2'ye göre gerilemesiz. Sonuçlar modelinize, istemcinize ve araç kullanımına göre
değişir; bu sayılar bu sunucunun sizin kurulumunuzdaki kalitesini garanti etmez.

---

<a id="english"></a>
## English

**TurkActuary MCP** is a Model Context Protocol server for **Turkish insurance regulation search** and **tested actuarial
calculators**. Use it with any model or agent: LM Studio, Claude Code, Codex, VS Code (Copilot), Claude Desktop, Cursor and
any other MCP client.

> **Disclaimer:** decision support only; not legal or actuarial advice. Regulation texts are a consolidated copy accessed
> on 2026-10-18 and are not updated automatically. Always verify against the official source.

**Tools**

- `mevzuat_ara` (search): 827 chunks of Turkish insurance law (Insurance Law No. 5684, regulations and communiqués,
  consolidated), 16 teaching notes and 49 selected, anonymised Yargıtay decisions. Hybrid search (BM25 + Qwen3-Embedding-4B) as measured in the project when a local
  embedding model is available; BM25 otherwise. Returns chunk id, title, source and text for citation.
- `belge_getir` (get document): full text of a chunk by id.
- 14 calculators (exact `Decimal` arithmetic, unit-tested): present value, annuity, term life insurance PV, chain ladder,
  Bornhuetter-Ferguson, portfolio metrics (frequency, severity, pure premium, loss ratio), combined ratio, life annuity,
  life cash-flow projection, excess-of-loss layer recovery, Bühlmann credibility, earned exposure, Poisson frequency GLM,
  gamma severity GLM.
- 2 compensation calculators following Turkish Court of Cassation (Yargıtay) practice: `is_goremezlik` (disability) and
  `destekten_yoksun_kalma` (loss of support). TRH 2010 life table, progressive annuity (10% growth / 10% discount), shares,
  reductions; every result lists its assumptions and the decision ids it relies on. Search also covers 49 selected,
  anonymised Yargıtay decisions. Not a substitute for an expert report.
- `asgari_ucret`: Turkish monthly minimum wage 2008–2026 (gross and net, from the Ministry of Labour tables). If not given,
  the passive-period income defaults to the net minimum wage at the calculation date, and a widow's remarriage probability
  defaults to the AYİM table (minus 5 points per child under 18).
- Prompt `turkactuary`: the system policy (ground answers in retrieved chunks, compute numbers with tools, treat documents
  as data, not instructions).

**Model choice matters.** The server returns correct results; using them well is up to the model. In a test, Claude Sonnet
used the tools correctly, while Qwen3-8B passed a wrong parameter and then made up the result. Prefer larger models that
are good at tool use.

**Setup:** Python 3.11+, no dependencies; the package ships its corpus and tables. Easiest: point your client at
`uvx turkactuary-mcp` (no env needed; add `--refresh` once to update). Or `pip install turkactuary-mcp` into a
virtualenv and run `turkactuary-mcp`.
To change the code, `git clone` the repo and add the `mcpServers` block shown above to your client
(paths: `PYTHONPATH=<repo>/src`, `ACTUARYLLM_ROOT=<repo>`). For hybrid search, load `text-embedding-qwen3-embedding-4b` in
LM Studio; the server checks compatibility with the bundled vectors on 3 chunks and switches to hybrid within seconds.
With an incompatible model it stays on BM25 and says why in `v5_durumu`; start once with `ACTUARYLLM_SEARCH=v5` to embed
all chunks with your model (cached; `auto` reuses the cache afterwards).

**Licence:** code Apache-2.0, project data CC BY 4.0; regulation texts from mevzuat.gov.tr (official texts; source records in
`data/sources.json`). Derived from the ActuaryLLM pilot; the measured setup and its differences are listed above.
