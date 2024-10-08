import numpy as np
import matplotlib.pyplot as plt

# Data bits for Pseudoternary
data_bits_pseudoternary = [0, 1, 0, 0, 1, 1, 0, 1, 0, 0]

# Pseudoternary signal: 1 is 0V, 0 alternates between +1 and -1
signal_pseudoternary = []
current_level = 1  # Start with positive level for 0s

for bit in data_bits_pseudoternary:
    if bit == 0:
        signal_pseudoternary.append(current_level)
        current_level = -current_level  # Alternate between +1 and -1 for consecutive 0s
    else:
        signal_pseudoternary.append(0)  # Zero voltage for 1s

# Time vector for the signal
time_vector_pseudoternary = np.linspace(0, len(data_bits_pseudoternary), num=len(data_bits_pseudoternary) * 100, endpoint=True)

# Plotting Pseudoternary signal
plt.figure(figsize=(8, 5))
plt.step(time_vector_pseudoternary, np.repeat(signal_pseudoternary, 100), where='post', linewidth=2, color='#C71585')
plt.title('Pseudoternary Encoding')
plt.xlabel('Time')
plt.ylabel('Signal Level')
plt.grid(True)
plt.axhline(0, color='#A9A9A9', linewidth=1.5) 
plt.ylim(-1.5, 1.5)

# Data element boundaries
for i in range(len(data_bits_pseudoternary) + 1):
    plt.axvline(x=i, color='#D3D3D3', linestyle='--')  

plt.show()
