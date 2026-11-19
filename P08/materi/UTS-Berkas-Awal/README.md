# Berkas Awal — Ujian Tengah Semester

Pemrograman Berorientasi Objek · Prodi Teknik Informatika FT UPTT

## Isi

Folder ini sengaja hampir kosong. Seluruh kode Bagian B Anda tulis sendiri
dari berkas kosong.

```
src/
  __init__.py
  model/
    __init__.py          ← seluruh kelas Anda diletakkan di sini
tests/
  __init__.py            ← seluruh berkas uji Anda diletakkan di sini
pyproject.toml           ← JANGAN diubah
periksa_pbo.py           ← JANGAN diubah
```

## Sebelum mulai

```
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # Linux atau macOS
pip install pytest mypy
```

Bila laboratorium sudah menyediakan `.venv` siap pakai, cukup aktifkan.

## Sebelum mengumpulkan

Ketiga perintah berikut wajib bersih. Kegagalan salah satunya mengurangi
15 poin dari Bagian B.

```
python periksa_pbo.py src --profil p06
python -m mypy
python -m pytest
```

## Pengumpulan

Kompres seluruh folder ini menjadi `UTS-<NIM>.zip`, lalu unggah ke LMS
sebelum waktu ujian berakhir. Folder `.venv` tidak perlu disertakan.
