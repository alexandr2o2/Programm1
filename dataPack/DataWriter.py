import csv
import sys


class DataWriter:
    @staticmethod
    def readCSVData(dataPath):
        with open(dataPath, newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';', dialect=csv.excel)
            _data = []
            try:
                for row in csv_reader:
                    _data.append(tuple([row[0], row[1]]))
            except csv.Error as e:
                sys.exit('file {}, line {}: {}'.format(dataPath, csv_reader.line_num, e))
            return _data


if __name__ == "__main__":
    data = DataWriter.readCSVData(r"C:\Users\user\Desktop\Книга1.csv")
    print(data)
