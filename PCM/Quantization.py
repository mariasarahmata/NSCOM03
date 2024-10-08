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

# Quantization
quantization_levels = 8  # Number of quantization levels
min_val = -1  # Minimum amplitude of the signal
max_val = 1  # Maximum amplitude of the signal

# Compute the quantization step size (delta)
delta = (max_val - min_val) / quantization_levels

# Quantize the sampled signal
quantized_signal = np.round((sampled_signal - min_val) / delta) * delta + min_val

# Plot the quantized signal
plt.figure(figsize=(8, 5))
plt.plot(t, analog_signal, label='Analog Signal', color='#C71585')  
plt.stem(sample_times, quantized_signal, linefmt='gray', markerfmt='bo', label='Quantized Signal')  # Quantized signal
plt.title('Quantization of Sampled Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()
