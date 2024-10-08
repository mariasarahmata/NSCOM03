import numpy as np
import matplotlib.pyplot as plt

# Data bits
data_bits = [1, 0, 1, 1, 0]

# NRZ-L Signal: +1 for 1, -1 for 0
signal = np.array([1 if bit == 1 else -1 for bit in data_bits])

# Time vector
time_vector = np.linspace(0, len(data_bits), num=len(data_bits) * 100, endpoint=True)

# Plotting
plt.figure(figsize=(8, 5))
plt.step(time_vector, np.repeat(signal, 100), where='post', linewidth=2, color='#C71585')
plt.title('NRZ-L Encoding')
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
