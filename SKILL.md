# SSOT Buku — Pintu Tunggal Skill Buku

**Status: DRAF v0.1 (28 Okt 2026). Belum live.** Draf ini ditulis sesudah
putusan final P-01..P-13 dan koreksi standar (Bagian I inventaris). Yang BELUM
terjadi: arsip skill lama di VPS, penyambungan ke web, dan deploy. Sampai tiga
itu terjadi, skill lama masih yang berlaku di lapangan — dokumen ini adalah
spesifikasi yang disetujui, bukan mesin yang berjalan.

## Peta: mana yang dipakai untuk apa

| Minta | Pakai |
|---|---|
| Buku referensi | `PROFIL-referensi.md` |
| Monograf | `PROFIL-monograf.md` |
| Buku ajar OBE | `PROFIL-ajar.md` |
| Buku umum | `PROFIL-umum.md` |
| Book chapter | `PROFIL-chapter.md` |
| Buku anak / pendidikan | `PROFIL-anak.md` / `PROFIL-pendidikan.md` (status PARSIAL — gaya presisi, isi ikut umum) |
| Artikel jurnal (SINTA/IMRaD) | BUKAN di sini — skill induk penelitian-ilmiah (artikel), jangan dicampur |
| Gabung bab, nomor halaman | Pendukung rakit-docx-aman (tetap berlaku, menunjuk ke SSOT) |
| Gambar hilang dari docx | Pendukung diagnosa-gambar-hilang-docx (tetap berlaku) |
| Ilustrasi / infografis / diagram | Aturan visual di profil jenis + inti (gaya per P-01) |

**Jangan baca skill lama untuk produksi baru.** Skill lama (`buku-referensi`,
`buku-monograf`, `buku-ajar-obe`, `buku-umum`, `book-chapter` di VPS) akan
dipindah ke arsip baca-saja. Bila isi dokumen ini bertentangan dengan skill
lama, dokumen ini yang menang (putusan Boss 28 Okt 2026).

## Cara pakai (agen / operator / mesin)

1. Baca `INTI-BERSAMA.md` (aturan yang berlaku semua jenis).
2. Baca SATU profil sesuai jenis yang dipesan. Jangan campur aparat antar jenis
   (objectives hanya untuk ajar/volume ajar; APA in-text hanya untuk jenis
   akademik; glosarium wajib hanya di referensi/monograf/ajar sesuai profil).
3. Periksa label tiap aturan: **[STANDAR]** (praktik universal — tidak boleh
   dilanggar tanpa alasan tertulis), **[HOUSE]** (pilihan Boss — boleh
   di-override brief editor/penerbit/pelanggan bila mereka memberi spesifikasi
   sendiri), **[GATE]** (bisa dicek mesin — checker menolak bila gagal),
   **[TERBUKA]** (belum diputuskan — jangan diklaim sudah standar).
4. Jalankan `python3 periksa_ssot_buku.py` sebelum menyatakan SSOT sehat.
   Checker lolos = tidak ada kontradiksi/angka tak menutup; item TERBUKA dan
   PARSIAL tetap dilaporkan (mereka memblokir klaim 'siap' untuk jenis itu,
   bukan seluruh SSOT).
5. Kartu web hanya boleh bertanda 'siap' bila profil + mesin + gerbang
   ketiganya ada untuk jenis itu (P-09).

## Putusan terkunci (28 Okt 2026 — jangan diubah tanpa Boss)

- **P-01 ilustrasi:** umum = premium-konseptual (navy/terracotta/krem, satu
  metafora, bukan 3D); anak = clay 3D cerah; pendidikan = clay 3D kalem;
  infografis ikut paket masing-masing.
- **P-02 sitasi:** KETAT fail-closed untuk semua jenis akademik; umum dicek
  faktanya lewat endnotes.
- **P-03 format:** referensi B5/TNR, umum B5/TNR, ajar B5 (boleh A5 bila
  dominan teks), monograf A5/Cambria, chapter A5/Cambria.
- **P-04 monograf:** janji 150–180 halaman; lantai kata ≥45.000; diagram 4
  (Bab 3/5/6/7). Konsekuensi: produksi ±2× hitungan lama.
- **P-05 chapter:** referensi akhir 8–10 (rentang, bukan angka mati).
- **P-06 approver:** Gate 1 operator = Boss; web = pelanggan.
- **P-07 peta:** Peta Bab = intro bab, bukan sub N.0.
- **P-08 singkatan:** Daftar Singkatan wajib bila singkatan teknis >20 +
  generator dibangun di fase mesin.
- **P-09 input:** jenis tanpa field inputnya = kartu "belum presisi";
  anak/pendidikan PARSIAL sampai profil lengkap.
- **P-10 provider:** konfigurasi LLM satu tempat di inti (9router + model hidup).
- **P-11 angka sitasi:** 5+/bab = pedoman lunak (bukan gate); metrik coverage %
  dihapus.
- **P-12 paragraf ajar:** ambang 60–100 kata (<50 gabung, >100 belah).
- **P-13 chapter:** rentang halaman 7–15.
- **Koreksi standar (Bagian I inventaris):** N.3 fungsional; Gate 5 sebagai
  proses; review per jenis; etik + anonimisasi monograf; rewrite
  skripsi-jadi-monograf; Bab 7 dua varian; TIU/TIK → CPMK/Sub-CPMK; gerbang
  keselarasan + kunci jawaban + Bacaan Lanjutan (ajar); endnotes + glosarium
  opsional + target rentang tanpa ganjalan (umum); brief editor didahulukan +
  abstrak bersyarat + objectives hanya volume ajar + dua varian chapter;
  edisi/errata; DPI cetak; KDT urusan penerbit.

## Changelog

- **v0.1 (28 Okt 2026, DRAF):** ditulis dari inventaris Fase 1 + putusan final
  P-01..P-13 + koreksi standar. Belum diarsip, belum disambung web, belum
  deploy. Item TERBUKA: target halaman ajar (menunggu ukur buku nyata),
  target halaman umum (opsi: naikkan kata/bab atau turunkan target dari 170+),
  profil anak/pendidikan (PARSIAL).
- **Aturan tata kelola:** ubah di SSOT, bukan di skill lama. Setiap perubahan:
  changelog + tanggal + putusan Boss yang menguncinya. Review agen Boss tetap
  berlaku (Wulan verifikasi ke berkas nyata sebelum memperbaiki).

## Berkas di folder ini

- `INTI-BERSAMA.md` — aturan semua jenis.
- `PROFIL-<jenis>.md` — satu per jenis (7 berkas). Tiap profil punya BLOK
  ANGKA yang dibaca checker — jangan ubah format barisnya.
- `periksa_ssot_buku.py` — checker (stdlib saja; keluar 0 = tidak ada error,
  item TERBUKA/PARSIAL dilaporkan sebagai peringatan).
- `INVENTARIS-ATURAN-SKILL-BUKU.md` — dokumen Fase 1 (sumber + kontradiksi +
  lembar putusan + koreksi standar).
