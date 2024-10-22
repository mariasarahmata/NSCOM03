import matplotlib.pyplot as plt

def add_parity_bit(data, even_parity=True):
    """
    Adds a parity bit to the binary data.
    """
    count_ones = data.count('1')
    parity_bit = '0' if (count_ones % 2 == 0) else '1'
    if not even_parity:
        parity_bit = '1' if parity_bit == '0' else '0'
    return data + parity_bit

# Example data
data = "1101011"
data_with_parity = add_parity_bit(data)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Draw the process flow as a series of text boxes and arrows
ax.text(0.1, 0.8, f"Original Data: {data}", fontsize=12, bbox=dict(facecolor='lightblue', alpha=0.5))
ax.annotate('', xy=(0.3, 0.75), xytext=(0.1, 0.75), arrowprops=dict(arrowstyle='->', lw=2))

ax.text(0.3, 0.6, f"Calculate Parity Bit\n(Count 1s: {data.count('1')}, Parity: {data_with_parity[-1]})",
        fontsize=12, bbox=dict(facecolor='lightgreen', alpha=0.5), ha='center')
ax.annotate('', xy=(0.5, 0.55), xytext=(0.3, 0.55), arrowprops=dict(arrowstyle='->', lw=2))

ax.text(0.5, 0.4, f"Data with Parity Bit: {data_with_parity}",
        fontsize=12, bbox=dict(facecolor='lightblue', alpha=0.5), ha='center')
ax.annotate('', xy=(0.7, 0.35), xytext=(0.5, 0.35), arrowprops=dict(arrowstyle='->', lw=2))

ax.text(0.7, 0.2, "Transmission\n(Data Sent)", fontsize=12, bbox=dict(facecolor='lightyellow', alpha=0.5), ha='center')
ax.annotate('', xy=(0.9, 0.15), xytext=(0.7, 0.15), arrowprops=dict(arrowstyle='->', lw=2))

ax.text(0.9, 0.0, f"Received Data: {data_with_parity}\nCheck Parity", fontsize=12, bbox=dict(facecolor='lightcoral', alpha=0.5), ha='center')

# Set axis limits and remove axes for a clean look
ax.set_xlim(0, 1)
ax.set_ylim(-0.2, 1)
ax.axis('off')

# Show the plot
plt.title("Single Parity-Check Process")
plt.show()
