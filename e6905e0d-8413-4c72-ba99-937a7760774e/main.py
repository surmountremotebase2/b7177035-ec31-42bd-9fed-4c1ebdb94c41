
from surmount.base_class import Strategy, TargetAllocation
from surmount.technical_indicators import SMA
from surmount.logging import log
from surmount.data import Asset

class TradingStrategy(Strategy):
    """
    A trading strategy that decides whether to buy SPXL (a 3x leveraged ETF that aims to return 
    three times the daily performance of the S&P 500 index) or SPXS (a 3x leveraged inverse ETF 
    that aims to return three times the inverse of the daily performance of the S&P 500 index) 
    based on the 10-day simple moving average (SMA) trend of the SPY (S&P 500 ETF).
    """

    @property
    def assets(self):
        # Assets that are involved in this strategy
        return ["SPXL", "SPXS", "SPY"]

    @property
    def interval(self):
        # The data interval required for this strategy
        return "1day"

    def run(self, data):
        """
        Executes the trading strategy logic.
        
        Args:
            data (dict): Contains data required for making trading decisions.
        
        Returns:
            TargetAllocation: An object specifying the target allocation for each asset.
        """
        sma = SMA("SPY", data["ohlcv"], 10)  # Calculate 10-day SMA for SPY
        
        allocation_dict = {"SPXL": 0, "SPXS": 0}  # Initial allocation (no holdings)
        
        if len(sma) >= 2:
            # Check if the SMA is trending upwards, downwards, or staying flat
            if sma[-1] > sma[-2]:
                allocation_dict["SPXL"] = 1  # Buy SPXL if trending upwards
                #log("Trend is upwards, buying SPXL")
            elif sma[-1] < sma[-2]:
                allocation_dict["SPXS"] = 1  # Buy SPXS if trending downwards
                #log("Trend is downwards, buying SPXS")
            else:
                allocation_dict["SPXS"] = 0
                allocation_dict["SPXL"] = 0
                #log("Trend is flat, holding nothing")

        return TargetAllocation(allocation_dict)
