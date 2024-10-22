# Given values
bit_rate = 3e6  # 3 Mbps in bits per second
bits_per_symbol = 3  # 3 bits at a time
carrier_frequency = 10e6  # 10 MHz

# Calculate the number of levels (L)
L = 2 ** bits_per_symbol

# Calculate the baud rate (S)
baud_rate = bit_rate / bits_per_symbol

# Given 2Δf (frequency separation) as 1 MHz
delta_f = 1e6  # 1 MHz

# Calculate the bandwidth (B)
bandwidth = L * delta_f

# Display the results
print(f"Number of Levels (L): {L}")
print(f"Baud Rate (S): {baud_rate / 1e6} Mbaud")
print(f"Bandwidth (B): {bandwidth / 1e6} MHz")
