from surmount.base_class import Strategy, TargetAllocation, backtest
from surmount.logging import log

class TradingStrategy(Strategy):
    def __init__(self):
        self.tickers = ["SPY"]
        self.weights = [100]
        self.count = 0

    @property
    def interval(self):
        return "5min"

    @property
    def assets(self):
        return self.tickers

    def run(self, data):
        self.count += 1
        log(data['ohlcv'][-1]['SPY']['date'])
        if (True):
            allocation_dict = {self.tickers[i]: self.weights[i]/sum(self.weights) for i in range(len(self.tickers))}
            return TargetAllocation(allocation_dict)
        return None