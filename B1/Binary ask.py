import numpy as np
import matplotlib.pyplot as plt

def plot_modulated_signal(bit_rate, baud_rate, duration=1):
    samples_per_bit = 100  
    total_samples = bit_rate * samples_per_bit
    t = np.linspace(0, duration, total_samples, endpoint=False)
    
    bits = np.array([1, 0, 1, 1, 0])
    signal = np.repeat(bits, samples_per_bit)

    sine_wave = np.sin(2 * np.pi * baud_rate * t) * signal  
    
    plt.figure(figsize=(14, 4))
    line, = plt.plot(t, sine_wave, label='Modulated Sine Wave')

    for i in range(len(bits)):
        plt.axvline(x=i * 0.2, color='gray', linestyle='--', linewidth=1)
        plt.text(i * 0.2 + 0.1, 1.3, str(bits[i]), horizontalalignment='center', verticalalignment='center', fontsize=12, color='red')

    plt.axvline(x=1.0, color='gray', linestyle='--', linewidth=1)
    
    params_text = f'Bit Rate: {bit_rate} bps\nBaud Rate: {baud_rate} bauds\nAmplitude: ±1\nTime: {duration} s'
    plt.text(1.02, 0.5, params_text, fontsize=10, verticalalignment='center', bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='white'))

    plt.title('Sine Wave Modulated by Digital Signal')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    plt.ylim(-1.5, 1.5)
    plt.xlim(0, duration)  
    plt.grid(True)

    plt.legend(handles=[line], loc='upper right', bbox_to_anchor=(1.12, 1.15))

    plt.show()

bit_rate = 5  
baud_rate = 5 
duration = 1  

plot_modulated_signal(bit_rate, baud_rate, duration)



