from unittest import TestCase
import numpy as np
import main


class Test(TestCase):
    def test_find_centroids(self):
        h = 10 / np.sqrt(2 * np.pi)
        d = 100
        c = 2500
        x_dots = list(range(0, 4016, 1))
        y_dots = [h * np.exp(-(np.square((x - c) / d)) / 2) for x in x_dots]
        c1, c2 = main.findCentroids(x_dots, y_dots)
        self.assertEqual(c, c1)
        self.assertEqual(c, c2)
