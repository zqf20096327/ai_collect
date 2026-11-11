# turkish-humanizer

Türkçe metinleri yapay zeka izlerinden arındıran bir [Claude skill'i](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview).

*[English summary below](#english)*

## Neden?

İngilizce için yazılmış "humanizer" araçları *delve*, *crucial*, *tapestry* gibi sözcükleri avlar. Türkçede bunların neredeyse hiçbir karşılığı yok, çünkü Türkçede yapay zeka izi sözcükten çok **yapıda** görülür:

- Her cümle aynı dizilimde ve benzer uzunlukta.
- Bağlaç olarak hep "ve, ama, çünkü".
- Yüklemler hep "-mektedir, -maktadır".
- "Önemli bir rol oynamaktadır", "bu bağlamda", "günümüzde".
- Çeviri kokan kalıplar: "günün sonunda", "derinlemesine dalmak", "-e sahip olmak".
- İngilizce noktalama: cümle içinde uzun çizgi (—), "ve"den önce virgül, *25%*.

turkish-humanizer bu örüntüleri yakalar ve metni yeniden yazar. İsterseniz yeniden yazmadan yalnızca hangi örüntülerin nerede geçtiğini de raporlar. Bunu yaparken **anlamı, sayıları, terimleri ve özel isimleri olduğu gibi korur**, bilgi eklemez ve çıkarmaz. Akademik bir metin akademik kalır.

## Önce / sonra

> **Önce:** Teknolojinin hızla geliştiği günümüzde, yapay zeka birçok sektörü dönüştürmektedir. Bu bağlamda, söz konusu dönüşüm göz önünde bulundurulduğunda şirketlerin hazırlıklı olması gerekmektedir.
>
> **Sonra:** Yapay zeka birçok sektörü dönüştürüyor ve şirketlerin buna hazırlanması gerekiyor.

Altı metin türü için tam örnekler [`turkish-humanizer/examples/`](turkish-humanizer/examples/) klasöründe.

## Nasıl kullanılır?

Kullandığınız yapay zekaya göre aşağıdaki yollardan birini seçin. Hepsinin sonunda yapmanız gereken aynı: metninizi yapıştırıp **"insanlaştır"** demek.

| Kullandığınız araç | En kolay yol | Süre |
|---|---|---|
| **Claude** (claude.ai, masaüstü, mobil) | Skill olarak yükleyin | 2 dakika |
| **Claude Code** | Klasörü kopyalayın | 1 dakika |
| **ChatGPT** | Kısa talimatı yapıştırın ya da bir GPT oluşturun | 2-5 dakika |
| **Gemini** | Bir Gem oluşturun | 3 dakika |
| **Diğerleri** (Copilot, DeepSeek, Le Chat...) | Dosyayı sohbete yükleyin | 1 dakika |

> Menü adları uygulamaların güncellemeleriyle değişebilir. Aşağıdaki adımlar Kasım 2026 itibarıyla geçerlidir. Bulamadığınız bir menü olursa lütfen bir issue açın.

### Claude (claude.ai, masaüstü ve mobil uygulama)

Skill yalnızca Claude'da tam hâliyle çalışır: Claude ihtiyaç duydukça örüntü kataloğunu ve kural dosyalarını kendisi açar.

1. [`dist/turkish-humanizer.zip`](dist/turkish-humanizer.zip) dosyasını indirin. Bu sayfada dosyaya tıklayıp sağ üstteki indirme düğmesine basın. Zip'i **açmayın**.
2. claude.ai'de sol alttaki adınıza tıklayın, ardından **Ayarlar → Yetenekler (Capabilities)** bölümüne gidin.
3. **Skills** başlığı altında **Skill yükle (Upload skill)** düğmesine basıp zip dosyasını seçin.
4. Listede *turkish-humanizer* görününce açık olduğundan emin olun.

Artık herhangi bir sohbette şöyle yazabilirsiniz:

```
Bu metni insanlaştır:

(metniniz)
```

Skill'i bir kez yüklemeniz yeterli. Masaüstü ve mobil uygulamada da çalışır. Skills özelliği hesap türünüze göre açık ya da kapalı olabilir. Ayarlarda göremiyorsanız aşağıdaki "Diğerleri" yöntemini Claude'da da kullanabilirsiniz.

### Claude Code

```bash
git clone https://github.com/DevVettel/turkish-humanizer.git
cp -r turkish-humanizer/turkish-humanizer ~/.claude/skills/
```

Ardından Claude Code'da "şu dosyadaki metni insanlaştır: yazi.md" demeniz yeterli.

### ChatGPT

ChatGPT, Claude skill'lerini doğrudan yükleyemez. Ama aynı kuralları iki yolla verebilirsiniz.

**Yol 1: Kendi GPT'nizi oluşturun (önerilen, ücretli planlarda)**

1. ChatGPT'de sol menüden **GPT'ler → Oluştur** bölümüne gidin ve **Yapılandır (Configure)** sekmesini açın.
2. **Ad:** *Türkçe İnsanlaştırıcı*
3. **Talimatlar** kutusuna aşağıdaki [kısa talimatı](#kisa-talimat) yapıştırın.
4. **Bilgi (Knowledge)** bölümüne [`dist/turkish-humanizer-tek-dosya.md`](dist/turkish-humanizer-tek-dosya.md) dosyasını yükleyin. Bütün örüntü kataloğu ve TDK kuralları bu dosyada.
5. **Oluştur**'a basın. Metinlerinizi artık bu GPT ile konuşarak düzeltebilirsiniz.

**Yol 2: Hızlı ve ücretsiz**

Tek seferlik kullanım için [`dist/turkish-humanizer-tek-dosya.md`](dist/turkish-humanizer-tek-dosya.md) dosyasını sohbete sürükleyip şöyle yazın:

```
Bu dosyadaki kurallara göre aşağıdaki metni insanlaştır:

(metniniz)
```

> **Neden "Özel talimatlar" değil?** ChatGPT'nin *Kişiselleştirme → Özel talimatlar* alanına kısa talimatı yapıştırırsanız bütün sohbetlerinizi etkiler. Yalnızca metin düzeltmek için ChatGPT kullanıyorsanız bu da işe yarar.

### Gemini

1. [gemini.google.com](https://gemini.google.com)'da sol menüden **Gem yöneticisi → Yeni Gem** seçin.
2. **Ad:** *Türkçe İnsanlaştırıcı*
3. **Talimatlar** kutusuna aşağıdaki [kısa talimatı](#kisa-talimat) yapıştırın.
4. **Bilgi** bölümüne [`dist/turkish-humanizer-tek-dosya.md`](dist/turkish-humanizer-tek-dosya.md) dosyasını ekleyin ve kaydedin.

### Diğer yapay zeka araçları

Dosya yüklemeye izin veren her sohbet aracında (Microsoft Copilot, DeepSeek, Mistral Le Chat, Perplexity...) ChatGPT'deki "Yol 2"yi uygulayın: tek dosyayı sohbete ekleyin ve metninizi isteyin. Dosya yükleyemiyorsanız kısa talimatı mesajınızın başına yapıştırın.

<a id="kisa-talimat"></a>
### Kısa talimat

GPT, Gem ya da başka bir aracın talimat kutusuna yapıştırmak için (1.340 karakter, ChatGPT'nin 1.500 karakterlik sınırına sığar):

```text
Türkçe bir metni "insanlaştır", "doğallaştır" ya da "Türkçeleştir" dediğimde yapay zeka izlerini temizleyerek yeniden yaz.

Asla değiştirme: anlam, sayılar, tarihler, özel isimler, terimler, alıntılar. Bilgi, ayrıntı ya da örnek ekleme. Bilgi çıkarma. "olabilir" gibi temkinleri koru. Hitabı (siz/sen) ve registerı koru: akademik metin akademik kalsın.

Düzelt:
- Hep aynı uzunlukta, aynı dizilimde cümleler: bir kısmını birleştir (-ıp, -ınca, -an), bir kısmını kısalt.
- ve/ama/çünkü tekeli: bağlacı sil, virgül, nokta ya da zarf-fiil kullan.
- -mektedir/-maktadır yığılması (gündelik metinde -yor ya da geniş zaman).
- Klişeler: günümüzde, bu bağlamda, söz konusu, önemli bir rol oynamaktadır, büyük önem taşımaktadır, sonuç olarak.
- Çeviri kokusu: günün sonunda, derinlemesine dalmak, oyunun kurallarını değiştiren, -e sahip olmak.
- Cümle içinde uzun çizgi (—): virgül, iki nokta ya da yeni cümle kullan.
- Üçlü sıfat ve madde alışkanlığı, emoji ve ünlem bolluğu, gereksiz başlıklar.
- "Harika bir soru!", "Umarım yardımcı olur" gibi dolgular.
- TDK yazımı: de/da ve mi ayrı yazılır, "ve"den önce virgül konmaz, %25, 3,5.

Ölçülü ol: İyi cümlelere dokunma. Devrik ve eksiltili cümleyi yalnızca blog ve sosyal medyada, gerekiyorsa kullan.
Çıktı: yalnızca düzeltilmiş metin. Önsöz ve açıklama yazma. Değişiklik özetini ben istersem ver.
```

Aynı metin [`dist/kisa-talimat.txt`](dist/kisa-talimat.txt) dosyasında da var.

### Örnek istekler

| Ne istiyorsanız | Şöyle yazın |
|---|---|
| Yalnızca düzeltilmiş metin | "Bu metni insanlaştır: ..." |
| Neyin değiştiğini de görmek | "Doğallaştır, altına kısa bir değişiklik özeti ekle: ..." |
| Resmi tonun korunması | "Bu resmi bir yazı, resmiyetini bozmadan doğallaştır: ..." |
| İngilizce bir metni doğal Türkçeye | "Bunu Türkçeleştir: ..." |
| Yeniden yazım olmadan yalnızca inceleme | "Bunu yeniden yazma, nerelerinde iz var göster: ..." |
| Kendi üslubunuza yakın bir sonuç | "Şu benim yazdığım bir paragraf: ... Aşağıdaki metni buna yakın bir sesle doğallaştır: ..." |

### Bilmeniz gerekenler

- **Sonucu mutlaka okuyun.** Skill anlamı korumak için tasarlandı ve testlerde bunu başardı, ama yayımlamadan ya da göndermeden önce sayıları ve isimleri kontrol etmek sizin güvenceniz.
- **En iyi sonucu Claude'da verir.** Testler Claude ile yapıldı. Diğer araçlarda kurallar aynı, ama sonuçlar modelden modele değişebilir.
- **Bir şey ters giderse** (bir sayı değiştiyse, metne olmayan bir bilgi eklendiyse) lütfen [bir issue açın](../../issues/new/choose). Bu tür bildirimler projeyi en çok geliştiren katkılardır.

## Tarayıcı: `tara.py`

Skill ile birlikte küçük bir komut satırı aracı gelir. Katalogdaki örüntülerden düz metinde sayılabilenleri ve cümle uzunluğu dağılımını raporlar. Yalnızca Python'ın standart kitaplığını kullanır, kurulum gerektirmez.

```bash
python3 turkish-humanizer/scripts/tara.py yazi.md
python3 turkish-humanizer/scripts/tara.py yazi.md --register akademik   # gundelik | is | akademik
python3 turkish-humanizer/scripts/tara.py yazi.md --json
```

```
Register: gundelik · 11 cümle, 133 sözcük
Cümle uzunluğu: ortalama 12.1, en kısa 4, en uzun 24, değişim katsayısı 0.51, 14-22 bandında %27

DOL-01 · Açılış dolguları (1)
    satır 5: Umarım bu e-posta sizi iyi bulur. Bu e-postayı…
YAPI-04 · Gereksiz edilgen yapı (2)
    satır 7: …incelemeler sonucunda ekibimiz tarafından tespit edilmiştir…
```

İkinci işi, yeniden yazılmış bir metni kaynağıyla karşılaştırmaktır. Kaynaktaki sayıların, URL ve e-posta adreslerinin, özel adların yeni metinde bulunup bulunmadığına, "-ebilir", "bazı", "muhtemelen" gibi temkin ifadelerinin azalıp azalmadığına bakar. *25%* ile *%25* gibi biçim farklarını değer farkı saymaz.

```bash
python3 turkish-humanizer/scripts/tara.py yeni.md --kaynak eski.md
```

Üç şeyi bilmekte yarar var:

- **Yapay zeka dedektörü değildir.** Metni kimin yazdığını söylemez, puan vermez. İnsanlar da bu kalıplarla yazar.
- **Bulgular adaydır.** `--register akademik` ile "söz konusu", "bu bağlamda" gibi o türde olağan kalıplar ayrı listelenir, ama son kararı katalogdaki **Dokunma** satırı ve okuyan kişi verir.
- **Anlamı okuyamaz.** Karşılaştırma sözcük düzeyindedir. Bir sayının yerinde durması cümlenin aynı şeyi söylediğini göstermez.

## Depo yapısı

```
turkish-humanizer/          ← skill'in kendisi (kurulan klasör)
├── SKILL.md                ← tetikleyici ve çalışma adımları
├── references/
│   ├── ai-oruntuleri.md    ← örüntü kataloğu (katkıların ana adresi)
│   ├── cumle-turleri.md    ← cümle çeşitliliği araç kutusu
│   ├── baglaclar.md        ← bağlaç alternatifleri ve register etiketleri
│   └── noktalama.md        ← TDK'ya dayalı noktalama ve yazım denetimi
├── examples/               ← 6 metin türü için önce/sonra çiftleri
├── scripts/tara.py         ← örüntü tarayıcı ve kaynak karşılaştırma
└── evals/                  ← test vakaları
kaynaklar/                  ← ayrıntılı kaynak belgeler ve kaynakça
dist/                       ← kullanıma hazır dosyalar (zip, tek dosya, kısa talimat)
scripts/                    ← dist/ dosyalarını üreten script
tests/                      ← tara.py ve katalog tutarlılığı testleri
```

Skill dosyalarını değiştirdiyseniz `python3 scripts/tek-dosya-olustur.py` ile `dist/` klasörünü yeniden üretin. Testler `python3 -m unittest discover -s tests` ile çalışır.

## Katkı

En değerli katkı, **yeni bir yapay zeka örüntüsü** eklemektir. [`ai-oruntuleri.md`](turkish-humanizer/references/ai-oruntuleri.md) dosyasındaki her örüntü aynı şablonla yazılmış bağımsız bir bloktur. Yeni bir örüntü eklemek için bir bloğu kopyalamanız yeterli.

Skill'in bir metinde anlamı değiştirdiğini fark ettiyseniz bu da çok değerli: lütfen "Anlam kayması" şablonuyla bir issue açın.

Ayrıntılar için: [CONTRIBUTING.md](CONTRIBUTING.md)

## Doğrulama ve sınırlar

Noktalama ve yazım kuralları TDK *Yazım Kılavuzu* ve *Güncel Türkçe Sözlük* ile doğrulandı. Kılavuzda açık bir hükmü bulunmayan maddeler `kaynaklar/` dosyalarında **[DOĞRULANMADI]** etiketiyle işaretli. Bunları doğrulamak da iyi bir ilk katkı olur.

Bu skill bir üslup aracıdır, bir yapay zeka tespit aracını atlatma aracı değildir. Amaç, metni okuyan **insan** için daha iyi hale getirmektir.

## Lisans

[MIT](LICENSE)

---

<a id="english"></a>
## English

**turkish-humanizer** is a Claude skill that removes AI-writing patterns from Turkish text.

Existing humanizer skills target English tells like *delve* or *crucial*, which barely exist in Turkish. In Turkish, AI text shows itself through **structure**: uniform subject-object-verb sentences of equal length, a monopoly of *ve/ama/çünkü* (and/but/because), stacked *-mektedir* verb endings, calqued English idioms (*günün sonunda* = "at the end of the day"), and English punctuation habits (em dashes, Oxford commas, *25%*).

The skill rewrites the text while preserving meaning, numbers, terminology and proper nouns exactly, and it keeps the original register: academic text stays academic.

- **Install:** on claude.ai, upload `dist/turkish-humanizer.zip` under *Settings → Capabilities → Skills*. In Claude Code, copy the inner `turkish-humanizer/` folder to `~/.claude/skills/`. For ChatGPT, Gemini and other assistants, use `dist/turkish-humanizer-tek-dosya.md` (all rules in one file) as a knowledge file, or paste `dist/kisa-talimat.txt` as instructions.
- **Use:** give Claude Turkish text and say *"insanlaştır"*, *"doğallaştır"* or *"humanize this"*.
- **Audit only:** ask *"yeniden yazma, sadece izleri göster"* to get a report instead of a rewrite. `turkish-humanizer/scripts/tara.py` counts the catalog's countable patterns from the command line and, with `--kaynak`, checks that numbers, names, addresses and hedges survived a rewrite. It is not an AI detector.
- **Contribute:** the pattern catalog in `turkish-humanizer/references/ai-oruntuleri.md` uses one copy-paste template per pattern. See [CONTRIBUTING.md](CONTRIBUTING.md) (in Turkish). Issues and PRs in English are welcome too.

License: MIT.
