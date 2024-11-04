import matplotlib.pyplot as plt
import matplotlib.patches as patches

def improved_fdma_fdm_diagram():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

    # FDMA Visualization (Separate Frequencies for Each User)
    ax1.add_patch(patches.Rectangle((1, 1.5), 6, 4, edgecolor="black", facecolor="lightgrey", lw=2))
    ax1.text(4, 6, "FDMA - Frequency Division Multiple Access", ha="center", va="center", fontsize=16, fontweight="bold")

    # Draw frequency bands for each user in FDMA
    fdma_colors = ['dodgerblue', 'gold', 'limegreen', 'orangered']
    fdma_labels = ["User 1 - f1", "User 2 - f2", "User 3 - f3", "User 4 - f4"]

    for i, (color, label) in enumerate(zip(fdma_colors, fdma_labels)):
        y_position = 2 + i * 0.9
        ax1.add_patch(patches.Rectangle((1, y_position), 6, 0.7, edgecolor="black", facecolor=color, lw=1.5))
        ax1.text(7.2, y_position + 0.35, label, ha="left", va="center", fontsize=12, color=color, fontweight="bold")

    # Label for FDMA access method
    ax1.text(4, 1, "Separate Frequencies for Each User", ha="center", va="center", fontsize=14, color="black", fontstyle="italic")

    # FDM Visualization (Combined Signals on a Single Channel)
    ax2.add_patch(patches.Rectangle((1, 1.5), 6, 4, edgecolor="black", facecolor="lightgrey", lw=2))
    ax2.text(4, 6, "FDM - Frequency Division Multiplexing", ha="center", va="center", fontsize=16, fontweight="bold")

    # Draw combined frequency bands for each signal in FDM
    fdm_colors = ['dodgerblue', 'gold', 'limegreen', 'orangered']
    fdm_labels = ["Signal 1 - f1", "Signal 2 - f2", "Signal 3 - f3", "Signal 4 - f4"]

    for i, (color, label) in enumerate(zip(fdm_colors, fdm_labels)):
        y_position = 5 - i * 0.9
        ax2.add_patch(patches.Rectangle((1, y_position), 6, 0.7, edgecolor="black", facecolor=color, lw=1.5))
        ax2.text(7.2, y_position + 0.35, label, ha="left", va="center", fontsize=12, color=color, fontweight="bold")

    # Label for FDM multiplexing method
    ax2.text(4, 1, "Combined Signals on a Single Channel", ha="center", va="center", fontsize=14, color="black", fontstyle="italic")

    # Adjust plot limits and remove axis lines for both subplots
    for ax in [ax1, ax2]:
        ax.set_xlim(0, 9)
        ax.set_ylim(0.5, 7)
        ax.axis('off')

    # Main title for the visualization
    plt.suptitle("Difference Between FDMA and FDM", fontsize=20, fontweight="bold")
    plt.subplots_adjust(bottom=0.2)  # Add more padding at the bottom
    plt.show()

improved_fdma_fdm_diagram()
