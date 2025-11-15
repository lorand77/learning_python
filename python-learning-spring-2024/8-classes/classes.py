class A:
    def __init__(self, x):
        self.x = x

    def increment(self):
        self.x += 1

    def print(self):
        print(self.x)

a1 = A(1)
print(a1.x)
a1.print()
a1.increment()
a1.print()

a2 = A(2)
a2.increment()
a2.print()


