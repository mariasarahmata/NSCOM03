import numpy as np
import matplotlib.pyplot as plt

# Data bits
data_bits = [1, 0, 1, 1, 0]

# Initializing signal levels for NRZ-I
signal = np.zeros(len(data_bits))
current_level = 1  # Start signal (+1)

# NRZ-I logic: Invert on 1, hold on 0
for i in range(len(data_bits)):
    if data_bits[i] == 1:
        current_level = -current_level
    signal[i] = current_level

# Time vector
time_vector = np.linspace(0, len(data_bits), num=len(data_bits) * 100, endpoint=True)

# Plotting
plt.figure(figsize=(8, 5))
plt.step(time_vector, np.repeat(signal, 100), where='post', linewidth=2, color='#C71585')  # Dark pink color
plt.title('NRZ-I Encoding')
plt.xlabel('Time')
plt.ylabel('Signal Level')
plt.grid(True)
plt.xticks(np.arange(len(data_bits) + 1), labels=[str(i) for i in range(len(data_bits) + 1)])
plt.axhline(0, color='#A9A9A9', linewidth=1.5)  # Lighter gray line for zero level
plt.ylim(-1.5, 1.5)

# Data element boundaries
for i in range(len(data_bits) + 1):
    plt.axvline(x=i, color='#D3D3D3', linestyle='--')  # Lighter gray for vertical lines

plt.show()
