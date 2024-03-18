# portfolio.py
#
# Exercise 7.5: Sorting on a field
# Exercise 7.6: Sorting on a field with lambda

class Portfolio:

    def __init__(self, holdings):
        self._holdings = holdings

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
