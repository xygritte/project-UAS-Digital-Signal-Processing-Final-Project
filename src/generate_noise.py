from __future__ import annotations

import numpy as np
from skimage.util import random_noise


def add_salt_pepper_noise(image: np.ndarray, amount: float = 0.05, seed: int = 42) -> np.ndarray:
    """Menambahkan noise salt-and-pepper yang dapat direproduksi ke citra grayscale uint8."""
    if not 0.0 <= amount <= 1.0:
        raise ValueError("jumlah noise harus berada di antara 0 dan 1")

    rng = np.random.default_rng(seed)
    noisy = random_noise(
        image,
        mode="s&p",
        amount=amount,
        salt_vs_pepper=0.5,
        rng=rng,
        clip=True,
    )
    return np.clip(noisy * 255.0, 0, 255).round().astype(np.uint8)
