import numpy as np
import matplotlib.pyplot as plt

data_bits = [1, 0, 1] 

signal_patterns = {
    1: [1, 0],
    0: [0, 1]
}

signal = [level for bit in data_bits for level in signal_patterns[bit]]

time_vector = np.linspace(0, len(signal), num=len(signal) * 100, endpoint=True)

fig, ax = plt.subplots(figsize=(6, 4))
ax.step(time_vector, np.repeat(signal, 100), where='post', linewidth=2, color='magenta', label='Signal Level')
ax.set_xlabel('Time')
ax.set_ylabel('Signal Level')
ax.set_ylim(-0.5, 1.5)
ax.set_xlim(0, len(signal)) 
ax.grid(True)

for i in range(0, len(signal) + 1, 2):  
    ax.axvline(x=i, color='gray', linestyle='--', label='Data Element Boundary' if i == 0 else "")

ax.legend()

plt.show()
