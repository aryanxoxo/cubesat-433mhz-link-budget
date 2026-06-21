"""BER curves for common binary modulation assumptions.

The curves are analytical references. Add measured BER/PER points from a radio
or attenuator test when available.
"""

from __future__ import annotations

from math import erfc
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent
FIGURE_DIR = ROOT / "figures"


def q_function(x: np.ndarray) -> np.ndarray:
    return np.vectorize(lambda value: 0.5 * erfc(value / np.sqrt(2)))(x)


def ber_bpsk_awgn(ebn0_db: np.ndarray) -> np.ndarray:
    ebn0_linear = 10 ** (ebn0_db / 10)
    return 0.5 * np.vectorize(erfc)(np.sqrt(ebn0_linear))


def ber_noncoherent_fsk(ebn0_db: np.ndarray) -> np.ndarray:
    ebn0_linear = 10 ** (ebn0_db / 10)
    return 0.5 * np.exp(-ebn0_linear / 2)


def ber_coherent_fsk(ebn0_db: np.ndarray) -> np.ndarray:
    ebn0_linear = 10 ** (ebn0_db / 10)
    return q_function(np.sqrt(ebn0_linear))


def plot_ber() -> None:
    FIGURE_DIR.mkdir(exist_ok=True)
    ebn0_db = np.linspace(0, 16, 161)

    fig, ax = plt.subplots(figsize=(8, 5), dpi=160)
    ax.semilogy(ebn0_db, ber_bpsk_awgn(ebn0_db), linewidth=2, label="BPSK coherent AWGN")
    ax.semilogy(ebn0_db, ber_coherent_fsk(ebn0_db), linewidth=2, label="Coherent BFSK approx.")
    ax.semilogy(ebn0_db, ber_noncoherent_fsk(ebn0_db), linewidth=2, label="Noncoherent BFSK approx.")
    ax.axhline(1e-3, color="tab:red", linestyle="--", linewidth=1.2, label="BER = 1e-3")
    ax.axhline(1e-5, color="tab:green", linestyle=":", linewidth=1.2, label="BER = 1e-5")
    ax.set_title("BER vs Eb/N0 Reference Curves")
    ax.set_xlabel("Eb/N0 (dB)")
    ax.set_ylabel("Bit error rate")
    ax.set_ylim(1e-7, 1)
    ax.grid(True, which="both", alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "ber_vs_ebn0.png")
    plt.close(fig)


def main() -> None:
    plot_ber()
    print("Wrote figures/ber_vs_ebn0.png")


if __name__ == "__main__":
    main()

