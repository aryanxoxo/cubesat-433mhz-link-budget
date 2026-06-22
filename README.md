# UBC ORBIT ALEASAT 433 MHz CubeSat Radio Link

> Public archive note: this repository is a portfolio/demo-safe version prepared from private working repositories/materials; sensitive details, credentials, raw logs, and proprietary context are intentionally omitted.

Link-budget and BER modeling package for a 433 MHz CubeSat UHF downlink study. The files document the engineering method: free-space path loss, received power, receiver noise floor, link margin, and BER sensitivity versus Eb/N0.

The numeric values are reference assumptions for a reviewable public model. Project-specific radio settings, measured hardware performance, detailed antenna data, and mission parameters belong in a local engineering analysis copy.

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

## Reference Assumptions

These values are generic and editable:

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

## Values To Substitute During Hardware Validation

For hardware validation, substitute measured or project-specific values for:

- Measured TX output power at the antenna port.
- Measured or simulated antenna gain pattern.
- RX antenna gain and cable loss.
- SDR/radio receiver sensitivity at target BER or packet error rate.
- Measured packet success rate versus attenuation.
- Measured frequency error / drift.
- Real modulation settings, such as 2-FSK, GFSK, or MSK.
- Real occupied bandwidth and data rate.

## Portfolio Description

Modeled a 433 MHz CubeSat radio link for ALEASAT / UBC ORBIT using link-budget and BER calculations. The analysis estimates received power, noise floor, link margin, and expected BER across LEO slant ranges, then identifies the required antenna gain, receiver sensitivity, and fade margin for reliable ground-station downlink.
