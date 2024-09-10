# INF601 - Advanced Programming in Python
# Stephen Blomberg
# Mini Project 1

import yfinance as yf
import pprint

mytickers = ["MSFT", "AAPL", "NVDA", "GME", "AMC"]

mydata = {}

mytickers.sort()

for ticker in mytickers:
    result = yf.Ticker(ticker)
    mydata[ticker] = {'ticker': ticker,
                      'dayHigh': result.info['dayHigh']}

    print(f"Ticker: {ticker} \t Daily High: {result.info['dayHigh']}")
    
msft = yf.Ticker("MSFT")

# get all stock info
#msft.info

#pprint.pprint(msft.info)

# get historical market data
#hist = msft.history(period="5d", interval="1d")
#hist = msft.history(start=2024-8-27, end=2024-9-10)

#pprint.pprint(hist)