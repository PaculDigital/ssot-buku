# PROFIL: Book Chapter

## Definisi

**[STANDAR]** SATU bab buku kolaborasi (edited volume) — kontribusi ilmiah
yang mandiri sekaligus pas dengan tema volume. BUKAN buku komplit/multi-bab.
Sesudah selesai: serahkan file; DILARANG menawar "Mau lanjut bab berikutnya?".

## Input wajib

**[GATE]** Nomor bab (int 1–99); judul bab; **[STANDAR]** BRIEF EDITOR
VOLUME DIDAHULUKAN: tema volume, batas kata, gaya sitasi, format, deadline,
proses review. Format rumah hanya berlaku bila editor tidak memberi
spesifikasi. Judul buku opsional (konteks antar-bab). CV penulis dari input
pemesanan — **[STANDAR]** DILARANG hardcode CV. Form web WAJIB meminta brief
editor + CV sebelum produksi (P-09).

## Anatomi

**[STANDAR]** Abstrak + kata kunci (bersyarat: bila volume memintanya) →
BAB N + judul (centered, 14pt bold, BUKAN 20pt) → 15 section (lihat Struktur
bab) → Referensi → Glosarium → CV Penulis (nama, email, biodata singkat,
format bio volume bila ada).

## Struktur bab

**[STANDAR]** A Pendahuluan (5–6 paragraf formal + kalimat "Setelah
mempelajari bab ini..." + 6 learning objectives a–f HANYA untuk volume ajar;
volume riset: masalah + argumen + kontribusi, TANPA objectives) → B Konsep
dan Karakteristik → C Proses → D Pendekatan → E Faktor yang Memengaruhi →
F Bias Kognitif dan Risiko → G Alat Bantu → H Era Digital dan AI → I Etika,
Tata Kelola, dan Keberlanjutan → J Ilustrasi Kasus → K Prinsip Praktis
(bullet 10 prinsip) → L Ringkasan Bab (bullet 6 poin) → M DILOMPATI (penanda
saduran BAB 7 — dicatat, bukan disembunyikan) → N Referensi → O Glosarium
(TABEL 2 kolom, bukan daftar teks) → CV Penulis.
**[HOUSE]** Judul section memakai `{judul_short}` (frasa inti judul; potong
di koma kedua, jangan potong tengah kata/angka; sanitasi `{`/`}` → `(`/`)`
sebelum `.format()`). Section A–L MENGALIR (tanpa page break antar section);
page break SEBELUM N dan O. **[HOUSE]** Dua varian chapter: riset (default)
vs ajar (objectives + aparat ajar) — template 15 section saat ini adalah
template chapter ajar; varian riset memakai struktur yang sama TANPA
objectives.
**[GATE]** Paragraf: belah bila >80 kata (prioritas: akhir kalimat → koma →
hard split); body 11pt justified, left_indent 0.5cm, first_line_indent 1.0cm.

## Sitasi

**[STANDAR]** OpenAlex per bab (topik + tahun ≥2020, kueri dibersihkan dari
nama author + tahun, sort relevance) + classic refs; search-then-lock.
**[GATE]** Verifikasi KETAT fail-closed (P-02). Referensi akhir = rentang
8–10 (P-05), output SEMUA final_refs (dedup surname+tahun, sort alfabetis),
hanging indent 0.5″, APA 7 — KECUALI gaya sitasi volume editor menentukan
lain (brief editor menang).

## Visual

**[STANDAR]** 1 diagram matplotlib/bab, rotasi 6 template per `bab_num % 6`
(hub-and-spoke, flowchart horizontal, hierarchy tree, process flow vertikal,
pyramid, matrix grid) + 6 palet berotasi; label spoke dari keyword judul.
Tulis ke OUTPUT_DIR (bukan /tmp); gagal = jalan tanpa diagram, tidak crash.
Tabel konten hanya di section B–G (marker di section lain di-extract =
silent drop, acceptable). Tabel: Table Grid, header bold 10pt centered, isi
10pt, lebar kolom = total 14cm dibagi rata, caption bold 11pt di atas tabel.

## Format

**[HOUSE]** DOCX A5 (5.83″ × 8.27″), margin 2 cm, Cambria 11pt body / 14pt
judul + heading (TANPA warna, hitam polos); PDF Turnitin = A4 (tidak terikat
batas halaman chapter). **[GATE]** Rentang halaman DOCX A5: 7–15 (P-13).
Kata terverifikasi contoh BAB 4: ~4000–5000 kata ≈ 15 halaman.

## Gerbang

**[GATE]** QC fail-closed (paling lengkap): 2 berkas ada + ukuran non-trivial;
baca docx (paragraf/tabel/kata/sel tabel); 0 `[Section gagal dibuat]` /
`[Section kosong]`; ekstrak PDF (halaman >0, teks substansial); cek ZIP/XML
(0 placeholder bocor); cek `word/media/` (diagram ada; gagal matplotlib =
visual hilang, bukan sukses); ukuran halaman (DOCX A5, PDF A4). Gagal =
jangan kirim link, perbaiki + ulang. **[STANDAR]** Review: editor volume
( + reviewer bila volume memakainya).

## BLOK ANGKA (dibaca checker — jangan ubah format baris ini)

kata_total_min: 2331
kata_total_max: 4995
kata_per_halaman: 333
target_halaman_min: 7
target_halaman_max: 15
status_target: TETAP
status_profil: TETAP
