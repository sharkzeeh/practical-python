# report.py
#
# Exercise 2.18: Tabulating with Counters
import csv, pprint

printer = pprint.PrettyPrinter()


def read_portfolio(filename):
    portfolio = []
    with open(filename) as fh:
        csv_rows = csv.reader(fh)
        headers = next(csv_rows)
        for row in csv_rows:
            holding = dict(zip(headers, row))
            holding['shares'] = int(holding['shares'])
            holding['price'] = float(holding['price'])
            portfolio.append(holding)
    return portfolio


if __name__ == '__main__':
    fn_portfolio = '../Data/portfolio.csv'
    portfolio = read_portfolio(fn_portfolio)

    from collections import Counter
    holdings = Counter()
    for s in portfolio:
        holdings[s['name']] += s['shares']
    printer.pprint(holdings)