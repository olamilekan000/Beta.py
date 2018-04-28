import math

def cost_of_equity(d, Mv):
	"""
	It calculates the cost of capital or equity shareholder required
	rate of return for an investment in which dividend is expected to be paid 
	
	d = Constant dividend per share	
	Mv = ex-dividend share price 
	"""
	try:
		ke = d/Mv
		return ke
	except Exception as e:
		raise e

		