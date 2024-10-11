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


print(factorial(10))
print(factorial_with_recursion(10))
