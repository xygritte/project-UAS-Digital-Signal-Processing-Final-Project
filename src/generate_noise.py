from __future__ import annotations

import numpy as np
from skimage.util import random_noise


def add_salt_pepper_noise(image: np.ndarray, amount: float = 0.05, seed: int = 42) -> np.ndarray:
    """Add reproducible salt-and-pepper noise to a grayscale uint8 image."""
    if not 0.0 <= amount <= 1.0:
        raise ValueError("amount must be between 0 and 1")

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
