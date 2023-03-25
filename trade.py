class Trade:
    def __init__(self, id, symbol, price, quantity):
        self.id = id
        self.symbol = symbol
        self.price = price
        self.current_price = price
        self.quantity = quantity
        self.profit = []
        self.profit_fee_adjusted = []
        self.fee_trade = 0.001
        self.status = 'close'
        self.side = 'neutral'
    
    def log(self):
        # Log the trade, current price, target price, and stop loss price
        print(f"Trade: {self.id} | Symbol: {self.symbol} | Side: {self.side} | Price: {self.price} | Target: {self.target_price} | Stop Loss: {self.stop_loss_price} | Quantity: {self.quantity}")
    
    def calculate_profit(self):
        # Calculate the profit based on the side of the trade and quantity  
        current_profit = 0
        if self.side == 'long':
            current_profit = (self.price - self.target_price) * self.quantity
        elif self.side == 'short':
            current_profit = (self.stop_loss_price - self.price) * self.quantity
        self.profit.append(current_profit)
        self.profit_fee_adjusted.append(current_profit - (self.fee_trade * self.quantity * self.price))
    
    def close(self):
        # Calculate the profit based on the side of the trade
        self.calculate_profit()
        self.status = 'close'
        self.side = 'neutral'

    def open(self, quantity, current_price, target_price, stop_loss_price):
        self.price = current_price
        self.target_price = target_price
        self.stop_loss_price = stop_loss_price
        self.status = 'open'
        self.quantity = quantity
        
    
    def long(self, quantity, current_price, target_price, stop_loss_price):
        if self.status == 'open' and self.side == 'long':
            print('Trade is already open')
            return
        if self.status == 'open' and self.side == 'short':
            # Close the short position
            self.close()
        self.side = 'long'
        self.open(quantity, current_price, target_price, stop_loss_price)
    
    def short(self, quantity, current_price, target_price, stop_loss_price):
        if self.status == 'open' and self.side == 'short':
            print('Trade is already open')
            return
        if self.status == 'open' and self.side == 'long':
            # Close the long position
            self.close()
        self.side = 'short'
        self.open(quantity, current_price, target_price, stop_loss_price)
        self.log()
    
    def check_long(self):
        if self.current_price <= self.stop_loss_price:
            self.close()
        elif self.current_price >= self.target_price:
            self.close()
        
    def check_short(self):
        if self.current_price >= self.stop_loss_price:
            self.close()
        elif self.current_price <= self.target_price:
            self.close()
    
    def update(self, price):
        self.current_price = price
        if self.status == 'open' and self.side == 'long':
            self.check_long()
        elif self.status == 'open' and self.side == 'short':
            self.check_short()


# Test the Trade class
# trade = Trade(1, 'BTCUSDT', 10000, 1)
# trade.log()
# trade.long(1, 11000, 9000)
# trade.log()
# trade.update(8000)
# trade.log()
# trade.long(1, 10000, 7000)
# trade.log()
# trade.update(11000)
# trade.log()

