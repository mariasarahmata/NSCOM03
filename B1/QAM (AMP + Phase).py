import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.table as table

def plot_detailed_qam_constellation():
    fig, ax = plt.subplots(figsize=(8, 6))
    x = np.array([-3, -1, 1, 3])
    xx, yy = np.meshgrid(x, x)
    points = xx.flatten() + 1j * yy.flatten()

    points /= np.sqrt(np.mean(np.abs(points)**2))

    labels = [
        '1111', '1001', '0101', '0111',
        '1101', '1100', '0100', '0110',
        '1010', '1000', '0000', '0001',
        '1011', '1001', '0010', '0011'
    ]

    ax.scatter(points.real, points.imag, color='turquoise', edgecolors='black', s=100, zorder=3)

    for point, label in zip(points, labels):
        ax.text(point.real, point.imag + 0.1, label, fontsize=9, ha='center', color='black', zorder=5)

    center_point = 0+0j
    ax.scatter([center_point.real], [center_point.imag], color='red', s=200, zorder=4)
    ax.text(center_point.real, center_point.imag, '0000', fontsize=9, ha='center', color='white', zorder=5)
    
    circle_radius = np.abs(points[0]) * 0.5  
    phase_arc = patches.Arc((0, 0), 2 * circle_radius, 2 * circle_radius, angle=0, theta1=0, theta2=225, color='red', linestyle='-', linewidth=2)
    ax.add_patch(phase_arc)

    phase_line = np.exp(1j * np.deg2rad(225)) * circle_radius  
    ax.plot([0, phase_line.real], [0, phase_line.imag], color='red', linestyle='-', linewidth=2, zorder=5)

    ax.axhline(0, color='black', lw=0.5, zorder=1)
    ax.axvline(0, color='black', lw=0.5, zorder=1)
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])

    col_labels = ["Amp", "Phase", "Data"]
    table_data = [["25%", "225°", "1100"]]
    table_ax = fig.add_axes([0.45, 0.2, 0.1, 0.05])  
    table_ax.axis('off')
    data_table = table.table(ax=table_ax, cellText=table_data, colLabels=col_labels, loc='center', cellLoc='center', edges='horizontal')
    data_table.auto_set_font_size(False)
    data_table.set_fontsize(9)
    data_table.scale(1.2, 1.2)  
    plt.show()
plot_detailed_qam_constellation()


