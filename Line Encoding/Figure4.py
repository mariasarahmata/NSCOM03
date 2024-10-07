import numpy as np
import matplotlib.pyplot as plt

data_bits = '1101'
signal_mapping = {
    '1101': [1, -0.5, 0.5]
}

signal = signal_mapping[data_bits]

time_vector = np.linspace(0, 3, num=300, endpoint=True)

fig, ax = plt.subplots(figsize=(6, 4))

ax.step(time_vector, np.repeat(signal, 100), where='post', linewidth=2, color='magenta', label='Signal Level')

ax.axhline(y=0, color='black', linewidth=1.5, label='Zero Level')

ax.set_xlabel('Time')
ax.set_ylabel('Signal Level')
ax.set_ylim(-1.5, 1.5)
ax.set_xlim(0, 3)
ax.grid(True)

ax.legend()

plt.show()
