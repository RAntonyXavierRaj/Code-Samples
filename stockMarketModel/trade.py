
class trade:
    ' Creating trade object '
    def __init__(self, timeStamp, quantity, buySellIndicator, price):
        self.timeStamp = timeStamp
        self.quantity = quantity
        self.buySellIndicator = buySellIndicator
        self.price = price
        
    def getTimeStamp(self):
        return self.timeStamp

    def getQuantity(self):
        return self.quantity

    def getBuySellIndicator(self):
        return self.buySellIndicator

    def getPrice(self):
        return self.price
