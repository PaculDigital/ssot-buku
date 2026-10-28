# INVENTARIS ATURAN SKILL BUKU — SSOT Buku Fase 1

**Tanggal:** 28 Okt 2026 malam. **Status:** DRAF inventaris untuk putusan Boss.
**Yang sudah terjadi:** inventaris selesai dibaca dan didaftar. **Yang BELUM terjadi:**
tidak satu pun skill lama diubah, tidak satu pun aturan baru diberlakukan.
Perubahan hanya mulai sesudah Boss menjawab Lembar Putusan (bagian H).

**Cara baca dokumen ini:** Bagian A = apa saja sumbernya. Bagian B = aturan yang
diusulkan jadi INTI BERSAMA (berlaku semua jenis). Bagian C = aturan PER JENIS
(hanya yang benar-benar beda). Bagian D = duplikasi (satu aturan di banyak tempat).
Bagian E = kontradiksi (dua sumber bilang beda — butuh putusan Boss).
Bagian F = yang basi dan harus pindah ke arsip. Bagian G = kerangka SSOT yang
akan ditulis di Fase 2. Bagian H = lembar putusan — Boss jawab dengan nomor.

---

## A. Sumber yang diinventaris

Semua berkas dibaca langsung dari VPS (`/opt/data/skills/`), 28 Okt 2026.

| # | Berkas | Ukuran | Tgl | Peran | Status |
|---|---|---|---|---|---|
| S-01 | `penelitian-ilmiah/buku-referensi/SKILL.md` | 14.692 B | 17 Okt | Skill buku referensi | Aktif — paling presisi |
| S-02 | `penelitian-ilmiah/buku-monograf/SKILL.md` | 14.740 B | 17 Okt | Skill monograf | Aktif — angka bermasalah |
| S-03 | `penelitian-ilmiah/buku-ajar-obe/SKILL.md` | 98.982 B | 17 Okt | Skill buku ajar OBE | Aktif — paling menggembung |
| S-04 | `penelitian-ilmiah/buku-umum/SKILL.md` | 53.771 B | 19 Okt | Skill buku umum | Aktif — doktrin paling matang |
| S-05 | `penelitian-ilmiah/book-chapter/SKILL.md` | 23.603 B | 17 Okt | Skill book chapter | Aktif — paling operasional |
| S-06 | `penelitian-ilmiah/SKILL.md` (induk) | ~919 baris | v2.2.0, 12 Agu | Workflow ARTIKEL jurnal (SINTA/IMRaD, kanban) | Aktif — BUKAN ruter buku |
| S-07 | `penelitian-ilmiah/rakit-docx-aman/SKILL.md` | 16.243 B | — | Gabung bab + nomor halaman | Pendukung — matang |
| S-08 | `penelitian-ilmiah/diagnosa-gambar-hilang-docx/SKILL.md` | 23.946 B | — | Diagnosis gambar hilang dari docx | Pendukung — matang |
| S-09 | `creative/ai-book-illustration/SKILL.md` | 40.957 B | v2 kunci 18 Okt | Ilustrasi + infografis + diagram buku | Pendukung — gaya bertentangan (E-01) |
| S-10 | `publishing/template-buku-resmi/SKILL.md` | 10.944 B | — | Template + angka XML + gerbang | Pendukung — tipis tapi disiplin |
| S-11 | `.archive/book_chapter/SKILL.md` | 6.516 B | 18 Agu | Chapter versi lama | Arsip — sudah tergantikan (lihat F) |
| S-12 | `penelitian-ilmiah/buku-ajar-obe/references/` (21 dok) | — | Jul–Agu | Jurnal debug/audit/uji | Sejarah — BUKAN spesifikasi |
| S-13 | `penelitian-ilmiah/buku-umum/scripts/` (gerbang dkk) | — | — | Gerbang jenis/tone/menu/penyusunan | Mesin pendukung — hidup |
| S-14 | Repo `template-buku-resmi/jenis/*/` | — | — | `profil.json` + SPESIFIKASI 5/5 jenis | BIBIT SSOT mesin (sudah ada) |

**Yang diverifikasi masih hidup di server:** `scripts/book_chapter_pipeline.py`,
`scripts/monograf_pipeline.py`, `scripts/similarity_precheck.py`, `.venv`,
`bcp_phase3_visual.py` — semua ADA. Jadi yang basi adalah konfigurasi dan
angka di dalam skill, bukan jalannya.

**Yang TIDAK punya skill tapi dijual web:** paket `anak` dan `pendidikan`.
Keduanya hanya punya paket gaya (doktrin 18 Okt) + arah tone — tidak punya
anatomi, gerbang, atau aturan isi sendiri. Lihat kontradiksi E-09.

---

## B. Register aturan INTI BERSAMA (usulan — berlaku semua jenis)

Aturan di bawah ini muncul di ≥2 skill dengan isi yang sama. Di SSOT, aturan
ini ditulis SEKALI di inti, dan profil jenis hanya menunjuk — tidak menyalin.

| ID | Aturan | Sumber |
|---|---|---|
| I-01 | **Gerbang manusia:** outline disetujui SEBELUM produksi penuh; naskah jadi direview pakar sebelum final (Gate 1 + Gate 5) | S-01, S-02, S-03, S-04, S-05 |
| I-02 | **Tanpa karangan:** tidak menambah data/angka/responden/lokasi/hasil yang tidak ada di bahan; sitasi hanya dari daftar terverifikasi (search-then-lock); anekdot/kisah nyata wajib bersumber, kalau tidak ada sumber beri label ilustrasi hipotetis | S-01, S-02, S-03, S-04, S-05 |
| I-03 | **Kueri bersih:** saat mencari referensi, buang nama author + tahun dari kueri (kueri terkontaminasi = hasil tidak relevan) | S-01, S-02, S-05 |
| I-04 | **0 markdown di cetak:** asterisk, underscore, backtick dilarang; istilah asing miring; EYD | S-01, S-03, S-04, S-05 |
| I-05 | **Margin 2 cm semua sisi** untuk semua jenis | S-01, S-02, S-03, S-04, S-05 |
| I-06 | **Nomor halaman footer (field PAGE, center)**, semua halaman kecuali cover | S-01, S-02, S-03, S-04 |
| I-07 | **Fail-closed QC:** exit code 0 ≠ sukses; cek artefak langsung (jumlah paragraf/tabel/kata, 0 placeholder bocor `[TABEL]`, `@@TABLEBLOCK`, `[Section gagal dibuat]`, `[Section kosong]`); gagal = perbaiki + ulang, jangan kirim | S-02, S-05, S-07 |
| I-08 | **BCP Council 4 agen** (Architect → Skeptic → Pragmatist → Editor) + chunking per sub-bab (800–1200 kata/panggilan) + ringkasan berjalan antar bab (koherensi) | S-01, S-02, S-03, S-04 |
| I-09 | **Penanda visual:** konten tabel/diagram ditulis lewat marker `[TABEL]...[/TABEL]` / `[DIAGRAM ...]`, dirender jadi tabel/docx, marker dicabut sebelum penilai bentuk bekerja | S-02, S-03, S-05, S-09 |
| I-10 | **Tanpa fallback diam-diam:** jenis yang dipilih user tidak boleh jatuh ke `umum` tanpa ketahuan; jenis WAJIB diteruskan ke semua fungsi (brief, label, infografis) | S-04, S-09 |
| I-11 | **Tanpa hardcode:** penulis, CV penulis, doc ID, dan nama berkas WAJIB dinamis dari input/bab yang sedang diproduksi | S-02, S-05 |
| I-12 | **Tanpa kunci di dokumen; tanpa font berlisensi/komersial di repo publik** | S-05 (kunci — dilanggar, lihat F), S-10 (font) |
| I-13 | **Daftar hitam budaya ilustrasi (Indonesia)** — berlaku untuk semua gambar buku | S-09 |
| I-14 | **PDF Turnitin = A4** (tidak boleh diubah ke A5); DOCX buku = ukuran jenisnya (lihat C) | S-02, S-05 |

