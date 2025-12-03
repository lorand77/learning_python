import matplotlib.pyplot as plt
from divisors import get_divisors, get_number_of_divisors_using_prime_factors
import time
from collections import Counter


def get_number_of_divisors_for_1toN(N):
    numbers = list(range(1, N+1))
    number_of_divisors = []
    for i in numbers:
        number_of_divisors.append(get_number_of_divisors_using_prime_factors(i))
    return number_of_divisors


def main():
    N = 100000
    print(f"N={N}")

    start = time.perf_counter()
    number_of_divisors = get_number_of_divisors_for_1toN(N)
    end = time.perf_counter()
    print(f"Time:{end - start}")

    #plt.bar(numbers, number_of_divisors)
    #plt.hist(number_of_divisors, bins=200)
    #plt.show()      

    for ndiv_cnt in sorted(Counter(number_of_divisors).items()):
        print(f"Number of divisors={ndiv_cnt[0]}. Numbers with this many divisors={ndiv_cnt[1]}")   

main()
