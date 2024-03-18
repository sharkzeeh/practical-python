# stock.py
# 
# Exercise 7.2: Passing tuple and dicts as arguments

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
    # 7.2
    data = ('GOOG', 100, 490.1)
    s = Stock(*data)
    print(s)

    data = { 'name': 'GOOG', 'shares': 100, 'price': 490.1 }
    s = Stock(**data)
    print(s)
