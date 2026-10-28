# INTI BERSAMA — Aturan Semua Jenis Buku

Berlaku untuk referensi, monograf, ajar, umum, chapter, anak, pendidikan.
Bila profil jenis bertentangan dengan inti, inti menang — kecuali profil
menyatakan pengecualian eksplisit yang disetujui Boss.

## Label (wajib di semua aturan SSOT)

- **[STANDAR]** praktik universal penerbitan/akademik.
- **[HOUSE]** pilihan Boss; boleh di-override brief editor/penerbit/pelanggan.
- **[GATE]** bisa dicek mesin; checker menolak bila gagal.
- **[TERBUKA]** belum diputuskan; jangan diklaim standar.

## Aturan inti

- **[STANDAR] Gerbang manusia.** Outline disetujui SEBELUM produksi penuh
  (Gate 1); naskah jadi direview pakar sebelum final (Gate 5). Approver Gate 1
  dibedakan per jalur (P-06): operator = Boss; web = pelanggan. Pelanggan
  menyetujui outline bukunya sendiri, bukan mengubah standar.
- **[STANDAR] Review per jenis (proses, bukan hanya jumlah).** Referensi =
  ahli bidang; monograf = 1–2 reviewer sejawat; ajar = dosen sejawat + uji
  keterbacaan mahasiswa; chapter = editor volume; umum = editor naskah +
  fact-checker. Tulis kriteria reviewer, apa yang direview, dan log revisi.
- **[STANDAR] Tanpa karangan.** Tidak menambah data/angka/responden/lokasi/
  hasil yang tidak ada di bahan. Sitasi hanya dari daftar terverifikasi
  (search-then-lock). Anekdot/kisah nyata wajib bersumber (boleh non-jurnal:
  berita, laporan resmi); tanpa sumber = beri label ilustrasi hipotetis
  ('Ilustrasi:' / 'Misalkan...').
- **[GATE] Sitasi KETAT fail-closed (P-02).** Untuk semua jenis akademik:
  sitasi tak terverifikasi = ditolak (bukan sekadar flag). Verifikasi 3 lapis
  untuk referensi (eksistensi → atribusi → makna); untuk jenis lain minimal
  eksistensi + atribusi. Kueri pencarian WAJIB dibersihkan dari nama author +
  tahun (kueri terkontaminasi = hasil tidak relevan).
- **[STANDAR] Sitasi per-klaim, bukan angka (P-11).** Angka per bab (mis. 5+)
  hanya pedoman lunak untuk perencanaan, BUKAN gate. Yang diuji: tiap klaim
  faktual ada sumbernya. Metrik "coverage %" DIHAPUS sampai didefinisikan.
- **[STANDAR] 0 markdown di cetak.** Asterisk, underscore, backtick dilarang;
  istilah asing miring; EYD; satu istilah = satu makna di seluruh buku.
- **[STANDAR] Margin 2 cm semua sisi** untuk semua jenis.
- **[STANDAR] Nomor halaman footer (field PAGE, center)**, semua halaman
  kecuali cover. Aturan page break per jenis ada di profil (tidak diseragamkan).
- **[GATE] Fail-closed QC.** Exit code 0 ≠ sukses. Cek artefak langsung:
  berkas ada + ukuran non-trivial; jumlah paragraf/tabel/kata; 0 placeholder
  bocor (`[TABEL]`, `[/TABEL]`, `@@TABLEBLOCK`, `[Section gagal dibuat]`,
  `[Section kosong]`); media gambar yang dijanjikan benar-benar ada di docx.
  Gagal = perbaiki + ulang, jangan kirim.
- **[STANDAR] BCP Council 4 agen** (Architect → Skeptic → Pragmatist → Editor)
  + chunking per sub-bab (800–1200 kata/panggilan) + ringkasan berjalan antar
  bab (koherensi). Satu unit argumen tidak boleh terbelah dua chunk (khusus
  perbandingan dan posisi penulis referensi: besarkan chunk, jangan belah).
- **[STANDAR] Penanda visual.** Tabel/diagram ditulis lewat marker
  `[TABEL]...[/TABEL]` / `[DIAGRAM ...]`, dirender ke docx, marker dicabut
  SEBELUM penilai bentuk bekerja. Label ditempel SESUDAH gambar jadi, tidak
  pernah diminta ke model gambar.
- **[GATE] Tanpa fallback diam-diam.** Jenis yang dipilih user tidak boleh
  jatuh ke `umum` tanpa ketahuan; jenis WAJIB diteruskan ke semua fungsi
  (brief, label, infografis). Gerbang memeriksa ini.
- **[STANDAR] Tanpa hardcode.** Penulis, CV penulis, doc ID, dan nama berkas
  WAJIB dinamis dari input/bab yang sedang diproduksi.
- **[STANDAR] Tanpa kunci di dokumen; tanpa font berlisensi/komersial di repo
  publik.** Dokumen SSOT tidak boleh memuat fragmen kunci apa pun.
- **[STANDAR] Daftar hitam budaya ilustrasi (Indonesia)** berlaku untuk semua
  gambar buku.
- **[STANDAR] PDF Turnitin = A4** (tidak boleh diubah ke A5); DOCX buku =
  ukuran jenisnya (lihat profil). **[TERBUKA]** Apa yang sebenarnya
  diverifikasi "pre-check Turnitin" bila modenya mock-up — jangan diklaim
  sebagai cek kesamaan beneran sampai dijelaskan.
- **[HOUSE] Konfigurasi LLM satu tempat (P-10).** Gateway + model yang hidup
  sekarang (9router) ditulis di sini, bukan di tiap profil. Profil/skill
  dilarang menulis endpoint/model sendiri. Bila gateway berganti, ubah di
  sini sekali.
- **[STANDAR] Edisi / revisi / errata.** Semua jenis punya aturan pencatatan
  koreksi dan edisi baru (khususnya referensi dan ajar yang hidup dari edisi
  revisi). Edisi baru tidak menimpa edisi lama tanpa catatan perubahan.
- **[STANDAR] Resolusi gambar minimal untuk cetak (DPI)** dicantumkan di
  profil visual tiap jenis (melengkapi aturan ukuran berkas).
- **[STANDAR] KDT adalah urusan penerbit** (diterbitkan Perpusnas, ditempel
  penerbit — bukan ditulis penulis); tidak boleh hilang dari anatomi (tulis
  sebagai "diisi penerbit", seperti ISBN).

## BLOK ANGKA (dibaca checker — jangan ubah format baris ini)

checker_scope: profil
wajib_section: Definisi, Input wajib, Anatomi, Struktur bab, Sitasi, Visual, Format, Gerbang
larang_string: enowx, 172.17.0.1, LENIENT
wajib_label: [STANDAR], [HOUSE], [GATE]
