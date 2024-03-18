# portfolio.py
#
# Exercise 7.11: Class Methods in Practice

import stock
import fileparse

class Portfolio:

    def __init__(self):
        self._holdings = []

    def append(self, holding):
        if not isinstance(holding, stock.Stock):
            raise TypeError('Expected a Stock instance')
        self._holdings.append(holding)

    @classmethod
    def from_csv(cls, lines, **opts):
        self = cls()
        portdicts = fileparse.parse_csv(lines,
                                        select=['name','shares','price'],
                                        types=[str,int,float],
                                        **opts)
        for d in portdicts:
            self.append(stock.Stock(**d))

        return self

    def __iter__(self):
        return self._holdings.__iter__()
    
    def __len__(self):
        return len(self._holdings)
    
    def __getitem__(self, index):
        return self._holdings[index]
    
    def __contains__(self, name):
        return any([s.name == name for s in self._holdings])

    @property
    def total_cost(self):
        return sum([s.cost for s in self._holdings])

    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares


if __name__ == '__main__':
    import report
    portfolio = report.read_portfolio('../Data/portfolio.csv')
    portfolio, portfolio2 = list(portfolio), list(portfolio)

    def stock_name(stock):
        return stock.name
    portfolio.sort(key=stock_name)

    portfolio2.sort(key=lambda stock: stock.name)
    print(portfolio)
    print(portfolio2)
