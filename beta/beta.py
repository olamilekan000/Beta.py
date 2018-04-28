import math

def cost_of_equitycumdiv(d, Mv):
	"""
	Calculates the cost of capital or equity shareholder required rate of 
	return for an investment in which dividend is expected to be paid forever
	(dividend is about to be paid)
	Arguments
	-------------------------------------------------------------------------
	d = Constant dividend per share	
	Mv = cum-dividend share price 
	"""
	Mv = Mv - d
	try:
		ke = d/Mv
		return round(ke, 4)
	except Exception as e:
		raise e

def cost_of_equity_exdiv(d, Mv):
	"""
	Calculates the cost of capital or equity shareholder required rate of 
	return for an investment in which dividend is expected to be paid forever
	(dividend has just been paid)
	Arguments
	-------------------------------------------------------------------------
	d = Constant dividend per share	
	Mv = ex-dividend share price 
	"""
	try:
		ke = d/Mv
		return ke
	except Exception as e:
		raise e

		