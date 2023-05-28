class Data:
    """A class with information about the data. Contains write, check, transform methods"""

    def __init__(self, data):
        Data.dataValidType(self, data)
        Data.dataValueSameLength(self)
        Data.dataValidDem(self, data)
        Data.dataValidSign(self, data)
        self.data = data
        self.x, self.y = self.dataToTwoList()


    @staticmethod
    def dataValidType(self, data):
        if not isinstance(data, (list, tuple)):
            raise ValueError("Wrong data input type")

    @staticmethod
    def dataValidDem(self, data):
        try:
            data[0][0]
        except TypeError:
            raise ValueError("Wrong data input array dimension")

    @staticmethod
    def dataValidSign(self, data):
        for l1 in data:
            for l2 in l1:
                if l2 < 0:
                    raise ValueError("Invalid data, value less than 0")

    def dataValueSameLength(self):
        if len(self.x) != len(self.y):
            raise ValueError("Invalid data point with no value")

    def dataToTwoList(self):
        y = [i[1] for i in self.data]
        x = [i[0] for i in self.data]
        return x, y