**Catatan:** I-02 soal sitasi hanya intinya yang bersama. KETAT vs LONGGAR-nya
berbeda antar skill — itu kontradiksi E-02, bukan inti.

---

## C. Register PER JENIS (hanya yang benar-benar beda)

### C-1. Buku referensi (S-01) — pola acuan SSOT

- **Definisi:** rujukan otoritatif bidang ilmu; pembaca merujuk, bukan dibacakan cerita. BUKAN ajar (pedagogis), BUKAN umum (naratif), BUKAN monograf (satu riset spesifik), BUKAN ensiklopedia/tinjauan literatur (tanpa suara penulis).
- **Input wajib:** judul + bidang, penulis (nama+gelar+afiliasi+kepakaran), jumlah bab (default 8–12), ukuran/font, pustaka terpusat/per bab, bahan (tema/naskah/outline), pakar reviewer.
- **Anatomi:** Cover → Hak Cipta/ISBN → Kata Pengantar ILMIAH → Daftar Isi+Tabel+Gambar → Daftar Singkatan (WAJIB) → BAB 1 Pendahuluan (peta buku) → BAB 2..N-1 inti → BAB N Penutup (sintesis lintas bab + agenda riset) → Glosarium (wajib bila >20 istilah) → Indeks Subjek + Indeks Nama (WAJIB) → Daftar Pustaka (APA 7) → Tentang Penulis.
- **Struktur bab:** N.0 Peta Bab → N.1 Definisi/Konsep Kunci (sumber primer) → N.2 Perkembangan Teori → N.3 Perbandingan Kritis (TABEL komparasi WAJIB) → N.4 Posisi/Sintesis Penulis (EKSPLISIT, kalimat posisi contoh benar/salah ada) → N.5 Implikasi → Ringkasan Bab formal (poin, bukan paragraf mengalir). Lima unsur N.1–N.5 = GATE.
- **Sitasi:** PER-KLAIM, bukan angka per bab (koreksi eksplisit atas mitos ≥15/bab; pedoman lunak 10–25/bab hanya untuk perencanaan, bukan gate). Hierarki primer > sekunder; empiris mutakhir ≤5 tahun; posisi penulis (N.4) tidak butuh sitasi tapi harus berdiri di atas N.3 yang bersitasi.
- **Verifikasi 3 lapis:** eksistensi (OpenAlex/Crossref, judul+DOI) → atribusi (tokoh+tahun+karya tidak tertukar) → makna (klaim selaras abstrak/kesimpulan). Sitasi fiktif lolos = bab ditolak, generate ulang dari nol.
- **Tone:** akademik-presisi (kalimat definisional, satu istilah = satu makna, suara penulis hadir; BUKAN ensiklopedia kering, BUKAN hook anekdot).
- **Visual:** tabel komparasi wajib/bab; bagan/peta konsep minimal 1/bab; tabel data hanya dari data nyata; ilustrasi 3D dekoratif DILARANG.
- **Format + hitung:** B5, TNR 12pt, spasi 1.15, target 150+ halaman, 8–12 bab. Hitung kasar: 8–12 bab × ~5 sub × 800–1200 kata ≈ 32.000–72.000 kata; pada ~400 kata/halaman B5 ≈ 80–180 halaman — target 150+ hanya tercapai di ujung atas. **SSOT wajib menulis asumsi kata/halaman dan anggaran kata per bab (bukan hanya target halaman).**
- **Gerbang:** Gate 1 outline (cakupan tidak tumpang tindih, alur logis) → Gate 2 verifikasi fakta/bab → Gate 3 konsistensi terminologi (state file) → Gate 4 kelengkapan perangkat → Gate 5 review pakar.
- **Kekurangan yang dicatat (bukan dihapus):** nomor halaman indeks masih dijelaskan dari perkiraan 360 kata/halaman (mesin baru sudah pakai nomor render nyata); Daftar Singkatan wajib tapi tanpa pembangun; Peta N.0 ambigu (sub vs intro, lihat E-07); approver Gate 1 ambigu (Bos vs pelanggan web, lihat E-06); pointer modul indeks menunjuk lokasi lama proyek.

### C-2. Monograf (S-02)

