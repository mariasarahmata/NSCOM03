import numpy as np
import matplotlib.pyplot as plt

def generate_signals(bit_pattern, samples_per_bit, baud_rate):
 
    t = np.linspace(0, len(bit_pattern) / baud_rate, len(bit_pattern) * samples_per_bit, endpoint=False)
    
    digital_signal = np.repeat(bit_pattern, samples_per_bit)
    
    carrier_wave = np.sin(2 * np.pi * baud_rate * t)
    
    modulated_wave = carrier_wave * digital_signal

    return t, digital_signal, carrier_wave, modulated_wave

def plot_signals(t, digital_signal, carrier_wave, modulated_wave, bit_pattern, baud_rate):
    fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)  

    axs[0].step(t, digital_signal, 'r', where='post', linewidth=2)
    axs[0].set_ylabel('Amplitude')
    axs[0].set_title('Digital Signal')

    axs[1].plot(t, carrier_wave, 'k')
    axs[1].set_ylabel('Amplitude')
    axs[1].set_title('Carrier Signal')

    axs[2].plot(t, modulated_wave, 'b')
    axs[2].set_xlabel('Time (s)')
    axs[2].set_ylabel('Amplitude')
    axs[2].set_title('Modulated Signal')

    for ax in axs:
        ax.grid(True)
        ax.set_xlim(t[0], t[-1]) 

        for i in range(len(bit_pattern)):
            ax.axvline(x=i / baud_rate, color='gray', linestyle='--', linewidth=1)
            if ax == axs[0]:  
                ax.text(i / baud_rate + 0.5 / baud_rate, 1.2, str(bit_pattern[i]),
                        horizontalalignment='center', fontsize=12, color='blue')

    plt.tight_layout()
    plt.show()

bit_pattern = np.array([1, 0, 1, 1, 0]) 
samples_per_bit = 100 
baud_rate = 5 

t, digital_signal, carrier_wave, modulated_wave = generate_signals(bit_pattern, samples_per_bit, baud_rate)

plot_signals(t, digital_signal, carrier_wave, modulated_wave, bit_pattern, baud_rate)


