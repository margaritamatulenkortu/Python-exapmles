import unittest
import math
from math import pi
from circle import circle
class TestCircleArea(unittest.TestCase):
    def test_area(self):
        #Test area radiuss is > 0
        self.assertAlmostEqual(circle(1), pi)
        self.assertAlmostEqual(circle(0), 0)
        self.assertAlmostEqual(circle(2.1), pi)
