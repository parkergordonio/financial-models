
# Stock Averages
class PriceAverager:
    fiftyTwoWeekWindow=[]
    fiftyTwoWeekAverage=0
    twentySixWeekWindow=[]
    twentySixWeekAverage=0

    def __init__(self, initialPrice):
        self.initialPrice = initialPrice

    def get52WeekAvg(self):
        return sum(self.fiftyTwoWeekWindow) / len(self.fiftyTwoWeekWindow)