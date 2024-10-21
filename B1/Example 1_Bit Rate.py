def calculate_bit_rate(bits_per_element, signal_elements_per_sec):
    bit_rate = bits_per_element * signal_elements_per_sec
    return bit_rate

r = 4  
S = 1000  
bit_rate = calculate_bit_rate(r, S)
print("The bit rate is:", bit_rate, "bps")
