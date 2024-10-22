# Given values
bandwidth = 100  # kHz
delta_f = 25     # kHz (half of 2Δf)
d = 1            # Modulation factor

# Calculate signal rate (baud rate)
signal_rate = (bandwidth - 2 * delta_f) / (1 + d)

# Calculate bit rate (assuming r = 1)
bit_rate = signal_rate * 1  # r = 1

# Carrier frequency is the midpoint of the given band
carrier_frequency = (200 + 300) / 2  # kHz

# Display the results
print(f"Carrier Frequency (fc): {carrier_frequency} kHz")
print(f"Baud Rate (S): {signal_rate} kbaud")
print(f"Bit Rate (N): {bit_rate} kbps")
