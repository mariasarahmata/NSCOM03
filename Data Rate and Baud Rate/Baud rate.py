def calculate_baud_rate(data_rate, case_factor, ratio):
    baud_rate = case_factor * data_rate * (1 / ratio)
    return baud_rate

data_rate = 100000  
case_factor = 0.5 
ratio = 1 

baud_rate = calculate_baud_rate(data_rate, case_factor, ratio)
print(f"The baud rate is: {baud_rate:.2f} kbaud")
