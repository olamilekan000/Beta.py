import unittest
from beta import beta

class my_test(unittest.TestCase):
	def test_capm(self):
		self.assertAlmostEqual(beta.capm(0.07, 1.2, 0.10), 0.106)
	def test_growth_rate_gm(self):
		self.assertAlmostEqual(beta.div_growth_rateGm(62858, 315000, 6158), 18.0)
	def test_pv(self):
		self.assertAlmostEqual(beta.pv(0.08, 4, 300000), 220509)
	def test_roi(self):
		self.assertAlmostEqual(beta.roi(1000, 1200), 0.2)			