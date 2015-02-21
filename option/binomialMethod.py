import math,sys

class ParameterNotSetError(Exception):
	def __init__(self,value):
		self.value = value
	def __str__(self):
		return repr(self.value)

def payoffFunc(s,k):
	return 0 if s < k else s - k

def binomialMethod(assetPrice = None, strike = None, expired = None, vol = None, noSteps = 10, interest = 0):
	'''
	Author: Cheng Yan
	This is binomial method to price option

	parameters: 
	under asset price, interest rate, strike price, expired days, number of steps

	default sitting:
	steps is 10, interest rate is 0
	'''
	if not (assetPrice and strike and expired and vol):
		# need to add more detail, raise name of missing value 
		raise ParameterNotSetError('missing value')
		sys.exit(1)

	priceLst = [0] * noSteps 	
	timeStep = expired / float(noSteps)
	
	discountFactor = math.exp(-interest * timeStep)
    	temp = 0.5 * (discountFactor + math.exp((interest + vol ** 2) * timeStep) )

	up = temp + math.sqrt(temp ** 2 - 1)
	down = 1.0 / up
	p = math.exp((interest * timeStep) - down) / (up - down)
	print(p,up,down)
	priceLst[0] = assetPrice
	for i in range(1,noSteps):
		for j in range(i,0,-1):
			priceLst[j] = up * priceLst[j-1]
		priceLst[0] = down * priceLst[0]

	optionLst =  [ payoffFunc(priceLst[i],strike) for i in range(noSteps)]

	for i in range(noSteps,1,-1):
		for j in range(i - 1):
			optionLst[j] = (p * optionLst[j+1] +(1 - p) * optionLst[j]) * discountFactor

	return optionLst[0]	

if __name__ == "__main__":
	print(binomialMethod.__doc__)
