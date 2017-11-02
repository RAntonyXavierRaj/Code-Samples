import datetime
from trade import trade

class stock:
    'Main class for the stock'
    
    def __init__(self, symbol, stockType, lastDividend, fixedDividend, parValue):
        self.symbol = symbol
        self.stockType = stockType
        self.lastDividend = lastDividend
        self.fixedDividend = fixedDividend
        self.parValue = parValue
        self.record = []
        
    def getSymbol(self):
        return self.symbol
    def getStockType(self):
        return self.stockType
    def getLastDividend(self):
        return self.lastDividend
    def getFixedDividend(self):
        return self.fixedDividend
    def getParValue(self):
        return self.parValue
    
    # Function to calculate Dividend Yield
    def calculateDividendYield(self, price):
        if self.stockType == 'common':
            return (self.lastDividend / price)
        elif self.stockType == 'preferred':
            return (self.fixedDividend * self.parValue / price)
    
    # Function to calculate PE ratio
    def calculatePriceToEarningsRatio(self, price):
        if (self.lastDividend) == 0:
            return (0)
        else:
            return (price / self.lastDividend)
    
    # Function to record trade  (which create trade objects)
    # Created trade objects are appended to the list named record
    def recordTrade(self, timeStamp, quantity, buySellIndicator, price):
        trades = trade (timeStamp, quantity, buySellIndicator, price)
        self.record.append(trades)

   
    # function to calculate Volume weighted stock price
    # recorded trades under the stocks are used to find the volume weights.  
    def calculateVolumeWeightedStockPrice(self):
        cutOffTime = datetime.datetime.now() - datetime.timedelta(minutes=15)
        x = 0
        y = 0
        for i in self.record:
            if i.timeStamp > cutOffTime:
                y = y + (i.price * i.quantity)    # numerator
                x = x + i.quantity                # denominator
        return (y/x)                


