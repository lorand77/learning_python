import time
from divisors import get_divisors
from primefac import primefac
from sympy.ntheory import factorint

# https://stackoverflow.com/questions/15347174/python-finding-prime-factors
def prime_factors_SO(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n = n // i
        else:
            i += 1
    if n > 1:
        factors.append(n)
    return factors


def main():

    # N = 100
    # for n in range(2, N + 1):
    #     print(f"n={n} prime_factors_SO={prime_factors_SO(n)}")
    #     print(f"n={n} prime_factors_my={prime_factors(n)}")
    #     print(f"n={n} prime_factors_p1={list(primefac(n))}")
    #     print(f"n={n} prime_factors_p2={factorint(n, multiple=True)}")


    N = 10_000_000

    start = time.perf_counter()
    for n in range(2, N + 1):
        prime_factors(n)
    end = time.perf_counter()
    print(f"Prime factorization time:{end - start}")

    # start = time.perf_counter()
    # for n in range(2, N + 1):
    #     get_divisors(n)
    # end = time.perf_counter()
    # print(f"Get all divisors time:{end - start}")

    start = time.perf_counter()
    for n in range(2, N + 1):
        list(primefac(n))
    end = time.perf_counter()
    print(f"Prime factorization (pypi pckg primefac) time:{end - start}")    

    start = time.perf_counter()
    for n in range(2, N + 1):
        list(factorint(n, multiple=True))
    end = time.perf_counter()
    print(f"Prime factorization (pypi pckg sympy) time:{end - start}")    

 
main()

