import pandas as pd
import numpy as np
import yfinance as yf
import datetime
from scipy.optimize import minimize

def get_data(tickers, start_date, end_date):
    """
    Function to get the historical data for the given tickers and date range
    """
    data = pd.DataFrame()
    for ticker in tickers:
        temp = yf.download(ticker, start_date, end_date)
        data[ticker] = temp['Adj Close']
    return data

def get_returns(data):
    """
    Function to calculate the daily returns of the given data
    """
    returns = np.log(data / data.shift(1))
    return returns

def get_portfolio_volatility(weights, returns):
    """
    Function to calculate the volatility of the given portfolio weights and returns
    """
    portfolio_return = np.sum(returns.mean() * weights) * 252
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
    return portfolio_volatility

def get_portfolio_return(weights, returns):
    """
    Function to calculate the return of the given portfolio weights and returns
    """
    portfolio_return = np.sum(returns.mean() * weights) * 252
    return portfolio_return

def optimize_portfolio(tickers, start_date, end_date):
    """
    Function to optimize the portfolio by finding the optimal weights using Markowitz optimization
    """
    data = get_data(tickers, start_date, end_date)
    returns = get_returns(data)
    n_assets = len(tickers)
    initial_weights = np.array([1/n_assets] * n_assets)
    bounds = tuple((0,1) for i in range(n_assets))
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    optimal_weights = minimize(get_portfolio_volatility, initial_weights, args=returns, method='SLSQP', bounds=bounds, constraints=constraints).x
    optimal_return = get_portfolio_return(optimal_weights, returns)
    optimal_volatility = get_portfolio_volatility(optimal_weights, returns)
    return optimal_weights, optimal_return, optimal_volatility

# Example usage
tickers = ['AAPL', 'GOOG', 'IBM', 'TSLA','PGR', 'KO']
start_date = '2018-01-01'
end_date = '2023-01-01'

optimal_weights, optimal_return, optimal_volatility = optimize_portfolio(tickers, start_date, end_date)

print("Optimal Weights:", np.round(optimal_weights,2))
print("Optimal Return:", optimal_return)
print("Optimal Volatility:", optimal_volatility)




