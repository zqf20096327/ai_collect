# Browser Bridge

Kendalikan **Chrome milikmu sendiri** dari agent AI — memakai sesi login yang sudah ada.
Tanpa Playwright, tanpa Chrome for Testing, tanpa login ulang, tanpa menyentuh profile Chrome.

```
[Agent AI / kamu] --HTTP--> bridge-server.mjs (127.0.0.1:8787)
                                   ^
                                   | long-poll
                          extension/ (Chrome) --CDP--> tab asli
```

Bridge ini generik: bisa dipakai untuk **situs apa pun** yang kamu izinkan. Tiga situs yang
sudah diuji dan punya helper khusus: **Tinkercad**, **Logicly**, dan **Canva**.

> Dulu proyek ini bernama **Tinkercad Bridge**. Namanya berubah karena semua perintah inti
> bersifat generik; Tinkercad hanya salah satu target.

![Node >= 18](https://img.shields.io/badge/node-%3E%3D18-339933)
![Chrome >= 116](https://img.shields.io/badge/chrome-%3E%3D116-4285F4)
![License MIT](https://img.shields.io/badge/license-MIT-blue)

---

## Kenapa bukan browser automation biasa?

| Masalah automation biasa | Solusi bridge ini |
|---|---|
| Login dari nol → Google SSO diblokir | Memakai sesi Chrome kamu yang sudah login |
| Chrome for Testing mudah terdeteksi | Chrome asli, tanpa flag automation |
| Profile terkunci saat Chrome terbuka | Tidak menyentuh profile sama sekali |
| Butuh browser terpisah | Mengendalikan tab yang sedang kamu pakai |

Yang dipakai adalah `chrome.debugger` (CDP) di dalam Chrome kamu sendiri. Chrome akan
menampilkan banner *"… started debugging this browser"* selama bridge menempel di satu tab.
Itu normal.

---

## Yang dibutuhkan

- **Node.js 18+** (`node --version`)
- **Chrome 116+** (atau Chromium/Brave/Edge yang mendukung MV3 + `chrome.debugger`)
- Windows, macOS, atau Linux
- Tidak ada dependency npm. Cukup Node.

---

## Mulai cepat

### 1. Pasang extension (sekali saja)

1. Buka `chrome://extensions`
2. Aktifkan **Developer mode** (kanan atas)
3. Klik **Load unpacked**
4. Pilih folder `extension/` dari repo ini
5. Pin extension-nya (ikon puzzle → pin **Browser Bridge**)

Badge extension:

| Badge | Arti |
|---|---|
| `ok` hijau | Tersambung ke bridge |
| `!` biru | Sedang menjalankan perintah |
| `x` merah | Bridge tidak jalan / belum tersambung |

### 2. Jalankan bridge

```bash
npm start
# atau: node bridge-server.mjs
```

Biarkan terminal itu terbuka. Bridge hanya mendengarkan di `127.0.0.1:8787`.

Kalau perlu mengganti port (`BRIDGE_PORT=9000 npm start`), ubah juga
`const BRIDGE = "http://127.0.0.1:8787"` di `extension/background.js` agar extension
menunjuk ke port yang sama.

### 3. Cek semuanya

```bash
npm run doctor
```

Contoh hasil sehat:

```json
{
  "node": "v22.0.0",
  "bridge": { "ok": true, "connected": true, "queued": 0, "port": 8787 },
  "extension": { "ok": true, "data": { "pong": true, "version": "1.6.0" } }
}
```

`node ab.mjs ping` juga cukup untuk memastikan extension hidup. Gunakan `ping`, bukan
`health`: `health.connected` bisa `false` saat long-poll sedang menunggu — itu normal.

---

## Perintah

Semua perintah dijalankan dari folder repo ini.

```bash
node ab.mjs health                 # status bridge
node ab.mjs ping                   # bukti extension hidup + versinya
node ab.mjs doctor                 # cek Node + bridge + extension
node ab.mjs tabs [--all]           # daftar tab (default: domain yang dikonfigurasi)
node ab.mjs match github.com       # daftar tab yang URL/judulnya mengandung string
node ab.mjs newtab https://...     # buka tab baru dan tunggu load
node ab.mjs info                   # judul, URL, ukuran viewport
node ab.mjs maximize               # maksimalkan window
node ab.mjs dpr 1                  # paksa skala 1:1 supaya koordinat akurat
node ab.mjs shot out.png           # screenshot
node ab.mjs nav https://...        # navigasi
node ab.mjs reload                 # muat ulang halaman
node ab.mjs wait 1000              # tunggu milidetik
node ab.mjs wait "#siap" 15000     # tunggu sampai selector muncul
```

### Input & DOM

```bash
node ab.mjs click X Y              # klik kiri (koordinat CSS viewport)
node ab.mjs dblclick X Y
node ab.mjs drag X1 Y1 X2 Y2 [n]   # drag & drop
node ab.mjs wheel X Y DY           # scroll / zoom di posisi kursor
node ab.mjs key Control+s          # tombol / kombinasi
node ab.mjs type "teks"            # ketik (insertText)
node ab.mjs move X Y               # pindahkan kursor

node ab.mjs eval "document.title"  # jalankan JS di halaman
node ab.mjs click-sel "#tombol"    # klik elemen via selector CSS
node ab.mjs click-text "D Latch"   # klik elemen berdasarkan teks
node ab.mjs fill-sel "#input" teks # isi input via selector CSS
node ab.mjs text "#hasil"          # ambil teks elemen
node ab.mjs open-file "#file" path # isi <input type=file> dengan file lokal
```

Semua perintah tab mendukung `--match <domain>` dan `--tab <id>`:

```bash
node ab.mjs --match logic.ly logicly state
node ab.mjs --tab 123456 shot logicly.png
```

Tanpa flag, extension memilih tab aktif yang cocok dengan domain di
`DEFAULT_MATCHES` (`tinkercad.com`, `logic.ly`, `canva.com`). Kalau tab aktif bukan salah
satunya, dipilih tab pertama yang cocok.

### Logicly (model, bukan piksel)

Target yang didukung adalah **Logicly Online Demo** di `https://logic.ly/demo/`.
Aplikasi desktop Logicly tidak bisa ditempel `chrome.debugger` karena berjalan di luar Chrome.

```bash
node ab.mjs newtab https://logic.ly/demo/
node ab.mjs click-text "D Latch"          # masuk editor dari halaman samples
node ab.mjs logicly state                 # objek + sinyal + koneksi
node ab.mjs logicly palette               # komponen yang tersedia
node ab.mjs logicly add "AND Gate" 400 200
node ab.mjs logicly connect 0 0 1 0       # output 0 -> input 0
node ab.mjs logicly disconnect 0
node ab.mjs logicly set 0 1               # switch = high
node ab.mjs logicly move 1 620 240
node ab.mjs logicly rotate 1 cw
node ab.mjs logicly remove 1
node ab.mjs logicly clear
node ab.mjs logicly save hasil.logiclyx
node ab.mjs logicly load hasil.logiclyx
node ab.mjs logicly open hasil.logiclyx
```

Perintah Logicly bekerja pada **model editor** (objek, terminal, kabel, sinyal), bukan
koordinat piksel. Tidak perlu drag mouse. Verifikasi selalu ke `logicly state` — bukan ke
screenshot.

Contoh lengkap: [`examples/half-adder.md`](examples/half-adder.md).

### Canva (eksperimental)

Fase 2A: baca + tulis terbatas lewat UI automation. Setiap perintah tulis mengembalikan
`verified: true|false`; kalau `false`, jangan lanjut.

```bash
node ab.mjs canva state            # url/designId, zoom, halaman, jumlah elemen
node ab.mjs canva list             # elemen halaman aktif
node ab.mjs canva texts            # hanya elemen yang punya teks
node ab.mjs canva pages            # halaman aktif/total + dimensi
node ab.mjs canva sel              # seleksi saat ini (best-effort)
node ab.mjs canva el <id|index>    # detail satu elemen

node ab.mjs canva text <id|sel> "teks baru"
node ab.mjs canva move <id|sel> <x> <y>     # koordinat model px (1920x1080)
node ab.mjs canva dup <id|sel>
node ab.mjs canva del <id|sel>
node ab.mjs canva undo [n]
```

Baca aturan tulis yang sudah teruji di [`AGENTS.md` §7](AGENTS.md#7-canva-editor-desain)
sebelum mengedit desain orang lain. Canva melakukan autosave ke cloud: **duplikat desain
dulu** sebelum operasi tulis.

---

## Memakai bridge ini untuk situs lain

Checklist 5 menit:

1. **Domain.** Tambahkan host di `extension/manifest.json`:

   ```json
   "host_permissions": [
     "https://www.tinkercad.com/*",
     "https://logic.ly/*",
     "https://app-kamu.com/*",
     "http://127.0.0.1/*"
   ]
   ```

2. **(Opsional) domain default.** Tambahkan domain ke
   `const DEFAULT_MATCHES = ["tinkercad.com", "logic.ly", "canva.com"];`
   di `extension/background.js` supaya `tabs` otomatis mencarinya.

3. **Reload extension** di `chrome://extensions` (tombol ↻). Agent tidak bisa melakukannya
   untukmu. Cek `node ab.mjs ping` dan pastikan `version` berubah.

4. **Kalibrasi:** `info` → `maximize` → `dpr 1` → `shot`.

Tidak ada bagian lain yang terikat Tinkercad. Semua perintah inti generik.

---

## Keamanan

Bridge ini hanya untuk **komputer kamu sendiri**:

- Hanya mendengarkan di `127.0.0.1` (tidak bisa diakses dari jaringan).
- Menolak `Host` selain `127.0.0.1`/`localhost` (proteksi DNS rebinding).
- Menolak request browser dengan `Origin` selain `chrome-extension://` — jadi halaman web
  yang sedang kamu buka tidak bisa diam-diam mengendalikan Chrome lewat `localhost`.
- Tidak menyimpan password, cookie, atau token.
- Extension hanya punya host permission untuk domain yang tertulis di manifest.

Matikan dengan **Remove** di `chrome://extensions`, atau hentikan `bridge-server.mjs`.

---

## Troubleshooting

| Gejala | Penyebab / solusi |
|---|---|
| `health` → `connected:false` | Normal saat long-poll menunggu. Pakai `ping`. |
| `timeout: no result from extension` | Service worker mati / extension baru di-reload / DevTools terbuka. Klik ikon extension untuk membangunkan. |
| `unknown command: X` | Versi extension lama — reload, cek `ping.version`. |
| `No tab open matching: …` | Tab target belum dibuka, atau pakai `--match` / `--tab`. |
| `Another debugger is already attached` | Tutup DevTools (F12) di tab itu. |
| Klik tidak berpengaruh | Skala DPR bukan 1, banner menutupi, atau tab tidak fokus. Jalankan `dpr 1` dan `maximize`. |
| `Logicly editor not found` | Masih di halaman samples. Klik sample dulu: `click-text "D Latch"`. |
| `logicly open` → *Untitled Circuit* kosong | File terkompresi dibaca sebagai teks; pakai `logicly load` atau `save --raw`. |
| Output gerbang tidak berubah setelah `logicly set` | Pastikan memakai versi extension terbaru (`ping.version` ≥ 1.6.0). Helper mengembalikan sinyal kanonik `Signal.TRUE/FALSE`; instance baru tidak dikenali gerbang strict. |
| `canva state` → *editor not ready* | Desain belum selesai load, atau tab yang dipilih tab beranda (pakai `--tab`). |

---

## Dokumentasi

| File | Isi |
|---|---|
| [`AGENTS.md`](AGENTS.md) | Aturan operasional untuk agent: 15 aturan wajib, alur kerja, anti-pattern |
| [`docs/logicly.md`](docs/logicly.md) | Format `.logiclyx`, model objek Logicly, perintah bridge |
| [`docs/tinkercad-ids.md`](docs/tinkercad-ids.md) | Katalog `data-did` komponen Tinkercad + cara membaca model rangkaian |
| [`docs/RIWAYAT-2026-11-18.md`](docs/RIWAYAT-2026-11-18.md) | Catatan sesi: kenapa `agent-browser` gagal, temuan internal Tinkercad |
| [`docs/canva/`](docs/canva/) | Konsep dan hasil discovery Canva (Phase 0 & 1) |
| [`examples/half-adder.md`](examples/half-adder.md) | Contoh Logicly dari nol sampai terverifikasi |

---

## Struktur repo

```
browser-bridge/
├─ bridge-server.mjs      # HTTP queue di 127.0.0.1:8787
├─ ab.mjs                 # CLI untuk agent (satu perintah = satu proses)
├─ canva-cli.mjs          # CLI tambahan untuk Canva (eval/run)
├─ extension/
│  ├─ manifest.json       # MV3, host permission
│  └─ background.js       # poll loop + CDP + helper Logicly/Canva
├─ docs/
├─ examples/
└─ scripts-canva/
```

Tiga komponen:

| File | Peran | Hidup di |
|---|---|---|
| `bridge-server.mjs` | Antrean perintah + hasil, HTTP | Node, background |
| `extension/` | Eksekutor CDP di dalam Chrome | Chrome (Load unpacked) |
| `ab.mjs` | CLI untuk agent | Dipanggil per perintah |

Setiap perintah adalah satu proses Node baru yang HTTP POST ke bridge. Tidak ada state di
CLI; state ada di Chrome (tab, scroll, fokus).

---

## Lisensi

MIT — lihat [`LICENSE`](LICENSE).
