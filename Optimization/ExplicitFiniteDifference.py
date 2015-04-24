import math
import numpy as np
import matplotlib.pyplot as plt
from random import gauss as gs

class ExplicitFiniteDifference():  
    def __init__(self,intrate,payoff,vol,etype,strike,nas = 40,expn = 1):
        payoffFlag = {'p':-1,'c':1}
        self.dummy ,self.price,self.vOld,self.vNew = np.array([[0.0]*nas]*2),np.array([0.0]*nas),np.array([0.0]*nas),np.array([0.0]*nas)
        self.ds = 2.0 * strike / nas
        self.dt = 0.9/((vol**2)*(nas**2))
        self.nts = int(expn / self.dt) + 2
        self.nas = nas 
        self.strike = strike
        self.payoff = payoffFlag[payoff]
        self.intrate = intrate
        self.vol = vol
        self.etype = etype

    def plot(self):
        location = {1:'upper left',-1:'upper right'}[self.payoff]
        plt.plot(self.optionPrice)
        plt.plot(self.dummy[1])
        plt.ylim([-0.2,1.1])
        plt.legend(['Option','Payoff'],loc = location)
        plt.show()    

    def getPayoff(self):
        func = lambda x : 1 if x > 0 else 0
        for i in range(self.nas):
            self.price[i] = i * self.ds 
            self.dummy[0][i] = i * self.ds 
            self.vOld[i] = max( func(self.payoff*(self.price[i] - self.strike)),0)
            self.dummy[1][i] = max(func(self.payoff*(self.price[i] - self.strike)),0)
        

    def calculate(self):
        self.getPayoff()
        for i in range(self.nts):
            for j in range(1,self.nas - 1):
                delta = (self.vOld[j + 1] - self.vOld[j - 1]) / (2.0 * self.ds)
                gamma = 1.0*(self.vOld[j + 1] -2*self.vOld[j] + self.vOld[j-1]) /self.ds**2
                theta = -0.5 * (self.vol*self.price[j])**2 * gamma - self.intrate*(self.price[j]*delta -self.vOld[j])
                self.vNew[j] = self.vOld[j] - theta*self.dt*1.0
            self.vNew[0] = (1- self.intrate * self.dt)*self.vOld[0] 
            self.vNew[self.nas-1] = 2 * self.vOld[self.nas -2] -self.vOld[self.nas - 3]
            self.vOld = np.array(self.vNew)

            if self.etype == 'y':
                func = lambda x,y : x if x > y else y
                self.vOld = np.array([func(self.vOld[i],self.dummy[1][i]) for i in range(self.nas)])

        self.optionPrice  = np.array(self.vOld[:])
        res = 0 
        index = np.where( self.strike == self.dummy[0])
        print(index[0])
        index = index[0][0] if len(index[0]) == 1 else -1
        return  (index,self.optionPrice[index])
        self.plot()         
