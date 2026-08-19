# Penelitian Penyaringan Citra Digital - Pengolahan Sinyal Digital

**Final Project - Pengolahan Sinyal Digital**

## Topik Penelitian

**Perbandingan Penyaringan Mean, Gaussian, dan Median untuk Mengurangi Noise Salt-and-Pepper pada Citra Digital**

## Tujuan Penelitian

Proyek ini membandingkan secara eksperimen tiga metode penyaringan spasial untuk mengurangi noise salt-and-pepper pada citra digital:

- Mean Filter dengan kernel 3x3
- Gaussian Filter dengan kernel 5x5
- Median Filter dengan kernel 5x5

Evaluasi menggunakan MSE, PSNR, dan SSIM.

## Alur Eksperimen

```text
Citra bersih
    ↓
Pra-pemrosesan / grayscale
    ↓
Penambahan noise salt-and-pepper
    ↓
┌──────────────┬────────────────┬───────────────┐
│ Mean 3x3     │ Gaussian 5x5   │ Median 5x5    │
└──────────────┴────────────────┴───────────────┘
    ↓
MSE / PSNR / SSIM
    ↓
Tabel + visualisasi + analisis
    ↓
Paper IEEE Conference
```

## Struktur Repository

```text
├── data/
├── outputs/
│   ├── figures/
│   └── results/
├── papper/
│   ├── Perbandingan Filtering Citra Digital.docx
│   ├── paper.tex
│   └── referensi.bib
├── src/
│   ├── generate_noise.py
│   ├── filtering.py
│   ├── evaluation.py
│   └── main.py
├── requirements.txt
└── README.md
```

## Data

Implementasi menggunakan tiga gambar contoh yang dapat direproduksi dari `scikit-image`, yaitu `camera`, `coins`, dan `moon`, sebagai citra referensi bersih. Program menghasilkan citra noisy dan hasil penyaringan secara deterministik menggunakan seed yang ditetapkan.

## Hasil Eksperimen

Rata-rata hasil dari tiga citra:

| Metode | MSE | PSNR (dB) | SSIM |
|---|---:|---:|---:|
| Mean 3x3 | 186,8367 | 25,7440 | 0,5275 |
| Gaussian 5x5 | 155,8329 | 26,7129 | 0,5985 |
| Median 5x5 | **89,2895** | **30,8361** | **0,8355** |

Median Filter menjadi metode terbaik pada ketiga metrik dan juga unggul secara konsisten pada `camera`, `coins`, dan `moon`.

## Cara Menjalankan

```bash
pip install -r requirements.txt
python src/main.py
```

Program menghasilkan:

- citra yang telah diberi noise;
- citra hasil penyaringan dari ketiga metode;
- `outputs/results/metrics.csv`;
- `outputs/results/method_summary.csv`;
- visualisasi perbandingan.

## Paper

Sumber paper IEEE tersedia pada:

- `papper/paper.tex`
- `papper/referensi.bib`
- `papper/Perbandingan Filtering Citra Digital.docx`

PDF final dibuat berdasarkan sumber tersebut dan hasil eksperimen aktual yang tersimpan di `outputs/results/`.

## Reproduksibilitas

Seed noise ditetapkan sehingga eksperimen dapat dijalankan kembali. Tidak ada hasil eksperimen yang ditulis secara manual atau dibuat-buat di dalam program.
