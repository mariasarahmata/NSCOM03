import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000  # Sampling frequency
f1 = 5     # Frequency for '0'
f2 = 10    # Frequency for '1'
duration = 2  # Duration of each bit
t = np.linspace(0, duration, fs * duration)  # Time for one bit

# Coherent FSK: Phase alignment
coherent_signal_0 = np.sin(2 * np.pi * f1 * t)
coherent_signal_1 = np.sin(2 * np.pi * f2 * t)

# Non-Coherent FSK: No phase alignment
non_coherent_signal_0 = np.sin(2 * np.pi * f1 * t)
non_coherent_signal_1 = np.sin(2 * np.pi * f2 * t + np.pi / 4)  # Phase shift

# Concatenate time arrays for two signals
t_full = np.linspace(0, 2 * duration, fs * 2 * duration)

# Concatenate the coherent and non-coherent signals
coherent_full_signal = np.concatenate([coherent_signal_0, coherent_signal_1])
non_coherent_full_signal = np.concatenate([non_coherent_signal_0, non_coherent_signal_1])

# Plot the signals
plt.figure(figsize=(12, 6))

# Coherent FSK Signals
plt.subplot(2, 1, 1)
plt.title("Coherent FSK: Phase Aligned")
plt.plot(t_full, coherent_full_signal, label="Coherent FSK")
plt.legend()
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Non-Coherent FSK Signals
plt.subplot(2, 1, 2)
plt.title("Non-Coherent FSK: No Phase Alignment")
plt.plot(t_full, non_coherent_full_signal, label="Non-Coherent FSK", color='orange')
plt.legend()
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
