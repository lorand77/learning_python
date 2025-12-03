numbers = [1, 2, 23, 4, 6, 15]       # length L
# indexes  0  1   2  3  4  5           0..L-1
# indexes -6 -5  -4 -3 -2 -1           (-1)..(-L)
print(numbers)
print(type(numbers))

print(numbers[2])
print(len(numbers))
# lenght=6 index=0..5    lenght=L  index=0..L-1
#print(numbers[6])  #error (out of range)

print(numbers[-1])
# print(numbers[-7])   #error (out of range)

# print(numbers[3.0])  #error (index must be int) 
i = 2
print(numbers[i*2])

numbers = []
print(numbers)
print(len(numbers))

numbers = [7]
print(numbers)
print(len(numbers))

numbers = [1, 2, 23, 4, 6, 15] 
numbers[1] = 7
print(numbers)
my_fav_numb = numbers[1]   
print(my_fav_numb)
# numbers[i] = value    # set value at index i
# x = numbers[i]        # get value at index i
# set value:   numbers[i] = expression
# get value:   function_call(numbers[i]*2,"abc")
#numbers[6] = 7   #error (out of range)

#function call:  len(numbers)
#                ^name of the func
#                     (
#                     ^argument (or several arguments separated by commas)
#                            )
#method=function of an object
#method call:     numbers.append(argument(s))
#                  ^object
#                        .
#                           ^name of the method
#                                (
#                                ^argument (or several arguments separated by commas)
#                                       )
print(numbers)
numbers.append(100)
print(numbers)

numbers.sort()
print(numbers)
numbers.insert(2, 200)
print(numbers)

del numbers[1]
print(numbers)

removed_number = numbers.pop(2)  
print(numbers)
print(removed_number)

del numbers[-1]
print(numbers)
numbers.pop(-1) 
print(numbers)

numbers.reverse()
print(numbers)

print(numbers.index(1))

# TODO: slice, in, clear, copy, extend/join(+), 
# https://www.w3schools.com/python/python_lists.asp

print(200 in numbers)
print(300 in numbers)

numbers = [1, 1, 3, 2, 1, 4]
print(numbers.count(1))
print(numbers.count(2))
print(numbers.count(1.0))
print(1==1.0)


