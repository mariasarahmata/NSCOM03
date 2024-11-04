import matplotlib.pyplot as plt

transmissions = {
    1: [(1, "1.1"), (3, "1.2")],
    2: [(2, "2.1"), (4, "2.2")],
    3: [(2, "3.1"), (6, "3.2")],
    4: [(3, "4.1"), (5, "4.2")]
}

num_slots = 6
num_stations = 4

fig, ax = plt.subplots(figsize=(12, 6))

colors = ['yellow', 'blue', 'green', 'purple']
station_labels = [f'Station {i}' for i in range(1, num_stations + 1)]

# Plot each transmission
for station, frames in transmissions.items():
    for slot, frame_id in frames:
        ax.barh(station, 0.8, left=slot - 0.5, color=colors[station - 1], align='center',
                edgecolor='black', label=f'{frame_id} (Station {station})')
        ax.hlines(y=station, xmin=0.5, xmax=num_slots + 0.5, colors='black', linestyles='dashed', lw=1)

# Draw slot boundaries and highlight collision areas
for slot in range(1, num_slots + 1):
    ax.axvline(x=slot, color='black', linestyle='-', linewidth=1)  
    if slot in {2, 3}:
        ax.axvspan(slot - 0.5, slot, color='red', alpha=0.3, label='Collision duration' if slot == 2 else "")

# Configure the plot aesthetics
ax.set_xlabel('Slots')
ax.set_ylabel('Stations')
ax.set_yticks(range(1, num_stations + 1))
ax.set_yticklabels(station_labels)
ax.set_xticks(range(1, num_slots + 1))
ax.set_xticklabels(range(1, num_slots + 1))
ax.set_xlim(0.5, num_slots + 0.5)
ax.set_title('Frames in Slotted ALOHA Network')

# Legend handling to show unique labels
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))  
ax.legend(by_label.values(), by_label.keys(), title='Frame IDs and Collisions', bbox_to_anchor=(1.05, 1), loc='upper left')

ax.grid(True)

plt.tight_layout()
plt.show()
