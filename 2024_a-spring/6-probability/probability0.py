import random

N = 100000000

n = 0
for i in range(N):
    roll = random.randint(1,6)
    if roll == 6:
        n += 1

print(f"N={N}  n={n}  n/N={n/N}  prob={1/6}")