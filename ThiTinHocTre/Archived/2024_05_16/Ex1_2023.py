import math
from collections import Counter

def prime_factors(n):
    """Returns the prime factorization of n as a dictionary {prime: exponent}."""
    i = 2
    factors = Counter()
    while i * i <= n:
        while (n % i) == 0:
            factors[i] += 1
            n //= i
        i += 1
    if n > 1:
        factors[n] += 1
    return factors

def count_p_in_factorial(m, p):
    """Returns the number of times prime p appears in m!"""
    count = 0
    power = p
    while power <= m:
        count += m // power
        power *= p
    return count

def max_k(m, n):
    n_factors = prime_factors(n)
    min_k = float('inf')
    
    for p, e in n_factors.items():
        count_p = count_p_in_factorial(m, p)
        k = count_p // e
        if k < min_k:
            min_k = k
            
    return min_k

# # Example usage:
# m = 10
# n = 12
# print(max_k(m, n))  # Output the largest k

# Input values
m = int(input("Enter value for m: "))
n = int(input("Enter value for n: "))

# Compute and print the result
result = max_k(m, n)
print(f"The largest k such that {m}! % {n}^k == 0 is: {result}")
