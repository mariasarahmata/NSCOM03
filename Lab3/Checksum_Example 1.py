def ones_complement_sum(data):
    total_sum = sum(data)
    
    high_nibble = (total_sum >> 4) & 0xF  
    low_nibble = total_sum & 0xF 
    wrapped_sum = high_nibble + low_nibble
    
    checksum = (15 - wrapped_sum) % 16
    
    return checksum, wrapped_sum, total_sum

def send_packet(data, checksum):
    return data + [checksum]

def verify_checksum(packet):
    total_sum = sum(packet)

    high_nibble = (total_sum >> 4) & 0xF  
    low_nibble = total_sum & 0xF  
    wrapped_sum = high_nibble + low_nibble
 
    final_checksum = (15 - wrapped_sum) % 16
    
    return final_checksum == 0, wrapped_sum, total_sum, final_checksum

data = [7, 11, 12, 0, 6]
checksum, sender_wrapped_sum, sender_total_sum = ones_complement_sum(data)
packet = send_packet(data, checksum)

verification_result, receiver_wrapped_sum, receiver_total_sum, receiver_final_checksum = verify_checksum(packet)

print(f"Sender Side:\nData = {data}\nSum = {sender_total_sum}\nWrapped Sum = {sender_wrapped_sum}\nChecksum = {checksum}\n")
print(f"Packet Sent: {packet}\n")
print(f"Receiver Side:\nSum = {receiver_total_sum}\nWrapped Sum = {receiver_wrapped_sum}\nFinal Checksum = {receiver_final_checksum}\n")
