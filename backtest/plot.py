import matplotlib.pyplot as plt

# Plot the close price
def plot_close_price(data):
    plt.figure(figsize=(16, 8))
    plt.plot(data['Close'], label='Close Price', color='blue')
    plt.title('BTCUSDT Close Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend(loc='upper left')
    plt.show()

def plot_MACD(data):
    plt.figure(figsize=(16, 8))
    plt.plot(data['macd'], label='MACD', color='blue')
    plt.plot(data['signal'], label='Signal Line', color='red')
    plt.title('BTCUSDT MACD')
    plt.xlabel('Date')
    plt.ylabel('MACD')
    plt.legend(loc='upper left')
    plt.show()

# Plot the volatility based stop-loss
def plot_volatility_stop_loss(data):
    plt.figure(figsize=(16, 8))
    plt.plot(data['Close'], label='Close Price', color='blue')
    plt.plot(data['stop_loss'], label='Stop Loss', color='red')
    plt.title('BTCUSDT Close Price & Stop Loss')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend(loc='upper left')
    plt.show()

# Plot the short signals
def plot_short(data):
    # Plot only the first 100 days
    plt.figure(figsize=(16, 8))
    plt.plot(data['Close'][-1000:], label='Close Price', color='blue')
    plt.scatter(data.index[-1000:], data['Close'][-1000:], c=data['short'][-1000:].replace({1: 'g', -1: 'r', 0: 'w'}), label='Short Signal', marker='^', s=20)
    plt.legend(loc='upper left')
    # In a different chart, plot the macd and signal
    fig, ax1 = plt.subplots(figsize=(16, 8))
    color = 'tab:red'
    ax1.set_xlabel('Date')
    ax1.set_ylabel('MACD', color=color)
    ax1.plot(data['macd'][-1000:], color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Signal', color=color)
    ax2.plot(data['signal'][-1000:], color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    ax3 = ax1.twinx()
    color = 'tab:green'
    ax3.set_ylabel('Short Signal', color=color)
    ax3.scatter(data.index[-1000:], data['short_entry'][-1000:].replace({1: 1, -1: -1, 0: 0}), color=color)
    ax3.tick_params(axis='y', labelcolor=color)

    ax4 = ax1.twinx()
    color = 'tab:orange'
    ax4.set_ylabel('Short Signal', color=color)
    ax4.scatter(data.index[-1000:], data['short_exit'][-1000:].replace({1: 1, -1: -1, 0: 0}), color=color)
    ax4.tick_params(axis='y', labelcolor=color)


    fig.tight_layout()

    plt.show()