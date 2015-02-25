from stockUnderlying import Equity

class EquityOption(Equity):
	def __init__(self,strike = None,expiredDays = None, price = None,volatility = None , noSteps = 10, interest = 0):
		self.strike = strike
		self.expiredDays = expiredDays
		self.noSteps = noSteps
		self.interest = interest
		super(EquityOption,self).setValueToEquity(price,volatility)

