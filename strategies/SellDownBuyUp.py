import csv

from PriceAverager import PriceAverager
from StockPrice import StockPrice
from InvestUtils import InvestHistory

class SellDownBuyUpStrategy():
    _history = None
    initialPrice = None
    stockQuantity = None
    bankAccount = None
    prevPrice = None

    def __init__(self, history):
        self._history = history
        self.initialPrice = self._history.prices()[0].price
        self.stockQuantity = 14 # 2500/177
        self.bankAccount = 5000 - (self.stockQuantity * self.initialPrice)
        self.prevPrice = self.initialPrice

    def nextDay(self, p):
        if p.price < self.prevPrice:
            self._history.buyStock(p)
            self.prevPrice = p.price
        else:
            self._history.sellStock(p)
            self.prevPrice = p.price
        self._history.appendStockHistory(p)
        print self._history.verboseWealth(p)

    def printUpdate(self):
        print self._history.verboseWealthNow()

    def stockPriceGraphData(self):
        return self._history.stockPriceGraphData()

    def wealthGraphData(self):
        return self._history.wealthGraphData()

    def buyStockBulk(self, p, quantity=1):
        self._history.buyStock(p, quantity)