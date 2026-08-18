from __future__ import annotations

import numpy as np
from skimage.metrics import mean_squared_error, peak_signal_noise_ratio, structural_similarity


def evaluate(reference: np.ndarray, processed: np.ndarray) -> dict[str, float]:
    """Mengembalikan nilai MSE, PSNR, dan SSIM untuk dua citra grayscale uint8."""
    reference_f = reference.astype(np.float64)
    processed_f = processed.astype(np.float64)

    mse = float(mean_squared_error(reference_f, processed_f))
    psnr = float(peak_signal_noise_ratio(reference_f, processed_f, data_range=255))
    ssim = float(structural_similarity(reference_f, processed_f, data_range=255))

    return {
        "mse": mse,
        "psnr_db": psnr,
        "ssim": ssim,
    }
