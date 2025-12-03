

def factorial_recursion(n):
    if n>1:
        return factorial_recursion(n-1)*n
    else:
        return 1

#print(factorial_recursion(999))
#print(factorial_recursion(1000))   # RecursionError: maximum recursion depth exceeded


def factorial_loop(n):
    factorial = 1
    for v in range(1, n + 1):
        factorial = factorial * v
    return factorial


#print(factorial_loop(999))
print(factorial_recursion(999) == factorial_loop(999))



x = factorial_loop(100000)

import math
print(int(math.log10(x))+1)   # number of digits

import sys
sys.set_int_max_str_digits(500000)

print(x)

with open("/Users/Lorand/tmp/aa.txt", "a") as f:
  print(x, file=f)

print(factorial_loop(26))

#403 291 461 126 605 635 584 000 000
# 9   8   7   6   5   4   3   2   1

print(float(403291461126605635584000000))

print(403291461126605635584000000/1000000/3600/24/365/1e9)