- **Definisi:** satu hasil penelitian spesifik dikupas sangat dalam. BUKAN tema bebas, BUKAN RPS.
- **Input wajib:** naskah penelitian (skripsi/tesis/jurnal/laporan, DOCX/PDF). Default penulis = nama Boss (lihat F: hardcode berbahaya untuk pelanggan).
- **Anatomi:** Cover → Hak Cipta/ISBN → Kata Pengantar (dinamis) → Daftar Isi+Tabel+Gambar → 8 BAB → Daftar Pustaka (APA 7, hanging indent) → Glosarium (tabel 2 kolom) → Indeks (tanpa aturan) → Tentang Penulis.
- **Struktur 8 bab + target halaman/bab:** 1 Pendahuluan (15–18) → 2 Konteks Objek (15–18) → 3 Landasan Teoretis (20–24) → 4 Kajian Terdahulu + Kerangka (18–22) → 5 Metodologi (15–18) → 6 Temuan (20–25) → 7 Debat + Pembahasan (25–35, BAB INTI: 7.1 posisi → 7.2 Pro → 7.3 Kontra → 7.4 Sintesis → 7.5 Novelty → 7.6 Implikasi) → 8 Penutup (10–15). Jumlah target: 138–175 halaman (mendekati 150–180, ujung bawah di bawah janji).
- **Novelty 5 lapis:** objek, konteks, hubungan konsep, metode, temuan — tiap klaim berstatus: Terbukti dari naskah / Didukung literatur / Interpretasi masuk akal / Belum cukup bukti (→ tulis sebagai proposisi, bukan fakta).
- **Pipeline 5 tahap:** 1 Ekstraksi naskah (`extracted_research.json` + ringkasan untuk review Bos) → 2 Analisis novelty → 3 Outline + approve → 4 Produksi per sub-bab (khusus Bab 7: call terpisah Pro/Kontra/Sintesis/Novelty) → 5 Assembly + QC + Turnitin.
- **Sitasi:** OpenAlex per bab (topik + tahun ≥2020) + classic refs; **verify LENIENT (flag saja, tidak hapus)** — lihat E-02.
- **Visual:** 8–10 tabel (hanya data asli/sintesis bersumber), 4 diagram (kerangka konsep, alur metode, peta temuan, matriks debat), 0 infografis, 0 ilustrasi AI dalam bab, 1 cover sederhana. Distribusi per bab ada — TAPI bertentangan dengan QC (lihat E-04).
- **Format + hitung:** A5, Cambria 11pt body / 14pt heading, margin 2cm, spasi 1.15, target 150–180 halaman, kata ≥25.000. **Hitung tidak menutup:** 25.000 kata ÷ ~300 kata/halaman A5 ≈ 83–100 halaman, BUKAN 150–180 (lihat E-04).
- **QC fail-closed:** docx >100KB, 0 section gagal/kosong, diagram terpasang, PDF Turnitin A4, visual sesuai komposisi. **QC menuntut ≥1 diagram/bab (8 total)** — bertentangan dengan komposisi 4 total (lihat E-04).

### C-3. Buku ajar OBE (S-03)

- **Definisi:** buku ajar berbasis RPS OBE. BUKAN buku umum. Dipakai bila: upload RPS, sebut CPL/CPMK/OBE, atau minta buku ajar/matkul.
- **Input wajib + triase (Phase 0, WAJIB PERTAMA):** deteksi jenis input SEBELUM mulai — (1) marker RPS (CPL/CPMK/Sub-CPMK/RPS/mata kuliah/SKS/minggu ke; skor ≥4 = RPS) → Mode A; (2) struktur bab (BAB romawi) → (3) rasio pertanyaan body (≥5% = workbook) → Mode C rewrite total, (<5% = narasi) → Mode B enhance; (4) naskah tidak jelas (<30 paragraf, atau >70% bullet pendek, atau tanpa struktur bab) → TOLAK + TANYA BOS (jangan asumsi). Pelajaran kritis: enhance workbook = Frankenstein (kasus Syahrul v1–v17, kata Boss "pusing, tidak layak buku") — workbook WAJIB rewrite total, jangan patch.
- **Mode A (RPS → buku baru):** ekstrak CPL/CPMK/Sub-CPMK → outline (approve Bos) → BCP per bab (chain: ringkasan bab N = konteks bab N+1) → visual → assembly → QC.
- **Mode B (naskah jadi → enhance):** tambah sitasi APA 7, visual, proofreading.
- **Mode C (workbook → rewrite):** ekstrak konten per bab → BCP chain per bab (~85 detik/bab; paralel 3 subagent TERBUKTI lebih cepat ~30 detik/bab tapi tidak koheren — chain dipilih) → verifikasi: 0 pertanyaan di body, sitasi ≥60% coverage, struktur utuh.
- **Anatomi:** Cover → Kata Pengantar/Pendahuluan DINAMIS (400–600 kata, hook cerita, manfaat, target mahasiswa+profesional, tutup "Penulis/nama/gelar/universitas" rata kanan) → Daftar Isi+Tabel+Diagram (dot leader + tab stop) → BAB 1..N → Glosarium (tabel 2 kolom) → Indeks (istilah → bab) → Daftar Pustaka (APA 7) → Tentang Penulis (nama+gelar+universitas+riwayat S1/S2/S3+pekerjaan+keahlian).
- **Struktur bab (WUJUD PEDAGOGIS — pembeda ajar):** Tujuan & Sasaran → TIU (2–3 poin "Mahasiswa mampu...") → TIK (5–7 poin kata kerja) → sub-bab (2–3 paragraf UTUH 60–100 kata; p1 konsep+contoh, p2 analisis+aplikasi+sitasi, p3 opsional studi kasus) + VISUAL MARKER → Ringkasan (5–7 kalimat + kaitan bab berikut) → Latihan (5–7 soal) → Checklist (`- [ ] <Kata Kerja> <objek>`; DILARANG awalan "Saya dapat/mampu/memahami"; gaya self-assessment pembaca).
- **Aturan editor (GAGAL bila dilanggar):** paragraf 60–100 kata (3–5 kalimat), <50 kata = GAGAL (gabung via `merge_short_paragraphs`), hook cerita di awal, transisi MAKSIMAL 3 frasa/bab (>3 = GAGAL), personal ≥25% (Anda, mahasiswa), 0 pertanyaan "Jelaskan..." di body, sitasi APA 7 WAJIB 5+/bab (<5 = GAGAL), jangan kurangi narasi (output ≥ draft), cross-bab ("Pada bab sebelumnya..." bab>1 + "Bab selanjutnya..." semua bab).
- **Sitasi:** APA 7, 5+/bab (gate) — TAPI Mode C memakai metrik lain (≥60% coverage) — lihat E-11. Skeptic memeriksa: gap, inkonsistensi, panjang paragraf, transisi (>15%?), personal refs (<25%), hook, pertanyaan lolos, sitasi kurang — ambang skeptic vs editor tidak sama (lihat E-12).
- **Visual:** strategi 7 lapis (tidak dirinci di inventaris ini — dipindah utuh ke profil Fase 2); tabel format wajib (kolom); diagram `[DIAGRAM N.1: ...]`; cover HTML+CSS.
- **Format + hitung:** B5 DEFAULT (lebih aman untuk visual) atau A5 HANYA bila dominan teks minim visual; margin 2cm; TNR 12pt body, 9pt italic TIU/TIK, 16pt heading bab; target narasi 1500–2000 kata/bab. **Hitung:** 8–12 bab × 1500–2000 kata = 12.000–24.000 kata; pada ~400 kata/halaman B5 ≈ 30–60 halaman teks murni (+ perangkat) — skill tidak menulis target halaman total ajar. **SSOT wajib menulis target halaman ajar + asumsi kata/halamannya.**
- **Gerbang:** TIDAK ADA gerbang bernama (0 rujukan "gerbang" di skill) — hanya QC sesudah jadi + approval outline. Ini lubang terbesar ajar (lihat audit).
- **Kekurangan yang dicatat:** duplikasi (Pitfalls ×2, Cross-Reference ×2), "DISKUSI BERJALAN" Juli masih di dalam skill, konfigurasi LLM basi (E-10), referensi = jurnal debug (S-12) bukan spesifikasi, struktur bab ajar di skill umum (perbandingan ajar vs umum) menduplikasi struktur di sini.

