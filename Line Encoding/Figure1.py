import numpy as np
import matplotlib.pyplot as plt

data_bits = [1, 0, 1]

time_vector = np.linspace(0, len(data_bits), num=len(data_bits) * 100, endpoint=True)  

signal = np.repeat(data_bits, 100)

fig, ax = plt.subplots(figsize=(6, 4))
ax.step(time_vector, signal, where='post', linewidth=2, color='magenta', label='Signal Level')
ax.set_xlabel('Time')
ax.set_ylabel('Signal Level')
ax.set_ylim(-0.5, 1.5)
ax.set_xlim(0, len(data_bits))  
ax.set_yticks([0, 1])
ax.set_xticks(np.arange(len(data_bits) + 1))
ax.grid(True)

for i in range(len(data_bits) + 1):
    ax.axvline(x=i, color='gray', linestyle='--', label='Data Element Boundary' if i == 0 else "")  

# Add legend
ax.legend()

plt.show()
