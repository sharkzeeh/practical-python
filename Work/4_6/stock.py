# stock.py

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        if shares > self.shares:
            raise RuntimeError("You can't sell more than you have")
        self.shares -= shares

class MyStock(Stock):
    def panic(self):
        self.sell(self.shares)


if __name__ == '__main__':
    s = MyStock('GOOG', 100, 490.1)
    print(f'Number of shares: {s.shares:d}')
    s.panic()
    print(f'Number of shares after panic: {s.shares:d}')
    print(f'Total cost: {s.cost():.2f}')
