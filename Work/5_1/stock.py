# stock.py
#
# Exercise 5.1 - 5.4

class Stock:

    foo = 42
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
    ibm  = Stock('IBM', 50, 91.23)
    # 5.1
    print('GOOG __dict__:', goog.__dict__)

    # 5.2
    goog.date = goog.date = '6/11/2007'
    assert 'date' in goog.__dict__

    # 5.3
    assert 'foo' not in goog.__dict__
    assert hasattr(goog, 'foo')
    assert 'foo' in Stock.__dict__

    print('GOOG __dict__ has key "cost":', 'cost' in goog.__dict__)
    print()
    print('Stock __dict__ has key "cost:', 'cost' in Stock.__dict__)  # goog.__class__.__dict__
    print(Stock.__dict__['cost'])
    print('### Stock cost function help ###')
    print(help(Stock.__dict__['cost']))
    print('###')
    cost = Stock.__dict__['cost'](goog)
    print('GOOG cost:', cost)

    # 5.4: Bound methods
    s = goog.sell
    print(s) # <bound method Stock.sell of Stock(GOOG, 100, 490.1)>
    print(s.__func__) # <function Stock.sell at 0x000001917D4DF370>
    assert Stock.__dict__['sell'] == s.__func__
    print()

    print('self:', s.__self__)
    s.__func__(s.__self__, shares=10)  # same as s(1)
    print(goog.shares)                 # 90