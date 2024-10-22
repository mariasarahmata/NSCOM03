import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000  # Sampling frequency (samples per second)
duration = 1  # Duration of each bit sequence in seconds
n_bits = 3  # Number of bits per signal element
L = 2**n_bits  # Number of levels (frequencies)
frequencies = np.linspace(5, 20, L)  # Define 8 different frequencies for 3-bit sequences
t = np.linspace(0, duration, fs * duration)

# Generate random bit sequences and map to frequencies
np.random.seed(42)  # For reproducible results
bit_sequences = np.random.randint(0, L, size=5)  # Generate 5 random 3-bit sequences
signals = [np.sin(2 * np.pi * frequencies[seq] * t) for seq in bit_sequences]

# Concatenate the signals
full_signal = np.concatenate(signals)
t_full = np.linspace(0, duration * len(bit_sequences), len(full_signal))

# Plot the signal
plt.figure(figsize=(12, 6))
plt.plot(t_full, full_signal)
plt.title(f"Multi-level FSK (3 Bits per Symbol, {L} Levels)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()
