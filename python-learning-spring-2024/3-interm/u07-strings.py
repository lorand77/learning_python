a = 1
a = 1.2
a = True
a = "abc"

print(float(1))
print(int(1.2))
print(str(1))


a = [1,2,3]
a = [ [1,2], ["a","b"] ]
a = {"a":"A", "b":"B"}


print("abcdef"[0])
print("abcdef"[0:2])
print("abcdef"[-1])
print("abcdef"[2:])

print(len("abcdef"))
print("abcdef" + "XYZ")
print("abcdef " * 2)
print("a" in "abcdef")
print("x" in "abcdef")
print("cd" in "abcdef")


print(list("abcdef"))

print(str([1,2,3]))
print("[1, 2, 3]")
print(str(["x","y"]))

for c in "abcdef":
    print(c)


print("abcde".replace("c","X"))    
print("abcde".replace("cd","XXX"))    

x = "Video games have         a significant positive and negative impact on children."
x = x.replace(".","")
x = x.split()
print(x)

print("ab\"\'c")
print("I \"like\" soccer")
print('I "like" soccer')

print("abc def".capitalize())
print("abc def".upper())
print("Abc DEF".lower())
print("Abc DEF a A".count("a"))
print("abcdef".find("cd"))
print("abcdef".find("cx"))
print("abcdef".index("cd"))
#print("abcdef".index("cx"))

print("abcdef".isnumeric())
print("123".isnumeric())   # piece of shit!!!


