import time
import sys

N = 100000
sys.setrecursionlimit(N + 1)

def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f = f * i
    return f


def factorial_with_recursion(n):
    if n > 1:
        return n * factorial_with_recursion(n-1)
    else:
        return 1


start_time = time.time()
x = factorial(N)
end_time = time.time()
print(end_time - start_time)


start_time = time.time()
x2 = factorial_with_recursion(N)
end_time = time.time()
print(end_time - start_time)

# print(x, x2)
