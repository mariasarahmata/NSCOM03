import numpy as np
import matplotlib.pyplot as plt

# Data bits
data_bits = [1, 0, 1, 1, 0]

# Differential Manchester encoding: Transition at the start for 0, middle for both
signal = []
current_level = 1  # Starting level

for bit in data_bits:
    if bit == 1:
        signal.extend([current_level, -current_level])  # Invert at the middle for 1
    else:
        signal.extend([-current_level, current_level])  # Transition at the start for 0
    current_level = -current_level  # Invert for next bit

# Time vector
time_vector = np.linspace(0, len(signal)/2, num=len(signal) * 50, endpoint=True)

# Plotting
plt.figure(figsize=(8, 5))
plt.step(time_vector, np.repeat(signal, 50), where='post', linewidth=2, color='#C71585')  
plt.title('Differential Manchester Encoding')
plt.xlabel('Time')
plt.ylabel('Signal Level')
plt.grid(True)
plt.xticks(np.arange(len(data_bits) + 1), labels=[str(i) for i in range(len(data_bits) + 1)])
plt.axhline(0, color='#A9A9A9', linewidth=1.5)  
plt.ylim(-1.5, 1.5)

# Data element boundaries
for i in range(len(data_bits) + 1):
    plt.axvline(x=i, color='#D3D3D3', linestyle='--')  

plt.show()
