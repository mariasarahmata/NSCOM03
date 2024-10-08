import numpy as np
import matplotlib.pyplot as plt

f = 1  

fs = 4 * f

cycles = 2.5

t = np.linspace(0, cycles/f, 1250)  
ts = np.linspace(0, cycles/f, int(fs * cycles + 1))[:-1]  

y = np.sin(2 * np.pi * f * t)
ys = np.sin(2 * np.pi * f * ts)

plt.figure(figsize=(14, 3))
plt.plot(t, y, label='Continuous Sine Wave', color='magenta')

plt.scatter(ts, ys, color='black', label='Samples at $f_s = 4f$')

plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.axhline(0, color='black', linewidth=0.5)
plt.legend()

plt.xlim(t[0], t[-1])

plt.tight_layout()  
plt.show()
