# stock.py
#
# Exercise 4.9: Better output for printing objects

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

    def __repr__(self):
        return f"Stock({self.name}, {self.shares:d}, {self.price:.1f})"


if __name__ == '__main__':
    goog = Stock('GOOG', 100, 490.1)
    print(repr(goog))
