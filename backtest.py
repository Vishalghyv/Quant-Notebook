# Pull data from 'data/Crypto/Binance_BTCUSDT_d.csv'
# Pull signals from strategy.py
# Trade class bot from trade.py
# Bactest the strategy

# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Import data
def import_data():
    data = pd.read_csv('data/Crypto/Binance_BTCUSDT_d.csv')
    return data

data = import_data()

# Import sigals from strategy.py
from strategy import final_signals
print(len(final_signals))
# Import Trade class from trade.py
from trade import Trade

print("\n\nBacktesting the strategy\n\n")
# Backtest the strategy
quantity = 1
symbol = 'BTCUSDT'
initalPrice = data['Close'][0]
target_multiplier = 1

bot = Trade(1, symbol, initalPrice, quantity)

for row in final_signals.iterrows():
    i = row[0]
    # try:
    price = final_signals['Close'][i]
    signal = final_signals['short'][i]
    target_price = price - final_signals['atr'][i] * target_multiplier
    stop_price = price + final_signals['atr'][i]
    bot.update(price)
    if signal == 1:
        bot.close()
    elif signal == -1:
        bot.short(quantity, price, target_price, stop_price)
        # bot.log()

    # except:
    #     pass
print(bot.profit)

# Plot the results
plt.plot(bot.profit)
plt.plot(bot.profit_fee_adjusted)
plt.show()
