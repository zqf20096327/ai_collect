# kalkan 🛡️

[![test](https://github.com/CelkMehmett/kalkan/actions/workflows/ci.yml/badge.svg)](https://github.com/CelkMehmett/kalkan/actions/workflows/ci.yml)
[![crates.io](https://img.shields.io/crates/v/kalkan.svg)](https://crates.io/crates/kalkan)
[![PyPI](https://img.shields.io/pypi/v/kalkan.svg)](https://pypi.org/project/kalkan/)
[![docs.rs](https://img.shields.io/docsrs/kalkan)](https://docs.rs/kalkan)
[![license](https://img.shields.io/badge/lisans-MIT%20OR%20Apache--2.0-blue.svg)](#katkı-ve-lisans)

**Türkçe kişisel verileri LLM'e gitmeden maskeleyen, cevapta geri yükleyen KVKK motoru.**
Rust ile yazıldı; aynı motor Rust'ta, Python'da (`pip install kalkan`) ve tarayıcıda (WebAssembly)
birebir aynı sonucu verir.

```text
Kullanıcı  : Ben Ayşe Kaya, TC 10000000146. İadeyi TR33 0006 1005 1978 6457 8413 26 hesabıma yapın.
LLM'e giden: Ben [AD_SOYAD_1], TC [TCKN_1]. İadeyi [IBAN_1] hesabıma yapın.
LLM cevabı : Merhaba [AD_SOYAD_1], iadeniz [IBAN_1] hesabına yapılacak.
Kullanıcıya: Merhaba Ayşe Kaya, iadeniz TR33 0006 1005 1978 6457 8413 26 hesabına yapılacak.
```

**Canlı demo:** `wasm/demo.html` (GitHub Pages'e otomatik yayınlanır, aşağıya bakın). Metni yazarsınız,
maskeleme tarayıcınızda olur; hiçbir veri sayfadan çıkmaz. Demo dış font, CDN veya analitik
yüklemez; tüm kaynaklar tek dosyanın içindedir.

## İçindekiler

- [Neden?](#neden)
- [Neler yapar?](#neler-yapar)
- [Kurulum](#kurulum)
- [Python](#python)
- [Rust](#rust)
- [Entegrasyonlar: OpenAI, LiteLLM, LangChain](#entegrasyonlar)
- [Tarayıcı (WebAssembly)](#tarayıcı-webassembly)
- [Stratejiler](#stratejiler)
- [Komut satırı](#komut-satırı)
- [API sözleşmesi](#api-sözleşmesi)
- [Ölçümler](#ölçümler)
- [Güvenlik modeli](#güvenlik-modeli)
- [Sınırlamalar](#sınırlamalar)
- [Test](#test)
- [Katkı ve lisans](#katkı-ve-lisans)

## Neden?

Şirketler ChatGPT, Claude veya Gemini kullanmak istiyor ama müşterinin TC kimlik numarasını,
IBAN'ını, telefonunu yurt dışındaki bir sunucuya göndermek KVKK açısından risk. `kalkan` bu
verileri istek çıkmadan önce yer tutucularla değiştirir, cevap gelince gerçek değerleri geri koyar.

kalkan bir ürün değil, **gömülebilir bir motor**: kendi ağ geçidinizin, Python servisinizin,
tarayıcı eklentinizin veya toplu veri temizleme işinizin içine koyarsınız.

## Neler yapar?

| | |
|---|---|
| **14 veri türü** | TCKN, VKN, IBAN, telefon, kart, e-posta, plaka, ad-soyad, adres, SGK sicil no, IP, doğum tarihi, pasaport, kuruma özel terimler |
| **Sağlama doğrulaması** | TCKN, VKN, IBAN (mod-97), kart (Luhn); tarih, fiyat, sipariş no, sürüm numarası yakalanmaz |
| **Geri yükleme** | Oturum kasası; aynı değerin farklı yazımları aynı token'ı alır |
| **Akış (streaming)** | Yer tutucu iki parçaya bölünse bile (`"[TC"` + `"KN_1]"`) doğru geri yükler |
| **Sahte ama geçerli** | `Synthetic` modda sağlaması tutan sahte TCKN/IBAN/kart, belgeleme bloklarından IP |
| **Sızıntı denetimi** | Modelin ürettiği yeni kişisel veriyi ve uydurduğu yer tutucuları yakalar |
| **Kuruma özel terimler** | Müşteri, proje, ürün adları; Türkçe büyük/küçük harf duyarsız (`IŞIK` ↔ `ışık`, `HOLDING` ↔ `holding`) |
| **Türkçe'ye duyarlı** | `Yılmaz'ın` → yalnızca ad maskelenir, `'ın` kalır |
| **Sıfır bağımlılık** | Çekirdek `unsafe` içermez; C ABI yalnızca `ffi` özelliğiyle açılır |

## Kurulum

| Hedef | Kurulum | Not |
|---|---|---|
| Rust | `cargo add kalkan` | MSRV 1.82; çekirdek bağımlılıksız |
| Python | `pip install kalkan` | CPython ≥ 3.9, abi3 tekerlekleri |
| CLI | `cargo install kalkan` | `mask`, `detect`, `audit`, `restore` |
| Tarayıcı | `wasm/build.sh` → `wasm/dist/index.html` | Tek dosyalık demo, derleme gerektirmez |

Kaynaktan çalıştırmak için:

```bash
git clone https://github.com/CelkMehmett/kalkan kalkan && cd kalkan
cargo test --workspace --exclude kalkan-py
```

### Tespit edilen türler

| Tür | Etiket | Nasıl? |
|---|---|---|
| T.C. Kimlik No | `TCKN` | İki sağlama hanesi; `11111111110` gibi sahte kalıplar elenir |
| Vergi Kimlik No | `VKN` | GİB sağlaması **ve** yakında "vergi/VKN" kelimesi |
| IBAN | `IBAN` | TR + 24 hane, mod-97; boşluklu veya bitişik |
| Telefon | `TELEFON` | Cep, sabit hat, 0850/0800; `+90`, `0090`, `(0532)`, `532.123.45.67` |
| Kart | `KART` | Luhn + kart ağı öneki |
| E-posta | `EPOSTA` | Yapısal kontrol |
| Plaka | `PLAKA` | İl kodu 01-81, harf/rakam kuralı; `12 TL 500` gibi birimler düşük güvenle |
| Ad-soyad | `AD_SOYAD` | Unvan (`Sayın`, `Prof. Dr.`), hitap (`Bey`, `Hanım`), form etiketi (`Ad Soyad:`), yaygın ad sözlüğü |
| IP | `IP` | IPv4 (oktet ≤ 255) ve IPv6; saat (`14:30:00`), MAC ve sürüm numaraları elenir |
| Doğum tarihi | `DOGUM_TARIHI` | `05.03.1990`, `1990-03-05`, `5 Mart 1990`; yalnızca "doğum" bağlamıyla, takvim doğrulamalı |
| Pasaport | `PASAPORT` | Harf + 7-8 hane, yalnızca "pasaport" bağlamıyla |
| Adres | `ADRES` | Önünde ad veya sayı olan `Mah.`, `Cad.`, `Sok.`, `Blv.` çapası; ardından `No:`, kat/daire, posta kodu, `İlçe/İl`. Tek başına cadde adı (`Bağdat Caddesi`) maskelenmez |
| SGK sicil no | `SGK` | 6-13 hane, yalnızca "SGK/SSK/Bağ-Kur" bağlamıyla; geçerli TCKN ise `TCKN` kalır |
| Özel terim | `OZEL` | Sizin verdiğiniz liste |

## Python

```bash
pip install kalkan
```

```python
import kalkan

k = kalkan.Kalkan(terms=["Proje Atlas"])
s = k.session()                       # her sohbet için bir oturum

istem = s.mask("Ayşe Kaya Hanım, TC 10000000146, Proje Atlas bütçesi")
# "[AD_SOYAD_1] Hanım, TC [TCKN_1], [OZEL_1] bütçesi"

cevap = llm(istem)
rapor = s.audit(cevap)                # model yeni kişisel veri üretti mi?
if not rapor:
    log.warning(rapor)
print(s.restore(cevap))

# Akış (streaming)
akis = s.stream()
for parca in llm_akisi(istem):
    gonder(akis.push(parca))
gonder(akis.finish())

# Toplu anonimleştirme: tüm çekirdeklerde, GIL serbest
temiz = kalkan.Kalkan(strategy="label").mask_batch(milyonlarca_kayit)
```

`detect()` sonuçlarındaki `start`/`end` karakter indeksidir: `metin[e.start:e.end]` doğrudan çalışır.
Kasa `s.vault` ile sözlük olarak alınır ve başka bir süreçte `import_vault` ile yüklenebilir.

## Rust

```rust
use kalkan::{Kalkan, Strategy};

let kalkan = Kalkan::builder()
    .strategy(Strategy::Token)
    .terms(["Proje Atlas"])
    .build();
let mut oturum = kalkan.session();

let istem = oturum.mask("Müşteri TC 10000000146, tel 0532 123 45 67");
// "Müşteri TC [TCKN_1], tel [TELEFON_1]"

let cevap = llm_cagir(&istem);
assert!(oturum.audit(&cevap).is_clean());
let kullaniciya = oturum.restore(&cevap);

// Akış: StreamRestorer oturumdan bağımsızdır, başka bir göreve taşınabilir.
let mut akis = oturum.stream();
for parca in llm_akisi { gonder(&akis.push(&parca)); }
gonder(&akis.finish());
```

Çalışan örnek: `cargo run --example llm_akisi`

## Entegrasyonlar

Hazır adaptörler istemi maskeler, cevabı (yer tutucu parçalar arasında bölünse bile akış dahil)
geri yükler; oturumları elle yönetmeniz gerekmez. Her çağrı kendi oturumunu alır, kasa süreç
belleğinde kalır.

**OpenAI biçimli mesajlar (bağımlılıksız)** — OpenAI SDK'sı veya herhangi bir `messages` listesi:

```python
from kalkan.messages import mask_messages

s = kalkan.Kalkan().session()
cevap = client.chat.completions.create(model="gpt-4o", messages=mask_messages(s, mesajlar))
print(s.restore(cevap.choices[0].message.content))
```

Çok parçalı içerik ve araç çağrısı argümanları da işlenir; argümanlar JSON olarak ayrıştırılır,
geri yüklenen değer JSON'u bozmaz.

**LiteLLM** (`pip install "kalkan[litellm]"`) — `litellm.completion`/`acompletion` yerine:

```python
from kalkan.integrations.litellm import completion

r = completion(model="gpt-4o", messages=[{"role": "user", "content": "TC 10000000146"}])
for parca in completion(model="gpt-4o", messages=..., stream=True): ...
```

veya ağ geçidinin arkasındaki tüm uygulamaları korumak için **LiteLLM Proxy guardrail'i**:

```yaml
guardrails:
  - guardrail_name: kalkan
    litellm_params:
      guardrail: kalkan.integrations.litellm.KalkanGuardrail
      mode: [pre_call, post_call]
      default_on: true
      # isteğe bağlı: strategy, terms, kinds, exclude, min_confidence
```

Kasa istek metadata'sına veya LiteLLM loglarına yazılmaz (yalnızca anlamsız bir kimlik).
Not: `--detailed_debug` açıkken proxy, guardrail'den önce gelen isteği kendisi loglar.

**LangChain** (`pip install "kalkan[langchain]"`) — her Runnable'ı veya sohbet modelini sarar:

```python
from kalkan.integrations.langchain import with_kalkan

model = with_kalkan(ChatOpenAI(model="gpt-4o"), on_leak=lambda rapor: log.warning(rapor))
zincir = prompt | model | StrOutputParser()
zincir.invoke({"soru": "Ben Ayşe Kaya, TC 10000000146 ..."})
```

`invoke`, `ainvoke`, `stream`, `astream` desteklenir; araç çağrısı argümanları da geri yüklenir.
Model yeni kişisel veri üretirse `on_leak` denetim raporuyla çağrılır.
LiteLLM 1.110 (SDK ve gerçek proxy) ve langchain-core 1.7 ile test edildi.

## Tarayıcı (WebAssembly)

```js
import { kalkanYukle } from "./kalkan.js";
const motor = await kalkanYukle("./kalkan.wasm");
const oturum = motor.oturum({ strateji: "token", terimler: ["Proje Atlas"] });
oturum.maskele("TC 10000000146");          // "TC [TCKN_1]"
oturum.tespit(metin);                      // konumlar JS dizgi indeksi (emoji dahil doğru)
const akis = oturum.akis();                // akış geri yükleyici
```

Derleme ve tek dosyalık demo: `./wasm/build.sh` → `wasm/dist/index.html`.
`.github/workflows/demo.yml` bunu her `main` push'unda yapıp GitHub Pages'e yayınlar
(Settings → Pages → Source: GitHub Actions).

## Stratejiler

| Strateji | `10000000146` → | Geri yüklenir mi? | Ne zaman? |
|---|---|---|---|
| `Token` (varsayılan) | `[TCKN_1]` | Evet | Genel kullanım |
| `Synthetic` | `91176921220` (geçerli sahte) | Evet | Biçim doğrulayan araç çağrıları, gerçekçi test verisi |
| `Partial` | `*********46` | Hayır | Loglar, ekran görüntüleri |
| `Label` | `[TCKN]` | Hayır | Eğitim verisi anonimleştirme |

## Komut satırı

```bash
cargo install --path .

kalkan detect < belge.txt
kalkan mask -s partial -t "Proje Atlas,Acme Holding" < belge.txt
kalkan mask -v kasa.tsv < istem.txt | llm-cli > cevap.txt
kalkan audit -v kasa.tsv < cevap.txt     # bulgu varsa çıkış kodu 1
kalkan restore -v kasa.tsv < cevap.txt
```

## API sözleşmesi

| Katman | `start`/`end` birimi | Kasa taşıma |
|---|---|---|
| Rust (`Match.span`), CLI (`detect --json`) | **bayt** (her zaman UTF-8 sınırı) | `Session::vault` / `import_vault` |
| Python (`Entity.start/end`) | **karakter** (Python dilimiyle uyumlu) | `session.vault` sözlüğü |
| WASM/JS (`tespit()`) | **UTF-16 kod birimi** (`String.slice` ile uyumlu) | `kasa()` nesnesi |

Üç birim birbirine karıştırılmamalı: Rust'ta `&metin[m.span]` çalışır, Python'da
`metin[e.start:e.end]`, JS'te `metin.slice(e.start, e.end)` çalışır. Bayt konumlarını
doğrudan JS/Python dizgisine vermeyin.

Oturum (`Session`) kasası **tek kullanımlıktır**: her sohbet/istek için yeni bir
oturum açın. Aynı değerin farklı yazımları aynı yer tutucuyu alır ve ilk görülen
yazımla geri yüklenir. `audit` ham LLM cevabında çağrılmalı, `restore`/`stream`
ise ondan sonra.

## Ölçümler

5 MB'lık, 11.617 mesajlık Türkçe müşteri destek derlemi (`bench/gen_corpus.py` ile üretilir, her
mesajın doğru etiketleri bilinir). Karşılaştırma: [kvkk-pii](https://pypi.org/project/kvkk-pii/)
**yalnızca regex katmanı** ile (model yok; adil kıyas için kişi adı kuralı eklendi).
Ortam: 2 çekirdekli Intel Xeon 2.1 GHz sanal makine. kalkan v0.2'nin 12 türü açık (v0.3'te eklenen adres
ve SGK dedektörleri tespit süresini yaklaşık %14 artırır).
**v0.4, tespitte v0.3.1'den yaklaşık 2 kat yavaştır** (aynı makinede ölçüldü: 5,8 → 11,9 µs/mesaj);
büyüyen ad sözlükleri ve ad yayılım geçişi, isabet karşılığında süre harcar. Aşağıdaki tablo v0.2 ile
ölçülmüştür ve özgün sanal makinede yeniden çalıştırılmamıştır.

| | kalkan | kvkk-pii (regex) |
|---|---|---|
| Tespit, Rust'tan | **8 µs/mesaj** | 105 µs/mesaj |
| Maskele, Python'dan (tek çekirdek) | **12 µs/mesaj** | 104 µs/mesaj |
| Maskele, Python `mask_batch` (2 çekirdek) | **8 µs/mesaj** | — |
| İsabet (recall) | 100% | 79% |
| Kesinlik (precision) | 100% | 99,8% |

Doğruluk farkının ana kaynakları: boşluklu IBAN'lar (rakip %30 yakalıyor ve IBAN'ın ortasındaki
16 haneyi bazen kart sanıyor) ve unvansız adlar (`Merhaba, ben Emre Yılmaz`).

```bash
python3 bench/gen_corpus.py corpus.txt 5
cargo run --release --example bench -- corpus.txt kalkan.jsonl
pip install kvkk-pii && python3 bench/karsilastir.py corpus.txt kalkan.jsonl
python3 bench/python_hiz.py corpus.txt
```

> ⚠️ **Bu sayıları doğru okuyun.** Derlemi ben ürettim; şablonlar sınırlı ve adlar kalkan'ın
> sözlüğündeki yaygın adlardan seçildi. Bu yüzden %100 isabet, gerçek dünya isabeti değildir.
> Hız karşılaştırması ise sağlamdır: iki kütüphane aynı metni işliyor. kvkk-pii'nin NER ve
> GLiNER katmanları (adres, sağlık verisi gibi özel nitelikli veriler) bu kıyasta yoktur;
> o katmanlar kalkan'ın kapsamadığı şeyleri bulur. Sohbet uygulamasında LLM'in cevabı saniyeler
> sürdüğü için hız farkı asıl olarak **toplu işlerde** (log, çağrı kaydı, eğitim verisi temizleme) önemlidir.

## Güvenlik modeli

kalkan, veriyi **gönderimden önce** yerel olarak maskeler; kasa yalnızca sizin
sürecinizde durur. Bu, KVKK açısından "veri yurt dışına gitmedi" iddiasını
**destekleyen** bir araçtır, tek başına yasal uyumluluk garantisi değildir.

- Gerçek değerler yalnızca `Session` kasasında tutulur; kasayı diske yazmak
  (`--vault`, `vault`) açıkça sizin tercihinizdir ve dosya izinlerini siz yönetin.
- `Synthetic` modundaki üretim **kriptografik değildir**; `secret` değerini
  gizli tutun ve üretilen sahte değerleri gerçek sanıp loglamayın.
- `audit` bulguları engellemez, **raporlar**: üretimde bulgu varsa cevabı
  kullanıcıya göstermeden önce karar verin (CLI `audit` bu durumda çıkış kodu 1 döner).
- Tespit edilemeyen bir veri maskelenemez; tek başına `%100` güven varsaymayın.
  Kritik akışlarda kalkan'ı bir NER katmanı ve çıkış filtresiyle birlikte kullanın.
- FFI çıktı tamponu süreç genelindedir: eşzamanlı çağrılarda yalnızca son
  tamamlanan çağrının çıktısı okunmalıdır.

Güvenlik açığı bildirimi için [SECURITY.md](SECURITY.md) dosyasına bakın.

## Sınırlamalar

> **Önemli:** kalkan bir yardımcı araçtır, hukuki uyum garantisi değildir. Tespit %100 değildir;
> kalkan kullanmak tek başına KVKK veya GDPR uyumu sağlamaz. Hassas akışlarda çıktıyı `audit` ile
> denetleyin ve kendi hukuki değerlendirmenizi yapın. Yazılım lisansta belirtildiği gibi "olduğu gibi",
> hiçbir garanti olmaksızın sunulur.

- **Adlar sezgisel.** Unvan, hitap, form etiketi veya sözlükteki bir ad + soyad yoksa ad kaçabilir
  (ör. `Gülizar Tunç geldi`). Serbest metinde yüksek isabet için bir NER modeliyle birlikte kullanın.
- **Adresler sezgisel.** `Mah./Cad./Sok./Blv.` çapası olmayan adresler (ör. `Kadıköy'de oturuyorum`,
  köy adresleri) kaçar. SGK numarasının sağlaması yoktur, bağlam kelimesi gerekir.
- **Özel nitelikli veriler (sağlık, din vb.) yok.**
- `Synthetic` modda model sahte değeri yeniden biçimlendirirse (ör. boşlukları silerse) geri yükleme
  o değeri tanımaz. Kritik akışlarda `Token` kullanın.
- Aynı değerin farklı yazımları (`0532 123 45 67` / `+905321234567`, `ACME` / `Acme`) bilerek aynı
  token'ı alır ve ilk görülen yazımla geri yüklenir.
- Sentetik üretim kriptografik değildir; sahte değer gerçek değer hakkında bilgi taşımaz ama
  `secret` değerini gizli tutun. Çok sayıda özel terimde (yüzlerce) tarama doğrusal yavaşlar.

## Test

```bash
cargo test --workspace --exclude kalkan-py   # 18 birim + 35 entegrasyon + 4 doctest
cargo test --features ffi --lib              # + 3 C ABI testi
cd python && maturin develop && pytest       # 12 test
cargo build --release --features ffi && cd wasm && bun install && bun test   # 9 test
```

> Ortamda `rustdoc` kütüphaneleri eksikse doctest'ler atlanabilir:
> `cargo test --lib --tests`. CI tüm testleri çalıştırır.

- **Fuzz:** 20.000 rastgele girdide panik yok, aralıklar UTF-8 sınırında ve çakışmasız, `restore(mask(x)) == x`.
- **Akış:** Cevap her olası bayt noktasından ve 1-12 karakterlik parçalara bölünerek doğrulanır;
  JS tarafında emoji (UTF-16 vekil çifti) ortasından bölme dahil.
- **JS sarmalayıcı ve demo sayfası:** WASM yerine aynı C ABI yerel kütüphane olarak `bun:ffi` ile
  yüklenir; demo sayfası happy-dom içinde gerçek motorla çalıştırılıp HTML enjeksiyonu dahil test edilir.
- **CI:** `.github/workflows/ci.yml` üç dilin testlerini her push'ta çalıştırır;
  `wheels.yml` etiket atıldığında Linux/macOS/Windows tekerleklerini PyPI'ye yükler.

## Katkı ve lisans

Katkı kuralları [CONTRIBUTING.md](CONTRIBUTING.md), sürüm geçmişi
[CHANGELOG.md](CHANGELOG.md), güvenlik bildirimleri [SECURITY.md](SECURITY.md)
dosyasında. Yayın öncesi kontrol listesi de CONTRIBUTING.md içinde.

MIT veya Apache-2.0, size hangisi uygunsa. Lisans metinleri:
[LICENSE-MIT](LICENSE-MIT), [LICENSE-APACHE](LICENSE-APACHE).
