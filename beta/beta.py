import math

def cost_of_equitycumdiv(d, Mv):
	"""
	Calculates the cost of capital or equity shareholder required rate of 
	return for an investment in which dividend is expected to remain constant forever
	(dividend is about to be paid)
	Arguments
	-------------------------------------------------------------------------
	d = dividend per share	
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
	return for an investment in which dividend is expected to remain constant forever
	(dividend has just been paid)
	Arguments
	------------------------------------------------------------------------  
	Mv = ex-dividend share price 
	"""
	try:
		ke = d/Mv
		return ke
	except Exception as e:
		raise e


def cost_of_equity_growth(div, Mv, g):
	"""
	Calculates the cost of capital or equity shareholder required rate of 
	return for an investment in which dividend is expected to grow  at a constant growth rate
	(dividend is about to be paid)

	Arguments
	-------------------------------------------------------------------------
	d = dividend per share.	
	Mv = ex-dividend share price. 
	g = growth rate.

	"""
	Mv = Mv - div
	try:
		ke = (div * (1 + g)/Mv) + g
		return round(ke, 4)
	except Exception as e:
		raise e


def div_growth_rate(t, dt, d0):
	"""
	Calculates the growth rate of a dividend using the dividend growth rate
	valuation model.
	
	Arguments
	-------------------------------------------------------------------------
	t = time
	dt = current price of dividend
	d0 = price of dividend t years ago

	"""
	try:
		growth_rate = (((dt/d0) ** (1/t)) - 1) * 100
		return round(growth_rate, 4)
	except Exception as e:
		return e


def div_growth_rateYr(t, dt, d0):
	"""
	Calculates the growth rate of a dividend using the dividend growth rate
	valuation model where dividend is paid yearly.
	
	Arguments
	-------------------------------------------------------------------------
	t = time
	dt = current price of dividend
	d0 = base year dividend price

	"""	
	try:
		t = t - 1
		growth_rate = (((dt/d0) ** (1/t)) - 1) * 100
		return round(growth_rate, 4)
	except Exception as e:
		raise e


def div_growth_rateGm(curr_earn, cap_emp, dt):
	"""
	Calculates the growth rate of a dividend using the dividend growth rate
	valuation model where dividend is paid yearly.
	
	Arguments
	-------------------------------------------------------------------------
	curr_earn = current earnings 
	cap_emp = capital employed
	dt = current dividend

	"""	
	try:
		roi = curr_earn/cap_emp
		b = (curr_earn - dt)/curr_earn 
		g = (roi * b) * 100
		return g
	except Exception as e:
		raise e