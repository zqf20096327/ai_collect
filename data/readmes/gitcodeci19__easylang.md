# LingoEx - Yapay Zekâ Destekli Dil Öğrenme Tarayıcı Eklentisi

Tarayıcınızda gezinirken aktif hatırlama, sesli dikte ve yapay zekâ destekli kişisel derslerle İngilizce öğrenmenizi sağlayan açık kaynaklı Chrome / Edge / Brave eklentisi.

<p align="left">
  <a href="https://github.com/gitcodeci19/easylang/releases">
    <img src="https://img.shields.io/github/downloads/gitcodeci19/easylang/total?style=for-the-badge&label=%C4%B0ndirme&color=7c3aed" alt="Toplam İndirme" />
  </a>
  <a href="https://github.com/gitcodeci19/easylang/releases/latest">
    <img src="https://img.shields.io/github/v/release/gitcodeci19/easylang?style=for-the-badge&label=S%C3%BCr%C3%BCm&color=10b981" alt="Son Sürüm" />
  </a>
  <a href="https://github.com/gitcodeci19/easylang/stargazers">
    <img src="https://img.shields.io/github/stars/gitcodeci19/easylang?style=for-the-badge&label=Y%C4%B1ld%C4%B1z&color=f59e0b" alt="GitHub Yıldız" />
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/github/license/gitcodeci19/easylang?style=for-the-badge&label=Lisans&color=3b82f6" alt="Lisans" />
  </a>
</p>

## Öne Çıkan Özellikler

- **A1–C1 Yol Haritası & Özel Dersler:** Tarayıcınızın herhangi bir sekmesinde etkileşimli kelime, cümle kurma, boşluk doldurma ve dikte dersleri.
- **Akıllı Hata Analizi:** Yanlışlarınızı ve zorlandığınız dilbilgisi yapılarını takip ederek size özel telafi dersleri oluşturur.
- **Doğal Çevrimdışı Seslendirme:** Tamamen tarayıcı içinde (sunucusuz, GPU gerektirmeden) çalışan İngilizce **Heart** nöral sesi, Türkçe **EMA Lightning** AI Koç ve 142 sesli gramer/soru anlatımı.
- **Aralıklı Hatırlatma & Sayfa Challenge:** Belirlediğiniz aralıklarla karşınıza kısa tekrar kartları çıkarır ve gezdiğiniz sayfalardaki gerçek cümlelerden anlık pratik yaptırır.

<p align="center">
  <img src="docs/gifs/01-auto-exposure-ai.gif" alt="Otomatik hatırlatma ve AI değerlendirme kartı" width="820" />
</p>

<p align="center">
  <img src="docs/gifs/02-mistake-focus-loop.gif" alt="Hata yakalama ve kişisel odak döngüsü" width="820" />
</p>

---

## Kurulum (Chrome / Edge / Brave)

