from talib import abstract 
import yfinance as yf
import pandas as pd
from backtesting import Backtest, Strategy
from backtesting.lib import crossover

df = yf.download('GOOG', '2010-01-01', '2024-09-30')

# print(df)

df_modified = df.rename(columns={"Open":"open", "High": "high", "Low":"low", "Close": "close", "Adj Close": "adj close", "Volume": "volume"})

print(df_modified)

df['nvda_sma_20'] = abstract.SMA(df_modified, timeperiod=20)


df_rsi = abstract.RSI(df_modified, 14)

print(df_rsi)

df_backtest = pd.merge(df, df_rsi, on="Date")



bt = Backtest(df_backtest, KdCross, cash=10000, commission=0.01)
output=bt.run()

print(output)

bt.plot()