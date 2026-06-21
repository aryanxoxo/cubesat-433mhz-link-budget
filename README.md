# UBC ORBIT ALEASAT 433 MHz CubeSat Radio Link

Public link-budget and BER modeling package for a 433 MHz CubeSat UHF downlink study. The files here document the engineering method: free-space path loss, received power, receiver noise floor, link margin, and BER sensitivity versus Eb/N0.

The numeric values in this public repository are placeholder assumptions for demonstration. They are intentionally not station-specific, flight-specific, or hardware-sensitive values. Keep private radio settings, measured hardware performance, detailed antenna data, and any mission-sensitive parameters in a local/private analysis copy.

## Contents

```text
README.md
link_budget.py
ber_model.py
data/
  example_link_budget.csv
figures/
  ber_vs_ebn0.png
  link_margin_vs_range.png
notebooks/
  433mhz_link_budget.ipynb
```

## Quick Start

```bash
python link_budget.py
python ber_model.py
```

Outputs:

- `data/example_link_budget.csv`
- `figures/link_margin_vs_range.png`
- `figures/ber_vs_ebn0.png`

## Engineering Model

Free-space path loss:

```text
FSPL(dB) = 20log10(range_km) + 20log10(frequency_MHz) + 32.44
```

Received power:

```text
Pr(dBm) = Ptx + Gtx + Grx - FSPL - losses
```

Thermal noise floor:

```text
N(dBm) = -174 + 10log10(BW_Hz) + NF
```

Carrier-to-noise ratio:

```text
C/N(dB) = Pr - N
```

Approximate Eb/N0:

```text
Eb/N0(dB) = C/N(dB) - 10log10(data_rate / bandwidth)
```

## Public Placeholder Assumptions

These values are intentionally generic and editable:

| Parameter | Example |
|---|---:|
| Frequency | 433.5 MHz |
| TX power | 10 dBm |
| TX antenna gain | 0 dBi |
| RX antenna gain | 10 dBi |
| Cable / polarization / implementation loss | 5 dB total |
| Receiver noise figure | 6 dB |
| Receiver bandwidth | 12.5 kHz |
| Data rate | 1.2 kbps |
| Receiver sensitivity reference | -110 dBm |
| LEO slant range sweep | 500 to 2500 km |

## Private Values To Keep Local

For internal engineering work, use a private/local copy to substitute:

- Measured TX output power at the antenna port.
- Measured or simulated antenna gain pattern.
- RX antenna gain and cable loss.
- SDR/radio receiver sensitivity at target BER or packet error rate.
- Measured packet success rate versus attenuation.
- Measured frequency error / drift.
- Real modulation settings, such as 2-FSK, GFSK, or MSK.
- Real occupied bandwidth and data rate.

Do not publish values that expose proprietary hardware behavior, mission constraints, or unreleased station performance.

## Portfolio Description

Modeled a 433 MHz CubeSat radio link for ALEASAT / UBC ORBIT using link-budget and BER calculations. The analysis estimates received power, noise floor, link margin, and expected BER across LEO slant ranges, then identifies the required antenna gain, receiver sensitivity, and fade margin for reliable ground-station downlink.