### C-4. Buku umum (S-04)

- **Definisi:** non-fiksi umum (hukum, ekonomi, bisnis, psikologi, manajemen, dll), tone formal-santai-naratif. BUKAN ajar (tanpa TIU/TIK/Latihan/Checklist).
- **Input wajib:** naskah, tema, atau outline. Pertanyaan wajib sebelum produksi: judul, penulis, target pembaca, jumlah bab, ukuran/font, bahan.
- **Anatomi:** Cover (PNG HTML+CSS) → Hak Cipta/ISBN (kosong untuk penerbit) → Kata Pengantar DINAMIS (hook naratif, manfaat, target, harapan) → Daftar Isi+Tabel+Diagram (dot leader + tab stop) → Daftar Singkatan (OPSIONAL, bila banyak akronim) → BAB 1..N → Glosarium (tabel 2 kolom) → Indeks → Daftar Pustaka (APA 7) → Tentang Penulis.
- **Struktur bab:** hook pembuka WAJIB kuat (kasus nyata/anekdot/data mengejutkan/pertanyaan retoris — anekdot tunduk aturan verifikasi I-02) → 4–6 sub-bab/bab (ajar cuma 3–4) → penutup bab paragraf naratif natural 2–4 kalimat (BUKAN section Ringkasan formal) + transisi ke bab berikut.
- **Sitasi:** APA 7 WAJIB ≥5/bab, masing-masing harus menopang klaim faktual (bukan tempelan) — lihat E-11 (angka vs per-klaim).
- **Tone:** "ngobrol cerdas" — mengalir, bervariasi, ritme, kadang kalimat pendek untuk efek; sapaan "Anda/pembaca/kita"; contoh kisah nyata/perumpamaan sehari-hari. DILARANG ciri AI/kaku ("Penting untuk dicatat", "Secara komprehensif", "Di era digital ini", "Dapat disimpulkan bahwa", frasa repetitif, struktur terasa template, kalimat seragam panjangnya).
- **Paragraf:** 60–100 kata (standar readability); kata/bab 3000–5000 (via chunking per sub-bab).
- **Visual + doktrin paket gaya (putusan Bos 18 Okt):** JENIS = SATU PAKET GAYA (bukan pilihan bebas). Tabel paket: `umum` = ilustrasi premium-konseptual navy/terracotta + infografis krem+navy kotak radius 18px + label kotak + tone "ngobrol cerdas" + brief konseptual; `anak` = clay 3D cerah (contoh Bos) + infografis krem hangat+langit biru kapsul 999px + label kapsul font 800 + kalimat pendek "kamu" + brief literal; `pendidikan` = clay 3D kalem + infografis putih kebiruan kapsul 16px + label kapsul tegas + bertahap/istilah dijelaskan + brief literal. ANAK ≠ PENDIDIKAN (ceria/mainan vs jelas/instruktif). Gerbang paket: `gerbang_jenis_buku.py` 32/0 (terbukti bergigi: fallback senyap → GAGAL; palet dikunci ke umum → GAGAL). Menu `/buku` SUDAH ADA (18 Okt): kartu Buku Umum punya dropdown Bidang + Untuk siapa (Profesional/Anak-anak/Pelajar → umum/anak/pendidikan); kartu lain saat itu TIDAK disentuh.
- **Format + hitung:** B5 (17.6×25.0) atau A5 alternatif; TNR 12pt (alternatif Garamond 12pt); spasi 1.15 (alternatif 1.5); heading bab 16pt, sub-bab 14pt; target 170+ halaman; bab FLEKSIBEL 8–12 (spesifik = 8, general = 12). **Hitung tidak menutup:** 8–12 bab × 3000–5000 kata = 24.000–60.000 kata; pada ~400 kata/halaman B5 ≈ 60–150 halaman — target 170+ tidak tercapai bahkan di ujung atas tanpa asumsi kepadatan lain. **SSOT wajib menulis asumsi kata/halaman atau merevisi target.**
- **Gerbang:** gerbang paket gaya (di atas) + gerbang menu (30/0, 42/0, 17/0, 35/0 — terbukti bergigi). Gerbang ISI umum (mutu narasi/sitasi per bab) tidak dirumuskan sebagai gate — hanya aturan editor.
- **Kekurangan yang dicatat:** Glosarium + Indeks diwajibkan di anatomi tapi hampir tanpa aturan (1 rujukan masing-masing); riwayat "BELUM UI" lalu "SUDAH ADA UI" tertulis berurutan di skill (pola jurnal-di-dalam-spesifikasi — SSOT memisahkan spesifikasi kini dari changelog); pointer SOT `/opt/data/jenis_buku.py` ambigu (salinan host vs repo `app/jenis_buku.py` — SSOT menunjuk repo).

### C-5. Book chapter (S-05)

