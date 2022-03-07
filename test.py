import matplotlib.pyplot as plt

from data import data5


def axes(data):
    y = [i[1] for i in data]
    x = [i[0] for i in data]
    return x, y


def diff2(x, y):
    x_d = []
    y_d = []
    h = x[1] - x[0]
    for i in range(1, len(x) - 1):
        y_d.append((y[i - 1] - 2 * y[i] + y[i + 1]) / ((2 * h) * (2 * h)))
        x_d.append(x[i])
    return x_d, y_d


x, y = axes(data5)

x1, y1 = diff2(x, y)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.plot(x1, [y1*200 for y1 in y1])
plt.show()
