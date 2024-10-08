import numpy as np
import matplotlib.pyplot as plt

f = 1  

cycles = 2.5

t = np.linspace(0, cycles/f, 1000)

ts = np.linspace(0, cycles/f, int(4 * cycles + 1))
ys = np.sin(2 * np.pi * f * ts)

y = np.sin(2 * np.pi * f * t)

plt.figure(figsize=(10, 4))
plt.plot(t, y, label='Continuous Sine Wave', color='magenta')

plt.scatter(ts, ys, color='black', label='Samples (Peaks, Troughs, and Zero Crossings)')

plt.xlim(0, cycles/f)

plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.axhline(0, color='black', linewidth=0.5)
plt.legend()

plt.tight_layout()  
plt.show()
