import matplotlib.pyplot as plt
import matplotlib.patches as patches

def nav_visualization():
    fig, ax = plt.subplots(figsize=(10, 5))

    # Define the stations and their timeline positions
    station_positions = {
        "Station A (Source)": 4,
        "Station B (Destination)": 3,
        "Station C (Other Station)": 2
    }

    # Plot each station's timeline
    for station, y in station_positions.items():
        ax.plot([0, 10], [y, y], color="black", linewidth=0.5)
        ax.text(0, y + 0.1, station, verticalalignment='bottom', fontsize=10)

    # Define the RTS, CTS, Data, and ACK packets between Station A and Station B
    ax.annotate("RTS", xy=(1, 4), xytext=(2, 3), arrowprops=dict(arrowstyle="->", color="blue", lw=2))
    ax.annotate("CTS", xy=(3, 3), xytext=(4, 4), arrowprops=dict(arrowstyle="->", color="green", lw=2))
    ax.annotate("Data", xy=(4.5, 4), xytext=(6.5, 3), arrowprops=dict(arrowstyle="->", color="purple", lw=2))
    ax.annotate("ACK", xy=(7, 3), xytext=(8, 4), arrowprops=dict(arrowstyle="->", color="orange", lw=2))

    # NAV indication for Station C
    nav_rect = patches.Rectangle((1, 1.8), 7, 0.4, linewidth=1, edgecolor='red', facecolor='red', alpha=0.3)
    ax.add_patch(nav_rect)
    ax.text(4.5, 2, "NAV Timer (Station C)", color="red", fontsize=10, ha="center")

    # Set plot limits and labels
    ax.set_ylim(1, 5)
    ax.set_xlim(0, 10)
    ax.set_xlabel("Time")
    ax.set_yticks([])
    plt.title("Network Allocation Vector (NAV) Visualization in CSMA/CA")
    plt.show()

nav_visualization()
