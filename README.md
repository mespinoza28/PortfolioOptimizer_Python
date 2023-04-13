---
name: "Portfolio Optimizer"
about: The script allows you to calculate the optimal weights in a portfolio given a list of ticker symbols.
labels: Quantitative Finance

---

## Description
This code provides a set of functions to optimize a portfolio of assets using Markowitz optimization. The code uses historical data from Yahoo Finance to calculate the expected returns and covariance matrix for the assets.

## Functions

get_data(tickers, start_date, end_date): This function retrieves the historical data for a list of ticker symbols within a specified date range. It returns a pandas DataFrame containing the adjusted close prices for each asset.

get_returns(data): This function calculates the daily returns of the given data. It returns a pandas DataFrame containing the daily returns for each asset.

get_portfolio_volatility(weights, returns): This function calculates the volatility of a given portfolio using the given weights and returns. It returns a float value representing the volatility of the portfolio.

get_portfolio_return(weights, returns): This function calculates the expected return of a given portfolio using the given weights and returns. It returns a float value representing the expected return of the portfolio.

optimize_portfolio(tickers, start_date, end_date): This function optimizes the portfolio by finding the optimal weights using Markowitz optimization. It returns a tuple containing the optimal weights, the expected return of the portfolio, and the volatility of the portfolio.

### Environment
Libraries required:
-pandas
-numpy
-yfinance
-datetime
-scipy


### Basic example
 The output represents the optimal weights, expected return, and volatility of the portfolio. The weights show how much of each asset should be held in the portfolio to maximize returns while minimizing risk.

<img width="690" alt="image" src="https://user-images.githubusercontent.com/129782426/231868024-97025753-a855-4db1-bab2-10a7e8ec109c.png">


### Motivation
This tool was initially developed to assist in the portfolio construction process for clients.
