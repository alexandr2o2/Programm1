# Скрипт для вычисления центроиды функции
#!TODO: Интерполяцию данных
#!TODO: Дебаг метода пяти каналов при поиске многих цендроид
#!TODO: Убрать ненкжные списки из 2 методов для поиска центроид
#!TODO: Создать отдельную библиотеку для кода

import data
from scipy import signal
import math


def join(x:list, y:list):
    l = []
    for i in range(len(x)):
        l.append((x[i],y[i]))
    return tuple(l)

def savitzky_Golay_filter(data):
    """Фильтр Савицкого-Голея"""
    x,y = axesSplit(data)
    filted_y = signal.savgol_filter(y,80,2)
    return x, filted_y


def hight_filter(data):
    """Фильтр высоких частот"""
    b, a = signal.butter(8,0.1,'lowpass')
    x,y = axesSplit(data)
    filted_y = signal.filtfilt(b,a,y)
    return x, filted_y


def axesSplit(data):
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


def maxFind(y):
    x_max = []
    for i in range(1,len(y)-2):
        if y[i-1] < y[i]:
            if y[i+1] < y[i]:
                x_max.append(i)
    return x_max


def fiveChennels(x,y):
    #yM = y.index(max(y))
    yM = 2
    centroid = x[yM]+(y[yM+1]*(y[yM]-y[yM-2])-y[yM-1]*(y[yM]-y[yM+2]))/(y[yM+1]*(y[yM]-y[yM-2])+y[yM-1]*(y[yM]-y[yM+2]))
    return centroid


def firstMoment(x,y):
    def sumOfProd(x,y):
        xy = 0;
        for i in range(len(x)):
            xy += x[i]*y[i]
        return xy
    centroid = sumOfProd(x,y)/sum(y)
    return centroid

def findCentroids(x,y,a):
    x1, y1 = diff2(x, y)
    def edgePoints (x,y):
        ind = []
        for i in range(len(y1)):
            if (y1[i] < 0 and math.fabs(y1[i]) > a*max(y1)):
                ind.append(i)
        #print(ind)
        l = []
        l.append(ind[0])
        for j in range(0, len(ind)-1):
            if ind[j+1] != ind[j]+1:
                l.append(ind[j])
                l.append(ind[j+1])
        l.append(ind[-1])
        return l
    l = edgePoints(x1,y1)
    #print(l)

    centroidsByFive = []
    centroidsByFirst = []

    for i in range(0,len(l),2):
        a = l[i]
        b = l[i+1]
        #print("Начальные значения a,b: "+str(a)+" "+str(b) )

        x_p = [x[k] for k in range(a,b+1)]
        y_p = [y[k] for k in range(a,b+1)]
        centroidsByFirst.append(firstMoment(list(x_p), list(y_p)))

        if (a == b) and (a >= 5):
            a = a - 2
            b = b + 2
        elif (abs(b-a+1) < 5) :
            a = a - int(abs(5 - (b - a) + 1) / 2)
            b = b + int(abs(5 - (b - a) + 1) / 2)
       #print(a,b)

        x_p = [x[k] for k in range(a,b+1)]
        y_p = [y[k] for k in range(a,b+1)]
        #print(x_p)
        #print(y_p)
        centroidsByFive.append(fiveChennels(list(x_p),list(y_p)))


    return centroidsByFive, centroidsByFirst


def main():
    # d = []
    # d.append(data.data1)
    # d.append(data.data2)
    # d.append(data.data3)
    # d.append(data.data4)
    # d.append(data.data5)
    # k=1
    #
    # for i in d:
    #     x,y = axesSplit(i)
    #     print("Данные № " + str(k))
    #     print("Метод первых моментов")
    #     print(firstMoment(x,y))
    #     print("Метод пяти каналов")
    #     print(fiveChennels(x,y))
    #     k+=1
    x, y = axesSplit(data.data9)
    x1, x2 = findCentroids(x,y)
    print("Метод пяти каналов")
    print(x1)
    print("Метод первых моментов")
    print(x2)

    
if __name__ == '__main__':
    main()
