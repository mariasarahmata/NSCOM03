# Given data
bandwidth_khz = 200  # Bandwidth in kHz

# Nyquist theorem: minimum sampling rate is 2 times the highest frequency (bandwidth)
minimum_sampling_rate = 2 * bandwidth_khz  # in kHz

# Convert to samples per second
minimum_sampling_rate_samples_per_second = minimum_sampling_rate * 1000  # kHz to Hz

# Print result
print(f"Minimum Sampling Rate: {minimum_sampling_rate_samples_per_second} samples per second")
