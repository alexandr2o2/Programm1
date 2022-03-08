import matplotlib.pyplot as plt

from data import data1


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

    x_d.insert(0, x[0])
    y_d.insert(0, 0)
    x_d.append(x[-1])
    y_d.append(0)
    return x_d, y_d


x, y = axes(data1)

x1, y1 = diff2(x, y)

print(len(x))
print(len(x1))

fig, ax = plt.subplots()
ax.plot(x, y)
ax.plot(x1, [y1*200 for y1 in y1])
plt.show()
