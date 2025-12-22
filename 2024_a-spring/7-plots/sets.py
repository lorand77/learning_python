
x_list = [1,2,3,2,3]

x_set = {3,2,1}

print(x_list)
print(type(x_list))

print(x_set)
print(type(x_set))

print(len(set([1,2,3,1,1,1,2,4])))


A = {1,3,2}
A = {"a", "b","c"}
print(type(A))

D = {1:"a", 2:"b", 3:"c"}
print(type(D))

print(A)
#print(A[0])   #'set' object is not subscriptable

for v in A:
    print(v)

print("a" in A)
print("d" in A)
print("d" not in A)

print(len(A))

D = {}
print(type(D))

E = set()
print(type(E))

A = {1,2,3,4}
B = {0,2,4,6}

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))

print(A | B)
print(A & B)
print(A - B)
print(B - A)

A.add(5)
print(A)

A.remove(3)
print(A)

print(set([1,2,3,1,1,1,2,4]))
print(list({3,1,2}))


print({3,2,1})
print({3.,2.4,1.})
print({"a","b","c"})

X = {1,2,3}
Y = {1,2,3,4,5}
print(X.issubset(Y))
print(Y.issuperset(X))