1. **[Releases](https://github.com/gitcodeci19/easylang/releases/latest)** sayfasından `LingoEx-v2.3.0-Ultimate.zip` dosyasını indirip bir klasöre çıkartın.
2. Tarayıcıda `chrome://extensions` adresini açıp sağ üstten **Geliştirici modu**nu etkinleştirin.
3. **Paketlenmemiş öğe yükle** butonuna tıklayıp çıkarttığınız klasörü seçin.

> Python, Node.js veya ek bir kurulum gerekmez; tüm ses motorları doğrudan tarayıcı içinde çalışır.

---

## Ücretsiz Yapay Zekâ API Kurulumu (İsteğe Bağlı)

Temel dersler, sözlük ve seslendirme tamamen çevrimdışı çalışır. AI değerlendirme, **AI'a Sor** ve **Challenge** özellikleri için Groq, NVIDIA veya AMD'nin ücretsiz geliştirici kotalarından **tek bir API anahtarı** eklemeniz yeterlidir.

<details>
<summary><strong>Groq — Önerilen (Hızlı ve Ücretsiz)</strong></summary>

- **Önerilen model:** `qwen/qwen3.8-27b`
- **API sayfası:** [console.groq.com/keys](https://console.groq.com/keys)

1. [console.groq.com](https://console.groq.com) adresinde ücretsiz hesap açın.
2. **Create API Key** ile yeni bir anahtar oluşturun (`gsk_...`).
3. Eklentide **Ayarlar → Yapay Zekâ → ANA API** alanına yapıştırıp kaydedin.

</details>

<details>
<summary><strong>NVIDIA NIM — Alternatif API</strong></summary>

- **API sayfası:** [build.nvidia.com](https://build.nvidia.com/)

1. Ücretsiz NVIDIA Developer hesabıyla giriş yapıp bir model (ör. Gemma 4 31B) seçin.
2. **Get API Key → Generate API Key** adımıyla `nvapi-...` anahtarını alın.
3. Eklentide **ANA API** veya **Yedek API** alanına yapıştırıp kaydedin.

</details>

<details>
<summary><strong>AMD TokenLab — Alternatif API</strong></summary>

- **API sayfası:** [developer.amd.com/ai-developer-program](https://developer.amd.com/ai-developer-program/)

1. AMD Developer Portal üzerinden ücretsiz kayıt olup **Token Lab (Radeon Cloud)** bölümünü açın.
2. **Get API Key** ile anahtarınızı alıp eklentideki API alanına yapıştırın.

</details>

---

## Kullanılan Açık Kaynaklar ve Veri Kaynakları

| Kategori | Proje / Kaynak | Kullanım Amacı | Lisans |
|---|---|---|---|
| **İngilizce TTS** | [mesm-tts](https://huggingface.co/mesmertech/mesm-tts) (`Heart v2g` & `PDN` WASM) | Çevrimdışı 24 kHz İngilizce seslendirme *(Kokoro-82M & Paradee-8M tabanlı)* | Apache-2.0 |
| **İngilizce Fonem** | [Misaki](https://github.com/hexgrad/misaki) (`us_gold` + `us_silver`) | Saf JS Amerikan İngilizcesi fonem sözlüğü (G2P) | Apache-2.0 |
| **Türkçe TTS** | [EMA Lightning](https://huggingface.co/canberkkkkkk/ema-lightning) | Çevrimdışı 48 kHz Türkçe AI Gramer Koçu (`int8` ağırlık paketli) | Apache-2.0 |
| **Çalışma Motoru** | [ONNX Runtime Web](https://github.com/microsoft/onnxruntime) | Tarayıcı içi WASM SIMD model çıkarımı | MIT |
| **Sesli Anlatımlar** | ElevenLabs + [Opus](https://opus-codec.org/) (32 kbps VBR) | 35 gramer, 92 soru ve 15 rehber ses kaydı | — |
| **Cümle Veri Seti** | [Tatoeba Project](https://tatoeba.org) | İngilizce–Türkçe örnek cümle çiftleri | CC BY 2.0 FR / CC0 |
| **Sözlük Verisi** | [FreeDict (`eng-tur`)](https://github.com/freedict/fd-dictionaries) | İngilizce–Türkçe kelime tanımları | GPL-2.0+ |
| **CEFR Seviyeleri** | [Oxford 5000 CEFR JSON](https://github.com/winterdl/oxford-5000-vocabulary-audio-definition) | A1–C1 seviye, kelime türü ve IPA etiketleri | Açık kaynak |
| **Çeviri Yedeği** | [MyMemory Translation API](https://mymemory.translated.net) | AI kapalıyken sağ tık kelime çevirisi (isteğe bağlı) | — |
| **Derleme** | TypeScript + [esbuild](https://esbuild.github.io/) | Manifest V3 paketleme | MIT |

Ayrıntılı lisans ve atıf bilgileri için [ATTRIBUTIONS.md](ATTRIBUTIONS.md) dosyasına bakabilirsiniz.

---

<details>
<summary><strong>Kaynak Koddan Derleme & Gizlilik</strong></summary>

```bash
npm install
npm run build
```

- İlerleme verileriniz ve API anahtarınız yalnızca tarayıcınızın yerel depolamasında tutulur.
- Yapay zekâ özelliği açıksa yalnızca soru değerlendirme/sohbet istekleri seçtiğiniz API sağlayıcısına gider.
- Proje lisansı: [GNU GPL-3.0](LICENSE)

</details>

> **Not:** Bu açık kaynak proje bağımsız olarak geliştirilmektedir; `easylang.com` veya benzer adlı herhangi bir hizmet ya da marka ile resmi bağlantısı yoktur.
