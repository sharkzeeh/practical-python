# stock.py
#
# Exercise 5.5 - 5.8

class Stock:

    __slots__ = ('name', '_shares', 'price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares # Triggers @shares.setter (L22)
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price
    
    @property
    def shares(self):
        return self._shares
    
    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value  # this is just a naming convention (not forced)

    def sell(self, shares):
        if shares > self.shares:
            raise RuntimeError("You can't sell more than you have")
        self.shares -= shares

    def __repr__(self):
        return f"Stock({self.name}, {self.shares:d}, {self.price:.1f})"


if __name__ == '__main__':
    goog = Stock('GOOG', 100, 490.1)
    # 5.6
    cost = goog.cost
    print(f'Total cost: {cost:.2f}')

    goog.shares = 50   # Triggers @shares.setter (L22)
    print(goog.shares) # Triggers @property      (L18)

    # 5.8
    try:
        goog.prices = 42
    except AttributeError as e:
        print(e)

    # ERROR! AttributeError: 'Stock' object has no attribute '__dict__'
    # print(goog.__dict__)
