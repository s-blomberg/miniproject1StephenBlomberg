# INF601 - Advanced Programming in Python
# Stephen Blomberg
# Mini Project 1

import yfinance as yf
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
import os

#Checks for charts folder to place pictures into.
os.makedirs("charts", exist_ok=True)

#Get today's date
today = datetime.now()

#Calculate the date 10 days ago
ten_days_ago = today - timedelta(days=15)

#List of personal tickers
myTickers = ["SPY", "AMD", "NVDA", "GME", "KOSS"]
myTickers.sort()

#Loops through each ticker in the list and creates the graphs
for ticker in myTickers:
    result = yf.Ticker(ticker)
    hist = result.history(start=ten_days_ago, end=today)
    last10days = []
    for date in hist['Close'][:11]:
        last10days.append(date)
    if len(last10days) >= 10:
        myarray = np.array(last10days)
        max_price = myarray.max() + (myarray.max()*.05)
        min_price = myarray.min() - (myarray.min()*.05)
        plt.plot(myarray)
        plt.xlabel('Days Ago')
        plt.ylabel('Closing Price')
        plt.axis((9, 0, min_price, max_price))
        plt.title(f"{ticker} Last 10 Trading Days")
        plt.savefig(f"charts/{ticker}.png")
    else:
        print(f"Do not have 10 days of data to plot. Only have {len(last10days)} days.")
