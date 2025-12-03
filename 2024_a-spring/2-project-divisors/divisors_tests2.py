from divisors import get_divisors, get_number_of_divisors_using_prime_factors
import time

for n in [2,6,100,101,4675,9767,54689,400,5978,72,123456789]:
    print(f"n={n} n.div1={len(get_divisors(n))} n.div2={get_number_of_divisors_using_prime_factors(n)}")
    if len(get_divisors(n)) != get_number_of_divisors_using_prime_factors(n):
        print("Fuuuuuck!!!!")

