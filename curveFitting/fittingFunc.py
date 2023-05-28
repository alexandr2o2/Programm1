import inspect
import random

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def lineAppr(x: list, y: list):
    if len(x) != len(y):
        return None
    N = len(x)
    a2 = 0
    for i in x:
        a2 += i * i
    a2 = a2 / N
    a1 = 0
    for i in range(N):
        a1 += x[i] * y[i]
    a1 = a1 / N
    a3 = 0
    a3 = sum(x) / N
    a4 = sum(y) / N
    k = (a1 - a3 * a4) / (a2 - a3 * a3)
    b = a4 - k * a3
    x_f = x
    y_f = [k * i + b for i in x_f]
    return x_f, y_f


def gauss1(x, h, c, d):
    return h * np.exp(-(np.square((x - c) / d)) / 2)


def gauss2(x, h1, c1, d1, h2, c2, d2):
    return gauss1(x, h1, c1, d1) + gauss1(x, h2, c2, d2)


def gauss3(x, h1, c1, d1, h2, c2, d2, h3, c3, d3):
    return gauss2(x, h1, c1, d1, h2, c2, d2) + gauss1(x, h3, c3, d3)


def gauss4(x, h1, c1, d1, h2, c2, d2, h3, c3, d3, h4, c4, d4):
    return gauss2(x, h1, c1, d1, h2, c2, d2) + gauss2(x, h3, c3, d3, h4, c4, d4)


def derivative(f, x0):
    """
    :param f:
    :param x0:
    :return:
    """
    if not inspect.isfunction(f):
        raise ValueError
    h = 1e-5
    # inspect.
    return (f(x0 + h) - f(x0 - h)) / (2 * h)


def nonLinerSqAppr(f, x: list, y: list, ip0: list, bounds=(-np.inf, np.inf)):
    p, _ = curve_fit(f, x, y, p0=ip0, bounds=bounds)
    return p


def smooth1(x: list, y: list):
    y_smooth = []
    y_smooth.append((3 * y[0] + 2 * y[1] + y[2] - y[4]) / 5)
    y_smooth.append((4 * y[0] + 3 * y[1] + 2 * y[2] + y[3]) / 10)
    for i in range(2, len(y) - 2):
        y_smooth.append((y[i - 2] + y[i - 1] + y[i] + y[i + 1] + y[i + 1]) / 5)
    y_smooth.append((4 * y[-1] + 3 * y[-2] + 2 * y[-3] + y[-4]) / 10)
    y_smooth.append((3 * y[-1] + 2 * y[-2] + y[-3] - y[-4]) / 5)
    return x, y_smooth


def main():
    h1 = 0.04 / np.sqrt(2 * np.pi)
    d1 = 0.2
    c1 = 1
    h2 = 0.03 / np.sqrt(2 * np.pi)
    d2 = 0.2
    c2 = 1.5
    x_dots = [x*0.01 for x in range(300)]
    y_dots = []
    for x in x_dots:
        y_dots.append(gauss2(x, h1, c1, d1, h2, c2, d2) + random.random()*0.0005)

    # [h1, c1, d1, h2, c2, d2]
    ip0 = [.01, .1, 1, .01, .01, 1.5]
    #print(x_dots)
    #print(y_dots)
    par = nonLinerSqAppr(gauss2, x_dots, y_dots, ip0)
    print(par)
    x_f = x_dots
    y_f = []
    for x in x_dots:
        y_f.append(gauss2(x, *par))
    # x_f, y_f = smooth1(x_dots, y_dots)
    y1 = []
    y2 = []
    for x in x_dots:
        y1.append(gauss1(x, *par[0:3]))

    for x in x_dots:
        y2.append(gauss1(x, *par[3:6]))

    fig, ax = plt.subplots()
    ax.plot(x_dots, y_dots)
    ax.plot(x_f, y_f)
    ax.plot(x_dots, y1)
    ax.plot(x_dots, y2)
    plt.show()


if __name__ == "__main__":
    main()
