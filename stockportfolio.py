stock_portfolio_tracker/
data/
stock_data.csv
portfolio_data.csv
config.py
data_fetcher.py
portfolio_tracker.py
visualization.py
main.py
requirements.txt
README.md
import os


STOCK_DATA_FILE = 'data/stock_data.csv'
PORTFOLIO_DATA_FILE = 'data/portfolio_data.csv'

# API keys
YAHOO_FINANCE_API_KEY = 'YOUR_API_KEY_HERE'

# Other settings
START_DATE = '2017-01-01'
END_DATE = '2022-01-01'
  import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

def fetch_portfolio_data(portfolio_tickers, start_date, end_date):
    portfolio_data = pd.DataFrame()
    for ticker in portfolio_tickers:
        data = fetch_stock_data(ticker, start_date, end_date)
        portfolio_data[ticker] = data['Close']
    return portfolio_data
    import matplotlib.pyplot as plt

def plot_portfolio_returns(returns):
    plt.plot(returns)
    plt.title('Portfolio Returns')
    plt.xlabel('Date')
    plt.ylabel('Return')
    plt.show()

def plot_portfolio_value(value):
    plt.plot(value)
    plt.title('Portfolio Value')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.show()

    import portfolio_tracker
import visualization

def main():
    portfolio_tickers = ['AAPL', 'GOOG', 'MSFT']
    start_date = '2017-01-01'
    end_date = '2022-01-01'

    tracker = portfolio_tracker.PortfolioTracker(portfolio_tickers, start_date, end_date)
    returns, value = tracker.track_portfolio()

    visualization.plot_portfolio_returns(returns)
    visualization.plot_portfolio_value(value)

if __name__ == '__main__':
    main()
