from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from skimage import data, img_as_ubyte

from evaluation import evaluate
from filtering import gaussian_filter, mean_filter, median_filter
from generate_noise import add_salt_pepper_noise

ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs"
FIGURES = OUTPUTS / "figures"
NOISY = ROOT / "data" / "noisy"

SEED = 42
NOISE_AMOUNT = 0.05

FILTERS = {
    "Mean": lambda image: mean_filter(image, 3),
    "Gaussian": lambda image: gaussian_filter(image, 5),
    "Median": lambda image: median_filter(image, 5),
}


def load_dataset() -> dict[str, np.ndarray]:
    """Load small reproducible grayscale reference images from scikit-image."""
    return {
        "camera": img_as_ubyte(data.camera()),
        "coins": img_as_ubyte(data.coins()),
        "moon": img_as_ubyte(data.moon()),
    }


def save_image(path: Path, image: np.ndarray) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.imsave(path, image, cmap="gray", vmin=0, vmax=255)


def run() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    NOISY.mkdir(parents=True, exist_ok=True)

    rows: list[dict[str, object]] = []
    dataset = load_dataset()

    for index, (name, reference) in enumerate(dataset.items()):
        noisy_seed = SEED + index
        noisy = add_salt_pepper_noise(reference, amount=NOISE_AMOUNT, seed=noisy_seed)
        save_image(NOISY / f"{name}_noisy.png", noisy)

        for method_name, method in FILTERS.items():
            filtered = method(noisy)
            method_dir = OUTPUTS / method_name.lower()
            save_image(method_dir / f"{name}.png", filtered)

            metrics = evaluate(reference, filtered)
            rows.append(
                {
                    "image": name,
                    "noise_type": "salt-and-pepper",
                    "noise_amount": NOISE_AMOUNT,
                    "method": method_name,
                    "kernel": "3x3" if method_name == "Mean" else "5x5",
                    **metrics,
                }
            )

        # One figure per source image for direct visual comparison.
        figure, axes = plt.subplots(1, 5, figsize=(15, 3.2))
        display_images = [
            ("Original", reference),
            ("Noisy", noisy),
            ("Mean 3x3", FILTERS["Mean"](noisy)),
            ("Gaussian 5x5", FILTERS["Gaussian"](noisy)),
            ("Median 5x5", FILTERS["Median"](noisy)),
        ]
        for ax, (title, image) in zip(axes, display_images):
            ax.imshow(image, cmap="gray", vmin=0, vmax=255)
            ax.set_title(title)
            ax.axis("off")
        figure.tight_layout()
        figure.savefig(FIGURES / f"{name}_comparison.png", dpi=200, bbox_inches="tight")
        plt.close(figure)

    results = pd.DataFrame(rows)
    results_dir = OUTPUTS / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    results.to_csv(results_dir / "metrics.csv", index=False)

    summary = (
        results.groupby("method", as_index=False)[["mse", "psnr_db", "ssim"]]
        .mean()
        .sort_values("psnr_db", ascending=False)
    )
    summary.to_csv(results_dir / "method_summary.csv", index=False)

    # Summary chart: average PSNR across the three reference images.
    figure, ax = plt.subplots(figsize=(7, 4))
    ax.bar(summary["method"], summary["psnr_db"])
    ax.set_ylabel("Average PSNR (dB)")
    ax.set_xlabel("Filtering method")
    ax.set_title("Average PSNR by Filtering Method")
    figure.tight_layout()
    figure.savefig(FIGURES / "average_psnr.png", dpi=200, bbox_inches="tight")
    plt.close(figure)

    print("Experiment complete.")
    print(f"Results: {results_dir / 'metrics.csv'}")
    print(f"Summary: {results_dir / 'method_summary.csv'}")
    print(summary.to_string(index=False))


if __name__ == "__main__":
    run()
