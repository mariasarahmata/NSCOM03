import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000  # Sampling frequency
bit_duration = 1  # Duration of each bit in seconds
f_c = 5  # Carrier frequency in Hz
bits = [0, 1, 1, 0, 1]  # Example bit stream

# Generate time for one bit
t = np.linspace(0, bit_duration, fs * bit_duration, endpoint=False)

# Generate BPSK signal
bpsk_signal = np.array([])

for bit in bits:
    # Phase shift: 0 for bit "1", pi for bit "0"
    phase_shift = 0 if bit == 1 else np.pi
    # Create the modulated signal for each bit
    modulated_signal = np.sin(2 * np.pi * f_c * t + phase_shift)
    # Concatenate the modulated signals to form the full BPSK signal
    bpsk_signal = np.concatenate((bpsk_signal, modulated_signal))

# Generate time for the entire bit stream
t_full = np.linspace(0, bit_duration * len(bits), fs * bit_duration * len(bits), endpoint=False)

# Plot the BPSK signal
plt.figure(figsize=(10, 5))
plt.plot(t_full, bpsk_signal)
plt.title("Binary Phase Shift Keying (BPSK)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
