import csv
import plotly
from plotly import tools
import plotly.graph_objs as go
import plotly.plotly as plot

from strategies.InvestUtils import InvestHistory
from StockPrice import StockPrice
from strategies.sellDownBuyUp import SellDownBuyUpStrategy

def plotSingle(strategy):
    stockGraph = strategy.stockPriceGraphData()
    xAxis = stockGraph[0]
    yAxis = stockGraph[1]

    plotly.offline.plot({
        "data": [go.Scatter(x=xAxis, y=yAxis)],
        "layout": go.Layout(title="Performance for IBM")
    }, auto_open=True)

def plotStockAndWealth(strategy):
    stockGraph = strategy.stockPriceGraphData()
    stockXAxis = stockGraph[0]
    stockYAxis = stockGraph[1]

    stockScatter = go.Scatter(x=stockXAxis, y=stockYAxis)
    
    # Wealth (Cash, Stock)
    wealthGraph = strategy.wealthGraphData()
    wealthXAxis = wealthGraph[0]
    cashWorthYAxis = wealthGraph[1]
    stockWorthYAxis = wealthGraph[2]
    buyAndHoldWorthYAxis = wealthGraph[3]

    cashTrace = go.Bar(
        x=wealthXAxis,
        y=cashWorthYAxis,
        name='Worth (Cash)'
    )
    stockTrace = go.Bar(
        x=wealthXAxis,
        y=stockWorthYAxis,
        name='Worth (Stock)'
    )
    buyAndHoldTrace = go.Scatter(
        x=wealthXAxis,
        y=buyAndHoldWorthYAxis,
        name='Buy+Hold (Total)'
    )

    # wealthData = [stockTrace, cashTrace, buyAndHoldTrace]
    # wealthLayout = go.Layout(barmode='stack')

    # wealthFig = go.Figure(data=wealthData, layout=wealthLayout)


    fig = tools.make_subplots(rows=2, cols=1, shared_xaxes=True)

    fig.append_trace(stockScatter,1,1)
    fig.append_trace(stockTrace,2,1)
    fig.append_trace(cashTrace,2,1)
    fig.append_trace(buyAndHoldTrace,2,1)
    fig['layout'].update(title='IBM Performance', barmode='stack')
    
    plotly.offline.plot(fig, filename='graphs/simple-subplot-with-annotations.html')

# Setup Parameters
initialAccountBalance = 10000
initialStockPurchase = 10 # Units
priceList = []


with open('HistoricalQuotes.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # print(row['date'], row['open'])
        stock = StockPrice(row['date'], float(row['open']))
        priceList.append(stock)

priceList.reverse()

history = InvestHistory(priceList[0], initialAccountBalance)
strategy = SellDownBuyUpStrategy(history)

# Buy Initial Amount
strategy.buyStockBulk(priceList[0], initialStockPurchase)

for p in priceList:
    strategy.nextDay(p)

plotStockAndWealth(strategy)