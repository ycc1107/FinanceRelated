import math,sys

class ParameterNotSetError(Exception):
	def __init__(self,value):
		self.value = value
	def __str__(self):
		return repr(self.value)


def payoffFunc(s,k):
	return 0 if s < k else s - k

def binomialMethod(underlyingAsset):
	'''
	Author: Cheng Yan
	This is binomial method to price option

	parameters: 
	self,strik = None,expiredDays = None, price = None,volatility = None , noSteps = 10

	'''
	# need to add more detail, raise name of missing value 
	for var in vars(underlyingAsset):
		varLst, exitFlag = [], False
		print(var,vars(underlyingAsset)[var])
		if vars(underlyingAsset)[var] == None:
			varLst.append(var)
			exitFlag =True
		if exitFlag:
			raise ParameterNotSetError("The parameter(s) {} can not be empty".format((varLst)))
			sys.exit(1)

	priceLst = [0] * underlyingAsset.noSteps 	
	timeStep = underlyingAsset.expiredDays / float(underlyingAsset.noSteps)
	
	discountFactor = math.exp(-underlyingAsset.interest * timeStep)
	temp = 0.5 * (discountFactor + math.exp((underlyingAsset.interest + underlyingAsset.volatility ** 2) * timeStep))

	up = temp + math.sqrt(temp ** 2 - 1)
	down = 1.0 / up
	p = math.exp((underlyingAsset.interest * timeStep) - down) / (up - down)
	priceLst[0] = underlyingAsset.price
	for i in range(1,underlyingAsset.noSteps):
		for j in range(i,0,-1):
			priceLst[j] = up * priceLst[j-1]
		priceLst[0] = down * priceLst[0]

	optionLst =  [ payoffFunc(priceLst[i],underlyingAsset.strike) for i in range(underlyingAsset.noSteps)]

	for i in range(underlyingAsset.noSteps,1,-1):
		for j in range(i - 1):
			optionLst[j] = (p * optionLst[j+1] +(1 - p) * optionLst[j]) * discountFactor

	return optionLst[0]	

if __name__ == "__main__":
	print(binomialMethod.__doc__)