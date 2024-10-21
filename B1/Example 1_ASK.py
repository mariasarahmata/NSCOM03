def calculate_ask_parameters(bandwidth, lower_freq, upper_freq, d=1, r=1):
    carrier_frequency = (lower_freq + upper_freq) / 2
    
    bit_rate = bandwidth / (1 + d) * r  

    return carrier_frequency, bit_rate

bandwidth_khz = 100  
lower_freq_khz = 200  
upper_freq_khz = 300  

carrier_freq_khz, bit_rate_kbps = calculate_ask_parameters(bandwidth_khz, lower_freq_khz, upper_freq_khz)

print(f"Carrier Frequency: {carrier_freq_khz} kHz")
print(f"Bit Rate: {bit_rate_kbps} kbps")



