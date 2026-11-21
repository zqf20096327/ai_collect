<p align="center">
  <img src="docs/gorsel/kapak.png" width="830" alt="Short Motoru (claude-shorts-editor): your raw footage in, a vertical Short out. An editor, not a video generator.">
</p>

**Short Motoru is an editor, not a video generator.** You bring the raw footage (your own game recording, or a stream you are allowed to clip) and tell your own Claude Code agent in the chat what you want. The agent picks the moment and writes the edit as code; ffmpeg, HyperFrames and Whisper render a vertical Short or clip on your own PC.
It needs your own Claude subscription, takes about 25–30 minutes per video, and the edit quality is a first version: the agent looks at frames and measurements, it cannot hear the sound or watch the motion. Tested on two Windows PCs (Windows 10 and Windows 11).

<p align="center">
  <img src="docs/gorsel/demo.gif" width="720" alt="Left: a 16.5-second horizontal recording with a bar marking the seven parts used; the marker jumps to the source moment each part comes from. Right: the 12.6-second vertical Short cut from it, with the spoken words on screen.">
</p>
<p align="center"><sub>A real job run with this repo on the author's own footage. The bar shows the seven parts of the recording that were used; the Short does not follow the recording's order.</sub></p>

<p align="center">
  <img src="docs/gorsel/nasil-calisir.png" width="830" alt="How it works in three steps: 1. say what you want in the chat, 2. Claude edits in five stages (transcribe, pick the moments, edit as code, technical check, ready), 3. you get the video and one question whose answer goes into your style notebook.">
</p>

A read-only watch page shows the job in progress, the finished videos and the style notebook: what you said you liked, kept in your own words as hints for the next video. The page, the agent's messages and the docs are in Turkish. Speech in another language can be transcribed too (`--dil en`, or `--dil auto`); that was tried on one 2-minute English recording only, and the moment finder's word signals are tuned for Turkish.

<p align="center">
  <img src="docs/gorsel/izleme-sayfasi.png" width="830" alt="The watch page: a clip job at the edit stage (3 of 5), the latest finished Short with the thing the agent tried on purpose, and a style notebook with five entries.">
</p>
<p align="center"><sub>The finished Short is the real job above; the job in progress and the notebook lines are sample data.</sub></p>

**Türkçe belgeler aşağıda.**

---

# Short motoru

Short motoru video üreten bir yapay zekâ değil, bir kurgucudur: sen ham görüntüyü verirsin (kendi oyun kaydın, kullanma iznin olan bir yayın kaydı, istersen kendi sesin). Senin Claude Code ajanın kayıttaki aday anlardan seçer ve kurguyu kod olarak yazar; bilgisayarındaki ffmpeg ve HyperFrames o kodu dikey bir videoya (klip ya da Short) çevirir. Paylaşmadan önce izleyip kararı sen verirsin. Ajan için Claude aboneliği gerekir.

Yapan: Furkan Cavlak (yapay zekâ üzerine Türkçe YouTube kanalı).

