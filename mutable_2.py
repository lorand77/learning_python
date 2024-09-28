import copy

x = [[1, 2, 3], [11, 22, 33]]
y1 = x
y2 = x.copy()
y3 = list(x)
y4 = copy.copy(x)
y5 = x[:]
y6 = copy.deepcopy(x)

x[0][0] = 111

print(x, y1, y2, y3, y4, y5, y6)