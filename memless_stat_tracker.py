from random import random, randint
from math import sqrt

class variableStats():
    '''
    An object which keeps a record of the standard deviation
    and mean of all numbers passed through it, without holding
    past values in memory.
    '''

    def __init__(self, num = None, statType = "standard"):
        '''
        The stat type has three settings; standard, absolute, and signSplit.
        Standard computes the stats in the standard manner.
        Absolute computes the stats, taking all values as positive.
        SignSplit computes two separate stats for positive and negative
        values.
        '''
        self.statType = statType
        
        if num is not None:
            num = float(num)
            self.counter = 1
            
            if self.statType == "standard":
                self.sqrSum = num**2
                self.mean = num
                self.sd = 0
                
            elif self.statType == "absolute":
                self.sqrSum = num **2
                self.mean = abs(num)
                self.sd = 0
                
            elif self.statType == "signSplit":
                if num > 0:
                    self.posMean = num
                    self.negMean = None
                    self.posSqrSum = num **2
                    self.negSqrSum = None
                    self.posSd = 0
                    self.negSd = None
                    self.posCounter = 1
                    self.negCounter = 0

                    
                elif num < 0:
                    self.posMean = None
                    self.negMean = num
                    self.posSqrSum = None
                    self.negSqrSum = num **2
                    self.posSd = None
                    self.negSd = 0
                    self.negCounter = 1
                    self.posCounter = 0

                elif num == 0:
                    #Treat 0 as both positive and negative
                    self.posMean = num
                    self.posSqrSum = num **2
                    self.posSd = 0
                    self.posCounter = 1
                    self.negMean = num
                    self.negSqrSum = num **2
                    self.negSd = 0
                    self.negCounter = 1
                    
        #If num is None
        else:
            self.counter = 0
            self.sqrSum = None
            self.mean = None
            self.sd = None
            if self.statType == "signSplit":
                self.posMean = None
                self.negMean = None
                self.posSd = None
                self.negSd = None
                self.posSqrSum = None
                self.negSqrSum = None
                self.posCounter = 0
                self.negCounter = 0

            
    def calcAvg (self, ExtAvg, ExtCount, NewNum):
        if ExtAvg is not None:
            NewAvg = (ExtAvg * ExtCount + NewNum)/(ExtCount +1)
        else:
            NewAvg = NewNum
        return NewAvg

    def calcSqrSum (self, ExtSqrSum, NewNum):
        if ExtSqrSum is not None:
            NewSqrSum = ExtSqrSum + NewNum**2
        else:
            NewSqrSum = NewNum **2
        return NewSqrSum
    
    def calcSd (self, ExtSqrSum, ExtAvg, ExtCount, NewNum):
        #Assume it is sd for entire population
        if ExtAvg is not None:
            NewAvg = self.calcAvg(ExtAvg, ExtCount, NewNum)
            NewSqrSum = self.calcSqrSum(ExtSqrSum, NewNum)
            #This is not the real variance, but the sum of squared deviation 
            NewVar = NewSqrSum - 2*NewAvg *(ExtAvg*ExtCount + NewNum)+ (ExtCount +1)* (NewAvg**2)
            NewSd = sqrt(NewVar/(ExtCount + 1))
        else:
            NewSd = 0
        return NewSd


                    
    def updateStats(self, num):
        num = float(num)
        if self.statType != "signSplit":
            if self.statType == "absolute":
                num = abs(num)
            self.sd = self.calcSd(self.sqrSum, self.mean, self.counter, num)
            self.mean = self.calcAvg(self.mean, self.counter, num)
            self.sqrSum = self.calcSqrSum(self.sqrSum, num)

        else:
            if num > 0:
                self.posSd = self.calcSd(self.posSqrSum, self.posMean, self.posCounter, num)
                self.posMean = self.calcAvg(self.posMean, self.posCounter, num)
                self.posSqrSum = self.calcSqrSum(self.posSqrSum, num)
                self.posCounter = self.posCounter + 1
                
            elif num < 0:
                self.negSd = self.calcSd(self.negSqrSum, self.negMean, self.negCounter, num)
                self.negMean = self.calcAvg(self.negMean, self.negCounter, num)
                self.negSqrSum = self.calcSqrSum(self.negSqrSum, num)
                self.negCounter = self.negCounter + 1

            elif num == 0:
                self.posSd = self.calcSd(self.posSqrSum, self.posMean, self.posCounter, num)
                self.posMean = self.calcAvg(self.posMean, self.posCounter, num)
                self.posSqrSum = self.calcSqrSum(self.posSqrSum, num)
                self.posCounter = self.posCounter + 1  
                
                
                self.negSd = self.calcSd(self.negSqrSum, self.negMean, self.negCounter, num)
                self.negMean = self.calcAvg(self.negMean, self.negCounter, num)
                self.negSqrSum = self.calcSqrSum(self.negSqrSum, num)
                self.negCounter = self.negCounter + 1

        self.counter = self.counter + 1
        
