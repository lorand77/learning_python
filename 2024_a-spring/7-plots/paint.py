import matplotlib.pyplot as plt

N = 5

x_hist = []
y_hist = []

# x = 0
# y = 0
# for i in range(N+1):
#     for j in range(N+1):
#         x_hist.append(x)
#         y_hist.append(y)
#         x += 1
#     x = 0
#     y += 1

x = 0
y = 0
for i in range(N+1):
    for j in range(N+1):
        x_hist.append(x)
        y_hist.append(y)
        if i % 2 == 0:
            if x < N:
                x += 1
        else:
            if x > 0:
                x -= 1
    y += 1


# for y in range(N+1):
#     for x in range(N+1):
#         x_hist.append(x)
#         y_hist.append(y)


plt.plot(x_hist, y_hist, marker = "o")
ax = plt.gca()
ax.set_xlim([0, N])
ax.set_ylim([0, N])
ax.set_aspect('equal', adjustable='box')
plt.show()

# plt.plot(x_hist, marker = "o")
# plt.plot(y_hist, marker = "o")
# plt.show()
