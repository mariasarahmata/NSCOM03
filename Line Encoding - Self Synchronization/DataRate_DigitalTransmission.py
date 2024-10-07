def calculate_extra_bits_with_details(data_rate, clock_difference_percentage):
    """
    Calculate the number of extra bits received per second with detailed output and formatted decimal places.
    
    Parameters:
    - data_rate (float): The data rate in bits per second.
    - clock_difference_percentage (float): The percentage by which the receiver clock is faster.
    
    Returns:
    - dict: A dictionary with the bits sent, bits received, and extra bits per second, all formatted with two decimal places.
    """
    # Calculate extra bits based on the clock difference
    extra_bits = data_rate * (clock_difference_percentage / 100)
    bits_received = data_rate + extra_bits
    
    # Format the output with two decimal places
    return {
        'Bits Sent': f"{data_rate:.2f}",
        'Bits Received': f"{bits_received:.2f}",
        'Extra Bits per Second': f"{extra_bits:.2f}"
    }

# Example calculation for 1 kbps
details_1kbps = calculate_extra_bits_with_details(1000, 0.1)
print(f"At 1 kbps: Bits Sent: {details_1kbps['Bits Sent']} bps, Bits Received: {details_1kbps['Bits Received']} bps, Extra Bits: {details_1kbps['Extra Bits per Second']} bps")

# Example calculation for 1 Mbps
details_1mbps = calculate_extra_bits_with_details(1000000, 0.1)
print(f"At 1 Mbps: Bits Sent: {details_1mbps['Bits Sent']} bps, Bits Received: {details_1mbps['Bits Received']} bps, Extra Bits: {details_1mbps['Extra Bits per Second']} bps")
