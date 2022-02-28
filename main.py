# Скрипт для вычисления центроиды функции
#!TODO: Интерполяию данных
#!TODO: Расширить на несколько пиков

import data


def fiveChennels(data):
    yAll = [i[1] for i in data]
    y_Max = yAll.index(max(yAll))
    """ Для данных со множеством пиков
    idexlist_max = []
    for i in range(1,len(data)-2):
        if data[i + 1][1] > data[i][1] > data[i - 1][1]:
            idexlist_max.append(i)
    """
    centroid_x = data[y_Max][0]+(yAll[y_Max+1]*(yAll[y_Max]-yAll[y_Max-2])-yAll[y_Max-1]*(yAll[y_Max]-yAll[y_Max+2]))/\
                 (yAll[y_Max+1]*(yAll[y_Max]-yAll[y_Max-2])+yAll[y_Max-1]*(yAll[y_Max]-yAll[y_Max+2]))
    return centroid_x



def firstMoment(data):
    def sumOfProd(data):
        xy =0;
        for dot in data:
            xy+= dot[0]*dot[1]
        return xy


    yAll = [i[1] for i in data]

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
