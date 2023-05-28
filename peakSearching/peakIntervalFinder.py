import math
import numdifftools as nd
import numpy as np
from findiff import FinDiff
from scipy.misc import derivative
import matplotlib.pyplot as plt


class PeakIntervalFinder:

    @staticmethod
    def find_peak_interval(data, sens=0.1):
        def by_points(list):
            l = []
            start_point = list[0]
            stop_point = None
            for i in range(len(list) - 1):
                if list[i + 1] - list[i] > 1:
                    stop_point = list[i]
                    l.append((start_point, stop_point))
                    start_point = list[i + 1]
            if stop_point is None:
                stop_point = list[-1]
                l.append((start_point, stop_point))
            return l

        def axes(d):
            _y = [i[1] for i in d]
            _x = [i[0] for i in d]
            return _x, _y

        x, y = axes(data)
        # print(x)
        # print(y)
        dx = x[1] - x[0]

        y = np.array(y)
        y = y.astype('float64')

        d_dx = FinDiff(0, dx)
        diff_data = d_dx(d_dx(y))
        # print(diff_data)

        print(diff_data)
        a = np.max(diff_data)*sens
        print(np.max(diff_data))
        print("a = " + str(a))

        y_less = np.where(diff_data < a)  # значение производной меньше задонного числа
        print(y_less)
        out = by_points(y_less[0].tolist())
        return out, diff_data

    # ToDo: Переписать с использованием from scipy.misc import derivative

    @staticmethod
    def diff2(data):
        def axes(d):
            _y = [i[1] for i in d]
            _x = [i[0] for i in d]
            return _x, _y

        x, y = axes(data)
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

    @staticmethod
    def edgePoints(x, y, a):
        x1, y1 = PeakIntervalFinder.diff2(x, y)
        ind = []
        for i in range(len(y1)):
            if (y1[i] < 0 and math.fabs(y1[i]) > a * max(y1)):
                ind.append(i)
        # print(ind)
        l = []
        l.append(ind[0])
        for j in range(0, len(ind) - 1):
            if ind[j + 1] != ind[j] + 1:
                l.append(ind[j])
                l.append(ind[j + 1])
        l.append(ind[-1])
        return l


if __name__ == '__main__':
    from data import data_real

    PeakIntervalFinder.find_peak_interval(data_real)
    PeakIntervalFinder.diff2(data_real)
