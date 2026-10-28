#!/usr/bin/env python3
"""Checker SSOT Buku — memeriksa profil di folder ini (stdlib saja).

Keluar 0 = tidak ada ERROR (item TERBUKA/PARSIAL hanya peringatan).
Keluar 1 = ada ERROR (kontradiksi, angka tak menutup, profil hilang,
string terlarang, section/label wajib hilang).

Cara pakai:  python3 periksa_ssot_buku.py   (dari folder ssot-buku)
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

JENIS = ["referensi", "monograf", "ajar", "umum", "chapter", "anak",
         "pendidikan"]

WAJIB_SECTION = ["Definisi", "Input wajib", "Anatomi", "Struktur bab",
                 "Sitasi", "Visual", "Format", "Gerbang"]
LARANG = ["enowx", "172.17.0.1", "lenient"]
WAJIB_LABEL = ["[STANDAR]", "[HOUSE]", "[GATE]"]


def baca_profil(jenis):
    path = os.path.join(HERE, "PROFIL-%s.md" % jenis)
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as f:
        return f.read()


def blok_angka(teks):
    """Ambil pasangan kunci: nilai dari BLOK ANGKA (sampai header berikutnya)."""
    m = re.search(r"## BLOK ANGKA.*?\n(.*?)(?=\n## |\Z)", teks, re.S)
    data = {}
    if not m:
        return data
    for line in m.group(1).strip().splitlines():
        mm = re.match(r"\s*([a-z_]+):\s*(.+?)\s*$", line)
        if mm:
            data[mm.group(1)] = mm.group(2)
    return data


def angka(data, key, default=None):
    try:
        return float(data[key])
    except (KeyError, ValueError):
        return default


def main():
    errors, warnings = [], []
    for jenis in JENIS:
        teks = baca_profil(jenis)
        if teks is None:
            errors.append("%s: PROFIL hilang" % jenis)
            continue
        for sec in WAJIB_SECTION:
            if sec not in teks:
                errors.append("%s: section wajib hilang: %s" % (jenis, sec))
        for lab in WAJIB_LABEL:
            if lab not in teks:
                errors.append("%s: label wajib hilang: %s" % (jenis, lab))
        rendah = teks.lower()
        for s in LARANG:
            if s in rendah:
                errors.append("%s: string terlarang: %s" % (jenis, s))
        data = blok_angka(teks)
        status = data.get("status_profil", "TETAP")
        if status == "PARSIAL":
            warnings.append("%s: PARSIAL — gaya presisi, isi ikut umum; "
                            "kartu tidak boleh diklaim presisi penuh" % jenis)
            continue
        if data.get("status_target", "TETAP") == "TERBUKA":
            warnings.append("%s: target halaman TERBUKA — %s"
                            % (jenis, data.get("catatan_target", "")))
            continue
        kph = angka(data, "kata_per_halaman")
        tmin = angka(data, "target_halaman_min")
        tmax = angka(data, "target_halaman_max")
        if kph is None or tmin is None:
            errors.append("%s: BLOK ANGKA tak lengkap (kata_per_halaman / "
                          "target_halaman_min)" % jenis)
            continue
        if "kata_total_min" in data:
            pmin = angka(data, "kata_total_min") / kph
            pmax = (angka(data, "kata_total_max") or 0) / kph
        else:
            pmin = (angka(data, "kata_per_bab_min") or 0) * \
                   (angka(data, "jumlah_bab_min") or 0) / kph
            pmax = (angka(data, "kata_per_bab_max") or 0) * \
                   (angka(data, "jumlah_bab_max") or 0) / kph
        if pmax < tmin:
            errors.append("%s: angka TAK MENUTUP — maks %.0f halaman < "
                          "target min %.0f" % (jenis, pmax, tmin))
        elif tmax is not None and pmin > tmax:
            errors.append("%s: angka TAK MENUTUP — min %.0f halaman > "
                          "target maks %.0f" % (jenis, pmin, tmax))
        else:
            print("%s: OK — %.0f–%.0f halaman vs target %.0f%s"
                  % (jenis, pmin, pmax, tmin,
                     ("–%.0f" % tmax) if tmax is not None else "+"))
    print("---")
    for w in warnings:
        print("PERINGATAN: " + w)
    for e in errors:
        print("ERROR: " + e)
    if errors:
        print("HASIL: %d ERROR — SSOT rusak, tahan deploy" % len(errors))
        return 1
    print("HASIL: 0 ERROR (%d peringatan terbuka/parsial)" % len(warnings))
    return 0


if __name__ == "__main__":
    sys.exit(main())
