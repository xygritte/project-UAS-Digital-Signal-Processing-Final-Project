# Penelitian Penyaringan Citra Digital - Pengolahan Sinyal Digital

**Final Project — Pengolahan Sinyal Digital**

## Topik Penelitian

**Perbandingan Penyaringan Mean, Gaussian, dan Median untuk Mengurangi Noise Salt-and-Pepper pada Citra Digital**

## Tujuan Penelitian

Proyek ini membandingkan secara eksperimen tiga metode penyaringan spasial untuk mengurangi noise salt-and-pepper pada citra digital:

- Mean Filter dengan kernel 3×3
- Gaussian Filter dengan kernel 5×5
- Median Filter dengan kernel 5×5

Hasil citra yang telah diproses dibandingkan dengan citra referensi yang bersih menggunakan **MSE, PSNR, dan SSIM**.

## Alur Eksperimen

```text
Citra bersih
    ↓
Pra-pemrosesan / grayscale
    ↓
Penambahan noise salt-and-pepper
    ↓
┌──────────────┬────────────────┬───────────────┐
│ Mean 3×3     │ Gaussian 5×5   │ Median 5×5    │
└──────────────┴────────────────┴───────────────┘
    ↓
MSE / PSNR / SSIM
    ↓
Tabel + visualisasi
```

## Struktur Repository

```text
├── data/
│   ├── original/
│   └── noisy/
├── outputs/
│   ├── figures/
│   ├── mean/
│   ├── gaussian/
│   ├── median/
│   └── results/
├── src/
│   ├── generate_noise.py
│   ├── filtering.py
│   ├── evaluation.py
│   └── main.py
├── requirements.txt
└── README.md
```

## Data

Implementasi saat ini menggunakan gambar contoh yang dapat direproduksi dari `scikit-image`, yaitu `camera`, `coins`, dan `moon`, sebagai citra referensi bersih. Program menyimpan citra yang telah diberi noise dan hasil penyaringan secara lokal sehingga pengukuran dapat diulang kembali.

## Cara Menjalankan

```bash
pip install -r requirements.txt
python src/main.py
```

Program akan menghasilkan:

- citra yang telah diberi noise;
- citra hasil penyaringan dari ketiga metode;
- tabel CSV yang berisi MSE, PSNR, dan SSIM;
- visualisasi perbandingan.

## Reproduksibilitas

Seed acak ditetapkan pada konfigurasi eksperimen sehingga noise dan hasil pengukuran dapat direproduksi. Tidak ada hasil eksperimen yang ditulis secara manual atau dibuat-buat di dalam repository.

## Keterkaitan dengan Tugas

Proyek ini dirancang agar memenuhi persyaratan Final Project Pengolahan Sinyal Digital dengan mencakup eksperimen pengolahan citra, minimal tiga skenario eksperimen, evaluasi kuantitatif, visualisasi, dan keluaran yang siap dianalisis untuk paper ilmiah.
