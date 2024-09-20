# INF601 - Advanced Programming in Python
# Stephen Blomberg
# Mini Project 1

import yfinance as yf
import pprint
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt

#Get today's date
today = datetime.now()

#Calculate the date 10 days ago
ten_days_ago = today - timedelta(days=15)

print("Today's date:", today.strftime("%Y-%m-%d"))
print("Date 10 days ago:", ten_days_ago.strftime("%Y-%m-%d"))

mytickers = ["MSFT", "AAPL", "NVDA", "GME", "AMC"]
mytickers.sort()

for ticker in mytickers:
    result = yf.Ticker(ticker)
    hist = result.history(start=ten_days_ago, end=today)
    last10days = []
    for date in hist['Close'][:10]:
        last10days.append(date)
    if len(last10days) == 10:
        myarray = np.array(last10days)
        plt.plot(myarray)
        plt.xlabel('Days Ago')
        plt.ylabel('Closing Price')
        plt.title(f"{ticker} Last 10 Trading Days")
        plt.show()
    else:
        print(f"Do not have 10 days of data to plot. Only have {len(last10days)} days.")