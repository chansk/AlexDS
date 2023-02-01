import os
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import date # data class from datetime module

def my_function(x):
    return str(5 * x)

# stck = yf.Ticker("AAPL")
# # print(stck.info)

def print_date(x):
    today = date.today()
    MyDate = today.strftime("%Y-%m-%d")
    return(MyDate + x)

def stock_pred():
    today = date.today()
    MyDate = today.strftime("%Y-%m-%d")
    
    # Retrieve Apple stock data from Yahoo Finance
    apple = yf.Ticker("AAPL").history(start="2010-01-01", end=MyDate)

    # Plot the close price
#     plt.plot(apple["Close"])
#     plt.xlabel("Date")
#     plt.ylabel("Close Price")
#     plt.title("Apple Stock Price")
#     plt.show()
    # trouble plotting in webpage for some reason
    
    # Create the X and y arrays for training
    X = np.array(range(len(apple))).reshape(-1, 1) # Number day
    y = np.array(apple["Close"]).reshape(-1, 1) # Closing price

#     return(str(X[1] + y[1]))
    
    # Train the model
    model = LinearRegression() # using single linear regression
    model.fit(X, y)
    # could be improved if we had another factor to go along with it

#     # Predict the close price for tomorrow
    tomorrow = model.predict(np.array([len(apple)]).reshape(-1, 1))

#     # Print the prediction
    return("Tomorrow's closing price prediction: " + str(tomorrow[0][0]))