from surmount.base_class import Strategy, TargetAllocation, backtest
from surmount.logging import log

class TradingStrategy(Strategy):

   def __init__(self):
      self.alloc = {}

   @property
   def assets(self):
      return ["SVXY"]

   @property
   def interval(self):
      return "1hour"

   def run(self, data):
      if len(data["ohlcv"]) == 0: 
         self.alloc = {"SVXY":0}
         return TargetAllocation(self.alloc)
      data1 = data["ohlcv"][-1]["SVXY"]
      if "14:00" in data1["date"]:
         self.alloc = {"SVXY":0}
         return TargetAllocation(self.alloc)
      high = data1["high"]
      low = data1["low"]
      mid = high + low / 2
      if data1["close"] <= mid: return TargetAllocation({"SVXY":1})
      return TargetAllocation({"SVXY":0})

from datetime import datetime

start = datetime.strptime("2024-04-01", '%Y-%m-%d')
end = datetime.strptime("2024-04-20", '%Y-%m-%d')
a = backtest(TradingStrategy(), start, end, 10000)

print(a['stats'])

# from surmount.data_client import _FMPClient

# client = _FMPClient()
# print(client.get_stock_splits({'SVXY', 'PALAD', 'BON', 'FLNT', 'SPXV'},start, end))

# print(client.get_history("SVXY", "1hour", start, end))