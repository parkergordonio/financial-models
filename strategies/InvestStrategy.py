import abc
from SellDownBuyUp import SellDownBuyUpStrategy

class InvestStrategy:
    __metaclass__ = abc.ABCMeta

    prices = []

    @property
    def priceList(self):
        self.priceList


InvestStrategy.register(SellDownBuyUpStrategy)