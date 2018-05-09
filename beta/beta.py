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
	ke = d/Mv
	return round(ke, 4)
	
	
def cost_of_equity_exdiv(d, Mv):
	"""
	Calculates the cost of capital or equity shareholder required rate of 
	return for an investment in which dividend is expected to remain constant forever
	(dividend has just been paid)
	Arguments
	------------------------------------------------------------------------  
	Mv = ex-dividend share price 
	"""
	ke = d/Mv
	return round(ke, 4)


def cost_of_equity_growth(div, Mv, g):
	"""
	Calculates the cost of capital or equity shareholder required rate of 
	return for an investment in which dividend is expected to grow  at a 
	constant growth rate (dividend is about to be paid)

	Arguments
	-------------------------------------------------------------------------
	d = dividend per share.	
	Mv = ex-dividend share price. 
	g = growth rate.

	"""
	Mv = Mv - div
	ke = (div * (1 + g)/Mv) + g
	return round(ke, 4)
	

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
	growth_rate = (((dt/d0) ** (1/t)) - 1) * 100
	return round(growth_rate, 4)
	

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
	t = t - 1
	growth_rate = (((dt/d0) ** (1/t)) - 1) * 100
	return round(growth_rate, 4)
	

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
	roi = curr_earn/cap_emp
	b = (curr_earn - dt)/curr_earn 
	g = (roi * b) * 100
	return round(g, 4)

def capm(rf, beta, rm):
    """
    calculate the minimum rate of return using CAPM 
    (Capital Asset Pricing Model).

    parameters:
    -----------
    rf: The risk free rate of retun.
    beta: The company's beta factor which measures the sensitivity
        of an investment return to market movement
    rm: market rate of return

    Notes.
    ------
    The CAPM is an alternative method of calculating cost of equity
    capital for an investment. it is made up of two sides; Risk free
    rate i.e. the basic rate which all projects must earn if 
    it is completely free from risk. and the Risk Premium which
    is gotten after applying the project
    beta to the difference between market return and risk rate of return.

    Example:
    --------
    XYZ limited wants to determine its minimum required rate of return if 
    the risk free rate is 7%, market rate of return is 10% and the company
    has a beta factor of 12.

        Solution
        --------
        rf = 0.07, beta = 12, rm = 0.10
        
        min.required rate of return = 0.07 + 1.2(0.10 - 0.07) = .106 i.e. 10.6%

    """
    
    if rf >= 1 or rm >= 1:
        return "values cannot be greater than or equals 1"
    else:
        ke = rf + beta * (rm - rf)
        return round(ke, 4)

def pv(rate, n, fv):
    """
    Calaculates the present value of a cashflow 
    
    parameters:
    -----------
    rate: The rate of return of the investment.
    n: The lifespan of the investment.
    fv: The future value of the investment.

    Example:
    --------
    """	