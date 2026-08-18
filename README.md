# DSP Image Filtering Research

**Final Project — Pengolahan Sinyal Digital**

## Research Topic

**Comparison of Mean, Gaussian, and Median Filtering for Salt-and-Pepper Noise Reduction in Digital Images**

## Research Objective

This project experimentally compares three spatial filtering methods for reducing salt-and-pepper noise in digital images:

- Mean Filter, 3×3 kernel
- Gaussian Filter, 5×5 kernel
- Median Filter, 5×5 kernel

The experiments evaluate the processed images against the corresponding clean reference images using **MSE, PSNR, and SSIM**.

## Experimental Pipeline

```text
Clean image
    ↓
Preprocessing / grayscale
    ↓
Add salt-and-pepper noise
    ↓
┌──────────────┬───────────────┬───────────────┐
│ Mean 3×3     │ Gaussian 5×5  │ Median 5×5    │
└──────────────┴───────────────┴───────────────┘
    ↓
MSE / PSNR / SSIM
    ↓
Tables + visualizations
```

## Repository Structure

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

The current implementation uses reproducible sample images provided by `scikit-image` (`camera`, `coins`, and `moon`) as clean reference images. The code saves generated noisy images and filtered outputs locally so the reported measurements can be reproduced.

## How to Run

```bash
pip install -r requirements.txt
python src/main.py
```

The script generates:

- noisy images;
- filtered images for all three methods;
- a CSV table containing MSE, PSNR, and SSIM;
- comparison figures.

## Reproducibility

The random seed is fixed in the experiment configuration so that the generated noise and measurements can be reproduced. No experimental result is hard-coded in the repository.

## Relation to the Course Assignment

The project is designed to satisfy the final-project requirements for DSP by including a real image-processing experiment, at least three experimental scenarios, quantitative evaluation, visualization, and analysis-ready outputs.
