# Скрипт для вычисления центроиды функции
#!TODO: Интерполяцию данных
#!TODO: Расширить на несколько пиков

import data

def maxFind(data):
    y = [i[1] for i in data]
    x_max = []
    for i in range(1,len(y)-2):
        if y[i-1] < y[i]:
            if y[i+1] < y[i]:
                x_max.append(i)
    return x_max



def fiveChennels(data):
    y = [i[1] for i in data]
    yMs = maxFind(data)
    centroid_x = []
    for yM in yMs:
        centroid = data[yM][0]+(y[yM+1]*(y[yM]-y[yM-2])-y[yM-1]*(y[yM]-y[yM+2]))/\
                     (y[yM+1]*(y[yM]-y[yM-2])+y[yM-1]*(y[yM]-y[yM+2]))
        centroid_x.append(centroid)
    return centroid_x

def firstMoment(data):
    def sumOfProd(data):
        xy = 0;
        for dot in data:
            xy+= dot[0]*dot[1]
        return xy
    yAll = [i[1] for i in data]

    centroid_x = []

    centroid_x = sumOfProd(data)/sum(yAll)
    return centroid_x


def main():
    d = []
    d.append(data.data1)
    d.append(data.data2)
    d.append(data.data3)
    d.append(data.data4)
    d.append(data.data5)
    k=1

    for i in d:
        print("Данные № " + str(k))
        print("Метод первых моментов")
        print(firstMoment(i))
        print("Метод пяти каналов")
        print(fiveChennels(i))
        k+=1

    
if __name__ == '__main__':
    main()
