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

# Natural sampling: Using short-width pulses
pulse_width = 0.02  # Width of each pulse

# Create sampled signal for natural sampling (short pulses)
natural_sampled_signal = np.zeros_like(t)
for sample_time in sample_times:
    pulse_start = int(sample_time * fs)
    pulse_end = int((sample_time + pulse_width) * fs)
    natural_sampled_signal[pulse_start:pulse_end] = analog_signal[pulse_start:pulse_end]

# Plot the natural sampled signal
plt.figure(figsize=(8, 5))
plt.plot(t, analog_signal, label='Analog Signal', color='#C71585')  
plt.plot(t, natural_sampled_signal, label='Natural Sampled Signal', color='green')  # Natural Sampling
plt.title('Natural Sampling of an Analog Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()
