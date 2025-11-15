
#while True:
#    print("Hello, World!")


i = 1
while i <= 3:
    print("Meow!")
    i = i + 1

i = 0
while i < 3:
    print("Woof!")
    i = i + 1

i = 0
while i < 3:
    print("Squeak!")
    i += 1

for i in [1,2,3]:
    print(i)

for i in ["a","b","c"]:
    print(i)

for i in range(3):
    print("Chirp!",i)

print(range(10))
print(list(range(10)))

for _ in range(3):
    print("Moo!")


for i in [1,2]:
    print("Meow!")

while i < 3:
    print("Woof!")
    i = i + 1


numbers = [1, 27, 3, 42, 64, 15]
numbers_doubled = []
i = 0
while i < len(numbers):
    numbers_doubled.append(numbers[i] * 2)
    i = i + 1
print(numbers_doubled)


numbers = [1, 27, 3, 42, 64, 15]
numbers_doubled = []
for i in range(len(numbers)):
    numbers_doubled.append(numbers[i] * 2)
print(numbers_doubled)


numbers = [1, 27, 3, 42, 64, 15]
numbers_doubled = []
for v in numbers:
    numbers_doubled.append(v * 2)
print(numbers_doubled)
