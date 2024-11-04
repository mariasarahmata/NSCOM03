import matplotlib.pyplot as plt
import random

# Configuration
num_stations = 4
total_time = 100
frame_duration = 10  # Duration each frame occupies on the timeline
collision_duration = 10  # Duration in which frames can collide

# Predefined frames with start times for each station (for visualization purposes)
transmissions = {
    1: [(5, "1.1"), (30, "1.2")],    # Station 1
    2: [(15, "2.1"), (40, "2.2")],   # Station 2
    3: [(20, "3.1"), (70, "3.2")],   # Station 3
    4: [(25, "4.1"), (75, "4.2")]    # Station 4
}

# Function to detect collisions
def detect_collisions(transmissions):
    collisions = []
    for station, frames in transmissions.items():
        for start_time, frame_id in frames:
            end_time = start_time + frame_duration
            # Check if any other station has overlapping frames
            for other_station, other_frames in transmissions.items():
                if other_station != station:
                    for other_start, other_frame_id in other_frames:
                        other_end = other_start + frame_duration
                        if (start_time < other_end) and (other_start < end_time):
                            collisions.append((start_time, end_time))
                            break
    return collisions

# Detect collisions based on transmissions
collisions = detect_collisions(transmissions)

# Plotting
fig, ax = plt.subplots(figsize=(12, 6))

# Colors for each station for clarity
colors = ['yellow', 'blue', 'green', 'pink']
station_labels = [f'Station {i}' for i in range(1, num_stations + 1)]

# Plot each station's transmissions and dashed time lines
for station, frames in transmissions.items():
    # Dashed line across the entire timeline for each station
    ax.hlines(y=station, xmin=0, xmax=total_time, colors='black', linestyles='dashed', lw=0.5)
    for start_time, frame_id in frames:
        # Plot the transmission block for each frame
        ax.barh(station, frame_duration, left=start_time, height=0.4, color=colors[station - 1], align='center',
                edgecolor='black', label=f'Frame {frame_id}' if start_time == frames[0][0] else "")
        ax.text(start_time + frame_duration / 2, station, frame_id, ha='center', va='center', color='black')

# Highlight collision periods
for start, end in collisions:
    ax.axvspan(start, end, color='grey', alpha=0.3, label="Collision Duration" if start == collisions[0][0] else "")

# Draw solid vertical lines to represent time intervals
for time in range(0, total_time + 1, 10):
    ax.axvline(x=time, color='black', linestyle='-', linewidth=0.5)

# Configure the plot
ax.set_xlabel('Time')
ax.set_ylabel('Stations')
ax.set_yticks(range(1, num_stations + 1))
ax.set_yticklabels(station_labels)
ax.set_xticks(range(0, total_time + 1, 10))
ax.set_xlim(0, total_time)

# Remove duplicate labels in legend
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys(), title='Frames and Collision Periods', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show plot
plt.tight_layout()
plt.show()
