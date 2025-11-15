def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Thomas")


def my_function(x):
  if not (type(x) == int or type(x) == float):
    raise TypeError
  return 5 * x

print(my_function(1))

def my_function(x):
  return 6 * x

print(my_function(1))
print(my_function(3))
print(my_function(4))
print(my_function(10))


#Lorand's absolute value
def l_abs(x):
  if x >= 0:
    return x
  else:
    return -x

print(l_abs(5))
print(l_abs(-5))
print(l_abs(0))
print(l_abs(0.3))
print(l_abs(-0.3))


#lists
numbers1 = [1, 2, 5, 4, 5, 2]
numbers2 = [1, -2, 0, 5.5, 2.5]
numbers3 = [3]
numbers4 = []


#adding numbers in a list
def list_add(numbers):
  s = 0
  for v in numbers:
    s = s + v
  return s

print(list_add(numbers1))
print(list_add(numbers2))
print(list_add(numbers3))
print(list_add(numbers4))


#counting even numbers in a list
def list_count_even(numbers):
  count = 0
  for v in numbers:
    if v % 2 == 0:
      count = count + 1
  return count

print(list_count_even(numbers1))
print(list_count_even(numbers2))
print(list_count_even(numbers3))
print(list_count_even(numbers4))

