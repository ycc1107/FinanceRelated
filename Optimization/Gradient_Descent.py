import numpy as np 
import random

class objectType():
    def __init__(self,n,bias,variance):
        self.numPoints = n
        self.bias = bias
        self.variance = variance

    def generateObject(self):
        self.x = np.zeros(shape = (self.numPoints,2))
        self.y = np.zeros(shape = self.numPoints)
        self.genData()
        self.size,n = np.shape(self.x)
        self.theta = np.ones(n)
        self.alpha = 0.0005
        self.m = self.numPoints
    def genData(self):
        for i in range(self.numPoints):
            self.x[i][0] = 1
            self.x[i][1] = i
            self.y[i] = (i+self.bias) + random.uniform(0,1)*self.variance



def gradientDescent(obj,numIterations = 10000):
    xTrans = obj.x.transpose()
    for i in range(numIterations):
        hypothesis = np.dot(obj.x,obj.theta)
        loss = hypothesis - obj.y
        cost = np.sum(loss**2) / (2*obj.size)
        print("Iteration %d | Cost %f" %(i,cost))
        gradient = np.dot(xTrans,loss)/obj.size
        obj.theta = obj.theta - obj.alpha * gradient
    return obj.theta 

def main():
    obj = objectType(100,25,10)
    obj.generateObject()
    theta = gradientDescent(obj)
    print(theta)

	
	


if __name__ == "__main__":main()
