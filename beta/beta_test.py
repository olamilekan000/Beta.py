import unittest
from beta import *

class my_test(unittest.TestCase):
	def test_growth_rate_gm(self):
		self.assertAlmostEqual(div_growth_rateGm(62858, 315000, 6158), 18.0)


	def test_cost_of_equitycumdiv(self):
		self.assertAlmostEqual(cost_of_equitycumdiv(),)

	def test_cost_of_equity_exdiv(self):
		self.assertAlmostEqual(cost_of_equity_exdiv(), )

	def test_cost_of_equity_growth(self):
		self.assertAlmostEqual(cost_of_equity_growth(), )

	def test_div_growth_rate(self):
		self.assertAlmostEqual(div_growth_rate(),)

	def test_div_growth_rateYr(self):
		self.assertAlmostEqual(div_growth_rateYr(),)