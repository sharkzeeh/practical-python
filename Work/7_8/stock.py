# stock.py
#
# Exercise 7.8: Simplifying Function Calls

from typedproperty import typedproperty, String, Integer, Float

class Stock:

    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        if shares > self.shares:
            raise RuntimeError("You can't sell more than you have")
        self.shares -= shares

    def __repr__(self):
        return f"Stock({self.name}, {self.shares:d}, {self.price:.1f})"


if __name__ == '__main__':
    s = Stock('IBM', 50, 90.1)
    print(s.name)
    try:
        s.price = [100]
    except TypeError as e:
        print('TypeError Reason:', e)