- **Definisi:** SATU bab buku kolaborasi (bukan buku komplit/multi-bab). Sesudah selesai: serahkan file, DILARANG menawar "Mau lanjut bab berikutnya?".
- **Input wajib:** nomor_bab (int 1–99), judul_bab, judul_buku OPSIONAL (konteks antar-bab). **TIDAK diminta:** tema induk, editor, volume/penerbit, CV penulis — lihat E-09.
- **Anatomi/struktur 15 section:** BAB N + judul (centered, 14pt bold, BUKAN 20pt) → A Pendahuluan (5–6 paragraf formal + "Setelah mempelajari bab ini, pembaca diharapkan mampu:" + 6 learning objectives a–f kata kerja aktif) → B Konsep/Karakteristik → C Proses → D Pendekatan → E Faktor → F Bias Kognitif/Risiko → G Alat Bantu → H Era Digital/AI → I Etika/Tata Kelola → J Ilustrasi Kasus → K Prinsip Praktis (bullet 10 prinsip) → L Ringkasan Bab (bullet 6 poin) → M DILOMPATI → N Referensi (APA 7 hanging indent 0.5″, output SEMUA final_refs) → O Glosarium (TABEL 2 kolom, bukan daftar teks) → CV Penulis (nama, email, biodata singkat, style No Spacing). Section A–L MENGALIR (tanpa page break antar section, ikut BAB 7 asli); page break SEBELUM N dan O. Judul section memakai `{judul_short}` (frasa inti judul; potong di koma kedua, jangan potong tengah kata/angka; sanitasi `{`/`}` → `(`/`)` sebelum `.format()`).
- **Sitasi:** OpenAlex per bab (topik + tahun ≥2020, strip author/tahun, sort relevance) + classic refs (Porter 1985, Barney 1991, Prahalad & Hamel 1990, Robbins & Coulter 2018, Kotler & Keller 2016, Simon 1977, March 1991, Brynjolfsson & McAfee 2014, Hart 1995, dll); **verify LENIENT (flag saja, tidak hapus)** — lihat E-02. Jumlah: 6 OpenAlex + 4 klasik = 10, tapi skill bilang total 8 — lihat E-05.
- **Visual:** 1 diagram matplotlib/bab (rotasi 6 template per `bab_num % 6`: hub-and-spoke, flowchart horizontal, hierarchy tree, process flow vertikal, pyramid, matrix grid; 6 palet berotasi; label spoke dari keyword judul; tulis ke OUTPUT_DIR bukan /tmp; gagal = jalan tanpa diagram, tidak crash); tabel konten hanya di section B–G (marker di section lain di-extract = silent drop, acceptable).
- **Paragraf:** split >80 kata (prioritas: akhir kalimat → koma → hard split max+15); body 11pt justified, left_indent 0.5cm, first_line_indent 1.0cm; learning objectives indent 1.3cm; bullet hanging (left 1.0cm, first −0.5cm); spasi default (BUKAN Pt(6)/1.15 eksplisit).
- **Format + hitung:** DOCX A5 (5.83″×8.27″), margin 2cm, Cambria 11pt body / 14pt judul+heading (TANPA warna, hitam polos — bukan biru template), MAKSIMAL 15 halaman DOCX A5; PDF Turnitin A4 (tidak terikat 15 halaman). Verifikasi 18 Agu 2026 (BAB 4 contoh): tabel XML ≥3 → aktual 7; gambar 1 → 1; referensi 8 → 8; placeholder bocor 0 → 0; kata ~4000–5000 → aktual 4993; ukuran ~90–100KB → 96KB. **Hitung:** 4993 kata ÷ 15 halaman ≈ 333 kata/halaman A5 — konsisten. **Tapi:** tidak ada anggaran kata per section — batas 15 halaman dicek sesudah jadi, bukan direncanakan (lihat E-09).
- **QC fail-closed (paling lengkap):** cek 2 berkas ada + ukuran non-trivial; baca docx (paragraf/tabel/kata/sel tabel); 0 `[Section gagal dibuat]`/`[Section kosong]`; ekstrak PDF (halaman >0, teks substansial); cek ZIP/XML (0 placeholder bocor); cek `word/media/` (diagram ada; gagal matplotlib = visual hilang, bukan sukses); ukuran halaman (DOCX A5, PDF A4); gagal = jangan kirim link MEDIA, perbaiki + ulang. Pelajaran tercatat: pipeline pernah klaim SELESAI padahal semua section gagal; file kosong pernah dikirim tanpa dibaca isinya.
- **Kekurangan yang dicatat:** angka saduran BAB 7 sebagai template universal (6 objectives, 10 prinsip, 6 poin, M dilompati — tanpa label "dari BAB 7"); input tema induk/editor/volume/CV hilang; anggaran kata per section hilang; LENIENT sitasi; Turnitin "mock-up mode" tak jelas; konfigurasi LLM basi (E-10); fragmen kunci di dokumen (F); penomoran pitfalls loncat (13–16 lalu 1–12 — kosmetik).

### C-6. Paket anak & pendidikan (tanpa skill sendiri)

- **Yang ada:** paket gaya doktrin 18 Okt (lihat C-4) + arah tone + brief literal + label kapsul. **Yang tidak ada:** definisi presisi, ANTI-BINGUNG, anatomi, struktur bab, aturan sitasi, gerbang isi, target halaman/kata, input wajib (usia pembaca? jenjang? kurikulum?). Produksi anak/pendidikan saat ini = mesin umum + paket gaya — **gaya presisi, isi ikut umum.** SSOT wajib menulis profil anak + pendidikan sebelum kartunya dinyatakan presisi (lihat E-09).

---

## D. Tabel duplikasi (satu aturan, banyak tempat — SSOT simpan SATU)

| Aturan | Muncul di | Rumah kanonik di SSOT |
|---|---|---|
| BCP Council + chunking + ringkasan berjalan | S-01, S-02, S-03, S-04 | Inti I-08 |
| Search-then-lock + strip author/tahun dari kueri | S-01, S-02, S-05 (+ verifikasi_sitasi di S-04) | Inti I-02/I-03 |
| Marker `[TABEL]`/`[DIAGRAM]` + render + cabut marker | S-02, S-03, S-05, S-09 | Inti I-09 |
| Glosarium tabel 2 kolom + Indeks + Daftar Pustaka APA 7 di akhir | S-01, S-02, S-03, S-04, S-05 | Inti (bentuk) + profil (aturan isi per jenis — referensi paling detail, umum paling tipis) |
| Footer PAGE + margin 2cm | S-01, S-02, S-03, S-04 | Inti I-05/I-06 |
| PDF Turnitin A4 | S-02, S-05 | Inti I-14 |
| Doktrin paket gaya (jenis → ilustrasi+infografis+label+tone) | S-04, S-09 | Inti (doktrin) + profil (nilai per jenis) |
| Diagnosis gambar hilang (3 akar) | S-08, S-09 (section sendiri) | Pendukung S-08 saja; S-09 cukup menunjuk |
| Struktur bab ajar (TIU/TIK/latihan/checklist) | S-03 + tabel perbandingan di S-04 | Profil ajar saja; S-04 cukup menunjuk |
| Aturan "jangan fallback diam-diam ke umum" | S-04, S-09 | Inti I-10 |
| Changelog + pelajaran tercatat (pitfalls) | S-01 s.d. S-05, S-09, S-10 | Changelog SSOT (terpisah dari spesifikasi kini) |

---

## E. Tabel kontradiksi (butuh putusan Boss — rekomendasi Wulan tercantum)

