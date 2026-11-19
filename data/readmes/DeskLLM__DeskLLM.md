<p align="center">
  <img src="assets/deskllm.png" alt="DeskLLM logosu" width="120">
</p>

<h1 align="center">DeskLLM</h1>

<p align="center">
  <strong>Yapay zekâ modellerini kendi bilgisayarında çalıştır. Hesap yok, abonelik yok, sohbetlerin sende kalır.</strong>
</p>

<p align="center">
  Windows 10/11 · Türkçe ve İngilizce arayüz · 0.9 Beta
</p>

<p align="center">
  <strong>Türkçe</strong> · <a href="README.en.md">English</a>
</p>

---

DeskLLM, yerel yapay zekâ modelleriyle sohbet etmeni sağlayan bir masaüstü uygulamasıdır. Bilgisayarının donanımına bakar, sana uygun modelleri önerir ve tek tıkla indirir. Bir kez indirdiğin modelle internet olmadan da sohbet edebilirsin.

Terminal komutlarıyla uğraşmana, Python kurmana ya da API anahtarı almana gerek yok. Kurulum dosyasını çalıştır, modelini seç, yazmaya başla.

![DeskLLM sohbet ekranı: tablo ve kod içeren bir cevap](docs/screenshots/chat.png)

## Neler yapabilir?

**Model Kütüphanesi**
- 200'den fazla modeli tek ekranda inceleme
- Ekran kartına, belleğine ve işlemcine göre "sana uygun" öneriler
- Hugging Face'ten tek tıkla indirme, yarıda kalan indirmeye devam etme
- Elindeki `.gguf` dosyasını doğrudan açma ya da Ollama ile çalışma
- İndirdiğin her şeyi Depolama sayfasında boyutlarıyla görme ve silme

![Model Kütüphanesi: bilgisayara uygun model önerileri](docs/screenshots/library.png)

**Sohbet**
- Cevapları yazılırken canlı görme
- Düşünebilen modellerde beyin düğmesiyle düşünme modunu açıp kapatma
- Cevap sınıra takılırsa kaldığı yerden otomatik devam etme
- Kod renklendirme ve kopyalama, tablolar, matematik formülleri
- Mesaj düzenleme, cevabı yeniden üretme, sohbet arama
- Sohbetlerin otomatik kaydedilmesi

**Dosyalar ve resimler**
- PDF, Word, metin ve kod dosyalarıyla sohbet etme
- Cevabın belgenin hangi bölümüne dayandığını görme
- Görsel destekli modellerle resimler hakkında konuşma

**Ses**
- Mikrofonla Türkçe ve İngilizce yazdırma, internetsiz
- Cevapları Windows'un kendi sesleriyle okutma

**Donanım**
- Modeli ekran kartına, kart ile işlemciye birlikte ya da yalnızca işlemciye otomatik yerleştirme
- Modelin nerede çalışacağını kendin de seçebilme
- CPU, RAM, GPU ve VRAM kullanımını canlı izleme

![Model ayarları: modelin nerede çalışacağı ve cevap uzunluğu](docs/screenshots/settings.png)

**Arayüz**
- Koyu ve açık tema
- İlk açılışta uygulamayı adım adım tanıtan tur
- Türkçe ve İngilizce arayüz
- Hatalar teknik kodlar yerine anlaşılır uyarılarla, uygulamanın içinde gösterilir

<p align="center">
  <img src="docs/screenshots/home.png" alt="Koyu tema karşılama ekranı" width="49%">
  <img src="docs/screenshots/home-light.png" alt="Açık tema karşılama ekranı" width="49%">
</p>

## Sistem gereksinimleri

| | En az | Önerilen |
|---|---|---|
| İşletim sistemi | Windows 10, 64 bit | Windows 11 |
| Bellek (RAM) | 8 GB | 16 GB veya üstü |
| Ekran kartı | Gerekmez, model işlemcide de çalışır | En az 6 GB belleği olan NVIDIA RTX ya da Vulkan destekli bir kart |
| Disk | Uygulama için yaklaşık 250 MB, her model için 2–20 GB | SSD |

CUDA motoru için NVIDIA sürücüsünün 580 veya üstü olması gerekir. Sürücü daha eskiyse uygulama Vulkan ile çalışır.

## Kurulum

