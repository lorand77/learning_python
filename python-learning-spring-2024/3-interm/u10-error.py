import random

# (             SyntaxError
# 1 + "a"       TypeError
#x              NameError
#l = [17,8]
#l[14]          IndexError
# d = {1:3,5:45}
# d[4]          KeyError
#int("12.67")   ValueError
#9/0            ZeroDivisionError
#import agh     ModuleNotFoundError


a = 1.3
b = 0

try:
    print(a/b)
except ZeroDivisionError:
    print("Congrats! You have just divided by ZERO!!!")

print(a+b)

print("*"*50)


import math

def get_divisors(n):
    """Returns a list of all divisors of n (n must be a positive integer number)."""
    if not (type(n) == int and n > 0):
        raise ValueError("Input must be a positive integer.")
    divisors = []
    for v in range(1, int(math.sqrt(n)) + 1):
        if n % v == 0:
            divisors.append(v)
            if v != n // v:
                divisors.append(n // v)
    return sorted(divisors)


# print(get_divisors(24))
# print(get_divisors(3))
# print(get_divisors(1))

#print(get_divisors(0))   #incorrect
#print(get_divisors(-2))
#print(get_divisors("haha"))
#print(get_divisors(3.4))  #incorrect?


for i in range(10):
    n = random.randint(0,100)
    try:
        print(f"i={i}  n={n}  div={get_divisors(n)}")
    except ValueError:
        print(f"i={i}  n={n}  is not a positive integer.")

print("*"*50)


from sympy.ntheory import factorint
print(factorint(24))
#print(factorint("abc"))
print(factorint(-4))
print(factorint(0))
#print(factorint(2.4))