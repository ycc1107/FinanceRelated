from binomialMethod import binomialMethod
from derivative import EquityOption


engineDict = {'binomialMethodEngine' : binomialMethod}

def Engine(method = 'binomialMethodEngine',asset = EquityOption()):
	for i in range(50,100):
		asset = EquityOption(100,20,90,0.35,i)
		price = engineDict[method](asset)
		print(price)

	


if __name__ == "__main__":
	Engine()