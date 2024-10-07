import matplotlib.pyplot as plt
import numpy as np

bits = np.array([1, 0, 1, 1, 0])

time = np.arange(0, len(bits))

signal = np.repeat(bits, 2)
time = np.repeat(time, 2)

time = np.append(time, time[-1] + 1)
signal = np.append(signal, signal[-1])

plt.figure(figsize=(10, 3))
plt.step(time, signal, where='post', linewidth=2, color='magenta', label='Unipolar NRZ Signal')
plt.xlim(0, len(bits))  
plt.ylim(-0.5, 1.5)
plt.xlabel('Time')
plt.ylabel('Amplitude (V)')
plt.grid(True)
plt.xticks(ticks=np.arange(0, len(bits) + 1))
plt.yticks([0, 1])

plt.legend()

plt.show()
