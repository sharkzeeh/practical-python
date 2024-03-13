# stock.py
#
# Exercise 4.4: Using your class

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


if __name__ == '__main__':
    import fileparse, report
    with open('../Data/portfolio.csv') as fh:
        portdicts = fileparse.parse_csv(
            fh, select=['name', 'shares', 'price'], types=[str, int, float]
            )

    portfolio = [
        Stock(holding['name'], holding['shares'], holding['price'])
        for holding in portdicts
        ]

    print(f'Total cost: {sum([s.cost() for s in portfolio])}')

    report.portfolio_report('../Data/portfolio.csv', '../Data/prices.csv')
