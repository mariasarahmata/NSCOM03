import numpy as np
import matplotlib.pyplot as plt

# Data bits for AMI
data_bits_ami = [1, 0, 1, 1, 0, 0, 1, 1, 0, 1]

# AMI signal: 0 is 0V, 1 alternates between +1 and -1
signal_ami = []
current_level = 1  # Start with positive level for 1

for bit in data_bits_ami:
    if bit == 1:
        signal_ami.append(current_level)
        current_level = -current_level  # Alternate between +1 and -1 for consecutive 1s
    else:
        signal_ami.append(0)  # Zero voltage for 0s

# Time vector for the signal
time_vector_ami = np.linspace(0, len(data_bits_ami), num=len(data_bits_ami) * 100, endpoint=True)

# Plotting AMI signal
plt.figure(figsize=(8, 5))
plt.step(time_vector_ami, np.repeat(signal_ami, 100), where='post', linewidth=2, color='#C71585')  
plt.title('Bipolar AMI Encoding')
plt.xlabel('Time')
plt.ylabel('Signal Level')
plt.grid(True)
plt.axhline(0, color='#A9A9A9', linewidth=1.5)  
plt.ylim(-1.5, 1.5)

# Data element boundaries
for i in range(len(data_bits_ami) + 1):
    plt.axvline(x=i, color='#D3D3D3', linestyle='--') 

plt.show()
