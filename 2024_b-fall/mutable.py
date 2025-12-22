a = [0]*6
x = []
for i in range(3):
    x.append(a.copy())

print(x)

x[0][0]=1
print(x)

x = 2

def f(a):
    print(a)
    a = 3
    print(a)

f(x)
print(x)




def f(a):
    print(a)
    a[0] = 0
    print(a)

x = [1,2]
f(x)
print(x)

x = [1,2]
f(x.copy())
print(x)

