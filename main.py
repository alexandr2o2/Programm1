# Скрипт для вычисления центроиды функции
#!TODO: Интерполяцию данных
#!TODO: Дебаг метода пяти каналов при поиске многих цендроид
#!TODO: Убрать ненкжные списки из 2 методов для поиска центроид

import data

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
    yMs = maxFind(y)
    centroid_x = []
    for yM in yMs:
        centroid = x[yM]+(y[yM+1]*(y[yM]-y[yM-2])-y[yM-1]*(y[yM]-y[yM+2]))/\
                     (y[yM+1]*(y[yM]-y[yM-2])+y[yM-1]*(y[yM]-y[yM+2]))
        centroid_x.append(centroid)
    return centroid_x

def firstMoment(x,y):
    def sumOfProd(x,y):
        xy = 0;
        for i in range(len(x)):
            xy += x[i]*y[i]
        return xy

    centroid_x = []

    centroid_x = sumOfProd(x,y)/sum(y)
    return centroid_x

def findCentroids(x,y):
    x1, y1 = diff2(x, y)
    def edgePoints (x,y):
        i = []
        for val in y1:
            if val < 0:
                i.append(y1.index(val))
        l = []
        l.append(i[0])
        for j in range(0, len(i)-1):
            if i[j+1] != i[j]+1:
                l.append(i[j])
                l.append(i[j+1])
        l.append(i[-1])
        return l
    l = edgePoints(x1,y1)

    centroidsByFive = []
    centroidsByFirst = []

    for i in range(0,len(l),2):
        a = l[i]
        b = l[i+1]
        x_p = [x[k] for k in range(a,b)]
        y_p = [y[k] for k in range(a,b)]
        centroidsByFive.append(fiveChennels(list(x_p),list(y_p)))
        centroidsByFirst.append(firstMoment(list(x_p),list(y_p)))

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
    x, y = axesSplit(data.data1)
    x1, x2 = findCentroids(x,y)
    print("Метод пяти каналов")
    print(x1)
    print("Метод пяти каналов")
    print(x2)

    
if __name__ == '__main__':
    main()