| ID | Pihak A | Pihak B | Rekomendasi Wulan | Putusan Boss |
|---|---|---|---|---|
| E-01 | **Ilustrasi umum = premium-konseptual flat-vector, "no 3D"** (S-09 v2 kunci 18 Okt + doktrin S-04 18 Okt; alasan: aman cetak B/W) | **Ilustrasi buku umum = 3D kartun edukatif, flat/line-art DITOLAK** (catatan 23 Okt) | Putuskan PER JENIS, jangan satu kata untuk semua: umum = premium-konseptual (hormati doktrin 18 Okt + alasan B/W); anak/pendidikan = clay 3D (kedua sumber sepakat); infografis 3D hanya bila Boss menegaskan itu untuk umum juga | _(kosong — tunggu Boss)_ |
| E-02 | **Sitasi KETAT fail-closed** (S-01: tak terverifikasi = bab ditolak) | **Sitasi LENIENT flag saja** (S-02, S-05: tidak hapus apa pun) | Samakan ke KETAT untuk semua jenis akademik (monograf/chapter membawa klaim akademik juga; flag tanpa penyalur = tidak pernah dibaca) | _(kosong)_ |
| E-03 | **Format B5/TNR 12** (S-01, S-04, S-03 default B5) | **Format A5/Cambria 11** (S-02, S-05) + S-03 membolehkan A5 bila teks-dominan | Kunci per jenis di profil (bukan diseragamkan): referensi B5/TNR, umum B5/TNR, ajar B5 default/A5 bila teks-dominan, monograf A5/Cambria, chapter A5/Cambria — sahkan pembagian yang sudah dipraktikkan | _(kosong)_ |
| E-04 | **Monograf: 4 diagram total** (distribusi per bab) + **≥25.000 kata** | **Monograf QC: ≥1 diagram/bab (8 total)** + **target 150–180 halaman A5** | Jaga janji halaman (150–180) karena itu yang dijual: perbaiki lantai kata ke **≥45.000 kata** (≈150 halaman × ~300 kata/halaman A5) DAN samakan diagram ke **4 diagram pada Bab 3/5/6/7** (hapus tuntutan "per bab" dari QC) — ATAU turunkan janji halaman ke ~100. Wulan merekomendasikan opsi pertama | _(kosong)_ |
| E-05 | **Chapter: 6 OpenAlex + 4 klasik** (= 10) | **Chapter: total 8 referensi** (struktur + verifikasi 18 Agu) | Ubah rumus jadi rentang **8–10 referensi akhir** (dedup dijelaskan) + doktrin per-klaim (jumlah mengikuti klaim, bukan angka mati) | _(kosong)_ |
| E-06 | **Gate 1: "disetujui Bos eksplisit"** (semua skill) | **Web: pelanggan menyetujui outline** (mesin referensi yang sudah live) | Bedakan per jalur di SSOT: operator = Bos; web = pelanggan. Mesin sudah benar; skill yang harus ditulis ulang | _(kosong)_ |
| E-07 | **Peta Bab = sub bernomor "### N.0"** (S-01 struktur bab) | **Peta Bab = intro bab** (mesin referensi: hook = peta; validator outline menuntut tepat N.1–N.5) | Tetapkan: **Peta = intro bab, bukan sub bernomor.** Perbaiki teks S-01 (hapus N.0 dari daftar sub, tulis "Intro = Peta Bab") | _(kosong)_ |
| E-08 | **Daftar Singkatan = WAJIB** (anatomi S-01) | **Tidak ada pembangun daftar singkatan** di mesin mana pun | Turunkan jadi **wajib bila >20 singkatan teknis** (sejajar glosarium) + bangun generatornya di Fase mesin; bila tidak dibangun, hapus dari anatomi wajib | _(kosong)_ |
| E-09 | **Chapter/ajar/monograf punya input wajib** (tema induk+editor+volume+CV; RPS; naskah) | **Form web tidak meminta input-input itu** (chapter: hanya judul; ajar/monograf: tanpa RPS/naskah; anak/pendidikan: tanpa profil) | Profil SSOT MENDEKLARASIKAN input wajib; form web dicek terhadap deklarasi; **jenis tanpa field inputnya = kartu "belum presisi"** (tidak dijual sebagai presisi). Anak/pendidikan: tulis profilnya di SSOT sebelum dinyatakan presisi | _(kosong)_ |
| E-10 | **Konfigurasi LLM = gateway + model lama** (S-03 puluhan rujukan; S-02, S-05) | **App live = 9router satu-satunya pintu teks** (deploy 28 Okt) | Pindahkan konfigurasi ke SATU tempat di inti SSOT (gateway + model hidup sekarang); profil/skill dilarang menulis endpoint/model sendiri | _(kosong)_ |
| E-11 | **Sitasi angka = gate** (S-04: ≥5/bab; S-03 editor: <5 = GAGAL) | **Sitasi per-klaim, angka = pedoman lunak** (S-01) + **Mode C ajar: ≥60% coverage** (cakupan dari apa? tak terdefinisi) | Samakan ke per-klaim untuk semua; angka 5+ (ajar/umum) jadi pedoman lunak bukan gate; hapus metrik coverage % sampai didefinisikan | _(kosong)_ |
| E-12 | **Skeptic ajar: paragraf ">60/<40 kata"** | **Editor ajar: 60–100 kata, <50 = GAGAL, >100 = split** | Samakan ke editor (diduga typo skeptic); SSOT menulis satu ambang: 60–100 kata, <50 gabung, >100 belah | _(kosong)_ |
| E-13 | **Chapter: hanya MAKSIMAL 15 halaman** (S-05 kini) | **Arsip chapter: 7–15 halaman, target 12** (S-11) | Pulihkan rentang **7–15 halaman** di profil chapter (batas bawah hilang saat pembaruan) — bab 3 halaman tidak boleh lolos sebagai chapter | _(kosong)_ |

---

## F. Daftar basi → arsip (pindah, bukan hapus)

| Item | Alasan | Tujuan |
|---|---|---|
| Konfigurasi gateway/model lama di S-02, S-03, S-05 | Penyedia sudah tidak dipakai app (E-10) | Arsip; diganti inti SSOT |
| Fragmen kunci API di S-05 (bertanda tak valid) | Kunci tidak boleh tinggal di dokumen skill (I-12) | HAPUS dari dokumen (bukan arsip) — fragmen tak valid sekalipun |
| Penjelasan nomor halaman perkiraan 360 kata/halaman (S-01 + pointer modul indeks lama) | Mesin baru pakai nomor render nyata | Arsip sebagai sejarah metode lama |
| Pointer `/opt/data/jenis_buku.py` (S-04) | Ambigu: salinan host vs repo `app/jenis_buku.py` | Arsip; SSOT menunjuk repo |
| Jurnal debug/audit/uji di `buku-ajar-obe/references/` (S-12) | Sejarah, bukan spesifikasi kini | Arsip referensi (tetap bisa dibaca, tidak mengikat) |
| Riwayat "BELUM UI → SUDAH ADA UI" di dalam S-04; "DISKUSI BERJALAN" Juli di S-03; duplikasi Pitfalls/Cross-Reference di S-03 | Pola jurnal-di-dalam-spesifikasi; pembaca tidak tahu mana yang berlaku kini | Changelog SSOT (terpisah dari spesifikasi) |
| `.archive/book_chapter` (S-11) | Sudah tergantikan S-05 (QC fail-closed, doc ID dinamis, pipeline marker lebih lengkap) | Tetap di arsip; satu-satunya kehilangan = batas bawah halaman (E-13) |
| Turnitin "mock-up mode" (S-02, S-05) | Tidak jelas apa yang sebenarnya diverifikasi | Tandai TERBUKA di SSOT sampai dijelaskan (bukan klaim pre-check beneran) |
| Model gambar/prompt gaya lama di S-09 bila bertentangan dengan E-01 | Tunggu putusan E-01 | Arsip sesudah putusan |

