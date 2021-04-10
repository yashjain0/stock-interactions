import nsepy
import datetime
import pandas as pd
import matplotlib.pyplot as plt

def getHistoricalData(stockname):
    today=datetime.date.today()
    duration=450
    start = today+datetime.timedelta(-duration)

    stockData = nsepy.get_history(symbol=stockname, start=start, end=today )
    return stockData

df = getHistoricalData('SBIN')
df['Close'].plot()
plt.show()

