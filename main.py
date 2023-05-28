import csv
import locale
import os

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.signal import correlate

from data import data_real
from data import data6

locale.setlocale(locale.LC_ALL, "ru_RU")


def read_data(name, path):
    pwd = os.getcwd()
    iPath = path
    os.chdir(iPath)
    x = []
    y = []
    y_en = []
    with open(name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            x.append(row[0])
            y.append(row[1])
            y_en.append(row[2])
    os.chdir(pwd)
    x = x[1:-1]
    y = y[1:-1]
    y_en = y_en[1:-1]
    return np.asarray(x, dtype=np.float64), np.asarray(y, dtype=np.float64), np.asarray(y_en, dtype=np.float64)


def write_csv(path: str, dataDict: list):
    """

    :param path: Путь до файла с названием
    :param dataDict: Список словарей данных
    :return: None
    """
    with open(path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=dataDict[0].keys(), dialect='excel')
        w.writeheader()
        for data in dataDict:
            w.writerow(data)


def find_ROI(x, y, h=0.01):
    temp = []
    start = 0
    stop = 0
    y = y / np.max(y)
    for i in range(0, len(y) - 1):
        # start - ныало диапозона, stop - конец диапозона
        print(y[i])
        if y[i] < h < y[i + 1]:
            start = i + 1
        if y[i] > h > y[i + 1]:
            stop = i + 1
        if start != 0 and stop != 0:
            temp.append([start, stop])
            start = 0
            stop = 0
    return temp


def find_FWHM(x, y):
    t = x
    x = np.arange(t[0], t[-1], 0.01)
    y = np.interp(x, t, y)
    print(x)
    print(y)
    bottom = y[0] + (y[-1] - y[0]) / 2
    height_half = (max(y) - bottom) / 2 + bottom
    # print(height_half)
    indexes = []
    for i, val in enumerate(y):
        if val > height_half:
            # print(str(val)+" and " + str(height_half))
            indexes.append(i)
    # print("Длинна: " + str(len(x)))
    # print(indexes)
    # print(len(indexes))
    if indexes[0] == 0:
        print("!!!Упс в find_FWHM ошибка из-за интервалов слево")
        indexes[0] = 1
    elif indexes[-1] == len(x) - 1:
        print("!!!Упс в find_FWHM ошибка из-за интервалов справо")
        indexes[-1] = len(x) - 2
    FWHM = ((x[indexes[-1] - 1] - x[indexes[0]]) + (x[indexes[-1]] - x[indexes[0] - 1])) / 2
    return FWHM


def find_area(x, y):
    bottom = y[0] + (y[-1] - y[0]) / 2
    return sum(y) - (x[0] - x[-1]) * bottom


def axes(d):
    y = [i[1] for i in d]
    x = [i[0] for i in d]
    return x, y


def graph_show(x, y, y_d=None):
    fig, ax = plt.subplots()
    if y_d is None:
        ax.plot(x, y)
        plt.show()
        return

    l = []
    for (a, b) in y_d:
        l.append(a)
        l.append(b)
    ax.vlines(l, 0, 1, transform=ax.get_xaxis_transform(), color='r')
    plt.show()


def graph_save(x, y, name: str):
    matplotlib.rcParams['font.family'] = "Times New Roman"
    fontsize = 12

    fig, ax = plt.subplots()

    ax.plot(x, y)

    plt.xlabel("Канал", fontsize=fontsize)
    plt.ylabel("Число отсчётов", fontsize=fontsize)

    # plt.show()
    plt.savefig(f"pictures\сем8\{name}.png", bbox_inches='tight')


def graph_save2(x, y, name: str, centroids):
    matplotlib.rcParams['font.family'] = "Times New Roman"
    fontsize = 12

    fig, ax = plt.subplots()

    ax.plot(x, y)

    plt.xlabel("Канал", fontsize=fontsize)
    plt.ylabel("Число отсчётов", fontsize=fontsize)
    ax.vlines([centroids[0]], 0, 1, transform=ax.get_xaxis_transform(), color='r')
    ax.vlines([centroids[1]], 0, 1, transform=ax.get_xaxis_transform(), color='b')
    ax.vlines([centroids[2]], 0, 1, transform=ax.get_xaxis_transform(), color='g')
    ax.vlines([centroids[3]], 0, 1, transform=ax.get_xaxis_transform(), color='black')

    ax.set_ylim([min(y) - 10, max(y) + 10])
    # plt.show()
    plt.savefig(f"pictures\сем8\{name}.png", bbox_inches='tight')


def graph_save3(x, y, name: str, rois):
    matplotlib.rcParams['font.family'] = "Times New Roman"
    fontsize = 12

    fig, ax = plt.subplots()

    ax.plot(x, y)

    plt.xlabel("Канал", fontsize=fontsize)
    plt.ylabel("Число отсчётов", fontsize=fontsize)
    for roi in rois:
        ax.vlines(roi, 0, 1, transform=ax.get_xaxis_transform(), color='g')
        ax.fill_between(x[roi[0]:roi[1]], y[roi[0]:roi[1]], color='green', alpha=0.5)
    ax.set_ylim([min(y) - 20, max(y) + 20])
    plt.show()
    plt.savefig(f"pictures\сем8\{name}.png", bbox_inches='tight')


def part1():
    x, y = axes(data_real)
    # graph_save(x, y, "Сложные спект")
    # graph_show(x, y)
    rois = [(478, 500), (563, 586), (586, 608),
            (661, 683), (684, 705), (705, 732),
            (986, 1004), (1418, 1460), (1604, 1630),
            (1833, 1856), (1853, 1877), (2264, 2299),
            (2597, 2631), (2704, 2735), (4485, 4527),
            (4694, 4727)]

    from main_0 import fiveChennels, firstMoment, correlMethod, derMethod

    data = []
    for i, (x1, x2) in enumerate(rois):
        x0 = x[x1:x2]
        y0 = y[x1:x2]
        # graph_show(x0, y0)

        l = []
        l.append(fiveChennels(x0, y0))
        l.append(firstMoment(x0, y0))
        l.append(correlMethod((x0, y0)))
        l.append(derMethod((x0, y0)))
        l.append(find_area(x0, y0))

        data.append(
            {"№ пика": i, "Метод пяти каналов": l[0],
             "Метод первых моментов": l[1], "Метод кореляции": l[2],
             "Метод производных": l[3], "Площадь пика:": l[4]}
        )

        print(f"******* ПИК {i} **********")
        print(f"Метод пяти каналов: " + str(l[0]))
        print(f"Метод первых моментов: " + str(l[1]))
        print(f"Метод кореляции: " + str(l[2]))
        print(f"Метод производных: " + str(l[3]))
        print(f"Площадь пика: " + str(l[4]))

        graph_save2(x0, y0, f"пик_{i}", centroids=l)

    write_csv(r"pictures\сем8\data.csv", data)

    rois = [(478, 500), (563, 586), (586, 608),
            (661, 683), (684, 705), (705, 732),
            (986, 1004), (1418, 1460), (1604, 1630),
            (1833, 1856), (1853, 1877), (2264, 2299),
            (2597, 2631), (2704, 2735), (4485, 4527),
            (4694, 4727)]

    data = []
    for i, (x1, x2) in enumerate(rois):
        x0 = x[x1:x2]
        y0 = y[x1:x2]
        graph_show(x0, y0)

        l = []
        l.append(fiveChennels(x0, y0))
        l.append(firstMoment(x0, y0))

        data.append(
            {"№ пика": i, "Метод кореляции": l[2],
             "Метод производных": l[3], "Площадь пика:": l[4]}
        )

        print(f"******* ПИК {i} **********")
        print(f"Метод пяти каналов: " + str(l[0]))
        print(f"Метод первых моментов: " + str(l[1]))
        print(f"Метод кореляции: " + str(l[2]))
        print(f"Метод производных: " + str(l[3]))
        print(f"Площадь пика: " + str(l[4]))

        graph_save2(x0, y0, f"пик_{i}_сложный", centroids=l)

    write_csv(r"pictures\сем8\data2.csv", data)


def part2():
    x, y = axes(data_real)
    # graph_save(x, y, "Сложные спект")
    # graph_show(x, y)
    rois = [(478, 500), (563, 586), (586, 608),
            (661, 683), (684, 705), (705, 732),
            (986, 1004), (1418, 1460), (1604, 1630),
            (1833, 1856), (1853, 1877), (2264, 2299),
            (2597, 2631), (2704, 2735), (4485, 4527),
            (4694, 4727)]

    graph_save3(x, y, "Сложный_с_roi", rois=rois)


def part3():
    x, y = axes(data_real)
    rois = [(4694, 4727), ]
    x = x[4694:4727]
    x = [xs - 4694 for xs in x]
    y = y[4694:4727]
    from curveFitting.fittingFunc import nonLinerSqAppr, gauss2, gauss1
    import numpy as np
    y = [np.interp(xs, x, y) for xs in np.arange(0, len(x), len(x) / 10)]
    x = list(np.arange(0, len(x), len(x) / 10))
    # h1, c1, d1, h2, c2, d2
    result = nonLinerSqAppr(gauss2, x, y, None, bounds=(0, [10000, 200, 200, 1000, 200, 200]))
    print(result)
    print(gauss2(4000, *result))
    y1 = [gauss1(xs, *result[0:3]) for xs in x]
    y2 = [gauss1(xs, *result[3:6]) for xs in x]
    print(y1)
    print(y2)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.plot(x, y1)
    ax.plot(x, y2)

    plt.xlabel("Канал", fontsize=12)
    plt.ylabel("Число отсчётов", fontsize=12)
    plt.show()


def part4():
    # x - Ox в каналах, x_en - Ox в кэВ, у - Oy значение отсчёта
    x, x_en, y = read_data(r"Европий_Германиевый датчик.csv", r"C:\Users\user\Desktop\ВКР\Материалы\Данные_спектров")
    # print(x)
    # print(y)
    # print(x_en)

    from main_0 import fiveChennels, firstMoment, correlMethod, derMethod, diff2
    from curveFitting.fittingFunc import nonLinerSqAppr, gauss2, gauss1

    tempx = np.arange(0, 1, 0.01)
    params = (15, 0.5, 0.1)
    tempy = gauss1(tempx, *params)

    y_cor = correlate(y, tempy, mode='same')
    _, y_d = diff2(x_en, y_cor)
    y_d = np.asarray(y_d, dtype=np.float64) * -1
    # print(y_d)

    rois = find_ROI(x_en, y_d, h=0.002)
    # print(rois)
    from main_0 import fiveChennels, firstMoment, correlMethod, derMethod

    datas = []
    for i, roi in enumerate(rois):
        data = {}
        print("*******")
        print(roi[0], roi[1], sep=',')
        data["№ пика"] = i + 1
        data["Начальный канал"] = x_en[roi[0]]
        data["Конечный канал"] = x_en[roi[1]]
        x_p = x[roi[0]:roi[1]]
        y_p = y[roi[0]:roi[1]]
        x_p_en = x_en[roi[0]:roi[1]]
        y_p = y[roi[0]:roi[1]]
        FWHM = find_FWHM(x_p_en, y_p)
        data["FWHM, каналов"] = FWHM
        FWHM = find_FWHM(x_p, y_p)
        print("FWHM: " + str(FWHM))
        data["Тип"] = "Одиночный"

        for j in range(0, i):
            _roi = rois[j]
            val = roi[0] - 3 * FWHM
            if val < _roi[0] or val < _roi[1]:
                print("Мультиплентный слева")
                print("Пересечение с " + str(_roi))
                data["Тип"] = "Мультиплетный"

        for j in range(i + 1, len(rois)):
            _roi = rois[j]
            val = roi[1] + 3 * FWHM
            if val > _roi[0] or val > _roi[1]:
                print("Мультиплентный справа")
                print("Пересечение с " + str(_roi))
                data["Тип"] = "Мультиплетный"

        data["Метод пяти каналов"] = fiveChennels(x_p_en, y_p)
        data["Метод первых моментов"] = firstMoment(x_p_en, y_p)
        data["Метод корреляции"] = correlMethod([x_p_en, y_p])
        data["Метод плоизводной"] = derMethod([x_p_en, y_p])
        data["Площадь"] = find_area(x_p_en, y_p)
        print(data)
        datas.append(data)

    write_csv(r"C:\Users\user\Desktop\ВКР\Материалы\Данные_спектров\Результаты.csv", datas)

    f, ax = plt.subplots()
    ax.plot(x_en, y / np.max(y), linestyle='-', color='black', linewidth=1, label="Не обработанные данные")
    # ax.plot(x_en, y_cor, linestyle='-', color='red', linewidth=1, label="Не обработанные данные")
    # ax.plot(x_en, y_cor, linestyle='-', color='red', linewidth=1, label="Не обработанные данные")
    ax.set_xlabel(r"$X$")
    ax.set_ylabel(r"$Y$")
    plt.show()


def part5():
    # x - Ox в каналах, x_en - Ox в кэВ, у - Oy значение отсчёта
    x, x_en, y = read_data(r"Европий_NaI.csv", r"C:\Users\user\Desktop\ВКР\Материалы\Данные_спектров")
    # print(x_en)
    # print(x)
    # print(y)

    from main_0 import fiveChennels, firstMoment, correlMethod, derMethod, diff2
    from curveFitting.fittingFunc import nonLinerSqAppr, gauss2, gauss1

    tempx = np.arange(0, 1, 0.01)
    params = (100, 0.5, 0.01)
    tempy = gauss1(tempx, *params)

    y_cor = correlate(y, tempy, mode='same')
    _, y_d = diff2(x_en, y_cor)
    y_d = np.asarray(y_d, dtype=np.float64) * -1
    # print(y_d)

    rois = find_ROI(x_en, y_d, h=0.02)
    print(rois)
    from main_0 import fiveChennels, firstMoment, correlMethod, derMethod

    datas = []
    for i, roi in enumerate(rois):
        data = {}
        print("*******")
        print(roi[0], roi[1], sep=',')
        data["№ пика"] = i + 1
        data["Начальный канал"] = x_en[roi[0]]
        data["Конечный канал"] = x_en[roi[1]]
        x_p = x[roi[0]:roi[1]]
        y_p = y[roi[0]:roi[1]]
        x_p_en = x_en[roi[0]:roi[1]]
        FWHM = find_FWHM(x_p_en, y_p)
        data["FWHM, каналов"] = FWHM
        FWHM = find_FWHM(x_p, y_p)
        print("FWHM: " + str(FWHM))
        data["Тип"] = "Одиночный"

        for j in range(0, i):
            _roi = rois[j]
            val = roi[0] - 3 * FWHM
            if val < _roi[0] or val < _roi[1]:
                print("Мультиплентный слева")
                print("Пересечение с " + str(_roi))
                data["Тип"] = "Мультиплетный"

        for j in range(i + 1, len(rois)):
            _roi = rois[j]
            val = roi[1] + 3 * FWHM
            if val > _roi[0] or val > _roi[1]:
                print("Мультиплентный справа")
                print("Пересечение с " + str(_roi))
                data["Тип"] = "Мультиплетный"

        data["Метод пяти каналов"] = fiveChennels(x_p_en, y_p)
        data["Метод первых моментов"] = firstMoment(x_p_en, y_p)
        data["Метод корреляции"] = correlMethod([x_p_en, y_p])
        data["Метод плоизводной"] = derMethod([x_p_en, y_p])
        data["Площадь"] = find_area(x_p_en, y_p)
        print(data)
        datas.append(data)

    write_csv(r"C:\Users\user\Desktop\ВКР\Материалы\Данные_спектров\Результаты_NaI.csv", datas)

    f, ax = plt.subplots()
    ax.plot(x, y / np.max(y), linestyle='-', color='black', linewidth=1, label="Не обработанные данные")
    ax.plot(x, y_d / np.max(y_d), linestyle='-', color='red', linewidth=1, label="Не обработанные данные")
    ax.plot(x, y_cor / np.max(y_cor), linestyle='-', color='green', linewidth=1, label="Не обработанные данные")
    ax.set_xlabel(r"$X$")
    ax.set_ylabel(r"$Y$")
    plt.show()

def data_do():
    a = -28.414
    b = 6.95
    with open(r"C:\Users\user\Desktop\ВКР\Материалы\Данные_спектров\Европий_NaI.txt") as f:
        datas = []
        for row in f:
            x0 = int(row.split(':')[0])
            print(x0)
            ys = row.split(':')[1].strip().split(' ')
            print(ys)
            for i, y in enumerate(ys):
                print(y)
                data = {"x": x0 + i - 1, "x_en": a + b*(x0 + i - 1), "y": int(y)}
                datas.append(data)
    write_csv(r"C:\Users\user\Desktop\ВКР\Материалы\Данные_спектров\Европий_NaI.csv", datas)



def main():
    # data = (x, y)
    # from peakSearching.peakIntervalFinder import PeakIntervalFinder
    # y_d, y_diff = PeakIntervalFinder.find_peak_interval(data_real)
    # print(y_d)
    # graph_show(x, y_diff, y_d)
    # graph_show(x, y, y_d)
    # fig, ax = plt.subplots()
    # ax.plot(x, y, x, y_diff)
    # plt.show()
    part5()


if __name__ == "__main__":
    main()
