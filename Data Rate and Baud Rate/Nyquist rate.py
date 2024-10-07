import math

def nyquist_rate(bandwidth, levels):
    return 2 * bandwidth * math.log2(levels)

bandwidth = 3000 
levels = 4 

max_data_rate = nyquist_rate(bandwidth, levels)
print(f"The maximum data rate: {max_data_rate:.2f} bps")


