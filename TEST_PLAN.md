# Test Plan: Filling In the 433 MHz CubeSat Link Project

Use this checklist to replace the example assumptions in the scripts with real measured values.

## 1. TX Output Power

Goal: measure actual radio output at the transmitter antenna port.

Equipment:

- RF power meter or spectrum analyzer with suitable attenuation
- 433 MHz radio board
- Known attenuators and coax

Record:

- TX power in dBm
- modulation mode
- data rate
- supply voltage/current
- board temperature if available

Update:

- `TX_POWER_DBM` in `link_budget.py`

## 2. Receiver Sensitivity / Packet Success

Goal: find the received power where packets or bits start failing.

Equipment:

- signal generator or second radio
- step attenuator
- receiver board or SDR
- packet counter or BER test script

Procedure:

1. Send a known payload repeatedly.
2. Step attenuation in 1 to 3 dB increments.
3. Count received packets, CRC failures, and bit errors.
4. Record the input power where BER reaches targets such as `1e-3` and `1e-5`.

Update:

- `RECEIVER_SENSITIVITY_DBM`
- measured points in the BER plot, if you add them

## 3. Frequency Error / PPM

Goal: quantify oscillator drift and Doppler correction needs.

Equipment:

- spectrum analyzer or SDR
- known 433 MHz reference signal

Record:

- center frequency error in Hz
- PPM error
- drift after warmup
- drift over temperature if possible

Use:

- helps explain frequency correction and receiver acquisition margin

## 4. Antenna Gain and Pattern

Goal: estimate or measure antenna gain for both spacecraft and ground sides.

Options:

- use datasheet or simulation values if hardware is unavailable
- measure relative pattern with a VNA/signal source and turntable
- document assumptions clearly

Update:

- `TX_ANTENNA_GAIN_DBI`
- `RX_ANTENNA_GAIN_DBI`
- `POINTING_LOSS_DB`
- `POLARIZATION_LOSS_DB`

## 5. Cable and Connector Loss

Goal: measure feedline loss around 433 MHz.

Equipment:

- VNA or calibrated signal source/power meter

Record:

- cable type and length
- connector/adaptor count
- insertion loss in dB at 433 MHz

Update:

- `CABLE_LOSS_DB`

## 6. Bandwidth and Data Rate

Goal: document actual occupied bandwidth and data throughput.

Record:

- modulation type: 2-FSK, GFSK, MSK, etc.
- bit rate
- receiver bandwidth
- frequency deviation
- packet length and coding/checksum

Update:

- `RX_BANDWIDTH_HZ`
- `DATA_RATE_BPS`
- BER curve choice in `ber_model.py`

## 7. Over-the-Air Sanity Test

Goal: demonstrate the link over a controlled local path before orbital assumptions.

Record:

- distance
- antenna orientation
- RSSI or received power estimate
- packet success rate
- observed dropouts

Use:

- compare measured received power against the model at short range
- explain differences due to multipath, polarization, and antenna mismatch

## Strong Evidence To Add Later

- photo of radio boards and test setup
- screenshot of spectrum analyzer at 433 MHz
- table of attenuation vs packet success
- measured BER/PER curve overlay
- VNA screenshot for antenna or filter
- final link budget table with real values
- short paragraph explaining whether link margin was enough for low-elevation passes

