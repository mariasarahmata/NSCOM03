import matplotlib.pyplot as plt
import numpy as np

# Define the codes for each station
codes = {
    1: np.array([-1, -1, -1, -1]),
    2: np.array([-1, +1, -1, +1]),
    3: np.array([0, 0, 0, 0]),  # Silent station
    4: np.array([+1, -1, -1, +1])
}

# Define the bits each station transmits (0 or 1)
bits = {
    1: 0,
    2: 0,
    3: None,  # Silent
    4: 1
}

# Encode the data: if bit is 1, use code as-is; if bit is 0, invert the code
encoded_signals = {}
for station, bit in bits.items():
    if bit is None:  # Silent station
        encoded_signals[station] = codes[station]
    elif bit == 1:
        encoded_signals[station] = codes[station]
    else:
        encoded_signals[station] = -codes[station]

# Calculate the composite signal on the channel by summing all encoded signals
composite_signal = sum(encoded_signals.values())

# Plotting
fig, axes = plt.subplots(5, 1, figsize=(8, 6), sharex=True)

# Colors for each station
colors = ['cyan', 'yellow', 'pink', 'black']

# Plot each station's signal as boxes
for idx, (station, signal) in enumerate(encoded_signals.items(), start=1):
    axes[idx - 1].bar(range(len(signal)), signal, color=colors[idx - 1], edgecolor="black", width=1)
    axes[idx - 1].set_ylim(-2, 2)
    axes[idx - 1].set_ylabel(f'Station {station}')
    axes[idx - 1].set_yticks([])
    axes[idx - 1].set_xticks(range(len(signal)))
    axes[idx - 1].set_xlim(-0.5, len(signal) - 0.5)

# Plot the composite signal as boxes
axes[-1].bar(range(len(composite_signal)), composite_signal, color='black', edgecolor="black", width=1)
axes[-1].set_ylim(-4, 4)
axes[-1].set_ylabel('Composite')
axes[-1].set_yticks([])
axes[-1].set_xticks(range(len(composite_signal)))
axes[-1].set_xlim(-0.5, len(composite_signal) - 0.5)

# Add titles and labels
axes[-1].set_xlabel("Time")

plt.tight_layout()
plt.show()
