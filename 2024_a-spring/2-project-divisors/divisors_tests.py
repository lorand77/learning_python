from divisors import get_divisors
import time
import math


def get_divisors_v1(n):
    divisors = []
    for v in range(1, n + 1):
        if n % v == 0:
            divisors.append(v)
    return divisors


start = time.perf_counter()
x = get_divisors_v1(int(1e7))
end = time.perf_counter()
print(end - start)

start = time.perf_counter()
x = get_divisors(int(1e7))
end = time.perf_counter()
print(end - start)
print("-" * 30)


# print(math.sqrt(12345678))

print(get_divisors_v1(12345678))
print(get_divisors(12345678))

print(get_divisors_v1(1000000))
print(get_divisors(1000000))
print("-" * 30)


for i in range(1, 101):
   print(i, get_divisors(i))
