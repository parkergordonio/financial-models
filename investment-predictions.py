import csv

from PriceAverager import PriceAverager
from StockPrice import StockPrice

priceList = []

with open('HistoricalQuotes.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # print(row['date'], row['open'])
        stock = StockPrice(row['date'], float(row['open']))
        priceList.append(stock)

priceList.reverse()

initialPrice = priceList[0].price
stockQuantity = 14 # 2500/177
bankAccount = 5000 - (stockQuantity * initialPrice)
prevPrice = initialPrice

averager = PriceAverager(initialPrice)

for p in priceList:
    if p.price < prevPrice:
        if bankAccount - p.price > 0.0:
            stockQuantity = stockQuantity + 1
            bankAccount = bankAccount - p.price
        prevPrice = p.price
    else:
        if stockQuantity > 1:
            stockQuantity = stockQuantity - 1
            bankAccount = bankAccount + p.price
        prevPrice = p.price
    print "({date}), Worth: (${worth}), Stocks: {stocks} (v={stockValue})".format(stockValue=p.price,date=p.date,stocks=stockQuantity,worth=(float(stockQuantity) * float(p.price) + float(bankAccount)))