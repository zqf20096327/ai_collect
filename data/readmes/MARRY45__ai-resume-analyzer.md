# AI Resume Analyzer

[![CI](https://github.com/MARRY45/ai-resume-analyzer/actions/workflows/ci.yml/badge.svg)](https://github.com/MARRY45/ai-resume-analyzer/actions/workflows/ci.yml)
![Python 3.12](https://img.shields.io/badge/python-3.12-blue)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

CV'yi hedef iş ilanına göre analiz eden, hangi gereksinimin karşılandığını CV'den kanıtıyla
gösteren ve geliştirilebilecek alanları listeleyen LLM/RAG tabanlı analiz motoru.

> **English summary.** An LLM/RAG service that scores a CV against a job posting. It extracts
> the posting's requirements, retrieves supporting evidence from the CV with embeddings, has the
> model judge each requirement as met / partial / missing, and then computes the match score in
> code so that it is reproducible. Quotes the model cites are verified against the CV text.
> Built with FastAPI, Pydantic and the Gemini API; the UI and reports are in Turkish or English.

**Stack:** Python · FastAPI · Gemini (LLM + embedding) · RAG · Pydantic

![Analiz raporu ekran görüntüsü](docs/screenshot.jpg)

## Nasıl çalışır

```
İş ilanı ──► 1. Gereksinim çıkarma (LLM, yapılandırılmış çıktı)
                     │
CV ──► 2. Bölümlere/parçalara ayırma ──► 3. Embedding ile her gereksinime kanıt getirme
                     │
             4. Kanıta dayalı değerlendirme + öneriler (LLM, yapılandırılmış çıktı)
                     │
             5. Skor, anahtar kelime kapsamı, alıntı doğrulama (kod, deterministik)
```

## Tasarım kararları

- **Skoru LLM vermez.** Model her gereksinime yalnızca `met / partial / missing` der; 0–100 skoru
  kod hesaplar (zorunlu gereksinimler 2 kat ağırlıklı). Aynı durumlar her zaman aynı skoru verir.
- **Aynı ilan aynı gereksinim listesini verir.** İlandan çıkarılan gereksinimler önbelleğe alınır;
  CV'yi düzeltip tekrar analiz edince skor farkı ilanın farklı bölünmesinden değil CV'den gelir.
- **Alıntılar doğrulanır.** Modelin "kanıt" diye gösterdiği alıntı CV'de birebir geçmiyorsa
  rapordan çıkarılır.
- **Anahtar kelime kapsamı deterministiktir.** İlandaki teknolojilerin CV'de geçip geçmediği
  metin eşleştirmesiyle kontrol edilir (`C++`, `Node.js` gibi terimler ve Türkçe karakterler dahil).
- **Yedek model zinciri.** Asıl model yoğunsa (503), kotası dolduysa (429) ya da bağlantı koparsa
  sıradaki modele geçilir; yoğun çıkan model 2 dakika atlanır. Raporda yanıtı üreten model yazar.
- **CV ve ilan veri olarak işlenir.** Metinler etiketler içinde gönderilir ve modele içlerindeki
  talimatları yok sayması söylenir. Bu, CV'ye gizlenmiş "bu adaya 100 ver" türü metinlere karşı
  bir önlemdir, garanti değildir.

## Kurulum

Python 3.12 ve bir [Gemini API anahtarı](https://aistudio.google.com/apikey) gerekir.

```bash
git clone https://github.com/MARRY45/ai-resume-analyzer.git
cd ai-resume-analyzer
python -m venv .venv
```

Sanal ortamı etkinleştir (Windows: `.venv\Scripts\activate`, macOS/Linux: `source .venv/bin/activate`),
ardından:

```bash
pip install -r requirements.txt
cp .env.example .env
```

`.env` dosyasını açıp anahtarını `GEMINI_API_KEY=` satırına yapıştır. `.env` git'e girmez;
anahtarı `.env.example` içine yazma.

İsteğe bağlı ayarlar (`.env`):

| Değişken | Varsayılan |
|---|---|
| `GEMINI_MODEL` | `gemini-3.8-flash` |
| `GEMINI_FALLBACK_MODELS` | `gemini-3.7-flash,gemini-3.5-flash` |
| `GEMINI_EMBEDDING_MODEL` | `gemini-embedding-001` |

## Çalıştırma

```bash
uvicorn app.main:app --port 8000
```

- Demo arayüzü: http://localhost:8000 ("Örnek veriyi doldur" ile hazır bir CV ve ilan gelir)
- API dokümantasyonu: http://localhost:8000/docs

## API

`POST /api/analyze` (multipart/form-data)

| Alan | Zorunlu | Açıklama |
|---|---|---|
| `job_text` | evet | İş ilanının metni |
| `cv_file` | `cv_text` yoksa | PDF, DOCX, TXT ya da MD (en fazla 5 MB) |
| `cv_text` | `cv_file` yoksa | CV'nin düz metni |
| `language` | hayır | Rapor dili: `tr` (varsayılan) ya da `en` |

```bash
curl -X POST http://localhost:8000/api/analyze \
  -F "cv_file=@samples/cv_ornek.txt" \
  -F "job_text=<samples/ilan_ornek.txt"
```

Yanıt (`AnalysisReport`), kısaltılmış:

```json
{
  "job_title": "AI Backend Engineer",
  "match_score": 63,
  "summary": "Aday Python backend tarafında güçlü...",
  "requirements": [
    {
      "requirement": {"id": "R5", "text": "PostgreSQL ile veri modelleme ve sorgu optimizasyonu",
                      "category": "hard_skill", "importance": "must_have"},
      "status": "met",
      "reasoning": "İndeksleme ile sorguları optimize ettiğini belirtmiştir.",
      "evidence_quote": "PostgreSQL üzerinde yavaş çalışan sorguları indeksleme ile iyileştirdim",
      "evidence": [{"chunk_id": 2, "section": "DENEYİM", "text": "...", "similarity": 0.71}]
    }
  ],
  "keywords": {"present": ["Python", "PostgreSQL"], "missing": ["FastAPI", "Docker"]},
  "strengths": ["..."],
  "improvements": [
    {"area": "Deneyim", "priority": "medium", "issue": "...", "suggestion": "...",
     "example_rewrite": "...yanıt sürelerini %[X] oranında azalttım."}
  ],
  "meta": {"model": "gemini-3.5-flash", "embedding_model": "gemini-embedding-001",
           "cv_chunks": 8, "duration_seconds": 21.3}
}
```

Hata kodları: `400` geçersiz girdi ya da okunamayan dosya · `413` dosya çok büyük ·
`429` Gemini kota sınırı · `502` Gemini hatası · `503` API anahtarı tanımlı değil.

## Geliştirme

```bash
pip install -r requirements-dev.txt
pytest -q
```

Testler ağ çağrısı yapmaz ve API anahtarı gerektirmez; LLM, `tests/conftest.py` içindeki sahte
istemciyle değiştirilir. Aynı testler her push'ta GitHub Actions üzerinde çalışır.

## Yapı

```
app/
  main.py        FastAPI uçları ve hata eşlemeleri
  analyzer.py    Analiz hattı, skor, anahtar kelime kapsamı, alıntı doğrulama
  retrieval.py   Embedding + kosinüs benzerliği ile kanıt getirme
  chunking.py    CV'yi bölüm başlıklarına göre parçalama (TR/EN)
  parsing.py     PDF / DOCX / TXT metin çıkarma
  llm.py         Gemini istemcisi (yapılandırılmış çıktı, embedding, yedek model zinciri)
  prompts.py     Prompt şablonları
  schemas.py     Pydantic şemaları
  static/        Demo arayüzü
samples/         Örnek CV ve iş ilanı (kurgusal)
tests/           Birim ve API testleri
```

## Sınırlar

- Skor aynı girdide koşudan koşuya birkaç puan oynayabilir: gereksinim listesi sabittir, ama sınırdaki
  bir gereksinimi model bir seferinde "karşılanıyor", diğerinde "kısmen" sayabilir.
- Bir analiz 20–60 saniye sürer; sürenin çoğu Gemini'nin yanıt süresidir.
- Taranmış (görüntü) PDF'lerden metin çıkarılamaz; OCR yok.
- Analiz başına 2 LLM + 2 embedding çağrısı yapılır; ücretsiz kotada art arda çok analiz `429` döndürebilir.
- Vektörler bellekte tutulur, kalıcı bir vektör veritabanı yok; tek CV için gerekmiyor.

## Lisans

[MIT](LICENSE)
