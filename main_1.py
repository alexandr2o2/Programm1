import csv

import matplotlib
import locale

from data import data_real
import os
import matplotlib.pyplot as plt
import numpy as np

locale.setlocale(locale.LC_ALL, "ru_RU")


class Const:
    PATH = r"C:\Users\user\Desktop\ВКР\Материалы\Созданные_картинки"
    DATAPATH = r"C:\Users\user\Desktop\ВКР\Материалы\Данные"
    FONTSIZE = 12
    LEGEND = dict(loc='upper right', fontsize=FONTSIZE, facecolor='w', framealpha=1.0, edgecolor='black')


def read_data(name):
    pwd = os.getcwd()
    iPath = Const.DATAPATH
    os.chdir(iPath)
    x = []
    y = []
    with open(name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            x.append(row[0])
            y.append(row[1])
    os.chdir(pwd)
    x = x[1:-1]
    y = y[1:-1]
    return np.asarray(x, dtype=np.float64), np.asarray(y, dtype=np.float64)


def set_by_def():
    matplotlib.rcParams['font.family'] = "Times New Roman"
    plt.rcParams['axes.formatter.use_locale'] = True
    plt.rcParams['axes.grid'] = True


def save(name='', fmt='png'):
    pwd = os.getcwd()
    iPath = Const.PATH.format(fmt)
    if not os.path.exists(iPath):
        os.mkdir(iPath)
    os.chdir(iPath)
    plt.savefig('{}.{}'.format(name, fmt), dpi=200, bbox_inches='tight')
    os.chdir(pwd)
    # plt.close()


def main():
    matplotlib.rcParams['font.family'] = "Times New Roman"
    fontsize = 12

    fig = plt.figure()  # Создание объекта Figure
    print(fig.axes)  # Список текущих областей рисования пуст
    print(type(fig))  # тип объекта Figure
    plt.scatter(1.0, 1.0)  # scatter - метод для нанесения маркера в точке (1.0, 1.0)

    # После нанесения графического элемента в виде маркера
    # список текущих областей состоит из одной области
    print(fig.axes)

    # смотри преамбулу
    # save(name='pic_1_4_1', fmt='pdf')
    # save(name='pic_1_4_1', fmt='png')

    plt.show()


def fig_5():
    from curveFitting.fittingFunc import gauss1
    from main_0 import diff
    from main_0 import diff2
    params = (15, 0.5, 0.1)  # h, c, d
    x = np.arange(-0.1, 1.1, 0.01)
    y = gauss1(x, *params)
    (_, y_d1) = diff(x, y)
    (_, y_d2) = diff2(x, y)
    y_d3 = np.zeros(x.shape)
    y_d1 = np.array(y_d1)
    y_d1 = y_d1 / np.max(y_d1)
    y_d2 = np.array(y_d2)
    y_d2 = y_d2 / np.max(y_d2)

    y_d4 = np.arange(-2.5, 17, 0.1)
    x_d4 = np.ones(y_d4.shape) * 0.5

    set_by_def()
    f, ax = plt.subplots()
    ax.plot(x, y, linestyle='-.', color='black', linewidth=1, label="Кривая Гаусса")
    ax.plot(x, y_d1, color='black', linestyle='--', linewidth=1, label="Первая производная")
    ax.plot(x, y_d2, color='black', linestyle='-', linewidth=1, label="Вторая производная")
    ax.plot(x, y_d3, color='black', linewidth=1)
    ax.plot(x_d4, y_d4, color='black', linewidth=1)

    ax.set_ybound(lower=-2.5, upper=16)
    ax.set_xbound(lower=0, upper=1)

    extraticks = [0.5, ]
    ax.set_xticks(list(ax.get_xticks()) + extraticks)

    # ax.annotate(
    #     'Кривая Гаусса',
    #     xy=(0.42, 11.1), xycoords='data',
    #     xytext=(0.08, 14),
    #     arrowprops=dict(arrowstyle="-|>", fc="black"),
    #     bbox=dict(boxstyle="square,pad=0.3",
    #               fc="w", ec="black", lw=1)
    # )
    ax.legend(**Const.LEGEND)

    ax.set_xlabel(r"$X$")
    ax.set_ylabel(r"$Y$")

    save('5')
    plt.show()


def fig_4():
    x, y = read_data("plot-data_4.csv")

    x = 1 - x
    y = 1 - y

    set_by_def()
    f, ax = plt.subplots()
    ax.plot(x, y, linestyle='', color='black', mfc='#000000', mec='#000000', linewidth=1, alpha=0.5,
            marker='.', label="Jcyj")

    ax.set_ybound(lower=0.1, upper=0.9)

    # ax.set_xlabel(r"$X$")
    # ax.set_ylabel(r"$Y$")

    save('4_2')

    plt.show()

def fig_5():
    from main_0 import diff
    from main_0 import diff2

    x, y = read_data("plot-data_5.csv")
    (_, y_d1) = diff2(x, y)

    set_by_def()
    f, ax = plt.subplots()

    ax.plot(x, y, linestyle='', color='black', mfc='black', mec='black', linewidth=1, alpha=0.5,
            marker='.', label="Данные")
    ax.plot(x, y_d1, linestyle='-', color='black', mfc='black', mec='black', linewidth=1, alpha=0.5,
            marker='', label="2-я производная")

    # ax.set_ybound(lower=0.1, upper=0.9)

    # ax.set_xlabel(r"$X$")
    # ax.set_ylabel(r"$Y$")

    # save('5')

    plt.show()

if __name__ == '__main__':
    fig_5()
