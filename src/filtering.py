from __future__ import annotations

import cv2
import numpy as np


def mean_filter(image: np.ndarray, kernel_size: int = 3) -> np.ndarray:
    """Menerapkan filter mean (box) yang dinormalisasi."""
    if kernel_size % 2 == 0 or kernel_size < 3:
        raise ValueError("ukuran kernel harus bilangan ganjil >= 3")
    return cv2.blur(image, (kernel_size, kernel_size))


def gaussian_filter(image: np.ndarray, kernel_size: int = 5, sigma: float = 0.0) -> np.ndarray:
    """Menerapkan penghalusan Gaussian."""
    if kernel_size % 2 == 0 or kernel_size < 3:
        raise ValueError("ukuran kernel harus bilangan ganjil >= 3")
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), sigmaX=sigma)


def median_filter(image: np.ndarray, kernel_size: int = 5) -> np.ndarray:
    """Menerapkan filter median yang umum digunakan untuk noise salt-and-pepper."""
    if kernel_size % 2 == 0 or kernel_size < 3:
        raise ValueError("ukuran kernel harus bilangan ganjil >= 3")
    return cv2.medianBlur(image, kernel_size)
