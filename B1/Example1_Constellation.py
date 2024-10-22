import numpy as np
import matplotlib.pyplot as plt

# Create a figure for the three constellation diagrams
plt.figure(figsize=(15, 5))

# ASK (OOK) Constellation Diagram
plt.subplot(1, 3, 1)
# Define ASK points (only on the I axis)
ask_points = [(0, 0), (1, 0)]
for point, label in zip(ask_points, ['0', '1']):
    plt.scatter(point[0], point[1], color='magenta', s=100)
    plt.text(point[0] + 0.1, point[1], label, fontsize=12)
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.title("a. ASK (OOK)")
plt.xlabel("In-phase (I)")
plt.ylabel("Quadrature (Q)")
plt.grid(True, linestyle='--', alpha=0.5)
plt.xlim(-1, 2)
plt.ylim(-1, 1)

# BPSK Constellation Diagram
plt.subplot(1, 3, 2)
# Define BPSK points (along the I axis, mirrored)
bpsk_points = [(-1, 0), (1, 0)]
for point, label in zip(bpsk_points, ['0', '1']):
    plt.scatter(point[0], point[1], color='magenta', s=100)
    plt.text(point[0] + 0.1, point[1], label, fontsize=12)
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.title("b. BPSK")
plt.xlabel("In-phase (I)")
plt.ylabel("Quadrature (Q)")
plt.grid(True, linestyle='--', alpha=0.5)
plt.xlim(-2, 2)
plt.ylim(-1, 1)

# QPSK Constellation Diagram
plt.subplot(1, 3, 3)
# Define QPSK points (on a circle with 90-degree separation)
qpsk_points = [
    (np.sqrt(2)/2, np.sqrt(2)/2),
    (-np.sqrt(2)/2, np.sqrt(2)/2),
    (-np.sqrt(2)/2, -np.sqrt(2)/2),
    (np.sqrt(2)/2, -np.sqrt(2)/2)
]
labels = ['00', '01', '11', '10']
for point, label in zip(qpsk_points, labels):
    plt.scatter(point[0], point[1], color='magenta', s=100)
    plt.text(point[0] + 0.1, point[1], label, fontsize=12)
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.title("c. QPSK")
plt.xlabel("In-phase (I)")
plt.ylabel("Quadrature (Q)")
plt.grid(True, linestyle='--', alpha=0.5)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

# Show the complete plot
plt.tight_layout()
plt.show()
