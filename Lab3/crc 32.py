from sympy import symbols, div

x = symbols('x')

P_crc32 = x**32 + x**26 + x**23 + x**22 + x**16 + x**12 + x**11 + x**10 + x**8 + x**7 + x**5 + x**4 + x**2 + x + 1

extended_message = int('1010011010' + '0' * 32, 2)

M_crc32_poly = sum(int(bit) * x**i for i, bit in enumerate(reversed(bin(extended_message)[2:])))

quotient_crc32, remainder_crc32 = div(M_crc32_poly, P_crc32, x)

def polynomial_to_binary(poly):
    binary_list = []
    for i in range(poly.as_poly().degree() + 1):
        coeff = poly.coeff(x, i)  
        binary_list.append('1' if coeff % 2 != 0 else '0')
    return ''.join(reversed(binary_list)).lstrip('0')

remainder_crc32_binary = polynomial_to_binary(remainder_crc32)

print("Result: " + remainder_crc32_binary)
