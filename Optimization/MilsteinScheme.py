class MilsteinScheme():
    def __init__(self,price,intrate,expn,step,vol,strike):
        self.price = price
        self.intrate = intrate
        self.expn = expn
        self.step = step
        self.tstep = 1.0/step
        self.vol = vol
        self.strike = strike

    def plot(self):
        for data in self.plotData:
            plt.plot(data)
        plt.show()

    def calculate(self):
        func = lambda x : 1 if x > 0 else 0
        res,counter,simNum = [],0,10000
        self.plotData = np.array([[0]*self.step]*10)
        for i in range(simNum):
            price = self.price
            for j in range(self.step):
                if counter < 10:
                    self.plotData[counter][j] = price
                z = gs(0,1)
                price = price*(1+self.intrate*self.tstep+self.vol*self.tstep**0.5*z) +0.5*self.vol**0.5*self.tstep*(z**2-1)
            res.append(func(price - self.strike)) 
            counter += 1
        discountedPrice = math.exp(-self.intrate*self.expn)*sum(res)/simNum
        
        return (discountedPrice)
        self.plot()
