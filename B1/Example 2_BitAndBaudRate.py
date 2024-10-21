import math

def calculate_levels(bit_rate, baud_rate):
    r = bit_rate / baud_rate

    L = 2 ** r

    return L

N = 8000  
S = 1000 
levels = calculate_levels(N, S)
print("The number of levels per signal element is:", levels)


