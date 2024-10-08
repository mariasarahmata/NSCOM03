import math

def digitize_voice(max_freq, sampling_rate, duration=1):
    
    num_samples = int(sampling_rate * duration)
    
    sampled_signal = []
    for n in range(num_samples):
        t = n / sampling_rate
        sample = math.sin(2 * math.pi * max_freq * t)
        sampled_signal.append(sample)
    
    return sampled_signal

max_frequency = 4000  
sampling_rate = 8000  

sampled_signal = digitize_voice(max_frequency, sampling_rate)

print("Sampled Signal Values:.", sampled_signal[:10])
