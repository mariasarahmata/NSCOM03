import numpy as np
import matplotlib.pyplot as plt

# Generate an analog signal (sine wave for example)
fs = 1000  # Sampling rate
f = 5  # Frequency of the signal
t = np.linspace(0, 1, fs)  # Time vector for 1 second
analog_signal = np.sin(2 * np.pi * f * t)

# Ideal sampling: Sample the signal at regular intervals
sampling_interval = 0.05  # Sampling interval (every 50ms)
sample_times = np.arange(0, 1, sampling_interval)
sampled_signal = np.sin(2 * np.pi * f * sample_times)

# Plot the analog signal and sampled signal
plt.figure(figsize=(8, 5))
plt.plot(t, analog_signal, label='Analog Signal', color='#C71585')  # Dark pink
plt.stem(sample_times, sampled_signal, linefmt='gray', markerfmt='go', label='Sampled Signal')  # Removed use_line_collection
plt.title('Ideal Sampling of an Analog Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()
