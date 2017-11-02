from stock import stock

class marketIndex():
    'main class which denotes the market as a whole whole. Stocks are added to this class and trades are added to stocks '
    def __init__(self):
        # This list contains of all stocks in the market (represents whole market)
        self.stocks = []
     
    # Function to create and append stock objects to stocks list    
    def createAndAppendStocks(self,symbol, stockType, lastDividend, fixedDividend, parValue):
        'adding all 5 Stocks to a single list which represents all stocks'
        self.stocks.append(stock(symbol, stockType, lastDividend, fixedDividend, parValue))              
        
    def allShareIndex(self):
        'All shares index - based on the price of the last trade of all stocks'
        z = 1
        for i in range(len(self.stocks)):
            z = z * float((self.stocks[i].record[-1].price))
        
        # finding root based on the number of stocks
        allShareIndex = z ** (1/len(self.stocks))  
        return allShareIndex
