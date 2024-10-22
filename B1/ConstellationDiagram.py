import numpy as np
import matplotlib.pyplot as plt

# Define a single QPSK point (representing a symbol)
i_value = 1
q_value = 1

# Define amplitude and phase for the vector
amplitude = np.sqrt(i_value**2 + q_value**2)
phase_angle = np.arctan2(q_value, i_value)  # Angle in radians

# Create a figure
plt.figure(figsize=(6, 6))
plt.plot([0, i_value], [0, q_value], 'k--', label='Amplitude')
plt.scatter(i_value, q_value, color='magenta', s=100)  # QPSK point

# Draw lines for I and Q components
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.plot([0, i_value], [q_value, q_value], 'k:', lw=1)
plt.plot([i_value, i_value], [0, q_value], 'k:', lw=1)

# Annotate the vector and axes
plt.text(i_value + 0.1, q_value + 0.1, f'({i_value}, {q_value})', fontsize=12)
plt.text(i_value / 2, q_value / 2, 'Length: amplitude', fontsize=10, rotation=45, ha='center')
plt.text(i_value + 0.1, 0, 'Amplitude of I component', fontsize=10)
plt.text(0, q_value + 0.1, 'Amplitude of Q component', fontsize=10)
plt.text(i_value / 2, -0.2, 'X (In-phase carrier)', fontsize=12, ha='center')
plt.text(-0.2, q_value / 2, 'Y (Quadrature carrier)', fontsize=12, va='center')

# Label the angle for phase
plt.text(i_value / 3, q_value / 3, 'Angle: phase', fontsize=10, rotation=45)

# Set plot limits and titles
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Concept of Constellation Diagram")
plt.xlabel("X (In-phase carrier)")
plt.ylabel("Y (Quadrature carrier)")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
