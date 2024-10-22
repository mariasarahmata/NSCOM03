# Given values
bit_rate = 12e6  # 12 Mbps in bits per second
bits_per_symbol = 2  # For QPSK, 2 bits per symbol
d = 0  # Modulation factor

# Calculate the signal rate (baud rate)
baud_rate = bit_rate / bits_per_symbol

# Calculate the bandwidth (B)
bandwidth = (1 + d) * baud_rate

# Display the results
print(f"Bit Rate (N): {bit_rate / 1e6} Mbps")
print(f"Bits per Symbol (r): {bits_per_symbol}")
print(f"Baud Rate (S): {baud_rate / 1e6} Mbaud")
print(f"Bandwidth (B): {bandwidth / 1e6} MHz")
