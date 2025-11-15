from fractions import Fraction as F

a = F(2,3)
a = F("2/3")
print(type(a))
print(a)
print(a.numerator)
print(a.denominator)

b = F(1,5)
print(a.__add__(b))
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print(1/3+1/6)
print(1/2)

print(F("1/3")+F("1/6"))
print(F("1/2")+1)
