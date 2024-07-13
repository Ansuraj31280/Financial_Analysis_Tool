import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
def fetch_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data
def plot_stock_data(stock_data, ticker):
    plt.figure(figsize=(14, 7))
    plt.plot(stock_data['Close'], label=f'{ticker} Closing Price')
    plt.title(f'{ticker} Stock Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.show()
def plot_moving_averages(stock_data, ticker, short_window=20, long_window=50):
    stock_data['Short_MA'] = stock_data['Close'].rolling(window=short_window, min_periods=1).mean()
    stock_data['Long_MA'] = stock_data['Close'].rolling(window=long_window, min_periods=1).mean()
    plt.figure(figsize=(14, 7))
    plt.plot(stock_data['Close'], label=f'{ticker} Closing Price')
    plt.plot(stock_data['Short_MA'], label=f'{short_window}-Day Moving Average')
    plt.plot(stock_data['Long_MA'], label=f'{long_window}-Day Moving Average')
    plt.title(f'{ticker} Stock Price and Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.show()
def main():
    ticker = input("Enter stock ticker symbol (e.g., AAPL, MSFT): ").upper()
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    stock_data = fetch_stock_data(ticker, start_date, end_date)
    
    if stock_data.empty:
        print("No data found for the given ticker and date range.")
        return
    plot_stock_data(stock_data, ticker)
    plot_moving_averages(stock_data, ticker)
if __name__ == "__main__":
    main()
