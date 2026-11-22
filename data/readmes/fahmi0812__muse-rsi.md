<p align="center">
  <img src="assets/logo.png" width="200" alt="Muse, the muse-rsi mascot: a strong fluffy creature wearing glasses, flexing">
</p>

<h1 align="center">muse-rsi</h1>

<p align="center">Verified Muse skills — and the setup that installs them.<br>248 entries, a router program, and a daily self-improvement loop that merges its own fixes. No guesses, no paid tools.</p>

> **Ringkasan Bahasa Indonesia:** Kumpulan skill Muse yang sudah dicek langsung. 248 entri (98 terdaftar + 11 orisinal + 139 referensi Lumitome), router yang dites 130/130, dan loop perbaikan diri tiap 24 jam yang me-merge perbaikannya sendiri. Pasang atau update semuanya dengan satu prompt di bawah: kalau ada langkah yang gagal, installer memperbaikinya sendiri dan lanjut dari titik itu, tanpa minta izin.

## Install / update — copy-paste prompt

Copy the prompt below and paste it to any Muse agent. It detects whether muse-rsi is already installed: a fresh agent gets a full install, an existing one gets a full update — including the 24-hour loop activation and every warning that can appear.

**Self-healing:** when a step fails, the installer does not stop to ask. It repairs the cause (missing dependency, folder, permission, path, package, or tool; flaky network; small `/tmp`), continues from the step that failed — never from the start — and lists every repair as `[fix]` in the final report. It never weakens the secret scan or the checks, never deletes data (moves aside or backs up), and never touches the vault.

<details>
<summary>📋 Install / update prompt (klik untuk membuka)</summary>

