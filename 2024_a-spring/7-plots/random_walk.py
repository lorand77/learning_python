import random
import matplotlib.pyplot as plt


for k in range(4):

    # x = random.choice([0,50,100])
    # y = random.choice([0,50,100])

    x = random.randint(0,100)
    y = random.randint(0,100)

    print(f'Starting at ({x},{y})')

    x_hist = [x]
    y_hist = [y]
    xy_hist = [(x, y)]

    for i in range(1000):
        move = random.randint(1,4)
        if move == 1:
            x += 1
            if x > 100:
                x -= 1
        elif move == 2:
            x -= 1
            if x < 0:
                x += 1
        elif move == 3:
            y += 1
            if y > 100:
                y -= 1
        else:
            y -= 1
            if y < 0:
                y += 1
        x_hist.append(x)
        y_hist.append(y)
        xy_hist.append((x, y))

    print(f'{len(set(xy_hist)) / 101 / 101 * 100}% was covered.')

    plt.plot(x_hist,y_hist, marker = "o")
    ax = plt.gca()
    ax.set_xlim([0, 100])
    ax.set_ylim([0, 100])
    ax.set_aspect('equal', adjustable='box')

plt.show()