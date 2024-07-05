from surmount.base_class import Strategy, TargetAllocation, backtest
from surmount.base_class import Strategy, TargetAllocation
from surmount.technical_indicators import SMA, MACD, RSI
from surmount.logging import log
from surmount.data import Asset 

class TradingStrategy(Strategy):
    def __init__(self):
        self._assets = ['SPY']

    @property
    def assets(self):
        return self._assets

    @property 
    def interval(self):
        return "1day"

    def run(self, data):
        return TargetAllocation({'GME': 1})

from datetime import datetime

start = datetime.strptime("2022-11-10", '%Y-%m-%d')
end = datetime.strptime("2022-11-16", '%Y-%m-%d')
a = backtest(TradingStrategy(), start, end, 1000)

print(a['stats'])