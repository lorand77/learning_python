import random

x = [2,4,5,10]

y = []
for v in x:
    if v % 2 == 0:
        y.append(v**2)

print(y)


y = []
for i in range(len(x)):
    if x[i] % 2 == 0:
        y.append(x[i]**2)

print(y)


#y = [v**2 for v in x]
y = [v**2 for v in x if v % 2 == 0]

print(y)


x = [random.randint(1, 6) for i in range(10)]

print(x)

