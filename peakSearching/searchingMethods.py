def fiveChennel(x, y):
    yM = y.index(max(y))
    centroid = x[yM] + (y[yM + 1] * (y[yM] - y[yM - 2]) - y[yM - 1] * (y[yM] - y[yM + 2])) / (
                y[yM + 1] * (y[yM] - y[yM - 2]) + y[yM - 1] * (y[yM] - y[yM + 2]))
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
