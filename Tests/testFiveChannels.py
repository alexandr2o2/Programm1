import unittest
import dataPack
import data
import peakSearching

class TestFiveChannels(unittest.TestCase):
    def setUp(self) -> None:
        self.d1 = dataPack.Data(data.data1)
        self.d2 = dataPack.Data(data.data2)
        self.d3 = dataPack.Data(data.data3)
        self.d4 = dataPack.Data(data.data4)
        self.d5 = dataPack.Data(data.data5)
        self.d6 = dataPack.Data(data.data6)
        self.d7 = dataPack.Data(data.data7)



    def test1(self):
        """
        Тест на одиночный пик с центроидой 100
        """
        self.assertEqual(peakSearching.fiveChennels(self.d1.x, self.d1.y), 100)

        self.assertEqual(peakSearching.fiveChennels(self.d1.x, self.d1.y), 100)
        self.assertEqual(peakSearching.fiveChennels(self.d1.x, self.d1.y), 100)
        self.assertEqual(peakSearching.fiveChennels(self.d1.x, self.d1.y), 100)

    def tearDown(self) -> None:
        pass