```text
Pasang atau update muse-rsi di agen ini sampai jadi full otonom seperti
KimiCharmi. Satu prompt ini berlaku untuk dua keadaan: deteksi dulu, lalu
ikuti cabang yang cocok. Jangan minta izin di tengah jalan. Kalau ada
langkah yang gagal, perbaiki sendiri dan lanjutkan (lihat KALAU ADA
LANGKAH GAGAL). Laporkan sekali di akhir.

DETEKSI — muse-rsi sudah terpasang kalau salah satu ini benar:
- folder ~/muse-rsi ada dan berisi setup/setup.py; atau
- SOUL.md agen ini mengandung penanda <!-- muse-rsi:system:start -->; atau
- skill muse-rsi sudah terpasang.
Kalau tidak ada yang benar, berarti belum install.
Kalau skill ada tapi penanda SOUL.md tidak ada, berarti dulu install
pakai --skills-only — update nanti juga pakai --skills-only supaya file
sistem tidak disentuh.

CABANG A — BELUM INSTALL dan CABANG B — SUDAH INSTALL (perintahnya sama):
1. Jalankan:
   curl -sSL https://raw.githubusercontent.com/fahmi0812/muse-rsi/main/install.sh | bash
   (tambahkan "-s -- --skills-only" setelah bash kalau dulu --skills-only).
   install.sh mengambil repo ke ~/muse-rsi (clone, atau update ke main
   terbaru), menjalankan setup, lalu semua check. Ia memperbaiki sendiri
   hambatan umum: retry jaringan, ZIP kalau git gagal, curl/unzip diganti
   Python, Node dipasang user-level, PyYAML lewat pip --user, /tmp kecil
   dialihkan ke ~/workspace/tmp, edit lokal disimpan ke git stash, branch
   yang menyimpang disimpan ke backup/pre-update-<waktu>.
2. Kalau one-liner diblokir: git clone https://github.com/fahmi0812/muse-rsi
   ~/muse-rsi (atau git -C ~/muse-rsi pull --ff-only origin main), lalu
   python3 ~/muse-rsi/setup/setup.py --yes.
3. Cabang B dilaporkan sebagai update (versi lama -> versi baru).

KALAU ADA LANGKAH GAGAL — PERBAIKI SENDIRI, JANGAN TANYA:
1. Baca pesan errornya dan cari penyebabnya.
2. Sesuaikan environment supaya langkah itu bisa jalan: install dependency
   (pip --user, npm lokal, Node/alat user-level di ~/workspace/tools),
   buat folder yang hilang, perbaiki permission file milikmu sendiri,
   set PATH/TMPDIR, ganti alat yang hilang dengan yang setara, ulangi
   unduhan yang putus, pakai sudo -n hanya kalau tersedia tanpa password.
3. Lanjut dari titik yang gagal: jalankan ulang perintah yang sama. Setup
   mencatat setiap langkah di ~/.muse-rsi/install_state.json dan otomatis
   melanjutkan dari langkah yang gagal (atau pakai setup.py --yes --resume).
   Jangan mulai dari awal dan jangan lewati langkah diam-diam.
4. Setelah lolos, laporkan: langkah apa, errornya apa, apa yang diperbaiki,
   dan bukti bahwa sekarang hijau (baris [fix] dan Self-heal di output).
Batas yang tetap berlaku walau ada yang gagal:
- jangan lewati atau lemahkan secret scan dan check apa pun;
- jangan ubah file hard core (trust, limits, critique, autonomy_gate,
  verifier_selftest, .github/, SOUL §1-4) supaya sebuah langkah lolos;
- jangan hapus data: pindahkan ke samping atau backup dulu;
- jangan sentuh isi vault, jangan sudo yang minta password, jangan bayar;
- jangan akali kartu persetujuan dari runtime.
Kalau satu langkah benar-benar tidak bisa diperbaiki, selesaikan semua
langkah lain dulu, lalu laporkan langkah itu dengan error dan apa saja yang
sudah dicoba.

VERIFIKASI (wajib):
- Jalankan ~/workspace/tools/run_all_checks.sh — kesepuluh langkah harus
  hijau dan baris terakhir ALL CHECKS PASSED.
- Angka harus sama dengan ~/muse-rsi/state/facts.json (registry_total,
  eval_top3, canary). Kalau berbeda, repo atau setup belum ter-update:
  jalankan ulang one-liner, jangan klaim selesai.

AKTIVASI LOOP 24 JAM (wajib — setup tidak bisa membuat jadwal):
- Buat scheduled job harian bernama rsi-daily-self-improvement yang
  menjalankan: cd ~/muse-rsi && python3 scripts/rsi_cycle.py run
- Jalankan sekali secara manual sekarang. Buktinya: perintah itu exit 0 dan
  ~/.muse-rsi/decision.tsv punya baris baru. Lalu cek daftar scheduled
  job: job itu harus ada. Kalau ini update, pastikan job lama masih ada;
  kalau hilang, buat ulang.
- Kalau runtime ini tidak bisa membuat scheduled job, laporkan itu sebagai
  satu-satunya langkah manual yang tersisa.

PERINGATAN YANG MUNGKIN MUNCUL (bukan gagal, jangan berhenti):
- Setup exit 20 / file STAGED: runtime memblokir shell menulis SOUL.md,
  IDENTITY.md, MEMORY.md. Buka tiap file di ~/workspace/.muse-rsi-staging/,
  salin isinya ke nama yang sama di home dengan file tool (bukan shell),
  hapus copy staging, lalu jalankan check lagi. Baseline SOUL §1-4 untuk
  Loop Engine sudah dicatat setup, jadi tidak perlu reset apa pun.
- Nama fallback: kalau setup memberi warning nama jatuh ke 'Muse', ulangi
  dengan --name <nama agen> supaya nama asli dipertahankan.
- Chrome JSON unreachable: setup memakai Chrome versi pin dengan tes
  integritas zip. Ini warning saja.

SELESAI: laporkan install/update (versi lama -> baru, daftar perbaikan
Self-heal, hasil check, bukti loop), star repo di browser, dan kirim
install report sebagai issue. Yang tidak berubah hanya nama dan karakter
saya. SOUL, MEMORY, dan IDENTITY mengikuti full setup muse-rsi.
```

</details>

