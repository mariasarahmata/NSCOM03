import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Configuration for the FDMA channels
stations = {
    1: {"color": "cyan", "frequency": 1, "label": "Station 1"},
    2: {"color": "yellow", "frequency": 2, "label": "Station 2"},
    3: {"color": "green", "frequency": 3, "label": "Station 3 (Silent)"},
    4: {"color": "pink", "frequency": 4, "label": "Station 4"}
}

# Create a figure for the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Define the width and height for the time-frequency slots
slot_width = 1.5
slot_height = 0.8

# Plot individual stations with time-frequency boxes over multiple time slots
for i, (station, config) in enumerate(stations.items()):
    y_position = 5 - i  # Assign each station a unique y position for its frequency band
    
    # If the station is silent, label it without a colored box
    if station == 3:  # Silent station
        ax.text(-1, y_position, config["label"], ha="right", va="center", fontsize=12, color="magenta")
        continue
    
    # Plot multiple time slots for each station
    for t in range(4):  # Show multiple time intervals
        rect = patches.Rectangle((t * slot_width, y_position - slot_height / 2),
                                 slot_width, slot_height, linewidth=1,
                                 edgecolor='black', facecolor=config["color"])
        ax.add_patch(rect)
    
    # Label each station's frequency band
    ax.text(-1, y_position, config["label"], ha="right", va="center", fontsize=12)

# Label the common channel at the top to represent the aggregated data
ax.text(2.5, 6, "Common Channel", ha="center", va="center", fontsize=14, fontweight="bold")
ax.plot([0, slot_width * 4], [5.5, 5.5], color="black", linewidth=1.5)  # Common channel line

# Configure the plot appearance
ax.set_xlim(-2, slot_width * 4)
ax.set_ylim(0, 6.5)
ax.set_xlabel("Time")
ax.set_ylabel("Frequency Bands")
ax.axis('off')  # Turn off axes for a cleaner look

plt.tight_layout()
plt.show()
