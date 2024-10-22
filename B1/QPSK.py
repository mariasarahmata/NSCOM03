import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000  # Sampling frequency (samples per second)
bit_duration = 1  # Duration of each bit in seconds
f_c = 5  # Carrier frequency in Hz
bits = [0, 1, 0, 0, 1, 1, 1, 0]  # Example bit stream

# Generate time for one bit
t = np.linspace(0, bit_duration, fs * bit_duration, endpoint=False)

# Map bits to QPSK symbols (00, 01, 10, 11)
# 00 -> 0°, 01 -> 90°, 10 -> 180°, 11 -> 270°
bit_pairs = [(bits[i], bits[i+1]) for i in range(0, len(bits), 2)]
phase_shifts = {
    (0, 0): 0,
    (0, 1): np.pi/2,
    (1, 0): np.pi,
    (1, 1): 3*np.pi/2
}

# Generate QPSK signal
qpsk_signal = np.array([])

for pair in bit_pairs:
    phase_shift = phase_shifts[pair]
    modulated_signal = np.sin(2 * np.pi * f_c * t + phase_shift)
    qpsk_signal = np.concatenate((qpsk_signal, modulated_signal))

# Generate time for the entire bit stream
t_full = np.linspace(0, bit_duration * len(bit_pairs), fs * bit_duration * len(bit_pairs), endpoint=False)

# Plot the QPSK signal
plt.figure(figsize=(10, 5))
plt.plot(t_full, qpsk_signal)
plt.title("Quadrature Phase Shift Keying (QPSK)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()
