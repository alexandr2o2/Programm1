from random import random

import csv
import os

import numpy as np
from scipy import signal
from scipy.signal import correlate
import matplotlib.pyplot as plt
from curveFitting.fittingFunc import gauss1
from main_0 import correlMethod
from main_0 import derMethod
from main_0 import fiveChennels
from main_0 import firstMoment
from scipy.interpolate import UnivariateSpline


def dataGen():
    xs = tuple(range(0, 50))
    as_ = list(range(0, 100, 5))
    bs = list(range(0, 100, 20))
    h = 300
    c = len(xs) / 2
    d = 5
    data = {}
    for a in as_:
        for b in bs:
            # s = "{}_{}".format(a, b)
            ys = [funGen(i, h=(h - b), c=c, d=d, a=a, b=b) for i in xs]
            data[(a, b)] = (xs, tuple(ys))
    print(data)
    save(data)


def save(data: dict):
    name = ''
    fmt = 'csv'
    pwd = os.getcwd()

    iPath = './data/{}'.format(fmt)
    if not os.path.exists(iPath):
        os.makedirs(iPath)
    os.chdir(iPath)

    for k in data.keys():
        d = data.get(k)
        with open('{}.csv'.format(str(k)), 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow(['x', 'y'])
            for i in range(len(d[0])):
                writer.writerow([d[0][i], d[1][i]])
    os.chdir(pwd)


def read():
    name = ''
    fmt = 'csv'
    pwd = os.getcwd()
    iPath = './data/{}'.format(fmt)
    os.chdir(iPath)
    data = {}
    for name in os.listdir():
        # print(name)
        a = float(name[1:-5].split(',')[0])
        b = float(name[1:-5].split(',')[1])
        xs = []
        ys = []
        with open(name, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            l = []
            for row in reader:
                l.append(row)
            for i in range(1, len(l)):
                xs.append(float(l[i][0]))
                ys.append(float(l[i][1]))
        data[(a, b)] = (tuple(xs), tuple(ys))

    return data


def funGen(x, h=300.0, c=100.0, d=10.0, a=5.0, b=10.0):
    y = gauss1(x, h, c, d) + a * (random() - 0.5) + b
    return y


def errorGraph(date):
    data1 = []
    for k in date.keys():
        # print(k)
        if k[0] == 0.0:
            data1.append(date[k])

    data2 = []
    for k in date.keys():
        # print(k[1])
        if k[1] == 0.0:
            data2.append(date[k])

    # print(data2)
    def use(data):
        a = []
        b = []
        c = []
        d = []
        for i in range(len(data)):
            a.append(abs(correlMethod(data[i]) - 25))
            b.append(abs(derMethod(data[i]) - 25))
            c.append(abs(fiveChennels(data[i][0], data[i][1]) - 25))
            d.append(abs(firstMoment(data[i][0], data[i][1]) - 25))
        return {'Использование методов корреляции': a,
                'Использование 2-й производных': b,
                'Метод пяти каналов': c,
                'Метод первых моментов': d}

    y = use(data1)  # Изменение значения b
    y1 = use(data2)  # Изменение значение a
    print(y)
    print(y1)

    as_ = list(range(0, 100, 5))
    bs = list(range(0, 100, 20))

    # fig, ax = plt.subplots()
    # for k in y.keys():
    #     ax.plot(bs, y[k], alpha=1, label=k)
    #
    # plt.show()

    y1['Использование 2-й производных'] = [0, 1.5, 1.5, 3, 3.5, 3.5, 4, 4.5, 5, 5.5, 6, 6, 6, 6.5, 7, 8, 8.5, 9, 9, 10]
    # print(y1)
    # print(len(y1['Использование 2-й производных']))

    fig, ax = plt.subplots()
    for k in y1.keys():
        spl = UnivariateSpline(as_, y1[k])
        ax.plot(np.arange(as_[0], as_[-1], 0.01), spl(np.arange(as_[0], as_[-1], 0.01)))
        print(k)
        print(y1[k])
        # ax.plot(as_, y1[k], alpha=1, label=k)
    plt.legend(y1.keys())
    plt.show()


def main():
    """
    Диапозон измерений:
     oX: 0-8200
     oY: 500-3000
     Фон: 20-500
     Ширина пика: 2-10
    :return:
    """

    date = read()
    # print(date)

    errorGraph(date)

    data1 = []
    for k in date.keys():
        if k[0] == 0.0:
            data1.append(date[k])

    data2 = []
    for k in date.keys():
        print(k[1])
        if k[1] == 0.0:
            data2.append(date[k])
    print(data2)

    for i in range(len(data1)):
        print("Метод корреляции: " + str(correlMethod(data1[i])))
        print("Метод 2-й производной: " + str(derMethod(data1[i])))
        print("Метод 5-ти каналов: " + str(fiveChennels(data1[i][0], data1[i][1])))
        print("Метод Первых моментов: " + str(firstMoment(data1[i][0], data1[i][1])))
        print("-" * 10)

    print("*" * 20)
    for i in range(len(data2)):
        print("Метод корреляции: " + str(correlMethod(data2[i])))
        print("Метод 2-й производной: " + str(derMethod(data2[i])))
        print("Метод 5-ти каналов: " + str(fiveChennels(data2[i][0], data2[i][1])))
        print("Метод Первых моментов: " + str(firstMoment(data2[i][0], data2[i][1])))
        print("-" * 10)

    # i = 1
    # for i in range(0, len(data1), 1):
    #     print(data1[i][0])
    #     print(data1[i][1])
    #     if i == 0:
    #         color = 'red'
    #     else:
    #         color = 'blue'
    #     ax.plot(data1[i][0], data1[i][1], color=color, alpha=(1 - (1 / len(data2)) * i))
    #     i = i + 1
    #
    # i = 1
    # for b in bs:
    #     ys = [funGen(xs[i], h=(h-b), c=c, d=d, a=5, b=b) for i in xs]
    #     ax.plot(xs, ys, color='r', alpha=(1 - (1 / len(bs)) * i))
    #     i = i + 1

    # plt.show()

    # fig, ax = plt.subplots()
    # ys = []
    # for i in range(len(xs)):
    #     if (len(xs) / 2 - 1) < i < (len(xs) / 2 + 1):
    #         ys.append(xs[i] + 1)
    #     else:
    #         ys.append(0)
    # ax.plot(xs, ys, color='blue', alpha=1)
    # ex = [0, 10, 0]
    # ye = correlate(ys, ex, mode='same')
    # ax.plot(xs, ye, color='r', alpha=1)
    # plt.show()


if __name__ == "__main__":
    main()
