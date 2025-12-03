import math
from sympy.ntheory import factorint

def get_divisors(n):
    """Returns a list of all divisors of n."""
    divisors = []
    for v in range(1, int(math.sqrt(n)) + 1):
        if n % v == 0:
            divisors.append(v)
            if v != n // v:
                divisors.append(n // v)
    return sorted(divisors)

def get_number_of_divisors_using_prime_factors(n):
    """Returns the number of divisors of n (using prime factorization for speed)."""
    prime_factors = factorint(n)
    number_of_divisors = 1
    for k in prime_factors:
        number_of_divisors = number_of_divisors * (prime_factors[k] + 1)
    return number_of_divisors
