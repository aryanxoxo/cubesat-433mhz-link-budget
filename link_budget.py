"""433 MHz CubeSat downlink link-budget model.

The constants below are example reconstruction values. Replace them with
measured ALEASAT / UBC ORBIT radio, antenna, and ground-station values when
available.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


FREQUENCY_MHZ = 433.5
TX_POWER_DBM = 10.0
TX_ANTENNA_GAIN_DBI = 0.0
RX_ANTENNA_GAIN_DBI = 10.0
CABLE_LOSS_DB = 1.5
POLARIZATION_LOSS_DB = 2.0
POINTING_LOSS_DB = 1.0
IMPLEMENTATION_MARGIN_DB = 0.5
RECEIVER_SENSITIVITY_DBM = -110.0
NOISE_FIGURE_DB = 6.0
RX_BANDWIDTH_HZ = 12_500.0
DATA_RATE_BPS = 1_200.0

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
FIGURE_DIR = ROOT / "figures"


def fspl_db(range_km: np.ndarray | float, frequency_mhz: float = FREQUENCY_MHZ) -> np.ndarray | float:
    """Free-space path loss in dB."""
    return 20 * np.log10(range_km) + 20 * np.log10(frequency_mhz) + 32.44


def thermal_noise_dbm(bandwidth_hz: float, noise_figure_db: float) -> float:
    """Receiver noise floor in dBm."""
    return -174.0 + 10 * np.log10(bandwidth_hz) + noise_figure_db


def received_power_dbm(range_km: np.ndarray) -> np.ndarray:
    losses = CABLE_LOSS_DB + POLARIZATION_LOSS_DB + POINTING_LOSS_DB + IMPLEMENTATION_MARGIN_DB
    return TX_POWER_DBM + TX_ANTENNA_GAIN_DBI + RX_ANTENNA_GAIN_DBI - fspl_db(range_km) - losses


def build_link_budget() -> pd.DataFrame:
    ranges_km = np.array([500, 700, 900, 1_100, 1_300, 1_500, 1_800, 2_100, 2_500], dtype=float)
    pr_dbm = received_power_dbm(ranges_km)
    noise_dbm = thermal_noise_dbm(RX_BANDWIDTH_HZ, NOISE_FIGURE_DB)
    cn_db = pr_dbm - noise_dbm
    ebn0_db = cn_db - 10 * np.log10(DATA_RATE_BPS / RX_BANDWIDTH_HZ)
    link_margin_db = pr_dbm - RECEIVER_SENSITIVITY_DBM

    return pd.DataFrame(
        {
            "range_km": ranges_km,
            "frequency_mhz": FREQUENCY_MHZ,
            "fspl_db": fspl_db(ranges_km),
            "tx_power_dbm": TX_POWER_DBM,
            "tx_gain_dbi": TX_ANTENNA_GAIN_DBI,
            "rx_gain_dbi": RX_ANTENNA_GAIN_DBI,
            "total_losses_db": CABLE_LOSS_DB + POLARIZATION_LOSS_DB + POINTING_LOSS_DB + IMPLEMENTATION_MARGIN_DB,
            "received_power_dbm": pr_dbm,
            "noise_floor_dbm": noise_dbm,
            "carrier_to_noise_db": cn_db,
            "ebn0_db": ebn0_db,
            "receiver_sensitivity_dbm": RECEIVER_SENSITIVITY_DBM,
            "link_margin_db": link_margin_db,
        }
    )


def plot_link_margin(df: pd.DataFrame) -> None:
    FIGURE_DIR.mkdir(exist_ok=True)
    fig, ax = plt.subplots(figsize=(8, 5), dpi=160)
    ax.plot(df["range_km"], df["link_margin_db"], marker="o", linewidth=2, label="Link margin")
    ax.axhline(0, color="tab:red", linestyle="--", linewidth=1.2, label="0 dB margin")
    ax.set_title("433 MHz CubeSat Link Margin vs Slant Range")
    ax.set_xlabel("Slant range (km)")
    ax.set_ylabel("Link margin (dB)")
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "link_margin_vs_range.png")
    plt.close(fig)


def main() -> None:
    DATA_DIR.mkdir(exist_ok=True)
    df = build_link_budget()
    df.to_csv(DATA_DIR / "example_link_budget.csv", index=False)
    plot_link_margin(df)
    print(df.to_string(index=False, float_format=lambda value: f"{value:0.2f}"))
    print("\nWrote data/example_link_budget.csv")
    print("Wrote figures/link_margin_vs_range.png")


if __name__ == "__main__":
    main()

