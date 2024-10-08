import numpy as np
import matplotlib.pyplot as plt

# Generate an analog signal (sine wave for example)
fs = 1000  # Sampling rate (1000 samples per second)
f = 5  # Frequency of the signal (5 Hz)
t = np.linspace(0, 1, fs)  # Time vector for 1 second
analog_signal = np.sin(2 * np.pi * f * t)

# Ideal sampling: Sample the signal at regular intervals
sampling_interval = 0.05  # Sampling interval (every 50ms)
sample_times = np.arange(0, 1, sampling_interval)
sampled_signal = np.sin(2 * np.pi * f * sample_times)

# Flat-top sampling: Hold each sampled value constant
pulse_width = 0.02  # Width of each pulse
flat_top_sampled_signal = np.zeros_like(t)

for sample_time, sample_value in zip(sample_times, sampled_signal):
    pulse_start = int(sample_time * fs)
    pulse_end = int((sample_time + pulse_width) * fs)
    flat_top_sampled_signal[pulse_start:pulse_end] = sample_value

# Plot the flat-top sampled signal
plt.figure(figsize=(8, 5))
plt.plot(t, analog_signal, label='Analog Signal', color='#C71585')  # Dark pink
plt.plot(t, flat_top_sampled_signal, label='Flat-Top Sampled Signal', color='blue')  # Flat-top Sampling
plt.title('Flat-Top Sampling of an Analog Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()
