import unittest
from beta import beta

class my_test(unittest.TestCase):
	def test_capm(self):
		self.assertAlmostEqual(beta.capm(0.07, 1.2, 0.10), 0.106)
	def test_growth_rate_gm(self):
		self.assertAlmostEqual(beta.div_growth_rateGm(62858, 315000, 6158), 18.0)	