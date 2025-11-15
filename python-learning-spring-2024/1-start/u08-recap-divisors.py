import math

#import time
#import matplotlib.pyplot as plt


# def get_divisors_v1(n):
#     divisors = []
#     for v in range(1, n + 1):
#         if n % v == 0:
#             divisors.append(v)
#     return divisors


def get_divisors(n):
    """Returns a list of all divisors of n."""
    divisors = []
    for v in range(1, int(math.sqrt(n)) + 1):
        if n % v == 0:
            divisors.append(v)
            if v != n // v:
                divisors.append(n // v)
    return sorted(divisors)


# start = time.perf_counter()
# x = get_divisors_v1(int(1e7))
# end = time.perf_counter()
# print(end - start)

# start = time.perf_counter()
# x = get_divisors(int(1e16))
# end = time.perf_counter()
# print(end - start)


# print(get_divisors_v1(12345678))
# print(get_divisors(12345678))

# print(get_divisors_v1(1000000))
# print(get_divisors(1000000))



# for i in range(1, 101):
#    print(i, get_divisors(i))


# numbers = list(range(1, 100001))
# number_of_divisors = []
# for i in numbers:
#     number_of_divisors.append(len(get_divisors(i)))

# max_divisors = max(number_of_divisors)
# print(max_divisors)
# print(number_of_divisors.index(max_divisors)+1)

# #print(sorted(number_of_divisors))
# numbers_max_divisors = []
# for i in range(len(number_of_divisors)):
#     if number_of_divisors[i] == max_divisors:
#         numbers_max_divisors.append(i+1)
# print(numbers_max_divisors)

# #plt.bar(numbers, number_of_divisors)
# plt.hist(number_of_divisors, bins=60)
# plt.show()



