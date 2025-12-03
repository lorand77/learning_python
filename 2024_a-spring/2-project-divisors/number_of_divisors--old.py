import matplotlib.pyplot as plt
from divisors import get_divisors, get_number_of_divisors_using_prime_factors
import time
from collections import Counter


def get_number_of_divisors_for_1toN(N):
    numbers = list(range(1, N+1))
    number_of_divisors = []
    for i in numbers:
        #number_of_divisors.append(len(get_divisors(i)))
        number_of_divisors.append(get_number_of_divisors_using_prime_factors(i))
    return number_of_divisors


# def get_numbers_with_n_divisors(number_of_divisors, n):
#     numbers_with_n_divisors = []
#     for i in range(len(number_of_divisors)):
#         if number_of_divisors[i] == n:
#             numbers_with_n_divisors.append(i + 1) 
#     return numbers_with_n_divisors


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
        
    #print(number_of_divisors)

    # max_divisors = max(number_of_divisors)
    # print(f"max divisors={max_divisors}")
    # print(f"Largest number of divisors={sorted(number_of_divisors)[-10:]}")

    # for n in range(1,max_divisors+1):
    #     print(f"Number of divisors={n}. Numbers with this many divisors={len(get_numbers_with_n_divisors(number_of_divisors, n))}")   

    for v in sorted(dict(Counter(number_of_divisors)).items()):
        print(f"Number of divisors={v[0]}. Numbers with this many divisors={v[1]}")   

main()
