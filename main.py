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
    for date in hist['Close'][:11]:
        last10days.append(date)
    myarray = np.array(last10days)
    plt.plot(myarray)
    plt.show()
