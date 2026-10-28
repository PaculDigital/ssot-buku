# PROFIL: Buku Referensi

## Definisi

**[STANDAR]** Karya ilmiah yang menjadi RUJUKAN otoritatif di suatu bidang
ilmu. Pembaca membukanya untuk merujuk: definisi baku, peta teori mutakhir,
dan pendirian penulis. BUKAN buku ajar (pedagogis), BUKAN buku umum (naratif),
BUKAN monograf (satu riset spesifik), BUKAN ensiklopedia/tinjauan literatur
(tanpa suara penulis).

## Input wajib

**[GATE]** Judul + bidang ilmu; penulis (nama + gelar + afiliasi + kepakaran);
jumlah bab (default 8–12); ukuran/font; pustaka terpusat di akhir atau per bab;
bahan (tema / naskah kajian / outline); pakar reviewer (Gate 5). Form web
WALIB meminta semua input ini sebelum produksi (P-09).

## Anatomi

**[STANDAR]** Cover → Hak Cipta/ISBN (diisi penerbit) → Kata Pengantar
ILMIAH (urgensi bidang, kontribusi, posisi penulis — BUKAN hook anekdot) →
Daftar Isi + Daftar Tabel + Daftar Gambar → Daftar Singkatan (wajib bila
singkatan teknis >20, P-08) → BAB 1 Pendahuluan (peta buku: ruang lingkup,
batasan, istilah kunci, struktur bab) → BAB 2..N-1 inti → BAB N Penutup
(sintesis lintas bab + agenda riset, bukan sekadar rangkuman) → Glosarium
(wajib bila >20 istilah teknis, tabel 2 kolom) → Indeks Subjek + Indeks Nama
(WAJIB) → Daftar Pustaka (APA 7) → Tentang Penulis (kredensial ilmiah).

## Struktur bab

**[STANDAR]** Intro = Peta Bab (P-07: Peta BUKAN sub bernomor N.0) → N.1
Definisi dan Konsep Kunci (dari SUMBER PRIMER) → N.2 Perkembangan Teori →
N.3 Perbandingan Kritis → N.4 Posisi dan Sintesis Penulis (EKSPLISIT, tidak
boleh netral hambar) → N.5 Implikasi (teoretis dan/atau praktis) → Ringkasan
Bab formal (poin substansi, bukan paragraf mengalir). Lima unsur N.1–N.5 =
GATE: bab kehilangan satu unsur = bab belum lolos.
**[STANDAR]** N.3 = FUNGSI membandingkan: tabel komparasi ATAU prosa
komparatif terstruktur, dipilih sesuai isi (tabel di setiap bab bukan standar).
**[HOUSE]** Contoh kalimat posisi benar vs salah ada di inventaris (N.4):
posisi harus menyebut teori, konteks, alasan, dan keterbatasan.

## Sitasi

**[STANDAR]** Per-klaim, bukan angka per bab (P-11). Setiap klaim faktual →
sitasi; definisi → sumber primer; angka/data → sumber asli (bukan sekunder);
atribusi teori (tokoh + tahun + karya) → terverifikasi. Hierarki: primer >
sekunder; temuan empiris mutakhir (≤5 tahun); teori induk = karya klasik
pencetusnya. Posisi penulis (N.4) TIDAK butuh sitasi, tapi harus berdiri di
atas N.3 yang bersitasi. Pedoman lunak (bukan gate): 10–25 sitasi/bab.
**[GATE]** Verifikasi 3 lapis: eksistensi (OpenAlex/Crossref, judul + DOI) →
atribusi (tokoh/tahun/karya tidak tertukar) → makna (klaim selaras
abstrak/kesimpulan sumber). Sitasi fiktif lolos = bab ditolak, generate ulang
dari nol. LLM hanya mengutip dari daftar terverifikasi yang di-feed ke prompt.

## Visual

**[STANDAR]** Tabel komparasi/bab (atau prosa komparatif, lihat Struktur);
bagan alir / peta konsep minimal 1/bab; tabel data hanya dari data nyata +
sumber. **[HOUSE]** Ilustrasi 3D dekoratif DILARANG untuk referensi; visual
harus informatif. Tabel pakai Table Grid (border wajib); caption bernomor
(Tabel N.M, Gambar N.M).

## Format

**[HOUSE]** B5 (17.6 × 25.0 cm), Times New Roman 12pt, spasi 1.15, margin 2 cm,
footer PAGE (kecuali cover), page break sebelum setiap bab. Target 150+
halaman, 8–12 bab. Nomor halaman indeks WAJIB dari render nyata (bukan
perkiraan kata/halaman — metode perkiraan 360 kata/halaman sudah diarsip).

## Gerbang

**[GATE]** Gate 1 outline (cakupan tidak tumpang tindih, alur logis,
disetujui approver jalur: operator = Boss, web = pelanggan) → Gate 2
verifikasi fakta per bab (3 lapis bersih) → Gate 3 konsistensi terminologi
(satu istilah = satu makna, cek via state file) → Gate 4 kelengkapan perangkat
(indeks subjek + nama + glosarium bila syarat + daftar pustaka) → Gate 5
review pakar (PROSES: kriteria reviewer, apa yang direview, log revisi
tertulis). Gerbang mesin: R1 indeks subjek bermakna, R2 indeks nama bermakna,
R3 perbandingan kritis nyata per bab, R4 paragraf posisi penulis (frasa
posisi, ≥10 kata), Rw glosarium + singkatan. Indeks: hanya istilah/nama yang
didefinisikan/dibahas substantif + rujukan silang "lihat juga".

## BLOK ANGKA (dibaca checker — jangan ubah format baris ini)

kata_per_bab_min: 4000
kata_per_bab_max: 6000
jumlah_bab_min: 8
jumlah_bab_max: 12
kata_per_halaman: 400
target_halaman_min: 150
status_target: TETAP
status_profil: TETAP
