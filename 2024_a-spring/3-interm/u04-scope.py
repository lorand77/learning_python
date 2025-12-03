# #print(a)  # NameError

# a = 1
# print(a)


# def f():
#     #print(b)   # UnboundLocalError: cannot access local variable 'b' where it is not associated with a value
#     b = 2
#     print(b)

# f()


# def g(c):
#     print(c)

# g(3)




def f1():
    f2()

def f2():
    print("hi")

f1()


