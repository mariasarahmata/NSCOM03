import numpy as np
import matplotlib.pyplot as plt

f = 1  

cycles = 2.5

t = np.linspace(0, cycles/f, 1000)  

sample_times = np.array([0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25]) / f
sample_times = sample_times[sample_times <= max(t)]  

y = np.sin(2 * np.pi * f * t)
ys = np.sin(2 * np.pi * f * sample_times)

plt.figure(figsize=(10, 4))
plt.plot(t, y, label='Continuous Sine Wave', color='magenta')

plt.scatter(sample_times, ys, color='black', label='Samples at $f_s = f$')

plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.axhline(0, color='black', linewidth=0.5)
plt.legend()

plt.xlim(t[0], t[-1])

plt.tight_layout()  
plt.show()
