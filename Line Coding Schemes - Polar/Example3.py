# Given data
data_rate_mbps = 1  # 1 Mbps (Megabits per second)
c = 1 / 2  # Average case for NRZ-I (worst case c = 1, best case c = 0)
N = 1  # Number of bits per signal element in NRZ-I
R = data_rate_mbps * 10**6  # Convert data rate to bits per second (bps)

# Average signal rate (baud rate) calculation
signal_rate = c * N * R  # Baud rate in baud (symbols per second)

# Minimum bandwidth calculation
min_bandwidth = signal_rate  # Bandwidth in Hz (for NRZ-I, bandwidth = baud rate)

# Print results
print(f"Average signal rate (baud rate): {signal_rate / 1000} kbaud")
print(f"Minimum bandwidth: {min_bandwidth / 1000} kHz")