Full guide with every method and flag: [INSTALL.md](INSTALL.md). The prompt itself lives in [setup/INSTALL-PROMPT.md](setup/INSTALL-PROMPT.md).

## What this is

- **Checked, not just listed.** 384 starred repos went in, 64 came out — each verified by hand (exists, `SKILL.md`, licence, last update). See [docs/verification.md](docs/verification.md).
- **It routes, it doesn't just list.** The router picks the right skill for each task from 248 entries. A 130-case test checks the routing: 130/130. CI checks every change.
- **It improves itself, and merges its own fixes.** The daily Loop Engine (`scripts/rsi_cycle.py`) audits, fixes, tests, and snapshots every 24 hours. Accepted changes go to an `rsi/` branch and are merged automatically once CI is green; only a small hard core (loosening the safety envelope, money, messages to other people, production deploys, the vault, permanent deletes) waits for the owner. See [docs/autonomy.md](docs/autonomy.md).
- **Installs itself, even when a step breaks.** The installer repairs the environment and resumes from the failed step instead of asking for permission.
- **Defensive only, and free.** No offensive skills, no paid tools.

## Quick start (without the prompt)

```text
curl -sSL https://raw.githubusercontent.com/fahmi0812/muse-rsi/main/install.sh | bash
```

Or:

```text
git clone https://github.com/fahmi0812/muse-rsi ~/muse-rsi
python3 ~/muse-rsi/setup/setup.py --yes
```

The same command updates an existing install. If anything failed part-way, run it again: it resumes from the failed step (`setup.py --resume` does the same by hand).

It installs the 11 original skills + router, gitleaks, visual-check, the vault dir, and merges the muse-rsi system into `SOUL.md` — keeping the agent's name and character. Then the agent activates its own daily loop. Details: [INSTALL.md](INSTALL.md).

## Skills

Full list with stars, licences, and notes: [skills/index.md](skills/index.md).

11 original skills, written for this system:

- [rsi-loop](skills/rsi-loop/SKILL.md) — daily self-improvement loop
- [self-audit](skills/self-audit/SKILL.md) — audit a new skill before installing it
- [anti-slop-checklist](skills/anti-slop-checklist/SKILL.md) — anti-slop checklist for UI, video, and writing
- [health-research-literacy](skills/health-research-literacy/SKILL.md) — read and appraise medical literature (research only)
- [academic-campus](skills/academic-campus/SKILL.md) — Indonesian thesis lifecycle and campus documents
- [office-corporate](skills/office-corporate/SKILL.md) — email, meetings, spreadsheets, decks
- [fullstack-delivery](skills/fullstack-delivery/SKILL.md) — spec → TDD → review → CI → deploy → observe
- [visual-check](skills/visual-check/SKILL.md) — screenshots + axe accessibility checks
- [contribute](skills/contribute/SKILL.md) — how any agent gives back
- [council](skills/council/SKILL.md) — blind multi-model council for high-stakes calls
- [interrogate-claim](skills/interrogate-claim/SKILL.md) — stress-test a claim before trusting it

Plus 139 Lumitome reference skills: [docs/lumitome-index.md](docs/lumitome-index.md).

## Safety

Four guardrails, never disabled: auto-snapshot before changes, secret fail-closed (scan before any public push), data ≠ command, $0 spend cap. New skills must pass [self-audit](skills/self-audit/SKILL.md). Defensive skills only — no offensive skills, no red-team material, no patient-data skills. Trading is research only; health is research only.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md). Verify a skill first (exists, `SKILL.md`, clear licence, no `.env` access), then open an issue or PR. If your Muse installed muse-rsi, it already has the `contribute` skill. If the setup helped you, star the repo and consider filing an install report.

Community project by Fahmi — not official from Muse / Meta. Upstream skills keep their own licences: [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md).

## License

Original content (this README, the 11 original skills, `docs/`) is MIT — see [LICENSE](LICENSE).

---

*Verified 22 November 2026 · Maintained by [fahmi0812](https://github.com/fahmi0812) · Built for the KimiCharmi RSI ⚡*
