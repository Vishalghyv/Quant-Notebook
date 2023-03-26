# Quant-Notebook

Repositories is consisted of three parts

## Quant Strategies for Crypto markets notebook

- Notebook contains various ideas and macro information for crypto markets
- Notebook also provides a Macd strategy to be executed

## Bitcoin vs Interest Rates notebook

- Notebook imports interest rates data
- ![plot](images/plot.png)
- Calculates the correlation between Bitcoin and Interest Rates using change in price after the announcement
- Plots the correlation
- ![change](images/change.png)
- ![daily_change](images/daily_change.png)
- Uses simple linear regression model summary better understand the correlation
- ![ols](images/ols.png)
- Notebook also provides a simple script to compare the correlation between Bitcoin and various countries interest rates
- ![comparison](images/comparison.png)

## Backtest folder

- Executed using command `python3 backtest.py`
- Backtest.py imports the strategy and trade bot to execute the strategy
- ![macd](images/macd.png)
- ![trades](images/trades.png)
- ![logs](images/logs.png)
- Plots cummulatve returns
- ![profit](images/profit.png)