---

## G. Kerangka SSOT yang akan ditulis di Fase 2 (sesudah putusan)

```
template-buku-resmi/jenis/<jenis>/
  profil.json        ← SUMBER MESIN (satu per jenis: referensi, monograf,
                        ajar, umum, chapter, anak, pendidikan)
  SPESIFIKASI.md     ← cermin manusia dari profil.json (digenerasi/dirujuk,
                        bukan ditulis kedua kali)
skills/buku-ssot/
  SKILL.md           ← PINTU: peta (artikel vs buku vs pendukung), cara pakai,
                        changelog, daftar putusan terkunci + tanggal
  INTI-BERSAMA.md    ← Bagian B dokumen ini, versi final sesudah putusan
  PROFIL-<jenis>.md  ← cermin manusia per jenis (dari Bagian C + putusan)
scripts/periksa_ssot_buku.py  ← CHECKER (gagal = SSOT rusak, deploy ditahan)
  1. setiap jenis yang dijual web punya profil
  2. angka profil menutup (kata × bab ÷ kata/halaman = target halaman)
  3. setiap input wajib profil punya field form web
  4. tidak ada profil bertentangan dengan inti
  5. tidak ada nama penyedia/model basi; tidak ada fragmen kunci
  6. setiap gerbang profil bisa dicek mesin (bukan prosa)
  7. kartu web 'siap' = profil + mesin + gerbang ketiganya ada
_arsip/skill-buku-28okt2026/  ← skill lama, BACA-SAJA (isi + riwayat utuh)
```

**Aturan tata kelola (supaya tidak berantakan lagi):**
- Ubah di SSOT, bukan di skill lama. Agen yang mengedit skill lama = salah alamat.
- Setiap perubahan SSOT: changelog + tanggal + putusan Boss yang menguncinya.
- Review agen Boss tetap berlaku untuk SSOT (Wulan verifikasi ke berkas nyata
  sebelum memperbaiki).
- Checker masuk gerbang deploy (`periksa_buku.sh`) — SSOT rusak = deploy ditahan.

---

## H. Lembar Putusan Boss (jawab dengan nomor)

Boss cukup jawab per nomor, atau tulis **"Setuju semua rekomendasi"** bila
semuanya cocok. Yang PALING memblokir Fase 2 adalah P-01, P-02, P-04.

- **P-01 (E-01, ilustrasi):** umum = premium-konseptual, anak/pendidikan = clay 3D, infografis 3D hanya bila Boss tegaskan untuk umum juga? Atau 3D kartun untuk SEMUA jenis umum?
- **P-02 (E-02, sitasi):** samakan ke KETAT fail-closed untuk semua jenis?
- **P-03 (E-03, format):** kunci pembagian B5/TNR vs A5/Cambria per jenis seperti rekomendasi?
- **P-04 (E-04, monograf):** jaga janji 150–180 halaman + lantai kata ≥45.000 + diagram 4 (Bab 3/5/6/7)? Atau turunkan janji halaman ke ~100?
- **P-05 (E-05, chapter):** referensi akhir jadi rentang 8–10 (bukan angka mati 8)?
- **P-06 (E-06, approver):** Gate 1 dibedakan operator = Bos, web = pelanggan?
- **P-07 (E-07, peta):** Peta Bab = intro bab (bukan sub N.0)?
- **P-08 (E-08, singkatan):** Daftar Singkatan jadi wajib-bersyarat (>20 singkatan) + dibangun generatornya?
- **P-09 (E-09, input+anak/pendidikan):** jenis tanpa field inputnya = kartu "belum presisi"? Dan profil anak/pendidikan ditulis di SSOT?
- **P-10 (E-10, provider):** konfigurasi LLM pindah ke satu tempat inti (9router + model hidup)?
- **P-11 (E-11, angka sitasi):** angka 5+/bab jadi pedoman lunak (bukan gate), metrik coverage % dihapus?
- **P-12 (E-12, ambang paragraf ajar):** samakan ke 60–100 kata (<50 gabung, >100 belah)?
- **P-13 (E-13, chapter):** pulihkan rentang 7–15 halaman?

**Sesudah Boss menjawab:** Wulan menulis SSOT final (Fase 2) + checker, lalu
menyambungkan ke web per jenis (chapter → ajar → monograf). Uji buku beneran +
review pakar tetap parkir sesuai putusan Boss ("nanti saja").

---

## I. Koreksi standar (DISETUJUI Boss 28 Okt malam — masuk spesifikasi SSOT Fase 2)

Penilaian Wulan sebagai ahli mutu (disampaikan 28 Okt malam) dan disetujui Boss
untuk dimasukkan ke SSOT. Koreksi ini MELENGKAPI putusan P-01..P-13, bukan
menggantikannya — P-01..P-13 tetap menunggu jawaban Boss sebelum Fase 2 ditulis.

### I.1 Aturan label (perbaikan utama, berlaku semua profil)

Setiap aturan SSOT WAJIB berlabel satu dari:
- **[STANDAR]** — praktik universal penerbitan/akademik (tidak boleh dilanggar
  tanpa alasan tertulis).
- **[HOUSE]** — pilihan Boss (boleh di-override brief editor / penerbit /
  pelanggan bila mereka memberi spesifikasi sendiri).
- **[GATE]** — bisa dicek mesin (checker menolak bila gagal).
- **[TERBUKA]** — belum diputuskan / belum jelas (contoh: Turnitin "mock-up mode").

Tanpa label, aturan rumah yang bagus terlihat seperti standar, dan aturan rumah
yang nyasar (APA untuk umum, objectives untuk chapter riset, TIU/TIK) tidak
ketahuan nyasarnya.

### I.2 Referensi

- **[STANDAR] N.3 = fungsi perbandingan kritis**, bukan furnitur: tabel komparasi
  ATAU prosa komparatif terstruktur, dipilih sesuai isi bab. Gerbang menguji
  fungsi membandingkan, bukan keberadaan tabel.
- **[STANDAR] Gate 5 ditulis sebagai PROSES**, bukan jumlah: kriteria reviewer,
  apa yang direview, log revisi yang ditindaklanjuti tertulis.
- **[STANDAR] Indeks memakai rujukan silang "lihat juga"** untuk istilah terkait
  (selain aturan entri substantif yang sudah ada).

### I.3 Monograf

