from sympy import symbols, div

x = symbols('x')

P = x**5 + x**4 + x**2 + 1  
M = int('101001101000000', 2) 

M_poly = sum(int(bit) * x**i for i, bit in enumerate(reversed(bin(M)[2:])))

quotient, remainder = div(M_poly, P, x)

def polynomial_to_binary(poly):
    binary_list = []
    for i in range(poly.as_poly().degree() + 1):
        coeff = poly.coeff(x, i)  
        binary_list.append('1' if coeff % 2 != 0 else '0')
    return ''.join(reversed(binary_list)).lstrip('0')

remainder_binary = polynomial_to_binary(remainder)
remainder_binary
