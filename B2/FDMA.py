import matplotlib.pyplot as plt
import matplotlib.patches as patches

def fdma_visualization():
    fig, ax = plt.subplots(figsize=(12, 8))

    # Define the main common channel
    ax.add_patch(patches.Rectangle((2, 2), 6, 3, edgecolor="black", facecolor="lightgrey", lw=2))
    ax.text(5, 3.5, "Common Channel", fontsize=14, ha="center", va="center", fontweight="bold", color="black")

    # Define vibrant colors and labels for each user
    user_colors = ['dodgerblue', 'gold', 'limegreen', 'orangered']
    users = ["User 1", "User 2", "User 3", "User 4"]

    # Draw each user's frequency band inside the common channel
    for i, (color, user) in enumerate(zip(user_colors, users)):
        # Draw frequency band in common channel
        y_position = 2.5 + i * 0.6
        ax.add_patch(patches.Rectangle((2, y_position), 6, 0.5, edgecolor="black", facecolor=color, lw=1.5))
        ax.text(8.2, y_position + 0.25, f"f{i+1}", ha="center", va="center", fontsize=10, color="black")

        # Draw each user's data block on the left side
        ax.add_patch(patches.Rectangle((0.5, y_position), 1, 0.5, edgecolor="black", facecolor=color, lw=1.5))
        ax.text(1, y_position + 0.25, "Data", ha="center", va="center", fontsize=10, color="black")
        ax.text(0.3, y_position + 0.25, user, ha="right", va="center", fontsize=12, fontweight="bold", color=color)

    # Add annotations and labels
    ax.set_xlim(0, 10)
    ax.set_ylim(2, 6)
    ax.axis('off')  # Hide the axes for a cleaner look
    plt.title("Frequency Division Multiple Access (FDMA)", fontsize=16, fontweight="bold", color="black")

    plt.show()

fdma_visualization()
