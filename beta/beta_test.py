import unittest
from beta import *

class my_test(unittest.TestCase):
	def test_growth_rate_gm(self):
		self.assertAlmostEqual(div_growth_rateGm(62858, 315000, 6158), 18.0)


