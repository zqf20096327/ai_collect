# llm-hallucination

# Deteksi dan Mitigasi Halusinasi LLM pada Pertanyaan Layanan Publik Berbahasa Indonesia

Project mata kuliah [NAMA MATA KULIAH] | Kelompok [NO. KELOMPOK] | Dosen pengampu: [NAMA DOSEN]

Topik: Deteksi dan Mitigasi Halusinasi LLM

## Deskripsi

Project ini mengukur tingkat halusinasi Qwen3-4B-Instruct-2507 pada pertanyaan layanan publik administrasi kependudukan dan dokumen berbahasa Indonesia, membangun detektor halusinasi berbasis konsistensi jawaban, dan mengevaluasi Retrieval-Augmented Generation (RAG) sebagai mitigasi.

## Ruang Lingkup

- Model yang diuji: Qwen3-4B-Instruct-2507 (`Qwen/Qwen3-4B-Instruct-2507`, varian Instruct resmi yang hanya beroperasi pada mode non-thinking)
- Domain: layanan publik (paspor, KTP-el, KK, KIA, akta)
- Dataset pembanding: TruthfulQA (300 pertanyaan acak, seed 42)
- Label jawaban: Benar, Halusinasi, Tidak menjawab

## Skenario Eksperimen

| Kode | Deskripsi |
|---|---|
| S1 | Qwen3-4B-Instruct-2507 tanpa RAG (baseline) |
| S2 | Qwen3-4B-Instruct-2507 dengan RAG (mitigasi) |
| S3 | Detektor halusinasi berbasis konsistensi jawaban |
| S4 | Detektor S3 diuji pada TruthfulQA |

## Struktur Repositori

| Folder | Isi |
|---|---|
| data/raw/ | Dokumen sumber asli: imigrasi, dukcapil, truthfulqa |
| data/processed/ | Chunk dan dataset QA hasil olahan |
| notebooks/ | Notebook eksperimen (Google Colab) |
| src/ | Kode program yang dipakai ulang |
| docs/ | Tabel literatur, rencana evaluasi, laporan progress |

## Sumber Data

Daftar URL dan tanggal akses setiap dokumen dicatat di `data/README.md`. Kebenaran jawaban dinilai terhadap salinan dokumen pada tanggal akses tersebut.

## Cara Menjalankan

Bagian ini dilengkapi bertahap seiring progress. Saat ini (Progress 3) yang tersedia adalah penyiapan lingkungan dan pemuatan model.

1. Buka `notebooks/00_setup.ipynb` di Google Colab, lalu pilih runtime GPU (T4).
2. Jalankan sel secara berurutan: pengecekan GPU dan versi pustaka, lalu pemuatan model `Qwen/Qwen3-4B-Instruct-2507` dalam presisi float16.
3. Versi pustaka dan revisi model yang dipakai dicatat di `docs/lingkungan.txt`.

Langkah untuk menjalankan baseline S1, RAG (S2), dan detektor (S3) akan ditambahkan pada progress berikutnya.

## Status Progress

| Progress | Kegiatan | Status |
|---|---|---|
| 1 | Inisiasi dan rencana | Selesai |
| 2 | EDA dan persiapan data | Selesai |
| 3 | Model baseline | Sedang dikerjakan |
| 4 | Model utama | Belum dimulai |
| 5 | Eksperimen inti | Belum dimulai |
| 6 | Evaluasi dan analisis | Belum dimulai |
| 7 | Prototipe dan draf akhir | Belum dimulai |

## Anggota Kelompok

| No | Nama | NIM | Peran |
|---|---|---|---|
| 1 | Tonggi Simanjuntak | 42324006 | Ketua koordinasi & Integrasi |
| 2 | Joice | 42324002 | Data Pengumpulan & Preprocessing |
| 3 | Joy | 42324022 | Dokumentasi |
| 4 | Brahmana | 42324029 | Evaluasi |
| 5 | Rido | 42324030 | Modeling |
| 6 | Hesekiel | 42324050 | Data EDA & Visualisasi |

## Penggunaan AI Generatif

Claude (Anthropic) digunakan untuk diskusi perumusan project, penyusunan draf kerangka laporan, bantuan penulisan kode notebook, pembuatan draf pasangan tanya-jawab, dan sebagai model judge pada pelabelan jawaban. Seluruh hasil diperiksa oleh anggota kelompok.
