import copy

x = [[1, 2, 3], [11, 22, 33]]
y1 = x
y2 = x.copy()
y3 = list(x)
y4 = copy.copy(x)
y5 = x[:]
y6 = copy.deepcopy(x)

x[0][0] = 111

print("x:", x, "\ny1:", y1, "\ny2:", y2, "\ny3:", y3, "\ny4:", y4, "\ny5:", y5, "\ny6:", y6)

id(x)
id(x[0])
id(y1[0])
id(y2[0])
id(y6[0])



x = [1, 2, 3]
y1 = x
y2 = x.copy()
y3 = list(x)
y4 = copy.copy(x)
y5 = x[:]
y6 = copy.deepcopy(x)

x[0] = 111

print("x:", x, "\ny1:", y1, "\ny2:", y2, "\ny3:", y3, "\ny4:", y4, "\ny5:", y5, "\ny6:", y6)