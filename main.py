# Скрипт для вычисления центроиды функции

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
                 (yAll[y_Max+1]*(yAll[y_Max]-yAll[y_Max-2])-yAll[y_Max-1]*(yAll[y_Max]-yAll[y_Max+2]))
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
    d = data.data
    print("Метод первых моментов")
    print(firstMoment(d))
    print("Метод пяти каналов")
    print(firstMoment(d))

if __name__ == '__main__':
    main()