- **[STANDAR] Gerbang review pakar WAJIB:** 1–2 reviewer sejawat sebelum final
  (selama ini hanya referensi yang punya Gate 5; monograf tanpa review = di
  bawah standar).
- **[STANDAR] Aturan etik + anonimisasi:** persetujuan etik, anonimisasi
  nama/lokasi informan, izin kutip — wajib sebelum Bab 6 memuat kutipan informan.
- **[STANDAR] Aturan ubah-skripsi-jadi-monograf:** tulis ulang untuk pembaca;
  BUANG aparat ujian (bahasa "tujuan penelitian", format sidang, halaman
  pengesahan). Skripsi dicetak apa adanya = gagal standar klasik.
- **[HOUSE] Bab 7 dua varian:** debat pro-kontra (riset hipotesis) ATAU sintesis
  interpretatif (riset deskriptif/kualitatif). Debat wajib untuk semua monograf
  adalah invensi rumah, bukan standar universal.

### I.4 Buku ajar OBE

- **[STANDAR] Petakan TIU/TIK ke bahasa OBE kini:** TIU = level CPMK, TIK = level
  Sub-CPMK (atau ganti istilahnya sekalian). TIU/TIK tanpa pemetaan dibaca
  sebagai buku lama di era MBKM.
- **[GATE] Gerbang keselarasan:** tiap TIK/Sub-CPMK minimal 1 butir latihan yang
  mengujinya (constructive alignment) — bukan hanya hitung jumlah soal.
- **[STANDAR] Kunci jawaban + pembahasan** (minimal di akhir buku) untuk Latihan,
  supaya siswa bisa memeriksa diri.
- **[STANDAR] "Bacaan Lanjutan" per bab** (bacaan wajib vs anjuran) sebagai aparat
  standar buku ajar.

### I.5 Buku umum

- **[STANDAR] Sitasi umum = endnotes / "Catatan & Sumber" bernomor per bab +
  Daftar Pustaka di akhir.** Sitasi kurung APA in-text untuk buku dagang TIDAK
  standar (mengganggu narasi); APA in-text hanya untuk jenis akademik
  (referensi, monograf, ajar).
- **[STANDAR] Glosarium umum = OPSIONAL** (hanya bila istilah teknis melewati
  ambang, seperti aturan referensi). Buku dagang standar cukup indeks.
- **[HOUSE] Target halaman = rentang + aturan "dilarang mengganjal"** (bukan angka
  mati demi ongkos cetak; buku 120 halaman yang padat mengalahkan buku 170
  halaman yang diganjal).

### I.6 Book chapter

- **[STANDAR] Brief editor volume DIDAHULUKAN:** tema, batas kata, gaya sitasi,
  format, deadline, proses review dari editor volume MENANG atas format rumah.
  Format rumah (A5/Cambria/15 halaman) hanya berlaku bila editor tidak memberi
  spesifikasi.
- **[STANDAR] Abstrak + kata kunci** sebagai aparat chapter (bersyarat: bila
  volume memintanya).
- **[STANDAR] Learning objectives HANYA untuk volume ajar** (buku ajar
  kolaborasi). Chapter riset standar berisi masalah + argumen + kontribusi,
  bukan objectives.
- **[HOUSE] Dua varian chapter:** riset vs ajar — atau minimal objectives
  dijadikan bersyarat. Template 15 section saat ini adalah template chapter
  ajar (saduran BAB 7), bukan template chapter riset.
- **[HOUSE] Batas 15 halaman = default rumah** saat editor diam (bukan standar
  universal); rentang profil = 7–15 halaman (lihat E-13).

### I.7 Lintas jenis

- **[STANDAR] Proses review per jenis:** referensi = ahli bidang; monograf =
  reviewer sejawat; ajar = dosen sejawat + uji keterbacaan mahasiswa; chapter =
  editor volume; umum = editor naskah + fact-checker.
- **[STANDAR] Aturan edisi / revisi / errata** untuk semua jenis (khususnya
  referensi dan ajar yang hidup dari edisi revisi): bagaimana koreksi dan edisi
  baru dicatat.
- **[STANDAR] Resolusi gambar minimal untuk cetak (DPI)** — melengkapi aturan
  ukuran berkas yang sudah ada di skill ilustrasi.
- **[STANDAR] Catatan KDT sebagai urusan penerbit** (diterbitkan Perpusnas,
  ditempel penerbit — bukan ditulis penulis) supaya tidak hilang dari anatomi.

---

## J. Putusan final P-01..P-13 (DISETUJUI Boss 28 Okt malam)

Boss mengetuk "Setuju semua jawaban terbaik" atas walkthrough 28 Okt malam.
Jawaban terbaik Wulan di bawah ini RESMI menjadi putusan SSOT dan dipakai
menulis profil Fase 2. Satu-satunya penyesuaian redaksional: P-01 ditulis
per jenis (bukan satu kata untuk semua).

- **P-01 (ilustrasi):** umum = premium-konseptual (navy/terracotta/krem, satu
  metafora, bukan 3D); anak = clay 3D cerah; pendidikan = clay 3D kalem;
  infografis ikut paket masing-masing. 3D kartun edukatif HANYA untuk
  anak/pendidikan.
- **P-02 (sitasi):** KETAT fail-closed untuk semua jenis akademik
  (referensi, monograf, ajar, chapter); umum dicek faktanya lewat endnotes.
- **P-03 (format):** dikunci per jenis — referensi B5/TNR, umum B5/TNR, ajar B5
  (boleh A5 bila dominan teks), monograf A5/Cambria, chapter A5/Cambria.
- **P-04 (monograf):** jaga janji 150–180 halaman; lantai kata ≥45.000;
  diagram 4 (Bab 3/5/6/7). Konsekuensi dicatat: produksi ±2× hitungan lama.
- **P-05 (chapter):** referensi akhir = rentang 8–10 (bukan angka mati 8).
- **P-06 (approver):** operator = Boss; web = pelanggan.
- **P-07 (peta):** Peta Bab = intro bab, bukan sub N.0.
- **P-08 (singkatan):** wajib bila singkatan teknis >20 + generator dibangun
  di fase mesin.
- **P-09 (input):** jenis tanpa field inputnya = kartu "belum presisi";
  profil anak/pendidikan ditulis di SSOT (status PARSIAL sampai lengkap).
- **P-10 (provider):** konfigurasi LLM satu tempat di inti (9router + model hidup).
- **P-11 (angka sitasi):** 5+/bab = pedoman lunak (bukan gate); metrik coverage %
  dihapus.
- **P-12 (paragraf ajar):** ambang 60–100 kata (<50 gabung, >100 belah).
- **P-13 (chapter):** rentang halaman 7–15 (batas bawah dipulihkan).