1. [Releases](https://github.com/DeskLLM/DeskLLM/releases) sayfasından `DeskLLM-Setup-0.9.0.exe` dosyasını indir (50 MB).
2. Dosyayı çalıştır. Yönetici izni istemez.
3. İstediğin seçmeli parçaları işaretle, kurulumu bitir.

Uygulama, Python ve Vulkan motoru kurulum dosyasının içinde gelir, ayrıca bir şey kurman gerekmez.

| Seçmeli parça | Ne işe yarar? | İndirme |
|---|---|---|
| NVIDIA CUDA motoru | Uyumlu RTX kartlarda daha yüksek hız | 620 MB |
| Konuşma tanıma (Türkçe, İngilizce) | Mikrofonla yazdırma | Dil başına yaklaşık 40 MB |
| Belgelerde anlamına göre arama | Dosyalardan daha isabetli cevap | 330 MB |
| Başlangıç modeli (Gemma 4 E4B) | Kurulumdan sonra hemen sohbet | 5,4 GB |

Seçmediğin parçaların çoğunu sonradan uygulamanın içinden de indirebilirsin. CUDA motoru için kurulumu yeniden çalıştırman gerekir.

> **Windows uyarısı:** Kurulum dosyası henüz dijital olarak imzalı olmadığı için Windows "bilinmeyen yayıncı" uyarısı gösterebilir. Devam etmek için **Ek bilgi → Yine de çalıştır** seç.

## İlk kullanım

1. DeskLLM'i aç. İlk açılışta kısa bir tanıtım turu ekranın bölümlerini gösterir.
2. **Önerilen Modeller** ekranına gir ve bilgisayarına uygun bir modeli indir.
3. Modeli seç, mesajını yaz.

![Tanıtım turu: mesaj kutusunu anlatan adım](docs/screenshots/tour.png)

Ne kadar büyük model çalıştırabileceğin ekran kartı belleğine ve RAM'ine bağlıdır. Model Kütüphanesi'ndeki uyum etiketleri bu konuda yol gösterir, ama dosya boyutu ve bellek miktarına dayalı tahminlerdir.

Turu daha sonra **Ayarlar → Uygulama Ayarları → Turu Başlat** ile yeniden açabilirsin.

## Ekran kartı desteği

| Donanım | Motor | Durum |
|---|---|---|
| NVIDIA RTX 30 serisi | CUDA veya Vulkan | RTX 3070'te denendi |
| NVIDIA RTX 40 serisi | CUDA veya Vulkan | Destekleniyor, gerçek kartta denenmedi |
| NVIDIA RTX 50 serisi | CUDA veya Vulkan | Deneysel, gerçek kartta denenmedi |
| AMD ve Intel | Vulkan | Deneysel, gerçek kartta denenmedi |
| Ekran kartı yok | İşlemci | Çalışır, daha yavaştır |

CUDA kullanılamazsa uygulama kendiliğinden Vulkan ile devam eder. Vulkan da yoksa model işlemcide çalışır.

Karşılaştırma için RTX 3070 ve Gemma 4 12B modeliyle ölçülen hızlar:

| Motor | Hız |
|---|---|
| CUDA | 12,8 token/sn |
| Vulkan | 6,4 token/sn |
| İşlemci | 3,3 token/sn |

Sonuçlar modele, donanıma ve ayarlara göre değişir.

## Gizlilik

- Sohbetlerin, belgelerin ve ayarların bilgisayarında kalır.
- Hesap istemez, kullanım verisi toplamaz.
- İnternet yalnızca model ve seçmeli parça indirirken, kütüphanede model bilgisi alırken ve günde en fazla bir kez yeni sürüm olup olmadığına bakarken kullanılır.
- Yeni sürüm denetimi GitHub'a yalnızca "son sürüm hangisi?" diye sorar, bilgisayarın hakkında bilgi göndermez. **Ayarlar → Uygulama Ayarları** bölümünden kapatabilirsin.

Veriler uygulamanın kurulu olduğu klasörde durur:

| Klasör | İçerik |
|---|---|
| `chats/` | Sohbetler, ayarlar, eklenen resimler |
| `models/` | İndirilen modeller, ses ve arama modelleri |

Uygulamayı kaldırırken bu verilerin silinip silinmeyeceği sorulur.

## Sık sorulanlar

**Ücretsiz mi?**
Evet. DeskLLM ücretsiz ve açık kaynaklıdır. İndirdiğin modeller de ücretsizdir, ama her modelin kendi kullanım lisansı vardır (örneğin Gemma ya da Llama lisansı). Lisansı modelin Hugging Face sayfasında görebilirsin.

**İnternet gerekir mi?**
Yalnızca model ve seçmeli parçaları indirirken. Model indikten sonra internet olmadan sohbet edebilirsin.

**Hangi modeli seçmeliyim?**
Emin değilsen **Önerilen Modeller** ekranında "sana uygun" etiketli bir model seç. Başlangıç için Gemma 4 E4B iyi bir seçimdir: 5,4 GB'tır, çoğu bilgisayarda çalışır ve resimleri de anlar.

**ChatGPT'den farkı ne?**
DeskLLM'deki modeller senin bilgisayarında çalışır: ücretsizdir, internet istemez ve yazdıkların bilgisayarından çıkmaz. Buna karşılık bilgisayarda çalışan modeller büyük bulut modellerinden küçüktür. Zor sorularda daha az başarılı olabilirler ve hızları donanımına bağlıdır.

**Modeller ne kadar yer kaplar?**
Küçük modeller 2–3 GB, orta boy modeller 5–10 GB, büyük modeller 20 GB ve üstü yer kaplar. İndirdiklerini **Ayarlar → Depolama** sayfasından görüp silebilirsin.

**Ollama ya da kendi modelimi kullanabilir miyim?**
Evet. Bilgisayarındaki herhangi bir `.gguf` dosyasını **Ayarlar → Model Ayarları** bölümünden açabilir ya da çalışan bir Ollama sunucusuna bağlanabilirsin.

## Kaynak koddan çalıştırma

Python 3.11 gerekir.

```bash
git clone https://github.com/DeskLLM/DeskLLM.git
cd DeskLLM
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python DeskLLM.py
```

`pip`, `llama-cpp-python` paketini derlemeye çalışabilir. Hazır Vulkan sürümü için:

```bash
pip install llama-cpp-python --force-reinstall --no-cache-dir --only-binary :all: --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/vulkan
```

Kurulum dosyasını kendin üretmek için Inno Setup 6.6 veya üstü de gerekir:

```powershell
powershell -ExecutionPolicy Bypass -File installer\build.ps1
```

## Bilinen kısıtlar

- Şu an yalnızca Windows sürümü var.
- Kurulum dosyası imzasız olduğu için Windows uyarı gösterebilir.
- AMD, Intel ve RTX 50 desteği gerçek kartlarda henüz denenmedi.
- Görsel destekli modeller Vulkan ve CUDA kurulumlarında tam olarak denenmedi.

## Yol haritası

- [ ] Sohbetleri dışa aktarma (Markdown, PDF)
- [ ] Kendi sistem talimatını yazabilme
- [ ] Daha fazla arayüz dili (topluluk çevirileriyle)
- [ ] Dijital olarak imzalı kurulum dosyası
- [ ] Windows tam sürümü
- [ ] Linux sürümü
- [ ] macOS sürümü

## Geri bildirim

DeskLLM tek kişilik bir proje ve beta aşamasında. Bir hata bulursan ya da fikrin varsa [Issues](https://github.com/DeskLLM/DeskLLM/issues) sayfasından yazabilirsin.

Hata bildirirken **Ayarlar → Hakkında → Sürüm Bilgisini Kopyala** çıktısını eklemen sorunu bulmayı çok kolaylaştırır.

## Teşekkürler

DeskLLM şu açık kaynak projeler sayesinde çalışır: [llama.cpp](https://github.com/ggml-org/llama.cpp), [llama-cpp-python](https://github.com/abetlen/llama-cpp-python), [PyQt5](https://www.riverbankcomputing.com/software/pyqt/), [Vosk](https://alphacephei.com/vosk/), [Lucide](https://lucide.dev) ve [Simple Icons](https://simpleicons.org).

## Lisans

Bu proje [GPL-3.0](LICENSE) lisansıyla dağıtılır. Kurulum dosyasının içindeki diğer açık kaynak bileşenlerin lisansları [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) dosyasında listelenir.
