
x = [1,2,3]
x = []

if len(x)>0:
    print("not empty")
else:
    print("empty")

if x:
    print("not empty")
else:
    print("empty")


class A:
    def __init__(self, x):
        self.x = x

a1 = A(1)
a2 = A(2)

print(a1.x)
print(a2.x)

class B(A):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

b1 = B(1, 2)
b2 = B(3, 4)

print(b1.x, b1.y)
print(b2.x, b2.y)


