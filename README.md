# SSOT Buku — Satu Sumber Kebenaran untuk Skill Buku

**Status: DRAF v0.1 (28 Okt 2026). Belum live.**
Repo ini mendokumentasikan perapian skill-skill buku menjadi SATU sumber
kebenaran (SSOT) yang dipakai presisi per jenis di web produksi buku.

**Yang BELUM terjadi:** arsip skill lama di VPS, penyambungan SSOT ke web,
dan deploy. Sampai tiga itu terjadi, skill lama masih yang berlaku di
lapangan — repo ini adalah spesifikasi yang disetujui, bukan mesin yang
berjalan.

## Latar belakang (singkat)

Skill-skill buku tumbuh satu per satu sejak Juli 2026, masing-masing mencatat
perbaikan dan kecelakaannya sendiri, tanpa satu pun yang berkuasa atas yang
lain. Akibatnya: 5 "kebenaran" yang saling bertabrakan (gaya ilustrasi,
aturan sitasi, format, angka target, konfigurasi LLM). Audit 28 Okt 2026
membuktikan fondasinya ada tapi belum sempurna; inventaris Fase 1 mendaftarkan
semua aturan, duplikasi, dan kontradiksinya; putusan P-01..P-13 + koreksi
standar disetujui Boss 28 Okt malam dan menjadi isi SSOT ini.

## Isi repo

| Berkas | Isi |
|---|---|
| `SKILL.md` | Pintu tunggal: peta pemakaian, cara pakai, daftar putusan terkunci, changelog |
| `INTI-BERSAMA.md` | Aturan yang berlaku untuk SEMUA jenis (dengan label [STANDAR]/[HOUSE]/[GATE]/[TERBUKA]) |
| `PROFIL-referensi.md` | Profil buku referensi (pola acuan SSOT) |
| `PROFIL-monograf.md` | Profil monograf |
| `PROFIL-ajar.md` | Profil buku ajar OBE |
| `PROFIL-umum.md` | Profil buku umum |
| `PROFIL-chapter.md` | Profil book chapter |
| `PROFIL-anak.md` | Profil buku anak (PARSIAL — gaya presisi, isi ikut umum) |
| `PROFIL-pendidikan.md` | Profil buku pendidikan (PARSIAL — gaya presisi, isi ikut umum) |
| `periksa_ssot_buku.py` | Checker SSOT (stdlib saja; keluar 0 = tidak ada error) |
| `INVENTARIS-ATURAN-SKILL-BUKU.md` | Dokumen Fase 1: sumber, inti, profil awal, duplikasi, kontradiksi + rekomendasi, daftar arsip, kerangka SSOT, lembar putusan P-01..P-13, koreksi standar, putusan final |

## Putusan terkunci (28 Okt 2026)

- **P-01 ilustrasi:** umum = premium-konseptual; anak = clay 3D cerah;
  pendidikan = clay 3D kalem; infografis ikut paket masing-masing.
- **P-02 sitasi:** KETAT fail-closed untuk semua jenis akademik.
- **P-03 format:** referensi B5/TNR, umum B5/TNR, ajar B5 (boleh A5 bila
  dominan teks), monograf A5/Cambria, chapter A5/Cambria.
- **P-04 monograf:** janji 150–180 halaman; lantai kata ≥45.000; diagram 4.
- **P-05 chapter:** referensi akhir 8–10 (rentang).
- **P-06 approver:** Gate 1 operator = Boss; web = pelanggan.
- **P-07 peta:** Peta Bab = intro bab, bukan sub N.0.
- **P-08 singkatan:** Daftar Singkatan wajib bila singkatan teknis >20.
- **P-09 input:** jenis tanpa field inputnya = kartu "belum presisi".
- **P-10 provider:** konfigurasi LLM satu tempat di inti (9router + model hidup).
- **P-11 angka sitasi:** 5+/bab = pedoman lunak (bukan gate).
- **P-12 paragraf ajar:** ambang 60–100 kata (<50 gabung, >100 belah).
- **P-13 chapter:** rentang halaman 7–15.
- **Koreksi standar:** N.3 fungsional; Gate 5 sebagai proses; review per jenis;
  etik + anonimisasi monograf; rewrite skripsi-jadi-monograf; Bab 7 dua varian;
  TIU/TIK → CPMK/Sub-CPMK; gerbang keselarasan + kunci jawaban + Bacaan
  Lanjutan (ajar); endnotes + glosarium opsional + target rentang tanpa
  ganjalan (umum); brief editor didahulukan + abstrak bersyarat + objectives
  hanya volume ajar + dua varian chapter; edisi/errata; DPI cetak; KDT urusan
  penerbit. Detail lengkap ada di Bagian I dokumen inventaris.

## Cara memeriksa SSOT

```bash
python3 periksa_ssot_buku.py
```

Hasil terakhir yang terverifikasi (28 Okt 2026): **0 ERROR, 4 peringatan**
(ajar target halaman TERBUKA — menunggu ukur buku nyata; umum target halaman
TERBUKA — target lama 170+ tidak menutup, opsi naikkan kata/bab atau turunkan
target; anak/pendidikan PARSIAL).

## Tata kelola

- Ubah di SSOT, bukan di skill lama. Skill lama akan dipindah ke arsip
  baca-saja (pindah, bukan hapus).
- Setiap perubahan SSOT: changelog + tanggal + putusan Boss yang menguncinya.
- Kartu web hanya boleh bertanda 'siap' bila profil + mesin + gerbang
  ketiganya ada untuk jenis itu.
- Checker masuk gerbang deploy — SSOT rusak = deploy ditahan.
