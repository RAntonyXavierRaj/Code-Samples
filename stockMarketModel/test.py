import doctest

__test__ = {
    'stock': '''
>>> symbol = ['TEA', 'POP', 'ALE', 'GIN', 'JOE']
>>> stockType = ['common', 'common', 'common', 'preferred', 'common']   
>>> lastDividend = [0.0, 8.0, 23.0, 8.0, 13.0]
>>> fixedDividend = [0.0, 0.0, 0.0, 0.02, 0.0]
>>> parValue = [100.0, 100.0, 60.0, 100.0, 250.0]    
>>> 
>>> buySellIndicator = ['BUY','SELL']
>>> 
>>> price = 105.0   # (SAMPLE) given price to calculate Dividend Yield and PE ratio   
>>> 
>>> index = marketIndex.marketIndex()
>>> #Creating and Appending 5 stocks
>>> for i in range(5):
...     index.createAndAppendStocks(symbol[i], stockType[i], lastDividend[i], fixedDividend[i], parValue[i])
...
>>> #Trades for stock
>>> index.stocks[0].recordTrade(datetime.datetime.now(), 200, buySellIndicator[0], 101.0)
>>> index.stocks[0].recordTrade(datetime.datetime.now(), 100, buySellIndicator[1], 102.0)
>>> #Trades for stock 2
>>> index.stocks[1].recordTrade(datetime.datetime.now(), 300, buySellIndicator[1], 102.0)
>>> index.stocks[1].recordTrade(datetime.datetime.now(), 200, buySellIndicator[1], 103.0)
>>> #Trades for stock 3 
>>> index.stocks[2].recordTrade(datetime.datetime.now(), 700, buySellIndicator[0], 100.0)
>>> index.stocks[2].recordTrade(datetime.datetime.now(), 500, buySellIndicator[1], 105.0)
>>> index.stocks[2].recordTrade(datetime.datetime.now(), 100, buySellIndicator[1], 106.0)
>>> #Trades for stock 4
>>> index.stocks[3].recordTrade(datetime.datetime.now(), 200, buySellIndicator[0], 101.0)
>>> index.stocks[3].recordTrade(datetime.datetime.now(), 200, buySellIndicator[0], 101.0)   
>>> #Trades for stock 5
>>> index.stocks[4].recordTrade(datetime.datetime.now(), 500, buySellIndicator[1], 104.0)
 
>>> #Sample output for Stock 'ALE'

>>> index.stocks[2].calculateDividendYield(price)
0.21904761904761905
>>> index.stocks[3].calculateDividendYield(price)
0.01904761904761905
>>> index.stocks[2].calculatePriceToEarningsRatio(price)
4.565217391304348
>>> index.stocks[2].calculateVolumeWeightedStockPrice()
102.38461538461539
>>> index.allShareIndex()
103.18571906530079
''',

}

if __name__ == "__main__":
    doctest.testmod(verbose=1)