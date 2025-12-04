my_dog = "Rex"
print(my_dog)

bread_rolls_Lorand_day = 2
bread_rolls_Papa_day = 3
bread_rolls_total_day = bread_rolls_Lorand_day + bread_rolls_Papa_day
bread_rolls_total_week = bread_rolls_total_day * 7
print(bread_rolls_total_week)

a = 1
print(a)
print(type(a))

b = 2/3
print(b)
print(type(b))

a = 5
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

# my own add function 
def add(a, b):
    c = a + b
    return c

my_sum = add(10, 11)
print(my_sum)

print(abs(-5))
print(abs(5))

print(pow(2, 3))

#write a Celsius the Fahrenheit converter
def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))

#write a Fahrenheit to Celsius converter
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

print(fahrenheit_to_celsius(32))
print(fahrenheit_to_celsius(212))
print(fahrenheit_to_celsius(98.6))

my_dog = "Rex"
print(my_dog)
my_cat = "Whiskers"
print(my_cat)
my_animals = my_dog + " and " + my_cat
print(my_animals)
print(my_dog * 3)
print(my_cat * 3)

print("ab" in "abc")
print("ab" in "bcd")

print(len(my_cat))

x = "abc\nxyz"
print(x)
print(len(x))
x = """abc
xyz"""
print(x)
print(len(x))

paragraph = "There are many benefits of having dogs, but there are some disadvantages. The most important benefits are that dogs provide love and companionship by following you everywhere therefore you don’t feel lonely. Another important benefit is that you can have fun together by playing in the yard, playing fetch or petting your dog. However, there are some disadvantages of having a dog, because you need to do a lot of work such as feeding and walking your dog. In summary, having dogs has more benefits than disadvantages."
print(paragraph)
print()

paragraph = "There are many benefits of having dogs, but there are some disadvantages. \
The most important benefits are that dogs provide love and companionship by following you everywhere \
therefore you don't feel lonely. Another important benefit is that you can have fun together by \
playing in the yard, playing fetch or petting your dog. However, there are some disadvantages of \
having a dog, because you need to do a lot of work such as feeding and walking your dog. \
In summary, having dogs has more benefits than disadvantages."
print(paragraph)
print("\n\n\n")

paragraph = """There are many benefits of having dogs, but there are some disadvantages. 
The most important benefits are that dogs provide love and companionship by following you everywhere 
therefore you don't feel lonely. Another important benefit is that you can have fun together by 
playing in the yard, playing fetch or petting your dog. However, there are some disadvantages of 
having a dog, because you need to do a lot of work such as feeding and walking your dog. 
In summary, having dogs has more benefits than disadvantages."""
print(paragraph)




words_per_day = 3
words_per_week = words_per_day * 6
words_per_year = words_per_week * 50
print("I learn", words_per_year, "words per year.")
print("I learn " + str(words_per_year) + " words per year.")

x = 8
x = 0b1000
x = 0xf
print(x)

y = 1.1
y = 0.1

y = 1.0

y = 1.
y = .1

y = 1.2e3   # 1.2 * 10**3  = 1.2 * 1000
y = 1e6
y = 1e9
y = 1e100
print(y)
y = 10**100
print(y)

y = 1.2e-3  # 1.2 * 0.001
y = 1e-3
print(y)

print(4.94e-324)
print(4.94e-324/2)
print(1.70e308)
print(1.70e308*2)

print(int(1.70e308))

print("abc" + "def")
print("abc" * 3)
print(len("abc"))

print("abc" == "abc")
print("abc" == "abcd")
print("abc" != "abc")
print("arr" < "ahu")
print("Ab".lower() == "aB".lower())
print("you've" > "youth club")
print('A' < 'a')

score = 95
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
elif score >= 45:
    grade = "D"
else:
    grade = "F"
print(grade)


# assign x NaN
x = float("nan")
print(x)
print(x > 0)
print(x <= 0)
print(x == x)

# assign x infinity
x = float("inf")
print(x)
print(x > 0)
print(x <= 0)

print(0.0*float("inf"))
import math
#print(math.sqrt(-1))

x = "abc"
print(x.upper())
print(x)
x = x.upper()
print(x)