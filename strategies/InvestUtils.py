import abc
from PriceAverager import PriceAverager

# Common utilities and tracking for investing strategies
class InvestHistory():
    # Averaging Util
    averager = PriceAverager(0)

    _prices = []
    _cashWorthTrend = []
    _stockWorthTrend = []

    # Buy and hold Trends
    _buyAndHoldUnits = 0
    _buyAndHoldTrend = []
    _buyAndHoldLeftoverCash = 0

    _accountBalance = 0.0
    _stockQuantity = 0.0

    def __init__(self, initialPrice, initialAccountBalance):
        self._prices.append(initialPrice)
        self._accountBalance = initialAccountBalance
        self._buyAndHoldUnits = int(initialAccountBalance / initialPrice.price)
        self._buyAndHoldLeftoverCash = initialAccountBalance - (self._buyAndHoldUnits * initialPrice.price)

    def prices(self):
        return self._prices

    # stock history tracking
    def appendStockHistory(self, p):
        self._prices.append(p)
        self.updateTotalWorth(p)
        return None

    def buyStock(self, p, quantity=1):
        if self._accountBalance > (p.price * quantity):
            self._stockQuantity = self._stockQuantity + quantity
            self._accountBalance = self._accountBalance - (p.price * quantity)



    def sellStock(self, p):
        if self._stockQuantity > 0:
            self._stockQuantity = self._stockQuantity - 1
            self._accountBalance = self._accountBalance + p.price

    def updateTotalWorth(self, p):
        cashWorth = self._accountBalance
        self._cashWorthTrend.append(cashWorth)

        stockWorth = self._stockQuantity * p.price
        self._stockWorthTrend.append(stockWorth)

        holdWorth = (self._buyAndHoldUnits * p.price) + self._buyAndHoldLeftoverCash
        self._buyAndHoldTrend.append(holdWorth)


    ## Printing Utilities
    def verboseWealthNow(self):
        # print(len(self._prices))
        # print self._prices[len(self._prices) - 1]
        return self.verboseWealth(self._prices[len(self._prices) - 1])


    # Print Utils
    def verboseWealth(self, p):
        return "({date}), Worth: (${worth}), Stocks: {stocks} (v={stockValue})".format(stockValue=p.price, date=p.date, stocks=self._stockQuantity, worth=self.totalWorth(p.price))
    
    def totalWorth(self, currentPrice):
        # print "Stock Quantity ->"
        # print float(self._stockQuantity)
        # print "Current Stock Price ->"
        # print float(currentPrice)
        # print "Account Balance ->"
        # print float(self._accountBalance)
        return (float(self._stockQuantity) * float(currentPrice) + float(self._accountBalance))


    # Graphing Utils
    def wealthGraphData(self):
        x = list(map(lambda p: p.date, self._prices))
        return (x, self._cashWorthTrend, self._stockWorthTrend, self._buyAndHoldTrend)

    def stockPriceGraphData(self):
        x = list(map(lambda p: p.date, self._prices))
        y = list(map(lambda p: p.price, self._prices))
        return (x, y)