# Türkçe Humanizer

[![Paketi denetle](https://github.com/RizgarOzan/turkce-humanizer/actions/workflows/validate.yml/badge.svg)](https://github.com/RizgarOzan/turkce-humanizer/actions/workflows/validate.yml)
[![skills.sh installs](https://skills.sh/b/RizgarOzan/turkce-humanizer)](https://skills.sh/RizgarOzan/turkce-humanizer)

Türkçe Humanizer, yapay zekâ kokan Türkçe metni, ne dediğini değiştirmeden bir insanın yazmış gibi okunacak hâle getirir. Yalnızca Markdown olduğu için skill destekleyen her ajanla çalışır: Claude Code, Codex, OpenCode, Cursor, Claude Desktop.

[blader/humanizer](https://github.com/blader/humanizer)'ın Türkçe karşılığıdır. İngilizce kalıp listesini çevirmek yerine Türkçede gerçekten görülen kalıpları temel alır: "sadece X değil, aynı zamanda Y" makine çevirisi, -mektedir zinciri, her paragrafın başındaki "bu bağlamda", "önemli bir rol oynamaktadır" şişirmesi, Oxford virgülü sızması. İngilizce kılavuzdaki iki madde Türkçede kural olduğu için bilerek dışarıda bırakıldı: başlıkta büyük harf ve kıvrık tırnak.

*English: a Turkish-language port of Humanizer. It removes the AI-writing tells specific to Turkish prose (calqued "not only… but also", passive -mektedir chains, paragraph-opening connectors, Oxford comma leakage) while keeping every fact. Plain Markdown, works with any skill-capable agent.*

## Kurulum

Skills CLI ile:

```bash
npx skills add RizgarOzan/turkce-humanizer --global
```

`--global` olmadan yalnızca bulunduğun projeye kurulur. `--agent <ad>` ya da `--agent '*'` ile hangi ajanlara kurulacağını seç, sonra ajanın skill listesini yenile. Skill `/turkce-humanizer` komutuna cevap verir.

Claude Code 2.1.142 ve üstü eklenti olarak da kurabilir:

```text
/plugin marketplace add RizgarOzan/turkce-humanizer
/plugin install turkce-humanizer@turkce-humanizer
```

Eklenti `/turkce-humanizer:turkce-humanizer` komutuna cevap verir.

Claude Desktop'ta bu depoyu ZIP olarak indirip skill olarak yükle. Elle kurmak için `SKILL.md` dosyasını ajanın skill klasörüne kopyala (Claude Code: `~/.claude/skills/turkce-humanizer/SKILL.md`).

## Kullanım

Doğrudan çağır:

```
/turkce-humanizer

[metni buraya yapıştır]
```

Ya da düz cümleyle iste:

```
Bu metnin yapay zekâ kokusunu al: [metin]
```

Bir dosyayı yeniden yazdırmak için yolunu ver:

```
docs/duyuru.md dosyasındaki metni doğallaştır
```

### Kendi sesini eşleştir

Sonucun sana benzemesini istiyorsan bir örnek ekle:

```
/turkce-humanizer

Ses eşleştirmesi için kendi yazımdan bir örnek:
[kendi yazından 2-3 paragraf]

Şimdi bu metni doğallaştır:
[yapay zekâ metni]
```

Skill örneğin ritmini, sözcük seçimini, noktalamasını ve bilinçli tuhaflıklarını izler; sen uzun tire kullanıyorsan o da kullanır.

### Model olmadan tarama

`scripts/tara.py`, bir metinde kalıp listesindeki ifadeleri model çağırmadan bulur. Çıktı bir kanıt değil, bakılacak yerlerin listesidir:

```bash
python scripts/tara.py odev.md
```

## Nasıl çalışır

Dil modeli her adımda en olası devamı seçer; bu yüzden en geniş okur kitlesine uyan seçimi yapar. İnsan tek bir okur ve tek bir konu için yazar. Türkçede bunun üstüne iki katman biner: İngilizce kalıpların birebir çevirisi ve Türkçe akademik yazının kendi klişelerinin üst üste yığılması. Skill'in aradığı her belirti bu "en güvenli seçim"in bir biçimidir.

Skill bulduğu her belirtiyi en güçlüsünden başlayarak işaretler. Özgün yapıyı sabit saymadan bir taslak yazar, taslağı özgün iddialara, kişiye, zamana ve kalıplara karşı denetler, sonra son hâli yazar. Hiçbir şey uydurmaz: ad, sayı, tarih, alıntı ve atıf kaynaktan ya da yazardan gelmek zorundadır; eksikse uydurmak yerine sorar. Bir iddiayı zayıflatmak ya da güçlendirmek de hata sayılır; çıkardığı ya da değiştirdiği iddiayı sana açıkça söyler.

Metin yapıştırdığında önce son metni, altında en fazla beş maddelik bir "Neleri değiştirdim" listesi verir; taslağı ancak istersen gösterir. Dosya verdiğinde yalnızca düzyazıyı değiştirir, kod, veri, üstbilgi ve bağlantı hedeflerine dokunmaz ve üç satırlık bir özet yazar. Zaten insan yazısı olan metni yeniden yazmaz. Kişisel yazı yazarın görüşlerini ve tuhaflıklarını korur. Teknik ve referans metni yansız ve düz kalır.

### Ne kadar işe yarıyor

`evals/` altındaki 15 senaryoda (ödev, blog, tanıtım, README, e-posta, LinkedIn, makale özeti, TÜBİTAK özeti, ürün açıklaması, tez önsözü, basın bülteni, niyet mektubu, istem enjeksiyonu ve dokunulmaması gereken bir insan metni) aynı model skill'le ve skill'siz çalıştırıldı. Çıktılar A/B diye karıştırılıp hangisinin skill'li olduğunu bilmeyen bir model puanlayıcıya verildi.

| Tur | Karşılaştırma | Skill'li kazandı | Not |
|---|---|---|---|
| 1.1.0 adayı, tam set | 16 | 12 | eski on senaryonun dokuzu |
| 1.1.0, düzeltilen ve hiç görülmemiş senaryolar | 7 | 6 | yeni iki senaryoda dörtte üç |

Farkın çoğu sadakatte (iddialar korunuyor mu, uydurma var mı) ve talimata uymada çıktı: 10 üzerinden sadakat 8,7'ye 7,7-8,1, talimat 8,7-8,8'e 8,2-8,4. Doğallıkta iki taraf başa baş. Yani skill'in asıl kazancı, metni ne dediğini bozmadan temizlemesi. Tek model, tek puanlayıcı ve küçük bir set söz konusu; sayıları gösterge olarak oku.

## 25 kalıp

Kalıplar güç ve sıklığa göre numaralanmıştır. İlk beşi tek görüşte düzenlemeyi haklı çıkarır. *Tek başına zayıf* işaretli olanlar yalnızca aynı pasajda birkaç belirti buluşuyorsa sayılır; dikkatli bir yazar bunların herhangi birini bilerek yapabilir.

### A. Söylemek yerine sahnelemek

| # | Kalıp | Önce | Sonra |
|---|-------|------|-------|
| 1 | **Sadece X değil, aynı zamanda Y** | "Bu sadece bir oyun değil, aynı zamanda bir deneyim", "Bu, X anlamına gelmez. Y anlamına gelir." | Noktayı doğrudan söyle |
| 2 | **Tek satırlık kapanış ve dramatik parçalar** | "İşte bu her şeyi değiştirdi." her bölümün sonunda; "Önyargı yoktu. Nostalji yoktu." | Tekrarlayan kapanışı kes; parçaları somut bir iddiada birleştir |
| 3 | **Derin görünen sözler** | "İşin özünde mesele…", "Simetri güvenin dilidir" | Sözü somut iddiayla değiştir |
| 4 | **Noktaya gelmeden sahne kurmak** | "Günümüzde teknolojinin hızla gelişmesiyle…", "Bu yazıda … ele alınacaktır", "Hadi başlayalım" | Girişi kaldır, noktayı söyle |
| 5 | **Kimseyle tartışmak** | "Bu, X demek değil", "Akla ilk gelen yol … olurdu ama" | Ortada olmayan itirazı ya da sahte seçeneği kaldır; gerçek iddiayı koru |

### B. Kurala bağlı ritim

| # | Kalıp | Önce | Sonra |
|---|-------|------|-------|
| 6 | **Zorlama üçlemeler** | "yenilik, ilham ve içgörü"; üç örnek artı ders | Anlamın gerektirdiği kadar madde |
| 7 | **Aynı cümle başlangıçları** | "O fark etti… O fark etti… O yazdı…" | Cümleleri birleştir ya da özneyi değiştir |
| 8 | **Her bağlantı için uzun tire** (*tek başına zayıf*) | "kurumlar — insanlar değil — yine de —" | Nokta, virgül, iki nokta ya da parantez; örnek tire kullanıyorsa ona uy |
| 9 | **Yığılmış ihtiyat** (*tek başına zayıf*) | "bir ölçüde etkisi olabileceği kısmen söylenebilir" | Yalnızca kaynağın desteklediği ihtiyatı koru |
| 10 | **-mektedir zinciri ve öznesiz edilgen** (*tek başına zayıf*) | "kullanılmıştır… analiz edilmiştir… karşılaştırılmıştır… tartışılmaktadır" | Eylemi yapanı adlandır; "-yor", "-di", "var" |
| 11 | **Her paragrafın başında bağlaç** (*tek başına zayıf*) | "Bu bağlamda… Bununla birlikte… Öte yandan… Sonuç olarak…" | Bağlacı sil; ilişkiyi gerçekten adlandıranı koru |

### C. Şişirme ve ödünç otorite

| # | Kalıp | Önce | Sonra |
|---|-------|------|-------|
| 12 | **Aşırı kullanılan yapay zekâ sözcükleri** | "kapsamlı… dinamik… ekosistem… değer katarak… altını çizmektedir" | Düz sözcükler; SKILL.md'deki liste tek sözcük listesidir |
| 13 | **Şişirilmiş önem** | "önemli bir rol oynamaktadır", "dönüm noktası", "Geleceği parlak görünüyor" | Olguyu tut, önemi at; son somut olguyla bitir |
| 14 | **Belirsiz ilişki** | "yönetimiyle ilişkilendirilmektedir", "kapsamında" | Kaynağın verdiği ilişkiyi söyle |
| 15 | **Yüzeysel -arak/-erek kuyrukları** | "yansıtarak… sembolize ederek… gözler önüne sererek" | Yalnızca kaynağın desteklediğini koru |
| 16 | **Reklam dili ve çeviri kokusu** | "kalbinde yer alan", "eşsiz bir deneyim sunmaktadır", "dört müzeye ev sahipliği yapmaktadır" | Şeyin ne olduğunu söyle: "Dört müzesi var" |
| 17 | **Ödünç otorite** | "Uzmanlara göre…", "ulusal ve uluslararası basında yer almıştır" | Gerçek kaynağı ve ne dediğini yaz, ya da iddiayı kes |
| 18 | **"-dır", "var" ve "yapar"dan kaçmak** | "işlevi görmektedir… bünyesinde barındırmaktadır" | "-dır… var" |

### D. Kurala bağlı biçim

| # | Kalıp | Önce | Sonra |
|---|-------|------|-------|
| 19 | **Süs olarak kalın** | "**Performans:** Performans artırıldı" | Kalını kaldır; etiketli listeyi düzyazıya çevir |
| 20 | **Süslü başlıklar** | "🚀 Lansman Aşaması:", her bölüm arası yatay çizgi | Emoji, ok ve çizgileri kaldır (Türkçede başlıkta büyük harf kuraldır, belirti değil) |
| 21 | **İngilizce noktalama** (*tek başına zayıf*) | "1,500 kullanıcıyı, 3.5 saniyede, ve" | "1.500 kullanıcıyı 3,5 saniyede ve" |

### E. Sohbetten ve taslaktan kalanlar

| # | Kalıp | Önce | Sonra |
|---|-------|------|-------|
| 22 | **Sohbet kalıntısı** | "Harika bir soru!", "Umarım yardımcı olur!", "…ister misiniz?" | Sargıyı kaldır, içeriği koru |
| 23 | **Bilgi sınırı uyarıları ve tahminler** | "mevcut kaynaklarda belgelenmemiş olsa da 1990'larda kurulduğu düşünülmektedir" | Kaynağın ne göstermediğini söyle ya da cümleyi kes |
| 24 | **İlk cümlede tekrarlanan başlık** | "## Performans / Hız önemlidir." | Tekrarlayan cümleyi kaldır |
| 25 | **Önceki sürümü anlatmak** | "önceki yaklaşımın yerine eklendi" | Şu anki davranışı anlat |

## Katkı

Yeni bir kalıp, eksik bir belirti ifadesi ya da daha iyi bir örnek gördüysen katkı bir PR uzağında. Kurallar kısa: [CONTRIBUTING.md](CONTRIBUTING.md). Kalıbın kaynağı varsa [KAYNAKLAR.md](KAYNAKLAR.md)'ye eklenir.

## Sürüm geçmişi

- **1.1.0**: 15 senaryoluk değerlendirme seti (`evals/`) ve kör karşılaştırmayla altı tur. İddialar artık gücüyle korunur, çıkan ya da değişen iddia kullanıcıya söylenir; dolgu ile iddia ayrıldı, beklentideki şişirme ("önemli katkılar sağlaması beklenmektedir") dolgu sayılır. Yanıt biçimi: önce son metin, altında en fazla beş maddelik değişiklik listesi. Metindeki talimatlar uygulanmaz, bildirilir. Ödevde uzunluk ve yapı korunur, boşluk uydurmayla doldurulmaz. `tara.py`: Türkçe küçük harf (I/ı), ek toleranslı eşleşme, sözcük sınırı, kod blokları ve konuşma çizgisi hariç, zayıf kalıplar üçten azsa sayılmaz.
- **1.0.0**: İlk sürüm. 25 kalıp; Türkçeye özgü §1, §4, §10, §11, §16 ve §21; model gerektirmeyen `scripts/tara.py` tarayıcısı; örnekleri denetleyen `scripts/test-patterns.py`.

## Lisans

MIT. Kalıp çatısı [blader/humanizer](https://github.com/blader/humanizer)'dan (MIT, Siqi Chen) ve Vikipedi'nin ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) sayfasından türetilmiştir.
