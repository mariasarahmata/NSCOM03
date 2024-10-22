import numpy as np
import matplotlib.pyplot as plt

# Create a figure for the constellation diagrams
plt.figure(figsize=(14, 4))

# Define axis limits for uniform intervals
axis_limits = (-1.5, 1.5)

# Subplot for 4-QAM (a) with points only in the first quadrant
plt.subplot(1, 4, 1)
qam_points_a = [(0.5, 0.5), (1, 0.5), (0.5, 1), (1, 1)]
for point in qam_points_a:
    plt.scatter(point[0], point[1], color='magenta', s=100)
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.title("a. 4-QAM")
plt.grid(True, linestyle='--', alpha=0.5)
plt.xlim(*axis_limits)
plt.ylim(*axis_limits)
plt.gca().set_aspect('equal', adjustable='box')

# Subplot for 4-QAM (b) with one point in each quadrant
plt.subplot(1, 4, 2)
qam_points_b = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
for point in qam_points_b:
    plt.scatter(point[0], point[1], color='magenta', s=100)
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.title("b. 4-QAM")
plt.grid(True, linestyle='--', alpha=0.5)
plt.xlim(*axis_limits)
plt.ylim(*axis_limits)
plt.gca().set_aspect('equal', adjustable='box')

# Subplot for 4-QAM (c) with smaller points in the first quadrant
plt.subplot(1, 4, 3)
qam_points_c = [(0.25, 0.25), (0.5, 0.25), (0.25, 0.5), (0.5, 0.5)]
for point in qam_points_c:
    plt.scatter(point[0], point[1], color='magenta', s=100)
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.title("c. 4-QAM")
plt.grid(True, linestyle='--', alpha=0.5)
plt.xlim(*axis_limits)
plt.ylim(*axis_limits)
plt.gca().set_aspect('equal', adjustable='box')

# Subplot for 16-QAM (d) with points in all quadrants
plt.subplot(1, 4, 4)
qam_points_d = [
    (1, 1), (1.2, 1), (1, 1.2), (1.2, 1.2),
    (-1, 1), (-1.2, 1), (-1, 1.2), (-1.2, 1.2),
    (-1, -1), (-1.2, -1), (-1, -1.2), (-1.2, -1.2),
    (1, -1), (1.2, -1), (1, -1.2), (1.2, -1.2)
]

axis_limits = (-1.5, 1.5)

for point in qam_points_d:
    plt.scatter(point[0], point[1], color='magenta', s=100)
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.title("d. 16-QAM")
plt.grid(True, linestyle='--', alpha=0.5)
plt.xlim(*axis_limits)
plt.ylim(*axis_limits)
plt.gca().set_aspect('equal', adjustable='box')

# Show the complete plot
plt.tight_layout()
plt.show()
