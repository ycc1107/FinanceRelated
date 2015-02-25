class Equity(object):
	#assetPrice = None, strike = None, expired = None, vol = None, noSteps = 10, interest = 0
	def __init__(self,price = None,volatility = None):
		self.price = price
		self.volatility = volatility

	def setValueToEquity(self,price,volatility):
		self.price = price
		self.volatility = volatility



