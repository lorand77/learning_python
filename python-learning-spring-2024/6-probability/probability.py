import random
import matplotlib.pyplot as plt
from collections import Counter
import time

def sum_rolls(n_rolls):
    dice_rolls = []
    for i in range(n_rolls):
        dice_rolls.append(random.randint(1,6))
    return sum(dice_rolls)

# N = 60
# dice_rolls = []
# for i in range(N):
#     dice_rolls.append(random.randint(1,6))
# print(sorted(dice_rolls))

# dice_roll_counts = []
# for i in range(6):
#     dice_roll_counts.append(dice_rolls.count(i + 1))
# print(dice_roll_counts)

# plt.bar(range(1, 7), dice_roll_counts)
# plt.show()
        
# for i in range(1,11):
#     print((1/6)**i)


# start = time.perf_counter()
# dice_rolls_sums = []
# for i in range(1000000):
#     dice_rolls_sums.append(sum_rolls(10))
# end = time.perf_counter()
# print(f"Time:{end - start}")

# print(Counter(dice_rolls_sums))
# plt.hist(dice_rolls_sums, bins = range(10,61))
# plt.show()

N = 1_000_000
n_win = 0
for i in range(N):
    if sum_rolls(10) == random.randint(10,60):
        n_win += 1
print(n_win/N*100)



