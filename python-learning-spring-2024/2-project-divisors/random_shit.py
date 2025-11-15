import sympy
from sympy.ntheory import factorint

x = [2,3,4,5]

def my_sum(x):
    s = 0
    for v in x:
        s = s + v
    return s

print(my_sum(x))
print(sum(x))


def my_product(x):
    s = 1
    for v in x:
        s = s * v
    return s

print(my_product(x))


print(my_sum([]))
print(my_product([]))


print(factorint(24))
print(factorint(2))
print(factorint(1))

def get_number_of_divisors_from_prime_factors(n):
    prime_factors = factorint(n)
    number_of_divisors = 1
    for k in prime_factors:
        number_of_divisors = number_of_divisors * prime_factors[k] + 1
    return number_of_divisors

print(get_number_of_divisors_from_prime_factors(24))
print(get_number_of_divisors_from_prime_factors(32))
print(get_number_of_divisors_from_prime_factors(101))
print(get_number_of_divisors_from_prime_factors(1))
print(get_number_of_divisors_from_prime_factors(0))