## Ne değildir
- **Görüntü üretmez.** Videodaki her kare senin verdiğin kayıttan gelir. Kaydın yoksa video da yok.
- **Bir video zaman alır.** Bir video ajanın yaklaşık 25–30 dakikasını alır (denemelerde bir iş 12 ile 38 dakika arası sürdü; kısa sürenler düz çıktı). O sırada Claude Code sohbetin açık kalır. Uzun bir kayıtta buna konuşmayı yazıya dökme süresi eklenir (aşağıda "Yazıya dökme ne kadar sürer").
- **Kendi Claude aboneliğin gerekir.** Deponun kendisi açık kaynaktır (MIT), ama işi senin Claude Code'un yapar ve her video aboneliğinin kullanım hakkından harcar; ne kadar harcadığını ölçmedik. Motor da izleme sayfası da Claude'u hiçbir zaman kendisi başlatmaz.
- **Tarzını öğrendiği ölçülmedi.** Tarz defteri yalnız söylediklerini hatırlar ve ajana ipucu olarak verir; videoların zamanla senin tarzına oturduğunu ölçmedik.
- **İki Windows bilgisayarda denendi:** Windows 10 (Ryzen 5 7500F, RTX 4060 Ti 16 GB, 32 GB RAM) ve ikinci bir Windows 11 (Ryzen 5 7500F, RTX 4060, 16 GB RAM; depo GitHub'dan indirilip kurulum rehberiyle baştan kuruldu). Mac ve Linux'ta denenmedi. Ekran kartı yalnız konuşmayı yazıya dökmeyi hızlandırır, o da ek kütüphaneler kuruluysa; motorun geri kalanı onsuz da çalışır.

## Gizlilik: ne bilgisayarında kalır, ne Claude'a gider
- **Video dosyan bilgisayarından çıkmaz.** Kesme, yazıya dökme (yerel Whisper) ve videoya çevirme senin bilgisayarında yapılır.
- **Ama ajanın baktığı kareler ve yazıya dökülen konuşma Claude sohbetine (Anthropic'e) gider.** Ajan kurguyu ancak kareleri ve konuşmanın yazısını görerek yapabilir. Çalıştırdığı komutların çıktıları (dosya adları ve yolları dahil) ve tarz defterindeki notlar da aynı sohbete girer.
- İzleme sayfası yalnız bu bilgisayarda açılır (`127.0.0.1`), hesap istemez, internete çıkmaz.
- HyperFrames (kurguyu videoya çeviren program) varsayılan olarak anonim kullanım verisi gönderir; kurulumda ajan bunu kapatmak isteyip istemediğini sorar.

## Üç katman
1. **Motor:** her video için bir iş klasörü ve bir izleme sayfası (ilerleme, çıkan videolar, tarz defteri). Uzun kayıtta sesin, söylenenlerin ve sohbetin hızlandığı yerlerden aday anları bulur, konuşmayı yerel Whisper ile yazıya döker, yayıncı kamerasının yerini önerir, bitmiş videoyu teknik olarak denetler.
2. **Alet çantası** (`alet/`): kare kâğıdı çıkarma, zaman haritası, çekim kesme, boş sahne açma, kodla ses, teknik kontrol. Hangisi ne yapar: `alet/ALETLER.md`.
3. **Beyin:** senin kendi ajanın. Sade klipte hazır bir düz kesim kalıbı çalışır. Editli klipte ve Short'larda hazır şablon yoktur; ajan kurguyu klipte olana bakıp kendisi tasarlar. Denenen modeller: Claude Opus 5.5 ve Claude Fable 5.2; başka modelde sonuç değişebilir. Ajanın izlediği adımlar: `panel/AJAN-TALIMATI.md`.

Her şeyi kendi Claude Code sohbetinden istersin; iş orada, senin gözünün önünde yapılır.

## Kurulum (üç adım)
Kurulumun çoğunu kendi Claude Code'un yapar. Sen her indirmeyi onaylarsın, Windows'un "değişikliğe izin ver" penceresi çıkarsa "Evet"e sen basarsın, ajan isterse Claude Code'u kapatıp yeniden açarsın.
1. **Claude Code'u kur:** claude.com/claude-code adresindeki adımları izle (Claude aboneliği gerekir).
2. **Bu klasörü indir ve Claude Code'da aç:** GitHub'da "Code → Download ZIP" ile indirip bir klasöre çıkar (ya da klonla), Claude Code'u o klasörde başlat.
3. **"bu depoyu kur" yaz** ve sorularına cevap ver. Ajan neyin eksik olduğuna bakar; her indirmeden önce ne olduğunu ve boyutunu söyleyip onayını ister (zorunluların hepsi diskte ~3,4 GB, en büyüğü 1,6 GB'lık yazıya dökme modeli; ~12 Mbit'lik bir hatta yalnız o model 15–20 dakika sürer). Sonunda görüntü gerektirmeyen bir deneme yapar ve her parçanın sonucunu sade Türkçe söyler.

Ajanın izlediği yordam `KURULUM-AJAN.md`, genel kuralları `CLAUDE.md`. `AGENTS.md` aynı metnin başka kodlama ajanları için kopyasıdır (başka ajanlarla denenmedi). Neyin kurulu olduğunu kendin görmek istersen: `py -3 kur_kontrol.py`.

### Gerekenler (bilgi için)
| Gereken | Ne için | Denenen sürüm |
|---|---|---|
| Python 3.11 ya da üstü | motorun kendisi | 3.14.5 |
| numpy, Pillow, scipy, opencv-python, faster-whisper | görüntü, ses, kamera bulma, yazıya dökme | `requirements.txt` |
| Node.js 22 ya da üstü | iş açma, izleme sayfası ve HyperFrames (22 ister) | 24.15.0 |
| ffmpeg ve ffprobe | bütün video işleri | 8.1.1 |
| HyperFrames ve onun Chrome'u | kurgu sahnesini videoya çevirir | 0.8.140 (Chrome 152.0.7977.30) |
| Whisper modeli `large-v3-turbo` (~1,6 GB) | konuşmayı yazıya dökme | — |
| Claude Code | işi yapan ajan | — |
| İsteğe bağlı: ekran kartı kütüphaneleri (~1,5 GB, yalnız NVIDIA kartta) | uzun kaydı yazıya dökmeyi hızlandırır | CUDA 12 cuBLAS + cuDNN 9 |

Yazı tipleri: `kod/font/Anton.ttf` klasörde geliyor; diğerleri Windows'un kendi yazı tipleri. İsteğe bağlı: Windows'un Türkçe sesi (ses vermeden metin yazarsan deneme sesi için).
Disk: HyperFrames kendi Chrome'unu ve yazı tiplerini kullanıcı klasöründeki `.cache/hyperframes` altında ortak tutar (denenen bilgisayarda ~640 MB); iş başına ayrı bir kare önbelleği oluşmaz. Her iş klasörü de yer tutar: denemelerde iş başına 150–330 MB (10 dakikalık kayıt ve kısa Short'larla; uzun işte artar). Ajan bir şey silmeden önce sana sorar.

### Yazıya dökme ne kadar sürer
Klip işinde motor önce bütün kaydın konuşmasını yazıya döker. Bu süre ajanın kurgu süresine eklenir.

| Durum | 10 dakikalık kayıt | 1 saatlik kayıt | 3 saatlik yayın |
|---|---|---|---|
| Ekran kartı kütüphaneleri var (RTX 4060 Ti) | 22–36 saniye | 108 saniye (~2 dk) | ~5,5 dakika (hesap) |
| Kütüphaneler yok, işlemci çalışır (Ryzen 5 7500F) | 157 saniye (bilgisayar o sırada başka iş de yapıyordu) | 649 saniye (~11 dk) | ~32 dakika (hesap) |

- **NVIDIA ekran kartın olsa bile bu kütüphaneler (~1,5 GB, isteğe bağlı) bulunamazsa yazıya dökme işlemcide çalışır ve uzun kayıt uzun sürer:** her saatlik kayıt için ~11 dakika. Kurulum kontrolü bu hâlde de "hazır" der, ama ekran kartının kullanılmayacağını ayrıca yazar; iş açılırken de cihaz ve tahmini süre yazılır. Kurulumda ajan kartını kendisi tanır ve bu dosyaları yalnız NVIDIA kartta, yine sorarak önerir.
- Kısa seslendirmeli Short'ta fark etmez (5 saniyelik cümle işlemcide ~6 saniye).
- Emin olmak için ajana sor: "Yazıya dökme ekran kartında mı çalışıyor?" Uzun bir kayıt verdiğinde ajan başlamadan önce ne kadar bekleyeceğini söyler.
- Denediğimiz en uzun kayıt 1 saatti; 3 saatlik süre ondan hesaplandı, denenmedi.

## Kullanım
1. **Bu klasörü Claude Code'da aç.**
2. **Ne istediğini söyle.** Örnekler:
   - "Şu videodan 3 klip çıkar: C:\Videolar\yayin.mp4"
   - "Şu metinle bir Liste Short'u yap, videolar C:\Videolar\gta klasöründe: …"
   - "Devam et" (sırada bekleyen işi sürdürür)
   - "İşe devam et" ya da "düzelt ve yeniden dene" (izleme sayfası bir iş takılınca ya da son kontrolden geçmeyince sana bunu söyletir)

Ajan gerekirse bir-iki şey sorar (kaç klip, Sade mi Editli mi, Short'ta sesin ya da metnin), işi açar, kurar, son kontrolden geçirir, videoyu bilgisayarının oynatıcısında açmayı dener (açılmazsa dosyanın yolunu verir) ve tek bir soru sorar. Altyazıyı sormaz: klipler altyazılı gelir; istemiyorsan "altyazısız" de. Komut çalıştırmak için izin istediğinde ne yaptığını okuyup onayla. Klip'te kayıt kopyalanmaz, olduğu yerden okunur; Short'ta verdiğin videolar iş klasörüne kopyalanır (500 MB'tan büyük dosya kopyalanmaz).

İlerlemeyi, çıkan videoları ve tarz defterini görmek istersen "paneli aç" de: izleme sayfası tarayıcıda `http://127.0.0.1:4317` adresinde açılır (Windows'ta `Paneli-ac.cmd` da olur; kapatmak için `Paneli-kapat.cmd`). Sayfa yalnız gösterir; iş açmaz, soru sormaz. İşler `panel/isler/<iş>/` altında durur. Motor kaynak videona ve kendi yazmadığı dosyalara dokunmaz; yalnız kendi ürettiği ara dosyaları yeniler.

## İş türleri
**Klip:** uzun bir yayından ya da oyun kaydından dikey klipler. Kaç klip istediğini sen seçersin; istersen anları kendin verirsin (`12:30-13:05` ya da `12:30`).
- *Sade:* düz kesim; kamera varsa üstte, oyun altta. Varsayılan; Editli'den kısa sürer.
- *Editli:* ajan klibe özel bir kurgu tasarlar (ne gerekiyorsa: hız, yazı, geçiş, ses). Daha uzun sürer.

**Short:** senin sesin ve oyun ya da fragman görüntüsü.
- *Tek bilgi:* tek bir bilgi, tek sahne.
- *Liste:* "bilmen gereken N şey"; her madde ayrı çekim.
- *Karşılaştırma:* iki şeyi (iki oyun, iki sürüm) karşılaştırır; her farkın iki tarafı da gösterilir.

## Tarz defteri
Her videodan sonra ajan tek bir soru sorar ("En çok neyi beğendin?"); üç videoda bir ikinci bir soru gelebilir. Cevabını senin sözünle `tarzim/` klasörüne yazar. Bu klasör GitHub'a gitmez; ama ajan okuduğu için notlar Claude sohbetine girer.
Aynı şeyi üç ayrı videoda söylersen sana sorar; "evet" dersen kalıcı tercih olur. Notlar ipucudur, kural değil; o günkü isteğin hep üstündür.
Defterin videolarını gerçekten senin tarzına yaklaştırdığını ölçmedik. Nasıl çalıştığı, ne söz vermediği ve nasıl kapatılacağı: `TARZ.md`.

Beğendiğin videoları `referans/` klasörüne koyarsan ajan kurgudan önce onlara kare kare bakar ve çıta olarak kullanır. Ajana verilen talimat kopyalamamaktır; sonucu sen de kontrol et. Bu klasör depoya girmez.

## Kullanım kuralları
- **Yalnız kullanma hakkın olan görüntü:** kendi oyun kaydın ya da klip almaya açıkça izin veren bir yayıncının yayını. İzin yoksa kesme. Klip programları ve kurallar hakkında kaynaklı notlar: `klipci-rehberi.md`.
- **Fragman ve resmî oyun görüntüsü sesi kapalı kullanılır;** çekim aleti sesi zaten atar. Sesi kapatmak kullanım izni vermez: oyunun yayımcısının video kuralları geçerlidir ve sorumluluk senindir. Bu konuda bulabildiklerimiz ve bulamadıklarımız: `klipci-rehberi.md`, bölüm 3b.
- **Rakam, tarih, fiyat** senin metninden ya da gösterdiğin kaynaktan gelir, ajan kendi rakam eklemez; GTA 6 bilgisi `bilgi-havuzu.md`'den ve ekranda kaynağıyla yazılır. Havuz 17.11.2026'da hazırlandı; eskiyebilir, kullanmadan önce kaynağına bak.
- **İlk 7 saniyede kanlı sahne yok, hikâye sürprizi (spoiler) yok.** Bu, ajana verilen bir talimattır; motor denetlemez. Sen bak.

## Dürüst sınırlar ve bilinen zayıf yerler
- **Bu sayfadaki "ajan şunu yapar" cümleleri ajana verilen talimattır.** Ajan bir dil modelidir, arada atlayabilir. Atlarsa sohbette söyle.
- **Kurgu kalitesi ilk sürüm ve değişken.** Denemelerde aynı yoldan hem görsel fikri olan hem de dümdüz altyazılı videolar çıktı. Ajan sesi duyamaz, hareketi izleyemez; yalnız karelere ve ölçümlere bakar. Akıcılığa ve sese sen bak.
- **Müzik ve efekt sesleri kodla üretiliyor ve zayıf.** İndirilmiş müzik ya da ses örneği yok.
- **Deneme sesi yer tutucudur.** Windows sesiyle yapılan Short'un ritmi yanıltır. Kendi sesini kaydedince dosyanın yolunu sohbete yazman yeter; Short o sesle yeniden kurulur.
- Aday an bulucu kabadır ve yalnız bir yayıncının CS2 kayıtlarıyla ayarlandı: 1 saatlik denemede iyi anların bir kısmı ilk on adayda yoktu; ajan konuşmanın yazısını da okuyarak seçer.
- **Başka dildeki kayıt:** konuşma `--dil en` (ya da `--dil auto`: dili Whisper tanır) ile yazıya dökülür. Türkçe dışında yalnız 2 dakikalık tek bir İngilizce kayıtla denendi (yazıya dökme, aday anlar ve tek bir altyazı önizleme karesi; bütün bir klip kurulmadı). An bulucunun söylenenlere bakan kısmı yalnız Türkçe için ayarlı; başka dilde kapanır, adaylar ses ve yapıya dayanır. Türkçe dışı harflerle (é, ä, ß…) altyazı denenmedi. Deneme sesi yalnız Türkçe okur: başka dilde Short için kendi sesini ver.
- Whisper adları ve bazı kelimeleri yanlış duyar, altyazıya da öyle yazılır; doğru yazımı sohbette söylemen yeter.
- Kamera bulucu çizgi film ya da 3D karakter yüzünü çoğu zaman bulamaz; o zaman ajan kareye bakıp karar verir, yanlışsa sohbette söyle.
- Son kontrol yalnız teknik hataları yakalar (kare tekrarı, ses kayması, son kelimede bitiş, ekran alanı); zevke karışmaz.
- `bilgi-havuzu.md` ve `klipci-rehberi.md` GTA VI'nın çıkışından iki gün önce yazıldı. Havuzda yalnız GTA VI bilgisi var: başka bir oyun için bilgi Short'u yapacaksan aynı biçimde, kaynaklı kendi havuzunu yazman gerekir (Klip işi oyundan bağımsızdır).

## Teşekkür
Aracı sahnenin içeriğine göre seçme ve efekt sesini görüntüye oturtma fikri için Leo'ya teşekkürler: [github.com/leodavincs/kalem](https://github.com/leodavincs/kalem) (MIT).
Sade klipteki 2-3 kelimelik altyazı gruplama kuralı Browser Use'un video-use projesinden: [github.com/browser-use/video-use](https://github.com/browser-use/video-use) (MIT).

## Lisans
Kod MIT lisanslıdır (`LICENSE`), Copyright (c) 2026 Furkan Cavlak. İçindeki üçüncü taraf dosyalar bu lisansın dışındadır, kendi lisanslarıyla gelir:
- **Anton yazı tipi** (`kod/font/Anton.ttf`): SIL Open Font License 1.1. Tam metin `kod/font/LISANS.txt`, kaynak notu `kod/font/KAYNAK.txt`.
- **YuNet yüz modeli** (`kod/model/yunet.onnx`): MIT, OpenCV Zoo. Lisans metni ve kaynak notu `kod/model/KAYNAK.txt`.
- **GSAP 3.14.2** (`alet/vendor/gsap.min.js`): açık kaynak lisansı değil ve MIT kapsamında değil. GSAP'ın kendi "Standard 'No Charge' GSAP License" şartlarıyla gelir (bugün sahibi Webflow; şartlar gsap.com/standard-license, 18.11.2026'da okundu): son kullanıcıdan ücret alınmayan işlerde ücretsiz kullanılır, Webflow'un görsel animasyon aracıyla yarışan kodsuz animasyon araçlarında kullanılamaz, dosyanın başındaki telif satırı silinmez. Dosya burada değiştirilmeden duruyor. Bu depodan ücretli bir ürün çıkaracaksan önce o sayfayı oku.
- **Altyazı gruplama kuralı** (`kod/klip.py`, `kumele`): video-use projesindeki `chunk_words` fonksiyonundan uyarlandı (MIT, Copyright (c) 2026 Browser Use). Lisans metni `kod/LISANS-video-use.txt`.
