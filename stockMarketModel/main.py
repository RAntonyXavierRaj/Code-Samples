import datetime
from marketIndex import marketIndex

class main:
    def main():
        try: 
        
            # Creating 5 stocks with the sample data
            symbol = ['TEA', 'POP', 'ALE', 'GIN', 'JOE']
            stockType = ['common', 'common', 'common', 'preferred', 'common']
            lastDividend = [0.0, 8.0, 23.0, 8.0, 13.0]
            fixedDividend = [0.0, 0.0, 0.0, 0.02, 0.0]
            parValue = [100.0, 100.0, 60.0, 100.0, 250.0]    
            
            buySellIndicator = ['BUY','SELL']
            
            price = 105.0   # (SAMPLE) given price to calculate Dividend Yield and PE ratio   
            
            # The whole market is denoted by a single object
            index = marketIndex()
            
            # Now stocks are added to the market
            for i in range(5):
                index.createAndAppendStocks(symbol[i], stockType[i], lastDividend[i], fixedDividend[i], parValue[i])
    
            # Now trades are being recorded for stocks
            # inputs --> time, quantity, buySellIndicator,price
            'Trades for stock 1'
            index.stocks[0].recordTrade(datetime.datetime.now(), 200, buySellIndicator[0], 101.0)
            index.stocks[0].recordTrade(datetime.datetime.now(), 100, buySellIndicator[1], 102.0)
            
            'Trades for stock 2'
            index.stocks[1].recordTrade(datetime.datetime.now(), 300, buySellIndicator[1], 102.0)
            index.stocks[1].recordTrade(datetime.datetime.now(), 200, buySellIndicator[1], 103.0)
            
            'Trades for stock 3'
            index.stocks[2].recordTrade(datetime.datetime.now(), 700, buySellIndicator[0], 100.0)
            index.stocks[2].recordTrade(datetime.datetime.now(), 500, buySellIndicator[1], 105.0)
            index.stocks[2].recordTrade(datetime.datetime.now(), 100, buySellIndicator[1], 106.0)
            
            'Trades for stock 4'
            index.stocks[3].recordTrade(datetime.datetime.now(), 200, buySellIndicator[0], 101.0)
            index.stocks[3].recordTrade(datetime.datetime.now(), 200, buySellIndicator[0], 101.0)   
            
            'Trades for stock 5'
            index.stocks[4].recordTrade(datetime.datetime.now(), 500, buySellIndicator[1], 104.0)
          
            # Sample summary for a stock
            print ("\nSample output for Stock 'ALE':\n")
            print (("|%-30s|%20s|") % ("Dividend Yield", str(index.stocks[2].calculateDividendYield(price))))
            print (("|%-30s|%20s|") % ("Dividend Yield - Pref", str(index.stocks[3].calculateDividendYield(price))))
            print (("|%-30s|%20s|") % ("PE ratio ", str(index.stocks[2].calculatePriceToEarningsRatio(price))))
            print (("|%-30s|%20s|") % ("Volume Weighted Stock Price", str(index.stocks[2].calculateVolumeWeightedStockPrice())))
            
            # Calculating all share index
            print ("\nGBCE All Share Index is " + str(index.allShareIndex()))

        except BaseException:
            pass
            

main.main()


