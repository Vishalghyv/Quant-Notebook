# Calculate the fast and slow Simple Moving Averages (SMA) in the 30-minute timeframe.
# Monitor the MACD (Moving Average Convergence Divergence) indicator for a crossover signal in the short direction for the smaller timeframe.
# Once a crossover signal occurs, use the daily timeframe to take a short position in BTC.
# Set the stop-loss in the resistance region for the 30-minute timeframe.
# Set the target in the support region for the daily timeframe.
# Aim for an expected risk-reward ratio of 1:5.


# Step 1: Import the libraries
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None 
import matplotlib.pyplot as plt
from plot import plot_close_price, plot_short, plot_MACD, plot_volatility_stop_loss

# Step 2: Import the data
# https://www.kaggle.com/datasets/prasoonkottarathil/btcinusd
# Use BTC-Daily.csv file

def import_data():
    data = pd.read_csv('data/Bitcoin.csv')
    data['Date'] = pd.to_datetime(data['Date'])
    data['Price'] = data['Price'].str.replace(',', '')
    data = data[(data['Date'].dt.year > 2014)].reset_index(drop=True)

    data['Close'] = data['Price'].astype(float)
    data['High'] = data['High'].str.replace(',', '')
    data['High'] = data['High'].astype(float)
    data['Low'] = data['Low'].str.replace(',', '')
    data['Low'] = data['Low'].astype(float)
    data['Open'] = data['Open'].str.replace(',', '')
    data['Open'] = data['Open'].astype(float)
    return data
data = import_data()

# Step 4: Calculate the MACD (Moving Average Convergence Divergence) indicator
def MACD(data, fast_period, slow_period, signal_period, column):
    data['fast_ema'] = data[column].ewm(span=fast_period, adjust=False).mean()
    data['slow_ema'] = data[column].ewm(span=slow_period, adjust=False).mean()
    data['macd'] = data['fast_ema'] - data['slow_ema']
    data['signal'] = data['macd'].ewm(span=signal_period, adjust=False).mean()
    return data

data = MACD(data, 15, 50, 9, 'Close')
# plot_MACD(data)

def generate_short_signals(data):
    # Mark the places where the MACD crosses below the signal line
    data['short_entry'] = np.where(data['macd'] < data['signal'], 1.0, 0.0)
    # Mark the places where the MACD crosses above the signal line
    data['short_exit'] = np.where(data['macd'] > data['signal'], -1.0, 0.0)

    # Calculate moment when to open and close the position
    data['short_entry'] = np.where(data['short_entry'].shift(1) == 1, 0, data['short_entry'])
    data['short_exit'] = np.where(data['short_exit'].shift(1) == -1, 0, data['short_exit'])

    # Combine the short_entry and short_exit columns
    data['short'] = data['short_entry'] + data['short_exit']
    
    return data


data = generate_short_signals(data)


plot_short(data)

def volatility_stop_loss(data, multiplier):
    # Calculate the average true range
    data['high-low'] = abs(data['High'] - data['Low'])
    data['high-pc'] = abs(data['High'] - data['Close'].shift(1))
    data['low-pc'] = abs(data['Low'] - data['Close'].shift(1))
    data['tr'] = data[['high-low', 'high-pc', 'low-pc']].max(axis=1, skipna=False)
    data['atr'] = data['tr'].rolling(100).mean()
    # Calculate the volatility based stop-loss
    data['stop_loss'] = data['High'] + (data['atr'] * multiplier)
    return data


# print(len(data))

new_data = data[-2000:]
new_data = volatility_stop_loss(new_data, 2)
# plot_volatility_stop_loss(new_data)
new_data = new_data[-1900:]

final_signals = new_data[['Close', 'short', 'stop_loss', 'atr']]
