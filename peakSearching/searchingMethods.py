def fiveChennels(x, y):
    yM = y.index(max(y))
    centroid = x[yM] + (y[yM + 1] * (y[yM] - y[yM - 2]) - y[yM - 1] * (y[yM] - y[yM + 2])) / (
                y[yM + 1] * (y[yM] - y[yM - 2]) + y[yM - 1] * (y[yM] - y[yM + 2]))
    return centroid
