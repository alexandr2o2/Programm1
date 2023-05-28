import numpy as np
import matplotlib.pyplot as plt
from data import data_real
from main_0 import axesSplit
from main_0 import hight_filter
from main_0 import join
from main_0 import savitzky_Golay_filter
from main_0 import findCentroids
from main_0 import *

def main():
    data0 = data_real
    x_f, y_f = hight_filter(data0)
    data2 = join(x_f, y_f)
    x_f2, y_f2 = savitzky_Golay_filter(data0)

    c1, c2 = findCentroids(x_f, y_f, 0.2)
    c3, c4 = findCentroids(x_f2, y_f2, 0.2)


    print('Центроиды первого фильтра:')
    print(c1)
    print('*'*20)
    print(c2)
    print('-'*20)
    print('Центроиды вторго фильтра:')
    print(c3)
    print('*' * 20)
    print(c4)

    x_dots, y_dots = axesSplit(data0)

    x_d, y_d = diff2(x_f, y_f)
    k = max(y_dots)/max(y_d)
    y_d = list(map(lambda y: y*k, y_d))

    x_d2, y_d2 = diff2(x_f2, y_f2)
    k = max(y_f2) / max(y_d2)
    y_d2 = list(map(lambda y: y * k, y_d2))

    fig, ax = plt.subplots()
    ax.plot(x_dots, y_dots, '--')
    ax.plot(x_f, y_f)
    ax.plot(x_d, y_d)

    fig2, ax2 = plt.subplots()
    ax2.plot(x_dots, y_dots, '--')
    ax2.plot(x_f2, y_f2)
    ax2.plot(x_d2, y_d2)

    plt.show()


if __name__ == '__main__':
    main()
