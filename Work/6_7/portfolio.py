# portfolio.py

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
    print('Size of holdings:', len(portfolio))
    print('First holding:', portfolio[0])
    print('IBM present in portfolio:', 'IBM' in portfolio)
