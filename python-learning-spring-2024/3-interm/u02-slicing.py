
sports = ["soccer", "basketball", "ping-pong", "swimming", "baseball"]
for v in sports:
    if v[0:3] == "bas":
        print(v)

print(len(sports))
sports_sorted = sorted(sports)
print(sports)
print(sports_sorted)
print(sports[0])
print(sports[-2])
print(sports[1:4])
print(sports[1:2])
print(sports[1])
print(sports[1:1])
print(type(sports[1:2]))
print(type(sports[1]))


a = [0,1,2,3,4,5,6,7,8,9]

print(a[1:5])
print(a[1:])
print(a[1:6:2])
print(a[1::2])
print(a[:4])
print(a[:])
print(a[::])
print(a[6:1:-1])
print(a[6::-1])
print(a[-1::-1])
print(a[-2::-1])
print(a[-2::-2])
print(a[-2:-6:-2])
print(a[-2:4:-2])

print(slice(1,4))
print(a[slice(1,4)])
print(a[1:4])

s = "Lorand"
print(s[0])
print(s[0:1])
print(type(s[0]))
print(type(s[0:1]))