word = "PKA_NSCOM03"

ascii_values = [ord(char) for char in word]

total_sum = sum(ascii_values)

wrapped_sum = total_sum % 256

checksum = (256 - wrapped_sum) % 256

print(f"Word: {word}")
print(f"ASCII values: {ascii_values}")
print(f"Sum of ASCII values: {total_sum}")
print(f"Wrapped sum: {wrapped_sum}")
print(f"Checksum: {checksum}")
